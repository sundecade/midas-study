# POST — 后处理 API

POST 部分用于提取分析结果：内力表、位移表、振型结果、时程结果等。这些接口让你可以自动化读取计算结果，导出到 Excel 或做进一步处理。

本章共 **92** 个接口。

## 工程背景

批量提取结果、自动化报告生成的核心工具。

## 接口列表

| 接口 | 方法 | 参数数 | 说明 |
|------|------|--------|------|
| `/post/BEAMDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/BRACEDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/COLDFORMEDSTEELMEMBERDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/COLUMNDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/PM` | POST | 1 (0 必填) |  |
| `/post/SRCBEAMDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/SRCCOLUMNDESIGNFORCES SRC` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/STEELCODECHECK` | POST | 12 (0 必填) | Section Data |
| `/post/STEELMEMBERDESIGNFORCES` | POST | 17 (1 必填) | Table Name• Response Table Title |
| `/post/WALLDESIGNFORCES` | POST | 18 (1 必填) | Table Name• Response Table Title |
| `Average Compression Strainᴶ⁾` | POST | 19 (1 必填) |  |
| `Axisymmetric Force-Local` | POST | 21 (1 必填) |  |
| `Beam Force` | POST | 19 (1 必填) |  |
| `Beam ForceBeam Force-View by Max Value Item` | POST | 22 (1 必填) |  |
| `Beam Summary-DXBeam Summary-DYBeam Summary-DZBeam Summary-RYBeam Summary-RZ` | POST | 18 (1 必填) |  |
| `Buckling Mode` | POST | 18 (1 必填) |  |
| `Cable Force` | POST | 20 (1 必填) |  |
| `Capacity Irregularity Check(Weak Story)` | POST | 14 (2 必填) | Table Name• Response Table Title |
| `Composite Section for C.S. ForceComposite Section for C.S. Stress` | POST | 21 (1 必填) |  |
| `Criteria for Regularity in Plan` | POST | 12 (1 必填) | Table Name• Response Table Title |
| `Deformation-LumpedDeformation-DistributedDeformation-WallDeformation-TrussDeformation-Spring` | POST | 15 (1 必填) |  |
| `Displacement` | POST | 18 (1 必填) |  |
| `Displacement Result` | POST | 22 (8 必填) |  |
| `Displacement-LocalDisplacement-Global` | POST | 21 (1 必填) |  |
| `DisplacementVelocityAbsolute AccelerationRelative Acceleration` | POST | 18 (1 必填) |  |
| `Ductility Factor(D/D1)-LumpedDuctility Factor(D/D1)-DistributedDuctility Factor(D/D1)-WallDuctility Factor(D/D1)-TrussDuctility Factor(D/D1)-Spring` | POST | 14 (1 必填) |  |
| `Ductility Factor(D/D2)-LumpedDuctility Factor(D/D2)-DistributedDuctility Factor(D/D2)-WallDuctility Factor(D/D2)-TrussDuctility Factor(D/D2)-Spring` | POST | 14 (1 必填) |  |
| `Effective Span Length-TrussEffective Span Length-BeamEffective Span Length-Plate` | POST | 13 (1 必填) |  |
| `Elastic Link Result` | POST | 21 (7 必填) |  |
| `Elastic LinkView by Max Value Item` | POST | 21 (1 必填) |  |
| `Elastic Modulus Retention Rateᴶ⁾` | POST | 14 (1 必填) |  |
| `Element Properties at Each Stage` | POST | 15 (3 必填) |  |
| `Element Result(Beam, Truss)` | POST | 21 (7 必填) |  |
| `Element Result(Plate)` | POST | 21 (7 必填) |  |
| `Element Result(Truss, Beam, Plane Stress/Strain, Solid)` | POST | 21 (7 必填) |  |
| `Element Result(Wall)` | POST | 21 (7 必填) |  |
| `Element Result(Wall)` | POST | 21 (7 必填) |  |
| `Element Rotation-BeamElement Rotation-Wall` | POST | 14 (1 必填) |  |
| `Element Weight` | POST | 8 (1 必填) |  |
| `Equilibrium Element Nodal Force` | POST | 13 (1 必填) |  |
| `Estimate Yield Strength` | POST | 18 (1 必填) |  |
| `Event Stepᴶ⁾` | POST | 18 (1 必填) |  |
| `Event Time-LumpedEvent Time-DistributedEvent Time-WallEvent Time-TrussEvent Time-Spring` | POST | 14 (1 必填) |  |
| `Force-LumpedForce-DistributedForce-WallForce-TrussForce-Spring` | POST | 14 (1 必填) |  |
| `General Link ForceDeformation` | POST | 20 (1 必填) |  |
| `General Link ForceGeneral Link Force-View by Max Value ItemGeneral Link Deformation` | POST | 21 (1 必填) |  |
| `General Link Result` | POST | 21 (7 必填) |  |
| `General Link Result` | POST | 21 (7 必填) |  |
| `General Link Summary-DXGeneral Link Summary-DYGeneral Link Summary-DZGeneral Link Summary-RXGeneral Link Summary-RYGeneral Link Summary-RZ` | POST | 14 (1 必填) |  |
| `Initial Element Force` | POST | 13 (1 必填) |  |
| `Lack of Fit Force-Truss` | POST | 13 (1 必填) |  |
| `Load Summary` | POST | 4 (1 必填) |  |
| `Mass Summary` | POST | 4 (1 必填) |  |
| `Material` | POST | 4 (1 必填) |  |
| `Maximum Strain of The Cellᴶ⁾` | POST | 19 (1 必填) |  |
| `Nodal Body Force` | POST | 4 (1 必填) |  |
| `Nodal Results of RS-Inertia ForceNodal Results of RS-Acceleration` | POST | 19 (1 必填) |  |
| `Node Results` | POST | 22 (8 必填) |  |
| `Overturning Moment` | POST | 16 (1 必填) | Table Name• Response Table Title |
| `Pipe Cooling Nodal Temperature` | POST | 14 (1 必填) |  |
| `Plane Strain Force-Local` | POST | 21 (1 必填) |  |
| `Plane Stress Force-Local` | POST | 21 (1 必填) |  |
| `Plate Force-Local` | POST | 21 (1 必填) |  |
| `Reaction-LocalReaction-GlobalReaction-Local-Surface Spring` | POST | 20 (1 必填) |  |
| `Restraint Supports` | POST | 4 (1 必填) |  |
| `Resultant ForceResultant Force-View by Max Value Item` | POST | 22 (1 必填) |  |
| `Section` | POST | 4 (1 必填) |  |
| `Solid Force-Local` | POST | 20 (1 必填) |  |
| `Stiffness Irregularity Check (Soft Story)` | POST | 15 (2 必填) | Table Name• Response Table Title |
| `Story Axial Force Sum` | POST | 13 (1 必填) | Table Name• Response Table Title |
| `Story Displacement (X,Y,Combined)` | POST | 13 (1 必填) | Table Name• Response Table Title |
| `Story Drift (X,Y,Combined)` | POST | 25 (4 必填) | Table Name• Response Table Title |
| `Story Eccentricity` | POST | 12 (1 必填) | Table Name• Response Table Title |
| `Story Load Summary` | POST | 3 (1 必填) | Table Name (Output Title) |
| `Story Mass Summary` | POST | 12 (1 必填) | Table Name• Response Table Title |
| `Story Mode Shape` | POST | 13 (1 必填) | Table Name• Response Table Title |
| `Story Shear Force Ratio` | POST | 16 (1 必填) | Table Name• Response Table Title |
| `Story Shear(R.S Analysis) - Story Shear(for R.S)Story Shear(R.S.Analysis) - Story Shear Force Coefficient` | POST | 13 (1 必填) | Table Name• Response Table Title |
| `Story Stability Coefficient` | POST | 22 (1 必填) | Table Name• Response Table Title |
| `Story Weight` | POST | 3 (1 必填) | Table Name (Output Title) |
| `Stress-LocalStress-Global` | POST | 21 (1 必填) |  |
| `Temperature` | POST | 18 (1 必填) |  |
| `Tendon Coordinates` | POST | 13 (1 必填) |  |
| `Tensile Stress` | POST | 18 (1 必填) |  |
| `Torsional Amplification Factor` | POST | 15 (2 必填) | Table Name• Response Table Title |
| `Torsional Irregularity Check` | POST | 15 (2 必填) | Table Name• Response Table Title |
| `Truss Force` | POST | 20 (1 必填) |  |
| `Truss Force` | POST | 18 (1 必填) |  |
| `Truss Summary-DX` | POST | 18 (1 必填) |  |
| `Ultimate Story Shear For Check` | POST | 15 (1 必填) | Table Name• Response Table Title |
| `Vibartion Mode-EigenvalueVibartion Mode-Participation Vector` | POST | 18 (1 必填) |  |
| `Wall Force/Moment` | POST | 18 (1 必填) | Table Name• Response Table Title |


---

# 详细教程

## Element Weight Table — `Element Weight`

**HTTP 方法**: POST | **参数总数**: 8（1 必填 + 7 可选）

### 1. 这是什么？（工程含义）

**Element Weight Table** — 这是后处理结果提取操作。

Table Name• Response Table Title

> 简单说：这个接口用来**Element Weight Table**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "TABLE": {
    "Argument (可选)": {},
    "Argument": {
      "TABLE_NAME (可选)": "Empty",
      "EXPORT_PATH (可选)": "<EXPORT_PATH>",
      "NODE_ELEMS (可选)": "All",
      "TABLE_TYPE": "<TABLE_TYPE>"
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "KEYS (可选)": 0,
              "TO (可选)": "<TO>",
              "STRUCTURE_GROUP_NAME (可选)": "<STRUCTURE_GROUP_NAME>"
            }
          }
        }
      }
    }
  }
}
```

**第 1 层：`TABLE`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`TABLE.Argument`** — 4 个参数在这一层

- `"TABLE_NAME"`: 文字（字符串） — Table Name• Response Table Title
- `"TABLE_TYPE"`: 文字（字符串） — Result Table Type• "ELEMENTWEIGHT"
- `"EXPORT_PATH"`: 文字（字符串） — Result Table Save Path
- `"NODE_ELEMS"`: 对象（一组键值对） — Node / Element No. Input• Use Only One of the Three Methods

**第 3 层：`TABLE.properties.Argument.properties.NODE_ELEMS.properties`** — 3 个参数在这一层

- `"KEYS"`: 整数数组 — • "KEYS": [ 101, 102, 103 ]
- `"TO"`: 文字（字符串） — • "TO": "101 to 105"
- `"STRUCTURE_GROUP_NAME"`: 文字（字符串） — • "STRUCTURE_GROUP_NAME": "SG1"


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `TABLE_TYPE` | 文字（字符串） | `TABLE.Argument.TABLE_TYPE` | Result Table Type• "ELEMENTWEIGHT" |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `TABLE_NAME` | 文字（字符串） | `Empty` | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | `无` | Result Table Save Path |
| `NODE_ELEMS` | 对象（一组键值对） | `All` | Node / Element No. Input• Use Only One of the Three Methods |
| `KEYS` | 整数数组 | `无` | • "KEYS": [ 101, 102, 103 ] |
| `TO` | 文字（字符串） | `无` | • "TO": "101 to 105" |
| `STRUCTURE_GROUP_NAME` | 文字（字符串） | `无` | • "STRUCTURE_GROUP_NAME": "SG1" |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"TABLE" → "Argument"**
  意思是：在 JSON 中依次打开 TABLE, Argument，最后填入 `Argument` 的值
