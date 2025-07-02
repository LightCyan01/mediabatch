from spandrel import ImageModelDescriptor, ModelLoader, UnsupportedModelError
from pathlib import Path
import torch
from PIL import Image
import torchvision.transforms as transforms


class PytorchModel():
    def __init__(self, model_path: str, device: None):
        loader = ModelLoader()
        model = loader.load_from_file(model_path)
        if not isinstance(model, ImageModelDescriptor):
            raise UnsupportedModelError()
        self.model = model.to(device).eval()
        
    def process(self, image_path: str) -> torch.Tensor:
        output_dir = Path("output/")
        
        output_dir.mkdir(exist_ok=True)
        
        #load image
        image = Image.open(image_path)
        
        if image.mode == "RGBA":
            image = image.convert('RGB')
            
        #convert to tensor
        to_tensor = transforms.ToTensor()
        #add batch dimension to image - tensor shape: [C, H, W] -> [1, C, H, W]
        image_tensor = to_tensor(image).unsqueeze(0).to(self.model.device)
        
        with torch.no_grad():
            result =  self.model(image_tensor)
            
        #convert tensor to PIL Image
        to_pil = transforms.ToPILImage()
        #remove batch dimension
        output_image = to_pil(result.cpu().squeeze(0))
        
        #save image
        input_path = Path(image_path)
        file_name = input_path.stem + "_upscaled" + input_path.suffix
        final_path = output_dir / file_name
        output_image.save(final_path)
    
        
        
    