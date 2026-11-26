THIRTY DAYS OF dbt – ElevenLabs (Eleven v3) text-to-speech scripts
==================================================================

This folder has ONE file for each day: day1.txt to day30.txt.

Every file has the funny conversation first and the narration after it. Each line starts with a speaker label:

  FEMALE:    – the female voice (conversation)
  MALE:      – the male voice (conversation)
  NARRATOR:  – the narrator voice (the rest of the video)

Your original scripts are NOT changed. They stay in the folder dbt_scripts and are still the files to use for video prompts.
The same text, split into two files per day, is kept in the subfolder separate_parts (dayN_conversation.txt and dayN_narration.txt).


HOW TO USE (Eleven v3, Text to Dialogue)
----------------------------------------
1) Open Text to Dialogue and choose the Eleven v3 model.
2) Add one dialogue line per row of the file. Give the FEMALE: lines your female voice, the MALE: lines your male voice and the NARRATOR: lines your narrator voice. Use the same three voices for all 30 days so the characters stay consistent.
3) Paste only the text AFTER the label. Keep the [tag] at the start of a line (for example [curious]). Do not paste "FEMALE:", "MALE:" or "NARRATOR:". Do not add other square brackets.
4) Language: set Telugu if the voice offers it (or leave it on automatic). Stability: try "Natural" first, then "Creative" if you want more emotion.
5) Keep the narration at 100% volume and background sound at 50% in your video editor.

If you prefer plain Text to Speech for the narration, use separate_parts\dayN_narration.txt. It has no labels, so you can paste the whole file.


WHAT WAS CHANGED FOR TEXT-TO-SPEECH
-----------------------------------
- Telugu words are written in Telugu script. Technical English words stay in English letters.
- Section tags such as [Explaining – Main Concept], the line "-----conversation end ------" and the speaker labels she:/he: were removed from the spoken text.
- Emotion cues became Eleven v3 audio tags: [curious], [excited], [confused], [sarcastic], [shocked], [panicked], [tired], [serious], [confident], and [laughs] where the original had a laughing emoji.
- Acronyms are spelled so they are read letter by letter: D B T, S Q L, A W S, S three (S3), C S V, C I, E L T, E T L, N D R, Y M L, and so on. "EdTech" is written "Ed Tech".
- Numbers are written as words (for example "one hundred", "twenty twenty six").
- Code is written the way it would be spoken: underscore, dot, star, equals, open bracket, close bracket, double curly braces, colon, dash dash, slash, backslash.


TIPS
----
- Generate Day 1 first and listen. If a word is pronounced wrongly, change that word in the text (for example spell it differently) and generate again. A native Telugu speaker should listen to each day once.
- The code is read literally, as in your earlier recordings. If a code block sounds too long, delete those lines from the narration file: the video shows the code on screen.
- All files are far below the 5,000 character limit of a single generation.
- Eleven v3 tags work best in short phrases. Do not put a tag in the middle of a code line.
- For video prompts, keep using the original files in dbt_scripts: they have the she:/he: labels and the Latin-script wording that the video prompt skill reads.
