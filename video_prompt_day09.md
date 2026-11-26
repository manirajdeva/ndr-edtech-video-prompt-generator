# Thirty Days of Snowflake – Day 9: Snowflake Data Types
Video prompt package (NDR EdTech) — script.txt + audio.mp3, analysed with Whisper

> **Timing status: MEASURED from audio.mp3 (112.27 s).**
> - Phrase and word times come from Whisper (faster-whisper, `small` model, run in English mode on Windows CPU) cross-checked against the silences in the audio. English words and code names are reliable. Telugu words were transcribed approximately, so **the wording below is your script's** and only the times come from Whisper.
> - Phrase starts taken from pauses are the most exact. Whisper word times can lag true speech by 0.1–0.3 s. Times marked **≈** are estimates inside continuous speech.
> - **Check by ear (67.96–69.38 s):** Whisper heard "Let's store customer name as the **number**", but your script says **VARCHAR**. Whisper also mistook VARCHAR for "watch" earlier (6.96 s), so this is probably a mishearing. If the audio really says NUMBER, either re-record that line or tell me and I will change the overlay.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 9: Snowflake Data Types |
| Duration | **112.27 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,368 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `audio.mp3` is the master track. No replacement narration. Optional subtle music, ducked under speech. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so longer scenes are split into shots. Hold the last frame or slow slightly in the edit if a clip comes out shorter. |

### Fresh palette – "Midnight Spectrum" (new for Day 9)
| Role | HEX | Use |
|---|---|---|
| Background | `#0E0A1F` | Base, gradients |
| Primary (Violet) | `#8B5CF6` | Brand glow, DATE / TIMESTAMP |
| Amber | `#FBBF24` | NUMBER, highlights |
| Lime | `#A3E635` | VARCHAR, "correct" states |
| Rose | `#FB7185` | BOOLEAN, wrong-choice warnings |
| Primary text | `#F8F7FF` | Titles, labels, VARIANT glass |
| Secondary text | `#A5A1C2` | Captions |

**Type colour code (use in every scene):** NUMBER = Amber · VARCHAR = Lime · DATE and TIMESTAMP = Violet · BOOLEAN = Rose · VARIANT = white glass with small glints of the other four colours.

### Motion effects used (from the skill's effects library)
Head stack (five-type list), Live cursor, Code body, Banknote, Day dial, Press font, Paper tear, Impact frame, Layer explode, Rack focus, Comment drop, Liquid glass. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.69 | "Hello guys! Andaru ela unnaru?" (0.20–2.08) · "Oka small question!" (2.54–3.44) | Funny, energetic | Title hook, question mark |
| 2 | 3.69–10.00 | "Mee age ni database lo store cheyyali ante" (3.94–6.57) · "VARCHAR use chesthara? Leda" (6.81–8.01) · "NUMBER use chesthara? 😂" (8.31–9.73) | Playful | Age typed as text vs number |
| 3 | 10.00–18.19 | "Alage date of birth ni NUMBER lo store chesthara?" (10.26–12.78) · *[scripted pause 12.78–14.23]* · "Correct data type select cheyyakapothe data processing lo problems ravachu!" (14.23–17.88) | Funny, then serious | Wrong type, then data problems |
| 4 | 18.19–30.20 | "Anduke ee roju Snowflake Data Types gurinchi simple ga understand cheskundham." (18.50–22.86) · "Welcome to NDR EdTech!" (23.37–25.00) · "Snowflake lo different types of data ni store cheyyadaniki different Data Types untayi." (25.66–29.93) | Warm, welcoming | Title, brand welcome, data-type overview |
| 5 | 30.20–37.07 | "First," (30.47–30.69) "NUMBER!" (31.09–31.42) · "Numbers, salary, account balance and transaction amounts store cheyyadaniki use chestham." (31.97–36.80) | Clear | NUMBER block with banknote examples |
| 6 | 37.07–44.32 | "Second," (37.35–37.80) "VARCHAR!" (38.12–38.55) · "Customer names, email addresses and city names lanti text data store cheyyadaniki use chestham." (39.14–44.09) | Clear | VARCHAR text strings |
| 7 | 44.32–53.22 | "Third," (44.55–44.90) "DATE and TIMESTAMP!" (45.26–46.18) · "Date of birth, transaction date and transaction timestamp lanti date and time information store cheyyadaniki use chestham." (46.75–52.97) | Clear | Calendar and clock |
| 8 | 53.22–57.70 | "Fourth," (53.46–53.70) "BOOLEAN!" (54.07–54.47) · "TRUE or FALSE values store cheyyadaniki use chestham." (54.93–57.43) | Crisp | Toggle switch |
| 9 | 57.70–63.05 | "Fifth," (57.98–58.18) "VARIANT!" (58.60–58.99) · "JSON lanti semi-structured data ni store cheyyadaniki use chestham." (59.50–62.77) | Clear | Nested JSON glass |
| 10 | 63.05–86.37 | "Oka Banking project example teesukundham." (63.32–65.19) · "CUSTOMER_ID ni NUMBER lo store chestham." (65.64–67.68) · "CUSTOMER_NAME ni VARCHAR lo store chestham." (68.10–70.31) · "DATE_OF_BIRTH ni DATE lo store chestham." (70.71–74.34) · "TRANSACTION_TIMESTAMP ni TIMESTAMP lo store chestham." (74.95–78.34) · "IS_ACTIVE ni BOOLEAN lo store chestham." (78.76–81.45) · "Customer API nunchi vachina JSON data ni VARIANT column lo store cheyyachu." (82.04–86.14) | Storytelling | Banking table builds column by column |
| 11 | 86.37–91.24 | "So, data ni store chesetappudu correct Data Type select cheyyadam chaala important." (86.59–90.99) | Confident | Recap of the five types |
| 12 | 91.24–112.27 | "Idi mana Thirty Days of Snowflake series lo Day Nine!" (91.48–94.29) · "Next video lo Permanent, Transient and Temporary Tables madhya differences real-time examples tho explain chesthanu." (94.69–100.94) · "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki" (101.32–104.10) "Instagram lo NDR EdTech ni Follow avvandi!" (104.30–106.76) · "Full course details kosam NDR EdTech ni Contact avvandi!" (107.20–110.14) · "Let's Learn and Grow Together!" (110.49–111.98) | Upbeat, closing | Series card, teaser, CTA, end card |

