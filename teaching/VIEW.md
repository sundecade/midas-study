# VIEW — 视图控制 API

VIEW 部分控制 MIDAS 的显示：选择对象、截图、控制显示状态。主要用于自动化截图和结果展示。

本章共 **7** 个接口。

## 工程背景

批量出报告时非常有用——自动截取每个工况的结果图。

## 接口列表

| 接口 | 方法 | 参数数 | 说明 |
|------|------|--------|------|
| `/view/ACTIVE` | POST | 6 (5 必填) |  |
| `/view/ANGLE` | POST | 3 (0 必填) |  |
| `/view/CAPTURE` | POST | 19 (2 必填) |  |
| `/view/DISPLAY` | POST | 124 (0 必填) |  |
| `/view/PRECAPTURE` | POST | 5 (4 必填) |  |
| `/view/RESULTGRAPHIC` | POST | 24 (0 必填) |  |
| `/view/SELECT` | GET | 0 (0 必填) |  |


---

# 详细教程

## Select — `/view/SELECT`

**HTTP 方法**: GET | **参数总数**: 0（0 必填 + 0 可选）

### 1. 这是什么？（工程含义）

**Select** — 这是视图控制操作。

> 简单说：这个接口用来**Select**。

### 2. JSON 结构（逐层解释）

这个接口不需要发送 JSON 数据（GET 请求）。

### 3. 必填 vs 可选参数

这个接口没有参数。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/view/SELECT"
r = requests.get(url, verify=False)
print(r.json())  # 查看返回结果
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

自动截图——写报告时，让程序自动截取每个结果视图，而不是手动截图几十次。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/view/SELECT`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

GET 请求不需要批量生成——直接发一次请求就能拿到所有数据。

### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

```python
# 使用 session 复用连接（比每次新建连接快 3-5 倍）
session = requests.Session()
session.verify = False

