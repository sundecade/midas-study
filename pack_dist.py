"""打包 MIDAS 学习助手为可分发的 zip 文件"""
import zipfile
import os
from pathlib import Path

ROOT = Path(__file__).parent
DIST_DIR = ROOT / "dist"
DIST_DIR.mkdir(exist_ok=True)

# 需要包含的文件/目录 (相对于项目根目录)
INCLUDE = [
    # 核心应用
    "midas_tutor/app.py",
    "midas_tutor/llm.py",
    "midas_tutor/retriever.py",
    "midas_tutor/search_cli.py",
    "midas_tutor/requirements.txt",
    "midas_tutor/启动助手.bat",
    "midas_tutor/.streamlit/config.toml",
    # 知识库
    "midas_api_knowledge_base.json",
    # 教学资料
    "teaching/",
    # 代码示例
    "code_examples/00_config_setup.py",
    "code_examples/01_project_management.py",
    "code_examples/02_create_model.py",
    "code_examples/03_apply_loads.py",
    "code_examples/04_run_analysis.py",
    "code_examples/05_extract_results.py",
    "code_examples/06_view_control.py",
    "code_examples/utils.py",
    "code_examples/README.md",
    # 工具
    "test_endpoint.py",
    "enhance_kb.py",
    # 文档
    "README.md",
]

# 需要排除的模式 (应用于 INCLUDE 中的目录递归)
EXCLUDE_PATTERNS = ["__pycache__", "*.pyc", "user_saved"]

def should_exclude(path: str) -> bool:
    for pat in EXCLUDE_PATTERNS:
        if pat.startswith("*"):
            if path.endswith(pat[1:]):
                return True
        elif pat in path:
            return True
    return False

def collect_files():
    """收集所有要打包的文件"""
    files = []
    for item in INCLUDE:
        src = ROOT / item
        if src.is_file():
            files.append(src)
        elif src.is_dir():
            for f in src.rglob("*"):
                if f.is_file() and not should_exclude(str(f)):
                    files.append(f)
        else:
            print(f"  ⚠ 跳过（不存在）: {item}")
    return files

def main():
    print("📦 正在收集文件...")
    files = collect_files()
    print(f"  共 {len(files)} 个文件")

    zip_path = DIST_DIR / "midas-study-分享版.zip"
    print(f"📦 正在打包到 {zip_path}...")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            arcname = f.relative_to(ROOT)
            zf.write(f, arcname)

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"✅ 打包完成！")
    print(f"   文件: {zip_path}")
    print(f"   大小: {size_mb:.1f} MB")
    print()
    print("📤 分享方式：")
    print("   - U盘/移动硬盘拷贝")
    print("   - 局域网共享文件夹")
    print("   - 微信/QQ 发送文件（如超过限制可分段压缩）")
    print("   - 上传到网盘（百度网盘/阿里云盘等）")
    print()
    print("👤 接收方使用方法：")
    print("   1. 解压 zip 文件")
    print("   2. 安装 Python 3.12")
    print("   3. 双击 midas_tutor/启动助手.bat")
    print("   或手动: pip install -r midas_tutor/requirements.txt")
    print("          cd midas_tutor && streamlit run app.py")
    print()
    print("💡 没有安装 MIDAS 也能使用：")
    print("   在侧边栏「MIDAS 连接设置」选择手动输入 base_url 和 MAPI-Key")
    print("   搜索、浏览、AI对话功能不受影响")

if __name__ == "__main__":
    main()
