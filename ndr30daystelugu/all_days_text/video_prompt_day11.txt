# Thirty Days of Snowflake – Day 11: Snowflake Time Travel
Video prompt package (NDR EdTech) — script.txt + audio.mp3, analysed with Whisper
Opening conversation: Arjun (he) and Meera (she), cartoon characters from `character_reference.png`

> **Timing status: MEASURED from audio.mp3 (125.15 s).**
> - Word times come from Whisper (faster-whisper, `small` model, English mode, Windows CPU), cross-checked against the silences in the audio (`silencedetect`, -20 dB for the conversation, -26 dB for the rest). **Phrase starts are taken from the end of each pause, so they are the most exact.** Whisper word times can be 0.1–0.3 s early or late. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from Whisper.
> - **Voices:** `she:` lines are mapped to the female voice and `he:` lines to the male voice **from your script labels**. I did not run a voice-gender detector on the audio, so please listen once: the first line (0.00–2.36 s, "Arey! Oka problem vachindhi ra!") should be the female voice.
>
> **Please check these before generating (3 items):**
> 1. **OFFSET needs a minus sign.** Your script (and the audio) says `AT (OFFSET => Sixty multiplied by five)`. In Snowflake, a Time Travel OFFSET is the number of seconds **back** from now, so it must be negative: `AT (OFFSET => -60*5)`. Without the minus the query is not valid for "five minutes ago". The on-screen code in this package shows `-60*5`. The narration will still say "sixty multiplied by five". Consider re-recording that phrase as "minus sixty multiplied by five", or keep the on-screen minus as the correction.
> 2. **54.08 s:** Whisper heard "80" where your script says **AT** ("AT and BEFORE keywords"). This is almost certainly a mishearing, and the overlays use AT.
> 3. **Follow and Contact lines (about 117–123 s):** Whisper reordered the Telugu words into English order, so the "Follow" and "Contact" word times are estimated (≈).

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 11: Snowflake Time Travel |
| Duration | **125.15 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 3,755 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `audio.mp3` is the master track. No replacement narration or voices. Optional subtle music, ducked under speech. |
| Style | **Part 1 (0–37.07 s):** flat-vector cartoon conversation (Arjun and Meera) on a motion-graphics set. **Part 2 (37.07 s–end):** premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography (same as Day 8–10). |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips. 33 shots in 12 scenes. Some shots are 2–4 s; generate a longer clip and trim it, or hold the last frame in the edit. |
| Lip sync | Most AI video tools cannot lip-sync to your uploaded audio. Generate the characters with natural mouth motion, then apply a lip-sync pass in post (or use a tool with audio-driven lip sync). Do not rely on the generator for exact mouth sync. |

### Fresh palette – "Chrono Emerald" (new for Day 11)
| Role | HEX | Use |
|---|---|---|
| Background | `#07130F` | Base, gradients (near-black green) |
| Emerald | `#10B981` | Time Travel, restored and recovered data, brand glow |
| Mint | `#6EE7B7` | Highlights, glows, "OK" states |
| Ice Cyan | `#67E8F9` | Clock dial, timeline, past versions of data |
| Alert Crimson | `#E11D48` | Deleted records, the mistake |
| Primary text | `#F3FBF7` | Titles, labels |
| Secondary text | `#8DB5A5` | Captions |

The two characters **keep their own colours** (orange, amber, brown, grey) in every video. The dark green background makes the orange characters stand out.

**Meaning of colour (use in every scene):** Emerald and Mint = data that is safe or recovered · Ice Cyan = time (dial, timeline, previous versions) · Crimson = deletion and the mistake.

### Motion effects used (from the skill's effects library)
Impact frame, Day dial, Liquid glass, Press font, Blade slice, Live cursor, Blow away (for deleted rows, which really are deleted), Orbit ring, Code body, Comment drop, Rack focus, Letter dive, Head stack. Each is named in the scene where it appears.

### Voice-to-character mapping
| Character | Voice | Detected from | Description | Screen position |
|---|---|---|---|---|
| Arjun | Male | Script label `he:` (audio not diarized) | Young man, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, small soft smile, orange collared shirt under a grey-brown checked jacket | Left |
| Meera | Female | Script label `she:` (audio not diarized) | Young woman, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top | Right |

Upload `character_reference.png` as the character/reference image for every Part 1 shot.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase. The **[emotion]** tags from your script are expression cues only and never appear on screen.

### Part 1 – Conversation (0.00–37.07 s)

| Shot | Scene time | Speaker | Emotion | Spoken phrase (speech time) | Visual beat |
|---|---|---|---|---|---|
| 1a | 0.00–5.55 | Meera (female) | worried | "Arey! Oka problem vachindhi ra!" (0.00–2.36) | Meera rushes in, hands raised |
| 1a | | Arjun (male) | confused | "Enti ra? Malli production lo ఏమైనా issue vachindha?" (2.75–5.41) | Arjun tilts head, one eyebrow up |
| 1b | 5.55–9.85 | Meera | panicking | "Adhi kaadhu ra… CUSTOMER table lo 2,000 records delete chesesanu!" (5.69–9.72) | Close-up on Meera, glass table losing rows |
| 1c | 9.85–16.73 | Arjun | shock | "WHATTT! 😱 2,000 records aa? Backup undha?" (9.97–13.19) | Impact frame, wide eyes |
| 1c | | Meera | tired | "Ledhu ra… Ippudu manager ki em cheppali?" (13.49–16.56) | Meera slumps, empty backup shelf |
| 1d | 16.73–22.48 | Arjun | serious | "Simple ra… Resignation letter ready, Chesuko! 😂" (16.90–19.70) | Deadpan, then laughs |
| 1d | | Meera | playfully sarcastic | "Arey! Konchem help cheyyara babu!" (19.97–22.34) | Smirk, hands wave |
| 1e | 22.48–26.75 | Arjun | curious | "Wait ra! Manam Snowflake, use chesthunnam kada?" (22.63–25.07) | Finger raised, snowflake glint |
| 1e | | Meera | confused | "Avunu… ayithe?" (25.35–26.54) | Head tilt |
| 1f | 26.75–32.40 | Arjun | confident | "Snowflake lo Time Travel ane powerful feature undhi ra! Dheenitho previous data ni recover cheyyachu!" (26.97–32.12, pause 29.78–30.28) | Clock-dial appears and turns back |
| 1g | 32.40–37.07 | Meera | excited | "Nijanganaa? Mari ela use Cheyyali?" (32.55–34.97) | Leans in, eyes bright |
| 1g | | Arjun | energetic | "Adhe ippudu mana video lo chuddam!" (35.18–36.89) | Both turn to the dial, which floods the frame |

