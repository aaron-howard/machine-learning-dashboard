@echo off
echo ============================================================
echo                ML Dashboard Startup Script
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher and try again
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements if needed
echo Checking dependencies...
pip install -r requirements.txt >nul 2>&1

REM Start the application
echo Starting ML Dashboard...
echo.
echo The dashboard will open in your browser automatically.
echo If it doesn't open, navigate to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python run.py

pause
