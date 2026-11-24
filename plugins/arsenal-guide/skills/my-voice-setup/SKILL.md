---
name: my-voice-setup
description: How this user's local voice studio works and which voice engine is allowed for what. Use for any voiceover, narration, audiobook, book promo, TikTok/Reels voice, reading text aloud, text-to-speech, voice cloning, "use my voice", dubbing or transcription request, before touching VoiceStudio or ElevenLabs.
---

# My voice setup

## Where it runs
- **VoiceStudio** runs in Docker on the user's Intel iMac: container
  `voicestudio`, image `ghcr.io/debpalash/voicestudio:latest`, port
  `127.0.0.1:3900`, data volume `omnivoice-data`, `--restart unless-stopped`.
- Web page: http://localhost:3900. API base: http://localhost:3900.
- API key: in `~/.voicestudio-key`. Read it from the file; **never print it**.
  To let the user log in, copy it to their clipboard: `pbcopy < ~/.voicestudio-key`.
- Only Claude running **on the Mac** can reach it. A cloud session cannot.
- If it's down: check Docker Desktop is running, then `docker start voicestudio`.
- Engine installs from the web page are blocked ("Remote installation is
  disabled") because Docker isn't loopback. Install from inside the container
  using VoiceStudio's own installer, never `pip install` into VoiceStudio's main
  Python environment: that breaks its torch/transformers.
- Stay on the `:latest` image: `:stable` has the MOSS `set + list` bug (#4063).

## Which engine (licences matter: the user sells books)
| Engine | Clones voices | Commercial use | Use for |
|---|---|---|---|
| **MOSS-TTS-Nano** (default) | yes | **allowed** (Apache-2.0) | Anything the user will sell or publish: audiobooks, book promos, ads, monetized videos |
| KittenTTS | no, 8 presets | allowed | Quick English narration without cloning |
| OmniVoice | yes | **NOT allowed** (CC-BY-NC) | Personal experiments only. Never for books, promos or paid work |

If unsure whether a job is commercial, assume it is and use MOSS-TTS-Nano.
Before switching engines for a commercial job, check its licence card says
"Commercial use of generated audio: Allowed".

## The user's voice
- Saved voice profiles (cloned from the user's own recording, with consent):
  - **"Mark Voice Clone (short)"**: **use this one with MOSS-TTS-Nano.**
  - "Mark Voice Clone" (long sample): makes MOSS-TTS-Nano produce gibberish.
    Don't use it with MOSS.
  Use the short one whenever the user says "my voice".
- Clone only voices the user has permission to use.

## Writing scripts for it
- MOSS-TTS-Nano does not understand ElevenLabs-style tags like `[excited]`,
  `[whisper]` or `[short pause]`. Strip them; use punctuation and short
  sentences for pacing instead.
- The iMac renders on its CPU. Split long scripts into paragraphs (under
  ~800 characters each) and render them one at a time, then join with
  ffmpeg-skill.
- Save finished audio in `~/ClaudeWork`.

## Where they sell
Store rules on AI narration vary (Audible/ACX in particular). If the user is
publishing an audiobook, remind them to check that store's current AI-voice
policy before uploading.
