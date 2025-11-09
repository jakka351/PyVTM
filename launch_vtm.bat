@echo off
REM Vehicle Traffic Monitor Launcher
REM Ford Motor Company CAN Bus Monitor

echo ========================================
echo  Vehicle Traffic Monitor v7.81.6
echo  Ford Motor Company
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python detected...
echo.

REM Check if j2534.py exists
if not exist "j2534.py" (
    echo WARNING: j2534.py not found
    echo The application will run in demo mode
    echo.
)

REM Check if vtm_main.py exists
if not exist "vtm_main.py" (
    echo ERROR: vtm_main.py not found
    echo Please ensure all project files are in the same directory
    pause
    exit /b 1
)

echo Launching Vehicle Traffic Monitor...
echo.
echo TIP: Connect your J2534 device before starting
echo      Go to Setup -^> Device Selection to select device
echo.

REM Launch the application
python vtm_main.py

if errorlevel 1 (
    echo.
    echo Application exited with error
    pause
)
