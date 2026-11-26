# Thirty Days of Snowflake – Day 22: Load Data from AWS S3 to Snowflake
Video prompt package (NDR EdTech) — `Audio\day22.mp3` + `days-scripts\day22.txt`, analysed with Whisper

> **Timing status: MEASURED from day22.mp3 (127.48 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio otherwise matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **The opening (0–3.6 s):** the line "Andaru ela unnaru?" was removed from this recording (you confirmed this), so the opening is "Hello guys! … Oka real-time Data Engineering scenario teesukundham!" ("Hello guys!" 0.00–0.74 s, then one phrase 1.08–3.58 s). Your `days-scripts\day22.txt` still contains the removed line; the package follows the audio.
> 2. **"AWS S3" versus "Amazon S3":** Whisper writes "Amazon S3". Your script says "AWS S3", so the overlays use **AWS S3**. Please listen once to confirm the narrator's wording.
> 3. **Follow and Contact lines (about 116–125 s):** Whisper's word order for these Telugu lines is unreliable, so the "Follow" and "Contact" times are estimated (≈).
> 4. **There is no scripted `[pause]`** in this script. The longest pause is 0.6 s.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 22: Load Data from AWS S3 to Snowflake |
| Duration | **127.48 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,824 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day22.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (34 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Bucket to Table" (new for Day 22)
| Role | HEX | Use |
|---|---|---|
| Background | `#0F172A` | Base, gradients (slate navy) |
| S3 Bucket Copper | `#F2994A` | The **AWS S3 bucket** and the CSV files in it (the source) |
| Stage Violet | `#A78BFA` | The **storage integration** (a key and bridge) and the **external stage** (a portal) |
| Snowflake Ice | `#6FD0FF` | **Snowflake**: the database and the CUSTOMER table (the target) |
| Data Lime | `#B7F04A` | Data **moving** (the COPY INTO flow), success |
| Cloud Glass | `#E8EEF8` | File Format template, SQL panels, neutral glass |
| Primary text | `#F7F9FD` | Titles, labels |
| Secondary text | `#9AA6BE` | Captions |

**Colour code (use in every scene):** source = **Copper** · connection (storage integration, stage) = **Violet** · target (Snowflake table) = **Ice** · data moving = **Lime**. The path always reads left to right: **Copper bucket → Violet bridge and portal → Lime flow → Ice table**.

**The core visual rule (technical accuracy):** the six steps are shown in the script's order: **1 create a bucket, 2 upload data files, 3 create a FILE FORMAT, 4 create a STORAGE INTEGRATION, 5 create an EXTERNAL STAGE, 6 COPY INTO**. A stage connects Snowflake to the source files; COPY INTO loads the data into a table. Use only a **generic cloud-bucket glyph** and write "AWS S3" as an overlay; **do not draw AWS logos**. Show abstract file shapes only (no readable data).

### Motion effects used (from the skill's effects library)
Post wall, Head stack, Letter dive, Impact frame, Liquid glass, Press font, Live cursor, Code body, Rack focus, Comment drop, Orbit ring. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.81 | "Hello guys! … Oka real-time Data Engineering scenario teesukundham!" (0.00–3.58) | Curious | Title hook |
| 2 | 3.81–15.90 | "Mee company ki daily lakhs of customer records AWS S3 bucket lo land avuthunnayi." (4.04–8.89) · "Ippudu aa data ni Snowflake loki ela load chestharu?" (9.29–12.61) · "Manual ga upload chesthara?" (12.98–14.30) · "Definitely not!" (14.69–15.68) | Curious, then firm | Lakhs of records in S3, how to load, not manually |
| 3 | 15.90–19.32 | "Data Engineers ga manam ee process ni automate cheyyali." (16.11–19.14) | Confident | Automate the process |
| 4 | 19.32–23.53 | "Let's understand step by step!" (19.50–21.07) · "Welcome to NDR EdTech!" (21.60–23.30) | Welcoming | Title and brand welcome |
| 5 | 23.53–29.16 | "AWS S3 nunchi Snowflake ki data load cheyyadaniki mainly ee steps follow avutham." (23.76–28.93) | Clear | The six steps appear |
| 6 | 29.16–52.07 | "First, AWS S3 lo bucket create chestham." (29.38–32.34) · "Second, data files ni S3 bucket lo upload chestham." (32.76–36.28) · "Third, Snowflake lo FILE FORMAT create chestham." (36.66–39.61) · "Fourth, S3 ki connect avvadaniki STORAGE INTEGRATION create chestham." (39.96–43.93) · "Fifth, EXTERNAL STAGE create chestham." (44.28–46.61) · "Finally, COPY INTO command use chesi data ni Snowflake table loki load chestham." (46.97–51.83) | Clear, structured | Six numbered steps |
| 7 | 52.07–96.00 | "Oka Banking project example teesukundham." (52.31–54.33) · "Mana CUSTOMER data CSV files AWS S3 bucket lo land ayyayi." (54.67–58.74) · "Ippudu Snowflake lo required objects create cheddham." (59.07–61.86) · "SQL commands chuddam!" (62.20–63.36) · "CREATE FILE FORMAT CSV_FORMAT TYPE = CSV SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '\"';" (63.80–72.71) · "CREATE STAGE CUSTOMER_STAGE URL = 's3://my-bank-bucket/customer/' STORAGE_INTEGRATION = MY_S3_INTEGRATION FILE_FORMAT = CSV_FORMAT;" (73.19–85.01) · "Ippudu data load cheyyadaniki:" (85.35–86.74) · "COPY INTO CUSTOMER FROM @CUSTOMER_STAGE;" (87.06–90.86) · "Anthe! S3 lo unna CSV data Snowflake CUSTOMER table loki load avuthundhi." (91.18–95.82) | Storytelling, focused | Banking: file format, stage, COPY INTO, data loaded |
| 8 | 96.00–106.90 | "So, simple ga gurthupettukondi!" (96.19–97.95) · "AWS S3 is our cloud storage." (98.28–100.69) · "Stage connects Snowflake to the source files." (100.98–103.46) · "COPY INTO loads the data into Snowflake tables." (103.80–106.72) | Confident | Three-card recap |
| 9 | 106.90–116.00 | "Idi mana Thirty Days of Snowflake series lo Day Twenty-Two!" (107.08–110.12) · "Next video lo COPY INTO vs Snowpipe madhya difference real-time examples tho explain chesthanu." (110.47–115.85) | Upbeat | Day 22 card, COPY INTO vs Snowpipe teaser |
| 10 | 116.00–127.48 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (116.15–121.80) · "Full course details kosam NDR EdTech ni Contact avvandi!" (122.10–125.20) · "Let's Learn and Grow Together!" (125.51–127.12) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.74–1.08, 3.58–4.04, 8.89–9.29, 12.61–12.98, 14.30–14.69, 15.68–16.11, 19.14–19.50, 21.07–21.60, 23.30–23.76, 28.93–29.38, 29.84–30.13, 32.34–32.76, 33.21–33.53, 36.28–36.66, 37.03–37.31, 39.61–39.96, 40.34–40.66, 43.93–44.28, 44.67–44.96, 46.61–46.97, 47.53–47.78, 51.83–52.31, 54.33–54.67, 58.74–59.07, 61.86–62.20, 63.36–63.80, 64.95–65.21, 66.08–66.52, 68.05–68.38, 70.04–70.42, 72.71–73.19, 74.01–74.28, 75.09–75.40, 77.02–77.27, 78.23–78.49, 78.92–79.22, 82.38–82.71, 85.01–85.35, 86.74–87.06, 89.15–89.37, 90.86–91.18, 91.51–91.81, 95.82–96.19, 97.95–98.28, 100.69–100.98, 103.46–103.80, 106.72–107.08, 110.12–110.47, 115.85–116.15, 121.80–122.10, 125.20–125.51, 127.12–127.48.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Oka real-time Data Engineering scenario teesukundham! | real-time ≈1.6 · Data Engineering scenario ≈2.2 |
| Mee company ki daily lakhs of customer records AWS S3 bucket lo land avuthunnayi. | daily lakhs ≈5.0 · customer records ≈6.0 · **AWS S3 bucket** ≈7.0 · land ≈8.3 |
| Ippudu aa data ni Snowflake loki ela load chestharu? | Snowflake ≈10.2 · load ≈11.3 |
| Manual ga upload chesthara? | Manual ga upload 12.98 |
| Definitely not! | Definitely not 14.69 |
| Data Engineers ga manam ee process ni automate cheyyali. | Data Engineers ≈16.6 · automate ≈18.0 |
| Let's understand step by step! / Welcome to NDR EdTech! | Let's 19.50 · Welcome 21.60 · NDR ≈22.2 · EdTech ≈22.7 |
| AWS S3 nunchi Snowflake ki data load cheyyadaniki mainly ee steps follow avutham. | AWS S3 ≈24.3 · Snowflake ≈25.5 · steps ≈27.8 |
| First, AWS S3 lo bucket create chestham. | First 29.38 · AWS S3 lo bucket ≈30.2 · create ≈31.4 |
| Second, data files ni S3 bucket lo upload chestham. | Second 32.76 · data files ≈33.6 · upload ≈35.2 |
| Third, Snowflake lo FILE FORMAT create chestham. | Third 36.66 · FILE FORMAT ≈37.6 · create ≈38.8 |
| Fourth, S3 ki connect avvadaniki STORAGE INTEGRATION create chestham. | Fourth 39.96 · connect ≈41.2 · STORAGE INTEGRATION ≈42.0 |
| Fifth, EXTERNAL STAGE create chestham. | Fifth 44.28 · EXTERNAL STAGE ≈45.2 |
| Finally, COPY INTO command use chesi data ni Snowflake table loki load chestham. | Finally 46.97 · COPY INTO ≈48.0 · Snowflake table ≈50.0 · load ≈50.9 |
| Mana CUSTOMER data CSV files AWS S3 bucket lo land ayyayi. | CUSTOMER data ≈55.2 · CSV files ≈56.3 · land ayyayi ≈58.0 |
| Ippudu Snowflake lo required objects create cheddham. | required objects ≈60.4 · create ≈61.2 |
| CREATE FILE FORMAT CSV_FORMAT | CREATE FILE FORMAT 63.80–64.95 · CSV_FORMAT 65.21–66.08 |
| TYPE = CSV | TYPE 66.52 · CSV ≈67.4 |
| SKIP_HEADER = 1 | SKIP_HEADER 68.38 · 1 ≈69.6 |
| FIELD_OPTIONALLY_ENCLOSED_BY = '"'; | FIELD_OPTIONALLY_ENCLOSED_BY 70.42–71.9 · '"' ≈72.2 |
| CREATE STAGE CUSTOMER_STAGE | CREATE STAGE 73.19 · CUSTOMER_STAGE 74.28 |
| URL = 's3://my-bank-bucket/customer/' | URL 75.40 · s3://… ≈76.0–78.2 |
| STORAGE_INTEGRATION = MY_S3_INTEGRATION | STORAGE_INTEGRATION 78.49 · MY_S3_INTEGRATION 79.22–82.38 |
| FILE_FORMAT = CSV_FORMAT; | FILE_FORMAT 82.71 · CSV_FORMAT ≈84.0 |
| Ippudu data load cheyyadaniki: | data load 85.35–86.7 |
| COPY INTO CUSTOMER FROM @CUSTOMER_STAGE; | COPY INTO CUSTOMER 87.06 · FROM @CUSTOMER_STAGE 89.37 |
| Anthe! S3 lo unna CSV data Snowflake CUSTOMER table loki load avuthundhi. | Anthe 91.18 · CSV data ≈92.6 · CUSTOMER table ≈94.0 · load avuthundhi ≈95.0 |
| AWS S3 is our cloud storage. | AWS S3 98.28 · cloud storage ≈99.6 |
| Stage connects Snowflake to the source files. | Stage 100.98 · connects ≈101.8 · source files ≈103.0 |
| COPY INTO loads the data into Snowflake tables. | COPY INTO 103.80 · loads ≈105.0 · tables ≈106.3 |
| Idi mana Thirty Days of Snowflake series lo Day Twenty-Two! | Thirty ≈107.8 · Snowflake ≈108.6 · Twenty-Two ≈109.4 |
| Next video lo COPY INTO vs Snowpipe madhya difference real-time examples tho explain chesthanu. | COPY INTO ≈111.2 · Snowpipe ≈112.6 · difference ≈113.4 · real-time examples ≈114.2 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈118.4 · NDR EdTech ≈119.4–120.4 · **Follow** ≈120.8 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 122.10–123.4 · NDR EdTech ≈123.6 · **Contact** ≈124.4 (estimated) |
| Let's Learn and Grow Together! | Let's 125.51 · Together ≈126.6 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, Cloud Glass #E8EEF8, text #F7F9FD.*

**Object look (keep identical in every scene):** the **S3 bucket** = a Copper glass bucket (a generic cloud-storage glyph, no AWS logo) holding small Copper file cards. **File Format** = a Cloud Glass template card with a grid glyph. **Storage integration** = a Violet key on a Violet bridge. **External stage** = a Violet portal window. **COPY INTO** = a Lime flow of data blocks. **Snowflake table** = an Ice glass table block with rows of cells.

### Scene 1 – Hook (0.00–3.81 s · 3.81 s)
**Voice-over:** "Hello guys! Oka real-time Data Engineering scenario teesukundham!"
**Tone:** curious.
**Visual objective:** Welcome viewers and introduce a real-time scenario.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, Cloud Glass #E8EEF8, text #F7F9FD. A slate-navy space with soft light and drifting glass particles. A glowing Copper glass cloud-bucket (generic glyph, no logo) at the upper-left sends a thin Lime line of data blocks toward a glass snowflake-crystal database at the upper-right. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–0.74 s: particles drift in on "Hello guys!".
- 1.08–3.58 s: the bucket and the database appear and the Lime line draws between them on "Oka real-time Data Engineering scenario teesukundham!" (real-time ≈1.6 s).
- 3.58–3.81 s: soft light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at ≈2.2 s on "scenario".
**Audio sync:** title lands at ≈1.2 s; the sweep completes in the pause at 3.58–4.04 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 22".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, real AWS or Snowflake logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – Lakhs of records in S3: how to load them? (3.81–15.90 s · 12.09 s)
**Voice-over:** "Mee company ki daily lakhs of customer records AWS S3 bucket lo land avuthunnayi. Ippudu aa data ni Snowflake loki ela load chestharu? Manual ga upload chesthara? Definitely not!"
**Tone:** curious, then firm.
**Visual objective:** Data keeps landing in S3 every day; it must get into Snowflake, but not by manual upload.
Generate as **three shots (2a–2c)**.

**Shot 2a (3.81–9.09 s) – lakhs of records landing in S3:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Cloud Glass #E8EEF8, text #F7F9FD. A large Copper glass bucket (generic cloud-storage glyph, no logo) sits at the centre. A steady rain of small Copper file cards (abstract, no readable data) lands in it from above, faster and faster, and the bucket fills and glows. A small calendar-page glyph shows that this happens daily. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.04–5.0 s the bucket appears on "Mee company ki"; ≈5.0–6.0 s the card rain starts on "daily lakhs of customer records" (daily lakhs ≈5.0 s); ≈7.0–8.89 s the bucket glows on "AWS S3 bucket lo land avuthunnayi". **Effect: Post wall** — a wall of file cards builds up inside the bucket.
Overlay (post): "DAILY LAKHS OF CUSTOMER RECORDS" from ≈5.0 s; "AWS S3 BUCKET" at ≈7.0 s.

**Shot 2b (9.09–12.80 s) – how do we load it into Snowflake?:**
"Same style and palette, plus Snowflake Ice #6FD0FF. On the far side an Ice glass snowflake-crystal database appears, with a wide empty gap between it and the bucket. A soft question-mark glow pulses in the gap. No readable text, no logos, no watermark."
Motion: 9.29–10.2 s the database appears on "Ippudu aa data ni"; ≈10.2–11.3 s the question mark builds on "Snowflake loki ela"; ≈11.3–12.61 s it pulses on "load chestharu?".
Overlay (post): "HOW TO LOAD IT INTO SNOWFLAKE?" from 9.29 s.

**Shot 2c (12.80–15.90 s) – not manually:**
"Same style and palette. A cursor tries to drag a single file card across the gap by hand, slowly, while hundreds of cards keep piling up behind it. A soft Violet barrier flashes and the manual attempt fades away. Firm, clear. No readable text, no logos, no watermark."
Motion: 12.98–14.30 s the cursor drags one card on "Manual ga upload chesthara?"; 14.69–15.68 s the barrier flashes on "Definitely not!". **Effect: Impact frame** — a one-frame flash at 14.69 s.
Overlay (post): "MANUAL UPLOAD?" from 12.98 s; "DEFINITELY NOT!" at 14.69 s.

**Audio sync:** card rain at ≈5.0 s; database at 9.29 s; cursor at 12.98 s; flash at 14.69 s.
**Negative prompt (all shots):** "Real AWS logos, readable data, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Automate the process (15.90–19.32 s · 3.42 s)
**Voice-over:** "Data Engineers ga manam ee process ni automate cheyyali."
**Tone:** confident.
**Visual objective:** Data engineers should automate this process.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, text #F7F9FD. A glowing glass gear-and-arrow emblem rises between the bucket and the database, and a thin Lime pipeline line starts to draw between them. Hopeful, forward-moving. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 16.11–17.5 s: the gear emblem rises on "Data Engineers ga manam".
- ≈18.0–19.14 s: the Lime pipeline draws on "ee process ni automate cheyyali" (automate ≈18.0 s).
**Audio sync:** emblem at 16.11 s; pipeline at ≈18.0 s.
**On-screen text (overlay, post):** "AUTOMATE THE PROCESS" from ≈17.0 s.
**Negative prompt:** "Readable text, specific tools, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Let's understand step by step, welcome (19.32–23.53 s · 4.21 s)
**Voice-over:** "Let's understand step by step! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Name the topic and welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Snowflake Ice #6FD0FF, Data Lime #B7F04A, text #F7F9FD. A calm, clean frame with the small bucket, a short Lime pipeline and the small database resting in a row at the lower-centre. A reserved clean area at the top for the logo and a soft glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 19.50–21.07 s the title lands on "Let's understand step by step!" (**Effect: Letter dive** — the letters settle fully before 20.9 s); 21.60–23.30 s a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** title at 19.50 s; logo and panel at 21.60 s; "NDR" at ≈22.2 s.
**On-screen text (overlay, post):** "AWS S3 → SNOWFLAKE" at 19.50 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 21.60 s.
**Negative prompt:** "Fake logos, distorted logo, misspelled title, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – The steps, in one list (23.53–29.16 s · 5.63 s)
**Voice-over:** "AWS S3 nunchi Snowflake ki data load cheyyadaniki mainly ee steps follow avutham."
**Tone:** clear.
**Visual objective:** Six main steps lead from S3 to Snowflake.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, Cloud Glass #E8EEF8, text #F7F9FD. Six small numbered glass tiles rise one after another in a vertical stack, each with a tiny abstract icon: a bucket (Copper), a file card (Copper), a template card (Cloud Glass), a key (Violet), a portal (Violet), a Lime flow arrow. Clean, uncluttered, phone-readable layout. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 23.76–25.5 s: the bucket-to-database path glows on "AWS S3 nunchi Snowflake ki data load cheyyadaniki" (AWS S3 ≈24.3 s, Snowflake ≈25.5 s).
- ≈25.5–28.93 s: the six tiles rise one by one on "mainly ee steps follow avutham". **Effect: Head stack.**
**Audio sync:** path at ≈24.3 s; the six tiles from ≈26.0 s to 28.9 s.
**On-screen text (overlay, post):** "6 STEPS" from ≈26.0 s.
**Negative prompt:** "Real AWS logos, readable fine text, extra steps, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – The six steps (29.16–52.07 s · 22.91 s)
**Voice-over:** "First, AWS S3 lo bucket create chestham. Second, data files ni S3 bucket lo upload chestham. Third, Snowflake lo FILE FORMAT create chestham. Fourth, S3 ki connect avvadaniki STORAGE INTEGRATION create chestham. Fifth, EXTERNAL STAGE create chestham. Finally, COPY INTO command use chesi data ni Snowflake table loki load chestham."
**Tone:** clear, structured.
**Visual objective:** One shot per step, each added to the same growing path.
Generate as **six shots (6a–6f)**. Keep the path layout and badge position identical so the steps stack up into one pipeline.

**Shot 6a (29.16–32.55 s) – 1 · create a bucket in AWS S3:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Cloud Glass #E8EEF8, text #F7F9FD. An empty Copper glass bucket (generic cloud-storage glyph, no logo) is assembled at the left of the frame from glowing edges and settles with a soft glow. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 29.38–29.84 s the badge appears on "First,"; 30.13–31.4 s the bucket assembles on "AWS S3 lo bucket"; ≈31.4–32.34 s it settles on "create chestham". **Effect: Press font** — "BUCKET" presses in at ≈30.2 s.
Overlay (post): "1 · CREATE A BUCKET IN AWS S3" at 29.38 s.

**Shot 6b (32.55–36.47 s) – 2 · upload data files:**
"Same style and palette. Copper file cards (abstract, no readable data) fly in from the lower edge and drop into the bucket one by one. The bucket fills and glows. A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark."
Motion: 32.76–33.21 s the badge appears on "Second,"; 33.53–35.2 s the cards fly in on "data files ni S3 bucket lo" (data files ≈33.6 s); ≈35.2–36.28 s the bucket glows on "upload chestham".
Overlay (post): "2 · UPLOAD DATA FILES TO THE BUCKET" at 32.76 s.

**Shot 6c (36.47–39.79 s) – 3 · create a FILE FORMAT in Snowflake:**
"Same style and palette, plus Snowflake Ice #6FD0FF. At the right of the frame an Ice glass snowflake-crystal database appears and a Cloud Glass template card with a grid glyph (columns and rows) lights up beside it, as the description of how the files are laid out. A numbered badge '3'. Calm, clear. No readable text, no logos, no watermark."
Motion: 36.66–37.03 s the badge appears on "Third,"; 37.31–38.8 s the database and the template card appear on "Snowflake lo FILE FORMAT" (FILE FORMAT ≈37.6 s); ≈38.8–39.61 s the template glows on "create chestham".
Overlay (post): "3 · CREATE A FILE FORMAT IN SNOWFLAKE" at 36.66 s.

**Shot 6d (39.79–44.11 s) – 4 · create a STORAGE INTEGRATION to connect to S3:**
"Same style and palette, plus Stage Violet #A78BFA. A Violet bridge draws itself across the gap between the Copper bucket and the Ice database, and a glowing Violet key settles at the bridge's centre as the connection. A numbered badge '4'. Calm, clear. No readable text, no logos, no watermark."
Motion: 39.96–40.34 s the badge appears on "Fourth,"; 40.66–42.0 s the bridge draws across on "S3 ki connect avvandi" (connect ≈41.2 s); ≈42.0–43.93 s the key settles on "STORAGE INTEGRATION create chestham". **Effect: Orbit ring** — a soft Violet ring circles the key once at ≈42.0 s.
Overlay (post): "4 · CREATE A STORAGE INTEGRATION" at 39.96 s; "CONNECT TO S3" from ≈41.2 s.

**Shot 6e (44.11–46.79 s) – 5 · create an EXTERNAL STAGE:**
"Same style and palette. A Violet portal window opens on the Snowflake side of the bridge, framing the Copper bucket's files as if looking through a window. A numbered badge '5'. Calm, clear. No readable text, no logos, no watermark."
Motion: 44.28–44.67 s the badge appears on "Fifth,"; 44.96–46.61 s the portal opens on "EXTERNAL STAGE create chestham" (EXTERNAL STAGE ≈45.2 s).
Overlay (post): "5 · CREATE AN EXTERNAL STAGE" at 44.28 s.

**Shot 6f (46.79–52.07 s) – 6 · COPY INTO loads the data:**
"Same style and palette, plus Data Lime #B7F04A. A Lime flow of data blocks runs from the portal into an Ice glass table block, filling its rows with glowing cells. A numbered badge '6'. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 46.97–47.53 s the badge appears on "Finally,"; 47.78–50.0 s the Lime flow starts on "COPY INTO command use chesi data ni" (COPY INTO ≈48.0 s); ≈50.0–51.83 s the table fills on "Snowflake table loki load chestham". **Effect: Rack focus** — focus pulls from the portal to the table at ≈50.0 s.
Overlay (post): "6 · COPY INTO → SNOWFLAKE TABLE" at 46.97 s.

**Audio sync:** badge 1 at 29.38 s; badge 2 at 32.76 s; badge 3 at 36.66 s; badge 4 at 39.96 s; badge 5 at 44.28 s; badge 6 at 46.97 s.
**Negative prompt (all shots):** "Real AWS or Snowflake logos, readable fine text, extra steps, wrong step order, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (52.07–96.00 s · 43.93 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana CUSTOMER data CSV files AWS S3 bucket lo land ayyayi. Ippudu Snowflake lo required objects create cheddham. SQL commands chuddam! CREATE FILE FORMAT CSV_FORMAT TYPE = CSV SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '\"'; CREATE STAGE CUSTOMER_STAGE URL = 's3://my-bank-bucket/customer/' STORAGE_INTEGRATION = MY_S3_INTEGRATION FILE_FORMAT = CSV_FORMAT; Ippudu data load cheyyadaniki: COPY INTO CUSTOMER FROM @CUSTOMER_STAGE; Anthe! S3 lo unna CSV data Snowflake CUSTOMER table loki load avuthundhi."
**Tone:** storytelling, focused.
**Visual objective:** Create a file format and a stage, then COPY INTO the CUSTOMER table from CSV files in S3.
Generate as **twelve shots (7a–7l)**. All shots use the same camera language and layout (bucket on the left, the code panel in the centre when shown, the Snowflake table on the right).

**Shot 7a (52.07–54.50 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Snowflake Ice #6FD0FF, Cloud Glass #E8EEF8, text #F7F9FD. A sleek abstract Cloud Glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈52.5 s.

**Shot 7b (54.50–58.91 s) – CUSTOMER CSV files landed in S3:**
"Same style and palette. Copper file cards with a small CSV glyph (comma-separated columns, no readable data) land in the Copper bucket, and a small CUSTOMER label-tag glow appears beside them. No readable fine text, no logos."
Overlay (post): "CUSTOMER DATA" at ≈55.2 s; "CSV FILES" at ≈56.3 s; "LANDED IN AWS S3" at ≈58.0 s.

**Shot 7c (58.91–62.03 s) – create the required objects in Snowflake:**
"Same style and palette. On the Snowflake side three empty glass slots appear in a row, waiting to be filled: a template slot, a portal slot and a table slot. A soft Violet glow pulses on them. No readable fine text, no logos."
Motion: 59.07–60.4 s the slots appear on "Ippudu Snowflake lo"; ≈60.4–61.86 s they pulse on "required objects create cheddham".
Overlay (post): "CREATE THE REQUIRED OBJECTS IN SNOWFLAKE" from 59.07 s.

**Shot 7d (62.03–65.08 s) – SQL: CREATE FILE FORMAT:**
"Same style and palette. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) slides in at the centre with a thin Ice edge. The template slot glows beside it. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 62.20–63.36 s the panel slides in on "SQL commands chuddam!"; 63.80–64.95 s the first words type on "CREATE FILE FORMAT". **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE FILE FORMAT
```
Appears at 63.80 s.

**Shot 7e (65.08–68.22 s) – SQL: CSV_FORMAT, TYPE = CSV:**
"Same style and palette. The code panel continues. The template slot fills with a Cloud Glass template card showing a comma glyph. No readable code, no logos, no watermark."
Motion: 65.21–66.08 s the name types on "CSV_FORMAT"; 66.52–68.05 s the next line types on "TYPE = CSV". **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE FILE FORMAT CSV_FORMAT
TYPE = CSV
```
"CSV_FORMAT" at 65.21 s; "TYPE = CSV" at 66.52 s.

**Shot 7f (68.22–72.95 s) – SQL: SKIP_HEADER and FIELD_OPTIONALLY_ENCLOSED_BY:**
"Same style and palette. The code panel continues. On the template card a thin header row dims (skipped) and a small quotation-mark glyph appears around one cell (optionally enclosed). No readable code, no logos, no watermark."
Motion: 68.38–70.04 s line 3 types on "SKIP_HEADER = 1" and the header row dims; 70.42–72.71 s line 4 types on "FIELD_OPTIONALLY_ENCLOSED_BY = '\"';" and the quote glyph lights. **Effect: Code body.**
Overlay (post, monospace; the full statement shown at the end):
```sql
CREATE FILE FORMAT CSV_FORMAT
TYPE = CSV
SKIP_HEADER = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"';
```
"SKIP_HEADER = 1" at 68.38 s; "FIELD_OPTIONALLY_ENCLOSED_BY = '"';" at 70.42 s.

**Shot 7g (72.95–75.25 s) – SQL: CREATE STAGE:**
"Same style and palette, plus Stage Violet #A78BFA. A new empty code editor panel appears and the portal slot glows Violet beside it. No readable code, no logos, no watermark."
Motion: 73.19–74.01 s the first words type on "CREATE STAGE"; 74.28–75.09 s the name types on "CUSTOMER_STAGE". **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE STAGE CUSTOMER_STAGE
```
"CREATE STAGE" at 73.19 s; "CUSTOMER_STAGE" at 74.28 s.

**Shot 7h (75.25–78.36 s) – SQL: URL of the S3 location:**
"Same style and palette. The code panel continues. A thin Copper line draws from the portal slot to the Copper bucket, as the stage's location. No readable code, no logos, no watermark."
Motion: 75.40–77.02 s the line types on "URL = 's3://" and the Copper line starts to draw; 77.27–78.23 s the path completes on "my-bank-bucket/customer/'". **Effect: Code body.**
Overlay (post, monospace; append):
```sql
CREATE STAGE CUSTOMER_STAGE
URL = 's3://my-bank-bucket/customer/'
```
"URL = 's3://my-bank-bucket/customer/'" from 75.40 s.

**Shot 7i (78.36–82.55 s) – SQL: STORAGE_INTEGRATION:**
"Same style and palette. The code panel continues. A Violet key and bridge (the already existing integration) glow between the bucket and the portal. No readable code, no logos, no watermark."
Motion: 78.49–78.92 s the keyword types on "STORAGE_INTEGRATION"; 79.22–82.38 s the value types on "= MY_S3_INTEGRATION" and the bridge glows. **Effect: Code body.**
Overlay (post, monospace; append):
```sql
STORAGE_INTEGRATION = MY_S3_INTEGRATION
```
"STORAGE_INTEGRATION" at 78.49 s; "= MY_S3_INTEGRATION" at 79.22 s.

**Shot 7j (82.55–85.18 s) – SQL: FILE_FORMAT:**
"Same style and palette. The code panel finishes the stage statement. The template card slides onto the portal, completing the stage. No readable code, no logos, no watermark."
Motion: 82.71–85.01 s the last line types on "FILE_FORMAT = CSV_FORMAT;" and the template card clicks into the portal. **Effect: Code body.**
Overlay (post, monospace; the full statement shown at the end):
```sql
CREATE STAGE CUSTOMER_STAGE
URL = 's3://my-bank-bucket/customer/'
STORAGE_INTEGRATION = MY_S3_INTEGRATION
FILE_FORMAT = CSV_FORMAT;
```
"FILE_FORMAT = CSV_FORMAT;" at 82.71 s.

**Shot 7k (85.18–91.02 s) – SQL: COPY INTO:**
"Same style and palette, plus Data Lime #B7F04A. A new code panel appears. As the statement types, a Lime flow of data blocks runs from the portal into the empty Ice CUSTOMER table block, and its rows start to fill. No readable code, no logos, no watermark."
Motion: 85.35–86.74 s the panel appears on "Ippudu data load cheyyadaniki:"; 87.06–89.15 s the first line types on "COPY INTO CUSTOMER"; 89.37–90.86 s the second line types on "FROM @CUSTOMER_STAGE;" and the Lime flow starts. **Effect: Code body.**
Overlay (post, monospace):
```sql
COPY INTO CUSTOMER
FROM @CUSTOMER_STAGE;
```
"COPY INTO CUSTOMER" at 87.06 s; "FROM @CUSTOMER_STAGE;" at 89.37 s.

**Shot 7l (91.02–96.00 s) – the data is loaded:**
"Same style and palette. The Ice CUSTOMER table block is full of glowing cells, the Lime flow settles, and a soft success pulse spreads across the path from the bucket to the table. The camera pulls back to show the whole path. No readable text, no logos."
Motion: 91.18–91.51 s a success flash on "Anthe!" (**Effect: Impact frame**); 91.81–93.5 s the Copper CSV cards glow on "S3 lo unna CSV data"; ≈94.0–95.82 s the table lights fully on "Snowflake CUSTOMER table loki load avuthundhi".
Overlay (post): "CSV DATA IN S3 → SNOWFLAKE CUSTOMER TABLE" from ≈92.6 s.

**Audio sync:** every statement starts at its pause end (63.80, 73.19, 87.06 s); inner times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, real AWS logos, readable personal data, readable fake text in the generated video, wrong syntax, extra statements, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (96.00–106.90 s · 10.90 s)
**Voice-over:** "So, simple ga gurthupettukondi! AWS S3 is our cloud storage. Stage connects Snowflake to the source files. COPY INTO loads the data into Snowflake tables."
**Tone:** confident.
**Visual objective:** Three-card recap.
Generate as **four shots (8a–8d)**.

**Shot 8a (96.00–98.12 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, text #F7F9FD. The Copper bucket, the Violet portal and the Ice table glide into a neat row at the centre with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈96.5 s.

**Shot 8b (98.12–100.84 s) – AWS S3:**
"Same style and palette. The Copper bucket fills the frame holding file cards. Clean and calm. No readable text, no logos."
Overlay (post): "AWS S3" at 98.28 s; "Our cloud storage" from ≈99.6 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 8c (100.84–103.63 s) – Stage:**
"Same style and palette. The Violet portal fills the frame with a thin line running through it from the bucket on one side to the Snowflake database on the other. Clean and calm. No readable text, no logos."
Overlay (post): "STAGE" at 100.98 s; "Connects Snowflake to the source files" from ≈101.8 s.

**Shot 8d (103.63–106.90 s) – COPY INTO:**
"Same style and palette. A Lime flow runs from the portal into the Ice table, filling its rows. Clean and calm. No readable text, no logos."
Overlay (post): "COPY INTO" at 103.80 s; "Loads the data into Snowflake tables" from ≈105.0 s.

**Audio sync:** card 1 at 98.28 s; card 2 at 100.98 s; card 3 at 103.80 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (106.90–116.00 s · 9.10 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty-Two! Next video lo COPY INTO vs Snowpipe madhya difference real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 22 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (106.90–110.30 s) – Day 22 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, text #F7F9FD. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty-two lit in Ice (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 22" from ≈107.8 s; the twenty-second node lights at ≈109.4 s on "Twenty-Two".

**Shot 9b (110.30–116.00 s) – teaser: COPY INTO vs Snowpipe:**
"Same style and palette. A teaser panel slides in with two glass paths side by side from the Copper bucket to the Ice table: on the left a Lime flow that starts with a cursor click (a manual command), on the right a Lime flow that runs by itself with a small glowing pipe glyph. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: COPY INTO vs SNOWPIPE" from ≈111.2 s; "DIFFERENCE" from ≈113.4 s; "REAL-TIME EXAMPLES" from ≈114.2 s. The visual only suggests two different paths. Do not show how Snowpipe works, settings or numbers.

**Audio sync:** card at ≈107.8 s; the twenty-second node at ≈109.4 s; the teaser title at ≈111.2 s.
**Negative prompt:** "Technical claims about Snowpipe, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (116.00–127.48 s · 11.48 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (116.00–121.95 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, text #F7F9FD. A calm, clean background with a soft slate glow, a small Copper bucket, a Lime pipeline and an Ice table drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈117.4 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈118.4 s, emphasised at ≈120.8 s on "Follow" (estimated).

**Shot 10b (121.95–125.36 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Copper and Ice glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 122.10 s, emphasised at ≈124.4 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (125.36–127.48 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 125.51 s. Hold the final frame for the last 0.35 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 22. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #0F172A, S3 Bucket Copper #F2994A, Stage Violet #A78BFA, Snowflake Ice #6FD0FF, Data Lime #B7F04A, Cloud Glass #E8EEF8, text #F7F9FD, secondary text #9AA6BE. Colour code: the AWS S3 bucket and its CSV files = Copper glass (a generic cloud-bucket glyph, never an AWS logo); the file format = a Cloud Glass template card with a grid glyph; the storage integration = a Violet key on a Violet bridge; the external stage = a Violet portal window; COPY INTO = a Lime flow of data blocks; the Snowflake database and CUSTOMER table = Ice glass. The path always reads left to right: Copper bucket → Violet bridge and portal → Lime flow → Ice table. Show the six steps in the script's order: create a bucket, upload files, create a file format, create a storage integration, create an external stage, COPY INTO. Never show real AWS or Snowflake logos, readable data, or numbers beyond the script. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–21: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day22.mp3` (127.48 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, step badges, the three SQL statements, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Write the quote character in `FIELD_OPTIONALLY_ENCLOSED_BY = '"';` exactly as in the script. Do not use real AWS logos.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a soft file-drop, a key click for the integration, a flow whoosh for COPY INTO) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start (the opening line, 0–3.6 s), at "Definitely not" (14.69 s), at each step badge (29.38, 32.76, 36.66, 39.96, 44.28, 46.97 s), at each SQL statement start (63.80, 73.19, 87.06 s), at "Anthe!" (91.18 s), at the recap cards (98.28, 100.98, 103.80 s), at the final tagline (125.51 s), and at the Follow and Contact lines (≈120.8, ≈124.4 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: the main steps to load data from AWS S3 to Snowflake are creating a bucket, uploading data files, creating a FILE FORMAT, creating a STORAGE INTEGRATION to connect to S3, creating an EXTERNAL STAGE, and using COPY INTO to load the data into a table. In the banking example, CSV files land in an S3 bucket, a file format and a stage are created, and COPY INTO loads the CUSTOMER table. The SQL statements from the script are valid Snowflake syntax. **No other options, permissions or settings** are shown.
- **The script's "automate" line:** the six steps set up a repeatable load, but COPY INTO is a command that is run. Fully automatic loading is the topic of the next video (COPY INTO vs Snowpipe), so the visuals show "automate" only as a pipeline being drawn.
- **Optional addition (not in the script, so not shown on screen):** the example uses `MY_S3_INTEGRATION`, but the script does not show the `CREATE STORAGE INTEGRATION` statement or the AWS-side access setup. The visuals show the integration as already existing. You may want to mention that in the caption; please verify the details against Snowflake's current documentation first.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
