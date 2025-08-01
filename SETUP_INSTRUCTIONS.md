# Setup Instructions for Slideshow Maker

## Quick Setup (Windows)

1. **Double-click `setup.bat`** - This will automatically:
   - Check if Python is installed
   - Install required packages
   - Create sample media files
   - Set everything up for you

## Manual Setup

If the automatic setup doesn't work, follow these steps:

### 1. Install Python (if not already installed)
- Download from: https://python.org/downloads/
- During installation, make sure to check "Add Python to PATH"
- Restart your command prompt after installation

### 2. Install Required Packages
Open Command Prompt or PowerShell and run:

```bash
# Try these commands in order until one works:
py -m pip install moviepy Pillow imageio imageio-ffmpeg
# OR
python -m pip install moviepy Pillow imageio imageio-ffmpeg
# OR
python3 -m pip install moviepy Pillow imageio imageio-ffmpeg
```

### 3. Create Sample Content (Optional)
```bash
py create_sample_media.py
```

### 4. Test the Slideshow Maker
```bash
py slideshow_maker.py
```

## Troubleshooting

### "Python not found"
- Install Python from https://python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart your terminal/command prompt

### "No module named pip"
```bash
py -m ensurepip --default-pip
py -m pip install --upgrade pip
```

### "No module named moviepy"
```bash
py -m pip install moviepy Pillow
```

### FFmpeg Issues
MoviePy requires FFmpeg. If you get FFmpeg errors:
```bash
py -m pip install imageio-ffmpeg
```

## Alternative: Using Conda/Anaconda
If you have Conda installed:
```bash
conda install -c conda-forge moviepy pillow
```

## Verification
To verify everything is working:
1. Run `py slideshow_maker.py --help`
2. You should see the help message with all available options

## Getting Started
1. Add your images/videos to the `media/` folder
2. Run: `py slideshow_maker.py`
3. Your slideshow will be saved as `slideshow_output.mp4`

For more options, see the main README.md file.