### Part 2 – Narrated video (37.07–125.15 s)

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 2 | 37.07–39.22 | "Welcome to NDR EdTech!" (37.26–39.02) | Energetic transition | Dial glow settles into the brand welcome |
| 3 | 39.22–45.55 | "Snowflake Time Travel ante previous state lo unna data ni access cheyyadaniki, recover cheyyadaniki use chese feature." (39.41–43.46, 43.67–45.38) | Clear | Table block with ghost past versions |
| 4 | 45.55–53.40 | "Dheenitho manam accidentally deleted tables ni recover cheyyachu," (45.71–48.99) · "previous data ni query cheyyachu," (49.28–50.92) · "and historical changes ni compare cheyyachu." (51.15–53.23) | Clear | Recover, query, compare |
| 5 | 53.40–61.51 | "Time Travel lo AT and BEFORE keywords use chesi specific timestamp," (53.56–57.82) · "offset, or statement-based historical data ni access cheyyachu." (58.07–61.35) | Clear | AT / BEFORE keywords, three ways to point to the past |
| 6 | 61.51–73.20 | "Oka Banking project example teesukundham." (61.68–63.60) · "Mana CUSTOMER table lo 10000 records unnayi." (63.94–66.25) · "Mistake valla 2000 records delete ayyayi." (66.56–68.80) · "Ippudu Time Travel use chesi five minutes mundu unna data ni retrieve cheyyachu." (69.12–73.04) | Storytelling | Banking table loses 2,000 rows, dial rewinds five minutes |
| 7 | 73.20–79.51 | "SQL Example:" (73.37–74.44) · "SELECT * FROM CUSTOMER" (74.83–76.71) · "AT (OFFSET => Sixty multiplied by five);" (76.99–79.33) | Focused | Code builds line by line |
| 8 | 79.51–87.25 | "Ee query five minutes mundu unna CUSTOMER table data ni retrieve chesthundhi," (79.68–83.33) · "provided aa data Time Travel retention period lo available unte." (83.63–87.09) | Clear | Result table, retention window condition |
| 9 | 87.25–97.10 | "Deleted records ni restore cheyyadaniki:" (87.40–89.42) · "CREATE TABLE CUSTOMER_RESTORED AS SELECT * FROM CUSTOMER AT (OFFSET => Sixty multiplied by five);" (89.72–96.92) | Focused | Restore code, new table appears |
| 10 | 97.10–106.65 | "So, simple ga gurthupettukondi!" (97.29–98.96) · "Time Travel ante mana database ki oka rewind button laantidhi!" (99.23–102.39) · "Mistakes jarigina kuda historical data ni recover cheyyadaniki help chesthundhi." (102.67–106.50) | Confident | Database with rewind button |
| 11 | 106.65–114.38 | "Idi mana Thirty Days of Snowflake series lo Day Eleven!" (106.79–109.61) · "Next video lo Zero-Copy Cloning gurinchi real-time examples tho explain chesthanu." (109.95–114.26) | Upbeat | Day 11 card, Zero-Copy Cloning teaser |
| 12 | 114.38–125.15 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (114.51–119.74) · "Full course details kosam NDR EdTech ni Contact avvandi!" (120.07–122.94) · "Let's Learn and Grow Together!" (123.20–124.84) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.60–1.04, 2.40–2.70, 3.28–3.61, 5.42–5.67, 6.50–6.91, 10.45–10.92, 12.17–12.56, 13.21–13.49, 14.36–14.75, 16.59–16.84, 17.44–17.93, 19.05–19.37, 19.71–19.96, 20.56–20.81, 22.37–22.60, 22.97–23.40, 25.09–25.35, 25.83–26.23, 26.56–26.85, 29.81–30.23, 32.31–32.55, 33.22–33.61, 34.97–35.18, 36.91–37.20, 39.02–39.41, 43.46–43.67, 45.38–45.71, 48.99–49.28, 50.92–51.15, 53.23–53.56, 57.82–58.07, 61.35–61.68, 63.60–63.94, 66.25–66.56, 68.80–69.12, 73.04–73.37, 74.44–74.83, 76.71–76.99, 79.33–79.68, 83.33–83.63, 87.09–87.40, 89.42–89.72, 92.16–92.39, 96.92–97.29, 98.96–99.23, 102.39–102.67, 106.50–106.79, 109.61–109.95, 114.26–114.51, 119.74–120.07, 122.94–123.20, 124.84–125.15.

