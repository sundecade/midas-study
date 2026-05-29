"""
MIDAS API 调用示例 —— 00 配置设置 —— 自动获取或手动指定连接
=============================================
目标读者：懂工程的工程师，第一次用 API
运行前提：
  1. MIDAS Civil 已安装（自动获取方式）或知道连接信息（手动方式）
  2. Python 3 已安装
  3. 已安装 requests 库：pip install requests

本文件演示两种配置方式，你可以根据情况选择。
每个例子都是完整的、可以单独运行的代码块。
"""

import requests
import urllib3

urllib3.disable_warnings()

print("=" * 60)
print("00 配置设置 —— 获取 MIDAS API 连接信息")
print("=" * 60)

# ============================================================
# 方式一：从 Windows 注册表自动获取（推荐）
# ============================================================
# 适用条件：
#   - Windows 系统
#   - MIDAS Civil/Gen 已安装
#   - MIDAS 软件已至少运行过一次
#
# MIDAS 安装后会在注册表中写入：
#   HKEY_CURRENT_USER\SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION
#     ├── URI  → 服务地址（如 127.0.0.1）
#     ├── PORT → 端口号
#     ├── Key  → MAPI-Key
#     └── STARTUP → 需设为 1（启用 API）

print("\n" + "=" * 60)
print("方式一：从注册表自动获取配置")
print("=" * 60)

try:
    import winreg

    # 注册表路径（MIDAS 安装时自动写入）
    reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"

    # 打开注册表键
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)

    # 读取连接信息
    reg_uri = winreg.QueryValueEx(key, "URI")[0]    # 服务地址
    reg_port = winreg.QueryValueEx(key, "PORT")[0]  # 端口号
    reg_key = winreg.QueryValueEx(key, "Key")[0]    # MAPI-Key

    winreg.CloseKey(key)

    # 拼接 base_url（注意末尾有 /civil）
    base_url = f"https://{reg_uri}:{reg_port}/civil"

    print(f"服务地址: {reg_uri}")
    print(f"端口号:   {reg_port}")
    print(f"base_url: {base_url}")
    print(f"MAPI-Key: {reg_key[:8]}...（已隐藏后半部分）")

    # 确保 STARTUP 已启用
    print("\n检查 API 服务状态...")
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path,
                             0, winreg.KEY_WRITE)
    except FileNotFoundError:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

    winreg.SetValueEx(key, "STARTUP", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)
    print("API 服务已启用。")

except ImportError:
    print("当前不是 Windows 系统，无法读取注册表。请使用方式二。")
    base_url = None
    reg_key = None

except FileNotFoundError:
    print("未找到 MIDAS 注册表项。请确认 MIDAS 已安装并至少运行过一次。")
    print("如果确认已安装，请使用方式二手动指定。")
    base_url = None
    reg_key = None

except Exception as e:
    print(f"读取注册表出错: {e}")
    print("请使用方式二手动指定配置。")
    base_url = None
    reg_key = None

# ============================================================
# 方式二：手动指定配置（备用）
# ============================================================
# 适用条件：
#   - 非 Windows 系统
#   - 注册表读取失败
#   - 需要连接远程 MIDAS 服务
#
# 如何获取这些信息：
#   1. 在 MIDAS 软件中找到 MAPI-Key（通常在设置或帮助菜单中）
#   2. 默认端口通常是 1102（Civil）、1202（Gen）、1302（Civil NX）
#   3. 本机地址是 127.0.0.1

print("\n" + "=" * 60)
print("方式二：手动指定配置")
print("=" * 60)

# 如果你已经从注册表获取成功，这里的值可以直接忽略
# 如果注册表获取失败，请手动填写以下三个值：
manual_host = "127.0.0.1"                    # MIDAS 服务地址
manual_port = "1102"                          # 端口号
manual_key = "your-mapi-key-here"             # MAPI-Key

manual_base_url = f"https://{manual_host}:{manual_port}/civil"

print(f"手动 - base_url: {manual_base_url}")
print(f"手动 - MAPI-Key: {manual_key}")
print("提示：如果使用注册表方式成功，请优先使用注册表获取的配置。")

# ============================================================
# 定义 MidasAPI 函数（两种方式共用）
# ============================================================
# MAPI-Key 放在 HTTP 请求头中发送，这是关键！

print("\n" + "=" * 60)
print("定义 MidasAPI 调用函数")
print("=" * 60)

def MidasAPI(method, command, body=None, base_url=None, mapi_key=None):
    """
    向 MIDAS 发送 API 请求。

    参数:
        method:   HTTP 方法（GET/POST/PUT/DELETE）
        command:  API 路径（如 /db/NODE）
        body:     请求体（POST/PUT 时使用）
        base_url: MIDAS 服务地址
        mapi_key: MAPI-Key
    """
    url = base_url + command
    # MAPI-Key 放在请求头中
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": mapi_key
    }

    print(f"发送 {method} 请求: {url}")

    try:
        if method == "POST":
            response = requests.post(url, headers=headers, json=body, verify=False, timeout=30)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=body, verify=False, timeout=30)
        elif method == "GET":
            response = requests.get(url, headers=headers, verify=False, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, verify=False, timeout=30)
        else:
            print(f"错误：不支持的 HTTP 方法 {method}")
            return None

        print(f"响应状态: {response.status_code}")

        if response.status_code == 200:
            return response.json()
        else:
            print(f"请求失败: {response.text}")
            return None

    except requests.exceptions.ConnectionError:
        print(f"连接失败：无法连接到 {base_url}")
        print("请确认 MIDAS 已启动并加载了项目。")
        return None
    except Exception as e:
        print(f"请求出错: {e}")
        return None

# ============================================================
# 测试连接
# ============================================================

print("\n" + "=" * 60)
print("测试 MIDAS API 连接")
print("=" * 60)

# 选择使用哪种配置：
#   如果注册表获取成功 → 使用注册表配置（推荐）
#   如果注册表获取失败 → 使用手动配置
if base_url is not None and reg_key is not None:
    print("使用自动获取的配置...")
    test_base_url = base_url
    test_mapi_key = reg_key
else:
    print("使用手动指定的配置...")
    test_base_url = manual_base_url
    test_mapi_key = manual_key

# 测试：查询项目状态
print(f"\n测试 GET /ope/PROJECTSTATUS ...")
result = MidasAPI("GET", "/ope/PROJECTSTATUS",
                  base_url=test_base_url, mapi_key=test_mapi_key)

if result:
    print("连接成功！MIDAS API 服务正常运行。")
    import json
    print("项目状态:", json.dumps(result, indent=2, ensure_ascii=False))
else:
    print("连接失败。请检查：")
    print("  1. MIDAS 软件是否已启动")
    print("  2. 是否已加载项目文件")
    print("  3. base_url 和 MAPI-Key 是否正确")
    print("  4. 注册表中 STARTUP 是否为 1")
