# Thirty Days of Snowflake – Day 23: COPY INTO vs Snowpipe
Video prompt package (NDR EdTech) — `Audio\day23.mp3` + `days-scripts\day23.txt`, analysed with Whisper

> **Timing status: MEASURED from day23.mp3 (116.04 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **The opening (0–2.1 s):** the line "Andaru ela unnaru?" was removed from this recording (you confirmed this), so the opening is "Hello guys! … Oka interesting situation!" ("Hello guys!" 0.00–0.53 s, then one short phrase 0.95–2.12 s). Your `days-scripts\day23.txt` still contains the removed line; the package follows the audio.
> 2. **The Contact line (111–114 s):** Whisper heard "…for this course, **contact us at ndritech.com**". Your script says only "Full course details kosam NDR EdTech ni Contact avvandi!" and has no website. **I did not add any website to the overlay.** If the narrator really says a website, tell me the exact words and I will add the known NDR EdTech website only after you confirm.
> 3. **"AWS S3" versus "Amazon S3":** Whisper writes "Amazon S3". Your script says "AWS S3", so the overlays use **AWS S3**. Please listen once to confirm.
> 4. **15.94–17.33 s** is your scripted `[pause]`, a real 1.39 s silence. The visuals hold a calm beat there.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 23: COPY INTO vs Snowpipe |
| Duration | **116.04 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,481 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day23.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (29 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Batch vs Stream" (new for Day 23)
| Role | HEX | Use |
|---|---|---|
| Background | `#1B1A22` | Base, gradients (charcoal violet-grey) |
| COPY INTO Rose | `#FF6BA8` | **COPY INTO**: a command that is run, loads a batch |
| Snowpipe Turquoise | `#19E0C8` | **Snowpipe**: a pipe with a continuous, automatic flow |
| Event Yellow | `#FFE14D` | The **event notification** (a bell) that triggers Snowpipe |
| File Peach | `#FFC9A3` | Data files (in AWS S3 or a stage) |
| Cloud Glass | `#EDEFF7` | Tables, stages, SQL panels, neutral glass |
| Primary text | `#FAFAFD` | Titles, labels |
| Secondary text | `#A3A1B5` | Captions |

**Colour code (use in every scene):** COPY INTO = **Rose** (a button that is pressed) · Snowpipe = **Turquoise** (a pipe that keeps flowing) · event notification = **Yellow bell** · files = **Peach** cards · tables and stages = **Cloud Glass**.

**The core visual rule (technical accuracy):** **COPY INTO is a Snowflake command that is executed**: when it runs, it loads files from a stage into a table; it is usually used for **batch loading**. **Snowpipe is a continuous data ingestion service**: when new files arrive, event notifications (or other supported automation mechanisms) trigger the load, so nobody has to run COPY INTO every time. Show COPY INTO with a visible "run" action every time, and Snowpipe with a Yellow bell and no run action. Show "100 GB" only as the script's example. No timings, costs or latency claims.

### Motion effects used (from the skill's effects library)
Live cursor, Day dial, Blade slice, Head stack, Press font, Letter dive, Impact frame, Liquid glass, Code body, Rack focus, Comment drop, Orbit ring. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–2.37 | "Hello guys! … Oka interesting situation!" (0.00–2.12) | Curious | Title hook |
| 2 | 2.37–16.64 | "Mee company ki daily 100 GB data AWS S3 nunchi Snowflake loki vasthundhi anukondi." (2.61–8.40) · "Prathi sari Data Engineer manual ga COPY INTO command execute cheyyala?" (8.87–12.62) · "Leda new files vachinappudu automatic ga load avvala?" (13.02–15.94) · *[scripted pause 15.94–17.33]* | Curious | Daily 100 GB, manual or automatic? |
| 3 | 16.64–23.45 | "Snowflake lo ee rendu approaches ki solutions unnayi!" (17.33–20.02) · "Adhe COPY INTO and Snowpipe!" (20.41–22.14) · "Let's understand!" (22.59–23.17) | Excited, reveal | Two solutions, title |
| 4 | 23.45–25.49 | "Welcome to NDR EdTech!" (23.73–25.25) | Welcoming | Brand welcome |
| 5 | 25.49–38.26 | "First, COPY INTO!" (25.72–26.79) · "COPY INTO anedhi Snowflake command." (27.24–28.95) · "Manam execute chesinappudu external stage or internal stage nunchi files ni Snowflake table loki load chesthundhi." (29.39–35.40) · "Usually batch loading scenarios lo use chestham." (35.78–38.02) | Clear | COPY INTO |
| 6 | 38.26–52.56 | "Second, Snowpipe!" (38.50–39.61) · "Snowpipe anedhi continuous data ingestion service." (40.06–42.72) · "New files vachinappudu event notifications or supported automation mechanisms through loading trigger avuthundhi." (43.15–48.56) · "Manam every time manually COPY INTO execute cheyyalsina avasaram undadhu." (48.91–52.32) | Clear | Snowpipe |
| 7 | 52.56–83.42 | "Oka Banking project example teesukundham." (52.79–54.58) · "Daily midnight ki AWS S3 lo 100 GB transaction files land avuthunnayi anukondi." (54.92–60.37) · "Manam scheduled batch process run chesi COPY INTO use cheyyachu." (60.73–63.83) · "Kaani files throughout the day continuously land avuthunte, Snowpipe use chesi automatic ingestion setup cheyyachu." (64.18–70.13) · "COPY INTO CUSTOMER FROM @CUSTOMER_STAGE;" (70.59–73.63) · "Snowpipe kosam:" (74.07–74.82) · "CREATE PIPE CUSTOMER_PIPE" (75.14–77.19) · "AUTO_INGEST = TRUE" (77.44–79.66) · "AS COPY INTO CUSTOMER FROM @CUSTOMER_STAGE;" (79.86–83.20) | Storytelling, focused | Banking: nightly batch, continuous files, two SQL statements |
| 8 | 83.42–95.86 | "So, simple ga gurthupettukondi!" (83.64–85.26) · "COPY INTO – Command-based data loading." (85.64–87.59) · "Snowpipe – Event-driven automated data ingestion." (88.01–90.73) · "Batch loading kosam COPY INTO useful." (91.10–93.05) · "Continuous file ingestion kosam Snowpipe useful." (93.32–95.65) | Confident | Two-card recap and when to use which |
| 9 | 95.86–105.43 | "Idi mana Thirty Days of Snowflake series lo Day Twenty-Three!" (96.07–99.03) · "Next video lo Snowpipe Auto-Ingest ela work avuthundho AWS S3 real-time example tho explain chesthanu." (99.39–105.26) | Upbeat | Day 23 card, Snowpipe Auto-Ingest teaser |
| 10 | 105.43–116.04 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (105.60–110.79) · "Full course details kosam NDR EdTech ni Contact avvandi!" (111.15–113.98) · "Let's Learn and Grow Together!" (114.28–115.74) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.53–0.95, 2.12–2.61, 8.40–8.87, 12.62–13.02, 15.94–17.33 (the scripted `[pause]`), 20.02–20.41, 22.14–22.59, 23.17–23.73, 25.25–25.72, 26.04–26.29, 26.79–27.24, 28.95–29.39, 35.40–35.78, 38.02–38.50, 38.85–39.16, 39.61–40.06, 42.72–43.15, 48.56–48.91, 52.32–52.79, 54.58–54.92, 60.37–60.73, 63.83–64.18, 70.13–70.59, 73.63–74.07, 74.82–75.14, 75.73–75.94, 77.19–77.44, 79.66–79.86, 83.20–83.64, 83.91–84.17, 85.26–85.64, 86.20–86.44, 87.59–88.01, 88.43–88.76, 90.73–91.10, 93.05–93.32, 95.65–96.07, 99.03–99.39, 105.26–105.60, 110.79–111.15, 113.98–114.28, 115.74–116.04.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee company ki daily 100 GB data AWS S3 nunchi Snowflake loki vasthundhi anukondi. | daily ≈3.6 · **100 GB** ≈4.3 · AWS S3 ≈5.6 · Snowflake ≈6.8 |
| Prathi sari Data Engineer manual ga COPY INTO command execute cheyyala? | Data Engineer ≈9.5 · manual ga ≈10.4 · COPY INTO command execute ≈11.2 |
| Leda new files vachinappudu automatic ga load avvala? | new files ≈13.6 · automatic ga ≈14.6 · load ≈15.4 |
| Snowflake lo ee rendu approaches ki solutions unnayi! | rendu approaches ≈18.4 · solutions ≈19.4 |
| Adhe COPY INTO and Snowpipe! | Adhe 20.41 · COPY INTO ≈21.0 · Snowpipe ≈21.6 |
| Let's understand! / Welcome to NDR EdTech! | Let's 22.59 · Welcome 23.73 · NDR ≈24.3 · EdTech ≈24.8 |
| First, COPY INTO! | First 25.72 · COPY INTO 26.29 |
| COPY INTO anedhi Snowflake command. | COPY INTO 27.24 · Snowflake command ≈28.0 |
| Manam execute chesinappudu external stage or internal stage nunchi files ni Snowflake table loki load chesthundhi. | execute ≈29.8 · external stage ≈31.0 · internal stage ≈32.2 · files ≈33.2 · load ≈34.6 |
| Usually batch loading scenarios lo use chestham. | batch loading ≈36.4 |
| Second, Snowpipe! | Second 38.50 · Snowpipe 39.16 |
| Snowpipe anedhi continuous data ingestion service. | continuous ≈41.0 · data ingestion service ≈41.6 |
| New files vachinappudu event notifications or supported automation mechanisms through loading trigger avuthundhi. | New files 43.15 · event notifications ≈44.6 · supported automation mechanisms ≈46.0 · trigger ≈48.0 |
| Manam every time manually COPY INTO execute cheyyalsina avasaram undadhu. | every time manually ≈49.6 · COPY INTO execute ≈50.6 · avasaram undadhu ≈51.7 |
| Oka Banking project example teesukundham. | Banking ≈53.2 · example ≈54.0 |
| Daily midnight ki AWS S3 lo 100 GB transaction files land avuthunnayi anukondi. | Daily midnight ≈55.2 · AWS S3 ≈56.6 · **100 GB** ≈57.6 · transaction files ≈58.4 · land ≈59.4 |
| Manam scheduled batch process run chesi COPY INTO use cheyyachu. | scheduled batch process ≈61.2 · COPY INTO ≈62.6 |
| Kaani files throughout the day continuously land avuthunte, Snowpipe use chesi automatic ingestion setup cheyyachu. | throughout the day ≈65.2 · continuously land ≈66.4 · Snowpipe ≈67.6 · automatic ingestion ≈68.8 |
| COPY INTO CUSTOMER FROM @CUSTOMER_STAGE; | COPY INTO CUSTOMER 70.59–72.0 · FROM @CUSTOMER_STAGE ≈72.2–73.63 |
| Snowpipe kosam: | Snowpipe kosam 74.07 |
| CREATE PIPE CUSTOMER_PIPE | CREATE PIPE 75.14 · CUSTOMER_PIPE 75.94 |
| AUTO_INGEST = TRUE | AUTO_INGEST 77.44 · TRUE ≈79.0 |
| AS COPY INTO CUSTOMER FROM @CUSTOMER_STAGE; | AS COPY INTO CUSTOMER 79.86–81.4 · FROM @CUSTOMER_STAGE ≈81.5–83.2 |
| So, simple ga gurthupettukondi! | So 83.64 · gurthupettukondi ≈84.4 |
| COPY INTO – Command-based data loading. | COPY INTO 85.64 · Command-based data loading 86.44 |
| Snowpipe – Event-driven automated data ingestion. | Snowpipe 88.01 · Event-driven automated data ingestion 88.76 |
| Batch loading kosam COPY INTO useful. | Batch loading ≈91.3 · COPY INTO useful ≈92.2 |
| Continuous file ingestion kosam Snowpipe useful. | Continuous file ingestion ≈93.5 · Snowpipe useful ≈94.8 |
| Idi mana Thirty Days of Snowflake series lo Day Twenty-Three! | Thirty ≈96.8 · Snowflake ≈97.5 · Twenty-Three ≈98.2 |
| Next video lo Snowpipe Auto-Ingest ela work avuthundho AWS S3 real-time example tho explain chesthanu. | Snowpipe Auto-Ingest ≈100.3–101.9 · AWS S3 ≈102.6 · real-time example ≈103.4 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈107.4 · NDR EdTech ≈108.4–109.4 · **Follow** ≈109.8 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 111.15–112.2 · NDR EdTech ≈112.4 · **Contact** ≈113.2 (estimated) |
| Let's Learn and Grow Together! | Let's 114.28 · Together ≈115.2 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Event Yellow #FFE14D, File Peach #FFC9A3, Cloud Glass #EDEFF7, text #FAFAFD.*

**Object look (keep identical in every scene):** **files** = small Peach glass file cards. **AWS S3** = a generic cloud-bucket glyph (no AWS logo). **Stage** = a Cloud Glass portal window. **Snowflake table** = a Cloud Glass table block with rows of cells. **COPY INTO** = a Rose "run" button pressed by a cursor, then a batch of files moves together. **Snowpipe** = a Turquoise glass pipe with a continuous flow, plus a Yellow bell when a new file lands, and no cursor.

### Scene 1 – Hook (0.00–2.37 s · 2.37 s)
**Voice-over:** "Hello guys! Oka interesting situation!"
**Tone:** curious.
**Visual objective:** Welcome viewers and tease the situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Event Yellow #FFE14D, File Peach #FFC9A3, Cloud Glass #EDEFF7, text #FAFAFD. A charcoal space with soft light and drifting glass particles. A glowing Rose glass button and a Turquoise glass pipe float side by side at the upper-centre, with a few Peach file cards drifting between them. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–0.53 s: particles drift in on "Hello guys!".
- 0.95–2.12 s: the button and the pipe appear on "Oka interesting situation!".
- 2.12–2.37 s: soft light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at ≈1.9 s on "situation".
**Audio sync:** title lands at ≈1.0 s; the sweep completes in the pause at 2.12–2.61 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 23".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – Daily 100 GB: manual or automatic? (2.37–16.64 s · 14.27 s)
**Voice-over:** "Mee company ki daily 100 GB data AWS S3 nunchi Snowflake loki vasthundhi anukondi. Prathi sari Data Engineer manual ga COPY INTO command execute cheyyala? Leda new files vachinappudu automatic ga load avvala?"
**Tone:** curious. The last 0.7 s is the start of the scripted pause.
**Visual objective:** Every day a lot of data arrives from AWS S3 into Snowflake: should it be loaded by running a command each time, or automatically when new files arrive?
Generate as **three shots (2a–2c)**.

**Shot 2a (2.37–8.64 s) – daily 100 GB from S3 to Snowflake:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1A22, File Peach #FFC9A3, Cloud Glass #EDEFF7, text #FAFAFD. On the left a large glass cloud-bucket (generic glyph, no logo) holding a heap of Peach file cards; on the right a Cloud Glass snowflake-crystal database. A broad band of Peach file cards flows from the bucket to the database, and a small calendar-page glyph shows that it happens daily. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 2.61–3.6 s the bucket and the database appear on "Mee company ki"; ≈3.6–5.6 s the band of cards starts on "daily 100 GB data" (100 GB ≈4.3 s); ≈5.6–8.4 s the band keeps flowing on "AWS S3 nunchi Snowflake loki vasthundhi anukondi".
Overlay (post): "DAILY 100 GB" at ≈4.3 s; "AWS S3 → SNOWFLAKE" from ≈5.6 s. Show "100 GB" as the script's example only.

**Shot 2b (8.64–12.82 s) – manually run COPY INTO each time?:**
"Same style and palette, plus COPY INTO Rose #FF6BA8. A glass cursor presses a Rose 'run' button beside the bucket; a batch of Peach cards moves across into the database. The cursor then returns to the button again and again, showing a repeated manual action. A soft question-mark glow pulses. No readable text, no logos, no watermark."
Motion: 8.87–9.8 s the button appears on "Prathi sari Data Engineer"; ≈10.4–11.2 s the cursor presses it on "manual ga"; ≈11.2–12.62 s the press repeats on "COPY INTO command execute cheyyala?". **Effect: Live cursor.**
Overlay (post): "RUN COPY INTO EVERY TIME?" from 8.87 s.

**Shot 2c (12.82–16.64 s) – or load automatically when new files arrive?:**
"Same style and palette, plus Snowpipe Turquoise #19E0C8 and Event Yellow #FFE14D. A single new Peach file card lands in the bucket and a small Yellow bell rings. A faint Turquoise pipe lights up by itself and the file slides into the database with no cursor. A soft question-mark glow pulses. Hold a calm still frame for the last 0.7 s. No readable text, no logos, no watermark."
Motion: 13.02–14.4 s a new file lands on "Leda new files vachinappudu" (new files ≈13.6 s); ≈14.6–15.94 s the bell rings and the pipe lights on "automatic ga load avvala?"; 15.94–16.64 s calm hold during the scripted pause.
Overlay (post): "OR AUTOMATICALLY WHEN NEW FILES ARRIVE?" from 13.02 s.

**Audio sync:** band at ≈3.6 s; cursor at ≈10.4 s; new file at ≈13.6 s; bell at ≈14.6 s.
**Negative prompt (all shots):** "Real AWS logos, readable text, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Two solutions: COPY INTO and Snowpipe (16.64–23.45 s · 6.81 s)
**Voice-over:** "Snowflake lo ee rendu approaches ki solutions unnayi! Adhe COPY INTO and Snowpipe! Let's understand!"
**Tone:** excited, reveal.
**Visual objective:** Snowflake has solutions for both approaches: COPY INTO and Snowpipe.
Generate as **two shots (3a, 3b)**.

**Shot 3a (16.64–20.22 s) – two approaches, two solutions:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Cloud Glass #EDEFF7, text #FAFAFD. The screen divides into two halves by a thin light line: on the left a Rose 'run' button and on the right a Turquoise pipe, each in a soft spotlight. Mysterious, then hopeful. Slow push-in. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 17.33–18.4 s the dividing line draws on "Snowflake lo ee rendu approaches"; ≈18.4–20.02 s the two spotlights light on "ki solutions unnayi!" (solutions ≈19.4 s). **Effect: Blade slice** — a thin line slices the screen into the two halves at ≈18.4 s.
Overlay (post): "TWO APPROACHES, TWO SOLUTIONS" from 17.33 s.

**Shot 3b (20.22–23.45 s) – COPY INTO and Snowpipe, let's understand:**
"Same style and palette. The two halves come together under a glass snowflake-crystal emblem. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark."
Motion: 20.41–22.14 s the title lands on "Adhe COPY INTO and Snowpipe!" (**Effect: Impact frame** — one-frame flash at 20.41 s; **Effect: Letter dive** — the letters settle fully before 22.0 s); 22.59–23.17 s a subtitle pops in on "Let's understand!".
Overlay (post): "COPY INTO vs SNOWPIPE" at 20.41 s; "LET'S UNDERSTAND!" at 22.59 s.

**Audio sync:** line at 17.33 s; title at 20.41 s; subtitle at 22.59 s.
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Welcome (23.45–25.49 s · 2.04 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, text #FAFAFD. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft rose-and-turquoise glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 23.73–25.25 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 23.73 s; "NDR" at ≈24.3 s; "EdTech" at ≈24.8 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – 1 · COPY INTO (25.49–38.26 s · 12.77 s)
**Voice-over:** "First, COPY INTO! COPY INTO anedhi Snowflake command. Manam execute chesinappudu external stage or internal stage nunchi files ni Snowflake table loki load chesthundhi. Usually batch loading scenarios lo use chestham."
**Tone:** clear.
**Visual objective:** COPY INTO is a Snowflake command; when we execute it, it loads files from an external or internal stage into a table; it is usually used for batch loading.
Generate as **three shots (5a–5c)**.

**Shot 5a (25.49–29.17 s) – a Snowflake command:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Cloud Glass #EDEFF7, text #FAFAFD. A large glowing Rose glass 'run' button with a small command-prompt glyph (a greater-than sign and a cursor line, no readable text) rises at the centre. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 25.72–26.04 s the badge appears on "First,"; 26.29–26.79 s the button lands on "COPY INTO!" (**Effect: Press font** — "COPY INTO" presses in at 26.29 s); 27.24–28.95 s the command-prompt glyph lights on "COPY INTO anedhi Snowflake command".
Overlay (post): "1 · COPY INTO" at 25.72 s; "A SNOWFLAKE COMMAND" from 27.24 s.

**Shot 5b (29.17–35.59 s) – executed: files from a stage into a table:**
"Same style and palette, plus File Peach #FFC9A3. A Cloud Glass portal window (a stage) holds a stack of Peach file cards on the left and a Cloud Glass table block on the right. A cursor presses the Rose button, and the stack of files moves together through the portal and fills the table's rows. Two small tags on the portal show 'external' (a cloud glyph) and 'internal' (a box glyph). Calm, satisfying. No readable text, no logos, no watermark."
Motion: 29.39–30.4 s the cursor presses the button on "Manam execute chesinappudu" (execute ≈29.8 s); ≈31.0–32.2 s the two stage tags light on "external stage or internal stage nunchi" (external stage ≈31.0 s, internal stage ≈32.2 s); ≈33.2–35.4 s the files move and fill the table on "files ni Snowflake table loki load chesthundhi" (load ≈34.6 s). **Effect: Live cursor.**
Overlay (post): "EXECUTE COPY INTO" from 29.39 s; "FILES FROM A STAGE (EXTERNAL OR INTERNAL)" from ≈31.0 s; "LOADED INTO A SNOWFLAKE TABLE" from ≈34.0 s.

**Shot 5c (35.59–38.26 s) – usually batch loading:**
"Same style and palette. A tidy batch (a crate of many Peach file cards) is loaded in one go: the cursor presses the button once and the whole crate moves into the table together. Calm, clear. No readable text, no logos, no watermark."
Motion: 35.78–36.4 s the crate appears on "Usually"; ≈36.4–38.02 s the whole crate moves on "batch loading scenarios lo use chestham" (batch loading ≈36.4 s). **Effect: Comment drop** — a small Rose note drops in beside the crate at ≈36.4 s.
Overlay (post): "USUALLY BATCH LOADING" from ≈36.4 s.

**Audio sync:** badge at 25.72 s; cursor at ≈29.8 s; stage tags at ≈31.0 and ≈32.2 s; crate at ≈36.4 s.
**Negative prompt (all shots):** "Real logos, readable fine text, COPY INTO shown without a run action, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – 2 · Snowpipe (38.26–52.56 s · 14.30 s)
**Voice-over:** "Second, Snowpipe! Snowpipe anedhi continuous data ingestion service. New files vachinappudu event notifications or supported automation mechanisms through loading trigger avuthundhi. Manam every time manually COPY INTO execute cheyyalsina avasaram undadhu."
**Tone:** clear.
**Visual objective:** Snowpipe is a continuous data ingestion service; new files trigger the load through event notifications or supported automation mechanisms, so there is no need to run COPY INTO manually every time.
Generate as **three shots (6a–6c)**.

**Shot 6a (38.26–42.93 s) – a continuous ingestion service:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1A22, Snowpipe Turquoise #19E0C8, File Peach #FFC9A3, Cloud Glass #EDEFF7, text #FAFAFD. A long glowing Turquoise glass pipe runs across the frame from a bucket-glyph on the left to a Cloud Glass table on the right; Peach file cards flow through it one after another in a steady stream. A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 38.50–38.85 s the badge appears on "Second,"; 39.16–39.61 s the pipe lights on "Snowpipe!" (**Effect: Press font** — "SNOWPIPE" presses in at 39.16 s); 40.06–42.72 s the steady stream flows on "Snowpipe anedhi continuous data ingestion service" (continuous ≈41.0 s).
Overlay (post): "2 · SNOWPIPE" at 38.50 s; "CONTINUOUS DATA INGESTION SERVICE" from 40.06 s.

**Shot 6b (42.93–48.74 s) – new files trigger the load:**
"Same style and palette, plus Event Yellow #FFE14D. A new Peach file card lands in the bucket and a Yellow bell rings; a thin Yellow line travels from the bell to the pipe, which lights up and carries that file into the table. This repeats with a second new file. No cursor appears anywhere. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 43.15–44.6 s the first new file lands on "New files vachinappudu"; ≈44.6–46.0 s the bell rings and the Yellow line travels on "event notifications" (event notifications ≈44.6 s); ≈46.0–48.56 s the pipe loads the files on "or supported automation mechanisms through loading trigger avuthundhi" (trigger ≈48.0 s). **Effect: Orbit ring** — a soft Yellow ring circles the bell once at ≈44.6 s.
Overlay (post): "NEW FILES ARRIVE" from 43.15 s; "EVENT NOTIFICATIONS OR SUPPORTED AUTOMATION MECHANISMS" from ≈44.6 s; "TRIGGER THE LOAD" from ≈48.0 s.

**Shot 6c (48.74–52.56 s) – no manual COPY INTO each time:**
"Same style and palette, plus COPY INTO Rose #FF6BA8. The Rose 'run' button from the last section appears faintly in the corner and fades away, unused, while the Turquoise pipe keeps loading new files by itself. Calm, clear. No readable text, no logos, no watermark."
Motion: 48.91–50.6 s the faint Rose button appears on "Manam every time manually COPY INTO execute"; ≈50.6–52.32 s it fades away on "cheyyalsina avasaram undadhu" (avasaram undadhu ≈51.7 s). **Effect: Rack focus** — focus pulls from the fading button to the working pipe at ≈50.6 s.
Overlay (post): "NO NEED TO RUN COPY INTO MANUALLY EVERY TIME" from ≈49.6 s.

**Audio sync:** badge at 38.50 s; bell at ≈44.6 s; trigger at ≈48.0 s; button fades at ≈51.0 s.
**Negative prompt (all shots):** "A cursor or run button used by Snowpipe, latency or cost claims, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (52.56–83.42 s · 30.86 s)
**Voice-over:** "Oka Banking project example teesukundham. Daily midnight ki AWS S3 lo 100 GB transaction files land avuthunnayi anukondi. Manam scheduled batch process run chesi COPY INTO use cheyyachu. Kaani files throughout the day continuously land avuthunte, Snowpipe use chesi automatic ingestion setup cheyyachu. COPY INTO CUSTOMER FROM @CUSTOMER_STAGE; Snowpipe kosam: CREATE PIPE CUSTOMER_PIPE AUTO_INGEST = TRUE AS COPY INTO CUSTOMER FROM @CUSTOMER_STAGE;"
**Tone:** storytelling, focused.
**Visual objective:** Files that land once a night suit a scheduled COPY INTO; files that land all day suit Snowpipe.
Generate as **eight shots (7a–7h)**. All shots use the same camera language and layout (bucket on the left, stage in the centre, CUSTOMER table on the right).

**Shot 7a (52.56–54.75 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Cloud Glass #EDEFF7, text #FAFAFD. A sleek abstract Cloud Glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈53.2 s.

**Shot 7b (54.75–60.55 s) – daily midnight: 100 GB of transaction files:**
"Same style and palette. A glass clock-dial (no numerals) turns to the top (midnight) beside a crescent-moon glyph, and at that moment a large heap of Peach transaction-file cards lands in the bucket all at once. A small 'GB' gauge glyph (no numbers) fills up. No readable fine text, no logos."
Motion: 54.92–56.2 s the clock turns to midnight on "Daily midnight ki" (Daily midnight ≈55.2 s); ≈56.6–58.4 s the heap lands on "AWS S3 lo 100 GB transaction files" (100 GB ≈57.6 s); ≈59.4–60.37 s the heap settles on "land avuthunnayi anukondi". **Effect: Day dial.**
Overlay (post): "DAILY MIDNIGHT" at ≈55.2 s; "100 GB TRANSACTION FILES" at ≈57.6 s; "AWS S3" at ≈56.6 s.

**Shot 7c (60.55–64.01 s) – a scheduled batch process with COPY INTO:**
"Same style and palette, plus COPY INTO Rose #FF6BA8. A small glass schedule-clock glyph triggers the Rose 'run' button at a set time; the whole heap of files moves through the stage into the table in one batch. No readable fine text, no logos."
Motion: 60.73–62.0 s the schedule clock appears on "Manam scheduled batch process"; ≈62.6–63.83 s the button runs and the batch moves on "run chesi COPY INTO use cheyyachu" (COPY INTO ≈62.6 s). **Effect: Live cursor.**
Overlay (post): "SCHEDULED BATCH PROCESS" from ≈61.2 s; "COPY INTO" at ≈62.6 s.

**Shot 7d (64.01–70.36 s) – files land all day: Snowpipe:**
"Same style and palette, plus Snowpipe Turquoise #19E0C8 and Event Yellow #FFE14D. A sun-arc glyph crosses the sky above the bucket and, all along it, single Peach files land one after another; each landing rings a small Yellow bell and the Turquoise pipe loads that file into the table straight away, with no cursor. No readable fine text, no logos."
Motion: 64.18–65.2 s the sun arc starts on "Kaani files"; ≈65.2–66.4 s files land along the arc on "throughout the day continuously land avuthunte" (throughout the day ≈65.2 s); ≈67.6–70.13 s the bells ring and the pipe loads each file on "Snowpipe use chesi automatic ingestion setup cheyyachu" (Snowpipe ≈67.6 s, automatic ingestion ≈68.8 s). **Effect: Rack focus** — focus pulls from the bucket to the pipe at ≈67.6 s.
Overlay (post): "FILES LAND CONTINUOUSLY THROUGHOUT THE DAY" from ≈65.2 s; "SNOWPIPE: AUTOMATIC INGESTION" from ≈67.6 s.

**Shot 7e (70.36–73.85 s) – SQL: COPY INTO:**
"Same style and palette. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) slides in at the centre with a thin Rose edge. The Rose button glows beside it. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 70.59–72.0 s line 1 types on "COPY INTO CUSTOMER"; ≈72.2–73.63 s line 2 types on "FROM @CUSTOMER_STAGE;". **Effect: Code body.**
Overlay (post, monospace):
```sql
COPY INTO CUSTOMER
FROM @CUSTOMER_STAGE;
```
"COPY INTO CUSTOMER" at 70.59 s; "FROM @CUSTOMER_STAGE;" at ≈72.2 s.

**Shot 7f (73.85–77.32 s) – SQL: CREATE PIPE:**
"Same style and palette. The first panel slides aside and a second, Turquoise-edged panel appears. The Turquoise pipe glows beside it. No readable code, no logos, no watermark."
Motion: 74.07–74.82 s the second panel appears on "Snowpipe kosam:"; 75.14–75.73 s the first words type on "CREATE PIPE"; 75.94–77.19 s the name types on "CUSTOMER_PIPE". **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE PIPE CUSTOMER_PIPE
```
"CREATE PIPE" at 75.14 s; "CUSTOMER_PIPE" at 75.94 s.

**Shot 7g (77.32–79.76 s) – SQL: AUTO_INGEST = TRUE:**
"Same style and palette, plus Event Yellow #FFE14D. The code panel continues. As the line types, a small Yellow bell glows on top of the pipe. No readable code, no logos, no watermark."
Motion: 77.44–79.66 s line 2 types on "AUTO_INGEST = TRUE" (TRUE ≈79.0 s) and the bell glows. **Effect: Code body.**
Overlay (post, monospace; append):
```sql
CREATE PIPE CUSTOMER_PIPE
AUTO_INGEST = TRUE
```
"AUTO_INGEST = TRUE" at 77.44 s.

**Shot 7h (79.76–83.42 s) – SQL: AS COPY INTO …:**
"Same style and palette. The code panel finishes the statement. The pipe, the bell and the table connect with a thin Turquoise line, and a first file flows through to the table. No readable code, no logos, no watermark."
Motion: 79.86–81.4 s the next lines type on "AS COPY INTO CUSTOMER"; ≈81.5–83.2 s the last line types on "FROM @CUSTOMER_STAGE;" and the file flows through. **Effect: Code body.**
Overlay (post, monospace; the full statement shown at the end):
```sql
CREATE PIPE CUSTOMER_PIPE
AUTO_INGEST = TRUE
AS
COPY INTO CUSTOMER
FROM @CUSTOMER_STAGE;
```
"AS" at 79.86 s; "COPY INTO CUSTOMER" at ≈80.2 s; "FROM @CUSTOMER_STAGE;" at ≈81.5 s.

**Audio sync:** every statement starts at its pause end (70.59, 75.14, 77.44, 79.86 s); inner times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, real AWS logos, readable personal data, readable fake text in the generated video, wrong syntax, extra statements, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (83.42–95.86 s · 12.44 s)
**Voice-over:** "So, simple ga gurthupettukondi! COPY INTO – Command-based data loading. Snowpipe – Event-driven automated data ingestion. Batch loading kosam COPY INTO useful. Continuous file ingestion kosam Snowpipe useful."
**Tone:** confident.
**Visual objective:** Two-card recap and when to use which.
Generate as **three shots (8a–8c)**.

**Shot 8a (83.42–87.80 s) – keep it simple, COPY INTO:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, text #FAFAFD. The Rose button and the Turquoise pipe glide to the centre with a soft bloom, then the Rose button comes forward and fills the frame, pressed by a cursor, with a crate of files moving together. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈83.8 s; "COPY INTO" at 85.64 s; "Command-based data loading" from 86.44 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 8b (87.80–90.92 s) – Snowpipe:**
"Same style and palette. The Turquoise pipe comes forward and fills the frame, with a Yellow bell ringing and single files flowing through by themselves. Clean and calm. No readable text, no logos."
Overlay (post): "SNOWPIPE" at 88.01 s; "Event-driven automated data ingestion" from 88.76 s.

**Shot 8c (90.92–95.86 s) – which one to use:**
"Same style and palette. The screen divides in two: on the left a Rose button with a crate of files (batch loading); on the right a Turquoise pipe with a continuous stream of files (continuous file ingestion). A soft tick-glow lights each half in turn. Clean and calm. No readable text, no logos."
Motion: ≈91.3–93.05 s the left half lights on "Batch loading kosam COPY INTO useful"; ≈93.5–95.65 s the right half lights on "Continuous file ingestion kosam Snowpipe useful".
Overlay (post): "BATCH LOADING → COPY INTO" from ≈91.3 s; "CONTINUOUS FILE INGESTION → SNOWPIPE" from ≈93.5 s. **Effect: Head stack.**

**Audio sync:** card 1 at 85.64 s; card 2 at 88.01 s; batch line at ≈91.3 s; continuous line at ≈93.5 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (95.86–105.43 s · 9.57 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty-Three! Next video lo Snowpipe Auto-Ingest ela work avuthundho AWS S3 real-time example tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 23 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (95.86–99.21 s) – Day 23 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Event Yellow #FFE14D, text #FAFAFD. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty-three lit in Turquoise (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 23" from ≈96.8 s; the twenty-third node lights at ≈98.2 s on "Twenty-Three".

**Shot 9b (99.21–105.43 s) – teaser: Snowpipe Auto-Ingest with AWS S3:**
"Same style and palette. A teaser panel slides in: on the left a generic glass cloud-bucket (no AWS logo), in the middle a Yellow bell and a small message glyph travelling along a thin line, on the right a Turquoise pipe leading into a Cloud Glass table. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: SNOWPIPE AUTO-INGEST" from ≈100.3 s; "AWS S3" from ≈102.6 s; "REAL-TIME EXAMPLE" from ≈103.4 s. The visual only suggests a bell travelling from a bucket to a pipe. Do not show how the setup works, settings or numbers.

**Audio sync:** card at ≈96.8 s; the twenty-third node at ≈98.2 s; the teaser title at ≈100.3 s.
**Negative prompt:** "Technical claims about the setup, real AWS logos, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (105.43–116.04 s · 10.61 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (105.43–110.97 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Event Yellow #FFE14D, text #FAFAFD. A calm, clean background with a soft glow, a small Rose button and a Turquoise pipe drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈106.6 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈107.4 s, emphasised at ≈109.8 s on "Follow" (estimated).

**Shot 10b (110.97–114.13 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Rose and Turquoise glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 111.15 s, emphasised at ≈113.2 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel. No website is added (see the note at the top).

**Shot 10c (114.13–116.04 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 114.28 s. Hold the final frame for the last 0.3 s.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 23. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #1B1A22, COPY INTO Rose #FF6BA8, Snowpipe Turquoise #19E0C8, Event Yellow #FFE14D, File Peach #FFC9A3, Cloud Glass #EDEFF7, text #FAFAFD, secondary text #A3A1B5. Colour code: files = small Peach glass cards; AWS S3 = a generic cloud-bucket glyph (never an AWS logo); a stage = a Cloud Glass portal window; a Snowflake table = a Cloud Glass block with rows of cells; COPY INTO = a Rose 'run' button pressed by a cursor, after which a batch of files moves together; Snowpipe = a Turquoise glass pipe with a continuous flow, triggered by a Yellow bell when a new file lands, with no cursor and no run button. COPY INTO always shows a run action; Snowpipe never does. Never show timings, costs or latency claims, real logos, or numbers other than the script's '100 GB'. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–22: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day23.mp3` (116.04 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, "100 GB", the two SQL statements, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Do not use real AWS logos.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a button click for COPY INTO, a soft bell chime for the event notification, a gentle pipe flow) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start (the opening line, 0–2.1 s), at the manual and automatic questions (≈10.4, ≈13.6 s), at the title (20.41 s), at each badge (25.72, 38.50 s), at the bell (≈44.6 s), at the midnight clock (≈55.2 s), at each SQL statement start (70.59, 75.14, 77.44, 79.86 s), at the recap cards (85.64, 88.01 s), at the final tagline (114.28 s), and at the Follow and Contact lines (≈109.8, ≈113.2 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: COPY INTO is a Snowflake command that, when executed, loads files from an external or internal stage into a table and is usually used for batch loading; Snowpipe is a continuous data ingestion service whose loads are triggered when new files arrive, through event notifications or supported automation mechanisms, so COPY INTO does not have to be run manually every time; in the banking example a scheduled batch with COPY INTO suits files that land once at midnight, and Snowpipe suits files that land continuously during the day. **No timings, costs, latencies or other numbers** are shown beyond the script's "100 GB". The SQL statements from the script are valid Snowflake syntax.
- **Optional addition (not in the script, so not shown on screen):** for `AUTO_INGEST = TRUE` on an external stage, the cloud storage must also be set up to send event notifications to Snowpipe. The script covers this in the next video, so the visuals only show a bell. Please verify any detail against Snowflake's current documentation before you publish it.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
