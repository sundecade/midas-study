"""
MIDAS API 工具函数
===================
提供两种配置方式：
  方式一（推荐）：自动从 Windows 注册表获取 base_url 和 MAPI-Key
  方式二（备用）：手动指定 base_url 和 MAPI-Key

所有 API 请求都通过 MAPI-Key 请求头进行身份认证。

使用方法：
    from utils import auto_config, manual_config, MidasAPI

    # 方式一：自动获取配置
    config = auto_config()
    result = MidasAPI("GET", "/db/NODE/1", config=config)

    # 方式二：手动指定配置
    config = manual_config("127.0.0.1", "1102", "your-mapi-key")
    result = MidasAPI("POST", "/db/NODE", {"Assign": {...}}, config=config)
"""

import requests
import urllib3
import json

urllib3.disable_warnings()

# ============================================================
# 配置函数 —— 两种方式获取 base_url 和 MAPI-Key
# ============================================================


def auto_config():
    """
    从 Windows 注册表自动获取 MIDAS API 配置（推荐方式）。

    读取 MIDAS 安装时写入注册表的连接信息：
      - URI:  服务地址（如 127.0.0.1）
      - PORT: 端口号
      - Key:  MAPI-Key

    返回:
        {"base_url": "...", "mapi_key": "..."}
        失败返回 None

    例子:
        config = auto_config()
        if config:
            result = MidasAPI("GET", "/db/NODE/1", config=config)
    """
    try:
        import winreg
        reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)

        uri = winreg.QueryValueEx(key, "URI")[0]
        port = winreg.QueryValueEx(key, "PORT")[0]
        mapi_key = winreg.QueryValueEx(key, "Key")[0]
        winreg.CloseKey(key)

        # 确保 STARTUP 已启用
        _ensure_startup_enabled(reg_path)

        base_url = f"https://{uri}:{port}/civil"
        print(f"自动获取配置成功: {base_url}")
        return {"base_url": base_url, "mapi_key": mapi_key}

    except Exception as e:
        print(f"自动获取配置失败: {e}")
        print("请确认 MIDAS 已安装，或使用 manual_config() 手动指定配置")
        return None


def manual_config(host="127.0.0.1", port="1102", mapi_key=""):
    """
    手动指定 MIDAS API 配置（备用方式）。

    参数:
        host:     MIDAS 服务地址（默认 127.0.0.1）
        port:     端口号（默认 1102）
        mapi_key: MAPI-Key（在 MIDAS 软件中生成）

    返回:
        {"base_url": "...", "mapi_key": "..."}

    例子:
        config = manual_config("127.0.0.1", "1102", "abc123-mapi-key")
    """
    base_url = f"https://{host}:{port}/civil"
    return {"base_url": base_url, "mapi_key": mapi_key}


def _ensure_startup_enabled(reg_path):
    """确保注册表中 STARTUP 值为 1（启用 API 服务）。"""
    try:
        import winreg
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path,
                                 0, winreg.KEY_WRITE)
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

        winreg.SetValueEx(key, "STARTUP", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
    except Exception:
        pass  # STARTUP 设置失败不影响后续使用


# ============================================================
# API 调用函数
# ============================================================


def MidasAPI(method, command, body=None, config=None):
    """
    向 MIDAS 发送 API 请求。

    参数:
        method:  HTTP 方法 — "GET"（查询）、"POST"（创建）、
                 "PUT"（修改）、"DELETE"（删除）
        command: API 路径，如 "/db/NODE"、"/doc/NEW"
        body:    Python 字典（POST/PUT 时发送），会自动转为 JSON
        config:  配置字典，包含 base_url 和 mapi_key。
                 可通过 auto_config() 或 manual_config() 获取。
                 如果未提供，会自动尝试 auto_config()。

    返回:
        MIDAS 返回的 JSON 数据（Python 字典），失败返回 None

    例子:
        config = auto_config()
        result = MidasAPI("GET", "/db/NODE/1", config=config)
        result = MidasAPI("POST", "/db/NODE",
                          {"Assign": {"1": {"X": 0, "Y": 0, "Z": 0}}},
                          config=config)
    """
    # 如果没传入配置，尝试自动获取
    if config is None:
        config = auto_config()
        if config is None:
            print("错误：无法获取 MIDAS 配置。")
            print("  方式一：确保 MIDAS 已安装，重试自动获取")
            print("  方式二：使用 manual_config(host, port, mapi_key) 手动指定")
            return None

    base_url = config["base_url"]
    mapi_key = config["mapi_key"]
    url = base_url + command

    # MAPI-Key 放在 HTTP 请求头中
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": mapi_key
    }

    try:
        if method == "POST":
            response = requests.post(url, headers=headers, json=body,
                                     verify=False, timeout=30)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=body,
                                    verify=False, timeout=30)
        elif method == "GET":
            response = requests.get(url, headers=headers,
                                    verify=False, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers,
                                       verify=False, timeout=30)
        else:
            print(f"错误：不支持的 HTTP 方法 {method}")
            return None

        if response.status_code == 200:
            return response.json()
        else:
            print(f"错误：{command} 返回状态码 {response.status_code}")
            print(f"  信息：{response.text}")
            return None

    except requests.exceptions.ConnectionError:
        print(f"错误：无法连接到 MIDAS（{base_url}）")
        print("  请确认 MIDAS 已启动并加载了项目。")
        return None
    except Exception as e:
        print(f"错误：{e}")
        return None


