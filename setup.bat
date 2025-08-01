@echo off
echo Setting up Slideshow Maker...
echo.

REM Check if Python is available
py --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not available via 'py' command
    echo Please install Python from https://python.org/downloads/
    pause
    exit /b 1
)

echo Python found: 
py --version

REM Try to install pip if not available
echo.
echo Installing/upgrading pip...
py -m ensurepip --default-pip
py -m pip install --upgrade pip

REM Install requirements
echo.
echo Installing required packages...
py -m pip install moviepy Pillow imageio imageio-ffmpeg

REM Create sample media files
echo.
echo Creating sample media files...
py create_sample_media.py

echo.
echo ✅ Setup complete! You can now run:
echo    py slideshow_maker.py
echo.
echo Or with custom options:
echo    py slideshow_maker.py --music background.mp3 --duration 4
echo.
pause