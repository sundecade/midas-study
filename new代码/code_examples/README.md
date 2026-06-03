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
