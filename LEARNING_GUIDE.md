# MIDAS API 智能学习助手 — 完整开发教程

> 从零开始，理解整个系统是如何构建的：爬虫 → 知识库 → 检索引擎 → 大模型 → 网页界面

---

## 一、系统总览

```
                    ┌──────────────┐
                    │  MIDAS API   │
                    │  在线手册     │
                    │ (Zendesk)    │
                    └──────┬───────┘
                           │ HTTP 请求
                           ▼
              ┌────────────────────────┐
              │     scraper.py         │  爬虫：抓取 348 个 API 文档
              │     rescrape.py        │  重爬：基于已有结构增量更新
              └───────────┬────────────┘
                          │ 输出
                          ▼
              ┌────────────────────────┐
              │ midas_api_knowledge    │  知识库 JSON（4.6 MB 原始数据）
              │ _base.json             │  - API 名称、方法、URL
              │                        │  - 参数列表（必填/可选/类型）
              └───────────┬────────────┘  - JSON Schema
                          │               - JSON 示例
              ┌───────────▼────────────┐
              │    enhance_kb.py       │  后处理：给每个端点添加
              │                        │  - request_templates（完整请求模板）
              └───────────┬────────────┘  - request_field_guide（字段速查）
                          │
                          ▼
      ┌───────────────────────────────────┐
      │     midas_api_knowledge_base.json  │  最终知识库（6.9 MB）
      │     (增强后)                       │
      └───────────────┬───────────────────┘
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
  ┌────────────┐ ┌──────────┐ ┌────────────────┐
  │ generate_  │ │ generate │ │ midas_tutor/   │
  │ teaching.py│ │ _code_   │ │                │
  │            │ │ examples │ │ ┌────────────┐ │
  │ → teaching/│ │ .py      │ │ │retriever.py│ │  检索引擎
  │   *.md     │ │ → code_  │ │ │搜索+格式化  │ │
  │            │ │ examples │ │ └─────┬──────┘ │
  └────────────┘ │ / *.py   │ │       │        │
                 └──────────┘ │ ┌─────▼──────┐ │
                              │ │  llm.py    │ │  大模型客户端
                              │ │ DeepSeek/  │ │
                              │ │ Ollama/    │ │
                              │ │ 自定义API  │ │
                              │ └─────┬──────┘ │
                              │       │        │
                              │ ┌─────▼──────┐ │
                              │ │  app.py    │ │  Streamlit 网页
                              │ │  4个标签页  │ │
                              │ └────────────┘ │
                              └────────────────┘
```

---

## 二、全部文件清单（41 个文件）

### 2.1 核心脚本（根目录）

| 文件 | 作用 | 输入 | 输出 |
|------|------|------|------|
| `scraper.py` | 主爬虫，从 Zendesk API 抓取全部 API 文档 | `midas_main.html`（缓存的主页） | `midas_api_knowledge_base.json` |
| `rescrape.py` | 增量重爬，基于已有 KB 结构重新请求文章 | 已有 `midas_api_knowledge_base.json` | 覆盖 KB + 生成备份 |
| `enhance_kb.py` | **必须执行** 的后处理脚本，给每个端点添加 `request_templates` 和 `request_field_guide` | KB JSON | 增强后的 KB JSON |
| `generate_teaching.py` | 从 KB 生成 Markdown 教学资料（part2） | KB JSON | `teaching/*.md` |
| `generate_code_examples.py` | 从 KB 生成 Python 代码示例（part3） | KB JSON | `code_examples/*.py` |
| `test_endpoint.py` | 测试工具：查任意端点的正确 JSON 格式 | 命令行参数 | 终端输出 |
| `reg&link.py` | 辅助脚本：从 Windows 注册表读取 MIDAS 配置 | — | — |
| `qusetion.py` | 用户测试问题的 Python 脚本 | — | — |

### 2.2 知识库文件（根目录）

