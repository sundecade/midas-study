"""
MIDAS API Code Examples Generator (Part 3)
Generates beginner-friendly, heavily-commented Python API calling scripts
organized by engineering workflow.

Target audience: engineers with domain knowledge, no programming experience.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

KB_PATH = "midas_api_knowledge_base.json"
OUT_DIR = "code_examples"


def load_kb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_section_endpoints(kb, section):
    """Get all endpoints for a section with their paths."""
    api_data = kb.get("api_data", {})
    sec_data = api_data.get(section, {})
    endpoints = {}

    def walk(data):
        if not isinstance(data, dict):
            return
        for key, value in data.get("endpoints", {}).items():
            if isinstance(value, dict) and "api_name" in value:
                endpoints[key] = value
        for key, value in data.get("subsections", {}).items():
            walk(value)
        for key, value in data.items():
            if key in ("endpoints", "subsections"):
                continue
            if isinstance(value, dict) and "api_name" in value:
                endpoints[key] = value

    walk(sec_data)
    return endpoints


# ── Script Generators ─────────────────────────────────────────────────────────

HEADER = '''"""
MIDAS API 调用示例 —— {title}
======================================
目标读者：懂工程的工程师，第一次用 API
运行前提：
  1. MIDAS Civil 已打开并加载了项目
  2. Python 3 已安装
  3. 已安装 requests 库：pip install requests