### Appendix A – Key trigger times
Words use your script's spelling. Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Arey! Oka problem vachindhi ra! | Arey 0.00 · Oka problem 1.04–1.6 · ra ≈2.2 |
| Enti ra? Malli production lo ఏమైనా issue vachindha? | Enti ra 2.75 · production ≈3.9 · issue ≈4.6 · vachindha ≈5.1 |
| Adhi kaadhu ra… CUSTOMER table lo 2,000 records delete chesesanu! | Adhi kaadhu ra 5.69 · CUSTOMER table ≈6.9–7.5 · 2,000 records ≈8.0–8.5 · delete chesesanu ≈8.8 |
| WHATTT! 2,000 records aa? Backup undha? | WHATTT 9.97 · 2,000 records 10.92–11.5 · Backup undha 12.61 |
| Ledhu ra… Ippudu manager ki em cheppali? | Ledhu 13.49 · Ippudu 14.89 · manager ≈15.4 · cheppali ≈16.1 |
| Simple ra… Resignation letter ready, Chesuko! | Simple 16.90 · Resignation 17.93 · letter 18.44 · ready 18.6 · Chesuko 19.38 |
| Arey! Konchem help cheyyara babu! | Arey 19.97 · Konchem help 20.83 · babu ≈22.0 |
| Wait ra! Manam Snowflake, use chesthunnam kada? | Wait 22.63 · Snowflake ≈23.7 · kada ≈24.8 |
| Avunu… ayithe? | Avunu 25.35 · ayithe 26.23 |
| Snowflake lo Time Travel ane powerful feature undhi ra! | Snowflake ≈26.97 · Time Travel 27.58–28.26 · powerful ≈28.6 |
| Dheenitho previous data ni recover cheyyachu! | previous data ≈30.7 · recover ≈31.5 |
| Nijanganaa? Mari ela use Cheyyali? | Nijanganaa 32.55 · Mari ela use 33.63 · Cheyyali ≈34.5 |
| Adhe ippudu mana video lo chuddam! | Adhe 35.18 · video ≈36.0 · chuddam ≈36.5 |
| Welcome to NDR EdTech! | Welcome 37.26 · NDR 37.82 · EdTech 38.44 |
| Snowflake Time Travel ante previous state lo unna data ni access cheyyadaniki, recover cheyyadaniki use chese feature | Snowflake 39.41 · Time Travel 39.92–40.2 · previous state ≈41.0–41.7 · access ≈43.0 · recover 43.68 |
| Dheenitho manam accidentally deleted tables ni recover cheyyachu | accidentally 46.5 · deleted 46.96 · tables 47.46 · recover ≈48.2 |
| previous data ni query cheyyachu | previous data 49.28–49.48 · query ≈50.2 |
| and historical changes ni compare cheyyachu | historical changes 51.28–51.7 · compare ≈52.4 |
| Time Travel lo AT and BEFORE keywords use chesi | Time Travel ≈53.6 · **AT** ≈54.1 · **BEFORE** ≈55.1 · keywords 55.44 · use chesi ≈56.0 |
| specific timestamp, offset, or statement-based historical data ni access cheyyachu | timestamp 57.1 · offset ≈58.1 · statement ≈58.8 · historical data 59.54 · access cheyyachu ≈60.5 |
| Oka Banking project example teesukundham | Banking 61.76 · project 62.2 · example 62.58 |
| Mana CUSTOMER table lo 10000 records unnayi | CUSTOMER 64.02 · 10,000 ≈65.3 · records 65.56 |
| Mistake valla 2000 records delete ayyayi | Mistake ≈66.6 · 2,000 ≈67.4 · delete ayyayi ≈68.2 |
| Ippudu Time Travel use chesi five minutes mundu unna data ni retrieve cheyyachu | Time Travel 69.24–69.68 · five minutes ≈70.8 · retrieve ≈72.2 |
| SQL Example: | SQL 73.37 · Example ≈73.8 |
| SELECT * FROM CUSTOMER | SELECT ≈74.85 · * ≈75.3 · FROM ≈75.6 · CUSTOMER ≈76.0 |
| AT (OFFSET => Sixty multiplied by five); | AT ≈77.0 · OFFSET ≈77.3 · Sixty ≈78.0 · multiplied ≈78.3 · five ≈79.0 |
| Ee query five minutes mundu unna CUSTOMER table data ni retrieve chesthundhi | query ≈79.8 · five minutes ≈80.6 · CUSTOMER table ≈81.5 · retrieve ≈82.6 |
| provided aa data Time Travel retention period lo available unte | provided 83.63 · Time Travel 84.86 · retention 85.34 · period 85.72 · available ≈86.4 |
| Deleted records ni restore cheyyadaniki | Deleted 87.4 · restore ≈88.3 |
| CREATE TABLE CUSTOMER_RESTORED AS SELECT * FROM CUSTOMER AT (OFFSET => Sixty multiplied by five); | CREATE TABLE ≈89.8 · CUSTOMER_RESTORED 90.4–92.1 · AS 92.4 · SELECT * ≈92.8 · FROM CUSTOMER ≈93.5 · AT 94.1 · OFFSET 94.5 · Sixty 95.5 · multiplied 95.9 · five 96.6 |
| So, simple ga gurthupettukondi! | So 97.29 · gurthupettukondi ≈98.0 |
| Time Travel ante mana database ki oka rewind button laantidhi! | Time Travel 99.2–99.7 · database ≈102.0 · **rewind** ≈101.2 · button 101.6 |
| Mistakes jarigina kuda historical data ni recover cheyyadaniki help chesthundhi | Mistakes 102.67 · historical data ≈104.3 · recover ≈105.2 · help chesthundhi ≈106.0 |
| Idi mana Thirty Days of Snowflake series lo Day Eleven! | Thirty ≈107.1 · Days 107.46 · Snowflake 107.9 · series 108.38 · Day 108.6 · Eleven 109.08 |
| Next video lo Zero-Copy Cloning gurinchi real-time examples tho explain chesthanu | Next 110.02 · Zero-Copy Cloning 110.88–111.42 · real-time 112.24–112.52 · examples 112.76 |
| Ilanti Data Engineering concepts Telugu lo nerchukovadaniki | Data Engineering 115.06 · concepts 115.52 · Telugu 116.18 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈117.1 · NDR EdTech ≈117.8–118.6 · **Follow** ≈119.0 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full 120.07 · course ≈120.6 · details ≈121.2 · NDR EdTech ≈121.4–122.0 · **Contact** ≈122.4 (estimated) |
| Let's Learn and Grow Together! | Let's 123.20 · Learn 123.48 · and 123.76 · Grow 124.02 · Together 124.28 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7.*

**Character line used in Part 1 (repeat it in full in every conversation shot; also upload `character_reference.png` as the reference image):**
*"Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, small soft smile, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Arjun always stays on the left and Meera on the right, waist-up, in the lower 60% of the vertical frame."*

**Table look (Part 2, keep identical in every scene):** a glass table block with rows of small glowing cells. Normal data = Emerald cells. Past versions = Ice Cyan translucent ghost copies stacked behind it. Deleted rows = Crimson.

---

## PART 1 – CONVERSATION

### Scene 1 – Conversation (0.00–37.07 s · 37.07 s)
**Visual objective:** Meera has deleted 2,000 records, Arjun first panics, then remembers Snowflake Time Travel, and the pair hand off to the video.
**Set:** a soft, uncluttered dark-green data-office background with a few blurred glowing glass server tiles. The characters are in the lower 60% of the frame, so the upper 40% is free for the glass table and dial props and for the logo.
Generate as **seven shots (1a–1g)**.

