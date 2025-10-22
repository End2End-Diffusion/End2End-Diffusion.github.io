"""
VAE Reconstruction Comparison Script
=====================================
This script generates an original image using FLUX.1 OR loads a local image,
and tests reconstruction across all 6 end-to-end tuned VAEs from the REPA-E-T2I project.

Usage:
    python vae_reconstruction_comparison.py "Your prompt here"
    python vae_reconstruction_comparison.py --image path/to/image.jpg

Examples:
    python vae_reconstruction_comparison.py "A hawksbill turtle over coral"
    python vae_reconstruction_comparison.py --image input.jpg
"""

import argparse
import os
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

import torch
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib as mpl

from diffusers import FluxPipeline, AutoencoderKL, AutoencoderKLQwenImage


# ============================================================================
# CONFIGURATION - Adjust these to control figure appearance
# ============================================================================

# Font configuration (matching convergence-analysis.py)
LABEL_FONT_SIZE = 19      # Size for VAE labels (e.g., "E2E-FLUX-VAE")
FIGURE_WIDTH = 24           # Figure width in inches
FIGURE_HEIGHT = 4.5         # Figure height in inches

# Configure matplotlib for professional plots
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['axes.linewidth'] = 1.0
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 11
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['savefig.dpi'] = 300

# ============================================================================


# VAE configurations
VAE_CONFIGS = [
    {
        'name': 'E2E-FLUX-VAE',
        'model_id': 'REPA-E/e2e-flux-vae',
        'class': AutoencoderKL,
        'resolution': 1024,
        'requires_frame_dim': False
    },
    {
        'name': 'E2E-SD3.5-VAE',
        'model_id': 'REPA-E/e2e-sd3.5-vae',
        'class': AutoencoderKL,
        'resolution': 1024,
        'requires_frame_dim': False
    },
    {
        'name': 'E2E-Qwen-VAE',
        'model_id': 'REPA-E/e2e-qwenimage-vae',
        'class': AutoencoderKLQwenImage,
        'resolution': 1024,
        'requires_frame_dim': True
    },
    {
        'name': 'E2E-SD-VAE',
        'model_id': 'REPA-E/e2e-sdvae-hf',
        'class': AutoencoderKL,
        'resolution': 512,
        'requires_frame_dim': False
    },
    {
        'name': 'E2E-VA-VAE',
        'model_id': 'REPA-E/e2e-vavae-hf',
        'class': AutoencoderKL,
        'resolution': 512,
        'requires_frame_dim': False
    },
    {
        'name': 'E2E-INVAE',
        'model_id': 'REPA-E/e2e-invae-hf',
        'class': AutoencoderKL,
        'resolution': 512,
        'requires_frame_dim': False
    },
]


def load_image_from_path(image_path, output_path, resolution=1024):
    """Load an image from local path"""
    print(f"\n{'='*60}")
    print(f"Loading image from: {image_path}")
    print(f"{'='*60}\n")

    try:
        # Local file path
        print(f"Loading from local path...")
        image = Image.open(image_path).convert('RGB')
        print(f"✓ Image loaded successfully")

        # Resize to target resolution
        print(f"Resizing to {resolution}x{resolution}...")
        image = image.resize((resolution, resolution), Image.LANCZOS)

        # Save
        image.save(output_path)
        print(f"✓ Original image saved to: {output_path}")

        return image

    except Exception as e:
        print(f"✗ Error loading image: {e}")
        raise


def generate_image_with_flux(prompt, output_path, resolution=1024, device='cuda'):
    """Generate an image using FLUX.1-dev"""
    print(f"\n{'='*60}")
    print(f"Generating original image with FLUX.1-dev...")
    print(f"Prompt: {prompt}")
    print(f"{'='*60}\n")

    # Load FLUX pipeline
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev",
        torch_dtype=torch.bfloat16
    )
    pipe = pipe.to(device)

    # Generate image
    image = pipe(
        prompt,
        height=resolution,
        width=resolution,
        num_inference_steps=28,
        guidance_scale=3.5,
    ).images[0]

    # Save original
    image.save(output_path)
    print(f"✓ Original image saved to: {output_path}")

    # Clean up
    del pipe
    torch.cuda.empty_cache()

    return image


