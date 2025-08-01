#!/usr/bin/env python3
"""
Creates sample media files for testing the slideshow maker
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_images():
    """Create sample images for testing"""
    media_dir = "media"
    os.makedirs(media_dir, exist_ok=True)
    
    # Sample colors and texts
    samples = [
        ((255, 100, 100), "Welcome to", "Your Slideshow"),
        ((100, 255, 100), "Sample Slide", "Number Two"),
        ((100, 100, 255), "Another", "Beautiful Slide"),
        ((255, 255, 100), "Almost Done", "Just One More"),
        ((255, 100, 255), "Thank You", "For Watching!")
    ]
    
    width, height = 1280, 720
    
    for i, (color, title, subtitle) in enumerate(samples, 1):
        # Create image
        img = Image.new('RGB', (width, height), color=color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a font, fallback to default if not available
        try:
            title_font = ImageFont.truetype("arial.ttf", 80)
            subtitle_font = ImageFont.truetype("arial.ttf", 50)
        except:
            try:
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
            except:
                title_font = None
                subtitle_font = None
        
        if title_font and subtitle_font:
            # Calculate text positions
            title_bbox = draw.textbbox((0, 0), title, font=title_font)
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            
            title_x = (width - (title_bbox[2] - title_bbox[0])) // 2
            title_y = height // 2 - 60
            
            subtitle_x = (width - (subtitle_bbox[2] - subtitle_bbox[0])) // 2
            subtitle_y = height // 2 + 20
            
            # Draw text with shadow effect
            shadow_offset = 3
            draw.text((title_x + shadow_offset, title_y + shadow_offset), title, 
                     fill=(0, 0, 0), font=title_font)
            draw.text((title_x, title_y), title, fill=(255, 255, 255), font=title_font)
            
            draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, 
                     fill=(0, 0, 0), font=subtitle_font)
            draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 255, 255), font=subtitle_font)
        
        # Save image
        filename = f"{i:02d}_sample_slide.png"
        filepath = os.path.join(media_dir, filename)
        img.save(filepath)
        print(f"Created: {filepath}")
    
    print(f"\n✅ Created {len(samples)} sample images in the '{media_dir}' folder")
    print("You can now run: python slideshow_maker.py")

if __name__ == "__main__":
    create_sample_images()