Silences longer than 0.3 s (safe cut points): 0.79, 2.08, 3.44, 6.57, 9.73–10.26, 12.78–14.23 (the scripted `[pause]`), 17.88–18.50, 22.86, 25.00, 29.93, 30.69, 31.42, 32.48, 33.32, 36.80, 37.80, 38.55, 39.92, 44.09, 44.90, 46.18, 47.39, 52.97, 53.70, 54.47, 57.43, 58.18, 58.99, 62.77, 65.19, 67.68, 70.31, 74.34, 77.01, 78.34, 81.45, 86.14, 86.88, 88.59, 90.99, 94.29, 95.48, 96.24, 100.94, 104.10, 106.76, 110.14, 111.98.

### Appendix A – Word-level times from Whisper
Words use your script's spelling. Time = Whisper word start in seconds. Add 0.1–0.3 s tolerance.

| Phrase | Word times (s) |
|---|---|
| Hello guys! Andaru ela unnaru? | Hello 0.2 · guys 0.4 · Andaru ela unnaru 1.1–2.0 |
| Oka small question! | small 2.6 · question 3.0 |
| Mee age ni database lo store cheyyali ante | store 4.0 · age 4.0 · database 4.9 |
| VARCHAR use chesthara? Leda | **VARCHAR** 6.9 · use chesthara 7.1 |
| NUMBER use chesthara? | **NUMBER** 8.6 |
| Alage date of birth ni NUMBER lo store chesthara? | date 10.7 · of 11.0 · birth 11.1 · **NUMBER** 11.7 |
| Correct data type select cheyyakapothe | Correct 14.2 · data 14.5 · type 14.7 |
| data processing lo problems ravachu | problems 16.1 · data processing 16.2–16.4 |
| Anduke ee roju Snowflake Data Types gurinchi simple ga understand cheskundham | Snowflake 19.9 · Data 20.3 · Types 20.6 · simple ga 21.6–21.8 |
| Welcome to NDR EdTech! | Welcome 23.3 · NDR 23.9 · EdTech 24.5 |
| Snowflake lo different types of data ni store cheyyadaniki different Data Types untayi | different 26.5 · types 26.8 · data 27.2 · Data Types ≈28.6–29.5 |
| First, NUMBER! | First 30.5 · **NUMBER** 31.1 |
| Numbers, salary, account balance and transaction amounts store… | salary 32.8 · account 33.5 · balance 33.8 · transaction 34.5 · amounts 34.9 |
| Second, VARCHAR! | Second 37.4 · **VARCHAR** 38.1 |
| Customer names, email addresses and city names lanti text data… | Customer names 39.1–39.4 · email 40.2 · addresses 40.4 · city 41.2 · names 41.5 · text 42.1 |
| Third, DATE and TIMESTAMP! | Third 44.5 · **DATE** 45.3 · **TIMESTAMP** 45.7 |
| Date of birth, transaction date and transaction timestamp lanti date and time information… | Date of birth 46.7–47.1 · transaction date 47.7–48.1 · transaction timestamp 48.8–49.2 · date and time information 50.3–51.1 |
| Fourth, BOOLEAN! | Fourth 53.5 · **BOOLEAN** 54.1 |
| TRUE or FALSE values store… | **TRUE** 54.9 · **FALSE** 55.4 |
| Fifth, VARIANT! | Fifth 58.0 · **VARIANT** 58.6 |
| JSON lanti semi-structured data ni store… | **JSON** 59.5 · semi-structured 60.3–60.5 · data 61.0 |
| Oka Banking project example teesukundham | banking 63.4 · project 63.8 · example 64.3 |
| CUSTOMER_ID ni NUMBER lo store chestham | CUSTOMER_ID 65.6–65.9 · **NUMBER** 66.7 |
| CUSTOMER_NAME ni VARCHAR lo store chestham | CUSTOMER_NAME 68.0–68.4 · **VARCHAR** ≈69.2 (check, see note at top) |
| DATE_OF_BIRTH ni DATE lo store chestham | DATE 70.7 · OF 71.9 · BIRTH 72.9 · **DATE** 73.6 |
| TRANSACTION_TIMESTAMP ni TIMESTAMP lo store chestham | TRANSACTION 74.95 · TIMESTAMP 76.2 · **TIMESTAMP** (type) ≈77.1 |
| IS_ACTIVE ni BOOLEAN lo store chestham | IS 78.7 · ACTIVE 79.6 · **BOOLEAN** 80.6 |
| Customer API nunchi vachina JSON data ni VARIANT column lo store cheyyachu | Customer API 82.1–82.4 · JSON 82.0 · **VARIANT** 84.6 · column 84.9 |
| So, data ni store chesetappudu correct Data Type select cheyyadam chaala important | So 86.6 · data 87.2 · store 87.7 · correct 88.8 · Data Type 89.0–89.2 |
| Idi mana Thirty Days of Snowflake series lo Day Nine! | Thirty 91.8 · Days 92.2 · Snowflake 92.6 · series 93.1 · Day 93.6 · Nine 93.9 |
| Next video lo Permanent, Transient and Temporary Tables… | Next 94.8 · video 94.9 · Permanent ≈95.8 · Transient 96.4 · Temporary 97.1 · Tables 97.5 · real-time 99.0–99.3 · examples 99.5 |
| Ilanti Data Engineering concepts Telugu lo nerchukovadaniki | Data 101.5 · Engineering 101.8 · concepts 102.2 · Telugu 102.9 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈104.3 · NDR ≈104.6 · EdTech ≈105.5 · **Follow** ≈105.8 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full 106.2 · course 106.8 · details 107.6 · NDR ≈108.5 · EdTech ≈108.9 · **Contact** ≈109.3 (estimated) |
| Let's Learn and Grow Together! | Let's 110.1 · Learn 110.7 · and 111.0 · Grow 111.3 · Together 111.6 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. If you change the palette, update the palette line in each. The common palette line used below is: *background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF.*

