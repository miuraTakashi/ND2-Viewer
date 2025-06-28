# 🍎 ND2 Viewer - macOS Application

## 🚀 Quick Start

Your ND2 Viewer is now available as a native macOS application!

### ✨ Double-Click to Launch
1. **Desktop Shortcut**: Double-click `ND2 Viewer.app` on your Desktop
2. **From Project Folder**: Double-click `ND2 Viewer.app` in the project directory
3. **Automatic Launch**: The application will:
   - Start the Python web server in the background
   - Automatically open your web browser to `http://127.0.0.1:5001`
   - Display a success notification when ready

## 🔧 Features

- **🖱️ One-Click Launch**: No need to open Terminal or run Python commands
- **🌐 Auto Browser**: Automatically opens your default web browser
- **🔄 Process Management**: Kills existing instances before starting new ones
- **📱 Notifications**: Shows system notifications for status updates
- **🖥️ Desktop Integration**: Creates a convenient desktop shortcut

## 🛠️ Troubleshooting

### First Time Running
- **Security Warning**: macOS may show "ND2 Viewer can't be opened because it is from an unidentified developer"
- **Solution**: Right-click the app → Select "Open" → Click "Open" in the dialog

### Application Won't Start
1. **Check Python Environment**: Ensure your Python environment is active
2. **Dependencies**: Make sure all required packages are installed:
   ```bash
   pip install -r requirements_web.txt
   ```
3. **Port Conflict**: If port 5001 is busy, the app will show an error notification

### Browser Doesn't Open
- **Manual Access**: Open any browser and go to `http://127.0.0.1:5001`
- **Check Console**: Look for error messages in the notification

### Stopping the Application
- **Close Browser**: Simply close the browser tab/window
- **Force Quit**: The Python server runs in background - it will auto-terminate when you launch again
- **Manual Kill**: Run in Terminal: `pkill -f "python.*web_nd2_viewer"`

## 📁 File Locations

- **Application**: `ND2 Viewer.app` (in project directory)
- **Desktop Shortcut**: `~/Desktop/ND2 Viewer.app`
- **Python Source**: `web_nd2_viewer_simple.py`
- **AppleScript Source**: `launch_nd2_viewer.applescript`

## 🔨 Rebuilding the Application

If you modify the Python code or want to rebuild the app:

```bash
./create_mac_app.sh
```

This will recreate the application bundle with any updates.

## 💡 Advanced Usage

### Running from Dock
- Drag `ND2 Viewer.app` to your Dock for quick access

### Creating Aliases
- Right-click the app → "Make Alias" to create shortcuts anywhere

### Customizing Launch
- Edit `launch_nd2_viewer.applescript` to modify startup behavior
- Rebuild with `./create_mac_app.sh` after changes

## 🆘 Getting Help

If you encounter issues:
1. Check this README for common solutions
2. Look at the main project README.md for Python-specific help
3. Check Terminal output for detailed error messages
4. Ensure your ND2 files are accessible and not corrupted

---

**Enjoy your ND2 microscopy imaging with the convenience of a native macOS application!** 🔬✨ 