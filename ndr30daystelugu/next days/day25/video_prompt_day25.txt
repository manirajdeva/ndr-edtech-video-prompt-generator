# Thirty Days of Snowflake – Day 25: What are Snowflake Streams?
Video prompt package (NDR EdTech) — `days-scripts\day25.txt` (**no audio file yet**)

> **Timing status: ESTIMATED. `Audio\day25.mp3` was not found.**
> - Every time in this file is an **estimate** (marked ≈) made from the script at a natural speaking pace (about 0.37 s per spoken word, 0.45 s between lines), calibrated against the measured timings of Days 15–24. The estimated total is **≈115 s**, and the real narration can differ by about ±10%.
> - **Final synchronisation needs the audio.** When you add `Audio\day25.mp3`, tell me "update day 25 with the audio" and I will measure it with Whisper, replace every estimated time with measured ones, re-check the cut points and re-save the day folder.
> - Because the times are estimates, scene cuts are placed at the midpoint between lines, and the shots are written so that trimming or holding a few frames will not break them.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please note (3 items):**
> 1. **This script opens differently from earlier days:** it starts with "Welcome to NDR EdTech!" and then goes straight into the production incident (no "Hello guys" and no scripted `[pause]`). The visuals follow that order.
> 2. **No audio, so no audio checks were possible.** I could not check Whisper-style mishearings, the Follow and Contact timing, or how the narrator actually reads `METADATA$ACTION`, `METADATA$ISUPDATE` and `METADATA$ROW_ID`.
> 3. **The audio may differ from the script** (it did on Day 16). I will compare them when the audio is added.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 25: What are Snowflake Streams? |
| Duration | **≈115 s (estimated)** |
| Format | 9:16 vertical, 30 FPS (≈ 3,450 frames, estimated) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | The user's voice-over (`Audio\day25.mp3`, not yet supplied) is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (26 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Change Ledger" (new for Day 25)
| Role | HEX | Use |
|---|---|---|
| Background | `#161B22` | Base, gradients (ink slate) |
| Insert Green | `#6EE06E` | An **INSERT** (a new row) |
| Update Azure | `#5AA9FF` | An **UPDATE** (a changed row; it is the pair "old row out, new row in") |
| Delete Coral | `#FF5C6C` | A **DELETE** (a removed row) |
| Stream Teal | `#2FD5C5` | The **Stream** (the lane that records the changes) |
| Metadata Gold | `#FFD166` | The three **METADATA$** columns |
| Table Glass | `#E8EDF5` | Tables, SQL panels, neutral glass |
| Primary text | `#F5F7FA` | Titles, labels |
| Secondary text | `#9AA5B5` | Captions |

**Colour code (use in every scene):** a **table** = a Table Glass block with rows of cells · a **Stream** = a Teal lane beside the table that fills with small **change cards** · INSERT = Green "+" card · DELETE = Coral "−" card · UPDATE = a Coral "−" card and a Green "+" card as a pair, joined by a small Azure tag · metadata = three Gold chips on every change card.

**The core visual rule (technical accuracy):** a Stream **tracks the data changes in a table** (a Change Data Capture mechanism). It identifies **INSERT, UPDATE and DELETE** operations. Every change record carries three metadata columns: **METADATA$ACTION** (INSERT or DELETE), **METADATA$ISUPDATE** (whether the record is part of an update) and **METADATA$ROW_ID** (identifies the row uniquely). Because an update is recorded as a delete plus an insert, an UPDATE is drawn as **a Coral card and a Green card joined by an Azure tag**. The Stream shows **only the changes**, so the table is never re-processed in full. Show abstract shapes only (no readable data). No counts, timings or sizes beyond the script's "thousands of changes".

### Motion effects used (from the skill's effects library)
Letter dive, Impact frame, Liquid glass, Post wall, Head stack, Press font, Live cursor, Code body, Rack focus, Comment drop, Layer explode. Each is named in the scene where it appears.

---

## 2. Audio timing map (ESTIMATED – replace with measured times when the audio is added)