def reconstruct_with_vae(image, vae_config, device='cuda'):
    """Reconstruct image using a specific VAE"""
    print(f"\nProcessing {vae_config['name']}...")

    # Resize image if needed
    target_res = vae_config['resolution']
    if image.size != (target_res, target_res):
        resized_image = image.resize((target_res, target_res), Image.LANCZOS)
    else:
        resized_image = image

    # Convert to tensor
    image_tensor = torch.from_numpy(
        np.array(resized_image)
    ).permute(2, 0, 1).unsqueeze(0).to(torch.float32) / 127.5 - 1
    image_tensor = image_tensor.to(device)

    # Load VAE
    vae = vae_config['class'].from_pretrained(
        vae_config['model_id'],
        torch_dtype=torch.float32
    ).to(device)

    # Add frame dimension for Qwen-Image VAE
    if vae_config['requires_frame_dim']:
        image_tensor = image_tensor.unsqueeze(2)

    # Encode and decode
    with torch.no_grad():
        latents = vae.encode(image_tensor).latent_dist.sample()
        reconstructed = vae.decode(latents).sample

    # Remove frame dimension if needed
    if vae_config['requires_frame_dim']:
        reconstructed = reconstructed.squeeze(2)

    # Convert back to image
    reconstructed = (reconstructed.squeeze(0).permute(1, 2, 0).cpu().numpy() + 1) * 127.5
    reconstructed = np.clip(reconstructed, 0, 255).astype(np.uint8)
    reconstructed_image = Image.fromarray(reconstructed)

    print(f"✓ {vae_config['name']} reconstruction complete")

    # Clean up
    del vae
    torch.cuda.empty_cache()

    return reconstructed_image


def create_comparison_figure(original_image, reconstructions, vae_configs, prompt, output_path):
    """Create a professional comparison figure in the style of the project page"""
    print(f"\n{'='*60}")
    print(f"Creating comparison figure...")
    print(f"{'='*60}\n")

    # Single row layout - 7 images total
    n_cols = 7
    n_rows = 1

    # Create figure with specific styling (using global config)
    fig = plt.figure(figsize=(FIGURE_WIDTH, FIGURE_HEIGHT), facecolor='#f5f5f5')

    # Adjust layout for tight, clean spacing
    plt.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.05, wspace=0.08)

    # Font settings (using global config - serif fonts from matplotlib rcParams)
    title_font = {'size': LABEL_FONT_SIZE, 'weight': 'normal'}

    # Plot original image
    ax = plt.subplot(n_rows, n_cols, 1)
    ax.imshow(original_image)
    ax.set_title('Original Image', fontdict=title_font, color='#333333', pad=8)
    ax.axis('off')

    # Plot reconstructions
    for idx, (recon_img, vae_config) in enumerate(zip(reconstructions, vae_configs)):
        ax = plt.subplot(n_rows, n_cols, idx + 2)

        # Resize if needed for display
        if recon_img.size != original_image.size:
            display_img = recon_img.resize(original_image.size, Image.LANCZOS)
        else:
            display_img = recon_img

        ax.imshow(display_img)

        # Simple title - no color, just black text
        ax.set_title(vae_config['name'], fontdict=title_font, color='#333333', pad=8)
        ax.axis('off')

    # Save figure
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#f5f5f5', edgecolor='none')
    plt.close()

    print(f"✓ Comparison figure saved to: {output_path}")


