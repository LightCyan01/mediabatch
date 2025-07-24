# Mediabatch

**Mediabatch** is a terminal-based image and video upscaling tool that uses AI models to enhance the resolution and quality of your media files. It provides both single file and batch processing capabilities through an intuitive text user interface (TUI).

## ✨ Features

- **🖼️ Image Upscaling**: Single and batch image processing
- **🎥 Video Upscaling**: Single and batch video processing
- **🚀 GPU Acceleration**: Automatic CUDA detection for faster processing
- **📁 Batch Processing**: Process entire directories of images or videos
- **🎯 User-Friendly**: Interactive terminal interface with clear navigation
- **🔧 Flexible**: Support for various image formats (PNG, JPEG, BMP, TIFF, WebP, GIF)
- **🎬 Video Support**: Multiple video formats (MP4, AVI, MOV, MKV, WEBM, FLV, WMV)

## 🔧 Requirements

### System Requirements

- **Python**: 3.11 or higher
- **FFmpeg**: Required for video processing
- **GPU**: NVIDIA GPU with CUDA support (optional, falls back to CPU)

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
- [ ] **NCNN Architecture Support**: Add support for NCNN models
- [ ] **CLI Arguments**: Command-line interface without TUI for automation
- [x] **Progress Bars**: Real-time progress indication for long operations
- [ ] **Model Management**: Built-in model organization and metadata
- [ ] **Configuration System**: Settings persistence and customization
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
