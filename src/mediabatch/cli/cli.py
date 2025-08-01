import os
import argparse
from pathlib import Path
from mediabatch.core.imageupscale import ImageUpscale
from mediabatch.core.videoupscale import VideoUpscale


def cli_main():
    parser = argparse.ArgumentParser(description="Media Batch CLI")
    parser.add_argument("--upscale", choices=["image", "video"], help="Specify the type of upscale operation")
    parser.add_argument("--single", action="store_true", help= "Perform single upscale operation")
    parser.add_argument("--batch", action="store_true", help="Perform batch upscale operation")
    parser.add_argument("--input", help="Path to the input file or directory", default="input")
    parser.add_argument("--output", help="Path to the output directory", required=False)
    parser.add_argument("--model", help="Name of the model", required=True)
    
    args = parser.parse_args()
    model_path = resolve_model_path(args.model)
    
    if args.upscale == "image":
        if args.single:
            single_image_upscale(input=args.input, model=model_path, output=args.output)
        elif args.batch:
            batch_image_upscale(model=model_path, input=args.input, output=args.output)

    elif args.upscale == "video":
        if args.single:
            single_video_upscale(input=args.input, model=model_path)
        elif args.batch:
            batch_video_upscale(model=model_path, input=args.input)


def resolve_model_path(model_arg, model_dir="models", extension=".pth"):
    if os.path.isfile(model_arg):
        return model_arg
    if not model_arg.endswith(extension):
        model_arg += extension
    model_path = os.path.join(model_dir, model_arg)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' does not exist.")
    return model_path

def resolve_input_path(input, input_dir="input"):
    if os.path.isfile(input):
        return input
    input_path = os.path.join(input_dir, input)
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_path}' does not exist.")
    return input_path

def single_image_upscale(input, model, output=None):
    upscaler = ImageUpscale(model)
    input_path = resolve_input_path(input)
    if output:
        upscaler.process_image(Path(input_path), Path(output))
    else:
        upscaler.process_image(Path(input_path))
        
def batch_image_upscale(model, input="input", output=None):
    upscaler = ImageUpscale(model)
    input_path = Path(input) if input else Path("input")
    if output:
        upscaler.process_batch_image(input_path, Path(output))
    else:
        upscaler.process_batch_image(input_path)

def single_video_upscale(input, model):
    upscaler = VideoUpscale(model)
    input_path = resolve_input_path(input)
    upscaler.process_video(Path(input_path))

def batch_video_upscale(model, input="input"):
    upscaler = VideoUpscale(model)
    input_path = Path(input) if input else Path("input")
    upscaler.batch_process_video(input_path)
    