### Scene 1 – Hook (0.00–3.69 s · 3.69 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka small question!"
**Tone:** funny, high energy.
**Visual objective:** Welcome viewers and tease the question.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A deep indigo-black space with soft violet light and drifting glass data-cube particles. A large glowing glass question-mark made of small data blocks forms at the upper-centre and settles with a soft violet bloom. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."

**Motion instructions:**
- 0.20–2.08 s: particles drift in; the cubes begin to assemble on "Hello guys".
- 2.54–3.44 s: question-mark completes with a bloom pulse on "small question".
- 3.44–3.69 s: quick light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at 2.96 s on "question".

**Audio sync:** title overlay lands at ≈1.1 s on "Andaru"; light sweep completes in the pause at 3.44–3.94 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 9".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, watermark, subtitles."

---

### Scene 2 – Age as VARCHAR or NUMBER (3.69–10.00 s · 6.31 s)
**Voice-over:** "Mee age ni database lo store cheyyali ante VARCHAR use chesthara? Leda NUMBER use chesthara?"
**Tone:** playful.
**Visual objective:** Show the two options for storing an age.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A glass database column slot at the centre waiting for a value. A friendly glass 'age' tile (an abstract number card, no readable text) hovers above it. Two glass option cards slide in from left and right: the left card is Lime-edged and shows a text-string shape, the right card is Amber-edged and shows a digit shape. The age tile swings between them with a playful bounce. Clean space for two labels. Gentle parallax, soft rim lighting. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 3.94–6.57 s: the slot and age tile appear on "Mee age ni database lo store".
- 6.81–8.01 s: the Lime card slides in on "VARCHAR".
- 8.31–9.73 s: the Amber card slides in on "NUMBER"; the tile bounces between both.
- Effect: **Comment drop** — a small glass "?" bubble drops beside the tile at 8.6 s.