- `TABLE_NAME` 的路径：**"TABLE" → "Argument" → "TABLE_NAME"**
  意思是：在 JSON 中依次打开 TABLE, Argument, TABLE_NAME，最后填入 `TABLE_NAME` 的值
- `EXPORT_PATH` 的路径：**"TABLE" → "Argument" → "EXPORT_PATH"**
  意思是：在 JSON 中依次打开 TABLE, Argument, EXPORT_PATH，最后填入 `EXPORT_PATH` 的值
- `NODE_ELEMS` 的路径：**"TABLE" → "Argument" → "NODE_ELEMS"**
  意思是：在 JSON 中依次打开 TABLE, Argument, NODE_ELEMS，最后填入 `NODE_ELEMS` 的值
- `KEYS` 的路径：**"TABLE" → "properties" → "Argument" → "properties" → "NODE_ELEMS" → "properties" → "KEYS"**
  意思是：在 JSON 中依次打开 TABLE, properties, Argument, properties, NODE_ELEMS, properties, KEYS，最后填入 `KEYS` 的值
- `TO` 的路径：**"TABLE" → "properties" → "Argument" → "properties" → "NODE_ELEMS" → "properties" → "TO"**
  意思是：在 JSON 中依次打开 TABLE, properties, Argument, properties, NODE_ELEMS, properties, TO，最后填入 `TO` 的值
- `STRUCTURE_GROUP_NAME` 的路径：**"TABLE" → "properties" → "Argument" → "properties" → "NODE_ELEMS" → "properties" → "STRUCTURE_GROUP_NAME"**
  意思是：在 JSON 中依次打开 TABLE, properties, Argument, properties, NODE_ELEMS, properties, STRUCTURE_GROUP_NAME，最后填入 `STRUCTURE_GROUP_NAME` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `NODE_ELEMS`：Node / Element No. Input• Use Only One of the Three Methods
- `KEYS` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TO` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STRUCTURE_GROUP_NAME` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}Element Weight"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "TABLE": {
#         "Argument": {
#             "TABLE_TYPE": "<TABLE_TYPE>"
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

