"""
MIDAS API 调用示例 —— 02 创建模型 —— 单位→材料→截面→节点→单元
============================================
建模顺序（重要！）：单位系统 → 材料 → 截面 → 节点 → 单元

运行前提：
  1. MIDAS Civil 已启动并加载了项目
  2. Python 3 已安装
  3. pip install requests
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import auto_config, manual_config, MidasAPI, create_nodes

print("=" * 60)
print("02 创建模型 —— 单位、材料、截面、节点、单元")
print("=" * 60)

# ── 获取配置 ──
config = auto_config()
if config is None:
    config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")

# ═══════════════════════════════════════════════════════════════
# 第 0 步：设置单位系统（新建项目后第一步！）
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 0 步：设置单位系统")

# 设置 kN/m 单位制（常用桥梁/建筑单位）
unit_data = {
    "Assign": {
        "1": {
            "FORCE": "KN",      # 力：千牛
            "LENGTH": "M",      # 长度：米
            "HEAT": "KCAL",     # 热量：千卡
            "TEMP": "C",        # 温度：摄氏度
        }
    }
}
result = MidasAPI("POST", "/db/UNIT", body=unit_data, config=config)
print("单位系统设置" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 1 步：定义材料（使用标准规范 JTG3362-18）
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 1 步：定义材料")

# C50 混凝土（编号 1）— 使用 JTG3362-18(RC) 标准
mat_concrete = {
    "Assign": {
        "1": {
            "TYPE": "CONC",
            "NAME": "C50",
            "PARAM": {
                "PRI": 1,                          # 材料方向
                "CODE": "GB",                      # 中国规范
                "P_TYPE": "1",                     # 1=使用标准规范
                "STANDARD": "JTG3362-18(RC)",      # 混凝土标准
                "DB": "C50",                       # 混凝土等级
                "bELAST": 0,                       # 0=非弹性(考虑非线性)
            }
        }
    }
}
result = MidasAPI("POST", "/db/MATL", body=mat_concrete, config=config)
print("C50 混凝土创建" + ("成功" if result else "失败"))

# Q345 钢材（编号 2）— 使用 JTG3362-18(S) 标准
mat_steel = {
    "Assign": {
        "2": {
            "TYPE": "STEEL",
            "NAME": "Q345",
            "PARAM": {
                "PRI": 1,                          # 材料方向
                "CODE": "GB12",                    # 中国规范(钢结构)
                "P_TYPE": "1",                     # 1=使用标准规范
                "STANDARD": "JTG3362-18(S)",       # 钢材标准
                "DB": "Q345",                      # 钢材等级
            }
        }
    }
}
result = MidasAPI("POST", "/db/MATL", body=mat_steel, config=config)
print("Q345 钢材创建" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 2 步：定义截面
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 2 步：定义截面")

# 矩形截面 0.3m × 0.5m（编号 1，使用材料 1 = C50）
section_beam = {
    "Assign": {
        "1": {
            "NAME": "Beam300x500",
            "MATERIAL": 1,
            "SHAPE": "RECT",       # 矩形
            "PARAM": {
                "H": 0.5,          # 高度 0.5m
                "B": 0.3,          # 宽度 0.3m
            }
        }
    }
}
result = MidasAPI("POST", "/db/SECT", body=section_beam, config=config)
print("矩形截面创建" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 3 步：创建节点
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 3 步：创建节点")

# 方法A：手动指定每个节点坐标
nodes_manual = {
    "Assign": {
        "1": {"X": 0,     "Y": 0, "Z": 0},
        "2": {"X": 3000,  "Y": 0, "Z": 0},
        "3": {"X": 6000,  "Y": 0, "Z": 0},
        "4": {"X": 9000,  "Y": 0, "Z": 0},
        "5": {"X": 12000, "Y": 0, "Z": 0},
    }
}
result = MidasAPI("POST", "/db/NODE", body=nodes_manual, config=config)
print("手动创建 5 个节点" + ("成功" if result else "失败"))

# 方法B：用循环批量创建节点（更高效）
print("\n用循环批量创建更多节点...")
nodes_batch = {}
for i in range(6, 21):  # 创建节点 6~20
    x = (i - 1) * 1000  # 间距 1000mm
    nodes_batch[str(i)] = {"X": x, "Y": 0, "Z": 0}

result = MidasAPI("POST", "/db/NODE", body={"Assign": nodes_batch}, config=config)
print(f"批量创建 {len(nodes_batch)} 个节点" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 4 步：创建单元（连接节点）
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 4 步：创建单元")

# 创建梁单元：节点1-2形成单元1，节点2-3形成单元2，以此类推
elements = {}
for i in range(1, 5):  # 创建 4 个单元
    elements[str(i)] = {
        "TYPE": "BEAM",        # 梁单元
        "MATERIAL": 1,         # 材料编号 1（C50）
        "SECTION": 1,          # 截面编号 1
        "NODE_LIST": [i, i + 1],  # 起始节点和终止节点
    }

result = MidasAPI("POST", "/db/ELEM", body={"Assign": elements}, config=config)
print(f"创建 {len(elements)} 个梁单元" + ("成功" if result else "失败"))

print("\n" + "=" * 60)
print("模型创建完成！建模顺序：材料 → 截面 → 节点 → 单元")
print("=" * 60)