Scene cuts sit at the midpoint between lines. **All times are estimates (≈).** Times in brackets are estimated speech start–end of each phrase.

| Scene | Scene time (≈) | Spoken phrase (estimated speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–1.86 | "Welcome to NDR EdTech!" (0.00–1.63) | Powerful, energetic | Brand welcome, "DAY 25" |
| 2 | 1.86–12.03 | "Production lo customer table update ayyindhi!" (2.08–4.45) · "Oka customer address change ayyindhi." (4.90–6.90) · "Inko customer record delete ayyindhi." (7.35–9.35) · "Maroka new customer insert ayyadu." (9.80–11.80) | Urgent | The production incident: update, delete, insert |
| 3 | 12.03–21.60 | "Ippudu Data Engineer ga mana question enti?" (12.25–14.99) · "Entire table ni malli process cheyyala?" (15.44–17.81) · "Leda only changes ni identify chesi process cheyyacha?" (18.26–21.37) | Questioning | Process the entire table, or only the changes? |
| 4 | 21.60–27.62 | "Exactly! Snowflake lo ee requirement kosam Streams ane powerful feature undhi!" (21.82–26.04) · "Let's understand!" (26.49–27.39) | Excited, reveal | Streams reveal, title |
| 5 | 27.62–40.29 | "Snowflake Stream ante table lo jarigina data changes ni track cheyyadaniki use chese Change Data Capture mechanism." (27.84–34.28) · "Simple ga cheppalante, INSERT, UPDATE and DELETE operations ni identify cheyyadaniki Streams help chesthayi." (34.73–40.06) | Clear | Stream as a CDC mechanism, three operations |
| 6 | 40.29–56.75 | "Stream lo mainly three metadata columns untayi." (40.51–43.25) · "First, METADATA$ACTION – INSERT or DELETE ani identify chesthundhi." (43.70–47.55) · "Second, METADATA$ISUPDATE – update operation lo part aa kaadha ani indicate chesthundhi." (48.00–52.22) · "Third, METADATA$ROW_ID – row ni uniquely identify cheyyadaniki use avuthundhi." (52.67–56.52) | Clear, structured | Three metadata columns |
| 7 | 56.75–82.27 | "Oka Banking project example teesukundham." (56.97–58.97) · "Mana CUSTOMER table lo daily thousands of changes jaruguthunnayi." (59.42–62.53) · "Ippudu Stream create cheddham!" (62.98–64.61) · "CREATE STREAM CUSTOMER_STREAM ON TABLE CUSTOMER;" (65.06–68.17) · "Changes ni check cheyyadaniki:" (68.62–70.25) · "SELECT * FROM CUSTOMER_STREAM;" (70.70–73.07) · "Ippudu source table lo changes jariginappudu, Stream change records ni expose chesthundhi." (73.52–78.11) · "Manam ee changes ni downstream processing kosam use cheyyachu." (78.56–82.04) | Storytelling, focused | Banking: create and read the stream |
| 8 | 82.27–93.69 | "So, simple ga gurthupettukondi!" (82.49–84.12) · "Snowflake Streams help us capture table changes without processing the entire table again." (84.57–89.53) · "Streams are an important building block for CDC pipelines." (89.98–93.46) | Confident | Recap |
| 9 | 93.69–103.03 | "Idi mana Thirty Days of Snowflake series lo Day Twenty-Five!" (93.91–97.76) · "Next video lo Snowflake Tasks gurinchi real-time automation example tho explain chesthanu." (98.21–102.80) | Upbeat | Day 25 card, Tasks teaser |
| 10 | 103.03–114.96 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (103.25–108.58) · "Full course details kosam NDR EdTech ni Contact avvandi!" (109.03–112.51) · "Let's Learn and Grow Together!" (112.96–114.96) | Upbeat, closing | Follow, contact, end card |

Estimated total: ≈115 s. **Word-level triggers are not listed**, because they cannot be estimated reliably. Inside each shot, the overlay timings are given relative to the phrase ("when the narrator says …"). Final times come from the audio.

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #161B22, Insert Green #6EE06E, Update Azure #5AA9FF, Delete Coral #FF5C6C, Stream Teal #2FD5C5, Metadata Gold #FFD166, Table Glass #E8EDF5, text #F5F7FA.*

**Object look (keep identical in every scene):** a **table** = a Table Glass block with rows of cells. A **Stream** = a Teal glass lane beside it. **Change cards**: INSERT = Green "+", DELETE = Coral "−", UPDATE = a Coral "−" card and a Green "+" card joined by an Azure tag. **Metadata** = three Gold chips on each card.

### Scene 1 – Welcome (≈0.00–1.86 s · ≈1.86 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** powerful, energetic.
**Visual objective:** Open with the brand welcome and the series tag.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #161B22, Insert Green #6EE06E, Update Azure #5AA9FF, Delete Coral #FF5C6C, Stream Teal #2FD5C5, Metadata Gold #FFD166, Table Glass #E8EDF5, text #F5F7FA. An ink-slate space with soft teal light and drifting glass particles. A glowing glass snowflake-crystal emblem rises at the upper-centre with a soft bloom, and a thin Teal stream line flows beneath it. A reserved clean area at the top for the logo and clean space for a title. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–1.63 s: the emblem rises and a glass panel slides in as the narrator says "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
- Last 0.2 s: soft light sweep into Scene 2.
**Audio sync:** logo and panel at the start of the line.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH"; "THIRTY DAYS OF SNOWFLAKE · DAY 25" right after.
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, human faces, watermark."

---

### Scene 2 – The production incident (≈1.86–12.03 s · ≈10.17 s)
**Voice-over:** "Production lo customer table update ayyindhi! Oka customer address change ayyindhi. Inko customer record delete ayyindhi. Maroka new customer insert ayyadu."
**Tone:** urgent.
**Visual objective:** Three kinds of change hit the production CUSTOMER table: an updated address, a deleted record and a new customer.
Generate as **two shots (2a, 2b)**.

**Shot 2a (≈1.86–4.68 s) – the production table is updated:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #161B22, Table Glass #E8EDF5, Update Azure #5AA9FF, Delete Coral #FF5C6C, text #F5F7FA. A large Table Glass CUSTOMER table block with rows of cells sits at the centre with a small 'production' beacon (a glowing red-orange dot, no text) above it. A soft alert pulse ripples through the table as if it has just changed. Tense, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: as the narrator says "Production lo customer table update ayyindhi!" the table pulses and the beacon glows.
Overlay (post): "PRODUCTION" and "CUSTOMER TABLE UPDATED" from the start of the line.

**Shot 2b (≈4.68–12.03 s) – an address change, a delete and an insert:**
"Same style and palette, plus Insert Green #6EE06E. Three things happen to the table one after another, each lit for a moment: first one row's cell changes colour to Azure (an address changed), then a second row turns Coral and fades out (a record deleted), then a new Green row slides in at the bottom (a customer inserted). Calm, clear, phone-readable. No readable text, no logos, no watermark."
Motion: as the narrator says "Oka customer address change ayyindhi." the first row turns Azure; on "Inko customer record delete ayyindhi." the second row turns Coral and fades; on "Maroka new customer insert ayyadu." the new Green row slides in. **Effect: Post wall** — a short wall of three change cards appears beside the table, one for each change.
Overlay (post): "ADDRESS CHANGED" on the first line; "RECORD DELETED" on the second; "NEW CUSTOMER INSERTED" on the third.

**Audio sync:** one change per sentence; each change lands as its sentence begins.
**Negative prompt (all shots):** "Readable personal data, human faces, real company names, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Process everything, or only the changes? (≈12.03–21.60 s · ≈9.57 s)
**Voice-over:** "Ippudu Data Engineer ga mana question enti? Entire table ni malli process cheyyala? Leda only changes ni identify chesi process cheyyacha?"
**Tone:** questioning.
**Visual objective:** The data engineer's question: re-process the entire table, or identify and process only the changes?
Generate as **three shots (3a–3c)**.

**Shot 3a (≈12.03–15.22 s) – the data engineer's question:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #161B22, Table Glass #E8EDF5, Stream Teal #2FD5C5, text #F5F7FA. The changed CUSTOMER table block sits at the centre with the three change glints still faintly lit. A soft white question-mark glow appears above it, and a small abstract glass pipeline glyph (the data engineer's job) appears beside it. Calm, thoughtful. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: as the narrator says "Ippudu Data Engineer ga mana question enti?" the question mark and the pipeline glyph appear.
Overlay (post): "THE DATA ENGINEER'S QUESTION" from the start of the line.

