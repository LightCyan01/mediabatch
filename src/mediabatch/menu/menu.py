import questionary
import torch
from questionary import Style
from rich.console import Console
from pathlib import Path
from mediabatch.utils.utils import  get_model, get_image, get_video, get_device
from mediabatch.core.imageupscale import ImageUpscale
from mediabatch.core.videoupscale import VideoUpscale


console = Console()

q_style = Style([
    ("qmark",       "bold fg:#FF9D00"),
    ("question",    "bold"),
    ("pointer",     "fg:#673AB7 bold"),
    ("highlighted", "fg:#673AB7"),       
    ("selected",    "fg:#2ECC71"),
    ("separator",   "fg:#6C6C6C"),
    ("instruction", "fg:#999999"),
    ("answer",      "fg:#2ECC71 bold"),
])


def main_menu():
    console.clear()
    
    print("Mediabatch - Image and Video Upscaling Tool")
    device = get_device()
    if device.type == 'cuda':
        print(f"Using GPU: {torch.cuda.get_device_name()}\n")
    else:
        print("Using CPU\n")
    return questionary.select(
        "▶ Main menu", choices=[
            "Image Upscale", "Video Upscale", "Settings", "Quit"],
        style=q_style
    ).ask()
    
def image_upscale_option():
    console.clear()
    return questionary.select(
        "Image Upscale", choices=["Single Image Upscale", "Batch Image Upscale", "Back"],
        style=q_style
    ).ask()
    
def video_upscale_option():
    console.clear()
    return questionary.select(
        "Video Upscale", choices=["Single Video Upscale", "Batch Video Upscale", "Back"],
        style=q_style
    ).ask()
    
def single_image_upscale():
    console.clear()
    print("Select Pytorch Model")
    model_path_str = get_model()
    if not model_path_str:
        print("No model file selected.")
        return
    model_path = Path(model_path_str)
    upscaler = ImageUpscale(model_path)
    print("Model loaded Successfully")
    
    image_path_str = get_image()
    if not image_path_str:
        print("No Image File Sleected")
        return
    
    image_path = Path(image_path_str)
    print("Image loaded Successfuly")
    upscaler.process_image(image_path)
    print("Image Upscale Complete!")
        
def batch_image_upscale():
    console.clear()
    print("Select Pytorch Model")
    model_path_str = get_model()
    if not model_path_str:
        print("No model file selected.")
        return
    model_path = Path(model_path_str)
    upscaler = ImageUpscale(model_path)
    print("Processing images from input/ directory")
    upscaler.process_batch_image(Path("input/"))
    print("Batch Image Upscale Complete!")

def single_video_upscale():
    console.clear()
    print("Select Pytorch Model")
    model_path_str = get_model()
    if not model_path_str:
        print("No model file selected.")
        return
    model_path = Path(model_path_str)
    upscaler = VideoUpscale(model_path)
    
    video_path_str = get_video()
    if not video_path_str:
        print("No Video File Selected")
        
    video_path = Path(video_path_str)
    print("Video Loaded Successfully")
    upscaler.process_video(video_path)
    print("Video Upscale Complete!")

def batch_video_upscale():
    console.clear()
    print("Select Pytorch Model")
    model_path_str = get_model()
    if not model_path_str:
        print("No model file selected.")
        return
    model_path = Path(model_path_str)
    upscaler = VideoUpscale(model_path)
    print("Processing videos from input/ directory")
    upscaler.batch_process_video(Path("input/"))
    print("Batch Video Upscale Complete!")
    
def pause(message="Press Enter to return to main menu..."):
    console.print()
    input(message)