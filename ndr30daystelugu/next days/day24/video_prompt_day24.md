# Thirty Days of Snowflake – Day 24: Snowpipe Auto-Ingest
Video prompt package (NDR EdTech) — `Audio\day24.mp3` + `days-scripts\day24.txt`, analysed with Whisper

> **Timing status: MEASURED from day24.mp3 (124.53 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio otherwise matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (5 items):**
> 1. **SQL correctness (important):** the script's statement includes `INTEGRATION = 'S3_NOTIFICATION_INT'`. In Snowflake's `CREATE PIPE`, the `INTEGRATION` parameter is, to my knowledge, used for **Google Pub/Sub and Azure Event Grid**, not for **Amazon S3**. For S3 you create the pipe with `AUTO_INGEST = TRUE`, then run `SHOW PIPES` and copy the pipe's SQS queue (the `notification_channel` column) into the S3 bucket's event notification. **Please check Snowflake's current documentation.** I have kept the on-screen code exactly as narrated (so it matches the audio), but if you agree it is wrong, the best fix is to re-record that line and remove the `INTEGRATION` line from the overlay. I have **not** changed your wording.
> 2. **The opening (0–3 s):** the line "Andaru ela unnaru?" was removed from this recording (you confirmed this), so the opening is "Hello guys! … Oka real-time scenario imagine cheyyandi!" ("Hello guys!" 0.00–0.77 s, then one phrase 1.08–3.04 s). Your `days-scripts\day24.txt` still contains the removed line; the package follows the audio.
> 3. **The SQL chunks (81–91 s):** the narration pauses between pieces of the statement, but the exact boundaries inside "AS COPY INTO TRANSACTIONS FROM @TRANSACTION_STAGE;" (88.55–91.11 s) are estimated (≈).
> 4. **Follow and Contact lines (about 113–122 s):** Whisper's word order is unreliable, so the "Follow" and "Contact" times are estimated (≈).
> 5. **There is no scripted `[pause]`** in this script. The longest pause is 0.6 s.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 24: Snowpipe Auto-Ingest |
| Duration | **124.53 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,736 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day24.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (29 shots in 11 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Event Relay" (new for Day 24)
| Role | HEX | Use |
|---|---|---|
| Background | `#1D1B16` | Base, gradients (dark taupe-olive) |
| S3 Bucket Gold | `#FFAA33` | **AWS S3**: the storage where files land |
| Event Coral | `#FF6B57` | The **S3 event notification** (a spark and a bell) |
| Queue Sky | `#4CC9FF` | **Amazon SQS**: the queue that delivers the notification |
| Pipe Mint | `#3DE8A5` | **Snowpipe**: receives the notification and loads the data |
| Cloud Glass | `#EDF1F7` | The Snowflake table, SQL panels, neutral glass |
| Primary text | `#F8F7F2` | Titles, labels |
| Secondary text | `#A8A596` | Captions |

**Colour code (use in every scene):** the relay always runs left to right: **Gold bucket → Coral spark/bell → Sky queue → Mint pipe → Cloud Glass table**. Files are small Gold cards; notifications are small Coral envelopes.

**The core visual rule (technical accuracy):** Snowpipe Auto-Ingest is an **event-driven mechanism** with **four components**: **AWS S3** (where files land), **S3 event notification** (generates an event when a new file is uploaded), **Amazon SQS** (delivers the file notification to Snowflake) and **Snowpipe** (receives the notification and triggers the COPY INTO process). The order never changes. No user presses a run button: there is **no cursor** in the relay. Show "every 5 minutes" only as the script's example. Use a **generic cloud-bucket glyph** and write "AWS S3" and "Amazon SQS" as overlays; **do not draw AWS logos**.

### Motion effects used (from the skill's effects library)
Post wall, Orbit ring, Live cursor, Code body, Press font, Head stack, Rack focus, Comment drop, Impact frame, Letter dive, Liquid glass. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–3.26 | "Hello guys! … Oka real-time scenario imagine cheyyandi!" (0.00–3.04) | Curious | Title hook |
| 2 | 3.26–19.63 | "Mee company ki AWS S3 bucket lo every 5 minutes ki new transaction files land avuthunnayi." (3.48–8.94) · "Prathi sari Data Engineer login ayyi COPY INTO execute chesthu untara?" (9.37–13.24) · "Definitely not!" (13.64–14.66) · "Mari new files vachinappudu Snowflake automatic ga data load cheyyalante ela?" (15.16–19.41) | Curious, then firm | Files every 5 minutes, not manually, how automatically? |
| 3 | 19.63–23.22 | "Adhe Snowpipe Auto-Ingest!" (19.85–21.92) · "Let's understand!" (22.24–23.04) | Excited, reveal | Title reveal |
| 4 | 23.22–25.26 | "Welcome to NDR EdTech!" (23.40–25.08) | Welcoming | Brand welcome |
| 5 | 25.26–35.96 | "Snowpipe Auto-Ingest anedhi AWS S3 nunchi Snowflake ki files automatic ga load cheyyadaniki use chese event-driven mechanism." (25.44–33.28) · "Indhulo main ga four components untayi." (33.72–35.73) | Clear | Event-driven mechanism, four components |
| 6 | 35.96–56.75 | "First, AWS S3 – files land ayye storage location." (36.19–39.75) · "Second, S3 Event Notification – new file upload ayinappudu event generate chesthundhi." (40.14–45.36) · "Third, Amazon SQS – file notification ni Snowflake ki deliver cheyyadaniki use avuthundhi." (45.76–51.06) · "Fourth, Snowpipe – notification receive chesi COPY INTO process ni trigger chesthundhi." (51.52–56.50) | Clear, structured | Four numbered components |
| 7 | 56.75–80.83 | "Oka Banking project example teesukundham." (56.99–58.97) · "Mana TRANSACTIONS.csv file AWS S3 bucket lo upload ayyindhi." (59.37–63.36) · "S3 event notification generate avuthundhi." (63.78–65.99) · "Aa notification Amazon SQS ki velthundhi." (66.35–68.95) · "Snowpipe notification receive cheskoni, corresponding file ni Snowflake TRANSACTIONS table loki load chesthundhi." (69.33–75.20) · "Ila manam manual ga COPY INTO execute cheyyakundane automated ingestion setup cheyyachu." (75.60–80.57) | Storytelling | Banking: the file travels the relay |
| 8 | 80.83–91.25 | "CREATE PIPE TRANSACTION_PIPE" (81.08–82.88) · "AUTO_INGEST = TRUE" (83.32–84.82) · "INTEGRATION = 'S3_NOTIFICATION_INT'" (85.15–88.22) · "AS COPY INTO TRANSACTIONS FROM @TRANSACTION_STAGE;" (88.55–91.11) | Focused | The pipe statement builds line by line |
| 9 | 91.25–104.60 | "So, simple ga gurthupettukondi!" (91.39–92.61) · "S3 – Stores files." (93.06–96.56) · "S3 Event Notification – Detects new files." (96.81–99.41) · "SQS – Delivers notifications." (99.72–101.77) · "Snowpipe – Loads data automatically." (102.07–104.40) | Confident | Four-card recap |
| 10 | 104.60–113.30 | "Idi mana Thirty Days of Snowflake series lo Day Twenty-Four!" (104.80–107.92) · "Next video lo Snowflake Streams gurinchi real-time CDC example tho explain chesthanu." (108.26–113.13) | Upbeat | Day 24 card, Streams and CDC teaser |
| 11 | 113.30–124.53 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (113.47–119.02) · "Full course details kosam NDR EdTech ni Contact avvandi!" (119.34–122.35) · "Let's Learn and Grow Together!" (122.63–124.26) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.77–1.08, 3.04–3.48, 8.94–9.37, 13.24–13.64, 14.66–15.16, 19.41–19.85, 20.12–20.43, 21.92–22.24, 23.04–23.40, 25.08–25.44, 33.28–33.72, 35.73–36.19, 36.59–36.84, 37.65–37.98, 39.75–40.14, 40.57–40.89, 42.37–42.69, 45.36–45.76, 46.04–46.30, 47.46–47.73, 51.06–51.52, 51.87–52.09, 52.59–52.95, 56.50–56.99, 58.97–59.37, 63.36–63.78, 65.99–66.35, 68.95–69.33, 75.20–75.60, 78.49–78.73, 80.57–81.08, 81.71–82.10, 82.88–83.32, 84.82–85.15, 86.24–86.51, 88.22–88.55, 88.88–89.15, 90.53–90.82, 91.11–91.39, 92.61–93.06, 94.86–95.19, 96.56–96.81, 99.41–99.72, 101.77–102.07, 102.59–102.88, 104.40–104.80, 107.92–108.26, 113.13–113.47, 119.02–119.34, 122.35–122.63, 124.26–124.53.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee company ki AWS S3 bucket lo every 5 minutes ki new transaction files land avuthunnayi. | AWS S3 bucket ≈4.6 · **every 5 minutes** ≈5.8–7.0 · new transaction files ≈7.4 · land ≈8.4 |
| Prathi sari Data Engineer login ayyi COPY INTO execute chesthu untara? | Data Engineer ≈10.0 · login ≈11.0 · COPY INTO execute ≈11.8 |
| Definitely not! | Definitely not 13.64 |
| Mari new files vachinappudu Snowflake automatic ga data load cheyyalante ela? | new files ≈15.8 · automatic ga ≈17.2 · ela ≈18.8 |
| Adhe Snowpipe Auto-Ingest! | Adhe 19.85 · Snowpipe Auto-Ingest 20.43 |
| Let's understand! / Welcome to NDR EdTech! | Let's 22.24 · Welcome 23.40 · NDR ≈24.0 · EdTech ≈24.5 |
| Snowpipe Auto-Ingest anedhi AWS S3 nunchi Snowflake ki files automatic ga load cheyyadaniki use chese event-driven mechanism. | Snowpipe Auto-Ingest ≈25.8 · AWS S3 ≈28.0 · files ≈30.0 · event-driven mechanism ≈31.6 |
| Indhulo main ga four components untayi. | four components ≈34.6 |
| First, AWS S3 – files land ayye storage location. | First 36.19 · AWS S3 36.84 · storage location ≈38.6 |
| Second, S3 Event Notification – new file upload ayinappudu event generate chesthundhi. | Second 40.14 · S3 Event Notification 40.89 · new file upload ≈43.0 · event generate ≈44.4 |
| Third, Amazon SQS – file notification ni Snowflake ki deliver cheyyadaniki use avuthundhi. | Third 45.76 · Amazon SQS 46.30 · deliver ≈49.0 |
| Fourth, Snowpipe – notification receive chesi COPY INTO process ni trigger chesthundhi. | Fourth 51.52 · Snowpipe 52.09 · notification receive ≈53.2 · COPY INTO ≈54.4 · trigger ≈55.6 |
| Mana TRANSACTIONS.csv file AWS S3 bucket lo upload ayyindhi. | TRANSACTIONS.csv ≈60.0 · AWS S3 bucket ≈61.4 · upload ≈62.5 |
| S3 event notification generate avuthundhi. | S3 event notification 63.78 · generate ≈65.0 |
| Aa notification Amazon SQS ki velthundhi. | notification ≈66.8 · Amazon SQS ≈67.6 · velthundhi ≈68.5 |
| Snowpipe notification receive cheskoni, corresponding file ni Snowflake TRANSACTIONS table loki load chesthundhi. | Snowpipe ≈69.6 · notification receive ≈70.8 · corresponding file ≈72.0 · TRANSACTIONS table ≈73.4 · load ≈74.6 |
| Ila manam manual ga COPY INTO execute cheyyakundane automated ingestion setup cheyyachu. | manual ga COPY INTO ≈76.6 · automated ingestion ≈78.8 |
| CREATE PIPE TRANSACTION_PIPE | CREATE PIPE 81.08 · TRANSACTION_PIPE 82.10 |
| AUTO_INGEST = TRUE | AUTO_INGEST 83.32 · TRUE ≈84.4 |
| INTEGRATION = 'S3_NOTIFICATION_INT' | INTEGRATION 85.15 · 'S3_NOTIFICATION_INT' 86.51 |
| AS COPY INTO TRANSACTIONS FROM @TRANSACTION_STAGE; | AS 88.55 · COPY INTO TRANSACTIONS ≈89.2 · FROM @TRANSACTION_STAGE ≈90.3 |
| So, simple ga gurthupettukondi! | So 91.39 · gurthupettukondi ≈91.9 |
| S3 – Stores files. | S3 93.06 · Stores files 95.19 |
| S3 Event Notification – Detects new files. | S3 Event Notification 96.81 · Detects new files ≈98.0 |
| SQS – Delivers notifications. | SQS ≈99.72 · Delivers notifications ≈100.4 |
| Snowpipe – Loads data automatically. | Snowpipe 102.07 · Loads data automatically 102.88 |
| Idi mana Thirty Days of Snowflake series lo Day Twenty-Four! | Thirty ≈105.6 · Snowflake ≈106.3 · Twenty-Four ≈107.0 |
| Next video lo Snowflake Streams gurinchi real-time CDC example tho explain chesthanu. | Snowflake Streams ≈109.2–110.2 · real-time CDC example ≈111.0 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈115.4 · NDR EdTech ≈116.4–117.6 · **Follow** ≈118.0 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 119.34–120.6 · NDR EdTech ≈120.8 · **Contact** ≈121.6 (estimated) |
| Let's Learn and Grow Together! | Let's 122.63 · Together ≈123.7 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2.*

**Object look (keep identical in every scene):** **AWS S3** = a Gold glass bucket (generic cloud-storage glyph, no AWS logo) holding small Gold file cards. **S3 event notification** = a Coral spark with a small bell. **Amazon SQS** = a Sky glass queue lane (a short conveyor with a few small envelopes, generic, no logo). **Snowpipe** = a Mint glass pipe. **Snowflake table** = a Cloud Glass table block with rows of cells. The relay runs left to right, and there is **no cursor**.

### Scene 1 – Hook (0.00–3.26 s · 3.26 s)
**Voice-over:** "Hello guys! Oka real-time scenario imagine cheyyandi!"
**Tone:** curious.
**Visual objective:** Welcome viewers and introduce a real-time scenario.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2. A dark taupe space with soft light and drifting glass particles. Four small glowing glass objects, a Gold bucket, a Coral spark, a Sky queue and a Mint pipe, line up in a gentle arc at the upper-centre, linked by a thin light line. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–0.77 s: particles drift in on "Hello guys!".
- 1.08–3.04 s: the four objects appear one by one and the light line draws between them on "Oka real-time scenario imagine cheyyandi!".
- 3.04–3.26 s: soft light sweep into Scene 2.
- Effect: **Orbit ring** — a soft ring circles the four objects once.
**Audio sync:** title lands at ≈1.2 s; the sweep completes in the pause at 3.04–3.48 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 24".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, real AWS or Snowflake logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – New files every 5 minutes (3.26–19.63 s · 16.37 s)
**Voice-over:** "Mee company ki AWS S3 bucket lo every 5 minutes ki new transaction files land avuthunnayi. Prathi sari Data Engineer login ayyi COPY INTO execute chesthu untara? Definitely not! Mari new files vachinappudu Snowflake automatic ga data load cheyyalante ela?"
**Tone:** curious, then firm.
**Visual objective:** New files land every few minutes; nobody should log in and run COPY INTO each time; so how can the load happen automatically?
Generate as **three shots (2a–2c)**.

**Shot 2a (3.26–9.16 s) – new transaction files every 5 minutes:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Cloud Glass #EDF1F7, text #F8F7F2. A Gold glass bucket (generic cloud-storage glyph, no logo) sits at the centre. Every second or so a new small Gold file card lands in it with a soft pulse, while a glass clock-dial (no numerals) ticks a short arc each time to suggest a repeating five-minute rhythm. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 3.48–4.6 s the bucket appears on "Mee company ki"; ≈4.6–7.0 s the first cards land and the clock ticks on "AWS S3 bucket lo every 5 minutes ki" (every 5 minutes ≈5.8 s); ≈7.4–8.94 s more cards land on "new transaction files land avuthunnayi". **Effect: Post wall** — the landed cards build into a wall inside the bucket.
Overlay (post): "AWS S3 BUCKET" at ≈4.6 s; "EVERY 5 MINUTES" at ≈5.8 s; "NEW TRANSACTION FILES" from ≈7.4 s.

**Shot 2b (9.16–13.44 s) – log in and run COPY INTO every time?:**
"Same style and palette. A glass cursor logs in at a small glowing login window and presses a 'run' button, again and again, while new file cards keep landing in the bucket faster than the cursor can keep up. A soft Coral 'tired' pulse spreads over the repeated action. No readable text, no logos, no watermark."
Motion: 9.37–10.8 s the login window appears on "Prathi sari Data Engineer login ayyi" (login ≈11.0 s); ≈11.0–13.24 s the cursor presses run repeatedly on "COPY INTO execute chesthu untara?". **Effect: Live cursor.**
Overlay (post): "LOG IN AND RUN COPY INTO EVERY TIME?" from 9.37 s.

**Shot 2c (13.44–19.63 s) – definitely not; how to load automatically?:**
"Same style and palette. A soft Coral barrier flashes over the login window and the cursor fades away. Then a single new file card lands in the bucket and a faint glowing path starts to light up all by itself between the bucket and a Cloud Glass table, with a soft question-mark glow above it. Firm, then curious. No readable text, no logos, no watermark."
Motion: 13.64–14.66 s the barrier flashes on "Definitely not!" (**Effect: Impact frame** — a one-frame flash at 13.64 s); 15.16–17.2 s a new file lands and the path starts to light on "Mari new files vachinappudu Snowflake automatic ga" (new files ≈15.8 s); ≈17.2–19.41 s the question mark pulses on "data load cheyyalante ela?".
Overlay (post): "DEFINITELY NOT!" at 13.64 s; "HOW TO LOAD AUTOMATICALLY WHEN NEW FILES ARRIVE?" from 15.16 s.

**Audio sync:** cards at ≈5.8 s; login at 9.37 s; flash at 13.64 s; new file at ≈15.8 s.
**Negative prompt (all shots):** "Real AWS logos, readable text, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Snowpipe Auto-Ingest (19.63–23.22 s · 3.59 s)
**Voice-over:** "Adhe Snowpipe Auto-Ingest! Let's understand!"
**Tone:** excited, reveal.
**Visual objective:** Name the answer and the topic.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2. The faint path lights up fully into the whole relay (Gold bucket, Coral spark, Sky queue, Mint pipe, Cloud Glass table) in a neat horizontal line under a glowing glass snowflake-crystal emblem. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 19.85–20.12 s: a soft glow on "Adhe".
- 20.43–21.92 s: the relay lights up from left to right and the title lands on "Snowpipe Auto-Ingest!" (**Effect: Impact frame** — one-frame flash at 20.43 s; **Effect: Letter dive** — the letters settle fully before 21.8 s).
- 22.24–23.04 s: a subtitle pops in on "Let's understand!".
**Audio sync:** glow at 19.85 s; title at 20.43 s; subtitle at 22.24 s.
**On-screen text (overlay, post):** "SNOWPIPE AUTO-INGEST" at 20.43 s; "LET'S UNDERSTAND!" at 22.24 s.
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Welcome (23.22–25.26 s · 2.04 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Pipe Mint #3DE8A5, Queue Sky #4CC9FF, text #F8F7F2. A calm, clean welcome frame with a reserved clean area at the top for the logo and a soft golden glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 23.40–25.08 s the glow blooms softly and a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 23.40 s; "NDR" at ≈24.0 s; "EdTech" at ≈24.5 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – An event-driven mechanism with four components (25.26–35.96 s · 10.70 s)
**Voice-over:** "Snowpipe Auto-Ingest anedhi AWS S3 nunchi Snowflake ki files automatic ga load cheyyadaniki use chese event-driven mechanism. Indhulo main ga four components untayi."
**Tone:** clear.
**Visual objective:** Snowpipe Auto-Ingest is an event-driven mechanism that loads files from AWS S3 into Snowflake automatically, and it has four main components.
Generate as **two shots (5a, 5b)**.

**Shot 5a (25.26–33.50 s) – event-driven automatic loading:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2. On the left the Gold bucket, on the right a Cloud Glass snowflake-crystal database. A new Gold file card lands in the bucket; a Coral spark and bell fire; and, with no cursor, the file travels across to the database along a glowing path. The spark makes the whole thing look 'event-driven': when an event happens, the load follows. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 25.44–27.4 s the bucket and the database appear on "Snowpipe Auto-Ingest anedhi" (Snowpipe Auto-Ingest ≈25.8 s); ≈28.0–30.0 s a file lands and the path lights on "AWS S3 nunchi Snowflake ki files" (AWS S3 ≈28.0 s); ≈30.0–33.28 s the spark fires and the file arrives on "automatic ga load cheyyadaniki use chese event-driven mechanism" (event-driven mechanism ≈31.6 s). **Effect: Orbit ring** — a Coral ring circles the spark at ≈31.6 s.
Overlay (post): "SNOWPIPE AUTO-INGEST" from ≈25.8 s; "AWS S3 → SNOWFLAKE, AUTOMATICALLY" from ≈28.0 s; "EVENT-DRIVEN MECHANISM" from ≈31.6 s.

**Shot 5b (33.50–35.96 s) – four components:**
"Same style and palette. Four glass tiles rise one after another in a neat vertical stack: a Gold bucket, a Coral spark with a bell, a Sky queue and a Mint pipe. Clean, uncluttered, phone-readable layout. No readable fine text, no logos, no watermark."
Motion: 33.72–34.6 s the first tiles rise on "Indhulo main ga"; ≈34.6–35.73 s the stack completes on "four components untayi" (four components ≈34.6 s). **Effect: Head stack.**
Overlay (post): "4 COMPONENTS" from ≈34.6 s.

**Audio sync:** spark at ≈31.6 s; the four tiles from ≈34.0 s.
**Negative prompt (all shots):** "Real AWS logos, a cursor or run button, readable fine text, extra components, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – The four components (35.96–56.75 s · 20.79 s)
**Voice-over:** "First, AWS S3 – files land ayye storage location. Second, S3 Event Notification – new file upload ayinappudu event generate chesthundhi. Third, Amazon SQS – file notification ni Snowflake ki deliver cheyyadaniki use avuthundhi. Fourth, Snowpipe – notification receive chesi COPY INTO process ni trigger chesthundhi."
**Tone:** clear, structured.
**Visual objective:** One shot per component, each added to the same relay.
Generate as **four shots (6a–6d)**. Keep the relay layout and badge position identical so the components stack up into one chain.

**Shot 6a (35.96–39.95 s) – 1 · AWS S3, where files land:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Cloud Glass #EDF1F7, text #F8F7F2. A Gold glass bucket (generic cloud-storage glyph, no logo) is assembled at the left of the frame; small Gold file cards land in it one by one. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 36.19–36.59 s the badge appears on "First,"; 36.84–37.65 s the bucket assembles on "AWS S3" (**Effect: Press font** — "AWS S3" presses in at 36.84 s); 37.98–39.75 s the cards land on "files land ayye storage location" (storage location ≈38.6 s).
Overlay (post): "1 · AWS S3" at 36.19 s; "STORAGE LOCATION WHERE FILES LAND" from 37.98 s.

**Shot 6b (39.95–45.56 s) – 2 · S3 event notification:**
"Same style and palette, plus Event Coral #FF6B57. A new Gold file card lands in the bucket and, at that moment, a Coral spark flashes beside the bucket and a small Coral envelope (the event) pops out of it. A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark."
Motion: 40.14–40.57 s the badge appears on "Second,"; 40.89–42.37 s the spark glows on "S3 Event Notification" (**Effect: Press font** — "S3 EVENT NOTIFICATION" presses in at 40.89 s); ≈43.0–44.4 s a new file lands on "new file upload ayinappudu"; ≈44.4–45.36 s the envelope pops out on "event generate chesthundhi".
Overlay (post): "2 · S3 EVENT NOTIFICATION" at 40.14 s; "GENERATES AN EVENT WHEN A NEW FILE IS UPLOADED" from ≈43.0 s.

**Shot 6c (45.56–51.29 s) – 3 · Amazon SQS:**
"Same style and palette, plus Queue Sky #4CC9FF. The Coral envelope slides onto a Sky glass queue lane (a short conveyor with a few waiting envelopes, generic, no logo) and travels along it toward the Snowflake side. A numbered badge '3'. Calm, clear. No readable text, no logos, no watermark."
Motion: 45.76–46.04 s the badge appears on "Third,"; 46.30–47.46 s the queue lane appears on "Amazon SQS" (**Effect: Press font** — "AMAZON SQS" presses in at 46.30 s); 47.73–51.06 s the envelope travels along the lane on "file notification ni Snowflake ki deliver cheyyadaniki use avuthundhi" (deliver ≈49.0 s). **Effect: Post wall** — a few envelopes wait in the queue.
Overlay (post): "3 · AMAZON SQS" at 45.76 s; "DELIVERS THE FILE NOTIFICATION TO SNOWFLAKE" from ≈47.8 s.

**Shot 6d (51.29–56.75 s) – 4 · Snowpipe:**
"Same style and palette, plus Pipe Mint #3DE8A5. The envelope reaches a Mint glass pipe at the Snowflake side. The pipe opens it, lights up, and a flow of data blocks starts through it into a Cloud Glass table. A numbered badge '4'. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 51.52–51.87 s the badge appears on "Fourth,"; 52.09–52.59 s the pipe lights on "Snowpipe" (**Effect: Press font** — "SNOWPIPE" presses in at 52.09 s); 52.95–54.4 s the envelope is received on "notification receive chesi"; ≈54.4–56.5 s the flow starts into the table on "COPY INTO process ni trigger chesthundhi" (COPY INTO ≈54.4 s, trigger ≈55.6 s). **Effect: Rack focus** — focus pulls from the envelope to the flowing pipe at ≈54.4 s.
Overlay (post): "4 · SNOWPIPE" at 51.52 s; "RECEIVES THE NOTIFICATION" from ≈53.2 s; "TRIGGERS THE COPY INTO PROCESS" from ≈54.4 s.

**Audio sync:** badge 1 at 36.19 s; badge 2 at 40.14 s; badge 3 at 45.76 s; badge 4 at 51.52 s.
**Negative prompt (all shots):** "Real AWS or Snowflake logos, a cursor or run button, readable fine text, wrong component order, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (56.75–80.83 s · 24.08 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana TRANSACTIONS.csv file AWS S3 bucket lo upload ayyindhi. S3 event notification generate avuthundhi. Aa notification Amazon SQS ki velthundhi. Snowpipe notification receive cheskoni, corresponding file ni Snowflake TRANSACTIONS table loki load chesthundhi. Ila manam manual ga COPY INTO execute cheyyakundane automated ingestion setup cheyyachu."
**Tone:** storytelling.
**Visual objective:** One TRANSACTIONS.csv file travels the whole relay with no manual step.
Generate as **six shots (7a–7f)**. All shots use the same camera language and layout (bucket on the left, queue in the middle, pipe and table on the right).

**Shot 7a (56.75–59.17 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2. A sleek abstract Cloud Glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with the empty relay layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈57.2 s.

**Shot 7b (59.17–63.57 s) – TRANSACTIONS.csv uploaded to S3:**
"Same style and palette. A single Gold file card with a small CSV glyph (comma-separated columns, no readable data) slides into the Gold bucket and lands with a soft pulse. No readable fine text, no logos."
Overlay (post): "TRANSACTIONS.CSV" at ≈60.0 s (monospace); "UPLOADED TO THE AWS S3 BUCKET" from ≈61.4 s.

**Shot 7c (63.57–66.17 s) – the S3 event notification is generated:**
"Same style and palette. As the file lands, a Coral spark flashes beside the bucket and a Coral envelope pops out. No readable fine text, no logos."
Motion: 63.78–65.0 s the spark flashes on "S3 event notification"; ≈65.0–65.99 s the envelope pops out on "generate avuthundhi".
Overlay (post): "S3 EVENT NOTIFICATION GENERATED" from 63.78 s.

**Shot 7d (66.17–69.14 s) – the notification goes to Amazon SQS:**
"Same style and palette. The Coral envelope slides along a thin line into the Sky queue lane and waits in it. No readable fine text, no logos."
Motion: 66.35–67.6 s the envelope travels on "Aa notification"; ≈67.6–68.95 s it enters the queue on "Amazon SQS ki velthundhi".
Overlay (post): "NOTIFICATION → AMAZON SQS" from 66.35 s.

**Shot 7e (69.14–75.40 s) – Snowpipe receives it and loads the file:**
"Same style and palette. The envelope moves from the queue to the Mint pipe, which opens it and then pulls the matching Gold file card from the bucket through itself into the Cloud Glass TRANSACTIONS table. The table's rows fill with glowing cells. No readable fine text, no logos."
Motion: 69.33–70.8 s the envelope reaches the pipe on "Snowpipe notification receive cheskoni" (Snowpipe ≈69.6 s); ≈72.0 s the file card is matched on "corresponding file ni"; ≈73.4–75.2 s the table fills on "Snowflake TRANSACTIONS table loki load chesthundhi". **Effect: Rack focus** — focus pulls from the queue to the pipe at ≈70.8 s.
Overlay (post): "SNOWPIPE RECEIVES THE NOTIFICATION" from ≈70.8 s; "CORRESPONDING FILE LOADED INTO THE TRANSACTIONS TABLE" from ≈72.0 s.

**Shot 7f (75.40–80.83 s) – no manual COPY INTO, automated ingestion:**
"Same style and palette. The whole relay glows as one calm line from the bucket to the table. In the corner a faint 'run' button with a cursor appears and fades away, unused. A soft Mint glow spreads along the line. Satisfying. No readable fine text, no logos."
Motion: 75.60–77.4 s the faint button appears and fades on "Ila manam manual ga COPY INTO execute cheyyakundane" (manual ga COPY INTO ≈76.6 s); ≈78.8–80.57 s the Mint glow spreads on "automated ingestion setup cheyyachu" (automated ingestion ≈78.8 s). **Effect: Comment drop** — a small Mint note drops in beside the line at ≈78.8 s.
Overlay (post): "NO MANUAL COPY INTO" from ≈76.6 s; "AUTOMATED INGESTION" from ≈78.8 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, real AWS logos, readable personal data, readable fake text in the generated video, a cursor in the relay, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – SQL: CREATE PIPE (80.83–91.25 s · 10.42 s)
**Voice-over:** "CREATE PIPE TRANSACTION_PIPE AUTO_INGEST = TRUE INTEGRATION = 'S3_NOTIFICATION_INT' AS COPY INTO TRANSACTIONS FROM @TRANSACTION_STAGE;"
**Tone:** focused.
**Visual objective:** The pipe statement is built line by line. (See note 1 at the top about the INTEGRATION line.)
Generate as **three shots (8a–8c)**.

**Shot 8a (80.83–84.99 s) – CREATE PIPE and AUTO_INGEST:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, Pipe Mint #3DE8A5, Event Coral #FF6B57, Cloud Glass #EDF1F7, text #F8F7F2. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) slides in at the centre with a thin Mint edge. Behind it, softly out of focus, the relay glows. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 81.08–81.71 s the first words type on "CREATE PIPE"; 82.10–82.88 s the name types on "TRANSACTION_PIPE"; 83.32–84.82 s line 2 types on "AUTO_INGEST = TRUE" and a Coral spark glows beside the line. **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE PIPE TRANSACTION_PIPE
AUTO_INGEST = TRUE
```
"CREATE PIPE" at 81.08 s; "TRANSACTION_PIPE" at 82.10 s; "AUTO_INGEST = TRUE" at 83.32 s.

**Shot 8b (84.99–88.39 s) – INTEGRATION:**
"Same style and palette. The code panel continues. A small Queue Sky glass key glows beside the line. No readable code, no logos, no watermark."
Motion: 85.15–86.24 s the keyword types on "INTEGRATION"; 86.51–88.22 s the value types on "= 'S3_NOTIFICATION_INT'". **Effect: Code body.**
Overlay (post, monospace; append, exactly as narrated):
```sql
INTEGRATION = 'S3_NOTIFICATION_INT'
```
"INTEGRATION" at 85.15 s; "= 'S3_NOTIFICATION_INT'" at 86.51 s. **Check note 1 at the top of this file before you publish this line.**

**Shot 8c (88.39–91.25 s) – AS COPY INTO:**
"Same style and palette. The code panel finishes the statement. The Mint pipe, the table and the stage connect with a thin Mint line, and a data flow runs into the table. No readable code, no logos, no watermark."
Motion: 88.55–88.88 s the keyword types on "AS"; ≈89.2–90.5 s the next line types on "COPY INTO TRANSACTIONS"; ≈90.5–91.11 s the last line types on "FROM @TRANSACTION_STAGE;". **Effect: Code body.**
Overlay (post, monospace; the full statement shown at the end, exactly as narrated):
```sql
CREATE PIPE TRANSACTION_PIPE
AUTO_INGEST = TRUE
INTEGRATION = 'S3_NOTIFICATION_INT'
AS
COPY INTO TRANSACTIONS
FROM @TRANSACTION_STAGE;
```
"AS" at 88.55 s; "COPY INTO TRANSACTIONS" at ≈89.2 s; "FROM @TRANSACTION_STAGE;" at ≈90.3 s.

**Audio sync:** every statement part starts at its pause end (81.08, 82.10, 83.32, 85.15, 86.51, 88.55 s); inner times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Readable fake code in the generated video, wrong syntax, extra lines, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Simple recap (91.25–104.60 s · 13.35 s)
**Voice-over:** "So, simple ga gurthupettukondi! S3 – Stores files. S3 Event Notification – Detects new files. SQS – Delivers notifications. Snowpipe – Loads data automatically."
**Tone:** confident.
**Visual objective:** Four-card recap.
Generate as **four shots (9a–9d)**.

**Shot 9a (91.25–96.69 s) – keep it simple; S3 stores files:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, text #F8F7F2. The four relay objects glide into a neat row at the centre with a soft bloom, then the Gold bucket comes forward and fills the frame with file cards inside. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈91.5 s; "S3" at 93.06 s; "Stores files" from 95.19 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 9b (96.69–99.57 s) – S3 event notification detects new files:**
"Same style and palette. The Coral spark and bell fill the frame; a new file card lands and the spark flashes. Clean and calm. No readable text, no logos."
Overlay (post): "S3 EVENT NOTIFICATION" at 96.81 s; "Detects new files" from ≈98.0 s.

**Shot 9c (99.57–101.92 s) – SQS delivers notifications:**
"Same style and palette. The Sky queue lane fills the frame with an envelope sliding along it toward the Snowflake side. Clean and calm. No readable text, no logos."
Overlay (post): "SQS" at ≈99.72 s; "Delivers notifications" from ≈100.4 s.

**Shot 9d (101.92–104.60 s) – Snowpipe loads data automatically:**
"Same style and palette. The Mint pipe fills the frame, loading a flow of data blocks into a table by itself with no cursor. Clean and calm. No readable text, no logos."
Overlay (post): "SNOWPIPE" at 102.07 s; "Loads data automatically" from 102.88 s.

**Audio sync:** card 1 at 93.06 s; card 2 at 96.81 s; card 3 at ≈99.72 s; card 4 at 102.07 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Series card and teaser (104.60–113.30 s · 8.70 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty-Four! Next video lo Snowflake Streams gurinchi real-time CDC example tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 24 and tease the next topic.
Generate as **two shots (10a, 10b)**.

**Shot 10a (104.60–108.09 s) – Day 24 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, text #F8F7F2. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty-four lit in Gold (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 24" from ≈105.6 s; the twenty-fourth node lights at ≈107.0 s on "Twenty-Four".

**Shot 10b (108.09–113.30 s) – teaser: Snowflake Streams and CDC:**
"Same style and palette. A teaser panel slides in with a Cloud Glass table block; a few rows change (one added, one edited, one removed) and a thin Mint 'change tracker' glow lists each change in a small side strip. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: SNOWFLAKE STREAMS" from ≈109.2 s; "REAL-TIME CDC EXAMPLE" from ≈111.0 s. The visual only suggests tracking changes in a table. Do not show how Streams work, settings or numbers.

**Audio sync:** card at ≈105.6 s; the twenty-fourth node at ≈107.0 s; the teaser title at ≈109.2 s.
**Negative prompt:** "Technical claims about Streams, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 11 – Follow, contact and end card (113.30–124.53 s · 11.23 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (11a–11c)**.

**Shot 11a (113.30–119.18 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, text #F8F7F2. A calm, clean background with a soft golden glow, the small relay (bucket, spark, queue, pipe) drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈114.6 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈115.4 s, emphasised at ≈118.0 s on "Follow" (estimated).

**Shot 11b (119.18–122.49 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Gold and Mint glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 119.34 s, emphasised at ≈121.6 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 11c (122.49–124.53 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 122.63 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 24. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #1D1B16, S3 Bucket Gold #FFAA33, Event Coral #FF6B57, Queue Sky #4CC9FF, Pipe Mint #3DE8A5, Cloud Glass #EDF1F7, text #F8F7F2, secondary text #A8A596. Colour code: AWS S3 = a Gold glass bucket holding small Gold file cards (a generic cloud-bucket glyph, never an AWS logo); the S3 event notification = a Coral spark with a small bell and a Coral envelope; Amazon SQS = a Sky glass queue lane with waiting envelopes (generic, no logo); Snowpipe = a Mint glass pipe; the Snowflake table = a Cloud Glass block with rows of cells. The relay always runs left to right: Gold bucket → Coral spark/bell → Sky queue → Mint pipe → Cloud Glass table, and there is never a cursor or a run button in it. Never show real AWS or Snowflake logos, readable data, or numbers other than the script's '5 minutes'. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–23: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day24.mp3` (124.53 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, "EVERY 5 MINUTES", "TRANSACTIONS.CSV", the SQL statement, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Do not use real AWS logos. Decide about the `INTEGRATION` line (note 1) before you finish the overlay.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a soft file-drop, a spark chime for the event, a queue slide, a pipe flow) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start (the opening line, 0–3 s), at "every 5 minutes" (≈5.8 s), at "Definitely not" (13.64 s), at the title (20.43 s), at each component badge (36.19, 40.14, 45.76, 51.52 s), at the banking relay (63.78, 66.35, 69.33 s), at each SQL part (81.08, 83.32, 85.15, 88.55 s), at the recap cards (93.06, 96.81, ≈99.72, 102.07 s), at the final tagline (122.63 s), and at the Follow and Contact lines (≈118.0, ≈121.6 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Snowpipe Auto-Ingest is an event-driven mechanism to load files from AWS S3 into Snowflake automatically; its four main components are AWS S3 (where files land), the S3 event notification (generates an event when a new file is uploaded), Amazon SQS (delivers the file notification to Snowflake) and Snowpipe (receives the notification and triggers the COPY INTO process); in the banking example a TRANSACTIONS.csv file travels this relay and is loaded into the TRANSACTIONS table without a manual COPY INTO. **No timings, costs, latencies or other numbers** are shown beyond the script's "every 5 minutes".
- **The `INTEGRATION` line (note 1):** the on-screen code follows the narration exactly. I believe that line is not used for Amazon S3 (it is used for Google Pub/Sub and Azure Event Grid). Please confirm against Snowflake's current documentation and, if you agree, fix the narration and the overlay.
- **Optional addition (not in the script, so not shown on screen):** for an S3 pipe, the SQS queue that Snowflake manages is shown in the pipe's `notification_channel` (via `SHOW PIPES`), and the S3 bucket's event notification must be pointed at it. The script covers the idea but not these setup steps. You may want to mention it in the caption; please verify it first.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
