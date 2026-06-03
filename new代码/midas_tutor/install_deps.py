"""Install dependencies for the Streamlit tutor app.

This script uses only the Python standard library so it can run on a fresh
machine before third-party packages are installed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQ = ROOT / "requirements.txt"
MIRROR = "https://pypi.tuna.tsinghua.edu.cn/simple"


def run(args: list[str]) -> bool:
    print("\n>", " ".join(args))
    completed = subprocess.run(args)
    return completed.returncode == 0


def main() -> int:
    python = sys.executable

    if not run([python, "-m", "pip", "--version"]):
        print("pip is not available. Trying ensurepip...")
        run([python, "-m", "ensurepip", "--upgrade"])

    if run([python, "-m", "pip", "install", "-r", str(REQ)]):
        return 0

    print("\nDefault PyPI install failed. Retrying with a China mirror...")
    if run([python, "-m", "pip", "install", "-r", str(REQ), "-i", MIRROR, "--trusted-host", "pypi.tuna.tsinghua.edu.cn"]):
        return 0

    print("\nInstall failed.")
    print("Try manually:")
    print(f"  {python} -m pip install -r {REQ}")
    print(f"  {python} -m pip install -r {REQ} -i {MIRROR}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