**Shot 1a (0.00–5.55 s) – the problem:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, small soft smile, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot in a dark-green data-office with soft glowing glass server tiles in the background. Meera enters from the right, worried, hands raised and eyebrows tilted up, and speaks. Arjun turns to her, confused, head tilted, one eyebrow raised, and answers. Natural mouth movement while each speaks, subtle idle motion on the listener. No readable text, no extra people, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 0.00–0.56 s: Meera steps in and raises her hands on "Arey!".
- 1.04–2.36 s: she speaks, shoulders tense, and glances at the floor on "problem vachindhi ra!".
- 2.36–2.75 s: Arjun turns toward her.
- 2.75–5.41 s: Arjun tilts his head with a raised eyebrow on "Enti ra?" and scratches his head on "production lo issue vachindha?".
- Camera: slow push-in to the two-shot.
**Audio sync:** speaker switch at 2.75 s; Arjun's head tilt lands on "Enti ra?".
**On-screen text:** none (optional "THIRTY DAYS OF SNOWFLAKE · DAY 11" tag in post at 0.5 s in the top safe zone).
**Negative prompt:** "Swapped voices, changed character appearance, extra people, distorted faces, mismatched lip movement, photorealistic faces, readable text, clutter, flicker, off-palette background, watermark."

**Shot 1b (5.55–9.85 s) – 2,000 records deleted:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Meera (right): a young woman in a flat-vector cartoon style with clean outlines and soft shading, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Arjun (left, partly in frame): a young man in the same style, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, orange collared shirt under a grey-brown checked jacket. Close-up on Meera, panicking, wide eyes, hands to her head. Above her, a small glass table block with rows of Emerald cells loses a chunk of rows that turn Crimson and vanish. Arjun listens at the left edge. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 5.69–6.49 s: Meera shakes her head on "Adhi kaadhu ra…".
- 6.91–8.5 s: she grips her hair, the glass table appears on "CUSTOMER table lo 2,000 records" (≈6.9–8.5 s).
- 8.8–9.72 s: about one fifth of the rows turn Crimson and disperse on "delete chesesanu!". **Effect: Blow away** (accurate: these rows really are deleted).
**Audio sync:** rows vanish at ≈8.8 s on "delete".
**On-screen text (overlay, post):** "CUSTOMER" at ≈6.9 s; "2,000 RECORDS" at ≈8.2 s.
**Negative prompt:** "Swapped voices, changed character appearance, readable text on the table, real database logos, distorted faces, flicker, clutter, watermark."

**Shot 1c (9.85–16.73 s) – shock and no backup:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot. Arjun jolts back in shock, very wide eyes, mouth open, hands up. Then Meera slumps, tired, shoulders drooping. In the upper background an empty dim glass shelf (a missing backup) glows faintly. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 9.97–10.24 s: Arjun jolts back on "WHATTT!". **Effect: Impact frame** — a one-frame punch-in and flash at 9.97 s.
- 10.92–12.15 s: he leans toward Meera on "2,000 records aa?".
- 12.61–13.19 s: he spreads his hands on "Backup undha?" and the empty shelf fades in.
- 13.49–14.30 s: Meera sighs and slumps on "Ledhu ra…".
- 14.89–16.56 s: she lifts her hands helplessly on "Ippudu manager ki em cheppali?".
**Audio sync:** flash at 9.97 s; shelf at 12.61 s; slump at 13.49 s.
**On-screen text (overlay, post):** none (optional "NO BACKUP" at 13.49 s).
**Negative prompt:** "Swapped voices, changed character appearance, extra people, distorted faces, blood or violence, readable text, flicker, clutter, watermark."

**Shot 1d (16.73–22.48 s) – the joke:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot. Arjun is deadpan and serious, then holds up a blank paper (a joke resignation letter, no readable text) and bursts out laughing. Meera gives a playful sarcastic smirk and an eye roll, waving her hands for help. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 16.90–17.41 s: Arjun deadpan, arms crossed, on "Simple ra…".
- 17.93–19.03 s: he holds up the blank paper on "Resignation letter ready".
- 19.38–19.70 s: he laughs and points at her on "Chesuko!".
- 19.97–20.51 s: Meera rolls her eyes on "Arey!".
- 20.83–22.34 s: she smirks and waves her hands on "Konchem help cheyyara babu!".
**Audio sync:** paper at 17.93 s; laugh at 19.38 s; eye roll at 19.97 s.
**On-screen text (overlay, post):** none. Keep the paper blank.
**Negative prompt:** "Swapped voices, changed character appearance, readable letter text, real company names, distorted faces, flicker, clutter, watermark."

**Shot 1e (22.48–26.75 s) – the idea:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot. Arjun suddenly perks up, raises one finger, curious. A small Ice Cyan snowflake glint appears above him. Meera tilts her head, confused. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 22.63–22.94 s: Arjun raises a finger on "Wait ra!".
- 23.40–25.07 s: the snowflake glint appears on "Manam Snowflake" (≈23.7 s) and he points at the screen on "use chesthunnam kada?".
- 25.35–25.81 s: Meera nods slowly on "Avunu…".
- 26.23–26.54 s: she tilts her head on "ayithe?".
**Audio sync:** finger at 22.63 s; snowflake at ≈23.7 s; Meera's tilt at 26.23 s.
**On-screen text (overlay, post):** none.
**Negative prompt:** "Swapped voices, changed character appearance, extra people, distorted faces, readable text, flicker, clutter, watermark."

**Shot 1f (26.75–32.40 s) – Time Travel:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, small confident smile, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot. Arjun smiles confidently and points up. A glowing Ice Cyan clock-dial (glass, no numerals) appears in the upper centre between them and turns backwards, and a small glass table block beside it regains its missing Crimson rows as Emerald cells. Meera's eyes widen with hope. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 26.97–27.5 s: Arjun grins and straightens on "Snowflake lo".
- 27.58–28.26 s: the clock-dial fades in on "Time Travel".
- 28.6–29.78 s: it glows and spins slowly on "powerful feature undhi ra!".
- 30.28–32.12 s: the dial turns back, the table regains its rows (≈31.5 s on "recover") on "Dheenitho previous data ni recover cheyyachu!". **Effect: Day dial.**
**Audio sync:** dial appears at 27.58 s; reverses at ≈30.5 s; rows return at ≈31.5 s.
**On-screen text (overlay, post):** "TIME TRAVEL" at 27.58 s.
**Negative prompt:** "Swapped voices, changed character appearance, readable numerals on the dial, specific retention numbers, distorted faces, flicker, clutter, watermark."