**Audio sync:** Lime card at 6.9 s ("VARCHAR"); Amber card at 8.6 s ("NUMBER").
**On-screen text (overlay):** "AGE = ?" / "VARCHAR" / "NUMBER".
**Negative prompt:** "Human faces, cartoon characters, cluttered UI, tiny text, flicker, off-palette colours, watermark."

---

### Scene 3 – Date of birth and the problem (10.00–18.19 s · 8.19 s)
**Voice-over:** "Alage date of birth ni NUMBER lo store chesthara? … Correct data type select cheyyakapothe data processing lo problems ravachu!"
**Tone:** funny, then serious.
**Visual objective:** Show a mismatched type, then the risk of problems.

Generate as **two shots (3a, 3b)**.

**Shot 3a (10.00–13.50 s) – date of birth as a number:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Rose #FB7185, text #F8F7FF. A glass calendar tile (abstract, no readable text) is squeezed into a rigid Amber number-shaped slot and visibly does not fit, with a small Rose warning glow. Playful wobble, soft glow, clean composition. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 10.26–12.78 s the calendar tile struggles to fit on "date of birth ni NUMBER lo store chesthara"; **Effect: Paper tear** — the Rose-edged wrong-fit scene tears away at 12.78–13.50 s (the scripted pause) to reveal the next shot.

**Shot 3b (13.50–18.19 s) – data problems:**
"Same style and palette as above. A neat glass data table with several rows begins to glitch: two rows jitter and shift out of alignment, and Rose warning marks appear next to them. The camera pushes in. A calm Lime check-line waits at the edge, hinting at the correct choice. Clean layout, no readable text, no logos, no watermark."
Motion: 14.23–16.1 s the table glitches on "correct data type select cheyyakapothe"; 16.1–17.88 s the Rose marks appear on "problems ravachu".

**Audio sync:** wrong-fit begins at 10.26 s; tear at 12.78 s; glitch at 14.23 s.
**On-screen text (overlay):** "DATE OF BIRTH → NUMBER?" / "WRONG DATA TYPE = PROBLEMS".
**Negative prompt:** "Specific false claims about errors, readable fake error messages, flicker, clutter, off-palette colours, watermark."

---

### Scene 4 – Today's topic, welcome and overview (18.19–30.20 s · 12.01 s)
**Voice-over:** "Anduke ee roju Snowflake Data Types gurinchi simple ga understand cheskundham. Welcome to NDR EdTech! Snowflake lo different types of data ni store cheyyadaniki different Data Types untayi."
**Tone:** warm, welcoming.
**Visual objective:** Name the topic, welcome viewers, tease the data types.

Generate as **three shots (4a–4c)**.

**Shot 4a (18.19–23.12 s) – topic card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A glowing glass snowflake-crystal emblem rises at the upper-centre with a soft violet bloom, surrounded by five small glass tiles in Amber, Lime, Violet, Rose and white glass that orbit it slowly. Clean space for a title. Soft volumetric light. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 18.50–22.86 s the tiles orbit and the emblem pulses; the title appears at 19.9 s on "Snowflake". **Effect: Orbit ring.**

