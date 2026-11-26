# Thirty Days of Snowflake – Day 14: Micro-partitions, Partition Pruning & Automatic Clustering
Video prompt package (NDR EdTech) — `Audio\day14.mp3` + `days-scripts\day14.txt`, analysed with Whisper

> **Timing status: MEASURED from day14.mp3 (152.84 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied word times inside phrases. Whisper word times can be 0.1–0.5 s early or late, especially in long Telugu phrases. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **Four lines were missed or garbled by Whisper:** "Prathi Micro-partition ki data gurinchi metadata maintain chesthundhi." (≈54.24–58.06 s), "Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu." (≈109.87–114.94 s), the end of the Automatic Clustering recap line (≈127.47–131.50 s), and "Next video lo Query Profile gurinchi real-time examples tho explain chesthanu." (≈135.56–139.81 s). Their start and end times come from the pauses and are reliable; the word times inside them are estimated (≈).
> 2. **Follow and Contact lines (about 143–150 s):** Whisper mixed up the word order of these two Telugu lines, so the "Follow" and "Contact" word times are estimated (≈). Adjust by 0.2–0.5 s if needed.
> 3. **36.30–37.61 s** is your scripted `[pause]`, a real 1.31 s silence. The visuals hold a calm beat there.
> 4. **The video opens with a 17-second support request** (follow, like, comment) before the topic. It is made as its own short scene with generic icons and no real social-media logos.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 14: Micro-partitions, Partition Pruning & Automatic Clustering |
| Duration | **152.84 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 4,585 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day14.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (38 shots in 13 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Honeycomb Prism" (new for Day 14)
| Role | HEX | Use |
|---|---|---|
| Background | `#17110C` | Base, gradients (warm dark brown) |
| Honey Amber | `#F5A524` | **Micro-partition** tiles, brand glow |
| Electric Blue | `#3AA0FF` | The query beam and the tiles it **scans** |
| Smoke Grey | `#6B6358` | Tiles that are **skipped** (pruned), dimmed items |
| Metadata Mint | `#5EE6B8` | The small **metadata** strip (min–max) on every tile |
| Cluster Orchid | `#C084FC` | **Automatic Clustering**, organised arrangement |
| Primary text | `#FFF8EE` | Titles, labels |
| Secondary text | `#B3A797` | Captions |

**Colour code (use in every scene):** Table data = Honey Amber glass · Micro-partition = a small rounded-hexagon glass tile with a thin Mint metadata strip · Scanned tile = lit Electric Blue · Skipped tile = dim Smoke Grey (never deleted, only not read) · Clustered / organised = Orchid glow.

**The core visual rule (technical accuracy):** a table's data is divided into many small tiles (micro-partitions). Each tile carries a small Mint metadata strip that shows a range (a minimum and a maximum, drawn as a bar without readable numbers). When a query has a WHERE condition, Snowflake **checks this metadata first**, then **scans only the tiles that can contain the required data (Electric Blue)** and **skips the others (Smoke Grey)**. Skipped tiles stay in the table; they are simply not read. The effect "Blow away" is **deliberately not used**, because it would suggest that skipped data is deleted. No tile sizes, no counts and no performance numbers are shown, because the script gives none.

### Motion effects used (from the skill's effects library)
Letter dive, Impact frame, Layer explode, Rack focus, Live cursor, Code body, Press font, Comment drop, Liquid glass, Head stack, Orbit ring. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.66 | "Hello guys! Andaru happy ga unnaru ani anukuntunnanu!" (0.00–3.43) | Friendly | Title hook |
| 2 | 3.66–20.96 | "Topic loki vellaboye mundu oka small request." (3.89–6.50) · "Ilanti manchi technical content meeku continue ga andinchalante mee support kuda chaala important." (6.93–12.69) · "Please follow cheyyandi, video nachithe like cheyyandi, mee feedback comments lo share cheyyandi." (13.13–18.65) · "Thank you so much for your support!" (19.05–20.74) | Warm, sincere | Follow, like, comment icons, thank you |
| 3 | 20.96–23.81 | "Coming to the topic!" (21.18–22.05) · "Oka interesting question!" (22.44–23.59) | Curious | Topic transition |
| 4 | 23.81–36.96 | "Mee daggara 10 crore customer records unnayi anukondi." (24.02–26.87) · "Ippudu meeru oka particular customer data kosam query run chesthe," (27.30–30.84) · "Snowflake anni records scan chesthundha?" (31.10–33.23) · "Leda required data matrame scan chesthundha?" (33.56–36.30) · *[scripted pause 36.30–37.61]* | Curious, building | 10 crore records, scan all or only required? |
| 5 | 36.96–44.00 | "Ee magic venakala unna important concepts" (37.61–40.09) · "Micro-partitions and Partition Pruning!" (40.39–42.61) · "Let's understand!" (43.01–43.80) | Excited, reveal | Magic reveal and title |
| 6 | 44.00–46.12 | "Welcome to NDR EdTech!" (44.21–45.86) | Welcoming | Brand welcome |
| 7 | 46.12–63.56 | "Snowflake lo tables data ni automatically small units ga divide chesi store chesthundhi." (46.39–51.54) · "Veetine Micro-partitions antaru." (51.92–53.83) · "Prathi Micro-partition ki data gurinchi metadata maintain chesthundhi." (54.24–58.06) · "For example, minimum value, maximum value and other metadata information untayi." (58.43–63.33) | Clear | Table divides into tiles, metadata on each |
| 8 | 63.56–74.11 | "Ippudu manam WHERE condition use chesi query run chesthe," (63.78–66.75) · "Snowflake metadata ni check chesi unnecessary Micro-partitions ni skip chesthundhi." (67.00–71.55) · "Dheenine Partition Pruning antaru." (71.96–73.88) | Clear | Query checks metadata, skips tiles |
| 9 | 74.11–83.45 | "Mari Automatic Clustering enti?" (74.34–76.29) · "Large tables lo data organization ni improve cheyyadaniki Snowflake Automatic Clustering service provide chesthundhi." (76.73–83.20) | Clear | Tiles get organised |
| 10 | 83.45–115.17 | "Oka Banking project example teesukundham." (83.69–85.66) · "Mana TRANSACTIONS table lo millions of records unnayi." (86.11–88.88) · "Manam oka particular date transactions kosam query run chesthunnam." (89.28–92.63) · "SQL query chuddam!" (93.06–94.22) · "SELECT * FROM TRANSACTIONS" (94.67–96.63) · "WHERE TRANSACTION_DATE = '2026-11-18';" (96.86–100.98) · "Snowflake metadata ni check chesi, required date data unna Micro-partitions ni scan chesthundhi." (101.40–106.58) · "Unnecessary Micro-partitions ni skip chesthundhi." (107.00–109.45) · "Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu." (109.87–114.94) | Storytelling | Banking: date query scans some tiles, skips the rest |
| 11 | 115.17–131.74 | "So, simple ga gurthupettukondi!" (115.38–117.21) · "Micro-partitions – Automatically organized data storage units." (117.64–121.55) · "Partition Pruning – Unnecessary Micro-partitions ni skip cheyyadam." (121.96–125.57) · "Automatic Clustering – Data organization ni maintain cheyyadaniki Snowflake provide chese service." (126.01–131.50) | Confident | Three-card recap |
| 12 | 131.74–139.94 | "Idi mana Thirty Days of Snowflake series lo Day Fourteen!" (131.97–135.12) · "Next video lo Query Profile gurinchi real-time examples tho explain chesthanu." (135.56–139.81) | Upbeat | Day 14 card, Query Profile teaser |
| 13 | 139.94–152.84 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (140.06–146.62) · "Full course details kosam NDR EdTech ni Contact avvandi!" (146.94–150.45) · "Let's Learn and Grow Together!" (150.81–152.46) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.78–1.11, 3.43–3.89, 6.50–6.93, 12.69–13.13, 18.65–19.05, 20.74–21.18, 22.05–22.44, 23.59–24.02, 26.87–27.30, 30.84–31.10, 33.23–33.56, 36.30–37.61 (the scripted `[pause]`), 40.09–40.39, 42.61–43.01, 43.80–44.21, 45.86–46.39, 51.54–51.92, 53.83–54.24, 58.06–58.43, 59.08–59.35, 63.33–63.78, 66.75–67.00, 71.55–71.96, 73.88–74.34, 76.29–76.73, 83.20–83.69, 85.66–86.11, 88.88–89.28, 92.63–93.06, 94.22–94.67, 96.63–96.86, 100.98–101.40, 106.58–107.00, 109.45–109.87, 112.87–113.07, 114.94–115.38, 115.74–115.95, 117.21–117.64, 118.66–118.97, 121.55–121.96, 122.88–123.19, 125.57–126.01, 127.09–127.47, 131.50–131.97, 135.12–135.56, 139.81–140.06, 146.62–146.94, 148.31–148.54, 150.45–150.81.

### Appendix A – Key trigger times
Words use your script's spelling. Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Hello guys! Andaru happy ga unnaru ani anukuntunnanu! | Hello 0.0 · guys 0.28 · Andaru happy ga unnaru ≈1.2–2.3 · anukuntunnanu ≈2.6 |
| Topic loki vellaboye mundu oka small request. | Topic ≈3.9 · small request ≈5.5–6.3 |
| Ilanti manchi technical content meeku continue ga andinchalante mee support kuda chaala important. | technical content ≈7.1 · support ≈10.9 · important ≈12.0 |
| Please follow cheyyandi, | Please 13.16 · follow ≈13.8 |
| video nachithe like cheyyandi, | video ≈14.9 · like ≈15.7 |
| mee feedback comments lo share cheyyandi. | feedback ≈16.9 · comments ≈17.4 · share ≈18.0 |
| Thank you so much for your support! | Thank 19.05 · you 19.3 · support ≈20.3 |
| Coming to the topic! | Coming 21.18 · topic 21.64 |
| Oka interesting question! | interesting 22.56 · question 23.02 |
| Mee daggara 10 crore customer records unnayi anukondi. | 10 crore ≈24.7–25.0 · customer records ≈25.4–25.7 |
| Ippudu meeru oka particular customer data kosam query run chesthe, | particular customer data ≈28.1–29.0 · query ≈29.5 |
| Snowflake anni records scan chesthundha? | Snowflake 31.22 · records ≈31.9 · scan ≈32.4 |
| Leda required data matrame scan chesthundha? | required data ≈34.2 · matrame ≈35.0 · scan ≈35.6 |
| Ee magic venakala unna important concepts | magic 37.76 · venakala ≈38.4 |
| Micro-partitions and Partition Pruning! | Micro-partitions 40.39–41.0 · Partition Pruning 41.7–42.22 |
| Let's understand! | Let's 43.01 · understand 43.28 |
| Welcome to NDR EdTech! | Welcome 44.21 · NDR 44.8 · EdTech 45.26 |
| Snowflake lo tables data ni automatically small units ga divide chesi store chesthundhi. | Snowflake 46.39 · tables data ≈47.4 · automatically ≈48.0 · small units ≈49.0 · divide ≈50.0 |
| Veetine Micro-partitions antaru. | Veetine 51.92 · Micro-partitions 52.4–52.78 |
| Prathi Micro-partition ki data gurinchi metadata maintain chesthundhi. | Prathi 54.24 · metadata ≈56.4 · maintain ≈57.2 |
| For example, minimum value, maximum value and other metadata information untayi. | For example 58.43 · minimum value 59.52–59.56 · maximum value 60.36–60.68 · other metadata information 61.26–62.26 |
| Ippudu manam WHERE condition use chesi query run chesthe, | WHERE ≈64.5 · condition ≈64.9 · query run ≈65.6 |
| Snowflake metadata ni check chesi unnecessary Micro-partitions ni skip chesthundhi. | Snowflake metadata 67.0–67.5 · check ≈68.3 · unnecessary Micro-partitions ≈69.0–70.0 · skip ≈70.8 |
| Dheenine Partition Pruning antaru. | Partition Pruning 71.96–72.98 |
| Mari Automatic Clustering enti? | Automatic Clustering 74.48–75.18 |
| Large tables lo data organization ni improve cheyyadaniki Snowflake Automatic Clustering service provide chesthundhi. | Large tables 76.73 · data organization ≈77.8–78.5 · improve ≈79.3 · Snowflake Automatic Clustering 80.08–81.24 · service provide ≈81.9–82.6 |
| Oka Banking project example teesukundham. | Banking 83.8 · project 84.2 · example 84.66 |
| Mana TRANSACTIONS table lo millions of records unnayi. | TRANSACTIONS ≈86.4 · millions ≈87.0 · records ≈88.2 |
| Manam oka particular date transactions kosam query run chesthunnam. | particular date ≈89.8–90.3 · query run ≈91.5 |
| SQL query chuddam! | SQL 93.06 · query 93.42 |
| SELECT * FROM TRANSACTIONS | SELECT 94.67 · * ≈95.0 · FROM ≈95.4 · TRANSACTIONS ≈95.8 |
| WHERE TRANSACTION_DATE = '2026-11-18'; | WHERE ≈96.9 · TRANSACTION_DATE ≈97.3–98.2 · = ≈98.3 · '2026-11-18' ≈98.6–100.9 |
| Snowflake metadata ni check chesi, required date data unna Micro-partitions ni scan chesthundhi. | Snowflake metadata 101.42–101.9 · check ≈102.7 · required date data ≈103.4–104.1 · scan ≈105.2 |
| Unnecessary Micro-partitions ni skip chesthundhi. | Unnecessary 107.08 · Micro-partitions 107.52–107.84 · skip ≈108.6 |
| Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu. | unnecessary data scanning ≈110.4–111.6 · reduce ≈112.4 · query performance ≈113.3 · improve ≈114.0 |
| So, simple ga gurthupettukondi! | So 115.38 · simple ga ≈116.0 · gurthupettukondi ≈116.5 |
| Micro-partitions – Automatically organized data storage units. | Micro-partitions 117.64–117.84 · Automatically organized 118.97–119.3 · data storage units 120.2–120.9 |
| Partition Pruning – Unnecessary Micro-partitions ni skip cheyyadam. | Partition Pruning 121.96–122.36 · Unnecessary Micro-partitions 123.2–123.6 · skip ≈124.5 |
| Automatic Clustering – Data organization ni maintain cheyyadaniki Snowflake provide chese service. | Automatic Clustering 126.01–126.48 · Data organization 127.47 · maintain ≈129.0 · service ≈130.8 |
| Idi mana Thirty Days of Snowflake series lo Day Fourteen! | Thirty 132.36 · Days 132.76 · Snowflake 133.18 · series 133.66 · Day 133.94 · Fourteen ≈134.5 |
| Next video lo Query Profile gurinchi real-time examples tho explain chesthanu. | Next 135.56 · Query Profile ≈136.4–137.2 · real-time examples ≈137.8–138.8 |
| Ilanti Data Engineering concepts Telugu lo nerchukovadaniki | Data Engineering 140.76 · concepts 141.26 · Telugu 142.1 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈143.7 · NDR EdTech ≈144.6–145.5 · **Follow** ≈145.7 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 146.94–148.31 · NDR EdTech ≈148.6–149.4 · **Contact** ≈149.5 (estimated) |
| Let's Learn and Grow Together! | Let's 150.81 · Learn 151.1 · and 151.42 · Grow 151.76 · Together 152.08 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Smoke Grey #6B6358, Metadata Mint #5EE6B8, Cluster Orchid #C084FC, text #FFF8EE.*

**Object look (keep identical in every scene):**
- **Table** = a large Honey Amber glass block with rows of small glowing cells.
- **Micro-partition** = a small rounded-hexagon Honey Amber glass tile with a thin Mint metadata strip (a range bar) along its bottom edge. No readable numbers.
- **Scanned tile** = lit Electric Blue. **Skipped tile** = dim Smoke Grey (still present, not deleted).
- **Query beam** = a thin Electric Blue light beam. **Clustered tiles** = tiles that slide into neat groups with a soft Orchid glow.

### Scene 1 – Hook (0.00–3.66 s · 3.66 s)
**Voice-over:** "Hello guys! Andaru happy ga unnaru ani anukuntunnanu!"
**Tone:** friendly.
**Visual objective:** Welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Smoke Grey #6B6358, Metadata Mint #5EE6B8, Cluster Orchid #C084FC, text #FFF8EE. A warm dark-brown space with soft honey light and drifting glass hexagon particles. A large glowing Honey Amber glass honeycomb of rounded-hexagon tiles assembles at the upper-centre and settles with a soft bloom, each tile with a tiny Mint edge. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."

**Motion instructions:**
- 0.00–0.78 s: particles drift in on "Hello guys!".
- 1.11–3.43 s: the honeycomb assembles tile by tile on "Andaru happy ga unnaru ani anukuntunnanu!".
- 3.43–3.66 s: soft light sweep into Scene 2.
- Effect: **Letter dive** — the title letters dive in at ≈1.2 s and settle before 2.3 s.

**Audio sync:** title lands at ≈1.2 s; the sweep completes in the pause at 3.43–3.89 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 14".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – A small request (3.66–20.96 s · 17.30 s)
**Voice-over:** "Topic loki vellaboye mundu oka small request. Ilanti manchi technical content meeku continue ga andinchalante mee support kuda chaala important. Please follow cheyyandi, video nachithe like cheyyandi, mee feedback comments lo share cheyyandi. Thank you so much for your support!"
**Tone:** warm, sincere.
**Visual objective:** Ask for support (follow, like, comment) and say thanks, in a friendly, uncluttered way.
Generate as **four shots (2a–2d)**. Use generic glass icons only: no Instagram, YouTube or other brand logos.

**Shot 2a (3.66–6.72 s) – a small request:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Metadata Mint #5EE6B8, text #FFF8EE. A single soft glass speech-bubble with a small heart-shaped glow slides gently into the centre of the frame over the honeycomb background, as a friendly request. Calm, warm light, slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 3.89–5.5 s the bubble slides in on "Topic loki vellaboye mundu"; ≈5.5–6.3 s the heart glows on "oka small request". **Effect: Comment drop.**
Overlay (post): "A SMALL REQUEST" from 3.89 s.

**Shot 2b (6.72–12.91 s) – your support matters:**
"Same style and palette. A row of glowing glass content-cards (abstract video thumbnails, no readable text) rises one after another along a gentle upward path, each lighting a little brighter than the last, with a steady warm Amber glow beneath them as if supported. Clean, calm, phone-readable layout. No readable text, no logos, no watermark."
Motion: 6.93–10.0 s the cards rise one by one on "Ilanti manchi technical content meeku continue ga andinchalante"; ≈10.9–12.69 s the warm glow builds under them on "mee support kuda chaala important".
Overlay (post): "YOUR SUPPORT MATTERS" from ≈10.9 s.

**Shot 2c (12.91–18.85 s) – follow, like, comment:**
"Same style and palette. Three large glass buttons appear one after another in a neat vertical stack: first a rounded button with a plus-and-person glyph (follow), then a button with a thumbs-up glyph (like), then a button with a chat-bubble glyph (comment). Each lights up with a soft Electric Blue pulse when it appears. Clean, uncluttered, generous spacing. No readable text, no brand logos, no watermark."
Motion: 13.16–14.8 s the follow button appears and pulses on "Please follow cheyyandi" (follow ≈13.8 s); ≈14.9–16.5 s the like button on "video nachithe like cheyyandi" (like ≈15.7 s); ≈16.9–18.65 s the comment button on "mee feedback comments lo share cheyyandi" (comments ≈17.4 s). **Effect: Head stack.**
Overlay (post): "FOLLOW" at ≈13.8 s; "LIKE" at ≈15.7 s; "COMMENT" at ≈17.4 s.

**Shot 2d (18.85–20.96 s) – thank you:**
"Same style and palette. The three buttons settle into a soft glowing cluster, and a gentle burst of warm Amber sparkles blooms behind them. Calm, grateful feeling. No readable text, no logos, no watermark."
Motion: 19.05–20.74 s the burst blooms on "Thank you so much for your support!".
Overlay (post): "THANK YOU!" from 19.05 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real social-media logos or app icons, readable text, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Coming to the topic (20.96–23.81 s · 2.85 s)
**Voice-over:** "Coming to the topic! Oka interesting question!"
**Tone:** curious.
**Visual objective:** Transition into the topic.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, text #FFF8EE. The glowing buttons from the last shot dissolve into Amber particles that gather into a large glowing question-mark made of small hexagon tiles at the upper-centre. Soft bloom, slow push-in, clean space for a title. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 21.18–22.05 s: the particles sweep in on "Coming to the topic!".
- 22.44–23.59 s: the question-mark forms on "Oka interesting question!" (interesting 22.56 s, question 23.02 s).
- Effect: **Impact frame** — a one-frame punch-in at 23.02 s on "question".
**Audio sync:** sweep at 21.18 s; question mark completes at 23.02 s.
**On-screen text (overlay, post):** "COMING TO THE TOPIC" from 21.18 s; "AN INTERESTING QUESTION" from 22.44 s.
**Negative prompt:** "Readable text, clutter, flicker, off-palette colours, human faces, watermark."

---

### Scene 4 – 10 crore records: scan all, or only what's needed? (23.81–36.96 s · 13.15 s)
**Voice-over:** "Mee daggara 10 crore customer records unnayi anukondi. Ippudu meeru oka particular customer data kosam query run chesthe, Snowflake anni records scan chesthundha? Leda required data matrame scan chesthundha?"
**Tone:** curious, building. The last 0.65 s is the start of the scripted pause.
**Visual objective:** Pose the question of how a query reads a very large table.
Generate as **four shots (4a–4d)**.

**Shot 4a (23.81–27.09 s) – 10 crore records:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, text #FFF8EE. A vast, dense wall of tiny glowing Honey Amber cells fills the frame and stretches far into the distance, to show a huge number of customer records. The camera pulls back slowly to reveal the scale. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 24.02–24.7 s the wall appears on "Mee daggara"; ≈24.7–26.0 s the camera pulls back on "10 crore customer records"; 26.0–26.87 s the wall fills the frame on "unnayi anukondi".
Overlay (post): "10 CRORE CUSTOMER RECORDS" from ≈24.7 s.

**Shot 4b (27.09–30.97 s) – a query for one customer:**
"Same style and palette, plus Electric Blue #3AA0FF. A glass query card with an abstract search glyph slides in from the lower edge and aims a thin Electric Blue beam at one single glowing cell in the huge wall. The cell pulses. No readable text, no logos, no watermark."
Motion: 27.30–28.1 s the query card slides in on "Ippudu meeru oka"; ≈28.1–29.0 s the beam targets one cell on "particular customer data"; ≈29.5–30.84 s the cell pulses on "query run chesthe". **Effect: Live cursor.**
Overlay (post): "QUERY FOR ONE CUSTOMER" from ≈28.1 s.

**Shot 4c (30.97–33.40 s) – scan all the records?:**
"Same style and palette. A wide Electric Blue scan line sweeps across the entire wall of cells, lighting every cell. The camera tilts to show how much is being lit. A soft white question-mark glow hovers above. No readable text, no logos, no watermark."
Motion: 31.10–31.9 s the scan line starts on "Snowflake anni records"; ≈31.9–33.23 s it sweeps the whole wall on "scan chesthundha?".
Overlay (post): "SCAN ALL THE RECORDS?" from 31.22 s.

**Shot 4d (33.40–36.96 s) – or only the required data?:**
"Same style and palette. The wall resets. This time a narrow Electric Blue beam lights only a small neat patch of cells and the rest stays dark and calm. A soft white question-mark glow pulses above. Hold a calm still frame for the last 0.65 s. No readable text, no logos, no watermark."
Motion: 33.56–34.2 s the wall resets on "Leda"; ≈34.2–35.6 s the narrow beam lights a small patch on "required data matrame scan chesthundha?"; 36.30–36.96 s calm hold during the scripted pause.
Overlay (post): "OR ONLY THE REQUIRED DATA?" from 33.56 s.

**Audio sync:** wall at 24.02 s; beam at ≈28.1 s; full sweep at 31.1 s; narrow beam at ≈34.2 s.
**Negative prompt (all shots):** "Readable numbers, real customer data, human faces, an answer shown too early, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – The magic behind it, and the title (36.96–44.00 s · 7.04 s)
**Voice-over:** "Ee magic venakala unna important concepts Micro-partitions and Partition Pruning! Let's understand!"
**Tone:** excited, reveal.
**Visual objective:** Reveal the two concepts and name the topic.
Generate as **two shots (5a, 5b)**.

**Shot 5a (36.96–40.24 s) – the magic:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Metadata Mint #5EE6B8, text #FFF8EE. The wall of cells from the last shot is covered by a soft shimmering Amber light curtain, like a magic reveal. The curtain parts in the middle to hint at hexagon tiles with Mint edges behind it. Slow push-in, mysterious but friendly. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 37.61–38.4 s the shimmer builds on "Ee magic venakala"; ≈38.4–40.09 s the curtain parts on "unna important concepts" (magic 37.76 s).
Overlay (post): none.

**Shot 5b (40.24–44.00 s) – title:**
"Same style and palette, plus Cluster Orchid #C084FC. A neat honeycomb of Honey Amber tiles fills the lower half. An Electric Blue beam passes over it, lights a few tiles, and leaves the rest dim grey. Big clean empty space above for a large title. Soft light burst. No rendered text, no logos, no watermark."
Motion: 40.39–41.0 s the honeycomb assembles on "Micro-partitions"; 41.7–42.22 s the beam passes on "Partition Pruning!"; 43.01–43.80 s a soft burst on "Let's understand!". **Effect: Letter dive** — the title letters settle fully before 42.6 s.
Overlay (post): "MICRO-PARTITIONS" at 40.39 s; "PARTITION PRUNING" at 41.7 s; "LET'S UNDERSTAND!" at 43.01 s.

**Audio sync:** curtain parts at ≈38.4 s; "MICRO-PARTITIONS" at 40.39 s; "PARTITION PRUNING" at 41.7 s.
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – Welcome (44.00–46.12 s · 2.12 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, text #FFF8EE. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft honey glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 44.21–45.86 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 44.21 s; "NDR" at 44.8 s; "EdTech" at 45.26 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – What are micro-partitions? (46.12–63.56 s · 17.44 s)
**Voice-over:** "Snowflake lo tables data ni automatically small units ga divide chesi store chesthundhi. Veetine Micro-partitions antaru. Prathi Micro-partition ki data gurinchi metadata maintain chesthundhi. For example, minimum value, maximum value and other metadata information untayi."
**Tone:** clear.
**Visual objective:** A table's data is automatically divided into small units (micro-partitions), and each one has metadata such as a minimum value, a maximum value and more.
Generate as **four shots (7a–7d)**. Keep the table position and the tile style identical in every shot.

**Shot 7a (46.12–51.73 s) – automatically divided into small units:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Metadata Mint #5EE6B8, text #FFF8EE. A large solid Honey Amber glass table block with rows of glowing cells floats at the centre. The block separates into a neat honeycomb of many small rounded-hexagon glass tiles that slide into a tidy grid, as if the data is divided automatically. Soft rim lighting, slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 46.39–47.4 s the table appears on "Snowflake lo tables data"; ≈48.0–49.5 s the block starts to split on "automatically small units"; ≈50.0–51.54 s the tiles settle into the grid on "divide chesi store chesthundhi". **Effect: Layer explode** (a clean separation into tiles).
Overlay (post): "AUTOMATICALLY DIVIDED INTO SMALL UNITS" from ≈48.0 s.

**Shot 7b (51.73–54.04 s) – Micro-partitions:**
"Same style and palette. The honeycomb of tiles stays in place while one tile at the centre lifts slightly and glows brighter, as if being named. The rest softly dim. No readable text, no logos, no watermark."
Motion: 51.92–52.4 s the tile lifts on "Veetine"; 52.4–52.78 s it glows on "Micro-partitions". **Effect: Press font** — "MICRO-PARTITIONS" presses into place at 52.4 s.
Overlay (post): "MICRO-PARTITIONS" at 52.4 s.

**Shot 7c (54.04–58.25 s) – metadata on every tile:**
"Same style and palette. A thin Metadata Mint strip (a small range bar with a left and a right end marker, no readable numbers) draws along the bottom edge of every tile in turn, rippling across the honeycomb. One tile lifts and shows its strip in close-up. No readable text, no logos, no watermark."
Motion: 54.24–56.4 s the strips ripple across the tiles on "Prathi Micro-partition ki data gurinchi"; ≈56.4–58.06 s one tile lifts and its strip glows on "metadata maintain chesthundhi" (metadata ≈56.4 s). **Effect: Rack focus** — focus pulls from the whole grid to the one tile at ≈56.4 s.
Overlay (post): "METADATA FOR EVERY MICRO-PARTITION" from ≈56.4 s.

**Shot 7d (58.25–63.56 s) – min, max and other metadata:**
"Same style and palette. In close-up on the lifted tile, the Mint strip shows a left marker and a right marker with a bar between them (minimum and maximum, no readable numbers), and then a few more small Mint chips slide in beside it to suggest other metadata information. Calm, clear. No readable text, no logos, no watermark."
Motion: 58.43–59.08 s the tile steadies on "For example,"; 59.52–60.0 s the left marker lights on "minimum value"; 60.36–61.0 s the right marker lights on "maximum value"; 61.26–62.3 s the extra chips slide in on "other metadata information". **Effect: Comment drop** — a small Mint note drops in beside the tile at ≈61.3 s.
Overlay (post): "MINIMUM VALUE" at 59.52 s; "MAXIMUM VALUE" at 60.36 s; "OTHER METADATA" at 61.26 s.

**Audio sync:** split at ≈48.0 s; "MICRO-PARTITIONS" at 52.4 s; strips at 54.24 s; min at 59.52 s; max at 60.36 s.
**Negative prompt (all shots):** "Readable numbers or dates on tiles, specific tile sizes, specific tile counts, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – Partition Pruning (63.56–74.11 s · 10.55 s)
**Voice-over:** "Ippudu manam WHERE condition use chesi query run chesthe, Snowflake metadata ni check chesi unnecessary Micro-partitions ni skip chesthundhi. Dheenine Partition Pruning antaru."
**Tone:** clear.
**Visual objective:** A query with a WHERE condition makes Snowflake check the metadata and skip unnecessary micro-partitions: this is Partition Pruning.
Generate as **three shots (8a–8c)**.

**Shot 8a (63.56–66.88 s) – a query with a WHERE condition:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Metadata Mint #5EE6B8, text #FFF8EE. The honeycomb of Honey Amber tiles with Mint strips sits in the lower two thirds. A glass query card with a small funnel glyph (a filter) slides in from the top and an Electric Blue beam points down at the honeycomb. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 63.78–64.5 s the card slides in on "Ippudu manam"; ≈64.5–64.9 s the funnel glyph lights on "WHERE condition" (WHERE ≈64.5 s); ≈65.6–66.75 s the beam aims at the honeycomb on "query run chesthe". **Effect: Live cursor.**
Overlay (post): "WHERE CONDITION" from ≈64.5 s.

**Shot 8b (66.88–71.76 s) – check metadata, skip the rest:**
"Same style and palette, plus Smoke Grey #6B6358. The Electric Blue beam first sweeps over the Mint metadata strips only (not the tile bodies), and the strips pulse as they are checked. Then most of the tiles dim to Smoke Grey and slide very slightly back, skipped, while a few tiles light Electric Blue. The skipped tiles stay in the table; none are removed. No readable text, no logos, no watermark."
Motion: 67.0–68.3 s the beam checks the strips on "Snowflake metadata ni check chesi" (metadata 67.0–67.5 s); ≈69.0–70.0 s most tiles dim on "unnecessary Micro-partitions"; ≈70.8–71.55 s a few tiles light Electric Blue and the rest stay dim on "skip chesthundhi".
Overlay (post): "CHECK METADATA" at 67.0 s; "SKIP UNNECESSARY MICRO-PARTITIONS" from ≈69.0 s.

**Shot 8c (71.76–74.11 s) – Partition Pruning:**
"Same style and palette. The dim Smoke Grey tiles and the lit Electric Blue tiles hold still while a clean soft light line frames the whole arrangement. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 71.96–72.4 s the frame line draws on "Dheenine"; 72.44–72.98 s the title presses in on "Partition Pruning antaru". **Effect: Press font** — "PARTITION PRUNING" presses into place at 72.44 s.
Overlay (post): "PARTITION PRUNING" at 72.44 s.

**Audio sync:** funnel at ≈64.5 s; strips pulse at 67.0 s; tiles dim at ≈69.0 s; title at 72.44 s.
**Negative prompt (all shots):** "Skipped tiles deleted or blown away, tiles disappearing, readable text, specific counts or percentages, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Automatic Clustering (74.11–83.45 s · 9.34 s)
**Voice-over:** "Mari Automatic Clustering enti? Large tables lo data organization ni improve cheyyadaniki Snowflake Automatic Clustering service provide chesthundhi."
**Tone:** clear.
**Visual objective:** Automatic Clustering is a Snowflake service that improves data organisation in large tables.
Generate as **two shots (9a, 9b)**.

**Shot 9a (74.11–76.51 s) – what is it?:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Cluster Orchid #C084FC, text #FFF8EE. The honeycomb of tiles hovers in a slightly messy arrangement, with tiles at a few different offsets. A soft Orchid glow pulses over it and a small question-mark glow appears. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 74.34–74.48 s the Orchid glow starts on "Mari"; 74.48–75.18 s it pulses on "Automatic Clustering"; 75.18–76.29 s the question mark pulses on "enti?".
Overlay (post): "AUTOMATIC CLUSTERING?" from 74.48 s.

**Shot 9b (76.51–83.45 s) – improving organisation in large tables:**
"Same style and palette. A very large honeycomb of Honey Amber tiles stretches across the frame, slightly disordered. A soft Orchid service-glow (a small glowing gear-like emblem, no text) moves across it and the tiles slide into neat, tidy groups with similar tones next to each other. The arrangement ends tidy and calm. No readable text, no logos, no watermark."
Motion: 76.73–78.0 s the large honeycomb is revealed on "Large tables lo"; ≈77.8–78.5 s the disorder is highlighted on "data organization"; ≈79.3–80.0 s the first tiles slide into groups on "improve cheyyadaniki"; 80.08–81.24 s the Orchid emblem sweeps over on "Snowflake Automatic Clustering"; ≈81.9–83.2 s the groups settle on "service provide chesthundhi". **Effect: Orbit ring** — the Orchid emblem circles the honeycomb once at ≈80.1 s.
Overlay (post): "AUTOMATIC CLUSTERING" at 80.08 s; "IMPROVES DATA ORGANIZATION IN LARGE TABLES" from ≈77.8 s.

**Audio sync:** disorder at ≈77.8 s; emblem at 80.08 s; groups settle at ≈82.0 s.
**Negative prompt (all shots):** "Technical claims about how clustering works, cluster-key syntax, cost or speed numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Banking project example (83.45–115.17 s · 31.72 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS table lo millions of records unnayi. Manam oka particular date transactions kosam query run chesthunnam. SQL query chuddam! SELECT * FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18'; Snowflake metadata ni check chesi, required date data unna Micro-partitions ni scan chesthundhi. Unnecessary Micro-partitions ni skip chesthundhi. Dheenivalla unnecessary data scanning reduce avuthundhi and query performance improve avvachu."
**Tone:** storytelling, focused.
**Visual objective:** A date query on a large TRANSACTIONS table scans only the micro-partitions that hold that date and skips the rest.
Generate as **seven shots (10a–10g)**. All shots use the same camera language and the same honeycomb layout so the story reads as one build.

**Shot 10a (83.45–85.89 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Metadata Mint #5EE6B8, text #FFF8EE. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in warm Amber, with an empty glass table frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from 83.8 s.

**Shot 10b (85.89–89.08 s) – TRANSACTIONS table:**
"Same style and palette. The glass table frame fills with a dense block of glowing cells, a very large table. The camera pulls back slowly to show how big it is. No readable fine text, no logos."
Overlay (post): "TRANSACTIONS" at ≈86.4 s (monospace); "MILLIONS OF RECORDS" at ≈87.0 s.

**Shot 10c (89.08–92.85 s) – a particular date:**
"Same style and palette. The large table block splits into its honeycomb of tiles, each with a Mint strip. A small glass calendar-page glyph (no readable date) lifts above the honeycomb and an Electric Blue beam points from it to the tiles. No readable fine text, no logos."
Motion: 89.28–89.8 s the table splits into tiles on "Manam oka"; ≈89.8–90.3 s the calendar glyph lifts on "particular date"; ≈91.5–92.63 s the beam aims on "query run chesthunnam".
Overlay (post): "QUERY FOR ONE DATE" from ≈89.8 s.

**Shot 10d (92.85–101.19 s) – SQL query:**
"Same style and palette. A dark glass code editor panel (a clean window with two empty lines, no readable code) floats at the centre with a thin Electric Blue edge and a blinking cursor. Behind it, softly out of focus, the honeycomb glows. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 93.06–94.22 s the panel slides in on "SQL query chuddam!"; 94.67–96.63 s line 1 types on "SELECT * FROM TRANSACTIONS"; 96.86–100.98 s line 2 types on "WHERE TRANSACTION_DATE = '2026-11-18';". **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
SELECT *
FROM TRANSACTIONS
WHERE TRANSACTION_DATE = '2026-11-18';
```
"SELECT *" at 94.67 s; "FROM TRANSACTIONS" at ≈95.4 s; "WHERE TRANSACTION_DATE = '2026-11-18';" from ≈96.9 s (the date completes by ≈100.9 s).

**Shot 10e (101.19–106.79 s) – check metadata and scan the required tiles:**
"Same style and palette, plus Smoke Grey #6B6358. The code panel shrinks to the top. Below it the honeycomb of tiles waits. An Electric Blue beam sweeps over the Mint metadata strips and the strips pulse. Then a few tiles light Electric Blue and are scanned, while the others stay dim. No readable text, no logos."
Motion: 101.42–102.7 s the beam checks the strips on "Snowflake metadata ni check chesi"; ≈103.4–104.1 s a few tiles light up on "required date data unna"; ≈105.2–106.58 s the lit tiles pulse on "Micro-partitions ni scan chesthundhi".
Overlay (post): "CHECK METADATA" at 101.42 s; "SCAN ONLY THE REQUIRED MICRO-PARTITIONS" from ≈103.4 s.

**Shot 10f (106.79–109.66 s) – skip the rest:**
"Same style and palette. The remaining tiles fade to Smoke Grey and slide very slightly back, skipped. They remain visible in the honeycomb. Calm, clear. No readable text, no logos."
Motion: 107.08–107.84 s the tiles dim on "Unnecessary Micro-partitions"; ≈108.6–109.45 s a soft Smoke Grey wave passes over them on "skip chesthundhi".
Overlay (post): "SKIP UNNECESSARY MICRO-PARTITIONS" from 107.08 s.

**Shot 10g (109.66–115.17 s) – less scanning, better performance:**
"Same style and palette. A simple side-by-side comparison: on the left a faint ghost of the whole honeycomb lit in Electric Blue (everything scanned); on the right the real result, with only a few tiles lit. A small soft gauge-arc (no numbers) on the right fills up a little more than the left, suggesting better performance. No readable text, no logos."
Motion: 109.87–111.6 s the ghost and the real result appear on "Dheenivalla unnecessary data scanning"; ≈112.4 s the lit area on the right shrinks on "reduce avuthundhi"; ≈113.3–114.94 s the gauge fills slightly on "query performance improve avvachu". **Effect: Rack focus** — focus pulls from the ghost to the real result at ≈112.4 s.
Overlay (post): "LESS UNNECESSARY SCANNING" from ≈110.4 s; "BETTER QUERY PERFORMANCE" from ≈113.3 s. Show "can improve", not a guarantee, and no numbers (the script says "improve avvachu").

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake dates or numbers, skipped tiles deleted or blown away, specific counts or percentages, guaranteed speed claims, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 11 – Simple recap (115.17–131.74 s · 16.57 s)
**Voice-over:** "So, simple ga gurthupettukondi! Micro-partitions – Automatically organized data storage units. Partition Pruning – Unnecessary Micro-partitions ni skip cheyyadam. Automatic Clustering – Data organization ni maintain cheyyadaniki Snowflake provide chese service."
**Tone:** confident.
**Visual objective:** Three-point recap.
Generate as **four shots (11a–11d)**.

**Shot 11a (115.17–117.43 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Cluster Orchid #C084FC, text #FFF8EE. A calm honeycomb of tiles glides to the centre with a soft bloom against the warm dark background. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈116.0 s.

**Shot 11b (117.43–121.76 s) – Micro-partitions:**
"Same style and palette. A single large Honey Amber tile with a Mint strip fills the frame, then it multiplies into a tidy honeycomb that fills the background. Clean and calm. No readable text, no logos."
Overlay (post): "MICRO-PARTITIONS" at 117.64 s; "Automatically organized data storage units" from 118.97 s. **Effect: Liquid glass** — the label sits on a glass panel.

**Shot 11c (121.76–125.79 s) – Partition Pruning:**
"Same style and palette. The honeycomb fills the frame. An Electric Blue beam lights a few tiles and the others dim to Smoke Grey but stay in place. Clean and calm. No readable text, no logos."
Overlay (post): "PARTITION PRUNING" at 121.96 s; "Skip unnecessary Micro-partitions" from 123.2 s.

**Shot 11d (125.79–131.74 s) – Automatic Clustering:**
"Same style and palette. A slightly disordered honeycomb slides into tidy Orchid-glowing groups while a small Orchid emblem rests above it, showing that a service keeps the organisation maintained. Clean and calm. No readable text, no logos."
Overlay (post): "AUTOMATIC CLUSTERING" at 126.01 s; "Snowflake service that maintains data organization" from 127.47 s.

**Audio sync:** card 1 at 117.64 s; card 2 at 121.96 s; card 3 at 126.01 s.
**Negative prompt:** "Claims about how clustering works, numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 12 – Series card and Query Profile teaser (131.74–139.94 s · 8.20 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Fourteen! Next video lo Query Profile gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 14 and tease the next topic.
Generate as **two shots (12a, 12b)**.

**Shot 12a (131.74–135.34 s) – Day 14 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Cluster Orchid #C084FC, text #FFF8EE. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first fourteen lit in Honey Amber (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 14" from ≈132.4 s; the fourteenth node lights at ≈134.5 s on "Fourteen".

**Shot 12b (135.34–139.94 s) – teaser:**
"Same style and palette. A teaser panel slides in showing a clean glass flow-chart of a few connected boxes (abstract, no readable text) with a magnifier lens passing over it and lighting up one box. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: QUERY PROFILE" from ≈136.4 s; "REAL-TIME EXAMPLES" from ≈137.8 s. The visual only suggests inspecting a query's steps. Do not show real Query Profile screenshots, numbers or specific operators.

**Audio sync:** card at ≈132.4 s; the fourteenth node at ≈134.5 s; the lens at ≈136.4 s; "REAL-TIME EXAMPLES" at ≈137.8 s.
**Negative prompt:** "Real Snowflake UI screenshots, readable text, numbers, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 13 – Follow, contact and end card (139.94–152.84 s · 12.90 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (13a–13c)**.

**Shot 13a (139.94–146.78 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Cluster Orchid #C084FC, text #FFF8EE. A calm, clean background with a soft honey glow, a small honeycomb of glass tiles drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at 140.76 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈143.7 s, emphasised at ≈145.7 s on "Follow" (estimated).

**Shot 13b (146.78–150.63 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Amber and Orchid glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 146.94 s, emphasised at ≈149.5 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 13c (150.63–152.84 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 150.81 s. Hold the final frame for the last 0.4 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 14. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #17110C, Honey Amber #F5A524, Electric Blue #3AA0FF, Smoke Grey #6B6358, Metadata Mint #5EE6B8, Cluster Orchid #C084FC, text #FFF8EE, secondary text #B3A797. Colour code: table data = Honey Amber glass block with rows of glowing cells; a micro-partition = a small rounded-hexagon Honey Amber glass tile with a thin Mint metadata strip (a range bar, no readable numbers); a scanned tile = lit Electric Blue; a skipped tile = dim Smoke Grey (still present, never deleted or blown away); the query = a thin Electric Blue beam; clustered or organised tiles = neat groups with a soft Orchid glow. A query first checks the Mint metadata strips, then scans only the tiles that can hold the required data and skips the rest. Never show tile sizes, counts, percentages or speed numbers. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Analyse the audio with Whisper (Windows)

This is how the timings in this file were produced (same workflow as Day 9–13).

1. **Create a virtual environment and install** (PowerShell, Python 3.10):
   ```powershell
   py -3.10 -m venv whisper-env
   .\whisper-env\Scripts\python.exe -m pip install faster-whisper
   ```
2. **Run the `run_whisper.py` script from Day 9's file** (`small` model, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`).
   ```powershell
   .\whisper-env\Scripts\python.exe run_whisper.py Audio\day14.mp3 whisper_out.json
   ```
   On a long file (about 2.5 minutes) this took more than 10 minutes on the CPU, so run it in the background and do not start a second copy.
3. **Cross-check with the real pauses:**
   ```powershell
   ffmpeg -i Audio\day14.mp3 -af "silencedetect=noise=-26dB:d=0.2" -f null - 2>&1 | Select-String "silence_(start|end)"
   ```
4. **Build the timing map:** use the end of each silence as the phrase start, use Whisper word times for emphasis words, keep your script's spelling, and place scene cuts in the middle of a pause.

**Notes for this audio**
- Whisper in English mode wrote this Telugu-English narration as an English translation. Four phrases were missed or garbled (see the note at the top), so their word times are estimated from the pauses.
- Whisper wrote "venakala" as "vanakal" and "WHERE" as "wear". These are spelling slips, not audio problems.
- Pause ends were preferred for phrase starts.

---

## 6. Editing and synchronisation plan

1. Import `day14.mp3` (152.84 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, labels such as TRANSACTIONS, the SQL code, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Do not use real Instagram or YouTube logos in the support-request scene; use the generic glyphs.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (soft tile clicks, a scan whoosh, a gentle dial tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at each button in the support request (≈13.8, ≈15.7, ≈17.4 s), at the question (23.02 s), at the scripted pause (36.30–37.61 s), at the title (40.39, 41.7 s), at the tile split (≈48.0 s), at min and max (59.52, 60.36 s), at WHERE (≈64.5 s), at the skip (≈69.0 s), at each code line (94.67, ≈96.9 s), at the scan and skip in the banking example (≈103.4, ≈108.6 s), at the three recap cards (117.64, 121.96, 126.01 s), at the final tagline (150.81 s), and at the Follow and Contact lines (≈145.7, ≈149.5 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Snowflake automatically divides a table's data into small units called micro-partitions; each one has metadata (a minimum value, a maximum value and other metadata information); with a WHERE condition Snowflake checks the metadata and skips unnecessary micro-partitions, which is Partition Pruning; Automatic Clustering is a Snowflake service that improves data organisation in large tables; in the banking example the date query scans only the micro-partitions that hold the required date and skips the rest, which reduces unnecessary scanning and can improve query performance. **No sizes, counts, percentages or performance numbers** are shown, because the script gives none.
- `SELECT * FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18';` is valid Snowflake syntax. The overlay uses the script's date form.
- Skipped micro-partitions are shown dimmed and still present, never deleted, so "Blow away" is not used.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
