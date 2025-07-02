from src import utils
import tkinter as tk
from tkinter.filedialog import askopenfilename
from src.upscaler import PytorchModel

def main():
    print("Mediabatch - A GPU-aware video & image batch-processor")

    image_process(utils.get_device())
    

def image_process(device):
    
    print(device)
    print("1. Image Upscale")
    
    option = input("Select your option: ")
    
    if option == "1":
        print("Select Pytorch Model")
        model_path = get_model()
        
        if model_path:
            upscaler = PytorchModel(model_path, device)
            print("Model loaded Successfully\n")
            print("Select an Image:")
            image_path = get_image()
            if image_path:
                print("Image loaded Successfully\n")
            else:
                raise FileNotFoundError("No Image file selected")
            upscaler.process(image_path)
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