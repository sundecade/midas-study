@echo off
title MIDAS API 智能学习助手
cd /d "%~dp0"

echo.
echo   ╔══════════════════════════════════════════╗
echo   ║    MIDAS API 智能学习助手              ║
echo   ║    搜索和浏览 - 无需 API Key           ║
echo   ╚══════════════════════════════════════════╝
echo.

REM 检查 streamlit 是否已安装
python -m pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo   首次运行，正在安装依赖...
    python -m pip install -q streamlit openai urllib3
    echo.
)

echo   正在启动服务器...
echo.
echo   ═══════════════════════════════════════════
echo   启动完成后，请打开浏览器访问:
echo.
echo       http://localhost:8501
echo.
echo   按 Ctrl+C 可停止服务器
echo   ═══════════════════════════════════════════
echo.

python -m streamlit run app.py --server.port 8501

pause