def create_grid_comparison(original_image, reconstructions, vae_configs, prompt, output_path):
    """Create a clean grid comparison (alternative vertical layout)"""
    print(f"Creating vertical grid comparison figure...")

    # Vertical grid: 7 rows, 1 column
    n_images = len(reconstructions) + 1  # +1 for original
    target_size = (800, 800)

    # Create grid image with light gray background
    padding = 20
    label_height = 50
    grid_width = target_size[0] + 2 * padding
    grid_height = (target_size[1] + label_height) * n_images + padding

    grid_img = Image.new('RGB', (grid_width, grid_height), color='#f5f5f5')
    draw = ImageDraw.Draw(grid_img)

    # Try to load a nice font
    try:
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        label_font = ImageFont.load_default()

    # Add images to grid
    all_images = [original_image] + reconstructions
    all_labels = ['Original Image'] + [cfg['name'] for cfg in vae_configs]

    for idx, (img, label) in enumerate(zip(all_images, all_labels)):
        # Resize image
        resized = img.resize(target_size, Image.LANCZOS)

        # Calculate position
        x = padding
        y = idx * (target_size[1] + label_height) + padding

        # Add label above image
        bbox = draw.textbbox((0, 0), label, font=label_font)
        text_width = bbox[2] - bbox[0]
        text_x = x + (target_size[0] - text_width) // 2
        text_y = y + 5

        draw.text((text_x, text_y), label, fill='#333333', font=label_font)

        # Paste image
        grid_img.paste(resized, (x, y + label_height - 10))

    # Save
    grid_img.save(output_path, quality=95)
    print(f"✓ Vertical grid comparison saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate and compare VAE reconstructions across all REPA-E-T2I VAEs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python vae_reconstruction_comparison.py "A hawksbill turtle over coral"
  python vae_reconstruction_comparison.py --image input.jpg
        """
    )
    parser.add_argument('prompt', type=str, nargs='?', default=None,
                       help='Text prompt for image generation (or use --image instead)')
    parser.add_argument('--image', type=str, default=None,
                       help='Path to local image (instead of generating with FLUX)')
    parser.add_argument('--resolution', type=int, default=1024,
                       help='Resolution for images (default: 1024)')
    parser.add_argument('--device', type=str, default='cuda',
                       help='Device to use (default: cuda)')
    parser.add_argument('--output-dir', type=str, default='helper_scripts/reconstruction_outputs',
                       help='Output directory for results')

    args = parser.parse_args()

    # Validate input
    if args.prompt is None and args.image is None:
        parser.error("Either provide a prompt or use --image to specify an image path/URL")

    if args.prompt and args.image:
        parser.error("Cannot use both prompt and --image. Choose one.")

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create filename-safe name
    if args.image:
        # Extract filename from local path
        safe_name = Path(args.image).stem
        safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in safe_name)
        safe_name = '_'.join(safe_name.split())[:50]
    else:
        safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in args.prompt)
        safe_name = '_'.join(safe_name.split())[:50]

    # Check device
    if args.device == 'cuda' and not torch.cuda.is_available():
        print("Warning: CUDA not available, using CPU")
        args.device = 'cpu'

    print(f"\n{'='*60}")
    print(f"VAE Reconstruction Comparison Tool")
    print(f"{'='*60}")
    if args.image:
        print(f"Image: {args.image}")
    else:
        print(f"Prompt: {args.prompt}")
    print(f"Device: {args.device}")
    print(f"Output: {output_dir}")
    print(f"{'='*60}\n")

    # Step 1: Get original image (generate or load)
    original_path = output_dir / f"{safe_name}_original.png"
    if args.image:
        original_image = load_image_from_path(
            args.image,
            original_path,
            resolution=args.resolution
        )
        display_prompt = f"Image: {args.image}"
    else:
        original_image = generate_image_with_flux(
            args.prompt,
            original_path,
            resolution=args.resolution,
            device=args.device
        )
        display_prompt = args.prompt

    # Step 2: Reconstruct with each VAE
    reconstructions = []
    for vae_config in VAE_CONFIGS:
        try:
            recon = reconstruct_with_vae(original_image, vae_config, device=args.device)
            reconstructions.append(recon)

            # Save individual reconstruction
            recon_path = output_dir / f"{safe_name}_{vae_config['name']}.png"
            recon.save(recon_path)

        except Exception as e:
            print(f"✗ Error with {vae_config['name']}: {e}")
            # Create placeholder
            reconstructions.append(Image.new('RGB', original_image.size, color='gray'))

    # Step 3: Create comparison figures
    comparison_path = output_dir / f"{safe_name}_comparison.png"
    create_comparison_figure(
        original_image,
        reconstructions,
        VAE_CONFIGS,
        display_prompt,
        comparison_path
    )

    grid_path = output_dir / f"{safe_name}_grid.png"
    create_grid_comparison(
        original_image,
        reconstructions,
        VAE_CONFIGS,
        display_prompt,
        grid_path
    )

    print(f"\n{'='*60}")
    print(f"✓ All done! Results saved to: {output_dir}")
    print(f"{'='*60}\n")
    print(f"Generated files:")
    print(f"  • Original image: {original_path.name}")
    print(f"  • Comparison figure: {comparison_path.name}")
    print(f"  • Grid comparison: {grid_path.name}")
    print(f"  • Individual reconstructions: {len(reconstructions)} files")
    print()


if __name__ == '__main__':
    main()
