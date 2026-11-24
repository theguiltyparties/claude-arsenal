---
name: my-toolkit
description: Map of this user's tools and when to use each, with a strict free-only rule (the user spends no money). Use at the start of any creative, writing, video, audio, voice, design, website, publishing, social-media or research task, or whenever the user asks "can you…", "what should I use…", or forgets which tool does what. The user is not technical; pick the right tool yourself instead of asking them.
---

# My toolkit

The user is a non-technical creator (books, video, social media). They often
won't remember tool names. Choose the right tool yourself, say in one plain
sentence which one you're using, and give step-by-step instructions in plain
words whenever they must click or type anything.

## Their computer
- 2017 Intel iMac, macOS Ventura 13.7.8, 64 GB RAM. No Homebrew (Intel Macs
  aren't supported). Docker Desktop 4.44.1 (do not let it update: newer
  versions need macOS 14).
- Work folder: `~/ClaudeWork`. Tools installed in `~/bin`: ffmpeg, ffprobe.
  Python 3.11, Node, gh (logged in as theguiltyparties).
- Cloud sessions (`/home/user/...`) can't reach this Mac or its apps. Anything
  that needs VoiceStudio, FFmpeg or local files must run in Claude on the Mac
  (Code tab or Terminal), not in the cloud.

## Apps the user owns (free to use: already paid for)
- **Adobe Photoshop, Premiere Pro, After Effects** are installed on the iMac
  (Creative Cloud). Using them costs nothing extra.
- **After Effects**: a local **AfterEffects** MCP connector ("Local dev") is set
  up on the Mac. Use it for motion graphics, kinetic text, title cards, lower
  thirds and logo stings. Test what its tools can do before relying on them.
- **Premiere Pro**: there is **no Premiere connector**, but Claude has used
  Premiere for the user before. Check how first: Premiere scripting
  (ExtendScript/UXP, e.g. via `osascript`), or computer use (see the screen and
  click) in the desktop app. Otherwise hand off Premiere-ready files: an XML/EDL
  timeline, `.srt` captions, and separate voice, music, SFX and graphics layers.
- **flow** local MCP connector = Google Flow/Veo video generation. It **uses
  paid credits**, so don't use it (free-only rule).
- The **Adobe** connector is Adobe's online tools, not these desktop apps. It
  may ask the user to sign in again.

## Ongoing projects (in ~/ClaudeWork; originals stay in ~/Downloads)
- **MOX** (`~/ClaudeWork/MOX`, from `~/Downloads/_MOX`): MOX International
  "STORY BOLD" history shorts. Episode 01 "The Man Who Survived Two Atomic
  Bombs" (Tsutomu Yamaguchi), 2-minute vertical. Follow its fact-check rules.
- **SHIFT** (`~/ClaudeWork/SHIFT`, from `~/Downloads/SHIFT_ASSETS`): 15-second
  spot for a fictional drink, "SHIFT Yuzu Lime". Tagline "Stay in it."
  Standard: **Lexus-level premium commercial** (motion-kit: premium-commercial-style), not Vox.
  Known fixes, all free by editing (no new AI footage): can on screen in the
  first 2 s; show the can opening (punch-in, upscale, RIFE slow-mo, crack sound
  on the frame); replace the last shot (old can design) with an After Effects
  product hero end card from the current can artwork. Plus 2–4 close-up
  cut-ins of her eyes and face (0.5–1.5 s each): punch-in on the sharpest,
  best-lit source frames, Real-ESRGAN upscale, slow push-in, RIFE slow-mo on
  blinks and glances, matched grade, subtle catchlight. Reject any frame with
  AI face artifacts; if no clip has enough detail, tell the user, don't fake
  it. Also a close-up of her hand picking up the can (macro punch-in, speed
  ramp into slow-mo as the fingers close, condensation glint, pick-up and
  fizz sound on the frame). Use only real source frames that show it; check
  the fingers for AI artifacts (count, shape, merging). If no clip shows a
  pick-up, say so and offer a product-lift move in AE (can cut-out rising,
  light sweep) instead of faking a hand. Three SFX downloaded from
  YouTube must be replaced; ask the user about the music tracks' origin.
- **MOX** has an approved style bible: `~/ClaudeWork/MOX/_upgrade/MOX_EP01_STYLE_BIBLE.md`
  ("The Yamaguchi Case File"). Follow it for every MOX edit.
- Goal for both: a modern, slick upgrade layer: GFX, transitions, kinetic and
  word-by-word captions, sound design, a stronger 3-second hook, and
  9:16 / 4:5 / 16:9 versions with thumbnails.
