"""
MIDAS API 命令行检索工具
========================
独立的命令行搜索工具，不依赖 Streamlit，可直接在终端使用或作为模块导入。

用途：
  1. 命令行搜索 API
  2. 作为 Python 模块导入到 AI 建模脚本中
  3. 批量导出搜索结果

用法：
  # 命令行搜索
  python search_cli.py "创建节点"
  python search_cli.py "施加荷载" --section DB --top 5
  python search_cli.py "提取位移" --format json

  # 查看接口详情
  python search_cli.py --detail /db/NODE

  # 列出所有章节
  python search_cli.py --list-sections

  # 作为模块使用
  from search_cli import search, get_endpoint, list_sections
  results = search("创建节点", top_k=5)
  for ep, score in results:
      print(ep["data"]["api_name"])

存储位置：
  此文件独立于 GUI，可复制到任何 AI 建模项目中使用。
  依赖：只需要同目录的 retriever.py 和知识库 JSON 文件。
"""

import sys
import os
import json
import argparse

# 自动推导知识库路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_KB_PATH = os.path.join(SCRIPT_DIR, "..", "midas_api_knowledge_base.json")

# 允许从外部指定知识库路径
KB_PATH = os.environ.get("MIDAS_KB_PATH", DEFAULT_KB_PATH)

_retriever = None


def _get_retriever():
    """延迟加载检索器（单例）。"""
    global _retriever
    if _retriever is None:
        sys.path.insert(0, SCRIPT_DIR)
        from retriever import APIRetriever
        _retriever = APIRetriever(KB_PATH)
    return _retriever


# ── 公开 API ─────────────────────────────────────────────────────────────────

def search(query, section=None, top_k=10):
    """
    搜索 API 接口。

    参数:
        query: 搜索关键词（支持中文、英文）
        section: 限定章节 (None=全部, 'DOC', 'DB', 'OPE', 'VIEW', 'POST')
        top_k: 返回结果数量

    返回:
        [(endpoint_dict, score), ...]

    示例:
        >>> results = search("创建节点", top_k=3)
        >>> for ep, score in results:
        ...     print(f"{ep['data']['api_name']} ({ep['path']})")
    """
    r = _get_retriever()
    return r.search(query, section=section, top_k=top_k)


def get_endpoint(path):
    """
    根据路径精确获取一个 API 接口。

    参数:
        path: API 路径，如 '/db/NODE'、'/doc/NEW'

    返回:
        endpoint_dict 或 None

    示例:
        >>> ep = get_endpoint("/db/NODE")
        >>> print(ep["data"]["api_name"])  # "Node"
    """
    r = _get_retriever()
    return r.get_by_path(path)


def get_detail(path):
    """
    获取格式化的接口详情（适合直接打印或发给 LLM）。

    返回:
        str 或 None
    """
    r = _get_retriever()
    ep = r.get_by_path(path)
    if ep:
        return r.format_endpoint_detail(ep)
    return None


def list_sections():
    """
    列出所有章节及接口数量。

    返回:
        {section_name: count, ...}
    """
    r = _get_retriever()
    return r.get_sections()


def search_and_format(query, top_k=5):
    """
    搜索并返回格式化文本——适合直接嵌入 LLM 上下文。

    返回:
        str
    """
    r = _get_retriever()
    results = r.search(query, top_k=top_k)
    if not results:
        return f"未找到与 '{query}' 相关的 API 接口。"

    lines = [f"搜索 '{query}' 找到 {len(results)} 个相关接口：\n"]
    for ep, score in results:
        lines.append(r.format_endpoint_detail(ep))
        lines.append("\n---\n")
    return "\n".join(lines)