自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：TABLE_TYPE 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 3 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：KEYS 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `Element Weight`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Element Weight Table 的 JSON 数据。"""
    data = {"TABLE": {"Argument": {"TABLE_TYPE": "<TABLE_TYPE>"}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}Element Weight", json=data, verify=False)
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
    r = session.post(f"{BASE}Element Weight", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Nodal Body Force Table — `Nodal Body Force`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "NODALBODYFORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "NODALBODYFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\NodalBodyForce_Output.JSON"
  }
}
```


---

### Mass Summary Table — `Mass Summary`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "MASS_SUMMARY_X"• "MASS_SUMMARY_Y"• "MASS_SUMMARY_Z" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MASS_SUMMARY_X",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Mass_Summary_X_Output.JSON"
  }
}
```


---

### Load Summary Table — `Load Summary`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "LOAD_SUMMARY_X"• "LOAD_SUMMARY_Y"• "LOAD_SUMMARY_Z" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "LOAD_SUMMARY_X",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Load_Summary_X_Output.JSON"
  }
}
```


---

### Material Table — `Material`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "MATERIAL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MATERIAL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Material_Output.JSON"
  }
}
```


---

### Section Table — `Section`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "SECTIONALL"• "SECTIONCOMBINED"• "SECTIONCOMPOSITE"• "SECTION |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SECTIONALL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Section_Output.JSON"
  }
}
```


---

### Restraint Supports Table — `Restraint Supports`

**方法**: POST | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "SUPPORTS" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Result Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SUPPORTS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Supports_Output.JSON"
  }
}
```


---

### Story Mass Summary — `Story Mass Summary`

**方法**: POST | **参数**: 1 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_MASS"• "STORY_MASS_X"• "STORY_MASS_Y"• "STORY_MASS_Z" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```


---

### Story Load Summary — `Story Load Summary`

**方法**: POST | **参数**: 1 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name (Output Title) |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path (JSON Format) |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```


---

### Story Weight — `Story Weight`

**方法**: POST | **参数**: 1 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name (Output Title) |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path (JSON Format) |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```


---

### Reaction - Analysis Result Table — `Reaction-LocalReaction-GlobalReaction-Local-Surface Spring`

**方法**: POST | **参数**: 1 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Global: "REACTIONG"• Local: "REACTIONL"• Local-Surface Spring |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Global)",
    "TABLE_TYPE": "REACTIONG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Load",
      "FX",
      "FY",
      "FZ",
      "MX",
      "MY",
      "MZ",
      "Mb"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "DL(ST)"
    ]
  }
}
```


---

### Displacements - Analysis Result Table — `Displacement-LocalDisplacement-Global`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Global: "DISPLACEMENTG"• Local: "DISPLACEMENTL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Displacements(Global)",
    "TABLE_TYPE": "DISPLACEMENTG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Scientific",
      "PLACE": 3
    },
    "COMPONENTS": [
      "Node",
      "Load",
      "DX",
      "DY",
      "DZ",
      "RX",
      "RY",
      "RZ",
      "RW"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        43
      ]
    },
    "LOAD_CASE_NAMES": [
      "Self(ST)"
    ]
  }
}
```


---

### Truss Force - Analysis Result Table — `Truss Force`

**方法**: POST | **参数**: 1 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Truss Force: "TRUSSFORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "TrussForce",
    "TABLE_TYPE": "TRUSSFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Force-I",
      "Force-J"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        33
      ]
    },
    "LOAD_CASE_NAMES": [
      "DL(ST)"
    ]
  }
}
```


---

### Cable Force - Analysis Result Table — `Cable Force`

**方法**: POST | **参数**: 1 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Cable Force: "CABLEFORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "NodeI",
      "NodeJ",
      "Load",
      "Step",
      "Tension",
      "FX",
      "FY",
      "FZ",
      "Tension",
      "FX",
      "FY",
      "FZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "SelfWeight(ST)"
    ]
  }
}
```


---

### Beam Force - Analysis Result Table — `Beam ForceBeam Force-View by Max Value Item`

**方法**: POST | **参数**: 1 必填 + 21 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "BEAMFORCE"• Beam Force - View by Max Value Items |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `PARTS` | 字符串数组 | 否 | Element Part Number• "Part I"• "Part 1/4"• "Part 2/4"• "Part 3/4"• "Part J" |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 11 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "BeamForce",
    "TABLE_TYPE": "BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Part",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z",
      "Bi-Moment",
      "T-Moment",
      "W-Moment"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "Selfweight(ST)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ]
  }
}
```


---

### Plate Force (Local) - Analysis Result Table — `Plate Force-Local`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Plate Force - Local: "PLATEFORCEL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `AVERAGE_NODAL_RESULT` | 是/否（布尔值） | 否 | Average Nodal Result Option |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "PlateForce(Local)",
    "TABLE_TYPE": "PLATEFORCEL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Node",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        592
      ]
    },
    "LOAD_CASE_NAMES": [
      "DL(ST)"
    ],
    "AVERAGE_NODAL_RESULT": true
  }
}
```


---

### Plane Force (Local) - Analysis Result Table — `Plane Stress Force-Local`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Plane Force - Local: "PLANESTRESSFL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `AVERAGE_NODAL_RESULT` | 是/否（布尔值） | 否 | Average Nodal Result Option |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "PlaneForce(Local)",
    "TABLE_TYPE": "PLANESTRESSFL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Node",
      "Fx",
      "Fy"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "DeadLoads(ST)"
    ],
    "AVERAGE_NODAL_RESULT": true
  }
}
```


---

### Plane Strain Force (Local) - Analysis Result Table — `Plane Strain Force-Local`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Plane Strain Force - Local: "PLANESTRAINFL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `AVERAGE_NODAL_RESULT` | 是/否（布尔值） | 否 | Average Nodal Result Option |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainForce(Local)",
    "TABLE_TYPE": "PLANESTRAINFL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Node",
      "Fx",
      "Fy",
      "Fz"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "DeadLoads(ST)"
    ],
    "AVERAGE_NODAL_RESULT": true
  }
}
```


---

### Axisymmetric Force (Local) - Analysis Result Table — `Axisymmetric Force-Local`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Axisymmetric Force - Local: "AXISYMMETRICFL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `AVERAGE_NODAL_RESULT` | 是/否（布尔值） | 否 | Average Nodal Result Option |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "AxisymmetricForce(Local)",
    "TABLE_TYPE": "AXISYMMETRICFL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Node",
      "Fx",
      "Fy",
      "Fz"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        168
      ]
    },
    "LOAD_CASE_NAMES": [
      "Pressure(ST)"
    ],
    "AVERAGE_NODAL_RESULT": true
  }
}
```


---

### Solid Force (Local) - Analysis Result Table — `Solid Force-Local`

**方法**: POST | **参数**: 1 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Solid Force - Local: "SOLIDFL" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "SolidForce(Local)",
    "TABLE_TYPE": "SOLIDFL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Node",
      "Fx",
      "Fy",
      "Fz"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        3381
      ]
    },
    "LOAD_CASE_NAMES": [
      "DL(ST)"
    ]
  }
}
```


---

### Elastic Link - Analysis Result Table — `Elastic LinkView by Max Value Item`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Elastic Link: "ELASTICLINK"• Elastic Link - View by Max Value |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "ElasticLink",
    "TABLE_TYPE": "ELASTICLINK",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "No.",
      "Load",
      "Node",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "SWofGirders(ST)"
    ]
  }
}
```


---

### General Link - Analysis Result Table — `General Link ForceGeneral Link Force-View by Max Value ItemGeneral Link Deformation`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Force: "GENERAL_LINK_FORCE"• Deformation: "GENERAL_LINK_DEFOR |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Force",
    "TABLE_TYPE": "GENERAL_LINK_FORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "No.",
      "Load",
      "Node",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "SWofGirders(ST)"
    ]
  }
}
```


---

### Resultant Forces - Analysis Result Table — `Resultant ForceResultant Force-View by Max Value Item`

**方法**: POST | **参数**: 1 必填 + 21 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Force: "RESULTANT_FORCES"• Force - View by Max Value Items: " |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `PARTS` | 字符串数组 | 否 | Element Part Number• "Part I"• "Part J" |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 11 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "ResultantForces",
    "TABLE_TYPE": "RESULTANT_FORCES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "VirtualBeam",
      "Load",
      "Part",
      "Axial",
      "Shear-Y",
      "Shear-Z",
      "Torsion",
      "Moment-Y",
      "Moment-Z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "SWofGirders(ST)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ]
  }
}
```


---

### Vibration Mode Shape - Analysis Result Table — `Vibartion Mode-EigenvalueVibartion Mode-Participation Vector`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Eigenvalue Mode: "EIGENVALUEMODE"• Participation Vector Mode: |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `MODES` | Array [string] | 否 | Mode Number• "Mode " + "#" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "EigenvalueMode",
    "TABLE_TYPE": "EIGENVALUEMODE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Scientific",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Mode",
      "UX",
      "UY",
      "UZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "MODES": [
      "Mode1",
      "Mode2"
    ]
  }
}
```


---

### Buckling Mode Shape - Analysis Result Table — `Buckling Mode`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Buckling Mode Shape: "BUCKLINGMODE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `MODES` | Array [string] | 否 | Mode Number• "Mode " + "#" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "BucklingMode",
    "TABLE_TYPE": "BUCKLINGMODE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Scientific",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Mode",
      "UX",
      "UY",
      "UZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "MODES": [
      "Mode1",
      "Mode2"
    ]
  }
}
```


---

### Effective Span Length - Analysis Result Table — `Effective Span Length-TrussEffective Span Length-BeamEffective Span Length-Plate`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Truss: "EFFECTIVE_LENGTH_TRUSS"• Beam: "EFFECTIVE_LENGTH_BEAM |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "EffectiveSpanLength-Truss",
    "TABLE_TYPE": "EFFECTIVE_LENGTH_TRUSS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Element",
      "Lane",
      "Max",
      "Min"
    ]
  }
}
```


---

### Nodal Results of RS - Analysis Result Table — `Nodal Results of RS-Inertia ForceNodal Results of RS-Acceleration`

**方法**: POST | **参数**: 1 必填 + 18 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Nodal Inertia Force: "RS_NODAL_INERTIA"• Nodal Acceleration:  |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Response Spectrum◦ NAME + "(RS)" |
| `MODES` | Array [string] | 否 | Mode Number• "Mode " + "#" |
| `FORCE` | 文字（字符串） | 否 | Force |
| ... | ... | ... | *还有 8 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "NodalInertiaforce",
    "TABLE_TYPE": "RS_NODAL_INERTIA",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "LoadCase",
      "Mode",
      "Node",
      "FX",
      "FY",
      "FZ",
      "MX",
      "MY",
      "MZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        30
      ]
    },
    "LOAD_CASE_NAMES": [
      "X-dir(RS)",
      "Y-dir(RS)"
    ],
    "MODES": [
      "Mode1",
      "Mode2"
    ]
  }
}
```


---

### Tendon Coordinates - Analysis Result Table — `Tendon Coordinates`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Tendon Coordinates: "TNDN_COORDINATES" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "TendonCoordinates",
    "TABLE_TYPE": "TNDN_COORDINATES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "TendonName",
      "No",
      "x",
      "y",
      "z"
    ]
  }
}
```


---

### Composite Section for C.S. (Force and Stress) - Analysis Result Table — `Composite Section for C.S. ForceComposite Section for C.S. Stress`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Composite Section for C.S. - Force: "COMPSECTBEAMFORCE"• Comp |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `PARTS` | 字符串数组 | 否 | Element Part Number• "Part I"• "Part 1/4"• "Part 2/4"• "Part 3/4"• "Part J" |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation - Construction Stage Step |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "BeamForce",
    "TABLE_TYPE": "COMPSECTBEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "SectionPart",
      "Part",
      "Axial",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "DL(CBSC)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ]
  }
}
```


---

### Element Properties at Each Stage - Analysis Result Table — `Element Properties at Each Stage`

**方法**: POST | **参数**: 3 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Element Properties at Each Stage: "ELEM_PROP_EACH_STAGE" |
| `ADDITIONAL` | 对象（一组键值对） | **是** | Additional Input |
| `SET_STAGE` | 对象（一组键值对） | **是** | Set Stage |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>",
      "ADDITIONAL": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "ADDITIONAL": {
            "properties": {
              "SET_STAGE": {}
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
    "TABLE_NAME": "ElementPropertiesatEachStage",
    "TABLE_TYPE": "ELEM_PROP_EACH_STAGE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "StartAge",
      "EndAge",
      "StartElasticity",
      "EndElasticity",
      "CumulativeShrinkage",
      "CreepCoeff."
    ],
    "ADDITIONAL": {
      "SET_STAGE": {
        "STAGE": "CS14"
      }
    }
  }
}
```


---

### Lack of Fit Force (Truss) - Analysis Result Table — `Lack of Fit Force-Truss`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Lack-of-Fit-Force - Truss: "LACK_OF_FIT_FORCE_TRUSS" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lack-of-Fit-Force-Truss",
    "TABLE_TYPE": "LACK_OF_FIT_FORCE_TRUSS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "NodeI",
      "NodeJ",
      "Pretension",
      "LOFForce",
      "SUM",
      "LocalVector/V-X",
      "LocalVector/V-Y",
      "LocalVector/V-Z",
      "Angle",
      "Elasticity",
      "Area",
      "I-NodeDisp./DX",
      "I-NodeDisp./DY",
      "I-NodeDisp./DZ",
      "J-NodeDisp./DX",
      "J-NodeDisp./DY",
      "J-NodeDisp./DZ",
      "Deform"
    ]
  }
}
```


---

### Equilibrium Element Nodal Force - Analysis Result Table — `Equilibrium Element Nodal Force`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Equilibrium Element Nodal Force: "EQUILIBRIUM_ELEM_FORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "EquilibriumElementNodalForce",
    "TABLE_TYPE": "EQUILIBRIUM_ELEM_FORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Type",
      "ID",
      "ElementNodalForce-i/Fx",
      "ElementNodalForce-i/Fy",
      "ElementNodalForce-i/Fz",
      "ElementNodalForce-i/Mx",
      "ElementNodalForce-i/My",
      "ElementNodalForce-i/Mz",
      "ElementNodalForce-j/Fx",
      "ElementNodalForce-j/Fy",
      "ElementNodalForce-j/Fz",
      "ElementNodalForce-j/Mx",
      "ElementNodalForce-j/My",
      "ElementNodalForce-j/Mz"
    ]
  }
}
```


---

### Initial Element Force - Analysis Result Table — `Initial Element Force`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Initial Element Force: "INITIAL_ELEM_FORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "InitialElementForce",
    "TABLE_TYPE": "INITIAL_ELEM_FORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Type",
      "ID",
      "MemberForce-i/Axial",
      "MemberForce-i/Shear(y)",
      "MemberForce-i/Shear(z)",
      "MemberForce-i/Torsion",
      "MemberForce-i/Moment(y)",
      "MemberForce-i/Moment(z)",
      "MemberForce-j/Axial",
      "MemberForce-j/Shear(y)",
      "MemberForce-j/Shear(z)",
      "MemberForce-j/Torsion",
      "MemberForce-j/Moment(y)",
      "MemberForce-j/Moment(z)"
    ]
  }
}
```


---

### Wall Force - Analysis Result Table — `Wall Force/Moment`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "WALL_FORCE_MOMENT" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "WALL_FORCE_MOMENT",
    "TABLE_TYPE": "WALL_FORCE_MOMENT",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1,
        2,
        3
      ]
    },
    "LOAD_CASE_NAMES": [
      "gLCB6(CB)"
    ],
    "STORY_NAMES": [
      "1F"
    ],
    "COMPONENTS": [
      "Story",
      "Level",
      "Wall",
      "Load",
      "Part",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z",
      "Part",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ]
  }
}
```


---

## Story Drift(X,Y,Combine) - Story Result Table — `Story Drift (X,Y,Combined)`

**HTTP 方法**: POST | **参数总数**: 25（4 必填 + 21 可选）

### 1. 这是什么？（工程含义）

**Story Drift(X,Y,Combine) - Story Result Table** — 这是后处理结果提取操作。

Table Name• Response Table Title

> 简单说：这个接口用来**Story Drift(X,Y,Combine) - Story Result Table**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "TABLE_NAME (可选)": "Empty",
  "EXPORT_PATH (可选)": "<EXPORT_PATH>",
  "HEAT (可选)": "<HEAT>",
  "TEMP (可选)": "<TEMP>",
  "COMPONENTS (可选)": "<COMPONENTS>",
  "NAME (可选)": "<NAME>",
  "FACTOR (可选)": 0,
  "SET_STORY_DRIFT_CALCULATION_METHOD (可选)": "\"DRIFT_AT_THE_CENTER_OF_MASS\"",
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>",
    "UNIT (可选)": "System",
    "STYLES (可选)": "System",
    "LOAD_CASE_NAMES (可选)": "All",
    "ADDITIONAL (可选)": {},
    "UNIT": {
      "FORCE (可选)": "<FORCE>",
      "DIST (可选)": "<DIST>"
    },
    "STYLES": {
      "FORMAT (可选)": "<FORMAT>",
      "PLACE (可选)": 0
    },
    "ADDITIONAL": {
      "SET_STORY_DRIFT_PARAMS (可选)": {},
      "SET_STORY_DRIFT_PARAMS": {
        "BETA": {
          "FIX_USER_CHECK (可选)": "\"FIXED\"",
          "NAME_FROM (可选)": "<NAME_FROM>",
          "NAME_TO (可选)": "<NAME_TO>",
          "VALUE (可选)": "0"
        }
      }
    }
  },
  "X_DIR": 0,
  "Y_DIR": 0,
  "COMBINED": 0
}
```

**第 1 层：`Argument`** — 5 个参数在这一层

- `"TABLE_TYPE"`: 文字（字符串） — Result Table Type• X-Direction: "STORY_DRIFT_X"• Y-Direction: "STORY_DRIFT_Y"• XY-Direction : "STORY
- `"UNIT"`: 对象（一组键值对） — Response Unit Setting
- `"STYLES"`: 对象（一组键值对） — Response Number Format
- `"LOAD_CASE_NAMES"`: 字符串数组 — Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "(CB)"• Response Spect
- `"ADDITIONAL"`: 对象（一组键值对） — Additional Setting

**第 2 层：`Argument.ADDITIONAL`** — 1 个参数在这一层

- `"SET_STORY_DRIFT_PARAMS"`: 对象（一组键值对） — Set Story Drift Parameters Setting

**第 3 层：`Argument.ADDITIONAL.SET_STORY_DRIFT_PARAMS.BETA`** — 4 个参数在这一层

- `"FIX_USER_CHECK"`: 文字（字符串） — Beta value method• "FIXED" : fixed value, 1.0• "USER" : user defined values for each story can be di
- `"NAME_FROM"`: 文字（字符串） — Set Start Story to use beta value• When only set "FIX_USER_CHECK": "USER"
- `"NAME_TO"`: 文字（字符串） — Set End Story to use beta value• When only set "FIX_USER_CHECK": "USER"
- `"VALUE"`: 数字 — User defined beta value• When only set "FIX_USER_CHECK": "USER

**第 4 层：`Argument.STYLES`** — 2 个参数在这一层

- `"FORMAT"`: 文字（字符串） — Number Format• "Default"• "Fixed"• "Scientific"• "General"
- `"PLACE"`: 整数 — Digit Place• 0 to 15

**第 5 层：`Argument.UNIT`** — 2 个参数在这一层

- `"FORCE"`: 文字（字符串） — Force
- `"DIST"`: 文字（字符串） — Length

**第 6 层：最外层**
这是整个 JSON 的入口。
- `"TABLE_NAME"`: 文字（字符串） — Table Name• Response Table Title
- `"EXPORT_PATH"`: 文字（字符串） — Result Table Save Path
- `"HEAT"`: 文字（字符串） — Heat
- `"TEMP"`: 文字（字符串） — Temperature
- `"COMPONENTS"`: 字符串数组 — Components of Result Table
- `"NAME"`: 文字（字符串） — Vertical Load Case Name
- `"FACTOR"`: 数字 — Vertical Load Factor
- `"SET_STORY_DRIFT_CALCULATION_METHOD"`: Object [String] — Set Additional Story Drift Calculation Method• "DRIFT_AT_THE_CENTER_OF_MASS"• "AVERAGE_DRIFT_OF_VERT
- ... *还有 3 个参数*


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `TABLE_TYPE` | 文字（字符串） | `Argument.TABLE_TYPE` | Result Table Type• X-Direction: "STORY_DRIFT_X"• Y-Direction |
| `X_DIR` | 整数数组 | `X_DIR` | X Direction |
| `Y_DIR` | 整数数组 | `Y_DIR` | Y Direction |
| `COMBINED` | 整数数组 | `COMBINED` | Combined |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `TABLE_NAME` | 文字（字符串） | `Empty` | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | `无` | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | `System` | Response Unit Setting |
| `FORCE` | 文字（字符串） | `无` | Force |
| `DIST` | 文字（字符串） | `无` | Length |
| `HEAT` | 文字（字符串） | `无` | Heat |
| `TEMP` | 文字（字符串） | `无` | Temperature |
| `STYLES` | 对象（一组键值对） | `System` | Response Number Format |
| `FORMAT` | 文字（字符串） | `无` | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | `无` | Digit Place• 0 to 15 |
| `COMPONENTS` | 字符串数组 | `无` | Components of Result Table |
| `LOAD_CASE_NAMES` | 字符串数组 | `All` | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Com |
| `ADDITIONAL` | 对象（一组键值对） | `无` | Additional Setting |
| `SET_STORY_DRIFT_PARAMS` | 对象（一组键值对） | `无` | Set Story Drift Parameters Setting |
| `NAME` | 文字（字符串） | `` | Vertical Load Case Name |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `TABLE_NAME` 的路径：**"TABLE_NAME"**
  意思是：在 JSON 中依次打开 TABLE_NAME，最后填入 `TABLE_NAME` 的值
- `EXPORT_PATH` 的路径：**"EXPORT_PATH"**
  意思是：在 JSON 中依次打开 EXPORT_PATH，最后填入 `EXPORT_PATH` 的值
- `UNIT` 的路径：**"Argument" → "UNIT"**
  意思是：在 JSON 中依次打开 Argument, UNIT，最后填入 `UNIT` 的值
- `FORCE` 的路径：**"Argument" → "UNIT" → "FORCE"**
  意思是：在 JSON 中依次打开 Argument, UNIT, FORCE，最后填入 `FORCE` 的值
- `DIST` 的路径：**"Argument" → "UNIT" → "DIST"**
  意思是：在 JSON 中依次打开 Argument, UNIT, DIST，最后填入 `DIST` 的值
- `HEAT` 的路径：**"HEAT"**
  意思是：在 JSON 中依次打开 HEAT，最后填入 `HEAT` 的值
- `TEMP` 的路径：**"TEMP"**
  意思是：在 JSON 中依次打开 TEMP，最后填入 `TEMP` 的值
- `STYLES` 的路径：**"Argument" → "STYLES"**
  意思是：在 JSON 中依次打开 Argument, STYLES，最后填入 `STYLES` 的值
- `FORMAT` 的路径：**"Argument" → "STYLES" → "FORMAT"**
  意思是：在 JSON 中依次打开 Argument, STYLES, FORMAT，最后填入 `FORMAT` 的值
- `PLACE` 的路径：**"Argument" → "STYLES" → "PLACE"**
  意思是：在 JSON 中依次打开 Argument, STYLES, PLACE，最后填入 `PLACE` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `NAME_FROM`：Set Start Story to use beta value• When only set "FIX_USER_CHECK": "USER"
- `NAME_TO`：Set End Story to use beta value• When only set "FIX_USER_CHECK": "USER"
- `VALUE`：User defined beta value• When only set "FIX_USER_CHECK": "USER
- `TABLE_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `FIX_USER_CHECK` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `NAME_FROM` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `NAME_TO` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `VALUE` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}Story Drift (X,Y,Combined)"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "Argument": {
#         "TABLE_TYPE": "<TABLE_TYPE>"
#     },
#     "X_DIR": 0,
#     "Y_DIR": 0,
#     "COMBINED": 0
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

自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：TABLE_TYPE、X_DIR、Y_DIR、COMBINED 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 6 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：COMPONENTS、LOAD_CASE_NAMES、X_DIR 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `Story Drift (X,Y,Combined)`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Story Drift(X,Y,Combine) - Story Result Table 的 JSON 数据。"""
    data = {"Argument": {"TABLE_TYPE": "<TABLE_TYPE>"}, "X_DIR": 0, "Y_DIR": 0, "COMBINED": 0}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}Story Drift (X,Y,Combined)", json=data, verify=False)
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
    r = session.post(f"{BASE}Story Drift (X,Y,Combined)", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Story Displacement(X,Y,Combined) - Story Result Table — `Story Displacement (X,Y,Combined)`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• X-Direction: "STORY_DISPLACEMENT_X"• Y-Direction: "STORY_DISP |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "STORY_DISPLACEMENT_X",
    "TABLE_TYPE": "STORY_DISPLACEMENT_X",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ]
  }
}
```


---

### Story Shear Force(R.S.Analysis) - Story Result Table — `Story Shear(R.S Analysis) - Story Shear(for R.S)Story Shear(R.S.Analysis) - Story Shear Force Coefficient`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_SHEAR_FOR_RS" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_SHEAR_FOR_RS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "MM"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "LOAD_CASE_NAMES": [
      "Rx(RS)",
      "Ry(RS)"
    ]
  }
}
```


