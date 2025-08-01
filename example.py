#!/usr/bin/env python3
"""
Example usage of the SlideshowMaker class for programmatic use
"""

from slideshow_maker import SlideshowMaker

def create_family_slideshow():
    """Example: Create a family slideshow with custom settings"""
    slideshow = SlideshowMaker(
        media_folder="media",
        output_file="family_memories.mp4",
        music_file="family_song.mp3",
        image_duration=4.0,
        resolution=(1920, 1080),
        randomize=True  # Randomize order for variety
    )
    
    success = slideshow.generate(with_transitions=True, fps=30)
    if success:
        print("Family slideshow created successfully!")
    else:
        print("Failed to create slideshow")

def create_quick_montage():
    """Example: Create a quick photo montage without transitions"""
    slideshow = SlideshowMaker(
        media_folder="photos",
        output_file="quick_montage.mp4",
        image_duration=1.5,
        resolution=(1280, 720),
        randomize=True  # Randomize for variety
    )
    
    success = slideshow.generate(with_transitions=False, fps=24)
    if success:
        print("Quick montage created successfully!")

def create_business_presentation():
    """Example: Create a business presentation style slideshow"""
    slideshow = SlideshowMaker(
        media_folder="presentation_media",
        output_file="business_presentation.mp4",
        image_duration=6.0,  # Longer duration for reading
        resolution=(1920, 1080),
        randomize=False  # Keep order for business presentations
    )
    
    success = slideshow.generate(with_transitions=True, fps=24)
    if success:
        print("Business presentation created successfully!")

if __name__ == "__main__":
    # Choose which example to run
    print("Choose an example to run:")
    print("1. Family slideshow with music")
    print("2. Quick photo montage")
    print("3. Business presentation")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        create_family_slideshow()
    elif choice == "2":
        create_quick_montage()
    elif choice == "3":
        create_business_presentation()
    else:
        print("Invalid choice. Running family slideshow example...")
        create_family_slideshow()