每个例子都是完整的、可以单独运行的代码块。
直接复制粘贴到你的 Python 文件里就能跑。
"""

import requests
import urllib3

# 关闭 SSL 警告（MIDAS 使用自签名证书，会有 SSL 警告）
urllib3.disable_warnings()

# ============================================================
# 基础设置 —— 根据你的 MIDAS 产品修改端口号
# ============================================================
# MIDAS Civil   → 端口 1102
# MIDAS Gen     → 端口 1202
# MIDAS Civil NX → 端口 1302
BASE_URL = "https://127.0.0.1:1102"

print("=" * 60)
print("{title}")
print("=" * 60)
'''


def gen_project_management_script(kb):
    """Generate 01_project_management.py — DOC section examples."""
    eps = get_section_endpoints(kb, "DOC")

    content = HEADER.format(title="01 项目管理 —— 新建、打开、保存项目")

    content += '''
# ============================================================
# 第 1 步：新建一个空项目
# ============================================================
# 解释：
#   - 我们要向 MIDAS 发送一个 HTTP POST 请求
#   - 请求地址 = BASE_URL + "/doc/NEW"
#   - 请求体是一个 JSON 对象（ Python 中的 dict）
#   - 这个接口几乎不需要参数，给一个空的 Argument 对象即可

print("\\n>>> 第 1 步：新建项目")

# === 构建 JSON 数据 ===
# JSON 数据在 Python 中就是 dict（字典），写法几乎一模一样
# JSON          →  Python
# {"A": 1}      →  {"A": 1}
# {"A": [1,2]}  →  {"A": [1, 2]}
# {"A": {"B": 1}} → {"A": {"B": 1}}

# 这是要发给 MIDAS 的数据
data_new = {
    "Argument": {}  # Argument 是参数容器，新建项目不需要填任何参数，给空对象
}

# 打印一下我们要发的 JSON（方便调试）
print("要发送的 JSON：")
print(json.dumps(data_new, indent=2, ensure_ascii=False))
'''

    content += '''
import json  # json.dumps() 用来把 Python 字典转成格式化的 JSON 字符串

# === 发送请求 ===
# requests.post() 发送 POST 请求
#   参数1: URL（接口地址）
#   参数2: json=data（Python 字典，requests 会自动转成 JSON 字符串发出去）
#   参数3: verify=False（因为 MIDAS 使用自签名证书，不做 SSL 验证）
response = requests.post(
    f"{BASE_URL}/doc/NEW",
    json=data_new,
    verify=False
)

# === 检查结果 ===
# HTTP 状态码 200 表示成功
print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("项目创建成功！")
    # response.json() 把 MIDAS 返回的 JSON 转成 Python 字典
    print("MIDAS 返回的数据：", response.json())
else:
    print(f"创建失败，错误信息：{response.text}")

# ============================================================
# 第 2 步：保存项目到文件
# ============================================================
# /doc/SAVEAS 接口把当前项目另存为一个 .mcb 文件
# 可选参数 Argument：保存的文件路径

print("\\n>>> 第 2 步：保存项目")

# === 构建 JSON 数据 ===
data_save = {
    "Argument": "C:\\\\MIDAS\\\\my_project.mcb"
    #            ↑ 注意：Windows 路径中的反斜杠在 JSON 里要写双反斜杠 \\\\
    #            或者用正斜杠： "C:/MIDAS/my_project.mcb"
}

print("要发送的 JSON：")
print(json.dumps(data_save, indent=2, ensure_ascii=False))

response = requests.post(
    f"{BASE_URL}/doc/SAVEAS",
    json=data_save,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("项目保存成功！")
else:
    print(f"保存失败：{response.text}")

# ============================================================
# 第 3 步：关闭项目
# ============================================================

print("\\n>>> 第 3 步：关闭项目")

data_close = {"Argument": {}}

response = requests.post(
    f"{BASE_URL}/doc/CLOSE",
    json=data_close,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("项目已关闭。")
else:
    print(f"关闭失败：{response.text}")

# ============================================================
# 总结：DOC 部分学到的
# ============================================================
# 1. 所有 DOC 接口都用 POST 方法
# 2. JSON 结构都是 {"Argument": ...}
# 3. Argument 的值可以是空对象 {}、字符串（路径）、或者其他数值
# 4. 发请求用 requests.post(url, json=data, verify=False)
# 5. 检查 response.status_code 判断成功还是失败
'''
    return content


def gen_create_model_script(kb):
    """Generate 02_create_model.py — DB section: nodes, elements, materials."""
    eps = get_section_endpoints(kb, "DB")

    content = HEADER.format(title="02 创建模型 —— 节点、单元、材料、截面")
    content += '''
import json

# ============================================================
# 在开始之前 —— 理解 MIDAS API 的数据结构
# ============================================================
#
# MIDAS API 发送数据的通用格式（DB 部分）：
#
# {
#   "Assign": {           ← Assign 表示"分配数据到模型"
#     "1": { ... },       ← "1", "2", "3" 是你自己定义的序号
#     "2": { ... },       ← 每一个序号代表一个独立的数据对象
#     "3": { ... }        ← 一个请求可以同时发送多个对象
#   }
# }
#
# 为什么这样组织？
#   因为工程模型通常有大量相似的对象（几百个节点、几百个单元）。
#   把多个对象打包在 Assign 下面一次性发送，比逐个发要快得多。
#   这就好比你在 Excel 里复制粘贴一整列，而不是一个一个格子填。
#
# 重要规律：
#   - "Assign" 下的数字键是你自己定的序号（只在本请求中有效）
#   - MIDAS 用这些序号区分同一批请求中的不同对象
#   - 序号必须是字符串，不是数字（写 "1" 不写 1）
'''

    # Add node creation example
    content += '''
# ============================================================
# 示例 1：创建节点
# ============================================================
# 接口：/db/NODE
# 作用：在模型中创建节点（空间坐标点）
#
# 参数说明（来自 API 文档）：
#   必填：无（所有参数都有默认值 0）
#   可选：X, Y, Z —— 节点的三个坐标
#         单位：当前模型的长度单位（通常是 mm 或 m）

print("\\n>>> 示例 1：创建节点")

# === 步骤 1：在 Python 中构建 JSON 数据 ===
# 我们要创建 3 个节点：
#   节点 1: 原点 (0, 0, 0)
#   节点 2: X 方向 5 米处 (5000, 0, 0)   ← 假设单位是 mm
#   节点 3: X=5m, Y=3m 处 (5000, 3000, 0)

# 用一个 dict（字典）来存储所有节点数据
nodes_data = {
    "Assign": {
        "1": {"X": 0,     "Y": 0,     "Z": 0},       # 节点 1：原点
        "2": {"X": 5000,  "Y": 0,     "Z": 0},       # 节点 2：(5m, 0, 0)
        "3": {"X": 5000,  "Y": 3000,  "Z": 0}        # 节点 3：(5m, 3m, 0)
    }
}

# === 步骤 2：发送数据 ===
print("要创建的节点：")
print(json.dumps(nodes_data, indent=2, ensure_ascii=False))

response = requests.post(
    f"{BASE_URL}/db/NODE",
    json=nodes_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("节点创建成功！")
else:
    print(f"创建失败：{response.text}")

# ============================================================
# 示例 2：用 for 循环批量创建节点
# ============================================================
# 工程中经常需要创建一排等间距的节点（比如桥面纵梁的节点）。
# 用手动一个个写太慢了，用 for 循环可以自动生成。

print("\\n>>> 示例 2：用 for 循环批量创建节点")

# === 理解循环逻辑 ===
# for i in range(1, 11):
#     循环体
#
# range(1, 11) 生成数字序列：1, 2, 3, ..., 10
#   - 参数1：起始值（包含）
#   - 参数2：结束值（不包含！所以 range(1, 11) 只到 10）
#   ↓ 为什么从 1 开始？因为 MIDAS 中节点/单元编号习惯从 1 开始
#   ↓ 如果你要从 0 开始：range(0, 10) 生成 0, 1, 2, ..., 9
#
# i 是循环变量，每次循环 i 的值会自动加 1：
#   第 1 轮：i = 1
#   第 2 轮：i = 2
#   第 3 轮：i = 3
#   ...

# 需求：创建一排 X 方向等间距的节点
#   起点 X=0，终点 X=10000，共 11 个节点（间距 1000mm = 1m）

start_x = 0       # 起始 X 坐标（mm）
end_x = 10000     # 结束 X 坐标（mm）
num_nodes = 11    # 节点个数

# 用字典推导式批量生成节点数据
# （看不懂推导式没关系，后面有等价的 for 循环写法）
nodes_batch = {}
for i in range(num_nodes):
    x = start_x + (end_x - start_x) * i / (num_nodes - 1)
    #  ↑ 线性插值：均匀分布在起点和终点之间
    node_id = str(i + 1)  # 序号从 1 开始，转成字符串
    nodes_batch[node_id] = {"X": x, "Y": 0, "Z": 0}

batch_data = {"Assign": nodes_batch}

print(f"批量创建 {num_nodes} 个等间距节点：")
print(json.dumps(batch_data, indent=2, ensure_ascii=False))
print(f"\\n生成的 JSON 包含 {len(nodes_batch)} 个节点")
print("JSON 顶层是 Assign，下面每个数字键是一个节点的坐标")

response = requests.post(
    f"{BASE_URL}/db/NODE",
    json=batch_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print(f"{num_nodes} 个节点批量创建成功！")
else:
    print(f"创建失败：{response.text}")
'''

    # Add material creation
    content += '''
# ============================================================
# 示例 3：创建材料
# ============================================================
# 接口：/db/MATL
# 作用：定义材料属性（混凝土、钢材等）
#
# 关键参数：
#   必填：TYPE（材料类型）、NAME（材料名称）、PARAM（材料参数对象）
#   PARAM 里面的参数由 TYPE 决定：
#     TYPE="CONC" → 需要 STRENGTH（强度）、ELASTIC（弹模）等
#     TYPE="STEEL" → 需要 FY（屈服强度）、FU（极限强度）等

print("\\n>>> 示例 3：创建材料")

# === C50 混凝土 ===
conc_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC",         # 混凝土类型
            "NAME": "C50",          # 材料名称
            "PARAM": {              # 材料参数 —— 这里面的值取决于 TYPE
                "P_TYPE": 1,        # 参数类型编号（每种材料的定义不同）
                "STANDARD": "JTG04",  # 规范（中国 04 桥规）
                "DB": "C50",        # 强度等级
                "ELASTIC": 34500000,  # 弹性模量（单位：kN/m^2）
                "POISSON": 0.2,     # 泊松比
                "THERMAL": 0.00001, # 线膨胀系数
                "DAMP": 0.05        # 阻尼比
            }
        }
    }
}

print("C50 混凝土的 JSON 数据：")
print(json.dumps(conc_data, indent=2, ensure_ascii=False))
print("\\nJSON 结构说明：")
print("  第 1 层: Assign → 数据容器")
print("  第 2 层: '1' → 这一批要创建的材料序号")
print("  第 3 层: TYPE, NAME, PARAM → 材料的基本属性")
print("  第 4 层: PARAM 内部 → 由 TYPE 决定的具体力学参数")

response = requests.post(
    f"{BASE_URL}/db/MATL",
    json=conc_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("材料创建成功！")
else:
    print(f"创建失败：{response.text}")

# ============================================================
# 总结：模型创建部分学到的
# ============================================================
# 1. DB 接口的数据都包在 {"Assign": {...}} 里面
# 2. Assign 下的数字键是你自定义的序号（必须用字符串 "1" 不是数字 1）
# 3. 一次可以发多个对象（批量操作），比逐个发快得多
# 4. for 循环可以高效生成规律性的数据（等距节点、编号递增等）
# 5. 参数之间的关系：TYPE 决定 PARAM 里面需要填什么
'''
    return content


def gen_apply_loads_script(kb):
    """Generate 03_apply_loads.py — DB section: boundary conditions and loads."""
    content = HEADER.format(title="03 施加荷载和边界条件")
    content += '''
import json

# ============================================================
# 在开始之前 —— 理解荷载数据的 JSON 组织方式
# ============================================================
#
# 荷载相关接口也使用 {"Assign": {...}} 的结构。
# 但和节点/单元不同的是，荷载通常需要引用已有的模型对象。
#
# 例如：节点荷载要指定加载到哪些节点上
# {
#   "Assign": {
#     "1": {
#       "ITEMS": [1, 2, 3],     ← 表示这些节点编号
#       "LCNAME": "自重",        ← 荷载工况名称
#       ...
#     }
#   }
# }
#
# 关键规则：
#   - ITEMS 是一个列表（方括号 []），存的是节点/单元编号
#   - 编号是 MIDAS 模型中的实际编号（不是 API 请求里的序号）
#   - LCNAME 引用已定义的荷载工况名

# ============================================================
# 示例 1：创建边界条件组
# ============================================================
# 接口：/db/BNGR
# 作用：创建一个边界条件组（给支座起个名字）

print("\\n>>> 示例 1：创建边界条件组")

bngr_data = {
    "Assign": {
        "1": {
            "NAME": "固定支座",     # 组名称（你自己起名）
            "AUTOTYPE": 0           # 0=手动定义（不是自动生成的）
        }
    }
}

print("要发送的 JSON：")
print(json.dumps(bngr_data, indent=2, ensure_ascii=False))

response = requests.post(
    f"{BASE_URL}/db/BNGR",
    json=bngr_data,
    verify=False
)
print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("边界组创建成功！")
else:
    print(f"创建失败：{response.text}")

# ============================================================
# 示例 2：创建节点约束（支座条件）
# ============================================================
# 接口：/db/CONS
# 作用：在节点上施加约束（固定铰、活动铰、固结等）

print("\\n>>> 示例 2：创建节点约束")

# 约束条件用一个 6 位字符串表示，每位代表一个自由度：
#   Dx, Dy, Dz, Rx, Ry, Rz
#   1 = 约束（固定），0 = 自由
#
# 例如：
#   "111000" = 固定铰支座（约束三个方向位移，允许转动）
#   "111111" = 完全固结（约束所有自由度）
#   "001000" = 只约束 Z 方向位移

cons_data = {
    "Assign": {
        "1": {
            "ITEMS": [1, 2],           # 约束施加在节点 1 和节点 2 上
            "GROUP_NAME": "固定支座",   # 归属的边界组
            "CONSTRAINT": "111000"     # 约束类型：固定铰
            #               ||||||
            #               |||||└─ Rz（绕Z轴转动）：0 = 自由
            #               ||||└── Ry（绕Y轴转动）：0 = 自由
            #               |||└─── Rx（绕X轴转动）：0 = 自由
            #               ||└──── Dz（Z方向位移）：1 = 约束
            #               |└───── Dy（Y方向位移）：1 = 约束
            #               └────── Dx（X方向位移）：1 = 约束
        }
    }
}

print("要发送的 JSON：")
print(json.dumps(cons_data, indent=2, ensure_ascii=False))
print("\\nCONSTRAINT 字段说明：")
print("  '111000' = 约束 Dx,Dy,Dz，放开 Rx,Ry,Rz → 固定铰支座")

response = requests.post(
    f"{BASE_URL}/db/CONS",
    json=cons_data,
    verify=False
)
print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("节点约束创建成功！")
else:
    print(f"创建失败：{response.text}")

# ============================================================
# 示例 3：用循环批量创建弹簧支座
# ============================================================
# 场景：桥墩上每个支座位置都有一个弹簧约束

print("\\n>>> 示例 3：批量创建弹簧约束")

# 假设我们有墩顶节点编号列表
pier_top_nodes = [11, 12, 13, 14]  # 4 个墩顶节点

# 弹簧刚度值（单位：kN/m）
Kx = 1000000   # X 方向弹簧刚度
Ky = 1000000   # Y 方向弹簧刚度
Kz = 5000000   # Z 方向弹簧刚度（竖向刚度大）

# === 用 for 循环生成弹簧数据 ===
spring_assign = {}
for idx, node_id in enumerate(pier_top_nodes, start=1):
    # enumerate(列表, start=1) 同时遍历列表元素和序号
    # idx 从 1 开始递增，node_id 是列表中的节点编号

    spring_assign[str(idx)] = {
        "ITEMS": [node_id],         # 这个弹簧作用的节点
        "GROUP_NAME": "弹簧支座",
        "SDx": Kx,                  # X 方向弹簧刚度
        "SDy": Ky,                  # Y 方向弹簧刚度
        "SDz": Kz                   # Z 方向弹簧刚度
        # 注意：这个例子只是一个示意，具体参数名请参考 API 文档
    }

spring_data = {"Assign": spring_assign}

print("生成的弹簧约束数据：")
print(json.dumps(spring_data, indent=2, ensure_ascii=False))
print(f"\\n循环逻辑：用 enumerate 给 {len(pier_top_nodes)} 个节点各配一个弹簧")
print("idx 从 1 开始递增，node_id 是实际的节点编号")
'''
    return content


def gen_run_analysis_script(kb):
    """Generate 04_run_analysis.py — OPE section examples."""
    content = HEADER.format(title="04 运行分析 —— 执行计算命令")
    content += '''
import json

# ============================================================
# OPE 部分 —— 操作和分析命令
# ============================================================
#
# OPE 接口用于执行操作：划分单元、计算截面特性、运行分析等。
# 和 DOC/DB 不同的是，有些 OPE 接口用 GET 方法（只查询不用发数据）。

# ============================================================
# 示例 1：查询项目状态（GET 请求）
# ============================================================
# 接口：/ope/PROJECTSTATUS
# 方法：GET
# 作用：查看当前项目的信息（不修改任何数据）

print("\\n>>> 示例 1：查询项目状态")

# GET 请求不需要发 JSON 数据
response = requests.get(
    f"{BASE_URL}/ope/PROJECTSTATUS",
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    status_data = response.json()
    print("项目状态信息：")
    print(json.dumps(status_data, indent=2, ensure_ascii=False))
else:
    print(f"查询失败：{response.text}")

# ============================================================
# 示例 2：划分单元
# ============================================================
# 接口：/ope/DIVIDEELEM
# 作用：把选中的单元按指定方式划分（等分、按长度等）

print("\\n>>> 示例 2：划分单元")

# 说明：以下 JSON 结构是示意性的
# 实际使用时请根据 MIDAS API 文档的具体参数名调整
divide_data = {
    "Argument": {
        "TARGETS": [5, 6, 7],     # 要划分的单元编号列表
        "DIVIDE": {
            "TYPE": "UNIFORM",     # 均匀划分
            "NUMBER": 4            # 每个单元分成 4 段
        },
        "START_NUMBER": {
            "NODE_NUMBER": 100,    # 新节点的起始编号
            "ELEM_NUMBER": 200     # 新单元的起始编号
        }
    }
}

print("要发送的 JSON：")
print(json.dumps(divide_data, indent=2, ensure_ascii=False))
print("\\nJSON 层级说明：")
print("  第 1 层：Argument → 命令参数容器")
print("  第 2 层：TARGETS, DIVIDE, START_NUMBER")
print("  第 3 层：DIVIDE.TYPE, DIVIDE.NUMBER → 划分方式的具体参数")

response = requests.post(
    f"{BASE_URL}/ope/DIVIDEELEM",
    json=divide_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("单元划分完成！")
else:
    print(f"划分失败：{response.text}")
'''
    return content


def gen_extract_results_script(kb):
    """Generate 05_extract_results.py — POST section examples."""
    content = HEADER.format(title="05 提取结果 —— 读取分析结果数据")
    content += '''
import json

# ============================================================
# POST 部分 —— 后处理和结果提取
# ============================================================
#
# POST 接口用于提取分析结果：内力、位移、应力、反力等。
# 这些接口帮你把 MIDAS 的计算结果读到 Python 里做进一步处理。
#
# 和 DB 接口不同，POST 接口的数据结构通常是：
# {
#   "Argument": {
#     "TABLE_NAME": "...",     ← 结果表名称
#     "TABLE_TYPE": "...",     ← 结果类型（如 "ELEMENTWEIGHT"）
#     "EXPORT_PATH": "...",    ← 导出路径（可选）
#     ...
#   }
# }

# ============================================================
# 示例 1：提取单元重量表
# ============================================================

print("\\n>>> 示例 1：提取单元重量表")

weight_data = {
    "Argument": {
        "TABLE_NAME": "element_weight",   # 表名称
        "TABLE_TYPE": "ELEMENTWEIGHT",    # 表类型（必须是 MIDAS 定义的值）
        "EXPORT_PATH": ""                 # 留空 = 不导出文件，只在内存中返回
    }
}

print("要发送的 JSON：")
print(json.dumps(weight_data, indent=2, ensure_ascii=False))
print("\\n理解这个 JSON：")
print("  Argument 里面是查询条件 —— 告诉 MIDAS 你要哪张表的数据")
print("  TABLE_TYPE 必须是 MIDAS 预定义的类型名，不能随便写")

response = requests.post(
    f"{BASE_URL}/post/PM",
    json=weight_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    result = response.json()
    print("结果返回成功！")
    print("返回的数据结构：")
    print(json.dumps(result, indent=2, ensure_ascii=False)[:500])  # 只显示前 500 字符
    print("...(数据太长，只显示前 500 个字符)")
else:
    print(f"提取失败：{response.text}")

# ============================================================
# 示例 2：提取节点位移结果
# ============================================================

print("\\n>>> 示例 2：提取节点位移")

displacement_data = {
    "Argument": {
        "TABLE_NAME": "node_displacement",
        "TABLE_TYPE": "NODISPLACEMENT",
        "EXPORT_PATH": "C:/MIDAS/displacement_results.txt"
        # ↑ 指定导出路径，MIDAS 会把结果写成文件
    }
}

print("要发送的 JSON：")
print(json.dumps(displacement_data, indent=2, ensure_ascii=False))

response = requests.post(
    f"{BASE_URL}/post/PM",
    json=displacement_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("位移结果提取成功！")
    print("结果已导出到 C:/MIDAS/displacement_results.txt")
else:
    print(f"提取失败：{response.text}")

# ============================================================
# 示例 3：用循环提取多个工况的结果
# ============================================================

print("\\n>>> 示例 3：批量提取多个工况的结果")

# 假设我们有这些荷载工况
load_cases = ["自重", "二期恒载", "活载-车道1", "活载-车道2", "温度-升温"]

# === 用 for 循环逐个工况提取 ===
results = {}  # 空字典，用来存储每个工况的结果

for lc_name in load_cases:
    # lc_name 是循环变量，每轮取一个荷载工况名
    print(f"正在提取工况：{lc_name}")

    data = {
        "Argument": {
            "TABLE_NAME": lc_name,       # 用循环变量作为表名
            "TABLE_TYPE": "RESULT",      # 结果类型
            "EXPORT_PATH": f"C:/MIDAS/{lc_name}.txt"
            # f"..." 是 f-string，花括号里的变量会被替换成实际值
            # 例如 {lc_name} → "自重" → 路径变成 "C:/MIDAS/自重.txt"
        }
    }

    response = requests.post(
        f"{BASE_URL}/post/PM",
        json=data,
        verify=False
    )

    if response.status_code == 200:
        results[lc_name] = response.json()
        print(f"  {lc_name} 提取成功")
    else:
        print(f"  {lc_name} 提取失败：{response.text}")

print(f"\\n批量提取完成！共处理 {len(load_cases)} 个工况")
print(f"成功提取 {len(results)} 个工况的结果")

# ============================================================
# 总结：结果提取学到的
# ============================================================
# 1. POST 接口使用 {"Argument": {...}} 结构传递查询参数
# 2. TABLE_TYPE 必须是 MIDAS 预定义的值（参考 API 文档）
# 3. EXPORT_PATH 指定导出文件路径，留空则只在内存中返回
# 4. for 循环可以批量提取多个工况的结果
# 5. f-string (f"...{变量}...") 是一种方便的字符串拼接方式
'''
    return content


def gen_view_control_script(kb):
    """Generate 06_view_control.py — VIEW section examples."""
    content = HEADER.format(title="06 视图控制 —— 选择和截图")
    content += '''
import json

# ============================================================
# VIEW 部分 —— 视图控制和截图
# ============================================================

# ============================================================
# 示例 1：选择对象
# ============================================================
# 接口：/view/SELECT
# 方法：GET
# 作用：获取当前选中的节点和单元列表

print("\\n>>> 示例 1：查询当前选中对象")

response = requests.get(
    f"{BASE_URL}/view/SELECT",
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    sel = response.json()
    print("当前选中的对象：")
    print(json.dumps(sel, indent=2, ensure_ascii=False))
else:
    print(f"查询失败：{response.text}")

# ============================================================
# 示例 2：截图
# ============================================================
# 接口：/view/CAPTURE
# 作用：截取当前视图窗口并保存为图片

print("\\n>>> 示例 2：截图保存")

capture_data = {
    "Argument": {
        "FIGURE_NAME": "my_screenshot",        # 图片文件名（不含扩展名）
        "EXPORT_PATH": "C:/MIDAS/screenshots", # 导出文件夹
        "WIDTH": 1920,                         # 图片宽度（像素）
        "HEIGHT": 1080,                        # 图片高度（像素）
        "SET_HIDDEN": False                    # 是否隐藏被遮挡的线
    }
}

print("要发送的 JSON：")
print(json.dumps(capture_data, indent=2, ensure_ascii=False))

response = requests.post(
    f"{BASE_URL}/view/CAPTURE",
    json=capture_data,
    verify=False
)

print(f"响应状态码：{response.status_code}")
if response.status_code == 200:
    print("截图已保存到 C:/MIDAS/screenshots/my_screenshot.png")
else:
    print(f"截图失败：{response.text}")

# ============================================================
# 示例 3：批量截图多个视角
# ============================================================

print("\\n>>> 示例 3：批量截图不同视角")

# 定义要截图的视角和文件名
views = [
    {"name": "立面图",   "stage": "立面"},
    {"name": "平面图",   "stage": "平面"},
    {"name": "侧面图",   "stage": "侧面"},
    {"name": "三维视图", "stage": "3D"},
]

for view in views:
    # view 是一个 dict，包含 name 和 stage 两个键
    view_name = view["name"]   # 取出视角名称
    stage = view["stage"]      # 取出 STAGE_NAME

    print(f"正在截图：{view_name}（STAGE_NAME={stage}）")

    data = {
        "Argument": {
            "FIGURE_NAME": view_name,
            "EXPORT_PATH": "C:/MIDAS/screenshots",
            "WIDTH": 1920,
            "HEIGHT": 1080,
            "STAGE_NAME": stage  # 用循环变量设置视角
        }
    }

    response = requests.post(
        f"{BASE_URL}/view/CAPTURE",
        json=data,
        verify=False
    )

    if response.status_code == 200:
        print(f"  {view_name} 截图完成")
    else:
        print(f"  {view_name} 截图失败")

print(f"\\n共截图 {len(views)} 张，保存在 C:/MIDAS/screenshots/")
'''
    return content


def gen_utils_module():
    """Generate utils.py — shared helper functions."""
    content = '''"""
