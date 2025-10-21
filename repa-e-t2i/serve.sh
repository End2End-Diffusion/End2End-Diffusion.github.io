#!/bin/bash
# Simple HTTP server for local preview of the project page

PORT=8009

echo "Starting local server on http://localhost:$PORT"
echo "Press Ctrl+C to stop"
echo ""

# Use Python 3's built-in HTTP server
python3 -m http.server $PORT
