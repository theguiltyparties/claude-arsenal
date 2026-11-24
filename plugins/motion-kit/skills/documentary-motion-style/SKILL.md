---
name: documentary-motion-style
description: The quality bar and build method for this user's explainer and promo videos: Vox-style and MOX "STORY BOLD" documentary motion graphics, kinetic typography, 2.5D parallax, textured collage, map moves, high-end transitions, sound design and mix. Use for ANY video upgrade, re-edit, explainer, history short, promo, title sequence, or whenever the user says slick, modern, Vox-style, MOX-style, GFX, transitions, typography, parallax, or "make it incredible". Read before planning or rendering any edit.
---

# Documentary motion style (Vox / MOX)

The user is a professional video editor. A plain FFmpeg edit (crossfades,
`drawtext` captions, a zoom or two) is **not acceptable** and will be rejected
as "basic". Every edit must look designed, layered and intentional.

## 0. Build method (do this, in order)

1. **Study the references before designing anything.** Extract a frame every
   0.5 s (`ffmpeg -vf fps=2,scale=480:-1,tile=6x5`) from:
   - the project's own look/style guide and finished episode (e.g. MOX
     "STORY BOLD" files: follow its wordmark, colours and fonts first), and
   - any reference video in the project (e.g. the Vox-style reference in MOX).
   Look at the contact sheets. Write a short **style bible**: palette (hex),
   fonts, texture, how text enters and exits, transition vocabulary, average
   shot length, SFX palette. Show it to the user before building.
2. **Storyboard / animatic:** a beat sheet against the voiceover, with one row
   per 1–3 seconds: visual, text on screen, move, transition, SFX.
3. **Build the graphics in a real motion tool, not FFmpeg:**
   - **Remotion** (React, runs on this Mac with Node; see the
     remotion-video-creation skill). Default for typography, GFX, maps, collage,
     captions, parallax and transitions. Free for individuals and companies of
     up to 3 people; check remotion.dev/license if that changes.
   - **After Effects** via the AfterEffects MCP connector, when it's working
     (test first). The user owns AE.
   - **FFmpeg only for**: trimming source clips, conforming formats, final
     assembly, loudness and exports.
4. **Render a 10–15 s preview of the hardest section first.** Run the QA
   checklist (section 7) on it yourself before showing the user.
5. Only then render the full piece and the platform versions.

## 1. Pacing
- Hook in the first 1–3 s: the most surprising line plus the strongest visual,
  with motion from frame 1. No logo first.
- A **new visual event every 1–3 s** (cut, move, text pop, map change, highlight).
  Nothing static for more than 3 s; even stills have a slow move.
- Cut on the voice: hits land on stressed syllables, numbers, names and dates.
- Vary rhythm: fast clusters (0.5–1 s) around reveals, then a 3–4 s held beat
  before a big line.

## 2. Typography
- **Use the project's fonts first.** Otherwise pick free commercial-use fonts
  (Google Fonts, OFL licence), for example:
  - Headline: Anton, Bebas Neue, Oswald, Archivo Black (condensed and heavy)
  - Editorial serif for quotes and dates: Playfair Display, Libre Caslon, DM Serif Display
  - Document or typewriter for archival labels: Special Elite, IBM Plex Mono
- Big and confident: headline words fill 60–80% of frame width on 9:16.
  **Six words or fewer on screen at once.**
- Kinetic entrances matched to the voice: word-by-word pop with overshoot
  (spring), mask reveals, slide-up with blur, typewriter for documents.
  Key words get an accent colour, a **highlighter-marker swipe** or a hand-drawn
  underline or circle that draws on.
- Exits are designed too (wipe, slide or mask). Never a plain fade.
- Captions: word-by-word with the active word highlighted, heavy weight, an
  outline or shadow plate, kept clear of the platform UI (9:16 safe zone: keep
  roughly the top 220 px and bottom 420 px free).

