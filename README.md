# Mediabatch

**Mediabatch** is a terminal-based image and video upscaling tool powered by [Spandrel](https://github.com/chaiNNer-org/spandrel) that uses AI models to enhance the resolution and quality of your media files. It provides both single file and batch processing capabilities through an intuitive text user interface (TUI).

## ✨ Features

- **🖼️ Image Upscaling**: Single and batch image processing
- **🎥 Video Upscaling**: Single and batch video processing with audio preservation
- **🚀 GPU Acceleration**: Automatic CUDA detection for faster processing
- **📁 Batch Processing**: Process entire directories of images or videos
- **🎯 User-Friendly**: Interactive terminal interface with clear navigation
- **🔧 Flexible**: Support for various image formats (PNG, JPEG, BMP, TIFF, WebP, GIF)
- **🎬 Video Support**: Multiple video formats (MP4, AVI, MOV, MKV)

## 🔧 Requirements

### System Requirements

- **Python**: 3.11 or higher
- **FFmpeg**: Required for video processing
- **GPU**: NVIDIA GPU with CUDA support (optional, falls back to CPU)

### Dependencies

- PyTorch (with CUDA support)
- Spandrel (AI model loader)
- Rich (terminal UI)
- Pillow (image processing)
- Questionary (interactive prompts)

## 📦 Installation

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

```bash
pip install uv
```

### 3. Clone and Install

```bash
git clone <repository-url>
cd mediabatch
uv pip install .
```

For development:

```bash
uv pip install .[dev]
```

## 🚀 Usage

### Quick Start

```bash
# Run the interactive TUI
uv run main.py

# Or use the batch file (Windows)
run-tui.bat
```

### Directory Structure

The tool expects and creates these directories:

- `input/` - Place files here for batch processing
- `output/` - Processed files are saved here
- `models/` - Store your AI upscaling models

### Workflow

1. **Launch the application**
2. **Select processing type**:
   - Image Upscale → Single/Batch
   - Video Upscale → Single/Batch
3. **Choose your AI model** (PyTorch .pth/.pt/.safetensors files)
4. **Select input files** (single mode) or ensure files are in `input/` directory (batch mode)
5. **Wait for processing** - files will be saved to `output/` directory

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

## 🔄 Processing Flow

### Image Processing

1. Load AI model using Spandrel (supports 50+ architectures)
2. Convert image to RGB format
3. Transform to tensor and add batch dimension
4. Run inference on GPU/CPU
5. Convert back to PIL image
6. Save to output directory

### Video Processing

1. Extract frames using FFmpeg
2. Process each frame through Spandrel-powered upscaling pipeline
3. Combine upscaled frames back to video with original audio
4. Preserve original frame rate and audio quality

## 🐛 Troubleshooting

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

## 📋 Requirements

### Core Dependencies

```toml
dependencies = [
    "rich>=14.0.0",         # Terminal UI
    "spandrel>=0.4.1",      # AI model loader
    "torch>=2.7.0",         # PyTorch
    "torchvision>=0.22.0",  # Vision utilities
    "pillow>=11.3.0",       # Image processing
    "questionary>=2.1.0",   # Interactive prompts
]
```

### Development Dependencies

```toml
[dependency-groups]
dev = [
    "pytest>=8.4.1",
]
```

## 📝 TODO

### ✅ Completed Features

- [x] Image upscaling (single and batch)
- [x] Video upscaling (single and batch)
- [x] GPU/CPU automatic detection
- [x] Interactive TUI with Rich and Questionary
- [x] Spandrel model loading support
- [x] FFmpeg integration for video processing
- [x] Audio preservation in video upscaling
- [x] Multiple image/video format support
- [x] Cross-platform compatibility

### 🚧 Planned Features

- [ ] **Model Download System**: Automatic downloading of popular Spandrel-supported models
- [ ] **NCNN Architecture Support**: Add support for NCNN models for mobile/embedded devices
- [ ] **CLI Arguments**: Command-line interface without TUI for automation
- [ ] **Progress Bars**: Real-time progress indication for long operations
- [ ] **Model Management**: Built-in model organization and metadata
- [ ] **Configuration System**: Settings persistence and customization
- [ ] **Batch Queue System**: Queue management for large batch operations
- [ ] **Preview Mode**: Before/after comparison preview
- [ ] **Plugin System**: Extensible architecture for custom processing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🆘 Support

For issues, questions, or contributions:

- Open an issue on GitHub
- Check the troubleshooting section
- Review existing issues and discussions

---

**Happy upscaling! 🚀**
