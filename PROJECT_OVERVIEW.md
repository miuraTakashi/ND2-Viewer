# ND2 Viewer - Project Overview

## 🔬 About
A professional web-based viewer for Nikon ND2 microscopy files with advanced scientific imaging features including zoom, pan, multi-channel visualization, and auto-shutdown functionality.

## 🚀 Quick Start

### For Users
```bash
# Start the viewer
./start.sh

# Stop the viewer  
./stop.sh

# Or use macOS app
open app/ND2\ Viewer.app
```

### For Developers
```bash
# Install dependencies
pip install -r requirements.txt

# Run directly
python3 web_nd2_viewer_simple.py

# Build macOS app
./scripts/create_mac_app.sh
```

## 📁 Project Structure

```
ND2Viewer/
├── 🎯 Core Application
│   ├── web_nd2_viewer_simple.py    # Main Flask application
│   ├── templates/index.html        # Web interface
│   └── requirements.txt            # Python dependencies
│
├── 🛠️ Scripts & Tools
│   ├── start.sh                    # Quick start
│   ├── stop.sh                     # Quick stop
│   └── scripts/
│       ├── stop_nd2_viewer.sh      # Process management
│       ├── create_mac_app.sh       # macOS app builder
│       └── launch_nd2_viewer.applescript # App launcher
│
├── 🖥️ macOS Application
│   └── app/
│       └── ND2 Viewer.app/         # Native macOS app
│
├── 🎨 Assets & Resources
│   └── assets/
│       ├── nd2_icon.icns           # App icon
│       └── create_icon.py          # Icon generator
│
└── 📚 Documentation
    └── docs/
        ├── MAC_APP_README.md       # macOS app guide
        └── GITHUB_SETUP.md         # Setup instructions
```

## ✨ Key Features

- **🔍 Advanced Zoom**: 10%-500% with mouse wheel and pan support
- **📺 Multi-channel**: Scientific color mapping (Blue, Green, Red, Magenta)
- **⏱️ Time-lapse**: Navigate through temporal sequences
- **🎛️ Contrast Control**: Manual and auto-contrast adjustment
- **💾 Export**: Individual frames, channels, or complete datasets
- **🔄 Auto-shutdown**: Server stops when browser closes
- **🖥️ Native macOS App**: Desktop integration with custom icon

## 🧪 Scientific Applications

Perfect for:
- Live cell imaging analysis
- Multi-channel fluorescence microscopy
- Time-lapse data visualization
- Z-stack inspection
- High-content screening
- Publication-quality figure preparation

## 🔧 Development

The project follows a clean, modular structure:
- **Core logic**: Single Python file for easy deployment
- **Frontend**: Modern HTML5/CSS3/JavaScript interface
- **Scripts**: Automated build and management tools
- **Documentation**: Comprehensive guides and setup instructions

## 📊 Technical Stack

- **Backend**: Python 3.7+, Flask, nd2, numpy, Pillow
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Deployment**: Standalone Flask server
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **macOS Integration**: AppleScript, native app bundle

---

**Ready for scientific image analysis! 🔬✨** 