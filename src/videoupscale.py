from src.imageupscale import ImageUpscale
from pathlib import Path
from src.utils import get_video_fps, load_videos
import subprocess
import tempfile

class VideoUpscale(ImageUpscale):
    def process_video(self, video_path: Path):
        fps = get_video_fps(video_path)
        output_folder = Path("output/")
        output_folder.mkdir(exist_ok=True)
        
        with tempfile.TemporaryDirectory(dir=output_folder) as temp_dir:
            frames_dir = Path(temp_dir) / "frames"
            upscaled_dir = Path(temp_dir) / "upscaled"
            frames_dir.mkdir()
            upscaled_dir.mkdir()
            
            #extract frames using ffmpeg
            subprocess.run(["ffmpeg", "-i", str(video_path), "-qscale:v", "1", "-qmin", "1", "-qmax", "1", "-vsync", "0", 
                            str(frames_dir / "frame%08d.png")], check=True)
            
            #upscales each image in frames folder
            for frames in frames_dir.iterdir():
                self.process_image(frames, upscaled_dir)
            
            #combine frames 
            output_video = output_folder / f"upscaled_{video_path.name}"
            subprocess.run(["ffmpeg", "-y", "-framerate", fps, "-i", str(upscaled_dir / "frame%08d.png"), "-i", str(video_path),                          
                "-map", "0:v:0", "-map", "1:a:0?", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", fps, "-c:a", "copy",
                str(output_video)], check=True)
                
    def batch_process_video(self, input_dir: Path):
        video_files = load_videos(input_dir)
        
        if not video_files:
            print(f"No videos found in {input_dir}")
            
        for i, video_file in enumerate(video_files, 1):
            try:
                print(f"[{i}/{len(video_files)}] Processing: {video_file.name}")
                
                self.process_video(video_file)
                print(f"Complete: {video_file.name}")
            except Exception as e:
                  print(f"Error processing {video_file.name}: {e}") 
                  continue         
        
        
        
        