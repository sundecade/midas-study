# MIDAS API 代码示例

> 面向工程师的 Python API 调用示例 —— 每个脚本都可以单独运行。

## 文件说明

| 文件 | 内容 | 适合谁 |
|------|------|--------|
| `00_config_setup.py` | **先看这个！** 两种配置方式：注册表自动获取 / 手动指定 | **所有人先看** |
| `utils.py` | 工具函数库（封装了 auto_config、manual_config、MidasAPI） | 需要快速上手 |
| `01_project_management.py` | 新建、保存、打开、关闭项目 | 第一次用 API |
| `02_create_model.py` | 创建节点、单元、材料、截面 | 需要自动化建模 |
| `03_apply_loads.py` | 施加边界条件和荷载 | 需要批量加载 |
| `04_run_analysis.py` | 执行分析和操作命令 | 需要自动化分析 |
| `05_extract_results.py` | 提取分析结果数据 | 需要批量出结果 |
| `06_view_control.py` | 选择对象和截图 | 需要自动截图 |

## 配置方式

**方式一（推荐）：从 Windows 注册表自动获取**
- 适用于 Windows 系统 + MIDAS 已安装
- 自动读取 base_url 和 MAPI-Key
- 无需手动填写任何参数
- 详见 `00_config_setup.py` 中的「方式一」

**方式二（备用）：手动指定**
- 适用于非 Windows 系统或注册表读取失败
- 需要手动填写 host、port、mapi_key
- 详见 `00_config_setup.py` 中的「方式二」

## 怎么用？

1. 确保 MIDAS 已打开并加载了项目
2. 安装 Python 依赖：`pip install requests urllib3`
3. **先运行 `00_config_setup.py`** 确认配置正确
4. 从 `01_project_management.py` 开始，逐个运行
5. **不要一次全运行** —— 每个脚本会修改你的模型

## MAPI-Key 认证机制

- **MAPI-Key 放在 HTTP 请求头中**（`"MAPI-Key": key`），不是 URL 参数
- 每个用户的 MIDAS 软件中生成唯一的 MAPI-Key
- 所有 API 请求都需要携带 MAPI-Key 进行身份认证

## Python 零基础？

建议先花 5 分钟看 `../teaching/appendix/json-basics.md` 了解 JSON 基础。

## 代码风格

所有代码遵循以下原则：
- 只使用最基础的 Python 语法（dict, list, for, if, def）
- 每个操作都有中文注释
- 循环逻辑单独解释
- JSON 结构和生成过程都有说明
- 不使用 lambda、生成器、装饰器、类等高阶语法