MIDAS API 工具函数
===================
把这些常用的功能打包成函数，方便在多个脚本中重复使用。

使用方法：
    from utils import post_to_midas, get_from_midas, create_nodes, create_materials
"""

import requests
import urllib3
import json

urllib3.disable_warnings()

# 默认连接设置
BASE_URL = "https://127.0.0.1:1102"


def set_base_url(url):
    """修改 MIDAS 服务地址（如果你的端口不是 1102）"""
    global BASE_URL
    BASE_URL = url


# ============================================================
# 基础函数 —— 封装 HTTP 请求
# ============================================================

def post_to_midas(path, data):
    """
    向 MIDAS 发送 POST 请求。

    参数：
        path: API 路径，如 "/db/NODE"、"/doc/NEW"
        data: Python 字典（会自动转成 JSON）

    返回：
        MIDAS 的响应数据（Python 字典），失败返回 None

    例子：
        result = post_to_midas("/db/NODE", {"Assign": {"1": {"X": 0, "Y": 0, "Z": 0}}})
    """
    url = f"{BASE_URL}{path}"
    try:
        response = requests.post(url, json=data, verify=False, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"错误：{path} 返回状态码 {response.status_code}")
            print(f"  信息：{response.text}")
            return None
    except requests.exceptions.ConnectionError:
        print(f"错误：无法连接到 MIDAS（{BASE_URL}）")
        print("  请确认 MIDAS 已启动并加载了项目。")
        return None
    except Exception as e:
        print(f"错误：{e}")
        return None


def get_from_midas(path):
    """
    向 MIDAS 发送 GET 请求。

    参数：
        path: API 路径，如 "/view/SELECT"

    返回：
        MIDAS 的响应数据（Python 字典），失败返回 None
    """
    url = f"{BASE_URL}{path}"
    try:
        response = requests.get(url, verify=False, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"错误：{path} 返回状态码 {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print(f"错误：无法连接到 MIDAS（{BASE_URL}）")
        return None
    except Exception as e:
        print(f"错误：{e}")
        return None


# ============================================================
# 高级函数 —— 封装常用建模操作
# ============================================================

def create_nodes(nodes_dict):
    """
    批量创建节点。

    参数：
        nodes_dict: {
            "1": {"X": 0, "Y": 0, "Z": 0},
            "2": {"X": 5000, "Y": 0, "Z": 0},
            ...
        }

    返回：
        MIDAS 的响应数据，失败返回 None

    例子：
        nodes = {}
        for i in range(10):
            nodes[str(i+1)] = {"X": i*1000, "Y": 0, "Z": 0}
        create_nodes(nodes)
    """
    return post_to_midas("/db/NODE", {"Assign": nodes_dict})


def create_materials(materials_dict):
    """
    批量创建材料。

    参数：
        materials_dict: {
            "1": {"TYPE": "CONC", "NAME": "C50", "PARAM": {...}},
            "2": {"TYPE": "STEEL", "NAME": "Q345", "PARAM": {...}},
        }

    返回：
        MIDAS 的响应数据
    """
    return post_to_midas("/db/MATL", {"Assign": materials_dict})


def make_linear_nodes(start_x, end_x, num, y=0, z=0):
    """
    生成一排等间距节点的数据字典（不发送）。

    参数：
        start_x: 起点 X 坐标
        end_x: 终点 X 坐标
        num: 节点数量
        y: Y 坐标（默认 0）
        z: Z 坐标（默认 0）

    返回：
        {"1": {"X": ..., "Y": ..., "Z": ...}, "2": {...}, ...}

    例子：
        nodes = make_linear_nodes(0, 10000, 11, y=0, z=0)
        create_nodes(nodes)
    """
    nodes = {}
    for i in range(num):
        # 线性插值计算 X 坐标
        x = start_x + (end_x - start_x) * i / (num - 1) if num > 1 else start_x
        nodes[str(i + 1)] = {"X": x, "Y": y, "Z": z}
    return nodes


def make_grid_nodes(x0, y0, nx, ny, dx, dy, z=0):
    """
    生成二维网格节点（平面正交网格）。

    参数：
        x0, y0: 起始点坐标
        nx, ny: X 和 Y 方向的节点数
        dx, dy: X 和 Y 方向的间距
        z: Z 坐标（默认 0）

    返回：
        {"1": {"X": ..., "Y": ..., "Z": ...}, "2": {...}, ...}

    例子：
        # 生成 5x4 的网格，间距 2000mm
        nodes = make_grid_nodes(0, 0, nx=5, ny=4, dx=2000, dy=2000)
        create_nodes(nodes)
    """
    nodes = {}
    node_id = 1
    for j in range(ny):
        for i in range(nx):
            nodes[str(node_id)] = {
                "X": x0 + i * dx,
                "Y": y0 + j * dy,
                "Z": z
            }
            node_id += 1
    return nodes


def new_project():
    """新建项目。"""
    return post_to_midas("/doc/NEW", {"Argument": {}})


def save_project(filepath):
    """保存项目。"""
    return post_to_midas("/doc/SAVEAS", {"Argument": filepath})


def close_project():
    """关闭项目。"""
    return post_to_midas("/doc/CLOSE", {"Argument": {}})


# ============================================================
# 使用示例（运行这个文件可以看到效果）
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("MIDAS API 工具函数测试")
    print("=" * 50)

    # 测试连接
    print("\\n测试连接...")
    result = get_from_midas("/ope/PROJECTSTATUS")
    if result:
        print("连接成功！")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("连接失败。请确保 MIDAS 已启动。")

    # 演示 make_linear_nodes
    print("\\n演示 make_linear_nodes：")
    print("输入: start_x=0, end_x=10000, num=5")
    nodes = make_linear_nodes(0, 10000, 5)
    print("输出:")
    print(json.dumps(nodes, indent=2, ensure_ascii=False))

    # 演示 make_grid_nodes
    print("\\n演示 make_grid_nodes：")
    print("输入: x0=0, y0=0, nx=3, ny=2, dx=2000, dy=3000")
    grid = make_grid_nodes(0, 0, nx=3, ny=2, dx=2000, dy=3000)
    print("输出:")
    print(json.dumps(grid, indent=2, ensure_ascii=False))
'''
    return content


def gen_readme():
    """Generate README for code examples."""
    return '''# MIDAS API 代码示例

> 面向工程师的 Python API 调用示例 —— 每个脚本都可以单独运行。

## 文件说明

| 文件 | 内容 | 适合谁 |
|------|------|--------|
| `utils.py` | 工具函数库（封装了常用操作） | **所有人先读这个** |
| `01_project_management.py` | 新建、保存、关闭项目 | 第一次用 API |
| `02_create_model.py` | 创建节点、单元、材料、截面 | 需要自动化建模 |
| `03_apply_loads.py` | 施加边界条件和荷载 | 需要批量加载 |
| `04_run_analysis.py` | 执行分析和操作命令 | 需要自动化分析 |
| `05_extract_results.py` | 提取分析结果数据 | 需要批量出结果 |
| `06_view_control.py` | 选择对象和截图 | 需要自动截图 |

## 怎么用？

1. 确保 MIDAS 已打开并加载了项目
2. 安装 Python 依赖：`pip install requests urllib3`
3. 从 `01_project_management.py` 开始，逐个运行
4. **不要一次全运行** —— 每个脚本会修改你的模型

## Python 零基础？

建议先花 5 分钟看 `../teaching/appendix/json-basics.md` 了解 JSON 基础。

## 代码风格

所有代码遵循以下原则：
- 只使用最基础的 Python 语法（dict, list, for, if, def）
- 每个操作都有中文注释
- 循环逻辑单独解释
- JSON 结构和生成过程都有说明
- 不使用 lambda、生成器、装饰器、类等高阶语法
'''

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Reading knowledge base...")
    kb = load_kb(KB_PATH)

    os.makedirs(OUT_DIR, exist_ok=True)

    generators = [
        ("01_project_management.py", gen_project_management_script),
        ("02_create_model.py", gen_create_model_script),
        ("03_apply_loads.py", gen_apply_loads_script),
        ("04_run_analysis.py", gen_run_analysis_script),
        ("05_extract_results.py", gen_extract_results_script),
        ("06_view_control.py", gen_view_control_script),
    ]

    for filename, gen_func in generators:
        print(f"Generating {filename}...")
        content = gen_func(kb)
        filepath = os.path.join(OUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print("Generating utils.py...")
    with open(os.path.join(OUT_DIR, "utils.py"), "w", encoding="utf-8") as f:
        f.write(gen_utils_module())

    print("Generating README.md...")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(gen_readme())

    # Count lines
    total = 0
    for f in os.listdir(OUT_DIR):
        if f.endswith(".py") or f.endswith(".md"):
            filepath = os.path.join(OUT_DIR, f)
            with open(filepath, "r", encoding="utf-8") as fp:
                lines = len(fp.readlines())
            print(f"  {f}: {lines} lines")
            total += lines

    print(f"\nDone! {total} total lines in '{OUT_DIR}/'")


if __name__ == "__main__":
    main()
