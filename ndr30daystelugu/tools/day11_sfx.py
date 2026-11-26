import numpy as np, wave, sys, os
SR = 48000
DUR = 126.15
rng = np.random.default_rng(11)
N = int(SR * DUR)
sfx = np.zeros((N, 2), dtype=np.float32)

def put(t, sig, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N or i < 0: return
    sig = sig[: N - i]
    l = gain * (1 - max(0, pan)) ; r = gain * (1 + min(0, pan))
    sfx[i:i + len(sig), 0] += sig * l
    sfx[i:i + len(sig), 1] += sig * r

def env(n, a=0.005, d=0.1, curve=4.0):
    t = np.arange(n) / SR
    e = np.exp(-t * curve / max(d, 1e-3))
    att = np.minimum(1, t / a)
    return e * att

def sine(f, dur, f_end=None):
    n = int(dur * SR); t = np.arange(n) / SR
    if f_end is None: ph = 2 * np.pi * f * t
    else: ph = 2 * np.pi * (f * t + (f_end - f) * t * t / (2 * dur))
    return np.sin(ph)

def hp(x, k=0.95):
    y = np.zeros_like(x); p = 0; q = 0
    for i in range(len(x)):
        y[i] = k * (y[i - 1] + x[i] - (x[i - 1] if i else 0))
    return y

def lp_noise(n, cutoff_start, cutoff_end):
    # time-varying one-pole lowpass over white noise
    x = rng.standard_normal(n).astype(np.float32)
    y = np.zeros(n, dtype=np.float32); acc = 0.0
    cs = np.linspace(cutoff_start, cutoff_end, n)
    for i in range(n):
        a = 1 - np.exp(-2 * np.pi * cs[i] / SR)
        acc += a * (x[i] - acc); y[i] = acc
    return y

def pop(t, f=620, gain=0.5, pan=0.0):
    s = sine(f * 1.6, 0.14, f * 0.8) * env(int(.14 * SR), .003, .07, 5)
    b = 0.4 * sine(f * 3.2, 0.06) * env(int(.06 * SR), .002, .03, 5)
    s[:len(b)] += b
    put(t, s.astype(np.float32), gain, pan)

def tick(t, gain=0.25, pan=0.0, f=2400):
    n = int(.012 * SR); x = rng.standard_normal(n) * env(n, .0005, .006, 6)
    x += sine(f, .012)[:n] * env(n, .0005, .006, 6) * 0.8
    put(t, x.astype(np.float32), gain, pan)

def key(t, gain=0.22, pan=0.0):
    n = int(.02 * SR); x = rng.standard_normal(n) * env(n, .0005, .008, 7)
    x += sine(rng.uniform(1500, 2600), .02)[:n] * env(n, .0005, .01, 7) * 0.6
    put(t, (x * 0.8).astype(np.float32), gain, pan)

def ding(t, f=880, gain=0.35, pan=0.0, d=0.9):
    n = int(d * SR)
    s = sine(f, d) + 0.5 * sine(f * 2, d) * 0.6 + 0.25 * sine(f * 3.01, d)
    s *= env(n, .003, d * .45, 5)
    put(t, s.astype(np.float32), gain, pan)

def chime(t, gain=0.35, base=523.25):
    for k, m in enumerate([1, 1.26, 1.5, 2]):
        ding(t + k * 0.09, base * m, gain * (0.8 + 0.1 * k), pan=(k - 1.5) * 0.15, d=1.2)

def whoosh(t, dur=0.8, gain=0.4, up=True, pan=0.0):
    n = int(dur * SR)
    x = lp_noise(n, 300 if up else 3500, 3500 if up else 300)
    e = np.sin(np.linspace(0, np.pi, n)) ** 1.6
    put(t, (x * e * 2.2).astype(np.float32), gain, pan)

def thud(t, gain=0.7):
    n = int(.6 * SR)
    s = sine(95, .6, 40) * env(n, .002, .3, 5)
    s += lp_noise(n, 900, 120) * env(n, .001, .15, 6) * 1.2
    put(t, s.astype(np.float32), gain)

def shock(t, gain=0.4):
    n = int(1.0 * SR)
    s = sine(900, 1.0, 140) * env(n, .003, .5, 4) * 0.5
    s += lp_noise(n, 4000, 300) * env(n, .002, .4, 5) * 0.5
    put(t, s.astype(np.float32), gain)

def warn(t, gain=0.35):
    for k in range(2):
        n = int(.16 * SR)
        s = (np.sign(sine(170, .16)) * 0.35 + sine(170, .16)) * env(n, .004, .09, 4)
        put(t + k * 0.2, s.astype(np.float32), gain)

def sparkle(t, dur=1.2, gain=0.25):
    for k in range(14):
        f = rng.choice([1568, 1976, 2349, 2637, 3136, 3520])
        n = int(.35 * SR); s = sine(f, .35) * env(n, .002, .18, 5)
        put(t + k * dur / 14 + rng.uniform(0, .03), s.astype(np.float32), gain * rng.uniform(.4, 1), rng.uniform(-.7, .7))

def riser(t, dur=2.5, gain=0.3):
    n = int(dur * SR)
    x = lp_noise(n, 200, 6000) * np.linspace(0, 1, n) ** 2
    s = sine(220, dur, 880) * np.linspace(0, 1, n) ** 2 * 0.4
    put(t, ((x * 1.5 + s) * 0.8).astype(np.float32), gain)

def swell(t, dur=1.8, gain=0.35):
    n = int(dur * SR); tt = np.arange(n) / SR
    s = (sine(261.6, dur) + sine(329.6, dur) + sine(392, dur) + 0.5 * sine(523.2, dur)) * (np.linspace(0, 1, n) ** 2)
    put(t, (s * 0.25).astype(np.float32), gain)

def lock(t, gain=0.4):
    tick(t, gain, f=1200); tick(t + .06, gain * .8, f=1800); ding(t + .1, 1320, gain * .6, d=.6)

def shimmer(t, gain=0.25):
    for k, f in enumerate([1760, 2217, 2637, 3322]):
        n = int(.9 * SR); s = sine(f, .9) * env(n, .01, .5, 4)
        put(t + k * .05, s.astype(np.float32), gain, (k - 1.5) * .3)

def impact(t, gain=0.6):
    thud(t, gain); shock(t, gain * .35)


# ---------------- Day 11 events ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
def typing(t0, t1, n, gain=.2):
    for i in range(n): E(t0 + (t1 - t0) * i / max(n, 1), 'key', gain, (i % 5 - 2) * .1)
for t in [39.22, 45.55, 53.40, 61.51, 73.20, 79.51, 87.25, 97.10, 106.65, 114.38]:
    E(t - 0.3, 'whoosh', 0.7, 0.35)
# ---- part 1: conversation (kept light) ----
E(0.0, 'whoosh', .5, .22, False); E(0.5, 'pop', 520, .25)
E(6.9, 'pop', 620, .3); E(8.2, 'pop', 560, .3); E(8.8, 'warn', .3); E(8.85, 'whoosh', .9, .3, False); E(9.1, 'sparkle', .9, .15)
E(9.97, 'impact', .55); E(9.99, 'shock', .3)
E(12.61, 'pop', 480, .3); E(13.49, 'thud', .3); E(13.52, 'warn', .2)
E(17.93, 'tick', .3, 0, 1400); E(18.0, 'tick', .25, 0, 1800); E(19.38, 'pop', 700, .3); E(20.0, 'pop', 520, .22)
E(22.63, 'pop', 760, .3); E(22.66, 'ding', 1318, .22); E(23.7, 'shimmer', .3)
E(27.58, 'chime', .4); E(27.6, 'whoosh', .6, .25, True)
for i in range(8): E(28.6 + i * .15, 'tick', .22, .2, 1800 + 100 * i)
E(30.3, 'whoosh', 1.4, .4, False)
for i in range(10): E(30.4 + i * .12, 'tick', .2, 0, 2400 - 120 * i)
E(31.5, 'shimmer', .3); E(31.52, 'ding', 1046, .3); E(31.9, 'ding', 1318, .25)
E(33.0, 'pop', 600, .25); E(35.2, 'pop', 640, .25)
E(35.6, 'riser', 1.5, .4); E(36.0, 'whoosh', 1.0, .4, True)
E(37.07, 'impact', .6); E(37.1, 'sparkle', 1.0, .3); E(37.26, 'chime', .45); E(37.5, 'shimmer', .3)
# ---- scene 3 ----
E(39.41, 'pop', 560, .38); E(40.6, 'pop', 640, .3); E(41.0, 'whoosh', .9, .3, False); E(41.1, 'shimmer', .2)
E(43.0, 'tick', .3, 0, 1600); E(43.68, 'chime', .4); E(43.7, 'ding', 1046, .3)
# ---- scene 4 ----
E(45.71, 'warn', .3); E(45.9, 'whoosh', .9, .3, False); E(46.5, 'pop', 560, .4); E(46.55, 'ding', 784, .25)
E(48.0, 'whoosh', .9, .3, True); E(48.99, 'chime', .4)
E(49.28, 'pop', 600, .4); E(49.33, 'ding', 880, .25)
for i in range(5): E(50.2 + i * .15, 'tick', .22, 0, 2000 + 120 * i)
E(51.28, 'shock', .3); E(51.3, 'impact', .3); E(51.35, 'pop', 640, .4); E(51.4, 'ding', 988, .25); E(52.2, 'ding', 1174, .3)
# ---- scene 5 ----
E(53.6, 'whoosh', .7, .25, True); E(54.1, 'impact', .4); E(54.12, 'ding', 784, .35); E(55.1, 'impact', .4); E(55.12, 'ding', 988, .35)
E(57.1, 'pop', 560, .38); E(58.1, 'pop', 620, .38); E(58.8, 'pop', 680, .38); E(59.54, 'chime', .4); E(59.6, 'shimmer', .2)
# ---- scene 6 ----
E(61.76, 'pop', 540, .38); E(61.8, 'ding', 880, .25)
for i in range(10): E(63.94 + i * .07, 'tick', .2, (i % 5 - 2) * .2, 1800 + 100 * i)
E(65.3, 'ding', 1046, .3); E(65.32, 'pop', 600, .3)
E(66.56, 'warn', .3); E(67.4, 'warn', .3); E(68.2, 'whoosh', .9, .3, False); E(68.25, 'sparkle', .9, .22)
E(69.12, 'pop', 640, .38); E(69.2, 'shimmer', .2)
for i in range(10): E(70.8 + i * .12, 'tick', .2, 0, 2500 - 120 * i)
E(70.8, 'whoosh', 1.2, .3, False); E(72.2, 'chime', .4); E(72.22, 'shimmer', .3); E(72.5, 'ding', 1046, .3)
# ---- scene 7 ----
E(73.37, 'pop', 560, .35); typing(74.85, 75.6, 8); typing(75.6, 76.7, 13); typing(77.0, 79.0, 21)
E(77.3, 'ding', 1174, .3); E(78.0, 'pop', 680, .3)
# ---- scene 8 ----
E(79.8, 'whoosh', .7, .25, False); E(80.6, 'pop', 600, .35); E(81.5, 'ding', 988, .3); E(82.6, 'shimmer', .3)
E(83.63, 'pop', 560, .35); E(84.86, 'chime', .4); E(85.3, 'pop', 700, .35); E(86.4, 'ding', 1318, .35); E(86.45, 'shimmer', .2)
# ---- scene 9 ----
E(87.4, 'impact', .4); E(87.45, 'ding', 880, .3); E(88.3, 'shimmer', .25)
typing(89.8, 92.2, 33); typing(92.8, 93.3, 8); typing(93.5, 94.0, 13); typing(94.1, 96.6, 21)
E(94.5, 'ding', 1174, .3)
for i in range(10): E(96.0 + i * .09, 'tick', .2, 0, 1800 + 100 * i)
E(96.5, 'chime', .45); E(96.55, 'sparkle', .9, .22)
# ---- scene 10 ----
E(97.1, 'swell', 1.6, .3); E(97.8, 'pop', 600, .38); E(99.23, 'chime', .4)
E(101.2, 'impact', .6); E(101.0, 'whoosh', 1.2, .4, False)
for i in range(10): E(101.3 + i * .1, 'tick', .2, 0, 2400 - 120 * i)
E(102.67, 'warn', .3); E(104.3, 'shimmer', .3); E(105.2, 'swell', 1.4, .35); E(105.3, 'chime', .45)
# ---- scene 11 ----
E(107.1, 'sparkle', 1.0, .3); E(107.0, 'swell', 1.2, .3)
for i in range(12): E(107.3 + i * .15, 'tick', .18, (i % 5 - 2) * .2, 2000 + 90 * i)
E(108.55, 'pop', 620, .4); E(109.08, 'chime', .5); E(109.1, 'impact', .35)
E(110.0, 'whoosh', .6, .25, True); E(110.88, 'pop', 560, .38); E(111.04, 'shimmer', .3); E(111.9, 'ding', 1046, .3); E(112.24, 'pop', 640, .38)
# ---- scene 12 ----
E(114.5, 'impact', .4); E(114.52, 'shimmer', .3)
for t in [115.06, 116.0, 116.6, 117.1, 117.7, 118.9]: E(t, 'pop', 600, .38)
E(118.95, 'ding', 1174, .3)
E(120.07, 'pop', 600, .38)
for t in [120.4, 121.1, 121.8]: E(t, 'pop', 560, .4); E(t + .05, 'ding', 1046, .25)
E(123.05, 'swell', 1.6, .4); E(123.2, 'chime', .5); E(123.3, 'shimmer', .3); E(123.76, 'pop', 620, .38)

fn = dict(pop=pop, tick=tick, key=key, ding=ding, chime=chime, whoosh=whoosh, thud=thud, shock=shock, warn=warn,
          sparkle=sparkle, riser=riser, swell=swell, lock=lock, shimmer=shimmer, impact=impact)
for t, kind, a, k in ev:
    if kind == 'whoosh':
        dur = a[0]; gain = a[1]; up = a[2] if len(a) > 2 else True
        whoosh(t, dur, gain, up)
    elif kind == 'pop': pop(t, *a)
    elif kind == 'tick': tick(t, *a)
    elif kind == 'key': key(t, *a)
    elif kind == 'ding': ding(t, *a)
    elif kind == 'swell': swell(t, a[0], a[1])
    elif kind == 'riser': riser(t, a[0], a[1])
    elif kind == 'sparkle': sparkle(t, *a)
    else: fn[kind](t, *a)

# ---------------- ambient music bed (soft pad + sparse bells) ----------------
mus = np.zeros((N, 2), dtype=np.float32)
chords = [[220.0, 261.63, 329.63], [174.61, 261.63, 349.23], [261.63, 329.63, 392.0], [196.0, 293.66, 392.0]]
bar = 6.0
tt = np.arange(int(bar * SR + SR)) / SR
for b in range(int(DUR / bar) + 1):
    ch = chords[b % 4]
    for fq in ch:
        for det in (-0.8, 0.8):
            s = np.sin(2 * np.pi * (fq + det) * tt) * 0.5 + np.sin(2 * np.pi * (fq * 2 + det) * tt) * 0.12
            e = np.minimum(1, tt / 1.6) * np.minimum(1, (bar + 1 - tt) / 1.6)
            i = int(b * bar * SR); seg = (s * e).astype(np.float32) * 0.09
            L = min(len(seg), N - i)
            if L <= 0: continue
            mus[i:i + L, 0] += seg[:L]; mus[i:i + L, 1] += seg[:L] * (1 if det < 0 else .9)
# bells on pentatonic every 1.5 s, sparse
pent = [523.25, 587.33, 659.25, 783.99, 880.0]
for k in range(int(DUR / 1.5)):
    if rng.random() < .55:
        f = pent[int(rng.integers(0, 5))]; n = int(1.6 * SR); s = (sine(f, 1.6) + .3 * sine(f * 2, 1.6)) * env(n, .004, .6, 5) * 0.05
        i = int(k * 1.5 * SR); L = min(n, N - i)
        pan = rng.uniform(-.6, .6)
        mus[i:i + L, 0] += s[:L] * (1 - max(0, pan)); mus[i:i + L, 1] += s[:L] * (1 + min(0, pan))
fade = np.ones(N, dtype=np.float32); fi = int(1.5 * SR); fade[:fi] = np.linspace(0, 1, fi); fo = int(2.5 * SR); fade[-fo:] = np.linspace(1, 0, fo)
mus *= fade[:, None]
light = np.ones(N, dtype=np.float32); li = int(37.0 * SR); light[:li] = 0.55; ramp = int(1.0 * SR); light[li:li+ramp] = np.linspace(0.55, 1, ramp)
mus *= light[:, None]

def save(name, arr):
    arr = np.clip(arr, -1, 1)
    with wave.open(name, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((arr * 32767).astype(np.int16).tobytes())
peak = np.abs(sfx).max(); print('sfx peak', peak)
if peak > 0.9: sfx *= 0.9 / peak
save(sys.argv[1], sfx); save(sys.argv[2], mus)
print('ok', len(ev), 'events')
