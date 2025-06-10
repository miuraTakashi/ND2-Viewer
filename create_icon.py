#!/usr/bin/env python3
"""
ND2 Viewer Icon Generator
Creates a nice icon for the macOS ND2 Viewer application
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

def create_nd2_icon():
    """Create a professional ND2 viewer icon"""
    
    # Icon size (1024x1024 for high resolution, will be scaled down)
    size = 1024
    
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Color scheme - scientific/microscopy colors
    bg_color = (45, 55, 72, 255)      # Dark blue-gray background
    primary_color = (59, 130, 246, 255)  # Blue (scientific)
    secondary_color = (16, 185, 129, 255) # Green (cells/biology)
    accent_color = (245, 101, 101, 255)   # Red (contrast)
    text_color = (255, 255, 255, 255)     # White text
    
    # Draw rounded rectangle background
    margin = 80
    corner_radius = 180
    bg_rect = [margin, margin, size - margin, size - margin]
    
    # Draw background with rounded corners
    draw.rounded_rectangle(bg_rect, radius=corner_radius, fill=bg_color)
    
    # Draw microscope lens circles (representing ND2 multi-channel imaging)
    center_x, center_y = size // 2, size // 2
    
    # Main lens circle
    lens_radius = 180
    lens_center = (center_x, center_y - 80)
    draw.ellipse([lens_center[0] - lens_radius, lens_center[1] - lens_radius,
                  lens_center[0] + lens_radius, lens_center[1] + lens_radius],
                 outline=primary_color, width=12)
    
    # Inner lens details
    inner_radius = 120
    draw.ellipse([lens_center[0] - inner_radius, lens_center[1] - inner_radius,
                  lens_center[0] + inner_radius, lens_center[1] + inner_radius],
                 outline=secondary_color, width=8)
    
    # Lens center
    center_radius = 60
    draw.ellipse([lens_center[0] - center_radius, lens_center[1] - center_radius,
                  lens_center[0] + center_radius, lens_center[1] + center_radius],
                 fill=accent_color)
    
    # Draw channel indicators (3 small circles for 3-channel imaging)
    channel_radius = 25
    channel_y = center_y + 160
    channel_colors = [primary_color, secondary_color, accent_color]
    
    for i, color in enumerate(channel_colors):
        x_offset = (i - 1) * 80  # -80, 0, 80
        channel_x = center_x + x_offset
        draw.ellipse([channel_x - channel_radius, channel_y - channel_radius,
                      channel_x + channel_radius, channel_y + channel_radius],
                     fill=color)
    
    # Draw microscope stand/base
    stand_width = 40
    stand_height = 120
    stand_x = center_x - stand_width // 2
    stand_y = lens_center[1] + lens_radius - 20
    draw.rectangle([stand_x, stand_y, stand_x + stand_width, stand_y + stand_height],
                   fill=primary_color)
    
    # Draw microscope eyepiece
    eyepiece_width = 60
    eyepiece_height = 30
    eyepiece_x = center_x - eyepiece_width // 2
    eyepiece_y = lens_center[1] - lens_radius - 40
    draw.rectangle([eyepiece_x, eyepiece_y, eyepiece_x + eyepiece_width, eyepiece_y + eyepiece_height],
                   fill=secondary_color)
    
    # Add "ND2" text
    try:
        # Try to use a system font
        font_size = 120
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    text = "ND2"
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = center_x - text_width // 2
    text_y = center_y + 280
    
    # Draw text with shadow
    shadow_offset = 3
    draw.text((text_x + shadow_offset, text_y + shadow_offset), text, font=font, fill=(0, 0, 0, 128))
    draw.text((text_x, text_y), text, font=font, fill=text_color)
    
    return img

def save_icon_formats(img, base_name="nd2_icon"):
    """Save icon in multiple formats and sizes"""
    
    # Common icon sizes for macOS
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    
    # Save as PNG files
    for size in sizes:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f"{base_name}_{size}.png")
    
    # Save original high-res version
    img.save(f"{base_name}.png")
    
    print(f"✅ Created icon files:")
    for size in sizes:
        print(f"   📁 {base_name}_{size}.png")
    print(f"   📁 {base_name}.png (original)")

def main():
    print("🎨 Creating ND2 Viewer Icon...")
    
    # Create the icon
    icon = create_nd2_icon()
    
    # Save in multiple formats
    save_icon_formats(icon)
    
    print("\n🎉 Icon creation complete!")
    print("💡 The icon represents:")
    print("   🔬 Microscope lens (scientific imaging)")
    print("   🌈 Three colored circles (multi-channel support)")
    print("   📊 Professional scientific aesthetic")
    print("   📝 'ND2' text for clear identification")

if __name__ == "__main__":
    main() 