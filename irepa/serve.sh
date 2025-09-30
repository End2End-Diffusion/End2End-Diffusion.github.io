#!/bin/bash

# Simple script to serve the project page locally

PORT=8000

echo "Starting local server for iREPA project page..."
echo "Open your browser and navigate to: http://localhost:${PORT}"
echo "Press Ctrl+C to stop the server"
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 -m http.server $PORT
elif command -v python &> /dev/null; then
    python -m http.server $PORT
else
    echo "Error: Python is not installed or not in PATH"
    exit 1
fi