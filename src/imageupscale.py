from src.baseupscaler import BaseUpscaler
from src.utils import convert_to_rgb, save_image, get_device, load_images
import torch

class ImageUpscale(BaseUpscaler):
    def __init__(self, model_path):
        #load model
        upscaler = BaseUpscaler.load_from_file(model_path)
        
        #initialize parent class with loaded model
        super().__init__(upscaler._model)
        
        self._device = get_device()
        self.model = self._model.to(self._device).eval()
        
    def run(self, image_tensor: torch.Tensor):
        with torch.no_grad():
            return self.model(image_tensor.to(self._device))
        
    def process_image(self, image_path, output_dir = None) -> None:
        #load and convert image to RGB
        image = convert_to_rgb(image_path)
        
        #convert to tensor
        image_tensor = self.pil_to_tensor(image)
        
        #run through model
        result = self.run(image_tensor)
        
        #convert to PIL
        output_image = self.tensor_to_pil(result)
        
        #save image
        if output_dir:
            save_image(output_image, image_path, output_dir)
        else:
            save_image(output_image, image_path)
        
    def process_batch_image(self, input_dir) -> None:
        image_files = load_images(input_dir)
        
        if not image_files:
            print(f"No images found in {input_dir}")
            return

        for image_file in image_files:
            print(f"Processing {image_file.name}")
            self.process_image(image_file)
        
        print("Batch processing Complete!")
        
        

    
        
        
    