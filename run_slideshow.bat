@echo off
echo 🎬 Guatemala Slideshow Maker
echo ============================
echo.

echo 📁 Creating presentation-ready slideshow...
echo.

REM Try to run with the working virtual environment path
"C:\Users\aiden\IdeaProjects\Slidshow\venv\Scripts\python.exe" slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Virtual environment failed, trying system Python...
    echo.
    python slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_100_photos.mp4" --duration 3 --fast --max-files 100 --resolution 1920x1080
)

if %errorlevel% neq 0 (
    echo.
    echo ❌ Failed to run slideshow maker
    echo.
    echo 💡 Try these solutions:
    echo 1. Install Python from python.org
    echo 2. Run: pip install moviepy Pillow imageio imageio-ffmpeg
    echo 3. Then run this script again
    echo.
    pause
) else (
    echo.
    echo ✅ Slideshow created successfully!
    echo 📹 File: guatemala_100_photos.mp4
    echo.
    echo 🎉 Your presentation is ready!
    echo.
    pause
) 