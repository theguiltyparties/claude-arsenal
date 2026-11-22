# Arsenal

My curated Claude skills, packaged as one plugin marketplace so the same set
works in **Claude Code** and **Cowork**.

## Plugins

### `design-kit`
| Skill | Source | What it does |
|---|---|---|
| landing-page-design | elayadesign/ai-design-skills | Landing page from scratch: intake, structure, copy, visual system |
| figma-designer | elayadesign/ai-design-skills | Structured Figma work: variables, text styles, auto layout, components |
| frontend-design-direction | affaan-m/ecc | Stronger, product-specific design judgment for any web UI |
| design-system | affaan-m/ecc | Extract/audit design tokens from a codebase, with HTML preview |
| frontend-slides | affaan-m/ecc | Animated HTML presentations, PPTX → web, PDF export |
| brand-discovery | affaan-m/ecc | Multi-session brand identity interview |
| brand-voice | affaan-m/ecc | Writing-style profile built from real copy |
| motion-foundations | affaan-m/ecc | Motion tokens and springs for React / Next.js |
| motion-patterns | affaan-m/ecc | Ready-made animation patterns (modals, toasts, page transitions…) |
| frontend-a11y | affaan-m/ecc | Accessibility patterns for React / Next.js |

### `voice-kit`
| Skill | Source | What it does |
|---|---|---|
| voicestudio | debpalash/VoiceStudio | TTS, voice design, transcription, dubbing via the local VoiceStudio app |

**voice-kit only works on a computer where the VoiceStudio app is installed and
running** (it talks to `http://localhost:3900`). Install it from
https://github.com/debpalash/VoiceStudio/releases/latest.

### `ffmpeg-skill`
Local video/audio editing with FFmpeg (cut, join, reframe, captions, silence
removal, loudness, YouTube/TikTok exports). Not copied here: this entry points
at the author's own published plugin (kajisho5/ffmpeg-skill, `plugin` branch,
MIT), because it ships scripts and an MCP server and updates often.
**Needs FFmpeg 6.1+ and Python 3.10+ on the same computer**
(macOS: `brew install ffmpeg`).

### `cli-hub`
One skill that lets Claude drive desktop apps through CLI-Anything's tools.
When a task needs an app (GIMP, Blender, OBS, Inkscape, Audacity,
LibreOffice, Kdenlive, Krita, draw.io, Zotero and ~60 more), it installs just
that app's CLI with `cli-hub install <name>` instead of loading all 70 app
skills into every session. Copied from HKUDS/CLI-Anything (Apache-2.0).
**Needs Python 3 + pip, and the real app installed, on the same computer.**

### `cli-anything`
The official CLI-Anything plugin (referenced from HKUDS/CLI-Anything, `main`).
Adds `/cli-anything` commands to build, test and refine a new CLI for an app
that isn't in the hub yet. Only needed if you want to make new ones.

### `dev-kit`
| Skill | Source | What it does |
|---|---|---|
| public-apis | public-apis/public-apis | Search ~2,400 free APIs by keyword, category, key/no key, HTTPS, CORS |

The catalog is bundled (snapshot of commit 4c134b6); the skill can refresh it
from the live list. Needs Python 3.

## Install

### Claude Code (terminal / desktop / IDE)
```
/plugin marketplace add theguiltyparties/claude-arsenal
/plugin install design-kit@arsenal
/plugin install voice-kit@arsenal
/plugin install ffmpeg-skill@arsenal
/plugin install cli-hub@arsenal
/plugin install cli-anything@arsenal
/plugin install dev-kit@arsenal
```

### Cowork (Claude desktop app)
Add a plugin marketplace from GitHub in the app's plugin settings, enter
`theguiltyparties/claude-arsenal`, then install the plugins you want.

The repo is private, so the computer needs to be signed in to GitHub
(e.g. `gh auth login`) for the marketplace to load.

### Getting updates
After this repo changes: `/plugin marketplace update arsenal` in Claude Code
(Cowork refreshes from its plugin settings).

## Adding more

Two ways:

- **Copy** a plain skill (just a folder with `SKILL.md` and maybe some
  reference files) into a kit, as below. You control the version.
- **Point at** a repo that already publishes its own Claude plugin (it has a
  `.claude-plugin/` folder), the way `ffmpeg-skill` does: add an entry to
  `.claude-plugin/marketplace.json` with a `github` or `git-subdir` source.
  Updates come from the author.

To copy a skill:

1. Copy the skill folder (the one containing `SKILL.md`) into
   `plugins/<kit>/skills/`, or make a new kit under `plugins/` with its own
   `.claude-plugin/plugin.json` and add it to `.claude-plugin/marketplace.json`.
2. Copy the source repo's LICENSE into `licenses/`.
3. Bump the `version` in the kit's `plugin.json` and in `marketplace.json`.
4. Commit and push, then update the marketplace in Claude Code / Cowork.

Keep kits small: each installed skill adds to what Claude has to choose from in
every session. Install a kit only where you use it.

## Sources and licenses

Skills are copied unchanged from these upstream repos:

| Upstream | Commit | License |
|---|---|---|
| elayadesign/ai-design-skills | 456d9e0 | MIT |
| affaan-m/ecc | 4adeee6 | MIT |
| debpalash/VoiceStudio (skills/voicestudio only) | e9a8bc2 | AGPL-3.0 |
| kajisho5/ffmpeg-skill (referenced, not copied) | `plugin` branch | MIT |
| public-apis/public-apis (converted to a searchable catalog) | 4c134b6 | MIT |
| HKUDS/CLI-Anything (cli-hub-meta-skill copied; plugin referenced) | 34f5195 / `main` | Apache-2.0 |

Full license texts are in `licenses/`.