**Shot 1g (32.40–37.07 s) – hand-off to the video:**
"Create a vertical 9:16 flat-vector cartoon motion-graphics shot for NDR EdTech. Palette for the background and props: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. Arjun (left): a young man in a flat-vector cartoon style with clean outlines and soft shading, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, orange collared shirt under a grey-brown checked jacket. Meera (right): a young woman in the same style, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Waist-up two-shot. Meera leans in, excited, big smile and bright eyes. Arjun, energetic, pumps a fist. Both turn to look at the glowing Ice Cyan clock-dial floating between them. The dial grows, its glow floods the whole frame in Emerald and Mint light and the characters are swept out of view. Natural mouth movement. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 32.55–33.20 s: Meera leans forward on "Nijanganaa?".
- 33.63–34.97 s: she clasps her hands on "Mari ela use Cheyyali?".
- 35.18–36.0 s: Arjun pumps his fist on "Adhe ippudu mana video…".
- 36.0–36.89 s: both turn to the dial, which grows on "lo chuddam!" (video ≈36.0 s).
- 36.89–37.07 s: the glow floods the frame, **Effect: Impact frame** (soft flash) for the cut into Scene 2.
**Audio sync:** dial grows at ≈36.0 s; flash completes in the pause at 36.91–37.20 s.
**On-screen text (overlay, post):** none.
**Negative prompt:** "Swapped voices, changed character appearance, extra people, distorted faces, readable text, flicker, clutter, watermark."

---

## PART 2 – NARRATED VIDEO

### Scene 2 – Welcome transition (37.07–39.22 s · 2.15 s)
**Voice-over:** "Welcome to NDR EdTech!"
**Tone:** energetic transition.
**Visual objective:** Turn the dial's glow into the brand welcome.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A glowing Ice Cyan clock-dial (glass, no numerals) settles at the upper-centre into a glass snowflake-crystal emblem with a soft Emerald bloom. A reserved clean area at the top for the logo and clean space below for a title. Quick light sweep, smooth push-in, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 37.07–37.26 s: the glow settles from the previous shot.
- 37.26–39.02 s: the emblem forms and blooms on "Welcome to NDR EdTech!".
- Effect: **Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** logo and panel at 37.26 s; "NDR" at 37.82 s; "EdTech" at 38.44 s.
**On-screen text (overlay, post):** exact NDR EdTech logo and "WELCOME TO NDR EDTECH".
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – What is Snowflake Time Travel? (39.22–45.55 s · 6.33 s)
**Voice-over:** "Snowflake Time Travel ante previous state lo unna data ni access cheyyadaniki, recover cheyyadaniki use chese feature."
**Tone:** clear.
**Visual objective:** Time Travel lets you access and recover data as it was in a previous state.

**Visual generation prompt:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A glass table block with rows of small Emerald cells floats at the centre. Behind it, three translucent Ice Cyan ghost copies of the table recede in depth like earlier versions on a timeline. A glass clock-dial (no numerals) glows above them. Soft rim lighting, slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:**
- 39.41–40.8 s: the table block appears on "Snowflake Time Travel ante".
- 41.0–42.4 s: the ghost copies slide back in depth on "previous state lo unna data".
- 42.6–43.46 s: the camera reaches toward a ghost copy on "access cheyyadaniki".
- 43.67–45.38 s: a ghost copy slides forward and becomes solid Emerald on "recover cheyyadaniki use chese feature". **Effect: Day dial** — the dial turns back as the ghosts appear.
**Audio sync:** ghosts at ≈41.0 s; "access" at ≈43.0 s; recover at 43.68 s.
**On-screen text (overlay, post):** "SNOWFLAKE TIME TRAVEL" from 39.92 s; "ACCESS · RECOVER PREVIOUS DATA" from ≈42.6 s.
**Negative prompt:** "Retention numbers, readable table text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Recover, query, compare (45.55–53.40 s · 7.85 s)
**Voice-over:** "Dheenitho manam accidentally deleted tables ni recover cheyyachu, previous data ni query cheyyachu, and historical changes ni compare cheyyachu."
**Tone:** clear.
**Visual objective:** Three things Time Travel lets you do.
Generate as **three shots (4a–4c)**.

**Shot 4a (45.55–49.13 s) – recover deleted tables:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. A glass table block with a Crimson edge breaks into particles and disappears, then the particles gather back in reverse and the table re-forms in Emerald with a soft glow. Numbered badge '1'. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 45.71–46.5 s the table disperses on "manam accidentally"; 46.96–47.46 s empty space on "deleted tables"; ≈48.0–48.99 s particles re-form on "recover cheyyachu". **Effect: Blow away**, played in reverse for the recovery.
Overlay (post): "1 · RECOVER DELETED TABLES" from 46.5 s.

**Shot 4b (49.13–51.04 s) – query previous data:**
"Same style and palette. A cursor moves over an Ice Cyan translucent past version of the table and a few rows highlight in Mint, as if being read. Numbered badge '2'. No readable text, no logos, no watermark."
Motion: 49.28–49.48 s the ghost version appears on "previous data"; ≈50.2–50.92 s the cursor highlights rows on "query cheyyachu". **Effect: Live cursor.**
Overlay (post): "2 · QUERY PREVIOUS DATA" from 49.28 s.

**Shot 4c (51.04–53.40 s) – compare historical changes:**
"Same style and palette. A glass table splits down the middle into an Ice Cyan 'before' half and an Emerald 'now' half, with a few rows glowing in Mint and Crimson where they differ. Numbered badge '3'. No readable text, no logos, no watermark."
Motion: 51.28–51.7 s the table splits on "historical changes"; ≈52.2–53.2 s the differing rows light up on "compare cheyyachu". **Effect: Blade slice.**
Overlay (post): "3 · COMPARE HISTORICAL CHANGES" from 51.28 s.

**Audio sync:** badge 1 at 46.5 s; badge 2 at 49.28 s; badge 3 at 51.28 s.
**Negative prompt:** "Readable table text, retention numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – AT and BEFORE keywords (53.40–61.51 s · 8.11 s)
**Voice-over:** "Time Travel lo AT and BEFORE keywords use chesi specific timestamp, offset, or statement-based historical data ni access cheyyachu."
**Tone:** clear.
**Visual objective:** The AT and BEFORE keywords reach historical data using a timestamp, an offset, or a statement.
Generate as **two shots (5a, 5b)**.

**Shot 5a (53.40–57.95 s) – the two keywords:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. Two glass keyword plates, one Emerald and one Ice Cyan, are pressed into place side by side above a timeline that stretches into the distance. A small Ice Cyan clock chip lights up on the timeline. Soft rim lighting, slow push-in, clean space for the keywords and a caption. No readable fine text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: ≈53.6 s the timeline appears on "Time Travel lo"; ≈54.1 s the Emerald plate presses in on "AT"; ≈55.1 s the Ice Cyan plate presses in on "BEFORE"; ≈57.1 s the clock chip lights on "timestamp". **Effect: Press font.**
Overlay (post): "AT" at ≈54.1 s and "BEFORE" at ≈55.1 s, large and crisp.

