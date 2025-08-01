# 🎬 Guatemala Slideshow Maker
Write-Host "🎬 Guatemala Slideshow Maker" -ForegroundColor Cyan
Write-Host "============================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📁 Creating presentation-ready slideshow..." -ForegroundColor Green
Write-Host ""

# Try to run with the working virtual environment path
try {
    Write-Host "🔄 Attempting to run with virtual environment..." -ForegroundColor Yellow
    & "C:\Users\aiden\IdeaProjects\Slidshow\venv\Scripts\python.exe" slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_presentation.mp4" --duration 4 --fast --max-files 25 --resolution 1920x1080
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Slideshow created successfully!" -ForegroundColor Green
        Write-Host "📹 File: guatemala_presentation.mp4" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "🎉 Your presentation is ready!" -ForegroundColor Green
    } else {
        throw "Virtual environment failed"
    }
} catch {
    Write-Host ""
    Write-Host "⚠️  Virtual environment failed, trying system Python..." -ForegroundColor Yellow
    Write-Host ""
    
    try {
        python slideshow_maker.py --media-folder "E:\Photos\Gutamala" --output "guatemala_presentation.mp4" --duration 4 --fast --max-files 25 --resolution 1920x1080
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host ""
            Write-Host "✅ Slideshow created successfully!" -ForegroundColor Green
            Write-Host "📹 File: guatemala_presentation.mp4" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "🎉 Your presentation is ready!" -ForegroundColor Green
        } else {
            throw "System Python failed"
        }
    } catch {
        Write-Host ""
        Write-Host "❌ Failed to run slideshow maker" -ForegroundColor Red
        Write-Host ""
        Write-Host "💡 Try these solutions:" -ForegroundColor Yellow
        Write-Host "1. Install Python from python.org" -ForegroundColor White
        Write-Host "2. Run: pip install moviepy Pillow imageio imageio-ffmpeg" -ForegroundColor White
        Write-Host "3. Then run this script again" -ForegroundColor White
        Write-Host ""
    }
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 