---

### Story Mode Shape - Story Result Table — `Story Mode Shape`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_MODE_SHAPE" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_MODE_SHAPE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "MODES": [
      "Mode1",
      "Mode2"
    ]
  }
}
```


---

### Story Shear Force Ratio - Story Result Table — `Story Shear Force Ratio`

**方法**: POST | **参数**: 1 必填 + 15 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_SHEAR_FORCE_RATIO" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 5 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "LOAD_CASE_NAMES": [
      "EX(ST)"
    ],
    "STORY_NAMES": [
      "2F"
    ],
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 33.5
      }
    }
  }
}
```


---

### Story Eccentricity - Story Result Table — `Story Eccentricity`

**方法**: POST | **参数**: 1 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_ECNTRICITY" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_ECNTRICITY",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    }
  }
}
```


---

### Overturning Moment - Story Result Table — `Overturning Moment`

**方法**: POST | **参数**: 1 必填 + 15 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "OVERTURNING_MOMENT" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 5 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
[
  "Rx(RS)",
  "Ry(RS)"
]
```


---

### Story Axial Force Sum - Story Result Table — `Story Axial Force Sum`

**方法**: POST | **参数**: 1 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STORY_AXIAL_FORCE_SUM" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_AXIAL_FORCE_SUM",
    "UNIT": {
      "FORCE": "LBF",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "LOAD_CASE_NAMES": [
      "DL(ST)"
    ]
  }
}
```


---

### Story Stability Coefficient - Story Result Table — `Story Stability Coefficient`

**方法**: POST | **参数**: 1 必填 + 21 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• X-Direction : "STORY_STABILITY_COEFFICIENT_X"• Y-Direction :  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 11 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_X",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ],
    "ADDITIONAL": {
      "SET_STABILITY_COEFFICIENT_PARAMS": {
        "DEFLECTION_AMPL_FACTOR_VALUE": 2,
        "IMPORTANCE_FACTOR_VALUE": 5,
        "SCALE_FACTOR_VALUE": 2,
        "LCOMS": [
          {
            "NAME": "DL",
            "FACTOR": 1
          }
        ],
        "BETA": {
          "FIX_USER_CHECK": "USER",
          "NAME_FROM": "1F",
          "NAME_TO": "12F",
          "VALUE": 2
        }
      },
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Max.DriftofAllVerticalElements"
      }
    }
  }
}
```


---

### Torsional Irregularity Check - Story Result Table — `Torsional Irregularity Check`

**方法**: POST | **参数**: 2 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• X-Direction: "TORSIONAL_IRRGULARITY_X"• Y-Direction : "TORSIO |
| `SELECT_IRREGULAR_ENDS` | 对象（一组键值对） | **是** | Set Select Target End Nodes |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  },
  "SELECT_IRREGULAR_ENDS": {}
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ]
  }
}
```


---

### Torsional Amplification Factor - Story Result Table — `Torsional Amplification Factor`

**方法**: POST | **参数**: 2 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• X-Direction : "TORSIONAL_AMPLIFICATION_FACTOR_X"• Y-Direction |
| `SELECT_IRREGULAR_ENDS` | 对象（一组键值对） | **是** | Set Select Target End Nodes |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  },
  "SELECT_IRREGULAR_ENDS": {}
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ]
  }
}
```


---

### Stiffness Irregularity Check (Soft Story) - Story Result Table — `Stiffness Irregularity Check (Soft Story)`

**方法**: POST | **参数**: 2 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• X-Direction : "STIFFNESS_IRREGULARITY_X"• Y-Direction : "STIF |
| `SET_CALCULATION_METHOD` | 对象（一组键值对） | **是** | Set Calculation Method |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>",
    "ADDITIONAL": {
      "SET_CALCULATION_METHOD": {}
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ],
    "ADDITIONAL": {
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Drift at the Center of Mass",
        "STORY_STIFFNESS_METHOD": "1 / Story Drift Ratio"
      }
    }
  }
}
```


---

### Capacity Irregularity Check(Weak Story) - Story Result Table — `Capacity Irregularity Check(Weak Story)`

**方法**: POST | **参数**: 2 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "CAPACITY_IRREGULARITY" |
| `SET_ANGLE` | 对象（一组键值对） | **是** | Set Angle |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>",
    "ADDITIONAL": {
      "SET_ANGLE": {}
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "CAPACITY_IRREGULARITY",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 33.5
      }
    }
  }
}
```


---

### Criteria for Regularity in Plan - Story Result Table — `Criteria for Regularity in Plan`

**方法**: POST | **参数**: 1 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "CRITERIA_FOR_REGULARITY_IN_PLAN" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "EXPORT_PATH": "D:\\00.2023년\\00.9월\\Output.JSON",
    "TABLE_TYPE": "CRITERIA_FOR_REGULARITY_IN_PLAN",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    }
  }
}
```


---

### Ultimate Story Shear For Check - Story Result Table — `Ultimate Story Shear For Check`

**方法**: POST | **参数**: 1 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "ULTIMATE_STORY_SHEAR_FORCE_CHECK" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "Argument": {
    "TABLE_TYPE": "<TABLE_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 4
    },
    "LOAD_CASE_NAMES": [
      "RX(RS)"
    ],
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 0
      }
    }
  }
}
```


---

### Displacement/Velocity/Acceleration - TH Result Table — `DisplacementVelocityAbsolute AccelerationRelative Acceleration`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Displacement: "THISDISPLACEMENT"• Velocity: "THISVELOCITY"• A |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Displacement",
    "TABLE_TYPE": "THISDISPLACEMENT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Load",
      "DX/DX",
      "DX/Time/Step",
      "DY/DY",
      "DY/Time/Step",
      "DZ/DZ",
      "DZ/Time/Step",
      "RX/RX",
      "RX/Time/Step",
      "RY/RY",
      "RY/Time/Step",
      "RZ/RZ",
      "RZ/Time/Step"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        10
      ]
    },
    "LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Beam Force - TH Result Table — `Beam Force`

