from abc import ABC
from PIL import Image
from pathlib import Path
from spandrel import ImageModelDescriptor, ModelLoader
import torch
import torchvision.transforms as transforms

class BaseUpscaler(ABC):
    def __init__(self, model: ImageModelDescriptor):
        self._model = model
    
    @staticmethod
    def pil_to_tensor(image: Image) -> torch.Tensor:
        """
        converts PIL image to torch.Tensor format
        """
        tensor = transforms.ToTensor()
        image_tensor = tensor(image)
        
        #Add Batch Dimensions: [C, H, W] -> [N, C, H, W]
        image_dim = image_tensor.unsqueeze(0)
        return image_dim
    
    @staticmethod
    def tensor_to_pil(tensor: torch.Tensor) -> Image.Image:
        """
        converts torch.Tensor to a PIL Image
        """
        to_pil = transforms.ToPILImage()
        
        #Move tensor from GPU to CPU (PIL requires CPU tensors)
        #Remove Batch Dimensions: [N, C, H, W] -> [C, H, W]
        output_image = to_pil(tensor.cpu().squeeze(0))
        return output_image
    
    @classmethod
    def load_from_file(cls, path: Path):
        loader = ModelLoader()
        model = loader.load_from_file(path)
        return cls(model)
    
    @classmethod
    def load_state_dict_from_file(cls, path: Path):
        loader = ModelLoader()
        model = loader.load_state_dict_from_file(path)
        return cls(model)

        