---
name: local-ai-tools
description: Free local AI helpers that run on this user's Intel iMac. Real-ESRGAN upscaling (sharp punch-ins and close-ups), RIFE frame interpolation (smooth slow motion, speed ramps), rembg subject cut-outs (collage, parallax layers) and Depth Anything V2 depth maps (2.5D parallax). Use whenever a video or graphics job needs a close-up from low-resolution footage, upscaled archive photos, slow motion, cut-outs, background removal, depth or parallax, before reaching for paid AI tools.
---

# Local AI tools (free, Intel Mac)

Everything installs into `~/ClaudeWork/.ai-tools` and runs on the Mac. No
accounts, no credits, licences OK for business use:

| Tool | Does | Licence | Runs on |
|---|---|---|---|
| Real-ESRGAN (ncnn-vulkan) | 2–4× upscaling of stills and frames | BSD-3 | Radeon GPU (Vulkan to Metal); `-g -1` = CPU |
| RIFE v4.6 (ncnn-vulkan) | Frame interpolation: 2×/4× smoother, slow motion | MIT | Radeon GPU; `-g -1` = CPU |
| rembg (isnet-general-use) | Subject cut-out to transparent PNG plus mask | MIT (model Apache-2.0) | CPU, seconds per image |
| Depth Anything V2 Small | Depth map (white = near) | Apache-2.0 | CPU, a few seconds per image |

## Setup (once, on the Mac)
```bash
bash <skill-dir>/scripts/setup.sh
```
Needs about 1.5 GB free (it checks). It downloads from GitHub and Hugging Face,
verifies the checksums of the two binaries, removes the macOS quarantine flag
from just those files, and makes a Python venv for rembg and onnxruntime.
**Never** disable Gatekeeper system-wide (`spctl --master-disable`), even if a
README suggests it. After setup, test each GPU tool on one image. If the GPU
path errors, add `-g -1` (CPU, slower).

Paths after setup:
```
T=~/ClaudeWork/.ai-tools
$T/bin/realesrgan/realesrgan-ncnn-vulkan
$T/bin/rife/rife-ncnn-vulkan   (model dir: $T/bin/rife/rife-v4.6)
$T/venv/bin/python <skill-dir>/scripts/cutout.py
$T/venv/bin/python <skill-dir>/scripts/depth.py
```

## Recipes

**Sharp punch-in or close-up from 1080p footage** (do this before cropping past
about 1.3×). Upscale only the frames of that shot:
```bash
mkdir -p f up
ffmpeg -ss START -to END -i clip.mp4 -qscale:v 1 f/%06d.jpg
$T/bin/realesrgan/realesrgan-ncnn-vulkan -i f -o up -n realesrgan-x4plus -s 2 -f jpg
ffmpeg -framerate FPS -i up/%06d.jpg -c:v libx264 -crf 14 -pix_fmt yuv420p shot_2x.mp4
```
Use `realesrgan-x4plus` for photos and real footage (`realesr-animevideov3` is
for animation). Upscale archive photos the same way, one image at a time.

**Smooth slow motion or speed ramp:**
```bash
mkdir -p f s
ffmpeg -i shot.mp4 f/%08d.png
$T/bin/rife/rife-ncnn-vulkan -i f -o s -m $T/bin/rife/rife-v4.6 -n FRAMES_x2
ffmpeg -framerate FPS -i s/%08d.png -c:v libx264 -crf 14 -pix_fmt yuv420p shot_slow.mp4
```
`-n` is the target frame count (2× the input for half speed). Play at the
original fps for slow motion, or at 2× fps for smoother motion.

**2.5D parallax from a still:**
1. Upscale the photo (Real-ESRGAN) if it's small.
2. `cutout.py photo.jpg -o layers --mask` gives the foreground subject.
3. `depth.py photo.jpg -o layers` gives a depth map for mid- and background
   separation.
4. Background plate: the original photo with the subject area covered (dilate
   the mask, then blur or clone-fill, or scale the background up so the gap
   hides behind the subject).
5. Animate in Remotion or After Effects: background moves slow, subject moves
   faster, slight scale (a 1.00 to 1.06 push), optional depth-map displacement.
   Follow motion-kit's documentary-motion-style.

**Collage cut-outs:** `cutout.py` on each photo, then add the white border,
drop shadow and paper texture in Remotion or After Effects.

## Speed on this iMac (be realistic)
GPU upscaling is about seconds per 1080p frame, so use it on **specific shots and
stills**, not whole long videos. A full 2-minute video would take hours.
Process only the frames the edit needs, and check disk space first (frames are
large; delete the `f/`, `up/` and `s/` folders when done).

## Not here, on purpose
AI video or image generation (Wan, LTX, Hunyuan, MiniMax H3, Flux, SDXL) can't
run usefully on this iMac. See my-toolkit.
