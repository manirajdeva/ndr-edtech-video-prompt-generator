# Thirty Days of Snowflake – Day 21: Resource Monitors & Warehouse Cost Optimization
Video prompt package (NDR EdTech) — `Audio\day21.mp3` + `days-scripts\day21.txt`, analysed with Whisper

> **Timing status: MEASURED from day21.mp3 (114.99 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio otherwise matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **The opening (0–2.4 s):** the line "Andaru ela unnaru?" was removed from this recording (you confirmed this), so the opening is "Hello guys! … Oka interesting situation!" (0.00–0.69 s and 1.10–2.41 s). Your `days-scripts\day21.txt` still contains the removed line; the package follows the audio.
> 2. **The end of the Contact line (110–113 s)** is garbled in Whisper. The pauses show it as one phrase (110.02–112.85 s). The "Follow" and "Contact" word times are estimated (≈).
> 3. **11.93–13.17 s** is your scripted `[pause]`, a real 1.24 s silence. The visuals hold a calm beat there.
> 4. **The end of this video differs slightly from earlier days:** it announces "Real-Time Data Engineering concepts" and "Day 22: load data from AWS S3 to Snowflake". The teaser follows that.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 21: Resource Monitors & Warehouse Cost Optimization |
| Duration | **114.99 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,450 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day21.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (29 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Credit Meter" (new for Day 21)
| Role | HEX | Use |
|---|---|---|
| Background | `#1E2633` | Base, gradients (steel slate) |
| Compute Blue | `#4DA3FF` | The **virtual warehouse** and its **credits** |
| Safe Lime | `#7CE38B` | Credit usage that is within the limit (safe) |
| Notify Amber | `#FFB938` | The **50% notification** (a bell) |
| Suspend Red | `#FF5D5D` | The **100% suspend action** (a power-off), and the "bill shock" |
| Cloud Glass | `#E9EEF7` | Bills, SQL panels, neutral glass |
| Primary text | `#F8FAFD` | Titles, labels |
| Secondary text | `#9FAABD` | Captions |

**Colour code (use in every scene):** a **virtual warehouse** = a Compute Blue glass block with a small power ring · **credits** = small Blue coins · the **credit meter** = a ring gauge that is Lime while safe, Amber at 50% (with a bell) and Red at 100% (with a power-off).

**The core visual rule (technical accuracy):** a Resource Monitor **monitors the credit usage of virtual warehouses** and, once a credit quota is set, can **notify** or **suspend** when usage reaches a limit. It mainly covers **virtual warehouse compute credits** and **does not control the complete Snowflake bill**, so the bill is shown with only the compute slice covered by the monitor. Only the script's numbers appear: 100 credits, 50%, 100%. No dollar amounts, no real prices.

### Motion effects used (from the skill's effects library)
Banknote, Day dial, Impact frame, Letter dive, Liquid glass, Press font, Code body, Rack focus, Comment drop, Head stack. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–2.61 | "Hello guys! … Oka interesting situation!" (0.00–2.41) | Funny, curious | Title hook |
| 2 | 2.61–12.55 | "Mee Snowflake Virtual Warehouse ni ON chesi marchipoyaru anukondi!" (2.80–6.09) · "Hours kaadhu… days motham running lo undhi!" (6.53–9.20) · "Ippudu bill entha vasthundho imagine cheyyandi! 😂" (9.66–11.93) · *[scripted pause 11.93–13.17]* | Funny | Warehouse left ON, days running, bill shock |
| 3 | 12.55–18.56 | "Snowflake lo unnecessary compute credits consume avvakunda control cheyyadaniki em features unnayi?" (13.17–18.34) | Curious | The question |
| 4 | 18.56–21.72 | "Let's understand!" (18.78–19.37) · "Welcome to NDR EdTech!" (19.88–21.42) | Welcoming | Title and brand welcome |
| 5 | 21.72–44.03 | "Snowflake lo Resource Monitor ane feature warehouse credit usage ni monitor and control cheyyadaniki use chestham." (22.01–27.97) · "Manam credit quota set chesi, usage limit reach ayinappudu notifications or suspension actions configure cheyyachu." (28.35–34.15) · "For example, 100 credits limit set chesam anukondi." (34.54–37.25) · "50% reach ayithe notification pampinchachu." (37.64–40.04) · "100% reach ayithe warehouse suspend cheyyela configure cheyyachu." (40.39–43.86) | Clear | Resource Monitor, quota, 50% notify, 100% suspend |
| 6 | 44.03–52.96 | "Kaani important point enti ante…" (44.20–46.01) · "Resource Monitors mainly Virtual Warehouse compute credit usage ni monitor chesthayi." (46.27–50.56) · "Complete Snowflake bill ni control cheyyavu." (50.88–52.75) | Serious, emphasis | Only compute credits, not the whole bill |
| 7 | 52.96–78.66 | "Oka Banking project example teesukundham." (53.17–54.99) · "Mana ETL warehouse daily data processing kosam run avuthundhi." (55.34–58.50) · "Developers testing kosam separate warehouse use chesthunnaru." (58.81–61.71) · "Testing warehouse unnecessary ga running lo undakunda Resource Monitor configure cheyyachu." (62.03–66.31) · "SQL command chuddam!" (66.66–67.59) · "CREATE RESOURCE MONITOR" (68.03–69.31) · "DEV_MONITOR" (69.52–70.94) · "WITH CREDIT_QUOTA = 100" (71.16–73.75) · "TRIGGERS ON 50 PERCENT" (74.18–75.57) · "DO NOTIFY ON 100 PERCENT" (75.77–77.61) · "DO SUSPEND;" (77.85–78.39) | Storytelling, focused | Banking: ETL and testing warehouses, DEV_MONITOR |
| 8 | 78.66–90.73 | "So, simple ga gurthupettukondi!" (78.93–80.62) · "Resource Monitor helps track warehouse credit usage and control compute costs." (80.92–84.90) · "Warehouse auto-suspend, right sizing and workload separation kuda cost optimization lo important." (85.37–90.52) | Confident | Recap and three cost tips |
| 9 | 90.73–104.27 | "Idi mana Thirty Days of Snowflake series lo Day Twenty-One!" (90.95–94.01) · "Next video nunchi Real-Time Data Engineering concepts start cheddham!" (94.36–97.54) · "Day 22 lo AWS S3 nunchi Snowflake ki data ela load cheyyalo practical example tho explain chesthanu." (97.89–104.11) | Upbeat | Day 21 card, real-time series starts, Day 22 teaser |
| 10 | 104.27–114.99 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (104.42–109.59) · "Full course details kosam NDR EdTech ni Contact avvandi!" (110.02–112.85) · "Let's Learn and Grow Together!" (113.16–114.62) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.69–1.10, 2.41–2.80, 6.09–6.53, 7.26–7.58, 9.20–9.66, 11.93–13.17 (the scripted `[pause]`), 18.34–18.78, 19.37–19.88, 21.42–22.01, 27.97–28.35, 34.15–34.54, 37.25–37.64, 40.04–40.39, 43.86–44.20, 46.01–46.27, 50.56–50.88, 52.75–53.17, 54.99–55.34, 58.50–58.81, 61.71–62.03, 66.31–66.66, 67.59–68.03, 69.31–69.52, 70.94–71.16, 73.75–74.18, 75.57–75.77, 77.61–77.85, 78.39–78.93, 79.23–79.44, 80.62–80.92, 84.90–85.37, 90.52–90.95, 94.01–94.36, 97.54–97.89, 104.11–104.42, 109.59–110.02, 112.85–113.16, 114.62–114.99.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee Snowflake Virtual Warehouse ni ON chesi marchipoyaru anukondi! | Virtual Warehouse ≈3.6 · **ON** ≈4.6 · marchipoyaru ≈5.4 |
| Hours kaadhu… days motham running lo undhi! | Hours kaadhu 6.53 · days motham ≈7.8 · running ≈8.5 |
| Ippudu bill entha vasthundho imagine cheyyandi! | bill ≈10.2 · imagine ≈11.2 |
| Snowflake lo unnecessary compute credits consume avvakunda control cheyyadaniki em features unnayi? | unnecessary compute credits ≈14.5–16.0 · control ≈16.8 · features ≈17.7 |
| Let's understand! / Welcome to NDR EdTech! | Let's 18.78 · Welcome 19.88 · NDR ≈20.6 · EdTech ≈21.0 |
| Snowflake lo Resource Monitor ane feature warehouse credit usage ni monitor and control cheyyadaniki use chestham. | Resource Monitor ≈22.9–24.0 · warehouse credit usage ≈24.8 · monitor and control ≈26.2 |
| Manam credit quota set chesi, usage limit reach ayinappudu notifications or suspension actions configure cheyyachu. | credit quota ≈29.0 · usage limit reach ≈30.6 · notifications ≈32.0 · suspension actions ≈33.0 |
| For example, 100 credits limit set chesam anukondi. | **100 credits** ≈35.4–36.2 |
| 50% reach ayithe notification pampinchachu. | **50%** ≈37.8 · notification ≈39.0 |
| 100% reach ayithe warehouse suspend cheyyela configure cheyyachu. | **100%** ≈40.5 · suspend ≈42.2 |
| Kaani important point enti ante… | important point ≈44.8 |
| Resource Monitors mainly Virtual Warehouse compute credit usage ni monitor chesthayi. | Resource Monitors 46.27 · compute credit usage ≈48.4 · monitor ≈50.0 |
| Complete Snowflake bill ni control cheyyavu. | Complete Snowflake bill 50.88–51.8 · control cheyyavu ≈52.2 |
| Mana ETL warehouse daily data processing kosam run avuthundhi. | ETL warehouse ≈55.9 · daily data processing ≈57.0 |
| Developers testing kosam separate warehouse use chesthunnaru. | Developers 58.81 · separate warehouse ≈60.4 |
| Testing warehouse unnecessary ga running lo undakunda Resource Monitor configure cheyyachu. | unnecessary ga running ≈63.0 · Resource Monitor ≈65.0 · configure ≈65.8 |
| CREATE RESOURCE MONITOR | CREATE 68.03 · RESOURCE MONITOR ≈68.5 |
| DEV_MONITOR | DEV_MONITOR 69.52 |
| WITH CREDIT_QUOTA = 100 | WITH 71.16 · CREDIT_QUOTA ≈71.8 · 100 ≈73.0 |
| TRIGGERS ON 50 PERCENT | TRIGGERS 74.18 · 50 PERCENT ≈75.0 |
| DO NOTIFY ON 100 PERCENT | DO NOTIFY 75.77 · 100 PERCENT ≈76.8 |
| DO SUSPEND; | DO SUSPEND 77.85 |
| So, simple ga gurthupettukondi! | So 78.93 · gurthupettukondi ≈79.8 |
| Resource Monitor helps track warehouse credit usage and control compute costs. | Resource Monitor 80.92 · credit usage ≈82.6 · control compute costs ≈84.0 |
| Warehouse auto-suspend, right sizing and workload separation kuda cost optimization lo important. | auto-suspend ≈85.8 · right sizing ≈87.0 · workload separation ≈88.0 |
| Idi mana Thirty Days of Snowflake series lo Day Twenty-One! | Thirty ≈91.6 · Snowflake ≈92.4 · Twenty-One ≈93.0 |
| Next video nunchi Real-Time Data Engineering concepts start cheddham! | Real-Time Data Engineering ≈95.2–96.5 |
| Day 22 lo AWS S3 nunchi Snowflake ki data ela load cheyyalo practical example tho explain chesthanu. | Day 22 ≈98.0 · AWS S3 ≈99.0 · Snowflake ≈100.0 · load ≈101.0 · practical example ≈102.5 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈106.4 · NDR EdTech ≈107.4–108.4 · **Follow** ≈108.8 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 110.02–111.2 · NDR EdTech ≈111.3 · **Contact** ≈112.0 (estimated) |
| Let's Learn and Grow Together! | Let's 113.16 · Together ≈114.2 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, Suspend Red #FF5D5D, Cloud Glass #E9EEF7, text #F8FAFD.*

**Object look (keep identical in every scene):** a **virtual warehouse** = a Compute Blue glass block with a small power ring on top. **Credits** = small Blue coins. The **credit meter** = a ring gauge: Lime while safe, Amber at 50% (a bell appears), Red at 100% (a power-off symbol appears). A **bill** = a Cloud Glass page with abstract bars.

### Scene 1 – Hook (0.00–2.61 s · 2.61 s)
**Voice-over:** "Hello guys! Oka interesting situation!"
**Tone:** funny, curious.
**Visual objective:** Welcome viewers and tease the situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, Suspend Red #FF5D5D, Cloud Glass #E9EEF7, text #F8FAFD. A steel-slate space with soft blue light and drifting glass particles. A glowing Compute Blue glass warehouse block with a power ring floats at the upper-centre, a small Blue coin drifting above it. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–0.69 s: particles drift in on "Hello guys!".
- 1.10–2.41 s: the warehouse appears and the coin spins on "Oka interesting situation!".
- 2.41–2.61 s: soft light sweep into Scene 2.
- Effect: **Impact frame** — a one-frame punch-in at ≈2.3 s on "situation".
**Audio sync:** title lands at ≈1.2 s; the sweep completes in the pause at 2.41–2.80 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 21".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – Warehouse left ON for days (2.61–12.55 s · 9.94 s)
**Voice-over:** "Mee Snowflake Virtual Warehouse ni ON chesi marchipoyaru anukondi! Hours kaadhu… days motham running lo undhi! Ippudu bill entha vasthundho imagine cheyyandi! 😂"
**Tone:** funny. The last 0.6 s is the start of the scripted pause.
**Visual objective:** A warehouse is switched ON and forgotten, running for days, and the bill is imagined.
Generate as **three shots (2a–2c)**.

**Shot 2a (2.61–6.31 s) – switched ON and forgotten:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Cloud Glass #E9EEF7, text #F8FAFD. A Compute Blue glass warehouse block with a power ring is switched ON by a cursor click and the ring glows Lime. Then the cursor drifts away and a small glass thought-bubble with a forgotten-sticky-note glyph (no text) appears. Light, playful. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 2.80–4.2 s the warehouse appears and the ring switches ON on "Mee Snowflake Virtual Warehouse ni ON chesi" (Virtual Warehouse ≈3.6 s, ON ≈4.6 s); ≈4.6–6.09 s the cursor drifts away and the bubble appears on "marchipoyaru anukondi!".
Overlay (post): "VIRTUAL WAREHOUSE: ON" from ≈3.6 s.

**Shot 2b (6.31–9.43 s) – not hours, but days:**
"Same style and palette. A clock-dial (no numerals) beside the warehouse spins quickly and a calendar-page strip flips through many days while the warehouse keeps running and Blue coins stream out of it. Playful exaggeration. No readable text, no logos, no watermark."
Motion: 6.53–7.26 s a short clock tick on "Hours kaadhu…" (a small dial turns once); 7.58–9.20 s the calendar strip flips fast on "days motham running lo undhi!" (days motham ≈7.8 s). **Effect: Day dial.**
Overlay (post): "NOT HOURS… DAYS!" from 7.58 s.

**Shot 2c (9.43–12.55 s) – the bill:**
"Same style and palette, plus Suspend Red #FF5D5D. A long Cloud Glass bill-page unrolls from the warehouse like a receipt, growing longer and longer with abstract bars, and its edge glows Red. A funny shocked sparkle bursts. Hold a calm still frame for the last 0.6 s. No readable text, no real currency symbols, no watermark."
Motion: 9.66–10.2 s the bill starts to unroll on "Ippudu bill"; ≈10.2–11.93 s it grows and the Red glow builds on "entha vasthundho imagine cheyyandi!" (imagine ≈11.2 s); 11.93–12.55 s calm hold during the scripted pause. **Effect: Banknote** — abstract banknote-style bill sheets flutter around the receipt.
Overlay (post): "IMAGINE THE BILL!" from ≈11.2 s.

**Audio sync:** ON at ≈4.6 s; days flip at 7.58 s; bill at 9.66 s.
**Negative prompt (all shots):** "Real currency symbols, readable amounts, human faces, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – How do we control unnecessary credits? (12.55–18.56 s · 6.01 s)
**Voice-over:** "Snowflake lo unnecessary compute credits consume avvakunda control cheyyadaniki em features unnayi?"
**Tone:** curious.
**Visual objective:** Pose the question: which features can control unnecessary compute credit use?

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Suspend Red #FF5D5D, Cloud Glass #E9EEF7, text #F8FAFD. The long bill fades back. Blue coins keep draining out of the running warehouse block; a soft question-mark glow and a small closed glass 'feature' card with a dial glyph appear beside it. Calm, curious feeling. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 13.17–15.0 s: the coins drain from the warehouse on "Snowflake lo unnecessary compute credits".
- ≈15.0–16.8 s: the drain continues on "consume avvakunda".
- ≈16.8–18.34 s: the feature card glows with a question mark on "control cheyyadaniki em features unnayi?" (features ≈17.7 s).
**Audio sync:** coins at ≈14.5 s; card at ≈16.8 s.
**On-screen text (overlay, post):** "HOW TO CONTROL UNNECESSARY COMPUTE CREDITS?" from 13.17 s.
**Negative prompt:** "Readable text, the answer shown too early, clutter, flicker, off-palette colours, human faces, watermark."

---

### Scene 4 – Title and welcome (18.56–21.72 s · 3.16 s)
**Voice-over:** "Let's understand! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Name the topic and welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, text #F8FAFD. A calm, clean frame with a glowing glass ring gauge (Lime) and a Blue warehouse block resting at the lower-centre. A reserved clean area at the top for the logo and a soft blue glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 18.78–19.37 s the title lands on "Let's understand!" (**Effect: Letter dive** — the letters settle fully before 19.3 s); 19.88–21.42 s a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** title at 18.78 s; logo and panel at 19.88 s; "NDR" at ≈20.6 s.
**On-screen text (overlay, post):** "RESOURCE MONITORS & COST OPTIMIZATION" at 18.78 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 19.88 s.
**Negative prompt:** "Fake logos, distorted logo, misspelled title, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – Resource Monitor (21.72–44.03 s · 22.31 s)
**Voice-over:** "Snowflake lo Resource Monitor ane feature warehouse credit usage ni monitor and control cheyyadaniki use chestham. Manam credit quota set chesi, usage limit reach ayinappudu notifications or suspension actions configure cheyyachu. For example, 100 credits limit set chesam anukondi. 50% reach ayithe notification pampinchachu. 100% reach ayithe warehouse suspend cheyyela configure cheyyachu."
**Tone:** clear.
**Visual objective:** A Resource Monitor monitors and controls warehouse credit usage using a credit quota, with a notification at 50% and a suspend action at 100%.
Generate as **five shots (5a–5e)**. Keep the warehouse and meter positions identical in every shot.

**Shot 5a (21.72–28.16 s) – monitor and control credit usage:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Cloud Glass #E9EEF7, text #F8FAFD. A Compute Blue warehouse block with a power ring sits on the left. A glass monitoring-lens (a magnifier with a small dial inside) appears on the right and watches the coins flowing from the warehouse into a ring gauge that glows Lime. A small glass hand-on-dial glyph shows control. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 22.01–23.5 s the lens appears on "Snowflake lo Resource Monitor ane feature" (Resource Monitor ≈22.9 s); ≈24.8 s the coins flow into the gauge on "warehouse credit usage ni"; ≈26.2–27.97 s the dial-hand glyph glows on "monitor and control cheyyadaniki use chestham".
Overlay (post): "RESOURCE MONITOR" at ≈22.9 s; "MONITOR AND CONTROL WAREHOUSE CREDIT USAGE" from ≈24.8 s.

**Shot 5b (28.16–34.35 s) – credit quota, notifications or suspension:**
"Same style and palette, plus Notify Amber #FFB938 and Suspend Red #FF5D5D. A Blue coin-jar (the credit quota) appears beside the gauge with a limit line drawn across it. At the limit line a bell (Amber) and a power-off symbol (Red) appear as two options. Calm, clear. No readable text, no logos, no watermark."
Motion: 28.35–30.0 s the coin-jar and limit line appear on "Manam credit quota set chesi" (credit quota ≈29.0 s); ≈30.6 s the gauge fills toward the line on "usage limit reach ayinappudu"; ≈32.0–34.15 s the bell and the power-off symbol appear on "notifications or suspension actions configure cheyyachu".
Overlay (post): "CREDIT QUOTA" at ≈29.0 s; "NOTIFICATIONS OR SUSPENSION ACTIONS" from ≈32.0 s.

**Shot 5c (34.35–37.45 s) – for example, 100 credits:**
"Same style and palette. The coin-jar shows a clean round limit of one hundred Blue coins (a neat stack, no numerals) and a Press-style badge stamps onto it. No readable text apart from the overlay, no logos, no watermark."
Motion: 34.54–35.4 s the jar appears on "For example,"; ≈35.4–36.2 s the badge stamps on "100 credits"; ≈36.2–37.25 s the limit line glows on "limit set chesam anukondi". **Effect: Press font** — "100 CREDITS" presses in at ≈35.4 s.
Overlay (post): "EXAMPLE: 100 CREDITS" at ≈35.4 s.

**Shot 5d (37.45–40.22 s) – 50% reached: notification:**
"Same style and palette. The ring gauge fills to its half-way mark and turns Amber; a glowing Amber bell swings and a small glass envelope-notification slides toward a simple inbox glyph. The warehouse keeps running with its ring still lit. No readable text, no logos, no watermark."
Motion: 37.64–38.4 s the gauge fills to half on "50% reach ayithe" (50% ≈37.8 s); ≈39.0–40.04 s the bell swings and the notification slides on "notification pampinchachu". **Effect: Comment drop** — a small Amber note drops in beside the bell at ≈39.0 s.
Overlay (post): "50% → NOTIFICATION" from ≈37.8 s.

**Shot 5e (40.22–44.03 s) – 100% reached: suspend:**
"Same style and palette. The gauge fills completely and turns Red. The warehouse's power ring switches off, the block dims, and the coins stop flowing. A soft Red power-off symbol glows. The meter's reading holds. Calm, decisive. No readable text, no logos, no watermark."
Motion: 40.39–41.5 s the gauge fills fully on "100% reach ayithe" (100% ≈40.5 s); ≈42.2–43.86 s the power ring switches off and the coins stop on "warehouse suspend cheyyela configure cheyyachu" (suspend ≈42.2 s). **Effect: Rack focus** — focus pulls from the gauge to the dimmed warehouse at ≈42.2 s.
Overlay (post): "100% → SUSPEND THE WAREHOUSE" from ≈40.5 s.

**Audio sync:** lens at ≈22.9 s; quota at ≈29.0 s; "100 CREDITS" at ≈35.4 s; bell at ≈39.0 s; power-off at ≈42.2 s.
**Negative prompt (all shots):** "Other numbers, dollar amounts, readable text, a monitor that blocks other costs, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – Important point: not the complete bill (44.03–52.96 s · 8.93 s)
**Voice-over:** "Kaani important point enti ante… Resource Monitors mainly Virtual Warehouse compute credit usage ni monitor chesthayi. Complete Snowflake bill ni control cheyyavu."
**Tone:** serious, emphasis.
**Visual objective:** Resource Monitors mainly monitor virtual warehouse compute credit usage; they do not control the complete Snowflake bill.
Generate as **two shots (6a, 6b)**.

**Shot 6a (44.03–46.14 s) – important point:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Notify Amber #FFB938, Compute Blue #4DA3FF, Cloud Glass #E9EEF7, text #F8FAFD. A calm Compute Blue warehouse block fills the centre with a soft spotlight and a small glowing 'important' marker above it. A slow, serious push-in. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 44.20–45.0 s the spotlight rises on "Kaani important"; ≈45.0–46.01 s the marker pulses on "point enti ante…". **Effect: Rack focus** — focus pulls from the background to the warehouse at ≈44.8 s.
Overlay (post): "IMPORTANT POINT" from 44.20 s.

**Shot 6b (46.14–52.96 s) – compute credits only, not the whole bill:**
"Same style and palette. A large Cloud Glass bill-page is shown as a round chart with several slices. The slice that matches the warehouse's compute credits glows Compute Blue and the monitor's lens rings that slice only. The other slices stay dim and are not covered by the lens. A soft Amber 'not all' marker pulses. Calm, clear. No readable text, no logos, no watermark."
Motion: 46.27–48.4 s the chart appears and the Blue slice glows on "Resource Monitors mainly Virtual Warehouse"; ≈48.4–50.56 s the lens rings the Blue slice on "compute credit usage ni monitor chesthayi" (compute credit usage ≈48.4 s); 50.88–52.75 s the other slices stay dim and the marker pulses on "Complete Snowflake bill ni control cheyyavu".
Overlay (post): "MAINLY VIRTUAL WAREHOUSE COMPUTE CREDIT USAGE" from 46.27 s; "NOT THE COMPLETE SNOWFLAKE BILL" from 50.88 s.

**Audio sync:** marker at 44.8 s; Blue slice at 46.27 s; "NOT THE COMPLETE BILL" at 50.88 s.
**Negative prompt (all shots):** "Naming specific other cost types, slice percentages, dollar amounts, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (52.96–78.66 s · 25.70 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana ETL warehouse daily data processing kosam run avuthundhi. Developers testing kosam separate warehouse use chesthunnaru. Testing warehouse unnecessary ga running lo undakunda Resource Monitor configure cheyyachu. SQL command chuddam! CREATE RESOURCE MONITOR DEV_MONITOR WITH CREDIT_QUOTA = 100 TRIGGERS ON 50 PERCENT DO NOTIFY ON 100 PERCENT DO SUSPEND;"
**Tone:** storytelling, focused.
**Visual objective:** An ETL warehouse and a separate testing warehouse; a Resource Monitor keeps the testing warehouse from running unnecessarily.
Generate as **seven shots (7a–7g)**. All shots use the same camera language and layout (ETL warehouse on the left, testing warehouse on the right, the meter in the centre).

**Shot 7a (52.96–55.17 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Cloud Glass #E9EEF7, text #F8FAFD. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre in cool blue, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈53.4 s.

**Shot 7b (55.17–58.66 s) – the ETL warehouse:**
"Same style and palette. A Compute Blue warehouse block on the left runs steadily: data blocks flow through it from a table into a report, with a calm Lime ring. A small calendar-page glyph shows that it runs daily. No readable fine text, no logos."
Overlay (post): "ETL WAREHOUSE" at ≈55.9 s; "DAILY DATA PROCESSING" from ≈57.0 s.

**Shot 7c (58.66–61.87 s) – developers' separate testing warehouse:**
"Same style and palette. A second, smaller Blue warehouse block appears on the right, separate from the first, with an abstract code-editor glyph beside it. Both blocks are clearly separate. No readable fine text, no logos."
Overlay (post): "DEVELOPERS: SEPARATE WAREHOUSE FOR TESTING" from 58.81 s.

**Shot 7d (61.87–66.49 s) – avoid unnecessary running; configure a Resource Monitor:**
"Same style and palette. The testing warehouse keeps running idly with coins slowly dripping out. A glass monitor-lens with a ring gauge slides in and attaches to the testing warehouse with a thin light line; the drip slows and the ring turns calm Lime. Calm, satisfying. No readable fine text, no logos."
Motion: 62.03–63.6 s the idle drip shows on "Testing warehouse unnecessary ga running lo undakunda" (unnecessary ga running ≈63.0 s); ≈65.0–66.31 s the monitor attaches on "Resource Monitor configure cheyyachu" (Resource Monitor ≈65.0 s).
Overlay (post): "TESTING WAREHOUSE SHOULD NOT RUN UNNECESSARILY" from 62.03 s; "CONFIGURE A RESOURCE MONITOR" from ≈65.0 s.

**Shot 7e (66.49–69.42 s) – SQL: CREATE RESOURCE MONITOR:**
"Same style and palette. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) floats at the centre with a thin Blue edge. Behind it, softly out of focus, the two warehouses glow. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 66.66–67.59 s the panel slides in on "SQL command chuddam!"; 68.03–69.31 s line 1 types on "CREATE RESOURCE MONITOR". **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE RESOURCE MONITOR
```
Appears at 68.03 s.

**Shot 7f (69.42–73.97 s) – SQL: DEV_MONITOR and CREDIT_QUOTA:**
"Same style and palette. The code panel continues. A coin-jar glyph with a limit line appears beside the code as the quota is typed. No readable code, no logos, no watermark."
Motion: 69.52–70.94 s the name types on "DEV_MONITOR"; 71.16–73.75 s the quota types on "WITH CREDIT_QUOTA = 100" (100 ≈73.0 s). **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE RESOURCE MONITOR DEV_MONITOR
WITH CREDIT_QUOTA = 100
```
"DEV_MONITOR" at 69.52 s; "WITH CREDIT_QUOTA = 100" at 71.16 s.

**Shot 7g (73.97–78.66 s) – SQL: TRIGGERS:**
"Same style and palette. The code panel finishes the statement. As each trigger line types, the meter beside it lights: at the 50 mark an Amber bell appears and at the 100 mark a Red power-off symbol appears. Calm, satisfying. No readable code, no logos, no watermark."
Motion: 74.18–75.57 s line 4 types on "TRIGGERS ON 50 PERCENT" and the bell lights; 75.77–77.61 s line 5 types on "DO NOTIFY ON 100 PERCENT"; 77.85–78.39 s the last words type on "DO SUSPEND;" and the power-off symbol lights. **Effect: Code body.**
Overlay (post, monospace; the full statement shown at the end):
```sql
CREATE RESOURCE MONITOR DEV_MONITOR
WITH CREDIT_QUOTA = 100
TRIGGERS
ON 50 PERCENT DO NOTIFY
ON 100 PERCENT DO SUSPEND;
```
"TRIGGERS" at 74.18 s; "ON 50 PERCENT DO NOTIFY" from ≈75.0 s; "ON 100 PERCENT DO SUSPEND;" from ≈76.8 s (completes at ≈78.4 s). The spoken words slightly reorder the lines (the narrator says "ON 50 PERCENT" before "DO NOTIFY"); keep the on-screen code exactly as the script shows it.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake text in the generated video, wrong syntax, extra lines, dollar amounts, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap and cost tips (78.66–90.73 s · 12.07 s)
**Voice-over:** "So, simple ga gurthupettukondi! Resource Monitor helps track warehouse credit usage and control compute costs. Warehouse auto-suspend, right sizing and workload separation kuda cost optimization lo important."
**Tone:** confident.
**Visual objective:** One-line recap and three more cost-optimisation ideas.
Generate as **three shots (8a–8c)**.

**Shot 8a (78.66–80.77 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, text #F8FAFD. A calm ring gauge (Lime) and a Blue warehouse block glide to the centre with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈79.0 s.

**Shot 8b (80.77–85.14 s) – Resource Monitor tracks and controls:**
"Same style and palette. The monitor lens rests over the warehouse and the ring gauge, with coins flowing steadily and a small hand-on-dial glyph glowing. Clean and calm. No readable text, no logos."
Overlay (post): "RESOURCE MONITOR" at 80.92 s; "TRACK WAREHOUSE CREDIT USAGE" from ≈82.6 s; "CONTROL COMPUTE COSTS" from ≈84.0 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 8c (85.14–90.73 s) – three more cost tips:**
"Same style and palette. Three glass cards rise one after another in a vertical stack: a moon-and-power glyph (auto-suspend), three warehouse blocks in small, medium and large sizes with the middle one highlighted (right sizing), and two separate warehouse blocks with different workloads (workload separation). Clean, uncluttered, phone-readable layout. No readable fine text, no logos."
Motion: ≈85.8 s card 1 on "auto-suspend"; ≈87.0 s card 2 on "right sizing"; ≈88.0 s card 3 on "workload separation"; ≈89.0–90.52 s a soft glow on "kuda cost optimization lo important". **Effect: Head stack.**
Overlay (post): "WAREHOUSE AUTO-SUSPEND" at ≈85.8 s; "RIGHT SIZING" at ≈87.0 s; "WORKLOAD SEPARATION" at ≈88.0 s.

**Audio sync:** cards at ≈85.8, ≈87.0 and ≈88.0 s.
**Negative prompt:** "Sizes or numbers, technical claims beyond the script, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card, real-time series begins, Day 22 (90.73–104.27 s · 13.54 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty-One! Next video nunchi Real-Time Data Engineering concepts start cheddham! Day 22 lo AWS S3 nunchi Snowflake ki data ela load cheyyalo practical example tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 21, announce the real-time data engineering part and tease Day 22.
Generate as **three shots (9a–9c)**.

**Shot 9a (90.73–94.19 s) – Day 21 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, text #F8FAFD. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty-one lit in Blue (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 21" from ≈91.6 s; the twenty-first node lights at ≈93.0 s on "Twenty-One".

**Shot 9b (94.19–97.72 s) – real-time data engineering starts:**
"Same style and palette. The row of nodes continues past the twenty-first with a glowing data-pipeline ribbon (a flowing line of data blocks) that starts to run from the right side of the progress row. Energetic, forward-moving. No readable text, no logos, no watermark."
Motion: 94.36–95.2 s the ribbon appears on "Next video nunchi"; ≈95.2–96.5 s it starts to flow on "Real-Time Data Engineering"; ≈96.5–97.54 s a soft burst on "concepts start cheddham!".
Overlay (post): "FROM THE NEXT VIDEO: REAL-TIME DATA ENGINEERING CONCEPTS" from 94.36 s.

**Shot 9c (97.72–104.27 s) – Day 22 teaser: AWS S3 to Snowflake:**
"Same style and palette. A teaser panel slides in: on the left a generic glass cloud-storage bucket glyph (no AWS logo) holding glowing data files, on the right a glass snowflake-crystal database. A thin Blue line carries data blocks from the bucket into the database. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "DAY 22" at ≈98.0 s; "AWS S3 → SNOWFLAKE" from ≈99.0 s; "PRACTICAL EXAMPLE" from ≈102.5 s. The visual only suggests data moving from a bucket to a database. Do not show real AWS branding, commands or settings.

**Audio sync:** card at ≈91.6 s; the twenty-first node at ≈93.0 s; ribbon at ≈95.2 s; Day 22 at ≈98.0 s.
**Negative prompt:** "Real AWS or Snowflake logos, specific load steps, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (104.27–114.99 s · 10.72 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (104.27–109.81 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, text #F8FAFD. A calm, clean background with a soft blue glow, a small ring gauge and a Blue warehouse block drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈105.6 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈106.4 s, emphasised at ≈108.8 s on "Follow" (estimated).

**Shot 10b (109.81–113.01 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Blue and Lime glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 110.02 s, emphasised at ≈112.0 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (113.01–114.99 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 113.16 s. Hold the final frame for the last 0.35 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 21. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #1E2633, Compute Blue #4DA3FF, Safe Lime #7CE38B, Notify Amber #FFB938, Suspend Red #FF5D5D, Cloud Glass #E9EEF7, text #F8FAFD, secondary text #9FAABD. Colour code: a virtual warehouse = a Compute Blue glass block with a small power ring; credits = small Blue coins; the credit meter = a ring gauge that is Safe Lime while within the limit, Notify Amber at 50% with a bell, and Suspend Red at 100% with a power-off symbol; a bill = a Cloud Glass page with abstract bars. A Resource Monitor is a glass monitoring-lens attached to a warehouse; it covers the warehouse's compute credit slice only, never the complete bill. Never show dollar amounts, real prices or numbers other than 100 credits, 50% and 100%. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–20: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day21.mp3` (114.99 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, "100 CREDITS", the SQL code, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a bell chime for the 50% notification, a power-down tone for the suspend, a gentle tick) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start (the opening line, 0–2.4 s), at ON and "days" (≈4.6, 7.58 s), at the title (18.78 s), at 100 credits, 50% and 100% (≈35.4, ≈37.8, ≈40.5 s), at "not the complete bill" (50.88 s), at each SQL part (68.03, 69.52, 71.16, 74.18, 75.77, 77.85 s), at the three cost tips (≈85.8, ≈87.0, ≈88.0 s), at the Day 22 teaser (≈98.0 s), at the final tagline (113.16 s), and at the Follow and Contact lines (≈108.8, ≈112.0 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: a Resource Monitor monitors and controls warehouse credit usage; you set a credit quota and configure notifications or suspension actions for when a usage limit is reached; the example uses a 100-credit limit with a notification at 50% and a suspend action at 100%; Resource Monitors mainly monitor virtual warehouse compute credit usage and do not control the complete Snowflake bill; in the banking example a testing warehouse is kept from running unnecessarily; auto-suspend, right sizing and workload separation also matter for cost optimization. **No dollar amounts, prices or other numbers** are shown. The SQL `CREATE RESOURCE MONITOR DEV_MONITOR WITH CREDIT_QUOTA = 100 TRIGGERS ON 50 PERCENT DO NOTIFY ON 100 PERCENT DO SUSPEND;` is valid Snowflake syntax.
- **Optional addition (not in the script, so not shown on screen):** a resource monitor only limits a warehouse once it is assigned to it (for example with `ALTER WAREHOUSE … SET RESOURCE_MONITOR = DEV_MONITOR`), and creating one needs a high-privilege role such as ACCOUNTADMIN. The script says only "configure", so the visuals attach the monitor to the testing warehouse without showing the command. You may want to mention it in the caption; please verify it against Snowflake's current documentation first.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
