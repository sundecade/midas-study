"""
正确参考代码：20+30+20m 连续梁模型
===================================
C50混凝土 + 1.5m箱型截面 + 2m单元划分 + 连续梁支座

这是 AI 助手应该生成的正确代码基准。
用于与 LLM 实际输出进行逐项对比验证。
"""
import json

# ═══════════════════════════════════════════════════════════════
# Step 0: 新建项目
# ═══════════════════════════════════════════════════════════════
STEP0_NEW_PROJECT = {
    "step": 0,
    "name": "新建项目",
    "method": "POST",
    "endpoint": "/doc/NEW",
    "body": {"Argument": {}},
    "code": '''
# --- 新建项目 ---
result = MidasAPI("POST", "/doc/NEW", {"Argument": {}})
print("新建项目:", result)
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 1: 设置单位系统 (N, m, C)
# ═══════════════════════════════════════════════════════════════
STEP1_UNIT = {
    "step": 1,
    "name": "单位系统",
    "method": "PUT",
    "endpoint": "/db/UNIT",
    "body": {
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
    "code": '''
# --- 设置单位系统 ---
# 注意：/db/UNIT 只支持 GET 和 PUT，没有 POST！
unit_data = {
    "Assign": {
        "1": {
            "ID": 1,
            "FORCE": "N",      # 力：牛顿
            "DIST": "m",       # 长度：米
            "HEAT": "C",       # 温度：摄氏度
            "TEMPER": "C"      # 温差：摄氏度
        }
    }
}
result = MidasAPI("PUT", "/db/UNIT", unit_data)
print("单位系统:", result)
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 2: 定义 C50 混凝土材料
# ═══════════════════════════════════════════════════════════════
STEP2_MATERIAL = {
    "step": 2,
    "name": "C50混凝土材料",
    "method": "POST",
    "endpoint": "/db/MATL",
    # 关键检查点：
    # - PARAM 是数组 [{...}]，不是对象 {...}
    # - 没有 PRI 字段
    # - CODE 为空字符串 ""
    # - P_TYPE=1 表示标准规范
    # - bELAST=False, ELAST=0
    "body": {
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
                "PARAM": [
                    {
                        "P_TYPE": 1,
                        "STANDARD": "JTG3362-18(RC)",
                        "CODE": "",
                        "DB": "C50",
                        "bELAST": False,
                        "ELAST": 0
                    }
                ]
            }
        }
    },
    "code": '''
# --- 定义 C50 混凝土材料 ---
matl_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC",                    # 混凝土
            "NAME": "C50",                     # 材料名称
            "HE_SPEC": 0,                      # 热膨胀系数(0=使用规范默认)
            "HE_COND": 0,                      # 热传导率(0=使用规范默认)
            "PLMT": 0,                         # 塑性材料类型(0=自动)
            "P_NAME": "",                      # 塑性材料名称(空=默认)
            "bMASS_DENS": False,               # 是否自定义密度
            "DAMP_RAT": 0,                     # 阻尼比
            "PARAM": [{                        # 材料参数(数组!)
                "P_TYPE": 1,                   # 1=标准规范
                "STANDARD": "JTG3362-18(RC)",  # 规范名称
                "CODE": "",                    # 规范代码(空)
                "DB": "C50",                   # 材料等级
                "bELAST": False,               # 0=非线性, 1=弹性
                "ELAST": 0                     # 弹性模量(0=使用规范默认)
            }]
        }
    }
}
result = MidasAPI("POST", "/db/MATL", matl_data)
print("C50材料:", result)
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 3: 箱型截面 1.5m 高
# ═══════════════════════════════════════════════════════════════
STEP3_SECTION = {
    "step": 3,
    "name": "箱型截面1.5m高",
    "method": "POST",
    "endpoint": "/db/SECT",
    # SHAPE="B" = Box section
    # vSIZE: [H, B, tw, tf1, tf2] — 高度, 宽度, 腹板厚, 顶板厚, 底板厚
    "body": {
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
                    "SECT_I": {
                        "vSIZE": [1.5, 1.0, 0.2, 0.2, 0.2, 0.2]
                    }
                }
            }
        }
    },
    "code": '''