| 文件 | 作用 |
|------|------|
| `midas_api_knowledge_base.json` | **核心数据文件**（6.9 MB），348 个 API 接口的结构化知识库 |
| `midas_api_knowledge_base_backup.json` | KB 备份文件（rescrape 前自动创建） |
| `scraper_progress.json` | 爬虫进度文件（每 20 个端点保存一次，支持断点续传） |
| `rescrape_progress.json` | 重爬进度文件 |

### 2.3 任务定义（根目录）

| 文件 | 内容 |
|------|------|
| `part1.ini` | 阶段一任务描述：爬取 API 文档 |
| `part2.ini` | 阶段二任务描述：生成教学内容 |
| `part3.ini` | 阶段三任务描述：生成代码示例 |
| `CLAUDE.md` | 项目文档（给 Claude Code 看的） |

### 2.4 测试问题文件（根目录）

| 文件 | 内容 |
|------|------|
| `question.txt` / `question2.txt` / `question3.txt` / `questions4.txt` | 用户测试问题时使用的输入样例 |

### 2.5 midas_tutor/ — 网页应用

| 文件 | 作用 |
|------|------|
| `app.py` | **Streamlit 网页主程序**，4 个标签页：智能搜索、AI 助手、教学资料、代码示例 |
| `retriever.py` | **检索引擎**，加载 KB → 构建搜索索引 → 搜索 → 格式化端点详情给 LLM |
| `llm.py` | **大模型客户端**，支持 DeepSeek / Ollama / 自定义 API，包含系统提示词和 MAPI 工作流程文档 |
| `search_cli.py` | **命令行检索工具**，不依赖 Streamlit，可在终端直接搜索 API |
| `requirements.txt` | Python 依赖：`streamlit`, `openai`, `urllib3` |
| `启动助手.bat` | Windows 批处理文件，双击启动网页应用 |
| `.streamlit/config.toml` | Streamlit 主题配置 |

### 2.6 teaching/ — 教学资料

| 文件 | 内容 |
|------|------|
| `README.md` | 教学手册总览和阅读顺序 |
| `DOC.md` | DOC 章节教学（11 个接口）— 项目管理 |
| `DB.md` | DB 章节教学（225 个接口）— 模型数据库 |
| `OPE.md` | OPE 章节教学（13 个接口）— 操作命令 |
| `VIEW.md` | VIEW 章节教学（7 个接口）— 视图控制 |
| `POST.md` | POST 章节教学（92 个接口）— 后处理 |
| `appendix/json-basics.md` | 附录 A：JSON 快速入门（5 分钟） |
| `appendix/common-errors.md` | 附录 B：常见错误和解决方案 |

### 2.7 code_examples/ — 代码示例

| 文件 | 内容 | 适合 |
|------|------|------|
| `README.md` | 代码示例总览和使用说明 | 所有人 |
| `00_config_setup.py` | 两种配置方式：注册表自动获取 / 手动指定 | **必须先看** |
| `utils.py` | 工具函数库（封装 auto_config、manual_config、MidasAPI） | 快速上手 |
| `01_project_management.py` | 新建、保存、打开、关闭项目 | 第一次用 API |
| `02_create_model.py` | 创建节点、单元、材料、截面 | 自动化建模 |
| `03_apply_loads.py` | 施加边界条件和荷载 | 批量加载 |
| `04_run_analysis.py` | 执行分析和操作命令 | 自动化分析 |
| `05_extract_results.py` | 提取分析结果数据 | 批量出结果 |
| `06_view_control.py` | 选择对象和截图 | 自动截图 |

---

## 三、详细教程：从爬虫到网页界面的完整流程

### 第 1 步：爬取 API 文档 → 知识库 JSON

**涉及文件**：`scraper.py`、`midas_main.html`

**做了什么**：
1. 从本地 `midas_main.html`（MIDAS API 在线手册的缓存页面）解析出全部 349 个 API 接口的目录结构
2. 按章节（DOC/DB/OPE/VIEW/POST）和子章节（如 DB → Boundary、DB → Node/Element）组织
3. 通过 Zendesk API 逐个请求每篇文章的详细内容：
   ```
   https://support.midasuser.com/api/v2/help_center/en-us/articles/{文章ID}
   ```