**Shot 3b (≈15.22–18.04 s) – process the entire table again?:**
"Same style and palette, plus Delete Coral #FF5C6C. A wide scan beam sweeps across every row of the whole table, lighting all of it with a heavy Coral-tinted glow, while a progress ring turns slowly. A soft question-mark glow pulses. No readable text, no logos, no watermark."
Motion: as the narrator says "Entire table ni malli process cheyyala?" the beam sweeps the whole table.
Overlay (post): "PROCESS THE ENTIRE TABLE AGAIN?" from the start of the line.

**Shot 3c (≈18.04–21.60 s) – or only the changes?:**
"Same style and palette, plus Stream Teal #2FD5C5. The table resets. This time a narrow Teal beam lights only the three changed rows (Azure, Coral, Green) and the rest of the table stays dark and calm. A soft question-mark glow pulses. No readable text, no logos, no watermark."
Motion: as the narrator says "Leda only changes ni identify chesi process cheyyacha?" the narrow beam finds the three changed rows. **Effect: Rack focus** — focus pulls from the whole table to the three changed rows.
Overlay (post): "OR ONLY THE CHANGES?" from the start of the line.

**Audio sync:** each shot starts with its sentence.
**Negative prompt (all shots):** "The answer shown too early, readable text, clutter, flicker, off-palette colours, human faces, watermark."

