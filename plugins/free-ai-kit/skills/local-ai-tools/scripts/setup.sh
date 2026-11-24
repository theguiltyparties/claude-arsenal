#!/bin/bash
# One-time setup of the free local AI tools into ~/ClaudeWork/.ai-tools (macOS).
# Safe to run again: anything already installed is skipped.
set -euo pipefail

ROOT="${AI_TOOLS_DIR:-$HOME/ClaudeWork/.ai-tools}"
BIN="$ROOT/bin"; MODELS="$ROOT/models"; TMP="$ROOT/tmp"
mkdir -p "$BIN" "$MODELS" "$TMP"

ESR_URL="https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-macos.zip"
ESR_SHA="e0ad05580abfeb25f8d8fb55aaf7bedf552c375b5b4d9bd3c8d59764d2cc333a"
RIFE_URL="https://github.com/nihui/rife-ncnn-vulkan/releases/download/20221029/rife-ncnn-vulkan-20221029-macos.zip"
RIFE_SHA="4a63a1f3c9c715773c57d2ee51df1b315ed20cd6c63103e45c483ecc4400b595"
DEPTH_URL="https://huggingface.co/onnx-community/depth-anything-v2-small/resolve/main/onnx/model.onnx"

sha_ok() { [ "$(shasum -a 256 "$1" | cut -d' ' -f1)" = "$2" ]; }
unquarantine() { xattr -dr com.apple.quarantine "$1" 2>/dev/null || true; }

need_mb=1500
free_mb=$(df -m "$HOME" | awk 'NR==2{print $4}')
if [ "$free_mb" -lt "$need_mb" ]; then
  echo "Not enough disk space: ${free_mb} MB free, need about ${need_mb} MB." >&2; exit 1
fi

# 1. Real-ESRGAN (upscaling), ncnn-vulkan build, runs on the Mac GPU via Metal.
if [ ! -x "$BIN/realesrgan/realesrgan-ncnn-vulkan" ]; then
  echo "Installing Real-ESRGAN..."
  curl -fL --retry 3 -o "$TMP/esr.zip" "$ESR_URL"
  sha_ok "$TMP/esr.zip" "$ESR_SHA" || { echo "Real-ESRGAN checksum mismatch" >&2; exit 1; }
  rm -rf "$BIN/realesrgan"; mkdir -p "$BIN/realesrgan"
  unzip -q -o "$TMP/esr.zip" -x 'input*.jpg' 'onepiece_demo.mp4' -d "$BIN/realesrgan"
  chmod +x "$BIN/realesrgan/realesrgan-ncnn-vulkan"; unquarantine "$BIN/realesrgan"
  rm -f "$TMP/esr.zip"
fi

# 2. RIFE (frame interpolation / slow motion). Keep only the rife-v4.6 model to save disk.
if [ ! -x "$BIN/rife/rife-ncnn-vulkan" ]; then
  echo "Installing RIFE (about 440 MB download)..."
  curl -fL --retry 3 -o "$TMP/rife.zip" "$RIFE_URL"
  sha_ok "$TMP/rife.zip" "$RIFE_SHA" || { echo "RIFE checksum mismatch" >&2; exit 1; }
  rm -rf "$TMP/rife_x" "$BIN/rife"; mkdir -p "$TMP/rife_x" "$BIN/rife"
  unzip -q -o "$TMP/rife.zip" -d "$TMP/rife_x"
  src="$TMP/rife_x/rife-ncnn-vulkan-20221029-macos"
  cp "$src/rife-ncnn-vulkan" "$src/LICENSE" "$BIN/rife/"
  cp -R "$src/rife-v4.6" "$BIN/rife/"
  chmod +x "$BIN/rife/rife-ncnn-vulkan"; unquarantine "$BIN/rife"
  rm -rf "$TMP/rife_x" "$TMP/rife.zip"
fi

# 3. Python tools: rembg (cut-outs) + onnxruntime for depth maps, in their own venv.
if [ ! -x "$ROOT/venv/bin/python" ]; then
  echo "Creating Python environment..."
  python3 -m venv "$ROOT/venv"
fi
"$ROOT/venv/bin/python" -m pip install -q --upgrade pip
"$ROOT/venv/bin/python" -m pip install -q "rembg[cpu]>=2.0.88" onnxruntime pillow numpy

# 4. Depth Anything V2 Small (ONNX, Apache-2.0).
if [ ! -s "$MODELS/depth-anything-v2-small.onnx" ]; then
  echo "Downloading Depth Anything V2 Small..."
  curl -fL --retry 3 -o "$MODELS/depth-anything-v2-small.onnx.part" "$DEPTH_URL"
  mv "$MODELS/depth-anything-v2-small.onnx.part" "$MODELS/depth-anything-v2-small.onnx"
fi

echo
echo "Done. Installed in $ROOT"
"$BIN/realesrgan/realesrgan-ncnn-vulkan" -h >/dev/null 2>&1 && echo "Real-ESRGAN: OK" || echo "Real-ESRGAN: installed (run a test image to confirm the GPU works)"
"$BIN/rife/rife-ncnn-vulkan" -h >/dev/null 2>&1 && echo "RIFE: OK" || echo "RIFE: installed (run a test to confirm the GPU works)"
"$ROOT/venv/bin/python" -c "import rembg, onnxruntime; print('rembg + onnxruntime: OK')"
