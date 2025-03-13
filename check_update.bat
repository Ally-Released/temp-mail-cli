@echo off
setlocal enabledelayedexpansion

echo Checking for updates and dependencies...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.8 or later.
    echo You can download it from: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip.
    pause
    exit /b 1
)

:: Check if virtualenv is installed
pip show virtualenv >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing virtualenv...
    pip install virtualenv
)

:: Create and activate virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Install required packages
echo Installing required packages...
pip install -r requirements.txt

:: Check for updates
echo Checking for updates...
python -c "import requests; response = requests.get('https://api.github.com/repos/yourusername/temp-mail/releases/latest'); print(response.json()['tag_name'])" > latest_version.txt
set /p LATEST_VERSION=<latest_version.txt

:: Read current version from manifest.json
for /f "tokens=* delims=" %%a in (browser_extension\manifest.json) do (
    set "line=%%a"
    if "!line:~0,20!"=="  \"version\": \"" (
        set "CURRENT_VERSION=!line:~20,10!"
        set "CURRENT_VERSION=!CURRENT_VERSION:,=!"
    )
)

:: Compare versions
if "%LATEST_VERSION%" neq "%CURRENT_VERSION%" (
    echo New version available: %LATEST_VERSION%
    echo Current version: %CURRENT_VERSION%
    echo Opening download page...
    start https://github.com/yourusername/temp-mail/releases/latest
) else (
    echo You are using the latest version (%CURRENT_VERSION%)
)

:: Deactivate virtual environment
deactivate

echo.
echo Setup complete! You can now run install_extension.bat to install the extension in your browser.
pause 