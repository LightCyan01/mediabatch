import tkinter as tk
import torch
from src.utils import get_device
from src.imageupscale import ImageUpscale
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
    print("1. Image Upscale")
    
    option = input("Select your option: ")
    
    if option == "1":
        print("Select Pytorch Model")
        model_path = get_model()
        
        if model_path:
            upscaler = ImageUpscale(model_path)
            print("Model loaded Successfully\n")
            print("Select an Image:")
            image_path = get_image()
            if image_path:
                print("Image loaded Successfully\n")
            else:
                raise FileNotFoundError("No Image file selected")
            upscaler.process_image(image_path)
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
    
    image = askopenfilename(title="Select Image")
    
    root.destroy()
    return image
    
if __name__ == "__main__":
    main()