**Shot 4b (23.12–25.33 s) – welcome:**
"Same style and palette. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft violet glow below it. Slow gentle light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "WELCOME TO NDR EDTECH" from 23.3 s. **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.

**Shot 4c (25.33–30.20 s) – the five types:**
"Same style and palette. Five glass tiles rise in a vertical stack, in Amber, Lime, Violet, Rose and white glass, each with an abstract icon (digits, text lines, calendar, switch, braces). They stack neatly one above the other. Clean, uncluttered, phone-readable layout with space for labels. No readable fine text, no logos, no watermark."
Motion: 26.46–29.93 s the tiles rise one by one on "different types of data … different Data Types". **Effect: Head stack.**

**Audio sync:** title at 19.9 s; welcome at 23.3 s; stack rises from 26.5 s.
**On-screen text (overlay):** "SNOWFLAKE DATA TYPES" / "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, tiny text, flicker, clutter, off-palette colours, watermark."

---

### Scene 5 – NUMBER (30.20–37.07 s · 6.87 s)
**Voice-over:** "First, NUMBER! Numbers, salary, account balance and transaction amounts store cheyyadaniki use chestham."
**Tone:** clear.
**Visual objective:** NUMBER stores numeric values.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, text #F8F7FF. A large glowing Amber glass block with a clean digit motif floats at the centre with a numbered badge '1'. Three smaller Amber glass cards drift in beside it, each a different banknote-style graphic: a salary slip shape, an account-balance card, and a transaction arrow. Soft rim lighting, slow push-in. Leave space for a title and caption. No readable amounts, no real currency logos, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 30.47–31.42 s: the Amber block materialises on "First, NUMBER!".
- 32.48–36.80 s: the three cards drift in on "salary" (32.8 s), "account balance" (33.5 s) and "transaction amounts" (34.5 s).
- Effect: **Banknote**.

**Audio sync:** block at 31.09 s; cards at 32.8, 33.5 and 34.5 s.
**On-screen text (overlay):** "1 · NUMBER" / "Salary · Balance · Amounts".
**Negative prompt:** "Real currency logos, readable fake amounts, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – VARCHAR (37.07–44.32 s · 7.25 s)
**Voice-over:** "Second, VARCHAR! Customer names, email addresses and city names lanti text data store cheyyadaniki use chestham."
**Tone:** clear.
**Visual objective:** VARCHAR stores text.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Lime #A3E635, text #F8F7FF. A large glowing Lime glass block with a text-line motif floats at the centre with a numbered badge '2'. Three Lime-edged glass text capsules slide in around it: an abstract name tag, an envelope shape, and a map-pin. Soft rim lighting, slow push-in. Leave space for a title and caption. No readable names or email addresses, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 37.35–38.55 s: the Lime block materialises on "Second, VARCHAR!".
- 39.14–44.09 s: the capsules slide in on "Customer names" (39.1 s), "email addresses" (40.2 s) and "city names" (41.2 s).
- Effect: **Press font** — the word "VARCHAR" presses into the block at 38.1 s.

**Audio sync:** block at 38.1 s; capsules at 39.1, 40.2 and 41.2 s.
**On-screen text (overlay):** "2 · VARCHAR" / "Names · Emails · Cities".
**Negative prompt:** "Real personal data, readable email addresses, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – DATE and TIMESTAMP (44.32–53.22 s · 8.90 s)
**Voice-over:** "Third, DATE and TIMESTAMP! Date of birth, transaction date and transaction timestamp lanti date and time information store cheyyadaniki use chestham."
**Tone:** clear.
**Visual objective:** DATE and TIMESTAMP store date and time information.

Generate as **two shots (7a, 7b)**.

**Shot 7a (44.32–47.05 s) – introduce:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, text #F8F7FF. A large glowing Violet glass block with a calendar-and-clock motif floats at the centre with a numbered badge '3'. Clean space for a title. Soft rim lighting, slow push-in. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 44.55–46.18 s the block appears on "Third, DATE and TIMESTAMP!".

