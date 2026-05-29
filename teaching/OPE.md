# OPE — 操作命令 API

OPE（Operation）部分包含分析和建模过程中的操作命令：划分单元、计算截面特性、运行分析等。这些接口通常在执行前后需要调用 DB 接口来准备数据或获取结果。

本章共 **13** 个接口。

## 工程背景

适合在建模完成后、分析前的自动化流程中使用。

## 接口列表

| 接口 | 方法 | 参数数 | 说明 |
|------|------|--------|------|
| `/ope/AUTOMESH` | POST | 22 (9 必填) |  |
| `/ope/DIVIDEELEM` | POST | 11 (3 必填) |  |
| `/ope/EDMP` | POST | 8 (4 必填) |  |
| `/ope/LINEBMLD` | POST | 25 (13 必填) |  |
| `/ope/MEMB` | POST | 4 (3 必填) | Assign Type• "MANUAL"• "AUTO" |
| `/ope/PROJECTSTATUS` | GET | 0 (0 必填) |  |
| `/ope/SECTPROP` | GET | 0 (0 必填) |  |
| `/ope/SSPS` | POST | 17 (15 必填) |  |
| `/ope/STOR` | POST | 6 (6 必填) | Seismic Accidental Eccentricity |
| `/ope/STORPROP` | POST | 4 (0 必填) | Force Unit of Response Unit Setting• "N", "KN", "KGF", "TONF |
| `/ope/STORY_IRR_PARAM` | GET, POST | 3 (3 必填) | Set Country Code• "NTC2018"• "NTC2012"• "NTC2008"• "KBC2009" |
| `/ope/STORY_PARAM` | GET, POST | 1 (1 必填) | Set Country Code• "NTC2012"• "NTC2008"• "KBC2009"• "NTC2012" |
| `/ope/USLC` | POST | 24 (4 必填) |  |


---

# 详细教程

## Project Status — `/ope/PROJECTSTATUS`

**HTTP 方法**: GET | **参数总数**: 0（0 必填 + 0 可选）

### 1. 这是什么？（工程含义）

**Project Status** — 这是一个操作/计算命令。

> 简单说：这个接口用来**Project Status**。

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

url = f"{BASE}/ope/PROJECTSTATUS"
r = requests.get(url, verify=False)
print(r.json())  # 查看返回结果
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/ope/PROJECTSTATUS`——多一个斜杠或少一个都会导致 404 错误。


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
    r = session.post(f"{BASE}/ope/PROJECTSTATUS", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

## Divide Elements — `/ope/DIVIDEELEM`

**HTTP 方法**: POST | **参数总数**: 11（3 必填 + 8 可选）

### 1. 这是什么？（工程含义）

**Divide Elements** — 这是一个操作/计算命令。

Divide Element ID Number

> 简单说：这个接口用来**Divide Elements**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "DIVIDEELEM": {
    "Argument (可选)": {},
    "Argument": {
      "TARGETS (可选)": 0,
      "START_NUMBER (可选)": "System",
      "DIVIDE": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "START_NUMBER": {
            "properties": {
              "NODE_NUMBER (可选)": {},
              "ELEM_NUMBER (可选)": {}
            }
          },
          "DIVIDE": {
            "properties": {
              "ELEM_TYPE": "<ELEM_TYPE>",
              "DIV_METHOD": "<DIV_METHOD>",
              "OPTION (可选)": {},
              "SUBDIVIDE_ELEM (可选)": false,
              "MERGE_DUPLICATE_NODES (可选)": {}
            }
          }
        }
      }
    }
  }
}
```

**第 1 层：`DIVIDEELEM`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`DIVIDEELEM.Argument`** — 3 个参数在这一层

- `"TARGETS"`: 整数数组 — Divide Element ID Number
- `"START_NUMBER"`: 对象（一组键值对） — Starting Node/Element Number
- `"DIVIDE"`: 对象（一组键值对） — Setting Divide

**第 3 层：`DIVIDEELEM.properties.Argument.properties.DIVIDE.properties`** — 5 个参数在这一层

- `"ELEM_TYPE"`: 文字（字符串） — Element Type• Line Element: "Frame"• Wall Element: "Wall"• Planar Element: "Planar"• Solid Element: 
- `"DIV_METHOD"`: 文字（字符串） — Divide Methods• Equal Distance: "Equal"• Unequal Distance: "Unequal"• Parametric Unequal Distance: "
- `"OPTION"`: 对象（一组键值对） — Divide Option
- `"SUBDIVIDE_ELEM"`: 是/否（布尔值） — Subdivide Frame Elements
- `"MERGE_DUPLICATE_NODES"`: 对象（一组键值对） — Merge Duplicate Nodes

**第 4 层：`DIVIDEELEM.properties.Argument.properties.START_NUMBER.properties`** — 2 个参数在这一层

