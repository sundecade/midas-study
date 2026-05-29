"""
MIDAS API Teaching Content Generator (Part 2)
Reads midas_api_knowledge_base.json and generates beginner-friendly
teaching materials in Markdown format.

Target audience: engineers with domain knowledge, no programming experience,
first time using APIs.
"""

import json
import os
import sys
from collections import defaultdict

# Fix Windows UTF-8
sys.stdout.reconfigure(encoding="utf-8")

KB_PATH = "midas_api_knowledge_base.json"
OUT_DIR = "teaching"

# ── Helper Functions ─────────────────────────────────────────────────────────

def load_kb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def norm_type(vt):
    """Normalize value_type strings to consistent format."""
    if not vt:
        return "unknown"
    vt = vt.strip()
    # Fix common inconsistencies
    mapping = {
        "string": "String", "number": "Number", "integer": "Integer",
        "boolean": "Boolean", "object": "Object", "array": "Array",
        "Array[Integer]": "Array[Integer]", "Array [String]": "Array[String]",
        "Array(Integer)": "Array[Integer]", "Array [Integer]": "Array[Integer]",
    }
    return mapping.get(vt, vt)


def is_required(p):
    return p.get("required", False)


def is_optional(p):
    return p.get("optional", False) and not p.get("required", False)


def flat_params(endpoint):
    """Return parameters sorted: required first, then optional."""
    params = endpoint.get("parameters", [])
    req = [p for p in params if is_required(p)]
    opt = [p for p in params if is_optional(p)]
    return req, opt


def json_path_leaf(path):
    """Extract the last component of a json_path."""
    parts = path.split(".") if path else []
    return parts[-1] if parts else ""


def describe_type(vt):
    """Human-readable type description in Chinese-friendly terms."""
    vt = norm_type(vt)
    type_map = {
        "String": "文字（字符串）",
        "Number": "数字",
        "Integer": "整数",
        "Boolean": "是/否（布尔值）",
        "Object": "对象（一组键值对）",
        "Array[Integer]": "整数数组",
        "Array[String]": "字符串数组",
        "Array[Number]": "数字数组",
        "Array[Boolean]": "布尔数组",
    }
    return type_map.get(vt, vt)


def get_example(endpoint):
    """Get the first JSON example from an endpoint."""
    examples = endpoint.get("json_examples", [])
    if examples:
        return examples[0].get("content", {})
    return {}


def get_http_methods(endpoint):
    methods = endpoint.get("http_method", ["POST"])
    if isinstance(methods, str):
        methods = [methods]
    return [m.upper() for m in methods]


def build_minimal_json(endpoint):
    """Build a minimal valid JSON body showing required fields only."""
    req_params, opt_params = flat_params(endpoint)
    result = {}

    for p in req_params:
        path = p.get("json_path", p["key"])
        parts = path.split(".")
        # Build nested structure, handling potential list collisions
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                # Conflict: was set to a list/number by another param, reset to dict
                current[part] = {}
            current = current[part]
        # Set a placeholder value
        vt = norm_type(p.get("value_type", "String"))
        if "String" in vt:
            val = f"<{p['key']}>"
        elif "Integer" in vt or "Number" in vt:
            val = 0
        elif "Boolean" in vt:
            val = True
        elif "Array" in vt or "array" in vt.lower():
            val = []
        else:
            val = {}
        current[parts[-1]] = val

    return result


def build_full_json(endpoint):
    """Build a JSON body showing all parameters with placeholders."""
    params = endpoint.get("parameters", [])
    result = {}

    for p in params:
        path = p.get("json_path", p["key"])
        parts = path.split(".")
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]

        vt = norm_type(p.get("value_type", "String"))
        default = p.get("default")
        if default is not None and str(default) != "null" and str(default) != "":
            val = default
        elif "String" in vt:
            val = f"<{p['key']}>"
        elif "Integer" in vt or "Number" in vt:
            val = 0
        elif "Boolean" in vt:
            val = False
        elif "Array" in vt or "array" in vt.lower():
            val = []
        else:
            val = {}

        if is_required(p):
            current[parts[-1]] = val
        else:
            # Place optional params in a comment-like structure
            if "_optional" not in current:
                current["_optional"] = {}
            current["_optional"][parts[-1]] = val

    return result


def collect_all_endpoints(kb):
    """Collect all endpoints as a flat list with section/subsection info."""
    api_data = kb.get("api_data", {})
    endpoints = []

    def walk(data, section, subsection=""):
        if not isinstance(data, dict):
            return
        # Handle flat endpoints (DOC, OPE, VIEW style)
        for key, value in data.get("endpoints", {}).items():
            if isinstance(value, dict) and "api_name" in value:
                endpoints.append({
                    "section": section,
                    "subsection": subsection,
                    "path": key,
                    "data": value,
                })
        # Handle subsections (DB, POST style) — endpoints stored directly in subsection dict
        for key, value in data.get("subsections", {}).items():
            walk(value, section, key)
        # Handle endpoints stored directly at this level (DB/POST subsection style)
        for key, value in data.items():
            if key in ("endpoints", "subsections"):
                continue
            if isinstance(value, dict) and "api_name" in value:
                endpoints.append({
                    "section": section,
                    "subsection": subsection,
                    "path": key,
                    "data": value,
                })

    for sec_name, sec_data in api_data.items():
        walk(sec_data, sec_name)

    return endpoints


