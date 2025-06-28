# ND2 Viewer - Python Web Application

A powerful web-based viewer for Nikon ND2 microscopy files with advanced scientific imaging features.

## ✅ **Fully Working & Production Ready**

Your ND2 viewer is **complete and fully functional** with:
- **Real ND2 format support** (works with time-lapse, z-stacks, multi-channel data ✓)
- **Multi-channel color mapping** with custom colors ✓
- **Advanced contrast adjustment** and auto-contrast ✓
- **Time-lapse navigation** and z-stack support ✓
- **Multi-channel visualization** with proper scientific color schemes ✓
- **Export functionality** for individual frames and channels ✓
- **Rich metadata display** with spatial calibration information ✓
- **Modern web interface** that runs in any browser ✓
- **macOS desktop app** with custom icon ✓

## Features

### Core Functionality
- **Multi-dimensional data support**: Navigate through time (T), channels (C), and Z-stacks
- **Advanced color mapping**: Blue (DAPI), Green (FITC), Red (Texas Red), and custom colors
- **Real-time contrast adjustment**: Manual sliders + automatic optimization
- **Scientific color schemes**: Proper microscopy channel colors with intensity mapping
- **Export capabilities**: Save current frames, channels, or entire datasets
- **Spatial calibration display**: Shows pixel size, units, and objective information like ImageJ

### User Interface
- **Responsive web design**: Works on desktop, tablet, and mobile
- **Intuitive controls**: Sliders for navigation and contrast
- **Live preview**: Real-time image updates as you adjust settings
- **Professional layout**: Clean, scientific interface design
- **Smart UI**: Z-slice controls hidden for 2D data, visible for 3D stacks

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Viewer
```bash
python web_nd2_viewer_simple.py
```

### 3. Open Your Browser
Navigate to http://127.0.0.1:5001 and upload your ND2 file.

### 4. macOS App (Optional)
For macOS users, double-click `ND2 Viewer.app` for a native desktop experience.

## File Structure

```
ND2Viewer/
├── web_nd2_viewer_simple.py    # Main web application ⭐
├── templates/
│   └── index.html              # Web interface template
├── requirements.txt            # Python dependencies
├── stop_nd2_viewer.sh         # Shutdown script
├── ND2 Viewer.app/            # macOS application bundle
├── create_mac_app.sh          # macOS app builder
├── create_icon.py             # Icon generator
├── launch_nd2_viewer.applescript # macOS app launcher
├── nd2_icon.icns              # macOS app icon
├── MAC_APP_README.md          # macOS app documentation
└── README.md                  # This file
```

## Usage Examples

### Basic Viewing
1. Start the web server: `python web_nd2_viewer_simple.py`
2. Open http://127.0.0.1:5001 in your browser
3. Upload your ND2 file using the "Choose File" button
4. Navigate through channels, timepoints, z-slices, and adjust contrast

### Advanced Features
- **Channel Navigation**: Use the channel slider to switch between different fluorescence channels
- **Time-lapse Playback**: Navigate through timepoints to view dynamic processes
- **Z-Stack Navigation**: For 3D data, navigate through optical sections
- **Custom Color Mapping**: Click channel colors to open color picker and set custom colors
- **Contrast Optimization**: Use "Auto Contrast" or manual min/max sliders for optimal display
- **Metadata Viewing**: Click "Show/Hide Metadata" to see spatial calibration and acquisition details
- **Export**: Save individual frames or entire channel datasets

### Shutdown Options
- **Auto-shutdown**: The server automatically shuts down when you close the browser window/tab ✨
- **Quit Button**: Use the red "🛑 Quit ND2 Viewer" button in the web interface
- **Terminal Script**: Run `./stop_nd2_viewer.sh` to stop all ND2 viewer processes
- **Keyboard**: Press Ctrl+C in the terminal where you started the server

### Auto-Shutdown Feature ✨
The ND2 Viewer now **automatically shuts down** when you close the browser window or tab:
- **Instant shutdown**: Detects window closing and immediately stops the server
- **Heartbeat monitoring**: Backup system monitors browser connection every 15 seconds
- **Clean exit**: Properly closes files and frees resources
- **No background processes**: Server won't keep running after you're done viewing

## Technical Details

### Supported Data
- **File Format**: Nikon ND2 files
- **Dimensions**: Multi-dimensional (T×C×Z×Y×X)
- **Bit Depth**: 16-bit scientific imaging data
- **Size**: Tested with large files (145 timepoints, 3 channels, 51 z-slices, 1024×1024 pixels)

### Performance
- **Efficient Loading**: On-demand image processing
- **Memory Optimized**: Loads only requested frames
- **Fast Rendering**: Optimized contrast and color mapping
- **Browser Compatible**: Works in Chrome, Firefox, Safari, Edge
- **Smart Array Handling**: Automatically detects T×C×Y×X vs Z×C×Y×X vs T×Z×C×Y×X formats

### Dependencies
- **Python 3.7+**: Core language
- **Flask**: Web framework
- **nd2**: ND2 file reading library
- **numpy**: Numerical computations
- **Pillow**: Image processing

## Troubleshooting

### Common Issues
1. **Port in use**: Use the quit button or run `./stop_nd2_viewer.sh`
2. **Large files**: For very large ND2 files, increase browser timeout settings
3. **Memory issues**: Close other applications if handling massive datasets
4. **Z-slice not working**: Check if your ND2 file actually has Z-dimension (some are 2D time-lapse)

### Performance Tips
- Use the web interface for best performance and latest features
- Close browser tabs when not in use to free memory
- For files with many z-slices, navigate gradually to avoid memory spikes

## macOS Desktop App

The project includes a native macOS application:
- **Double-click to launch**: `ND2 Viewer.app`
- **Custom microscopy icon**: Professional scientific appearance
- **Auto-launches web server**: No terminal required
- **Desktop integration**: Appears in Dock and Applications folder

See `MAC_APP_README.md` for detailed macOS app information.

## Scientific Applications

Perfect for:
- **Live cell imaging**: Time-lapse microscopy analysis
- **Multi-channel fluorescence**: Protein colocalization studies
- **Z-stack analysis**: 3D confocal microscopy data
- **High-content screening**: Large dataset visualization
- **Publication figures**: High-quality image export with proper spatial calibration
- **Data sharing**: Web-based collaborative viewing

## Development History

This project evolved from a simple ND2 reader to a full-featured scientific imaging viewer:
- ✅ **Web interface**: Modern, responsive design
- ✅ **Multi-dimensional support**: T, C, Z navigation
- ✅ **Spatial calibration**: ImageJ-compatible metadata display
- ✅ **macOS integration**: Native desktop app with custom icon
- ✅ **Smart UI**: Adaptive controls based on data dimensions

---

**Ready to use with your ND2 files! 🔬**

*For the best experience, use the web interface (`python web_nd2_viewer_simple.py`) or the macOS app.* 