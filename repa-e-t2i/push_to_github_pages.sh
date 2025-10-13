#!/bin/bash

# Script to update and push the project page to End2End-Diffusion.github.io
# Usage: ./push_to_github_pages.sh

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Updating REPA-E-T2I Project Page ===${NC}"

# Define paths
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_REPO="/home/colligo/project/vlm/End2End-Diffusion.github.io"
DEST_DIR="$DEST_REPO/repa-e-t2i"

# Check if destination repo exists
if [ ! -d "$DEST_REPO" ]; then
    echo -e "${RED}Error: Destination repo not found at $DEST_REPO${NC}"
    exit 1
fi

echo -e "${BLUE}Step 1: Removing old project page...${NC}"
rm -rf "$DEST_DIR"

echo -e "${BLUE}Step 2: Copying updated project page...${NC}"
mkdir -p "$DEST_DIR"
cp -r "$SOURCE_DIR"/* "$DEST_DIR/"

echo -e "${BLUE}Step 3: Updating metadata...${NC}"
# Update the og:url metadata to the correct GitHub Pages URL
sed -i 's|https://repa-e-t2i\.github\.io|https://end2end-diffusion.github.io/repa-e-t2i|g' "$DEST_DIR/index.html"

echo -e "${BLUE}Step 4: Committing changes...${NC}"
cd "$DEST_REPO"

# Check if there are any changes
if git diff --quiet && git diff --cached --quiet; then
    echo -e "${GREEN}No changes detected. Project page is already up to date.${NC}"
    exit 0
fi

git add repa-e-t2i/
git commit -m "Update repa-e-t2i project page

🤖 Auto-updated from fuse-dit/docs/project_page"

echo -e "${BLUE}Step 5: Pushing to GitHub...${NC}"
git push origin main

echo -e "${GREEN}✓ Successfully updated project page!${NC}"
echo -e "${GREEN}View at: https://end2end-diffusion.github.io/repa-e-t2i/${NC}"
echo -e "${BLUE}Note: GitHub Pages may take 1-2 minutes to rebuild and deploy${NC}"