- `"NODE_NUMBER"`: 对象（一组键值对） — Starting Node Number
- `"ELEM_NUMBER"`: 对象（一组键值对） — Starting Element Number


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `DIVIDE` | 对象（一组键值对） | `DIVIDEELEM.Argument.DIVIDE` | Setting Divide |
| `ELEM_TYPE` | 文字（字符串） | `DIVIDEELEM.properties.Argument.properties.DIVIDE.properties.ELEM_TYPE` | Element Type• Line Element: "Frame"• Wall Element: "Wall"• P |
| `DIV_METHOD` | 文字（字符串） | `DIVIDEELEM.properties.Argument.properties.DIVIDE.properties.DIV_METHOD` | Divide Methods• Equal Distance: "Equal"• Unequal Distance: " |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `TARGETS` | 整数数组 | `无` | Divide Element ID Number |
| `START_NUMBER` | 对象（一组键值对） | `System` | Starting Node/Element Number |
| `NODE_NUMBER` | 对象（一组键值对） | `无` | Starting Node Number |
| `ELEM_NUMBER` | 对象（一组键值对） | `无` | Starting Element Number |
| `OPTION` | 对象（一组键值对） | `` | Divide Option |
| `SUBDIVIDE_ELEM` | 是/否（布尔值） | `无` | Subdivide Frame Elements |
| `MERGE_DUPLICATE_NODES` | 对象（一组键值对） | `无` | Merge Duplicate Nodes |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"DIVIDEELEM" → "Argument"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, Argument，最后填入 `Argument` 的值
- `TARGETS` 的路径：**"DIVIDEELEM" → "Argument" → "TARGETS"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, Argument, TARGETS，最后填入 `TARGETS` 的值
- `START_NUMBER` 的路径：**"DIVIDEELEM" → "Argument" → "START_NUMBER"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, Argument, START_NUMBER，最后填入 `START_NUMBER` 的值
- `NODE_NUMBER` 的路径：**"DIVIDEELEM" → "properties" → "Argument" → "properties" → "START_NUMBER" → "properties" → "NODE_NUMBER"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, properties, Argument, properties, START_NUMBER, properties, NODE_NUMBER，最后填入 `NODE_NUMBER` 的值
- `ELEM_NUMBER` 的路径：**"DIVIDEELEM" → "properties" → "Argument" → "properties" → "START_NUMBER" → "properties" → "ELEM_NUMBER"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, properties, Argument, properties, START_NUMBER, properties, ELEM_NUMBER，最后填入 `ELEM_NUMBER` 的值
- `OPTION` 的路径：**"DIVIDEELEM" → "properties" → "Argument" → "properties" → "DIVIDE" → "properties" → "OPTION"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, properties, Argument, properties, DIVIDE, properties, OPTION，最后填入 `OPTION` 的值
- `SUBDIVIDE_ELEM` 的路径：**"DIVIDEELEM" → "properties" → "Argument" → "properties" → "DIVIDE" → "properties" → "SUBDIVIDE_ELEM"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, properties, Argument, properties, DIVIDE, properties, SUBDIVIDE_ELEM，最后填入 `SUBDIVIDE_ELEM` 的值
- `MERGE_DUPLICATE_NODES` 的路径：**"DIVIDEELEM" → "properties" → "Argument" → "properties" → "DIVIDE" → "properties" → "MERGE_DUPLICATE_NODES"**
  意思是：在 JSON 中依次打开 DIVIDEELEM, properties, Argument, properties, DIVIDE, properties, MERGE_DUPLICATE_NODES，最后填入 `MERGE_DUPLICATE_NODES` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `ELEM_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `DIV_METHOD` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/ope/DIVIDEELEM"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "DIVIDEELEM": {
#         "Argument": {
#             "DIVIDE": {}
#         },
#         "properties": {
#             "Argument": {
#                 "properties": {
#                     "DIVIDE": {
#                         "properties": {
#                             "ELEM_TYPE": "<ELEM_TYPE>",
#                             "DIV_METHOD": "<DIV_METHOD>"
#                         }
#                     }
#                 }
#             }
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

操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：DIVIDE、ELEM_TYPE、DIV_METHOD 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 4 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：TARGETS 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/ope/DIVIDEELEM`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Divide Elements 的 JSON 数据。"""
    data = {"DIVIDEELEM": {"Argument": {"DIVIDE": {}}, "properties": {"Argument": {"properties": {"DIVIDE": {"properties": {"ELEM_TYPE": "<ELEM_TYPE>", "DIV_METHOD": "<DIV_METHOD>"}}}}}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/ope/DIVIDEELEM", json=data, verify=False)
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
    r = session.post(f"{BASE}/ope/DIVIDEELEM", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Section Properties Calculation Results — `/ope/SECTPROP`

**方法**: GET | **参数**: 0 必填 + 0 可选

**官方示例**：
```json
{
  "SECTPROP": {
    "1": {
      "HEAD": [
        "Property",
        "Value",
        "Unit"
      ],
      "DATA": [
        [
          "Area",
          "0.011980",
          "m2"
        ],
        [
          "Asy",
          "0.007500",
          "m2"
        ],
        [
          "Asz",
          "0.003000",
          "m2"
        ],
        [
          "Ixx",
          "0.000001",
          "m4"
        ],
        [
          "Iyy",
          "0.000204",
          "m4"
        ],
        [
          "Izz",
          "0.000068",
          "m4"
        ],
        [
          "Cyp",
          "0.150000",
          "m"
        ],
        [
          "Cym",
          "0.150000",
          "m"
        ],
        [
          "Czp",
          "0.150000",
          "m"
        ],
        [
          "Czm",
          "0.150000",
          "m"
        ],
        [
          "Qyb",
          "0.073237",
          "m2"
        ],
        [
          "Qzb",
          "0.011250",
          "m2"
        ],
        [
          "Peri:O",
          "1.780000",
          "m"
        ],
        [
          "Peri:I",
          "0.000000",
          "m"
        ],
        [
          "Center:y",
          "0.150000",
          "m"
        ],
        [
          "Center:z",
          "0.150000",
          "m"
        ],
        [
          "y1",
          "-0.150000",
          "m"
        ],
        [
          "z1",
          "0.150000",
          "m"
        ],
        [
          "y2",
          "0.150000",
          "m"
        ],
        [
          "z2",
          "0.150000",
          "m"
        ],
        [
          "y3",
          "0.150000",
          "m"
        ],
        [
          "z3",
          "-0.150000",
          "m"
        ],
        [
          "y4",
          "-0.150000",
          "m"
        ],
        [
          "z4",
          "-0.150000",
          "m"
        ]
      ]
    }
  }
}
```


---

### Using Load Combinations — `/ope/USLC`

**方法**: POST | **参数**: 4 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `POSITION` | 文字（字符串） | **是** | Desing Combination Generate Position• Steel Design: "STEEL"• Concrete Design: "C |
| `LCOM_LIST` | Array[Object] | **是** | Select Combinations• Insert data as object |
| `TYPE` | 文字（字符串） | **是** | Load Combination Type• General: "GEN"• Steel Design: "STEEL"• Concrete Design: " |
| `NAME` | 文字（字符串） | **是** | Load Combination Name |
| `Argument` | 对象（一组键值对） | 否 |  |
| `PREFIX` | 文字（字符串） | 否 | Load Case & Design Combination Name |
| `LOADS` | 对象（一组键值对） | 否 | Select Loads |
| `SELF_WEIGHT` | 是/否（布尔值） | 否 | Self-Weight |
| `NODAL_BODY_FROCE` | 是/否（布尔值） | 否 | Nodal Body Force |
| `NODAL_LOAD` | 是/否（布尔值） | 否 | Nodal Load |
| `SPECIFIED_DISPLACEMENT` | 是/否（布尔值） | 否 | Specified Displacement |
| `BEAM_LOAD` | 是/否（布尔值） | 否 | Beam Load |
| `FLOOR_LOAD` | 是/否（布尔值） | 否 | Floor Load |
| `FINISHING_MATERIAL_LOAD` | 是/否（布尔值） | 否 | Finishing Material Load |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "USLC": {
    "Argument": {
      "POSITION": "<POSITION>",
      "LCOM_LIST": []
    },
    "properties": {
      "Argument": {
        "properties": {
          "LCOM_LIST": {
            "items": {
              "properties": {
                "TYPE": "<TYPE>",
                "NAME": "<NAME>"
              }
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
    "LCOM_LIST": [
      {
        "TYPE": "STEEL",
        "NAME": "sLCB1"
      }
    ],
    "PREFIX": "N",
    "POSITION": "STEEL",
    "LOADS": {
      "SELF_WEIGHT": true,
      "NODAL_BODY_FROCE": true,
      "NODAL_LOAD": true,
      "SPECIFIED_DISPLACEMENT": true,
      "BEAM_LOAD": true,
      "FLOOR_LOAD": true,
      "FINISHING_MATERIAL_LOAD": true,
      "PRESSURE_LOAD": true,
      "PLANE_LOAD": true,
      "SYSTEM_TEMPERATURE": true,
      "NODAL_TEMPERATURE": true,
      "ELEMENT_TEMPERATURE": true,
      "TEMPERATURE_GRADIENT": true,
      "BEAM_SECTION_TEMPERATURE": true,
      "PRESTRESS_LOAD": true,
      "PRETENSION_LOAD": true,
      "TENDON_PRESTRESS_LOAD": true
    }
  }
}
```


---

## Line Beam Load — `/ope/LINEBMLD`

**HTTP 方法**: POST | **参数总数**: 25（13 必填 + 12 可选）

### 1. 这是什么？（工程含义）

**Line Beam Load** — 这是一个操作/计算命令。

Load Case Name

> 简单说：这个接口用来**Line Beam Load**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "LINEBMLD": {
    "Argument (可选)": {},
    "Argument": {
      "LCNAME": "<LCNAME>",
      "GROUP_NAME (可选)": "<GROUP_NAME>",
      "ECCEN (可选)": {},
      "ADD_H (可选)": {},
      "COPY (可选)": {},
      "TYPE": 0,
      "TARGET": {},
      "LOAD": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "TARGET": {
            "properties": {
              "METHOD": 0,
              "ELEM": 0,
              "NODE": 0
            }
          },
          "ECCEN": {
            "properties": {
              "USE (可选)": "false",
              "I_END (可选)": {},
              "J_END (可选)": {},
              "USE_J_END (可选)": false,
              "DIR": "<DIR>"
            }
          },
          "LOAD": {
            "properties": {
              "USE_PROJECTION (可选)": "Systems",
              "D": [],
              "P": [],
              "A": {},
              "B": {},
              "C": {}
            }
          },
          "COPY": {
            "properties": {
              "AXIS (可选)": "<AXIS>",
              "DIST (可选)": "<DIST>"
            }
          }
        }
      }
    }
  }
}
```

**第 1 层：`LINEBMLD`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`LINEBMLD.Argument`** — 8 个参数在这一层

- `"LCNAME"`: 文字（字符串） — Load Case Name
- `"GROUP_NAME"`: 文字（字符串） — Load Group Name
- `"TYPE"`: 整数 — Distance Type• Relative (P(x) = ax**0.5 + b): 0• Absolute (P(x) = ax**2 + bx + c): 1
- `"TARGET"`: 对象（一组键值对） — Method, Elements and Nodes Information to load
- `"ECCEN"`: 对象（一组键值对） — Option - Eccentricity• It is available when "TYPE" value is as follows;◦ "CONLOAD"◦ "UNILOAD"◦ "TRAL
- `"ADD_H"`: 对象（一组键值对） — Option - Additional H from Top• It is available when "TYPE" value is as follows;◦ "UNIPRESSURE"◦ "TR
- `"LOAD"`: 对象（一组键值对） — Load
- `"COPY"`: 对象（一组键值对） — Copy Options

**第 3 层：`LINEBMLD.properties.Argument.properties.COPY.properties`** — 2 个参数在这一层

- `"AXIS"`: 文字（字符串） — Axis• "X", "Y", "Z"
- `"DIST"`: 文字（字符串） — Copy Distance• e.g.) 5, 3, 4.5, 3@5.0

**第 4 层：`LINEBMLD.properties.Argument.properties.ECCEN.properties`** — 5 个参数在这一层

- `"USE"`: 是/否（布尔值） — Activate option
- `"DIR"`: 文字（字符串） — Directions• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Global X: "GX"• Global Y: "GY"• Global Z: "
- `"I_END"`: Real — Eccentricity of I-node
- `"J_END"`: Real — Eccentricity of J-node• Available when the value of "USE_J_END" is true
- `"USE_J_END"`: 是/否（布尔值） — Activate option for J-node

**第 5 层：`LINEBMLD.properties.Argument.properties.LOAD.properties`** — 6 个参数在这一层

- `"USE_PROJECTION"`: 是/否（布尔值） — Projection• Defaults◦ "METHOD" = 0 then false◦ "METHOD" = 1 then true,
- `"D"`: Array[Real, 4] — Distance• x1: index 0• x2: index 1• x3: index 2• x4: index 3
- `"P"`: Array[Real, 4] — Magnitude• P1/M1/W1/w/p: index 0• P1/M1/W2: index 1• P1/M1/W3: index 2• P4/M4/W4: index 3
- `"A"`: Real — Value a in formula
- `"B"`: Real — Value b in formula
- `"C"`: Real — Value c in formula

**第 6 层：`LINEBMLD.properties.Argument.properties.TARGET.properties`** — 3 个参数在这一层

- `"METHOD"`: 整数 — Select Method to Load• On the loading line: 0• Selected Element: 1
- `"ELEM"`: 整数数组 — Elements to load
- `"NODE"`: Array[Integer, 2] — Nodes for loading line


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `LCNAME` | 文字（字符串） | `LINEBMLD.Argument.LCNAME` | Load Case Name |
| `TYPE` | 整数 | `LINEBMLD.Argument.TYPE` | Distance Type• Relative (P(x) = ax**0.5 + b): 0• Absolute (P |
| `TARGET` | 对象（一组键值对） | `LINEBMLD.Argument.TARGET` | Method, Elements and Nodes Information to load |
| `LOAD` | 对象（一组键值对） | `LINEBMLD.Argument.LOAD` | Load |
| `METHOD` | 整数 | `LINEBMLD.properties.Argument.properties.TARGET.properties.METHOD` | Select Method to Load• On the loading line: 0• Selected Elem |
| `ELEM` | 整数数组 | `LINEBMLD.properties.Argument.properties.TARGET.properties.ELEM` | Elements to load |
| `NODE` | Array[Integer, 2] | `LINEBMLD.properties.Argument.properties.TARGET.properties.NODE` | Nodes for loading line |
| `DIR` | 文字（字符串） | `LINEBMLD.properties.Argument.properties.ECCEN.properties.DIR` | Directions• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Glo |
| `D` | Array[Real, 4] | `LINEBMLD.properties.Argument.properties.LOAD.properties.D` | Distance• x1: index 0• x2: index 1• x3: index 2• x4: index 3 |
| `P` | Array[Real, 4] | `LINEBMLD.properties.Argument.properties.LOAD.properties.P` | Magnitude• P1/M1/W1/w/p: index 0• P1/M1/W2: index 1• P1/M1/W |
| `A` | Real | `LINEBMLD.properties.Argument.properties.LOAD.properties.A` | Value a in formula |
| `B` | Real | `LINEBMLD.properties.Argument.properties.LOAD.properties.B` | Value b in formula |
| `C` | Real | `LINEBMLD.properties.Argument.properties.LOAD.properties.C` | Value c in formula |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `GROUP_NAME` | 文字（字符串） | `无` | Load Group Name |
| `ECCEN` | 对象（一组键值对） | `无` | Option - Eccentricity• It is available when "TYPE" value is  |
| `ADD_H` | 对象（一组键值对） | `无` | Option - Additional H from Top• It is available when "TYPE"  |
| `COPY` | 对象（一组键值对） | `无` | Copy Options |
| `USE` | 是/否（布尔值） | `false` | Activate option |
| `I_END` | Real | `无` | Eccentricity of I-node |
| `J_END` | Real | `无` | Eccentricity of J-node• Available when the value of "USE_J_E |
| `USE_J_END` | 是/否（布尔值） | `无` | Activate option for J-node |
| `USE_PROJECTION` | 是/否（布尔值） | `Systems` | Projection• Defaults◦ "METHOD" = 0 then false◦ "METHOD" = 1  |
| `AXIS` | 文字（字符串） | `无` | Axis• "X", "Y", "Z" |
| `DIST` | 文字（字符串） | `无` | Copy Distance• e.g.) 5, 3, 4.5, 3@5.0 |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"LINEBMLD" → "Argument"**
  意思是：在 JSON 中依次打开 LINEBMLD, Argument，最后填入 `Argument` 的值
- `GROUP_NAME` 的路径：**"LINEBMLD" → "Argument" → "GROUP_NAME"**
  意思是：在 JSON 中依次打开 LINEBMLD, Argument, GROUP_NAME，最后填入 `GROUP_NAME` 的值
- `ECCEN` 的路径：**"LINEBMLD" → "Argument" → "ECCEN"**
  意思是：在 JSON 中依次打开 LINEBMLD, Argument, ECCEN，最后填入 `ECCEN` 的值
- `ADD_H` 的路径：**"LINEBMLD" → "Argument" → "ADD_H"**
  意思是：在 JSON 中依次打开 LINEBMLD, Argument, ADD_H，最后填入 `ADD_H` 的值
- `COPY` 的路径：**"LINEBMLD" → "Argument" → "COPY"**
  意思是：在 JSON 中依次打开 LINEBMLD, Argument, COPY，最后填入 `COPY` 的值
- `USE` 的路径：**"LINEBMLD" → "properties" → "Argument" → "properties" → "ECCEN" → "properties" → "USE"**
  意思是：在 JSON 中依次打开 LINEBMLD, properties, Argument, properties, ECCEN, properties, USE，最后填入 `USE` 的值
- `I_END` 的路径：**"LINEBMLD" → "properties" → "Argument" → "properties" → "ECCEN" → "properties" → "I_END"**
  意思是：在 JSON 中依次打开 LINEBMLD, properties, Argument, properties, ECCEN, properties, I_END，最后填入 `I_END` 的值
- `J_END` 的路径：**"LINEBMLD" → "properties" → "Argument" → "properties" → "ECCEN" → "properties" → "J_END"**
  意思是：在 JSON 中依次打开 LINEBMLD, properties, Argument, properties, ECCEN, properties, J_END，最后填入 `J_END` 的值
- `USE_J_END` 的路径：**"LINEBMLD" → "properties" → "Argument" → "properties" → "ECCEN" → "properties" → "USE_J_END"**
  意思是：在 JSON 中依次打开 LINEBMLD, properties, Argument, properties, ECCEN, properties, USE_J_END，最后填入 `USE_J_END` 的值
- `USE_PROJECTION` 的路径：**"LINEBMLD" → "properties" → "Argument" → "properties" → "LOAD" → "properties" → "USE_PROJECTION"**
  意思是：在 JSON 中依次打开 LINEBMLD, properties, Argument, properties, LOAD, properties, USE_PROJECTION，最后填入 `USE_PROJECTION` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `DIR`：Directions• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Global X: "GX"• Global Y: "GY"• Global Z: "GZ"When the load typ
- `TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `METHOD` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `DIR` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `D` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `P` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/ope/LINEBMLD"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "LINEBMLD": {
#         "Argument": {
#             "LCNAME": "<LCNAME>",
#             "TYPE": 0,
#             "TARGET": {},
#             "LOAD": {}
#         },
#         "properties": {
#             "Argument": {
#                 "properties": {
#                     "TARGET": {
#                         "properties": {
#                             "METHOD": 0,
#                             "ELEM": 0,
#                             "NODE": 0
#                         }
#                     },
#                     "ECCEN": {
#                         "properties": {
#                             "DIR": "<DIR>"
#                         }
#                     },
#                     "LOAD": {
#                         "properties": {
#                             "D": [],
#                             "P": [],
#                             "A": {},
#                             "B": {},
#                             "C": {}
#                         }
#                     }
#                 }
#             }
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

操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：LCNAME、TYPE、TARGET、LOAD、METHOD、ELEM、NODE、DIR、D、P、A、B、C 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 6 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：ELEM、NODE、D 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/ope/LINEBMLD`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Line Beam Load 的 JSON 数据。"""
    data = {"LINEBMLD": {"Argument": {"LCNAME": "<LCNAME>", "TYPE": 0, "TARGET": {}, "LOAD": {}}, "properties": {"Argument": {"properties": {"TARGET": {"properties": {"METHOD": 0, "ELEM": 0, "NODE": 0}}, "ECCEN": {"properties": {"DIR": "<DIR>"}}, "LOAD": {"properties": {"D": [], "P": [], "A": {}, "B": {}, "C": {}}}}}}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/ope/LINEBMLD", json=data, verify=False)
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
    r = session.post(f"{BASE}/ope/LINEBMLD", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Auto-Mesh Planar Area — `/ope/AUTOMESH`

**方法**: POST | **参数**: 9 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MESHER` | 对象（一组键值对） | **是** | Mesher |
| `MESH_SIZE` | 对象（一组键值对） | **是** | Mesh Size |
| `PROPERTY` | 对象（一组键值对） | **是** | Property |
| `DOMAIN_NAME` | 对象（一组键值对） | **是** | Domain Name |
| `TARGETS` | 整数数组 | **是** | Assign a Mesh Element |
| `LENGTH` | 数字 | **是** | Based on Length• Do not use with "DIV" |
| `DIV` | 数字 | **是** | Based on Division• Do not use with "LENGTH" |
| `MATERIAL` | 整数 | **是** | Select a Material for Mesh |
| `NAME` | 文字（字符串） | **是** | Domain Name |
| `Argument` | 对象（一组键值对） | 否 |  |
| `ADDITIONAL_OPTION` | 对象（一组键值对） | 否 | Additional Option |
| `METHOD` | 文字（字符串） | 否 | Auto Mesh Method• Nodes: "Nodes"• Line Elements: "Line Elements"• Planar Element |
| `TYPE` | 文字（字符串） | 否 | Meshing Type• Quadrilateral: "Quadrilateral"• Quad and Triangle: "Quad and Trian |
| `MESH_INNER_DOMAIN` | 是/否（布尔值） | 否 | Select Creating a Mesh in the Inner Domain |
| `INCLUDE_INTERIOR_NODES` | 对象（一组键值对） | 否 | Select Whether a Mesh is Generated Considering the Node within the Area. |
| `INCLUDE_INTERIOR_LINES` | 对象（一组键值对） | 否 | Select Whether a Mesh is Generated Considering the Line Elements within the Area |
| `INCLUDE_BOUNDARY_CONNECTIVITY` | 是/否（布尔值） | 否 | Decide Whether Connect Mesh Boundary |
| `ELEMENT_TYPE` | 文字（字符串） | 否 | Define Elements Type• "Plate"• "Plane Stress"• "Plane Strain"• "Axisymmetric" |
| `ELEMENT_SUB_TYPE` | 对象（一组键值对） | 否 | Defining Elements Sub Type |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "AUTOMESH": {
    "Argument": {
      "MESHER": {},
      "MESH_SIZE": {},
      "PROPERTY": {},
      "DOMAIN_NAME": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "MESHER": {
            "properties": {
              "TARGETS": 0
            }
          },
          "MESH_SIZE": {
            "properties": {
              "LENGTH": 0,
              "DIV": 0
            }
          },
          "PROPERTY": {
            "properties": {
              "MATERIAL": 0
            }
          },
          "DOMAIN_NAME": {
            "properties": {
              "NAME": "<NAME>"
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
    "MESHER": {
      "TARGETS": [
        1400,
        1397,
        1398,
        1399
      ]
    },
    "MESH_SIZE": {
      "LENGTH": 1
    },
    "PROPERTY": {
      "MATERIAL": 1,
      "THICKNESS": 1
    },
    "DOMAIN_NAME": {
      "NAME": "frame"
    }
  }
}
```


---

## Surface Spring — `/ope/SSPS`

**HTTP 方法**: POST | **参数总数**: 17（15 必填 + 2 可选）

### 1. 这是什么？（工程含义）

**Surface Spring** — 这是一个操作/计算命令。

Convert Method• Point Spring: "POINT_SPRING"• Elastic Link: "ELASTIC_LINK"

> 简单说：这个接口用来**Surface Spring**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "SSPS": {
    "Argument (可选)": {},
    "Argument": {
      "CONVERT_TO": "<CONVERT_TO>",
      "GROUP_NAME (可选)": "Blank",
      "NODE_ELEMS": {},
      "ELEMENT": {},
      "BOUNDARY": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "KEYS": 0
            }
          },
          "ELEMENT": {
            "properties": {
              "TYPE": "<TYPE>",
              "WIDTH": 0,
              "FACE": 0
            }
          },
          "BOUNDARY": {
            "properties": {
              "STIFF": 0,
              "bDAMP": false,
              "DAMP": 0,
              "DIR": 0,
              "SUBGRADE": 0,
              "PHU": 0,
              "LENGTH": 0
            }
          }
        }
      }
    }
  }
}
```

**第 1 层：`SSPS`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`SSPS.Argument`** — 5 个参数在这一层

- `"CONVERT_TO"`: 文字（字符串） — Convert Method• Point Spring: "POINT_SPRING"• Elastic Link: "ELASTIC_LINK"
- `"GROUP_NAME"`: 文字（字符串） — Boundary Group Name
- `"NODE_ELEMS"`: 对象（一组键值对） — Node / Element No.Input
- `"ELEMENT"`: 对象（一组键值对） — Element Type
- `"BOUNDARY"`: 对象（一组键值对） — Boundary Information

**第 3 层：`SSPS.properties.Argument.properties.BOUNDARY.properties`** — 7 个参数在这一层

- `"STIFF"`: Array[Number,3] — Stiffness• [Kx, Ky, Kz]
- `"bDAMP"`: 是/否（布尔值） — Consider Damping Constant / Area
- `"DAMP"`: Array[Number,3] — Damping Constant / Area• [Cx, Cy, Cz]
- `"DIR"`: 整数 — Boundary Direction• Normal(+): 0• Normal(-): 1• UCS-x(+): 2• UCS-x(-): 3• UCS-y(+): 4• UCS-y(-): 5• 
- `"SUBGRADE"`: 数字 — Modulus of Subgrade Reaction
- `"PHU"`: 数字 — Limit Strength
- `"LENGTH"`: 数字 — Length of Elastic Link

**第 4 层：`SSPS.properties.Argument.properties.ELEMENT.properties`** — 3 个参数在这一层

- `"TYPE"`: 文字（字符串） — Boundary Type• Linear: "LINEAR"• Compression-only: "COMP"• Tension-only: "TENS"• Multi-linear (Bi): 
- `"WIDTH"`: 数字 — Width• Only for Frame Type
- `"FACE"`: 整数 — face• Only for Solid(Face) Type• Face #1: 1• Face #2: 2• Face #3: 3• Face #4: 4• Face #5: 5• Face #6

**第 5 层：`SSPS.properties.Argument.properties.NODE_ELEMS.properties`** — 1 个参数在这一层

- `"KEYS"`: 整数数组 — • "KEYS": [101, 102, 103]


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `CONVERT_TO` | 文字（字符串） | `SSPS.Argument.CONVERT_TO` | Convert Method• Point Spring: "POINT_SPRING"• Elastic Link:  |
| `NODE_ELEMS` | 对象（一组键值对） | `SSPS.Argument.NODE_ELEMS` | Node / Element No.Input |
| `ELEMENT` | 对象（一组键值对） | `SSPS.Argument.ELEMENT` | Element Type |
| `BOUNDARY` | 对象（一组键值对） | `SSPS.Argument.BOUNDARY` | Boundary Information |
| `KEYS` | 整数数组 | `SSPS.properties.Argument.properties.NODE_ELEMS.properties.KEYS` | • "KEYS": [101, 102, 103] |
| `TYPE` | 文字（字符串） | `SSPS.properties.Argument.properties.ELEMENT.properties.TYPE` | Boundary Type• Linear: "LINEAR"• Compression-only: "COMP"• T |
| `WIDTH` | 数字 | `SSPS.properties.Argument.properties.ELEMENT.properties.WIDTH` | Width• Only for Frame Type |
| `FACE` | 整数 | `SSPS.properties.Argument.properties.ELEMENT.properties.FACE` | face• Only for Solid(Face) Type• Face #1: 1• Face #2: 2• Fac |
| `STIFF` | Array[Number,3] | `SSPS.properties.Argument.properties.BOUNDARY.properties.STIFF` | Stiffness• [Kx, Ky, Kz] |
| `bDAMP` | 是/否（布尔值） | `SSPS.properties.Argument.properties.BOUNDARY.properties.bDAMP` | Consider Damping Constant / Area |
| `DAMP` | Array[Number,3] | `SSPS.properties.Argument.properties.BOUNDARY.properties.DAMP` | Damping Constant / Area• [Cx, Cy, Cz] |
| `DIR` | 整数 | `SSPS.properties.Argument.properties.BOUNDARY.properties.DIR` | Boundary Direction• Normal(+): 0• Normal(-): 1• UCS-x(+): 2• |
| `SUBGRADE` | 数字 | `SSPS.properties.Argument.properties.BOUNDARY.properties.SUBGRADE` | Modulus of Subgrade Reaction |
| `PHU` | 数字 | `SSPS.properties.Argument.properties.BOUNDARY.properties.PHU` | Limit Strength |
| `LENGTH` | 数字 | `SSPS.properties.Argument.properties.BOUNDARY.properties.LENGTH` | Length of Elastic Link |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `GROUP_NAME` | 文字（字符串） | `Blank` | Boundary Group Name |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"SSPS" → "Argument"**
  意思是：在 JSON 中依次打开 SSPS, Argument，最后填入 `Argument` 的值
- `GROUP_NAME` 的路径：**"SSPS" → "Argument" → "GROUP_NAME"**
  意思是：在 JSON 中依次打开 SSPS, Argument, GROUP_NAME，最后填入 `GROUP_NAME` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `TYPE`：Boundary Type• Linear: "LINEAR"• Compression-only: "COMP"• Tension-only: "TENS"• Multi-linear (Bi): "MULTI"
- `WIDTH`：Width• Only for Frame Type
- `FACE`：face• Only for Solid(Face) Type• Face #1: 1• Face #2: 2• Face #3: 3• Face #4: 4• Face #5: 5• Face #6: 6
- `CONVERT_TO` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `KEYS` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `FACE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `DIR` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/ope/SSPS"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "SSPS": {
#         "Argument": {
#             "CONVERT_TO": "<CONVERT_TO>",
#             "NODE_ELEMS": {},
#             "ELEMENT": {},
#             "BOUNDARY": {}
#         },
#         "properties": {
#             "Argument": {
#                 "properties": {
#                     "NODE_ELEMS": {
#                         "properties": {
#                             "KEYS": 0
#                         }
#                     },
#                     "ELEMENT": {
#                         "properties": {
#                             "TYPE": "<TYPE>",
#                             "WIDTH": 0,
#                             "FACE": 0
#                         }
#                     },
#                     "BOUNDARY": {
#                         "properties": {
#                             "STIFF": 0,
#                             "bDAMP": true,
#                             "DAMP": 0,
#                             "DIR": 0,
#                             "SUBGRADE": 0,
#                             "PHU": 0,
#                             "LENGTH": 0
#                         }
#                     }
#                 }
#             }
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

