# Thirty Days of Snowflake – Day 20: Snowflake RBAC – Roles & Privileges
Video prompt package (NDR EdTech) — `Audio\day20.mp3` + `days-scripts\day20.txt`, analysed with Whisper

> **Timing status: MEASURED from day20.mp3 (140.59 s).**
> - **Phrase starts and ends come from the pauses** in the audio (`silencedetect`, -26 dB, 0.2 s), so they are the most exact. Whisper (faster-whisper, `small` model, English mode, Windows CPU) supplied phrase-level times. Times marked **≈** are estimates inside continuous speech.
> - Whisper writes Telugu as approximate English, so **all wording below is your script's**; only the times come from the audio. The audio matches your script, including the ending.
> - No `she:` / `he:` labels in the script, so this is a **single-narrator video** in the usual NDR EdTech motion-graphics style. No cartoon characters.
>
> **Please check these before generating (4 items):**
> 1. **The last 6 seconds are garbled in Whisper** ("follow-up and full course details course and NDR at Technique contact of Andy…"). The pauses are clear, so the lines are placed as: Follow ends at 134.80 s, **Contact line 135.15–138.33 s**, **tagline 138.64–140.22 s**. The "Follow" and "Contact" word times inside those lines are estimated (≈).
> 2. **SQL lines (77–104 s):** the five statements are separated by real pauses (77.64, 80.39, 85.80, 92.92, 100.77 s), so each statement's start is exact. The words inside a statement are estimated (≈).
> 3. **The example's story:** the script says developers need read and modify permissions, but the only role created is REPORTING_ROLE, and it is granted to user DEVA. The visuals show DEVA as a generic user who receives the reporting role. I did not label DEVA a developer.
> 4. **There is no scripted `[pause]`** in this script. The longest pause is 0.6 s.

---

## 1. Production overview

| Item | Setting |
|---|---|
| Title | Thirty Days of Snowflake – Day 20: Snowflake RBAC – Roles & Privileges |
| Duration | **140.59 s** (measured) |
| Format | 9:16 vertical, 30 FPS (≈ 4,218 frames) |
| Resolution | Master 2160 × 3840 if the tool supports it; otherwise 1080 × 1920 |
| Audio | `Audio\day20.mp3` is the master track at 100%. No replacement narration. Optional background sound effects or music at **50% volume**. |
| Style | Premium SaaS / tech-commercial motion graphics, polished 3D-inspired glass objects, clean UI, kinetic typography, smooth object-to-object transitions |
| Logo | Reserved clean area; add the exact NDR EdTech logo in post. Do not generate it. |
| Clip lengths | Most AI tools make 4–10 s clips, so scenes are split into shots (34 shots in 10 scenes). Some shots are 2–3 s; generate a longer clip and trim it, or hold the last frame in the edit. |

### Fresh palette – "Access Triad" (new for Day 20)
| Role | HEX | Use |
|---|---|---|
| Background | `#1B1530` | Base, gradients (dusty indigo) |
| User Coral | `#FF6F91` | **Users** (an abstract avatar dot, no faces) |
| Role Gold | `#FFCB47` | **Roles** (a golden badge) |
| Privilege Teal | `#22D3C5` | **Privileges** (a teal key) |
| Silver Glass | `#E6EAF5` | Database, schema, table, vault, SQL panels |
| Primary text | `#FAF8FF` | Titles, labels |
| Secondary text | `#A9A3C4` | Captions |

**Colour code (use in every scene):** the access chain is always **Privilege (Teal key) → granted to Role (Gold badge) → assigned to User (Coral avatar)**. Objects (database, schema, table) are Silver Glass.