---

### Scene 4 – Exactly! Streams (≈21.60–27.62 s · ≈6.02 s)
**Voice-over:** "Exactly! Snowflake lo ee requirement kosam Streams ane powerful feature undhi! Let's understand!"
**Tone:** excited, reveal.
**Visual objective:** Reveal Streams as the feature for this requirement, and name the topic.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Insert Green #6EE06E, Update Azure #5AA9FF, Delete Coral #FF5C6C, Table Glass #E8EDF5, text #F5F7FA. The narrow Teal beam widens into a glowing Teal glass lane (a stream) beside the CUSTOMER table, and three small change cards (Green, Azure/Coral pair, Coral) float into it and line up. A glowing glass snowflake-crystal emblem rises above. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- As the narrator says "Exactly!" a bright flash. **Effect: Impact frame** — one-frame flash.
- As the narrator says "Snowflake lo ee requirement kosam Streams ane powerful feature undhi!" the Teal lane forms and the cards line up, and the title lands on "Streams". **Effect: Letter dive** — the letters settle fully before the narrator moves on.
- As the narrator says "Let's understand!" a subtitle pops in.
**Audio sync:** flash on "Exactly!"; title on "Streams"; subtitle on "Let's understand!".
**On-screen text (overlay, post):** "SNOWFLAKE STREAMS"; "LET'S UNDERSTAND!".
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – What is a Stream? (≈27.62–40.29 s · ≈12.67 s)
**Voice-over:** "Snowflake Stream ante table lo jarigina data changes ni track cheyyadaniki use chese Change Data Capture mechanism. Simple ga cheppalante, INSERT, UPDATE and DELETE operations ni identify cheyyadaniki Streams help chesthayi."
**Tone:** clear.
**Visual objective:** A Stream is a Change Data Capture mechanism that tracks data changes in a table, and it identifies INSERT, UPDATE and DELETE operations.
Generate as **two shots (5a, 5b)**.

