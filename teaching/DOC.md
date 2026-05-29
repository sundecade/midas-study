# DOC — 项目管理 API

DOC 部分的 API 用于管理 MIDAS 项目文件：新建项目、打开已有项目、保存和关闭。这是最简单的部分，所有接口都只有 0-2 个参数，非常适合作为学习 API 的起点。

本章共 **11** 个接口。

## 工程背景

在工程实际操作中，你打开软件第一步就是新建或打开项目。DOC API 把这些操作变成了程序指令，让你可以自动化项目管理——比如批量处理多个模型文件。

## 接口列表

| 接口 | 方法 | 参数数 | 说明 |
|------|------|--------|------|
| `/doc/ANAL` | POST | 2 (1 必填) |  |
| `/doc/CLOSE` | POST | 1 (0 必填) |  |
| `/doc/EXPORT` | POST | 1 (0 必填) |  |
| `/doc/EXPORTMXT` | POST | 1 (0 必填) |  |
| `/doc/IMPORT` | POST | 1 (0 必填) |  |
| `/doc/IMPORTMXT` | POST | 1 (0 必填) |  |
| `/doc/NEW` | POST | 1 (0 必填) |  |
| `/doc/OPEN` | POST | 1 (0 必填) |  |
| `/doc/SAVE` | POST | 1 (0 必填) |  |
| `/doc/SAVEAS` | POST | 1 (0 必填) |  |
| `/doc/STAGAS` | POST | 2 (1 必填) | Save File Path |


---

# 详细教程

## New Project — `/doc/NEW`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**New Project** — 这是项目文件管理操作。

> 简单说：这个接口用来**New Project**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": {}
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 对象（一组键值对） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/NEW"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/NEW`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 New Project 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/NEW", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/NEW", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Open Project — `/doc/OPEN`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Open Project** — 这是项目文件管理操作。

> 简单说：这个接口用来**Open Project**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/OPEN"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/OPEN`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Open Project 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/OPEN", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/OPEN", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Close Project — `/doc/CLOSE`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Close Project** — 这是项目文件管理操作。

> 简单说：这个接口用来**Close Project**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": {}
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 对象（一组键值对） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/CLOSE"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/CLOSE`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Close Project 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/CLOSE", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/CLOSE", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Save — `/doc/SAVE`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Save** — 这是项目文件管理操作。

> 简单说：这个接口用来**Save**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": {}
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 对象（一组键值对） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/SAVE"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/SAVE`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Save 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/SAVE", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/SAVE", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Save As — `/doc/SAVEAS`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Save As** — 这是项目文件管理操作。

> 简单说：这个接口用来**Save As**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/SAVEAS"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/SAVEAS`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Save As 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/SAVEAS", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/SAVEAS", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Save Current Stage As — `/doc/STAGAS`

**HTTP 方法**: POST | **参数总数**: 2（1 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Save Current Stage As** — 这是项目文件管理操作。

Save File Path

> 简单说：这个接口用来**Save Current Stage As**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "EXPORT_PATH (可选)": "<EXPORT_PATH>",
  "STAGE_STEP": "<STAGE_STEP>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"EXPORT_PATH"`: 文字（字符串） — Save File Path
- `"STAGE_STEP"`: 文字（字符串） — Stage Step Name


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `STAGE_STEP` | 文字（字符串） | `STAGE_STEP` | Stage Step Name |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `EXPORT_PATH` | 文字（字符串） | `无` | Save File Path |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `EXPORT_PATH` 的路径：**"EXPORT_PATH"**
  意思是：在 JSON 中依次打开 EXPORT_PATH，最后填入 `EXPORT_PATH` 的值

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

url = f"{BASE}/doc/STAGAS"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "STAGE_STEP": "<STAGE_STEP>"
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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：STAGE_STEP 是必填的，漏掉任何一个都会报错。
4. **URL 写错**：确认路径是 `/doc/STAGAS`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Save Current Stage As 的 JSON 数据。"""
    data = {"STAGE_STEP": "<STAGE_STEP>"}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/doc/STAGAS", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/STAGAS", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Import to Json — `/doc/IMPORT`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Import to Json** — 这是项目文件管理操作。

> 简单说：这个接口用来**Import to Json**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/IMPORT"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/IMPORT`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Import to Json 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/IMPORT", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/IMPORT", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Import to mct/mgt — `/doc/IMPORTMXT`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Import to mct/mgt** — 这是项目文件管理操作。

> 简单说：这个接口用来**Import to mct/mgt**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/IMPORTMXT"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/IMPORTMXT`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Import to mct/mgt 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/IMPORTMXT", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/IMPORTMXT", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Export to Json — `/doc/EXPORT`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Export to Json** — 这是项目文件管理操作。

> 简单说：这个接口用来**Export to Json**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/EXPORT"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/EXPORT`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Export to Json 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/EXPORT", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/EXPORT", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Export to mct/mgt — `/doc/EXPORTMXT`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Export to mct/mgt** — 这是项目文件管理操作。

> 简单说：这个接口用来**Export to mct/mgt**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": "<Argument>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 文字（字符串） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 文字（字符串） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/doc/EXPORTMXT"

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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/doc/EXPORTMXT`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Export to mct/mgt 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/doc/EXPORTMXT", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/EXPORTMXT", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Perform Analysis — `/doc/ANAL`

**HTTP 方法**: POST | **参数总数**: 2（1 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**Perform Analysis** — 这是项目文件管理操作。

Input Analysis Type• "Pushover"

> 简单说：这个接口用来**Perform Analysis**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "Argument (可选)": {},
  "Argument": {
    "TYPE": "<TYPE>"
  }
}
```

**第 1 层：`Argument`** — 1 个参数在这一层

- `"TYPE"`: 文字（字符串） — Input Analysis Type• "Pushover"

**第 2 层：最外层**
这是整个 JSON 的入口。
- `"Argument"`: 对象（一组键值对） — 


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `TYPE` | 文字（字符串） | `Argument.TYPE` | Input Analysis Type• "Pushover" |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"Argument"**
  意思是：在 JSON 中依次打开 Argument，最后填入 `Argument` 的值

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

url = f"{BASE}/doc/ANAL"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "Argument": {
#         "TYPE": "<TYPE>"
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

自动化项目管理工作流——当你有几十个项目需要批量处理时，不需要手动逐个打开关闭。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：TYPE 是必填的，漏掉任何一个都会报错。
4. **URL 写错**：确认路径是 `/doc/ANAL`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Perform Analysis 的 JSON 数据。"""
    data = {"Argument": {"TYPE": "<TYPE>"}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/doc/ANAL", json=data, verify=False)
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
    r = session.post(f"{BASE}/doc/ANAL", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---
