"""Refresh curated learning docs, code examples, and the Windows launcher.

The scraper keeps the full API knowledge base.  These generated files are the
small, opinionated "normal workflow" layer shown to beginner users.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEACHING = ROOT / "teaching"
EXAMPLES = ROOT / "code_examples"
TUTOR = ROOT / "midas_tutor"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


UTILS = r'''
"""Small helper functions for MIDAS API examples.

All example scripts use the same call shape:

    result = MidasAPI("POST", "/db/NODE", {"Assign": {...}}, config)

DB endpoints create/update data with:
    {"Assign": {"1": {data}, "2": {data}}}

DOC/OPE/VIEW/POST endpoints usually use:
    {"Argument": {data}}
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests
import urllib3

urllib3.disable_warnings()


def auto_config() -> dict[str, str] | None:
    """Read base_url and MAPI-Key from the Windows registry."""
    try:
        import winreg

        reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
        uri = winreg.QueryValueEx(key, "URI")[0]
        port = winreg.QueryValueEx(key, "PORT")[0]
        mapi_key = winreg.QueryValueEx(key, "Key")[0]
        winreg.CloseKey(key)

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "STARTUP", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
        except Exception:
            pass

        return {"base_url": f"https://{uri}:{port}/civil", "mapi_key": mapi_key}
    except Exception as exc:
        print(f"Cannot read MIDAS registry config: {exc}")
        return None


def manual_config(
    base_url: str = "https://127.0.0.1:1102/civil",
    mapi_key: str = "replace-with-your-mapi-key",
) -> dict[str, str]:
    """Use this when registry lookup is not available."""
    return {"base_url": base_url.rstrip("/"), "mapi_key": mapi_key}


def get_config() -> dict[str, str]:
    """Prefer registry config, then fall back to manual placeholders."""
    config = auto_config()
    if config:
        return config
    print("Using manual_config placeholder. Edit mapi_key before sending requests.")
    return manual_config()


def MidasAPI(
    method: str,
    command: str,
    body: dict[str, Any] | None = None,
    config: dict[str, str] | None = None,
) -> Any:
    """Send one request to MIDAS and return decoded JSON when possible."""
    config = config or get_config()
    method = method.upper()
    url = config["base_url"].rstrip("/") + command
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": config["mapi_key"],
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, verify=False, timeout=60)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=body or {}, verify=False, timeout=60)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=body or {}, verify=False, timeout=60)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, json=body or {}, verify=False, timeout=60)
        else:
            raise ValueError(f"Unsupported method: {method}")
    except requests.exceptions.ConnectionError:
        print(f"Cannot connect to {config['base_url']}. Start MIDAS and enable API first.")
        return None

    if not response.ok:
        print(f"{method} {command} failed: HTTP {response.status_code}")
        print(response.text[:1000])
        return None

    try:
        return response.json()
    except ValueError:
        return response.text


def show(title: str, value: Any) -> None:
    """Pretty-print one API response."""
    print(f"\n--- {title} ---")
    if isinstance(value, (dict, list)):
        print(json.dumps(value, ensure_ascii=False, indent=2))
    else:
        print(value)


def save_json(path: str, value: Any) -> None:
    """Save a response beside the example script."""
    out = Path(__file__).resolve().parent / path
    out.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {out}")
'''


CONFIG_EXAMPLE = r'''
"""00 - Check the MIDAS API connection.

Run this first.  It does not modify the model.
"""

from utils import MidasAPI, get_config, show


config = get_config()
print("base_url:", config["base_url"])
print("mapi_key:", config["mapi_key"][:8] + "..." if config["mapi_key"] else "<empty>")

status = MidasAPI("GET", "/ope/PROJECTSTATUS", config=config)
show("Project status", status)
'''


PROJECT_EXAMPLE = r'''
"""01 - Project setup.

Normal order starts with a new project, then units.  /db/UNIT supports GET and
PUT only, so do not send POST to /db/UNIT.
"""

from utils import MidasAPI, get_config, show


config = get_config()

show("New project", MidasAPI("POST", "/doc/NEW", {"Argument": {}}, config))

unit_body = {
    "Assign": {
        "1": {
            "ID": 1,
            "FORCE": "N",
            "DIST": "m",
            "HEAT": "C",
            "TEMPER": "C",
        }
    }
}
show("Set units", MidasAPI("PUT", "/db/UNIT", unit_body, config))
'''


MODEL_EXAMPLE = r'''
"""02 - Build a 20+30+20 m continuous beam.

Correct order:
1. Material
2. Section
3. Nodes
4. Elements
5. Supports
"""

from utils import MidasAPI, get_config, show


config = get_config()

