# Slideshow Maker

A Python script that creates PowerPoint-style slideshow videos from images and videos with optional background music.

## Features

- ✅ Combines images and videos from a folder
- ✅ Creates smooth transitions between slides
- ✅ Adds background music (with looping/trimming)
- ✅ Maintains aspect ratios and centers content
- ✅ Supports multiple image and video formats
- ✅ Customizable image duration and output resolution
- ✅ Randomizes file order for variety (can be disabled)
- ✅ Command-line interface with options

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

1. **Add your media files** to the `media/` folder:
   - Images: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`
   - Videos: `.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`

2. **Run the basic slideshow creation**:
```bash
python slideshow_maker.py
```

3. **Add background music** (optional):
```bash
python slideshow_maker.py --music background.mp3
```

## Advanced Usage

### Custom Options

```bash
# Full customization example
python slideshow_maker.py \
    --media-folder "my_photos" \
    --output "my_slideshow.mp4" \
    --music "background.mp3" \
    --duration 4.5 \
    --resolution "1920x1080" \
    --fps 30
```

### Available Options

| Option | Default | Description |
|--------|---------|-------------|
| `--media-folder` | `media` | Folder containing your images/videos |
| `--output` | `slideshow_output.mp4` | Output video filename |
| `--music` | None | Background music file |
| `--duration` | `3.0` | Seconds to show each image |
| `--resolution` | `1280x720` | Output video resolution |
| `--no-transitions` | False | Disable fade transitions |
| `--no-randomize` | False | Keep files in alphabetical order |
| `--fps` | `24` | Video frames per second |

### Folder Structure Example

```
Slidshow/
├── slideshow_maker.py
├── requirements.txt
├── media/                    # Your content goes here
│   ├── 01_intro.jpg         # Files are processed alphabetically
│   ├── 02_family.mp4
│   ├── 03_vacation.jpg
│   └── 04_finale.png
├── background.mp3           # Optional music
└── slideshow_output.mp4     # Generated slideshow
```

## Supported Formats

### Images
- JPEG (`.jpg`, `.jpeg`)
- PNG (`.png`)
- BMP (`.bmp`)
- GIF (`.gif`)

### Videos
- MP4 (`.mp4`)
- MOV (`.mov`)
- AVI (`.avi`)
- MKV (`.mkv`)
- WMV (`.wmv`)

### Audio
- MP3 (`.mp3`)
- WAV (`.wav`)
- AAC (`.aac`)
- M4A (`.m4a`)

## Tips for Best Results

1. **File Naming**: Name files with numbers/letters to control order (e.g., `01_first.jpg`, `02_second.mp4`)

2. **Image Quality**: Use high-resolution images for better output quality

3. **Video Length**: Keep individual video clips reasonable in length

4. **Music**: Choose music that matches your slideshow duration, or the script will loop/trim automatically

5. **Resolution**: Use `1920x1080` for full HD or `1280x720` for faster processing

## Examples

### Basic slideshow:
```bash
python slideshow_maker.py
```

### Wedding slideshow with music:
```bash
python slideshow_maker.py --music "wedding_song.mp3" --duration 4 --resolution "1920x1080"
```

### Quick photo montage:
```bash
python slideshow_maker.py --duration 1.5 --no-transitions --fps 30
```

### Randomized slideshow (default):
```bash
python slideshow_maker.py
```

### Ordered slideshow (alphabetical):
```bash
python slideshow_maker.py --no-randomize
```

## Troubleshooting

- **"No valid media files found"**: Check that your media folder exists and contains supported file formats
- **Audio issues**: Ensure your music file is in a supported format (MP3 recommended)
- **Memory errors**: Try reducing resolution or processing fewer files at once
- **Slow rendering**: Lower the FPS or resolution for faster processing