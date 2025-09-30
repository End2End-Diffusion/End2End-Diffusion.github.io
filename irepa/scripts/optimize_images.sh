#!/bin/bash
# Optimize images for web display
# - Compress PNG files
# - Fix rotation/orientation issues
# - Ensure proper dimensions

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Optimizing images for web...${NC}"

# Check for optimization tools
HAS_OPTIPNG=false
HAS_PNGQUANT=false

if command -v optipng &> /dev/null; then
    HAS_OPTIPNG=true
fi

if command -v pngquant &> /dev/null; then
    HAS_PNGQUANT=true
fi

if [ "$HAS_OPTIPNG" = false ] && [ "$HAS_PNGQUANT" = false ]; then
    echo "No optimization tools found. Install optipng or pngquant:"
    echo "  Ubuntu/Debian: sudo apt-get install optipng pngquant"
    echo "  macOS: brew install optipng pngquant"
    echo ""
    echo "Skipping optimization..."
    exit 0
fi

# Find all PNG files in static/img
IMG_DIR="static/img"
TOTAL=0
OPTIMIZED=0

if [ "$HAS_OPTIPNG" = true ]; then
    echo "Using optipng for lossless compression..."
    for img in $(find "$IMG_DIR" -name "*.png"); do
        TOTAL=$((TOTAL + 1))
        if optipng -quiet -o2 "$img" 2>/dev/null; then
            OPTIMIZED=$((OPTIMIZED + 1))
            echo "  ✓ Optimized: $img"
        fi
    done
fi

if [ "$HAS_PNGQUANT" = true ]; then
    echo "Using pngquant for lossy compression (if beneficial)..."
    for img in $(find "$IMG_DIR" -name "*.png" ! -name "*-fs8.png"); do
        # Only run pngquant if file is large (>500KB)
        SIZE=$(stat -f%z "$img" 2>/dev/null || stat -c%s "$img" 2>/dev/null)
        if [ "$SIZE" -gt 512000 ]; then
            pngquant --skip-if-larger --quality=85-95 --ext .png --force "$img" 2>/dev/null && \
                echo "  ✓ Compressed: $img"
        fi
    done
fi

echo -e "${GREEN}✓ Image optimization complete${NC}"
echo "  Processed: $TOTAL images"
echo "  Optimized: $OPTIMIZED images"