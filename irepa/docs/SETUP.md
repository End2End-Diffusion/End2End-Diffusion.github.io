# iREPA Project Page - Setup Guide

This project page is designed like a GitHub repository with scripts to generate all assets from scratch.

## Directory Structure

```
docs/project_page/
├── index.html              # Main page
├── serve.sh               # Local server
│
├── assets/                # Source materials & generation scripts
│   ├── flux/             # Flux AI image generation
│   │   ├── generate_hero.py
│   │   ├── generate_icons.py
│   │   ├── prompts.yaml
│   │   ├── requirements.txt
│   │   └── outputs/      # Generated images
│   │
│   ├── figures/          # Figure generation scripts
│   │   ├── plot_teaser.py
│   │   ├── requirements.txt
│   │   └── *.png         # Generated figures
│   │
│   ├── interactive/      # Interactive visualizations
│   │   └── data/
│   │
│   └── tables/           # Table generation
│       └── data/
│
├── static/               # Final web assets
│   ├── css/
│   ├── js/
│   ├── img/             # Processed images
│   └── webfonts/
│
├── scripts/              # Build & automation
│   ├── build.sh         # Main build script
│   ├── optimize_images.sh
│   └── deploy.sh
│
└── docs/                 # Documentation
    ├── SETUP.md         # This file
    └── FLUX_GUIDE.md
```

## Quick Start

### 1. View Existing Page

```bash
cd docs/project_page
./serve.sh
# Open http://localhost:8000
```

### 2. Build All Assets (Full Build)

```bash
# Set up Python environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Run full build
./scripts/build.sh
```

This will:
- Generate Flux images (hero, icons)
- Generate all figures from scratch
- Optimize images for web
- Copy everything to `static/`

### 3. Partial Builds

```bash
# Only generate Flux images
./scripts/build.sh --only-flux

# Only generate figures
./scripts/build.sh --only-figures

# Skip Flux (if no API token)
./scripts/build.sh --skip-flux
```

## Detailed Setup

### A. Flux Image Generation

Generate AI-powered images for hero and icons.

**Requirements:**
```bash
cd assets/flux
pip install -r requirements.txt
```

**Get API Token:**
1. Sign up at https://replicate.com
2. Get token from https://replicate.com/account
3. Set environment variable:
   ```bash
   export REPLICATE_API_TOKEN="your-token-here"
   ```

**Generate:**
```bash
# Hero image
cd assets/flux
python generate_hero.py

# Icons
python generate_icons.py

# Specific icon only
python generate_icons.py --icon=accuracy
```

**Copy to static:**
```bash
cp assets/flux/outputs/hero.png static/img/
cp assets/flux/outputs/icon_*.png static/img/icons/
```

### B. Figure Generation

Generate figures from data/scripts.

**Requirements:**
```bash
cd assets/figures
pip install -r requirements.txt
```

**Generate:**
```bash
cd assets/figures
python plot_teaser.py
```

**Customize:**
Edit `plot_teaser.py` to:
- Replace example data with actual experimental results
- Adjust dimensions, colors, labels
- Add/remove subplots

**Copy to static:**
```bash
cp assets/figures/*.png static/img/
```

### C. Image Optimization

Compress and optimize images for web.

**Install tools (optional):**
```bash
# Ubuntu/Debian
sudo apt-get install optipng pngquant

# macOS
brew install optipng pngquant
```

**Run:**
```bash
./scripts/optimize_images.sh
```

This is automatically called by `build.sh`.

## Customization

### Update Hero Image

1. Edit prompt in `assets/flux/prompts.yaml`
2. Regenerate: `python assets/flux/generate_hero.py`
3. Copy: `cp assets/flux/outputs/hero.png static/img/`
4. Enable in HTML: Edit `index.html` line ~73, remove `style="display: none;"`

### Update Teaser Figure

1. Edit `assets/figures/plot_teaser.py`
2. Replace example data with actual results
3. Regenerate: `python assets/figures/plot_teaser.py`
4. Copy: `cp assets/figures/teaser.png static/img/`
5. HTML already uses `static/img/teaser-v2.png`, rename or update path

### Add New Figures

1. Create script: `assets/figures/plot_newgfig.py`
2. Generate: `python assets/figures/plot_newfig.py`
3. Copy: `cp assets/figures/newfig.png static/img/`
4. Add to HTML: `<img src="static/img/newfig.png">`

### Update Content

Edit `index.html` directly:
- Line ~50-62: Update links (arXiv, PDF, Code)
- Line ~81-88: Update author links
- Line ~102-112: Update abstract
- Sections: Update text and figures as needed

## Deployment

### GitHub Pages

1. Commit all changes:
   ```bash
   git add docs/project_page
   git commit -m "Update project page"
   git push
   ```

2. Enable GitHub Pages:
   - Go to: Repository Settings → Pages
   - Source: Deploy from branch
   - Branch: `main`, folder: `/docs/project_page`
   - Save

3. Access at: `https://username.github.io/repo-name/`

### Manual Deploy

Upload entire `docs/project_page/` directory to your server.

## Troubleshooting

### Flux API Errors

**Issue:** "REPLICATE_API_TOKEN not set"
**Fix:** Export your API token (see section A above)

**Issue:** "Rate limit exceeded"
**Fix:** Wait and try again, or upgrade Replicate plan

### Image Not Loading

**Issue:** Images show as broken in browser
**Fix:**
1. Check file exists: `ls static/img/filename.png`
2. Check HTML path matches filename
3. Hard refresh browser (Ctrl+Shift+R / Cmd+Shift+R)

### Build Failures

**Issue:** Python module not found
**Fix:** Install requirements:
```bash
cd assets/flux && pip install -r requirements.txt
cd ../figures && pip install -r requirements.txt
```

**Issue:** Permission denied on scripts
**Fix:** Make executable:
```bash
chmod +x scripts/*.sh
chmod +x assets/**/*.py
```

## Development Workflow

1. **Edit content:** Modify HTML, CSS, or add new sections
2. **Update assets:** Regenerate figures/images as needed
3. **Test locally:** `./serve.sh` and view at localhost:8000
4. **Optimize:** `./scripts/optimize_images.sh`
5. **Deploy:** Commit and push, or upload to server

## Next Steps

- See `FLUX_GUIDE.md` for detailed Flux usage
- See `../CHECKLIST.md` for deployment checklist
- See `../README.md` for general documentation