**Shot 7b (47.05–53.22 s) – date vs time examples:**
"Same style and palette. The Violet block splits into two glass cards: a calendar page labelled with an abstract date shape, and a clock face with a precise time marker. A glowing dial turns to a date, then the clock hand ticks to a time. No readable fine text, no logos, no watermark."
Motion: 47.39–48.5 s the date dial turns on "date of birth" and "transaction date" (47.7–48.1 s); 48.76–49.5 s the clock hand ticks on "transaction timestamp"; the two cards glow together on "date and time information" (50.3–51.1 s). **Effect: Day dial.**

**Audio sync:** block at 45.3 s; dial at 47.7 s; clock at 48.8 s.
**On-screen text (overlay):** "3 · DATE & TIMESTAMP" / "Date of birth · Transaction date · Timestamp".
**Negative prompt:** "Readable fake dates, wrong time-zone claims, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – BOOLEAN (53.22–57.70 s · 4.48 s)
**Voice-over:** "Fourth, BOOLEAN! TRUE or FALSE values store cheyyadaniki use chestham."
**Tone:** crisp.
**Visual objective:** BOOLEAN stores TRUE or FALSE.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Rose #FB7185, text #F8F7FF. A large glowing Rose glass toggle switch at the centre with a numbered badge '4'. The switch flips on to a bright glow, then off to a dim glow. Soft rim lighting, quick, crisp motion. Leave space for a title and two labels. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 53.46–54.47 s: the toggle appears on "Fourth, BOOLEAN!".
- 54.9 s: toggle flips on ("TRUE"); 55.4 s: flips off ("FALSE").
- Effect: **Impact frame** — a one-frame flash on each flip.

**Audio sync:** toggle on at 54.9 s; off at 55.4 s.
**On-screen text (overlay):** "4 · BOOLEAN" / "TRUE · FALSE".
**Negative prompt:** "Clutter, flicker, off-palette colours, tiny text, watermark."

---

### Scene 9 – VARIANT (57.70–63.05 s · 5.35 s)
**Voice-over:** "Fifth, VARIANT! JSON lanti semi-structured data ni store cheyyadaniki use chestham."
**Tone:** clear.
**Visual objective:** VARIANT stores semi-structured data such as JSON.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A large translucent white glass block with curly-brace motif floats at the centre with a numbered badge '5'. Inside it, nested glass layers of abstract key-value rows glow with small Amber, Lime, Violet and Rose glints. Soft rim lighting, slow push-in. Leave space for a title and caption. No readable code, no logos, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 57.98–58.99 s: the white glass block appears on "Fifth, VARIANT!".
- 59.5–62.77 s: the block separates into nested layers on "JSON lanti semi-structured data".
- Effect: **Layer explode**.

**Audio sync:** block at 58.6 s; layers separate at 59.5 s.
**On-screen text (overlay):** "5 · VARIANT" / "JSON · semi-structured data".
**Negative prompt:** "Readable fake code, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Banking example (63.05–86.37 s · 23.32 s)
**Voice-over:** "Oka Banking project example teesukundham. CUSTOMER_ID ni NUMBER lo store chestham. CUSTOMER_NAME ni VARCHAR lo store chestham. DATE_OF_BIRTH ni DATE lo store chestham. TRANSACTION_TIMESTAMP ni TIMESTAMP lo store chestham. IS_ACTIVE ni BOOLEAN lo store chestham. Customer API nunchi vachina JSON data ni VARIANT column lo store cheyyachu."
**Tone:** storytelling, step by step.
**Visual objective:** Build a banking table, one column and data type at a time.

Generate as **seven shots (10a–10g)**. All shots use the same style so the table appears to build continuously.

