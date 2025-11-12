#!/usr/bin/env bash
set -euo pipefail

echo "Bootstrapping LiveTracks tooling (macOS)"

# Homebrew deps
if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew not found. Install from https://brew.sh then re-run this script."
  exit 1
fi

echo "Installing brew packages (ffmpeg, aubio)"
brew list ffmpeg >/dev/null 2>&1 || brew install ffmpeg
brew list aubio  >/dev/null 2>&1 || brew install aubio

# Python deps
echo "Installing Python packages (mido, pyyaml)"
python3 -m pip install --user --upgrade pip
python3 -m pip install --user mido pyyaml

echo "Done. Verify with:"
echo "  ffmpeg -version  &&  aubio tempo -h  &&  python3 -c 'import mido, yaml; print(\"OK\")'"
