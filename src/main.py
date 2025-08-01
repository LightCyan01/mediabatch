import sys
from rich.console import Console
from rich.panel import Panel
from mediabatch.cli.cli import cli_main
from mediabatch.menu.menu import main_menu, image_upscale_option, single_image_upscale, batch_image_upscale, video_upscale_option, single_video_upscale, batch_video_upscale, pause
console = Console()

def tui_main():
    while True:
        choice = main_menu()
        
        if choice == "Image Upscale":
            while True:
                sub = image_upscale_option()
                if sub == "Single Image Upscale":
                    console.clear()
                    single_image_upscale()
                    pause()
                elif sub == "Batch Image Upscale":
                    console.clear()
                    batch_image_upscale()
                    pause()
                elif sub == "Back":
                    break
        elif choice == "Video Upscale":
            while True:
                sub = video_upscale_option()
                if sub == "Single Video Upscale":
                    console.clear()
                    single_video_upscale()
                    pause()
                elif sub == "Batch Video Upscale":
                    console.clear()
                    batch_video_upscale()
                    pause()
                elif sub == "Back":
                    break
        elif choice == "Quit":
            console.clear()
            console.print(Panel("👋 Goodbye!", expand=False))
            sys.exit(0) 
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_main()
    else:
        tui_main()