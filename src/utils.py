from pathlib import Path
from PIL import Image
import subprocess
import torch
import tkinter as tk
from tkinter.filedialog import askopenfilename

def get_device():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def convert_to_rgb(image_path: Path):
    image = Image.open(image_path)
    
    if image.mode == "RGBA":
        image = image.convert('RGB')
    return image

def save_image(image: Image.Image, image_path: Path, output_dir: Path = Path("output/")):
    output_dir.mkdir(exist_ok=True)
    
    filename = image_path.name
    final_path = output_dir / filename
    image.save(final_path)
    
def load_images(input_dir: Path = Path("input/")):
    input_dir.mkdir(exist_ok=True)
    
    image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif', '.webp', '.gif'}
    image_files = [f for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() in image_extensions]
    return image_files

def load_videos(input_dir: Path = Path("input/")):
    input_dir.mkdir(exist_ok=True)
    
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv'}
    video_files = [f for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() in video_extensions]
    return video_files


def get_video_fps(video_path: Path):
    def probe(field: str):
        cmd = [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", f"stream={field}",
            "-of", "default=nokey=1:noprint_wrappers=1",
            str(video_path),
        ]
        return subprocess.check_output(cmd, text=True).strip()

    fps = probe("avg_frame_rate")            
    if fps in ("0/0", "", "N/A"):            # malformed or raw stream
        fps = probe("r_frame_rate")          # last resort
    return fps                               

def get_model():
    root = tk.Tk()
    root.withdraw()
    
    model = askopenfilename(title="Select Pytorch Model")
    
    root.destroy()
    return model

def get_image():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    image = askopenfilename(
        title="Select Image File",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp *.gif"),
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("BMP files", "*.bmp"),
            ("TIFF files", "*.tiff *.tif"),
            ("WebP files", "*.webp"),
            ("GIF files", "*.gif"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()
    return image

def get_video():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    video = askopenfilename(
        title="Select Video File",
        filetypes=[
            ("Video files", "*.mp4 *.avi *.mov *.mkv *.webm *.flv *.wmv"),
            ("MP4 files", "*.mp4"),
            ("AVI files", "*.avi"),
            ("MOV files", "*.mov"),
            ("MKV files", "*.mkv"),
            ("WebM files", "*.webm"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()
    return video