**Shot 5a (≈27.62–34.51 s) – tracking the changes in a table:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Table Glass #E8EDF5, Insert Green #6EE06E, Delete Coral #FF5C6C, text #F5F7FA. A Table Glass table block on the left and a Teal glass lane (the Stream) on its right. Whenever a row in the table changes, a small change card (Green, Coral or Azure) slides out of the table into the lane and rides along it, in order. A small glass eye glyph hovers over the lane to show tracking. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: as the narrator says "Snowflake Stream ante table lo jarigina data changes ni" the table and the lane appear; on "track cheyyadaniki use chese" the first change cards ride into the lane; on "Change Data Capture mechanism" a small label appears. **Effect: Layer explode** — the table's changed rows lift off as cards into the lane.
Overlay (post): "STREAM" at the start; "TRACKS DATA CHANGES IN A TABLE" from "jarigina data changes"; "CHANGE DATA CAPTURE (CDC)" on "Change Data Capture mechanism".

**Shot 5b (≈34.51–40.29 s) – INSERT, UPDATE and DELETE:**
"Same style and palette. Three change cards appear one after another in the lane and stay lit: a Green '+' card (INSERT), an Azure-tagged pair of a Coral '−' card and a Green '+' card (UPDATE), and a Coral '−' card (DELETE). Clean, uncluttered, phone-readable. No readable fine text, no logos, no watermark."
Motion: as the narrator says "INSERT," the Green card appears; on "UPDATE" the Azure-tagged pair appears; on "and DELETE operations" the Coral card appears; on "Streams help chesthayi" the lane glows. **Effect: Head stack.**
Overlay (post): "INSERT" with the Green card; "UPDATE" with the pair; "DELETE" with the Coral card.

**Audio sync:** each card appears as its word is spoken.
**Negative prompt (all shots):** "Copying the table's data into the stream, readable fine text, extra operation types, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – The three metadata columns (≈40.29–56.75 s · ≈16.46 s)
**Voice-over:** "Stream lo mainly three metadata columns untayi. First, METADATA$ACTION – INSERT or DELETE ani identify chesthundhi. Second, METADATA$ISUPDATE – update operation lo part aa kaadha ani indicate chesthundhi. Third, METADATA$ROW_ID – row ni uniquely identify cheyyadaniki use avuthundhi."
**Tone:** clear, structured.
**Visual objective:** Every change record carries three metadata columns: ACTION, ISUPDATE and ROW_ID.
Generate as **four shots (6a–6d)**. Keep the card position and the badge position identical so the list reads as one sequence.

**Shot 6a (≈40.29–43.48 s) – three metadata columns:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Metadata Gold #FFD166, Table Glass #E8EDF5, text #F5F7FA. One change card (Green '+') floats at the centre of the Teal lane. Three empty Gold chips slide in and attach to its right edge one after another, like extra columns. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: as the narrator says "Stream lo mainly three metadata columns untayi." the three Gold chips attach one by one.
Overlay (post): "3 METADATA COLUMNS" from the start of the line.

**Shot 6b (≈43.48–47.78 s) – 1 · METADATA$ACTION:**
"Same style and palette. The first Gold chip lights up on a Green card, showing a small '+' glyph, then on a Coral card, showing a small '−' glyph, to show that the action is either INSERT or DELETE. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark."
Motion: as the narrator says "First," the badge appears; on "METADATA$ACTION" the chip glows (**Effect: Press font** — the column name presses in); on "INSERT or DELETE ani identify chesthundhi" the chip shows '+' on the Green card and '−' on the Coral card.
Overlay (post, monospace): "1 · METADATA$ACTION"; "INSERT or DELETE".

**Shot 6c (≈47.78–52.45 s) – 2 · METADATA$ISUPDATE:**
"Same style and palette, plus Update Azure #5AA9FF. An UPDATE pair (a Coral '−' card and a Green '+' card) slides in joined by an Azure tag, and the second Gold chip lights on both cards with a small tick glyph, to show that they are part of an update. A single stand-alone Green card beside them has its chip dim (not part of an update). A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark."
Motion: as the narrator says "Second," the badge appears; on "METADATA$ISUPDATE" the chip glows (**Effect: Press font**); on "update operation lo part aa kaadha ani indicate chesthundhi" the tick lights on the pair and the stand-alone card's chip stays dim.
Overlay (post, monospace): "2 · METADATA$ISUPDATE"; "PART OF AN UPDATE?".

