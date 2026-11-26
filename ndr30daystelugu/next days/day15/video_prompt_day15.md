# Thirty Days of Snowflake – Day 15: Snowflake Query Profile
Video prompt package (NDR EdTech) — `Audio\day15.mp3` + `days-scripts\day15.txt`, analysed with Whisper

> **Timing status: MEASURED from day15.mp3 (112.51 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied word times inside phrases and can be 0.1–0.5 s early or late. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (3 items):**
> 1. **Follow and Contact lines (about 104–110 s):** Whisper mixed up the word order of these two Telugu lines, so the "Follow" and "Contact" word times are estimated (≈). Adjust by 0.2–0.5 s if needed.
> 2. **Spelling slips in Whisper only:** it wrote "NDR at Tech" (26.5–28 s) and "IOI" (about 55.8 s, your script says "chudachu"). These are transcription slips, not audio problems.
> 3. **18.43–19.24 s** is your scripted `[pause]`, a real 0.81 s silence. The visuals hold a calm beat there.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 15: Snowflake Query Profile |
| Duration | **112.51 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,375 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day15.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (27 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Heat Trace" (new for Day 15)
| Role | HEX | Use |
|---|---|---|
| Background | `#120D10` | Base, gradients (dark wine-black) |
| Cool Cyan | `#2FD6E8` | Cheap or fast operations, calm states |
| Warm Yellow | `#FFD23F` | Medium-cost operations |
| Hot Orange-Red | `#FF5A36` | The slowest or most expensive operation, the problem |
| Node Slate | `#8FA3B8` | Operator nodes, links, neutral glass |
| Primary text | `#F6F4F2` | Titles, labels |
| Secondary text | `#A99FA3` | Captions |

**Colour code (use in every scene):** Query Profile is drawn as a graph of connected glass **operator nodes** in Node Slate. A node's glow shows how much time it uses: Cool Cyan (small), Warm Yellow (medium), Hot Orange-Red (large, the bottleneck). Tables are white glass blocks.

**The core visual rule (technical accuracy):** Query Profile is a **graphical representation of how a query executed**. Show abstract nodes and bars only. Do not show real Snowflake UI screenshots, real operator statistics, percentages or specific numbers. The only number on screen is the script's "10 MINUTES".

### Motion effects used (from the skill's effects library)
Comment drop, Live cursor, Day dial, Head stack, Letter dive, Impact frame, Liquid glass, Layer explode, Rack focus, Press font. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–4.09 | "Hello guys! Andaru ela unnaru?" (0.00–1.91) · "Oka situation imagine cheyyandi!" (2.37–3.84) | Curious | Title hook, "imagine" |
| 2 | 4.09–18.84 | "Meeru Snowflake lo oka SQL query execute chesaru." (4.33–7.54) · "Kaani query run avvadaniki 10 minutes time teesukuntundhi!" (7.94–10.97) · "Ippudu problem ekkada undho ela identify chestharu?" (11.45–14.18) · "Query lo na? Data scanning lo na? Leda JOIN operation lo na?" (14.65–18.43) · *[scripted pause 18.43–19.24]* | Worried, searching | Slow query, three suspects |
| 3 | 18.84–26.22 | "Ee problems identify cheyyadaniki Snowflake lo oka powerful feature undhi!" (19.24–23.25) · "Adhe Query Profile!" (23.68–24.93) · "Let's understand!" (25.34–25.95) | Reveal, excited | Black box opens, title |
| 4 | 26.22–28.40 | "Welcome to NDR EdTech!" (26.48–28.15) | Welcoming | Brand welcome |
| 5 | 28.40–38.42 | "Snowflake Query Profile ante mana SQL query execution ela jarigindho graphical representation lo chupinche feature." (28.65–35.04) · "Dheenitho query execution steps ni analyze cheyyachu." (35.48–38.24) | Clear | Query becomes a node graph |
| 6 | 38.42–62.29 | "Main ga manam ee operations observe cheyyali." (38.60–40.80) · "First, Table Scan! Entha data scan ayyindho identify cheyyachu." (41.28–45.19) · "Second, Join Operations! JOIN operations lo ekkada performance issue undho analyze cheyyachu." (45.65–51.05) · "Third, Aggregation! GROUP BY and aggregation operations ela execute ayyayo chudachu." (51.53–56.65) · "Fourth, Execution Time! Query lo ekkuva time ekkada spend ayyindho identify cheyyachu." (57.14–62.01) | Clear, structured | Four numbered operations |
| 7 | 62.29–83.65 | "Oka Banking project example teesukundham." (62.57–64.42) · "Mana CUSTOMER table and TRANSACTIONS table ni JOIN chesi monthly reports generate chesthunnam." (64.82–69.44) · "Kaani query chala slow ga execute avuthundhi." (69.80–72.21) · "Ippudu Query Profile open chesi table scan, join operations and execution time analyze chestham." (72.60–78.00) · "Unnecessary data scanning or expensive operations identify chesi query ni optimize cheyyachu." (78.37–83.42) | Storytelling | Banking: slow report, open Query Profile, find the bottleneck |
| 8 | 83.65–92.31 | "So, simple ga gurthupettukondi!" (83.87–85.51) · "Query Profile helps us understand how Snowflake executes our SQL query and where performance bottlenecks exist." (85.86–92.10) | Confident | One-line recap |
| 9 | 92.31–101.28 | "Idi mana Thirty Days of Snowflake series lo Day Fifteen!" (92.51–95.40) · "Next video lo Snowflake Query Optimization Techniques gurinchi real-time examples tho explain chesthanu." (95.80–101.09) | Upbeat | Day 15 card, optimisation teaser |
| 10 | 101.28–112.51 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (101.46–106.92) · "Full course details kosam NDR EdTech ni Contact avvandi!" (107.33–110.28) · "Let's Learn and Grow Together!" (110.65–112.17) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.57–1.05, 1.91–2.37, 3.84–4.33, 7.54–7.94, 9.41–9.65, 10.97–11.45, 14.18–14.65, 15.23–15.59, 16.52–16.89, 18.43–19.24 (the scripted `[pause]`), 23.25–23.68, 23.95–24.21, 24.93–25.34, 25.95–26.48, 28.15–28.65, 35.04–35.48, 38.24–38.60, 40.80–41.28, 41.60–41.92, 42.47–42.93, 45.19–45.65, 46.01–46.32, 47.07–47.63, 51.05–51.53, 51.77–52.12, 52.71–53.21, 56.65–57.14, 57.30–57.74, 58.50–58.99, 62.01–62.57, 64.42–64.82, 69.44–69.80, 72.21–72.60, 78.00–78.37, 83.42–83.87, 85.51–85.86, 89.93–90.20, 92.10–92.51, 95.40–95.80, 101.09–101.46, 106.92–107.33, 110.28–110.65, 112.17–112.51.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Hello guys! Andaru ela unnaru? | Hello 0.0 · Andaru ela unnaru 1.05–1.9 |
| Oka situation imagine cheyyandi! | situation ≈2.5 · imagine ≈3.0 |
| Meeru Snowflake lo oka SQL query execute chesaru. | Snowflake ≈5.0 · SQL ≈5.8 · query ≈6.3 · execute ≈6.9 |
| Kaani query run avvadaniki 10 minutes time teesukuntundhi! | **10 minutes** 9.65–10.2 · teesukuntundhi ≈10.5 |
| Ippudu problem ekkada undho ela identify chestharu? | problem ≈11.8 · identify ≈13.2 |
| Query lo na? Data scanning lo na? Leda JOIN operation lo na? | Query 14.65 · Data scanning 15.59–16.1 · JOIN ≈17.4 |
| Ee problems identify cheyyadaniki Snowflake lo oka powerful feature undhi! | problems ≈20.0 · powerful ≈22.0 |
| Adhe Query Profile! | Adhe 23.68 · Query Profile 24.21–24.5 |
| Let's understand! | Let's 25.34 · understand 25.52 |
| Welcome to NDR EdTech! | Welcome 26.48 · NDR 27.04 · EdTech ≈27.7 |
| Snowflake Query Profile ante mana SQL query execution ela jarigindho graphical representation lo chupinche feature. | Query Profile 29.1–29.4 · SQL query execution 30.5–31.3 · graphical representation 32.9–33.3 |
| Dheenitho query execution steps ni analyze cheyyachu. | query execution steps 36.0–36.9 · analyze ≈37.2 |
| Main ga manam ee operations observe cheyyali. | observe ≈39.4 · operations ≈39.6 |
| First, Table Scan! | First 41.28 · Table Scan 41.92 |
| Entha data scan ayyindho identify cheyyachu. | Entha data scan 42.93–43.8 · identify ≈44.3 |
| Second, Join Operations! | Second 45.65 · Join Operations 46.32 |
| JOIN operations lo ekkada performance issue undho analyze cheyyachu. | JOIN 47.63 · performance issue ≈49.2 · analyze ≈50.0 |
| Third, Aggregation! | Third 51.53 · Aggregation 52.12 |
| GROUP BY and aggregation operations ela execute ayyayo chudachu. | GROUP BY 53.21–53.6 · aggregation ≈53.9 · execute ≈55.4 |
| Fourth, Execution Time! | Fourth 57.14 · Execution Time 57.74 |
| Query lo ekkuva time ekkada spend ayyindho identify cheyyachu. | ekkuva time ≈59.2 · spend ≈60.6 · identify ≈61.2 |
| Oka Banking project example teesukundham. | Banking 62.7 · project 63.08 · example 63.5 |
| Mana CUSTOMER table and TRANSACTIONS table ni JOIN chesi monthly reports generate chesthunnam. | CUSTOMER ≈65.0 · TRANSACTIONS ≈66.3 · JOIN ≈67.4 · monthly reports ≈68.0 |
| Kaani query chala slow ga execute avuthundhi. | query 70.1 · slow ≈70.9 |
| Ippudu Query Profile open chesi table scan, join operations and execution time analyze chestham. | Query Profile ≈72.9–73.4 · table scan ≈74.3 · join operations ≈75.4 · execution time ≈76.3 |
| Unnecessary data scanning or expensive operations identify chesi query ni optimize cheyyachu. | unnecessary data scanning ≈78.5–79.4 · expensive operations ≈80.0 · optimize ≈81.9 |
| So, simple ga gurthupettukondi! | So 83.87 · simple ga ≈84.4 |
| Query Profile helps us understand how Snowflake executes our SQL query and where performance bottlenecks exist. | Query Profile 86.06 · understand 87.04 · executes 88.42 · SQL query 89.14–89.5 · bottlenecks 91.02 |
| Idi mana Thirty Days of Snowflake series lo Day Fifteen! | Thirty ≈92.8 · Days 93.14 · Snowflake 93.54 · series 93.98 · Day 94.54 · Fifteen 94.8 |
| Next video lo Snowflake Query Optimization Techniques gurinchi real-time examples tho explain chesthanu. | Next 95.86 · Query Optimization Techniques ≈97.2–98.1 · real-time examples ≈99.0 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈104.4 · NDR EdTech ≈105.2–106.0 · **Follow** ≈106.2 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 107.92–110.06 · NDR EdTech ≈108.7 · **Contact** ≈109.5 (estimated) |
| Let's Learn and Grow Together! | Let's 110.65 · Learn 110.9 · Grow 111.48 · Together 111.76 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2.*

**Object look (keep identical in every scene):** a **SQL query** = a glass card with abstract lines. A **table** = a white glass block with rows of small cells. A **Query Profile node** = a rounded Node Slate glass box with a small glowing bar showing its share of time (Cyan small, Yellow medium, Orange-Red large). Nodes are linked by thin Slate lines.

### Scene 1 – Hook (0.00–4.09 s · 4.09 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka situation imagine cheyyandi!"
**Tone:** curious.
**Visual objective:** Welcome viewers and ask them to imagine a situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2. A dark wine-black space with soft cyan light and drifting glass particles. A glowing glass SQL query card (abstract lines, no readable text) floats at the upper-centre and a soft thought-bubble of glass forms above it. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–1.91 s: particles drift in and the query card appears on "Hello guys! Andaru ela unnaru?".
- 2.37–3.84 s: the thought-bubble forms on "Oka situation imagine cheyyandi!" (situation ≈2.5 s).
- 3.84–4.09 s: soft light sweep into Scene 2.
- Effect: **Comment drop** — the thought-bubble drops in beside the card at ≈2.9 s.
**Audio sync:** title lands at ≈1.05 s; the sweep completes in the pause at 3.84–4.33 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 15".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – A query that takes 10 minutes (4.09–18.84 s · 14.75 s)
**Voice-over:** "Meeru Snowflake lo oka SQL query execute chesaru. Kaani query run avvadaniki 10 minutes time teesukuntundhi! Ippudu problem ekkada undho ela identify chestharu? Query lo na? Data scanning lo na? Leda JOIN operation lo na?"
**Tone:** worried, searching. The last 0.4 s is the start of the scripted pause.
**Visual objective:** A query runs very slowly and it is not clear where the problem is.
Generate as **four shots (2a–2d)**.

**Shot 2a (4.09–7.74 s) – run the query:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Node Slate #8FA3B8, text #F6F4F2. A glass SQL query card (abstract lines) slides into a glass Snowflake warehouse panel (a snowflake-crystal glyph, no logo) and a glowing 'run' button is pressed by a cursor. A soft cyan pulse starts. Calm, clean, phone-readable. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.33–5.0 s the card slides in on "Meeru Snowflake"; ≈5.8–6.9 s the cursor presses run on "SQL query execute"; ≈6.9–7.54 s the pulse starts on "chesaru". **Effect: Live cursor.**
Overlay (post): "SQL QUERY EXECUTED" from ≈5.8 s.

**Shot 2b (7.74–11.21 s) – it takes 10 minutes:**
"Same style and palette, plus Hot Orange-Red #FF5A36. A progress bar crawls very slowly under the query card while a glass clock dial (no numerals) turns steadily; the bar's glow shifts from Cyan to Orange-Red. Tense, slow feeling. No readable text, no logos, no watermark."
Motion: 7.94–9.41 s the bar starts to crawl on "Kaani query run avvadaniki"; 9.65–10.97 s the dial turns and the glow turns Orange-Red on "10 minutes time teesukuntundhi!". **Effect: Day dial.**
Overlay (post): "10 MINUTES" at 9.65 s.

**Shot 2c (11.21–14.42 s) – where is the problem?:**
"Same style and palette. The query card becomes a dark closed glass box. A magnifier glass moves over it, searching, and a soft white question-mark glow pulses above. Tense, curious. No readable text, no logos, no watermark."
Motion: 11.45–13.2 s the magnifier searches on "Ippudu problem ekkada undho"; ≈13.2–14.18 s the question mark pulses on "ela identify chestharu?".
Overlay (post): "WHERE IS THE PROBLEM?" from 11.45 s.

**Shot 2d (14.42–18.84 s) – three suspects:**
"Same style and palette. Three glass cards appear one after another in a neat vertical stack, each with a small soft question-mark glow: first a SQL query card, second a wall of small data cells (data scanning), third two table blocks about to merge (a JOIN). Clean, uncluttered, phone-readable. Hold a calm still frame for the last 0.4 s. No readable text, no logos, no watermark."
Motion: 14.65–15.23 s the query card appears on "Query lo na?"; 15.59–16.52 s the data wall appears on "Data scanning lo na?"; 16.89–18.43 s the join cards appear on "Leda JOIN operation lo na?" (JOIN ≈17.4 s); 18.43–18.84 s calm hold during the scripted pause. **Effect: Head stack.**
Overlay (post): "IN THE QUERY?" at 14.65 s; "IN DATA SCANNING?" at 15.59 s; "IN THE JOIN?" at 16.89 s.

**Audio sync:** run at ≈6.0 s; "10 MINUTES" at 9.65 s; magnifier at 11.45 s; suspects at 14.65, 15.59 and 16.89 s.
**Negative prompt (all shots):** "Readable text, real error messages, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – The powerful feature: Query Profile (18.84–26.22 s · 7.38 s)
**Voice-over:** "Ee problems identify cheyyadaniki Snowflake lo oka powerful feature undhi! Adhe Query Profile! Let's understand!"
**Tone:** reveal, excited.
**Visual objective:** Reveal Query Profile and name the topic.
Generate as **two shots (3a, 3b)**.

**Shot 3a (18.84–23.47 s) – a powerful feature:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Node Slate #8FA3B8, text #F6F4F2. The dark closed glass box from the last scene cracks along its edges and a ray of Cool Cyan light shines out, opening it to reveal a glowing snowflake-crystal emblem inside. Mysterious, then hopeful. Slow push-in. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 19.24–21.5 s the box edges start to glow on "Ee problems identify cheyyadaniki"; ≈21.7–23.25 s the box opens and the emblem rises on "Snowflake lo oka powerful feature undhi!" (powerful ≈22.0 s). Hold the still frame in the pause at 18.84–19.24 s.

**Shot 3b (23.47–26.22 s) – Query Profile, let's understand:**
"Same style and palette. The emblem moves to the upper-centre and a small glass node-graph (a few connected rounded boxes in Slate with Cyan, Yellow and Orange-Red bars) draws itself below it. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark."
Motion: 23.68–23.95 s a soft glow on "Adhe"; 24.21–24.93 s the title lands on "Query Profile!" (**Effect: Impact frame** — one-frame flash at 24.21 s; **Effect: Letter dive** — the letters settle fully before 24.9 s); 25.34–25.95 s a subtitle pops in on "Let's understand!".
Overlay (post): "QUERY PROFILE" at 24.21 s; "LET'S UNDERSTAND!" at 25.34 s.

**Audio sync:** box opens at ≈21.7 s; title at 24.21 s; subtitle at 25.34 s.
**Negative prompt:** "Misspelled title, real Snowflake UI screenshots, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Welcome (26.22–28.40 s · 2.18 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Node Slate #8FA3B8, text #F6F4F2. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft cyan glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 26.48–28.15 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 26.48 s; "NDR" at 27.04 s; "EdTech" at ≈27.7 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – What is Query Profile? (28.40–38.42 s · 10.02 s)
**Voice-over:** "Snowflake Query Profile ante mana SQL query execution ela jarigindho graphical representation lo chupinche feature. Dheenitho query execution steps ni analyze cheyyachu."
**Tone:** clear.
**Visual objective:** Query Profile shows how a query executed, as a graph, so you can analyse the steps.
Generate as **two shots (5a, 5b)**.

**Shot 5a (28.40–35.26 s) – a graphical view of execution:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2. A glass SQL query card (abstract lines) floats at the upper-centre. It separates into layers and re-forms below it as a clean graph of six connected Node Slate glass boxes, each with a small glowing bar (Cyan, Yellow or Orange-Red). Soft rim lighting, slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 28.65–30.0 s the query card glows on "Snowflake Query Profile ante"; 30.5–32.5 s the card separates into layers on "mana SQL query execution ela jarigindho"; ≈32.9–35.04 s the node graph forms on "graphical representation lo chupinche feature". **Effect: Layer explode.**
Overlay (post): "QUERY PROFILE" at 29.1 s; "GRAPHICAL VIEW OF QUERY EXECUTION" from ≈32.9 s.

**Shot 5b (35.26–38.42 s) – analyse the steps:**
"Same style and palette. A cursor travels along the node graph from the first box to the last, pausing briefly on each and lighting it. The graph stays calm and tidy. No readable text, no logos, no watermark."
Motion: 35.48–36.0 s the cursor appears on "Dheenitho"; 36.0–37.2 s it moves step by step on "query execution steps"; ≈37.2–38.24 s it lights the last box on "analyze cheyyachu". **Effect: Live cursor.**
Overlay (post): "ANALYZE EXECUTION STEPS" from 36.0 s.

**Audio sync:** layers separate at 30.5 s; graph forms at ≈32.9 s; cursor at 36.0 s.
**Negative prompt (all shots):** "Real Snowflake UI screenshots, readable node labels, real statistics, percentages, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – Four operations to observe (38.42–62.29 s · 23.87 s)
**Voice-over:** "Main ga manam ee operations observe cheyyali. First, Table Scan! Entha data scan ayyindho identify cheyyachu. Second, Join Operations! JOIN operations lo ekkada performance issue undho analyze cheyyachu. Third, Aggregation! GROUP BY and aggregation operations ela execute ayyayo chudachu. Fourth, Execution Time! Query lo ekkuva time ekkada spend ayyindho identify cheyyachu."
**Tone:** clear, structured.
**Visual objective:** The four things to observe: Table Scan, Join Operations, Aggregation, Execution Time.
Generate as **five shots (6a–6e)**. Keep the node-graph layout identical so each shot highlights a different part of the same graph.

**Shot 6a (38.42–41.04 s) – four operations:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Node Slate #8FA3B8, text #F6F4F2. Four glass tiles with small abstract icons (a data wall, two merging blocks, a stack collapsing into one, a stopwatch ring) rise one by one in a neat vertical stack. Clean, uncluttered, phone-readable layout. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 38.60–39.4 s the first tiles rise on "Main ga manam"; ≈39.4–40.8 s the stack completes on "ee operations observe cheyyali". **Effect: Head stack.**
Overlay (post): "OBSERVE THESE 4 OPERATIONS" from 38.60 s.

**Shot 6b (41.04–45.42 s) – 1 · Table Scan:**
"Same style and palette. A wall of small glowing data cells fills the lower half. A thin Cyan scan beam sweeps across part of it and a simple meter bar on the side fills in proportion to the cells scanned. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark."
Motion: 41.28–42.47 s the badge and title appear on "First, Table Scan!" (**Effect: Press font** — "TABLE SCAN" presses in at 41.92 s); 42.93–44.0 s the beam sweeps on "Entha data scan ayyindho"; ≈44.3–45.19 s the meter settles on "identify cheyyachu".
Overlay (post): "1 · TABLE SCAN" at 41.28 s; "HOW MUCH DATA WAS SCANNED" from 42.93 s.

**Shot 6c (45.42–51.29 s) – 2 · Join Operations:**
"Same style and palette, plus Hot Orange-Red #FF5A36. Two white glass table blocks slide toward a Slate join-node and merge into one wider block. The join-node's glow starts Yellow and turns Orange-Red, marking the slow part, and a magnifier lens passes over it. A numbered badge '2'. No readable text, no logos, no watermark."
Motion: 45.65–47.07 s the badge and title appear on "Second, Join Operations!" (Join Operations at 46.32 s); 47.63–48.8 s the tables slide in on "JOIN operations lo ekkada"; ≈49.2–50.0 s the node turns Orange-Red on "performance issue undho"; ≈50.0–51.05 s the lens passes over it on "analyze cheyyachu".
Overlay (post): "2 · JOIN OPERATIONS" at 45.65 s; "FIND WHERE THE JOIN IS SLOW" from ≈48.5 s.

**Shot 6d (51.29–56.90 s) – 3 · Aggregation:**
"Same style and palette. A stack of many small row-bars slides into a funnel-shaped Slate node and comes out as a few thicker group-bars, showing grouping and aggregation. A numbered badge '3'. Calm, clear. No readable text, no logos, no watermark."
Motion: 51.53–52.71 s the badge and title appear on "Third, Aggregation!"; 53.21–54.0 s the row-bars gather on "GROUP BY and aggregation operations"; ≈54.5–56.65 s the thicker bars come out on "ela execute ayyayo chudachu" (execute ≈55.4 s).
Overlay (post): "3 · AGGREGATION" at 51.53 s; "GROUP BY" at 53.21 s; "HOW IT EXECUTED" from ≈55.0 s.

**Shot 6e (56.90–62.29 s) – 4 · Execution Time:**
"Same style and palette. A ring-shaped stopwatch splits into coloured segments, one for each operation: most are small Cyan segments, one is a large Orange-Red segment. A numbered badge '4'. The focus pulls to the largest segment. No readable text, no logos, no watermark."
Motion: 57.14–58.50 s the badge and title appear on "Fourth, Execution Time!" (Execution Time at 57.74 s); 58.99–60.4 s the ring splits on "Query lo ekkuva time"; ≈60.6–62.01 s the largest segment glows on "ekkada spend ayyindho identify cheyyachu". **Effect: Rack focus** — focus pulls to the largest segment at ≈60.6 s.
Overlay (post): "4 · EXECUTION TIME" at 57.14 s; "WHERE MOST TIME IS SPENT" from ≈59.2 s.

**Audio sync:** badge 1 at 41.28 s; badge 2 at 45.65 s; badge 3 at 51.53 s; badge 4 at 57.14 s.
**Negative prompt (all shots):** "Real statistics, percentages, readable text, specific causes of slow joins, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (62.29–83.65 s · 21.36 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana CUSTOMER table and TRANSACTIONS table ni JOIN chesi monthly reports generate chesthunnam. Kaani query chala slow ga execute avuthundhi. Ippudu Query Profile open chesi table scan, join operations and execution time analyze chestham. Unnecessary data scanning or expensive operations identify chesi query ni optimize cheyyachu."
**Tone:** storytelling.
**Visual objective:** A slow monthly report is analysed in Query Profile, and the expensive parts are found so the query can be optimised.
Generate as **five shots (7a–7e)**. All shots use the same camera language so the story reads as one build.

**Shot 7a (62.29–64.62 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in cool cyan, with an empty glass report-page frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from 62.7 s.

**Shot 7b (64.62–69.62 s) – JOIN CUSTOMER and TRANSACTIONS:**
"Same style and palette. Two white glass table blocks slide in from left and right: one smaller (customers), one much larger with many rows (transactions). They merge through a Slate join-node into a glowing report page (abstract bars and lines, no readable text). No readable fine text, no logos."
Motion: 64.82–65.8 s the CUSTOMER table slides in on "Mana CUSTOMER table"; ≈66.3 s the TRANSACTIONS table slides in; ≈67.4 s the join-node glows on "JOIN chesi"; ≈68.0–69.44 s the report page forms on "monthly reports generate chesthunnam".
Overlay (post): "CUSTOMER" at ≈65.0 s; "TRANSACTIONS" at ≈66.3 s; "JOIN" at ≈67.4 s; "MONTHLY REPORTS" at ≈68.0 s (monospace for the table names).

**Shot 7c (69.62–72.41 s) – the query is slow:**
"Same style and palette. The report page stays half-built while a progress bar crawls and its glow turns from Cyan to Orange-Red. A small spinner turns slowly. Tense feeling. No readable text, no logos."
Motion: 69.80–70.6 s the bar crawls on "Kaani query chala"; ≈70.9–72.21 s the glow turns Orange-Red on "slow ga execute avuthundhi".
Overlay (post): "QUERY IS VERY SLOW" from 69.80 s.

**Shot 7d (72.41–78.19 s) – open Query Profile:**
"Same style and palette. The report page slides aside and a Query Profile node graph (six Slate boxes with small glowing bars) fills the frame. A cursor lights the table-scan node, then the join node, then the stopwatch ring for execution time, one after another. No readable text, no logos."
Motion: 72.60–74.2 s the graph opens on "Ippudu Query Profile open chesi"; ≈74.3 s the cursor lights the scan node on "table scan"; ≈75.4 s the join node on "join operations"; ≈76.3–77.9 s the stopwatch ring on "execution time analyze chestham". **Effect: Live cursor.**
Overlay (post): "OPEN QUERY PROFILE" from 72.60 s; "TABLE SCAN" at ≈74.3 s; "JOIN OPERATIONS" at ≈75.4 s; "EXECUTION TIME" at ≈76.3 s.

**Shot 7e (78.19–83.65 s) – find the bottleneck and optimise:**
"Same style and palette. In the node graph the scan node and the join node glow Orange-Red. A magnifier passes over them. Then, after a soft pulse, those two nodes cool from Orange-Red to Yellow and Cyan, showing that the query has been optimised. Calm, satisfying. No readable text, no numbers, no logos."
Motion: 78.37–79.4 s the scan node glows on "Unnecessary data scanning" (≈78.5 s); ≈80.0–81.2 s the join node glows on "expensive operations identify chesi"; ≈81.9–83.42 s the nodes cool on "query ni optimize cheyyachu". **Effect: Rack focus** — focus pulls from the whole graph to the hot nodes at ≈79.0 s.
Overlay (post): "UNNECESSARY DATA SCANNING" at ≈78.5 s; "EXPENSIVE OPERATIONS" at ≈80.0 s; "OPTIMIZE THE QUERY" at ≈81.9 s. Show "can optimise", with no improvement numbers.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake numbers, real Snowflake UI screenshots, specific causes or fixes, improvement numbers, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (83.65–92.31 s · 8.66 s)
**Voice-over:** "So, simple ga gurthupettukondi! Query Profile helps us understand how Snowflake executes our SQL query and where performance bottlenecks exist."
**Tone:** confident.
**Visual objective:** One-line recap.
Generate as **two shots (8a, 8b)**.

**Shot 8a (83.65–85.69 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Node Slate #8FA3B8, text #F6F4F2. A calm Node Slate node graph glides to the centre with a soft cyan bloom against the dark background. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈84.2 s.

**Shot 8b (85.69–92.31 s) – what Query Profile gives you:**
"Same style and palette, plus Hot Orange-Red #FF5A36. A glass SQL query card flows into the node graph, which lights up step by step to show how the query executed. Then one node glows Orange-Red and a soft marker points to it as the bottleneck. Clean and calm. No readable text, no logos."
Motion: 86.06–87.04 s the card flows in on "Query Profile helps us"; 87.04–89.93 s the graph lights step by step on "understand how Snowflake executes our SQL query" (executes 88.42 s); ≈90.9–92.10 s one node glows and the marker appears on "where performance bottlenecks exist" (bottlenecks 91.02 s). **Effect: Liquid glass** — the recap line sits on a glass panel.
Overlay (post): "QUERY PROFILE" at 86.06 s; "HOW YOUR SQL QUERY EXECUTES" from 87.04 s; "WHERE THE BOTTLENECKS ARE" from 90.32 s.

**Audio sync:** graph lights at 87.04 s; bottleneck marker at ≈91.0 s.
**Negative prompt:** "Readable text, numbers, real UI screenshots, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (92.31–101.28 s · 8.97 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Fifteen! Next video lo Snowflake Query Optimization Techniques gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 15 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (92.31–95.60 s) – Day 15 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first fifteen lit in Cool Cyan (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 15" from ≈92.8 s; the fifteenth node lights at 94.8 s on "Fifteen".

**Shot 9b (95.60–101.28 s) – teaser:**
"Same style and palette. A teaser panel slides in with a node graph whose Orange-Red nodes cool one by one to Yellow and Cyan, with a small glass wrench glint passing over them. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: QUERY OPTIMIZATION TECHNIQUES" from ≈97.2 s; "REAL-TIME EXAMPLES" from ≈99.0 s. The visual only suggests nodes getting cooler. Do not show specific techniques or numbers.

**Audio sync:** card at ≈92.8 s; the fifteenth node at 94.8 s; teaser title at ≈97.2 s; "REAL-TIME EXAMPLES" at ≈99.0 s.
**Negative prompt:** "Specific optimisation techniques, improvement numbers, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (101.28–112.51 s · 11.23 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (101.28–107.13 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Node Slate #8FA3B8, text #F6F4F2. A calm, clean background with a soft cyan glow, a small Slate node graph drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈102.0 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈104.4 s, emphasised at ≈106.2 s on "Follow" (estimated).

**Shot 10b (107.13–110.47 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Cyan and Yellow glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 107.33 s, emphasised at ≈109.5 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (110.47–112.51 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 110.65 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 15. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #120D10, Cool Cyan #2FD6E8, Warm Yellow #FFD23F, Hot Orange-Red #FF5A36, Node Slate #8FA3B8, text #F6F4F2, secondary text #A99FA3. Colour code: Query Profile is a graph of connected rounded Node Slate glass boxes (operators), each with a small glowing bar that shows its share of time: Cool Cyan = small, Warm Yellow = medium, Hot Orange-Red = large (the bottleneck). A SQL query is a glass card with abstract lines; a table is a white glass block with rows of small cells. Never show real Snowflake UI screenshots, real statistics, percentages or improvement numbers; the only number allowed is '10 MINUTES'. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–14: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause; Whisper word times are used for emphasis words only. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day15.mp3` (112.51 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text overlays in the editor (titles, badges, table names, "10 MINUTES", and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (soft node clicks, a scan whoosh, a stopwatch tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at "10 minutes" (9.65 s), at the three suspects (14.65, 15.59, 16.89 s), at the title (24.21 s), at each numbered badge (41.28, 45.65, 51.53, 57.14 s), at the banking joins and the Query Profile (≈67.4, 72.60 s), at the bottleneck (≈78.5 s, ≈91.0 s), at the final tagline (110.65 s), and at the Follow and Contact lines (≈106.2, ≈109.5 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Query Profile shows, in a graphical form, how a SQL query was executed; it lets you analyse the execution steps; the main operations to observe are Table Scan (how much data was scanned), Join Operations (where a join has a performance issue), Aggregation (how GROUP BY and aggregation operations executed) and Execution Time (where most time was spent); in the banking example the profile is used to find unnecessary data scanning or expensive operations so that the query can be optimised. **No real operator statistics, percentages or improvement numbers** are shown, because the script gives none.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
