"""
MIDAS API 调用示例 —— 05 批量建模与结果提取
============================================
用循环批量创建模型 → 运行分析 → 提取结果

运行前提：MIDAS Civil 已启动并加载了项目
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import auto_config, manual_config, MidasAPI

print("=" * 60)
print("05 批量建模与结果提取")
print("=" * 60)

config = auto_config()
if config is None:
    config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")

# ═══════════════════════════════════════════════════════════════
# 第 1 步：批量创建材料
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 1 步：批量创建材料")

materials = {}
for i, (name, db) in enumerate([
    ("C50", "C50"),
    ("Q345", "Q345"),
    ("C40", "C40"),
], start=1):
    materials[str(i)] = {
        "TYPE": "CONC" if name.startswith("C") else "STEEL",
        "NAME": name,
        "PARAM": {
            "PRI": 1,
            "CODE": "GB" if name.startswith("C") else "GB12",
            "DB": db,
        } if name.startswith("C") else {
            "PRI": 1,
            "CODE": "GB12",
            "DB": db,
        }
    }

result = MidasAPI("POST", "/db/MATL", body={"Assign": materials}, config=config)
print(f"批量创建 {len(materials)} 个材料" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 2 步：批量创建截面
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 2 步：批量创建截面")

sections = {}
section_specs = [
    ("RECT", "Beam300x500", {"H": 0.5, "B": 0.3}),
    ("RECT", "Beam400x600", {"H": 0.6, "B": 0.4}),
    ("CIRC", "ColD500",     {"D": 0.5}),
]
for i, (shape, name, params) in enumerate(section_specs, start=1):
    sections[str(i)] = {
        "NAME": name,
        "MATERIAL": 1,
        "SHAPE": shape,
        "PARAM": params,
    }

result = MidasAPI("POST", "/db/SECT", body={"Assign": sections}, config=config)
print(f"批量创建 {len(sections)} 个截面" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 3 步：批量创建节点
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 3 步：批量创建节点")

# 用循环生成节点坐标：一行 10 个，间距 2000mm
nodes = {}
for i in range(1, 21):
    nodes[str(i)] = {
        "X": (i - 1) * 2000,
        "Y": 0,
        "Z": 0,
    }

result = MidasAPI("POST", "/db/NODE", body={"Assign": nodes}, config=config)
print(f"批量创建 {len(nodes)} 个节点" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 4 步：批量创建单元
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 4 步：批量创建单元")

elements = {}
for i in range(1, 20):
    elements[str(i)] = {
        "TYPE": "BEAM",
        "MATERIAL": 1,
        "SECTION": 1,
        "NODE_LIST": [i, i + 1],
    }

result = MidasAPI("POST", "/db/ELEM", body={"Assign": elements}, config=config)
print(f"批量创建 {len(elements)} 个梁单元" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 5 步：施加边界条件
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 5 步：施加边界条件")

support = {
    "Assign": {
        "1": {
            "NODE_LIST": [1],
            "DOF": {"Dx": 1, "Dy": 1, "Dz": 1, "Rx": 1, "Ry": 1, "Rz": 1},
        },
        "2": {
            "NODE_LIST": [20],
            "DOF": {"Dx": 1, "Dy": 1, "Dz": 1, "Rx": 0, "Ry": 0, "Rz": 0},
        }
    }
}
MidasAPI("POST", "/db/CONS", body=support, config=config)

# ═══════════════════════════════════════════════════════════════
# 第 6 步：施加荷载
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 6 步：施加荷载")

# 荷载工况
load_case = {
    "Assign": {
        "1": {"NAME": "DEAD", "TYPE": "DEAD"},
        "2": {"NAME": "LIVE", "TYPE": "USER"},
    }
}
MidasAPI("POST", "/db/BODF", body=load_case, config=config)

# 梁单元均布荷载（所有单元）
beam_load = {
    "Assign": {
        "1": {
            "ELEM_LIST": list(range(1, 20)),
            "LCNAME": "DEAD",
            "LOADTYPE": "UDL",
            "FORCE": {"FZ": -15000},
        }
    }
}
MidasAPI("POST", "/db/BMLD", body=beam_load, config=config)
print("荷载施加完成")

# ═══════════════════════════════════════════════════════════════
# 第 7 步：运行分析
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 7 步：运行分析")

result = MidasAPI("POST", "/doc/ANAL", body={"Argument": {}}, config=config)
if result:
    print("分析已提交，等待计算完成...")
    import time
    time.sleep(3)
    print("分析执行完毕")
else:
    print("分析提交失败")
    exit(1)

# ═══════════════════════════════════════════════════════════════
# 第 8 步：批量提取结果
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 8 步：批量提取结果")

result_types = [
    ("/post/DISPLACEMENTS", "位移"),
    ("/post/BEAM_FORCES",   "梁内力"),
    ("/post/REACTIONS",     "反力"),
]

import json
all_results = {}
for path, label in result_types:
    result = MidasAPI("GET", path, config=config)
    if result:
        all_results[label] = result
        print(f"  {label} — 提取成功")
    else:
        print(f"  {label} — 提取失败")

# 打印位移结果摘要
if "位移" in all_results:
    disp = all_results["位移"]
    output = json.dumps(disp, indent=2, ensure_ascii=False)
    print(f"\n位移结果（前 600 字符）:")
    print(output[:600])

print("\n" + "=" * 60)
print(f"完成！共提取 {len(all_results)} 类结果")
print("=" * 60)