## 3. Look and texture (the Vox / MOX feel)
- **Paper and print texture:** a subtle paper grain overlay, halftone dots on
  photos, slight film grain (2–4%), a soft vignette.
- **Cut-out collage:** photos as torn-edge or white-bordered cut-outs with drop
  shadows, layered on textured backgrounds. Subjects cut out with **rembg**
  (free, MIT, runs on CPU) and placed on their own layer.
- **Archive treatment:** duotone or desaturated plus one accent colour; red,
  yellow or highlighter green against off-black or newsprint cream.
- **Maps:** draw-on routes, pulsing location dots, labels that pop, a camera push
  from region to city, distance lines that measure out (e.g. Hiroshima to
  Nagasaki).
- **Data and callouts:** numbers count up, dates stamp in, arrows and brackets
  draw on.

## 4. Camera moves and 2.5D parallax
- Every shot moves: slow push-in (2–5% scale over the shot), drift or a
  rack-focus feel via blur.
- **Parallax on stills:** split into foreground subject (rembg cut-out),
  midground and background (inpaint the gap, or blur and extend it); move layers
  at different speeds with slight scale. Optional depth map from Depth Anything
  V2 **Small** (Apache-2.0, CPU-friendly) for displacement.
- **Punch-ins** for close-ups on faces, hands, documents and objects, from the
  highest-resolution source. Past about 1.3× on 1080 sources, upscale that shot
  first with Real-ESRGAN (free-ai-kit). Smooth slow-mo and speed ramps with RIFE.

## 5. Transitions (with sound)
Vocabulary, all built in Remotion or AE:
- Whip pan with directional motion blur
- Zoom-through (into a detail, out the other side)
- Match cut on shape or colour
- Paper tear and page turn, collage slide-in
- Light leak and film burn (sparingly, on emotional beats)
- Glitch, RGB split, frame stutter (for tension or tech only)
- Mask wipe driven by a shape or a text element
**Every transition gets a sound** (whoosh, swish, paper rip, impact). Never more
than 2–3 transition types per piece; consistency reads as premium.

## 6. Sound design and mix
- **SFX layers:** whooshes on moves, hits and "dings" on text pops, paper and
  rustle for collage, typewriter for documents, a sub-boom on reveals, risers
  into big lines, room tone or ambience under scenes.
- **Free commercial sources only:**
  - Pixabay sound effects (Pixabay Content License)
  - Freesound **CC0** (CC-BY only with credit; never CC-BY-NC)
  - Sonniss GDC free bundles (royalty-free, commercial)
  - Never BBC Sound Effects (non-commercial) or anything ripped from YouTube.
- **Music:** the project's own track if it's licensed, otherwise free
  business-licensed beds; edit to the beats so cuts land on the music.
- **Mix targets (social):** dialogue around −14 LUFS integrated; music ducked
  12–18 dB under voice (sidechain); SFX audible but under the voice; true peak
  ≤ −1 dBTP. Check with `ffmpeg -af ebur128`.

## 7. QA before showing the user (be harsh)
Look at a 2 fps contact sheet and the loudness readout, then answer each:
- Would a Vox or MOX editor ship this? If anything looks like a template or a
  default FFmpeg effect, redo it.
- New visual event at least every 3 s? Any static frames?
- Is typography designed (font, scale, accent, entrance and exit), not just
  burned-in text?
- Parallax and collage depth present on stills?
- Every transition has a sound; SFX present on text pops and reveals?
- Mix: voice clear, music ducked, no clipping, around −14 LUFS?
- Safe zones respected; no text under the platform UI?
- Facts, names, dates and spellings match the project's fact-check rules?
- Licences of every font, SFX, music and stock clip noted?
Fix the failures, re-render the preview, then show it, with the style bible
and a short list of what's on screen.

## Free-only reminder
No paid AI video generation (Flow, Veo, TopView, Higgsfield, MiniMax H3), no
paid stock, no ElevenLabs credits. Skills that mention paid tools (fal.ai,
ElevenLabs, Descript, CapCut Pro) are reference only; use the free route.