# ============================================================
# 便捷函数 —— 封装常用建模操作
# ============================================================


def create_nodes(nodes_dict, config=None):
    """
    批量创建节点。

    参数:
        nodes_dict: {
            "1": {"X": 0, "Y": 0, "Z": 0},
            "2": {"X": 5000, "Y": 0, "Z": 0},
            ...
        }
        config: 配置字典（可选）

    返回:
        MIDAS 的响应数据

    例子:
        nodes = {}
        for i in range(10):
            nodes[str(i+1)] = {"X": i*1000, "Y": 0, "Z": 0}
        create_nodes(nodes, config)
    """
    return MidasAPI("POST", "/db/NODE", {"Assign": nodes_dict}, config=config)


def create_materials(materials_dict, config=None):
    """
    批量创建材料。

    参数:
        materials_dict: {
            "1": {"TYPE": "CONC", "NAME": "C50", "PARAM": {...}},
            "2": {"TYPE": "STEEL", "NAME": "Q345", "PARAM": {...}},
        }
        config: 配置字典（可选）

    返回:
        MIDAS 的响应数据
    """
    return MidasAPI("POST", "/db/MATL", {"Assign": materials_dict}, config=config)


def make_linear_nodes(start_x, end_x, num, y=0, z=0):
    """
    生成一排等间距节点的数据字典（不发送请求）。

    参数:
        start_x: 起点 X 坐标
        end_x:   终点 X 坐标
        num:     节点数量
        y:       Y 坐标（默认 0）
        z:       Z 坐标（默认 0）

    返回:
        {"1": {"X": ..., "Y": ..., "Z": ...}, "2": {...}, ...}

    例子:
        nodes = make_linear_nodes(0, 10000, 11)
        create_nodes(nodes, config)
    """
    nodes = {}
    for i in range(num):
        if num > 1:
            x = start_x + (end_x - start_x) * i / (num - 1)
        else:
            x = start_x
        nodes[str(i + 1)] = {"X": x, "Y": y, "Z": z}
    return nodes


def make_grid_nodes(x0, y0, nx, ny, dx, dy, z=0):
    """
    生成二维网格节点数据（不发送请求）。

    参数:
        x0, y0: 起始点坐标
        nx, ny: X 和 Y 方向的节点数
        dx, dy: X 和 Y 方向的间距
        z:      Z 坐标（默认 0）

    返回:
        {"1": {"X": ..., "Y": ..., "Z": ...}, "2": {...}, ...}

    例子:
        nodes = make_grid_nodes(0, 0, nx=5, ny=4, dx=2000, dy=2000)
        create_nodes(nodes, config)
    """
    nodes = {}
    node_id = 1
    for j in range(ny):
        for i in range(nx):
            nodes[str(node_id)] = {
                "X": x0 + i * dx,
                "Y": y0 + j * dy,
                "Z": z
            }
            node_id += 1
    return nodes


def new_project(config=None):
    """新建项目。"""
    return MidasAPI("POST", "/doc/NEW", {"Argument": {}}, config=config)


def save_project(filepath, config=None):
    """保存项目。"""
    return MidasAPI("POST", "/doc/SAVEAS", {"Argument": filepath}, config=config)


def close_project(config=None):
    """关闭项目。"""
    return MidasAPI("POST", "/doc/CLOSE", {"Argument": {}}, config=config)


# ============================================================
# 测试运行
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("MIDAS API 工具函数测试")
    print("=" * 50)

    # 先尝试自动获取配置
    print("\n--- 尝试自动获取配置 ---")
    config = auto_config()

    if config is None:
        print("\n--- 自动获取失败，使用手动配置示例 ---")
        config = manual_config("127.0.0.1", "1102", "your-mapi-key-here")
        print(f"base_url:  {config['base_url']}")
        print(f"mapi_key:  {config['mapi_key']}")
        print("\n请将 your-mapi-key-here 替换为实际的 MAPI-Key")
    else:
        print(f"\nbase_url:  {config['base_url']}")
        print(f"mapi_key:  {config['mapi_key'][:8]}...")

        # 测试连接
        print("\n--- 测试连接 ---")
        result = MidasAPI("GET", "/ope/PROJECTSTATUS", config=config)
        if result:
            print("连接成功！")
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("连接失败。请确保 MIDAS 已启动并加载了项目。")

    # 演示 make_linear_nodes
    print("\n--- 演示 make_linear_nodes ---")
    print("输入: start_x=0, end_x=10000, num=5")
    nodes = make_linear_nodes(0, 10000, 5)
    print("输出:")
    print(json.dumps(nodes, indent=2, ensure_ascii=False))

    # 演示 make_grid_nodes
    print("\n--- 演示 make_grid_nodes ---")
    print("输入: x0=0, y0=0, nx=3, ny=2, dx=2000, dy=3000")
    grid = make_grid_nodes(0, 0, nx=3, ny=2, dx=2000, dy=3000)
    print("输出:")
    print(json.dumps(grid, indent=2, ensure_ascii=False))
