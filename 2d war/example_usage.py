#!/usr/bin/env python3
"""
Example usage script for the Historical Video Generator
Run this after installing dependencies to test the system
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys


def create_sample_photo():
    """Create a sample historical-style photo for testing"""
    
    # Create examples directory
    examples_dir = Path("examples")
    examples_dir.mkdir(exist_ok=True)
    
    photo_path = examples_dir / "sample_photo.jpg"
    
    if photo_path.exists():
        print(f"Sample photo already exists at: {photo_path}")
        return str(photo_path)
    
    # Create a simple vintage-style image
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color=(240, 230, 210))
    
    draw = ImageDraw.Draw(img)
    
    # Draw a simple historical scene representation
    # Sky
    for y in range(0, height // 2):
        color_value = int(200 - (y / (height // 2)) * 50)
        draw.rectangle([0, y, width, y + 1], fill=(color_value, color_value, color_value + 20))
    
    # Ground
    for y in range(height // 2, height):
        color_value = int(150 - ((y - height // 2) / (height // 2)) * 30)
        draw.rectangle([0, y, width, y + 1], fill=(color_value - 20, color_value - 10, color_value - 30))
    
    # Simple building silhouette
    building_x = width // 3
    building_y = height // 3
    building_w = width // 3
    building_h = height // 2
    draw.rectangle(
        [building_x, building_y, building_x + building_w, building_y + building_h],
        fill=(80, 80, 90)
    )
    
    # Windows
    for i in range(3):
        for j in range(4):
            wx = building_x + 50 + i * 150
            wy = building_y + 50 + j * 100
            draw.rectangle([wx, wy, wx + 80, wy + 60], fill=(200, 200, 150))
    
    # Add some text
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    text = "Historical Moment"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (width - text_width) // 2
    
    draw.text((text_x, height - 150), text, fill=(100, 100, 100), font=font)
    
    # Save
    img.save(photo_path, quality=95)
    print(f"Created sample photo at: {photo_path}")
    
    return str(photo_path)


def run_example_1():
    """Documentary style example"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Documentary Style")
    print("="*60)
    
    photo_path = create_sample_photo()
    
    cmd = f'''python main.py \
  --photo_path "{photo_path}" \
  --topic "A pivotal moment in history that shaped our modern world" \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 12 \
  --output_dir output/example1'''
    
    print(f"\nCommand:\n{cmd}\n")
    os.system(cmd)


def run_example_2():
    """Authoritarian newsreel style example"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Authoritarian Newsreel Style")
    print("="*60)
    
    photo_path = create_sample_photo()
    
    cmd = f'''python main.py \
  --photo_path "{photo_path}" \
  --topic "Workers unite for progress and prosperity" \
  --style_template authoritarian \
  --voice_profile deep_male_retro \
  --duration_seconds 8 \
  --output_dir output/example2'''
    
    print(f"\nCommand:\n{cmd}\n")
    os.system(cmd)


def run_example_3():
    """Academic lecture example"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Academic Lecture Style")
    print("="*60)
    
    photo_path = create_sample_photo()
    
    cmd = f'''python main.py \
  --photo_path "{photo_path}" \
  --topic "Examining the social and economic transformations of the twentieth century" \
  --style_template lecture \
  --voice_profile authoritative_male \
  --duration_seconds 15 \
  --output_dir output/example3'''
    
    print(f"\nCommand:\n{cmd}\n")
    os.system(cmd)


def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║     Historical Video Generator - Example Usage            ║
║                                                            ║
║     This script demonstrates different styles and          ║
║     voice profiles for educational content generation.     ║
╚════════════════════════════════════════════════════════════╝
""")
    
    if len(sys.argv) > 1:
        example_num = sys.argv[1]
        if example_num == "1":
            run_example_1()
        elif example_num == "2":
            run_example_2()
        elif example_num == "3":
            run_example_3()
        else:
            print("Usage: python example_usage.py [1|2|3]")
            print("  1 - Documentary style")
            print("  2 - Authoritarian newsreel style")
            print("  3 - Academic lecture style")
    else:
        print("Choose an example:")
        print("  1 - Documentary style (engaging, narrative)")
        print("  2 - Authoritarian newsreel style (commanding, retro)")
        print("  3 - Academic lecture style (analytical, thoughtful)")
        print("\nRun: python example_usage.py [1|2|3]")
        print("\nOr create your own with:")
        print("  python main.py --photo_path YOUR_PHOTO.jpg --topic 'Your topic' ...")


if __name__ == "__main__":
    main()

