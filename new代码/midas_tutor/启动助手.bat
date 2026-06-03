@echo off
chcp 65001 >nul
title MIDAS API Tutor
cd /d "%~dp0"

echo.
echo MIDAS API Tutor
echo ----------------------------------------

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found. Please install Python 3.10+ and tick "Add Python to PATH".
    pause
    exit /b 1
)

python -m pip show streamlit requests openai urllib3 beautifulsoup4 >nul 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    python install_deps.py
    if errorlevel 1 (
        echo Dependency installation failed.
        pause
        exit /b 1
    )
)

echo.
echo Starting Streamlit...
echo Open this address if the browser does not open automatically:
echo http://localhost:8501
echo.

python -m streamlit run app.py --server.port 8501
pause