**Shot 5b (57.95–61.51 s) – three ways to point to the past:**
"Same style and palette. Three glass chips (an Ice Cyan clock chip for timestamp, a dial-with-arrow chip for offset, a query-card chip for statement) orbit slowly around the clock-dial. Then they link to a glowing timeline and one past version of a table lights up in Mint. No readable fine text, no logos, no watermark."
Motion: ≈58.1 s the offset chip appears on "offset"; ≈58.8 s the statement chip appears on "statement-based"; 59.54–61.35 s the past version lights on "historical data ni access cheyyachu". **Effect: Orbit ring.**
Overlay (post): "TIMESTAMP" (kept from 5a), "OFFSET" at ≈58.1 s, "STATEMENT" at ≈58.8 s.

**Audio sync:** keywords at ≈54.1 and ≈55.1 s (check by ear); chips at 57.1, 58.1 and 58.8 s.
**Negative prompt:** "Readable fake syntax, extra keywords, retention numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – Banking project example (61.51–73.20 s · 11.69 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana CUSTOMER table lo 10000 records unnayi. Mistake valla 2000 records delete ayyayi. Ippudu Time Travel use chesi five minutes mundu unna data ni retrieve cheyyachu."
**Tone:** storytelling.
**Visual objective:** The 10,000-row table loses 2,000 rows, then Time Travel gets them back.
Generate as **four shots (6a–6d)**. Same camera language so the story reads as one continuous build.