**方法**: POST | **参数**: 1 必填 + 18 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "THISBEAMFORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `PARTS` | 字符串数组 | 否 | Element Part Number• "Part I"• "Part 1/4"• "Part 2/4"• "Part 3/4"• "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| ... | ... | ... | *还有 8 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "BeamForce",
    "TABLE_TYPE": "THISBEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Part",
      "Axial/Force",
      "Axial/Time/Step",
      "Shear-y/Force",
      "Shear-y/Time/Step",
      "Shear-z/Force",
      "Shear-z/Time/Step",
      "Torsion/Force",
      "Torsion/Time/Step",
      "Moment-y/Force",
      "Moment-y/Time/Step",
      "Moment-z/Force",
      "Moment-z/Time/Step"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        2
      ]
    },
    "LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ]
  }
}
```


---

### Truss Force - TH Result Table — `Truss Force`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Truss Force: "THISTRUSSFORCE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "TrussForce",
    "TABLE_TYPE": "THISTRUSSFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Force-I/Force",
      "Force-I/Time/Step",
      "Force-J/Force",
      "Force-J/Time/Step"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        49
      ]
    },
    "LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### General Link - TH Result Table — `General Link ForceDeformation`

**方法**: POST | **参数**: 1 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• General Link - Force: "THISGLINKFORCE"• General Link - Deform |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Load Name & Type• Static Load Cases◦ NAME + "(ST)"• Load Combinations◦ NAME + "( |
| `OPT_CS` | 是/否（布尔值） | 否 | Activation-ConstructionStageStep |
| `STAGE_STEP` | Array | 否 | StageStepName |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Force",
    "TABLE_TYPE": "THISGLINKFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "No.",
      "Load",
      "Node",
      "Axial/Force",
      "Axial/Time/Step",
      "Shear-y/Force",
      "Shear-y/Time/Step",
      "Shear-z/Force",
      "Shear-z/Time/Step",
      "Torsion/Force",
      "Torsion/Time/Step",
      "Moment-y/Force",
      "Moment-y/Time/Step",
      "Moment-z/Force",
      "Moment-z/Time/Step"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Event Time - TH Result Table — `Event Time-LumpedEvent Time-DistributedEvent Time-WallEvent Time-TrussEvent Time-Spring`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Event Time - Lumped: "IEHG_EVENT_TIME_LUMPED"• Event Time - D |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_EVENT_TIME_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "HingeLocation",
      "Load",
      "1stYield/Dx",
      "1stYield/Dy",
      "1stYield/Dz",
      "1stYield/Rx",
      "1stYield/Ry",
      "1stYield/Rz",
      "2ndYield/Dx",
      "2ndYield/Dy",
      "2ndYield/Dz",
      "2ndYield/Rx",
      "2ndYield/Ry",
      "2ndYield/Rz",
      "3rdYield/Dx",
      "3rdYield/Dy",
      "3rdYield/Dz",
      "3rdYield/Rx",
      "3rdYield/Ry",
      "3rdYield/Rz"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent"
    ]
  }
}
```


---

### Inelastic Hinge Beam Summary - TH Result Table — `Beam Summary-DXBeam Summary-DYBeam Summary-DZBeam Summary-RYBeam Summary-RZ`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Summary - Dx: "IEHG_BEAM_SUM_DX"• Beam Summary - Dy: "IE |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_BEAM_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Type",
      "Elem",
      "HingeLocation",
      "InelasticHingeProp.",
      "Load",
      "Time/Step",
      "Deform",
      "Force",
      "max(D/D1)",
      "max(D/D2)",
      "Status",
      "Performance",
      "P1",
      "P2",
      "P3",
      "D1",
      "D2",
      "D3"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        2,
        3
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Truss Summary - TH Result Table — `Truss Summary-DX`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Truss Summary - Dx: "IEHG_TRUSS_SUM_DX" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_TRUSS_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Truss/Elem",
      "Truss/Node1",
      "Truss/Node2",
      "InelasticHingeProp.",
      "Load",
      "Time/Step",
      "Deform",
      "Force",
      "max(D/D1)",
      "max(D/D2)",
      "Status",
      "Performance",
      "P1",
      "P2",
      "P3",
      "D1",
      "D2",
      "D3"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        49
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge General Link Summary - TH Result Table — `General Link Summary-DXGeneral Link Summary-DYGeneral Link Summary-DZGeneral Link Summary-RXGeneral Link Summary-RYGeneral Link Summary-RZ`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• GL-Link Summary - Dx: "IEHG_GL_LINK_SUM_DX"• GL-Link Summary  |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_GL_LINK_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "GeneralLink/No",
      "GeneralLink/Prop.",
      "GeneralLink/Node1",
      "GeneralLink/Node2",
      "InelasticHingeProp.",
      "Load",
      "Time/Step",
      "Deform",
      "Force",
      "max(D/D1)",
      "max(D/D2)",
      "Status",
      "Performance",
      "P1",
      "P2",
      "P3",
      "D1",
      "D2",
      "D3"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Force - TH Result Table — `Force-LumpedForce-DistributedForce-WallForce-TrussForce-Spring`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Force - Lumped: "IEHG_FORCE_LUMPED"• Force - Distributed: "IE |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_FORCE_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "HingeLocation",
      "InelasticHingeProp.",
      "Load",
      "Fx/Force",
      "Fx/Time",
      "Fy/Force",
      "Fy/Time",
      "Fz/Force",
      "Fz/Time",
      "Mx/Force",
      "Mx/Time",
      "My/Force",
      "My/Time",
      "Mz/Force",
      "Mz/Time"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Deformation - TH Result Table — `Deformation-LumpedDeformation-DistributedDeformation-WallDeformation-TrussDeformation-Spring`

**方法**: POST | **参数**: 1 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Deformation - Lumped: "IEHG_DEFORM_LUMPED"• Deformation - Dis |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | Array | 否 | TimeHistoryLoadCaseName |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DEFORM_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "HingeLocation",
      "InelasticHingeProp.",
      "Load",
      "Dx/Deform",
      "Dx/Time",
      "Dy/Deform",
      "Dy/Time",
      "Dz/Deform",
      "Dz/Time",
      "Rx/Deform",
      "Rx/Time",
      "Ry/Deform",
      "Ry/Time",
      "Rz/Deform",
      "Rz/Time"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Element Rotation - TH Result Table — `Element Rotation-BeamElement Rotation-Wall`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Element Rotation - Beam: "IEHG_ELEM_ROT_BEAM"• Element Rotati |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Beam",
    "TABLE_TYPE": "IEHG_ELEM_ROT_BEAM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Part",
      "Ry/Rotation",
      "Ry/Time",
      "Rz/Rotation",
      "Rz/Time"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Ductility Factor(D/D1) - TH Result Table — `Ductility Factor(D/D1)-LumpedDuctility Factor(D/D1)-DistributedDuctility Factor(D/D1)-WallDuctility Factor(D/D1)-TrussDuctility Factor(D/D1)-Spring`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Ductility Factor(D/D1) - Lumped: "IEHG_DUCT_D1_LUMPED"• Ducti |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D1_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "HingeLocation",
      "InelasticHingeProp.",
      "Load",
      "Dx/max",
      "Dx/Time",
      "Dy/max",
      "Dy/Time",
      "Dz/max",
      "Dz/Time",
      "Rx/max",
      "Rx/Time",
      "Ry/max",
      "Ry/Time",
      "Rz/max",
      "Rz/Time"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Inelastic Hinge Ductility Factor(D/D2) - TH Result Table — `Ductility Factor(D/D2)-LumpedDuctility Factor(D/D2)-DistributedDuctility Factor(D/D2)-WallDuctility Factor(D/D2)-TrussDuctility Factor(D/D2)-Spring`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Ductility Factor(D/D2) - Lumped: "IEHG_DUCT_D2_LUMPED"• Ducti |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `TH_LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Case Name• NAME• NAME + "(TH:all)"• NAME + "(TH:max)"• NAME +  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D2_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "HingeLocation",
      "InelasticHingeProp.",
      "Load",
      "Dx/max",
      "Dx/Time",
      "Dy/max",
      "Dy/Time",
      "Dz/max",
      "Dz/Time",
      "Rx/max",
      "Rx/Time",
      "Ry/max",
      "Ry/Time",
      "Rz/max",
      "Rz/Time"
    ],
    "TH_LOAD_CASE_NAMES": [
      "Elcent(TH:max)",
      "Elcent(TH:min)"
    ]
  }
}
```


---

### Fiber Section Estimate Yield Strength - TH Result Table — `Estimate Yield Strength`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "FIBR_YILEDSTRENGTH" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "YieldStrength",
    "TABLE_TYPE": "FIBR_YILEDSTRENGTH",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Type",
      "Definition",
      "Elem",
      "Hinge Location",
      "Inelastic Hinge Prop.",
      "Load Case",
      "Crack/Rc'",
      "Crack/Mc'",
      "Crack/Step",
      "Yield/Ry'",
      "Yield/My'",
      "Yield/Step",
      "Ultimate/Ru",
      "Ultimate/Mu",
      "Ultimate/Step",
      "Estimate Yield/Ry",
      "Estimate Yield/My",
      "Estimate Yield/Step",
      "Mmax",
      "Ieff",
      "Ieff/I"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1240
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "kh"
    ]
  }
}
```


---

### Fiber Section Elastic Modulus Retention Rate - TH Result Table — `Elastic Modulus Retention Rateᴶ⁾`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "FIBR_ELASTREMAIN" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "ElasticModulus",
    "TABLE_TYPE": "FIBR_ELASTREMAIN",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "番号/要素",
      "番号/断面",
      "番号/セルNo.",
      "番号/荷重",
      "セル位置/y",
      "セル位置/z",
      "弾性剛性残存率/K",
      "セル面積/△A"
    ],
    "TH_LOAD_CASE_NAMES": [
      "kh"
    ]
  }
}
```


---

### Fiber Section Maximum Strain of The Cell - TH Result Table — `Maximum Strain of The Cellᴶ⁾`

**方法**: POST | **参数**: 1 必填 + 18 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "FIBR_MAXCONTRACT" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Two Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Name |
| `SECT_POSITION` | 文字（字符串） | 否 | Section Positions |
| `FIBER_CELL_MINMAX` | 是/否（布尔值） | 否 | All Fiber Cell Min/Max Strain Table |
| ... | ... | ... | *还有 8 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "MaximumStrain",
    "TABLE_TYPE": "FIBR_MAXCONTRACT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "要素",
      "断面位置",
      "材料",
      "荷重",
      "セルNo.",
      "最小/ε",
      "最小/時間/ステップ",
      "最大/ε",
      "最大/時間/ステップ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1240
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "kh"
    ],
    "SECT_POSITION": "1to2",
    "FIBER_CELL_MINMAX": true
  }
}
```


---

### Fiber Section Event Step - TH Result Table — `Event Stepᴶ⁾`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "FIBR_EVENTSTEP" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Two Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Name |
| `SECT_POSITION` | 文字（字符串） | 否 | Section Positions |
| `FORCE` | 文字（字符串） | 否 | Force |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "EventStep",
    "TABLE_TYPE": "FIBR_EVENTSTEP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "要素",
      "断面位置",
      "荷重",
      "鉄骨/引張降伏/セルNo.",
      "鉄骨/引張降伏/ε",
      "鉄骨/引張降伏/時間/ステップ",
      "鉄骨/圧縮降伏/セルNo.",
      "鉄骨/圧縮降伏/ε",
      "鉄骨/圧縮降伏/時間/ステップ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1240
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "kh"
    ],
    "SECT_POSITION": "1to2"
  }
}
```


