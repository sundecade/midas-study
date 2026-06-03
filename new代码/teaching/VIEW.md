# VIEW 视图命令

VIEW 端点只影响显示和截图，不负责建模或计算。

常用命令：

- `POST /view/ANGLE` 设置视角，例如 `{"Argument": {"HORIZONTAL": 30, "VERTICAL": 20}}`。
- `POST /view/CAPTURE` 输出图片，`FIGURE_NAME`、`EXPORT_PATH`、`WIDTH`、`HEIGHT` 放在 `Argument` 内。

如果要截取结果云图，请先完成分析并设置结果显示。