# ── Content Generators ────────────────────────────────────────────────────────

def gen_main_index(all_endpoints, sections_order):
    """Generate the main README.md with table of contents."""
    lines = []
    lines.append("# MIDAS API 教学手册")
    lines.append("")
    lines.append("> 面向工程师的 API 入门教程 —— 不需要编程基础，只需要懂工程。")
    lines.append("")
    lines.append("## 这是什么？")
    lines.append("")
    lines.append(
        "MIDAS API 是一套基于 HTTP 协议的接口，让你可以通过发送 **JSON 数据** 来操作 "
        "MIDAS 结构分析软件（Civil、Gen 等）。简单说：**你不用点鼠标，用代码发指令就能完成建模、分析、取结果。**"
    )
    lines.append("")
    lines.append("## 你可以用 API 做什么？")
    lines.append("")
    lines.append("| 功能类别 | 说明 | 对应章节 |")
    lines.append("|---------|------|---------|")
    section_names = {
        "DOC": "项目管理 — 新建、打开、保存项目",
        "DB": "模型数据库 — 建节点、单元、材料、荷载...",
        "OPE": "操作命令 — 划分单元、计算截面特性...",
        "VIEW": "视图控制 — 选择、截图、显示控制",
        "POST": "后处理 — 提取表格结果、内力、位移...",
    }
    for sec in sections_order:
        cnt = len([e for e in all_endpoints if e["section"] == sec])
        lines.append(f"| {sec} | {section_names.get(sec, sec)} | [{sec}.md]({sec}.md) ({cnt} 个接口) |")
    lines.append("")
    lines.append("## 阅读顺序建议")
    lines.append("")
    lines.append("1. **先读** [附录A：JSON 快速入门](appendix/json-basics.md) —— 5 分钟了解 JSON 是什么")
    lines.append("2. **再读** [DOC 章节](DOC.md) —— 从最简单的接口开始，感受 API 怎么用")
    lines.append("3. **然后读** [DB 章节](DB.md) —— 核心建模接口，工作中用得最多")
    lines.append("4. **按需查阅** OPE、VIEW、POST 章节")
    lines.append("")
    lines.append("## 每个接口的教程包含")
    lines.append("")
    lines.append("1. 工程含义 — 这个接口在工程上做什么")
    lines.append("2. JSON 逐层解释 — 每一层是什么意思")
    lines.append("3. 必填 vs 可选参数 — 哪些必须填，哪些可以不填")
    lines.append("4. 可选参数放在哪里 — JSON 结构中的位置")
    lines.append("5. 参数之间的关系 — 填了 A 才能填 B 的情况")
    lines.append("6. 最小可运行例子 — 最简单的调用代码")
    lines.append("7. 工程意义解释 — 为什么工程师需要这个功能")
    lines.append("8. 常见错误 — 踩过的坑告诉你")
    lines.append("9. 批量生成案例 — 一次性生成多个调用")
    lines.append("10. for 循环优化 — 用循环提高效率")
    lines.append("")
    return "\n".join(lines)


