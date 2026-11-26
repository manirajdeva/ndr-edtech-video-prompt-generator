import numpy as np, wave, sys, os
SR = 48000
DUR = 99.4
rng = np.random.default_rng(10)
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


# ---------------- Day 10 events ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
for t in [3.59, 9.97, 16.99, 21.45, 24.62, 33.18, 43.5, 51.53, 65.93, 79.86, 87.59]:
    E(t - 0.3, 'whoosh', 0.7, 0.35)
def reveal(t, base):
    E(t, 'impact', .35); E(t + .02, 'ding', base, .3); E(t + .4, 'shimmer', .15)
E(0.0, 'riser', 2.5, 0.28); E(0.1, 'pop', 700, .35)
for i in range(16): E(0.3 + i * .1, 'tick', .18, (i % 5 - 2) * .3, 2000 + 120 * i)
E(0.9, 'ding', 1046, .3); E(1.3, 'pop', 520, .4); E(2.1, 'shimmer', .3); E(2.88, 'impact', .5); E(2.9, 'sparkle', .8, .2)
E(3.94, 'pop', 480, .4); E(4.12, 'pop', 540, .35); E(4.3, 'pop', 600, .35); E(4.4, 'whoosh', .7, .3, True)
E(6.35, 'thud', .5); E(6.4, 'lock', .4); E(6.5, 'chime', .3); E(6.95, 'pop', 620, .4); E(7.0, 'ding', 880, .25); E(7.7, 'shimmer', .2)
E(8.8, 'sparkle', 1.0, .28); E(8.85, 'whoosh', .9, .3, False); E(9.3, 'ding', 523, .2)
E(10.36, 'impact', .5); E(10.38, 'ding', 1318, .3); E(11.64, 'sparkle', 1.0, .22); E(11.7, 'pop', 620, .35)
for i, t in enumerate([12.3, 12.88, 13.36]): E(t, 'pop', 560 + 80 * i, .4, (i - 1) * .3); E(t + .05, 'ding', 784 * (1.19 ** i), .22)
for i in range(10): E(14.9 + i * .08, 'tick', .2, 0, 1500 + 120 * i)
E(15.8, 'pop', 480, .4); E(15.85, 'ding', 1174, .3)
E(17.2, 'pop', 560, .35); E(18.2, 'thud', .4); E(18.22, 'ding', 1046, .3)
for i in range(9): E(17.7 + i * .12, 'tick', .15, (i % 3 - 1) * .3, 2200)
E(19.58, 'chime', .4); E(20.16, 'pop', 600, .35)
E(21.64, 'sparkle', 1.0, .2)
for i, t in enumerate([22.82, 23.36, 23.92]): E(t, 'pop', 520 + 80 * i, .45, (i - 1) * .3); E(t + .05, 'ding', 784 * (1.19 ** i), .25)
reveal(24.8, 880); E(25.36, 'pop', 620, .4); E(26.62, 'pop', 520, .3)
E(27.5, 'thud', .4); E(27.55, 'whoosh', .6, .25, True)
for i in range(9): E(28.24 + i * .14, 'tick', .22, .2, 1800 + 100 * i)
E(30.6, 'pop', 700, .4); E(30.62, 'shimmer', .25); E(31.72, 'lock', .45); E(31.8, 'chime', .35); E(32.24, 'swell', 1.2, .35)
reveal(33.39, 988); E(33.88, 'pop', 640, .4)
for i in range(14): E(35.07 + i * .25, 'tick', .14, (i % 5 - 2) * .3, 2000 + 90 * (i % 5))
E(36.74, 'sparkle', 1.2, .2); E(40.14, 'pop', 660, .4); E(40.2, 'ding', 1174, .25)
E(41.9, 'warn', .3)
for i in range(5): E(42.4 + i * .12, 'tick', .25, 0, 700)
reveal(43.71, 1046); E(44.24, 'pop', 600, .4); E(45.46, 'pop', 700, .4); E(45.5, 'ding', 932, .25)
E(46.5, 'riser', 1.2, .22); E(47.7, 'ding', 1396, .3)
E(48.02, 'whoosh', .8, .3, False); E(48.8, 'shock', .4)
for i in range(8): E(49.1 + i * .1, 'tick', .25, (i % 3 - 1) * .4, 900 + 150 * i)
E(50.08, 'sparkle', 1.0, .28); E(50.1, 'whoosh', .9, .3, False)
E(51.84, 'pop', 560, .4); E(51.9, 'ding', 784, .25)
E(54.4, 'pop', 540, .35); E(54.5, 'whoosh', .6, .25, True); E(55.88, 'lock', .4); E(55.95, 'ding', 880, .28)
E(57.5, 'pop', 540, .35)
for i in range(14): E(57.6 + i * .2, 'tick', .14, (i % 5 - 2) * .3, 2000 + 90 * (i % 5))
E(60.5, 'lock', .4); E(60.58, 'ding', 988, .28); E(61.9, 'pop', 540, .35)
for i in range(6): E(62.4 + i * .4, 'pop', 700 + 60 * (i % 3), .18, (i % 3 - 1) * .4)
E(64.6, 'lock', .4); E(64.68, 'ding', 1046, .28); E(65.1, 'chime', .45)
E(66.2, 'pop', 560, .35)
for i in range(3): E(66.4 + i * .3, 'pop', 540 + 60 * i, .3, (i - 1) * .3)
for i, t in enumerate([68.15, 70.0, 73.34]): E(t, 'pop', 600 + 70 * i, .4); E(t + .05, 'ding', 784 * (1.19 ** i), .28)
E(72.22, 'warn', .22)
for i in range(4): E(75.4 + i * .6, 'tick', .3, (i % 3 - 1) * .3, 1600)
E(76.96, 'chime', .35); E(77.78, 'chime', .35); E(78.2, 'swell', 1.4, .3)
E(80.0, 'sparkle', 1.0, .25); E(80.4, 'pop', 600, .35)
for i in range(9): E(80.9 + i * .17, 'tick', .22, 0, 2300 + 120 * i)
E(82.4, 'ding', 1318, .4); E(82.4, 'pop', 520, .45); E(82.45, 'shimmer', .25)
E(83.2, 'pop', 600, .35); E(84.5, 'whoosh', 1.1, .35, False)
for i in range(8): E(84.6 + i * .13, 'tick', .18, 0, 1800 - 90 * i)
E(86.2, 'whoosh', 1.0, .3, True); E(86.9, 'ding', 1174, .35); E(86.95, 'shimmer', .2)
E(87.8, 'impact', .5); E(88.0, 'shimmer', .3)
for t in [87.92, 89.3, 90.2, 90.9, 92.4]: E(t, 'pop', 600, .38)
E(93.2, 'whoosh', .5, .25, True)
for t in [93.7, 94.4, 95.0]: E(t, 'pop', 560, .4); E(t + .05, 'ding', 1046, .25)
E(96.5, 'swell', 1.8, .4); E(96.64, 'whoosh', .6, .3); E(97.1, 'chime', .5); E(97.2, 'shimmer', .3)

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
