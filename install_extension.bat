@echo off
setlocal enabledelayedexpansion

echo Detecting installed browsers...

:: Check for Chrome
set "CHROME_PATH="
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe"
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) else if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" (
    set "CHROME_PATH=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
)

:: Check for Edge
set "EDGE_PATH="
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    set "EDGE_PATH=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
)

:: Check for Brave - Added more possible paths
set "BRAVE_PATH="
if exist "%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe" (
    set "BRAVE_PATH=%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"
) else if exist "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" (
    set "BRAVE_PATH=C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
) else if exist "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe" (
    set "BRAVE_PATH=C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
)

:: Check for Firefox
set "FIREFOX_PATH="
if exist "C:\Program Files\Mozilla Firefox\firefox.exe" (
    set "FIREFOX_PATH=C:\Program Files\Mozilla Firefox\firefox.exe"
) else if exist "C:\Program Files (x86)\Mozilla Firefox\firefox.exe" (
    set "FIREFOX_PATH=C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
)

:: Show menu
echo.
echo Available browsers:
if not "!CHROME_PATH!"=="" echo 1. Google Chrome
if not "!EDGE_PATH!"=="" echo 2. Microsoft Edge
if not "!BRAVE_PATH!"=="" echo 3. Brave Browser
if not "!FIREFOX_PATH!"=="" echo 4. Mozilla Firefox
echo.

:: Get user choice
set /p CHOICE=Enter the number of the browser to install the extension (1-4): 

:: Get the extension directory
set "EXT_DIR=%~dp0browser_extension"
echo Extension directory: %EXT_DIR%

