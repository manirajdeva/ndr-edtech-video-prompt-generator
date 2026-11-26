# Thirty Days of Snowflake – Day 16: Snowflake Query Optimization Techniques
Video prompt package (NDR EdTech) — `Audio\Day16.mp3` + `days-scripts\day16.txt`, analysed with Whisper

> **Timing status: MEASURED from Day16.mp3 (143.96 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times and helped place words inside phrases. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's** for the Telugu-English part; only the times come from the audio.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **The audio's ending is different from the script (important).** The script ends with "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!". The audio from **113.23 s** instead has an English outro: "Are you interested in learning data engineering too? But are you facing difficulties in understanding concepts? Don't worry! Now, learn complex data engineering concepts easily in Telugu. For technical updates, industry insights, and career tips, follow the NDR EdTech Instagram page… Contact us for complete course details. Start your career growth journey right now. NDR EdTech. Learn, Build, Grow." **The audio is the master, so Scene 10 follows the audio.** The overlays say "LEARN · BUILD · GROW", not "Let's Learn and Grow Together!". If you want the script's ending instead, the audio needs to be re-recorded.
> 2. **Around 133–135 s** Whisper heard "Follow up with your questions", which is uncertain. The pauses show one phrase ending at 134.16 s and a new one starting at 134.52 s ("Contact us for complete course details"). The "follow" overlay is placed on "NDR EdTech Instagram page" (≈132 s).
> 3. **The "15 minutes → 30 seconds" story** is your scripted "imagine" example, so the on-screen numbers are labelled as an example, not a measured result.
> 4. **There is no scripted `[pause]`** in this script. The longest pause is 0.5 s.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 16: Snowflake Query Optimization Techniques |
| Duration | **143.96 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 4,319 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\Day16.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (32 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Carbon Turbo" (new for Day 16)
| Role | HEX | Use |
|---|---|---|
| Background | `#0E1012` | Base, gradients (carbon black) |
| Turbo Lime | `#C6F135` | Optimised, fast, the columns and rows you need, the result |
| Heavy Amber | `#FFB020` | Slow or heavy work, unnecessary scanning |
| Query Ice | `#BFD7FF` | SQL query glass, code panels, neutral highlights |
| Skipped Slate | `#5A6472` | Data that is not needed (dimmed, filtered out, skipped) |
| Primary text | `#F4F6F8` | Titles, labels |
| Secondary text | `#98A1AD` | Captions |

**Colour code (use in every scene):** Slow / heavy = Amber · Fast / optimised = Lime · SQL = Ice · Not needed = dim Slate. A **table** is a white glass block drawn with vertical column strips and rows of small cells.

**The core visual rule (technical accuracy):** every technique is shown as **"do less work"**: read fewer columns (SELECT with required columns), read fewer rows (WHERE), scan fewer micro-partitions (pruning), join only what is needed on the correct keys, and find the slow part with Query Profile. Show abstract shapes only, no real statistics or percentages. The only numbers on screen are the script's "15 MINUTES", "30 SECONDS" and "10 CRORE", and they are labelled as the story's example.

### Motion effects used (from the skill's effects library)
Comment drop, Day dial, Blade slice, Letter dive, Impact frame, Liquid glass, Head stack, Press font, Live cursor, Code body, Rack focus. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–4.21 | "Hello guys! Andaru ela unnaru?" (0.00–2.19) · "Oka interesting situation!" (2.53–4.00) | Funny, curious | Title hook |
| 2 | 4.21–16.14 | "Meeru oka SQL query execute chesaru…" (4.41–6.79) · "kani result ravadaniki 15 minutes paduthundhi!" (7.14–10.01) · "Ade query ni optimize chesaka just 30 seconds lo result vachindhi anukondi!" (10.45–14.78) · "Amazing kada?" (15.14–15.92) | Playful, surprised | 15 minutes versus 30 seconds |
| 3 | 16.14–22.14 | "Mari Snowflake lo SQL queries ni fast ga execute cheyyadaniki em techniques follow avvali?" (16.36–21.95) | Curious | The question |
| 4 | 22.14–25.44 | "Let's understand!" (22.33–22.99) · "Welcome to NDR EdTech!" (23.49–25.21) | Welcoming | Title and brand welcome |
| 5 | 25.44–33.38 | "Snowflake lo Query Optimization ante SQL queries performance improve cheyyadam." (25.66–30.52) · "Main ga five important techniques chuddam." (30.92–33.12) | Clear | Definition, five techniques |
| 6 | 33.38–64.52 | "First, SELECT * avoid cheyyandi. Required columns matrame select cheyyandi." (33.63–38.24) · "Second, WHERE conditions use cheyyandi. Unnecessary data ni filter cheyyandi." (38.70–43.23) · "Third, Partition Pruning improve cheyyandi. Filter conditions valla unnecessary micro-partitions scan avvakunda chudandi." (43.70–50.79) · "Fourth, JOIN conditions optimize cheyyandi. Correct join keys use cheyyandi and unnecessary joins avoid cheyyandi." (51.27–58.05) · "Fifth, Query Profile analyze cheyyandi. Query ekkada ekkuva time teesukuntundho identify cheyyandi." (58.55–64.27) | Clear, structured | Five numbered techniques |
| 7 | 64.52–93.53 | "Oka Banking project example teesukundham." (64.76–66.76) · "Mana TRANSACTIONS table lo 10 crore records unnayi." (67.14–70.02) · "Reporting kosam SELECT * use chesthe unnecessary columns kuda scan avvachu." (70.40–75.01) · "Instead, required columns and date filter use cheddham." (75.42–78.53) · "SELECT CUSTOMER_ID, TRANSACTION_AMOUNT FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18';" (78.90–88.42) · "Ila required columns and filters use cheyyadam valla query performance improve avvachu." (88.81–93.32) | Storytelling | Banking: SELECT * versus required columns and a date filter |
| 8 | 93.53–104.20 | "So, simple ga gurthupettukondi!" (93.74–95.66) · "Good SQL writing," (96.01–97.29) · "efficient filtering," (97.52–98.48) · "proper JOINs and Query Profile analysis are important for Snowflake performance optimization." (98.74–104.02) | Confident | Four-point recap |
| 9 | 104.20–113.03 | "Idi mana Thirty Days of Snowflake series lo Day Sixteen!" (104.37–107.59) · "Next video lo Partition Pruning gurinchi detailed real-time example tho explain chesthanu." (107.95–112.82) | Upbeat | Day 16 card, Partition Pruning teaser |
| 10 | 113.03–143.96 | **(audio outro, not in the script)** "Are you interested in learning data engineering too?" (113.23–116.49) · "But are you facing difficulties in understanding concepts?" (116.90–120.45) · "Don't worry!" (120.81–121.46) · "Now, learn complex data engineering concepts easily in Telugu." (121.85–126.75) · "For technical updates, industry insights, and career tips, follow the NDR EdTech Instagram page." (127.12–134.16) · "Contact us for complete course details." (134.52–137.23) · "Start your career growth journey right now." (137.62–140.17) · "NDR EdTech." (140.57–141.60) · "Learn, Build, Grow." (141.95–143.59) | Warm, motivating, closing | Question, reassurance, follow, contact, career, tagline |

Silences longer than 0.2 s (safe cut points): 0.90–1.16, 2.19–2.53, 4.00–4.41, 6.79–7.14, 10.01–10.45, 14.78–15.14, 15.92–16.36, 21.95–22.33, 22.99–23.49, 25.21–25.66, 28.01–28.30, 30.52–30.92, 33.12–33.63, 33.96–34.20, 35.77–36.18, 38.24–38.70, 39.13–39.48, 40.97–41.37, 43.23–43.70, 43.98–44.32, 46.00–46.43, 50.79–51.27, 51.63–51.91, 53.74–54.12, 55.75–55.96, 58.05–58.55, 58.88–59.16, 60.82–61.20, 64.27–64.76, 66.76–67.14, 70.02–70.40, 75.01–75.42, 75.78–76.08, 78.53–78.90, 80.81–81.11, 82.68–83.02, 84.07–84.31, 88.42–88.81, 91.51–91.73, 93.32–93.74, 95.66–96.01, 97.29–97.52, 98.48–98.74, 104.02–104.37, 107.59–107.95, 112.82–113.23, 116.49–116.90, 120.45–120.81, 121.46–121.85, 126.75–127.12, 134.16–134.52, 137.23–137.62, 140.17–140.57, 141.60–141.95, 142.30–142.59, 142.94–143.21, 143.59–143.96.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Oka interesting situation! | interesting ≈2.8 · situation ≈3.4 |
| Meeru oka SQL query execute chesaru… | SQL query ≈5.0 · execute ≈5.8 |
| kani result ravadaniki 15 minutes paduthundhi! | result ≈7.4 · **15 minutes** ≈8.6–9.3 · paduthundhi ≈9.6 |
| Ade query ni optimize chesaka just 30 seconds lo result vachindhi anukondi! | optimize ≈11.0 · **30 seconds** ≈12.5–13.5 · result vachindhi ≈13.8 |
| Amazing kada? | Amazing 15.14 |
| Mari Snowflake lo SQL queries ni fast ga execute cheyyadaniki em techniques follow avvali? | fast ga ≈18.3 · techniques ≈20.0 · follow avvali ≈21.0 |
| Let's understand! | Let's 22.33 · understand 22.5 |
| Welcome to NDR EdTech! | Welcome 23.49 · NDR ≈24.2 · EdTech ≈24.7 |
| Snowflake lo Query Optimization ante SQL queries performance improve cheyyadam. | Query Optimization ≈26.5–27.6 · performance improve ≈28.8–29.8 |
| Main ga five important techniques chuddam. | five ≈31.4 · techniques ≈32.2 |
| First, SELECT * avoid cheyyandi. | First 33.63 · SELECT * 34.20 · avoid ≈35.0 |
| Required columns matrame select cheyyandi. | Required columns 36.18 · select ≈37.2 |
| Second, WHERE conditions use cheyyandi. | Second 38.70 · WHERE 39.48 · use ≈40.3 |
| Unnecessary data ni filter cheyyandi. | Unnecessary data 41.37 · filter ≈42.3 |
| Third, Partition Pruning improve cheyyandi. | Third 43.70 · Partition Pruning 44.32 |
| Filter conditions valla unnecessary micro-partitions scan avvakunda chudandi. | Filter conditions 46.43 · unnecessary micro-partitions ≈48.0–49.2 · scan avvakunda ≈49.6 |
| Fourth, JOIN conditions optimize cheyyandi. | Fourth 51.27 · JOIN 51.91 · optimize ≈52.9 |
| Correct join keys use cheyyandi and unnecessary joins avoid cheyyandi. | Correct join keys 54.12–55.0 · unnecessary joins ≈56.4 · avoid ≈57.3 |
| Fifth, Query Profile analyze cheyyandi. | Fifth 58.55 · Query Profile 59.16 · analyze ≈60.2 |
| Query ekkada ekkuva time teesukuntundho identify cheyyandi. | ekkuva time ≈62.0 · identify ≈63.4 |
| Oka Banking project example teesukundham. | Banking ≈65.0 · example ≈66.0 |
| Mana TRANSACTIONS table lo 10 crore records unnayi. | TRANSACTIONS ≈67.5 · **10 crore** ≈68.6–69.2 |
| Reporting kosam SELECT * use chesthe unnecessary columns kuda scan avvachu. | SELECT * ≈71.8 · unnecessary columns ≈73.0 · scan ≈74.2 |
| Instead, required columns and date filter use cheddham. | Instead 75.42 · required columns ≈76.4 · date filter ≈77.4 |
| SELECT CUSTOMER_ID, TRANSACTION_AMOUNT | SELECT CUSTOMER_ID 78.90–80.81 · TRANSACTION_AMOUNT 81.11–82.68 |
| FROM TRANSACTIONS | FROM TRANSACTIONS 83.02–84.07 |
| WHERE TRANSACTION_DATE = '2026-11-18'; | WHERE 84.31 · TRANSACTION_DATE ≈85.0–86.0 · '2026-11-18' ≈86.4–88.3 |
| Ila required columns and filters use cheyyadam valla query performance improve avvachu. | required columns ≈89.4 · filters ≈90.3 · performance improve ≈92.0 |
| So, simple ga gurthupettukondi! | So 93.74 · gurthupettukondi ≈94.6 |
| Good SQL writing, efficient filtering, proper JOINs and Query Profile analysis are important for Snowflake performance optimization. | Good SQL writing 96.01 · efficient filtering 97.52 · proper JOINs 98.74 · Query Profile analysis ≈100.5 · performance optimization ≈102.5 |
| Idi mana Thirty Days of Snowflake series lo Day Sixteen! | Thirty ≈105.0 · Snowflake ≈105.8 · Day ≈106.6 · Sixteen ≈107.0 |
| Next video lo Partition Pruning gurinchi detailed real-time example tho explain chesthanu. | Partition Pruning ≈108.7–109.5 · detailed real-time example ≈110.0–111.5 |
| Are you interested in learning data engineering too? | Are you 113.23 · data engineering ≈114.5 |
| But are you facing difficulties in understanding concepts? | difficulties ≈118.0 · concepts ≈119.8 |
| Don't worry! | Don't worry 120.81 |
| Now, learn complex data engineering concepts easily in Telugu. | learn 121.85 · complex ≈122.6 · easily ≈124.6 · Telugu ≈125.8 |
| For technical updates, industry insights, and career tips, follow the NDR EdTech Instagram page. | technical updates ≈127.5 · industry insights ≈128.6 · career tips ≈130.0 · **follow** ≈130.9 · NDR EdTech Instagram page ≈131.5–134.0 |
| Contact us for complete course details. | Contact 134.52 · complete course details ≈135.6 |
| Start your career growth journey right now. | Start 137.62 · career growth ≈138.5 · right now ≈139.6 |
| NDR EdTech. | NDR 140.57 · EdTech ≈141.0 |
| Learn, Build, Grow. | Learn 141.95 · Build 142.59 · Grow 143.21 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, Skipped Slate #5A6472, text #F4F6F8.*

**Object look (keep identical in every scene):** a **SQL query** = an Ice glass card with abstract lines. A **table** = a white glass block drawn with vertical column strips and rows of small cells. **Needed** columns, rows and tiles = lit Lime. **Heavy / unnecessary work** = Amber. **Not needed** = dim Slate (still visible, never deleted).

### Scene 1 – Hook (0.00–4.21 s · 4.21 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka interesting situation!"
**Tone:** funny, curious.
**Visual objective:** Welcome viewers and tease the situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, Skipped Slate #5A6472, text #F4F6F8. A carbon-black space with soft lime light and drifting glass particles. A glowing Ice glass SQL query card (abstract lines, no readable text) floats at the upper-centre with a small glass stopwatch ring beside it, half Amber and half Lime. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–2.19 s: particles drift in and the card appears on "Hello guys! Andaru ela unnaru?".
- 2.53–4.00 s: the stopwatch ring spins up on "Oka interesting situation!" (interesting ≈2.8 s).
- 4.00–4.21 s: soft light sweep into Scene 2.
- Effect: **Comment drop** — a small "?" glass bubble drops in beside the card at ≈2.8 s.
**Audio sync:** title lands at ≈1.2 s; the sweep completes in the pause at 4.00–4.41 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 16".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – 15 minutes versus 30 seconds (4.21–16.14 s · 11.93 s)
**Voice-over:** "Meeru oka SQL query execute chesaru… kani result ravadaniki 15 minutes paduthundhi! Ade query ni optimize chesaka just 30 seconds lo result vachindhi anukondi! Amazing kada?"
**Tone:** playful, surprised.
**Visual objective:** The same query takes 15 minutes, and after optimisation an imagined 30 seconds.
Generate as **three shots (2a–2c)**.

**Shot 2a (4.21–6.97 s) – run the query:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, text #F4F6F8. An Ice glass SQL query card (abstract lines) slides into a glass warehouse panel (a snowflake-crystal glyph, no logo) and a cursor presses a glowing run button. A soft Ice pulse starts. Calm, clean, phone-readable. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.41–5.0 s the card slides in on "Meeru oka SQL query"; ≈5.8–6.79 s the cursor presses run on "execute chesaru…". **Effect: Live cursor.**
Overlay (post): "SQL QUERY" from ≈5.0 s.

**Shot 2b (6.97–10.23 s) – 15 minutes:**
"Same style and palette. A very slow Amber progress bar crawls under the query card while a large glass stopwatch ring (no numerals) turns slowly and glows Amber. Tense, heavy feeling. No readable text, no logos, no watermark."
Motion: 7.14–8.6 s the bar crawls on "kani result ravadaniki"; ≈8.6–10.01 s the ring turns on "15 minutes paduthundhi!". **Effect: Day dial.**
Overlay (post): "15 MINUTES" at ≈8.6 s.

**Shot 2c (10.23–16.14 s) – after optimising: 30 seconds:**
"Same style and palette. A soft Lime pulse sweeps over the query card (it is optimised), the bar fills quickly and the stopwatch ring turns Lime and snaps to a short arc. A glass result-table (white glass, no readable data) appears with a bright Lime glow, and a small amazed sparkle bursts. Clean, satisfying. No readable text, no logos, no watermark."
Motion: 10.45–12.3 s the Lime pulse passes over the card on "Ade query ni optimize chesaka"; ≈12.5–14.78 s the ring snaps to a short Lime arc and the result appears on "just 30 seconds lo result vachindhi anukondi!"; 15.14–15.92 s a sparkle bursts on "Amazing kada?". **Effect: Blade slice** — a thin line slices the screen into the slow (Amber) half and the fast (Lime) half at ≈12.4 s.
Overlay (post): "OPTIMIZED" at 10.45 s; "30 SECONDS" at ≈12.5 s; small caption "EXAMPLE" under both numbers.

**Audio sync:** "15 MINUTES" at ≈8.6 s; slice at ≈12.4 s; "30 SECONDS" at ≈12.5 s.
**Negative prompt (all shots):** "Presenting the numbers as measured results, readable text, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Which techniques? (16.14–22.14 s · 6.00 s)
**Voice-over:** "Mari Snowflake lo SQL queries ni fast ga execute cheyyadaniki em techniques follow avvali?"
**Tone:** curious.
**Visual objective:** Pose the question.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, text #F4F6F8. The result table and stopwatch from the last shot fade back and five small closed glass 'technique' cards rise in a loose fan, each with a soft question-mark glow, around an Ice query card at the centre. Calm, curious feeling. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 16.36–18.3 s: the query card glows on "Mari Snowflake lo SQL queries ni".
- ≈18.3–20.0 s: the Lime speed streak crosses the card on "fast ga execute cheyyadaniki".
- ≈20.0–21.95 s: the five cards rise and glow on "em techniques follow avvali?".
**Audio sync:** speed streak at ≈18.3 s; cards at ≈20.0 s.
**On-screen text (overlay, post):** "HOW TO RUN SQL QUERIES FASTER?" from 16.36 s.
**Negative prompt:** "Readable text, an answer shown too early, clutter, flicker, off-palette colours, human faces, watermark."

---

### Scene 4 – Title and welcome (22.14–25.44 s · 3.30 s)
**Voice-over:** "Let's understand! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Name the topic and welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Query Ice #BFD7FF, text #F4F6F8. A glowing glass snowflake-crystal emblem rises at the upper-centre with a soft lime bloom, and a thin Lime speed-streak circles it once. A reserved clean area at the top for the logo, and clean space for a title. Slow push-in, soft volumetric light. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 22.33–22.99 s: the emblem rises and the title lands on "Let's understand!". **Effect: Letter dive** — the letters settle fully before 22.9 s.
- 23.49–25.21 s: a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** title at 22.33 s; logo and panel at 23.49 s; "NDR" at ≈24.2 s.
**On-screen text (overlay, post):** "QUERY OPTIMIZATION TECHNIQUES" at 22.33 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 23.49 s.
**Negative prompt:** "Fake logos, distorted logo, misspelled title, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – What is query optimisation? (25.44–33.38 s · 7.94 s)
**Voice-over:** "Snowflake lo Query Optimization ante SQL queries performance improve cheyyadam. Main ga five important techniques chuddam."
**Tone:** clear.
**Visual objective:** Query optimisation means improving the performance of SQL queries, and there are five techniques.
Generate as **two shots (5a, 5b)**.

**Shot 5a (25.44–30.72 s) – improve performance:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, text #F4F6F8. An Ice glass SQL query card sits between two gauges: on the left a heavy Amber gauge-arc, on the right a bright Lime gauge-arc (no numbers). A Lime glow sweeps from the card, the arc on the left shrinks and the arc on the right grows. Calm, clear, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 25.66–28.01 s the card and gauges appear on "Snowflake lo Query Optimization ante"; 28.30–30.52 s the arcs shift on "SQL queries performance improve cheyyadam" (performance improve ≈28.8–29.8 s).
Overlay (post): "QUERY OPTIMIZATION" at ≈26.5 s; "IMPROVE SQL QUERY PERFORMANCE" from ≈28.8 s.

**Shot 5b (30.72–33.38 s) – five techniques:**
"Same style and palette. Five numbered glass tiles (1 to 5) rise one by one in a neat vertical stack, each with a small abstract icon (columns, a funnel, honeycomb tiles, two linked blocks, a node graph). Clean, uncluttered, phone-readable layout. No readable fine text, no logos, no watermark."
Motion: 30.92–31.4 s the first tiles rise on "Main ga"; ≈31.4–33.12 s the stack completes on "five important techniques chuddam". **Effect: Head stack.**
Overlay (post): "5 TECHNIQUES" from ≈31.4 s.

**Audio sync:** arcs shift at ≈28.8 s; stack at ≈31.4 s.
**Negative prompt:** "Real gauges with numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – The five techniques (33.38–64.52 s · 31.14 s)
**Voice-over:** "First, SELECT * avoid cheyyandi. Required columns matrame select cheyyandi. Second, WHERE conditions use cheyyandi. Unnecessary data ni filter cheyyandi. Third, Partition Pruning improve cheyyandi. Filter conditions valla unnecessary micro-partitions scan avvakunda chudandi. Fourth, JOIN conditions optimize cheyyandi. Correct join keys use cheyyandi and unnecessary joins avoid cheyyandi. Fifth, Query Profile analyze cheyyandi. Query ekkada ekkuva time teesukuntundho identify cheyyandi."
**Tone:** clear, structured.
**Visual objective:** One shot per technique, each showing "do less work".
Generate as **five shots (6a–6e)**. Keep the numbered-badge position and the table style identical so the list reads as one sequence.

**Shot 6a (33.38–38.47 s) – 1 · avoid SELECT *, select required columns:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Skipped Slate #5A6472, text #F4F6F8. A wide white glass table drawn with eight vertical column strips fills the frame. First every column glows Amber (everything is read, heavy). Then only two columns turn Lime and the other six dim to Skipped Slate. A numbered badge '1'. Calm, clear, phone-readable. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 33.63–34.2 s the badge appears on "First,"; 34.20–35.77 s all columns glow Amber on "SELECT * avoid cheyyandi" (**Effect: Press font** — "SELECT *" presses in at 34.2 s with a soft cross); 36.18–38.24 s two columns turn Lime and the rest dim on "Required columns matrame select cheyyandi".
Overlay (post): "1 · AVOID SELECT *" at 33.63 s; "SELECT ONLY REQUIRED COLUMNS" from 36.18 s.

**Shot 6b (38.47–43.47 s) – 2 · WHERE conditions:**
"Same style and palette. A glass funnel (filter) sits above the table. Rows pour through it: the rows that are needed pass and glow Lime, the unneeded rows dim to Skipped Slate and slide aside (still visible, not deleted). A numbered badge '2'. No readable text, no logos, no watermark."
Motion: 38.70–39.48 s the badge appears on "Second,"; 39.48–40.97 s the funnel glows on "WHERE conditions use cheyyandi"; 41.37–43.23 s the rows are filtered on "Unnecessary data ni filter cheyyandi" (filter ≈42.3 s).
Overlay (post): "2 · USE WHERE CONDITIONS" at 38.70 s; "FILTER UNNECESSARY DATA" from 41.37 s.

**Shot 6c (43.47–51.03 s) – 3 · improve Partition Pruning:**
"Same style and palette. The table splits into a honeycomb of small rounded-hexagon tiles with thin Ice metadata strips. A filter beam passes over: a few tiles light Lime (scanned) while the others dim to Skipped Slate and stay in place (skipped, not deleted). A numbered badge '3'. No readable text, no logos, no watermark."
Motion: 43.70–44.32 s the badge appears on "Third,"; 44.32–46.0 s the table splits into tiles on "Partition Pruning improve cheyyandi"; 46.43–48.0 s the filter beam passes on "Filter conditions valla"; ≈48.0–50.79 s most tiles dim on "unnecessary micro-partitions scan avvakunda chudandi" (micro-partitions ≈48.0 s, scan avvakunda ≈49.6 s).
Overlay (post): "3 · IMPROVE PARTITION PRUNING" at 43.70 s; "SKIP UNNECESSARY MICRO-PARTITIONS" from ≈48.0 s.

**Shot 6d (51.03–58.30 s) – 4 · optimise JOIN conditions:**
"Same style and palette. Two white glass tables sit side by side. A thin Lime link joins one key column in the left table to the matching key column in the right table, and rows connect along it neatly. A third, unneeded table block slides in and is gently pushed away and dimmed to Skipped Slate. A numbered badge '4'. No readable text, no logos, no watermark."
Motion: 51.27–51.91 s the badge appears on "Fourth,"; 51.91–53.74 s the two tables appear on "JOIN conditions optimize cheyyandi"; 54.12–55.75 s the Lime key link draws on "Correct join keys use cheyyandi" (Correct join keys 54.12–55.0 s); ≈56.4–58.05 s the extra table is pushed away on "unnecessary joins avoid cheyyandi".
Overlay (post): "4 · OPTIMIZE JOIN CONDITIONS" at 51.27 s; "CORRECT JOIN KEYS" at 54.12 s; "AVOID UNNECESSARY JOINS" at ≈56.4 s.

**Shot 6e (58.30–64.52 s) – 5 · analyse Query Profile:**
"Same style and palette. A node graph of six rounded Slate glass boxes with small glowing bars (Lime small, Amber large) fills the frame. A magnifier passes over it and settles on the one box with the largest Amber bar. A numbered badge '5'. No readable text, no logos, no watermark."
Motion: 58.55–58.88 s the badge appears on "Fifth,"; 59.16–60.82 s the graph appears on "Query Profile analyze cheyyandi"; ≈62.0–64.27 s the magnifier settles on the Amber box on "Query ekkada ekkuva time teesukuntundho identify cheyyandi" (ekkuva time ≈62.0 s). **Effect: Rack focus** — focus pulls to the largest box at ≈62.0 s.
Overlay (post): "5 · ANALYZE QUERY PROFILE" at 58.55 s; "FIND WHERE THE MOST TIME GOES" from ≈62.0 s.

**Audio sync:** badge 1 at 33.63 s; badge 2 at 38.70 s; badge 3 at 43.70 s; badge 4 at 51.27 s; badge 5 at 58.55 s.
**Negative prompt (all shots):** "Real statistics, percentages, readable text, filtered or skipped data shown as deleted, specific query plans, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (64.52–93.53 s · 29.01 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS table lo 10 crore records unnayi. Reporting kosam SELECT * use chesthe unnecessary columns kuda scan avvachu. Instead, required columns and date filter use cheddham. SELECT CUSTOMER_ID, TRANSACTION_AMOUNT FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18'; Ila required columns and filters use cheyyadam valla query performance improve avvachu."
**Tone:** storytelling.
**Visual objective:** A 10 crore-row TRANSACTIONS table: SELECT * can scan unnecessary columns; selecting required columns and a date filter improves performance.
Generate as **seven shots (7a–7g)**. All shots use the same camera language and the same table layout so the story reads as one build.

**Shot 7a (64.52–66.95 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, text #F4F6F8. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in cool Ice, with an empty glass table frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈65.0 s.

**Shot 7b (66.95–70.21 s) – 10 crore records:**
"Same style and palette. The glass table frame fills with a vast, dense block of tiny glowing cells with eight column strips, stretching far into the distance. The camera pulls back slowly to show the scale. No readable fine text, no logos."
Overlay (post): "TRANSACTIONS" at ≈67.5 s (monospace); "10 CRORE RECORDS" at ≈68.6 s.

**Shot 7c (70.21–75.22 s) – SELECT * scans unnecessary columns:**
"Same style and palette. An Ice query card with a large star glyph (SELECT *) sends a wide scan beam across all eight columns, which all glow Amber. Several of the columns glow with a small warning dot to show they are not needed for the report. Heavy feeling. No readable text, no logos."
Motion: 70.40–71.8 s the card slides in on "Reporting kosam"; ≈71.8–73.0 s the wide beam sweeps all columns on "SELECT * use chesthe"; ≈73.0–75.01 s the unneeded columns pulse on "unnecessary columns kuda scan avvachu".
Overlay (post): "SELECT * → ALL COLUMNS SCANNED" from ≈71.8 s; "UNNECESSARY COLUMNS" at ≈73.0 s.

**Shot 7d (75.22–78.72 s) – instead: required columns and a date filter:**
"Same style and palette. The wide beam narrows. Two columns turn Lime while the other six dim to Skipped Slate. A small calendar-page glyph (no readable date) and a funnel glyph appear above the table. Calm, clear. No readable text, no logos."
Motion: 75.42–75.78 s the beam narrows on "Instead,"; ≈76.4–77.2 s the two columns turn Lime on "required columns"; ≈77.4–78.53 s the calendar and funnel appear on "date filter use cheddham".
Overlay (post): "REQUIRED COLUMNS + DATE FILTER" from ≈76.4 s.

**Shot 7e (78.72–84.19 s) – SQL: SELECT and FROM:**
"Same style and palette. A dark glass code editor panel (a clean window with three empty lines, no readable code) floats at the centre with a thin Ice edge and a blinking cursor. Behind it, softly out of focus, the table glows. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 78.90–80.81 s line 1 types on "SELECT CUSTOMER_ID,"; 81.11–82.68 s the second column name types on "TRANSACTION_AMOUNT"; 83.02–84.07 s line 2 types on "FROM TRANSACTIONS". **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
SELECT CUSTOMER_ID,
       TRANSACTION_AMOUNT
FROM TRANSACTIONS
```
"SELECT CUSTOMER_ID," at 78.90 s; "TRANSACTION_AMOUNT" at 81.11 s; "FROM TRANSACTIONS" at 83.02 s.

**Shot 7f (84.19–88.62 s) – SQL: WHERE:**
"Same style and palette. The code panel continues and a funnel glow appears at the end of the last line while the table's rows are filtered: only the rows for one date stay Lime. No readable code, no logos, no watermark."
Motion: 84.31–86.0 s the last line starts on "WHERE TRANSACTION_DATE"; ≈86.4–88.3 s the date value completes and the rows filter on "= '2026-11-18'". **Effect: Code body.**
Overlay (post, monospace; the full query shown at the end):
```sql
SELECT CUSTOMER_ID,
       TRANSACTION_AMOUNT
FROM TRANSACTIONS
WHERE TRANSACTION_DATE = '2026-11-18';
```
"WHERE TRANSACTION_DATE" at 84.31 s; "= '2026-11-18';" at ≈86.4 s.

**Shot 7g (88.62–93.53 s) – better performance:**
"Same style and palette. The result: a small Lime glass result-table appears with a bright glow, next to a faint ghost of the heavy Amber full scan. A soft gauge-arc (no numbers) on the Lime side fills more than the ghost's. Calm, satisfying. No readable text, no logos."
Motion: 88.81–91.51 s the result appears on "Ila required columns and filters use cheyyadam"; ≈92.0–93.32 s the gauge fills on "valla query performance improve avvachu". **Effect: Rack focus** — focus pulls from the ghost scan to the result at ≈89.4 s.
Overlay (post): "REQUIRED COLUMNS + FILTERS" from ≈89.4 s; "CAN IMPROVE QUERY PERFORMANCE" from ≈92.0 s. Show "can improve", with no numbers (the script says "improve avvachu").

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake numbers or dates in the generated video, performance numbers, guaranteed speed claims, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (93.53–104.20 s · 10.67 s)
**Voice-over:** "So, simple ga gurthupettukondi! Good SQL writing, efficient filtering, proper JOINs and Query Profile analysis are important for Snowflake performance optimization."
**Tone:** confident.
**Visual objective:** Four-point recap.
Generate as **three shots (8a–8c)**.

**Shot 8a (93.53–95.84 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Query Ice #BFD7FF, text #F4F6F8. A calm Ice query card glides to the centre with a soft lime bloom against the carbon background. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈94.0 s.

**Shot 8b (95.84–98.61 s) – good SQL writing and efficient filtering:**
"Same style and palette. Two glass cards rise one after another: the first shows a slim query card with only two Lime columns (good SQL writing), the second shows a funnel filtering rows (efficient filtering). Clean, uncluttered. No readable text, no logos."
Motion: 96.01–97.29 s the first card rises on "Good SQL writing,"; 97.52–98.48 s the second card rises on "efficient filtering,". **Effect: Head stack.**
Overlay (post): "GOOD SQL WRITING" at 96.01 s; "EFFICIENT FILTERING" at 97.52 s.

**Shot 8c (98.61–104.20 s) – proper JOINs and Query Profile:**
"Same style and palette. Two more glass cards rise: two tables joined by a single clean Lime key link (proper JOINs), then a node graph with one magnified Amber node (Query Profile analysis). A soft Lime bloom settles over all four cards, now in a neat stack. No readable text, no logos."
Motion: 98.74–100.2 s the join card rises on "proper JOINs"; ≈100.5–102.0 s the node-graph card rises on "Query Profile analysis"; ≈102.5–104.02 s the bloom settles on "important for Snowflake performance optimization". **Effect: Liquid glass** — the final line sits on a glass panel.
Overlay (post): "PROPER JOINS" at 98.74 s; "QUERY PROFILE ANALYSIS" at ≈100.5 s; "SNOWFLAKE PERFORMANCE OPTIMIZATION" from ≈102.5 s.

**Audio sync:** card 1 at 96.01 s; card 2 at 97.52 s; card 3 at 98.74 s; card 4 at ≈100.5 s.
**Negative prompt:** "Numbers, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (104.20–113.03 s · 8.83 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Sixteen! Next video lo Partition Pruning gurinchi detailed real-time example tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 16 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (104.20–107.77 s) – Day 16 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, text #F4F6F8. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first sixteen lit in Turbo Lime (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 16" from ≈105.0 s; the sixteenth node lights at ≈107.0 s on "Sixteen".

**Shot 9b (107.77–113.03 s) – teaser:**
"Same style and palette. A teaser panel slides in showing a neat honeycomb of small glass tiles; a Lime beam lights a few and the others dim to Slate. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: PARTITION PRUNING" from ≈108.7 s; "DETAILED REAL-TIME EXAMPLE" from ≈110.0 s. The visual only suggests skipping tiles. Do not show tile counts or sizes.

**Audio sync:** card at ≈105.0 s; the sixteenth node at ≈107.0 s; the teaser title at ≈108.7 s.
**Negative prompt:** "Tile counts or sizes, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Audio outro: learn data engineering in Telugu (113.03–143.96 s · 30.93 s)
**Voice-over (audio; not in the script):** "Are you interested in learning data engineering too? But are you facing difficulties in understanding concepts? Don't worry! Now, learn complex data engineering concepts easily in Telugu. For technical updates, industry insights, and career tips, follow the NDR EdTech Instagram page. Contact us for complete course details. Start your career growth journey right now. NDR EdTech. Learn, Build, Grow."
**Tone:** warm, motivating, closing.
**Visual objective:** A short branded outro: question, reassurance, benefit, follow, contact, career, tagline.
Generate as **seven shots (10a–10g)**. Use the Carbon Turbo palette throughout.

**Shot 10a (113.03–116.70 s) – interested in learning data engineering?:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E1012, Turbo Lime #C6F135, Query Ice #BFD7FF, text #F4F6F8. A calm carbon background with a soft lime glow. A glowing glass database cylinder and a small data-pipeline arrow fade in at the centre, with a soft question-mark glow above them. Generous empty space for text. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 113.23–115.0 s the cylinder and pipeline appear on "Are you interested in learning"; ≈114.5–116.49 s the question glow pulses on "data engineering too?".
Overlay (post): "INTERESTED IN LEARNING DATA ENGINEERING?" from 113.23 s.

**Shot 10b (116.70–120.63 s) – difficulties in understanding concepts:**
"Same style and palette, plus Heavy Amber #FFB020. The pipeline tangles into a knot of Amber lines, and a dim Slate cloud hovers above it, showing confusion about the concepts. No human faces. No text rendered, no logos, no watermark."
Motion: 116.90–118.0 s the pipeline tangles on "But are you facing"; ≈118.0–120.45 s the knot tightens on "difficulties in understanding concepts?" (difficulties ≈118.0 s).
Overlay (post): "DIFFICULTIES UNDERSTANDING CONCEPTS?" from 116.90 s.

**Shot 10c (120.63–126.93 s) – don't worry, learn easily in Telugu:**
"Same style and palette. A soft Lime light unties the tangled knot into a clean, straight pipeline of glowing glass nodes. A small glass speech-bubble with a simple 'Telugu' script glyph (no readable letters) glows beside it. Calm, reassuring. No text rendered, no logos, no watermark."
Motion: 120.81–121.46 s a Lime flash on "Don't worry!"; 121.85–124.6 s the knot untangles on "Now, learn complex data engineering concepts"; ≈124.6–126.75 s the speech-bubble glows on "easily in Telugu" (easily ≈124.6 s, Telugu ≈125.8 s).
Overlay (post): "DON'T WORRY!" at 120.81 s; "LEARN COMPLEX DATA ENGINEERING CONCEPTS EASILY IN TELUGU" from 121.85 s.

**Shot 10d (126.93–134.34 s) – follow for updates, insights and tips:**
"Same style and palette. Three glass cards rise one after another in a vertical stack (a bell for technical updates, a lightbulb for industry insights, a stair-step for career tips), then a generic glass profile-card with a plus glyph glows (follow). Clean, uncluttered, generous empty space. No real social-media logos, no text rendered, no watermark."
Motion: ≈127.5 s card 1 on "technical updates"; ≈128.6 s card 2 on "industry insights"; ≈130.0 s card 3 on "career tips"; ≈130.9–134.0 s the follow card glows on "follow the NDR EdTech Instagram page". **Effect: Head stack.**
Overlay (post): "TECHNICAL UPDATES" at ≈127.5 s; "INDUSTRY INSIGHTS" at ≈128.6 s; "CAREER TIPS" at ≈130.0 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈130.9 s.

**Shot 10e (134.34–137.43 s) – contact for course details:**
"Same style and palette. A calm background with a soft Ice and Lime glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR COMPLETE COURSE DETAILS" from 134.52 s, emphasised at 134.52 s on "Contact". **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10f (137.43–140.37 s) – start your career growth journey:**
"Same style and palette. A glowing Lime path of glass steps rises from the lower-left to the upper-right across the frame, each step lighting in turn, with a soft light at the top. Hopeful, forward-moving. No text rendered, no logos, no watermark."
Motion: 137.62–138.5 s the first steps light on "Start your career"; ≈138.5–139.6 s the path rises on "growth journey"; ≈139.6–140.17 s the top light blooms on "right now".
Overlay (post): "START YOUR CAREER GROWTH JOURNEY" from 137.62 s.

**Shot 10g (140.37–143.96 s) – end card: NDR EdTech, Learn · Build · Grow:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo at 140.57 s; "LEARN" at 141.95 s, "BUILD" at 142.59 s, "GROW" at 143.21 s, as three words appearing one after another. Hold the final frame for the last 0.35 s.

Contact details (phone, email, website) are not in the audio, so they are omitted. Add them to a split end card only if you want them.

**Audio sync:** follow card at ≈130.9 s; contact card at 134.52 s; the three tagline words at 141.95, 142.59 and 143.21 s.
**Negative prompt (all shots):** "Real social-media logos, fake handles beyond @NDREDTECH, invented phone numbers or URLs, human faces, readable letters, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 16. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #0E1012, Turbo Lime #C6F135, Heavy Amber #FFB020, Query Ice #BFD7FF, Skipped Slate #5A6472, text #F4F6F8, secondary text #98A1AD. Colour code: slow or heavy work = Amber; fast or optimised = Lime; SQL = Ice glass; data that is not needed = dim Slate (still visible, never deleted or blown away). A table is a white glass block drawn with vertical column strips and rows of small cells; needed columns, rows and tiles glow Lime. Every technique is shown as 'do less work': fewer columns, fewer rows, fewer micro-partitions scanned, only needed joins on the right keys, and Query Profile to find the slow node. Never show real statistics, percentages or performance numbers; the only numbers allowed are the story's '15 MINUTES', '30 SECONDS' and '10 CRORE', labelled as an example. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–15: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

**Note for this audio:** the last 30 seconds are spoken in English, so Whisper's transcript of the outro is reliable, and it is the evidence that the ending differs from the script.

## 6. Editing and synchronisation plan

1. Import `Day16.mp3` (143.96 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, "15 MINUTES", "30 SECONDS", "10 CRORE", the SQL code, and the outro lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Do not use real Instagram logos; use the generic glyphs.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (soft clicks, a speed whoosh, a stopwatch tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at "15 minutes" and "30 seconds" (≈8.6, ≈12.5 s), at the title (22.33 s), at each numbered badge (33.63, 38.70, 43.70, 51.27, 58.55 s), at the SQL lines (78.90, 81.11, 83.02, 84.31 s), at the recap cards (96.01, 97.52, 98.74 s), at the outro (113.23, 120.81, 121.85, 127.12, 134.52 s), and at the final tagline (141.95, 142.59, 143.21 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: query optimisation means improving SQL query performance; the five techniques are avoiding SELECT * and selecting required columns, using WHERE conditions to filter unnecessary data, improving Partition Pruning so that unnecessary micro-partitions are not scanned, optimising JOIN conditions with correct join keys and no unnecessary joins, and analysing Query Profile to find where the query takes the most time. In the banking example, SELECT * can scan unnecessary columns, and selecting required columns with a date filter can improve performance. **No performance numbers** are shown beyond the story's own example. `SELECT CUSTOMER_ID, TRANSACTION_AMOUNT FROM TRANSACTIONS WHERE TRANSACTION_DATE = '2026-11-18';` is valid Snowflake syntax.
- Filtered rows and skipped micro-partitions are dimmed and still present, never deleted, so "Blow away" is not used.
- **The outro follows the audio, not the script** (see the first note). `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
