@echo off
REM Check if the .venv directory exists
if not exist .venv (
    echo Virtual environment .venv not found. Please create it first.
    exit /b
)

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Run the application
python app.py

REM Deactivate the environment after the app is closed
deactivate
