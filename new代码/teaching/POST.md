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
