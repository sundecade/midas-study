# MIDAS API 智能学习助手

面向结构工程师的 MIDAS Civil API 学习工具。支持智能搜索、AI 对话、代码生成，让不懂编程的工程师也能快速上手 MIDAS API 二次开发。

## 系统要求

- **Windows 10/11**（需读取注册表获取 MAPI-Key）
- **Python 3.12**
- **MIDAS Civil**（已安装并配置 MAPI-Key，软件运行时后台启动 HTTP 服务）
- 4GB 内存，约 200MB 磁盘空间

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/sundecade/midas-study.git
cd midas-study

# 2. 安装依赖
pip install -r midas_tutor/requirements.txt

# 3. 启动应用
cd midas_tutor
streamlit run app.py
```

或者直接**双击** `midas_tutor/启动助手.bat`，一键启动（首次自动安装依赖）。

启动后在浏览器打开 http://localhost:8501 即可使用。

## 功能介绍

| 功能 | 说明 | 是否需要 API Key |
|------|------|:---:|
| 智能搜索 | 中文关键词搜索 348 个 API 接口，查看参数、JSON 示例 | 否 |
| 按章节浏览 | 按 DOC/DB/OPE/VIEW/POST 分类浏览全部接口 | 否 |
| AI 对话 | RAG 增强的 AI 助手，生成建模代码 | 是 |
| 教学资料 | 6 章入门教程，JSON 基础，常见错误附录 | 否 |
| 代码示例 | 预置示例 + AI 生成代码保存/运行/下载 | 否 |

### AI 后端选择

| 后端 | 费用 | 说明 |
|------|------|------|
| Ollama 本地模型 | 免费 | 需安装 Ollama，推荐 qwen2.5:7b |
| DeepSeek API | 极低价 | 注册 platform.deepseek.com 获取 Key |
| 自定义 OpenAI API | — | 兼容任何 OpenAI 格式的服务 |

## 前置条件

使用前请确保：
1. MIDAS Civil 已打开并完成 MAPI-Key 配置
2. 注册表中 `HKEY_CURRENT_USER\SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION` 路径下 STARTUP 值为 1
3. 如使用 AI 功能，先在侧边栏配置后端和 API Key

## 命令行工具

```bash
# 命令行搜索（无需启动 Web 界面）
cd midas_tutor && python search_cli.py "创建节点"

# 查询接口的正确 JSON 格式
python test_endpoint.py /db/CONS
python test_endpoint.py --list DB
```

## 项目结构

```
midas-study/
├── scraper.py                  # KB 爬虫
├── enhance_kb.py               # KB 后处理（模板注入）
├── midas_api_knowledge_base.json  # 结构化的 API 知识库 (348 接口)
├── midas_tutor/                # Streamlit 应用
│   ├── app.py                  # 主界面
│   ├── retriever.py            # 中文检索引擎
│   ├── llm.py                  # 多后端 LLM 接入
│   ├── search_cli.py           # 命令行搜索
│   └── 启动助手.bat             # 一键启动
├── teaching/                   # 教学资料 (Markdown)
├── code_examples/              # 代码示例
└── LEARNING_GUIDE.md           # 开发者学习指南
```

## 常见问题

**Q: 搜索能用但 AI 助手不能用？**
A: 需要在侧边栏配置 AI 后端。推荐先用免费的 Ollama 本地模型测试。

**Q: AI 生成的代码运行报错？**
A: 确保 MIDAS Civil 已打开，注册表中的 STARTUP=1，且 MAPI-Key 配置正确。

**Q: 如何更新知识库？**
A: 运行 `python rescrape.py` 从 MIDAS 官网重新抓取，然后运行 `python enhance_kb.py` 重新生成模板。
