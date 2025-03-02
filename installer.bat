@echo off
:: Check for Python installation
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.7 or higher and run this script again.
    pause
    exit /b 1
)

:: Create a virtual environment
echo Creating a virtual environment...
python -m venv venv

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
