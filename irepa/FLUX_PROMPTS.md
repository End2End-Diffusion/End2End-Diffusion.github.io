# Flux Image Generation Prompts for iREPA Project Page

## Overview
Generate professional, abstract/conceptual images for the project page header using Flux AI image generation.

---

## Header/Hero Image
**Filename:** `hero-image.png`
**Location:** `docs/project_page/static/img/hero-image.png`
**Dimensions:** 1200x600px (2:1 ratio)

### Prompt:
```
A clean, professional scientific illustration showing the concept of representation alignment in AI.
Split composition: left side shows scattered colorful points representing "global information" with low accuracy,
right side shows a structured grid pattern representing "spatial structure" with high accuracy.
Connect them with flowing lines to a central neural network node.
Use a gradient background from deep blue to purple.
Modern, minimalist design, technical aesthetic, suitable for computer vision research paper.
No text, no people.
```

### Alternative Prompt (More Abstract):
```
Abstract scientific visualization of spatial structure vs global information in AI.
Show two contrasting patterns: chaotic scattered dots (representing global information)
and organized geometric grid (representing spatial structure).
Deep blue and purple color scheme with glowing connections.
Clean, modern, technical aesthetic. High-tech illustration style.
No text, no people, minimalist composition.
```

---

## Optional: Section Icons

If you want custom icons for the 3 key takeaways instead of just numbers:

### Icon 1: Higher Accuracy ≠ Better Generation
**Filename:** `icon-accuracy-paradox.png`
**Dimensions:** 256x256px (square)

**Prompt:**
```
Minimalist icon showing a broken correlation between accuracy and performance.
Show an upward trending line that suddenly drops, or a checkmark with a question mark.
Simple geometric shapes, purple and blue gradient.
Clean, modern style suitable for research presentation. No text.
```

### Icon 2: Spatial Structure Metric
**Filename:** `icon-spatial-structure.png`
**Dimensions:** 256x256px (square)

**Prompt:**
```
Minimalist icon representing spatial structure in computer vision.
Show a grid or mesh pattern with highlighted connections between points.
Geometric, abstract design with purple and blue colors.
Clean, technical aesthetic. No text, simple and clear.
```

### Icon 3: iREPA Method
**Filename:** `icon-irepa.png`
**Dimensions:** 256x256px (square)

**Prompt:**
```
Minimalist icon showing improvement and optimization.
Ascending arrow or layered geometric shapes showing enhancement.
Purple and blue gradient, modern technical style.
Clean, abstract design suitable for scientific presentation. No text.
```

---

## How to Generate with Flux

### Option 1: Online Services
1. **Replicate.com**: https://replicate.com/black-forest-labs/flux-schnell
2. **Hugging Face**: https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell
3. **fal.ai**: https://fal.ai/models/flux/schnell

### Option 2: Local Generation (if you have GPU)
```bash
# Using Replicate API
export REPLICATE_API_TOKEN="your-token"

replicate run black-forest-labs/flux-schnell \
  --input prompt="[paste prompt here]" \
  --input num_outputs=1 \
  --input aspect_ratio="2:1" \
  --input output_format="png" \
  --input output_quality=100
```

### Option 3: Python Script
```python
import replicate

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input={
        "prompt": "[paste prompt here]",
        "num_outputs": 1,
        "aspect_ratio": "2:1",  # for hero image
        "output_format": "png",
        "output_quality": 100
    }
)
print(output)
```

---

## After Generation

1. **Download images** and place them in `docs/project_page/static/img/`

2. **Update HTML** to show the hero image:
   - Edit `index.html` line ~73
   - Change `style="display: none;"` to remove it or delete the style attribute

3. **(Optional) Replace numbered icons** with generated icons:
   - Update the CSS in `custom.css`
   - Replace `.takeaway-number` background with `background-image: url(...)`

---

## Style Guidelines

- **Color scheme**: Deep blue (#667eea) to purple (#764ba2) gradient
- **Style**: Clean, modern, minimalist, technical
- **Avoid**: Text overlays, people, faces, cluttered designs
- **Goal**: Professional, suitable for computer vision/ML research

---

## Example CSS Update (if using custom icons)

```css
.takeaway-item:nth-child(1) .takeaway-number {
    background-image: url('../img/icon-accuracy-paradox.png');
    background-size: cover;
    background-color: transparent;
}

.takeaway-item:nth-child(2) .takeaway-number {
    background-image: url('../img/icon-spatial-structure.png');
    background-size: cover;
    background-color: transparent;
}

.takeaway-item:nth-child(3) .takeaway-number {
    background-image: url('../img/icon-irepa.png');
    background-size: cover;
    background-color: transparent;
}
```

---

## Quick Commands

```bash
# After downloading images, move them:
mv ~/Downloads/hero-image.png docs/project_page/static/img/

# Verify images are in place:
ls -lh docs/project_page/static/img/*.png | grep -E "(hero|icon)"

# View the updated page:
cd docs/project_page && ./serve.sh
```