# Thirty Days of Snowflake – Day 19: What is a Materialized View?
Video prompt package (NDR EdTech) — `Audio\day19.mp3` + `days-scripts\day19.txt`, analysed with Whisper

> **Timing status: MEASURED from day19.mp3 (106.37 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (3 items):**
> 1. **SQL lines (58–71 s):** the pauses split the spoken SQL into five chunks, but the exact word boundaries inside the code are estimated (≈). The order is certain: CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS → SELECT TRANSACTION_DATE, → COUNT(*) → AS TOTAL_TRANSACTIONS FROM TRANSACTIONS → GROUP BY TRANSACTION_DATE;
> 2. **Follow and Contact lines (about 95–104 s):** Whisper's word order for these Telugu lines is unreliable, so the "Follow" and "Contact" times are estimated (≈).
> 3. **There is no scripted `[pause]`** in this script. The longest pause is 0.6 s.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 19: What is a Materialized View? |
| Duration | **106.37 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,191 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day19.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (26 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Crystal Ledger" (new for Day 19)
| Role | HEX | Use |
|---|---|---|
| Background | `#0B1030` | Base, gradients (midnight cobalt) |
| Materialized View Gold | `#FFC15E` | The **Materialized View**: a solid block that holds stored, pre-computed results |
| Normal View Periwinkle | `#9FB4FF` | The **Normal View**: a hollow outline that holds only the SQL definition |
| Auto-Maintain Mint | `#5BF0B5` | Snowflake automatically maintaining the Materialized View (a refresh ring) |
| Table Glass | `#DDE6FF` | Base tables, SQL cards, neutral glass |
| Primary text | `#F6F8FF` | Titles, labels |
| Secondary text | `#9AA6CC` | Captions |

**Colour code (use in every scene):** Normal View = a **hollow Periwinkle outline** with query lines inside and **no data** · Materialized View = a **solid Gold block** with stored result rows inside · Automatic maintenance = a **Mint refresh ring** · Base table = Table Glass.

**The core visual rule (technical accuracy):** a **Normal View stores only the SQL query definition**. A **Materialized View stores the pre-computed query results physically**, and **Snowflake maintains it automatically when the underlying table data changes**. This can improve performance for repeated and expensive queries. Show abstract shapes only. Do not show timings, sizes, costs or percentages, and do not claim that it is always faster.

### Motion effects used (from the skill's effects library)
Comment drop, Orbit ring, Letter dive, Impact frame, Liquid glass, Press font, Live cursor, Code body, Rack focus, Head stack. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.89 | "Hello guys! Andaru ela unnaru?" (0.00–1.89) · "Oka situation imagine cheyyandi!" (2.34–3.67) | Curious | Title hook |
| 2 | 3.89–13.00 | "Mee company lo daily millions of transaction records unnayi." (4.10–7.08) · "Prathi sari monthly report generate cheyyalante same calculations malli malli execute cheyyalsi vastundhi!" (7.52–12.77) | Worried | Millions of records, the same calculations again and again |
| 3 | 13.00–20.44 | "Ila repeated calculations avoid cheyyadaniki Snowflake lo oka powerful feature undhi!" (13.23–17.52) · "Adhe Materialized View!" (17.92–19.20) · "Let's understand!" (19.58–20.17) | Excited, reveal | Feature reveal, title |
| 4 | 20.44–22.57 | "Welcome to NDR EdTech!" (20.70–22.34) | Welcoming | Brand welcome |
| 5 | 22.57–40.32 | "Materialized View ante pre-computed query results ni store chese database object." (22.79–27.13) · "Normal View lo SQL query definition matrame store avuthundhi." (27.64–30.99) · "Kaani Materialized View lo query results physically store avuthayi." (31.38–34.54) · "Underlying table data change ayinappudu, Snowflake Materialized View ni automatically maintain chesthundhi." (34.94–40.12) | Clear | Definition, Normal View vs Materialized View, auto maintenance |
| 6 | 40.32–44.41 | "Dheenivalla repeated and expensive queries ki performance improve avvachu." (40.51–44.20) | Clear | Better performance |
| 7 | 44.41–75.13 | "Oka Banking project example teesukundham." (44.61–46.41) · "Mana TRANSACTIONS table lo millions of records unnayi." (46.82–49.36) · "Manaki daily transaction summary kavali." (49.74–51.68) · "Prathi sari GROUP BY calculation execute cheyyakunda, Materialized View create cheyyachu." (52.06–56.27) · "SQL command chuddam!" (56.68–57.62) · "CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS SELECT TRANSACTION_DATE, COUNT(*) AS TOTAL_TRANSACTIONS FROM TRANSACTIONS GROUP BY TRANSACTION_DATE;" (58.05–70.65) · "Ippudu daily transaction summary query cheyyadaniki Materialized View ni use cheyyachu." (71.06–74.83) | Storytelling | Banking: a daily summary Materialized View |
| 8 | 75.13–85.84 | "So, simple ga gurthupettukondi!" (75.43–77.08) · "Normal View – Stores SQL query definition." (77.49–80.12) · "Materialized View – Stores pre-computed query results and Snowflake maintains it automatically." (80.56–85.62) | Confident | Two-card recap |
| 9 | 85.84–95.25 | "Idi mana Thirty Days of Snowflake series lo Day Nineteen!" (86.05–88.98) · "Next video lo Snowflake RBAC – Roles and Privileges gurinchi real-time examples tho explain chesthanu." (89.40–95.05) | Upbeat | Day 19 card, RBAC teaser |
| 10 | 95.25–106.37 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (95.44–100.72) · "Full course details kosam NDR EdTech ni Contact avvandi!" (101.12–104.08) · "Let's Learn and Grow Together!" (104.48–105.95) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.64–1.01, 1.89–2.34, 3.67–4.10, 7.08–7.52, 12.77–13.23, 17.52–17.92, 18.17–18.39, 19.20–19.58, 20.17–20.70, 22.34–22.79, 27.13–27.64, 30.99–31.38, 34.54–34.94, 40.12–40.51, 44.20–44.61, 46.41–46.82, 49.36–49.74, 51.68–52.06, 56.27–56.68, 57.62–58.05, 63.02–63.22, 65.04–65.47, 66.67–66.88, 68.98–69.23, 70.65–71.06, 74.83–75.43, 77.08–77.49, 78.12–78.40, 80.12–80.56, 81.40–81.64, 85.62–86.05, 88.98–89.40, 91.56–91.79, 95.05–95.44, 100.72–101.12, 104.08–104.48, 105.95–106.37.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee company lo daily millions of transaction records unnayi. | daily millions ≈5.0–5.8 · transaction records ≈6.2 |
| Prathi sari monthly report generate cheyyalante same calculations malli malli execute cheyyalsi vastundhi! | monthly report ≈8.2 · same calculations ≈9.7 · malli malli ≈10.8 · execute ≈11.8 |
| Ila repeated calculations avoid cheyyadaniki Snowflake lo oka powerful feature undhi! | repeated calculations ≈14.0 · avoid ≈15.2 · powerful feature ≈16.6 |
| Adhe Materialized View! | Adhe 17.92 · Materialized View 18.39 |
| Let's understand! | Let's 19.58 · understand 19.8 |
| Welcome to NDR EdTech! | Welcome 20.70 · NDR ≈21.4 · EdTech ≈21.8 |
| Materialized View ante pre-computed query results ni store chese database object. | Materialized View 22.79 · pre-computed query results ≈23.9–25.5 · database object ≈26.3 |
| Normal View lo SQL query definition matrame store avuthundhi. | Normal View 27.64 · SQL query definition ≈29.0 · matrame ≈30.2 |
| Kaani Materialized View lo query results physically store avuthayi. | Materialized View ≈32.0 · query results ≈33.0 · physically ≈33.8 |
| Underlying table data change ayinappudu, Snowflake Materialized View ni automatically maintain chesthundhi. | Underlying table data change ≈35.0–36.2 · Snowflake Materialized View ≈37.0 · automatically ≈38.5 · maintain ≈39.4 |
| Dheenivalla repeated and expensive queries ki performance improve avvachu. | repeated and expensive queries ≈41.0–43.0 · performance improve ≈43.4 |
| Oka Banking project example teesukundham. | Banking ≈44.9 · example ≈45.8 |
| Mana TRANSACTIONS table lo millions of records unnayi. | TRANSACTIONS ≈47.2 · millions ≈48.2 |
| Manaki daily transaction summary kavali. | daily transaction summary ≈50.2 · kavali ≈51.3 |
| Prathi sari GROUP BY calculation execute cheyyakunda, Materialized View create cheyyachu. | GROUP BY ≈53.0 · calculation execute cheyyakunda ≈54.0 · Materialized View ≈55.0 |
| SQL command chuddam! | SQL 56.68 |
| CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS | CREATE MATERIALIZED VIEW ≈58.1–60.5 · DAILY_TXN_SUMMARY ≈60.8–62.8 |
| SELECT TRANSACTION_DATE, | SELECT 63.22 · TRANSACTION_DATE ≈63.9–65.0 |
| COUNT(*) | COUNT(*) 65.47–66.67 |
| AS TOTAL_TRANSACTIONS FROM TRANSACTIONS | AS TOTAL_TRANSACTIONS 66.88–68.0 · FROM TRANSACTIONS ≈68.2–68.98 |
| GROUP BY TRANSACTION_DATE; | GROUP BY 69.23–69.8 · TRANSACTION_DATE ≈69.9–70.65 |
| Ippudu daily transaction summary query cheyyadaniki Materialized View ni use cheyyachu. | daily transaction summary ≈71.8 · Materialized View ≈73.0 · use ≈74.0 |
| So, simple ga gurthupettukondi! | So 75.43 · gurthupettukondi ≈76.3 |
| Normal View – Stores SQL query definition. | Normal View 77.49 · Stores SQL query definition 78.40 |
| Materialized View – Stores pre-computed query results and Snowflake maintains it automatically. | Materialized View 80.56 · pre-computed query results ≈82.4 · Snowflake maintains it automatically ≈84.0 |
| Idi mana Thirty Days of Snowflake series lo Day Nineteen! | Thirty ≈86.8 · Snowflake ≈87.6 · Nineteen ≈88.2 |
| Next video lo Snowflake RBAC – Roles and Privileges gurinchi real-time examples tho explain chesthanu. | RBAC ≈90.4 · Roles and Privileges ≈92.0–93.0 · real-time examples ≈93.6 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈97.2 · NDR EdTech ≈98.0–99.2 · **Follow** ≈99.5 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 101.12–102.4 · NDR EdTech ≈102.6 · **Contact** ≈103.3 (estimated) |
| Let's Learn and Grow Together! | Let's 104.48 · Together ≈105.4 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, Auto-Maintain Mint #5BF0B5, Table Glass #DDE6FF, text #F6F8FF.*

**Object look (keep identical in every scene):** a **base table** = a Table Glass block with rows of small cells. A **Normal View** = a hollow Periwinkle outline frame with query lines inside and no data. A **Materialized View** = a solid Gold glass block with stored result rows inside. **Automatic maintenance** = a thin Mint ring that sweeps around the Gold block.

### Scene 1 – Hook (0.00–3.89 s · 3.89 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka situation imagine cheyyandi!"
**Tone:** curious.
**Visual objective:** Welcome viewers and ask them to imagine a situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, Auto-Maintain Mint #5BF0B5, Table Glass #DDE6FF, text #F6F8FF. A deep midnight-cobalt space with soft golden light and drifting glass particles. A glowing glass table block floats at the upper-centre and a soft thought-bubble of glass forms above it. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–1.89 s: particles drift in and the table appears on "Hello guys! Andaru ela unnaru?".
- 2.34–3.67 s: the thought-bubble forms on "Oka situation imagine cheyyandi!".
- 3.67–3.89 s: soft light sweep into Scene 2.
- Effect: **Comment drop** — the thought-bubble drops in beside the table at ≈2.6 s.
**Audio sync:** title lands at ≈1.0 s; the sweep completes in the pause at 3.67–4.10 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 19".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – The same calculations again and again (3.89–13.00 s · 9.11 s)
**Voice-over:** "Mee company lo daily millions of transaction records unnayi. Prathi sari monthly report generate cheyyalante same calculations malli malli execute cheyyalsi vastundhi!"
**Tone:** worried.
**Visual objective:** A huge table and a monthly report that needs the same calculations to be run again and again.
Generate as **two shots (2a, 2b)**.

**Shot 2a (3.89–7.30 s) – millions of transaction records:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0B1030, Table Glass #DDE6FF, Materialized View Gold #FFC15E, text #F6F8FF. A vast, dense Table Glass table block fills the frame with rows of tiny glowing cells and stretches far into the distance, with a small glass company-building glyph (no logo) above it. The camera pulls back slowly to show the scale. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.10–5.0 s the building glyph and table appear on "Mee company lo"; ≈5.0–6.2 s the camera pulls back on "daily millions of transaction records"; 6.2–7.08 s the table fills the frame on "unnayi".
Overlay (post): "DAILY MILLIONS OF TRANSACTION RECORDS" from ≈5.0 s.

**Shot 2b (7.30–13.00 s) – the same calculations again and again:**
"Same style and palette. A glass monthly-report page (abstract bars, no readable text) is requested. A cluster of calculation glyphs (plus, sigma, bars) appears over the table and runs, then the whole cluster appears again and again in a repeating loop, each time lighting the table. The loop's glow grows heavier and warmer. Tense, repetitive. No readable text, no logos, no watermark."
Motion: 7.52–8.8 s the report page appears on "Prathi sari monthly report generate cheyyalante" (monthly report ≈8.2 s); ≈9.7 s the first calculation cluster runs on "same calculations"; ≈10.8–12.77 s the loop repeats several times on "malli malli execute cheyyalsi vastundhi!". **Effect: Orbit ring** — the calculation cluster circles the table in a repeating loop.
Overlay (post): "MONTHLY REPORT" from ≈8.2 s; "SAME CALCULATIONS AGAIN AND AGAIN" from ≈9.7 s.

**Audio sync:** report page at ≈8.2 s; first cluster at ≈9.7 s; loop at ≈10.8 s.
**Negative prompt (all shots):** "Readable numbers, readable text, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – A powerful feature: Materialized View (13.00–20.44 s · 7.44 s)
**Voice-over:** "Ila repeated calculations avoid cheyyadaniki Snowflake lo oka powerful feature undhi! Adhe Materialized View! Let's understand!"
**Tone:** excited, reveal.
**Visual objective:** Reveal the feature and name the topic.
Generate as **two shots (3a, 3b)**.

**Shot 3a (13.00–17.72 s) – avoid repeated calculations:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Table Glass #DDE6FF, text #F6F8FF. The repeating calculation loop from the last shot slows, then a soft golden light cuts through it and the loop dissolves into calm. A glowing glass snowflake-crystal emblem rises at the upper-centre. Hopeful, satisfying. Slow push-in. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 13.23–15.2 s the loop slows on "Ila repeated calculations avoid cheyyadaniki"; ≈15.2–16.6 s the golden light cuts through on "Snowflake lo oka"; ≈16.6–17.52 s the emblem rises on "powerful feature undhi!".
Overlay (post): "AVOID REPEATED CALCULATIONS" from 13.23 s.

**Shot 3b (17.72–20.44 s) – Materialized View, let's understand:**
"Same style and palette. The emblem moves up and a solid Gold glass block with stored result rows inside appears beneath it with a soft bloom. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark."
Motion: 17.92–18.17 s a soft glow on "Adhe"; 18.39–19.20 s the title lands on "Materialized View!" (**Effect: Impact frame** — one-frame flash at 18.39 s; **Effect: Letter dive** — the letters settle fully before 19.1 s); 19.58–20.17 s a subtitle pops in on "Let's understand!".
Overlay (post): "MATERIALIZED VIEW" at 18.39 s; "LET'S UNDERSTAND!" at 19.58 s.

**Audio sync:** light cuts through at ≈15.2 s; title at 18.39 s; subtitle at 19.58 s.
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Welcome (20.44–22.57 s · 2.13 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Table Glass #DDE6FF, text #F6F8FF. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft golden glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 20.70–22.34 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 20.70 s; "NDR" at ≈21.4 s; "EdTech" at ≈21.8 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – What a Materialized View is (22.57–40.32 s · 17.75 s)
**Voice-over:** "Materialized View ante pre-computed query results ni store chese database object. Normal View lo SQL query definition matrame store avuthundhi. Kaani Materialized View lo query results physically store avuthayi. Underlying table data change ayinappudu, Snowflake Materialized View ni automatically maintain chesthundhi."
**Tone:** clear.
**Visual objective:** A Materialized View is a database object that stores pre-computed query results; a Normal View stores only the query definition; a Materialized View stores results physically and Snowflake maintains it automatically.
Generate as **four shots (5a–5d)**. Keep the table position and the view styles identical in every shot.

**Shot 5a (22.57–27.39 s) – stores pre-computed query results:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Table Glass #DDE6FF, text #F6F8FF. A SQL query card runs once against a Table Glass base table and a small set of glowing result rows comes out, then slides into a solid Gold glass block (a database object) and locks in with a soft glow. Calm, clear, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 22.79–24.0 s the query runs on "Materialized View ante"; ≈24.0–25.5 s the result rows come out on "pre-computed query results"; ≈25.5–27.13 s the Gold block locks them in on "ni store chese database object" (database object ≈26.3 s).
Overlay (post): "MATERIALIZED VIEW" at 22.79 s; "STORES PRE-COMPUTED QUERY RESULTS" from ≈24.0 s.

**Shot 5b (27.39–31.19 s) – Normal View: only the definition:**
"Same style and palette, plus Normal View Periwinkle #9FB4FF. A hollow Periwinkle outline frame appears with only query lines inside it and no data rows; the frame is see-through and empty of results. A numbered tag 'Normal View'. Calm, clear. No readable text, no logos, no watermark."
Motion: 27.64–29.0 s the hollow frame draws on "Normal View lo"; ≈29.0–30.2 s the query lines appear inside on "SQL query definition"; ≈30.2–30.99 s the frame stays empty of data on "matrame store avuthundhi".
Overlay (post): "NORMAL VIEW" at 27.64 s; "STORES ONLY THE SQL QUERY DEFINITION" from ≈29.0 s.

**Shot 5c (31.19–34.74 s) – Materialized View: results physically stored:**
"Same style and palette. Beside the hollow Periwinkle frame, a solid Gold glass block fills with real result rows that glow from inside, to show that the results are physically stored. Calm, clear. No readable text, no logos, no watermark."
Motion: 31.38–33.0 s the Gold block appears on "Kaani Materialized View lo"; ≈33.0–34.54 s the result rows fill and glow on "query results physically store avuthayi" (physically ≈33.8 s). **Effect: Rack focus** — focus pulls from the hollow frame to the Gold block at ≈33.0 s.
Overlay (post): "MATERIALIZED VIEW" at ≈32.0 s; "QUERY RESULTS PHYSICALLY STORED" from ≈33.0 s.

**Shot 5d (34.74–40.32 s) – automatically maintained:**
"Same style and palette, plus Auto-Maintain Mint #5BF0B5. A few new rows appear at the bottom of the Table Glass base table (the underlying data changes). A thin Mint ring sweeps around the Gold block by itself and one new Gold row appears in it, so the Gold block is updated automatically. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 34.94–36.2 s the new rows drop into the base table on "Underlying table data change ayinappudu"; ≈37.0 s the Mint ring starts on "Snowflake Materialized View ni"; ≈38.5–40.12 s the Gold block updates on "automatically maintain chesthundhi" (automatically ≈38.5 s). **Effect: Comment drop** — a small Mint note drops in beside the ring at ≈38.5 s.
Overlay (post): "UNDERLYING TABLE DATA CHANGES" from ≈35.0 s; "SNOWFLAKE MAINTAINS IT AUTOMATICALLY" from ≈38.5 s.

**Audio sync:** query result at ≈24.0 s; hollow frame at 27.64 s; Gold block fills at ≈33.0 s; Mint ring at ≈37.0 s.
**Negative prompt (all shots):** "A Normal View shown with data, a Materialized View shown hollow, readable text, timings, costs, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – Better performance for repeated, expensive queries (40.32–44.41 s · 4.09 s)
**Voice-over:** "Dheenivalla repeated and expensive queries ki performance improve avvachu."
**Tone:** clear.
**Visual objective:** A Materialized View can improve performance for repeated and expensive queries.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Table Glass #DDE6FF, Auto-Maintain Mint #5BF0B5, text #F6F8FF. A simple side-by-side comparison: on the left a faint ghost of the repeated calculation loop over the whole table (heavy and slow); on the right the Gold block answering a query card straight away, with a calm Mint glow. A small soft gauge-arc (no numbers) on the right fills a little more than the left. Calm, satisfying. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 40.51–42.0 s: the ghost loop and the Gold block appear on "Dheenivalla repeated and expensive queries".
- ≈43.0–44.20 s: the gauge fills slightly on "performance improve avvachu". **Effect: Rack focus** — focus pulls from the ghost loop to the Gold block at ≈43.0 s.
**Audio sync:** comparison at 40.51 s; gauge at ≈43.4 s.
**On-screen text (overlay, post):** "REPEATED AND EXPENSIVE QUERIES" from ≈41.0 s; "CAN IMPROVE PERFORMANCE" from ≈43.4 s. Show "can improve", with no numbers.
**Negative prompt:** "Performance numbers, percentages, guaranteed speed claims, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (44.41–75.13 s · 30.72 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS table lo millions of records unnayi. Manaki daily transaction summary kavali. Prathi sari GROUP BY calculation execute cheyyakunda, Materialized View create cheyyachu. SQL command chuddam! CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS SELECT TRANSACTION_DATE, COUNT(*) AS TOTAL_TRANSACTIONS FROM TRANSACTIONS GROUP BY TRANSACTION_DATE; Ippudu daily transaction summary query cheyyadaniki Materialized View ni use cheyyachu."
**Tone:** storytelling.
**Visual objective:** A daily transaction summary over millions of rows is created once as a Materialized View, so the GROUP BY calculation does not run every time.
Generate as **seven shots (7a–7g)**. All shots use the same camera language and layout (base table at the bottom, Gold block above it, code panel in the middle when shown).

**Shot 7a (44.41–46.62 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Table Glass #DDE6FF, text #F6F8FF. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in warm gold, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈44.9 s.

**Shot 7b (46.62–51.87 s) – TRANSACTIONS and the daily summary:**
"Same style and palette. A very large Table Glass TRANSACTIONS table block fills the lower half with rows of tiny cells. A small glass summary-card (a few abstract bars grouped by day, no readable text) glows above it. No readable fine text, no logos."
Motion: 46.82–48.2 s the table appears on "Mana TRANSACTIONS table lo millions of records unnayi" (TRANSACTIONS ≈47.2 s); ≈50.2–51.68 s the summary-card glows on "Manaki daily transaction summary kavali".
Overlay (post): "TRANSACTIONS" at ≈47.2 s (monospace); "MILLIONS OF RECORDS" at ≈48.2 s; "DAILY TRANSACTION SUMMARY" at ≈50.2 s.

**Shot 7c (51.87–56.48 s) – no GROUP BY every time; create a Materialized View:**
"Same style and palette. The heavy calculation loop (a group-by funnel and calculation glyphs) starts over the table and is stopped by a soft golden hand-less barrier. A solid Gold glass block then slides in beside the table and takes the summary-card inside, as the stored summary. Calm, clear. No readable text, no logos."
Motion: 52.06–53.0 s the group-by funnel lights on "Prathi sari GROUP BY"; ≈54.0 s the loop is stopped on "calculation execute cheyyakunda"; ≈55.0–56.27 s the Gold block slides in on "Materialized View create cheyyachu".
Overlay (post): "NO GROUP BY CALCULATION EVERY TIME" from ≈53.0 s; "CREATE A MATERIALIZED VIEW" at ≈55.0 s.

**Shot 7d (56.48–63.12 s) – SQL: CREATE MATERIALIZED VIEW:**
"Same style and palette. A dark glass code editor panel (a clean window with five empty lines, no readable code) floats at the centre with a thin Gold edge and a blinking cursor. Behind it, softly out of focus, the table and the Gold block glow. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 56.68–57.62 s the panel slides in on "SQL command chuddam!"; 58.05–63.02 s line 1 types on "CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS" (DAILY_TXN_SUMMARY ≈60.8–62.8 s). **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS
```
"CREATE MATERIALIZED VIEW" at ≈58.1 s; "DAILY_TXN_SUMMARY AS" at ≈60.8 s.

**Shot 7e (63.12–66.78 s) – SQL: SELECT and COUNT(*):**
"Same style and palette. The code panel continues with the next lines while the summary-card's bars begin to form on the Gold block. No readable code, no logos, no watermark."
Motion: 63.22–65.04 s line 2 types on "SELECT TRANSACTION_DATE,"; 65.47–66.67 s line 3 types on "COUNT(*)". **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS
SELECT
    TRANSACTION_DATE,
    COUNT(*) AS TOTAL_TRANSACTIONS
```
"SELECT" at 63.22 s; "TRANSACTION_DATE," at ≈63.9 s; "COUNT(*)" at 65.47 s (the alias completes at ≈68.0 s in the next shot).

**Shot 7f (66.78–70.86 s) – SQL: FROM and GROUP BY:**
"Same style and palette. The code panel finishes the query. At the end of the last line a soft Gold glow runs along the line and the Gold block's bars settle, grouped by day. No readable code, no logos, no watermark."
Motion: 66.88–68.98 s the rest of line 3 and the FROM line type on "AS TOTAL_TRANSACTIONS FROM TRANSACTIONS"; 69.23–70.65 s the last line types on "GROUP BY TRANSACTION_DATE;". **Effect: Code body.**
Overlay (post, monospace; the full query shown at the end):
```sql
CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS
SELECT
    TRANSACTION_DATE,
    COUNT(*) AS TOTAL_TRANSACTIONS
FROM TRANSACTIONS
GROUP BY TRANSACTION_DATE;
```
"AS TOTAL_TRANSACTIONS" at 66.88 s; "FROM TRANSACTIONS" at ≈68.2 s; "GROUP BY TRANSACTION_DATE;" at 69.23 s.

**Shot 7g (70.86–75.13 s) – use the Materialized View:**
"Same style and palette. The code panel shrinks to the top. A fresh query card for the daily summary goes straight to the Gold block, which answers at once with the grouped bars, while the heavy table below stays calm and dark. A soft Mint ring turns slowly around the Gold block. No readable text, no logos."
Motion: 71.06–72.4 s the query card appears on "Ippudu daily transaction summary query cheyyadaniki"; ≈73.0–74.83 s the Gold block answers on "Materialized View ni use cheyyachu". **Effect: Rack focus** — focus pulls from the table to the Gold block at ≈73.0 s.
Overlay (post): "USE THE MATERIALIZED VIEW FOR THE DAILY SUMMARY" from ≈71.8 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake numbers in the generated video, wrong syntax, extra lines, timings or costs, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (75.13–85.84 s · 10.71 s)
**Voice-over:** "So, simple ga gurthupettukondi! Normal View – Stores SQL query definition. Materialized View – Stores pre-computed query results and Snowflake maintains it automatically."
**Tone:** confident.
**Visual objective:** Two-card recap.
Generate as **three shots (8a–8c)**.

**Shot 8a (75.13–77.29 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, text #F6F8FF. A hollow Periwinkle frame and a solid Gold block glide side by side to the centre with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈75.6 s.

**Shot 8b (77.29–80.34 s) – Normal View:**
"Same style and palette. The hollow Periwinkle frame fills the screen with query lines inside and no data. Clean and calm. No readable text, no logos."
Overlay (post): "NORMAL VIEW" at 77.49 s; "Stores SQL query definition" from 78.40 s. **Effect: Liquid glass** — the labels sit on a glass panel.

**Shot 8c (80.34–85.84 s) – Materialized View:**
"Same style and palette, plus Auto-Maintain Mint #5BF0B5. The solid Gold block fills the screen with stored result rows, while a Mint ring turns slowly around it. Clean and calm. No readable text, no logos."
Overlay (post): "MATERIALIZED VIEW" at 80.56 s; "Stores pre-computed query results" from ≈82.4 s; "Snowflake maintains it automatically" from ≈84.0 s.

**Audio sync:** card 1 at 77.49 s; card 2 at 80.56 s; Mint ring at ≈84.0 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (85.84–95.25 s · 9.41 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Nineteen! Next video lo Snowflake RBAC – Roles and Privileges gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 19 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (85.84–89.19 s) – Day 19 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, Auto-Maintain Mint #5BF0B5, text #F6F8FF. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first nineteen lit in Gold (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 19" from ≈86.8 s; the nineteenth node lights at ≈88.2 s on "Nineteen".

**Shot 9b (89.19–95.25 s) – teaser: RBAC, roles and privileges:**
"Same style and palette. A teaser panel slides in with a glass key and a small row of glass role-badges (abstract, no readable text) connected to a glowing glass table by thin lines. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: SNOWFLAKE RBAC" from ≈90.4 s; "ROLES AND PRIVILEGES" from ≈92.0 s; "REAL-TIME EXAMPLES" from ≈93.6 s. The visual only suggests keys and roles. Do not show specific privileges, role names or hierarchies.

**Audio sync:** card at ≈86.8 s; the nineteenth node at ≈88.2 s; the teaser title at ≈90.4 s.
**Negative prompt:** "Specific roles or privileges, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (95.25–106.37 s · 11.12 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (95.25–100.92 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, text #F6F8FF. A calm, clean background with a soft golden glow, a small Gold block and a Periwinkle frame drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈96.6 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈97.2 s, emphasised at ≈99.5 s on "Follow" (estimated).

**Shot 10b (100.92–104.28 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Gold and Periwinkle glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 101.12 s, emphasised at ≈103.3 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (104.28–106.37 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 104.48 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 19. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #0B1030, Materialized View Gold #FFC15E, Normal View Periwinkle #9FB4FF, Auto-Maintain Mint #5BF0B5, Table Glass #DDE6FF, text #F6F8FF, secondary text #9AA6CC. Colour code: a base table = a Table Glass block with rows of small cells; a Normal View = a hollow Periwinkle outline frame with only query lines inside and no data; a Materialized View = a solid Gold glass block with stored result rows inside; Snowflake maintaining it automatically = a thin Mint ring sweeping around the Gold block when the base table's data changes. A Normal View never holds data; a Materialized View always shows stored rows. Show 'can improve', never 'always faster'. Never show timings, sizes, costs or percentages. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–18: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day19.mp3` (106.37 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, labels, table and view names, the SQL code, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a soft lock-in click for the stored results, a gentle refresh chime for the Mint ring, a gentle tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at the calculation loop (≈9.7, ≈10.8 s), at the title (18.39 s), at the hollow frame and the Gold block (27.64, ≈33.0 s), at the Mint ring (≈37.0 s), at each SQL chunk (58.05, 63.22, 65.47, 66.88, 69.23 s), at the recap cards (77.49, 80.56 s), at the final tagline (104.48 s), and at the Follow and Contact lines (≈99.5, ≈103.3 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: a Materialized View is a database object that stores pre-computed query results; a Normal View stores only the SQL query definition; a Materialized View physically stores the query results; Snowflake maintains the Materialized View automatically when the underlying table data changes; this can improve performance for repeated and expensive queries. In the banking example, a daily transaction summary is created once as a Materialized View so the GROUP BY calculation does not run every time. **No timings, costs or percentages** are shown, because the script gives none. The SQL `CREATE MATERIALIZED VIEW DAILY_TXN_SUMMARY AS SELECT TRANSACTION_DATE, COUNT(*) AS TOTAL_TRANSACTIONS FROM TRANSACTIONS GROUP BY TRANSACTION_DATE;` is valid Snowflake syntax.
- **Optional addition (not in the script, so not shown on screen):** in Snowflake, Materialized Views are available from Enterprise Edition upwards. You may want to mention this in the caption or a pinned comment. Please verify it against Snowflake's current documentation before you publish it.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
