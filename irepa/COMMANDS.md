# Quick Command Reference

## 🚀 Essential Commands

### View Page Locally
```bash
cd /home/colligo/project/vlm/repa-baseline/docs/project_page
./serve.sh
# Open http://localhost:8000
```

### Build Everything
```bash
./scripts/build.sh                   # Full build (needs API token)
./scripts/build.sh --skip-flux       # Skip Flux generation
./scripts/build.sh --only-figures    # Only generate figures
```

## 🎨 Generate Flux Images

### Setup
```bash
# Get token from https://replicate.com/account
export REPLICATE_API_TOKEN="your-token-here"

# Install dependencies
cd assets/flux
pip install -r requirements.txt
```

### Generate
```bash
cd assets/flux

# Hero image
python generate_hero.py

# All icons
python generate_icons.py

# Specific icon only
python generate_icons.py --icon=accuracy
```

### Copy to Static
```bash
cp assets/flux/outputs/hero.png static/img/
cp assets/flux/outputs/icon_*.png static/img/icons/
```

## 📊 Generate Figures

### Setup
```bash
cd assets/figures
pip install -r requirements.txt
```

### Generate
```bash
cd assets/figures
python plot_teaser.py
```

### Copy to Static
```bash
cp assets/figures/*.png static/img/
```

## 🔧 Optimize Images

```bash
# Install tools (optional, one-time)
# Ubuntu/Debian:
sudo apt-get install optipng pngquant

# macOS:
brew install optipng pngquant

# Run optimization
./scripts/optimize_images.sh
```

## 📝 Edit Content

### Update Links
```bash
# Edit index.html
nano index.html   # or your preferred editor

# Lines to update:
# ~50: arXiv URL
# ~56: PDF URL
# ~62: Code/GitHub URL
```

### Update Abstract/Content
```bash
# Edit index.html directly
nano index.html

# Sections:
# ~102-112: Abstract
# ~115-126: Teaser figure caption
# ~131-160: Key takeaways
```

## 🚢 Deploy

### GitHub Pages
```bash
cd /home/colligo/project/vlm/repa-baseline
git add docs/project_page
git commit -m "Add/update project page"
git push

# Then enable in: Repository Settings → Pages → Source: /docs/project_page
```

### Manual Deploy
```bash
# Create zip
cd /home/colligo/project/vlm/repa-baseline/docs
zip -r project_page.zip project_page/

# Or rsync to server
rsync -avz project_page/ user@server:/path/to/public_html/
```

## 🔍 Verify

### Check Structure
```bash
# View directory tree
tree -L 2 -I '__pycache__|*.pyc'

# Or
ls -R | head -50
```

### Check Images
```bash
# List generated Flux images
ls -lh assets/flux/outputs/

# List static images
ls -lh static/img/*.png

# Check specific file exists
test -f static/img/teaser-v2.png && echo "✓ Teaser exists" || echo "✗ Missing"
```

### Test Links
```bash
# Start server
./serve.sh &

# Test (requires curl)
curl -I http://localhost:8000 | head -1

# Stop server
killall python3  # or Ctrl+C in terminal
```

## 🛠️ Development

### Watch for Changes (requires entr)
```bash
# Auto-reload on file change
ls *.html static/css/*.css | entr -r ./serve.sh
```

### Quick Edit-Test Cycle
```bash
# 1. Edit
nano index.html

# 2. Refresh browser (Ctrl+Shift+R / Cmd+Shift+R)
# No need to restart server for HTML/CSS changes
```

### Add New Figure
```bash
# 1. Create script
nano assets/figures/plot_newfig.py

# 2. Generate
cd assets/figures
python plot_newfig.py

# 3. Copy to static
cp newfig.png ../../static/img/

# 4. Add to HTML
nano ../../index.html
# Add: <img src="static/img/newfig.png" alt="New Figure">
```

## 📦 Package for Sharing

```bash
# Create complete package
cd /home/colligo/project/vlm/repa-baseline/docs
tar -czf project_page.tar.gz project_page/

# Or without source (just web files)
cd project_page
tar -czf ../project_page_web.tar.gz index.html static/ serve.sh README.md
```

## 🆘 Troubleshooting

### Permission Issues
```bash
# Fix script permissions
chmod +x serve.sh scripts/*.sh assets/flux/*.py assets/figures/*.py
```

### Clear Cache
```bash
# Remove generated files and start fresh
rm -rf assets/flux/outputs/*
rm -rf assets/figures/*.png
./scripts/build.sh
```

### Check Python Dependencies
```bash
# Flux
cd assets/flux
pip install -r requirements.txt --upgrade

# Figures
cd ../figures
pip install -r requirements.txt --upgrade
```

### Test Individual Scripts
```bash
# Test Flux generation (without actual generation)
cd assets/flux
python -c "import replicate, yaml; print('✓ Dependencies OK')"

# Test figure generation
cd assets/figures
python -c "import matplotlib, numpy, pandas; print('✓ Dependencies OK')"
```

## 📚 Documentation

- **README.md** - Main overview
- **docs/SETUP.md** - Complete setup guide
- **PROJECT_SUMMARY.md** - What was created
- **QUICK_START.md** - Fast reference
- **COMMANDS.md** - This file

---

**Pro tip:** Bookmark this file for quick reference!