4. 解析每篇文章的 HTML 内容，提取：
   - **Input URI** → 提取 API 路径（如 `/db/CONS`）
   - **HTTP Method** → 提取 GET/POST/PUT/DELETE
   - **JSON Schema** → 提取完整参数结构（类型、嵌套关系）
   - **Spec 表格** → 提取参数说明、必填/可选、默认值
   - **JSON 示例** → 提取实际请求样例
5. 合并 Schema 参数和 Spec 表格参数（Spec 表格优先于 Schema 提供 required/default 信息）
6. 每处理 20 个端点保存一次进度，支持断点续传

**关键代码片段理解**：
```python
# scraper.py 核心流程
structure = parse_main_page()       # 解析目录结构
api_data = process_all_endpoints()  # 逐个抓取详情
# 输出: midas_api_knowledge_base.json
```

**输出**：`midas_api_knowledge_base.json`（约 4.6MB），包含：
- 348 个端点（1 个因权限无法访问）
- 4863 个参数
- 每个端点的 Schema、示例、参数表

---

### 第 2 步：增强知识库 → 添加请求模板

**涉及文件**：`enhance_kb.py`

**问题**：JSON Schema 只展示内部数据结构（如 `ITEMS` 数组），但**不包含外层包装层**。对于 DB 章节的端点，实际请求需要：
```json
{"Assign": {"1": {实际数据}}}     ← Schema 只显示"实际数据"部分
```

**解决方案**：`enhance_kb.py` 给每个端点添加两个新字段：

1. **`request_templates`** — 根据示例推断出完整的请求 JSON 结构：
   - `_wrapper_type`：包装类型（Assign+Numeric / Argument / EndpointKey）
   - `_wrapper_info`：强制结构规则说明
   - `POST`/`GET`/`PUT`/`DELETE`：每种方法的完整 JSON 模板

2. **`request_field_guide`** — 每个字段的快速参考（必填/可选、类型、默认值、说明）

**核心逻辑**：
```python
# 1. 从示例中识别包装类型
#    - DB 章节: {"Assign": {"1": {data}}} → "Assign+Numeric"
#    - DOC/OPE: {"Argument": {data}}      → "Argument"
#    - 其他:    {"KEY": {data}}           → "EndpointKey"

# 2. 生成完整模板
#    - 有示例: 从示例内容提取结构，值替换为 <string>/<integer> 等占位符
#    - 无示例: 从 JSON Schema 推断结构
#    - 都没: 从参数列表推断结构

# 3. 同时构建字段速查表
```

**执行**：
```bash
PYTHONUTF8=1 python enhance_kb.py
# Enhanced 348/348 endpoints
```

---

### 第 3 步：检索引擎 → 把知识库变成可搜索

**涉及文件**：`midas_tutor/retriever.py`

`APIRetriever` 类是整个系统的数据中枢，负责：

#### 3.1 加载和索引
```python
retriever = APIRetriever("midas_api_knowledge_base.json")
# 内部做了：
#   1. 加载 JSON 文件
#   2. 扁平化所有端点（遍历所有章节和子章节）
#   3. 为每个端点构建搜索索引文本
```

#### 3.2 搜索索引的构建
每个端点生成一段"搜索文本"，包含：
- API 英文名（x2 权重）
- 中文名（x3 权重，保证中文搜索命中）
- 路径、章节、子章节
- 所有参数名和描述
- JSON 示例中的键名
- 参考表中的可选值（x3 权重）
- HTTP 方法对应的中文动词（POST → "创建/新建/添加"，GET → "查询/获取/提取" 等）

#### 3.3 中英文关键词映射
```python
CN_EN_MAP = {
    "约束": "constraint support CONS boundary restraint",
    "节点": "node nodal NODE",
    "梁单元": "beam element BEM BEAM ELEM frame",
    # ... 共 290+ 个映射
}
```

搜索 "约束" 时，自动扩展为 `"约束 constraint support CONS boundary restraint"` 进行匹配。

