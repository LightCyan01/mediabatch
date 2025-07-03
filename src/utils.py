from pathlib import Path
from PIL import Image
import torch

def get_device():
    if torch.cuda.is_available():
        return torch.device('cuda')
    return torch.device('cpu')

def convert_to_rgb(image_path: Path):
    image = Image.open(image_path)
    
    if image.mode == "RGBA":
        image = image.convert('RGB')
    return image

def save_image(image: Image.Image, image_path: Path, output_dir: Path = Path("output/")):
    """
    Save PIL image to output directory with original filename from path
    """
    output_dir.mkdir(exist_ok=True)
    
    filename = image_path.name
    final_path = output_dir / filename
    image.save(final_path)
    
def load_images(input_dir: Path = Path("input/")):
    """
    Loads PIL images from input directory 
    """
    input_dir.mkdir(exist_ok=True)
    ext = {'.png', '.jpg','.jpeg','.bmp','.tiff','.webp'}
    
    image_files = [f for f in input_dir.iterdir() 
                   if f.is_file() and f.suffix.lower() in ext]
    return image_files
        
