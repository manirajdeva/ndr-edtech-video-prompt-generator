---
name: ndr-video-builder
description: Build a finished 9:16 (1080x1920, 30 FPS) NDR EdTech "30 Days of Snowflake" explainer MP4 from the user's own voice-over (day*.mp3) and its video_prompt_dayNN.md timing file. Use for "do it for dayNN", "make the video for day N", or any NDR EdTech animated explainer synced to supplied audio.
---

# NDR video builder

Turns `next days\dayNN\<audio>.mp3` + `video_prompt_dayNN.md` into `dayNN\NDR_Snowflake_DayNN_1080x1920.mp4`.
Real assets are made (HTML canvas animation -> PNG frames -> ffmpeg), not AI-generated clips.

## Hard rules (never break)
1. **Voice-over is never altered, regenerated or re-timed.** The audio is the master; video length = audio + ~1 s logo hold.
2. **NDR logo** (`assets/ndredtech_logo.png`) is used unchanged, via `logoCard`.
3. **Contact details exact**: Phone +91 87223 55666 | +91 81509 78999; Email ndredtech@gmail.com, info@ndredtech.com; Website www.ndredtech.com; handle @NDREDTECH. (If the prompt file omits them, still add them around "Contact NDR EdTech" and tell the user they can drop them.)
4. **Sound effects stay quiet** (user rule from Day 14): SFX gain multiplier 0.55 in the script, mix SFX volume 0.25, music 0.35, voice untouched.
5. Follow the prompt file's **palette, colour code and technical-accuracy rule** (e.g. "no numbers except the script's", "skipped data is dimmed, never deleted", "can help / can improve, never always"). Never use "Blow away" for data that is not really deleted.
6. Prompt-file timings are Whisper-measured: pause ends = phrase starts (most exact); "≈" times are estimates. Cut scenes inside pauses.
7. Where the audio differs from the script (e.g. Day 16 English outro), **follow the audio** and say so.
8. Report honestly: stills and frame counts were checked, the video was not watched or heard end to end. Flag the prompt's "please check" items (mis-heard words, estimated Follow/Contact times).

## Inputs
- `next days\dayNN\` : audio mp3, `video_prompt_dayNN.md` (production overview, palette, timing map, Appendix A trigger times, per-scene motion + overlay lists).

## Project layout (`dayNN\`)
`head.html` (canvas, palette consts, helpers, bg) + `shared.html` (dpanel, ringBurst, flash, icoCircle, igIcon, cap, cursorArrow) + `objs*.html` (day-specific shapes) + `scenes_*.html` (scenes + master `SC` table, `hud`, `window.renderFrame(t)`), concatenated:
`cat head.html shared.html objs.html objs2.html helpers.html scenes_a.html scenes_b.html > index.html`
Also `render.js`, `shot.js`, `mk6.sh`, `package.json`, `node_modules` (junction to day8\node_modules), `assets\` (voiceover.mp3, logo, sfx.wav, music.wav, mix.wav), `out\`.
Start a new day by copying the previous day's folder files and swapping palette + DUR in `head.html` (`DUR` = audio length + ~1.0).

## Workflow
1. Read the prompt file: palette, rules, "please check" list, timing table, Appendix A, per-scene overlays. Get audio length with ffprobe.
2. Scaffold `dayNN` from the previous day; set palette constants and `DUR`.
3. Write scenes as `fn(u, s)` with `s` = absolute audio seconds, deterministic (time-driven, no state). Helpers: `kin` (kinetic text), `cap` (caption pill), `sec(s,a,b,fn,{f,out})` (fade window), `ebo/eo/eio` easing, `P(t,a,b)`, `rr`, `pill`, `tbl`, `honey/tile`, `dive/pressT`, `logoCard`.
   Standard order: hook (title + DAY NN pill) -> question/problem scenes -> title reveal -> "Welcome to NDR EdTech" -> concept scenes -> banking example (with SQL typed line by line) -> "Keep it simple" recap -> series card (30 nodes, node NN lights on the number word) + next-topic teaser -> Follow -> Contact -> end veil with "Let's Learn and Grow Together!".
   HUD (logo dot, title, progress bar) hides during contact/end.
4. Preview: `node shot.js t1 t2 ...` writes `out/s_<t>.png`; `bash mk6.sh m.png t1..t6` makes a montage (run inside `out/`). Check layout, overlaps, text fit, safe zone; fix; re-check. (Gotcha: reset `ctx.shadowOffsetY` with `shadowBlur`; `shot.js` names files with `Number(t)`.)
5. Render 6 parallel chunks (N = DUR*30 frames; step = N/6, last chunk takes the remainder):
   `for i in 0..5: nohup node render.js $((i*step)) $((i+1)*step) out/part$i.mp4 &`
   Wait until all six open with ffprobe; verify each chunk's frame count (a chunk can still be finalising -> "moov atom not found" means wait). Do not poll with node.exe checks.
6. SFX: copy last day's `tools/dayN_sfx.py` to `dayNN_sfx.py`, set `DUR`, rng seed, `GM` (0.55) and rewrite the event list: a soft whoosh ~0.3 s before each scene cut, pop/ding on each overlay trigger time, ticks for sweeps/loading, key clicks for code typing, chime for success/reveal, warn for problems, impact on flashes. Output `assets/sfx.wav`, `assets/music.wav`.
7. Join and mux:
   - `ffmpeg -f concat -safe 0 -i out/list.txt -c copy out/video_all.mp4` (list.txt has bare `part0.mp4`..`part5.mp4`)
   - mix: `[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[v1][v2];[1:a]volume=0.35[m];[m][v2]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=400[md];[2:a]volume=0.25[sx];[v1][md][sx]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.93,apad=pad_dur=3` with `-t DUR` -> `assets/mix.wav`
   - mux: `-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart -t DUR` -> `NDR_Snowflake_DayNN_1080x1920.mp4`
   - verify: h264 1080x1920 30/1, duration = DUR, frame count = DUR*30.
8. Final message: file link, specs, what was verified, scene summary, palette/accuracy rules applied, SFX note, contact-details note, and the "please check by ear" items.

## Environment
Windows; Chrome at `C:/Program Files/Google/Chrome/Application/chrome.exe` driven by puppeteer-core; ffmpeg on PATH; Python (numpy, wave) for SFX; Whisper (faster-whisper) only if timings must be re-measured: `python -I tools/transcribe.py <audio> <out.json> en`.

---

## Prompt template (to ask any assistant for a day)

> Build the NDR EdTech "30 Days of Snowflake" Day NN video from `next days\dayNN\` (audio + video_prompt_dayNN.md).
> 9:16, 1080x1920, 30 FPS. Use my voice-over unchanged, my NDR logo unchanged, and the exact contact details. Follow the prompt file's palette, colour code and technical-accuracy rules. Sync every overlay to the Whisper-measured times. Add quiet sound effects and a soft music bed ducked under the voice. Deliver an MP4 plus the project folder, and list anything I should check by ear.