#### 3.4 搜索结果格式化（⭐ 最关键的环节）
`format_endpoint_detail()` 将端点数据格式化为发给 LLM 的文本：
1. 基本信息（名称、路径、章节、HTTP 方法）
2. **⚠️ 强制 JSON 结构规则**（`request_templates._wrapper_info`）
3. 参数表（参数名、类型、必填、说明）
4. **完整 JSON 请求模板**（POST/GET/PUT/DELETE 每种方法的完整结构）
5. **字段速查**（每个字段的必填/可选/类型/说明）
6. JSON 示例

**这一步是防止 LLM 生成错误 JSON 的关键防线。**

---

### 第 4 步：大模型接入 → 让 AI 理解知识库

**涉及文件**：`midas_tutor/llm.py`

#### 4.1 多后端支持
```python
class LLMClient:
    def __init__(self, backend="deepseek", api_key="", ...):
        # 支持三种后端：
        #   - deepseek: api.deepseek.com（极低价）
        #   - ollama:   localhost:11434（完全免费）
        #   - custom:   任何 OpenAI 兼容 API
```

#### 4.2 系统提示词
`SYSTEM_PROMPT` 包含：
- **MAPI 工作流程文档**：MAPI-Key 认证、base_url 获取（注册表/手动）、请求流程
- **标准代码模板**：包含 `MidasAPI()` 函数的完整实现
- **建模工作流程**：0~9 步严格顺序（新建项目 → 单位 → 材料 → 截面 → 节点 → 单元 → 边界 → 荷载 → 分析 → 结果）
- **JSON 格式规范**：禁止自行杜撰结构、必须使用 `Assign` 包装、字段名大小写不可改
- **回答规则**：中文回答、每行注释、只用简单语法、标注必填参数

#### 4.3 RAG 流程
```python
def chat_with_context(self, user_query, context_docs, chat_history):
    # 1. 把检索到的 API 文档注入上下文
    context_msg = f"以下是和用户问题相关的 MIDAS API 文档：\n{context_docs}\n..."
    
    # 2. 把上下文作为 system message 发送给 LLM
    messages = [{"role": "system", "content": context_msg},
                {"role": "user", "content": user_query}]
    
    # 3. LLM 根据上下文生成回答
    return self.chat(messages)
```

---

### 第 5 步：Streamlit 网页界面 → 用户可以交互

**涉及文件**：`midas_tutor/app.py`

#### 5.1 四个标签页

| 标签页 | 功能 | 用到哪些模块 |
|--------|------|-------------|
| 🔍 智能搜索 | 关键词搜索 + 章节筛选 + 快捷标签 + 按章节浏览 | `retriever.py` |
| 💬 AI 助手 | RAG 对话 + 代码生成 + 运行代码 + 保存/下载 | `retriever.py` + `llm.py` |
| 📖 教学资料 | 展示 Markdown 教学文档 | `teaching/*.md` |
| 📝 代码示例 | 展示和下载 Python 代码 | `code_examples/*.py` |

#### 5.2 AI 助手的完整调用链
```
用户输入问题
    │
    ▼
retriever.search(query) → 找到 Top 5 相关 API
    │
    ▼
retriever.format_endpoint_detail(ep) → 格式化每个 API 的详情
    │
    ▼
llm_client.chat_with_context(query, context_docs, history) → LLM 生成回答
    │
    ▼
显示回答 + 提取代码块 → 保存/运行/下载 HTML
```

#### 5.3 代码运行功能
```python
def _run_code_safely(code, timeout=15):
    # 1. 把代码写入临时 .py 文件
    # 2. 用 subprocess 在子进程中执行
    # 3. 捕获 stdout/stderr
    # 4. 超时 15 秒自动终止
    # 5. 清理临时文件
```

---

### 第 6 步：教学资料和代码示例生成

**涉及文件**：`generate_teaching.py`、`generate_code_examples.py`

这两个脚本从 KB JSON 自动生成教学材料：

