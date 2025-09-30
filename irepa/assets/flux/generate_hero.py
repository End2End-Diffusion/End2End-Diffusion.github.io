#!/usr/bin/env python3
"""
Generate hero image for iREPA project page using Flux AI.

Usage:
    python generate_hero.py [--alt]  # Use alternative prompt

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
    print("Install with: pip install pillow")
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

    print(f"Generating: {prompt_config['name']}")
    print(f"Prompt: {prompt_config['prompt'][:100]}...")

    # Generate with Flux
    try:
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt_config["prompt"],
                "num_outputs": 1,
                "aspect_ratio": prompt_config.get("dimensions", "16:9"),
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


def optimize_image(input_path, output_path, max_width=1920):
    """Optimize image for web (resize and compress)."""
    if Image is None:
        print("Skipping optimization (pillow not installed)")
        return

    try:
        img = Image.open(input_path)

        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Save optimized
        img.save(output_path, "PNG", optimize=True, quality=95)
        print(f"✓ Optimized: {output_path}")

    except Exception as e:
        print(f"Error optimizing image: {e}")


def main():
    # Parse args
    use_alt = "--alt" in sys.argv

    # Load prompts
    prompts = load_prompts()

    # Select prompt
    if use_alt:
        prompt_config = prompts["hero_image_alt"]
    else:
        prompt_config = prompts["hero_image"]

    # Setup directories
    script_dir = Path(__file__).parent
    outputs_dir = script_dir / "outputs"
    outputs_dir.mkdir(exist_ok=True)

    # Generate
    raw_image = generate_image(prompt_config, outputs_dir)

    if raw_image and Image:
        # Optimize for web
        optimized_path = outputs_dir / f"{prompt_config['output_file']}.png"
        optimize_image(raw_image, optimized_path, max_width=1920)

        print("\n" + "="*60)
        print("✓ Hero image generation complete!")
        print(f"Raw: {raw_image}")
        print(f"Optimized: {optimized_path}")
        print("\nNext steps:")
        print(f"1. Review the image: open {optimized_path}")
        print("2. Copy to static: cp {} ../../static/img/hero.png".format(optimized_path))
        print("3. Update index.html to show the hero image")
        print("="*60)


if __name__ == "__main__":
    main()