# NDR EdTech Video Prompt Generator

This Claude Skill turns a voice-over script and/or audio into production-ready AI video prompts, storyboards, audio timing maps, motion-graphics instructions, and export workflows.

## Install
1. Download the ZIP.
2. In Claude, open **Customize** / **Manage** and go to **Skills** (the exact menu wording may vary).
3. Choose **Upload a skill** and upload this ZIP.
4. Enable the skill.
5. Start a new chat and provide your script, voice-over audio, and any visual references.

## Recommended use
For best audio synchronization, upload the actual narration audio as well as the script. The skill instructs Claude to use Whisper or an equivalent timestamped transcription workflow where available. If only a script is provided, timing is an estimate.

**Sound:** the original voice-over stays at 100%, and any background sound effects or music are set to 50% volume.

**Day-wise files:** put the audio in the `Audio` folder as `day12.mp3` and the script in the `days-scripts` folder as `day12.txt`. Then just say "create the video prompt for day 12". The skill picks both files for that day, measures the audio with Whisper, and writes `video_prompt_day12.md` and `.txt`.

After the video prompt is created, the skill makes a folder for that day (for example `D:\ndr edtech\ndr30daystelugu\next days\day11`) and copies the audio, the video prompt files, and the character reference image (only for conversation videos) into it.

If your script has no conversation (a single narrator), the skill works exactly as before, with no cartoon characters.

Write conversations with `she:` and `he:` labels, `[emotion]` tags, and a `-----conversation end ------` line (see `script.txt` for an example). The skill reads `she` as the female cartoon character and `he` as the male one, turns the emotion tags into facial expressions and gestures, and uses the end marker to switch from the characters to the narrated video.

If your video starts with a conversation, the skill finds the male and female voices (from script labels or the audio), maps each turn to a consistent animated male or female character (the default cartoon pair in `character_reference.png`, which you upload to the video tool as the reference image), and writes the conversation shots with speaker timing, gestures, and lip-sync notes.

The skill defaults to vertical 9:16 and 4K when supported, falls back to 1080 × 1920, and selects a fresh colour palette for each new video unless the current brief mandates a specific palette.
