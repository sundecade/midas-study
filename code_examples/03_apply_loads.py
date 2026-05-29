"""
MIDAS API 调用示例 —— 03 施加边界条件和荷载
============================================
顺序：边界条件 → 荷载工况 → 施加荷载

运行前提：已完成建模（材料、截面、节点、单元）
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import auto_config, manual_config, MidasAPI

print("=" * 60)
print("03 施加边界条件和荷载")
print("=" * 60)

config = auto_config()
if config is None:
    config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")

# ═══════════════════════════════════════════════════════════════
# 第 1 步：施加边界条件（支座约束）
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 1 步：施加边界条件")

# 在节点 1 处设置固定支座（约束所有自由度）
# DOF: Dx=1,Dy=1,Dz=1,Rx=1,Ry=1,Rz=1 → 固定端
support = {
    "Assign": {
        "1": {
            "NODE_LIST": [1],        # 约束的节点列表
            "DOF": {
                "Dx": 1, "Dy": 1, "Dz": 1,   # 平动约束
                "Rx": 1, "Ry": 1, "Rz": 1,   # 转动约束
            }
        },
        "2": {
            "NODE_LIST": [5],        # 节点 5 为铰支座
            "DOF": {
                "Dx": 1, "Dy": 1, "Dz": 1,   # 约束平动
                "Rx": 0, "Ry": 0, "Rz": 0,   # 释放转动
            }
        }
    }
}
result = MidasAPI("POST", "/db/CONS", body=support, config=config)
print("边界条件施加" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 2 步：定义荷载工况
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 2 步：定义荷载工况")

load_case = {
    "Assign": {
        "1": {
            "NAME": "DEAD",     # 恒载工况
            "TYPE": "DEAD",     # 荷载类型：恒荷载
        },
        "2": {
            "NAME": "LIVE",     # 活载工况
            "TYPE": "USER",     # 荷载类型：活荷载
        }
    }
}
result = MidasAPI("POST", "/db/BODF", body=load_case, config=config)
print("荷载工况创建" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 3 步：施加节点荷载
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 3 步：施加节点荷载")

# 在节点 3 施加竖向集中力 100kN（LC=1 恒载）
nodal_load = {
    "Assign": {
        "1": {
            "NODE_LIST": [3],
            "LCNAME": "DEAD",
            "FORCE": {
                "FZ": -100000  # Z 方向 -100kN（向下）
            }
        }
    }
}
result = MidasAPI("POST", "/db/CNLD", body=nodal_load, config=config)
print("节点荷载施加" + ("成功" if result else "失败"))

# ═══════════════════════════════════════════════════════════════
# 第 4 步：施加梁单元荷载
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 4 步：施加梁单元荷载")

# 在所有梁单元上施加均布荷载 10kN/m（LC=2 活载）
beam_load = {
    "Assign": {
        "1": {
            "ELEM_LIST": [1, 2, 3, 4],  # 加载的单元列表
            "LCNAME": "LIVE",
            "LOADTYPE": "UDL",           # 均布荷载
            "FORCE": {
                "FZ": -10000,            # Z 方向 -10kN/m
            }
        }
    }
}
result = MidasAPI("POST", "/db/BMLD", body=beam_load, config=config)
print("梁单元荷载施加" + ("成功" if result else "失败"))

print("\n" + "=" * 60)
print("荷载施加完成！建模→加载→分析→提取结果")
print("=" * 60)
