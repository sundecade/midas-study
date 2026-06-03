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
