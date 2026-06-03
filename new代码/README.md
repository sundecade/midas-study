# MIDAS API 学习助手完整整理版

这个文件夹既可以直接运行，也可以在没有知识库文件时重新生成知识库。

## 1. 直接使用

如果 `midas_api_knowledge_base.json` 已存在，双击：

`midas_tutor/启动助手.bat`

首次运行会自动安装依赖。如果默认 PyPI 安装失败，会自动尝试清华镜像。

## 2. 没有知识库时重新生成

在这个目录打开命令行，按顺序运行：

```bash
python midas_tutor/install_deps.py
python build_kb_from_snapshot.py
python enhance_kb.py
python tools/refresh_learning_assets.py
```

说明：

- `build_kb_from_snapshot.py` 读取 `midas_api_structure_snapshot.json`，逐篇抓取 MIDAS Zendesk 文章并生成 `midas_api_knowledge_base.json`。
- `enhance_kb.py` 必须在生成知识库后运行，它会补 `request_templates` 和 `request_field_guide`。
- `tools/refresh_learning_assets.py` 会刷新精简教学资料和代码示例。

如果你有新的 `midas_main.html`，也可以使用原始爬虫流程：

```bash
python scraper.py
python enhance_kb.py
python tools/refresh_learning_assets.py
```

## 3. 验证

```bash
python test_endpoint.py /db/CONS
cd midas_tutor
python test_model_gen.py
python test_integration.py
```

## 4. 目录说明

- `midas_api_knowledge_base.json`：已生成的接口知识库。
- `midas_api_structure_snapshot.json`：没有主页面缓存时用于重建知识库的文章目录快照。
- `scraper.py`：从 `midas_main.html` 抓取完整知识库。
- `build_kb_from_snapshot.py`：从结构快照重建知识库。
- `enhance_kb.py`：补全请求模板，生成后必须运行。
- `midas_tutor/`：Streamlit 学习助手。
- `teaching/`：精简教学资料。
- `code_examples/`：按正常工程流程整理的代码示例。
