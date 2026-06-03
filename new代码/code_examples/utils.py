"""Small helper functions for MIDAS API examples.

All example scripts use the same call shape:

    result = MidasAPI("POST", "/db/NODE", {"Assign": {...}}, config)

DB endpoints create/update data with:
    {"Assign": {"1": {data}, "2": {data}}}

DOC/OPE/VIEW/POST endpoints usually use:
    {"Argument": {data}}
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests
import urllib3

urllib3.disable_warnings()


def auto_config() -> dict[str, str] | None:
    """Read base_url and MAPI-Key from the Windows registry."""
    try:
        import winreg

        reg_path = r"SOFTWARE\MIDAS\CVLwNX_CH\CONNECTION"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
        uri = winreg.QueryValueEx(key, "URI")[0]
        port = winreg.QueryValueEx(key, "PORT")[0]
        mapi_key = winreg.QueryValueEx(key, "Key")[0]
        winreg.CloseKey(key)

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "STARTUP", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
        except Exception:
            pass

        return {"base_url": f"https://{uri}:{port}/civil", "mapi_key": mapi_key}
    except Exception as exc:
        print(f"Cannot read MIDAS registry config: {exc}")
        return None


def manual_config(
    base_url: str = "https://127.0.0.1:1102/civil",
    mapi_key: str = "replace-with-your-mapi-key",
) -> dict[str, str]:
    """Use this when registry lookup is not available."""
    return {"base_url": base_url.rstrip("/"), "mapi_key": mapi_key}


def get_config() -> dict[str, str]:
    """Prefer registry config, then fall back to manual placeholders."""
    config = auto_config()
    if config:
        return config
    print("Using manual_config placeholder. Edit mapi_key before sending requests.")
    return manual_config()


def MidasAPI(
    method: str,
    command: str,
    body: dict[str, Any] | None = None,
    config: dict[str, str] | None = None,
) -> Any:
    """Send one request to MIDAS and return decoded JSON when possible."""
    config = config or get_config()
    method = method.upper()
    url = config["base_url"].rstrip("/") + command
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": config["mapi_key"],
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, verify=False, timeout=60)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=body or {}, verify=False, timeout=60)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=body or {}, verify=False, timeout=60)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, json=body or {}, verify=False, timeout=60)
        else:
            raise ValueError(f"Unsupported method: {method}")
    except requests.exceptions.ConnectionError:
        print(f"Cannot connect to {config['base_url']}. Start MIDAS and enable API first.")
        return None

    if not response.ok:
        print(f"{method} {command} failed: HTTP {response.status_code}")
        print(response.text[:1000])
        return None

    try:
        return response.json()
    except ValueError:
        return response.text


def show(title: str, value: Any) -> None:
    """Pretty-print one API response."""
    print(f"\n--- {title} ---")
    if isinstance(value, (dict, list)):
        print(json.dumps(value, ensure_ascii=False, indent=2))
    else:
        print(value)


def save_json(path: str, value: Any) -> None:
    """Save a response beside the example script."""
    out = Path(__file__).resolve().parent / path
    out.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {out}")