操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：CONVERT_TO、NODE_ELEMS、ELEMENT、BOUNDARY、KEYS、TYPE、WIDTH、FACE、STIFF、bDAMP、DAMP、DIR、SUBGRADE、PHU、LENGTH 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 5 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：KEYS、STIFF、DAMP 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/ope/SSPS`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Surface Spring 的 JSON 数据。"""
    data = {"SSPS": {"Argument": {"CONVERT_TO": "<CONVERT_TO>", "NODE_ELEMS": {}, "ELEMENT": {}, "BOUNDARY": {}}, "properties": {"Argument": {"properties": {"NODE_ELEMS": {"properties": {"KEYS": 0}}, "ELEMENT": {"properties": {"TYPE": "<TYPE>", "WIDTH": 0, "FACE": 0}}, "BOUNDARY": {"properties": {"STIFF": 0, "bDAMP": true, "DAMP": 0, "DIR": 0, "SUBGRADE": 0, "PHU": 0, "LENGTH": 0}}}}}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/ope/SSPS", json=data, verify=False)
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
    r = session.post(f"{BASE}/ope/SSPS", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Change Property — `/ope/EDMP`

**方法**: POST | **参数**: 4 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No.Input |
| `PARAMETER` | 数字 | **是** | Parameter Value(a) |
| `H_VS` | 数字 | **是** | Change Property Value• Notional Size of Member: h• Volume Surface Ratio: v/s |
| `KEYS` | 整数数组 | **是** | • "KEYS": [101, 102, 103] |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TYPE` | 文字（字符串） | 否 | Change Property Method• Notional Size of Member: "NSM"• Volume Surface Ratio: "V |
| `AUTO` | 是/否（布尔值） | 否 | Auto Calculate• Volume Surface Ratio can only be false |
| `CODE` | 文字（字符串） | 否 | Code• Korean Standard: "Korean Standard"• CEB-FIP(1990): "CEB-FIP(1990)"• Japane |

