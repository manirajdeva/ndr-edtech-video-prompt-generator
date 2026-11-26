# Thirty Days of Snowflake – Day 12: Snowflake Zero-Copy Cloning
Video prompt package (NDR EdTech) — `Audio\day12.mp3` + `days-scripts\day12.txt`, analysed with Whisper

> **Timing status: MEASURED from day12.mp3 (112.67 s).**
> - Word times come from Whisper (faster-whisper, `small` model, English mode, Windows CPU), cross-checked against the silences in the audio (`silencedetect`, -26 dB, 0.2 s). **Phrase starts are taken from the end of each pause, so they are the most exact.** Whisper word times can be 0.1–0.5 s early or late, especially in long Telugu phrases. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from Whisper.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (3 items):**
> 1. **82.02 s:** Whisper heard "bank fraud" where your script says **BANK_PROD**. It is a mishearing; the overlays use BANK_PROD.
> 2. **Follow and Contact lines (about 104–110 s):** Whisper mixed up the word order of these two Telugu lines, so the "Follow" and "Contact" word times are estimated (≈). Listen once and adjust by 0.2–0.5 s if needed.
> 3. **13.12–14.30 s** is your scripted `[pause]`, a real 1.18 s silence. The visuals hold a calm beat there.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 12: Snowflake Zero-Copy Cloning |
| Duration | **112.67 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,380 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day12.mp3` is the master track. No replacement narration. Optional subtle music, ducked under speech. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so some scenes are split into shots (29 shots in 13 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Twin Ember" (new for Day 12)
| Role | HEX | Use |
|---|---|---|
| Background | `#140A12` | Base, gradients (dark aubergine-black) |
| Ember Orange | `#FF8A3D` | The **original** (BANK_PROD, the original document and table) |
| Hot Pink | `#F43F9A` | The **clone** (BANK_TEST, the copy) |
| Shared Aqua | `#38D5E8` | **Shared storage** blocks and the links to them |
| New-Data Lemon | `#FDE047` | **New storage** created by changes in the clone, sparkles, "fast" |
| Primary text | `#FFF6F0` | Titles, labels |
| Secondary text | `#B9A3B0` | Captions, faded or not-used items |

**Colour code (use in every scene):** Original = solid Ember Orange · Clone = Hot Pink with a thin double outline · Shared storage = Aqua glass blocks on a "storage shelf" below the tables · New storage for changes = Lemon blocks.

**The core visual rule (technical accuracy):** at the start the original and the clone **share the same Aqua storage blocks** through thin Aqua links. No new Aqua blocks are created when the clone is made. Only when the clone is changed do a few **Lemon** blocks appear, just for the changes. The "Clone row" effect is **deliberately not used** in the Snowflake scenes, because it would suggest that data is physically copied.

