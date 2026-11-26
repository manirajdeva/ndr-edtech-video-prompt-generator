import numpy as np, wave, sys, os
SR = 48000
DUR = 113.6
rng = np.random.default_rng(8)
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

# ---------------- event timeline (matches the animation beats, transcript-timed) ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))

# scene transitions
for t in [3.7, 10.2, 23.5, 30.0, 37.5, 48.8, 60.5, 83.4, 94.0, 97.1, 101.6]:
    E(t - 0.3, 'whoosh', 0.7, 0.35)
# S1
E(0.0, 'riser', 2.5, 0.28); E(0.1, 'pop', 700, .35); E(0.6, 'sparkle', 1.2); E(1.1, 'ding', 1046, .3); E(1.45, 'pop', 520, .4); E(2.5, 'shimmer')
# S2 phone
E(3.9, 'pop', 480, .4)
for i, t in enumerate([4.5, 5.05, 5.6, 6.15]): E(t, 'pop', 560 + 60 * i, .4, (i - 1.5) * .3)
for i in range(12): E(4.1 + i * 0.2, 'tick', .22, (i % 5 - 2) * .25)
E(2.1, 'pop', 600, .3)
E(6.9, 'chime', .3)
E(8.1, 'warn', .3)
for i in range(12): E(8.1 + i * .06, 'tick', .18, (i % 5 - 2) * .25, 1400)
# S3
E(10.5, 'sparkle', 1.2); E(11.0, 'pop', 600, .35); E(12.0, 'pop', 700, .35)
E(13.5, 'pop', 520, .4)
for i in range(40): E(13.7 + i * 0.085, 'tick', .12, (i % 7 - 3) * .2, 1800 + (i % 5) * 250)
E(17.0, 'warn', .4); E(17.05, 'thud', .35)
E(18.3, 'pop', 520, .35)
for i, t in enumerate([19.8, 20.4, 21.2, 21.9]): E(t, 'pop', 480 + 90 * i, .45, (i - 1.5) * .25); E(t + .05, 'ding', 784 * (1.12 ** i), .22)
E(23.3, 'chime', .35)
# S4 database
E(23.7, 'pop', 600, .3); E(24.8, 'impact', .7); E(24.85, 'shimmer', .25)
for i in range(14): E(26.5 + i * .22 + .6, 'pop', 900 + (i % 4) * 120, .2, (i % 5 - 2) * .2)
E(26.45, 'pop', 620, .3); E(28.2, 'pop', 700, .35)
# S5 schema
E(30.2, 'whoosh', .9, .35, True); E(30.3, 'pop', 600, .4); E(31.4, 'ding', 987, .3); E(31.8, 'pop', 620, .3)
for i in range(5): E(34.2 + i * .45 + .5, 'pop', 700 + 70 * i, .4, (i - 2) * .3); E(34.2 + i * .45 + .55, 'ding', 1174, .15)
E(35.2, 'pop', 600, .3)
# S6 tables
E(37.9, 'pop', 600, .4); E(38.3, 'whoosh', .5, .25)
for r in range(5): E(39.5 + r * .5, 'tick', .3, 0, 2000)
E(40.6, 'whoosh', 1.0, .3); E(41.2, 'pop', 700, .3)
E(43.1, 'pop', 600, .4); E(44.0, 'ding', 880, .3); E(46.0, 'pop', 600, .4); E(46.2, 'ding', 988, .3)
for r in range(5): E(43.7 + r * .5, 'tick', .25, -.2, 2200); E(46.7 + r * .5, 'tick', .25, .2, 2200)
# S7 views
E(49.0, 'pop', 560, .4); E(49.1, 'whoosh', 1.2, .35, False)
for i in range(40): E(50.6 + i * 0.085, 'key', .2, (i % 3 - 1) * .2)
E(52.0, 'whoosh', .8, .3); E(52.9, 'sparkle', .8, .18)
E(54.7, 'lock', .4); E(58.0, 'shimmer', .2); E(58.9, 'warn', .22); E(59.0, 'pop', 480, .3)
# S8 banking
E(60.9, 'pop', 560, .35); E(62.9, 'pop', 600, .4); E(63.8, 'ding', 784, .25)
for i in range(7): E(64.1 + i * .08, 'key', .2)
E(65.7, 'whoosh', .7, .3); E(66.5, 'pop', 640, .4)
for i in range(15): E(66.4 + i * .06, 'key', .16)
E(70.2, 'pop', 620, .45, -.3); E(70.7, 'pop', 680, .45, .3)
for i in range(60): E(72.9 + i * .068, 'key', .2, (i % 3 - 1) * .2)
E(76.2, 'whoosh', .6, .3); E(76.8, 'ding', 880, .3)
for i, t in enumerate([78.5, 79.3, 80.0, 80.7]): E(t, 'ding', 659 * (1.125 ** i), .3, (i - 1.5) * .25)
E(81.3, 'chime', .4)
# S9 recap
E(83.6, 'pop', 600, .35)
for i, t in enumerate([84.8, 87.4, 89.5, 91.0]): E(t, 'pop', 500 + 70 * i, .45); E(t + .05, 'ding', 784 * (1.19 ** i), .3)
E(93.3, 'chime', .45)
# S10 series
E(94.1, 'sparkle', 1.0); E(94.3, 'pop', 600, .35)
for i in range(7): E(94.7 + i * .08, 'tick', .25, 0, 2500 + 150 * i)
E(96.1, 'ding', 1318, .35); E(96.0, 'pop', 520, .45); E(96.1, 'shimmer', .25)
# S11 teaser
E(97.5, 'pop', 600, .35); E(98.0, 'pop', 700, .35)
for i, t in enumerate([99.2, 99.7, 100.2, 100.7]): E(t, 'pop', 600 + 50 * i, .4, (i - 1.5) * .3); E(t + .05, 'ding', 880 * (1.12 ** i), .2)
# S12 outro
E(101.8, 'impact', .55); E(102.1, 'shimmer', .3); E(102.6, 'pop', 600, .3)
E(104.3, 'pop', 600, .4); E(104.5, 'pop', 700, .3); E(105.6, 'pop', 520, .4); E(106.5, 'pop', 700, .3)
E(108.0, 'whoosh', .5, .25)
for t in [108.3, 109.1, 109.8]: E(t, 'pop', 560, .4); E(t + .05, 'ding', 1046, .25)
E(110.5, 'swell', 1.8, .4); E(110.7, 'whoosh', .6, .3); E(111.3, 'chime', .5); E(111.4, 'shimmer', .3)

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

def save(name, arr):
    arr = np.clip(arr, -1, 1)
    with wave.open(name, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((arr * 32767).astype(np.int16).tobytes())
peak = np.abs(sfx).max(); print('sfx peak', peak)
if peak > 0.9: sfx *= 0.9 / peak
save(sys.argv[1], sfx); save(sys.argv[2], mus)
print('ok', len(ev), 'events')
