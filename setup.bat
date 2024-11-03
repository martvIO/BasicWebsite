@echo off
SET "PYTHON_VERSION=3.12.0"
SET "PYTHON_INSTALLER=python-3.12.0-amd64.exe"
SET "PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%"

REM Check if Python 3.12 is installed
python --version 2>nul | findstr /C:"%PYTHON_VERSION%" >nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python %PYTHON_VERSION% is not installed. Installing Python...
    
    REM Download Python installer
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER_URL% -OutFile %PYTHON_INSTALLER%"
    
    REM Install Python silently
    start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    REM Clean up installer
    del %PYTHON_INSTALLER%
) ELSE (
    echo Python %PYTHON_VERSION% is already installed.
)

REM Create the virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Upgrade pip
pip install --upgrade pip

REM Install required modules from requirements.txt
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo requirements.txt file not found.
)

echo Setup complete!
pause
