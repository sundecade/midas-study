# 常见错误

1. 对 `/db/UNIT` 发送 POST。正确做法是 PUT。
2. DB 端点缺少 `Assign` 包装。
3. 多个支座都塞进同一个 `ITEMS` 数组。正确做法是每个支座使用独立数字键。
4. `/db/ELEM` 使用旧字段名。正确字段是 `MATL`、`SECT`、`NODE`。
5. 把 POST 表名当 URL。正确做法是请求 `/post/TABLE`，再设置 `TABLE_TYPE`。
6. 把 schema 里的 `properties` 当作请求体。应以搜索结果中的 `request_templates` 为准。
