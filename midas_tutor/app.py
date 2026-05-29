"""
MIDAS API 智能学习助手
=======================
基于知识库检索 + 多后端大模型，帮助结构工程师学习和使用 MIDAS API。

🔍 智能搜索 & 📚 浏览全部 → 无需 API Key，直接使用
💬 AI 助手 → 支持 Ollama（免费本地）/ DeepSeek / 自定义 OpenAI API
📖 教学资料 & 📝 代码示例 → 内置学习资源

启动方式:
    streamlit run app.py
"""

import streamlit as st
import json
import sys
import os
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
KB_PATH = os.path.join(os.path.dirname(__file__), "..", "midas_api_knowledge_base.json")

from retriever import APIRetriever
from llm import LLMClient, FREE_MODELS

# ── 路径配置 ──────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
TEACHING_DIR = BASE_DIR / "teaching"
EXAMPLES_DIR = BASE_DIR / "code_examples"
USER_EXAMPLES_DIR = EXAMPLES_DIR / "user_saved"
USER_EXAMPLES_DIR.mkdir(parents=True, exist_ok=True)

TEACHING_FILES = {
    "概述": str(TEACHING_DIR / "README.md"),
    "附录A: JSON 入门": str(TEACHING_DIR / "appendix" / "json-basics.md"),
    "附录B: 常见错误": str(TEACHING_DIR / "appendix" / "common-errors.md"),
    "DOC — 项目管理": str(TEACHING_DIR / "DOC.md"),
    "DB — 模型数据库": str(TEACHING_DIR / "DB.md"),
    "OPE — 操作命令": str(TEACHING_DIR / "OPE.md"),
    "VIEW — 视图控制": str(TEACHING_DIR / "VIEW.md"),
    "POST — 后处理": str(TEACHING_DIR / "POST.md"),
}

# ── 页面配置 ─────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="MIDAS API 学习助手",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 全局 CSS：固定标签栏 + 回到顶部按钮 ──────────────────────────────────────

