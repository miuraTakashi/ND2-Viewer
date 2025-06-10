#!/bin/bash

# ND2 Viewer macOS Application Builder
# This script creates a double-clickable macOS application

echo "🔨 Creating ND2 Viewer macOS Application..."

# Define application name and paths
APP_NAME="ND2 Viewer"
APP_BUNDLE="${APP_NAME}.app"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Remove existing app bundle if it exists
if [ -d "$APP_BUNDLE" ]; then
    echo "📁 Removing existing application bundle..."
    rm -rf "$APP_BUNDLE"
fi

# Compile AppleScript to application
echo "⚙️  Compiling AppleScript..."
osacompile -o "$APP_BUNDLE" "$SCRIPT_DIR/launch_nd2_viewer.applescript"

# Check if compilation was successful
if [ ! -d "$APP_BUNDLE" ]; then
    echo "❌ Failed to create application bundle"
    exit 1
fi

# Create Contents/Resources directory if it doesn't exist
echo "🎨 Setting up application icon..."
RESOURCES_DIR="$APP_BUNDLE/Contents/Resources"
mkdir -p "$RESOURCES_DIR"

# Copy our custom icon if it exists
if [ -f "$SCRIPT_DIR/nd2_icon.icns" ]; then
    cp "$SCRIPT_DIR/nd2_icon.icns" "$RESOURCES_DIR/applet.icns"
    echo "   ✅ Custom ND2 icon installed"
else
    echo "   ⚠️  Custom icon not found, using default"
fi

# Create/update Info.plist with proper icon reference
echo "📝 Updating application metadata..."
INFO_PLIST="$APP_BUNDLE/Contents/Info.plist"

# Update the Info.plist to include icon and better metadata
/usr/libexec/PlistBuddy -c "Set :CFBundleIconFile applet.icns" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleIconFile string applet.icns" "$INFO_PLIST"

/usr/libexec/PlistBuddy -c "Set :CFBundleName $APP_NAME" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleName string '$APP_NAME'" "$INFO_PLIST"

/usr/libexec/PlistBuddy -c "Set :CFBundleDisplayName $APP_NAME" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleDisplayName string '$APP_NAME'" "$INFO_PLIST"

/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier com.nd2viewer.app" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleIdentifier string com.nd2viewer.app" "$INFO_PLIST"

/usr/libexec/PlistBuddy -c "Set :CFBundleVersion 1.0" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleVersion string 1.0" "$INFO_PLIST"

/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString 1.0" "$INFO_PLIST" 2>/dev/null || \
/usr/libexec/PlistBuddy -c "Add :CFBundleShortVersionString string 1.0" "$INFO_PLIST"

# Set permissions
echo "🔧 Setting permissions..."
chmod +x "$APP_BUNDLE/Contents/MacOS/applet"

# Create desktop shortcut
echo "🖥️  Creating desktop shortcut..."
DESKTOP_PATH="$HOME/Desktop/$APP_BUNDLE"
if [ -L "$DESKTOP_PATH" ] || [ -d "$DESKTOP_PATH" ]; then
    rm -rf "$DESKTOP_PATH"
fi
ln -s "$SCRIPT_DIR/$APP_BUNDLE" "$DESKTOP_PATH"

# Clean up temporary files
echo "🧹 Cleaning up..."
rm -rf nd2_icon.iconset
rm -f nd2_icon_*.png

echo
echo "✅ ND2 Viewer application created successfully!"
echo
echo "📍 Application Location: $SCRIPT_DIR/$APP_BUNDLE"
echo "🖥️  Desktop Shortcut: $DESKTOP_PATH"
echo "🎨 Icon: Custom ND2 microscopy icon installed"
echo
echo "🚀 To use:"
echo "   1. Double-click 'ND2 Viewer.app' from Finder or Desktop"
echo "   2. The ND2 viewer will start automatically in your browser"
echo "   3. Upload your ND2 files and start viewing!"
echo
echo "💡 Note: The first time you run it, macOS may ask for permission"
echo "   to run the application. Click 'Open' to allow it." 