for i in range(100):
    data = {...}  # 你的数据
    r = session.post(f"{BASE}/view/SELECT", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Capture — `/view/CAPTURE`

**HTTP 方法**: POST | **参数总数**: 19（2 必填 + 17 可选）

### 1. 这是什么？（工程含义）

**Capture** — 这是视图控制操作。

Smart Report Image Name

> 简单说：这个接口用来**Capture**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "CAPTURE": {
    "Argument (可选)": {},
    "Argument": {
      "FIGURE_NAME": "<FIGURE_NAME>",
      "EXPORT_PATH": "<EXPORT_PATH>",
      "WIDTH (可选)": 0,
      "HEIGHT (可选)": 0,
      "STAGE_NAME (可选)": "<STAGE_NAME>",
      "SET_MODE (可选)": "<SET_MODE>",
      "SET_HIDDEN (可选)": "false",
      "ACTIVE (可选)": {},
      "ANGLE (可选)": {},
      "DISPLAY (可选)": {},
      "RESULT_GRAPHIC (可选)": {}
    }
  },
  "PERSPECTIVE (可选)": "false",
  "ZOOM_LEVEL (可选)": "100",
  "BGCOLOR_TOP (可选)": {},
  "R (可选)": 0,
  "G (可选)": 0,
  "B (可选)": 0,
  "BGCOLOR_BOTTOM (可选)": {}
}
```

**第 1 层：`CAPTURE`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`CAPTURE.Argument`** — 11 个参数在这一层

- `"FIGURE_NAME"`: 文字（字符串） — Smart Report Image Name
- `"EXPORT_PATH"`: 文字（字符串） — Image File Save Path & File Name
- `"WIDTH"`: 整数 — Image Width’s Pixel Size
- `"HEIGHT"`: 整数 — Image Height’s Pixel Size
- `"STAGE_NAME"`: 文字（字符串） — Construction Stage Name
- `"SET_MODE"`: 文字（字符串） — Select Analysis Mode• Pre-Mode: "pre"• Post-Mode: "post"
- `"SET_HIDDEN"`: 是/否（布尔值） — Hidden option• Hidden: true• Not Hidden: false
- `"ACTIVE"`: 对象（一组键值对） — Active• refer to "view/ACTIVE" manual
- ... *还有 3 个参数*

**第 3 层：最外层**
这是整个 JSON 的入口。
- `"PERSPECTIVE"`: 是/否（布尔值） — Perspective
- `"ZOOM_LEVEL"`: 数字 — Zoom Level• Zoom Out: 25 <= value < 100• Zoom Fit: 100• Zoom in: 100 < value < 200
- `"BGCOLOR_TOP"`: 对象（一组键值对） — Background Color Top
- `"R"`: 整数 — Red
- `"G"`: 整数 — Green
- `"B"`: 整数 — Blue
- `"BGCOLOR_BOTTOM"`: 对象（一组键值对） — Background Color Bottom


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `FIGURE_NAME` | 文字（字符串） | `CAPTURE.Argument.FIGURE_NAME` | Smart Report Image Name |
| `EXPORT_PATH` | 文字（字符串） | `CAPTURE.Argument.EXPORT_PATH` | Image File Save Path & File Name |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `WIDTH` | 整数 | `无` | Image Width’s Pixel Size |
| `HEIGHT` | 整数 | `无` | Image Height’s Pixel Size |
| `STAGE_NAME` | 文字（字符串） | `无` | Construction Stage Name |
| `SET_MODE` | 文字（字符串） | `无` | Select Analysis Mode• Pre-Mode: "pre"• Post-Mode: "post" |
| `SET_HIDDEN` | 是/否（布尔值） | `false` | Hidden option• Hidden: true• Not Hidden: false |
| `ACTIVE` | 对象（一组键值对） | `无` | Active• refer to "view/ACTIVE" manual |
| `ANGLE` | 对象（一组键值对） | `无` | Viewpoint• refer to "view/ANGLE" manual |
| `DISPLAY` | 对象（一组键值对） | `无` | Display• refer to "view/DISPLAY" manual |
| `RESULT_GRAPHIC` | 对象（一组键值对） | `无` | Result Display• refer to "view/RESULTGRAPHIC" manual |
| `PERSPECTIVE` | 是/否（布尔值） | `false` | Perspective |
| `ZOOM_LEVEL` | 数字 | `100` | Zoom Level• Zoom Out: 25 <= value < 100• Zoom Fit: 100• Zoom |
| `BGCOLOR_TOP` | 对象（一组键值对） | `无` | Background Color Top |
| `R` | 整数 | `无` | Red |
| `G` | 整数 | `无` | Green |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"CAPTURE" → "Argument"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument，最后填入 `Argument` 的值
- `WIDTH` 的路径：**"CAPTURE" → "Argument" → "WIDTH"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, WIDTH，最后填入 `WIDTH` 的值
- `HEIGHT` 的路径：**"CAPTURE" → "Argument" → "HEIGHT"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, HEIGHT，最后填入 `HEIGHT` 的值
- `STAGE_NAME` 的路径：**"CAPTURE" → "Argument" → "STAGE_NAME"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, STAGE_NAME，最后填入 `STAGE_NAME` 的值
- `SET_MODE` 的路径：**"CAPTURE" → "Argument" → "SET_MODE"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, SET_MODE，最后填入 `SET_MODE` 的值
- `SET_HIDDEN` 的路径：**"CAPTURE" → "Argument" → "SET_HIDDEN"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, SET_HIDDEN，最后填入 `SET_HIDDEN` 的值
- `ACTIVE` 的路径：**"CAPTURE" → "Argument" → "ACTIVE"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, ACTIVE，最后填入 `ACTIVE` 的值
- `ANGLE` 的路径：**"CAPTURE" → "Argument" → "ANGLE"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, ANGLE，最后填入 `ANGLE` 的值
- `DISPLAY` 的路径：**"CAPTURE" → "Argument" → "DISPLAY"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, DISPLAY，最后填入 `DISPLAY` 的值
- `RESULT_GRAPHIC` 的路径：**"CAPTURE" → "Argument" → "RESULT_GRAPHIC"**
  意思是：在 JSON 中依次打开 CAPTURE, Argument, RESULT_GRAPHIC，最后填入 `RESULT_GRAPHIC` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `ACTIVE` 的取值需要参考其他接口文档
- `ANGLE` 的取值需要参考其他接口文档
- `DISPLAY` 的取值需要参考其他接口文档
- `RESULT_GRAPHIC` 的取值需要参考其他接口文档
- `SET_MODE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `SET_HIDDEN` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `ZOOM_LEVEL` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/view/CAPTURE"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "CAPTURE": {
#         "Argument": {
#             "FIGURE_NAME": "<FIGURE_NAME>",
#             "EXPORT_PATH": "<EXPORT_PATH>"
#         }
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

