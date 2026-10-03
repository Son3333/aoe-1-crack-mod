@echo off
chcp 65001 >nul
title AOE 1: Rise of Rome - Mod Pro Launcher
cd /d "%~dp0"

echo ======================================================================
echo          AOE 1: RISE OF ROME - MOD MENU PRO LAUNCHER
echo ======================================================================
echo.

:: 1. Kiem tra Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] May ban chua cai dat Python hoac chua them vao PATH!
    echo [*] Dang mo trinh duyet de tai Python 3...
    start https://www.python.org/downloads/
    echo.
    echo Vui long cai Python va nho tich vao o: "Add Python to PATH"!
    pause
    exit /b 1
)

:: 2. Tu dong kiem tra va cai dat thu vien can thiet
echo [*] Dang kiem tra thu vien (psutil, keyboard)...
python -c "import psutil, keyboard" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Dang tu dong cai dat thu vien can thiet...
    python -m pip install --quiet psutil keyboard
    if %errorlevel% neq 0 (
        echo [!] Khong the tu dong cai dat thu vien qua pip!
        pause
        exit /b 1
    )
    echo [OK] Cai dat thu vien thanh cong!
) else (
    echo [OK] Thu vien da san sang!
)

echo.
echo ======================================================================
echo [*] Dang khoi chay Game Age of Empires va Mod Menu Pro...
echo ======================================================================

:: 3. Khoi chay Game va Mod Menu
start "" "Age_of_Empires.exe" nostartup
start "" pythonw "mod_menu.py"

echo.
echo [THANH CONG] Game va Mod Menu da duoc khoi chay!
echo Biet danh: Bm F1-F8 hoac so 1-8 de su dung cheat.
echo Nhan [Insert] tren ban phim de an/hien Menu.
timeout /t 3 >nul
exit /b 0

