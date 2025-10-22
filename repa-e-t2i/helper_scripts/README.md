# VAE Reconstruction Comparison Tool

## Overview
This tool generates an original image using FLUX.1-dev OR loads an existing local image, and compares reconstructions across all 6 end-to-end tuned VAEs from the REPA-E-T2I project.

## Installation

```bash
pip install diffusers>=0.35.0 torch>=2.5.0 pillow matplotlib numpy
```

## Usage

### Option 1: Generate with FLUX.1-dev (text-to-image)
```bash
# Basic usage
python vae_reconstruction_comparison.py "Your prompt here"

# Example
python vae_reconstruction_comparison.py "A hawksbill turtle over coral"

# With custom resolution
python vae_reconstruction_comparison.py "Elephant seals on a beach" --resolution 1024
```

### Option 2: Load existing image (local path)
```bash
# From local file
python vae_reconstruction_comparison.py --image path/to/image.jpg

# With custom resolution
python vae_reconstruction_comparison.py --image input.jpg --resolution 1024
```

### Additional Options
```bash
# Specify output directory
python vae_reconstruction_comparison.py "Prompt" --output-dir custom_outputs

# Use CPU instead of GPU
python vae_reconstruction_comparison.py --image photo.jpg --device cpu
```

## Output Files

All outputs are saved to `reconstruction_outputs/` (or custom directory):

1. **`{prompt}_comparison.png`** - Main horizontal comparison figure
   - All 7 images in one row
   - Clean, professional styling matching project page
   - Light gray background (#f5f5f5)
   - Simple black text labels

2. **`{prompt}_grid.png`** - Alternative vertical grid layout
   - 7 rows, 1 column
   - Useful for presentations or detailed viewing

3. **`{prompt}_original.png`** - Original FLUX.1-dev generated image

4. **Individual reconstructions**:
   - `{prompt}_E2E-FLUX-VAE.png`
   - `{prompt}_E2E-SD3.5-VAE.png`
   - `{prompt}_E2E-Qwen-VAE.png`
   - `{prompt}_E2E-SD-VAE.png`
   - `{prompt}_E2E-VA-VAE.png`
   - `{prompt}_E2E-INVAE.png`

## VAEs Tested

1. **E2E-FLUX-VAE** (`REPA-E/e2e-flux-vae`) - 1024px
2. **E2E-SD3.5-VAE** (`REPA-E/e2e-sd3.5-vae`) - 1024px
3. **E2E-Qwen-VAE** (`REPA-E/e2e-qwenimage-vae`) - 1024px
4. **E2E-SD-VAE** (`REPA-E/e2e-sdvae-hf`) - 512px
5. **E2E-VA-VAE** (`REPA-E/e2e-vavae-hf`) - 512px
6. **E2E-INVAE** (`REPA-E/e2e-invae-hf`) - 512px

## Design Features

The output figures match the REPA-E-T2I project page aesthetics:
- Clean horizontal layout (all 7 images in one row)
- Light gray background (#f5f5f5)
- Serif fonts (Times New Roman / DejaVu Serif)
- Black text labels (#333333)
- No prompt display (reconstruction focus)
- Professional, publication-ready quality (300 DPI)

## Customizing Appearance

You can easily customize the figure appearance by editing the global configuration variables at the top of `vae_reconstruction_comparison.py`:

```python
# ============================================================================
# CONFIGURATION - Adjust these to control figure appearance
# ============================================================================

# Font configuration (matching convergence-analysis.py)
LABEL_FONT_SIZE = 14        # Size for VAE labels (e.g., "E2E-FLUX-VAE")
FIGURE_WIDTH = 24           # Figure width in inches
FIGURE_HEIGHT = 4.5         # Figure height in inches
```

**Examples:**
- For smaller labels: Set `LABEL_FONT_SIZE = 12`
- For larger labels: Set `LABEL_FONT_SIZE = 16`
- For wider figure: Set `FIGURE_WIDTH = 28`
- For taller figure: Set `FIGURE_HEIGHT = 5.5`

## Requirements

- CUDA-capable GPU (recommended)
- ~16GB VRAM for optimal performance
- Internet connection (for downloading models on first run)

## Example Commands

```bash
# Test with project page prompts
python vae_reconstruction_comparison.py "A hawksbill turtle over coral"
python vae_reconstruction_comparison.py "Elephant seals lounging on a California beach"
python vae_reconstruction_comparison.py "Bioluminescent bay in Puerto Rico"
python vae_reconstruction_comparison.py "Eureka lemons with leaves attached"
```

## Notes

- Models are downloaded on first run (may take time)
- Each VAE is loaded sequentially to manage memory
- GPU memory is cleared between VAE loads
- Images are automatically resized to each VAE's preferred resolution