**Shot 6d (≈52.45–56.75 s) – 3 · METADATA$ROW_ID:**
"Same style and palette. Each change card shows a small unique fingerprint glyph (a tiny pattern of dots, no readable text) on the third Gold chip, and a thin line links a card back to exactly one row of the table. A numbered badge '3'. Calm, clear. No readable text, no logos, no watermark."
Motion: as the narrator says "Third," the badge appears; on "METADATA$ROW_ID" the chip glows (**Effect: Press font**); on "row ni uniquely identify cheyyadaniki use avuthundhi" the line links the card to its row. **Effect: Rack focus** — focus pulls from the card to the row it points to.
Overlay (post, monospace): "3 · METADATA$ROW_ID"; "IDENTIFIES A ROW UNIQUELY".

**Audio sync:** chips attach as the narrator says "three metadata columns"; each badge appears on "First,", "Second," and "Third,".
**Negative prompt (all shots):** "Other metadata columns, readable fine text, specific row values, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (≈56.75–82.27 s · ≈25.52 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana CUSTOMER table lo daily thousands of changes jaruguthunnayi. Ippudu Stream create cheddham! CREATE STREAM CUSTOMER_STREAM ON TABLE CUSTOMER; Changes ni check cheyyadaniki: SELECT * FROM CUSTOMER_STREAM; Ippudu source table lo changes jariginappudu, Stream change records ni expose chesthundhi. Manam ee changes ni downstream processing kosam use cheyyachu."
**Tone:** storytelling, focused.
**Visual objective:** Create a stream on the CUSTOMER table, read its change records, and use them downstream.
Generate as **six shots (7a–7f)**. All shots use the same camera language and layout (CUSTOMER table on the left, the Teal lane in the centre, the code panel when shown).

