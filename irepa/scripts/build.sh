#!/bin/bash
# Build script for iREPA project page
# Generates all assets: Flux images, figures, and interactive visualizations

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}iREPA Project Page - Build Script${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 not found${NC}"
    exit 1
fi

# Function to check and install requirements
check_requirements() {
    local req_file=$1
    local context=$2

    if [ -f "$req_file" ]; then
        echo -e "${BLUE}Checking $context requirements...${NC}"
        python3 -m pip install -q -r "$req_file" 2>&1 | grep -v "Requirement already satisfied" || true
        echo -e "${GREEN}✓ Requirements satisfied${NC}"
    fi
}

# Parse arguments
SKIP_FLUX=false
SKIP_FIGURES=false
ONLY_FLUX=false
ONLY_FIGURES=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-flux)
            SKIP_FLUX=true
            shift
            ;;
        --skip-figures)
            SKIP_FIGURES=true
            shift
            ;;
        --only-flux)
            ONLY_FLUX=true
            shift
            ;;
        --only-figures)
            ONLY_FIGURES=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--skip-flux] [--skip-figures] [--only-flux] [--only-figures]"
            exit 1
            ;;
    esac
done

# ============================================
# 1. Generate Flux Images
# ============================================
if [ "$SKIP_FLUX" = false ] && [ "$ONLY_FIGURES" = false ]; then
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE}1. Generating Flux Images${NC}"
    echo -e "${BLUE}============================================${NC}"

    if [ -z "$REPLICATE_API_TOKEN" ]; then
        echo -e "${RED}Warning: REPLICATE_API_TOKEN not set${NC}"
        echo "Flux image generation will be skipped."
        echo "To generate images:"
        echo "  1. Get token at https://replicate.com/account"
        echo "  2. export REPLICATE_API_TOKEN='your-token'"
        echo "  3. Run: ./scripts/build.sh --only-flux"
        echo ""
    else
        check_requirements "assets/flux/requirements.txt" "Flux"

        # Generate hero image
        echo -e "${BLUE}Generating hero image...${NC}"
        cd assets/flux
        python3 generate_hero.py
        cd "$PROJECT_ROOT"

        # Generate icons
        echo -e "${BLUE}Generating takeaway icons...${NC}"
        cd assets/flux
        python3 generate_icons.py
        cd "$PROJECT_ROOT"

        echo -e "${GREEN}✓ Flux image generation complete${NC}"

        # Copy to static
        echo -e "${BLUE}Copying Flux images to static...${NC}"
        mkdir -p static/img/icons
        cp -f assets/flux/outputs/hero.png static/img/ 2>/dev/null || echo "  Hero image not found (ok if generation failed)"
        cp -f assets/flux/outputs/icon_*.png static/img/icons/ 2>/dev/null || echo "  Icons not found (ok if generation failed)"
        echo -e "${GREEN}✓ Images copied${NC}"
    fi
fi

# ============================================
# 2. Generate Figures
# ============================================
if [ "$SKIP_FIGURES" = false ] && [ "$ONLY_FLUX" = false ]; then
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE}2. Generating Figures${NC}"
    echo -e "${BLUE}============================================${NC}"

    check_requirements "assets/figures/requirements.txt" "Figure generation"

    # Generate teaser
    echo -e "${BLUE}Generating teaser figure...${NC}"
    cd assets/figures
    python3 plot_teaser.py
    cd "$PROJECT_ROOT"

    # TODO: Add more figure generation scripts here
    # python3 plot_correlations.py
    # python3 plot_convergence.py

    echo -e "${GREEN}✓ Figure generation complete${NC}"

    # Copy to static
    echo -e "${BLUE}Copying figures to static...${NC}"
    cp -f assets/figures/*.png static/img/ 2>/dev/null || true
    echo -e "${GREEN}✓ Figures copied${NC}"
fi

# ============================================
# 3. Optimize Images
# ============================================
echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}3. Optimizing Images${NC}"
echo -e "${BLUE}============================================${NC}"

if command -v scripts/optimize_images.sh &> /dev/null; then
    ./scripts/optimize_images.sh
else
    echo "Optimize script not found, skipping..."
fi

# ============================================
# Summary
# ============================================
echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}✓ Build Complete!${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo "Generated assets in:"
echo "  • assets/flux/outputs/ - Flux generated images"
echo "  • assets/figures/ - Generated figures"
echo "  • static/img/ - Final web-ready images"
echo ""
echo "Next steps:"
echo "  1. Review generated assets"
echo "  2. Test locally: ./serve.sh"
echo "  3. Deploy: ./scripts/deploy.sh"
echo ""