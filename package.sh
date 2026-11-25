#!/bin/sh
# Rebuild the site and make the upload zip. Always includes newton.zip (kept in assets/).
set -e
cd "$(dirname "$0")"
python3 build.py >/dev/null
mkdir -p dist; cp assets/* site.css site.js theo.js dist/; cp -r img dist/
ZIP="$(cd .. && pwd)/forgeline-website.zip"; rm -f "$ZIP"; (cd dist && zip -qr "$ZIP" .)
unzip -l "$ZIP" | grep -E "newton.zip|freezeframe-extension" 
unzip -l "$ZIP" | tail -1