### Motion effects used (from the skill's effects library)
Impact frame, Rack focus, Letter dive, Press font, Liquid glass, Head stack, Live cursor, Code body, Comment drop. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.35 | "Hello guys! Andaru ela unnaru?" (0.00–2.18) · "Oka question!" (2.55–3.16) | Funny, energetic | Title hook, two identical documents and "?" |
| 2 | 3.35–13.71 | "Mee daggara oka important document undhi." (3.53–5.48) · "Dhaaniki exact copy kavali ante malli same document motham create chesthara?" (5.79–10.20) · "Leda original document ki copy create chesthara?" (10.56–13.12) · *[scripted pause 13.12–14.30]* | Playful, curious | Recreate by hand versus quick copy |
| 3 | 13.71–22.14 | "Snowflake lo kuda ilanti concept undhi!" (14.30–16.40) · "Kaani interesting enti ante…" (16.76–18.36) · "data motham physically copy cheyyakundane clone create cheyyachu!" (18.59–21.95) | Curious, building | Original with a clone and no data movement |
| 4 | 22.14–25.02 | "Adhe Zero-Copy Cloning!" (22.33–23.73) · "Let's understand!" (24.10–24.78) | Excited | Title reveal |
| 5 | 25.02–27.15 | "Welcome to NDR EdTech!" (25.25–26.96) | Welcoming | Brand welcome |
| 6 | 27.15–35.01 | "Zero-Copy Cloning ante Snowflake lo existing Database," (27.33–30.88) · "Schema or Table" (31.11–32.40) · "ki quick copy create cheyyadaniki use chese feature." (32.61–34.81) | Clear | Database, Schema, Table; quick copy |
| 7 | 35.01–52.27 | "Initially, original data ni physically duplicate cheyyadhu." (35.21–38.18) · "Instead, original data tho storage ni share cheskuntu clone create chesthundhi." (38.55–42.86) · "Clone lo changes chesinappudu, new changes kosam additional storage use avuthundhi." (43.24–47.49) · "Anduke initial cloning process fast ga and storage-efficient ga untundhi." (47.83–52.07) | Clear, steady | No copy, shared storage, new storage for changes, fast and efficient |
| 8 | 52.27–69.39 | "Oka Banking project example teesukundham." (52.47–54.38) · "Mana production database name BANK_PROD." (54.75–57.72) · "Ippudu developers ki testing kosam same data structure and existing data kavali." (58.09–62.65) · "Production data ni separate ga full copy cheyyakunda," (63.02–65.76) · "Zero-Copy Cloning use chesi testing database create cheyyachu." (65.96–69.22) | Storytelling | BANK_PROD, developers need test data, clone without full copy |
| 9 | 69.39–75.60 | "SQL command chuddam!" (69.56–70.67) · "CREATE DATABASE BANK_TEST" (71.06–73.52) · "CLONE BANK_PROD;" (73.79–75.38) | Focused | Code builds line by line |
| 10 | 75.60–83.90 | "Anthe! Mana BANK_PROD database ki clone create ayyindhi." (75.81–78.85) · "Developers BANK_TEST lo changes chesina, original BANK_PROD data affect avvadhu." (79.19–83.70) | Satisfying, confident | Clone appears; original untouched |
| 11 | 83.90–93.28 | "So, simple ga gurthupettukondi!" (84.11–85.91) · "Zero-Copy Cloning helps us create fast and storage-efficient copies without initially duplicating the entire data." (86.23–93.09) | Confident | Three-point recap |
| 12 | 93.28–101.39 | "Idi mana Thirty Days of Snowflake series lo Day Twelve!" (93.46–96.28) · "Next video lo Snowflake Fail-safe gurinchi real-time examples tho explain chesthanu." (96.67–101.22) | Upbeat | Day 12 card, Fail-safe teaser |
| 13 | 101.39–112.67 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (101.56–107.12) · "Full course details kosam NDR EdTech ni Contact avvandi!" (107.56–110.58) · "Let's Learn and Grow Together!" (110.89–112.44) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.80–1.19, 2.18–2.55, 3.16–3.53, 5.48–5.79, 10.20–10.56, 13.12–14.30 (the scripted `[pause]`), 16.40–16.76, 18.36–18.59, 21.95–22.33, 23.73–24.10, 24.78–25.25, 26.96–27.33, 30.88–31.11, 32.40–32.61, 34.81–35.21, 38.18–38.55, 39.02–39.28, 42.86–43.24, 47.49–47.83, 52.07–52.47, 54.38–54.75, 57.72–58.09, 62.65–63.02, 65.76–65.96, 69.22–69.56, 70.67–71.06, 73.52–73.79, 75.38–75.81, 76.14–76.43, 78.85–79.19, 83.70–84.11, 85.91–86.23, 93.09–93.46, 96.28–96.67, 98.10–98.30, 101.22–101.56, 107.12–107.56, 110.58–110.89, 112.44–112.67.

