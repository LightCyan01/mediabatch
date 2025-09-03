# Mediabatch

**Mediabatch** is a terminal-based image and video upscaling tool that uses AI models to enhance the resolution and quality of your media files. It provides both single file and batch processing capabilities through an interactive text user interface (TUI) or command-line interface (CLI).

## Features

- **Image Upscaling**: Single and batch image processing
- **Video Upscaling**: Single and batch video processing
- **GPU Acceleration**: Automatic CUDA detection for faster processing
- **Batch Processing**: Process entire directories of images or videos
- **Dual Interface**: Interactive TUI or CLI for automation
- **Flexible**: Support for various image formats (PNG, JPEG, BMP, TIFF, WebP, GIF)
- **Video Support**: Multiple video formats (MP4, AVI, MOV, MKV, WEBM, FLV, WMV)

## Requirements

### System Requirements

- **Python**: 3.11 or higher
- **FFmpeg**: Required for video processing
- **GPU**: NVIDIA GPU with CUDA support (optional, falls back to CPU)

## Installation

### 1. Install FFmpeg

FFmpeg is required for video processing. Install it for your platform:

**Windows:**

- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Add to your system PATH

**macOS:**

```bash
brew install ffmpeg
```

**Linux:**

```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Install uv (Package Manager)

**Option 1: Using pip**

```bash
pip install uv
```

**Option 2: Using PowerShell (Windows)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Option 3: Using curl (macOS/Linux)**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Clone and Install

```bash
git clone <repository-url>
cd mediabatch
uv venv
uv pip install .
```

For development:

```bash
uv pip install .[dev]
```

## Usage

### Interactive TUI

```bash
# Run the interactive TUI
uv run src/main.py

# Or use the batch file (Windows)
run-tui.bat
```

### Command Line Interface (CLI)

#### CLI Options

- `--upscale`: Choose operation type (`image` or `video`)
- `--single`: Process a single file
- `--batch`: Process all files in a directory
- `--input`: Input file or directory path (defaults to `input/`)
- `--model`: Model file path or name (searches in `models/` if filename only)
- `--output`: Output directory path (defaults to `output/`)

#### Basic Syntax

```bash
uv run src/main.py --upscale <type> --<mode> --input <path> --model <model> [--output <path>]
```

#### CLI Examples

**Single Image Upscaling:**

```bash
# Upscale a single image with full paths
uv run src/main.py --upscale image --single --input "C:\path\to\image.jpg" --model "path\to\model.pth" --output "C:\output"

# Using default directories (input/ and output/)
uv run src/main.py --upscale image --single --input "photo.jpg" --model "2x_ESRGAN"
```

**Batch Image Processing:**

```bash
# Process all images in a directory
uv run src/main.py --upscale image --batch --input "C:\my_images" --model "4x_RealESRGAN" --output "C:\upscaled"

# Using default input directory
uv run src/main.py --upscale image --batch --model "2x_ESRGAN"
```

**Single Video Upscaling:**

```bash
# Upscale a single video file
uv run src/main.py --upscale video --single --input "movie.mp4" --model "4x_RealESRGAN"

# With custom output directory
uv run src/main.py --upscale video --single --input "C:\videos\clip.mkv" --model "2x_ESRGAN" --output "C:\enhanced"
```

**Batch Video Processing:**

```bash
# Process all videos in a directory
uv run src/main.py --upscale video --batch --input "videos" --model "2x_ESRGAN"

# Full path example
uv run src/main.py --upscale video --batch --input "C:\raw_videos" --model "C:\models\upscaler.pth" --output "C:\processed"
```

#### Model Path Handling

The CLI accepts both full paths and filenames for models:

```bash
# Full path to model
--model "C:\models\4x_RealESRGAN.pth"

# Filename only (searches in models/ directory)
--model "4x_RealESRGAN"

# Adds .pth extension automatically
--model "2x_ESRGAN"  # becomes "models/2x_ESRGAN.pth"
```

### Directory Structure

The tool expects and creates these directories:

- `input/` - Place files here for batch processing
- `output/` - Processed files are saved here
- `models/` - Store your AI upscaling models

### Supported Formats

**Images:**

- PNG, JPEG/JPG, BMP, TIFF/TIF, WebP, GIF

**Videos:**

- MP4, AVI, MOV, MKV, WMV, FLV, WebM, M4V

**Models:**

- All models supported by [Spandrel](https://github.com/chaiNNer-org/spandrel)
- PyTorch formats (.pth, .pt, .safetensors)
- Support for popular architectures (ESRGAN, Real-ESRGAN, SwinIR, HAT, etc.)
- See [Spandrel's supported architectures](https://github.com/chaiNNer-org/spandrel#supported-architectures) for complete list

## Troubleshooting

### Common Issues

**"ffmpeg not found"**

- Ensure FFmpeg is installed and in your system PATH
- Test with `ffmpeg -version` in terminal

**"CUDA not available"**

- Install CUDA-compatible PyTorch: `uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`
- Verify GPU detection: Check startup messages

**"Model loading failed"**

- Ensure model file is compatible with Spandrel
- Check model file integrity
- Verify file permissions

**"Permission denied"**

- Check file/directory permissions
- Ensure output directory is writable
- Close files in other applications

## TODO

### Completed Features

- [x] Image upscaling (single and batch)
- [x] Video upscaling (single and batch)
- [x] FFmpeg integration for video processing
- [x] Audio preservation in video upscaling
- [x] Multiple image/video format support
- [x] Cross-platform compatibility
- [x] CLI Arguments: Command-line interface without TUI for automation
- [x] Progress Bars: Real-time progress indication for long operations

### 🚧 Planned Features

- [ ] **NCNN Architecture Support**: Add support for NCNN models
- [ ] **Configuration System**: Settings persistence and customization

## Contributing

If you'd like to help improve Mediabatch, please follow these guidelines:

1. Fork the repository
2. Describe your changes
3. Write clear, maintainable code

If you have questions or want to discuss ideas, feel free to open an issue or start a discussion.

---

**Happy upscaling!**