**最简 JSON**：
```json
{
  "EDMP": {
    "Argument": {
      "NODE_ELEMS": {},
      "PARAMETER": 0,
      "H_VS": 0
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "KEYS": 0
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
    "NODE_ELEMS": {
      "KEYS": [
        1,
        2,
        3
      ]
    },
    "TYPE": "NSM",
    "AUTO": true,
    "CODE": "Korean Standard",
    "PARAMETER": 0.5
  }
}
```


---

## Story Calc OPT — `/ope/STOR`

**HTTP 方法**: POST | **参数总数**: 6（6 必填 + 0 可选）

### 1. 这是什么？（工程含义）

**Story Calc OPT** — 这是一个操作/计算命令。

Seismic Accidental Eccentricity

> 简单说：这个接口用来**Story Calc OPT**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "SEIS_ECC": {},
  "INC_SEIS_ECC": false,
  "SEIS_ECC_VALUE": 0,
  "WIND_ECC": {},
  "INC_WIND_ECC": false,
  "WIND_ECC_VALUE": 0
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"SEIS_ECC"`: 对象（一组键值对） — Seismic Accidental Eccentricity
- `"INC_SEIS_ECC"`: 是/否（布尔值） — Include Seismic Accidental Eccentricity
- `"SEIS_ECC_VALUE"`: 数字 — Value of Seismic Accidental Eccentricity(%)
- `"WIND_ECC"`: 对象（一组键值对） — Wind Eccentricity
- `"INC_WIND_ECC"`: 是/否（布尔值） — Include Wind Eccentricity
- `"WIND_ECC_VALUE"`: 数字 — Value of Wind Eccentricity(%)


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `SEIS_ECC` | 对象（一组键值对） | `SEIS_ECC` | Seismic Accidental Eccentricity |
| `INC_SEIS_ECC` | 是/否（布尔值） | `INC_SEIS_ECC` | Include Seismic Accidental Eccentricity |
| `SEIS_ECC_VALUE` | 数字 | `SEIS_ECC_VALUE` | Value of Seismic Accidental Eccentricity(%) |
| `WIND_ECC` | 对象（一组键值对） | `WIND_ECC` | Wind Eccentricity |
| `INC_WIND_ECC` | 是/否（布尔值） | `INC_WIND_ECC` | Include Wind Eccentricity |
| `WIND_ECC_VALUE` | 数字 | `WIND_ECC_VALUE` | Value of Wind Eccentricity(%) |


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

url = f"{BASE}/ope/STOR"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "SEIS_ECC": {},
#     "INC_SEIS_ECC": true,
#     "SEIS_ECC_VALUE": 0,
#     "WIND_ECC": {},
#     "INC_WIND_ECC": true,
#     "WIND_ECC_VALUE": 0
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

操作自动化——批量划分单元、批量计算截面特性，避免重复性手动操作。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：SEIS_ECC、INC_SEIS_ECC、SEIS_ECC_VALUE、WIND_ECC、INC_WIND_ECC、WIND_ECC_VALUE 是必填的，漏掉任何一个都会报错。
4. **URL 写错**：确认路径是 `/ope/STOR`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Story Calc OPT 的 JSON 数据。"""
    data = {"SEIS_ECC": {}, "INC_SEIS_ECC": true, "SEIS_ECC_VALUE": 0, "WIND_ECC": {}, "INC_WIND_ECC": true, "WIND_ECC_VALUE": 0}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/ope/STOR", json=data, verify=False)
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
    r = session.post(f"{BASE}/ope/STOR", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Story Check Parameter — `/ope/STORY_PARAM`

**方法**: GET, POST | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COUNTRY_CODE` | 文字（字符串） | **是** | Set Country Code• "NTC2012"• "NTC2008"• "KBC2009"• "NTC2012"• "NSR-10"• "NTC2018 |