### Appendix A – Key trigger times
Words use your script's spelling. Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Hello guys! Andaru ela unnaru? | Hello 0.0 · guys 0.4 · Andaru ela unnaru ≈1.2–2.1 |
| Oka question! | Oka 2.55 · question ≈2.7 |
| Mee daggara oka important document undhi. | important 4.2 · document 4.6 |
| Dhaaniki exact copy kavali ante malli same document motham create chesthara? | exact ≈6.1 · copy 6.6 · malli ≈7.6 · same document ≈8.4–8.7 · motham create ≈9.1 · chesthara ≈9.9 |
| Leda original document ki copy create chesthara? | Leda 10.56 · original ≈11.0 · document ≈11.4 · copy ≈12.0 · create chesthara ≈12.5 |
| Snowflake lo kuda ilanti concept undhi! | Snowflake 14.3 · concept ≈15.4 |
| Kaani interesting enti ante… | interesting 16.96 |
| data motham physically copy cheyyakundane clone create cheyyachu! | data motham 18.6 · physically ≈19.4 · copy cheyyakundane ≈20.0 · clone ≈20.8 · create cheyyachu ≈21.3 |
| Adhe Zero-Copy Cloning! | Adhe 22.33 · Zero 22.68 · Copy 23.0 · Cloning 23.32 |
| Let's understand! | Let's 24.10 · understand 24.36 |
| Welcome to NDR EdTech! | Welcome 25.25 · NDR 25.82 · EdTech 26.38 |
| Zero-Copy Cloning ante Snowflake lo existing Database, | Zero 27.33 · Cloning ≈28.0 · Snowflake ≈29.0 · Database ≈30.2 |
| Schema or Table | Schema ≈31.2 · Table ≈31.9 |
| ki quick copy create cheyyadaniki use chese feature | quick copy 32.68 · feature ≈34.4 |
| Initially, original data ni physically duplicate cheyyadhu. | Initially 35.21 · original data ≈36.0 · physically ≈36.8 · duplicate ≈37.3 · cheyyadhu ≈37.8 |
| Instead, original data tho storage ni share cheskuntu clone create chesthundhi. | Instead 38.55 · original data ≈39.4 · storage ≈40.0 · share ≈40.8 · clone ≈41.8 |
| Clone lo changes chesinappudu, new changes kosam additional storage use avuthundhi. | Clone 43.3 · changes 43.4–44.2 · new changes ≈45.5 · additional storage ≈46.2 · use avuthundhi ≈47.0 |
| Anduke initial cloning process fast ga and storage-efficient ga untundhi. | Anduke 47.83 · initial cloning 48.4–48.7 · fast ≈49.7 · storage-efficient ≈50.5 |
| Oka Banking project example teesukundham. | Banking 52.6 · project 53.0 · example 53.4 |
| Mana production database name BANK_PROD. | production 54.86 · database 55.26 · **BANK_PROD** ≈56.3 |
| Ippudu developers ki testing kosam same data structure and existing data kavali. | developers 58.24 · testing ≈59.5 · same data structure ≈60.0–61.0 · existing data ≈61.4 · kavali ≈62.3 |
| Production data ni separate ga full copy cheyyakunda, | Production 63.1 · separate ga ≈64.0 · full copy ≈64.8 |
| Zero-Copy Cloning use chesi testing database create cheyyachu. | Zero 66.0 · Cloning 66.56 · testing database ≈67.6 · create cheyyachu ≈68.4 |
| SQL command chuddam! | SQL 69.84 · command 69.92 |
| CREATE DATABASE BANK_TEST | CREATE 71.06 · DATABASE 71.3 · BANK_TEST ≈72.0–73.4 |
| CLONE BANK_PROD; | CLONE ≈73.8 · BANK_PROD ≈74.3–75.3 |
| Anthe! Mana BANK_PROD database ki clone create ayyindhi. | Anthe 75.81 · BANK_PROD ≈76.5 · clone create ayyindhi ≈77.7 |
| Developers BANK_TEST lo changes chesina, original BANK_PROD data affect avvadhu. | Developers 79.19 · BANK_TEST ≈80.0 · changes ≈80.8 · original BANK_PROD ≈81.5–82.8 · affect avvadhu ≈83.0 |
| So, simple ga gurthupettukondi! | So 84.11 · simple ga 84.66 · gurthupettukondi ≈85.2 |
| Zero-Copy Cloning helps us create fast and storage-efficient copies without initially duplicating the entire data. | Zero-Copy Cloning 86.23–86.82 · fast 88.14 · storage-efficient 88.88–89.24 · copies 89.72 · without initially duplicating 90.16–91.26 · entire data 92.16–92.66 |
| Idi mana Thirty Days of Snowflake series lo Day Twelve! | Thirty 93.84 · Days 94.22 · Snowflake 94.62 · series 95.02 · Day 95.64 · Twelve 95.86 |
| Next video lo Snowflake Fail-safe gurinchi real-time examples tho explain chesthanu. | Next 96.76 · Snowflake ≈97.8 · Fail-safe ≈98.3 · real-time ≈99.4 · examples ≈99.9 |
| Ilanti Data Engineering concepts Telugu lo nerchukovadaniki | Data Engineering 102.1 · concepts 102.5 · Telugu 103.3 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈104.3 · NDR EdTech ≈104.9–106.2 · **Follow** ≈106.3 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full 107.56 · course 107.6 · details 107.9 · NDR EdTech ≈108.6–109.5 · **Contact** ≈109.7 (estimated) |
| Let's Learn and Grow Together! | Let's 110.89 · Learn 111.16 · and 111.44 · Grow 111.72 · Together 111.98 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, New-Data Lemon #FDE047, text #FFF6F0.*

**Object look (keep identical in every scene):**
- **Original** = solid Ember Orange glass table or document with a calm steady glow.
- **Clone** = Hot Pink glass table or document with a thin double outline.
- **Storage shelf** = a row of Shared Aqua glass blocks under the tables. Thin Aqua links join each table to the blocks it uses.
- **New storage** = a few Lemon blocks, shown only after the clone has been changed.

### Scene 1 – Hook (0.00–3.35 s · 3.35 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka question!"
**Tone:** funny, high energy.
**Visual objective:** Welcome viewers and tease the question.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, New-Data Lemon #FDE047, text #FFF6F0. A deep aubergine-black space with soft warm light and drifting glass particles. Two identical glass document sheets (one Ember Orange, one Hot Pink, no readable text) float side by side and a large glowing glass question-mark forms between and above them, settling with a soft warm bloom. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."

**Motion instructions:**
- 0.00–2.18 s: particles drift in and the two document sheets slide into place on "Hello guys! Andaru ela unnaru?".
- 2.55–3.16 s: the question-mark forms with a bloom pulse on "Oka question!".
- 3.16–3.35 s: quick light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at ≈2.7 s on "question".

**Audio sync:** title overlay lands at ≈1.2 s on "Andaru"; light sweep completes in the pause at 3.16–3.53 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 12".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, watermark, subtitles."

