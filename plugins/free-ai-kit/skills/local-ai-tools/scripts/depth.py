#!/usr/bin/env python3
"""Depth maps with Depth Anything V2 Small (ONNX). White = near, black = far.

Usage: depth.py INPUT [INPUT ...] -o OUTDIR [--model PATH] [--size 518]
Run with ~/ClaudeWork/.ai-tools/venv/bin/python.
"""
import argparse, os, pathlib, sys
import numpy as np
import onnxruntime as ort
from PIL import Image

DEFAULT = os.path.expanduser("~/ClaudeWork/.ai-tools/models/depth-anything-v2-small.onnx")
MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32)
STD = np.array([0.229, 0.224, 0.225], dtype=np.float32)

ap = argparse.ArgumentParser()
ap.add_argument("inputs", nargs="+")
ap.add_argument("-o", "--outdir", required=True)
ap.add_argument("--model", default=DEFAULT)
ap.add_argument("--size", type=int, default=518, help="model input size, multiple of 14")
a = ap.parse_args()
if a.size % 14:
    sys.exit("--size must be a multiple of 14")

sess = ort.InferenceSession(a.model, providers=["CPUExecutionProvider"])
inp = sess.get_inputs()[0].name
out = pathlib.Path(a.outdir); out.mkdir(parents=True, exist_ok=True)

for p in map(pathlib.Path, a.inputs):
    img = Image.open(p).convert("RGB")
    w, h = img.size
    x = np.asarray(img.resize((a.size, a.size), Image.BICUBIC), dtype=np.float32) / 255.0
    x = ((x - MEAN) / STD).transpose(2, 0, 1)[None]
    d = np.squeeze(sess.run(None, {inp: x})[0]).astype(np.float32)
    d = (d - d.min()) / max(float(d.max() - d.min()), 1e-6)
    depth = Image.fromarray((d * 65535).astype(np.uint16)).resize((w, h), Image.BICUBIC)
    depth.save(out / f"{p.stem}_depth16.png")
    depth.point(lambda v: v / 257).convert("L").save(out / f"{p.stem}_depth.png")
    print(f"{p.name} -> {p.stem}_depth.png", file=sys.stderr)
