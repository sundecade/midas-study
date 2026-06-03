"""
端到端测试：模拟 RAG 检索 + 验证 JSON 生成
用法：PYTHONUTF8=1 python test_model_gen.py
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KB_PATH = os.path.join(SCRIPT_DIR, "..", "midas_api_knowledge_base.json")

with open(KB_PATH, "r", encoding="utf-8") as f:
    kb = json.load(f)


def find_ep(ep_path):
    """Find an endpoint by path."""
    for sec_name, sec_data in kb["api_data"].items():
        for p, d in sec_data.get("endpoints", {}).items():
            if p == ep_path:
                return d, sec_name
        for sub_name, sub_data in sec_data.get("subsections", {}).items():
            for p, d in sub_data.items():
                if p == ep_path:
                    return d, sec_name
    return None, None


def check_template(ep_path, method="POST"):
    """Verify a template for a specific endpoint and method."""
    ep, section = find_ep(ep_path)
    if not ep:
        return {"error": f"Endpoint {ep_path} not found"}

    t = ep.get("request_templates", {})
    methods = ep.get("http_method", [])

    result = {
        "endpoint": ep_path,
        "name": ep.get("api_name", "?"),
        "section": section,
        "methods": methods,
        "wrapper": t.get("_wrapper_type", "?"),
        "wrapper_info": t.get("_wrapper_info", "")[:200],
        "template": t.get(method),
        "field_guide": ep.get("request_field_guide", {}),
    }

    # Validate template structure
    issues = []
    tmpl = t.get(method)
    if tmpl is None:
        if method in methods:
            issues.append(f"Method {method} listed but no template")
    elif isinstance(tmpl, dict):
        # Check Assign wrapper has numeric keys
        if "Assign" in tmpl:
            av = tmpl["Assign"]
            if isinstance(av, dict):
                for k in av:
                    stripped = k.strip("<>")
                    if stripped.isdigit():
                        if int(stripped) > 100:
                            issues.append(f"Key '{k}' looks like example ID, not generic placeholder")
                    elif stripped != "ID" and not stripped.startswith("<"):
                        issues.append(f"Non-generic key in Assign: '{k}'")
            else:
                issues.append("Assign value is not dict")
        elif "Argument" in tmpl:
            pass  # OK
        else:
            issues.append(f"No Assign or Argument wrapper: keys={list(tmpl.keys())}")
    else:
        issues.append(f"Template is not dict: {type(tmpl)}")

    result["issues"] = issues
    return result


# ── 建模步骤定义 ──
# 模型：20+30+20m 连续梁，C50混凝土，箱型截面 1.5m高，2m单元划分

STEPS = [
    {
        "step": 0, "name": "新建项目", "ep": "/doc/NEW", "method": "POST",
        "expected": {"Argument": {}},
        "note": "Argument 可为空对象 {}"
    },
    {
        "step": 1, "name": "单位系统", "ep": "/db/UNIT", "method": "PUT",
        "expected": {
            "Assign": {
                "1": {
                    "ID": 1,
                    "FORCE": "N",
                    "DIST": "m",
                    "HEAT": "C",
                    "TEMPER": "C"
                }
            }
        },
        "note": "UNIT 仅支持 GET/PUT，不支持 POST"
    },
    {
        "step": 2, "name": "C50材料", "ep": "/db/MATL", "method": "POST",
        "expected": {
            "Assign": {
                "1": {
                    "TYPE": "CONC",
                    "NAME": "C50",
                    "HE_SPEC": 0,
                    "HE_COND": 0,
                    "PLMT": 0,
                    "P_NAME": "",
                    "bMASS_DENS": False,
                    "DAMP_RAT": 0,
                    "PARAM": [{
                        "P_TYPE": 1,
                        "STANDARD": "JTG3362-18(RC)",
                        "CODE": "",
                        "DB": "C50",
                        "bELAST": False,
                        "ELAST": 0
                    }]
                }
            }
        },
        "note": "PARAM 是数组！P_TYPE=1 标准规范，CODE 为空字符串"
    },
    {
        "step": 3, "name": "箱型截面1.5m", "ep": "/db/SECT", "method": "POST",
        "expected": {
            "Assign": {
                "1": {
                    "SECTTYPE": "DBUSER",
                    "SECT_NAME": "Box_1.5m",
                    "SECT_BEFORE": {
                        "OFFSET_PT": "CC",
                        "HORZ_OFFSET_OPT": 0,
                        "VERT_OFFSET_OPT": 0,
                        "USE_SHEAR_DEFORM": False,
                        "USE_WARPING_EFFECT": False,
                        "SHAPE": "B",
                        "DATATYPE": 2,
                        "SECT_I": {"vSIZE": [1.5, 1.0, 0.2, 0.2, 0.2, 0.2]}
                    }
                }
            }
        },
        "note": "SHAPE='B' 箱型，vSIZE=[H,B,tw,tf1,tf2,tf3]"
    },
    {
        "step": 4, "name": "节点创建(2m间距)", "ep": "/db/NODE", "method": "POST",
        "expected": {
            "Assign": {
                "1": {"X": 0, "Y": 0, "Z": 0},
                "2": {"X": 2, "Y": 0, "Z": 0},
                "3": {"X": 4, "Y": 0, "Z": 0},
                # ... 35 nodes for 70m span at 2m spacing
                "35": {"X": 70, "Y": 0, "Z": 0},
            }
        },
        "note": "70m/2m=35段→36个节点(含起点)，实际按20+30+20=70m"
    },
    {
        "step": 5, "name": "单元创建", "ep": "/db/ELEM", "method": "POST",
        "expected": {
            "Assign": {
                "1": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0},
                "2": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [2, 3], "ANGLE": 0},
                # ... 35 elements
            }
        },
        "note": "TYPE=BEAM, MATL=材料ID, SECT=截面ID, NODE=[i,i+1]"
    },
    {
        "step": 6, "name": "边界条件", "ep": "/db/CONS", "method": "POST",
        "expected": {
            "Assign": {
                "1": {"ITEMS": [{"ID": 1, "GROUP_NAME": "", "CONSTRAINT": "1111110"}]},
                "11": {"ITEMS": [{"ID": 11, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
                "26": {"ITEMS": [{"ID": 26, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
                "36": {"ITEMS": [{"ID": 36, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
            }
        },
        "note": "节点1(起点):1111110全固支, 节点11(20m):0110000仅DY,DZ, 节点26(50m):0110000, 节点36(70m终点):0110000"
    },
]


def main():
    print("=" * 70)
    print("端到端测试：20+30+20m 连续梁 — C50 + 箱型截面 1.5m + 2m单元")
    print("=" * 70)

    all_ok = True
    for s in STEPS:
        print(f"\n{'─' * 60}")
        print(f"Step {s['step']}: {s['name']}")
        print(f"Endpoint: {s['ep']} [{s['method']}]")
        print(f"{'─' * 60}")

        result = check_template(s["ep"], s["method"])
        if result.get("error"):
            print(f"  ❌ {result['error']}")
            all_ok = False
            continue

        print(f"  Section: {result['section']}")
        print(f"  Methods: {result['methods']}")
        print(f"  Wrapper: {result['wrapper']}")

        tmpl = result["template"]
        if tmpl:
            print(f"  Template ({s['method']}):")
            print(f"  {json.dumps(tmpl, indent=2, ensure_ascii=False)}")
        else:
            print(f"  ⚠ No {s['method']} template!")

        if result["issues"]:
            print(f"  ⚠ Issues:")
            for i in result["issues"]:
                print(f"    - {i}")
            all_ok = False
        else:
            print(f"  ✅ Template structure OK")

        # Show field guide summary
        guide = result["field_guide"]
        if guide:
            required = [k for k, v in guide.items() if v.get("required")]
            optional = [k for k, v in guide.items() if not v.get("required")]
            print(f"  Fields: {len(required)} required, {len(optional)} optional")
            if required:
                print(f"    Required: {', '.join(required)}")
            if optional:
                optional_with_default = [k for k, v in guide.items() if not v.get("required") and v.get("default") is not None]
                if optional_with_default:
                    print(f"    Optional w/ default: {', '.join(optional_with_default)}")

        # Print expected JSON for this step
        expected = s.get("expected", {})
        if expected:
            print(f"\n  📋 Expected JSON:")
            print(f"  {json.dumps(expected, indent=4, ensure_ascii=False)}")
        if s.get("note"):
            print(f"  💡 {s['note']}")

    print(f"\n{'=' * 70}")
    if all_ok:
        print("✅ All templates verified!")
    else:
        print("❌ Some templates have issues — check above")
    print("=" * 70)


if __name__ == "__main__":
    main()
