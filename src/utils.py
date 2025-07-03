from pathlib import Path
from PIL import Image
import torch


def get_device():
    if torch.cuda.is_available():
        return torch.device('cuda')
    return torch.device('cpu')

def convert_to_rgb(image_path: str):
    image = Image.open(image_path)
    
    if image.mode == "RGBA":
        image = image.convert('RGB')
    return image

def save_image(image: Image.Image, image_path: str):
    """
    Save PIL image to output directory with original filename from path
    """
    
    output_dir = Path("output/")
    output_dir.mkdir(exist_ok=True)
    
    filename = Path(image_path).name
    final_path = output_dir / filename
    image.save(final_path)
    
    