---

### Scene 2 – Make the same document again, or copy it? (3.35–13.71 s · 10.36 s)
**Voice-over:** "Mee daggara oka important document undhi. Dhaaniki exact copy kavali ante malli same document motham create chesthara? Leda original document ki copy create chesthara?"
**Tone:** playful, curious. The last 0.6 s is the start of the scripted pause.
**Visual objective:** Compare rebuilding a document from scratch with quickly copying the original.
Generate as **three shots (2a–2c)**.

**Shot 2a (3.35–5.64 s) – the important document:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, text #FFF6F0. A single large glowing Ember Orange glass document sheet with abstract lines and a small round seal motif (no readable text) floats at the centre. A soft steady glow suggests that it is important. Slow push-in, soft rim lighting, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 3.53–4.2 s the document rises on "Mee daggara oka"; 4.2–4.6 s the seal lights on "important document".
Overlay (post): "IMPORTANT DOCUMENT" from 4.2 s.

**Shot 2b (5.64–10.38 s) – recreate it from scratch:**
"Same style and palette, plus Hot Pink #F43F9A. Beside the original Ember Orange document, a blank Hot Pink sheet is being filled in line by line, slowly and laboriously, by a glowing cursor. A thin progress bar below it crawls forward. The original document waits patiently. Slightly impatient, playful feeling. No readable text, no logos, no watermark."
Motion: 5.79–6.6 s the blank pink sheet appears on "exact copy"; ≈7.6–9.1 s the cursor writes lines slowly on "malli same document motham create"; ≈9.9 s the progress bar is still far from full on "chesthara?". **Effect: Live cursor.**
Overlay (post): "CREATE IT AGAIN?" from ≈7.6 s.

**Shot 2c (10.38–13.71 s) – copy the original:**
"Same style and palette. A soft Aqua light bar sweeps over the Ember Orange document like a scanner, and a complete Hot Pink copy of it appears next to it instantly. The two sheets sit side by side, identical. Hold a calm still frame for the last 0.6 s. No readable text, no logos, no watermark."
Motion: 10.56–11.4 s the scan bar sweeps on "Leda original document"; ≈12.0–12.6 s the copy appears on "ki copy create chesthara?"; 13.12–13.71 s calm hold during the scripted pause.
Overlay (post): "COPY THE ORIGINAL?" from 10.56 s.

**Audio sync:** pink sheet at 5.79 s; cursor at ≈7.6 s; scan bar at 10.56 s; copy at ≈12.0 s.
**Negative prompt:** "Human faces, readable document text, cartoon characters, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Snowflake has this too (13.71–22.14 s · 8.43 s)
**Voice-over:** "Snowflake lo kuda ilanti concept undhi! Kaani interesting enti ante… data motham physically copy cheyyakundane clone create cheyyachu!"
**Tone:** curious, building to a reveal.
**Visual objective:** A clone can be created without physically copying the data.
Generate as **two shots (3a, 3b)**.

**Shot 3a (13.71–16.58 s) – the same idea in Snowflake:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A glowing glass snowflake-crystal emblem rises at the upper-centre with a soft warm bloom. Below it, the Ember Orange and Hot Pink document sheets from the last scene turn into two glass table blocks and settle side by side. Clean space for a title. Soft volumetric light. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 14.30–15.4 s the emblem rises on "Snowflake lo kuda"; ≈15.4–16.4 s the documents morph into table blocks on "ilanti concept undhi!".
Overlay (post): none (the title comes in Scene 4).

**Shot 3b (16.58–22.14 s) – clone without copying:**
"Same style and palette, plus Shared Aqua #38D5E8. A large Ember Orange glass table block sits on a storage shelf of Aqua glass blocks. A Hot Pink table block with a thin double outline appears beside it and is joined to the same Aqua blocks by thin Aqua light links. No new Aqua blocks appear and no particles travel from one table to another: it is clear that nothing is physically copied. Calm, magical feeling. Clean space for captions. No readable text, no logos, no watermark."
Motion: 16.76–18.36 s a mysterious glow builds around the table on "Kaani interesting enti ante…"; 18.59–20.4 s the orange table and the storage shelf stay perfectly still on "data motham physically copy cheyyakundane" (≈19.4 s "physically"); ≈20.8–21.95 s the pink clone fades in and the Aqua links draw to the shared blocks on "clone create cheyyachu!". **Effect: Impact frame** — a one-frame flash at ≈20.8 s when the clone appears.

