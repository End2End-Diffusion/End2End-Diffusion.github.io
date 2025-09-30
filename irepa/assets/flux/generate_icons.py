#!/usr/bin/env python3
"""
Generate takeaway icons for iREPA project page using Flux AI.

Usage:
    python generate_icons.py [--icon NAME]  # Generate specific icon
    python generate_icons.py                 # Generate all icons

Requirements:
    pip install replicate pyyaml pillow

Set your API key:
    export REPLICATE_API_TOKEN="your-token-here"
"""

import os
import sys
import yaml
from pathlib import Path

try:
    import replicate
except ImportError:
    print("Error: replicate package not installed")
    print("Install with: pip install replicate")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Warning: pillow not installed, skipping optimization")
    Image = None


def load_prompts():
    """Load prompts from YAML file."""
    prompts_file = Path(__file__).parent / "prompts.yaml"
    with open(prompts_file) as f:
        return yaml.safe_load(f)


def generate_image(prompt_config, output_dir):
    """Generate image using Flux via Replicate."""
    # Check for API token
    if not os.getenv("REPLICATE_API_TOKEN"):
        print("Error: REPLICATE_API_TOKEN not set")
        print("Get your token at https://replicate.com/account")
        print("Then: export REPLICATE_API_TOKEN='your-token-here'")
        sys.exit(1)

    print(f"\nGenerating: {prompt_config['name']}")
    print(f"Prompt: {prompt_config['prompt'][:100]}...")

    # Generate with Flux
    try:
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt_config["prompt"],
                "num_outputs": 1,
                "aspect_ratio": prompt_config.get("dimensions", "1:1"),
                "output_format": "png",
                "output_quality": 100,
            }
        )

        # Get the output URL
        if isinstance(output, list):
            image_url = output[0]
        else:
            image_url = output

        print(f"✓ Generated: {image_url}")

        # Download the image
        import urllib.request
        output_file = output_dir / f"{prompt_config['output_file']}_raw.png"
        urllib.request.urlretrieve(image_url, output_file)
        print(f"✓ Saved to: {output_file}")

        return output_file

    except Exception as e:
        print(f"Error generating image: {e}")
        return None


def optimize_icon(input_path, output_path, size=256):
    """Optimize icon for web (resize to square and compress)."""
    if Image is None:
        print("Skipping optimization (pillow not installed)")
        return

    try:
        img = Image.open(input_path)

        # Convert to RGBA if needed
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Resize to square
        img = img.resize((size, size), Image.Resampling.LANCZOS)

        # Save optimized
        img.save(output_path, "PNG", optimize=True)
        print(f"✓ Optimized: {output_path} ({size}x{size})")

    except Exception as e:
        print(f"Error optimizing icon: {e}")


def main():
    # Load prompts
    prompts = load_prompts()

    # Get icon configs
    icon_configs = {
        "accuracy": prompts["icon_accuracy"],
        "spatial": prompts["icon_spatial"],
        "irepa": prompts["icon_irepa"],
    }

    # Check if specific icon requested
    specific_icon = None
    for arg in sys.argv[1:]:
        if arg.startswith("--icon="):
            specific_icon = arg.split("=")[1]
        elif arg in icon_configs:
            specific_icon = arg

    # Filter configs if specific icon requested
    if specific_icon:
        if specific_icon not in icon_configs:
            print(f"Error: Unknown icon '{specific_icon}'")
            print(f"Available: {', '.join(icon_configs.keys())}")
            sys.exit(1)
        icon_configs = {specific_icon: icon_configs[specific_icon]}

    # Setup directories
    script_dir = Path(__file__).parent
    outputs_dir = script_dir / "outputs"
    outputs_dir.mkdir(exist_ok=True)

    # Generate all icons
    generated = []
    for name, config in icon_configs.items():
        print(f"\n{'='*60}")
        print(f"Processing: {name}")
        print(f"{'='*60}")

        raw_image = generate_image(config, outputs_dir)

        if raw_image and Image:
            # Optimize for web
            optimized_path = outputs_dir / f"{config['output_file']}.png"
            optimize_icon(raw_image, optimized_path, size=256)
            generated.append((name, optimized_path))

    # Summary
    print("\n" + "="*60)
    print("✓ Icon generation complete!")
    print("="*60)

    for name, path in generated:
        print(f"  {name}: {path}")

    print("\nNext steps:")
    print("1. Review the icons in assets/flux/outputs/")
    print("2. Copy to static/img/icons/:")
    print("   cp assets/flux/outputs/icon_*.png static/img/icons/")
    print("3. Update custom.css to use the icons (see docs/SETUP.md)")
    print("="*60)


if __name__ == "__main__":
    main()