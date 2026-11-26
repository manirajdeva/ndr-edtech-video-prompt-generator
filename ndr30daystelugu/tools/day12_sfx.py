import numpy as np, wave, sys, os
SR = 48000
DUR = 113.7
rng = np.random.default_rng(12)
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


# ---------------- Day 12 events ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
def typing(t0, t1, n, gain=.2):
    for i in range(n): E(t0 + (t1 - t0) * i / max(n, 1), 'key', gain, (i % 5 - 2) * .1)
for t in [3.35, 13.71, 22.14, 25.02, 27.15, 35.01, 52.27, 69.39, 75.60, 83.90, 93.28, 101.39]:
    E(t - 0.3, 'whoosh', 0.7, 0.35)
E(0.0, 'riser', 2.4, .28); E(0.1, 'pop', 700, .35)
for i in range(10): E(0.3 + i * .1, 'tick', .18, (i % 5 - 2) * .3, 2000 + 120 * i)
E(1.2, 'pop', 600, .4); E(1.35, 'ding', 988, .3); E(1.7, 'pop', 700, .35)
E(2.7, 'impact', .55); E(2.72, 'sparkle', .8, .25); E(2.75, 'chime', .35)
E(3.53, 'pop', 520, .38); E(4.2, 'ding', 880, .35); E(4.25, 'shimmer', .2)
E(5.79, 'pop', 560, .35)
for i in range(14): E(7.6 + i * .17, 'key', .22, (i % 5 - 2) * .1)
E(9.9, 'warn', .15)
E(10.56, 'whoosh', .9, .3, True); E(12.0, 'impact', .35); E(12.02, 'chime', .4); E(12.05, 'sparkle', .8, .22)
E(14.3, 'shimmer', .3); E(14.32, 'pop', 600, .38); E(15.4, 'whoosh', .8, .25, True)
E(16.76, 'riser', 1.8, .25); E(17.9, 'pop', 540, .3)
E(19.4, 'pop', 600, .38); E(19.45, 'ding', 784, .25)
E(20.8, 'impact', .55); E(20.82, 'chime', .45); E(20.85, 'sparkle', .9, .25); E(21.2, 'shimmer', .25)
E(22.45, 'impact', .5); E(23.0, 'impact', .5); E(22.7, 'sparkle', 1.0, .3); E(24.1, 'pop', 700, .4); E(24.15, 'ding', 1174, .3)
E(25.25, 'chime', .45); E(25.3, 'shimmer', .3)
E(27.33, 'swell', 1.6, .3); E(30.2, 'pop', 520, .4); E(31.2, 'pop', 580, .4); E(31.9, 'pop', 650, .4)
E(32.68, 'impact', .45); E(32.7, 'sparkle', .8, .25); E(32.8, 'chime', .35)
E(35.21, 'pop', 540, .35); E(36.0, 'whoosh', .8, .22, True); E(37.0, 'whoosh', .6, .22, False); E(37.8, 'ding', 880, .3)
E(38.55, 'pop', 600, .38)
for i in range(6): E(39.4 + i * .27, 'tick', .22, (i - 2.5) * .2, 1800 + 140 * i)
E(41.8, 'chime', .4); E(41.85, 'shimmer', .25)
E(43.3, 'pop', 640, .35); E(43.9, 'pop', 700, .3)
E(45.5, 'pop', 700, .4); E(45.95, 'pop', 760, .4); E(46.0, 'ding', 1318, .3); E(46.05, 'sparkle', .8, .25)
E(47.83, 'chime', .35); E(49.7, 'impact', .5); E(49.7, 'whoosh', .7, .35, True); E(50.5, 'ding', 1046, .35); E(50.55, 'shimmer', .25)
E(52.6, 'pop', 540, .38); E(54.86, 'pop', 520, .38); E(55.4, 'shimmer', .2); E(56.3, 'ding', 784, .4)
E(58.24, 'pop', 620, .35); E(58.3, 'pop', 700, .35)
for i in range(6): E(60.0 + i * .2, 'tick', .2, 0, 1700 + 100 * i)
for i in range(5): E(61.4 + i * .2, 'tick', .2, 0, 2000 + 100 * i)
E(63.02, 'riser', 1.7, .22); E(64.8, 'impact', .45); E(64.82, 'whoosh', .6, .4, False); E(65.3, 'warn', .2)
E(66.0, 'pop', 600, .38)
for i in range(6): E(66.0 + i * .22, 'tick', .22, (i - 2.5) * .2, 1700 + 100 * i)
E(67.6, 'pop', 680, .4); E(67.65, 'ding', 1046, .3); E(68.4, 'chime', .4)
E(69.56, 'pop', 560, .35); typing(71.06, 73.5, 25); typing(73.8, 75.3, 16); E(73.8, 'ding', 880, .25)
E(75.81, 'impact', .5); E(75.83, 'chime', .45); E(75.85, 'sparkle', 1.0, .3); E(77.7, 'ding', 1174, .35); E(77.72, 'shimmer', .3)
E(79.19, 'pop', 600, .35); E(80.0, 'pop', 640, .35); E(80.4, 'pop', 720, .4); E(80.45, 'ding', 1318, .3)
E(81.5, 'whoosh', .8, .3, True); E(83.0, 'chime', .4); E(83.02, 'shimmer', .3)
E(84.2, 'pop', 580, .38); E(84.45, 'ding', 880, .3)
E(86.23, 'swell', 1.4, .3); E(88.14, 'pop', 600, .4); E(88.16, 'ding', 1046, .3); E(88.88, 'pop', 640, .4); E(88.9, 'ding', 1174, .3); E(90.16, 'pop', 680, .4); E(90.2, 'ding', 1318, .3)
E(93.4, 'swell', 1.2, .35); E(93.6, 'sparkle', 1.0, .3)
for i in range(12): E(94.0 + i * .15, 'tick', .18, (i % 5 - 2) * .2, 2000 + 90 * i)
E(95.3, 'pop', 620, .4); E(95.86, 'chime', .5); E(95.88, 'impact', .35)
E(96.67, 'whoosh', .7, .25, True); E(97.0, 'pop', 560, .35); E(97.8, 'pop', 620, .38); E(98.3, 'chime', .4); E(98.32, 'shimmer', .3); E(99.4, 'pop', 680, .38)
E(101.6, 'impact', .4); E(101.62, 'shimmer', .3)
for t in [102.1, 103.3, 103.8, 104.3, 104.9, 106.2]: E(t, 'pop', 600, .38)
E(106.25, 'ding', 1174, .3); E(107.56, 'pop', 600, .38)
for t in [107.9, 108.6, 109.3]: E(t, 'pop', 560, .4); E(t + .05, 'ding', 1046, .25)
E(110.74, 'swell', 1.4, .4); E(110.89, 'chime', .5); E(110.95, 'shimmer', .3); E(111.45, 'pop', 620, .38)

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
light = np.ones(N, dtype=np.float32); li = 0; ramp = 1
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