- `generate_teaching.py`：遍历每个章节的端点，生成包含工程含义、JSON 解释、必填/可选参数、常见错误等内容的 Markdown 文件
- `generate_code_examples.py`：按工程工作流程（配置 → 项目管理 → 建模 → 加载 → 分析 → 结果）生成带详细中文注释的完整 Python 脚本

---

## 四、学习计划（6 天，每天 1~2 小时）

### 第 1 天：理解数据和爬虫

**目标**：理解知识库的数据结构和爬虫原理

**阅读顺序**：
1. `part1.ini`（5 分钟）— 了解阶段一的任务要求
2. `CLAUDE.md`（10 分钟）— 项目整体架构
3. `midas_api_knowledge_base.json`（20 分钟）— 用 VS Code 打开，浏览结构
   - 看 `meta` → 了解元数据
   - 看 `structure` → 了解章节组织
   - 看 `api_data.DB.subsections.Boundary["/db/CONS"]` → 仔细看一个端点
4. `scraper.py`（30 分钟）— 对照着读：
   - `parse_main_page()` — 怎么从 HTML 解析目录
   - `fetch_article()` — 怎么请求 Zendesk API
   - `parse_article_body()` — 怎么提取 Schema 和参数
   - `process_all_endpoints()` — 怎么协调整个流程

**练习**：用 `test_endpoint.py` 查 3 个不同章节的端点，对比它们的 JSON 结构差异

---

### 第 2 天：理解数据增强

**目标**：理解为什么需要 `enhance_kb.py`，它解决了什么问题

**阅读顺序**：
1. 先用 `test_endpoint.py /db/CONS` 看增强后的效果（10 分钟）
   - 对比 `json_schema`（只有内部结构）和 `request_templates.POST`（完整结构）
2. `enhance_kb.py`（40 分钟）
   - `get_wrapper_type_and_info()` — 怎么识别包装类型
   - `build_template_from_example()` — 怎么从示例生成模板
   - `build_template_from_schema()` — 怎么从 Schema 生成模板
   - `_build_template_from_params()` — 兜底方案
   - `_enhance_one_endpoint()` — 单端点增强的主流程

**练习**：
- 找一个 DB 端点，手动写出它的完整 JSON 结构（包括 Assign 包装）
- 找一个 DOC 端点，对比包装差异

---

### 第 3 天：理解检索引擎

**目标**：理解怎么把知识库变成可搜索的，以及怎么格式化给 LLM

**阅读顺序**：
1. `midas_tutor/retriever.py`（60 分钟）
   - `_load()` — 怎么扁平化知识库
   - `_add_endpoint()` — 怎么构建搜索索引
   - `CN_EN_MAP` — 中英文关键词映射表（290+ 条）
   - `_expand_query()` — 中文搜索词怎么扩展
   - `search()` — 搜索算法（路径匹配 > API 名匹配 > 中文匹配 > 英文匹配 > 章节语义）
   - **`format_endpoint_detail()`** — 最关键的格式化函数

**练习**：
```bash
cd midas_tutor
PYTHONUTF8=1 python search_cli.py "创建节点"
PYTHONUTF8=1 python search_cli.py "提取内力" --section POST
PYTHONUTF8=1 python search_cli.py --detail /db/CONS
```

---

### 第 4 天：理解大模型接入

**目标**：理解系统提示词设计和 RAG 流程

**阅读顺序**：
1. `midas_tutor/llm.py`（45 分钟）
   - `MAPI_WORKFLOW_DOC` — MAPI 工作流程文档（认证、base_url、请求流程）
   - `SYSTEM_PROMPT` — 系统提示词（建模流程、JSON 规则、回答规则）
   - `LLMClient.__init__()` — 多后端配置
   - `LLMClient.chat_with_context()` — **RAG 核心流程**
   - `FREE_MODELS` — 三种后端的配置

**练习**：
- 如果你有 DeepSeek API Key，配置并测试连接
- 如果没有，安装 Ollama 并拉取 `qwen2.5:7b` 模型测试

---

### 第 5 天：理解网页界面

**目标**：理解 Streamlit 应用的完整流程