def gen_json_basics():
    """Generate a JSON basics primer for engineers."""
    lines = []
    lines.append("# 附录A：JSON 快速入门（写给工程师）")
    lines.append("")
    lines.append("## JSON 是什么？")
    lines.append("")
    lines.append(
        "JSON（JavaScript Object Notation）是一种**纯文本的数据格式**，就像 TXT 文件一样。"
        "它用花括号 `{}`、方括号 `[]`、冒号 `:` 和逗号 `,` 来组织数据。"
    )
    lines.append("")
    lines.append("### 类比：JSON 就像工程表格")
    lines.append("")
    lines.append("| 工程概念 | JSON 表示 |")
    lines.append("|---------|----------|")
    lines.append('| 一个节点的坐标 X=1, Y=2, Z=3 | `{"X": 1, "Y": 2, "Z": 3}` |')
    lines.append('| 一个列表 [67, 130, 171] | `{"NODE_LIST": [67, 130, 171]}` |')
    lines.append('| 表格中的一行 | `{"NAME": "C50", "STRENGTH": 50}` |')
    lines.append("")
    lines.append("## JSON 的基本规则")
    lines.append("")
    lines.append('### 规则 1：花括号 `{}` 包住一个「对象」')
    lines.append("")
    lines.append('```json\n{\n  "X": 1,\n  "Y": 2\n}\n```')
    lines.append("")
    lines.append("花括号里面是 **键值对**：`\"键\": 值`。键是标签，值是数据。")
    lines.append("")
    lines.append('### 规则 2：方括号 `[]` 包住一个"数组"（列表）')
    lines.append("")
    lines.append('```json\n[67, 130, 171]\n```')
    lines.append("")
    lines.append("数组就是一串数据，用逗号隔开。可以放数字、字符串、甚至对象。")
    lines.append("")
    lines.append("### 规则 3：对象可以嵌套对象")
    lines.append("")
    lines.append("```json")
    lines.append("{")
    lines.append('  "MATERIAL": {          ← 第一层：材料对象')
    lines.append('    "NAME": "C50",        ← 第二层：材料名称')
    lines.append('    "PARAM": {            ← 第二层：参数对象')
    lines.append('      "STRENGTH": 50     ← 第三层：强度值')
    lines.append("    }")
    lines.append("  }")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("**理解嵌套的关键**：每一层花括号 `{}` 就是一个新的层级。像剥洋葱一样，一层一层往里看。")
    lines.append("")
    lines.append("### 规则 4：数据类型")
    lines.append("")
    lines.append("| 类型 | 写法 | 示例 |")
    lines.append("|------|------|------|")
    lines.append("| 字符串（文字） | 用双引号包住 | `\"C50\"` |")
    lines.append("| 数字 | 直接写 | `50`, `3.14`, `-1` |")
    lines.append("| 布尔（是/否） | `true` 或 `false` | `true` |")
    lines.append("| 空值 | `null` | `null` |")
    lines.append("| 对象 | 花括号 | `{\"X\": 1}` |")
    lines.append("| 数组 | 方括号 | `[1, 2, 3]` |")
    lines.append("")
    lines.append("### 规则 5：逗号分隔，最后一项不加逗号")
    lines.append("")
    lines.append('```json\n{"A": 1, "B": 2, "C": 3}   ← 正确\n{"A": 1, "B": 2, "C": 3,}  ← 错误！C 后面多了逗号\n```')
    lines.append("")
    lines.append("## MIDAS API 的 JSON 长什么样？")
    lines.append("")
    lines.append('以"创建节点"为例，发给 MIDAS 的 JSON 长这样：')
    lines.append("")
    lines.append("```json")
    lines.append("{")
    lines.append('  "Assign": {')
    lines.append('    "1": {"X": 0, "Y": 0, "Z": 0},')
    lines.append('    "2": {"X": 5, "Y": 0, "Z": 0},')
    lines.append('    "3": {"X": 5, "Y": 3, "Z": 0}')
    lines.append("  }")
    lines.append("}")
    lines.append("```")
    lines.append("")
    lines.append("**逐层解释：**")
    lines.append("")
    lines.append("- **最外层** `{}`：整个请求的容器")
    lines.append('- **`\"Assign\"`**：告诉 MIDAS "我要分配数据"')
    lines.append('- **`\"1\", \"2\", \"3\"`**：每个节点的编号（你自己定义的序号）')
    lines.append('- **`\"X\", \"Y\", \"Z\"`**：每个节点的坐标')
    lines.append("")
    lines.append("这就创建了 3 个节点：节点1在原点，节点2在(5,0,0)，节点3在(5,3,0)。")
    lines.append("")
    lines.append("## 怎么把 JSON 发给 MIDAS？")
    lines.append("")
    lines.append("用 Python 的 `requests` 库，三行代码就够了：")
    lines.append("")
    lines.append("```python")
    lines.append("import requests")
    lines.append('url = "https://127.0.0.1:1102/db/NODE"      # MIDAS 的地址')
    lines.append('data = {"Assign": {"1": {"X": 0, "Y": 0, "Z": 0}}}  # 要发的数据')
    lines.append('r = requests.post(url, json=data, verify=False)       # 发送！')
    lines.append("```")
    lines.append("")
    lines.append("下一章开始逐个接口详细讲解。")
    lines.append("")
    return "\n".join(lines)


def gen_common_errors():
    """Generate a common errors appendix."""
    lines = []
    lines.append("# 附录B：常见错误速查表")
    lines.append("")
    lines.append("## 错误类型一览")
    lines.append("")
    lines.append("### 1. JSON 格式错误（最常见！）")
    lines.append("")
    lines.append("**症状**：MIDAS 返回 400 错误或完全不响应")
    lines.append("**原因**：JSON 语法有问题")
    lines.append("")
    lines.append("| 错误写法 | 问题 | 正确写法 |")
    lines.append("|---------|------|---------|")
    lines.append('| `{X: 1}` | 键没有加引号 | `{\"X\": 1}` |')
    lines.append('| `{\"X\": 1,}` | 最后多了一个逗号 | `{\"X\": 1}` |')
    lines.append("| `{'X': 1}` | 用了单引号（Python字典可以，但JSON不行） | `{\"X\": 1}` |")
    lines.append('| `{\\"NAME\\": \\"C50\\"}` | 引号前面多了反斜杠 | `{\"NAME\": \"C50\"}` |')
    lines.append("")
    lines.append("### 2. 参数层级放错位置")
    lines.append("")
    lines.append("**症状**：MIDAS 不报错但数据没生效")
    lines.append("**原因**：把参数放在了错误的 JSON 层级")
    lines.append("")
    lines.append("```json")
    lines.append('// ❌ 错误：X, Y, Z 应该包在 NODE 里面')
    lines.append('{"X": 0, "Y": 0, "Z": 0}')
    lines.append("")
    lines.append('// ✅ 正确')
    lines.append('{"Assign": {"1": {"X": 0, "Y": 0, "Z": 0}}}')
    lines.append("```")
    lines.append("")
    lines.append("**记住**：看接口文档中的 `json_path` 字段，它告诉你每参数应该在哪一层。")
    lines.append("")
    lines.append("### 3. 数据类型不对")
    lines.append("")
    lines.append("**症状**：MIDAS 返回错误或数据被忽略")
    lines.append("")
    lines.append('| 错误 | 问题 | 正确 |')
    lines.append("|------|------|------|")
    lines.append('| `{\"X\": \"1\"}` | X 应该是数字，不是字符串 | `{\"X\": 1}` |')
    lines.append('| `{\"NAME\": C50}` | C50 没有引号，不是字符串 | `{\"NAME\": \"C50\"}` |')
    lines.append('| `{\"FLAG\": \"true\"}` | true 加引号变成了字符串 | `{\"FLAG\": true}` |')
    lines.append("")
    lines.append("### 4. 必填参数没填")
    lines.append("")
    lines.append("**症状**：MIDAS 返回错误提示缺少参数")
    lines.append("**解决**：检查文档中标记为 `required: true` 的参数，确保都填了。")
    lines.append("")
    lines.append("### 5. 忘记 `verify=False`")
    lines.append("")
    lines.append("**症状**：Python 报 SSL 错误")
    lines.append("**原因**：MIDAS 使用自签名证书，不是浏览器信任的证书")
    lines.append("**解决**：在 `requests.post(url, json=data, verify=False)` 加上 `verify=False`")
    lines.append("")
    lines.append("### 6. 端口号搞错")
    lines.append("")
    lines.append("| 产品 | 默认端口 |")
    lines.append("|------|---------|")
    lines.append("| MIDAS Civil | 1102 |")
    lines.append("| MIDAS Gen | 1202 |")
    lines.append("| MIDAS Civil NX | 1302 |")
    lines.append("")
    return "\n".join(lines)


