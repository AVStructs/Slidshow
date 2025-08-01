@echo off
echo 🎬 Guatemala 100-Photo Slideshow Creator
echo ========================================
echo.

echo 📸 Creating slideshow with 100 Guatemala photos...
echo ⏱️  Duration: 3 seconds per photo = ~5 minutes total
echo 🎥 Quality: HD (1920x1080)
echo.

REM First try with virtual environment
echo 🔄 Attempting with virtual environment...
"C:\Users\aiden\IdeaProjects\Slidshow\venv\Scripts\python.exe" slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Virtual environment failed, trying system Python...
    echo.
    python slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080
)

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Main folder failed, trying local media folder...
    echo.
    python slideshow_maker.py --media-folder "media" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080
)

if %errorlevel% neq 0 (
    echo.
    echo ❌ Failed to run slideshow maker
    echo.
    echo 💡 Quick Setup:
    echo 1. Download Python from python.org
    echo 2. Open Command Prompt as Administrator
    echo 3. Run: pip install moviepy Pillow imageio imageio-ffmpeg
    echo 4. Then double-click this script again
    echo.
    echo 📝 Alternative: Use the manual command below:
    echo python slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080
    echo.
    pause
) else (
    echo.
    echo ✅ 100-Photo Slideshow Created Successfully!
    echo 📹 File: guatemala_100_photos.mp4
    echo ⏱️  Duration: ~5 minutes (100 photos × 3 seconds)
    echo 📊 Quality: HD (1920×1080)
    echo 💾 Size: ~200-400 MB
    echo.
    echo 🎉 Your 100-photo Guatemala presentation is ready!
    echo.
    echo 💡 Pro Tips:
    echo - Add background music in video editor
    echo - Perfect for family gatherings
    echo - Share on social media or TV
    echo.
    pause
)