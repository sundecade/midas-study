import requests
import os

# 从注册表获取 Url 和 Mapi-key
reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)

reg_uri = winreg.QueryValueEx(key, "URI")[0]  # 获取URI
reg_port = winreg.QueryValueEx(key, "PORT")[0]  # 获取PORT
reg_key = winreg.QueryValueEx(key, "Key")[0]  # 获取Mapi-key

base_url = "https://" + reg_uri + ":" + reg_port + "/civil"  # 定义基础URL


# 查询注册表有无 STARTUP，没有的话添加
value_name = "STARTUP"
value_data = 1

# 打开注册表键
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         reg_path, 0, winreg.KEY_WRITE)
except FileNotFoundError:
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)

# 设置DWORD值
winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)

# 查询STARTUP
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
reg_startup = winreg.QueryValueEx(key, value_name)[0]  # 获取STARTUP
# 关闭注册表键
winreg.CloseKey(key)
def MidasAPI(method, command, body=None):
   
    url = base_url + command
    print(f"请求的 URL: {url}")
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": reg_key
    }

    try:
        if method == "POST":
            response = requests.post(url=url, headers=headers, json=body)
        elif method == "PUT":
            response = requests.put(url=url, headers=headers, json=body)
        elif method == "GET":
            response = requests.get(url=url, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url=url, headers=headers)

        response.raise_for_status()
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return None

    print(method, command, response.status_code)
    return response.json()