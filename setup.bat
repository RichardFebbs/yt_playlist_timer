@echo off
setlocal

set "VENV_PATH=yt_timer_venv"
set "VENV_PIP=%VENV_PATH%\Scripts\pip.exe"
set "VENV_ACTIVATE=%VENV_PATH%\Scripts\activate.bat"

:: Check if the virtual environment exists
if not exist "%VENV_PATH%" (
    python -m venv "%VENV_PATH%"
    if errorlevel 1 (
        echo Failed to create a virtual environment.
        exit /b 1
    )
)

:: Check if the activation script exists
if not exist "%VENV_ACTIVATE%" (
    echo Virtual environment activation script not found.
    exit /b 1
)

:: Check for and install requirements if needed
if exist requirements.txt (
    :: Get currently installed packages into a temp file
    "%VENV_PIP%" freeze > current_packages.txt

    :: Compare with requirements.txt using FC (file compare)
    fc current_packages.txt requirements.txt >nul
    if errorlevel 1 (
        echo Installing required packages...
        "%VENV_PIP%" install -r requirements.txt
        if errorlevel 1 (
            echo Failed to install requirements.
            del current_packages.txt
            exit /b 1
        )
    ) else (
        echo Setup complete
    )
    del current_packages.txt
) else (
    echo requirements.txt not found.
    echo Skipping installation.
)

echo.
echo ✓ Setup complete!
echo 💡 To activate the virtual environment, run:
echo     call "%VENV_ACTIVATE%"

endlocal