material = {
    "Assign": {
        "1": {
            "TYPE": "CONC",
            "NAME": "C50",
            "HE_SPEC": 0,
            "HE_COND": 0,
            "PLMT": 0,
            "P_NAME": "",
            "bMASS_DENS": False,
            "DAMP_RAT": 0,
            "PARAM": [
                {
                    "P_TYPE": 1,
                    "STANDARD": "JTG3362-18(RC)",
                    "CODE": "",
                    "DB": "C50",
                    "bELAST": False,
                    "ELAST": 0,
                }
            ],
        }
    }
}
show("Create C50 material", MidasAPI("POST", "/db/MATL", material, config))

section = {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "Box_1.5m",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "HORZ_OFFSET_OPT": 0,
                "VERT_OFFSET_OPT": 0,
                "USE_SHEAR_DEFORM": False,
                "USE_WARPING_EFFECT": False,
                "SHAPE": "B",
                "DATATYPE": 2,
                "SECT_I": {"vSIZE": [1.5, 1.0, 0.2, 0.2, 0.2, 0.2]},
            },
        }
    }
}
show("Create box section", MidasAPI("POST", "/db/SECT", section, config))

nodes = {}
for index in range(36):
    node_id = index + 1
    nodes[str(node_id)] = {"X": index * 2.0, "Y": 0, "Z": 0}
show("Create nodes", MidasAPI("POST", "/db/NODE", {"Assign": nodes}, config))

elements = {}
for index in range(35):
    elem_id = index + 1
    elements[str(elem_id)] = {
        "TYPE": "BEAM",
        "MATL": 1,
        "SECT": 1,
        "NODE": [index + 1, index + 2],
        "ANGLE": 0,
    }
show("Create beam elements", MidasAPI("POST", "/db/ELEM", {"Assign": elements}, config))