自动截图——写报告时，让程序自动截取每个结果视图，而不是手动截图几十次。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：FIGURE_NAME、EXPORT_PATH 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 3 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
4. **URL 写错**：确认路径是 `/view/CAPTURE`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Capture 的 JSON 数据。"""
    data = {"CAPTURE": {"Argument": {"FIGURE_NAME": "<FIGURE_NAME>", "EXPORT_PATH": "<EXPORT_PATH>"}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/view/CAPTURE", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

```python
# 使用 session 复用连接（比每次新建连接快 3-5 倍）
session = requests.Session()
session.verify = False

for i in range(100):
    data = {...}  # 你的数据
    r = session.post(f"{BASE}/view/CAPTURE", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Dialog Capture — `/view/PRECAPTURE`

**方法**: POST | **参数**: 4 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `EXPORT_PATH` | 文字（字符串） | **是** | Image File Save Path & File Name |
| `VIEW_TYPE` | 文字（字符串） | **是** | Preview Picture Type• Fiber Division of Section: "FIBR" |
| `OPTION` | 对象（一组键值对） | **是** | Image File Save Path & File Name |
| `ID` | 整数 | **是** | Picture Type ID Number |
| `Argument` | 对象（一组键值对） | 否 |  |

**最简 JSON**：
```json
{
  "CAPTURE": {
    "Argument": {
      "EXPORT_PATH": "<EXPORT_PATH>",
      "VIEW_TYPE": "<VIEW_TYPE>",
      "OPTION": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "OPTION": {
            "Properties": {
              "ID": 0
            }
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\Test.jpg",
    "VIEW_TYPE": "FIBR",
    "OPTION": {
      "ID": 1
    }
  }
}
```


---

### Viewpoint — `/view/ANGLE`

**方法**: POST | **参数**: 0 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Argument` | 对象（一组键值对） | 否 |  |
| `HORIZONTAL` | 数字 | 否 | Angle of Horizontal View |
| `VERTICAL` | 数字 | 否 | Angle of Vertical View |

**官方示例**：
```json
{
  "Argument": {
    "HORIZONTAL": 30,
    "VERTICAL": 15
  }
}
```


---

## Active — `/view/ACTIVE`

**HTTP 方法**: POST | **参数总数**: 6（5 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Active** — 这是视图控制操作。

Active Mode Type• Active by Identity: "Identity"

> 简单说：这个接口用来**Active**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "ACTIVE": {
    "Argument (可选)": {},
    "Argument": {
      "ACTIVE_MODE": "<ACTIVE_MODE>",
      "N_LIST": 0,
      "E_LIST": 0,
      "IDENTITY_TYPE": "<IDENTITY_TYPE>",
      "IDENTITY_LIST": "<IDENTITY_LIST>"
    }
  }
}
```

**第 1 层：`ACTIVE`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`ACTIVE.Argument`** — 5 个参数在这一层

- `"ACTIVE_MODE"`: 文字（字符串） — Active Mode Type• Active by Identity: "Identity"
- `"N_LIST"`: 整数 — Node Number List
- `"E_LIST"`: 整数 — Element Number List
- `"IDENTITY_TYPE"`: 文字（字符串） — Identity Type (if defined)• Structure Group: "Group"• Named Plane: "Named Plane"• Load Group: "Load 
- `"IDENTITY_LIST"`: 文字（字符串） — Identity List


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `ACTIVE_MODE` | 文字（字符串） | `ACTIVE.Argument.ACTIVE_MODE` | Active Mode Type• Active by Identity: "Identity" |
| `N_LIST` | 整数 | `ACTIVE.Argument.N_LIST` | Node Number List |
| `E_LIST` | 整数 | `ACTIVE.Argument.E_LIST` | Element Number List |
| `IDENTITY_TYPE` | 文字（字符串） | `ACTIVE.Argument.IDENTITY_TYPE` | Identity Type (if defined)• Structure Group: "Group"• Named  |
| `IDENTITY_LIST` | 文字（字符串） | `ACTIVE.Argument.IDENTITY_LIST` | Identity List |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"ACTIVE" → "Argument"**
  意思是：在 JSON 中依次打开 ACTIVE, Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `ACTIVE_MODE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `IDENTITY_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/view/ACTIVE"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "ACTIVE": {
#         "Argument": {
#             "ACTIVE_MODE": "<ACTIVE_MODE>",
#             "N_LIST": 0,
#             "E_LIST": 0,
#             "IDENTITY_TYPE": "<IDENTITY_TYPE>",
#             "IDENTITY_LIST": "<IDENTITY_LIST>"
#         }
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

自动截图——写报告时，让程序自动截取每个结果视图，而不是手动截图几十次。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：ACTIVE_MODE、N_LIST、E_LIST、IDENTITY_TYPE、IDENTITY_LIST 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 2 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
4. **URL 写错**：确认路径是 `/view/ACTIVE`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Active 的 JSON 数据。"""
    data = {"ACTIVE": {"Argument": {"ACTIVE_MODE": "<ACTIVE_MODE>", "N_LIST": 0, "E_LIST": 0, "IDENTITY_TYPE": "<IDENTITY_TYPE>", "IDENTITY_LIST": "<IDENTITY_LIST>"}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/view/ACTIVE", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

```python
# 使用 session 复用连接（比每次新建连接快 3-5 倍）
session = requests.Session()
session.verify = False

for i in range(100):
    data = {...}  # 你的数据
    r = session.post(f"{BASE}/view/ACTIVE", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Display — `/view/DISPLAY`

**HTTP 方法**: POST | **参数总数**: 124（0 必填 + 124 可选）

### 1. 这是什么？（工程含义）

**Display** — 这是视图控制操作。

Element Display Options

> 简单说：这个接口用来**Display**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "DISPLAY": {
    "Argument (可选)": {},
    "Argument": {
      "NODE (可选)": "false",
      "ELEMENT (可选)": {},
      "PROPERTY (可选)": {},
      "GROUP_SELECTION (可选)": "All",
      "BOUNDARY (可选)": {},
      "LOAD (可选)": {},
      "MISC (可选)": {},
      "VIEW (可选)": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE": {
            "properties": {
              "NODE_NUMBER (可选)": "false",
              "NODE_LOCAL_AXIS (可选)": "false",
              "STORY_NAME (可选)": "false"
            }
          },
          "ELEMENT": {
            "properties": {
              "ELEM_NUMBER (可选)": "false",
              "ELEM_NUMBER_WITH_BORDER (可选)": "false",
              "ELEM_TYPE_NUMBER (可选)": "false",
              "ELEM_TYPE_NAME (可选)": "false",
              "WALL_ID (可选)": "false",
              "GAP (可选)": "false",
              "HOOK (可选)": "false",
              "CABLE (可选)": "false",
              "LOCAL_AXIS (可选)": "false",
              "LOCAL_AXIS_LABEL (可选)": "false",
              "LOCAL_DIRECTION (可选)": "false",
              "SUB_DOMAIN_REBAR_DIRECTION (可选)": "false"
            }
          },
          "PROPERTY": {
            "properties": {
              "MATERIAL_NUMBER (可选)": "false",
              "MATERIAL_NAME (可选)": "false",
              "PROPERTY_NUMBER (可选)": "false",
              "PROPERTY_NAME (可选)": "false",
              "TAPERED_SECTION_GROUP (可选)": "false",
              "TIME_DEPENDENT_MATERIAL_LINK (可选)": "false",
              "SECTION_SHAPE (可选)": "false",
              "INELASTIC_HINGE_SYMBOL (可选)": "false",
              "INELASTIC_HINGE_NAME (可选)": "false",
              "REINFORCEMENT_OF_SECTIONS (可选)": "false",
              "VIRTUAL_SECTION_LOCAL_AXIS (可选)": "false"
            }
          },
          "BOUNDARY": {
            "properties": {
              "SUPPORT (可选)": "false",
              "SUPPORT_BY_DIRECTION (可选)": "false",
              "POINT_SPRING_SUPPORT (可选)": "false",
              "POINT_SPRING_SUPPORT_COMP_TENS (可选)": "false",
              "POINT_SPRING_SUPPORT_MULTI_LINEAR (可选)": "false",
              "POINT_SPRING_SUPPORT_BY_DIRECTION (可选)": "false",
              "POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS (可选)": "false",
              "POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR (可选)": "false",
              "SURFACE_SPRING_SUPPORT_TYPE (可选)": "false",
              "SURFACE_SPRING_SUPPORT_LINEAR (可选)": "false",
              "SURFACE_SPRING_SUPPORT_COMP_TENS (可选)": "false",
              "GENERAL_SPRING_SUPPORT (可选)": "false",
              "ELASTIC_LINK (可选)": "false",
              "ELASTIC_LINK_LOCAL_AXIS (可选)": "false",
              "ELASTIC_LINK_TYPE (可选)": "false",
              "ELASTIC_LINK_NUMBER (可选)": "false",
              "GENERAL_LINK (可选)": "false",
              "GENERAL_LINK_NUMBER (可选)": "false",
              "GENERAL_LINK_LOCAL_AXIS (可选)": "false",
              "GENERAL_LINK_TYPE (可选)": "false",
              "CHANGE_GENERAL_LINK_PROPERTIES (可选)": "false",
              "BEAM_END_RELEASE_SYMBOL (可选)": "false",
              "BEAM_END_RELEASE_DIGIT (可选)": "false",
              "BEAM_END_OFFSET_SYMBOL (可选)": "false",
              "BEAM_END_OFFSET_DIGIT (可选)": "false",
              "PLATE_END_RELEASE_SYMBOL (可选)": "false",
              "PLATE_END_RELEASE_DIGIT (可选)": "false",
              "RIGID_LINK (可选)": "false",
              "LINEAR_CONSTRAINTS (可选)": "false",
              "REACTION_POSITION (可选)": "false",
              "STORY_DIAPHRAGM (可选)": "false",
              "DIAPHRAGM_DISCONNECT (可选)": "false"
            }
          },
          "LOAD": {
            "properties": {
              "CASE_SELECTION (可选)": "All",
              "LOAD_VALUE (可选)": {},
              "NODAL_BODY_FORCE (可选)": "false",
              "NODAL_LOAD (可选)": "false",
              "SPECIFIED_DISPLACEMENT (可选)": "false",
              "BEAM_LOAD (可选)": "false",
              "PRESTRESS_LOAD (可选)": "false",
              "PRETENSION_LOAD (可选)": "false",
              "FLOOR_LOAD (可选)": "false",
              "FLOOR_LOAD_NAME (可选)": "false",
              "FLOOR_LOAD_AREA (可选)": "false",
              "LOADING_AREA_PLANE (可选)": "false",
              "FINISHING_MATERIAL_LOAD (可选)": "false",
              "PRESSURE_LOAD (可选)": "false",
              "AREA_PRESSURE_LOADS (可选)": "false",
              "PLANE_LOAD (可选)": "false",
              "PLANE_LOAD_NAME (可选)": "false",
              "NODAL_TEMPERATURE (可选)": "false",
              "ELEMENT_TEMPERATURE (可选)": "false",
              "TEMPERATURE_GRADIENT (可选)": "false",
              "BEAM_SECTION_TEMPERATURE (可选)": "false",
              "TENDON_PRESTRESS (可选)": "false",
              "WIND_LOAD (可选)": "false",
              "AREA_WIND_PRESSURE (可选)": "false",
              "AREA_WIND_PRESSURE_NAME (可选)": "false",
              "BEAM_WIND_PRESSURE (可选)": "false",
              "NODAL_WIND_PRESSURE (可选)": "false",
              "FUNCTION_WIND_PRESSURE (可选)": "false",
              "FUNCTION_WIND_PRESSURE_NAME (可选)": "false",
              "SEISMIC_EARTH_PRESSURE (可选)": "false",
              "STATIC_EARTH_PRESSURE (可选)": "false",
              "SEISMIC_LOAD (可选)": "false",
              "DYNAMIC_NODAL_LOAD (可选)": "false",
              "MULTIPLE_SUPPORT_EXCITATION (可选)": "false",
              "MULTIPLE_SUPPORT_EXCITATION_FUNCTION_NAME (可选)": "false",
              "DIR_X (可选)": "false",
              "DIR_Y (可选)": "false",
              "DIR_Z (可选)": "false"
            }
          },
          "MISC": {
            "properties": {
              "NODAL_MASS (可选)": "false",
              "LOAD_TO_MASS (可选)": "false",
              "TENDON_PROFILE_NAMES (可选)": "false",
              "TENDON_PROFILE_POINT (可选)": "false",
              "INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS (可选)": "false",
              "SETTLEMENT_GROUP (可选)": "false",
              "SETTLEMENT_GROUP_VALUE (可选)": "false",
              "HEAT_OF_HYDRATION_VALUE (可选)": "false",
              "HEAT_OF_HYDRATION_FUNC_NAME (可选)": "false",
              "HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY (可选)": "false",
              "HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE (可选)": "false",
              "HEAT_OF_HYDRATION_HEAT_SOURCE (可选)": "false",
              "HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT (可选)": "false"
            }
          },
          "VIEW": {
            "properties": {
              "UCS_AXIS (可选)": "false",
              "VIEW_POINT (可选)": "false",
              "DESCRIPTION (可选)": "Blank",
              "LABEL_ORIENTATION (可选)": "0"
            }
          }
        }
      }
    }
  },
  "GRID_MODEL_LOAD_LINE (可选)": "false",
  "VIEWPORT_GIZMO (可选)": "false"
}
```

**第 1 层：`DISPLAY`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`DISPLAY.Argument`** — 8 个参数在这一层

- `"NODE"`: 是/否（布尔值） — Node
- `"ELEMENT"`: 对象（一组键值对） — Element Display Options
- `"PROPERTY"`: 对象（一组键值对） — Property Display Options
- `"GROUP_SELECTION"`: 字符串数组 — Select Load Group
- `"BOUNDARY"`: 对象（一组键值对） — Boundary Display Options
- `"LOAD"`: 对象（一组键值对） — Load Display Options
- `"MISC"`: 对象（一组键值对） — Miscellaneous Display Options
- `"VIEW"`: 对象（一组键值对） — View Display Options

**第 3 层：`DISPLAY.properties.Argument.properties.BOUNDARY.properties`** — 32 个参数在这一层

- `"SUPPORT"`: 是/否（布尔值） — Supportˢ³⁾
- `"SUPPORT_BY_DIRECTION"`: 是/否（布尔值） — Support by Directionˢ³⁾
- `"POINT_SPRING_SUPPORT"`: 是/否（布尔值） — Point Spring Supportˢ⁴⁾
- `"POINT_SPRING_SUPPORT_COMP_TENS"`: 是/否（布尔值） — Point Spring Support (Comp/Tens)ˢ⁴⁾
- `"POINT_SPRING_SUPPORT_MULTI_LINEAR"`: 是/否（布尔值） — Point Spring Support (Multi-Linear)ˢ⁴⁾
- `"POINT_SPRING_SUPPORT_BY_DIRECTION"`: 是/否（布尔值） — Point Spring Support by Directionˢ⁴⁾
- `"POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS"`: 是/否（布尔值） — Point Spring Support by Direction (Comp/Tens)ˢ⁴⁾
- `"POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR"`: 是/否（布尔值） — Point Spring Support by Direction (Multi-Linear)ˢ⁴⁾
- ... *还有 24 个参数*

**第 4 层：`DISPLAY.properties.Argument.properties.ELEMENT.properties`** — 12 个参数在这一层

- `"ELEM_NUMBER"`: 是/否（布尔值） — Element Number
- `"ELEM_NUMBER_WITH_BORDER"`: 是/否（布尔值） — Element Number with Border
- `"ELEM_TYPE_NUMBER"`: 是/否（布尔值） — Element Type Number
- `"ELEM_TYPE_NAME"`: 是/否（布尔值） — Element Type Name
- `"WALL_ID"`: 是/否（布尔值） — Wall IDᴳ⁾
- `"GAP"`: 是/否（布尔值） — Gap
- `"HOOK"`: 是/否（布尔值） — Hook
- `"CABLE"`: 是/否（布尔值） — Cable
- ... *还有 4 个参数*

**第 5 层：`DISPLAY.properties.Argument.properties.LOAD.properties`** — 38 个参数在这一层

- `"CASE_SELECTION"`: 对象（一组键值对） — Load Selection by Load Case
- `"LOAD_VALUE"`: 对象（一组键值对） — Load Value
- `"NODAL_BODY_FORCE"`: 是/否（布尔值） — Nodal Body Force
- `"NODAL_LOAD"`: 是/否（布尔值） — Nodal Load
- `"SPECIFIED_DISPLACEMENT"`: 是/否（布尔值） — Specified Displacement
- `"BEAM_LOAD"`: 是/否（布尔值） — Beam Load
- `"PRESTRESS_LOAD"`: 是/否（布尔值） — Prestress Load
- `"PRETENSION_LOAD"`: 是/否（布尔值） — Pretension Load
- ... *还有 30 个参数*

**第 6 层：`DISPLAY.properties.Argument.properties.MISC.properties`** — 13 个参数在这一层

- `"NODAL_MASS"`: 是/否（布尔值） — Nodal Mass
- `"LOAD_TO_MASS"`: 是/否（布尔值） — Load to Mass
- `"TENDON_PROFILE_NAMES"`: 是/否（布尔值） — Tendon Profile Name
- `"TENDON_PROFILE_POINT"`: 是/否（布尔值） — Tendon Profile Point
- `"INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS"`: 是/否（布尔值） — Initial Forces for Geometric Stiffness
- `"SETTLEMENT_GROUP"`: 是/否（布尔值） — Settlement Group
- `"SETTLEMENT_GROUP_VALUE"`: 是/否（布尔值） — Settlement Group Value• When Settlement Group is True
- `"HEAT_OF_HYDRATION_VALUE"`: 是/否（布尔值） — Value of Head of Hydration
- ... *还有 5 个参数*

**第 7 层：`DISPLAY.properties.Argument.properties.NODE.properties`** — 3 个参数在这一层

- `"NODE_NUMBER"`: 是/否（布尔值） — Node Number
- `"NODE_LOCAL_AXIS"`: 是/否（布尔值） — Node Local Axis
- `"STORY_NAME"`: 是/否（布尔值） — Story Nameᴳ⁾

**第 8 层：`DISPLAY.properties.Argument.properties.PROPERTY.properties`** — 11 个参数在这一层

- `"MATERIAL_NUMBER"`: 是/否（布尔值） — Material Numberˢ¹⁾
- `"MATERIAL_NAME"`: 是/否（布尔值） — Material Nameˢ¹⁾
- `"PROPERTY_NUMBER"`: 是/否（布尔值） — Property Numberˢ¹⁾
- `"PROPERTY_NAME"`: 是/否（布尔值） — Property Nameˢ¹⁾
- `"TAPERED_SECTION_GROUP"`: 是/否（布尔值） — Tapered Section Groupˢ¹⁾
- `"TIME_DEPENDENT_MATERIAL_LINK"`: 是/否（布尔值） — Time Dependent Material Linkˢ¹⁾
- `"SECTION_SHAPE"`: 是/否（布尔值） — Section Shape
- `"INELASTIC_HINGE_SYMBOL"`: 是/否（布尔值） — Inelastic Hing Symbolˢ²⁾
- ... *还有 3 个参数*

**第 9 层：`DISPLAY.properties.Argument.properties.VIEW.properties`** — 4 个参数在这一层

- `"UCS_AXIS"`: 是/否（布尔值） — UCS Axis
- `"VIEW_POINT"`: 是/否（布尔值） — View Point
- `"DESCRIPTION"`: 文字（字符串） — Description
- `"LABEL_ORIENTATION"`: 整数 — Label Orientation

**第 10 层：最外层**
这是整个 JSON 的入口。
- `"GRID_MODEL_LOAD_LINE"`: 是/否（布尔值） — Grid Model Load Lineᴶ⁾
- `"VIEWPORT_GIZMO"`: 是/否（布尔值） — Dynamic View Control


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `NODE` | 是/否（布尔值） | `false` | Node |
| `ELEMENT` | 对象（一组键值对） | `无` | Element Display Options |
| `PROPERTY` | 对象（一组键值对） | `无` | Property Display Options |
| `GROUP_SELECTION` | 字符串数组 | `All` | Select Load Group |
| `BOUNDARY` | 对象（一组键值对） | `无` | Boundary Display Options |
| `LOAD` | 对象（一组键值对） | `无` | Load Display Options |
| `MISC` | 对象（一组键值对） | `无` | Miscellaneous Display Options |
| `VIEW` | 对象（一组键值对） | `无` | View Display Options |
| `NODE_NUMBER` | 是/否（布尔值） | `false` | Node Number |
| `NODE_LOCAL_AXIS` | 是/否（布尔值） | `false` | Node Local Axis |
| `STORY_NAME` | 是/否（布尔值） | `false` | Story Nameᴳ⁾ |
| `ELEM_NUMBER` | 是/否（布尔值） | `false` | Element Number |
| `ELEM_NUMBER_WITH_BORDER` | 是/否（布尔值） | `false` | Element Number with Border |
| `ELEM_TYPE_NUMBER` | 是/否（布尔值） | `false` | Element Type Number |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"DISPLAY" → "Argument"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument，最后填入 `Argument` 的值
- `NODE` 的路径：**"DISPLAY" → "Argument" → "NODE"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, NODE，最后填入 `NODE` 的值
- `ELEMENT` 的路径：**"DISPLAY" → "Argument" → "ELEMENT"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, ELEMENT，最后填入 `ELEMENT` 的值
- `PROPERTY` 的路径：**"DISPLAY" → "Argument" → "PROPERTY"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, PROPERTY，最后填入 `PROPERTY` 的值
- `GROUP_SELECTION` 的路径：**"DISPLAY" → "Argument" → "GROUP_SELECTION"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, GROUP_SELECTION，最后填入 `GROUP_SELECTION` 的值
- `BOUNDARY` 的路径：**"DISPLAY" → "Argument" → "BOUNDARY"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, BOUNDARY，最后填入 `BOUNDARY` 的值
- `LOAD` 的路径：**"DISPLAY" → "Argument" → "LOAD"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, LOAD，最后填入 `LOAD` 的值
- `MISC` 的路径：**"DISPLAY" → "Argument" → "MISC"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, MISC，最后填入 `MISC` 的值
- `VIEW` 的路径：**"DISPLAY" → "Argument" → "VIEW"**
  意思是：在 JSON 中依次打开 DISPLAY, Argument, VIEW，最后填入 `VIEW` 的值
- `NODE_NUMBER` 的路径：**"DISPLAY" → "properties" → "Argument" → "properties" → "NODE" → "properties" → "NODE_NUMBER"**
  意思是：在 JSON 中依次打开 DISPLAY, properties, Argument, properties, NODE, properties, NODE_NUMBER，最后填入 `NODE_NUMBER` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

这个接口的参数之间没有复杂的依赖关系。每个参数可以独立填写。

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/view/DISPLAY"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {}

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

自动截图——写报告时，让程序自动截取每个结果视图，而不是手动截图几十次。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
2. **JSON 层级放错**：这个接口有 10 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：GROUP_SELECTION 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/view/DISPLAY`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Display 的 JSON 数据。"""
    data = {}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/view/DISPLAY", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

```python
# 使用 session 复用连接（比每次新建连接快 3-5 倍）
session = requests.Session()
session.verify = False

for i in range(100):
    data = {...}  # 你的数据
    r = session.post(f"{BASE}/view/DISPLAY", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Type of Display — `/view/RESULTGRAPHIC`

**方法**: POST | **参数**: 0 必填 + 24 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Argument` | 对象（一组键值对） | 否 |  |
| `TYPE_OF_DISPLAY` | 对象（一组键值对） | 否 | Type of Display¹⁾ |
| `CONTOUR` | 对象（一组键值对） | 否 | Contour Details²⁾ |
| `VALUES` | 对象（一组键值对） | 否 | Values Output Details³⁾ |
| `LEGEND` | 对象（一组键值对） | 否 | Legend Details⁴⁾ |
| `DEFORM` | 对象（一组键值对） | 否 | Deformation Details⁵⁾ |
| `DISP_OPT` | 对象（一组键值对） | 否 | Display Option Details⁶⁾ |
| `MIRRORED` | 对象（一组键值对） | 否 | Symmetric Model Mirror Detail⁷⁾ |
| `CUTTING_DIAGRAM` | 对象（一组键值对） | 否 | Cutting Diagram⁸⁾ |
| `CUTTING_PLANE` | 对象（一组键值对） | 否 | Cutting Plane Detail Dialog⁹⁾ |
| ... | ... | ... | *还有 14 个可选参数* |

**官方示例**：
```json
{
  "Argument": {
    "CURRENT_MODE": "beamdiagrams",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "PART": "total",
      "COMP": "Fx"
    },
    "DISPLAY_OPTIONS": {
      "FIDELITY": "Exact",
      "FILL": "line",
      "SCALE": 1.0
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "OPTIONS": {
          "GRADIENT_FILL": false,
          "CONTOUR_FILL": false
        }
      }
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true
    }
  }
}
```


---
