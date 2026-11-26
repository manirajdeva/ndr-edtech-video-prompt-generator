# Thirty Days of Snowflake – Day 17: Partition Pruning in Snowflake
Video prompt package (NDR EdTech) — `Audio\day17.mp3` + `days-scripts\day17.txt`, analysed with Whisper

> **Timing status: MEASURED from day17.mp3 (101.72 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (3 items):**
> 1. **39.7–42.6 s:** Whisper's English reads "We can skip the **required** data or micro partitions". Your script says "**Required data leni** Micro-partitions ni skip chesthundhi" (skips the micro-partitions that do **not** have the required data). This is almost certainly a mishearing of "leni". The visuals follow your script. Please listen once to confirm.
> 2. **Follow and Contact lines (about 91–99 s):** Whisper's word order for these Telugu lines is unreliable, so the "Follow" and "Contact" times are estimated (≈).
> 3. **15.62–16.83 s** is your scripted `[pause]`, a real 1.21 s silence. The visuals hold a calm beat there.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 17: Partition Pruning in Snowflake |
| Duration | **101.72 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,052 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day17.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (27 shots in 11 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Prune & Shine" (new for Day 17)
| Role | HEX | Use |
|---|---|---|
| Background | `#0C1418` | Base, gradients (deep blue-teal slate) |
| Sun Yellow | `#FFD84D` | The micro-partitions that **are scanned** (they hold the required data), the result |
| Pruned Teal-Grey | `#4F6B72` | Micro-partitions that are **skipped** (pruned), dimmed items |
| Metadata Rose | `#FF9DB8` | The **min date – max date** strip on every micro-partition |
| Date Sky | `#7CC8FF` | The WHERE date marker, the date filter, SQL glass |
| Primary text | `#F5FAFB` | Titles, labels |
| Secondary text | `#9DB3B9` | Captions |

**Colour code (use in every scene):** a micro-partition = a rounded glass tile with a Rose date-range strip (min → max). The WHERE date = a vertical Sky marker line. A tile whose date range **includes** the marker = lit Sun Yellow (scanned). A tile whose range **does not** = dim Teal-Grey (skipped, still present, never deleted).

**The core visual rule (technical accuracy):** Snowflake stores table data automatically in micro-partitions; each micro-partition has metadata, such as a minimum date and a maximum date. For a query with a WHERE date condition, Snowflake **checks this metadata first** and **skips the micro-partitions that do not have the required data**. This is Partition Pruning. Show it only with abstract tiles and range strips (no readable dates except the script's). No counts, sizes or percentages. "Blow away" is **not** used, because skipped data is not deleted.

### Motion effects used (from the skill's effects library)
Comment drop, Letter dive, Impact frame, Liquid glass, Press font, Head stack, Live cursor, Code body, Rack focus, Blade slice. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.54 | "Hello guys! Andaru ela unnaru?" (0.00–1.78) · "Oka interesting question!" (2.26–3.29) | Curious | Title hook |
| 2 | 3.54–16.23 | "Mee daggara 10 crore transaction records unnayi anukondi." (3.78–6.47) · "Meeku only yesterday transactions kavali." (6.93–9.02) · "Ippudu Snowflake anni 10 crore records scan cheyyala?" (9.49–12.14) · "Leda required data unna portion matrame scan chesthundha?" (12.49–15.62) · *[scripted pause 15.62–16.83]* | Curious, building | 10 crore records, scan all or only the needed part? |
| 3 | 16.23–19.92 | "Exactly!" (16.83–17.50) · "Dheenine Partition Pruning antaru!" (17.88–19.71) | Excited, reveal | Answer and title |
| 4 | 19.92–22.99 | "Let's understand!" (20.12–20.74) · "Welcome to NDR EdTech!" (21.21–22.70) | Welcoming | Brand welcome |
| 5 | 22.99–33.79 | "Snowflake lo data automatically Micro-partitions lo store avuthundhi." (23.27–26.89) · "Prathi Micro-partition ki metadata maintain chesthundhi." (27.28–30.00) · "For example, minimum date and maximum date information untundhi." (30.40–33.60) | Clear | Tiles, metadata, min and max dates |
| 6 | 33.79–44.90 | "Ippudu manam WHERE condition use chesi specific date data adigithe," (33.98–37.42) · "Snowflake metadata ni check chesthundhi." (37.67–39.45) · "Required data leni Micro-partitions ni skip chesthundhi." (39.80–42.54) · "Dheenine Partition Pruning antaru." (42.88–44.73) | Clear | WHERE date, check metadata, skip |
| 7 | 44.90–49.81 | "Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu." (45.07–49.61) | Clear | Less scanning, better performance |
| 8 | 49.81–73.76 | "Oka Banking project example teesukundham." (50.00–51.78) · "Mana TRANSACTIONS table lo 10 crore records unnayi." (52.16–54.64) · "Manaki November 18th transactions matrame kavali." (55.00–57.84) · "SQL query chuddam!" (58.23–59.15) · "SELECT * FROM TRANSACTIONS" (59.62–61.33) · "WHERE TRANSACTION_DATE = '2026-11-18';" (61.56–65.25) · "Snowflake metadata ni use chesi, required data unna Micro-partitions ni identify chesthundhi." (65.68–70.45) · "Migatha unnecessary Micro-partitions ni skip chesthundhi." (70.77–73.55) | Storytelling | Banking: date query scans the needed tiles, skips the rest |
| 9 | 73.76–80.63 | "So, simple ga gurthupettukondi!" (73.97–75.59) · "Partition Pruning means skipping unnecessary Micro-partitions to reduce data scanning." (75.92–80.42) | Confident | One-line recap |
| 10 | 80.63–90.67 | "Idi mana Thirty Days of Snowflake series lo Day Seventeen!" (80.84–83.76) · "Next video lo Result Cache, Warehouse Cache and Metadata Cache madhya differences real-time examples tho explain chesthanu." (84.14–90.49) | Upbeat | Day 17 card, caches teaser |
| 11 | 90.67–101.72 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (90.84–96.18) · "Full course details kosam NDR EdTech ni Contact avvandi!" (96.58–99.51) · "Let's Learn and Grow Together!" (99.85–101.40) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.59–1.02, 1.78–2.26, 3.29–3.78, 6.47–6.93, 9.02–9.49, 12.14–12.49, 15.62–16.83 (the scripted `[pause]`), 17.50–17.88, 19.71–20.12, 20.74–21.21, 22.70–23.27, 26.89–27.28, 30.00–30.40, 33.60–33.98, 37.42–37.67, 39.45–39.80, 42.54–42.88, 44.73–45.07, 49.61–50.00, 51.78–52.16, 54.64–55.00, 57.84–58.23, 59.15–59.62, 61.33–61.56, 65.25–65.68, 70.45–70.77, 73.55–73.97, 75.59–75.92, 80.42–80.84, 83.76–84.14, 90.49–90.84, 96.18–96.58, 99.51–99.85, 101.40–101.72.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee daggara 10 crore transaction records unnayi anukondi. | **10 crore** ≈4.4–5.0 · transaction records ≈5.3 |
| Meeku only yesterday transactions kavali. | only yesterday ≈7.3–8.0 · transactions ≈8.4 |
| Ippudu Snowflake anni 10 crore records scan cheyyala? | anni 10 crore records ≈10.0–11.0 · scan ≈11.6 |
| Leda required data unna portion matrame scan chesthundha? | required data ≈13.2 · portion ≈14.2 · matrame scan ≈14.8 |
| Exactly! Dheenine Partition Pruning antaru! | Exactly 16.83 · Partition Pruning ≈18.4–19.0 |
| Let's understand! / Welcome to NDR EdTech! | Let's 20.12 · Welcome 21.21 · NDR ≈21.9 · EdTech ≈22.3 |
| Snowflake lo data automatically Micro-partitions lo store avuthundhi. | automatically ≈24.4 · Micro-partitions ≈25.2 · store ≈26.2 |
| Prathi Micro-partition ki metadata maintain chesthundhi. | Prathi 27.28 · metadata ≈28.5 · maintain ≈29.4 |
| For example, minimum date and maximum date information untundhi. | minimum date ≈31.3 · maximum date ≈32.4 · information ≈33.1 |
| Ippudu manam WHERE condition use chesi specific date data adigithe, | WHERE ≈34.6 · specific date data ≈36.0–37.0 |
| Snowflake metadata ni check chesthundhi. | Snowflake metadata 37.67–38.4 · check ≈39.0 |
| Required data leni Micro-partitions ni skip chesthundhi. | Required data leni ≈40.2 · Micro-partitions ≈41.0 · skip ≈42.0 |
| Dheenine Partition Pruning antaru. | Partition Pruning ≈43.4–44.3 |
| Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu. | unnecessary data scanning ≈45.9–47.0 · reduce ≈47.4 · query performance ≈48.2 · improve ≈49.0 |
| Oka Banking project example teesukundham. | Banking ≈50.4 · example ≈51.2 |
| Mana TRANSACTIONS table lo 10 crore records unnayi. | TRANSACTIONS ≈52.6 · **10 crore** ≈53.4 |
| Manaki November 18th transactions matrame kavali. | **November 18th** ≈55.6–56.4 · matrame ≈57.0 |
| SQL query chuddam! | SQL 58.23 |
| SELECT * FROM TRANSACTIONS | SELECT 59.62 · FROM ≈60.4 · TRANSACTIONS ≈60.7 |
| WHERE TRANSACTION_DATE = '2026-11-18'; | WHERE 61.56 · TRANSACTION_DATE ≈62.0–63.2 · '2026-11-18' ≈63.6–65.2 |
| Snowflake metadata ni use chesi, required data unna Micro-partitions ni identify chesthundhi. | metadata ≈66.4 · required data ≈67.6 · Micro-partitions ≈68.6 · identify ≈69.6 |
| Migatha unnecessary Micro-partitions ni skip chesthundhi. | Migatha 70.77 · unnecessary Micro-partitions ≈71.5 · skip ≈72.6 |
| So, simple ga gurthupettukondi! | So 73.97 · gurthupettukondi ≈74.8 |
| Partition Pruning means skipping unnecessary Micro-partitions to reduce data scanning. | Partition Pruning 75.92–76.6 · skipping ≈77.2 · reduce data scanning ≈79.0 |
| Idi mana Thirty Days of Snowflake series lo Day Seventeen! | Thirty ≈81.6 · Days ≈82.0 · Snowflake ≈82.4 · Seventeen ≈83.2 |
| Next video lo Result Cache, Warehouse Cache and Metadata Cache madhya differences real-time examples tho explain chesthanu. | Result Cache ≈85.0–86.0 · Warehouse Cache ≈86.3–87.4 · Metadata Cache ≈87.6–88.6 · real-time examples ≈89.0 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈93.0 · NDR EdTech ≈94.0–95.0 · **Follow** ≈95.3 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 96.58–98.0 · NDR EdTech ≈98.2 · **Contact** ≈98.8 (estimated) |
| Let's Learn and Grow Together! | Let's 99.85 · Together ≈101.0 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB.*

**Object look (keep identical in every scene):** a **table** = a large white glass block with rows of small cells. A **micro-partition** = a rounded glass tile with a thin Rose date-range strip (a left end and a right end marker, no readable dates). The **WHERE date** = a vertical Sky marker line over the tiles. **Scanned** tile = lit Sun Yellow. **Skipped** tile = dim Teal-Grey (present, not deleted).

### Scene 1 – Hook (0.00–3.54 s · 3.54 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka interesting question!"
**Tone:** curious.
**Visual objective:** Welcome viewers and tease the question.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB. A deep blue-teal space with soft warm light and drifting glass particles. A glowing glass question-mark made of small rounded glass tiles with thin rose strips forms at the upper-centre and settles with a soft bloom. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–1.78 s: particles drift in and the tiles start to gather on "Hello guys! Andaru ela unnaru?".
- 2.26–3.29 s: the question-mark completes with a bloom pulse on "Oka interesting question!".
- 3.29–3.54 s: soft light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at ≈2.9 s on "question".
**Audio sync:** title lands at ≈1.0 s; the sweep completes in the pause at 3.29–3.78 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 17".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – 10 crore records: scan all, or only what's needed? (3.54–16.23 s · 12.69 s)
**Voice-over:** "Mee daggara 10 crore transaction records unnayi anukondi. Meeku only yesterday transactions kavali. Ippudu Snowflake anni 10 crore records scan cheyyala? Leda required data unna portion matrame scan chesthundha?"
**Tone:** curious, building. The last 0.6 s is the start of the scripted pause.
**Visual objective:** Pose the question of how much data a query must read.
Generate as **four shots (2a–2d)**.

**Shot 2a (3.54–6.70 s) – 10 crore transaction records:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Date Sky #7CC8FF, text #F5FAFB. A vast, dense wall of tiny glowing cells in white glass fills the frame and stretches far into the distance, to show a huge number of transaction records. The camera pulls back slowly to reveal the scale. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 3.78–4.4 s the wall appears on "Mee daggara"; ≈4.4–5.5 s the camera pulls back on "10 crore transaction records"; 5.5–6.47 s the wall fills the frame on "unnayi anukondi".
Overlay (post): "10 CRORE TRANSACTION RECORDS" from ≈4.4 s.

**Shot 2b (6.70–9.26 s) – only yesterday's transactions:**
"Same style and palette. A small glass calendar-page glyph (no readable date) lifts above the wall and a thin Date Sky marker line points to one narrow strip of the wall, which glows warm Sun Yellow while the rest of the wall dims. No readable text, no logos, no watermark."
Motion: 6.93–7.3 s the calendar glyph lifts on "Meeku"; ≈7.3–8.0 s the Sky marker aims on "only yesterday"; ≈8.4–9.02 s the narrow strip glows on "transactions kavali".
Overlay (post): "ONLY YESTERDAY'S TRANSACTIONS" from ≈7.3 s.

**Shot 2c (9.26–12.32 s) – scan all 10 crore records?:**
"Same style and palette. The wall resets. A wide Date Sky scan line sweeps across the entire wall, lighting every cell Sun Yellow. A soft white question-mark glow hovers above. No readable text, no logos, no watermark."
Motion: 9.49–10.0 s the wall resets on "Ippudu Snowflake"; ≈10.0–11.6 s the scan line sweeps the whole wall on "anni 10 crore records scan cheyyala?".
Overlay (post): "SCAN ALL 10 CRORE RECORDS?" from 9.49 s.

**Shot 2d (12.32–16.23 s) – or only the required portion?:**
"Same style and palette. The wall resets again. This time a narrow Sky beam lights only a small neat portion of the wall and the rest stays dark and calm. A soft question-mark glow pulses above. Hold a calm still frame for the last 0.6 s. No readable text, no logos, no watermark."
Motion: 12.49–13.2 s the wall resets on "Leda"; ≈13.2–15.62 s the narrow beam lights a small portion on "required data unna portion matrame scan chesthundha?" (portion ≈14.2 s); 15.62–16.23 s calm hold during the scripted pause.
Overlay (post): "OR ONLY THE REQUIRED PORTION?" from 12.49 s.

**Audio sync:** wall at 3.78 s; calendar at 6.93 s; full sweep at ≈10.0 s; narrow beam at ≈13.2 s.
**Negative prompt (all shots):** "Readable numbers, real transaction data, human faces, the answer shown too early, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Exactly! Partition Pruning (16.23–19.92 s · 3.69 s)
**Voice-over:** "Exactly! Dheenine Partition Pruning antaru!"
**Tone:** excited, reveal.
**Visual objective:** Name the answer: Partition Pruning.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB. The wall of cells shrinks into a neat honeycomb of rounded glass tiles with rose strips. A Sky beam passes over it: a few tiles light Sun Yellow and the others dim to Teal-Grey and stay in place. Big clean empty space above for a large title. Soft light burst. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 16.83–17.50 s: a bright flash on "Exactly!". **Effect: Impact frame** — a one-frame flash at 16.83 s.
- 17.88–19.71 s: the beam passes and the title lands on "Dheenine Partition Pruning antaru!" (Partition Pruning ≈18.4–19.0 s). **Effect: Letter dive** — the title letters settle fully before 19.2 s.
**Audio sync:** flash at 16.83 s; title at ≈18.4 s.
**On-screen text (overlay, post):** "PARTITION PRUNING" at ≈18.4 s.
**Negative prompt:** "Misspelled title, skipped tiles deleted or blown away, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Let's understand, welcome (19.92–22.99 s · 3.07 s)
**Voice-over:** "Let's understand! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Date Sky #7CC8FF, text #F5FAFB. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft warm glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 20.12–20.74 s a small subtitle pops in on "Let's understand!"; 21.21–22.70 s a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** subtitle at 20.12 s; logo and panel at 21.21 s; "NDR" at ≈21.9 s.
**On-screen text (overlay, post):** "LET'S UNDERSTAND!" at 20.12 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 21.21 s.
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – Micro-partitions and their metadata (22.99–33.79 s · 10.80 s)
**Voice-over:** "Snowflake lo data automatically Micro-partitions lo store avuthundhi. Prathi Micro-partition ki metadata maintain chesthundhi. For example, minimum date and maximum date information untundhi."
**Tone:** clear.
**Visual objective:** Data is stored automatically in micro-partitions, each has metadata, such as a minimum date and a maximum date.
Generate as **three shots (5a–5c)**. Keep the table position and tile style identical in every shot.

**Shot 5a (22.99–27.09 s) – stored in micro-partitions:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Metadata Rose #FF9DB8, text #F5FAFB. A large white glass table block with rows of cells floats at the centre. It separates into a neat grid of many small rounded glass tiles that slide into place automatically. Soft rim lighting, slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 23.27–24.4 s the table appears on "Snowflake lo data"; ≈24.4–26.89 s it separates into tiles on "automatically Micro-partitions lo store avuthundhi" (Micro-partitions ≈25.2 s).
Overlay (post): "MICRO-PARTITIONS" at ≈25.2 s.

**Shot 5b (27.09–30.20 s) – metadata for every one:**
"Same style and palette. A thin Metadata Rose strip draws along the bottom of every tile in turn, rippling across the grid. One tile lifts and its strip glows. No readable text, no logos, no watermark."
Motion: 27.28–28.5 s the strips ripple on "Prathi Micro-partition ki"; ≈28.5–30.0 s one tile lifts and glows on "metadata maintain chesthundhi". **Effect: Rack focus** — focus pulls from the grid to the lifted tile at ≈28.5 s.
Overlay (post): "METADATA FOR EVERY MICRO-PARTITION" from ≈28.5 s.

**Shot 5c (30.20–33.79 s) – minimum date and maximum date:**
"Same style and palette, plus Date Sky #7CC8FF. In close-up, the lifted tile's Rose strip shows a left end marker and a right end marker with a bar between them (a date range, no readable dates). Two tiny calendar glyphs light at the two ends. No readable text, no logos, no watermark."
Motion: 30.40–31.3 s the strip steadies on "For example,"; ≈31.3–32.2 s the left marker and calendar light on "minimum date"; ≈32.4–33.0 s the right marker and calendar light on "maximum date"; ≈33.1–33.6 s a soft glow on "information untundhi". **Effect: Comment drop** — a small Rose note drops in beside the tile at ≈33.1 s.
Overlay (post): "MINIMUM DATE" at ≈31.3 s; "MAXIMUM DATE" at ≈32.4 s.

**Audio sync:** tiles at ≈25.2 s; strips at 27.28 s; min at ≈31.3 s; max at ≈32.4 s.
**Negative prompt (all shots):** "Readable dates, specific tile sizes or counts, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – How pruning works (33.79–44.90 s · 11.11 s)
**Voice-over:** "Ippudu manam WHERE condition use chesi specific date data adigithe, Snowflake metadata ni check chesthundhi. Required data leni Micro-partitions ni skip chesthundhi. Dheenine Partition Pruning antaru."
**Tone:** clear.
**Visual objective:** With a WHERE date condition, Snowflake checks the metadata and skips the micro-partitions that do not have the required data.
Generate as **three shots (6a–6c)**.

**Shot 6a (33.79–39.63 s) – WHERE date, check metadata:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB. A honeycomb of rounded glass tiles with rose date-range strips fills the lower two thirds. A vertical Date Sky marker line (a single date) drops over the tiles. A thin Sky beam then sweeps over the rose strips only, and the strips pulse as they are checked. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 33.98–35.2 s the filter glyph and marker drop in on "Ippudu manam WHERE condition" (WHERE ≈34.6 s); ≈36.0–37.42 s the marker settles on "specific date data adigithe"; 37.67–39.45 s the beam checks the strips on "Snowflake metadata ni check chesthundhi". **Effect: Live cursor.**
Overlay (post): "WHERE DATE = ONE SPECIFIC DATE" from ≈34.6 s; "CHECK METADATA" at 37.67 s.

**Shot 6b (39.63–42.71 s) – skip the micro-partitions without the required data:**
"Same style and palette. The tiles whose rose range includes the Sky marker light Sun Yellow. All the other tiles dim to Pruned Teal-Grey and slide very slightly back, skipped. The skipped tiles remain in the table; none are removed. No readable text, no logos, no watermark."
Motion: 39.80–40.6 s the matching tiles light on "Required data"; ≈40.6–41.5 s the others dim on "leni Micro-partitions ni"; ≈42.0–42.54 s the dimmed tiles slide back on "skip chesthundhi".
Overlay (post): "SKIP MICRO-PARTITIONS WITHOUT THE REQUIRED DATA" from ≈40.2 s.

**Shot 6c (42.71–44.90 s) – Partition Pruning:**
"Same style and palette. The lit tiles and the dim tiles hold still while a clean soft light line frames the arrangement. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 42.88–43.4 s the frame line draws on "Dheenine"; 43.4–44.3 s the title presses in on "Partition Pruning antaru". **Effect: Press font** — "PARTITION PRUNING" presses into place at ≈43.4 s.
Overlay (post): "PARTITION PRUNING" at ≈43.4 s.

**Audio sync:** marker at ≈34.6 s; metadata check at 37.67 s; dimming at ≈40.6 s; title at ≈43.4 s.
**Negative prompt (all shots):** "Skipped tiles deleted or blown away, readable dates, counts or percentages, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Less scanning, better performance (44.90–49.81 s · 4.91 s)
**Voice-over:** "Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu."
**Tone:** clear.
**Visual objective:** Pruning reduces unnecessary scanning, and query performance can improve.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Date Sky #7CC8FF, text #F5FAFB. A simple side-by-side comparison: on the left a faint ghost of the whole honeycomb lit entirely (everything scanned); on the right the real result with only a few tiles lit Sun Yellow and the rest dim. A small soft gauge-arc (no numbers) on the right fills a little more than the left. Calm, satisfying. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 45.07–46.0 s: the ghost and the real result appear on "Dheenivalla".
- ≈45.9–47.4 s: the lit area on the right shrinks on "unnecessary data scanning reduce avuthundhi".
- ≈48.2–49.61 s: the gauge fills slightly on "query performance improve avvachu". **Effect: Rack focus** — focus pulls from the ghost to the real result at ≈47.4 s.
**Audio sync:** shrink at ≈47.4 s; gauge at ≈48.2 s.
**On-screen text (overlay, post):** "LESS UNNECESSARY SCANNING" from ≈45.9 s; "CAN IMPROVE QUERY PERFORMANCE" from ≈48.2 s. Show "can improve", with no numbers.
**Negative prompt:** "Performance numbers, percentages, guaranteed speed claims, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – Banking project example (49.81–73.76 s · 23.95 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS table lo 10 crore records unnayi. Manaki November 18th transactions matrame kavali. SQL query chuddam! SELECT * FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18'; Snowflake metadata ni use chesi, required data unna Micro-partitions ni identify chesthundhi. Migatha unnecessary Micro-partitions ni skip chesthundhi."
**Tone:** storytelling.
**Visual objective:** A date query on a 10 crore-row TRANSACTIONS table scans only the micro-partitions that hold November 18th and skips the rest.
Generate as **six shots (8a–8f)**. All shots use the same camera language and layout so the story reads as one build.

**Shot 8a (49.81–51.97 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Date Sky #7CC8FF, text #F5FAFB. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in warm yellow, with an empty glass table frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈50.4 s.

**Shot 8b (51.97–54.82 s) – 10 crore records:**
"Same style and palette. The glass table frame fills with a dense block of tiny glowing cells, then splits into its honeycomb of micro-partition tiles with rose strips. The camera pulls back to show how many there are. No readable fine text, no logos."
Overlay (post): "TRANSACTIONS" at ≈52.6 s (monospace); "10 CRORE RECORDS" at ≈53.4 s.

**Shot 8c (54.82–58.04 s) – only November 18th:**
"Same style and palette. A glass calendar-page glyph (no readable date) lifts above the honeycomb and a Date Sky marker line drops over the tiles. No readable fine text, no logos."
Motion: 55.00–55.6 s the calendar glyph lifts on "Manaki"; ≈55.6–56.4 s the marker drops on "November 18th"; ≈57.0–57.84 s the marker glows on "transactions matrame kavali".
Overlay (post): "NOVEMBER 18TH" at ≈55.6 s; "ONLY NOVEMBER 18TH TRANSACTIONS" from ≈56.0 s.

**Shot 8d (58.04–65.47 s) – SQL query:**
"Same style and palette. A dark glass code editor panel (a clean window with three empty lines, no readable code) floats at the centre with a thin Date Sky edge and a blinking cursor. Behind it, softly out of focus, the honeycomb glows. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 58.23–59.15 s the panel slides in on "SQL query chuddam!"; 59.62–61.33 s lines 1–2 type on "SELECT * FROM TRANSACTIONS"; 61.56–65.25 s line 3 types on "WHERE TRANSACTION_DATE = '2026-11-18';". **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
SELECT *
FROM TRANSACTIONS
WHERE TRANSACTION_DATE = '2026-11-18';
```
"SELECT *" at 59.62 s; "FROM TRANSACTIONS" at ≈60.4 s; "WHERE TRANSACTION_DATE = '2026-11-18';" from 61.56 s (the date completes by ≈65.2 s).

**Shot 8e (65.47–70.61 s) – identify the required micro-partitions:**
"Same style and palette. The code panel shrinks to the top. A Sky beam sweeps over the rose strips of the honeycomb and the strips pulse. Then the tiles whose range includes the date marker light Sun Yellow. No readable text, no logos."
Motion: 65.68–67.4 s the beam checks the strips on "Snowflake metadata ni use chesi"; ≈67.6–69.6 s the matching tiles light on "required data unna Micro-partitions ni identify chesthundhi" (Micro-partitions ≈68.6 s).
Overlay (post): "USE METADATA" at ≈66.4 s; "IDENTIFY THE REQUIRED MICRO-PARTITIONS" from ≈67.6 s.

**Shot 8f (70.61–73.76 s) – skip the rest:**
"Same style and palette. The remaining tiles fade to Pruned Teal-Grey and slide very slightly back, skipped. They remain visible in the honeycomb. Calm, clear. No readable text, no logos."
Motion: 70.77–71.5 s the tiles begin to dim on "Migatha"; ≈71.5–72.6 s the dimming spreads on "unnecessary Micro-partitions"; ≈72.6–73.55 s a soft wave passes over them on "skip chesthundhi".
Overlay (post): "SKIP UNNECESSARY MICRO-PARTITIONS" from ≈71.5 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake dates in the generated video, skipped tiles deleted or blown away, counts or percentages, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 9 – Simple recap (73.76–80.63 s · 6.87 s)
**Voice-over:** "So, simple ga gurthupettukondi! Partition Pruning means skipping unnecessary Micro-partitions to reduce data scanning."
**Tone:** confident.
**Visual objective:** One-line recap.
Generate as **two shots (9a, 9b)**.

**Shot 9a (73.76–75.76 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, text #F5FAFB. A calm honeycomb of tiles glides to the centre with a soft warm bloom against the dark background. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈74.2 s.

**Shot 9b (75.76–80.63 s) – the definition:**
"Same style and palette. A Sky beam lights a few tiles Sun Yellow while the others dim to Teal-Grey and stay in place; a soft frame draws around the dimmed tiles to show they are skipped. Clean and calm. No readable text, no logos."
Motion: 75.92–77.2 s the honeycomb brightens on "Partition Pruning means"; ≈77.2–79.0 s the others dim on "skipping unnecessary Micro-partitions"; ≈79.0–80.42 s the scanned area stays small on "to reduce data scanning". **Effect: Liquid glass** — the recap line sits on a glass panel.
Overlay (post): "PARTITION PRUNING = SKIPPING UNNECESSARY MICRO-PARTITIONS TO REDUCE DATA SCANNING" from 75.92 s.

**Audio sync:** dimming at ≈77.2 s.
**Negative prompt:** "Numbers, skipped tiles deleted, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Series card and teaser (80.63–90.67 s · 10.04 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Seventeen! Next video lo Result Cache, Warehouse Cache and Metadata Cache madhya differences real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 17 and tease the next topic.
Generate as **two shots (10a, 10b)**.

**Shot 10a (80.63–83.95 s) – Day 17 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first seventeen lit in Sun Yellow (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 17" from ≈81.6 s; the seventeenth node lights at ≈83.2 s on "Seventeen".

**Shot 10b (83.95–90.67 s) – teaser: three caches:**
"Same style and palette. A teaser panel slides in with three glass cards in a row, each with a different small glow (a result-card, a warehouse block, a metadata strip), linked by thin lines. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: RESULT CACHE · WAREHOUSE CACHE · METADATA CACHE" — "RESULT CACHE" at ≈85.0 s, "WAREHOUSE CACHE" at ≈86.3 s, "METADATA CACHE" at ≈87.6 s; "REAL-TIME EXAMPLES" from ≈89.0 s. The visual only suggests three different cards. Do not show how each cache works or any numbers. **Effect: Head stack.**

**Audio sync:** card at ≈81.6 s; the seventeenth node at ≈83.2 s; the three caches at ≈85.0, ≈86.3 and ≈87.6 s.
**Negative prompt:** "Technical claims about caches, numbers, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 11 – Follow, contact and end card (90.67–101.72 s · 11.05 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (11a–11c)**.

**Shot 11a (90.67–96.38 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0C1418, Sun Yellow #FFD84D, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB. A calm, clean background with a soft warm glow, a small honeycomb of glass tiles drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈91.6 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈93.0 s, emphasised at ≈95.3 s on "Follow" (estimated).

**Shot 11b (96.38–99.68 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Sun Yellow and Rose glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 96.58 s, emphasised at ≈98.8 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 11c (99.68–101.72 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 99.85 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 17. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #0C1418, Sun Yellow #FFD84D, Pruned Teal-Grey #4F6B72, Metadata Rose #FF9DB8, Date Sky #7CC8FF, text #F5FAFB, secondary text #9DB3B9. Colour code: a micro-partition is a rounded glass tile with a thin Rose date-range strip (a left end and a right end marker, no readable dates); the WHERE date is a vertical Date Sky marker line; a tile whose range includes the marker is lit Sun Yellow (scanned); a tile whose range does not is dim Pruned Teal-Grey (skipped, still present, never deleted or blown away). A query first checks the Rose metadata strips, then scans only the tiles that hold the required data and skips the rest. Never show tile sizes, counts, percentages or speed numbers; the only numbers allowed are '10 CRORE' and the script's date. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–16: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day17.mp3` (101.72 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, labels, "10 CRORE", "NOVEMBER 18TH", the SQL code, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (soft tile clicks, a scan whoosh, a gentle tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at the three question beats (≈4.4, ≈10.0, ≈13.2 s), at "Exactly!" (16.83 s), at the tiles and metadata (≈25.2, 27.28 s), at min and max dates (≈31.3, ≈32.4 s), at WHERE (≈34.6 s), at the skip (≈40.6 s), at each SQL line (59.62, 61.56 s), at the final skip (≈71.5 s), at the final tagline (99.85 s), and at the Follow and Contact lines (≈95.3, ≈98.8 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Snowflake automatically stores table data in micro-partitions; each micro-partition has metadata, such as a minimum date and a maximum date; with a WHERE date condition Snowflake checks the metadata, identifies the micro-partitions that hold the required data and skips the rest; this is Partition Pruning; it reduces unnecessary data scanning and query performance can improve. **No sizes, counts, percentages or performance numbers** are shown, because the script gives none. `SELECT * FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18';` is valid Snowflake syntax.
- The visuals are a beginner-friendly simplification: they show tiles with date ranges and do not claim how many micro-partitions a real query would skip.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
