@echo off
setlocal enabledelayedexpansion

:: Check for Python installation
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.7 or higher and run this script again.
    pause
    exit /b 1
)

:: Download and update from GitHub
echo Checking for updates from GitHub...
echo Downloading latest version...
curl -L -o update.zip https://github.com/Ally-Released/temp-mail-cli/archive/refs/heads/main.zip
if exist update.zip (
    echo Extracting files...
    tar -xf update.zip
    xcopy /E /Y /I "temp-mail-cli-main" "." > nul
    rmdir /S /Q "temp-mail-cli-main"
    del /F /Q update.zip
    echo Update completed successfully.
) else (
    echo Failed to download updates. Using existing files.
)

:: Create a virtual environment
if not exist venv (
    echo Creating a virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating the virtual environment...
CALL venv\Scripts\activate

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install required packages
echo Installing required packages from requirements.txt...
pip install -r requirements.txt

:: Run the application
echo Running Temp Mail CLI...
python temp_mail.py

:: Keep the window open
echo Press any key to exit...
pause