supports = {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "GROUP_NAME": "", "CONSTRAINT": "1111110"}]},
        "11": {"ITEMS": [{"ID": 11, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
        "26": {"ITEMS": [{"ID": 26, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
        "36": {"ITEMS": [{"ID": 36, "GROUP_NAME": "", "CONSTRAINT": "0110000"}]},
    }
}
show("Create supports", MidasAPI("POST", "/db/CONS", supports, config))
'''


LOAD_EXAMPLE = r'''
"""03 - Add simple self-weight.

Use /db/BODF for self-weight.  Beam member loads use /db/BMLD and have a more
specific ITEMS structure; check the API search before changing that body.
"""

from utils import MidasAPI, get_config, show


config = get_config()

self_weight = {
    "Assign": {
        "1": {
            "LCNAME": "SelfWeight",
            "GROUP_NAME": "",
            "FV": [0, 0, -1],
        }
    }
}
show("Create self-weight load", MidasAPI("POST", "/db/BODF", self_weight, config))
'''


ANALYSIS_EXAMPLE = r'''
"""04 - Run analysis.

Some MIDAS versions accept an empty Argument for normal analysis.  If your
product asks for a type, use {"Argument": {"TYPE": "Pushover"}} only for
pushover analysis.
"""

from utils import MidasAPI, get_config, show


config = get_config()
show("Run analysis", MidasAPI("POST", "/doc/ANAL", {"Argument": {}}, config))
'''


RESULT_EXAMPLE = r'''
"""05 - Extract a POST result table.

Many result tables share the real command /post/TABLE.  The difference is the
TABLE_TYPE value in the Argument body.
"""

from utils import MidasAPI, get_config, save_json, show


config = get_config()

element_weight_table = {
    "Argument": {
        "TABLE_NAME": "Element Weight",
        "TABLE_TYPE": "ELEMENTWEIGHT",
        "EXPORT_PATH": "",
        "NODE_ELEMS": {"TO": "1 to 35"},
    }
}
result = MidasAPI("POST", "/post/TABLE", element_weight_table, config)
show("Element weight table", result)

if result is not None:
    save_json("element_weight_result.json", result)
'''


VIEW_EXAMPLE = r'''
"""06 - Set view angle and capture an image.

Edit EXPORT_PATH to a writable path on your computer before running capture.
"""

from utils import MidasAPI, get_config, show


config = get_config()

show("Set view angle", MidasAPI("POST", "/view/ANGLE", {"Argument": {"HORIZONTAL": 30, "VERTICAL": 20}}, config))

capture = {
    "Argument": {
        "FIGURE_NAME": "continuous_beam",
        "EXPORT_PATH": r"C:\temp\continuous_beam.png",
        "WIDTH": 1600,
        "HEIGHT": 900,
        "SET_MODE": "pre",
        "SET_HIDDEN": False,
    }
}
show("Capture image", MidasAPI("POST", "/view/CAPTURE", capture, config))
'''


EXAMPLES_README = r'''
# MIDAS API 代码示例

这些脚本按一条正常工程流程组织，建议从上到下运行：

1. `00_config_setup.py` 只检查连接，不修改模型。
2. `01_project_management.py` 新建项目并设置单位。
3. `02_create_model.py` 建立 20+30+20 m 连续梁。
4. `03_apply_loads.py` 添加自重。
5. `04_run_analysis.py` 提交分析。
6. `05_extract_results.py` 用 `/post/TABLE` 提取结果表。
7. `06_view_control.py` 设置视角并截图。

支撑函数放在 `utils.py`，在 App 的示例下拉框中默认隐藏，避免干扰初学者。

关键字段：

- `/db/ELEM` 使用 `MATL`、`SECT`、`NODE`。
- 不要使用旧写法 `MATERIAL`、`SECTION`、`NODE_LIST`。
- `/db/UNIT` 设置单位用 PUT，不用 POST。
- POST 结果表用真实路径 `/post/TABLE`，表类型放在 `TABLE_TYPE`。
'''


TEACHING_README = r'''
# MIDAS API 学习路径

这套资料只讲正常建模流程。完整接口仍然通过搜索页查询，不再把所有接口展开成很长的教学文档。

推荐顺序：

1. DOC：新建、打开、保存项目。
2. DB：写入模型数据。
3. OPE：需要时执行模型操作。
4. DOC：提交分析。
5. POST：提取结果表。
6. VIEW：调整视图或截图。

最重要的两条 JSON 规则：

- DB 端点使用 `{"Assign": {"1": {...}}}`，每个对象放在独立数字键下。
- DOC/OPE/VIEW/POST 通常使用 `{"Argument": {...}}`。

连续梁最小建模顺序：

`/db/UNIT` 用 PUT 设置单位，然后依次调用 `/db/MATL`、`/db/SECT`、`/db/NODE`、`/db/ELEM`、`/db/CONS`。
'''


DOC_MD = r'''
# DOC 项目命令

DOC 命令控制项目文件和分析状态，不负责创建节点、单元、材料或荷载。

常用流程：

1. `POST /doc/NEW` 新建项目，请求体为 `{"Argument": {}}`。
2. `PUT /db/UNIT` 设置单位。
3. 通过 DB 端点写入模型数据。
4. `POST /doc/ANAL` 提交分析。
5. `POST /doc/SAVEAS` 保存项目。

注意：`/doc/ANAL` 是分析命令；具体模型数据仍然来自 DB。
'''


DB_MD = r'''
# DB 模型数据库

DB 是建模主层。除少数查询外，写入数据都要包在 `Assign` 中：

```json
{
  "Assign": {
    "1": {
      "field": "value"
    }
  }
}
```

连续梁建模顺序：

1. `/db/UNIT` 只支持 GET/PUT，设置单位时用 PUT。
2. `/db/MATL` 创建材料。C50 示例中 `PARAM` 必须是数组。
3. `/db/SECT` 创建截面。
4. `/db/NODE` 创建节点坐标。
5. `/db/ELEM` 创建单元，字段用 `MATL`、`SECT`、`NODE`。
6. `/db/CONS` 创建约束支座，每个支座放在独立数字键下。

不要在这些示例里使用旧字段名 `MATERIAL`、`SECTION`、`NODE_LIST`、`DOF`。
'''


OPE_MD = r'''
# OPE 操作命令

OPE 用来对已有模型执行操作，例如网格划分、模型工具、属性变更等。

普通连续梁示例通常不需要 OPE：材料、截面、节点、单元、约束都由 DB 端点完成。

如果要使用 OPE，请先确认相关 DB 对象已经存在，再按对应接口的 `Argument` 模板填写。
'''


VIEW_MD = r'''
# VIEW 视图命令

VIEW 端点只影响显示和截图，不负责建模或计算。

常用命令：

- `POST /view/ANGLE` 设置视角，例如 `{"Argument": {"HORIZONTAL": 30, "VERTICAL": 20}}`。
- `POST /view/CAPTURE` 输出图片，`FIGURE_NAME`、`EXPORT_PATH`、`WIDTH`、`HEIGHT` 放在 `Argument` 内。

如果要截取结果云图，请先完成分析并设置结果显示。
'''


POST_MD = r'''
# POST 后处理结果

POST 用于提取结果表、文本结果和设计结果。

很多结果表共用真实请求命令：

- 表格结果：`/post/TABLE`
- 文本结果：`/post/TEXT`

具体取哪张表由 `TABLE_TYPE` 决定。

示例：提取 Element Weight 表

```json
{
  "Argument": {
    "TABLE_NAME": "Element Weight",
    "TABLE_TYPE": "ELEMENTWEIGHT",
    "EXPORT_PATH": "",
    "NODE_ELEMS": {
      "TO": "1 to 35"
    }
  }
}
```

不要把 `Element Weight` 当成 URL。真正的 URL 是 `/post/TABLE`。
'''


JSON_BASICS = r'''
# JSON 入门

Python 字典会变成 JSON 对象：

```python
body = {"Argument": {"TYPE": "Pushover"}}
```

列表会变成 JSON 数组：

```python
"NODE": [1, 2]
```

字符串要加引号，数字和布尔值不要加引号：

```python
{"NAME": "C50", "ELAST": 0, "bELAST": False}
```
'''


COMMON_ERRORS = r'''
# 常见错误

1. 对 `/db/UNIT` 发送 POST。正确做法是 PUT。
2. DB 端点缺少 `Assign` 包装。
3. 多个支座都塞进同一个 `ITEMS` 数组。正确做法是每个支座使用独立数字键。
4. `/db/ELEM` 使用旧字段名。正确字段是 `MATL`、`SECT`、`NODE`。
5. 把 POST 表名当 URL。正确做法是请求 `/post/TABLE`，再设置 `TABLE_TYPE`。
6. 把 schema 里的 `properties` 当作请求体。应以搜索结果中的 `request_templates` 为准。
'''


INSTALLER = r'''
"""Install dependencies for the Streamlit tutor app.

This script uses only the Python standard library so it can run on a fresh
machine before third-party packages are installed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQ = ROOT / "requirements.txt"
MIRROR = "https://pypi.tuna.tsinghua.edu.cn/simple"


def run(args: list[str]) -> bool:
    print("\n>", " ".join(args))
    completed = subprocess.run(args)
    return completed.returncode == 0


def main() -> int:
    python = sys.executable

    if not run([python, "-m", "pip", "--version"]):
        print("pip is not available. Trying ensurepip...")
        run([python, "-m", "ensurepip", "--upgrade"])

    if run([python, "-m", "pip", "install", "-r", str(REQ)]):
        return 0

    print("\nDefault PyPI install failed. Retrying with a China mirror...")
    if run([python, "-m", "pip", "install", "-r", str(REQ), "-i", MIRROR, "--trusted-host", "pypi.tuna.tsinghua.edu.cn"]):
        return 0

    print("\nInstall failed.")
    print("Try manually:")
    print(f"  {python} -m pip install -r {REQ}")
    print(f"  {python} -m pip install -r {REQ} -i {MIRROR}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
'''


BAT = r'''
@echo off
chcp 65001 >nul
title MIDAS API Tutor
cd /d "%~dp0"

echo.
echo MIDAS API Tutor
echo ----------------------------------------

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found. Please install Python 3.10+ and tick "Add Python to PATH".
    pause
    exit /b 1
)

python -m pip show streamlit requests openai urllib3 beautifulsoup4 >nul 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    python install_deps.py
    if errorlevel 1 (
        echo Dependency installation failed.
        pause
        exit /b 1
    )
)

echo.
echo Starting Streamlit...
echo Open this address if the browser does not open automatically:
echo http://localhost:8501
echo.

python -m streamlit run app.py --server.port 8501
pause
'''


def main() -> None:
    write(EXAMPLES / "utils.py", UTILS)
    write(EXAMPLES / "00_config_setup.py", CONFIG_EXAMPLE)
    write(EXAMPLES / "01_project_management.py", PROJECT_EXAMPLE)
    write(EXAMPLES / "02_create_model.py", MODEL_EXAMPLE)
    write(EXAMPLES / "03_apply_loads.py", LOAD_EXAMPLE)
    write(EXAMPLES / "04_run_analysis.py", ANALYSIS_EXAMPLE)
    write(EXAMPLES / "05_extract_results.py", RESULT_EXAMPLE)
    write(EXAMPLES / "06_view_control.py", VIEW_EXAMPLE)
    write(EXAMPLES / "README.md", EXAMPLES_README)

    write(TEACHING / "README.md", TEACHING_README)
    write(TEACHING / "DOC.md", DOC_MD)
    write(TEACHING / "DB.md", DB_MD)
    write(TEACHING / "OPE.md", OPE_MD)
    write(TEACHING / "VIEW.md", VIEW_MD)
    write(TEACHING / "POST.md", POST_MD)
    write(TEACHING / "appendix" / "json-basics.md", JSON_BASICS)
    write(TEACHING / "appendix" / "common-errors.md", COMMON_ERRORS)

    write(TUTOR / "install_deps.py", INSTALLER)
    write(TUTOR / "启动助手.bat", BAT)


if __name__ == "__main__":
    main()