---

### Fiber Section Average Compression Strain - TH Result Table — `Average Compression Strainᴶ⁾`

**方法**: POST | **参数**: 1 必填 + 18 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Beam Force: "FIBR_MEANCOMPCONTRACT" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Two Methods |
| `LOAD_CASE_NAMES` | 字符串数组 | 否 | Time History Load Name |
| `SECT_POSITION` | 文字（字符串） | 否 | Section Positions |
| `OUTPUT_STEP` | 文字（字符串） | 否 | Output Step |
| ... | ... | ... | *还有 8 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "AverageCompStrain",
    "TABLE_TYPE": "FIBR_MEANCOMPCONTRACT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "各ステップにおける外側セルの平均圧縮ひずみ/ステップ",
      "各ステップにおける外側セルの平均圧縮ひずみ/要素",
      "各ステップにおける外側セルの平均圧縮ひずみ/断面 位置",
      "各ステップにおける外側セルの平均圧縮ひずみ/材料",
      "各ステップにおける外側セルの平均圧縮ひずみ/荷重",
      "各ステップにおける外側セルの平均圧縮ひずみ/Ea"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1240
      ]
    },
    "TH_LOAD_CASE_NAMES": [
      "kh"
    ],
    "SECT_POSITION": "1to2",
    "OUTPUT_STEP": "1,3"
  }
}
```


---

### Stress - HY Result Table — `Stress-LocalStress-Global`

**方法**: POST | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Hydration Stress - Local: "HEAT_HYDR_STRESS_L"• Hydration Str |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `NODE_FLAG` | 对象（一组键值对） | 否 | Node Flag |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "HydrationStress(Local)",
    "TABLE_TYPE": "HEAT_HYDR_STRESS_L",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Elem",
      "Stage",
      "Step",
      "Time",
      "Node",
      "Sig-xx",
      "Sig-yy",
      "Sig-zz",
      "Sig-xy",
      "Sig-yz",
      "Sig-xz",
      "Sig-P1",
      "Sig-P2",
      "Sig-P3",
      "Max-Shear",
      "Sig-EFF",
      "Sig-OCT"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        2202
      ]
    },
    "NODE_FLAG": {
      "CENTER": true,
      "NODES": true
    },
    "STAGE_STEP": [
      "CS2:013"
    ]
  }
}
```


---

### Temperature - HY Result Table — `Temperature`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Hydration Temperature: "HEAT_HYDR_TEMPERATURE" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "HydrationTemperature",
    "TABLE_TYPE": "HEAT_HYDR_TEMPERATURE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Stage",
      "Step",
      "Time",
      "Temperature"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1252
      ]
    },
    "STAGE_STEP": [
      "CS2:013"
    ]
  }
}
```


---

### Displacement - HY Result Table — `Displacement`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Hydration Displacement: "HEAT_HYDR_DISPLACEMENT" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node/Element No. Input• Use Only One of the Three Methods |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "HydrationDisplacement",
    "TABLE_TYPE": "HEAT_HYDR_DISPLACEMENT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Stage",
      "Step",
      "Time",
      "DX",
      "DY",
      "DZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        2809
      ]
    },
    "STAGE_STEP": [
      "CS2:013"
    ]
  }
}
```


---

### Tensile Stress - HY Result Table — `Tensile Stress`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Hydration Tensile Stress: "HEAT_HYDR_TENS_STRESS" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | 否 | Node / Element No. Input• Use Only One of the Three Methods |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "HydrationTensileStress",
    "TABLE_TYPE": "HEAT_HYDR_TENS_STRESS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "Node",
      "Stage",
      "Step",
      "Time",
      "Stress"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        2809
      ]
    },
    "STAGE_STEP": [
      "CS2:013"
    ]
  }
}
```


---

### Pipe Cooling Nodal Temperature - HY Result Table — `Pipe Cooling Nodal Temperature`

**方法**: POST | **参数**: 1 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• Pipe Cooling Nodal Temperature: "HEAT_HYDR_PIPE_NODE_TEMP" |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `STAGE_STEP` | 字符串数组 | 否 | Stage Step Name |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "RESULTGRAPHIC": {
    "Argument": {
      "TABLE_TYPE": "<TABLE_TYPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "PipeCoolingNodalTemperature",
    "TABLE_TYPE": "HEAT_HYDR_PIPE_NODE_TEMP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "mm"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 12
    },
    "COMPONENTS": [
      "PipeCooling",
      "Stage",
      "Step",
      "Time",
      "Node",
      "Temperature"
    ],
    "STAGE_STEP": [
      "CS1:001"
    ]
  }
}
```


---

## Time History Text - Node Results — `Node Results`

**HTTP 方法**: POST | **参数总数**: 22（8 必填 + 14 可选）

### 1. 这是什么？（工程含义）

**Time History Text - Node Results** — 这是后处理结果提取操作。

ResultTableType