**Audio sync:** emblem at 14.30 s; "interesting" glow at 16.96 s; clone appears at ≈20.8 s.
**On-screen text (overlay, post):** "NO PHYSICAL COPY" from ≈19.4 s.
**Negative prompt:** "Particles flowing from the original into the clone, duplicated storage blocks, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Title reveal (22.14–25.02 s · 2.88 s)
**Voice-over:** "Adhe Zero-Copy Cloning! Let's understand!"
**Tone:** excited.
**Visual objective:** Name the topic.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. The Ember Orange table block and the Hot Pink clone block sit side by side over the Aqua storage shelf, glowing together. A big clean empty space above them for a large title. A soft light burst radiates behind them. Slow push-in. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 22.33–23.73 s: the title lands on "Adhe Zero-Copy Cloning!". **Effect: Letter dive** — the letters fly in and settle fully before 23.7 s.
- 24.10–24.78 s: a small subtitle pops in on "Let's understand!".
**Audio sync:** "ZERO-COPY" at 22.68 s; "CLONING" at 23.32 s; subtitle at 24.10 s.
**On-screen text (overlay, post):** "ZERO-COPY CLONING" / "LET'S UNDERSTAND!".
**Negative prompt:** "Fake logos, misspelled title, tiny text, flicker, off-palette colours, watermark."

---

### Scene 5 – Welcome (25.02–27.15 s · 2.13 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, text #FFF6F0. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft warm glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 25.25–26.96 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 25.25 s; "NDR" at 25.82 s; "EdTech" at 26.38 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – What is Zero-Copy Cloning? (27.15–35.01 s · 7.86 s)
**Voice-over:** "Zero-Copy Cloning ante Snowflake lo existing Database, Schema or Table ki quick copy create cheyyadaniki use chese feature."
**Tone:** clear.
**Visual objective:** It works on a Database, a Schema or a Table, and makes a quick copy.
Generate as **two shots (6a, 6b)**.

**Shot 6a (27.15–32.50 s) – Database, Schema, Table:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. Three Ember Orange glass objects rise one by one in a neat vertical stack: a database cylinder, a schema folder and a table block. Each has a faint Hot Pink outline that shows it can be cloned. Clean, uncluttered, phone-readable layout with space for three labels. Soft rim lighting, slow push-in. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 27.33–29.0 s the glow builds on "Zero-Copy Cloning ante Snowflake lo existing"; ≈30.2 s the cylinder rises on "Database"; ≈31.2 s the folder rises on "Schema"; ≈31.9 s the table rises on "Table". **Effect: Head stack.**
Overlay (post): "DATABASE" at ≈30.2 s, "SCHEMA" at ≈31.2 s, "TABLE" at ≈31.9 s.

**Shot 6b (32.50–35.01 s) – a quick copy:**
"Same style and palette. The stacked Ember Orange objects stay still while three Hot Pink twins appear beside them with a quick, clean light flash, joined to a shared Aqua glow beneath. Fast, crisp, clean motion. No readable fine text, no logos, no watermark."
Motion: 32.68 s the pink twins flash in on "quick copy"; 33.2–34.8 s they settle with a soft glow on "create cheyyadaniki use chese feature".
Overlay (post): "QUICK COPY" at 32.68 s.

**Audio sync:** Database at ≈30.2 s; Schema at ≈31.2 s; Table at ≈31.9 s; quick copy at 32.68 s.
**Negative prompt:** "Readable fake text, other object types, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – How it works (35.01–52.27 s · 17.26 s)
**Voice-over:** "Initially, original data ni physically duplicate cheyyadhu. Instead, original data tho storage ni share cheskuntu clone create chesthundhi. Clone lo changes chesinappudu, new changes kosam additional storage use avuthundhi. Anduke initial cloning process fast ga and storage-efficient ga untundhi."
**Tone:** clear, steady.
**Visual objective:** Four ideas: no physical copy, shared storage, new storage only for changes, fast and efficient.
Generate as **four shots (7a–7d)**. Keep the storage shelf and the table positions identical in every shot, so the story reads as one continuous build.

**Shot 7a (35.01–38.36 s) – not physically duplicated:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A solid Ember Orange glass table block sits above a storage shelf of six Aqua glass blocks. A faint, dim, bloated duplicate of the whole Aqua shelf tries to form, then fades away and is not created, leaving the original six blocks unchanged. Calm, clear. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 35.21–36.0 s the table and the shelf appear on "Initially"; ≈36.0–37.3 s the faint duplicate shelf forms and then fades on "original data ni physically duplicate"; ≈37.8 s the original shelf pulses once, unchanged, on "cheyyadhu".
Overlay (post): "NOT PHYSICALLY DUPLICATED" from ≈36.8 s.

**Shot 7b (38.36–43.05 s) – sharing storage:**
"Same style and palette. A Hot Pink glass clone table appears beside the Ember Orange table. Thin Aqua links draw from the clone to the same six Aqua blocks that the original uses. Both tables now light the same blocks. No new blocks are created. Calm, magical feeling. No readable text, no logos, no watermark."
Motion: 38.55–39.02 s the pink table fades in on "Instead,"; ≈39.4–41.0 s the Aqua links draw on "original data tho storage ni share"; ≈41.8–42.86 s the shared blocks glow in both colours on "clone create chesthundhi".
Overlay (post): "SHARED STORAGE" from ≈40.0 s.

