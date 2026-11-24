---
name: premium-commercial-style
description: The quality bar and build method for this user's ads and product spots. Luxury-automotive (Lexus-level) polish combined with what wins on TikTok, Reels and Shorts. Use for ANY commercial, promo, product video, brand spot, launch teaser or social ad (e.g. SHIFT), or when the user says premium, high-end, luxury, Lexus, glossy, cinematic, or "best ads on TikTok". Read before planning or rendering.
---

# Premium commercial style (luxury and top social ads)

The bar: a luxury car commercial's restraint and craft, cut for a phone feed.
Template transitions, shaky text, stock-looking glitches and "busy" edits read
as cheap. **Luxury is control: fewer, better moves, precise sound, perfect
light.**

## 0. Build method
1. **Study before designing.** Make 0.5 s contact sheets of the project's
   footage, its existing cuts and any reference spots. Write a **spot bible**:
   product truth (the one feeling to sell), palette from product and grade,
   type, motion rules, sound palette, shot list. Show it first.
2. **Beat sheet** against the music and VO, one row per beat, product moments
   marked.
3. **Build:** After Effects (via the AfterEffects connector) or Remotion
   (motion-kit) for the product hero, light sweeps, type and end card.
   free-ai-kit for upscaling (Real-ESRGAN) and slow motion (RIFE). FFmpeg only
   for conform, assembly, loudness and exports.
4. **15 s preview of the hardest moments first**, harsh self-QA (section 8),
   then the full render.

## 1. Structure (15 s; scale up for 30 s)
- **0–1 s: hook.** A striking product or sensory frame from frame 1: macro
  condensation rolling, the tab cracking, light catching the logo. No logo
  card or slow fade-in first. A pattern interrupt that stops the scroll.
- **1–10 s: desire.** Lifestyle and product interleaved, with the product on
  screen at least every 3 s. One idea, built in three to four beats.
- **10–13 s: payoff.** The hero moment: pour, sip, can turn, the "ahh".
- **13–15 s: end card.** Product hero, logo, tagline. Clean, held, no clutter.
- Optional TikTok-native open: one line of on-screen text that sets up
  curiosity, but still with a premium look.

## 2. Camera and shots (the luxury grammar)
- **Slow, controlled, motivated moves:** dolly-ins, slow orbits, slider
  reveals, top-down rotations. Speed ramps (fast into slow on the key moment,
  done with RIFE) instead of whips.
- **Macro and detail:** condensation, bubbles, the tab, the logo emboss, the
  rim of the can, fingertips. Punch in on source footage; upscale first past
  about 1.3× (Real-ESRGAN).
- **Shallow depth of field:** rack focus and soft foregrounds. Add depth blur in
  AE with a depth map (free-ai-kit) when the footage is flat.
- **Hold shots long enough to breathe** on hero moments (1–2 s), and cut fast
  only in the build-up. Rhythm contrast is what feels expensive.

## 3. Light and grade
- **Light sweeps / specular glints** across the can and logo (AE: a gradient
  ramp masked to the product, screen blend, animated across). One per hero shot.
- **Rim light and edge glow** on the product silhouette against dark grounds.
- **Grade:** deep, clean blacks; controlled highlights; product colours true and
  saturated; skin natural. Use the project's LUT, then unify all shots so the
  AI-generated clips match. Fine grain (1–2%) and a subtle vignette tie it
  together.
- Condensation and liquid should look **cold and wet**: lift the specular
  highlights and add a slight cool cast to the product only.

## 4. Product hero and end card
- Build the hero from the **current** product artwork (never an outdated design):
  a 2.5D can turn (cut-out plus displacement, or a cylinder wrap in AE), a slow
  push, a light sweep across the logo, droplets (particle or overlay), a soft
  reflection on the surface below.
- End card: product centred or rule-of-thirds, logo, tagline, plenty of
  negative space, held 1.5–2 s. No more than two lines of type.

## 5. Typography
- **Minimal and expensive:** one refined family (the brand's, or a clean
  geometric or grotesk such as Manrope, Sora, Plus Jakarta Sans or Barlow;
  avoid overused Inter), generous tracking on caps, thin-to-medium weights
  for luxury, bold only for the tagline.
- **Three words or fewer per frame.** Text enters with a slow mask reveal,
  fade-up or blur-in tied to the music, and exits cleanly.
- Captions for VO on social: small, elegant, lower third, inside the safe zones
  (9:16: keep roughly the top 220 px and bottom 420 px clear).

## 6. Transitions
- Mostly **clean cuts on the beat**. Motivated transitions only: match cuts
  (can shape to round object, pour to splash), **light-flash / lens-flare
  wipes** on beat drops, a speed-ramp push into the next shot, a liquid or
  droplet wipe once at most.
- **No** glitch, RGB split, film burn, page tear or whip pans in luxury spots.
- Every motivated transition gets a designed sound.

## 7. Sound design and mix (half the "premium" feeling)
- **ASMR product layer:** tab crack, fizz, pour, ice clink, condensation drip,
  swallow and "ahh", each synced to the exact frame and recorded clean.
- **Air:** soft whooshes on moves (low and smooth, not cartoony), sub swells
  into the hero moment, a short silence before the crack.
- **Music:** sparse and modern; edit cuts to the beat; the drop lands on the
  hero moment.
- Free commercial sources only (Pixabay, Freesound CC0, Sonniss GDC bundles);
  never sounds ripped from YouTube.
- **Mix:** VO clear around −14 LUFS integrated; music ducked under VO; product
  SFX forward; true peak ≤ −1 dBTP; check on phone speakers as well.

## 8. QA (be harsh)
- Would this sit next to a Lexus, Apple or premium beverage spot without looking
  cheap? If any effect looks like a template, cut it.
- Product on screen in the first second, then at least every 3 seconds? Current
  design only?
- Every key action (crack, pour, sip) **seen and heard on the same frame**?
- Consistent grade across all shots; no mismatched AI clips?
- Type minimal, refined, inside the safe zones?
- Rhythm: fast build-up, held hero, clean end card?
- Mix: product sounds crisp, VO clear, no clipping, around −14 LUFS?
- All fonts, SFX, music and footage licences noted? Free only?

## Versions
- 9:16 (TikTok/Reels/Shorts): re-frame per shot, product always in frame.
- 4:5 (Instagram feed) and 16:9 (YouTube/LinkedIn).
- Thumbnail: product hero plus a 1–3 word hook.

Free-only: no paid AI video generation (Flow, Veo, TopView, Higgsfield,
MiniMax H3), no paid stock, no ElevenLabs credits.
