@echo off
title Defect Tracker Pro — with Public Share
color 0A
echo.
echo  ============================================
echo   DEFECT TRACKER PRO  — Starting...
echo  ============================================
echo.

:: ── Check Python ──────────────────────────────────────────────
python --version >nul 2>&1
if %errorlevel% neq 0 (
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo  [ERROR] Python not found!
        echo  Download from: https://python.org
        echo  Check "Add Python to PATH" during install.
        pause
        exit /b 1
    )
    set PYTHON=py
) else (
    set PYTHON=python
)

echo  [OK] Python found.
echo.

:: ── Install dependencies via python -m pip (avoids PATH issues) ─
echo  [1/3] Installing / checking dependencies...
echo        (First run may take a minute)
echo.
%PYTHON% -m pip install flask flask-login psycopg2-binary werkzeug openpyxl pyngrok --quiet --upgrade

if %errorlevel% neq 0 (
    echo.
    echo  [ERROR] Dependency install failed.
    echo  Try: right-click this file, Run as Administrator.
    pause
    exit /b 1
)

echo  [2/3] Dependencies ready.
echo.
echo  [3/3] Starting server + public share link...
echo.
echo  ============================================
echo   FIRST TIME ONLY  (optional, stable links):
echo     1. Sign up free at https://ngrok.com
echo     2. Copy your authtoken from the dashboard
echo     3. Run once in CMD:
echo        python run_with_share.py --set-token TOKEN
echo  ============================================
echo.

%PYTHON% run_with_share.py
pause
