---
name: my-toolkit
description: Map of this user's tools and when to use each. Use at the start of any creative, writing, video, audio, voice, design, website, publishing, social-media or research task, or whenever the user asks "can you…", "what should I use…", or forgets which tool does what. The user is not technical; pick the right tool yourself instead of asking them.
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

## Which tool for which job
| Job | Use |
|---|---|
| Edit, cut, resize, caption, reframe video/audio; TikTok/Reels/YouTube exports | **ffmpeg-skill** (local, free) |
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

## Paid services: ask first
- **ElevenLabs** connector: free plan only. No voice cloning, no commercial
  use. Don't use it for anything the user will sell; use VoiceStudio instead.
  Every generation spends credits, so confirm before using it.
- Anything else that costs money or credits: say so and ask first.

## Adding new tools
The user's tools live in their private GitHub repo
`theguiltyparties/claude-arsenal` (a plugin marketplace). New skills get added
there, then installed in Claude Code (`claude plugin marketplace update arsenal`
and `claude plugin install <name>@arsenal`) and in Cowork (Plugins → Add →
Manage marketplaces → sync, then install).
