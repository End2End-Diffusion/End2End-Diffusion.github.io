# Project Page Deployment Checklist

## Pre-Deployment Tasks

### Content Review
- [ ] Verify abstract matches final paper version
- [ ] Check all 3 key takeaways are accurate
- [ ] Confirm all section content aligns with paper
- [ ] Review figure captions for accuracy
- [ ] Verify BibTeX citation is correct

### Links to Update in `index.html`
- [ ] Line 52: Replace `#` with arXiv URL
- [ ] Line 57: Replace `#` with PDF URL
- [ ] Line 62: Replace `#` with GitHub Code URL
- [ ] Lines 92-100: Update author personal page links (optional)

### Testing
- [ ] View page locally using `./serve.sh`
- [ ] Check all images load correctly
- [ ] Test zoom functionality on figures
- [ ] Verify responsive design on mobile (resize browser)
- [ ] Test on Chrome
- [ ] Test on Firefox
- [ ] Test on Safari (if available)
- [ ] Check all internal anchor links work

### Visual Check
- [ ] Header displays correctly
- [ ] Key takeaways section is prominent and styled well
- [ ] All figures are visible and properly sized
- [ ] Button links look correct (even if placeholder)
- [ ] Footer and BibTeX section render properly
- [ ] Page loads without console errors (check browser DevTools)

## Deployment

### Hosting Options

**Option 1: GitHub Pages**
```bash
# If your repo is already on GitHub:
# 1. Go to repository Settings > Pages
# 2. Select branch and /docs/project_page as source
# 3. Page will be available at: https://username.github.io/repo-name/
```

**Option 2: Manual Upload**
```bash
# Upload entire docs/project_page/ directory to your server
# Make sure to preserve directory structure
# Ensure web server can serve static files (HTML, CSS, JS, images)
```

**Option 3: Netlify/Vercel**
```bash
# Drag and drop docs/project_page/ folder to:
# - Netlify: https://app.netlify.com/drop
# - Vercel: https://vercel.com/new
```

## Post-Deployment

- [ ] Visit live URL and verify everything works
- [ ] Update paper with project page URL
- [ ] Update README.md with live URL
- [ ] Share link with co-authors for review
- [ ] Add project page link to arXiv submission (if not already)
- [ ] Tweet/share project page link (optional)

## Maintenance

### When Paper is Updated
- [ ] Update abstract in index.html if changed
- [ ] Update figures if new versions available
- [ ] Update BibTeX if publication venue changes
- [ ] Regenerate and re-upload

### Common Updates
- [ ] Add video demos (if created later)
- [ ] Add slides link (after conference talk)
- [ ] Add code release link (when ready)
- [ ] Add model checkpoints link (if applicable)

## Troubleshooting

### Images Not Loading
- Check file paths are relative: `static/img/filename.png`
- Verify images exist in static/img/ directory
- Check file extensions match (case-sensitive on some servers)

### Styling Issues
- Ensure custom.css is loaded after style.css
- Check browser console for CSS loading errors
- Try hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

### JavaScript Errors
- Check browser console for errors
- Verify all JS files are present in static/js/
- Ensure jQuery and other dependencies load before custom scripts

## Quick Commands

```bash
# View locally
cd docs/project_page && ./serve.sh

# Check file structure
tree docs/project_page -L 2

# Find all images
find docs/project_page/static/img -type f -name "*.png" -o -name "*.jpg"

# Check HTML syntax (if tidy installed)
tidy -q -e docs/project_page/index.html

# Create zip for manual upload
cd docs/project_page && zip -r ../project_page.zip .
```