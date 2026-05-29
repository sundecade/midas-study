"""
MIDAS API 调用示例 —— 06 视图控制（选择与截图）
============================================
查询选中对象 → 截图 → 批量截图不同视角

运行前提：MIDAS Civil 已启动并加载了项目
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import auto_config, manual_config, MidasAPI

print("=" * 60)
print("06 视图控制 —— 选择与截图")
print("=" * 60)

config = auto_config()
if config is None:
    config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")

import json

# ═══════════════════════════════════════════════════════════════
# 第 1 步：查询当前选中对象
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 1 步：查询当前选中对象")

result = MidasAPI("GET", "/view/SELECT", config=config)
if result:
    print("当前选中的节点和单元：")
    print(json.dumps(result, indent=2, ensure_ascii=False))
else:
    print("查询失败（可能未选中任何对象）")

# ═══════════════════════════════════════════════════════════════
# 第 2 步：截图当前视图
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 2 步：截图当前视图")

capture_data = {
    "Argument": {
        "FIGURE_NAME": "current_view",
        "EXPORT_PATH": "C:/MIDAS/screenshots",
        "WIDTH": 1920,
        "HEIGHT": 1080,
    }
}

result = MidasAPI("POST", "/view/CAPTURE", body=capture_data, config=config)
if result:
    print("截图已保存到 C:/MIDAS/screenshots/current_view.png")
else:
    print("截图失败")

# ═══════════════════════════════════════════════════════════════
# 第 3 步：批量截图不同视角
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 3 步：批量截图不同视角")

views = [
    {"name": "立面图",   "stage": "立面"},
    {"name": "平面图",   "stage": "平面"},
    {"name": "侧面图",   "stage": "侧面"},
    {"name": "三维视图", "stage": "3D"},
]

for view in views:
    print(f"  正在截图：{view['name']}...")
    data = {
        "Argument": {
            "FIGURE_NAME": view["name"],
            "EXPORT_PATH": "C:/MIDAS/screenshots",
            "WIDTH": 1920,
            "HEIGHT": 1080,
            "STAGE_NAME": view["stage"],
        }
    }
    result = MidasAPI("POST", "/view/CAPTURE", body=data, config=config)
    status = "完成" if result else "失败"
    print(f"    {view['name']} — {status}")

print(f"\n共截图 {len(views)} 张，保存在 C:/MIDAS/screenshots/")

# ═══════════════════════════════════════════════════════════════
# 第 4 步：选中指定节点
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 4 步：选中指定节点")

select_data = {
    "Argument": {
        "NODE_LIST": [1, 5, 10],
    }
}

result = MidasAPI("POST", "/view/SELECT", body=select_data, config=config)
if result:
    print("已选中节点 1, 5, 10")
    # 验证选中结果
    sel = MidasAPI("GET", "/view/SELECT", config=config)
    if sel:
        nodes = sel.get("NODE_LIST", []) if isinstance(sel, dict) else sel
        print(f"确认选中节点：{nodes}")
else:
    print("选择节点失败")

print("\n" + "=" * 60)
print("视图控制完成！")
print("=" * 60)