# --- 箱型截面 1.5m 高 ---
sect_data = {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER",              # 数据库/用户定义截面
            "SECT_NAME": "Box_1.5m",           # 截面名称
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",             # 截面偏移基准点(Center-Center)
                "HORZ_OFFSET_OPT": 0,          # 水平偏移选项(0=到边缘)
                "VERT_OFFSET_OPT": 0,          # 垂直偏移选项(0=到边缘)
                "USE_SHEAR_DEFORM": False,     # 不考虑剪切变形
                "USE_WARPING_EFFECT": False,   # 不考虑翘曲效应
                "SHAPE": "B",                  # B=箱型截面(Box)
                "DATATYPE": 2,                 # 数据类型
                "SECT_I": {
                    "vSIZE": [                 # 截面尺寸
                        1.5,                   # H = 高度 1.5m
                        1.0,                   # B = 宽度 1.0m
                        0.2,                   # tw = 腹板厚 0.2m
                        0.2,                   # tf1 = 顶板厚 0.2m
                        0.2,                   # tf2 = 底板厚 0.2m
                        0.2                    # 倒角(默认)
                    ]
                }
            }
        }
    }
}
result = MidasAPI("POST", "/db/SECT", sect_data)
print("箱型截面:", result)
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 4: 创建节点 (70m 总长, 2m 间距)
# ═══════════════════════════════════════════════════════════════
# 20+30+20=70m, 2m间距 → 35段, 36个节点
nodes_dict = {}
for i in range(36):
    nodes_dict[str(i + 1)] = {
        "X": i * 2.0,
        "Y": 0,
        "Z": 0
    }

