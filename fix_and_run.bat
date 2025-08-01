@echo off
echo 🔧 Fixing Python Environment & Creating 100-Photo Slideshow
echo =========================================================
echo.

echo 🗑️ Step 1: Cleaning up corrupted virtual environment...
if exist "C:\Users\aiden\IdeaProjects\Slidshow\venv" (
    echo Removing corrupted virtual environment...
    rmdir /s /q "C:\Users\aiden\IdeaProjects\Slidshow\venv"
    echo ✅ Old environment removed
) else (
    echo ℹ️ No existing virtual environment found
)
echo.

echo 🐍 Step 2: Installing Python packages globally...
echo Installing required packages for slideshow maker...
pip install --upgrade pip
pip install moviepy
pip install Pillow
pip install imageio
pip install imageio-ffmpeg

if %errorlevel% neq 0 (
    echo.
    echo ❌ Global pip installation failed
    echo.
    echo 💡 Please try:
    echo 1. Install Python from python.org (make sure to check "Add to PATH")
    echo 2. Restart your computer
    echo 3. Run this script again
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ All packages installed successfully!
echo.

echo 🎬 Step 3: Creating your 100-photo Guatemala slideshow...
echo.

python slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080

if %errorlevel% neq 0 (
    echo.
    echo ⚠️ Main folder failed, trying local media folder...
    python slideshow_maker.py --media-folder "media" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080
)

if %errorlevel% neq 0 (
    echo.
    echo ❌ Slideshow creation failed
    echo.
    echo 🔍 Troubleshooting:
    echo 1. Check if Python is installed: python --version
    echo 2. Check if packages are installed: pip list
    echo 3. Manually run: python slideshow_maker.py --help
    echo.
    pause
) else (
    echo.
    echo 🎉 SUCCESS! Your 100-photo Guatemala slideshow is ready!
    echo.
    echo 📹 File: guatemala_100_photos.mp4
    echo ⏱️ Duration: ~5 minutes (100 photos × 3 seconds)
    echo 📊 Quality: HD (1920×1080)
    echo 💾 Estimated size: 200-400 MB
    echo.
    echo 🎵 Next steps:
    echo - Add background music if desired
    echo - Share with family and friends
    echo - Upload to YouTube or social media
    echo.
    echo ✨ Enjoy your Guatemala memories!
    pause
)