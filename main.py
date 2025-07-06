import tkinter as tk
import torch
from pathlib import Path
from src.utils import get_device
from src.imageupscale import ImageUpscale
from src.videoupscale import VideoUpscale
from tkinter.filedialog import askopenfilename

def main():
    print("Mediabatch - Video & image batch-processor")
    device = get_device()
    if device.type == 'cuda':
        print(f"Using GPU: {torch.cuda.get_device_name()}\n")
    else:
        print("Using CPU\n")
        
    image_process()
    

def image_process():
    print("1. Image Upscaling")
    print("2. Video Upscaling")
    
    option = input("Select your option: ")
    
    if option == "1":
        print("1. Single Image Upscale")
        print("2. Batch Image Upscale")
        option2 = input("Select your option: ")
        if option2 == "1":
            print("Select Pytorch Model")
            model_path = Path(get_model())

            if model_path:
                upscaler = ImageUpscale(model_path)
                print("Model loaded Successfully\n")
                print("Select an Image:")
                image_path = Path(get_image())
                if image_path:
                    print("Image loaded Successfully\n")
                else:
                    raise FileNotFoundError("No Image file selected")
                upscaler.process_image(image_path)
            else:
                raise FileNotFoundError("No model file selected")
        else:
            print("Select Pytorch Model")
            model_path = Path(get_model())

            if model_path:
                upscaler = ImageUpscale(model_path)
                print("Model loaded Successfully\n")
                print("Processing images from input/ directory")
                upscaler.process_batch_image(Path("input/"))
            else:
                raise FileNotFoundError("No model file selected")
            
    if option == "2":
        print("1. Single Video Upscaling")
        print("2. Batch Video Upscaling")
        option3 = input("Select your option")
        if option3 == "1":
            print("Select Pytorch Model")
            model_path = Path(get_model())
            
            if model_path:
                upscaler = VideoUpscale(model_path)
                print("Model loaded successfully")
                print("Select a Video")
                video_path = Path(get_video())
                if video_path:
                    print("Video loaded successfully")
                else:
                    raise FileNotFoundError("No video file selected")
                upscaler.process_video(video_path)
            else:
                raise FileNotFoundError("No model file selected")

        
            

def get_model():
    root = tk.Tk()
    root.withdraw()
    
    model = askopenfilename(title="Select Pytorch Model")
    
    root.destroy()
    return model

def get_image():
    root = tk.Tk()
    root.withdraw()
    
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
    
    video = askopenfilename(
        title="Select Video File",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*")]
    )
    
    root.destroy()
    return video
    
if __name__ == "__main__":
    main()