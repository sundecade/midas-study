"""
测试脚本：根据端点路径或关键词，查看正确的 JSON 格式。

用法：
  PYTHONUTF8=1 python test_endpoint.py /db/CONS          # 精确路径
  PYTHONUTF8=1 python test_endpoint.py 约束               # 关键词搜索
  PYTHONUTF8=1 python test_endpoint.py --list             # 列出所有端点
  PYTHONUTF8=1 python test_endpoint.py --section DB       # 列出某分类
"""
import json
import os
import sys

KB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "midas_api_knowledge_base.json")


def load_kb():
    with open(KB, "r", encoding="utf-8") as f:
        return json.load(f)


def find_endpoint(kb, query):
    """精确路径匹配或关键词搜索"""
    results = []

    for sec_name, sec_data in kb["api_data"].items():
        # 直接端点
        for ep_path, ep_data in sec_data.get("endpoints", {}).items():
            if _match(ep_path, ep_data, query, sec_name, ""):
                results.append((ep_path, ep_data, sec_name, ""))

        # 子分类端点
        for sub_name, sub_data in sec_data.get("subsections", {}).items():
            for ep_path, ep_data in sub_data.items():
                if _match(ep_path, ep_data, query, sec_name, sub_name):
                    results.append((ep_path, ep_data, sec_name, sub_name))

    return results


def _match(ep_path, ep_data, query, sec_name, sub_name):
    query_lower = query.lower()
    return (
        query_lower in ep_path.lower()
        or query_lower in ep_data.get("api_name", "").lower()
        or query_lower in sub_name.lower()
        or query_lower in sec_name.lower()
    )


def show_endpoint(ep_path, ep_data, sec_name, sub_name):
    """展示端点的完整信息"""
    t = ep_data.get("request_templates", {})
    guide = ep_data.get("request_field_guide", {})

    print("=" * 65)
    print(f"端点: {ep_path}")
    print(f"名称: {ep_data.get('api_name', '?')}")
    print(f"位置: {sec_name}" + (f" > {sub_name}" if sub_name else ""))
    print(f"方法: {', '.join(ep_data.get('http_method', []))}")
    print(f"URL:  {ep_data.get('url', '?')}")
    print()

    # 包装规则
    wrapper_info = t.get("_wrapper_info", "")
    if wrapper_info:
        print(">>> 强制结构规则 <<<")
        print(wrapper_info)
        print()

    # 各方法模板
    for method in ["POST", "GET", "PUT", "DELETE"]:
        if method in t:
            print(f">>> {method} 请求模板 <<<")
            print(json.dumps(t[method], indent=2, ensure_ascii=False))
            note = t.get(f"{method}_note", "")
            if note:
                print(f"  ⚠ {note}")
            print()

    # 字段指南
    if guide:
        print(">>> 字段说明 <<<")
        print(f"{'字段':<25} {'必填':<6} {'类型':<20} {'说明'}")
        print("-" * 90)
        for key, info in guide.items():
            req = "必填" if info["required"] else "可选"
            dtype = info.get("type", "?")
            desc = (info.get("desc") or "")[:60]
            print(f"{key:<25} {req:<6} {dtype:<20} {desc}")
        print()


def list_all(kb, section=None):
    """列出所有端点"""
    for sec_name, sec_data in kb["api_data"].items():
        if section and section.upper() != sec_name:
            continue
        print(f"\n{'=' * 20} {sec_name} {'=' * 20}")

        for ep_path, ep_data in sec_data.get("endpoints", {}).items():
            methods = ",".join(ep_data.get("http_method", []))
            print(f"  {ep_path:<40} [{methods}] {ep_data.get('api_name', '')}")

        for sub_name, sub_data in sec_data.get("subsections", {}).items():
            print(f"  --- {sub_name} ---")
            for ep_path, ep_data in sub_data.items():
                methods = ",".join(ep_data.get("http_method", []))
                print(f"    {ep_path:<38} [{methods}] {ep_data.get('api_name', '')}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    arg = sys.argv[1]

    kb = load_kb()

    if arg == "--list":
        section = sys.argv[2] if len(sys.argv) > 2 else None
        list_all(kb, section)
        return

    results = find_endpoint(kb, arg)

    if not results:
        print(f"未找到与 '{arg}' 匹配的端点")
        print("尝试: PYTHONUTF8=1 python test_endpoint.py --list")
        return

    for ep_path, ep_data, sec_name, sub_name in results:
        show_endpoint(ep_path, ep_data, sec_name, sub_name)

    print(f"共找到 {len(results)} 个匹配端点")


if __name__ == "__main__":
    main()