**Shot 10a (63.05–65.42 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass table frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay: "BANKING PROJECT" from 63.4 s.

**Shot 10b (65.42–67.89 s) – CUSTOMER_ID → NUMBER:**
"Same style and palette. In the glass table frame, a first column appears with an Amber type-chip. A cursor types a column name, then the chip locks in. No readable fine text, no logos."
Overlay: `CUSTOMER_ID` at 65.6 s, chip `NUMBER` at 66.7 s. **Effect: Live cursor.**

**Shot 10c (67.89–70.51 s) – CUSTOMER_NAME → VARCHAR:**
"Same style and palette. A second column appears with a Lime type-chip. The cursor types a column name, then the chip locks in. No readable fine text, no logos."
Overlay: `CUSTOMER_NAME` at 68.0 s, chip `VARCHAR` at ≈69.2 s (see the note at the top about the audio).

**Shot 10d (70.51–74.64 s) – DATE_OF_BIRTH → DATE:**
"Same style and palette. A third column appears with a Violet type-chip and a small calendar glint. The cursor types the column name, then the chip locks in. No readable fine text, no logos."
Overlay: `DATE_OF_BIRTH` builds word by word (DATE 70.7 s, OF 71.9 s, BIRTH 72.9 s), chip `DATE` at 73.6 s.

**Shot 10e (74.64–78.55 s) – TRANSACTION_TIMESTAMP → TIMESTAMP:**
"Same style and palette. A fourth column appears with a Violet type-chip and a small clock glint. The cursor types the column name, then the chip locks in. No readable fine text, no logos."
Overlay: `TRANSACTION_TIMESTAMP` at 74.95 s, chip `TIMESTAMP` at ≈77.1 s.

**Shot 10f (78.55–81.75 s) – IS_ACTIVE → BOOLEAN:**
"Same style and palette. A fifth column appears with a Rose type-chip and a small toggle glint. The cursor types the column name, then the chip locks in. No readable fine text, no logos."
Overlay: `IS_ACTIVE` at 78.7 s, chip `BOOLEAN` at 80.6 s.

**Shot 10g (81.75–86.37 s) – JSON → VARIANT:**
"Same style and palette. A glass API panel on the left sends a JSON packet of glowing key-value layers into a sixth, wider white-glass column on the right. The camera pulls back to show the complete six-column table with its five coloured chips and the white VARIANT chip. No readable fine text, no logos."
Overlay: "CUSTOMER API → JSON" at 82.0 s, chip `VARIANT` at 84.6 s. **Effect: Code body** — a short abstract code card slides in beside the table (not readable).

**Audio sync:** every column and chip is timed to the word times in Appendix A.
**Negative prompt (all shots):** "Real bank logos, readable personal data, wrong type colours, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 11 – Closing recap (86.37–91.24 s · 4.87 s)
**Voice-over:** "So, data ni store chesetappudu correct Data Type select cheyyadam chaala important."
**Tone:** confident.
**Visual objective:** Reinforce the key message.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. The five glass type tiles (Amber digits, Lime text, Violet calendar, Rose toggle, white-glass braces) align in a clean row above a glowing Lime checkmark ring that lights up. Soft light bloom, slow push-in, clean space for one line of text. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."

**Motion instructions:**
- 86.59–86.88 s: the tiles fade in on "So,".
- 87.2–88.8 s: the tiles align on "data ni store chesetappudu".
- 88.8–90.99 s: the checkmark ring lights on "correct Data Type select cheyyadam chaala important".
- Effect: **Rack focus** — focus pulls from the tiles to the checkmark at 88.8 s.

**On-screen text (overlay):** "CHOOSE THE CORRECT DATA TYPE".
**Negative prompt:** "Clutter, tiny text, flicker, off-palette colours, watermark."

---

### Scene 12 – Series card, teaser and CTA outro (91.24–112.27 s · 21.03 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Nine! Next video lo Permanent, Transient and Temporary Tables madhya differences real-time examples tho explain chesthanu. Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** Series branding, next-episode teaser, one clear CTA, closing end card.

Generate as **five shots (12a–12e)**.

**Shot 12a (91.24–94.49 s) – Day 9 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first nine lit (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay: "THIRTY DAYS OF SNOWFLAKE · DAY 9" from 91.8 s; the ninth node lights at 93.9 s on "Nine".

**Shot 12b (94.49–101.13 s) – Teaser:**
"Same style and palette. A teaser panel slides in showing three glass table blocks in a row, with different glow treatments: one solid and steady, one with a dashed edge, and one translucent and faint. Clean, minimal, phone-readable. No readable fine text, no logos."
Overlay: "NEXT: PERMANENT · TRANSIENT · TEMPORARY TABLES". The three blocks appear on "Permanent" (≈95.8 s), "Transient" (96.4 s) and "Temporary" (97.1 s). The blocks only suggest three table types visually; do not imply specific retention or cost behaviour.

**Shot 12c (101.13–106.98 s) – Follow:**
"Same style and palette. A calm, clean background with a soft violet glow and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈104.3 s ("Instagram"), emphasised at ≈105.8 s on "Follow".

**Shot 12d (106.98–110.31 s) – Contact:**
"Same style and palette. A calm, clean background with a soft violet and lime glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 107.2 s, emphasised at ≈109.3 s on "Contact". **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 12e (110.31–112.27 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 110.49 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to the end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, claims about table features, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #0E0A1F, Violet #8B5CF6, Amber #FBBF24, Lime #A3E635, Rose #FB7185, text #F8F7FF, secondary text #A5A1C2. Data-type colour code: NUMBER = Amber, VARCHAR = Lime, DATE and TIMESTAMP = Violet, BOOLEAN = Rose, VARIANT = white glass with small glints of the other colours. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, logos, phone numbers or watermarks. No cartoon style, no stock footage, no off-palette colours."

---

## 5. Analyse the audio with Whisper (Windows)

This is how the timings in this file were produced. Repeat it whenever you have a new voice-over.

**Requirements:** Windows, Python **3.10–3.12** (very new Python versions such as 3.15 can't install the audio libraries), and ffmpeg on PATH. The first run downloads the model (about 0.5 GB for `small`, 1.5–2 GB for `medium`). CPU only is fine.

1. **Create a virtual environment and install** (PowerShell):
   ```powershell
   py -3.10 -m venv whisper-env
   .\whisper-env\Scripts\python.exe -m pip install faster-whisper
   ```
2. **Save this as `run_whisper.py`:**
   ```python
   import json, sys
   from faster_whisper import WhisperModel

   audio, out = sys.argv[1], sys.argv[2]
   model = WhisperModel("small", device="cpu", compute_type="int8")
   segments, info = model.transcribe(
       audio, language="en", word_timestamps=True,
       beam_size=1, condition_on_previous_text=False, temperature=0.0)

   result = []
   for s in segments:
       result.append({
           "start": round(s.start, 2), "end": round(s.end, 2), "text": s.text,
           "words": [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in s.words],
       })
   json.dump(result, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
   print("done", info.duration)
   ```
3. **Run it:**
   ```powershell
   .\whisper-env\Scripts\python.exe run_whisper.py audio.mp3 whisper_out.json
   ```
4. **Cross-check with the real pauses** (this catches mismatched lines):
   ```powershell
   ffmpeg -i audio.mp3 -af "silencedetect=noise=-26dB:d=0.15" -f null - 2>&1 | Select-String "silence_(start|end)"
   ```
5. **Build the timing map:** take the word start times from `whisper_out.json`, keep your script's spelling, and place scene cuts in the middle of a pause.

**What worked and what did not on this audio**
- The `medium` model in Telugu mode stalled for 15+ minutes (it appeared to loop) and produced misspelled Telugu on Day 8. The `small` model in English mode with `condition_on_previous_text=False` finished in a few minutes and gave reliable timings for Telugu-English narration. It writes the Telugu words as approximate English, so always replace its text with your script.
- Whisper can mishear technical words (for example VARCHAR as "watch" or "number"). Use the transcript for **times**, not for the wording, and listen to any word that matters.
- Words spoken in a different order from the transcript (for example "NDR EdTech ni Contact avvandi") can be placed wrongly. Those times are marked ≈.

---

## 6. Editing and synchronisation plan

1. Import `audio.mp3` (112.27 s) as the master audio track and do not alter it.
2. Place the generated clips on the timeline using the scene times in section 2. Cut inside the pauses.
3. Where a scene is longer than the tool's clip limit, use the shots listed in section 3. Slow the last seconds slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text overlays in the editor (titles, type names, column names such as `CUSTOMER_ID`, `DATE_OF_BIRTH`, `TRANSACTION_TIMESTAMP`, `IS_ACTIVE`, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. Add optional subtle music, ducked about 15–20 dB under narration, plus light whooshes only in pauses.
7. Check sync at the start, at every scene cut, at each type reveal (30.5, 37.4, 44.5, 53.5, 58.0 s), in Scene 10 (each column chip), and at the final tagline (110.49 s). Listen to 67.96–69.38 s for the VARCHAR/NUMBER question. Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration, pauses and word times are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: NUMBER for numeric values, VARCHAR for text, DATE and TIMESTAMP for date and time information, BOOLEAN for TRUE or FALSE, and VARIANT for semi-structured data such as JSON. No sizes, precision, range limits or other type properties are stated.
- The "problems" in Scene 3 are shown only as generic misalignment. No specific error messages are claimed.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
