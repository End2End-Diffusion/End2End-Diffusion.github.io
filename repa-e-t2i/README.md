# REPA-E-T2I Project Page

Professional project page for **REPA-E-T2I: Family of end-to-end tuned VAEs for supercharging T2I diffusion transformers**.

Built on the REPA-E framework by Xingjian Leng, Jaskirat Singh, and collaborators.

## Quick Start

### View Locally

```bash
cd docs/project_page
./serve.sh
# Open http://localhost:8000 in your browser
```

### Project Structure

```
project_page/
├── index.html              # Main HTML page
├── serve.sh               # Local preview server
├── README.md              # This file
│
├── static/
│   ├── css/               # Stylesheets
│   │   ├── style.css     # Base styles (from iREPA template)
│   │   ├── custom.css    # Custom overrides
│   │   └── fontawesome.all.min.css
│   │
│   ├── js/                # JavaScript files
│   │   ├── distill_template.v2.js
│   │   ├── medium-zoom.min.js
│   │   ├── zoom.js
│   │   └── hider.js
│   │
│   ├── img/               # All figures and images
│   │   ├── icons/        # SVG icons for sections
│   │   ├── convergence/  # Training convergence plots
│   │   ├── benchmarks/   # Benchmark comparison charts
│   │   ├── qualitative/  # Qualitative comparison samples
│   │   └── latent_viz/   # PCA and similarity visualizations
│   │
│   └── webfonts/         # Font files
```

## Content Sections

### 1. Hero Header
- Project title and subtitle
- Key highlights with icons:
  - Better T2I Performance
  - Superior Generation Quality
  - ImageNet Generalization
- Author list with affiliations
- Links: arXiv (REPA-E), Code, Models

### 2. Quantitative Results
- **Training Convergence at 100K Steps**: Comparison across 5 benchmarks
- **Extended Training (500K Steps)**: Full dataset results
- **High-Resolution Training (512px, 200K Steps)**: Resolution scaling
- **Benchmark Comparisons**: FLUX-VAE, Qwen-Image-VAE, SD3.5-VAE

### 3. Qualitative Comparison
- Side-by-side image gallery
- 30 selected samples from 227 available
- FLUX-VAE baseline vs REPA-E-T2I
- Interactive zoom on click

### 4. Latent Space Analysis
- **PCA Projections**: Visualizing latent structure
- **Spatial Self-Similarity**: Cosine similarity heatmaps
- Comparison across different VAE architectures

### 5. ImageNet Generalization
- Classification accuracy
- Reconstruction quality
- Transfer to downstream tasks

### 6. Conclusion & BibTeX
- Summary of contributions
- Citation for REPA-E paper

## Features

### Design Elements
- **Clean, Professional Layout**: Based on iREPA template
- **Responsive Design**: Works on desktop and mobile
- **Interactive Elements**:
  - Jump-to-section navigation
  - Image zoom (medium-zoom)
  - Smooth scrolling
  - Copy BibTeX button

### Typography & Colors
- **Fonts**: Charter for body text, clean sans-serif for headers
- **Color Scheme**: Professional gradient header, clean white content
- **Accessibility**: High contrast, readable font sizes

## Figures Included

### Convergence Plots (3 files)
- `3b-t2i-convergence-100k-combined.png` (100K steps)
- `3b-t2i-convergence-fulldata-500k-combined.png` (500K steps)
- `3b-t2i-convergence-fulldata-resume-res512-200k-combined.png` (200K steps at 512px)

### Benchmark Comparisons (15 files)
- FLUX-VAE: COCO30k, DPG-Bench, GenAI-Bench, GenEval, MJHQ30k
- Qwen-Image-VAE: Same 5 benchmarks
- SD3.5-VAE: Same 5 benchmarks

### Qualitative Samples (30 files)
- Selected from 227 available samples
- Best examples for visual comparison

### Latent Visualizations (~75 files)
- PCA projections for different VAEs and datasets
- Cosine similarity heatmaps
- Comparison across FLUX, Qwen, SD3.5 architectures

## Customization

### Update Content
Edit `index.html` directly to modify text, add sections, or change layout.

### Add More Images
1. Place images in appropriate `static/img/` subdirectory
2. Reference in HTML: `<img src="static/img/subdirectory/image.png">`

### Change Colors
Modify `static/css/custom.css` for styling overrides.

### Update Links
- arXiv: Update href in button container
- Code: Point to your repository
- Models: Point to HuggingFace collection

## Deployment Options

### Option 1: GitHub Pages
```bash
# Commit and push
git add docs/project_page
git commit -m "Add REPA-E-T2I project page"
git push

# Enable in: Settings → Pages → Source: /docs/project_page
```

### Option 2: Netlify/Vercel
Drag and drop `docs/project_page/` folder to hosting dashboard.

### Option 3: Custom Server
Upload entire directory to your server via FTP/rsync.

## Technical Notes

### Dependencies
- **Python 3**: For local server (serve.sh)
- **Modern Browser**: Chrome, Firefox, Safari, Edge

### Image Optimization (Optional)
To reduce page load time, you can optimize images:
```bash
# Using optipng
find static/img -name "*.png" -exec optipng -o7 {} \;

# Or using pngquant
find static/img -name "*.png" -exec pngquant --force --ext .png {} \;
```

### Browser Compatibility
- Tested on: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Features: CSS Grid, Flexbox, ES6 JavaScript
- Fallbacks: Included for older browsers where possible

## Credits

- **Template**: Based on [iREPA project page](https://end2end-diffusion.github.io/irepa)
- **Design Inspiration**: Cambrian-1, Distill.pub
- **Icons**: FontAwesome, custom SVGs
- **Fonts**: Charter, system fonts
- **Image Zoom**: medium-zoom library

## Citation

```bibtex
@article{leng2025repae,
  title={REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers},
  author={Leng, Xingjian and Singh, Jaskirat and Hou, Yunzhong and Xing, Zhenchang and Xie, Saining and Zheng, Liang},
  journal={arXiv preprint arXiv:2504.10483},
  year={2025}
}
```

## License

Project page code: MIT License (inherited from template)
Paper content: See paper for details

---

**Authors**: Xingjian Leng, Jaskirat Singh, Yunzhong Hou, Zhenchang Xing, Saining Xie, Liang Zheng

**Affiliations**: Australian National University, Adobe Research, New York University
