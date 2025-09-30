# Quick Start Guide

## Current Status ✅

✅ Project page structure created
✅ Teaser figure from paper prominently displayed as Figure 1
✅ All paper figures copied and organized
✅ 3 Key Takeaways styled and ready
✅ Professional design based on Cambrian template

## What You See Now

1. **Header**: Title + Authors + Action buttons (placeholder links)
2. **Abstract**: Your paper's abstract
3. **🎯 Figure 1 (TEASER)**: Your main teaser-v2.png - prominently displayed with detailed caption
4. **Key Takeaways**: 3 main findings in styled boxes
5. **Sections**: Motivation, Spatial Structure Analysis, Method, Results, Conclusion
6. **Footer**: BibTeX citation

## View It Now

```bash
cd docs/project_page
./serve.sh
```

Then open: http://localhost:8000

## The Teaser Figure

**Location in page**: Right after abstract, before Key Takeaways
**File used**: `static/img/teaser-v2.png` (from your paper)
**Why here**: This is your main visual that explains the core finding - it deserves prime real estate!

The teaser includes:
- Visual comparison of spatial structure vs global information
- Your key metrics (correlation values)
- Clear demonstration that spatial structure matters more

## Optional: Add Hero Image with Flux

If you want a decorative hero image in the header (next to title):

1. See `FLUX_PROMPTS.md` for generation prompts
2. Generate using Flux: https://replicate.com/black-forest-labs/flux-schnell
3. Save as: `docs/project_page/static/img/hero-image.png`
4. Edit `index.html` line ~73, remove `style="display: none;"`

**Note**: This is optional and decorative. The teaser from your paper is already the main visual highlight.

## Before Deployment

### Must Do:
1. ✏️ Update links in `index.html`:
   - Line ~50: arXiv URL
   - Line ~56: PDF URL
   - Line ~62: Code/GitHub URL

2. 👁️ Review content matches your final paper

3. 🧪 Test locally (already done above)

### Optional:
- Generate Flux hero image (see above)
- Generate custom icons for Key Takeaways (see `FLUX_PROMPTS.md`)
- Add video demos (if you have them)

## Deploy Options

**Easiest**: GitHub Pages
```bash
# In your repo settings: Settings > Pages > Source > docs/project_page
```

**Alternative**:
- Netlify: Drag & drop `docs/project_page/` folder to https://app.netlify.com/drop
- Your own server: Upload `docs/project_page/` directory

## Files Reference

- `index.html` - Main page ⭐
- `FLUX_PROMPTS.md` - Image generation prompts
- `CHECKLIST.md` - Full deployment checklist
- `SUMMARY.md` - Complete overview
- `README.md` - Documentation

## Key Design Decisions

✅ Teaser figure is prominently displayed as Figure 1 (main highlight)
✅ Clean, professional aesthetic (based on Cambrian)
✅ Research-focused tone (no hyperbole)
✅ 3 key takeaways clearly visible
✅ All supporting figures from paper included

---

**Questions?** Check the other documentation files or test locally with `./serve.sh`!