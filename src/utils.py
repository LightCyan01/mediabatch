import torch

def get_device():
    if torch.cuda.is_available():
        device = torch.device('cuda')
        print(f"Using GPU: {torch.cuda.get_device_name()}")
        return device
    else:
        device = torch.device('cpu')
        print("Using CPU")
        return device
        