> 简单说：这个接口用来**Time History Text - Node Results**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "TEXT": {
    "Argument (可选)": {},
    "Argument": {
      "TABLE_TYPE (可选)": "<TABLE_TYPE>",
      "EXPORT_PATH (可选)": "<EXPORT_PATH>",
      "UNIT (可选)": "System",
      "STYLES (可选)": "System",
      "COMPONENTS (可选)": "All",
      "REF_PT (可选)": "\"Ground\"",
      "NODE_ELEMS": {},
      "TH_CASE_NAME": "<TH_CASE_NAME>",
      "STEP": {},
      "ANR_NODE": 0
    },
    "properties": {
      "Argument": {
        "properties": {
          "UNIT": {
            "properties": {
              "FORCE (可选)": "<FORCE>",
              "DIST (可选)": "<DIST>",
              "HEAT (可选)": "<HEAT>",
              "TEMP (可选)": "<TEMP>"
            }
          },
          "STYLES": {
            "properties": {
              "FORMAT (可选)": "<FORMAT>",
              "PLACE (可选)": 0
            }
          },
          "NODE_ELEMS": {
            "properties": {
              "KEYS (可选)": 0,
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**第 1 层：`TEXT`** — 1 个参数在这一层

- `"Argument"`: 对象（一组键值对） — 

**第 2 层：`TEXT.Argument`** — 10 个参数在这一层

- `"TABLE_TYPE"`: 文字（字符串） — ResultTableType
- `"EXPORT_PATH"`: 文字（字符串） — Result Table Save Path
- `"UNIT"`: 对象（一组键值对） — Response Unit Setting
- `"STYLES"`: 对象（一组键值对） — Response Number Format
- `"COMPONENTS"`: 字符串数组 — Components of Result Table
- `"NODE_ELEMS"`: 对象（一组键值对） — Node / Element No. Input• Use Only One of the Two Methods
- `"TH_CASE_NAME"`: 字符串数组 — Time History Load Case
- `"STEP"`: 对象（一组键值对） — Output Time Step
- ... *还有 2 个参数*

**第 3 层：`TEXT.properties.Argument.properties.NODE_ELEMS.properties`** — 2 个参数在这一层

- `"KEYS"`: 整数数组 — • "KEYS": [101, 102, 103]
- `"TO"`: 数字 — End Time

**第 4 层：`TEXT.properties.Argument.properties.STEP.properties`** — 2 个参数在这一层

- `"FROM"`: 数字 — Start Time
- `"STEPS"`: 整数 — Time Interval

**第 5 层：`TEXT.properties.Argument.properties.STYLES.properties`** — 2 个参数在这一层

- `"FORMAT"`: 文字（字符串） — Number Format• "Default"• "Fixed"• "Scientific"• "General"
- `"PLACE"`: 整数 — Digit Place• 0 to 15

**第 6 层：`TEXT.properties.Argument.properties.UNIT.properties`** — 4 个参数在这一层

- `"FORCE"`: 文字（字符串） — Force
- `"DIST"`: 文字（字符串） — Length
- `"HEAT"`: 文字（字符串） — Heat
- `"TEMP"`: 文字（字符串） — Temperature

**第 7 层：最外层**
这是整个 JSON 的入口。
- `"TEXT_TYPE"`: 文字（字符串） — Result Text Type• Displacement: "TH_DISP"• Velocity: "TH_VELOCITY"• Acceleration: "TH_ACCEL"


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `NODE_ELEMS` | 对象（一组键值对） | `TEXT.Argument.NODE_ELEMS` | Node / Element No. Input• Use Only One of the Two Methods |
| `TH_CASE_NAME` | 字符串数组 | `TEXT.Argument.TH_CASE_NAME` | Time History Load Case |
| `STEP` | 对象（一组键值对） | `TEXT.Argument.STEP` | Output Time Step |
| `ANR_NODE` | 整数 | `TEXT.Argument.ANR_NODE` | Reference Point• Another Node |
| `TEXT_TYPE` | 文字（字符串） | `TEXT_TYPE` | Result Text Type• Displacement: "TH_DISP"• Velocity: "TH_VEL |
| `TO` | 数字 | `TEXT.properties.Argument.properties.NODE_ELEMS.properties.TO` | End Time |
| `FROM` | 数字 | `TEXT.properties.Argument.properties.STEP.properties.FROM` | Start Time |
| `STEPS` | 整数 | `TEXT.properties.Argument.properties.STEP.properties.STEPS` | Time Interval |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `Argument` | 对象（一组键值对） | `无` |  |
| `TABLE_TYPE` | 文字（字符串） | `无` | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | `无` | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | `System` | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | `System` | Response Number Format |
| `COMPONENTS` | 字符串数组 | `All` | Components of Result Table |
| `REF_PT` | 文字（字符串） | `"Ground"` | Reference Point• "Ground"• "Add Ground Motion" |
| `FORCE` | 文字（字符串） | `无` | Force |
| `DIST` | 文字（字符串） | `无` | Length |
| `HEAT` | 文字（字符串） | `无` | Heat |
| `TEMP` | 文字（字符串） | `无` | Temperature |
| `FORMAT` | 文字（字符串） | `无` | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | `无` | Digit Place• 0 to 15 |
| `KEYS` | 整数数组 | `无` | • "KEYS": [101, 102, 103] |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `Argument` 的路径：**"TEXT" → "Argument"**
  意思是：在 JSON 中依次打开 TEXT, Argument，最后填入 `Argument` 的值
- `TABLE_TYPE` 的路径：**"TEXT" → "Argument" → "TABLE_TYPE"**
  意思是：在 JSON 中依次打开 TEXT, Argument, TABLE_TYPE，最后填入 `TABLE_TYPE` 的值
- `EXPORT_PATH` 的路径：**"TEXT" → "Argument" → "EXPORT_PATH"**
  意思是：在 JSON 中依次打开 TEXT, Argument, EXPORT_PATH，最后填入 `EXPORT_PATH` 的值
- `UNIT` 的路径：**"TEXT" → "Argument" → "UNIT"**
  意思是：在 JSON 中依次打开 TEXT, Argument, UNIT，最后填入 `UNIT` 的值
- `STYLES` 的路径：**"TEXT" → "Argument" → "STYLES"**
  意思是：在 JSON 中依次打开 TEXT, Argument, STYLES，最后填入 `STYLES` 的值
- `COMPONENTS` 的路径：**"TEXT" → "Argument" → "COMPONENTS"**
  意思是：在 JSON 中依次打开 TEXT, Argument, COMPONENTS，最后填入 `COMPONENTS` 的值
- `REF_PT` 的路径：**"TEXT" → "Argument" → "REF_PT"**
  意思是：在 JSON 中依次打开 TEXT, Argument, REF_PT，最后填入 `REF_PT` 的值
- `FORCE` 的路径：**"TEXT" → "properties" → "Argument" → "properties" → "UNIT" → "properties" → "FORCE"**
  意思是：在 JSON 中依次打开 TEXT, properties, Argument, properties, UNIT, properties, FORCE，最后填入 `FORCE` 的值
- `DIST` 的路径：**"TEXT" → "properties" → "Argument" → "properties" → "UNIT" → "properties" → "DIST"**
  意思是：在 JSON 中依次打开 TEXT, properties, Argument, properties, UNIT, properties, DIST，最后填入 `DIST` 的值
- `HEAT` 的路径：**"TEXT" → "properties" → "Argument" → "properties" → "UNIT" → "properties" → "HEAT"**
  意思是：在 JSON 中依次打开 TEXT, properties, Argument, properties, UNIT, properties, HEAT，最后填入 `HEAT` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `NODE_ELEMS`：Node / Element No. Input• Use Only One of the Two Methods
- `REF_PT` 的取值需要参考其他接口文档
- `ANR_NODE` 的取值需要参考其他接口文档
- `TEXT_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `KEYS` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}Node Results"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "TEXT": {
#         "Argument": {
#             "NODE_ELEMS": {},
#             "TH_CASE_NAME": "<TH_CASE_NAME>",
#             "STEP": {},
#             "ANR_NODE": 0
#         },
#         "properties": {
#             "Argument": {
#                 "properties": {
#                     "NODE_ELEMS": {
#                         "properties": {
#                             "TO": 0
#                         }
#                     },
#                     "STEP": {
#                         "properties": {
#                             "FROM": 0,
#                             "STEPS": 0
#                         }
#                     }
#                 }
#             }
#         }
#     },
#     "TEXT_TYPE": "<TEXT_TYPE>"
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

自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：NODE_ELEMS、TH_CASE_NAME、STEP、ANR_NODE、TEXT_TYPE、TO、FROM、STEPS 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 7 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：COMPONENTS、TH_CASE_NAME、KEYS 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `Node Results`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Time History Text - Node Results 的 JSON 数据。"""
    data = {"TEXT": {"Argument": {"NODE_ELEMS": {}, "TH_CASE_NAME": "<TH_CASE_NAME>", "STEP": {}, "ANR_NODE": 0}, "properties": {"Argument": {"properties": {"NODE_ELEMS": {"properties": {"TO": 0}}, "STEP": {"properties": {"FROM": 0, "STEPS": 0}}}}}}, "TEXT_TYPE": "<TEXT_TYPE>"}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}Node Results", json=data, verify=False)
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
    r = session.post(f"{BASE}Node Results", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Time History Text - Element Result(Truss, Beam, Plane Stress/Strain, Solid) — `Element Result(Truss, Beam, Plane Stress/Strain, Solid)`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `TH_CASE_NAME` | 字符串数组 | **是** | Time History Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Time Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Beam Force: "TH_BEAMFORCE"• Truss Froce: "TH_TRUSSFORCE"• Plan |
| `TO` | 数字 | **是** | End Time |
| `FROM` | 数字 | **是** | Start Time |
| `STEPS` | 整数 | **是** | Time Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Beam Force/Stress◦ "Part I"◦ "Part J"• Plane Stress/Strain Force◦  |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "TH_CASE_NAME": "<TH_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "TH_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_BeamForce_Out.JSON",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Part",
      "Time/Step",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        5
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "TH_CASE_NAME": [
      "Elcent"
    ],
    "STEP": {
      "FROM": 0.1,
      "TO": 0.5,
      "STEPS": 1
    }
  }
}
```


---

### Time History Text - Element Result(Plate) — `Element Result(Plate)`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `TH_CASE_NAME` | 字符串数组 | **是** | Time History Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Time Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Plate Force: "TH_PLATEFORCE"• Plate Unit Force: "TH_PLATE_UNIT |
| `TO` | 数字 | **是** | End Time |
| `FROM` | 数字 | **是** | Start Time |
| `STEPS` | 整数 | **是** | Time Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Plate Force◦ "Part I"◦ "Part J"◦ "Part K"◦ "Part L"• Plate Unit Fo |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "TH_CASE_NAME": "<TH_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "TH_PLATEFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_PlateForce_Out.JSON",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Time/Step",
      "Part",
      "FX",
      "FY",
      "FZ",
      "MX",
      "MY",
      "MZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        51
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ",
      "PartK",
      "PartL"
    ],
    "TH_CASE_NAME": [
      "Elcent"
    ],
    "STEP": {
      "FROM": 0.1,
      "TO": 0.3,
      "STEPS": 1
    }
  }
}
```


---

### Time History Text - Element Result(Wall) — `Element Result(Wall)`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `TH_CASE_NAME` | 字符串数组 | **是** | Time History Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Time Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Wall Force : "TH_WALLFORCE"ᴳ⁾ |
| `TO` | 数字 | **是** | End Time |
| `FROM` | 数字 | **是** | Start Time |
| `STEPS` | 整数 | **是** | Time Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Wall Force◦ "Part I"◦ "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "TH_CASE_NAME": "<TH_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "TH_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_WallForce_Out.JSON",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Exponential",
      "PLACE": 6
    },
    "COMPONENTS": [
      "WallID",
      "Load",
      "Time/Step",
      "Part",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        466
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "TH_CASE_NAME": [
      "EQ1"
    ],
    "STEP": {
      "FROM": 0.1,
      "TO": 0.2,
      "STEPS": 1
    }
  }
}
```


---

### Time History Text - General Link Result — `General Link Result`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `TH_CASE_NAME` | 字符串数组 | **是** | Time History Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Time Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• General Link Deformation: "TH_GLINKDEFORM"• General Link Force |
| `TO` | 数字 | **是** | End Time |
| `FROM` | 数字 | **是** | Start Time |
| `STEPS` | 整数 | **是** | Time Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• General Link Force◦ "Part I"◦ "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "TH_CASE_NAME": "<TH_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "TH_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_GlinkDeform_Out.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "MM"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Key",
      "Node1",
      "Node2",
      "Load",
      "Time/Step",
      "DX",
      "DY",
      "DZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "TH_CASE_NAME": [
      "Elcent"
    ],
    "STEP": {
      "FROM": 0.1,
      "TO": 0.5,
      "STEPS": 1
    }
  }
}
```


---

### Pushover Text - Displacement Result — `Displacement Result`

**方法**: POST | **参数**: 8 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `PO_CASE_NAME` | 字符串数组 | **是** | Pushover Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Step |
| `ANR_NODE` | 整数 | **是** | Reference Point• Another Node |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Displacement: "PO_DISP" |
| `TO` | 数字 | **是** | End Step |
| `FROM` | 数字 | **是** | Start Step |
| `STEPS` | 整数 | **是** | Step Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `REF_PT` | 文字（字符串） | 否 | Reference Point• "Ground" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "PO_CASE_NAME": "<PO_CASE_NAME>",
      "STEP": {},
      "ANR_NODE": 0
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "PO_DISP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_Displacement_Out.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "MM"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Node",
      "Load",
      "Step",
      "Dx",
      "Dy",
      "Dz",
      "Rx",
      "Ry",
      "Rz"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        22
      ]
    },
    "PO_CASE_NAME": [
      "PX"
    ],
    "STEP": {
      "FROM": 1,
      "TO": 10,
      "STEPS": 1
    },
    "REF_PT": "Ground"
  }
}
```


---

### Pushover Text - Element Result(Beam, Truss) — `Element Result(Beam, Truss)`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `PO_CASE_NAME` | 字符串数组 | **是** | Pushover Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Beam Force: "PO_BEAMFORCE"• Truss Force: "PO_TRUSSFORCE"• Beam |
| `TO` | 数字 | **是** | End Step |
| `FROM` | 数字 | **是** | Start Step |
| `STEPS` | 整数 | **是** | Step Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Beam Force/Stress◦ "Part I"◦ "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "PO_CASE_NAME": "<PO_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "PO_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_BeamForce_Out.JSON",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Elem",
      "Load",
      "Part",
      "Step",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        16
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "PO_CASE_NAME": [
      "PX"
    ],
    "STEP": {
      "FROM": 1,
      "TO": 5,
      "STEPS": 1
    }
  }
}
```


---

### Pushover Text - Element Result(Wall) — `Element Result(Wall)`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `PO_CASE_NAME` | 字符串数组 | **是** | Pushover Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Wall Force: "PO_WALLFORCE"ᴳ⁾ |
| `TO` | 数字 | **是** | End Step |
| `FROM` | 数字 | **是** | Start Step |
| `STEPS` | 整数 | **是** | Step Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Beam Force/Stress◦ "Top"◦ "Bot" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "PO_CASE_NAME": "<PO_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "PO_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_WallForce_Out.JSON",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Exponential",
      "PLACE": 6
    },
    "COMPONENTS": [
      "WallID",
      "Load",
      "Step",
      "Part",
      "Axial",
      "Shear-y",
      "Shear-z",
      "Torsion",
      "Moment-y",
      "Moment-z"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        466
      ]
    },
    "PARTS": [
      "Top",
      "Bot"
    ],
    "PO_CASE_NAME": [
      "PX"
    ],
    "STEP": {
      "FROM": 1,
      "TO": 5,
      "STEPS": 1
    }
  }
}
```


---

### Pushover Text - General Link Result — `General Link Result`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `PO_CASE_NAME` | 字符串数组 | **是** | Pushover Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• General Link Deformation: "PO_GLINKDEFORM"• General Link Force |
| `TO` | 数字 | **是** | End Step |
| `FROM` | 数字 | **是** | Start Step |
| `STEPS` | 整数 | **是** | Step Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• General Link Force◦ "Part I"◦ "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "PO_CASE_NAME": "<PO_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "PO_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_GlinkDeform_Out.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "MM"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Key",
      "Node1",
      "Node2",
      "Load",
      "Step",
      "DX",
      "DY",
      "DZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "PO_CASE_NAME": [
      "PX"
    ],
    "STEP": {
      "FROM": 1,
      "TO": 5,
      "STEPS": 1
    }
  }
}
```


---

### Pushover Text - Elastic Link Result — `Elastic Link Result`

**方法**: POST | **参数**: 7 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE_ELEMS` | 对象（一组键值对） | **是** | Node / Element No. Input• Use Only One of the Two Methods |
| `PO_CASE_NAME` | 字符串数组 | **是** | Pushover Load Case |
| `STEP` | 对象（一组键值对） | **是** | Output Step |
| `TEXT_TYPE` | 文字（字符串） | **是** | Result Text Type• Elastic Link Deformation: "PO_ELINKDEFORM"• Elastic Link Force |
| `TO` | 数字 | **是** | End Step |
| `FROM` | 数字 | **是** | Start Step |
| `STEPS` | 整数 | **是** | Step Interval |
| `Argument` | 对象（一组键值对） | 否 |  |
| `TABLE_TYPE` | 文字（字符串） | 否 | ResultTableType |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `COMPONENTS` | 字符串数组 | 否 | Components of Result Table |
| `PARTS` | 字符串数组 | 否 | Element Part• Elastic Link Force◦ "Part I"◦ "Part J" |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "TEXT": {
    "Argument": {
      "NODE_ELEMS": {},
      "PO_CASE_NAME": "<PO_CASE_NAME>",
      "STEP": {}
    },
    "properties": {
      "Argument": {
        "properties": {
          "NODE_ELEMS": {
            "properties": {
              "TO": 0
            }
          },
          "STEP": {
            "properties": {
              "FROM": 0,
              "STEPS": 0
            }
          }
        }
      }
    }
  },
  "TEXT_TYPE": "<TEXT_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TEXT_TYPE": "PO_ELINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_ElinkDeform_Out.JSON",
    "UNIT": {
      "FORCE": "N",
      "DIST": "MM"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 6
    },
    "COMPONENTS": [
      "Key",
      "Node1",
      "Node2",
      "Load",
      "Step",
      "DX",
      "DY",
      "DZ",
      "RX",
      "RY",
      "RZ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "PO_CASE_NAME": [
      "PX"
    ],
    "STEP": {
      "FROM": 1,
      "TO": 5,
      "STEPS": 1
    }
  }
}
```


---

## P-M Interaction Diagram — `/post/PM`

**HTTP 方法**: POST | **参数总数**: 1（0 必填 + 1 可选）

### 1. 这是什么？（工程含义）

**P-M Interaction Diagram** — 这是后处理结果提取操作。

> 简单说：这个接口用来**P-M Interaction Diagram**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "PM": {
    "argument (可选)": {}
  }
}
```