**Shot 7a (≈56.75–59.20 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Table Glass #E8EDF5, text #F5F7FA. A sleek abstract Table Glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from the start of the line.

**Shot 7b (≈59.20–62.76 s) – daily thousands of changes:**
"Same style and palette. A large Table Glass CUSTOMER table block shimmers as many tiny Green, Azure and Coral flickers appear across it all the time, like a steady rain of small changes. A small calendar-page glyph shows that this happens daily. No readable fine text, no logos."
Overlay (post): "CUSTOMER" (monospace) on "CUSTOMER table"; "DAILY THOUSANDS OF CHANGES" on "daily thousands of changes".

**Shot 7c (≈62.76–68.40 s) – CREATE STREAM:**
"Same style and palette. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) slides in at the centre with a thin Teal edge. As the statement types, a Teal lane draws itself beside the CUSTOMER table, empty and ready. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: as the narrator says "Ippudu Stream create cheddham!" the panel slides in; on "CREATE STREAM CUSTOMER_STREAM ON TABLE CUSTOMER;" line 1 types, then line 2 types, and the Teal lane draws. **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE STREAM CUSTOMER_STREAM
ON TABLE CUSTOMER;
```
"CREATE STREAM CUSTOMER_STREAM" as the name is spoken; "ON TABLE CUSTOMER;" right after.

**Shot 7d (≈68.40–73.30 s) – SELECT * FROM CUSTOMER_STREAM:**
"Same style and palette. A new line of code appears under the first. As it types, a few Green, Azure/Coral and Coral change cards appear in the Teal lane, each with its three Gold chips. The cursor then points at the cards. No readable code, no logos, no watermark."
Motion: as the narrator says "Changes ni check cheyyadaniki:" a cursor appears; on "SELECT * FROM CUSTOMER_STREAM;" the code types and the cards appear in the lane. **Effect: Code body.**
Overlay (post, monospace; the second statement shown under the first):
```sql
SELECT *
FROM CUSTOMER_STREAM;
```
"SELECT *" and "FROM CUSTOMER_STREAM;" as they are spoken.

**Shot 7e (≈73.30–78.34 s) – the Stream exposes the change records:**
"Same style and palette. In the table, a few new rows change (one Green, one Azure/Coral pair, one Coral). Each change instantly appears as a card in the Teal lane, lit and in order. The rest of the table stays dark and calm. Satisfying. No readable fine text, no logos."
Motion: as the narrator says "Ippudu source table lo changes jariginappudu," the rows change; on "Stream change records ni expose chesthundhi" the cards appear in the lane. **Effect: Rack focus** — focus pulls from the table to the lane.
Overlay (post): "SOURCE TABLE CHANGES" then "STREAM EXPOSES THE CHANGE RECORDS".

**Shot 7f (≈78.34–82.27 s) – use the changes downstream:**
"Same style and palette. The change cards slide along a thin Teal line to a small glass 'downstream' processing block (a gear glyph) on the right, which lights up. Only the cards travel, not the table. Calm, satisfying. No readable fine text, no logos."
Motion: as the narrator says "Manam ee changes ni downstream processing kosam use cheyyachu." the cards travel and the gear block lights.
Overlay (post): "USE THE CHANGES FOR DOWNSTREAM PROCESSING".

**Audio sync:** every overlay is timed to the sentence it belongs to; final times come from the audio.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake code in the generated video, wrong syntax, extra statements, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (≈82.27–93.69 s · ≈11.42 s)
**Voice-over:** "So, simple ga gurthupettukondi! Snowflake Streams help us capture table changes without processing the entire table again. Streams are an important building block for CDC pipelines."
**Tone:** confident.
**Visual objective:** Recap: Streams capture changes without re-processing the whole table, and they are a building block for CDC pipelines.
Generate as **two shots (8a, 8b)**.

**Shot 8a (≈82.27–89.76 s) – keep it simple: capture changes only:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Insert Green #6EE06E, Update Azure #5AA9FF, Delete Coral #FF5C6C, Table Glass #E8EDF5, text #F5F7FA. The table and the Teal lane glide to the centre with a soft bloom. The change cards ride in the lane while the table stays dark and calm; a faint ghost of a whole-table scan beam appears and is cancelled by a soft Teal 'not needed' flash. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: as the narrator says "So, simple ga gurthupettukondi!" the elements glide in; on "capture table changes" the cards ride; on "without processing the entire table again" the ghost scan is cancelled. **Effect: Liquid glass** — the recap line sits on a glass panel.
Overlay (post): "KEEP IT SIMPLE"; "CAPTURE TABLE CHANGES"; "WITHOUT PROCESSING THE ENTIRE TABLE AGAIN".

**Shot 8b (≈89.76–93.69 s) – a building block for CDC pipelines:**
"Same style and palette. The Teal lane becomes the first block in a longer pipeline: it connects with a thin Teal line to two more glass blocks that fade in, as the start of a CDC pipeline. Clean and calm. No readable text, no logos."
Motion: as the narrator says "Streams are an important building block for CDC pipelines." the first block lights and the next two blocks fade in.
Overlay (post): "STREAMS: A BUILDING BLOCK FOR CDC PIPELINES".

**Audio sync:** ghost scan cancelled on "without processing the entire table again"; pipeline on "CDC pipelines".
**Negative prompt:** "Technical claims beyond the script, numbers, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (≈93.69–103.03 s · ≈9.34 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty-Five! Next video lo Snowflake Tasks gurinchi real-time automation example tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 25 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (≈93.69–97.99 s) – Day 25 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Insert Green #6EE06E, Update Azure #5AA9FF, Metadata Gold #FFD166, text #F5F7FA. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty-five lit in Teal (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 25" as "Thirty Days of Snowflake" is spoken; the twenty-fifth node lights on "Twenty-Five".

**Shot 9b (≈97.99–103.03 s) – teaser: Snowflake Tasks:**
"Same style and palette. A teaser panel slides in showing a glass clock-dial and a small chain of two or three glass blocks that light up one after another on a schedule, as simple automation. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: SNOWFLAKE TASKS" on "Snowflake Tasks"; "REAL-TIME AUTOMATION EXAMPLE" on "real-time automation example". The visual only suggests a schedule and a chain. Do not show how Tasks work, settings or numbers.

**Audio sync:** card on "Thirty Days of Snowflake"; the twenty-fifth node on "Twenty-Five"; teaser title on "Snowflake Tasks".
**Negative prompt:** "Technical claims about Tasks, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (≈103.03–114.96 s · ≈11.93 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (≈103.03–108.81 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #161B22, Stream Teal #2FD5C5, Insert Green #6EE06E, Update Azure #5AA9FF, Metadata Gold #FFD166, text #F5F7FA. A calm, clean background with a soft teal glow, a small table and a Teal lane with a few change cards drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" on "Data Engineering concepts Telugu lo"; "FOLLOW @NDREDTECH ON INSTAGRAM" from the word "Instagram", emphasised on "Follow".

**Shot 10b (≈108.81–112.74 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Teal and Gold glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from "Full course details", emphasised on "Contact". **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (≈112.74–114.96 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from the start of the last line. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 25. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #161B22, Insert Green #6EE06E, Update Azure #5AA9FF, Delete Coral #FF5C6C, Stream Teal #2FD5C5, Metadata Gold #FFD166, Table Glass #E8EDF5, text #F5F7FA, secondary text #9AA5B5. Colour code: a table = a Table Glass block with rows of cells; a Stream = a Teal glass lane beside the table that fills with small change cards; an INSERT = a Green '+' card; a DELETE = a Coral '−' card; an UPDATE = a Coral '−' card and a Green '+' card joined by a small Azure tag (an update is recorded as a delete plus an insert); the three metadata columns = three Gold chips on every change card. The Stream carries only the changes, never a copy of the whole table, and the table stays dark and calm while the lane is active. Never show readable data, counts, timings or numbers beyond the script. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no people, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows) – to do when the audio is added

No audio was available, so no Whisper analysis was run. When `Audio\day25.mp3` is added, run the same workflow as Day 9–24: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`, then use the end of each pause as the phrase start. Or just ask me to do it.

## 6. Editing and synchronisation plan

1. When the voice-over is ready, import it as the master audio track at 100% and do not alter it.
2. Generate the clips, then place them on the timeline using the **measured** times (after the audio has been analysed). Until then, treat the times in this file as a rough guide only.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, `METADATA$ACTION`, `METADATA$ISUPDATE`, `METADATA$ROW_ID`, the two SQL statements, and the CTA lines) at the times the audio gives. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a soft card slide, a chip click, a gentle lane hum) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at each of the three incident sentences, at "Exactly!", at the three metadata badges, at each SQL statement, at the recap, at the final tagline, and at the Follow and Contact lines. Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- **All timings are estimated** (see the status note at the top). Re-run with the audio before final editing.
- Technical content is kept to what the script says: a Stream tracks data changes in a table (a Change Data Capture mechanism); it identifies INSERT, UPDATE and DELETE operations; it has three metadata columns: METADATA$ACTION (INSERT or DELETE), METADATA$ISUPDATE (part of an update or not) and METADATA$ROW_ID (a unique row identifier); in the banking example `CREATE STREAM CUSTOMER_STREAM ON TABLE CUSTOMER;` creates the stream, `SELECT * FROM CUSTOMER_STREAM;` reads the change records, and the changes can be used for downstream processing. **No counts, timings or sizes** are shown beyond the script's "daily thousands of changes". Both SQL statements are valid Snowflake syntax.
- The drawing of an UPDATE as a pair (a delete card and an insert card joined by a tag) follows how Streams record updates. The script itself only says that METADATA$ISUPDATE indicates whether a record is part of an update.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
