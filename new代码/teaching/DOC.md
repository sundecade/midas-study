# DOC 项目命令

DOC 命令控制项目文件和分析状态，不负责创建节点、单元、材料或荷载。

常用流程：

1. `POST /doc/NEW` 新建项目，请求体为 `{"Argument": {}}`。
2. `PUT /db/UNIT` 设置单位。
3. 通过 DB 端点写入模型数据。
4. `POST /doc/ANAL` 提交分析。
5. `POST /doc/SAVEAS` 保存项目。

注意：`/doc/ANAL` 是分析命令；具体模型数据仍然来自 DB。