- Re-edits should be ambitious ("make it incredible"): re-cut from the
  full-resolution source clips, not the finished export. New shots, done for
  free: punch-ins and close-ups on source footage (watch resolution), slow
  push-ins, 2.5D parallax on stills (After Effects), and free business-licensed
  stock B-roll (MOX only if historically accurate). High-end transitions
  (whip, zoom-through, match cut, light leak, film burn, glitch), each synced
  with a sound effect. **No paid AI video generation** (Flow, Veo, TopView,
  Higgsfield).
- Always show a ~15-second preview before a full render.
- **Local AI video generators (MiniMax H3, Wan, Hunyuan, LTX and the like)
  can't run on this iMac**: no NVIDIA GPU, too little disk, and MiniMax H3's
  licence reportedly excludes the US/EU/UK. Don't try. Use the free punch-in,
  parallax, After Effects and stock-footage approach instead. Revisit only if
  the user gets an NVIDIA PC.
- **Voices: the user decides per project. Never swap a project's voice
  without asking.**
  - **MOX: keep Lily's voice** (the existing ElevenLabs "Lily" takes in the
    project). Do NOT use the user's cloned voice on MOX. Re-use the existing
    Lily recordings. If a new Lily line is ever needed, it would come from
    ElevenLabs, so ask first (credits, and the free plan doesn't allow
    commercial use).
  - **SHIFT: keep the existing voiceover (Bella/Sarah)** unless the user says
    otherwise.
  - The user's cloned voice is for projects where they ask for "my voice".
- Licence note (tell the user once, then follow their call): the ElevenLabs
  takes may not be cleared for business use if they were made on the free
  plan.
- Sound effects or music of unknown origin (e.g. downloaded from YouTube): swap
  them for free business-licensed ones (Pixabay, Freesound CC0).
- The iMac has limited free disk space (about 21 GB). Check before big renders
  and clean up temp files.

## Which tool for which job
| Job | Use |
|---|---|
| Edit, cut, resize, caption, reframe video/audio, transitions, sound mixing; TikTok/Reels/YouTube exports | **ffmpeg-skill** (local, free) |
| Ads, promos, product spots (SHIFT) | **motion-kit: premium-commercial-style** first (Lexus-level bar), then build in After Effects or Remotion |
| Explainers, history and story videos (MOX) | **motion-kit: documentary-motion-style** first (the quality bar), then build GFX in **Remotion** or **After Effects**; FFmpeg only for assembly |
| Motion graphics, kinetic text, title cards, logo stings | **Remotion** (motion-kit) or **After Effects** via the AfterEffects connector |
| Upscale for sharp close-ups, slow motion, cut-outs, depth/parallax | **free-ai-kit: local-ai-tools** (Real-ESRGAN, RIFE, rembg, Depth Anything) |
| Fine editing the user wants to do by hand | **Premiere Pro** hand-off files (XML timeline, .srt, separate layers) |
| Voiceover, narration, audiobook, read text aloud, clone voice, transcribe | **my-voice-setup** skill (VoiceStudio, local, free) |
| Photoshop-style edits, background removal, social resizes, PDFs, Adobe Stock, Express designs | **Adobe** connector |
| Landing page / website build | **taste-skill** for a polished company site; **design-kit: landing-page-design** for conversion-focused pages |
| Polish or critique an existing design | **impeccable** (`/impeccable polish`, `audit`, `critique`) |
| Animation, motion, gestures, UI polish | **emil-design** skills |
| Brand identity, brand voice, slides, design systems, Figma | **design-kit** |
| Find a free API / data source | **dev-kit: public-apis** |
| Drive desktop apps (GIMP, Blender, OBS, LibreOffice...) | **cli-hub** (only if installed) |
| Social posting/scheduling | **Buffer** or **Metricool** connectors |
| Docs, Drive, Gmail-style work | Google Docs / Google Drive connectors |

## Money rule: FREE ONLY
The user is not spending money. Use only free tools and free plans.
- Never use, suggest, or sign up for anything that costs money, uses paid
  credits, or needs a paid plan. If unsure whether something is free, ask
  first; never guess.
- **ElevenLabs**: don't use. Free plan has no cloning and no commercial use.
- **Adobe**: no Adobe Stock licensing, no Firefly/generative features, nothing
  that spends credits. Only features that cost nothing on their account; ask
  first if unsure.
- Stock footage, photos, music: only free sources whose licence allows
  business use (e.g. Pexels, Pixabay, Unsplash). Tell the user the licence.
- Posting: free plans of Buffer or Metricool only.
- Voice: VoiceStudio with MOSS-TTS-Nano (free, commercial OK).

## Adding new tools
The user's tools live in their private GitHub repo
`theguiltyparties/claude-arsenal` (a plugin marketplace). New skills get added
there, then installed in Claude Code (`claude plugin marketplace update arsenal`
and `claude plugin install <name>@arsenal`) and in Cowork (Plugins → Add →
Manage marketplaces → sync, then install).