def search_json(query, top_k=10):
    """
    搜索并返回 JSON 格式结果——适合程序化处理。

    返回:
        [{"api_name": ..., "path": ..., "section": ..., "score": ..., "params": [...]}, ...]
    """
    r = _get_retriever()
    results = r.search(query, top_k=top_k)
    output = []
    for ep, score in results:
        d = ep["data"]
        output.append({
            "api_name": d.get("api_name", ""),
            "path": ep["path"],
            "section": ep["section"],
            "subsection": ep.get("subsection", ""),
            "score": score,
            "http_methods": d.get("http_method", []) if isinstance(d.get("http_method"), list) else [d.get("http_method", "")],
            "params": [
                {
                    "key": p.get("key", ""),
                    "type": p.get("value_type", ""),
                    "required": p.get("required", False),
                    "description": p.get("description", ""),
                    "json_path": p.get("json_path", ""),
                }
                for p in d.get("parameters", [])
            ],
            "json_examples": d.get("json_examples", []),
        })
    return output


# ── 命令行接口 ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="MIDAS API 命令行检索工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python search_cli.py "创建节点"
  python search_cli.py "施加荷载" --section DB --top 5
  python search_cli.py --detail /db/NODE
  python search_cli.py --list-sections
  python search_cli.py "材料" --format json
        """,
    )

    parser.add_argument("query", nargs="?", help="搜索关键词")
    parser.add_argument("--section", "-s", choices=["DOC", "DB", "OPE", "VIEW", "POST"],
                        help="限定章节")
    parser.add_argument("--top", "-t", type=int, default=10, help="返回结果数（默认 10）")
    parser.add_argument("--format", "-f", choices=["text", "json"], default="text",
                        help="输出格式（默认 text）")
    parser.add_argument("--detail", "-d", help="查看指定路径的接口详情")
    parser.add_argument("--list-sections", "-l", action="store_true", help="列出所有章节")

    args = parser.parse_args()

    # 列出章节
    if args.list_sections:
        sections = list_sections()
        print("\n📊 MIDAS API 知识库章节\n")
        total = sum(sections.values())
        for sec, count in sections.items():
            bar = "█" * (count // 10)
            print(f"  {sec}: {count:>4} 个接口  {bar}")
        print(f"\n  总计: {total} 个接口")
        return 0

    # 查看详情
    if args.detail:
        detail = get_detail(args.detail)
        if detail:
            print(detail)
            return 0
        else:
            print(f"❌ 未找到接口: {args.detail}")
            print(f"   提示: 路径格式如 /db/NODE, /doc/NEW")
            return 1

    # 搜索
    if not args.query:
        parser.print_help()
        return 0

    results = search(args.query, section=args.section, top_k=args.top)

    if not results:
        print(f"\n❌ 未找到与 '{args.query}' 相关的接口。\n")
        print("建议:")
        print("  - 尝试更简短的关键词")
        print("  - 使用 --section 指定章节缩小范围")
        print("  - 使用 --list-sections 查看可用章节")
        return 1

    if args.format == "json":
        output = search_json(args.query, top_k=args.top)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        r = _get_retriever()
        section_info = f" (章节: {args.section})" if args.section else ""
        print(f"\n🔍 搜索 '{args.query}'{section_info} — 找到 {len(results)} 个结果:\n")

        for i, (ep, score) in enumerate(results, 1):
            d = ep["data"]
            methods = d.get("http_method", [])
            if isinstance(methods, str):
                methods = [methods]
            n_params = len(d.get("parameters", []))
            n_req = len([p for p in d.get("parameters", []) if p.get("required")])

            # 相关性标记
            if score >= 80:
                badge = "🔥"
            elif score >= 40:
                badge = "⭐"
            else:
                badge = "  "

            print(f"{badge} #{i} {d.get('api_name', '')}")
            print(f"     路径: {ep['path']}")
            print(f"     章节: {ep['section']} | 方法: {', '.join(methods)} | 参数: {n_params} ({n_req} 必填)")
            print(f"     子类: {ep.get('subsection', '—')}")

            # 显示参数摘要
            if d.get("parameters"):
                param_strs = []
                for p in d["parameters"][:5]:
                    key = p["key"]
                    req = "*" if p.get("required") else ""
                    param_strs.append(f"{req}{key}")
                print(f"     参数: {', '.join(param_strs)}" + (" ..." if n_params > 5 else ""))

            print()

        print(f"提示: 使用 --detail <路径> 查看接口完整详情")
        print(f"      使用 --format json 输出 JSON 格式")

    return 0


if __name__ == "__main__":
    sys.exit(main())