**Shot 7c (43.05–47.66 s) – changes use new storage:**
"Same style and palette, plus New-Data Lemon #FDE047. Two rows of the Hot Pink clone table change (they flash briefly). Two small Lemon glass blocks appear beside the shelf and link only to the clone. The six Aqua blocks and the Ember Orange original remain unchanged. Clear, focused. No readable text, no logos, no watermark."
Motion: 43.30–45.0 s two clone rows flash on "Clone lo changes chesinappudu"; ≈45.5–47.0 s the Lemon blocks drop in on "new changes kosam additional storage"; ≈47.0 s a soft glow on "use avuthundhi". **Effect: Comment drop** — a small Lemon note drops in beside the new blocks.
Overlay (post): "NEW CHANGES → NEW STORAGE" from ≈45.5 s.

**Shot 7d (47.66–52.27 s) – fast and storage-efficient:**
"Same style and palette. The Hot Pink clone appears instantly with a quick Lemon speed streak, and a small storage meter on the side rises only slightly (just the two Lemon blocks). The Aqua shelf is shared. Crisp, confident motion. No readable text, no logos, no watermark."
Motion: 47.83–48.7 s a clean glow on "Anduke initial cloning process"; ≈49.7 s the speed streak on "fast ga" (**Effect: Impact frame**, one-frame flash); ≈50.5–52.07 s the meter settles low on "storage-efficient ga untundhi".
Overlay (post): "FAST" at ≈49.7 s; "STORAGE-EFFICIENT" at ≈50.5 s.