**第 1 层：`PM`** — 1 个参数在这一层

- `"argument"`: 对象（一组键值对） — 


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `argument` | 对象（一组键值对） | `无` |  |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `argument` 的路径：**"PM" → "argument"**
  意思是：在 JSON 中依次打开 PM, argument，最后填入 `argument` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/post/PM"

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

自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
4. **URL 写错**：确认路径是 `/post/PM`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 P-M Interaction Diagram 的 JSON 数据。"""
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
    r = requests.post(f"{BASE}/post/PM", json=data, verify=False)
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
    r = session.post(f"{BASE}/post/PM", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Steel Code Check — `/post/STEELCODECHECK`

**方法**: POST | **参数**: 0 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `vSECT` | Array[Object] | 否 | Section Data |
| `Section ID` | "SECT" | 否 | (1) |
| `Combined Strength Ratio` | "RAT" | 否 | (2) |
| `Slenderness Ratio` | "SLN" | 否 | (3) |
| `Deflection` | "DEF" | 否 | (4) |
| `Allowable Deflection` | "DEFA" | 否 | (5) |
| `vELEM` | Array[Object] | 否 | Element Data |
| `ELEM` | 整数 | 否 | ELEMENT ID |
| `RAT` | 数字 | 否 | Combined Strength Ratio |
| `SLN` | 数字 | 否 | Slenderness Ratio |
| ... | ... | ... | *还有 2 个可选参数* |


---

### Concrete Design - Beam Design Forces — `/post/BEAMDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "BEAMDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_TYPE": "BEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1,
        2,
        3
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ]
  }
}
```


---

### Concrete Design - Column Design Forces — `/post/COLUMNDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "COLUMNDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "COLUMNDESIGNFORCES",
    "TABLE_TYPE": "COLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        56,
        57,
        58
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ]
  }
}
```


---

### Concrete Design - Brace Design Forces — `/post/BRACEDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "BRACEDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "BRACEDESIGNFORCES",
    "TABLE_TYPE": "BRACEDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        52,
        53,
        55
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ]
  }
}
```


---

### Concrete Design - Wall Design Forces — `/post/WALLDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 17 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "WALLDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 7 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "WALLDESIGNFORCES",
    "TABLE_TYPE": "WALLDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1
      ]
    },
    "COMPONENTS": [
      "Index",
      "WID",
      "Story",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ]
  }
}
```


---

### Steel Design - Steel Member Design Forces — `/post/STEELMEMBERDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "STEELMEMBERDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "STEELMEMBERDESIGNFORCES",
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1,
        2,
        3
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ]
  }
}
```


---

### SRC Design - SRC Beam Design Forces — `/post/SRCBEAMDESIGNFORCES`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "SRCBEAMDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "SRCBEAMDESIGNFORCES",
    "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        316
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ]
  }
}
```


---

### SRC Design - SRC Column Design Forces — `/post/SRCCOLUMNDESIGNFORCES SRC`

**方法**: POST | **参数**: 1 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TABLE_TYPE` | 文字（字符串） | **是** | Result Table Type• "SRCCOLUMNDESIGNFORCES" |
| `TABLE_NAME` | 文字（字符串） | 否 | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | 否 | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | 否 | Response Unit Setting |
| `FORCE` | 文字（字符串） | 否 | Force |
| `DIST` | 文字（字符串） | 否 | Length |
| `HEAT` | 文字（字符串） | 否 | Heat |
| `TEMP` | 文字（字符串） | 否 | Temperature |
| `STYLES` | 对象（一组键值对） | 否 | Response Number Format |
| `FORMAT` | 文字（字符串） | 否 | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | 否 | Digit Place• 0 to 15 |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**官方示例**：
```json
{
  "Argument": {
    "TABLE_NAME": "SRCCOLUMNDESIGNFORCES",
    "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        365
      ]
    },
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ]
  }
}
```


---

## Cold Formed Design - Cold Formed Steel Member Design Forces — `/post/COLDFORMEDSTEELMEMBERDESIGNFORCES`

**HTTP 方法**: POST | **参数总数**: 17（1 必填 + 16 可选）

### 1. 这是什么？（工程含义）

**Cold Formed Design - Cold Formed Steel Member Design Forces** — 这是后处理结果提取操作。

Table Name• Response Table Title

> 简单说：这个接口用来**Cold Formed Design - Cold Formed Steel Member Design Forces**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "TABLE_NAME (可选)": "Empty",
  "EXPORT_PATH (可选)": "<EXPORT_PATH>",
  "UNIT (可选)": "System",
  "FORCE (可选)": "<FORCE>",
  "DIST (可选)": "<DIST>",
  "HEAT (可选)": "<HEAT>",
  "TEMP (可选)": "<TEMP>",
  "STYLES (可选)": "System",
  "FORMAT (可选)": "<FORMAT>",
  "PLACE (可选)": 0,
  "COMPONENTS (可选)": "All",
  "NODE_ELEMS (可选)": "All",
  "KEYS (可选)": 0,
  "TO (可选)": "<TO>",
  "STRUCTURE_GROUP_NAME (可选)": "<STRUCTURE_GROUP_NAME>",
  "PARTS (可选)": "All",
  "TABLE_TYPE": "<TABLE_TYPE>"
}
```

**第 1 层：最外层**
这是整个 JSON 的入口。
- `"TABLE_NAME"`: 文字（字符串） — Table Name• Response Table Title
- `"TABLE_TYPE"`: 文字（字符串） — Result Table Type• "COLDFORMEDSTEELMEMBERDESIGNFORCES"
- `"EXPORT_PATH"`: 文字（字符串） — Result Table Save Path
- `"UNIT"`: 对象（一组键值对） — Response Unit Setting
- `"FORCE"`: 文字（字符串） — Force
- `"DIST"`: 文字（字符串） — Length
- `"HEAT"`: 文字（字符串） — Heat
- `"TEMP"`: 文字（字符串） — Temperature
- ... *还有 9 个参数*


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `TABLE_TYPE` | 文字（字符串） | `TABLE_TYPE` | Result Table Type• "COLDFORMEDSTEELMEMBERDESIGNFORCES" |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `TABLE_NAME` | 文字（字符串） | `Empty` | Table Name• Response Table Title |
| `EXPORT_PATH` | 文字（字符串） | `无` | Result Table Save Path |
| `UNIT` | 对象（一组键值对） | `System` | Response Unit Setting |
| `FORCE` | 文字（字符串） | `无` | Force |
| `DIST` | 文字（字符串） | `无` | Length |
| `HEAT` | 文字（字符串） | `无` | Heat |
| `TEMP` | 文字（字符串） | `无` | Temperature |
| `STYLES` | 对象（一组键值对） | `System` | Response Number Format |
| `FORMAT` | 文字（字符串） | `无` | Number Format• "Default"• "Fixed"• "Scientific"• "General" |
| `PLACE` | 整数 | `无` | Digit Place• 0 to 15 |
| `COMPONENTS` | 字符串数组 | `All` | Components of Result Table |
| `NODE_ELEMS` | 对象（一组键值对） | `All` | Node / Element No. Input• Use Only One of the Three Methods |
| `KEYS` | 整数数组 | `无` | • "KEYS": [101, 102, 103] |
| `TO` | 文字（字符串） | `无` | • "TO": "101 to 105" |
| `STRUCTURE_GROUP_NAME` | 文字（字符串） | `无` | • "STRUCTURE_GROUP_NAME": "SG1" |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `TABLE_NAME` 的路径：**"TABLE_NAME"**
  意思是：在 JSON 中依次打开 TABLE_NAME，最后填入 `TABLE_NAME` 的值
- `EXPORT_PATH` 的路径：**"EXPORT_PATH"**
  意思是：在 JSON 中依次打开 EXPORT_PATH，最后填入 `EXPORT_PATH` 的值
- `UNIT` 的路径：**"UNIT"**
  意思是：在 JSON 中依次打开 UNIT，最后填入 `UNIT` 的值
- `FORCE` 的路径：**"FORCE"**
  意思是：在 JSON 中依次打开 FORCE，最后填入 `FORCE` 的值
- `DIST` 的路径：**"DIST"**
  意思是：在 JSON 中依次打开 DIST，最后填入 `DIST` 的值
- `HEAT` 的路径：**"HEAT"**
  意思是：在 JSON 中依次打开 HEAT，最后填入 `HEAT` 的值
- `TEMP` 的路径：**"TEMP"**
  意思是：在 JSON 中依次打开 TEMP，最后填入 `TEMP` 的值
- `STYLES` 的路径：**"STYLES"**
  意思是：在 JSON 中依次打开 STYLES，最后填入 `STYLES` 的值
- `FORMAT` 的路径：**"FORMAT"**
  意思是：在 JSON 中依次打开 FORMAT，最后填入 `FORMAT` 的值
- `PLACE` 的路径：**"PLACE"**
  意思是：在 JSON 中依次打开 PLACE，最后填入 `PLACE` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `NODE_ELEMS`：Node / Element No. Input• Use Only One of the Three Methods
- `KEYS` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TO` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STRUCTURE_GROUP_NAME` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/post/COLDFORMEDSTEELMEMBERDESIGNFORCES"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "TABLE_TYPE": "<TABLE_TYPE>"
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

自动提取结果——内力、位移、反力等数据直接读到 Python 里，不需要手动复制粘贴到 Excel。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：TABLE_TYPE 是必填的，漏掉任何一个都会报错。
3. **数组格式错误**：COMPONENTS、KEYS、PARTS 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/post/COLDFORMEDSTEELMEMBERDESIGNFORCES`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Cold Formed Design - Cold Formed Steel Member Design Forces 的 JSON 数据。"""
    data = {"TABLE_TYPE": "<TABLE_TYPE>"}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/post/COLDFORMEDSTEELMEMBERDESIGNFORCES", json=data, verify=False)
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
    r = session.post(f"{BASE}/post/COLDFORMEDSTEELMEMBERDESIGNFORCES", json=data)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---