**Shot 6a (61.51–63.77 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A sleek abstract glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass table frame below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from 61.76 s.

**Shot 6b (63.77–66.41 s) – CUSTOMER table, 10,000 records:**
"Same style and palette. The glass table frame fills with rows of Emerald cells, a full, dense table. A counter-style glow runs along its side. No readable fine text, no logos."
Overlay (post): "CUSTOMER" at 64.02 s; "10,000 RECORDS" at ≈65.3 s.

**Shot 6c (66.41–68.96 s) – the mistake:**
"Same style and palette, plus Alert Crimson #E11D48. About one fifth of the table's rows flash Crimson and then disperse into particles, leaving a visible gap. A small Crimson warning glow pulses at the gap. No readable fine text, no logos."
Motion: 66.56–67.3 s a small warning pulse on "Mistake valla"; ≈67.4–68.2 s the rows flash Crimson on "2000 records"; ≈68.2–68.8 s they disperse on "delete ayyayi". **Effect: Blow away.**
Overlay (post): "2,000 RECORDS DELETED" at ≈67.4 s.

**Shot 6d (68.96–73.20 s) – five minutes back:**
"Same style and palette, plus Time Travel Ice #67E8F9. A glass clock-dial appears beside the table and turns backwards. An Ice Cyan arc marks the five-minute step back. The table's missing rows return as Emerald cells, and the table is full again. No readable fine text, no logos."
Motion: 69.12–70.7 s the dial appears on "Ippudu Time Travel use chesi"; ≈70.8–71.8 s the dial turns back along the arc on "five minutes mundu"; ≈72.2–73.04 s the rows return on "retrieve cheyyachu". **Effect: Day dial.**
Overlay (post): "5 MINUTES BACK" at ≈70.8 s.

**Audio sync:** every overlay is timed to Appendix A. Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake numbers, wrong colours (deletion must be Crimson, recovery Emerald), clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 7 – SQL example (73.20–79.51 s · 6.31 s)
**Voice-over:** "SQL Example: SELECT * FROM CUSTOMER AT (OFFSET => Sixty multiplied by five);"
**Tone:** focused.
**Visual objective:** Show the query being written line by line.
Generate as **two shots (7a, 7b)**.

**Shot 7a (73.20–76.85 s) – SELECT * FROM CUSTOMER:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A dark glass code editor panel (a clean window with empty lines, no readable code) floats at the centre with a thin Emerald edge and a blinking cursor. A small glass table block sits behind it, softly out of focus. Slow push-in. Keep the panel clean so that crisp code can be overlaid in post. No readable code, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 73.37–74.44 s the panel slides in on "SQL Example"; ≈74.85 s the cursor starts typing on "SELECT"; ≈75.6–76.71 s the second line types on "FROM CUSTOMER". **Effect: Code body.**
Overlay (post, monospace):
```sql
SELECT *
FROM CUSTOMER
```
"SELECT *" at ≈74.85 s; "FROM CUSTOMER" at ≈75.6 s.

**Shot 7b (76.85–79.51 s) – AT (OFFSET => -60*5):**
"Same style and palette. The code panel continues, and an Ice Cyan clock-dial glow appears at the end of the last line, as if time is being set. The camera pushes in slowly on the third line. No readable code, no logos, no watermark."
Motion: ≈77.0 s the third line starts on "AT"; ≈77.3 s the dial glow appears on "OFFSET"; ≈78.0–79.0 s the offset value completes on "Sixty multiplied by five".
Overlay (post, monospace):
```sql
SELECT *
FROM CUSTOMER
AT (OFFSET => -60*5);
```
"AT (OFFSET => -" at ≈77.0 s; "60*5);" at ≈78.0 s. The narration omits "minus", the on-screen minus is the correct form (see the note at the top).

**Audio sync:** line 1 at 74.85 s; line 2 at ≈75.6 s; line 3 at ≈77.0 s.
**Negative prompt:** "Readable fake code in the generated video, wrong syntax, extra lines, clutter, flicker, off-palette colours, watermark."

---

### Scene 8 – What the query returns, and the condition (79.51–87.25 s · 7.74 s)
**Voice-over:** "Ee query five minutes mundu unna CUSTOMER table data ni retrieve chesthundhi, provided aa data Time Travel retention period lo available unte."
**Tone:** clear.
**Visual objective:** The query returns the table as it was five minutes ago, if that data is still inside the Time Travel retention period.
Generate as **two shots (8a, 8b)**.

**Shot 8a (79.51–83.48 s) – five minutes before:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. The code panel shrinks to the top. Below it a glass table block appears as the Ice Cyan ghost of the table from five minutes ago, then turns solid Emerald with all its rows, as the query result. A small dial arc marks 'five minutes back'. Slow push-in, clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: ≈79.8 s the panel shrinks on "Ee query"; ≈80.6–81.5 s the dial arc shows on "five minutes mundu"; ≈81.5–82.6 s the table turns solid on "CUSTOMER table data"; ≈82.6–83.33 s the rows glow on "retrieve chesthundhi".
Overlay (post): "5 MINUTES AGO" at ≈80.6 s; "CUSTOMER" at ≈81.5 s.

**Shot 8b (83.48–87.25 s) – the retention condition:**
"Same style and palette. A horizontal timeline with a glowing glass band (the retention period) near 'now'. Table versions inside the band glow Emerald and are reachable; older versions beyond the band fade to dim grey-green and are unreachable. A small glass note drops beside the band. No readable text, no numbers, no logos, no watermark."
Motion: 83.63–84.8 s the timeline appears on "provided aa data"; 84.86–85.72 s the band lights on "Time Travel retention period"; ≈86.4–87.09 s the version inside the band glows on "available unte". **Effect: Comment drop** — a small note drops in beside the band at ≈85.3 s ("retention").
Overlay (post): "ONLY IF DATA IS WITHIN THE RETENTION PERIOD" from 83.63 s.

**Audio sync:** band lights at 85.34 s ("retention"); the version glows at ≈86.4 s.
**Negative prompt:** "Specific retention numbers (days or hours), readable text, wrong claims about data older than the retention period, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Restore the deleted records (87.25–97.10 s · 9.85 s)
**Voice-over:** "Deleted records ni restore cheyyadaniki: CREATE TABLE CUSTOMER_RESTORED AS SELECT * FROM CUSTOMER AT (OFFSET => Sixty multiplied by five);"
**Tone:** focused.
**Visual objective:** Create a new table from the five-minutes-ago data.
Generate as **three shots (9a–9c)**.

**Shot 9a (87.25–89.57 s) – restore intro:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7. A glass table block with a visible gap where Crimson rows once were. Faint Ice Cyan ghost rows hover in the gap, waiting to return. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 87.40–88.3 s the ghost rows appear on "Deleted records"; ≈88.3–89.42 s they glow on "restore cheyyadaniki".
Overlay (post): "RESTORE DELETED RECORDS" from 87.40 s. **Effect: Press font.**

**Shot 9b (89.57–92.27 s) – CREATE TABLE CUSTOMER_RESTORED:**
"Same style and palette. A dark glass code editor panel (clean, no readable code) with a blinking cursor. A small empty glass table frame outlined in Mint appears beside it, waiting to be created. No readable code, no logos, no watermark."
Motion: ≈89.8–90.3 s the first words type on "CREATE TABLE"; 90.4–92.1 s the table name types on "CUSTOMER_RESTORED" and the Mint frame glows. **Effect: Code body.**
Overlay (post, monospace): `CREATE TABLE CUSTOMER_RESTORED AS` from ≈89.8 s (full name by ≈92.1 s).

**Shot 9c (92.27–97.10 s) – AS SELECT … AT (OFFSET => -60*5):**
"Same style and palette. The code panel continues with the SELECT lines. At the end of the last line an Ice Cyan dial glow turns back, and the Mint frame fills with rows of Emerald cells: a complete new table. The camera pulls back to show the original table and the new restored table side by side. No readable code, no logos, no watermark."
Motion: ≈92.8–94.3 s the SELECT lines type on "AS SELECT * FROM CUSTOMER"; 94.1–96.9 s the AT line types and the dial glow turns on "AT (OFFSET => Sixty multiplied by five)"; ≈96.0–96.92 s the new table fills with rows. **Effect: Code body.**
Overlay (post, monospace; build line by line):
```sql
CREATE TABLE CUSTOMER_RESTORED AS
SELECT *
FROM CUSTOMER
AT (OFFSET => -60*5);
```
Lines appear at: line 1 ≈89.8 s, line 2 ≈92.8 s, line 3 ≈93.5 s, line 4 at 94.1 s with `-60*5);` at ≈95.5 s.

**Audio sync:** line 1 at ≈89.8 s; line 4 at 94.1 s; the new table completes before 96.92 s.
**Negative prompt:** "Readable fake code in the generated video, wrong syntax, extra lines, wrong table names, clutter, flicker, off-palette colours, watermark."

---

### Scene 10 – Rewind-button recap (97.10–106.65 s · 9.55 s)
**Voice-over:** "So, simple ga gurthupettukondi! Time Travel ante mana database ki oka rewind button laantidhi! Mistakes jarigina kuda historical data ni recover cheyyadaniki help chesthundhi."
**Tone:** confident.
**Visual objective:** Time Travel works like a rewind button for the database.
Generate as **three shots (10a–10c)**.

**Shot 10a (97.10–99.09 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A calm glass database cylinder glows at the centre with a soft Emerald bloom against the dark green background. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈97.8 s.

**Shot 10b (99.09–102.53 s) – the rewind button:**
"Same style and palette. A large glass rewind button (two left-pointing triangles) lights up in Ice Cyan on the front of the glass database cylinder. It is pressed, and the database's glowing rows run backwards. Soft rim lighting, quick crisp motion. No readable text, no logos, no watermark."
Motion: 99.23–99.74 s the cylinder is highlighted on "Time Travel"; ≈101.2 s the button is pressed on "rewind"; 101.6–102.39 s the rows run back on "button laantidhi". **Effect: Impact frame** — a one-frame flash at ≈101.2 s.
Overlay (post): "TIME TRAVEL = REWIND BUTTON" from 99.23 s.

**Shot 10c (102.53–106.65 s) – recover historical data:**
"Same style and palette. After the rewind, a Crimson crack in the table (the mistake) is healed by Emerald light and the table is whole again, with Ice Cyan past versions glowing behind it. Soft bloom, calm confident feel. No readable text, no logos, no watermark."
Motion: 102.67–104.0 s the crack appears on "Mistakes jarigina kuda"; ≈104.3 s the past versions glow on "historical data"; ≈105.2–106.5 s the Emerald light heals the table on "recover cheyyadaniki help chesthundhi". **Effect: Rack focus** — focus pulls from the crack to the healed table at ≈105.2 s.
Overlay (post): "RECOVER HISTORICAL DATA" from ≈104.3 s.

**Audio sync:** button press at ≈101.2 s; healing at ≈105.2 s.
**Negative prompt:** "Readable text, retention numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 11 – Series card and Zero-Copy Cloning teaser (106.65–114.38 s · 7.73 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Eleven! Next video lo Zero-Copy Cloning gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 11 and tease the next topic.
Generate as **two shots (11a, 11b)**.

**Shot 11a (106.65–109.78 s) – Day 11 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first eleven lit in Emerald (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 11" from ≈107.1 s; the eleventh node lights at 109.08 s on "Eleven".

**Shot 11b (109.78–114.38 s) – teaser:**
"Same style and palette. A teaser panel slides in with one glass table block. A second, matching table block appears beside it, joined by a thin Mint light line, like a clone. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: ZERO-COPY CLONING" from 110.88 s; "REAL-TIME EXAMPLES" from 112.24 s. The visual only suggests a second table appearing from the first. Do not imply storage sizes, cost or other technical behaviour.

**Audio sync:** card at ≈107.1 s; the eleventh node at 109.08 s; the clone appears at 111.04 s ("copy").
**Negative prompt:** "Technical claims about cloning, storage numbers, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 12 – Follow, contact and end card (114.38–125.15 s · 10.77 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (12a–12c)**.

**Shot 12a (114.38–119.90 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, text #F3FBF7. A calm, clean background with a soft Emerald glow, a few small glass table blocks drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at 115.06 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈117.1 s, emphasised at ≈119.0 s on "Follow" (estimated).

**Shot 12b (119.90–123.07 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Emerald and Mint glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 120.07 s, emphasised at ≈122.4 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 12c (123.07–125.15 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 123.20 s. Hold the final frame for the last 0.3 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

**For all Part 2 scenes (and the backgrounds and props of Part 1):**
"NDR EdTech – Thirty Days of Snowflake, Day 11. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #07130F, Emerald #10B981, Mint #6EE7B7, Ice Cyan #67E8F9, Alert Crimson #E11D48, text #F3FBF7, secondary text #8DB5A5. Colour meaning: Emerald and Mint = safe or recovered data, Ice Cyan = time (clock-dial, timeline, previous versions), Crimson = deleted records. Tables are glass blocks with rows of small glowing cells. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No stock footage, no off-palette colours."

**Character consistency prompt (Part 1 only; also upload `character_reference.png`):**
"Two recurring characters in a flat-vector cartoon style with clean outlines, soft shading and large friendly eyes, waist-up, animated as 2D/2.5D motion graphics. Arjun (always on the left): a young man, light skin, dark brown tousled side-swept hair with a raised quiff, large brown eyes, thin eyebrows, small soft smile, orange collared shirt under a grey-brown checked jacket. Meera (always on the right): a young woman, light skin, long flowing wavy golden-orange hair with a side-swept fringe, large blue eyes, soft pink lips, orange/amber V-neck top. Never change their faces, hair, clothing or colours between shots. Natural mouth movement while speaking; expressive but friendly, not childish. Characters keep their own orange, amber and brown colours and sit in front of the dark-green #07130F background. No extra people, no photorealistic faces, no readable text."

---

## 5. Analyse the audio with Whisper (Windows)

This is how the timings in this file were produced (same workflow as Day 9 and 10).

1. **Create a virtual environment and install** (PowerShell, Python 3.10):
   ```powershell
   py -3.10 -m venv whisper-env
   .\whisper-env\Scripts\python.exe -m pip install faster-whisper
   ```
2. **Run the `run_whisper.py` script from Day 9's file** (`small` model, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`).
   ```powershell
   .\whisper-env\Scripts\python.exe run_whisper.py audio.mp3 whisper_out.json
   ```
3. **Cross-check with the real pauses** (use `-20dB` and `d=0.1` for the fast conversation part, `-26dB` and `d=0.2` for the narration):
   ```powershell
   ffmpeg -i audio.mp3 -af "silencedetect=noise=-20dB:d=0.1" -f null - 2>&1 | Select-String "silence_(start|end)"
   ```
4. **Build the timing map:** use the end of each silence as the phrase start, use Whisper word times for emphasis words, keep your script's spelling, and place scene cuts in the middle of a pause.

**Notes for this audio**
- Whisper in English mode wrote this Telugu-English narration as an English translation. Word *times* are usable, but the word *order* can differ from the Telugu (for example the Instagram/Follow and Contact lines), so those are marked ≈.
- Whisper sometimes places a word before the true start (for example "SELECT" at 74.34 s versus the pause end at 74.83 s). Pause ends were preferred for phrase starts.
- Voice gender was taken from your `she:` / `he:` labels. To confirm from the audio, run a speaker-diarization tool (for example pyannote.audio or WhisperX) and check that the `she:` turns are the female voice.

---

## 6. Editing and synchronisation plan

1. Import `audio.mp3` (125.15 s) as the master audio track and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. For Part 1, generate each shot with the reference image. Lip-sync the mouth movement to the audio in post if the tool cannot do it. Check that Arjun is on the left and Meera on the right in every shot.
4. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
5. Add crisp text and code overlays in the editor (titles, badges, the SQL code, numbers such as "10,000 RECORDS" and "2,000 RECORDS DELETED", and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code. Use the corrected `-60*5` form.
6. Add the exact NDR EdTech logo in the reserved area, unaltered.
7. Add optional subtle music, ducked about 15–20 dB under narration, plus light whooshes only in pauses. Keep the conversation clean: no music over the fast dialogue except a very light bed.
8. Check sync at the start, at each speaker change in Part 1 (2.75, 9.97, 13.49, 16.90, 19.97, 22.63, 25.35, 26.97, 32.55, 35.18 s), at the hand-off (36.0–37.26 s), at the AT and BEFORE keywords (≈54.1, ≈55.1 s), at each code line (74.85, ≈75.6, ≈77.0, ≈89.8, 94.1 s), at the rewind button (≈101.2 s), at the final tagline (123.20 s), and at the Follow and Contact lines (≈119.0, ≈122.4 s). Check readability on a phone.
9. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration, pauses and word times are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: Time Travel accesses and recovers data from a previous state; it can recover deleted tables, query previous data and compare historical changes; AT and BEFORE keywords work with a timestamp, an offset or a statement; and the data must still be inside the Time Travel retention period. **No retention periods (days) are shown**, because the script gives none. If you want them on screen, tell me and I'll verify the numbers against Snowflake's documentation first.
- The script's `AT (OFFSET => Sixty multiplied by five)` is corrected to `-60*5` on screen (see the note at the top).
- The conversation is a story device. The visuals do not claim that Meera's deletion was a `DELETE` statement or a `DROP`. They show rows disappearing and coming back.
- The 😱 and 😂 emojis are tone cues only and are shown through the characters' faces, not as on-screen emoji.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
