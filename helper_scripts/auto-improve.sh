#!/bin/bash
#
# Auto-improvement loop for End2End-Diffusion landing page
# Runs /improve-landing command every 15 minutes
#
# Usage: ./helper_scripts/auto-improve.sh
#
# Safety: This script ONLY improves the landing page.
# Project pages (irepa/, repa-e/, repa-e-t2i/) are NEVER modified.
#

#!/bin/bash -il
# ν-bench Automated Improvement Script
# Runs on login node (4 GPUs available), loops every 30 minutes

set -e

# load bash profile
source ~/.local/.bashrc

# project directory
PROJECT_DIR="/scratch3/len091/project/vlm/End2End-Diffusion.github.io"
LOG_FILE="$PROJECT_DIR/helper_scripts/auto-improve.log"
INTERVAL=900  # 15 minutes
CONDA_ENV="repa"

# load conda environment
source /apps/miniforge3/enable_miniforge.sh >/dev/null 2>&1
conda activate $CONDA_ENV

cd "$PROJECT_DIR"

echo "Starting End2End-Diffusion landing page auto-improvement loop..."
echo "Interval: ${INTERVAL}s (30 min)"
echo "Press Ctrl+C to stop"

# define claude aliases
_claude_with_profile() {
  export CLAUDE_CONFIG_DIR="$1"
  command claude "${@:2}"
}
# Personal profile (default)
claude() {
    echo "Using personal profile"
  _claude_with_profile "$HOME/.local/.claude" "$@"
}
# Work profile
wclaude() {
    echo "Using work profile"
    _claude_with_profile "$HOME/.claude" "$@"
}

# # Configuration
# INTERVAL_SECONDS=900  # 15 minutes
# PROJECT_DIR="/scratch3/len091/project/vlm/End2End-Diffusion.github.io"
# LOG_FILE="${PROJECT_DIR}/helper_scripts/auto-improve.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Landing Page Auto-Improvement Loop${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}Project:${NC}  ${PROJECT_DIR}"
echo -e "${BLUE}Interval:${NC} Every 15 minutes"
echo -e "${BLUE}Log file:${NC} ${LOG_FILE}"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop${NC}"
echo ""

# # define claude aliases
# _claude_with_profile() {
#   export CLAUDE_CONFIG_DIR="$1"
#   command claude "${@:2}"
# }
# # Personal profile (default)
# claude() {
#     echo "Using personal profile"
#   _claude_with_profile "$HOME/.local/.claude" "$@"
# }
# # Work profile
# wclaude() {
#     echo "Using work profile"
#     _claude_with_profile "$HOME/.claude" "$@"
# }

# cd "${PROJECT_DIR}"

# Verify we're in the right directory
if [ ! -f "index.html" ]; then
    echo -e "${RED}Error: index.html not found. Are you in the right directory?${NC}"
    exit 1
fi

if [ ! -f "landing-todos.md" ]; then
    echo -e "${RED}Error: landing-todos.md not found. Please create it first.${NC}"
    exit 1
fi

# Create log file if it doesn't exist
touch "${LOG_FILE}"

iteration=1

while true; do
    echo "========================================" >> "$LOG_FILE"
    echo "Run started: $(date)" >> "$LOG_FILE"

    claude -p "/improve" \
      --permission-mode acceptEdits \
      --dangerously-skip-permissions \
      2>&1 | tee -a "$LOG_FILE"

    echo "Run completed: $(date)" >> "$LOG_FILE"
    echo "========================================" >> "$LOG_FILE"

    echo "Sleeping for 30 minutes..."
    sleep $INTERVAL
done
