# Generate Hero Image with Flux

## Quick Instructions

### 1. Get Replicate API Token
1. Go to https://replicate.com/account
2. Sign up/login
3. Copy your API token

### 2. Set Token
```bash
export REPLICATE_API_TOKEN="your-token-here"
```

### 3. Install Dependencies
```bash
cd assets/flux
pip install replicate pyyaml pillow
```

### 4. Generate Hero Image
```bash
cd assets/flux
python generate_hero.py
```

This will:
- Generate image using Flux AI
- Download to `assets/flux/outputs/hero_raw.png`
- Optimize to `assets/flux/outputs/hero.png`
- Print next steps

### 5. Copy to Static
```bash
cp assets/flux/outputs/hero.png ../../static/img/
```

### 6. View Result
```bash
cd ../..
./serve.sh
# Open http://localhost:8000
```

The hero image will appear next to the title!

## Current Prompt

The prompt generates an abstract 3D visualization showing:
- **Left**: Chaotic scattered particles (global information)
- **Right**: Organized geometric grid (spatial structure)
- **Center**: Flowing connections (alignment)
- **Style**: Deep blue to purple gradient, volumetric lighting, cinematic

## Customize Prompt

Edit `assets/flux/prompts.yaml` and change the `hero_image` prompt, then regenerate.

## Alternative: Use Web Interface

If you don't want to use Python:
1. Go to https://replicate.com/black-forest-labs/flux-schnell
2. Copy prompt from `assets/flux/prompts.yaml` (hero_image section)
3. Set aspect ratio to 16:9
4. Generate and download
5. Save as `static/img/hero.png`