:: Process user choice
if "%CHOICE%"=="1" (
    if not "!CHROME_PATH!"=="" (
        echo Installing extension in Chrome...
        echo Chrome path: !CHROME_PATH!
        
        :: Close Chrome if it's running
        taskkill /F /IM chrome.exe /T 2>nul
        
        :: Create directories
        echo Creating directories...
        if not exist "C:\Temp" mkdir "C:\Temp"
        if exist "C:\Temp\TempMailExt" rmdir /S /Q "C:\Temp\TempMailExt"
        mkdir "C:\Temp\TempMailExt"
        
        if exist "C:\Temp\ChromeProfile" rmdir /S /Q "C:\Temp\ChromeProfile"
        mkdir "C:\Temp\ChromeProfile"
        
        :: Copy extension files
        echo Copying extension files from "%EXT_DIR%" to "C:\Temp\TempMailExt\"
        xcopy /E /I /Y "%EXT_DIR%\*" "C:\Temp\TempMailExt\"
        
        :: Create batch file
        echo Creating batch file shortcut...
        (
            echo @echo off
            echo start "" "!CHROME_PATH!" --load-extension="C:\Temp\TempMailExt" --user-data-dir="C:\Temp\ChromeProfile"
        ) > "C:\Temp\TempMailChrome.bat"
        
        :: Copy to desktop
        echo Copying shortcut to desktop...
        copy "C:\Temp\TempMailChrome.bat" "%USERPROFILE%\Desktop\TempMailChrome.bat"
        
        :: Start Chrome
        echo Starting Chrome with the extension...
        start "" "!CHROME_PATH!" --load-extension="C:\Temp\TempMailExt" --user-data-dir="C:\Temp\ChromeProfile" --no-first-run
        
        echo.
        echo Extension has been installed in Chrome!
        echo.
        echo A batch file shortcut has been created on your desktop: "TempMailChrome.bat"
        echo Double-click this file to open Chrome with the extension loaded.
        echo.
        echo The extension files are located at: C:\Temp\TempMailExt
        echo The Chrome profile is located at: C:\Temp\ChromeProfile
        echo.
        echo IMPORTANT: If you see a warning about "Developer Mode Extensions", 
        echo click "Keep it" or "Keep extensions" to continue using the extension.
    ) else (
        echo Chrome is not installed.
    )
) else if "%CHOICE%"=="2" (
    if not "!EDGE_PATH!"=="" (
        echo Installing extension in Edge...
        
        :: Close Edge if it's running
        taskkill /F /IM msedge.exe /T 2>nul
        
        :: Create directories
        if not exist "C:\Temp" mkdir "C:\Temp"
        if exist "C:\Temp\TempMailExt" rmdir /S /Q "C:\Temp\TempMailExt"
        mkdir "C:\Temp\TempMailExt"
        
        :: Copy extension files
        echo Copying extension files...
        xcopy /E /I /Y "%EXT_DIR%\*" "C:\Temp\TempMailExt\"
        
        :: Start Edge
        echo Starting Edge with the extension...
        start "" "!EDGE_PATH!" --load-extension="C:\Temp\TempMailExt" --no-first-run
        
        echo.
        echo Extension has been installed in Edge!
        echo.
        echo The extension files are located at: C:\Temp\TempMailExt
    ) else (
        echo Edge is not installed.
    )
) else if "%CHOICE%"=="3" (
    if not "!BRAVE_PATH!"=="" (
        echo Installing extension in Brave...
        echo Brave path: !BRAVE_PATH!
        
        :: Close Brave if it's running
        taskkill /F /IM brave.exe /T 2>nul
        
        :: Create directories
        if not exist "C:\Temp" mkdir "C:\Temp"
        if exist "C:\Temp\TempMailExt" rmdir /S /Q "C:\Temp\TempMailExt"
        mkdir "C:\Temp\TempMailExt"
        
        :: Copy extension files
        echo Copying extension files...
        xcopy /E /I /Y "%EXT_DIR%\*" "C:\Temp\TempMailExt\"
        
        :: Create batch file
        echo Creating batch file shortcut...
        (
            echo @echo off
            echo start "" "!BRAVE_PATH!" --load-extension="C:\Temp\TempMailExt"
        ) > "C:\Temp\TempMailBrave.bat"
        
        :: Copy to desktop
        echo Copying shortcut to desktop...
        copy "C:\Temp\TempMailBrave.bat" "%USERPROFILE%\Desktop\TempMailBrave.bat"
        
        :: Start Brave
        echo Starting Brave with the extension...
        start "" "!BRAVE_PATH!" --load-extension="C:\Temp\TempMailExt" --no-first-run
        
        echo.
        echo Extension has been installed in Brave!
        echo.
        echo A batch file shortcut has been created on your desktop: "TempMailBrave.bat"
        echo Double-click this file to open Brave with the extension loaded.
        echo.
        echo The extension files are located at: C:\Temp\TempMailExt
    ) else (
        echo Brave is not installed.
        echo Checking for Brave in common locations...
        dir "%LOCALAPPDATA%\BraveSoftware\" /s /b | findstr "brave.exe"
        dir "C:\Program Files\BraveSoftware\" /s /b | findstr "brave.exe"
        dir "C:\Program Files (x86)\BraveSoftware\" /s /b | findstr "brave.exe"
        echo.
        echo If Brave is installed but not detected, please manually install the extension:
        echo 1. Open Brave
        echo 2. Go to brave://extensions/
        echo 3. Enable Developer Mode
        echo 4. Click "Load unpacked"
        echo 5. Navigate to %EXT_DIR% and select it
    )
) else if "%CHOICE%"=="4" (
    if not "!FIREFOX_PATH!"=="" (
        echo Installing extension in Firefox...
        
        :: Create Firefox profile
        if not exist "%APPDATA%\Mozilla\Firefox\Profiles" mkdir "%APPDATA%\Mozilla\Firefox\Profiles"
        set "PROFILE_DIR=%APPDATA%\Mozilla\Firefox\Profiles\temp-mail-profile"
        if not exist "%PROFILE_DIR%" mkdir "%PROFILE_DIR%"
        
        :: Copy extension files
        echo Copying extension files...
        if not exist "%PROFILE_DIR%\extensions\temp-mail" mkdir "%PROFILE_DIR%\extensions\temp-mail"
        xcopy /E /I /Y "%EXT_DIR%\*" "%PROFILE_DIR%\extensions\temp-mail\"
        
        :: Start Firefox
        echo Starting Firefox with the extension...
        start "" "!FIREFOX_PATH!" -P "temp-mail-profile" --new-instance
        
        echo.
        echo Extension has been installed in Firefox!
        echo.
        echo The extension files are located at: %PROFILE_DIR%\extensions\temp-mail
    ) else (
        echo Firefox is not installed.
    )
) else (
    echo Invalid choice.
)

echo.
echo Press any key to exit...
pause > nul 