st.markdown("""
<style>
/* 固定标签栏在顶部（使用主题变量，适配亮色/暗色模式）*/
[data-testid="stTabs"] {
    position: sticky;
    top: 0;
    z-index: 9999;
    background: var(--st-background-color, #ffffff);
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--st-border-color, #e0e0e0);
}
/* 回到顶部按钮 */
.back-to-top {
    position: fixed;
    bottom: 40px;
    right: 30px;
    z-index: 9998;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: #89b4fa;
    color: #1e1e2e;
    border: none;
    font-size: 22px;
    cursor: pointer;
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.3s, transform 0.3s;
    text-decoration: none;
}
.back-to-top:hover {
    opacity: 0.85;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# 回到顶部按钮（JavaScript 注入）
st.markdown("""
<script>
(function() {
    if (document.querySelector('.back-to-top')) return;
    const btn = document.createElement('button');
    btn.className = 'back-to-top';
    btn.innerHTML = '⬆';
    btn.title = '回到顶部';
    btn.onclick = function() { window.scrollTo({top: 0, behavior: 'smooth'}); };
    document.body.appendChild(btn);
})();
</script>
""", unsafe_allow_html=True)

# ── 辅助函数 ─────────────────────────────────────────────────────────────────

def _score_badge(score):
    if score >= 80:
        return "🔥 高度相关"
    elif score >= 40:
        return "⭐ 相关"
    elif score >= 10:
        return "📎 可能相关"
    else:
        return ""


def _render_endpoint_card(ep):
    """渲染一个 API 端点的详情卡片。"""
    d = ep["data"]
    methods = d.get("http_method", [])
    if isinstance(methods, str):
        methods = [methods]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("HTTP 方法", ", ".join(methods))
    with col2:
        st.metric("总参数", len(d.get("parameters", [])))
    with col3:
        n_req = len([p for p in d.get("parameters", []) if p.get("required")])
        st.metric("必填参数", n_req)

    st.caption(f"**章节**: {ep['section']} | **子类别**: {ep.get('subsection', '—')}")
    st.caption(f"**来源文章**: {d.get('source_article_id', '—')}")

    params = d.get("parameters", [])
    if params:
        st.markdown("**参数列表**")
        param_data = []
        for p in params:
            param_data.append({
                "参数名": f"`{p['key']}`",
                "类型": p.get("value_type", ""),
                "必填": "✅" if p.get("required") else "—",
                "JSON路径": f"`{p.get('json_path', '')}`",
                "说明": (p.get("description") or "")[:80],
            })
        st.dataframe(param_data, use_container_width=True, hide_index=True)

    examples = d.get("json_examples", [])
    if examples:
        st.markdown("**JSON 示例**")
        for ex in examples[:2]:
            st.caption(ex.get("name", "示例"))
            st.code(json.dumps(ex.get("content", {}), indent=2, ensure_ascii=False), language="json")


def _render_api_key_prompt():
    """显示 API Key 配置引导。"""
    st.info("⚙️ AI 助手需要配置大模型后端")
    st.markdown("""
    ### 三种方式启用 AI 功能

    **方式一：Ollama 本地模型（完全免费，推荐试用）**
    1. 下载安装 [Ollama](https://ollama.com)
    2. 终端运行 `ollama pull qwen2.5:7b`
    3. 在左侧边栏选择「Ollama」后端即可使用

    **方式二：DeepSeek API（极低价）**
    1. 访问 [platform.deepseek.com](https://platform.deepseek.com) 注册
    2. 在「API Keys」页面创建 Key
    3. 在左侧边栏粘贴 API Key

    **方式三：自定义 API**
    - 任何兼容 OpenAI 格式的 API 服务都可以接入

    ---
    💡 **不需要 AI 功能？** 🔍 智能搜索、📖 教学资料、📝 代码示例 可以直接使用。
    """)


def _load_md_file(filepath):
    """读取 markdown 文件内容。"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def _load_code_file(filepath):
    """读取代码示例文件。"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def _get_code_example_files():
    """获取所有代码示例文件。"""
    files = {}
    for f in sorted(EXAMPLES_DIR.glob("*.py")):
        files[f.stem] = str(f)
    # Also get user-saved examples
    for f in sorted(USER_EXAMPLES_DIR.glob("*.py")):
        files[f"💾 {f.stem}"] = str(f)
    return files


def _save_code_to_examples(code, filename=None):
    """保存生成的代码到示例库。"""
    if not filename:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{ts}.py"
    if not filename.endswith(".py"):
        filename += ".py"
    filepath = USER_EXAMPLES_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    return str(filepath)


def _extract_code_from_answer(answer):
    """从 AI 回答中提取 Python 代码块。"""
    import re
    # 提取所有 ```python ... ``` 代码块
    py_blocks = re.findall(r'```python\s*\n(.*?)```', answer, re.DOTALL)
    if py_blocks:
        # 返回最长的那个代码块（真正的代码，不是简短示例）
        return max(py_blocks, key=len).strip()
    # 回退：提取所有 ``` ... ``` 代码块
    generic_blocks = re.findall(r'```\s*\n(.*?)```', answer, re.DOTALL)
    for block in sorted(generic_blocks, key=len, reverse=True):
        code = block.strip()
        if code and ("import " in code or "def " in code or "=" in code or "MidasAPI" in code):
            return code
    return None


def _generate_html_page(code, title="MIDAS API 代码示例"):
    """生成包含代码的独立 HTML 页面。"""
    import html as html_module
    escaped_code = html_module.escape(code)
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: "Microsoft YaHei", "Segoe UI", sans-serif;
            background: #1e1e2e;
            color: #cdd6f4;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}
        .header {{
            background: #181825;
            padding: 20px 30px;
            border-bottom: 1px solid #313244;
        }}
        .header h1 {{ font-size: 1.5rem; color: #89b4fa; }}
        .header p {{ font-size: 0.9rem; color: #a6adc8; margin-top: 5px; }}
        .container {{
            display: flex;
            flex: 1;
            overflow: hidden;
        }}
        .code-panel {{
            flex: 1;
            padding: 20px;
            overflow: auto;
        }}
        .code-panel pre {{
            background: #11111b;
            border: 1px solid #313244;
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
            font-size: 14px;
            line-height: 1.6;
            color: #cdd6f4;
        }}
        .code-panel code {{ font-family: "Cascadia Code", "Fira Code", "Consolas", monospace; }}
        .info-panel {{
            width: 300px;
            background: #181825;
            padding: 20px;
            border-left: 1px solid #313244;
            overflow-y: auto;
        }}
        .info-panel h3 {{ color: #89b4fa; margin-bottom: 10px; font-size: 1rem; }}
        .info-panel .note {{
            background: #1e1e2e;
            border-left: 3px solid #f9e2af;
            padding: 10px;
            margin: 10px 0;
            font-size: 0.85rem;
            color: #a6adc8;
        }}
        .btn {{
            display: inline-block;
            background: #89b4fa;
            color: #1e1e2e;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            margin: 5px;
            text-decoration: none;
        }}
        .btn:hover {{ background: #b4d0fb; }}
        @media (max-width: 768px) {{
            .container {{ flex-direction: column; }}
            .info-panel {{ width: 100%; border-left: none; border-top: 1px solid #313244; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p>由 MIDAS API 学习助手生成 | 复制代码到 Python 文件即可运行</p>
    </div>
    <div class="container">
        <div class="code-panel">
            <pre><code>{escaped_code}</code></pre>
        </div>
        <div class="info-panel">
            <h3>使用说明</h3>
            <div class="note">
                1. 确保 MIDAS 软件已打开并加载项目<br>
                2. 修改 BASE_URL 和 MAPI-Key 为实际值<br>
                3. 运行前检查 JSON 参数是否正确
            </div>
            <h3>配置方式</h3>
            <div class="note">
                <strong>自动获取（推荐）：</strong><br>
                代码已包含从注册表读取的逻辑<br><br>
                <strong>手动指定：</strong><br>
                搜索 "手动配置" 替换对应参数
            </div>
            <button class="btn" onclick="navigator.clipboard.writeText(document.querySelector('code').innerText)">复制代码</button>
        </div>
    </div>
</body>
</html>'''
    return html_content


def _build_mapi_config():
    """根据用户侧边栏设置，构建传递给 LLM 的 MAPI 连接配置指令。"""
    mode = st.session_state.get("_mapi_mode", "registry")
    if mode == "manual":
        base_url = st.session_state.get("_mapi_base_url", "").strip()
        mapi_key = st.session_state.get("_mapi_key", "").strip()
        if base_url and mapi_key:
            return (
                f"用户已在界面中手动输入了 MIDAS 连接信息，请直接使用以下值，"
                f"**不要写 import winreg 或任何注册表读取代码**：\n"
                f'base_url = "{base_url}"\n'
                f'mapi_key = "{mapi_key}"\n'
                f"直接在代码中定义这两个变量即可，跳过注册表获取步骤。"
            )
        else:
            return (
                "用户选择了手动输入模式但尚未填写完整信息，"
                "请暂时使用注册表方式获取配置。"
            )
    else:
        return (
            "用户未提供手动配置，请使用 winreg 从 Windows 注册表自动获取 base_url 和 mapi_key。"
        )


def _run_code_safely(code, timeout=15):
    """在子进程中安全执行 Python 代码并返回输出。"""
    import subprocess, tempfile
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            tmp_path = f.name
        # 设置环境变量，让 utils.py 等模块可以被导入
        env = os.environ.copy()
        extra_paths = [str(EXAMPLES_DIR), str(BASE_DIR)]
        existing_pythonpath = env.get("PYTHONPATH", "")
        if existing_pythonpath:
            extra_paths.append(existing_pythonpath)
        env["PYTHONPATH"] = os.pathsep.join(extra_paths)
        result = subprocess.run(
            ["python", tmp_path],
            capture_output=True, text=True, timeout=timeout,
            cwd=str(BASE_DIR),
            env=env,
        )
        os.unlink(tmp_path)
        output = result.stdout
        if result.stderr:
            output += "\n[stderr]\n" + result.stderr
        return output[:8000] or "(无输出)"
    except subprocess.TimeoutExpired:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        return "代码执行超时（超过15秒）"
    except Exception as e:
        return f"执行失败: {e}"


# ── 初始化 ───────────────────────────────────────────────────────────────────

def _get_retriever_version():
    """基于 retriever.py 和 KB 文件的修改时间生成版本号，确保代码更新后缓存失效。"""
    import os
    mtimes = []
    for p in [os.path.join(os.path.dirname(__file__), "retriever.py"), KB_PATH]:
        try:
            mtimes.append(str(os.path.getmtime(p)))
        except OSError:
            pass
    return "|".join(mtimes)


@st.cache_resource(ttl=3600)
def load_retriever(version=""):
    return APIRetriever(KB_PATH)


def init_session_state():
    defaults = {
        "chat_history": [],
        "llm_client": None,
        "api_key_configured": False,
        "search_results": [],
        "_last_search_query": "",
        "_saved_query": "",
        "_last_pill_value": "",
        "_search_done": False,
        "_ai_input": "",
        "_lang": "zh",
        # MAPI 连接配置
        "_mapi_mode": "registry",   # "registry" 或 "manual"
        "_mapi_base_url": "https://127.0.0.1:1102/civil",
        "_mapi_key": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()
retriever = load_retriever(_get_retriever_version())

# ── 侧边栏 ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.title("🏗️ MIDAS API 助手")
    st.success("🔍 搜索 & 📚 浏览 — 立即可用")
    st.divider()

    with st.expander("🔑 AI 功能设置", expanded=False):
        st.caption("选择大模型后端和语言偏好，启用 💬 AI 助手")

        # 语言选择（放在最前面）
        lang_options = {"zh": "中文", "en": "English"}
        selected_lang = st.selectbox(
            "AI 回复语言",
            list(lang_options.keys()),
            format_func=lambda x: lang_options[x],
            key="sidebar_lang",
        )
        st.session_state._lang = selected_lang

        # 后端选择
        backend_options = {
            "ollama": "Ollama（免费本地）",
            "deepseek": "DeepSeek（极低价）",
            "custom": "自定义 OpenAI API",
        }
        selected_backend = st.selectbox(
            "选择 AI 后端",
            list(backend_options.keys()),
            format_func=lambda x: backend_options[x],
            key="sidebar_backend",
        )
        backend_config = FREE_MODELS[selected_backend]

        # 模型选择
        available_models = backend_config.get("models", [])
        default_model = backend_config.get("default_model", "")
        if available_models:
            model = st.selectbox(
                "选择模型",
                available_models,
                index=available_models.index(default_model) if default_model in available_models else 0,
                key="sidebar_model",
            )
        else:
            model = st.text_input(
                "模型名称",
                value=default_model,
                key="sidebar_model_custom",
                placeholder="如 gpt-3.5-turbo",
            )

        # API Key（Ollama 不需要）
        if backend_config.get("api_key_required", True):
            api_key = st.text_input(
                "API Key",
                type="password",
                value=st.session_state.get("_api_key", ""),
                placeholder="sk-...",
                key="sidebar_api_key",
            )
        else:
            api_key = "ollama"
            st.caption("💡 Ollama 无需 API Key，免费使用")

        # 自定义 base_url
        if selected_backend == "custom":
            custom_url = st.text_input(
                "API 地址",
                value=st.session_state.get("_custom_url", ""),
                placeholder="https://api.openai.com/v1",
                key="sidebar_custom_url",
            )
            disable_thinking = st.checkbox(
                "禁用深度思考（加速响应）",
                value=st.session_state.get("_disable_thinking", True),
                help="智谱 GLM-4.7 / DeepSeek-R1 等推理模型会先进行内部思考再输出，导致响应很慢。"
                     "勾选此项可跳过思考阶段，大幅加速回复。",
                key="sidebar_disable_thinking",
            )
        else:
            custom_url = ""
            disable_thinking = False

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("连接测试", use_container_width=True):
                if selected_backend != "ollama" and not api_key:
                    st.error("请输入 API Key")
                else:
                    with st.spinner("连接中..."):
                        extra_body = {}
                        if disable_thinking:
                            extra_body = {"thinking": {"type": "disabled"}}
                        client = LLMClient(
                            backend=selected_backend,
                            api_key=api_key,
                            base_url=custom_url,
                            model=model,
                            language=selected_lang,
                            extra_body=extra_body,
                        )
                        ok, msg = client.test_connection()
                        if ok:
                            st.success("连接成功！AI 助手已启用")
                            st.session_state.llm_client = client
                            st.session_state.api_key_configured = True
                            st.session_state._api_key = api_key
                            st.session_state._custom_url = custom_url
                            st.session_state._disable_thinking = disable_thinking
                        else:
                            st.error(f"连接失败: {msg}")

        with col2:
            if st.session_state.api_key_configured and st.button("断开", use_container_width=True):
                st.session_state.llm_client = None
                st.session_state.api_key_configured = False
                st.session_state._api_key = ""
                st.session_state._custom_url = ""
                st.rerun()

        # Ollama 状态检查
        if selected_backend == "ollama":
            if st.button("检测本地 Ollama", use_container_width=True):
                with st.spinner("检测中..."):
                    available, models = LLMClient.check_ollama_available()
                    if available:
                        st.success(f"Ollama 已就绪，已安装模型: {', '.join(models) if models else '(无)'}")
                        if not models:
                            st.caption("运行 `ollama pull qwen2.5:7b` 安装模型")
                    else:
                        st.warning("未检测到 Ollama，请确认已安装并启动")

    if st.session_state.api_key_configured:
        st.success("✅ AI 已就绪")

    st.divider()

    # ── MAPI 连接设置 ──────────────────────────────────────────────────────────
    with st.expander("🔌 MIDAS 连接设置", expanded=False):
        st.caption("选择 MIDAS API 的连接方式，影响 AI 生成代码中的配置方式")
        mapi_mode = st.radio(
            "连接方式",
            ["registry", "manual"],
            format_func=lambda x: "从注册表自动获取（需安装 MIDAS）" if x == "registry" else "手动输入 base_url 和 MAPI-Key",
            key="mapi_mode_radio",
            index=0 if st.session_state._mapi_mode == "registry" else 1,
        )
        st.session_state._mapi_mode = mapi_mode

        if mapi_mode == "manual":
            base_url = st.text_input(
                "Base URL",
                value=st.session_state._mapi_base_url,
                placeholder="https://127.0.0.1:1102/civil",
                key="mapi_base_url_input",
            )
            mapi_key = st.text_input(
                "MAPI-Key",
                type="password",
                value=st.session_state._mapi_key,
                placeholder="your-mapi-key-here",
                key="mapi_key_input",
            )
            st.session_state._mapi_base_url = base_url
            st.session_state._mapi_key = mapi_key
            if base_url and mapi_key:
                st.success("✅ 已配置手动连接信息，AI 将直接使用这些值生成代码")
            else:
                st.info("💡 填入 base_url 和 MAPI-Key 后，AI 生成的代码会跳过注册表读取")
        else:
            st.info("💡 AI 生成的代码将包含从 Windows 注册表自动获取配置的代码")

    st.divider()

    st.subheader("📊 知识库统计")
    total = retriever.get_total_count()
    st.metric("API 接口总数", total)
    sections = retriever.get_sections()
    for sec, count in sections.items():
        st.caption(f"  {sec}: {count} 个接口")

    st.divider()
    st.caption("v2.0 | 数据来源: MIDAS API 在线手册")

# ── 标签页 ───────────────────────────────────────────────────────────────────

tab_search, tab_ai, tab_teaching, tab_examples = st.tabs([
    "🔍 智能搜索",
    "💬 AI 助手",
    "📖 教学资料",
    "📝 代码示例",
])

# ═══════════════════════════════════════════════════════════════════════════════
# 标签 1：智能搜索
# ═══════════════════════════════════════════════════════════════════════════════

with tab_search:
    # 快捷标签 — 点击后直接搜索
    quick_tags = st.pills(
        "快捷搜索",
        ["创建节点", "创建单元", "定义材料", "施加约束",
         "提取位移", "提取内力", "新建项目", "网格划分", "截图"],
        key="quick_search_tags",
    )

    # 检测快捷标签点击 — 直接用标签值执行搜索
    if quick_tags and quick_tags != st.session_state.get("_last_pill_value", ""):
        st.session_state._last_pill_value = quick_tags
        section = None  # 快捷搜索不区分章节
        results = retriever.search(quick_tags, section=section, top_k=15)
        st.session_state.search_results = results
        st.session_state._search_done = True
        st.session_state._last_search_query = quick_tags
        st.session_state._saved_query = quick_tags
    elif not quick_tags:
        st.session_state._last_pill_value = ""

    with st.form("search_form", clear_on_submit=False):
        col_input, col_section, col_btn = st.columns([4, 1.5, 1])

        with col_input:
            search_keyword = st.text_input(
                "搜索关键词",
                value=st.session_state.get("_saved_query", ""),
                placeholder="如 '创建节点'、'施加荷载'、'提取位移'、'定义材料'...",
                key="search_keyword",
                label_visibility="collapsed",
            )

        with col_section:
            section_filter = st.selectbox(
                "章节",
                ["全部"] + list(retriever.get_sections().keys()),
                key="search_section",
                label_visibility="collapsed",
            )

        with col_btn:
            search_submitted = st.form_submit_button("🔍 搜索", type="primary", use_container_width=True)

    # 执行手动搜索
    if search_submitted and search_keyword:
        st.session_state._saved_query = search_keyword
        section = None if section_filter == "全部" else section_filter
        results = retriever.search(search_keyword, section=section, top_k=15)
        st.session_state.search_results = results
        st.session_state._search_done = True
        st.session_state._last_search_query = search_keyword

    # 显示结果
    results = st.session_state.get("search_results", [])
    last_query = st.session_state.get("_last_search_query", "")
    if st.session_state.get("_search_done"):
        if results:
            st.caption(f"搜索「{last_query}」— 找到 {len(results)} 个相关接口")
            for ep, score in results:
                badge = _score_badge(score)
                cn_name = retriever.get_cn_display_name(ep)
                en_name = ep['data'].get('api_name', '')
                path = ep['path']
                section = ep['section']
                methods = ep['data'].get('http_method', [])
                if isinstance(methods, str):
                    methods = [methods]
                method_str = ",".join(methods) if methods else ""
                with st.expander(
                    f"**[{en_name}][{cn_name}]** — `{path}` "
                    f"({method_str}) [{section}] {badge}",
                    expanded=len(results) <= 3,
                ):
                    _render_endpoint_card(ep)
        else:
            st.info(f"搜索「{last_query}」— 没有找到匹配的接口，试试其他关键词")
    else:
        st.info("👆 输入关键词后点击 **搜索** 按钮，或点击快捷标签")

    # 热门接口
    if not st.session_state.get("_search_done"):
        st.divider()
        st.subheader("常用接口速览")
        hot_paths = ["/db/NODE", "/db/ELEM", "/db/MATL", "/db/SECT",
                      "/doc/NEW", "/ope/DIVIDEELEM", "/view/CAPTURE"]
        for path in hot_paths:
            ep = retriever.get_by_path(path)
            if ep:
                cn_name = retriever.get_cn_display_name(ep)
                en_name = ep['data'].get('api_name', '')
                with st.expander(f"**[{en_name}][{cn_name}]** — `{path}`"):
                    _render_endpoint_card(ep)

    # 按章节浏览
    st.divider()
    st.subheader("按章节浏览所有接口")

    sections = retriever.get_sections()
    browse_section = st.selectbox(
        "按章节浏览",
        list(sections.keys()),
        format_func=lambda s: f"{s} — {sections[s]} 个接口",
        key="browse_section",
    )

    if browse_section:
        eps = retriever.get_endpoints_by_section(browse_section)
        subs = retriever.get_subsections(browse_section)

        filter_text = st.text_input(
            "章节内筛选",
            placeholder="输入关键词缩小范围...",
            key="browse_filter",
        )

        if filter_text:
            fl = filter_text.lower()
            eps = [e for e in eps if fl in e["data"].get("api_name", "").lower()
                   or fl in e["path"].lower()]

        st.caption(f"显示 {len(eps)} 个接口")

        if subs:
            for sub_name, sub_eps in subs.items():
                if filter_text:
                    fl = filter_text.lower()
                    sub_eps = [e for e in sub_eps
                               if fl in e["data"].get("api_name", "").lower()
                               or fl in e["path"].lower()]
                if not sub_eps:
                    continue
                with st.expander(f"📁 {sub_name} ({len(sub_eps)} 个接口)"):
                    for ep in sub_eps[:30]:
                        d = ep["data"]
                        cn_name = retriever.get_cn_display_name(ep)
                        n_params = len(d.get("parameters", []))
                        n_req = len([p for p in d.get("parameters", []) if p.get("required")])
                        methods = d.get("http_method", [])
                        if isinstance(methods, str):
                            methods = [methods]
                        st.markdown(
                            f"**[{d.get('api_name', '')}][{cn_name}]** `{ep['path']}` — "
                            f"{', '.join(methods)} | {n_req} 必填 / {n_params} 总参数"
                        )
        else:
            for ep in eps:
                cn_name = retriever.get_cn_display_name(ep)
                en_name = ep['data'].get('api_name', '')
                with st.expander(f"**[{en_name}][{cn_name}]** — `{ep['path']}`"):
                    _render_endpoint_card(ep)

# ═══════════════════════════════════════════════════════════════════════════════
# 标签 2：AI 助手（合并 AI 问答 + 代码生成）
# ═══════════════════════════════════════════════════════════════════════════════

with tab_ai:
    if not st.session_state.api_key_configured:
        _render_api_key_prompt()
    else:
        st.caption("可以自由提问，也可以要求 AI 生成完整的 Python 代码")

        # 快捷模板
        with st.expander("📋 常用需求模板", expanded=False):
            templates = [
                ("建模", "帮我创建一个10跨连续梁模型，每跨30米，用C50混凝土"),
                ("加载", "在模型上施加均布荷载，所有梁单元施加10kN/m的竖向荷载"),
                ("分析", "帮我写一段代码：运行线性分析，然后提取所有节点的位移结果"),
                ("批量", "批量创建100个节点，沿X方向等间距排列，间距1米"),
                ("提取", "提取所有梁单元在最大弯矩工况下的内力结果，保存到CSV文件"),
                ("材料", "在模型里创建C50混凝土和Q345钢材两种材料，并定义对应的截面"),
            ]
            cols = st.columns(3)
            for i, (label, template) in enumerate(templates):
                with cols[i % 3]:
                    if st.button(f"💡 {label}: {template[:20]}...", key=f"tpl_{i}", use_container_width=True):
                        st.session_state._ai_input = template

        # 对话历史
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # 输入区
        default_input = st.session_state.pop("_ai_input", "")
        user_input = st.chat_input("输入你的问题或需求，按 Enter 发送...")

        if user_input or default_input:
            query = user_input or default_input
            if not query:
                query = default_input

            st.session_state.chat_history.append({"role": "user", "content": query})
            with st.chat_message("user"):
                st.markdown(query)

            with st.spinner("🔍 正在搜索相关 API 文档..."):
                results = retriever.search(query, top_k=5)
                context_docs = "\n\n".join(
                    retriever.format_endpoint_detail(ep) for ep, _ in results
                )

            # 构建 MAPI 连接配置信息，传给 LLM
            mapi_config = _build_mapi_config()

            with st.chat_message("assistant"):
                with st.spinner("🤔 AI 正在回答..."):
                    try:
                        client = st.session_state.llm_client
                        answer = client.chat_with_context(
                            user_query=query,
                            context_docs=context_docs,
                            chat_history=st.session_state.chat_history[:-1],
                            mapi_config=mapi_config,
                        )
                        display = answer
                        if results:
                            refs = "\n\n---\n**📚 参考接口**: "
                            refs += " · ".join(f"`{ep['path']}`" for ep, _ in results[:5])
                            display = answer + refs
                        st.markdown(display)
                        # 只保存纯净回答到历史，避免参考信息污染后续对话
                        st.session_state.chat_history.append({"role": "assistant", "content": answer})
                    except Exception as e:
                        st.error(f"回答失败: {e}")

        # 对最后一条助手消息，如果包含代码则显示操作按钮（独立于输入处理，确保按钮持久显示）
        if st.session_state.chat_history:
            last_msg = st.session_state.chat_history[-1]
            if last_msg["role"] == "assistant":
                code_content = _extract_code_from_answer(last_msg["content"])
                if code_content:
                    st.divider()
                    # 用消息总数作为稳定 key，不随点击而改变
                    msg_key = len(st.session_state.chat_history)
                    col_save, col_run, col_html, _ = st.columns([1, 1, 1, 2])
                    with col_save:
                        if st.button("💾 保存", key=f"save_{msg_key}", use_container_width=True):
                            path = _save_code_to_examples(code_content)
                            st.success(f"已保存到 {Path(path).name}")
                    with col_run:
                        if st.button("▶️ 运行", key=f"run_{msg_key}", use_container_width=True):
                            with st.spinner("执行中..."):
                                output = _run_code_safely(code_content)
                                st.session_state[f"_run_output_{msg_key}"] = output
                    with col_html:
                        html_content = _generate_html_page(code_content)
                        st.download_button(
                            "🌐 HTML",
                            data=html_content,
                            file_name=f"midas_code_{msg_key}.html",
                            mime="text/html",
                            key=f"html_{msg_key}",
                            use_container_width=True,
                        )
                    # 显示之前的运行结果
                    if st.session_state.get(f"_run_output_{msg_key}"):
                        with st.expander("▶️ 运行输出", expanded=True):
                            st.code(st.session_state[f"_run_output_{msg_key}"], language="text")

        # 底部操作栏
        if st.session_state.chat_history:
            st.divider()
            col1, col2 = st.columns([1, 5])
            with col1:
                if st.button("清空对话", use_container_width=True):
                    st.session_state.chat_history = []
                    st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# 标签 3：教学资料
# ═══════════════════════════════════════════════════════════════════════════════

with tab_teaching:
    st.caption("面向工程师的 MIDAS API 教学手册，从零开始学习")

    # 教学资料子标签
    teaching_tabs = list(TEACHING_FILES.keys())
    if "teaching_active_tab" not in st.session_state:
        st.session_state.teaching_active_tab = 0

    # 使用 pills 切换章节
    selected_teaching = st.pills(
        "选择教学章节",
        teaching_tabs,
        default=teaching_tabs[st.session_state.teaching_active_tab],
        key="teaching_pills",
    )

    if selected_teaching:
        st.session_state.teaching_active_tab = teaching_tabs.index(selected_teaching)
        filepath = TEACHING_FILES[selected_teaching]
        content = _load_md_file(filepath)

        if content:
            st.markdown("---")
            st.markdown(content)
        else:
            st.warning(f"文件不存在: {filepath}")
    else:
        # 默认显示 README
        filepath = TEACHING_FILES["概述"]
        content = _load_md_file(filepath)
        if content:
            st.markdown(content)

# ═══════════════════════════════════════════════════════════════════════════════
# 标签 4：代码示例
# ═══════════════════════════════════════════════════════════════════════════════

with tab_examples:
    st.caption("完整的 Python 代码示例，可以直接复制运行")

    code_files = _get_code_example_files()
    code_names = list(code_files.keys())

    if "code_active_index" not in st.session_state:
        st.session_state.code_active_index = 0

    # 检查是否有用户保存的示例
    has_user_examples = any(k.startswith("💾") for k in code_names)

    col_select, col_info = st.columns([2, 3])
    with col_select:
        selected_code = st.selectbox(
            "选择代码示例",
            code_names,
            index=min(st.session_state.code_active_index, len(code_names) - 1) if code_names else 0,
            key="code_selector",
        )

    if selected_code:
        st.session_state.code_active_index = code_names.index(selected_code)
        filepath = code_files[selected_code]
        code_content = _load_code_file(filepath)

        if code_content:
            with col_info:
                # Count lines for info
                lines = code_content.strip().split("\n")
                st.caption(f"{len(lines)} 行 · {filepath}")

            st.code(code_content, language="python", line_numbers=True)

            col_dl, col_save = st.columns([1, 4])
            with col_dl:
                fname = Path(filepath).name
                st.download_button(
                    "📥 下载",
                    data=code_content,
                    file_name=fname,
                    mime="text/plain",
                    key=f"dl_{selected_code}",
                )
        else:
            st.warning(f"文件不存在: {filepath}")

    if has_user_examples:
        st.info("💾 标记的示例是 AI 生成后保存的代码")