**阅读顺序**：
1. `midas_tutor/app.py`（60 分钟）
   - 页面配置和 CSS（固定标签栏）
   - `init_session_state()` — 会话状态管理
   - 标签 1（智能搜索）：搜索表单 → 结果显示 → 章节浏览
   - 标签 2（AI 助手）：API Key 配置 → 对话 → 代码提取 → 运行/保存/HTML
   - 标签 3（教学资料）：Markdown 渲染
   - 标签 4（代码示例）：代码展示和下载
   - `_run_code_safely()` — 子进程安全执行

**练习**：
- 启动应用（双击 `启动助手.bat`）
- 在智能搜索中搜"创建梁单元"
- 浏览 DB 章节的所有子类别
- 如果配置了 AI，尝试问"帮我创建一个简支梁模型"

---

### 第 6 天：整体回顾和实战

**目标**：理解整个数据流，能独立排查问题

**实战任务**：
1. **追踪一次完整请求**：从用户在网页输入"创建固定支座"到 LLM 返回代码，画出数据流经的每个函数
2. **排查 JSON 格式问题**：模拟 LLM 生成错误 JSON 的场景，追踪是哪个环节出了问题
3. **修改系统提示词**：在 `llm.py` 的 `SYSTEM_PROMPT` 中加一条新规则，重启应用测试效果

**检查清单**：
- [ ] 能说出知识库 JSON 的完整结构
- [ ] 能解释为什么 DB 端点需要 `Assign` + 数字键包装
- [ ] 能解释 `retriever.format_endpoint_detail()` 为什么是防止 LLM 错误的关键
- [ ] 能说出 RAG 的三个步骤（检索 → 格式化 → 发送 LLM）
- [ ] 能解释系统提示词和检索上下文的区别和配合方式

---

## 五、关键设计决策（为什么这样做）

### 5.1 为什么不用数据库而用 JSON 文件？

- 数据量小（348 个端点，6.9 MB），JSON 文件足够
- 无需额外依赖（不需要安装数据库）
- 可以直接用文本编辑器查看和调试
- Python 一行 `json.load()` 就能全部加载到内存

### 5.2 为什么爬虫和增强是分开的两个步骤？

- 爬虫负责"忠实抓取"，增强负责"补充推断"
- 重新爬取时，只需要重跑爬虫 + 增强，不需要手工修改
- 如果增强逻辑需要改进，修改 `enhance_kb.py` 重跑即可，不需要重新爬取

### 5.3 为什么 JSON 包装规则要"双重保障"？

1. **知识库层面**（`enhance_kb.py`）：给每个端点添加 `request_templates`
2. **检索层面**（`retriever.py`）：`format_endpoint_detail()` 确保发给 LLM
3. **提示词层面**（`llm.py`）：系统提示词中硬编码了包装规则

三层防护，因为 LLM 天然倾向于按 Schema 生成（Schema 没有包装层），必须有足够的上下文约束它。

### 5.4 为什么用 Streamlit 而不是 Flask/FastAPI？

- 目标用户是工程师，不需要理解前后端分离
- Streamlit 纯 Python，一个文件就搞定界面
- 自带组件（聊天框、代码高亮、表格、文件下载）
- 不需要写 HTML/CSS/JavaScript

---

## 六、常见问题排查

| 问题 | 可能原因 | 排查方法 |
|------|---------|---------|
| LLM 生成没有 Assign 包装的 JSON | `enhance_kb.py` 没执行，或 `format_endpoint_detail` 没包含模板 | 检查 `test_endpoint.py /db/CONS` 有无 `request_templates` |
| 搜索不到中文关键词 | `CN_EN_MAP` 缺少映射 | 检查 `retriever.py` 是否有对应关键词 |
| 爬虫崩溃/编码错误 | 没用 `PYTHONUTF8=1` | 所有 Python 命令加 `PYTHONUTF8=1` 前缀 |
| AI 助手连接失败 | API Key 错误或网络不通 | 先用侧边栏的"连接测试"排查 |
| 知识库不完整 | 重新爬取后没跑 `enhance_kb.py` | 检查端点是否有 `request_templates` 字段 |