def gen_section_overview(section, endpoints, kb):
    """Generate section overview page."""
    section_info = {
        "DOC": {
            "title": "DOC — 项目管理 API",
            "intro": (
                "DOC 部分的 API 用于管理 MIDAS 项目文件：新建项目、打开已有项目、保存和关闭。"
                "这是最简单的部分，所有接口都只有 0-2 个参数，非常适合作为学习 API 的起点。"
            ),
            "engineering": (
                "在工程实际操作中，你打开软件第一步就是新建或打开项目。DOC API 把这些操作变成了"
                "程序指令，让你可以自动化项目管理——比如批量处理多个模型文件。"
            ),
        },
        "DB": {
            "title": "DB — 模型数据库 API",
            "intro": (
                "DB（Database）部分是 MIDAS API 的核心，包含 225 个接口，覆盖了结构建模的方方面面："
                "节点、单元、材料、截面、边界条件、各种荷载……几乎所有你在 MIDAS 界面里手动操作的建模步骤，"
                "都可以通过 DB API 来完成。"
            ),
            "engineering": (
                "这是工程师用得最多的部分。如果你需要批量建模型、参数化建模、或者从其他软件导入模型，"
                "DB API 就是你的主要工具。"
            ),
        },
        "OPE": {
            "title": "OPE — 操作命令 API",
            "intro": (
                "OPE（Operation）部分包含分析和建模过程中的操作命令：划分单元、计算截面特性、"
                "运行分析等。这些接口通常在执行前后需要调用 DB 接口来准备数据或获取结果。"
            ),
            "engineering": "适合在建模完成后、分析前的自动化流程中使用。",
        },
        "VIEW": {
            "title": "VIEW — 视图控制 API",
            "intro": (
                "VIEW 部分控制 MIDAS 的显示：选择对象、截图、控制显示状态。"
                "主要用于自动化截图和结果展示。"
            ),
            "engineering": "批量出报告时非常有用——自动截取每个工况的结果图。",
        },
        "POST": {
            "title": "POST — 后处理 API",
            "intro": (
                "POST 部分用于提取分析结果：内力表、位移表、振型结果、时程结果等。"
                "这些接口让你可以自动化读取计算结果，导出到 Excel 或做进一步处理。"
            ),
            "engineering": "批量提取结果、自动化报告生成的核心工具。",
        },
    }

    info = section_info.get(section, {"title": section, "intro": "", "engineering": ""})

    lines = []
    lines.append(f"# {info['title']}")
    lines.append("")
    lines.append(info["intro"])
    lines.append("")
    lines.append(f"本章共 **{len(endpoints)}** 个接口。")
    lines.append("")
    lines.append("## 工程背景")
    lines.append("")
    lines.append(info["engineering"])
    lines.append("")

    # List all endpoints in this section
    lines.append("## 接口列表")
    lines.append("")
    lines.append("| 接口 | 方法 | 参数数 | 说明 |")
    lines.append("|------|------|--------|------|")

    for ep in sorted(endpoints, key=lambda e: e["path"]):
        d = ep["data"]
        n_params = len(d.get("parameters", []))
        n_req = len([p for p in d.get("parameters", []) if is_required(p)])
        methods = ", ".join(get_http_methods(d))
        desc = d.get("parameters", [{}])[0].get("description", "")[:60] if d.get("parameters") else ""
        lines.append(f"| `{ep['path']}` | {methods} | {n_params} ({n_req} 必填) | {desc} |")

    lines.append("")
    return "\n".join(lines)


