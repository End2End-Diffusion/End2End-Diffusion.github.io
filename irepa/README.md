# iREPA Project Page

Professional project page for the paper:
**"What matters for Representation Alignment: Global Information or Spatial Structure?"**

🔗 [arXiv](#) | 📄 [PDF](#) | 💻 [Code](#)

## Overview

This is a complete project page repository with:
- ✅ Professional, clean design (based on Cambrian template)
- ✅ Source code to regenerate all assets
- ✅ Flux AI image generation scripts
- ✅ Figure generation from data
- ✅ Build automation
- ✅ Optimized for web display

Think of this as a GitHub repo for your project page - not just static files!

## Quick Start

### View Locally

```bash
./serve.sh
# Open http://localhost:8000
```

### Build All Assets

```bash
# Full build (requires Python & API tokens)
./scripts/build.sh

# Skip Flux generation (no API token needed)
./scripts/build.sh --skip-flux

# Only generate figures
./scripts/build.sh --only-figures
```

## Key Features

### 🎯 3 Prominent Key Takeaways
1. Higher validation accuracy ≠ better generation
2. Spatial structure drives performance (SSM: |r| = 0.852)
3. iREPA improves convergence (<4 lines of code)

### 📊 Asset Generation
- **Flux AI Images**: Hero image & custom icons
- **Figures**: Regenerated from scripts with proper formatting
- **Interactive**: D3.js visualizations (planned)
- **Optimization**: Automated image compression

### 🛠️ Reproducible Build System
```bash
scripts/
├── build.sh              # Generate everything
├── optimize_images.sh    # Compress images
└── deploy.sh             # Deploy to hosting
```

## Project Structure

```
project_page/
├── index.html              # Main page
├── serve.sh               # Local server
│
├── assets/                # Source & generation scripts
│   ├── flux/             # AI image generation
│   ├── figures/          # Plot generation
│   ├── interactive/      # D3.js visualizations
│   └── tables/           # Table generation
│
├── static/               # Final web assets
│   ├── css/
│   ├── js/
│   └── img/
│
├── scripts/              # Build automation
│   ├── build.sh
│   ├── optimize_images.sh
│   └── deploy.sh
│
└── docs/                 # Documentation
    ├── SETUP.md          # Detailed setup guide
    └── FLUX_GUIDE.md     # Flux image generation
```

## Documentation

📖 **Detailed Guides:**
- [SETUP.md](docs/SETUP.md) - Complete setup and build instructions
- [FLUX_GUIDE.md](FLUX_PROMPTS.md) - Flux AI image generation
- [QUICK_START.md](QUICK_START.md) - Fast reference
- [CHECKLIST.md](CHECKLIST.md) - Deployment checklist

## Customization

### Update Content
Edit `index.html` directly - update text, links, sections.

### Regenerate Teaser
```bash
cd assets/figures
# Edit plot_teaser.py with your data
python plot_teaser.py
cp teaser.png ../../static/img/
```

### Generate Hero Image
```bash
export REPLICATE_API_TOKEN="your-token"
cd assets/flux
python generate_hero.py
cp outputs/hero.png ../../static/img/
```

### Add New Figures
1. Create `assets/figures/plot_newfig.py`
2. Generate: `python plot_newfig.py`
3. Copy: `cp newfig.png ../../static/img/`
4. Add to HTML

## Deployment

### Option 1: GitHub Pages
```bash
git add . && git commit -m "Update project page"
git push
# Enable in: Settings → Pages → Source: /docs/project_page
```

### Option 2: Netlify/Vercel
Drag and drop `docs/project_page/` folder to hosting dashboard.

### Option 3: Custom Server
Upload entire directory to your server via FTP/rsync.

## Key Design Decisions

✅ **Repository-style**: Complete source code, not just static files
✅ **Reproducible**: All assets can be regenerated from scripts
✅ **Professional**: Clean design, research-focused tone
✅ **Optimized**: Automated image compression and formatting
✅ **Flexible**: Easy to customize and extend

## Before Publishing

- [ ] Update links in `index.html` (arXiv, PDF, Code)
- [ ] Generate/update hero image (optional)
- [ ] Regenerate figures with actual data
- [ ] Test locally: `./serve.sh`
- [ ] Optimize images: `./scripts/optimize_images.sh`
- [ ] Deploy to hosting

## Requirements

**Minimal (view only):**
- Python 3 (for local server)

**For building:**
- Python 3.8+
- Replicate API token (for Flux images)
- pip packages (see `assets/*/requirements.txt`)

**For optimization (optional):**
- optipng or pngquant

## Credits

- Template based on [Cambrian-1](https://github.com/cambrian-mllm/cambrian-mllm.github.io)
- Flux AI via [Replicate](https://replicate.com/black-forest-labs/flux-schnell)
- Icons from FontAwesome & Academicons

## License

Project page code: MIT License
Paper content: See paper for details

---

**Authors:** Jaskirat Singh¹'², Xingjian Leng², Zongze Wu¹, Liang Zheng², Richard Zhang¹, Eli Shechtman¹, Saining Xie³

¹Adobe Research | ²ANU | ³New York University