**The core visual rule (technical accuracy):** in RBAC, permissions are **not assigned to users directly**. **Privileges are granted to roles, and roles are assigned to users.** So a Teal key always attaches to a Gold badge first, and the Gold badge is then given to a Coral user. Never draw a Teal key attached straight to a Coral user. Show abstract shapes only (no faces, no real names except the script's `DEVA`, `REPORTING_ROLE`, `BANK_DB`).

### Motion effects used (from the skill's effects library)
Post wall, Head stack, Letter dive, Impact frame, Liquid glass, Press font, Live cursor, Code body, Rack focus, Comment drop. Each is named in the scene where it appears.

---

## 2. Audio timing map (MEASURED)

Scene cuts sit at the midpoint of a pause so each visual change lands in silence. Times in brackets are speech start–end of each phrase.

| Scene | Scene time | Spoken phrase (speech time) | Emotion | Visual beat |
|---|---|---|---|---|
| 1 | 0.00–4.14 | "Hello guys! Andaru ela unnaru?" (0.00–2.08) · "Oka situation imagine cheyyandi!" (2.46–3.94) | Curious | Title hook |
| 2 | 4.14–16.23 | "Mee company lo 100 employees unnaru." (4.34–6.51) · "Andariki production database access isthara?" (6.96–9.18) · "Developers ki, testers ki, managers ki… andariki same permissions isthara?" (9.60–14.31) · "Definitely not kada!" (14.76–16.01) | Curious, then firm | 100 employees, same access for all? No |
| 3 | 16.23–27.80 | "Because company lo evariki entha access undalo decide cheyyali." (16.44–19.92) · "Snowflake lo deenikosam oka powerful security feature undhi!" (20.37–23.68) · "Adhe RBAC – Role-Based Access Control!" (24.06–27.62) | Excited, reveal | Decide who gets what, RBAC reveal |
| 4 | 27.80–31.22 | "Let's understand!" (27.98–28.68) · "Welcome to NDR EdTech!" (29.24–30.99) | Welcoming | Title and brand welcome |
| 5 | 31.22–38.20 | "RBAC ante users ki direct ga permissions assign cheyyakunda," (31.44–35.43) · "Roles through access control manage cheyyadam." (35.76–37.98) | Clear | Not direct, through roles |
| 6 | 38.20–60.08 | "First, User! User ante Snowflake account access chese individual." (38.41–43.05) · "Second, Role! Role anedhi permissions ni group chesi users ki assign chestham." (43.46–48.53) · "Third, Privileges! Privileges ante SELECT, INSERT, UPDATE, DELETE lanti permissions." (48.91–54.65) · "Snowflake lo roles ki privileges grant chestham, and users ki roles assign chestham." (55.05–59.87) | Clear, structured | User, Role, Privileges, the chain |
| 7 | 60.08–104.18 | "Oka Banking project example teesukundham." (60.29–62.24) · "Mana BANK_DB lo CUSTOMER table undhi." (62.58–65.49) · "Developers ki data read and modify permissions kavali." (65.84–68.89) · "Reporting team ki only SELECT permission kavali." (69.24–71.87) · "Ippudu reporting role create chesi SELECT permission grant cheyyachu." (72.22–75.60) · "SQL commands chuddam!" (75.97–77.20) · "CREATE ROLE REPORTING_ROLE;" (77.64–79.99) · "GRANT USAGE ON DATABASE BANK_DB TO ROLE REPORTING_ROLE;" (80.39–85.46) · "GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA TO ROLE REPORTING_ROLE;" (85.80–92.59) · "GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER TO ROLE REPORTING_ROLE;" (92.92–100.42) · "GRANT ROLE REPORTING_ROLE TO USER DEVA;" (100.77–103.97) | Storytelling, focused | Banking: reporting role, five SQL statements |
| 8 | 104.18–118.89 | "So, simple ga gurthupettukondi!" (104.38–106.18) · "User – Who accesses Snowflake." (106.53–108.66) · "Role – Group of permissions." (109.00–110.75) · "Privileges – What actions users can perform." (111.14–113.84) · "RBAC helps organizations manage secure and controlled data access." (114.24–118.70) | Confident | Three-card recap and the RBAC benefit |
| 9 | 118.89–128.83 | "Idi mana Thirty Days of Snowflake series lo Day Twenty!" (119.08–122.02) · "Next video lo Resource Monitors and Warehouse Cost Optimization gurinchi real-time examples tho explain chesthanu." (122.39–128.66) | Upbeat | Day 20 card, cost-control teaser |
| 10 | 128.83–140.59 | "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi!" (129.00–134.80) · "Full course details kosam NDR EdTech ni Contact avvandi!" (135.15–138.33) · "Let's Learn and Grow Together!" (138.64–140.22) | Upbeat, closing | Follow, contact, end card |

Silences longer than 0.2 s (safe cut points): 0.77–1.10, 2.08–2.46, 3.94–4.34, 6.51–6.96, 9.18–9.60, 12.28–12.61, 14.31–14.76, 16.01–16.44, 19.92–20.37, 23.68–24.06, 24.39–24.60, 25.76–26.13, 27.62–27.98, 28.68–29.24, 30.99–31.44, 35.43–35.76, 37.98–38.41, 38.87–39.12, 39.52–39.96, 43.05–43.46, 43.94–44.20, 44.56–44.93, 48.53–48.91, 49.20–49.54, 50.18–50.51, 52.61–52.86, 54.65–55.05, 57.72–57.99, 59.87–60.29, 62.24–62.58, 65.49–65.84, 68.89–69.24, 71.87–72.22, 75.60–75.97, 77.20–77.64, 79.99–80.39, 85.46–85.80, 92.59–92.92, 100.42–100.77, 103.97–104.38, 106.18–106.53, 106.92–107.29, 108.66–109.00, 109.34–109.64, 110.75–111.14, 111.74–111.97, 113.84–114.24, 118.70–119.08, 122.02–122.39, 128.66–129.00, 134.80–135.15, 138.33–138.64, 140.22–140.59.

### Appendix A – Key trigger times
Add 0.1–0.3 s tolerance. **≈** = estimated inside continuous speech.

| Phrase | Trigger times (s) |
|---|---|
| Mee company lo 100 employees unnaru. | **100 employees** ≈5.0–6.0 |
| Andariki production database access isthara? | production database ≈7.5 · access ≈8.5 |
| Developers ki, testers ki, managers ki… | Developers ≈9.8 · testers ≈10.8 · managers ≈11.7 |
| andariki same permissions isthara? | andariki 12.61 · same permissions ≈13.2 |
| Definitely not kada! | Definitely not 14.76 |
| Because company lo evariki entha access undalo decide cheyyali. | evariki entha access ≈17.6 · decide ≈19.0 |
| Snowflake lo deenikosam oka powerful security feature undhi! | powerful security feature ≈22.0 |
| Adhe RBAC – Role-Based Access Control! | Adhe 24.06 · **RBAC** 24.60 · Role-Based Access Control 26.13 |
| Let's understand! / Welcome to NDR EdTech! | Let's 27.98 · Welcome 29.24 · NDR ≈29.9 · EdTech ≈30.4 |
| RBAC ante users ki direct ga permissions assign cheyyakunda, | users ≈32.6 · direct ga ≈33.5 · assign cheyyakunda ≈34.4 |
| Roles through access control manage cheyyadam. | Roles 35.76 · access control ≈36.6 · manage ≈37.3 |
| First, User! | First 38.41 · User 39.12 |
| User ante Snowflake account access chese individual. | Snowflake account ≈40.6 · individual ≈42.2 |
| Second, Role! | Second 43.46 · Role 44.20 |
| Role anedhi permissions ni group chesi users ki assign chestham. | permissions ≈45.8 · group ≈46.6 · assign ≈47.8 |
| Third, Privileges! | Third 48.91 · Privileges 49.54 |
| Privileges ante SELECT, INSERT, UPDATE, DELETE lanti permissions. | SELECT ≈51.2 · INSERT ≈52.0 · UPDATE ≈53.0 · DELETE ≈53.7 |
| Snowflake lo roles ki privileges grant chestham, | roles ≈55.9 · privileges ≈56.6 · grant ≈57.4 |
| and users ki roles assign chestham. | users 58.0 · roles ≈58.8 · assign ≈59.4 |
| Oka Banking project example teesukundham. | Banking ≈60.7 · example ≈61.6 |
| Mana BANK_DB lo CUSTOMER table undhi. | BANK_DB ≈63.0 · CUSTOMER ≈64.2 |
| Developers ki data read and modify permissions kavali. | read ≈67.0 · modify ≈68.0 |
| Reporting team ki only SELECT permission kavali. | Reporting team ≈69.6 · only SELECT ≈70.6 |
| Ippudu reporting role create chesi SELECT permission grant cheyyachu. | reporting role ≈72.9 · SELECT ≈74.0 · grant ≈75.0 |
| SQL commands chuddam! | SQL 75.97 |
| CREATE ROLE REPORTING_ROLE; | CREATE ROLE 77.64–78.6 · REPORTING_ROLE ≈78.7–79.99 |
| GRANT USAGE ON DATABASE BANK_DB TO ROLE REPORTING_ROLE; | GRANT USAGE ON DATABASE 80.39–82.3 · BANK_DB ≈82.4–83.2 · TO ROLE REPORTING_ROLE ≈83.4–85.46 |
| GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA TO ROLE REPORTING_ROLE; | GRANT USAGE ON SCHEMA 85.80–87.6 · BANK_DB.CUSTOMER_SCHEMA ≈87.7–90.2 · TO ROLE REPORTING_ROLE ≈90.3–92.59 |
| GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER TO ROLE REPORTING_ROLE; | GRANT SELECT ON TABLE 92.92–95.0 · BANK_DB.CUSTOMER_SCHEMA.CUSTOMER ≈95.1–98.0 · TO ROLE REPORTING_ROLE ≈98.1–100.42 |
| GRANT ROLE REPORTING_ROLE TO USER DEVA; | GRANT ROLE 100.77–101.5 · REPORTING_ROLE ≈101.6–102.6 · TO USER DEVA ≈102.7–103.97 |
| So, simple ga gurthupettukondi! | So 104.38 · gurthupettukondi ≈105.2 |
| User – Who accesses Snowflake. | User 106.53 · Who accesses Snowflake 107.29 |
| Role – Group of permissions. | Role 109.00 · Group of permissions 109.64 |
| Privileges – What actions users can perform. | Privileges 111.14 · What actions users can perform 111.97 |
| RBAC helps organizations manage secure and controlled data access. | RBAC 114.24 · secure and controlled ≈116.6 · data access ≈118.0 |
| Idi mana Thirty Days of Snowflake series lo Day Twenty! | Thirty ≈119.8 · Snowflake ≈120.6 · Twenty ≈121.6 |
| Next video lo Resource Monitors and Warehouse Cost Optimization gurinchi real-time examples tho explain chesthanu. | Resource Monitors ≈123.5–124.8 · Warehouse Cost Optimization ≈125.0–126.5 · real-time examples ≈127.0 |
| Instagram lo NDR EdTech ni Follow avvandi! | Instagram ≈131.8 · NDR EdTech ≈132.4–133.4 · **Follow** ≈133.8 (estimated) |
| Full course details kosam NDR EdTech ni Contact avvandi! | Full course details 135.15–136.4 · NDR EdTech ≈136.6 · **Contact** ≈137.3 (estimated) |
| Let's Learn and Grow Together! | Let's 138.64 · Together ≈139.7 |

---

## 3. Scene-by-scene generation prompts

Every prompt is self-contained. The common palette line used below is: *background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, Silver Glass #E6EAF5, text #FAF8FF.*

**Object look (keep identical in every scene):** a **user** = a Coral glass avatar dot (a round head-and-shoulders glyph, no face). A **role** = a Gold glass badge. A **privilege** = a Teal glass key. **Objects** (database, schema, table) = Silver Glass. The chain is always **Teal key → Gold badge → Coral user**.

### Scene 1 – Hook (0.00–4.14 s · 4.14 s)
**Voice-over:** "Hello guys! Andaru ela unnaru? Oka situation imagine cheyyandi!"
**Tone:** curious.
**Visual objective:** Welcome viewers and ask them to imagine a situation.

**Visual generation prompt:**
"Create a premium vertical 9:16 cinematic motion-graphics opening shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, Silver Glass #E6EAF5, text #FAF8FF. A dusty-indigo space with soft light and drifting glass particles. A glowing Silver glass vault door at the upper-centre with a Teal glass key floating beside it, and a soft thought-bubble of glass forms above them. Keep the upper-middle clean for a title and the top corner clean for a logo. Smooth push-in camera, shallow depth of field. No rendered text, no logos, no watermark. 30 FPS, designed for a 4K vertical master."
**Motion instructions:**
- 0.00–2.08 s: particles drift in and the vault appears on "Hello guys! Andaru ela unnaru?".
- 2.46–3.94 s: the thought-bubble forms on "Oka situation imagine cheyyandi!".
- 3.94–4.14 s: soft light sweep into Scene 2.
- Effect: **Comment drop** — the thought-bubble drops in beside the vault at ≈2.7 s.
**Audio sync:** title lands at ≈1.1 s; the sweep completes in the pause at 3.94–4.34 s.
**On-screen text (overlay):** "THIRTY DAYS OF SNOWFLAKE" / "DAY 20".
**Negative prompt:** "Low resolution, flicker, jitter, malformed text, random logos, clutter, off-palette colours, cartoonish style, human faces, watermark, subtitles."

---

### Scene 2 – 100 employees: the same access for everyone? (4.14–16.23 s · 12.09 s)
**Voice-over:** "Mee company lo 100 employees unnaru. Andariki production database access isthara? Developers ki, testers ki, managers ki… andariki same permissions isthara? Definitely not kada!"
**Tone:** curious, then firm.
**Visual objective:** A company of 100 employees should not all get the same access to the production database.
Generate as **three shots (2a–2c)**.

**Shot 2a (4.14–6.74 s) – 100 employees:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Silver Glass #E6EAF5, text #FAF8FF. A neat wall of one hundred small Coral glass avatar dots (round head-and-shoulders glyphs, no faces) fills the frame in a tidy grid, appearing in waves. A small Silver glass company-building glyph (no logo) sits above. Clean space for a caption. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 4.34–5.0 s the building glyph appears on "Mee company lo"; ≈5.0–6.0 s the wall fills wave by wave on "100 employees"; 6.0–6.51 s it settles on "unnaru". **Effect: Post wall** — a wall of avatar cards appears.
Overlay (post): "100 EMPLOYEES" at ≈5.0 s.

**Shot 2b (6.74–9.39 s) – access to the production database?:**
"Same style and palette. A large Silver glass database cylinder labelled by a small shield glyph (no text) glows at the centre, with a gold-red 'production' beacon on top. All hundred Coral avatar dots turn toward it and thin lines of light reach for it from every dot. A soft question-mark glow pulses. No readable text, no logos, no watermark."
Motion: 6.96–8.0 s the database and beacon appear on "Andariki production database"; ≈8.0–9.18 s the lines reach for it on "access isthara?" (access ≈8.5 s).
Overlay (post): "PRODUCTION DATABASE" at ≈7.5 s; "ACCESS FOR EVERYONE?" from ≈8.0 s.

**Shot 2c (9.39–16.23 s) – the same permissions for all? Definitely not:**
"Same style and palette. Three groups of Coral avatars step forward, each wearing a different abstract badge shape (a code glyph for developers, a check glyph for testers, a chart glyph for managers). The same set of Teal keys is offered to all three groups, then a soft Silver barrier flashes and the keys fade away from the groups, showing 'no'. Calm, firm. No readable text, no logos, no watermark."
Motion: 9.60–12.28 s the three groups step forward on "Developers ki, testers ki, managers ki…" (Developers ≈9.8 s, testers ≈10.8 s, managers ≈11.7 s); 12.61–14.31 s the same keys are offered to all on "andariki same permissions isthara?"; 14.76–16.01 s the barrier flashes on "Definitely not kada!". **Effect: Impact frame** — a one-frame flash at 14.76 s.
Overlay (post): "DEVELOPERS · TESTERS · MANAGERS" from ≈9.8 s; "SAME PERMISSIONS FOR ALL?" from 12.61 s; "DEFINITELY NOT!" at 14.76 s.

**Audio sync:** wall at ≈5.0 s; database at 6.96 s; groups at 9.8, 10.8, 11.7 s; flash at 14.76 s.
**Negative prompt (all shots):** "Human faces, readable text, real department names, clutter, flicker, off-palette colours, watermark."

---

### Scene 3 – Decide who gets what: RBAC (16.23–27.80 s · 11.57 s)
**Voice-over:** "Because company lo evariki entha access undalo decide cheyyali. Snowflake lo deenikosam oka powerful security feature undhi! Adhe RBAC – Role-Based Access Control!"
**Tone:** excited, reveal.
**Visual objective:** Access must be decided per person, and Snowflake's feature for it is RBAC.
Generate as **three shots (3a–3c)**.

**Shot 3a (16.23–20.15 s) – decide how much access:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Privilege Teal #22D3C5, Silver Glass #E6EAF5, text #FAF8FF. Three Coral avatar dots stand in front of a Silver glass vault. Each is offered a different number of Teal keys: one avatar gets three keys, another gets one, another gets two, shown as small glowing key-clusters. A soft balance-scale glyph glows above. Calm, thoughtful. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 16.44–17.6 s the avatars and vault appear on "Because company lo"; ≈17.6–19.0 s the key clusters of different sizes appear on "evariki entha access undalo"; ≈19.0–19.92 s the balance-scale glows on "decide cheyyali".
Overlay (post): "DECIDE WHO GETS HOW MUCH ACCESS" from ≈17.6 s.

**Shot 3b (20.15–23.87 s) – a powerful security feature:**
"Same style and palette. The Silver vault door gleams and a glowing glass snowflake-crystal emblem rises above it with a soft shield outline. Mysterious, then hopeful. Slow push-in. No readable text, no logos, no watermark."
Motion: 20.37–22.0 s the vault gleams on "Snowflake lo deenikosam oka"; ≈22.0–23.68 s the emblem and shield rise on "powerful security feature undhi!".
Overlay (post): "A POWERFUL SECURITY FEATURE" from ≈22.0 s.

**Shot 3c (23.87–27.80 s) – RBAC:**
"Same style and palette. The shield opens into a clean chain of three icons: a Teal key, a Gold badge and a Coral avatar, connected by thin light lines. Big clean space above for a title. Soft light burst. No rendered text, no logos, no watermark."
Motion: 24.06–24.39 s a soft glow on "Adhe"; 24.60–25.76 s the title lands on "RBAC" (**Effect: Impact frame** — one-frame flash at 24.60 s; **Effect: Letter dive** — the letters settle fully before 25.7 s); 26.13–27.62 s the full name appears on "Role-Based Access Control!".
Overlay (post): "RBAC" at 24.60 s; "ROLE-BASED ACCESS CONTROL" at 26.13 s.

**Audio sync:** keys at ≈17.6 s; vault at 20.37 s; title at 24.60 s; full name at 26.13 s.
**Negative prompt:** "Misspelled title, fake logos, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 4 – Title and welcome (27.80–31.22 s · 3.42 s)
**Voice-over:** "Let's understand! Welcome to NDR EdTech!"
**Tone:** welcoming.
**Visual objective:** Name the topic and welcome viewers.

**Visual generation prompt:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, Role Gold #FFCB47, Privilege Teal #22D3C5, User Coral #FF6F91, text #FAF8FF. A calm, clean welcome frame with the Teal key, Gold badge and Coral avatar resting in a row at the lower-centre. A reserved clean area at the top for the logo and a soft glow below it. Slow gentle light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
**Motion instructions:** 27.98–28.68 s a subtitle pops in on "Let's understand!"; 29.24–30.99 s a glass panel slides in on "Welcome to NDR EdTech!". **Effect: Liquid glass** — the welcome text sits on a translucent glass panel.
**Audio sync:** subtitle at 27.98 s; logo and panel at 29.24 s; "NDR" at ≈29.9 s.
**On-screen text (overlay, post):** "LET'S UNDERSTAND!" at 27.98 s; exact NDR EdTech logo and "WELCOME TO NDR EDTECH" at 29.24 s.
**Negative prompt:** "Fake logos, distorted logo, tiny text, clutter, flicker, off-palette colours, watermark."

---

### Scene 5 – What is RBAC? (31.22–38.20 s · 6.98 s)
**Voice-over:** "RBAC ante users ki direct ga permissions assign cheyyakunda, Roles through access control manage cheyyadam."
**Tone:** clear.
**Visual objective:** RBAC means not giving permissions directly to users, but managing access through roles.
Generate as **two shots (5a, 5b)**.

**Shot 5a (31.22–35.60 s) – not directly to users:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Privilege Teal #22D3C5, Silver Glass #E6EAF5, text #FAF8FF. A Teal glass key tries to attach straight to a Coral avatar dot; a soft Silver barrier blocks it and the key slides away with a gentle 'no' pulse. Clear, calm. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 31.44–32.6 s the key and avatar appear on "RBAC ante users ki"; ≈32.6–34.4 s the key moves toward the avatar on "direct ga permissions assign cheyyakunda" (direct ga ≈33.5 s); ≈34.4–35.43 s the barrier blocks it.
Overlay (post): "NOT DIRECTLY TO USERS" from ≈33.5 s.

**Shot 5b (35.60–38.20 s) – through roles:**
"Same style and palette, plus Role Gold #FFCB47. The Teal key clicks into a Gold badge, and the Gold badge is then handed to the Coral avatar along a light line. A soft Silver access-gate opens. Satisfying. No readable text, no logos, no watermark."
Motion: 35.76–36.6 s the key clicks into the badge on "Roles"; ≈36.6–38.0 s the badge is handed over on "through access control manage cheyyadam" (manage ≈37.3 s). **Effect: Press font** — "ROLES" presses in at 35.76 s.
Overlay (post): "ACCESS MANAGED THROUGH ROLES" from 35.76 s.

**Audio sync:** key tries at ≈33.5 s; key clicks into the badge at 35.76 s.
**Negative prompt (all shots):** "A key attached directly to a user in the final state, readable text, clutter, flicker, off-palette colours, watermark."

---

### Scene 6 – User, Role, Privileges (38.20–60.08 s · 21.88 s)
**Voice-over:** "First, User! User ante Snowflake account access chese individual. Second, Role! Role anedhi permissions ni group chesi users ki assign chestham. Third, Privileges! Privileges ante SELECT, INSERT, UPDATE, DELETE lanti permissions. Snowflake lo roles ki privileges grant chestham, and users ki roles assign chestham."
**Tone:** clear, structured.
**Visual objective:** Three building blocks (User, Role, Privileges) and how they connect.
Generate as **four shots (6a–6d)**. Keep the numbered-badge position identical so the list reads as one sequence.

**Shot 6a (38.20–43.26 s) – 1 · User:**
"Create a premium vertical 9:16 3D-inspired motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Silver Glass #E6EAF5, text #FAF8FF. A single large Coral glass avatar dot (head-and-shoulders glyph, no face) stands in front of a Silver glass door marked with a small snowflake-crystal glyph (no logo), as an individual entering a Snowflake account. A numbered badge '1'. Calm, clear. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Motion: 38.41–39.52 s the badge and title appear on "First, User!" (**Effect: Press font** — "USER" presses in at 39.12 s); 39.96–41.5 s the avatar approaches the door on "User ante Snowflake account"; ≈41.5–43.05 s the door opens for the individual on "access chese individual".
Overlay (post): "1 · USER" at 38.41 s; "AN INDIVIDUAL WHO ACCESSES A SNOWFLAKE ACCOUNT" from 39.96 s.

**Shot 6b (43.26–48.72 s) – 2 · Role:**
"Same style and palette, plus Role Gold #FFCB47. A large Gold glass badge appears. Several small Teal keys (permissions) gather into it and group together inside. The badge is then offered to two Coral avatars. A numbered badge '2'. Calm, clear. No readable text, no logos, no watermark."
Motion: 43.46–44.56 s the badge and title appear on "Second, Role!" (**Effect: Press font** — "ROLE" presses in at 44.20 s); 44.93–46.6 s the keys gather into the badge on "Role anedhi permissions ni group chesi" (group ≈46.6 s); ≈47.0–48.53 s the badge is offered to the avatars on "users ki assign chestham".
Overlay (post): "2 · ROLE" at 43.46 s; "GROUPS PERMISSIONS" from ≈45.8 s; "ASSIGNED TO USERS" from ≈47.8 s.

**Shot 6c (48.72–54.85 s) – 3 · Privileges:**
"Same style and palette, plus Privilege Teal #22D3C5. Four Teal glass keys appear one after another in a neat row, each with a different abstract icon: an eye (read), a plus (add), a pencil (change), a crossed bin (remove). Clean, uncluttered, phone-readable. A numbered badge '3'. No readable text, no logos, no watermark."
Motion: 48.91–50.18 s the badge and title appear on "Third, Privileges!" (**Effect: Press font** — "PRIVILEGES" presses in at 49.54 s); 50.51–52.61 s the first two keys appear on "Privileges ante SELECT, INSERT," (SELECT ≈51.2 s, INSERT ≈52.0 s); 52.86–54.65 s the other two appear on "UPDATE, DELETE lanti permissions" (UPDATE ≈53.0 s, DELETE ≈53.7 s). **Effect: Head stack.**
Overlay (post): "3 · PRIVILEGES" at 48.91 s; "SELECT" at ≈51.2 s; "INSERT" at ≈52.0 s; "UPDATE" at ≈53.0 s; "DELETE" at ≈53.7 s.

**Shot 6d (54.85–60.08 s) – the chain: privileges to roles, roles to users:**
"Same style and palette. A Teal key slides into a Gold badge, and then the Gold badge slides over to a Coral avatar, forming the chain Teal key → Gold badge → Coral avatar with soft light lines. Calm, satisfying. No readable text, no logos, no watermark."
Motion: 55.05–57.72 s the keys slide into the badge on "Snowflake lo roles ki privileges grant chestham," (roles ≈55.9 s, privileges ≈56.6 s, grant ≈57.4 s); 57.99–59.87 s the badge goes to the avatar on "and users ki roles assign chestham". **Effect: Rack focus** — focus pulls from the key to the avatar at ≈58.0 s.
Overlay (post): "PRIVILEGES → ROLES" at ≈56.0 s; "ROLES → USERS" at ≈58.0 s.

**Audio sync:** badge 1 at 38.41 s; badge 2 at 43.46 s; badge 3 at 48.91 s; the chain at 55.05 s.
**Negative prompt (all shots):** "Real names, human faces, a key attached directly to a user, readable fine text, clutter, flicker, off-palette colours, watermark."

---

### Scene 7 – Banking project example (60.08–104.18 s · 44.10 s)
**Voice-over:** "Oka Banking project example teesukundham. Mana BANK_DB lo CUSTOMER table undhi. Developers ki data read and modify permissions kavali. Reporting team ki only SELECT permission kavali. Ippudu reporting role create chesi SELECT permission grant cheyyachu. SQL commands chuddam! CREATE ROLE REPORTING_ROLE; GRANT USAGE ON DATABASE BANK_DB TO ROLE REPORTING_ROLE; GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA TO ROLE REPORTING_ROLE; GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER TO ROLE REPORTING_ROLE; GRANT ROLE REPORTING_ROLE TO USER DEVA;"
**Tone:** storytelling, focused.
**Visual objective:** Build a REPORTING_ROLE that can only read the CUSTOMER table, then give it to a user.
Generate as **ten shots (7a–7j)**. All shots use the same camera language and the same layout (BANK_DB database on the left, the code panel in the centre when shown, users on the right).

**Shot 7a (60.08–62.41 s) – banking setup:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, Role Gold #FFCB47, Privilege Teal #22D3C5, User Coral #FF6F91, Silver Glass #E6EAF5, text #FAF8FF. A sleek abstract Silver glass bank-vault shield motif (no real bank logo) glows at the upper-centre, with an empty glass layout below it. Soft push-in, rim light. Clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "BANKING PROJECT" from ≈60.7 s.

**Shot 7b (62.41–65.67 s) – BANK_DB and the CUSTOMER table:**
"Same style and palette. A Silver glass database cylinder opens like a nested set: a schema folder inside, and inside it a CUSTOMER table block with rows of cells. The camera dives in slowly. No readable fine text, no logos."
Overlay (post): "BANK_DB" at ≈63.0 s (monospace); "CUSTOMER TABLE" at ≈64.2 s.

**Shot 7c (65.67–69.07 s) – developers: read and modify:**
"Same style and palette. A group of Coral avatars with a code glyph (developers) stands beside the table. Two Teal keys appear for them: an eye (read) and a pencil (modify). No readable text, no logos."
Motion: 65.84–66.8 s the developer avatars appear on "Developers ki"; ≈67.0 s the eye key appears on "data read"; ≈68.0 s the pencil key appears on "and modify permissions kavali".
Overlay (post): "DEVELOPERS: READ AND MODIFY" from ≈66.0 s.

**Shot 7d (69.07–72.05 s) – reporting team: only SELECT:**
"Same style and palette. A second group of Coral avatars with a chart glyph (reporting team) stands beside the table. Only one Teal key (the eye, read) appears for them, and the pencil key stays dimmed and out of reach. No readable text, no logos."
Motion: 69.24–70.4 s the reporting avatars appear on "Reporting team ki"; ≈70.6–71.87 s the single eye key glows on "only SELECT permission kavali".
Overlay (post): "REPORTING TEAM: ONLY SELECT" from 69.24 s.

**Shot 7e (72.05–75.79 s) – create a reporting role and grant SELECT:**
"Same style and palette. A new empty Gold glass badge appears, then the eye-shaped Teal key clicks into it. The badge glows. The avatars of the reporting team wait nearby. Calm, satisfying. No readable text, no logos."
Motion: 72.22–73.6 s the Gold badge appears on "Ippudu reporting role create chesi" (reporting role ≈72.9 s); ≈74.0–75.6 s the key clicks into the badge on "SELECT permission grant cheyyachu" (SELECT ≈74.0 s, grant ≈75.0 s). **Effect: Rack focus** — focus pulls from the avatars to the badge at ≈72.9 s.
Overlay (post): "CREATE A REPORTING ROLE" from ≈72.9 s; "GRANT SELECT" at ≈74.0 s.

**Shot 7f (75.79–80.19 s) – SQL: CREATE ROLE:**
"Same style and palette. A dark glass code editor panel (a clean window with a blinking cursor, no readable code) floats at the centre with a thin Silver edge. Behind it, softly out of focus, the layout glows. Slow push-in. Keep the panel clean so crisp code can be overlaid in post. No readable code, no logos, no watermark."
Motion: 75.97–77.20 s the panel slides in on "SQL commands chuddam!"; 77.64–79.99 s statement 1 types on "CREATE ROLE REPORTING_ROLE;" and a Gold badge glows beside the line. **Effect: Code body.**
Overlay (post, monospace):
```sql
CREATE ROLE REPORTING_ROLE;
```
Appears at 77.64 s; "REPORTING_ROLE" at ≈78.7 s.

**Shot 7g (80.19–85.63 s) – SQL: GRANT USAGE ON DATABASE:**
"Same style and palette. The code panel continues. A Teal key (usage) clicks into the Gold badge and a thin light line connects the badge to the BANK_DB cylinder. No readable code, no logos, no watermark."
Motion: 80.39–83.2 s statement 2 types on "GRANT USAGE ON DATABASE BANK_DB"; ≈83.4–85.46 s the key clicks into the badge on "TO ROLE REPORTING_ROLE". **Effect: Code body.**
Overlay (post, monospace; append under the previous line):
```sql
GRANT USAGE ON DATABASE BANK_DB
TO ROLE REPORTING_ROLE;
```
Appears at 80.39 s; the second line at ≈83.4 s.

**Shot 7h (85.63–92.76 s) – SQL: GRANT USAGE ON SCHEMA:**
"Same style and palette. The code panel continues. A second Teal key (usage) clicks into the Gold badge and a thin light line connects the badge to the schema folder inside the cylinder. No readable code, no logos, no watermark."
Motion: 85.80–90.2 s statement 3 types on "GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA"; ≈90.3–92.59 s the key clicks in on "TO ROLE REPORTING_ROLE". **Effect: Code body.**
Overlay (post, monospace; append):
```sql
GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA
TO ROLE REPORTING_ROLE;
```
Appears at 85.80 s; the second line at ≈90.3 s.

**Shot 7i (92.76–100.60 s) – SQL: GRANT SELECT ON TABLE:**
"Same style and palette. The code panel continues. The eye-shaped Teal key (read) clicks into the Gold badge and a thin light line connects the badge to the CUSTOMER table block, which glows softly for reading. The pencil key stays dimmed. No readable code, no logos, no watermark."
Motion: 92.92–98.0 s statement 4 types on "GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER"; ≈98.1–100.42 s the key clicks in and the table glows on "TO ROLE REPORTING_ROLE". **Effect: Code body.**
Overlay (post, monospace; append):
```sql
GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER
TO ROLE REPORTING_ROLE;
```
Appears at 92.92 s; the second line at ≈98.1 s.

**Shot 7j (100.60–104.18 s) – SQL: GRANT ROLE to a user:**
"Same style and palette. The code panel finishes. The Gold badge, now holding its three keys, slides along a light line to a single Coral avatar on the right (the user DEVA). The avatar glows softly. No readable code, no logos, no watermark."
Motion: 100.77–102.6 s statement 5 types on "GRANT ROLE REPORTING_ROLE"; ≈102.7–103.97 s the badge slides to the avatar on "TO USER DEVA". **Effect: Code body.**
Overlay (post, monospace; the whole script shown together at the end):
```sql
CREATE ROLE REPORTING_ROLE;

GRANT USAGE ON DATABASE BANK_DB
TO ROLE REPORTING_ROLE;

GRANT USAGE ON SCHEMA BANK_DB.CUSTOMER_SCHEMA
TO ROLE REPORTING_ROLE;

GRANT SELECT ON TABLE BANK_DB.CUSTOMER_SCHEMA.CUSTOMER
TO ROLE REPORTING_ROLE;

GRANT ROLE REPORTING_ROLE TO USER DEVA;
```
The last statement appears at 100.77 s; "DEVA" at ≈102.9 s.

**Audio sync:** every statement starts at its pause end (77.64, 80.39, 85.80, 92.92, 100.77 s). Times marked ≈ should be checked by ear.
**Negative prompt (all shots):** "Real bank logos, readable personal data, readable fake text in the generated video, wrong syntax, extra statements, a key attached directly to a user, clutter, flicker, off-palette colours, malformed text, watermark."

---

### Scene 8 – Simple recap (104.18–118.89 s · 14.71 s)
**Voice-over:** "So, simple ga gurthupettukondi! User – Who accesses Snowflake. Role – Group of permissions. Privileges – What actions users can perform. RBAC helps organizations manage secure and controlled data access."
**Tone:** confident.
**Visual objective:** Three-card recap and the benefit.
Generate as **five shots (8a–8e)**.

**Shot 8a (104.18–106.36 s) – keep it simple:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, text #FAF8FF. The Teal key, Gold badge and Coral avatar glide into a neat row at the centre with a soft bloom. Slow push-in, clean space for a title. No readable text, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "KEEP IT SIMPLE" from ≈104.6 s.

**Shot 8b (106.36–108.83 s) – User:**
"Same style and palette. The Coral avatar fills the frame in front of a snowflake door. Clean and calm. No readable text, no logos."
Overlay (post): "USER" at 106.53 s; "Who accesses Snowflake" from 107.29 s. **Effect: Liquid glass** — labels sit on a glass panel.

**Shot 8c (108.83–110.95 s) – Role:**
"Same style and palette. The Gold badge fills the frame with a small group of Teal keys inside. Clean and calm. No readable text, no logos."
Overlay (post): "ROLE" at 109.00 s; "Group of permissions" from 109.64 s.

**Shot 8d (110.95–114.04 s) – Privileges:**
"Same style and palette. The Teal keys fill the frame in a neat row: eye, plus, pencil, crossed bin. Clean and calm. No readable text, no logos."
Overlay (post): "PRIVILEGES" at 111.14 s; "What actions users can perform" from 111.97 s.

**Shot 8e (114.04–118.89 s) – secure and controlled access:**
"Same style and palette. The full chain Teal key → Gold badge → Coral avatar glows in one calm line in front of the Silver vault, and a soft Silver shield settles over it. Satisfying, confident. No readable text, no logos."
Motion: 114.24–116.6 s the chain lights on "RBAC helps organizations manage"; ≈116.6–118.0 s the shield settles on "secure and controlled"; ≈118.0–118.70 s a soft bloom on "data access".
Overlay (post): "RBAC" at 114.24 s; "SECURE AND CONTROLLED DATA ACCESS" from ≈116.6 s.

**Audio sync:** card 1 at 106.53 s; card 2 at 109.00 s; card 3 at 111.14 s; shield at ≈116.6 s.
**Negative prompt:** "Technical claims beyond the script, readable fine text, numbers, clutter, flicker, off-palette colours, watermark."

---

### Scene 9 – Series card and teaser (118.89–128.83 s · 9.94 s)
**Voice-over:** "Idi mana Thirty Days of Snowflake series lo Day Twenty! Next video lo Resource Monitors and Warehouse Cost Optimization gurinchi real-time examples tho explain chesthanu."
**Tone:** upbeat.
**Visual objective:** Mark Day 20 and tease the next topic.
Generate as **two shots (9a, 9b)**.

**Shot 9a (118.89–122.21 s) – Day 20 card:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, text #FAF8FF. A glowing glass snowflake emblem rotates slowly above a progress-style row of thirty small nodes with the first twenty lit in Gold (abstract, no readable text). Soft light bloom, clean space for a title. No logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "THIRTY DAYS OF SNOWFLAKE · DAY 20" from ≈119.8 s; the twentieth node lights at ≈121.6 s on "Twenty".

**Shot 9b (122.21–128.83 s) – teaser: cost control:**
"Same style and palette. A teaser panel slides in with a glass warehouse block, a glowing meter-arc with a small Gold marker (no numbers) and a soft coin-stack glyph beneath it. Clean, minimal, phone-readable. No readable fine text, no logos, no watermark."
Overlay (post): "NEXT: RESOURCE MONITORS" from ≈123.5 s; "WAREHOUSE COST OPTIMIZATION" from ≈125.0 s; "REAL-TIME EXAMPLES" from ≈127.0 s. The visual only suggests a meter and cost. Do not show real credit numbers, limits or behaviour.

**Audio sync:** card at ≈119.8 s; the twentieth node at ≈121.6 s; the teaser title at ≈123.5 s.
**Negative prompt:** "Credit numbers or limits, technical claims, readable text, distorted logo, flicker, off-palette colours, watermark."

---

### Scene 10 – Follow, contact and end card (128.83–140.59 s · 11.76 s)
**Voice-over:** "Ilanti Data Engineering concepts Telugu lo nerchukovadaniki Instagram lo NDR EdTech ni Follow avvandi! Full course details kosam NDR EdTech ni Contact avvandi! Let's Learn and Grow Together!"
**Tone:** upbeat, inviting.
**Visual objective:** One clear Follow CTA, one Contact CTA, and a closing end card.
Generate as **three shots (10a–10c)**.

**Shot 10a (128.83–134.98 s) – Follow:**
"Create a premium vertical 9:16 motion-graphics shot for NDR EdTech. Palette: background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, text #FAF8FF. A calm, clean background with a soft indigo glow, a small Teal key, Gold badge and Coral avatar drifting slowly in the distance, and generous empty space for a call-to-action card in the upper half. Slow light drift. No text rendered, no logos, no watermark. 30 FPS, 4K vertical master."
Overlay (post): "DATA ENGINEERING IN TELUGU" at ≈130.4 s; "FOLLOW @NDREDTECH ON INSTAGRAM" from ≈131.8 s, emphasised at ≈133.8 s on "Follow" (estimated).

**Shot 10b (134.98–138.49 s) – Contact:**
"Same style and palette. A calm, clean background with a soft Gold and Teal glow and space for a contact call-to-action card. Slow light drift. No text rendered, no logos, no watermark."
Overlay (post): "CONTACT NDR EDTECH FOR FULL COURSE DETAILS" from 135.15 s, emphasised at ≈137.3 s on "Contact" (estimated). **Effect: Liquid glass** — the card is a translucent glass panel.

**Shot 10c (138.49–140.59 s) – End card:**
"Same style and palette. A clean, calm end-card background with a soft glow, a reserved clean area at the top for the logo, and generous empty space below for the tagline. Very slow light drift. No text rendered, no logos, no watermark."
Overlay (post): exact NDR EdTech logo and "Let's Learn and Grow Together!" from 138.64 s. Hold the final frame for the last 0.35 s.

Contact details (phone, email, website) are not in the script, so they are omitted. Add them to a split end card only if you want them.

**Negative prompt (all shots):** "Fake social handles, invented phone numbers or URLs, distorted logo, cramming contact details, flicker, off-palette colours, watermark."

---

## 4. Global consistency prompt (paste into the tool's style / project instructions)

"NDR EdTech – Thirty Days of Snowflake, Day 20. Vertical 9:16, 30 FPS, 4K vertical master (fall back to 1080×1920 if unsupported). Premium SaaS / technology-commercial motion graphics with polished 3D-inspired glass materials, soft volumetric rim lighting, subtle floating particles, smooth purposeful camera moves (push-in, parallax, pull-back). Palette only: background #1B1530, User Coral #FF6F91, Role Gold #FFCB47, Privilege Teal #22D3C5, Silver Glass #E6EAF5, text #FAF8FF, secondary text #A9A3C4. Colour code: a user = a Coral glass avatar dot (a round head-and-shoulders glyph, no face); a role = a Gold glass badge; a privilege = a Teal glass key; database, schema and table = Silver Glass. The access chain is always Teal key → Gold badge → Coral user: privileges are granted to roles and roles are assigned to users; a Teal key is never attached directly to a Coral user in a final state. Never show human faces, real names (except DEVA, REPORTING_ROLE, BANK_DB from the script), or any numbers beyond the script. Clean uncluttered compositions with generous empty space for overlays. Keep critical content inside the vertical safe zone. No rendered body text, code, logos, phone numbers or watermarks. No cartoon style, no stock footage, no off-palette colours."

---

## 5. Audio analysis (Whisper, Windows)

Timings were produced with the same workflow as Day 9–19: faster-whisper (`small`, `language="en"`, `word_timestamps=True`, `beam_size=1`, `condition_on_previous_text=False`, `temperature=0.0`) plus `ffmpeg -af "silencedetect=noise=-26dB:d=0.2"`. Phrase starts use the end of each pause. See the Day 9 file for the full commands.

## 6. Editing and synchronisation plan

1. Import `day20.mp3` (140.59 s) as the master audio track at 100% and do not alter it.
2. Place the generated clips on the timeline using the scene and shot times in sections 2 and 3. Cut inside the pauses.
3. Where a shot is shorter than the AI clip, trim it. Where it is longer, slow the last second slightly or hold the final frame, but never cut or shift the narration.
4. Add crisp text and code overlays in the editor (titles, badges, "100 EMPLOYEES", the five SQL statements, and the CTA lines) at the times given in each scene. Do not rely on the AI tool for exact text or code.
5. Add the exact NDR EdTech logo in the reserved area, unaltered.
6. **Set the music and sound-effect tracks to 50% volume; keep the voice-over at 100%.** Place sound effects (a key click, a badge hand-over chime, a soft lock tone) in the pauses or between phrases, not on top of key words. Check by ear that the narration stays clearly louder.
7. Check sync at the start, at the 100 employees (≈5.0 s), at "Definitely not" (14.76 s), at the title (24.60 s), at each numbered badge (38.41, 43.46, 48.91 s), at the chain (55.05 s), at each SQL statement start (77.64, 80.39, 85.80, 92.92, 100.77 s), at the recap cards (106.53, 109.00, 111.14 s), at the final tagline (138.64 s), and at the Follow and Contact lines (≈133.8, ≈137.3 s). Check readability on a phone.
8. Export.

## 7. Export settings
- 9:16 vertical, 2160 × 3840 at 30 FPS if supported (otherwise 1080 × 1920 at 30 FPS).
- H.264 MP4, high bitrate (for example 35–50 Mbps for 4K, 12–16 Mbps for 1080p).
- AAC audio, 48 kHz.
- Instagram and YouTube may recompress the upload.

## Assumptions and notes
- Audio duration and pauses are measured. Times marked ≈ are estimates inside continuous speech.
- Technical content is kept to what the script says: RBAC means managing access through roles instead of assigning permissions directly to users; a user is an individual who accesses a Snowflake account; a role groups permissions and is assigned to users; privileges are permissions such as SELECT, INSERT, UPDATE and DELETE; privileges are granted to roles and roles are assigned to users. In the banking example, a REPORTING_ROLE is created, given USAGE on the database and schema and SELECT on the CUSTOMER table, and granted to user DEVA. **No other roles, privileges or role hierarchies** are shown. The SQL statements from the script are valid Snowflake syntax.
- No contact details, URLs or handles were invented. `@NDREDTECH` is the only handle used, from the skill's known brand details.
- Tool not specified. Prompts are written in Google Flow / Veo style (short shots, one action each). Tell me if you use Runway or Kling and I'll adapt them.