def gen_endpoint_tutorial(ep, is_detailed=False):
    """Generate a full tutorial section for one endpoint."""
    d = ep["data"]
    api_name = d.get("api_name", ep["path"])
    methods = get_http_methods(d)
    req_p, opt_p = flat_params(d)
    example_data = get_example(d)

    lines = []
    lines.append(f"## {api_name} — `{ep['path']}`")
    lines.append("")
    lines.append(f"**HTTP 方法**: {', '.join(methods)} | **参数总数**: {len(req_p) + len(opt_p)}（{len(req_p)} 必填 + {len(opt_p)} 可选）")
    lines.append("")

    # 1. Engineering meaning
    lines.append("### 1. 这是什么？（工程含义）")
    lines.append("")
    lines.append(_gen_engineering_description(ep, d))
    lines.append("")

    # 2. JSON structure
    lines.append("### 2. JSON 结构（逐层解释）")
    lines.append("")
    lines.append(_gen_json_explanation(d))
    lines.append("")

    # 3. Required vs optional
    lines.append("### 3. 必填 vs 可选参数")
    lines.append("")
    lines.append(_gen_param_table(req_p, opt_p))
    lines.append("")

    # 4. Where optional params go
    if opt_p:
        lines.append("### 4. 可选参数放在哪里？")
        lines.append("")
        lines.append(_gen_optional_placement(opt_p, d))
        lines.append("")

    # 5. Parameter relationships
    if len(req_p) + len(opt_p) >= 2:
        lines.append("### 5. 参数之间的关系")
        lines.append("")
        lines.append(_gen_param_relationships(d))
        lines.append("")

    # 6. Minimal runnable example
    lines.append("### 6. 最小可运行代码")
    lines.append("")
    lines.append(_gen_minimal_code(ep, d, req_p))
    lines.append("")

    # 7. Engineering significance
    lines.append("### 7. 工程意义")
    lines.append("")
    lines.append(_gen_engineering_significance(ep, d))
    lines.append("")

    # 8. Common errors
    lines.append("### 8. 常见错误")
    lines.append("")
    lines.append(_gen_endpoint_errors(ep, d))
    lines.append("")

    # 9. Batch generation
    lines.append("### 9. Python 批量生成案例")
    lines.append("")
    lines.append(_gen_batch_generation(ep, d))
    lines.append("")

    # 10. For-loop optimization
    lines.append("### 10. for 循环优化案例")
    lines.append("")
    lines.append(_gen_for_loop_optimization(ep, d))
    lines.append("")

    return "\n".join(lines)


