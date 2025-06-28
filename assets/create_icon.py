#!/usr/bin/env python3
"""
Simple ND2 Icon Creator
Creates a clean, minimalist icon with just "ND2" text on white background
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_simple_nd2_icon():
    """Create a simple ND2 icon with text on white background"""
    
    # Create a white square image
    size = 1024
    image = Image.new('RGBA', (size, size), (255, 255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)
    
    # Try to use a bold system font, fallback to default if not available
    font_size = int(size * 0.35)  # 35% of image size
    
    try:
        # Try to use a bold font
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            # Fallback to Arial Bold
            font = ImageFont.truetype("/System/Library/Fonts/Arial Bold.ttf", font_size)
        except:
            try:
                # Another fallback
                font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)
            except:
                # Use default font if no system fonts available
                font = ImageFont.load_default()
    
    # Text to draw
    text = "ND2"
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Draw the text in dark color for good contrast
    text_color = (32, 32, 32, 255)  # Dark gray, almost black
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Add a subtle border for definition
    border_color = (200, 200, 200, 255)  # Light gray
    border_width = 2
    draw.rectangle([0, 0, size-1, size-1], outline=border_color, width=border_width)
    
    return image

def create_icon_set():
    """Create all required icon sizes for macOS"""
    
    print("🎨 Creating simple ND2 icon...")
    
    # Create the base 1024x1024 icon
    base_icon = create_simple_nd2_icon()
    
    # Icon sizes required for macOS
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    
    # Create iconset directory
    iconset_dir = "nd2_icon.iconset"
    if not os.path.exists(iconset_dir):
        os.makedirs(iconset_dir)
    
    # Generate all sizes
    for size in sizes:
        print(f"  📐 Creating {size}x{size} icon...")
        
        # Resize the base icon
        if size == 1024:
            resized = base_icon
        else:
            resized = base_icon.resize((size, size), Image.Resampling.LANCZOS)
        
        # Save standard resolution
        filename = f"icon_{size}x{size}.png"
        resized.save(os.path.join(iconset_dir, filename), "PNG")
        
        # Save @2x (retina) versions for applicable sizes
        if size <= 512:
            retina_filename = f"icon_{size}x{size}@2x.png"
            retina_size = size * 2
            if retina_size <= 1024:
                retina_resized = base_icon.resize((retina_size, retina_size), Image.Resampling.LANCZOS)
                retina_resized.save(os.path.join(iconset_dir, retina_filename), "PNG")
    
    print(f"✅ Icon set created in {iconset_dir}/")
    return iconset_dir

def convert_to_icns():
    """Convert the iconset to .icns format using macOS iconutil"""
    
    iconset_dir = "nd2_icon.iconset"
    icns_file = "nd2_icon.icns"
    
    print("🔄 Converting to .icns format...")
    
    # Use macOS iconutil to convert
    import subprocess
    try:
        result = subprocess.run([
            "iconutil", "-c", "icns", iconset_dir, "-o", icns_file
        ], check=True, capture_output=True, text=True)
        
        print(f"✅ Created {icns_file}")
        return icns_file
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating .icns file: {e}")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        return None
    except FileNotFoundError:
        print("❌ iconutil not found. This script requires macOS to create .icns files.")
        return None

if __name__ == "__main__":
    print("🎯 Creating Simple ND2 Icon")
    print("=" * 40)
    
    # Create the icon set
    iconset_dir = create_icon_set()
    
    # Convert to .icns
    icns_file = convert_to_icns()
    
    if icns_file:
        print("\n🎉 Simple ND2 icon created successfully!")
        print(f"📁 Icon files: {iconset_dir}/")
        print(f"🖼️  macOS icon: {icns_file}")
        print("\nYou can now use this icon for your ND2 Viewer app!")
    else:
        print("\n⚠️  Icon PNG files created, but .icns conversion failed.")
        print("You can still use the PNG files from the iconset directory.") 