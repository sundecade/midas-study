"""
端到端集成测试：模拟 RAG → LLM 的完整链路
验证每个建模步骤的上下文是否清晰、模板是否正确

用法：PYTHONUTF8=1 python test_integration.py
"""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from retriever import APIRetriever

KB = os.path.join(SCRIPT_DIR, "..", "midas_api_knowledge_base.json")
r = APIRetriever(KB)


def get_context_for(ep_path):
    """Get the formatted context for a specific endpoint."""
    for ep in r.endpoints:
        if ep["path"] == ep_path:
            return ep, r.format_endpoint_detail(ep)
    return None, None


# ── 测试查询 ──
USER_QUERY = "建立一个20+30+20m的连续梁模型，材料选用C50，截面选择1.5m高的箱型截面，单元划分为2m一个"

print("=" * 70)
print("端到端集成测试")
print(f"查询: {USER_QUERY}")
print("=" * 70)

# ── 第一步：搜索 ──
print("\n## 第一步：RAG 检索结果")
results = r.search(USER_QUERY, top_k=10)
for ep, score in results:
    d = ep["data"]
    methods = d.get("http_method", [])
    if isinstance(methods, str):
        methods = [methods]
    print(f"  {ep['path']:<25} score={score:.0f} [{', '.join(methods)}] {d.get('api_name', '?')[:50]}")

# ── 第二步：验证每个必需端点的上下文 ──
print("\n" + "=" * 70)
print("## 第二步：逐端点验证上下文质量")
print("=" * 70)

REQUIRED = [
    "/doc/NEW", "/db/UNIT", "/db/MATL", "/db/SECT",
    "/db/NODE", "/db/ELEM", "/db/CONS"
]

VALIDATIONS = {
    "/doc/NEW": {
        "must_have": ["Argument", "POST"],
        "must_not_have": ["Assign"],
    },
    "/db/UNIT": {
        "must_have": ["PUT", "FORCE", "HEAT", "TEMPER", "DIST", "Assign"],
        "must_not_have": ["POST", "ANGLE", "LENGTH"],
    },
    "/db/MATL": {
        "must_have": ["POST", "PARAM", "P_TYPE", "STANDARD", "DB", "CODE"],
        "must_not_have": ["PRI"],
    },
    "/db/SECT": {
        "must_have": ["POST", "SECTTYPE", "SHAPE", "SECT_BEFORE", "SECT_I", "vSIZE"],
        "must_not_have": [],
    },
    "/db/NODE": {
        "must_have": ["POST", "Assign", "X", "Y", "Z"],
        "must_not_have": [],
    },
    "/db/ELEM": {
        "must_have": ["POST", "TYPE", "MATL", "SECT", "NODE", "ANGLE"],
        "must_not_have": [],
    },
    "/db/CONS": {
        "must_have": ["POST", "ITEMS", "CONSTRAINT", "GROUP_NAME"],
        "must_not_have": [],
    },
}

all_good = True
for ep_path in REQUIRED:
    ep_obj, context = get_context_for(ep_path)
    if ep_obj is None:
        print(f"\n❌ {ep_path}: NOT FOUND in retriever!")
        all_good = False
        continue

    d = ep_obj["data"]
    methods = d.get("http_method", [])
    if isinstance(methods, str):
        methods = [methods]

    print(f"\n{'─' * 60}")
    print(f"端点: {ep_path} — {d.get('api_name', '?')}")
    print(f"方法: {', '.join(methods)}")

    validations = VALIDATIONS.get(ep_path, {})
    issues = []

    # Check must_have
    for keyword in validations.get("must_have", []):
        if keyword not in context:
            # Special case: UNIT should NOT have POST
            if keyword == "POST" and ep_path == "/db/UNIT":
                continue  # This is actually correct — UNIT is GET/PUT only
            issues.append(f"缺少关键词: '{keyword}'")
    for keyword in validations.get("must_not_have", []):
        if keyword in context:
            issues.append(f"不应出现关键词: '{keyword}'")

    # Check template structure
    t = d.get("request_templates", {})
    for method in methods:
        if method in t:
            tmpl = t[method]
        elif method == "GET":
            continue  # GET often has no template
        else:
            if method in ["POST", "PUT"]:
                issues.append(f"缺失 {method} 模板")

    # Special check: MATL PARAM should be array
    if ep_path == "/db/MATL" and "POST" in t:
        import json as _j
        post_str = _j.dumps(t["POST"])
        if '"PARAM": {}' in post_str or '"PARAM": {' in post_str:
            issues.append("PARAM 应为数组 [{...}], 不是对象 {...}")
        if '"PRI"' in post_str:
            issues.append("PARAM 中不应有 PRI 字段")

    # Special check: SECT vSIZE should be array
    if ep_path == "/db/SECT" and "POST" in t:
        import json as _j
        post_str = _j.dumps(t["POST"])
        if '"vSIZE"' not in post_str:
            issues.append("缺少 vSIZE 字段")

    # Special check: CONS multiple keys note
    if ep_path == "/db/CONS":
        note = t.get("POST_note", "")
        if "独立的数字键" not in note:
            issues.append("缺少多键说明")

    if issues:
        print(f"⚠ 发现 {len(issues)} 个问题:")
        for i in issues:
            print(f"  - {i}")
        all_good = False
    else:
        print(f"✅ 上下文完整")

    # Print context excerpt
    print(f"\n--- 上下文摘要 (前600字符) ---")
    print(context[:600])
    print("...")

print(f"\n{'=' * 70}")
if all_good:
    print("✅ 所有端点上下文验证通过！")
else:
    print("⚠ 部分端点有问题，需要修复")
print("=" * 70)
