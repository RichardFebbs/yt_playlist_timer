@echo off

set "VENV_PATH=.\yt_timer_venv"

:: Create the specified virtual environment if it doesn't exist
if not exist "%VENV_PATH%\Scripts\activate.bat" (
    python3 -m venv %VENV_PATH%
)

:: Start the environment
if exist "%VENV_PATH\Scripts\activate.bat" (
    call "%VENV_PATH%\Scripts\activate.bat"
) else (
    echo Virtual environment activation script not found
)

:: Install requirements if it exists
if exist "requirements.txt" (
    pip install -r requirements.txt
) else (
    echo requirements.txt not found.
    echo skipping installation.
)