STEP4_NODES = {
    "step": 4,
    "name": "节点创建(2m间距, 36个节点)",
    "method": "POST",
    "endpoint": "/db/NODE",
    "body": {"Assign": nodes_dict},
    "code": f'''
# --- 创建节点 ---
# 20+30+20=70m总长, 2m间距, 共35段36个节点
nodes = {{}}
for i in range(36):
    node_id = i + 1
    x = i * 2.0  # 2m间距
    nodes[str(node_id)] = {{"X": x, "Y": 0, "Z": 0}}

node_data = {{"Assign": nodes}}
result = MidasAPI("POST", "/db/NODE", node_data)
print(f"创建了{{len(nodes)}}个节点")
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 5: 创建梁单元 (35个单元)
# ═══════════════════════════════════════════════════════════════
elems_dict = {}
for i in range(35):
    elems_dict[str(i + 1)] = {
        "TYPE": "BEAM",
        "MATL": 1,     # 材料ID (第1个定义的材料=C50)
        "SECT": 1,     # 截面ID (第1个定义的截面=Box_1.5m)
        "NODE": [i + 1, i + 2],
        "ANGLE": 0
    }

STEP5_ELEMENTS = {
    "step": 5,
    "name": "梁单元创建(35个单元)",
    "method": "POST",
    "endpoint": "/db/ELEM",
    "body": {"Assign": elems_dict},
    "code": f'''
# --- 创建梁单元 ---
# 35个单元连接36个节点
elems = {{}}
for i in range(35):
    elem_id = i + 1
    elems[str(elem_id)] = {{
        "TYPE": "BEAM",    # 梁单元
        "MATL": 1,         # 材料ID=C50
        "SECT": 1,         # 截面ID=Box_1.5m
        "NODE": [i + 1, i + 2],  # 连接相邻节点
        "ANGLE": 0         # 单元角度
    }}

elem_data = {{"Assign": elems}}
result = MidasAPI("POST", "/db/ELEM", elem_data)
print(f"创建了{{len(elems)}}个梁单元")
'''
}

# ═══════════════════════════════════════════════════════════════
# Step 6: 边界条件 (连续梁支座)
# ═══════════════════════════════════════════════════════════════
# 连续梁支座布置 (20+30+20):
# - 节点1 (x=0m): 固定铰支座 1111110 (全约束)
# - 节点11 (x=20m): 活动铰支座 0110000 (仅DY,DZ)
# - 节点26 (x=50m): 活动铰支座 0110000 (仅DY,DZ)
# - 节点36 (x=70m): 活动铰支座 0110000 (仅DY,DZ)
#
# 关键：每个支座必须在独立的数字键下，不能堆在同一个 ITEMS 数组里！
STEP6_BOUNDARY = {
    "step": 6,
    "name": "边界条件(连续梁支座)",
    "method": "POST",
    "endpoint": "/db/CONS",
    "body": {
        "Assign": {
            "1": {
                "ITEMS": [{"ID": 1, "GROUP_NAME": "", "CONSTRAINT": "1111110"}]
            },
            "11": {
                "ITEMS": [{"ID": 11, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
            },
            "26": {
                "ITEMS": [{"ID": 26, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
            },
            "36": {
                "ITEMS": [{"ID": 36, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
            }
        }
    },
    "code": '''
# --- 施加边界条件 ---
# 连续梁支座: 起点全约束, 中间支点仅约束DY/DZ
# 关键：每个支座必须在独立的数字键下！
cons_data = {
    "Assign": {
        "1": {                                  # 节点1 (x=0m, 起点)
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "",               # 组名(空)
                "CONSTRAINT": "1111110"         # 全约束
            }]
        },
        "11": {                                 # 节点11 (x=20m, 中支点1)
            "ITEMS": [{
                "ID": 11,
                "GROUP_NAME": "",
                "CONSTRAINT": "0110000"         # 仅DY, DZ
            }]
        },
        "26": {                                 # 节点26 (x=50m, 中支点2)
            "ITEMS": [{
                "ID": 26,
                "GROUP_NAME": "",
                "CONSTRAINT": "0110000"         # 仅DY, DZ
            }]
        },
        "36": {                                 # 节点36 (x=70m, 终点)
            "ITEMS": [{
                "ID": 36,
                "GROUP_NAME": "",
                "CONSTRAINT": "0110000"         # 仅DY, DZ
            }]
        }
    }
}
result = MidasAPI("POST", "/db/CONS", cons_data)
print("边界条件:", result)
'''
}

# ═══════════════════════════════════════════════════════════════
# 完整示例代码 (可直接复制到 MIDAS)
# ═══════════════════════════════════════════════════════════════
FULL_CODE = """import requests
import urllib3
import winreg

urllib3.disable_warnings()

# --- 从注册表自动获取配置 ---
reg_path = r"SOFTWARE\\MIDAS\\CVLwNX_CH\\CONNECTION"
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
uri = winreg.QueryValueEx(key, "URI")[0]
port = winreg.QueryValueEx(key, "PORT")[0]
mapi_key = winreg.QueryValueEx(key, "Key")[0]
base_url = f"https://{uri}:{port}/civil"

def MidasAPI(method, command, body=None):
    url = base_url + command
    headers = {"Content-Type": "application/json", "MAPI-Key": mapi_key}
    if method == "POST":
        response = requests.post(url, headers=headers, json=body, verify=False)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=body, verify=False)
    elif method == "GET":
        response = requests.get(url, headers=headers, verify=False)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers, verify=False)
    return response.json()

# Step 0: 新建项目
print("Step 0: 新建项目...")
result = MidasAPI("POST", "/doc/NEW", {"Argument": {}})

# Step 1: 设置单位系统 (N, m, C)
print("Step 1: 设置单位系统...")
unit_data = {
    "Assign": {
        "1": {
            "ID": 1,
            "FORCE": "N",      # 力: 牛顿
            "DIST": "m",       # 长度: 米
            "HEAT": "C",       # 温度: 摄氏度
            "TEMPER": "C"      # 温差: 摄氏度
        }
    }
}
result = MidasAPI("PUT", "/db/UNIT", unit_data)

# Step 2: 定义 C50 混凝土材料
print("Step 2: 定义C50材料...")
matl_data = {
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
}
result = MidasAPI("POST", "/db/MATL", matl_data)

# Step 3: 箱型截面 1.5m 高
print("Step 3: 定义箱型截面...")
sect_data = {
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
                "SECT_I": {
                    "vSIZE": [1.5, 1.0, 0.2, 0.2, 0.2, 0.2]
                }
            }
        }
    }
}
result = MidasAPI("POST", "/db/SECT", sect_data)

# Step 4: 创建节点 (70m 总长, 2m 间距 → 36个节点)
print("Step 4: 创建36个节点...")
nodes = {}
for i in range(36):
    node_id = i + 1
    x = i * 2.0
    nodes[str(node_id)] = {"X": x, "Y": 0, "Z": 0}
result = MidasAPI("POST", "/db/NODE", {"Assign": nodes})

# Step 5: 创建梁单元 (35个单元)
print("Step 5: 创建35个梁单元...")
elems = {}
for i in range(35):
    elem_id = i + 1
    elems[str(elem_id)] = {
        "TYPE": "BEAM",
        "MATL": 1,
        "SECT": 1,
        "NODE": [i + 1, i + 2],
        "ANGLE": 0
    }
result = MidasAPI("POST", "/db/ELEM", {"Assign": elems})

# Step 6: 施加边界条件
print("Step 6: 施加边界条件...")
cons_data = {
    "Assign": {
        "1": {
            "ITEMS": [{"ID": 1, "GROUP_NAME": "", "CONSTRAINT": "1111110"}]
        },
        "11": {
            "ITEMS": [{"ID": 11, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
        },
        "26": {
            "ITEMS": [{"ID": 26, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
        },
        "36": {
            "ITEMS": [{"ID": 36, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]
        }
    }
}
result = MidasAPI("POST", "/db/CONS", cons_data)

print("\\n模型创建完成!")
print("- 材料: C50 混凝土 (JTG3362-18(RC))")
print("- 截面: 箱型截面 Box_1.5m (1.5m高×1.0m宽)")
print("- 节点: 36个 (0~70m, 2m间距)")
print("- 单元: 35个 梁单元")
print("- 边界: 连续梁支座 (全约束+3个活动铰)")
"""

# ═══════════════════════════════════════════════════════════════
# 验证函数
# ═══════════════════════════════════════════════════════════════

ALL_STEPS = [
    STEP0_NEW_PROJECT, STEP1_UNIT, STEP2_MATERIAL,
    STEP3_SECTION, STEP4_NODES, STEP5_ELEMENTS, STEP6_BOUNDARY
]


def validate_json(step, generated_body):
    """验证生成的 JSON 是否符合模板结构。返回 (ok, issues_list)."""
    issues = []
    expected = step["body"]
    ep = step["endpoint"]

    # 检查顶层包装
    if "Assign" in expected:
        if "Assign" not in generated_body:
            issues.append(f"缺少 Assign 包装层")
            return False, issues
        gen_av = generated_body["Assign"]
        exp_av = expected["Assign"]

        if not isinstance(gen_av, dict):
            issues.append("Assign 值应为 dict")
            return False, issues

        # 检查每个键是否为数字
        for k in gen_av:
            if not isinstance(k, str) or not k.isdigit():
                issues.append(f"Assign 键应为数字字符串，得到: '{k}'")

        # 检查第一个键的数据结构
        gen_first_key = list(gen_av.keys())[0]
        gen_inner = gen_av[gen_first_key]
        exp_first_key = list(exp_av.keys())[0]
        exp_inner = exp_av[exp_first_key]

        # 检查 PARAM 是否为数组 (MATL)
        if ep == "/db/MATL" and "PARAM" in gen_inner:
            if isinstance(gen_inner["PARAM"], dict):
                issues.append("PARAM 应为数组 [{...}]，不是对象 {...}")
            elif isinstance(gen_inner["PARAM"], list) and len(gen_inner["PARAM"]) > 0:
                if "PRI" in gen_inner["PARAM"][0]:
                    issues.append("PARAM 中不应有 PRI 字段")

        # 检查 ITEMS 结构 (CONS)
        if ep == "/db/CONS":
            if "ITEMS" in gen_inner:
                items = gen_inner["ITEMS"]
                if isinstance(items, list) and len(items) > 1:
                    # 检查是否多个节点堆在一个 ITEMS 数组里
                    ids = [item.get("ID") for item in items if isinstance(item, dict)]
                    if len(ids) > 1:
                        issues.append(
                            f"多个节点({ids})放在了同一个键的 ITEMS 数组里，"
                            "应该每个节点用独立的数字键"
                        )

        # 检查顶层字段名
        for key in exp_inner:
            if key not in gen_inner:
                issues.append(f"缺少字段: '{key}'")

    elif "Argument" in expected:
        if "Argument" not in generated_body:
            issues.append(f"缺少 Argument 包装层")
            return False, issues
    else:
        issues.append(f"未知包装类型: {list(expected.keys())}")

    return len(issues) == 0, issues


def test_step(step):
    """测试单个步骤。"""
    print(f"\n{'─' * 50}")
    print(f"Step {step['step']}: {step['name']}")
    print(f"{step['method']} {step['endpoint']}")
    print(f"Expected body:")
    print(json.dumps(step["body"], indent=2, ensure_ascii=False))
    ok, issues = validate_json(step, step["body"])
    if ok:
        print("✅ 自检通过")
    else:
        print(f"❌ 问题:")
        for i in issues:
            print(f"  - {i}")
    return ok


def run_all_tests():
    """运行所有步骤的自检。"""
    print("=" * 60)
    print("端到端验证：所有步骤的 JSON 结构")
    print("=" * 60)

    all_ok = True
    for step in ALL_STEPS:
        if not test_step(step):
            all_ok = False

    if all_ok:
        print(f"\n{'=' * 60}")
        print("✅ 所有步骤验证通过！")
        print("=" * 60)
        print("\n完整代码见 FULL_CODE 变量，可直接复制到 MIDAS 运行。")
    else:
        print(f"\n❌ 部分步骤有错误")

    return all_ok


if __name__ == "__main__":
    run_all_tests()
