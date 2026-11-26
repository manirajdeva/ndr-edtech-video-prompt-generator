# Thirty Days of Snowflake – Day 18: Result Cache vs Warehouse Cache vs Metadata Cache
Video prompt package (NDR EdTech) — `Audio\day18.mp3` + `days-scripts\day18.txt`, analysed with Whisper

> **Timing status: MEASURED from day18.mp3 (123.72 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (3 items):**
> 1. **Follow and Contact lines (about 112–121 s):** Whisper's word order for these Telugu lines is unreliable, so the "Follow" and "Contact" times are estimated (≈).
> 2. **107.5–112.0 s:** Whisper heard "…explain materialized views and real-time examples. I will explain it in detail." Your script says "Next video lo Materialized Views gurinchi real-time examples tho explain chesthanu." The pauses show one phrase (107.47–111.92 s), so I treated it as your script's line.
> 3. **17.67–18.46 s** is your scripted `[pause]`, a real 0.79 s silence. The visuals hold a calm beat there.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 18: Result Cache vs Warehouse Cache vs Metadata Cache |
| Duration | **123.72 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,712 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day18.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (28 shots in 11 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Triple Cache" (new for Day 18)
| Role | HEX | Use |
|---|---|---|
| Background | `#12150D` | Base, gradients (olive-black) |
| Result Cache Aqua | `#4DE3C2` | **Result Cache**: a saved query result |
| Warehouse Cache Orange | `#FF9F43` | **Warehouse Cache**: the warehouse's local cache |
| Metadata Cache Lilac | `#B79CFF` | **Metadata Cache**: table metadata |
| Cloud Glass | `#E6F0FF` | SQL query cards, tables, neutral glass |
| Primary text | `#F7F9F2` | Titles, labels |
| Secondary text | `#A5AD95` | Captions |

**Colour code (use in every scene):** Result Cache = Aqua · Warehouse Cache = Orange · Metadata Cache = Lilac. A SQL query is a Cloud Glass card; a table is a Cloud Glass block with rows of cells; the **storage** under the table is a plain dim shelf.

**The core visual rule (technical accuracy):** the three caches are three different things.
- **Result Cache** = the *saved result of a query that ran before*. A repeat of the same query, when the eligible conditions are met, gets that saved result back (shown as an Aqua result-card on a shelf that is returned instantly).
- **Warehouse Cache** = *data the virtual warehouse already processed*, kept in the warehouse's **local** cache (shown as an Orange drawer attached to a warehouse block). If the warehouse is suspended, this local cache is cleared; the **table's data in storage stays untouched**.
- **Metadata Cache** = *table metadata* that can answer some queries without scanning the actual table data (shown as a Lilac index-strip that answers a COUNT without lighting the table).
Show abstract shapes only. No timings, sizes or percentages. Say "can help" and "eligible", never "always".

### Motion effects used (from the skill's effects library)
Letter dive, Impact frame, Liquid glass, Head stack, Press font, Live cursor, Comment drop, Blow away (only for the warehouse's local cache being cleared), Rack focus, Orbit ring. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.98 | "Hello guys! Andaru ela unnaru?" (0.00–2.10) · "Oka interesting question!" (2.46–3.75) | Curious | Title hook |
| 2 | 3.98–18.07 | "Meeru Snowflake lo oka SQL query execute chesaru." (4.20–7.55) · "Malli same query execute chesthe, first time laga complete ga data process chesthundha?" (7.93–13.09) · "Leda already available information ni use chesi fast ga result isthundha?" (13.52–17.67) · *[scripted pause 17.67–18.46]* | Curious | Same query again: full work or reuse? |
| 3 | 18.07–24.98 | "Exactly! Snowflake lo caching concept undhi." (18.46–21.59) · "Kaani manaki three important types of caching untayi!" (21.96–24.79) | Excited | Caching, three types |
| 4 | 24.98–28.32 | "Let's understand!" (25.16–26.00) · "Welcome to NDR EdTech!" (26.37–28.10) | Welcoming | Title and brand welcome |
| 5 | 28.32–40.59 | "First, Result Cache!" (28.53–30.09) · "Previously executed query result ni Snowflake cache chesthundhi." (30.47–33.91) · "Same query malli execute chesinappudu, eligible conditions satisfy ayithe cached result ni return chesthundhi." (34.29–40.39) | Clear | Result Cache |
| 6 | 40.59–55.59 | "Second, Warehouse Cache!" (40.79–42.50) · "Virtual Warehouse process chesina data ni local cache lo maintain chesthundhi." (42.83–47.01) · "Same data malli query chesinappudu, warehouse cache help avvachu." (47.35–51.02) · "Important point: Warehouse suspend ayithe local cache clear avuthundhi." (51.34–55.36) | Clear, then emphasis | Warehouse Cache, suspend clears it |
| 7 | 55.59–64.57 | "Third, Metadata Cache!" (55.81–57.37) · "Snowflake metadata information ni use chesi konni queries ni actual table data scan cheyyakunda answer cheyyagaladhu." (57.70–64.36) | Clear | Metadata Cache |
| 8 | 64.57–90.73 | "Oka Banking project example teesukundham." (64.78–66.78) · "Mana TRANSACTIONS table lo daily reports generate chesthunnam." (67.06–70.22) · "First time monthly transaction query execute chesthe, Snowflake data process chesthundhi." (70.57–75.32) · "Malli same query eligible conditions tho execute chesthe Result Cache use avvachu." (75.59–80.19) · "Different query same data access chesthe Warehouse Cache help avvachu." (80.49–84.43) · "COUNT or metadata-based queries konni Metadata Cache information use chesi fast ga execute avvachu." (84.74–90.55) | Storytelling | Banking: three queries, three caches |
| 9 | 90.73–103.86 | "So, simple ga gurthupettukondi!" (90.91–92.81) · "Result Cache – Previous query results." (93.12–95.29) · "Warehouse Cache – Locally cached data used by a running warehouse." (95.60–99.42) · "Metadata Cache – Table metadata used to answer eligible queries." (99.71–103.70) | Confident | Three-card recap |
| 10 | 103.86–112.06 | "Idi mana Thirty Days of Snowflake series lo Day Eighteen!" (104.02–107.17) · "Next video lo Materialized Views gurinchi real-time examples tho explain chesthanu." (107.47–111.92) | Upbeat | Day 18 card, Materialized Views teaser |
| 11 | 112.06–123.72 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (112.20–117.96) · "Full course details kosam NDR EdTech ni Contact avvandi!" (118.25–121.49) · "Let's Learn and Grow Together!" (121.75–123.43) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.77–1.11, 2.10–2.46, 3.75–4.20, 7.55–7.93, 13.09–13.52, 16.24–16.47, 17.67–18.46 (the scripted `[pause]`), 19.32–19.59, 21.59–21.96, 24.79–25.16, 26.00–26.37, 28.10–28.53, 28.98–29.24, 30.09–30.47, 33.91–34.29, 36.43–36.68, 38.53–38.74, 40.39–40.79, 41.18–41.55, 42.50–42.83, 47.01–47.35, 49.39–49.59, 51.02–51.34, 52.21–52.48, 55.36–55.81, 56.11–56.35, 57.37–57.70, 64.36–64.78, 66.78–67.06, 70.22–70.57, 73.32–73.53, 75.32–75.59, 80.19–80.49, 84.43–84.74, 89.08–89.28, 90.55–90.91, 91.28–91.54, 92.81–93.12, 93.86–94.10, 95.29–95.60, 96.45–96.67, 99.42–99.71, 100.66–100.89, 103.70–104.02, 107.17–107.47, 111.92–112.20, 117.96–118.25, 121.49–121.75, 123.43–123.72.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Malli same query execute chesthe, first time laga complete ga data process chesthundha? | same query ≈8.4 · first time ≈10.3 · complete ga data process ≈11.2 |
| Leda already available information ni use chesi fast ga result isthundha? | already available information ≈14.0–15.2 · fast ga result ≈16.5 |
| Exactly! Snowflake lo caching concept undhi. | Exactly 18.46 · caching ≈20.0 |
| Kaani manaki three important types of caching untayi! | three ≈22.6 · types of caching ≈23.4 |
| First, Result Cache! | First 28.53 · Result Cache 29.24 |
| Previously executed query result ni Snowflake cache chesthundhi. | Previously 30.47 · query result ≈31.6 · cache ≈33.0 |
| Same query malli execute chesinappudu, eligible conditions satisfy ayithe cached result ni return chesthundhi. | Same query 34.29 · eligible conditions ≈36.9 · cached result ni return ≈38.9 |
| Second, Warehouse Cache! | Second 40.79 · Warehouse Cache 41.55 |
| Virtual Warehouse process chesina data ni local cache lo maintain chesthundhi. | Virtual Warehouse 42.83 · local cache ≈45.0 |
| Same data malli query chesinappudu, warehouse cache help avvachu. | Same data 47.35 · warehouse cache help ≈49.6 |
| Important point: Warehouse suspend ayithe local cache clear avuthundhi. | Important point 51.34 · Warehouse suspend ≈52.6 · local cache clear ≈54.0 |
| Third, Metadata Cache! | Third 55.81 · Metadata Cache 56.35 |
| Snowflake metadata information ni use chesi konni queries ni actual table data scan cheyyakunda answer cheyyagaladhu. | metadata information ≈58.2 · konni queries ≈60.0 · actual table data scan cheyyakunda ≈61.2 · answer ≈63.4 |
| Mana TRANSACTIONS table lo daily reports generate chesthunnam. | TRANSACTIONS ≈67.5 · daily reports ≈68.8 |
| First time monthly transaction query execute chesthe, Snowflake data process chesthundhi. | monthly transaction query ≈71.0 · Snowflake data process ≈73.8 |
| Malli same query eligible conditions tho execute chesthe Result Cache use avvachu. | same query ≈76.0 · eligible conditions ≈77.0 · Result Cache ≈78.8 |
| Different query same data access chesthe Warehouse Cache help avvachu. | Different query ≈80.8 · same data access ≈82.0 · Warehouse Cache ≈83.4 |
| COUNT or metadata-based queries konni Metadata Cache information use chesi fast ga execute avvachu. | **COUNT** ≈85.0 · metadata-based ≈86.0 · Metadata Cache ≈87.4 · fast ga ≈89.5 |
| So, simple ga gurthupettukondi! | So 90.91 · gurthupettukondi ≈92.0 |
| Result Cache – Previous query results. | Result Cache 93.12 · Previous query results 94.10 |
| Warehouse Cache – Locally cached data used by a running warehouse. | Warehouse Cache 95.60 · Locally cached data 96.67 · running warehouse ≈98.4 |
| Metadata Cache – Table metadata used to answer eligible queries. | Metadata Cache 99.71 · Table metadata 100.89 · eligible queries ≈102.6 |
| Idi mana Thirty Days of Snowflake series lo Day Eighteen! | Thirty ≈105.0 · Days ≈105.4 · Snowflake ≈105.8 · Eighteen ≈106.8 |
| Next video lo Materialized Views gurinchi real-time examples tho explain chesthanu. | Materialized Views ≈108.8–109.8 · real-time examples ≈110.2 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈115.0 · NDR EdTech ≈115.8–117.0 · **Follow** ≈117.2 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 118.25–119.6 · NDR EdTech ≈119.8 · **Contact** ≈120.6 (estimated) |
| Let's Learn and Grow Together! | Let's 121.75 · Together ≈123.0 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, Cloud Glass #E6F0FF, text #F7F9F2.*

**Object look (keep identical in every scene):** a **SQL query** = a Cloud Glass card with abstract lines. A **table** = a Cloud Glass block with rows of small cells, on a dim storage shelf. **Result Cache** = an Aqua result-card. **Warehouse Cache** = an Orange drawer on a warehouse block. **Metadata Cache** = a Lilac index-strip.

### Scene 1 – Hook (0.00–3.98 s · 3.98 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka interesting question!"
**Tone:** curious.
**Visual objective:** Welcome viewers and tease the question.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, Cloud Glass #E6F0FF, text #F7F9F2. An olive-black space with soft light and drifting glass particles. Three small glass cards, one Aqua, one Orange and one Lilac, orbit a glowing glass question-mark at the upper-centre and settle with a soft bloom. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–2.10 s: particles drift in and the cards start to orbit on "Hello guys! Andaru ela unnaru?".
- 2.46–3.75 s: the question-mark completes with a bloom pulse on "Oka interesting question!".
- 3.75–3.98 s: soft light sweep into Scene 2.
- Effect: **Orbit ring** — the three cards circle the question-mark.
**Audio sync:** title lands at ≈1.1 s; the sweep completes in the pause at 3.75–4.20 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 18".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – Same query again: full work, or reuse? (3.98–18.07 s · 14.09 s)
**Voice-over:** "Meeru Snowflake lo oka SQL query execute chesaru. Malli same query execute chesthe, first time laga complete ga data process chesthundha? Leda already available information ni use chesi fast ga result isthundha?"
**Tone:** curious. The last 0.4 s is the start of the scripted pause.
**Visual objective:** Pose the question: when the same query runs again, does Snowflake do all the work again or reuse information it already has?
Generate as **three shots (2a–2c)**.

**Shot 2a (3.98–7.74 s) – a query is executed:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #12150D, Cloud Glass #E6F0FF, Result Cache Aqua #4DE3C2, text #F7F9F2. A Cloud Glass SQL query card (abstract lines) slides into a glass warehouse panel (a snowflake-crystal glyph, no logo) and a cursor presses a glowing run button. A glass table block on a dim storage shelf lights up and a result card (abstract bars) comes out. Calm, clean, phone-readable. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.20–5.2 s the card slides in on "Meeru Snowflake lo"; ≈5.2–6.5 s the cursor presses run on "oka SQL query"; ≈6.5–7.55 s the result comes out on "execute chesaru". **Effect: Live cursor.**
Overlay (post): "SQL QUERY EXECUTED" from ≈5.2 s.

**Shot 2b (7.74–13.31 s) – the same query again, from the start?:**
"Same style and palette. An identical copy of the query card slides in again. The table block lights up fully, cell by cell, as if all the work is being done again from the beginning, and a progress ring turns. A soft question-mark glow pulses. No readable text, no logos, no watermark."
Motion: 7.93–8.8 s the second card slides in on "Malli same query execute chesthe" (same query ≈8.4 s); ≈10.3 s the table lights cell by cell on "first time laga"; ≈11.2–13.09 s the ring turns on "complete ga data process chesthundha?".
Overlay (post): "SAME QUERY AGAIN" from ≈8.4 s; "FULL PROCESSING AGAIN?" from ≈10.3 s.

**Shot 2c (13.31–18.07 s) – or reuse what is already available?:**
"Same style and palette. The scene resets. This time the query card goes to a small shelf holding a glowing result card and a few glowing glass pieces (already available information) and a result comes out quickly, with the table dark and calm. A soft question-mark glow pulses. Hold a calm still frame for the last 0.4 s. No readable text, no logos, no watermark."
Motion: 13.52–15.2 s the shelf lights on "Leda already available information ni use chesi"; ≈16.5–17.67 s the result comes out on "fast ga result isthundha?"; 17.67–18.07 s calm hold during the scripted pause.
Overlay (post): "OR USE ALREADY AVAILABLE INFORMATION?" from 13.52 s.

**Audio sync:** second card at ≈8.4 s; table lights at ≈10.3 s; shelf at 13.52 s; quick result at ≈16.5 s.
**Negative prompt (all shots):** "Readable text, real timings, human faces, the answer shown too early, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Caching: three types (18.07–24.98 s · 6.91 s)
**Voice-over:** "Exactly! Snowflake lo caching concept undhi. Kaani manaki three important types of caching untayi!"
**Tone:** excited.
**Visual objective:** The answer is caching, and there are three important types.
Generate as **two shots (3a, 3b)**.

**Shot 3a (18.07–21.78 s) – the caching concept:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #12150D, Cloud Glass #E6F0FF, Result Cache Aqua #4DE3C2, text #F7F9F2. A glass snowflake-crystal emblem rises at the upper-centre with a soft bloom, and a small glowing glass shelf with a stored card appears below it. Calm, satisfying. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 18.46–19.32 s a bright flash on "Exactly!" (**Effect: Impact frame** — one-frame flash at 18.46 s); 19.59–21.59 s the emblem rises and the shelf appears on "Snowflake lo caching concept undhi" (caching ≈20.0 s).
Overlay (post): "CACHING" at ≈20.0 s.

**Shot 3b (21.78–24.98 s) – three types:**
"Same style and palette, plus Warehouse Cache Orange #FF9F43 and Metadata Cache Lilac #B79CFF. Three glass cards rise one by one in a neat vertical stack: Aqua, Orange, Lilac, each with a small abstract icon. Clean, uncluttered, phone-readable layout. No readable fine text, no logos, no watermark."
Motion: 21.96–22.6 s the first card rises on "Kaani manaki"; ≈22.6–23.4 s the second and third cards rise on "three important types of caching" (three ≈22.6 s); 23.4–24.79 s the stack settles on "untayi!". **Effect: Head stack.**
Overlay (post): "3 TYPES OF CACHING" from ≈22.6 s.

**Audio sync:** flash at 18.46 s; the three cards at ≈22.6 s.
**Negative prompt:** "Cache names shown early, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Title and welcome (24.98–28.32 s · 3.34 s)
**Voice-over:** "Let's understand! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Name the topic and welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, text #F7F9F2. The three cards (Aqua, Orange, Lilac) rest in a row at the lower-centre under a glowing glass snowflake-crystal emblem. A reserved clean area at the top for the logo, and clean space for a title. Slow push-in, soft volumetric light. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 25.16–26.00 s: the title lands on "Let's understand!". **Effect: Letter dive** — the letters settle fully before 25.9 s.
- 26.37–28.10 s: a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** title at 25.16 s; logo and panel at 26.37 s; "NDR" at ≈27.0 s.
**On-screen text (overlay, post):** "RESULT · WAREHOUSE · METADATA CACHE" at 25.16 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 26.37 s.
**Negative prompt:** "Fake logos, distorted logo, misspelled title, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – 1 · Result Cache (28.32–40.59 s · 12.27 s)
**Voice-over:** "First, Result Cache! Previously executed query result ni Snowflake cache chesthundhi. Same query malli execute chesinappudu, eligible conditions satisfy ayithe cached result ni return chesthundhi."
**Tone:** clear.
**Visual objective:** Snowflake saves the result of a previously executed query; when the same query is run again and the eligible conditions are met, it returns the saved result.
Generate as **two shots (5a, 5b)**.

**Shot 5a (28.32–34.10 s) – the result is cached:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Cloud Glass #E6F0FF, text #F7F9F2. A Cloud Glass query card runs against a table and a glowing Aqua result-card comes out, then slides onto a small glass shelf and locks in with a soft Aqua glow. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 28.53–30.09 s the badge and title appear on "First, Result Cache!" (**Effect: Press font** — "RESULT CACHE" presses in at 29.24 s); 30.47–32.0 s the query runs on "Previously executed query result"; ≈32.0–33.91 s the Aqua card locks onto the shelf on "Snowflake cache chesthundhi".
Overlay (post): "1 · RESULT CACHE" at 28.53 s; "PREVIOUSLY EXECUTED QUERY RESULT IS CACHED" from 30.47 s.

**Shot 5b (34.10–40.59 s) – the same query returns the cached result:**
"Same style and palette. An identical Cloud Glass query card arrives. A small checklist-glow (three soft Aqua ticks, no text) lights up one by one, and the Aqua result-card slides straight off the shelf and is returned, while the table stays dark and untouched. Satisfying. No readable text, no logos, no watermark."
Motion: 34.29–36.43 s the second card arrives on "Same query malli execute chesinappudu"; 36.68–38.53 s the three ticks light on "eligible conditions satisfy ayithe" (eligible conditions ≈36.9 s); 38.74–40.39 s the Aqua card is returned on "cached result ni return chesthundhi".
Overlay (post): "SAME QUERY AGAIN" at 34.29 s; "ELIGIBLE CONDITIONS SATISFIED" from ≈36.9 s; "CACHED RESULT RETURNED" from ≈38.9 s. Show "eligible conditions", never "always".

**Audio sync:** badge at 28.53 s; Aqua card locks at ≈32.0 s; ticks at ≈36.9 s; return at ≈38.9 s.
**Negative prompt (all shots):** "Readable text, claims that the result cache is always used, timings, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – 2 · Warehouse Cache (40.59–55.59 s · 15.00 s)
**Voice-over:** "Second, Warehouse Cache! Virtual Warehouse process chesina data ni local cache lo maintain chesthundhi. Same data malli query chesinappudu, warehouse cache help avvachu. Important point: Warehouse suspend ayithe local cache clear avuthundhi."
**Tone:** clear, then emphasis.
**Visual objective:** The warehouse keeps the data it processed in a local cache; this can help when the same data is queried again; if the warehouse is suspended, the local cache is cleared.
Generate as **three shots (6a–6c)**.

**Shot 6a (40.59–47.18 s) – the warehouse keeps processed data locally:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #12150D, Warehouse Cache Orange #FF9F43, Cloud Glass #E6F0FF, text #F7F9F2. A glass virtual-warehouse block (a rounded box with a small glowing power ring) sits above a dim storage shelf with a table. A query pulls some table data into the warehouse, and a small Orange drawer on the side of the warehouse fills with glowing data pieces and glows (the local cache). A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 40.79–42.50 s the badge and title appear on "Second, Warehouse Cache!" (**Effect: Press font** — "WAREHOUSE CACHE" presses in at 41.55 s); 42.83–44.5 s the warehouse pulls data on "Virtual Warehouse process chesina data ni"; ≈45.0–47.01 s the Orange drawer fills and glows on "local cache lo maintain chesthundhi".
Overlay (post): "2 · WAREHOUSE CACHE" at 40.79 s; "DATA PROCESSED BY THE VIRTUAL WAREHOUSE" from 42.83 s; "LOCAL CACHE" at ≈45.0 s.

**Shot 6b (47.18–51.18 s) – the same data again: the warehouse cache can help:**
"Same style and palette. A second query card arrives asking for the same data. The warehouse takes it straight from its Orange drawer, while the storage shelf stays dim. A soft Orange pulse on the drawer shows that it helps. No readable text, no logos, no watermark."
Motion: 47.35–49.39 s the second query arrives on "Same data malli query chesinappudu"; 49.59–51.02 s the Orange drawer pulses on "warehouse cache help avvachu" (warehouse cache help ≈49.6 s). **Effect: Rack focus** — focus pulls from the storage shelf to the Orange drawer at ≈49.6 s.
Overlay (post): "SAME DATA AGAIN" from 47.35 s; "WAREHOUSE CACHE CAN HELP" from ≈49.6 s.

**Shot 6c (51.18–55.59 s) – important: suspend clears the local cache:**
"Same style and palette. A small glowing 'important' marker appears above the warehouse. The warehouse's power ring switches off (the warehouse is suspended), and the Orange drawer's data pieces drift away as soft dust and the drawer goes dark. The table data on the storage shelf below stays fully intact and lit. Serious, clear. No readable text, no logos, no watermark."
Motion: 51.34–52.21 s the marker pulses on "Important point"; 52.48–53.6 s the power ring switches off on "Warehouse suspend ayithe" (suspend ≈52.6 s); ≈54.0–55.36 s the drawer empties on "local cache clear avuthundhi". **Effect: Blow away** — accurate here, because the local cache really is cleared; the table data on the shelf is not.
Overlay (post): "IMPORTANT POINT" at 51.34 s; "WAREHOUSE SUSPENDED → LOCAL CACHE CLEARED" from ≈52.6 s.

**Audio sync:** badge at 40.79 s; drawer fills at ≈45.0 s; pulse at ≈49.6 s; power-off at ≈52.6 s; drawer empties at ≈54.0 s.
**Negative prompt (all shots):** "Table data on the storage shelf disappearing, readable text, timings, sizes, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – 3 · Metadata Cache (55.59–64.57 s · 8.98 s)
**Voice-over:** "Third, Metadata Cache! Snowflake metadata information ni use chesi konni queries ni actual table data scan cheyyakunda answer cheyyagaladhu."
**Tone:** clear.
**Visual objective:** Snowflake can use metadata information to answer some queries without scanning the actual table data.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #12150D, Metadata Cache Lilac #B79CFF, Cloud Glass #E6F0FF, text #F7F9F2. A Cloud Glass table block with rows of cells on a dim shelf stays dark and calm. Beside it a thin glowing Lilac index-strip (a small stack of metadata chips, no readable text) glows. A Cloud Glass query card arrives, touches only the Lilac strip, and a result card comes out, while the table stays dark. A numbered badge '3'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 55.81–57.37 s: the badge and title appear on "Third, Metadata Cache!". **Effect: Press font** — "METADATA CACHE" presses in at 56.35 s.
- 57.70–60.0 s: the Lilac strip glows on "Snowflake metadata information ni use chesi" (metadata information ≈58.2 s).
- ≈60.0–61.2 s: the query card arrives on "konni queries ni".
- ≈61.2–64.36 s: the card touches only the strip and the result comes out while the table stays dark on "actual table data scan cheyyakunda answer cheyyagaladhu" (answer ≈63.4 s).
**Audio sync:** badge at 55.81 s; strip glows at ≈58.2 s; the table stays dark at ≈61.2 s; result at ≈63.4 s.
**On-screen text (overlay, post):** "3 · METADATA CACHE" at 55.81 s; "USES METADATA INFORMATION" from ≈58.2 s; "SOME QUERIES ANSWERED WITHOUT SCANNING TABLE DATA" from ≈61.2 s. Show "some queries", never "all".
**Negative prompt:** "The table lighting up, claims that all queries use the metadata cache, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – Banking project example (64.57–90.73 s · 26.16 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS table lo daily reports generate chesthunnam. First time monthly transaction query execute chesthe, Snowflake data process chesthundhi. Malli same query eligible conditions tho execute chesthe Result Cache use avvachu. Different query same data access chesthe Warehouse Cache help avvachu. COUNT or metadata-based queries konni Metadata Cache information use chesi fast ga execute avvachu."
**Tone:** storytelling.
**Visual objective:** In one banking example, three different queries benefit from three different caches.
Generate as **six shots (8a–8f)**. All shots use the same camera language and the same layout (warehouse on the left, table on a storage shelf in the centre, cards on the right).

**Shot 8a (64.57–66.92 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, Cloud Glass #E6F0FF, text #F7F9F2. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in warm light, with an empty glass layout below it (a warehouse block on the left, a storage shelf in the centre). Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈65.0 s.

**Shot 8b (66.92–70.40 s) – TRANSACTIONS, daily reports:**
"Same style and palette. A large Cloud Glass TRANSACTIONS table block, dense with rows of cells, settles on the storage shelf. A glass report-page glyph (abstract bars, no readable text) appears beside it. No readable fine text, no logos."
Overlay (post): "TRANSACTIONS" at ≈67.5 s (monospace); "DAILY REPORTS" at ≈68.8 s.

**Shot 8c (70.40–75.46 s) – first time: the data is processed:**
"Same style and palette. A monthly-report query card arrives. The warehouse pulls rows from the table, the table lights up cell by cell, and a result comes out. A slow progress ring turns. Nothing is cached yet: the Aqua shelf and the Orange drawer are empty and dim. No readable text, no logos."
Motion: 70.57–71.6 s the card arrives on "First time monthly transaction query"; ≈71.6–73.32 s the table lights on "execute chesthe"; 73.53–75.32 s the result comes out on "Snowflake data process chesthundhi" (≈73.8 s).
Overlay (post): "FIRST TIME: DATA IS PROCESSED" from 70.57 s.

**Shot 8d (75.46–80.34 s) – the same query again: Result Cache:**
"Same style and palette. An identical query card arrives, three soft Aqua ticks light up (eligible conditions), and an Aqua result-card slides from the shelf straight to the output, while the table and the warehouse stay dark. No readable text, no logos."
Motion: 75.59–76.8 s the card arrives on "Malli same query"; ≈77.0 s the ticks light on "eligible conditions tho"; ≈78.8–80.19 s the Aqua card is returned on "Result Cache use avvachu". **Effect: Comment drop** — a small Aqua note drops in beside the card at ≈78.8 s.
Overlay (post): "SAME QUERY + ELIGIBLE CONDITIONS" from 75.59 s; "RESULT CACHE CAN BE USED" from ≈78.8 s.

**Shot 8e (80.34–84.59 s) – a different query, the same data: Warehouse Cache:**
"Same style and palette. A different query card (different abstract lines) arrives and asks for the same data. The warehouse takes it straight from its Orange drawer, which glows. The storage shelf stays dim. No readable text, no logos."
Motion: 80.49–82.0 s the different card arrives on "Different query same data access chesthe"; ≈82.0–83.4 s the drawer glows on "same data access"; ≈83.4–84.43 s the pulse settles on "Warehouse Cache help avvachu".
Overlay (post): "DIFFERENT QUERY, SAME DATA" from 80.49 s; "WAREHOUSE CACHE CAN HELP" from ≈83.4 s.

**Shot 8f (84.59–90.73 s) – COUNT or metadata-based queries: Metadata Cache:**
"Same style and palette. A query card with a small count glyph (a plus-and-hash mark, no readable text) arrives. It touches only the Lilac index-strip beside the table and a result comes out quickly, while the table and the warehouse stay dark. No readable text, no logos."
Motion: 84.74–86.0 s the card arrives on "COUNT or metadata-based queries" (COUNT ≈85.0 s); ≈86.0–87.4 s the Lilac strip lights on "konni"; ≈87.4–89.08 s the strip answers on "Metadata Cache information use chesi"; 89.28–90.55 s the result appears on "fast ga execute avvachu".
Overlay (post): "COUNT / METADATA-BASED QUERIES" from ≈85.0 s; "METADATA CACHE" at ≈87.4 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake numbers, claims that a cache is always used, timings or percentages, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 9 – Simple recap (90.73–103.86 s · 13.13 s)
**Voice-over:** "So, simple ga gurthupettukondi! Result Cache – Previous query results. Warehouse Cache – Locally cached data used by a running warehouse. Metadata Cache – Table metadata used to answer eligible queries."
**Tone:** confident.
**Visual objective:** Three-card recap.
Generate as **four shots (9a–9d)**.

**Shot 9a (90.73–92.97 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, text #F7F9F2. The three cards (Aqua, Orange, Lilac) glide into a neat row at the centre with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈91.5 s.

**Shot 9b (92.97–95.45 s) – Result Cache:**
"Same style and palette. The Aqua card fills the frame, with a result-card sliding off a shelf. Clean and calm. No readable text, no logos."
Overlay (post): "RESULT CACHE" at 93.12 s; "Previous query results" from 94.10 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 9c (95.45–99.57 s) – Warehouse Cache:**
"Same style and palette. The Orange card fills the frame, showing a warehouse block with a glowing drawer and a running power ring. Clean and calm. No readable text, no logos."
Overlay (post): "WAREHOUSE CACHE" at 95.60 s; "Locally cached data used by a running warehouse" from 96.67 s.

**Shot 9d (99.57–103.86 s) – Metadata Cache:**
"Same style and palette. The Lilac card fills the frame, showing an index-strip answering a query while the table stays dark. Clean and calm. No readable text, no logos."
Overlay (post): "METADATA CACHE" at 99.71 s; "Table metadata used to answer eligible queries" from 100.89 s.

**Audio sync:** card 1 at 93.12 s; card 2 at 95.60 s; card 3 at 99.71 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Series card and teaser (103.86–112.06 s · 8.20 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Eighteen! Next video lo Materialized Views gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 18 and tease the next topic.
Generate as **two shots (10a, 10b)**.

**Shot 10a (103.86–107.32 s) – Day 18 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, text #F7F9F2. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first eighteen lit in Aqua (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 18" from ≈105.0 s; the eighteenth node lights at ≈106.8 s on "Eighteen".

**Shot 10b (107.32–112.06 s) – teaser:**
"Same style and palette. A teaser panel slides in with a glass table block and, beside it, a second glowing glass block that mirrors a summary of the table (a smaller block with a few bright bars), linked by a thin line. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: MATERIALIZED VIEWS" from ≈108.8 s; "REAL-TIME EXAMPLES" from ≈110.2 s. The visual only suggests a stored summary of a table. Do not show how a materialized view works, refresh behaviour or any numbers.

**Audio sync:** card at ≈105.0 s; the eighteenth node at ≈106.8 s; teaser title at ≈108.8 s.
**Negative prompt:** "Technical claims about materialized views, numbers, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 11 – Follow, contact and end card (112.06–123.72 s · 11.66 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (11a–11c)**.

**Shot 11a (112.06–118.11 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, text #F7F9F2. A calm, clean background with a soft glow, the three small cards (Aqua, Orange, Lilac) drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈113.5 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈115.0 s, emphasised at ≈117.2 s on "Follow" (estimated).

**Shot 11b (118.11–121.62 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Aqua and Orange glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 118.25 s, emphasised at ≈120.6 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 11c (121.62–123.72 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 121.75 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 18. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #12150D, Result Cache Aqua #4DE3C2, Warehouse Cache Orange #FF9F43, Metadata Cache Lilac #B79CFF, Cloud Glass #E6F0FF, text #F7F9F2, secondary text #A5AD95. Colour code: Result Cache = an Aqua result-card on a shelf (the saved result of a query that ran before); Warehouse Cache = an Orange drawer attached to a glass virtual-warehouse block (data the warehouse already processed, kept locally, cleared when the warehouse is suspended while the table data in storage stays intact); Metadata Cache = a Lilac index-strip that answers some queries without lighting the table. SQL queries are Cloud Glass cards with abstract lines; tables are Cloud Glass blocks with rows of cells on a dim storage shelf. Always say 'can help' and 'eligible', never 'always'. Never show timings, sizes or percentages. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–17: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day18.mp3` (123.72 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text overlays in the editor (titles, badges, table names, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a soft card slide, a power-down tone for the suspend, a gentle tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at the three-cards reveal (≈22.6 s), at the title (25.16 s), at the three cache badges (28.53, 40.79, 55.81 s), at the suspend (≈52.6 s), at the three banking queries (≈71.6, ≈77.0, ≈82.0, ≈85.0 s), at the recap cards (93.12, 95.60, 99.71 s), at the final tagline (121.75 s), and at the Follow and Contact lines (≈117.2, ≈120.6 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Result Cache keeps the result of a previously executed query and returns it when the same query is run again and the eligible conditions are met; Warehouse Cache keeps data processed by a virtual warehouse in a local cache, can help when the same data is queried again, and is cleared when the warehouse is suspended; Metadata Cache uses metadata information so that some queries can be answered without scanning the actual table data. In the banking example, the first monthly query processes the data, the same query with eligible conditions can use Result Cache, a different query on the same data can be helped by Warehouse Cache, and COUNT or metadata-based queries can use Metadata Cache information. **No timings, sizes, eligibility rules or percentages** are shown, because the script gives none.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
