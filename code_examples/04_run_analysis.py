"""
MIDAS API 调用示例 —— 04 运行分析和提取结果
============================================
运行分析后提取位移和内力结果。

运行前提：已完成建模和荷载施加
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import auto_config, manual_config, MidasAPI

print("=" * 60)
print("04 运行分析和提取结果")
print("=" * 60)

config = auto_config()
if config is None:
    config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")

# ═══════════════════════════════════════════════════════════════
# 第 1 步：运行分析
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 1 步：运行分析")

# 发送分析命令
result = MidasAPI("POST", "/doc/ANAL", body={"Argument": {}}, config=config)
if result:
    print("分析已提交，等待计算完成...")
    # 实际项目中需等待分析完成（通常几秒到几分钟）
    import time
    time.sleep(2)
    print("分析执行完毕")
else:
    print("分析提交失败，请检查模型")

# ═══════════════════════════════════════════════════════════════
# 第 2 步：提取节点位移
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 2 步：提取位移结果")

# GET 请求查询位移结果表格
result = MidasAPI("GET", "/post/DISPLACEMENTS", config=config)
if result:
    print("位移结果提取成功")
    import json
    # 只打印前 500 字符以便查看
    output = json.dumps(result, indent=2, ensure_ascii=False)
    print(output[:500])
else:
    print("位移结果提取失败")

# ═══════════════════════════════════════════════════════════════
# 第 3 步：使用循环批量提取多个工况
# ═══════════════════════════════════════════════════════════════
print("\n>>> 第 3 步：批量提取结果")

# 定义要查询的结果类型列表
result_types = [
    ("/post/DISPLACEMENTS", "位移"),
    ("/post/BEAM_FORCES",   "梁内力"),
    ("/post/REACTIONS",     "反力"),
]

for path, label in result_types:
    print(f"\n查询 {label} ({path})...")
    result = MidasAPI("GET", path, config=config)
    if result:
        print(f"  {label} — 查询成功")
    else:
        print(f"  {label} — 查询失败（可能需要确保分析已完成）")

print("\n" + "=" * 60)
print("结果提取完成！")
print("=" * 60)
