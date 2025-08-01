import os
import sys
import random
from moviepy import VideoFileClip, ImageClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips
from PIL import Image
import argparse

class SlideshowMaker:
    def __init__(self, media_folder="media", output_file="slideshow_output.mp4", 
                 music_file=None, image_duration=3, resolution=(1280, 720), randomize=True, 
                 max_files=50, fast_mode=False):
        self.media_folder = media_folder
        self.output_file = output_file
        self.music_file = music_file
        self.image_duration = image_duration
        self.resolution = resolution
        self.randomize = randomize
        self.max_files = max_files
        self.fast_mode = fast_mode
        self.supported_image_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        self.supported_video_formats = ('.mp4', '.mov', '.avi', '.mkv', '.wmv')
        
    def load_media_files(self):
        """Load and sort media files from the specified folder"""
        if not os.path.exists(self.media_folder):
            print(f"Error: Media folder '{self.media_folder}' not found!")
            return []
            
        media_files = []
        print(f"Scanning folder: {self.media_folder}")
        
        # Get all files and filter by supported formats
        all_files = []
        for filename in os.listdir(self.media_folder):
            filepath = os.path.join(self.media_folder, filename)
            
            if not os.path.isfile(filepath):
                continue
                
            file_ext = filename.lower()
            
            if any(file_ext.endswith(ext) for ext in self.supported_image_formats):
                all_files.append(('image', filename, filepath))
            elif any(file_ext.endswith(ext) for ext in self.supported_video_formats):
                all_files.append(('video', filename, filepath))
        
        # Sort files alphabetically first, then randomize if requested
        all_files.sort(key=lambda x: x[1])  # Sort by filename
        
        if self.randomize:
            print("Randomizing media file order...")
            random.shuffle(all_files)
        else:
            print("Using alphabetical order for media files...")
        
        # Limit total number of files for faster processing
        max_files = self.max_files
        if len(all_files) > max_files:
            print(f"Limiting to {max_files} files for faster processing (found {len(all_files)})")
            all_files = all_files[:max_files]
        
        # Process files in the determined order
        for i, (media_type, filename, filepath) in enumerate(all_files, 1):
            try:
                print(f"Processing {media_type} {i}/{len(all_files)}: {filename}")
                if media_type == 'image':
                    clip = self.create_image_clip(filepath)
                    media_files.append(clip)
                else:  # video
                    clip = self.create_video_clip(filepath)
                    media_files.append(clip)
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue
                
        print(f"Successfully loaded {len(media_files)} media files")
        return media_files
    
    def create_image_clip(self, image_path):
        """Create a video clip from an image with proper sizing"""
        # Create clip with specified duration
        clip = ImageClip(image_path, duration=self.image_duration)
        
        # For now, skip resizing to avoid file locking issues
        # The optimization will come from limiting file count and using fast encoding
        return clip
    
    def create_video_clip(self, video_path):
        """Create a video clip with proper sizing"""
        clip = VideoFileClip(video_path)
        
        # Limit video duration to prevent very long clips from dominating
        max_duration = 5 if self.fast_mode else 10  # Shorter for fast mode
        if clip.duration > max_duration:
            print(f"  Trimming video from {clip.duration:.1f}s to {max_duration}s")
            clip = clip.subclip(0, max_duration)
        
        return clip
    
    def add_transitions(self, clips):
        """Add fade transitions between clips"""
        if len(clips) <= 1:
            return clips
            
        # For now, return clips without transitions since fade methods aren't available
        print("Note: Transitions disabled (not available in this MoviePy version)")
        return clips
    
    def create_slideshow(self, with_transitions=True):
        """Create the complete slideshow with optional music"""
        media_clips = self.load_media_files()
        
        if not media_clips:
            print("No valid media files found. Please check your media folder.")
            return None
            
        # Add transitions if requested
        if with_transitions:
            print("Adding transitions...")
            media_clips = self.add_transitions(media_clips)
        
        print("Concatenating clips...")
        slideshow = concatenate_videoclips(media_clips, method="compose")
        
        # Add background music if provided
        if self.music_file and os.path.exists(self.music_file):
            print(f"Adding background music: {self.music_file}")
            try:
                audio = AudioFileClip(self.music_file)
                
                # Loop audio if it's shorter than video, or trim if longer
                if audio.duration < slideshow.duration:
                    # Loop the audio to match video duration
                    loops_needed = int(slideshow.duration / audio.duration) + 1
                    audio = concatenate_audioclips([audio] * loops_needed)
                
                # Trim audio to match video duration
                audio = audio.subclip(0, slideshow.duration)
                slideshow = slideshow.set_audio(audio)
                
            except Exception as e:
                print(f"Error adding audio: {e}")
                print("Continuing without background music...")
        
        return slideshow
    
    def generate(self, with_transitions=True, fps=24):
        """Generate the final slideshow video"""
        print("Creating slideshow...")
        slideshow = self.create_slideshow(with_transitions)
        
        if slideshow is None:
            return False
            
        print(f"Rendering video to: {self.output_file}")
        try:
            # Optimize encoding settings based on mode
            if self.fast_mode:
                preset = 'ultrafast'
                bitrate = '1500k'
                fps = min(fps, 15)  # Lower FPS for fast mode
            else:
                preset = 'fast'
                bitrate = '2000k'
            
            slideshow.write_videofile(
                self.output_file, 
                fps=fps,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                threads=4,  # Use multiple CPU threads
                preset=preset,  # Fast encoding preset
                bitrate=bitrate  # Optimized bitrate
            )
            print(f"Slideshow successfully created: {self.output_file}")
            return True
            
        except Exception as e:
            print(f"Error creating video: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Create a slideshow from images and videos')
    parser.add_argument('--media-folder', default='media', help='Folder containing media files')
    parser.add_argument('--output', default='slideshow_output.mp4', help='Output video file')
    parser.add_argument('--music', help='Background music file')
    parser.add_argument('--duration', type=float, default=3.0, help='Duration for each image (seconds)')
    parser.add_argument('--resolution', default='1280x720', help='Output resolution (e.g., 1280x720)')
    parser.add_argument('--no-transitions', action='store_true', help='Disable fade transitions')
    parser.add_argument('--fps', type=int, default=24, help='Frames per second')
    parser.add_argument('--no-randomize', action='store_true', help='Keep files in alphabetical order (disable randomization)')
    parser.add_argument('--fast', action='store_true', help='Fast mode: limit files and use lower quality for speed')
    parser.add_argument('--max-files', type=int, default=50, help='Maximum number of files to process (default: 50)')
    
    args = parser.parse_args()
    
    # Parse resolution
    try:
        width, height = map(int, args.resolution.split('x'))
        resolution = (width, height)
    except:
        print("Invalid resolution format. Using default 1280x720")
        resolution = (1280, 720)
    
    # Create slideshow maker
    slideshow_maker = SlideshowMaker(
        media_folder=args.media_folder,
        output_file=args.output,
        music_file=args.music,
        image_duration=args.duration,
        resolution=resolution,
        randomize=not args.no_randomize,
        max_files=args.max_files,
        fast_mode=args.fast
    )
    
    # Generate slideshow
    success = slideshow_maker.generate(
        with_transitions=not args.no_transitions,
        fps=args.fps
    )
    
    if success:
        print("\n✅ Slideshow creation completed successfully!")
    else:
        print("\n❌ Slideshow creation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()