def gen_endpoint_reference(ep):
    """Generate a shorter reference card for an endpoint."""
    d = ep["data"]
    api_name = d.get("api_name", ep["path"])
    methods = ", ".join(get_http_methods(d))
    req_p, opt_p = flat_params(d)
    example_data = get_example(d)

    lines = []
    lines.append(f"### {api_name} — `{ep['path']}`")
    lines.append("")
    lines.append(f"**方法**: {methods} | **参数**: {len(req_p)} 必填 + {len(opt_p)} 可选")
    lines.append("")

    # Quick parameter table
    if req_p or opt_p:
        lines.append("| 参数 | 类型 | 必填 | 说明 |")
        lines.append("|------|------|------|------|")
        for p in req_p:
            lines.append(f"| `{p['key']}` | {describe_type(p.get('value_type',''))} | **是** | {p.get('description','')[:80]} |")
        for p in opt_p[:10]:  # limit optional params shown
            lines.append(f"| `{p['key']}` | {describe_type(p.get('value_type',''))} | 否 | {p.get('description','')[:80]} |")
        if len(opt_p) > 10:
            lines.append(f"| ... | ... | ... | *还有 {len(opt_p) - 10} 个可选参数* |")
        lines.append("")

    # Minimal JSON
    minimal = build_minimal_json(d)
    if minimal:
        lines.append("**最简 JSON**：")
        lines.append("```json")
        lines.append(json.dumps(minimal, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")

    # Example if available
    if example_data:
        lines.append("**官方示例**：")
        lines.append("```json")
        lines.append(json.dumps(example_data, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


# ── Sub-generators for each teaching point ────────────────────────────────────

def _gen_engineering_description(ep, d):
    """Generate simple engineering description."""
    api_name = d.get("api_name", "")
    section = ep["section"]
    path = ep["path"]
    params = d.get("parameters", [])

    # Build description from available data
    desc_parts = []

    # Check if there's a meaningful description in the first parameter
    for p in params:
        if p.get("description") and len(p["description"]) > 10:
            desc_parts.append(p["description"])
            break

    # Determine what kind of operation this is
    methods = get_http_methods(d)
    method_text = ""
    if "POST" in methods and "GET" in methods:
        method_text = "创建和查询"
    elif "POST" in methods:
        method_text = "创建/设置"
    elif "GET" in methods:
        method_text = "查询/获取"
    elif "DELETE" in methods:
        method_text = "删除"

    # Section-specific context
    section_context = {
        "DOC": "这是项目文件管理操作。",
        "DB": f"这是模型数据库的{method_text}操作，属于 {ep.get('subsection', '建模')} 类别。",
        "OPE": "这是一个操作/计算命令。",
        "VIEW": "这是视图控制操作。",
        "POST": "这是后处理结果提取操作。",
    }

    result = f"**{api_name}** — {section_context.get(section, '')}"
    if desc_parts:
        result += f"\n\n{desc_parts[0]}"
    result += f"\n\n> 简单说：这个接口用来**{' '.join(api_name.split()) if api_name else path}**。"
    return result


def _gen_json_explanation(d):
    """Explain JSON structure layer by layer."""
    params = d.get("parameters", [])
    if not params:
        return "这个接口不需要发送 JSON 数据（GET 请求）。"

    # Group params by json_level
    by_level = defaultdict(list)
    for p in params:
        level = p.get("json_level", "root")
        by_level[level].append(p)

    lines = []
    lines.append("下面按照从外到内的顺序解释每一层的 JSON 结构：")
    lines.append("")
    lines.append("```json")

    # Generate the JSON structure with comments
    full = build_full_json(d)
    lines.append(json.dumps(_clean_placeholders(full), indent=2, ensure_ascii=False))
    lines.append("```")
    lines.append("")

    # Layer explanation
    levels = sorted(by_level.keys())
    for i, level in enumerate(levels):
        level_params = by_level[level]
        if level == "root":
            lines.append(f"**第 {i+1} 层：最外层**")
            lines.append("这是整个 JSON 的入口。")
        else:
            parts = level.split(".")
            lines.append(f"**第 {i+1} 层：`{level}`** — {len(level_params)} 个参数在这一层")
            lines.append("")

        for p in level_params[:8]:
            lines.append(f"- `\"{p['key']}\"`: {describe_type(p.get('value_type', ''))} — {p.get('description', '')[:100]}")
        if len(level_params) > 8:
            lines.append(f"- ... *还有 {len(level_params) - 8} 个参数*")
        lines.append("")

    return "\n".join(lines)


def _clean_placeholders(obj):
    """Remove _optional placeholder keys and clean up values for display."""
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if k == "_optional":
                for ok, ov in v.items():
                    key = f"{ok} (可选)"
                    result[key] = _clean_placeholders(ov)
            else:
                result[k] = _clean_placeholders(v)
        return result
    elif isinstance(obj, list):
        return [_clean_placeholders(i) for i in obj]
    return obj


def _gen_param_table(req_p, opt_p):
    """Generate parameter table distinguishing required vs optional."""
    lines = []
    if req_p:
        lines.append("**必填参数**（不填会报错）：")
        lines.append("")
        lines.append("| 参数名 | 类型 | JSON 路径 | 说明 |")
        lines.append("|--------|------|-----------|------|")
        for p in req_p:
            lines.append(f"| `{p['key']}` | {describe_type(p.get('value_type',''))} | `{p.get('json_path', '')}` | {p.get('description', '')[:60]} |")
        lines.append("")

    if opt_p:
        lines.append("**可选参数**（填不填都行）：")
        lines.append("")
        lines.append("| 参数名 | 类型 | 默认值 | 说明 |")
        lines.append("|--------|------|--------|------|")
        for p in opt_p[:15]:
            default = p.get("default")
            if default is None:
                default = "无"
            lines.append(f"| `{p['key']}` | {describe_type(p.get('value_type',''))} | `{default}` | {p.get('description', '')[:60]} |")
        lines.append("")

    if not req_p and not opt_p:
        lines.append("这个接口没有参数。")
        lines.append("")

    return "\n".join(lines)


def _gen_optional_placement(opt_p, d):
    """Explain where optional params go in JSON structure."""
    lines = []
    lines.append("可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：")
    lines.append("")

    for p in opt_p[:10]:
        path = p.get("json_path", p["key"])
        parts = path.split(".")
        level_desc = " → ".join(f'"{part}"' for part in parts)
        lines.append(f"- `{p['key']}` 的路径：**{level_desc}**")
        lines.append(f"  意思是：在 JSON 中依次打开 {', '.join(f'{part}' for part in parts)}，最后填入 `{p['key']}` 的值")

    lines.append("")
    lines.append("**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。")
    lines.append("")
    return "\n".join(lines)


def _gen_param_relationships(d):
    """Explain relationships between parameters."""
    params = d.get("parameters", [])
    lines = []
    lines.append("以下参数之间存在关联关系：")
    lines.append("")

    # Find params with cross-references
    for p in params:
        desc = p.get("description", "")
        if "refer to" in desc.lower() or "reference" in desc.lower():
            lines.append(f"- `{p['key']}` 的取值需要参考其他接口文档")
        if "only" in desc.lower() or "must" in desc.lower() or "require" in desc.lower():
            lines.append(f"- `{p['key']}`：{desc[:120]}")

    # Enums that determine other params
    for p in params:
        desc = p.get("description", "")
        if ":" in desc or "{" in desc:
            lines.append(f"- `{p['key']}` 有多个可选值（见参数表），不同取值会影响后续参数的需求")

    if not lines[2:]:  # Only has header lines
        lines.append("这个接口的参数之间没有复杂的依赖关系。每个参数可以独立填写。")

    lines.append("")
    lines.append("**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。")
    lines.append("")
    return "\n".join(lines)


def _gen_minimal_code(ep, d, req_p):
    """Generate minimal runnable Python code."""
    section = ep["section"]
    path = ep["path"]
    methods = get_http_methods(d)
    method = methods[0] if methods else "POST"

    minimal_json = build_minimal_json(d)
    # Clean up for display
    clean_json = _remove_placeholders(minimal_json)

    lines = []
    lines.append("以下是能跑起来的最简代码：")
    lines.append("")
    lines.append("```python")
    lines.append("import requests")
    lines.append("import urllib3")
    lines.append("urllib3.disable_warnings()  # 关闭 SSL 警告")
    lines.append("")
    lines.append("# MIDAS 服务地址（根据你的产品修改端口）")
    lines.append('BASE = "https://127.0.0.1:1102"')
    lines.append("")

    if method == "GET":
        lines.append(f'url = f"{{BASE}}{path}"')
        lines.append("r = requests.get(url, verify=False)")
        lines.append("print(r.json())  # 查看返回结果")
    else:
        lines.append(f'url = f"{{BASE}}{path}"')
        lines.append("")
        lines.append("# JSON 数据 — 这是你要发给 MIDAS 的内容")
        lines.append("data = " + json.dumps(clean_json, indent=4, ensure_ascii=False).replace("\n", "\n# "))
        lines.append("")
        lines.append("# 发送请求")
        lines.append("r = requests.post(url, json=data, verify=False)")
        lines.append("")
        lines.append("# 检查结果")
        lines.append("if r.status_code == 200:")
        lines.append('    print("成功！")')
        lines.append("    print(r.json())")
        lines.append("else:")
        lines.append(f'    print(f"失败，错误码：{{r.status_code}}")')

    lines.append("```")
    lines.append("")
    lines.append("**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。")
    lines.append("")
    return "\n".join(lines)


def _remove_placeholders(obj):
    """Remove _optional keys from JSON for clean display."""
    if isinstance(obj, dict):
        return {k: _remove_placeholders(v) for k, v in obj.items() if k != "_optional"}
    elif isinstance(obj, list):
        return [_remove_placeholders(i) for i in obj]
    return obj


def _gen_engineering_significance(ep, d):
    """Explain why an engineer would need this."""
    section = ep["section"]
    api_name = d.get("api_name", "")

    patterns = {
        "DOC": "自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。",
        "DB": "参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。",
        "OPE": "操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。",
        "VIEW": "自动截图——写报告时，让程序自动截取每个结果视图，而不是手动截图几十次。",
        "POST": "自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。",
    }

    result = patterns.get(section, "提高工作效率，减少重复性劳动。")
    return result


def _gen_endpoint_errors(ep, d):
    """Generate common errors specific to this endpoint."""
    lines = []
    lines.append("使用这个接口时最容易犯的错误：")
    lines.append("")

    req_p, _ = flat_params(d)

    # Error 1: Missing required params
    if req_p:
        lines.append(f"1. **忘记填必填参数**：{'、'.join(p['key'] for p in req_p)} 是必填的，漏掉任何一个都会报错。")
    else:
        lines.append("1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。")

    # Error 2: Wrong JSON structure
    params = d.get("parameters", [])
    if len(params) > 2:
        # Find unique json_levels
        levels = set(p.get("json_level", "root") for p in params)
        if len(levels) > 1:
            lines.append(f"2. **JSON 层级放错**：这个接口有 {len(levels)} 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。")

    # Error 3: Type issues
    array_params = [p for p in params if "Array" in norm_type(p.get("value_type", ""))]
    if array_params:
        lines.append(f"3. **数组格式错误**：{'、'.join(p['key'] for p in array_params[:3])} 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。")

    # Error 4: URL issues
    lines.append(f"4. **URL 写错**：确认路径是 `{ep['path']}`——多一个斜杠或少一个都会导致 404 错误。")

    lines.append("")
    return "\n".join(lines)


def _gen_batch_generation(ep, d):
    """Generate batch generation example using Python."""
    path = ep["path"]
    methods = get_http_methods(d)
    if "POST" not in methods:
        return "GET 请求不需要批量生成——直接发一次请求就能拿到所有数据。"

    req_p, _ = flat_params(d)
    minimal = build_minimal_json(d)
    clean = _remove_placeholders(minimal)

    lines = []
    lines.append("如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：")
    lines.append("")
    lines.append("```python")
    lines.append("import requests")
    lines.append("import urllib3")
    lines.append("urllib3.disable_warnings()")
    lines.append("")
    lines.append(f'BASE = "https://127.0.0.1:1102"')
    lines.append("")
    lines.append("# 定义基础数据模板")
    lines.append("def make_data(**kwargs):")
    lines.append("    " + f'"""根据参数生成 {d.get("api_name", path)} 的 JSON 数据。"""')
    lines.append("    data = " + json.dumps(clean, ensure_ascii=False))
    lines.append("    # 在这里修改需要变化的值")
    lines.append("    for key, value in kwargs.items():")
    lines.append("        # 根据 json_path 更新对应位置的值")
    lines.append("        pass  # 具体逻辑见下面的 for 循环例子")
    lines.append("    return data")
    lines.append("")
    lines.append("# 批量调用")
    lines.append("results = []")
    lines.append("for i in range(1, 11):  # 生成 10 个")
    lines.append("    data = make_data()    # 在这里修改参数")
    lines.append(f'    r = requests.post(f"{{BASE}}{path}", json=data, verify=False)')
    lines.append("    results.append(r.json())")
    lines.append("    print(f'第 {i} 个完成')")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def _gen_for_loop_optimization(ep, d):
    """Generate for-loop optimization example."""
    path = ep["path"]
    api_name = d.get("api_name", "")
    section = ep["section"]

    lines = []
    lines.append("对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：")
    lines.append("")

    # Show specific optimization based on section
    if section == "DB":
        lines.append(f"**技巧 1：利用 Assign 结构一次发送多个对象**")
        lines.append("")
        lines.append("很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `\"1\"`, `\"2\"`, ... 区分。")
        lines.append("")
        lines.append("```python")
        lines.append("# ❌ 慢：循环 100 次，每次发一个节点")
        lines.append("for i in range(100):")
        lines.append('    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}')
        lines.append('    requests.post(url, json=data, verify=False)')
        lines.append("")
        lines.append("# ✅ 快：一次发 100 个节点")
        lines.append("nodes = {}")
        lines.append("for i in range(100):")
        lines.append(f'    nodes[str(i+1)] = {{"X": i, "Y": 0, "Z": 0}}')
        lines.append('data = {"Assign": nodes}')
        lines.append("requests.post(url, json=data, verify=False)")
        lines.append("```")
        lines.append("")
        lines.append(f"**技巧 2：使用列表推导式预生成数据**（在 {api_name} 中适用）")
        lines.append("")
        lines.append("```python")
        lines.append("# 列表推导式 — 一行代码生成所有节点的坐标")
        lines.append('nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}')
        lines.append('data = {"Assign": nodes}')
        lines.append("requests.post(url, json=data, verify=False)")
        lines.append("```")
    else:
        lines.append("```python")
        lines.append("# 使用 session 复用连接（比每次新建连接快 3-5 倍）")
        lines.append("session = requests.Session()")
        lines.append("session.verify = False")
        lines.append("")
        lines.append("for i in range(100):")
        lines.append("    data = {...}  # 你的数据")
        lines.append(f'    r = session.post(f"{{BASE}}{path}", json=data)')
        lines.append("```")

    lines.append("")
    lines.append("**通用优化原则**：")
    lines.append("")
    lines.append("1. 能一次发多个就不要循环发单个")
    lines.append("2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求")
    lines.append("3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送")
    lines.append("")
    return "\n".join(lines)


# ── Main Generation Logic ────────────────────────────────────────────────────

def main():
    print("Reading knowledge base...")
    kb = load_kb(KB_PATH)

    all_endpoints = collect_all_endpoints(kb)
    print(f"Found {len(all_endpoints)} endpoints")

    sections_order = ["DOC", "DB", "OPE", "VIEW", "POST"]

    # Create output directories
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "appendix"), exist_ok=True)

    # Generate appendix files
    print("Generating JSON basics primer...")
    with open(os.path.join(OUT_DIR, "appendix", "json-basics.md"), "w", encoding="utf-8") as f:
        f.write(gen_json_basics())

    print("Generating common errors reference...")
    with open(os.path.join(OUT_DIR, "appendix", "common-errors.md"), "w", encoding="utf-8") as f:
        f.write(gen_common_errors())

    # Generate section pages
    for section in sections_order:
        section_eps = [e for e in all_endpoints if e["section"] == section]
        if not section_eps:
            continue

        print(f"Generating {section} section ({len(section_eps)} endpoints)...")

        content = []
        content.append(gen_section_overview(section, section_eps, kb))
        content.append("")
        content.append("---")
        content.append("")
        content.append("# 详细教程")
        content.append("")

        # Select key endpoints for detailed tutorials
        # Criteria: representative parameter patterns, good for learning
        key_endpoints = _select_key_endpoints(section_eps, section)

        for ep in section_eps:
            if ep in key_endpoints:
                content.append(gen_endpoint_tutorial(ep, is_detailed=True))
            else:
                content.append(gen_endpoint_reference(ep))
            content.append("")
            content.append("---")
            content.append("")

        filepath = os.path.join(OUT_DIR, f"{section}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

    # Generate main index last (after we have all content)
    print("Generating main index...")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(gen_main_index(all_endpoints, sections_order))

    print(f"\nDone! Teaching materials generated in '{OUT_DIR}/'")
    print(f"  - README.md (main index)")
    for section in sections_order:
        path = os.path.join(OUT_DIR, f"{section}.md")
        if os.path.exists(path):
            print(f"  - {section}.md")
    print(f"  - appendix/json-basics.md")
    print(f"  - appendix/common-errors.md")


def _select_key_endpoints(section_eps, section):
    """Select representative endpoints for detailed tutorials."""
    key_endpoints = []

    # Section-specific selection logic
    if section == "DOC":
        # DOC is small, teach them all in detail
        return section_eps

    # For larger sections, select 3-6 representative endpoints
    # Criteria: minimum parameters, mid complexity, complex
    sorted_eps = sorted(section_eps, key=lambda e: len(e["data"].get("parameters", [])))

    # 1. Simplest endpoint (best for first example)
    if sorted_eps:
        key_endpoints.append(sorted_eps[0])

    # 2. A mid-complexity endpoint
    mid_idx = len(sorted_eps) // 2
    if mid_idx < len(sorted_eps) and sorted_eps[mid_idx] not in key_endpoints:
        key_endpoints.append(sorted_eps[mid_idx])

    # 3. One of the most complex (shows nesting)
    if len(sorted_eps) > 2:
        key_endpoints.append(sorted_eps[-1])

    # 4. Endpoints with examples
    for ep in section_eps:
        if ep not in key_endpoints and ep["data"].get("json_examples"):
            key_endpoints.append(ep)
            break

    # 5. Endpoints with the most required params (important ones)
    eps_by_req = sorted(section_eps, key=lambda e: len([p for p in e["data"].get("parameters", []) if is_required(p)]), reverse=True)
    if eps_by_req and eps_by_req[0] not in key_endpoints:
        key_endpoints.append(eps_by_req[0])

    return key_endpoints


if __name__ == "__main__":
    main()