**最简 JSON**：
```json
{
  "COUNTRY_CODE": "<COUNTRY_CODE>"
}
```


---

### Story Irregularity Check Parameter — `/ope/STORY_IRR_PARAM`

**方法**: GET, POST | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COUNTRY_CODE` | 文字（字符串） | **是** | Set Country Code• "NTC2018"• "NTC2012"• "NTC2008"• "KBC2009"• "NSR-10"• "NTCS202 |
| `STORY_DRIFT_METHOD` | 文字（字符串） | **是** | Story Drift Method• "Drift at the Center of Mass"• "Max. Drift of Outer Extreme  |
| `SEISMIC_BEHAVIOR_FACTOR` | 文字（字符串） | **是** | Seismic Behavior Factor• "4"• "3 or below" |

**最简 JSON**：
```json
{
  "COUNTRY_CODE": "<COUNTRY_CODE>",
  "STORY_DRIFT_METHOD": "<STORY_DRIFT_METHOD>",
  "SEISMIC_BEHAVIOR_FACTOR": "<SEISMIC_BEHAVIOR_FACTOR>"
}
```


---

### Story Properties — `/ope/STORPROP`

**方法**: POST | **参数**: 0 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FORCE_UNIT` | 文字（字符串） | 否 | Force Unit of Response Unit Setting• "N", "KN", "KGF", "TONF", "LBF", "KIPS" |
| `LENGTH_UNIT` | 文字（字符串） | 否 | Length Unit of Response Unit Setting• "M", "CM", "MM", "FT", "IN" |
| `FORMAT` | 文字（字符串） | 否 | Response Number Format• "Fixed", "Scientific" |
| `PLACE` | 文字（字符串） | 否 | Digit Place of Response Number Format• 0 to 15 |


---

### Member Assignment — `/ope/MEMB`

**方法**: POST | **参数**: 3 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ASSIGN_TYPE` | 文字（字符串） | **是** | Assign Type• "MANUAL"• "AUTO" |
| `SELETION_TYPE` | 文字（字符串） | **是** | Selection Type• "ALL"• "SELECTION" |
| `ALLOW_SINGLE` | 是/否（布尔值） | **是** | Allow Single Element Member |
| `ELEM_LIST` | Array | 否 | Element List |

**最简 JSON**：
```json
{
  "ASSIGN_TYPE": "<ASSIGN_TYPE>",
  "SELETION_TYPE": "<SELETION_TYPE>",
  "ALLOW_SINGLE": true
}
```


---
