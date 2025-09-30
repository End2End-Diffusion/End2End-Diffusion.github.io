#!/usr/bin/env python3
"""
Create a placeholder hero image for testing layout.
This creates a simple gradient image that matches the aspect ratio.

Usage:
    python create_placeholder_hero.py
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def create_placeholder_hero():
    """Create a placeholder hero image with gradient."""

    # Dimensions for 16:9 aspect ratio
    width, height = 1200, 675

    # Create gradient from blue to purple
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    # Create gradient
    for y in range(height):
        # Blue (#667eea) to Purple (#764ba2)
        r = int(102 + (118 - 102) * y / height)
        g = int(126 + (75 - 126) * y / height)
        b = int(234 + (162 - 234) * y / height)
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

    # Add some simple geometric shapes to suggest the concept
    # Left side: scattered circles (global information)
    np.random.seed(42)
    for _ in range(30):
        x = np.random.randint(50, width//2 - 50)
        y = np.random.randint(50, height - 50)
        r = np.random.randint(3, 8)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(180, 200, 255, 128))

    # Right side: grid pattern (spatial structure)
    grid_start = width // 2 + 50
    grid_size = 40
    for i in range(0, height, grid_size):
        for j in range(grid_start, width - 50, grid_size):
            draw.ellipse([j-5, i-5, j+5, i+5], fill=(200, 180, 255), outline=(255, 255, 255))
            # Connect to neighbors
            if i < height - grid_size:
                draw.line([j, i, j, i+grid_size], fill=(255, 255, 255, 100), width=1)
            if j < width - 50 - grid_size:
                draw.line([j, i, j+grid_size, i], fill=(255, 255, 255, 100), width=1)

    # Add text overlay (placeholder)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Add centered text
    text = "Generate with Flux"
    text2 = "python assets/flux/generate_hero.py"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    text_y = height // 2 - 40

    # Draw text with shadow
    draw.text((text_x+2, text_y+2), text, fill=(0, 0, 0, 100), font=font)
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

    bbox2 = draw.textbbox((0, 0), text2, font=font_small)
    text2_width = bbox2[2] - bbox2[0]
    text2_x = (width - text2_width) // 2
    text2_y = text_y + 50

    draw.text((text2_x, text2_y), text2, fill=(255, 255, 255, 200), font=font_small)

    # Save
    output_path = Path(__file__).parent.parent.parent / "static/img/hero.png"
    image.save(output_path, "PNG", optimize=True)
    print(f"✓ Placeholder hero image created: {output_path}")
    print(f"  Dimensions: {width}x{height} (16:9)")
    print("\nThis is a placeholder. Generate the real hero image with:")
    print("  cd assets/flux && python generate_hero.py")

    return str(output_path)


if __name__ == "__main__":
    print("Creating placeholder hero image...")
    print("="*60)
    create_placeholder_hero()
    print("="*60)