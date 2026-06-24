#!/bin/bash
# Local preview server for the NanoGen project page.
#
# The page references shared assets one level up (../static/...), so the
# server MUST run from the repo root, not from inside nanogen/.
# This script serves the repo root and points you at /nanogen/.

PORT=8008

# Repo root = parent of this script's directory (nanogen/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Serving repo root: $ROOT_DIR"
echo "Open: http://localhost:$PORT/nanogen/"
echo "Press Ctrl+C to stop"
echo ""

cd "$ROOT_DIR"
python3 -m http.server "$PORT"
