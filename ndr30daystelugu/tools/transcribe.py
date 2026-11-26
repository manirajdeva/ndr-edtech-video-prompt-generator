import sys, json
from faster_whisper import WhisperModel
audio, out, lang = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "en")
import subprocess, numpy as np
raw = subprocess.run(["ffmpeg","-v","error","-i",audio,"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True).stdout
audio_np = np.frombuffer(raw, dtype=np.float32)
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = m.transcribe(audio_np, language=lang, word_timestamps=True, beam_size=5, condition_on_previous_text=False)
res = []
for s in segs:
    res.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                "words": [[round(w.start, 2), round(w.end, 2), w.word.strip()] for w in (s.words or [])]})
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for r in res:
    print(f'{r["start"]:7.2f} {r["end"]:7.2f}  {r["text"]}')
