#!/usr/bin/env python3
"""Cut the subject out of images (transparent PNG) with rembg.

Usage: cutout.py INPUT [INPUT ...] -o OUTDIR [--model isnet-general-use] [--mask]
Run with ~/ClaudeWork/.ai-tools/venv/bin/python.
"""
import argparse, pathlib, sys
from PIL import Image
from rembg import new_session, remove

ap = argparse.ArgumentParser()
ap.add_argument("inputs", nargs="+")
ap.add_argument("-o", "--outdir", required=True)
ap.add_argument("--model", default="isnet-general-use",
                help="isnet-general-use (default), u2net, u2net_human_seg, birefnet-general, ...")
ap.add_argument("--mask", action="store_true", help="also save the black/white mask")
a = ap.parse_args()

out = pathlib.Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
session = new_session(a.model)
for p in map(pathlib.Path, a.inputs):
    img = Image.open(p).convert("RGB")
    cut = remove(img, session=session)
    cut.save(out / f"{p.stem}_cutout.png")
    if a.mask:
        cut.getchannel("A").save(out / f"{p.stem}_mask.png")
    print(f"{p.name} -> {p.stem}_cutout.png", file=sys.stderr)
