"""
MIDAS API 调用示例 —— 01 项目管理 —— 新建、打开、保存项目
======================================
目标读者：懂工程的工程师，第一次用 API
运行前提：
  1. MIDAS Civil 已启动并加载了项目
  2. Python 3 已安装
  3. 已安装 requests 库：pip install requests

每个例子都是完整的、可以单独运行的代码块。
直接复制粘贴到你的 Python 文件里就能跑。

⚠ 重要：MAPI-Key 放在 HTTP 请求头中，不是 URL 参数！
"""

import requests
import urllib3
import json
import sys
import os

# 关闭 SSL 警告（MIDAS 使用自签名证书）
urllib3.disable_warnings()

# ============================================================
# 第 0 步：获取配置
# ============================================================
# 两种方式任选其一：
#   方式一（推荐）：从注册表自动获取
#   方式二（备用）：手动指定

print("=" * 60)
print("01 项目管理 —— 新建、打开、保存项目")
print("=" * 60)

# ──── 方式一：从注册表自动获取（推荐，Windows 系统）────
print("\n>>> 获取 MIDAS API 配置")

def get_config_from_registry():
    """从 Windows 注册表自动获取 MIDAS 配置。"""
    try:
        import winreg
        reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)

        uri = winreg.QueryValueEx(key, "URI")[0]      # 服务地址
        port = winreg.QueryValueEx(key, "PORT")[0]    # 端口号
        mapi_key = winreg.QueryValueEx(key, "Key")[0] # MAPI-Key

        winreg.CloseKey(key)

        # 确保 STARTUP 已启用
        try:
            key_w = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path,
                                   0, winreg.KEY_WRITE)
        except FileNotFoundError:
            key_w = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        winreg.SetValueEx(key_w, "STARTUP", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key_w)

        base_url = f"https://{uri}:{port}/civil"
        print(f"从注册表获取配置成功: {base_url}")
        return base_url, mapi_key
    except Exception as e:
        print(f"注册表获取失败: {e}")
        return None, None

# ──── 方式二：手动指定配置（备用）────
def get_config_manual():
    """手动指定 MIDAS 配置。"""
    # ===== 修改这里 =====
    host = "127.0.0.1"              # MIDAS 服务地址
    port = "1102"                    # 端口号（Civil:1102, Gen:1202, Civil NX:1302）
    mapi_key = "your-mapi-key-here"  # MAPI-Key
    # ===================
    base_url = f"https://{host}:{port}/civil"
    print(f"使用手动配置: {base_url}")
    return base_url, mapi_key

# 先尝试自动获取，失败则使用手动配置
BASE_URL, MAPI_KEY = get_config_from_registry()
if BASE_URL is None:
    BASE_URL, MAPI_KEY = get_config_manual()
    print("提示：请将 get_config_manual() 中的参数修改为你的实际配置。")

# ============================================================
# 定义 MidasAPI 函数（核心！）
# ============================================================
# MAPI-Key 必须放在 HTTP 请求头中

def MidasAPI(method, command, body=None):
    """
    向 MIDAS 发送 API 请求。

    参数:
        method:  HTTP 方法 — "GET"（查询）、"POST"（创建）、
                 "PUT"（修改）、"DELETE"（删除）
        command: API 路径，如 "/db/NODE"
        body:    请求体数据（dict），POST/PUT 时使用
    """
    url = BASE_URL + command
    # 关键：MAPI-Key 放在请求头中
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY
    }

    print(f"发送 {method} 请求: {url}")

    if method == "POST":
        response = requests.post(url, headers=headers,
                                 json=body, verify=False, timeout=30)
    elif method == "PUT":
        response = requests.put(url, headers=headers,
                                json=body, verify=False, timeout=30)
    elif method == "GET":
        response = requests.get(url, headers=headers,
                                verify=False, timeout=30)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers,
                                   verify=False, timeout=30)
    else:
        print(f"错误：不支持的 HTTP 方法 {method}")
        return None

    print(f"响应状态码：{response.status_code}")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"请求失败：{response.text}")
        return None

# ============================================================
# 第 1 步：新建一个空项目
# ============================================================

print("\n>>> 第 1 步：新建项目")

# 构建 JSON 数据
# JSON → Python 对照:
#   {"A": 1}       →  {"A": 1}
#   {"A": [1,2]}   →  {"A": [1, 2]}
#   {"A": {"B":1}} →  {"A": {"B": 1}}

data_new = {
    "Argument": {}  # Argument 是参数容器，新建项目给空对象即可
}

print("要发送的 JSON：")
print(json.dumps(data_new, indent=2, ensure_ascii=False))

result = MidasAPI("POST", "/doc/NEW", body=data_new)
if result:
    print("项目创建成功！")
    print("MIDAS 返回：", json.dumps(result, indent=2, ensure_ascii=False))

# ============================================================
# 第 2 步：保存项目到文件
# ============================================================

print("\n>>> 第 2 步：保存项目")

data_save = {
    "Argument": "C:\\MIDAS\\my_project.mcb"
    #            ↑ Windows 路径中的 \ 要写成 \\（JSON 转义规则）
    #            或者用正斜杠: "C:/MIDAS/my_project.mcb"
}

print("要发送的 JSON：")
print(json.dumps(data_save, indent=2, ensure_ascii=False))

result = MidasAPI("POST", "/doc/SAVEAS", body=data_save)
if result:
    print("项目保存成功！")

# ============================================================
# 第 3 步：打开已有项目
# ============================================================

print("\n>>> 第 3 步：打开已有项目")

data_open = {
    "Argument": "C:\\MIDAS\\my_project.mcb"
}

result = MidasAPI("POST", "/doc/OPEN", body=data_open)
if result:
    print("项目打开成功！")

# ============================================================
# 第 4 步：关闭项目
# ============================================================

print("\n>>> 第 4 步：关闭项目")

data_close = {"Argument": {}}

result = MidasAPI("POST", "/doc/CLOSE", body=data_close)
if result:
    print("项目已关闭。")

# ============================================================
# 总结
# ============================================================
# 1. MAPI-Key 放在请求头中，参数名是 "MAPI-Key"
# 2. base_url 末尾有 /civil
# 3. 推荐从注册表自动获取配置（get_config_from_registry）
# 4. 备用方式：手动指定 host、port、mapi_key（get_config_manual）
# 5. 所有 DOC 接口都用 POST 方法
# 6. JSON 结构: {"Argument": ...}
# 7. 发请求用 MidasAPI(method, path, body)
# 8. 检查返回值是否为 None 判断成功或失败