**Audio sync:** every overlay is timed to Appendix A; times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Particles travelling from original to clone, a full duplicated Aqua shelf, clones shown as free or unlimited, specific storage numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – Banking project example (52.27–69.39 s · 17.12 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana production database name BANK_PROD. Ippudu developers ki testing kosam same data structure and existing data kavali. Production data ni separate ga full copy cheyyakunda, Zero-Copy Cloning use chesi testing database create cheyyachu."
**Tone:** storytelling.
**Visual objective:** Developers need a test copy of BANK_PROD without a full copy.
Generate as **five shots (8a–8e)**. All shots use the same camera language.

**Shot 8a (52.27–54.56 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in warm Ember Orange, with an empty glass storage shelf below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from 52.6 s.

**Shot 8b (54.56–57.90 s) – BANK_PROD:**
"Same style and palette. A large Ember Orange glass database cylinder fills with glowing rows and settles on the Aqua storage shelf with links to the blocks. A calm steady glow marks it as the live production system. No readable fine text, no logos."
Overlay (post): "PRODUCTION DATABASE" at 54.86 s; "BANK_PROD" at ≈56.3 s (monospace).

**Shot 8c (57.90–62.84 s) – developers need test data:**
"Same style and palette. Two abstract glass developer-laptop icons (no people, no faces) glow at the sides. Beside the production database a faint empty Hot Pink outline of a database waits. A schema outline and a block of rows are drawn inside it as dotted lines, showing the structure and the existing data that testing needs. No readable text, no logos."
Motion: 58.24–59.5 s the laptops light up on "Ippudu developers ki testing kosam"; ≈60.0–61.0 s the schema outline draws on "same data structure"; ≈61.4–62.3 s the dotted rows draw on "existing data kavali".
Overlay (post): "TESTING NEEDS: SAME STRUCTURE + EXISTING DATA" from ≈60.0 s.

**Shot 8d (62.84–65.86 s) – no full copy:**
"Same style and palette. A faint, grey, heavy duplicate of the whole database and its storage shelf starts to form beside the original and is swept aside with a clean white slash, then fades away. Calm, decisive motion. No readable text, no logos."
Motion: 63.02–64.0 s the heavy duplicate begins to form on "Production data ni separate ga"; ≈64.8–65.76 s the slash cancels it on "full copy cheyyakunda".
Overlay (post): "NO FULL COPY" at ≈64.8 s.

**Shot 8e (65.86–69.39 s) – clone for testing:**
"Same style and palette. A Hot Pink database cylinder with a thin double outline fades in beside the Ember Orange BANK_PROD, linked by Aqua lines to the same storage blocks. No new storage blocks appear. A soft warm glow. No readable text, no logos."
Motion: 66.0–67.4 s the Aqua links draw on "Zero-Copy Cloning use chesi"; ≈67.6–68.4 s the pink database settles on "testing database"; ≈68.4–69.22 s a light pulse on "create cheyyachu".
Overlay (post): "BANK_TEST" at ≈67.6 s (monospace).

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, human faces, readable personal data, wrong colours (original must be orange, clone pink, shared storage aqua), clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 9 – SQL command (69.39–75.60 s · 6.21 s)
**Voice-over:** "SQL command chuddam! CREATE DATABASE BANK_TEST CLONE BANK_PROD;"
**Tone:** focused.
**Visual objective:** Show the clone command being written.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A dark glass code editor panel (a clean window with two empty lines, no readable code) floats at the centre with a thin Aqua edge and a blinking cursor. Behind it, softly out of focus, the Ember Orange database and the Hot Pink database glow. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 69.56–70.67 s: the panel slides in on "SQL command chuddam!".
- 71.06–73.52 s: line 1 types on "CREATE DATABASE BANK_TEST" (BANK_TEST ≈72.0–73.4 s). **Effect: Code body.**
- 73.79–75.38 s: line 2 types on "CLONE BANK_PROD;" (BANK_PROD ≈74.3–75.3 s) and the pink database glow links to the orange one.
**Overlay (post, monospace; build line by line):**
```sql
CREATE DATABASE BANK_TEST
CLONE BANK_PROD;
```
Line 1 at 71.06 s; line 2 at ≈73.8 s.
**Audio sync:** line 1 at 71.06 s; BANK_TEST at ≈72.4 s; line 2 at ≈73.8 s.
**Negative prompt:** "Readable fake code in the generated video, wrong syntax, extra lines, wrong database names, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Clone created, original safe (75.60–83.90 s · 8.30 s)
**Voice-over:** "Anthe! Mana BANK_PROD database ki clone create ayyindhi. Developers BANK_TEST lo changes chesina, original BANK_PROD data affect avvadhu."
**Tone:** satisfying, confident.
**Visual objective:** The clone exists, and changes in the clone do not affect the original.
Generate as **two shots (10a, 10b)**.

**Shot 10a (75.60–79.02 s) – clone created:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. The code panel shrinks to the top. Below it the Ember Orange BANK_PROD database and the new Hot Pink BANK_TEST database sit side by side, linked to the shared Aqua storage shelf. A soft mint-white success glow pulses around the pink database. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 75.81–76.14 s a success flash on "Anthe!" (**Effect: Impact frame**); ≈76.5 s the panel shrinks on "Mana BANK_PROD"; ≈77.7–78.85 s the pink database glows on "clone create ayyindhi".
Overlay (post): "CLONE CREATED" at ≈77.7 s.

**Shot 10b (79.02–83.90 s) – changes stay in the clone:**
"Same style and palette, plus New-Data Lemon #FDE047. A few rows in the Hot Pink BANK_TEST database change and a small Lemon block appears beside the shelf linked only to the clone. The Ember Orange BANK_PROD stays perfectly calm and unchanged, with a steady warm glow and a thin protective outline. Focus pulls to BANK_PROD. No readable text, no logos, no watermark."
Motion: 79.19–80.0 s the developer laptop lights on "Developers"; ≈80.0–81.0 s clone rows flash and a Lemon block drops in on "BANK_TEST lo changes chesina"; ≈81.5–83.0 s focus moves to the orange database on "original BANK_PROD data"; ≈83.0–83.7 s it glows steadily on "affect avvadhu". **Effect: Rack focus** — focus pulls from BANK_TEST to BANK_PROD at ≈81.5 s.
Overlay (post): "BANK_PROD UNCHANGED" at ≈83.0 s.

**Audio sync:** flash at 75.81 s; Lemon block at ≈80.5 s; focus pull at ≈81.5 s.
**Negative prompt:** "Changes appearing in BANK_PROD, particles flowing into the original, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 11 – Simple recap (83.90–93.28 s · 9.38 s)
**Voice-over:** "So, simple ga gurthupettukondi! Zero-Copy Cloning helps us create fast and storage-efficient copies without initially duplicating the entire data."
**Tone:** confident.
**Visual objective:** Three-point recap.
Generate as **two shots (11a, 11b)**.

**Shot 11a (83.90–86.07 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. The Ember Orange table and the Hot Pink clone glide to the centre together over a calm Aqua storage shelf with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈84.2 s.

**Shot 11b (86.07–93.28 s) – three points:**
"Same style and palette, plus New-Data Lemon #FDE047. Three glass cards rise in a vertical stack. Card 1 has a Lemon speed streak (fast). Card 2 has a small compact Aqua block stack (storage-efficient). Card 3 shows an Ember Orange table and a Hot Pink table sharing one Aqua block (no initial duplication). Clean, uncluttered, phone-readable layout with space for three labels. No readable fine text, no logos, no watermark."
Motion: 86.23–87.4 s the stack area glows on "Zero-Copy Cloning helps us create"; 88.14 s card 1 rises on "fast"; 88.88 s card 2 rises on "storage-efficient"; 90.16–93.09 s card 3 rises on "without initially duplicating the entire data". **Effect: Head stack.**
Overlay (post): "FAST" at 88.14 s; "STORAGE-EFFICIENT" at 88.88 s; "NO INITIAL DUPLICATION" at 90.16 s.

**Audio sync:** card 1 at 88.14 s; card 2 at 88.88 s; card 3 at 90.16 s.
**Negative prompt:** "Claims that cloning is free or unlimited, storage numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 12 – Series card and Fail-safe teaser (93.28–101.39 s · 8.11 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twelve! Next video lo Snowflake Fail-safe gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 12 and tease the next topic.
Generate as **two shots (12a, 12b)**.

**Shot 12a (93.28–96.47 s) – Day 12 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twelve lit in Ember Orange (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 12" from 93.84 s; the twelfth node lights at 95.86 s on "Twelve".

**Shot 12b (96.47–101.39 s) – teaser:**
"Same style and palette. A teaser panel slides in with a glass table block surrounded by a soft glass shield and a safety-net glow underneath it. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: SNOWFLAKE FAIL-SAFE" from ≈97.8 s; "REAL-TIME EXAMPLES" from ≈99.4 s. The visual only suggests protection. Do not show retention periods, day counts or recovery claims.

**Audio sync:** card at 93.84 s; the twelfth node at 95.86 s; "Fail-safe" at ≈98.3 s; "REAL-TIME EXAMPLES" at ≈99.4 s.
**Negative prompt:** "Retention numbers, feature claims, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 13 – Follow, contact and end card (101.39–112.67 s · 11.28 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (13a–13c)**.

**Shot 13a (101.39–107.34 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, text #FFF6F0. A calm, clean background with a soft warm glow, a small Ember Orange table and a Hot Pink clone drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at 102.1 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈104.3 s, emphasised at ≈106.3 s on "Follow" (estimated).

**Shot 13b (107.34–110.74 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Ember Orange and Hot Pink glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 107.56 s, emphasised at ≈109.7 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 13c (110.74–112.67 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 110.89 s. Hold the final frame for the last 0.2 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 12. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #140A12, Ember Orange #FF8A3D, Hot Pink #F43F9A, Shared Aqua #38D5E8, New-Data Lemon #FDE047, text #FFF6F0, secondary text #B9A3B0. Colour code: the original (document, table, BANK_PROD) = solid Ember Orange glass; the clone (copy, BANK_TEST) = Hot Pink glass with a thin double outline; shared storage = Aqua glass blocks on a storage shelf under the tables; new storage for changes in the clone = a few Lemon blocks. At the start the original and the clone share the same Aqua blocks through thin Aqua links; never show data particles travelling from the original to the clone and never create new Aqua blocks when the clone is made. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Analyse the audio with Whisper (Windows)

This is how the timings in this file were produced (same workflow as Day 9–11).

1. **Create a virtual environment and install** (PowerShell, Python 3.10):
   ```powershell
   py -3.10 -m venv whisper-env
   .\whisper-env\Scripts\python.exe -m pip install faster-whisper
   ```
2. **Run the `run_whisper.py` script from Day 9's file** (`small` model, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`).
   ```powershell
   .\whisper-env\Scripts\python.exe run_whisper.py Audio\day12.mp3 whisper_out.json
   ```
3. **Cross-check with the real pauses:**
   ```powershell
   ffmpeg -i Audio\day12.mp3 -af "silencedetect=noise=-26dB:d=0.2" -f null - 2>&1 | Select-String "silence_(start|end)"
   ```
4. **Build the timing map:** use the end of each silence as the phrase start, use Whisper word times for emphasis words, keep your script's spelling, and place scene cuts in the middle of a pause.

**Notes for this audio**
- Whisper in English mode wrote this Telugu-English narration as an English translation. Word *times* are usable, but in long Telugu phrases Whisper's times can be early (for example "Without completing…" at 62.72 s) and the word *order* can differ from the Telugu (the Follow and Contact lines), so those are marked ≈.
- Pause ends were preferred for phrase starts.

---

## 6. Editing and synchronisation plan

1. Import `day12.mp3` (112.67 s) as the master audio track and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, labels such as BANK_PROD and BANK_TEST, the SQL code, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. Add optional subtle music, ducked about 15–20 dB under narration, plus light whooshes only in pauses.
7. Check sync at the start, at the clone reveal (≈20.8 s), at the title (22.33 s), at each of the four "how it works" ideas (36.0, 39.4, 43.3, 49.7 s), at BANK_PROD (≈56.3 s), at each code line (71.06, ≈73.8 s), at the rack focus (≈81.5 s), at the recap cards (88.14, 88.88, 90.16 s), at the final tagline (110.89 s), and at the Follow and Contact lines (≈106.3, ≈109.7 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration, pauses and word times are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: a clone of a Database, Schema or Table is made quickly; at first the original data is not physically duplicated and the clone shares storage with the original; changes in the clone use additional storage for the new changes; so the initial clone is fast and storage-efficient; changes in BANK_TEST do not affect BANK_PROD. `CREATE DATABASE BANK_TEST CLONE BANK_PROD;` is valid Snowflake syntax. The visuals never suggest that cloning is free or unlimited, and no storage numbers are shown.
- The script says only "Database, Schema or Table", so no other clonable objects are shown.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
