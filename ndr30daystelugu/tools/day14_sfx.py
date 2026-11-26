import numpy as np, wave, sys, os
SR = 48000
DUR = 153.6
rng = np.random.default_rng(14)
N = int(SR * DUR)
sfx = np.zeros((N, 2), dtype=np.float32)

GM = 0.55
def put(t, sig, gain=1.0, pan=0.0):
    gain = gain * GM
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


# ---------------- Day 14 events (soft) ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
def typing(t0, t1, n, gain=.15):
    for i in range(n): E(t0 + (t1 - t0) * i / max(n, 1), 'key', gain, (i % 5 - 2) * .1)
for t in [3.66, 20.96, 23.81, 36.96, 44.0, 46.12, 63.56, 74.11, 83.45, 115.17, 131.74, 139.94]:
    E(t - 0.3, 'whoosh', 0.6, 0.3)
E(0.0, 'riser', 2.0, .2); E(.3, 'pop', 600, .3)
for i in range(14): E(1.11 + i * .16, 'tick', .16, (i % 5 - 2) * .25, 1800 + 90 * i)
E(3.89, 'pop', 560, .32); E(5.5, 'ding', 880, .25)
for t in [6.93, 8.3, 9.6]: E(t, 'pop', 540, .3)
E(10.9, 'shimmer', .25)
for t, f in [(13.8, 660), (15.7, 740), (17.4, 820)]: E(t, 'pop', f, .35); E(t + .04, 'ding', f * 1.5, .22)
E(19.05, 'chime', .4); E(19.1, 'sparkle', 1.0, .22)
E(21.18, 'whoosh', .8, .22, True); E(22.44, 'pop', 520, .35); E(22.5, 'shimmer', .25)
E(24.02, 'swell', 1.2, .22); E(24.7, 'thud', .3); E(27.3, 'pop', 600, .3); E(28.1, 'ding', 988, .28)
for i in range(3): E(29.5 + i * .4, 'tick', .2, 0, 2200)
for i in range(12): E(31.9 + i * .11, 'tick', .18, 0, 1400 + 120 * i)
E(33.56, 'pop', 540, .3); E(34.2, 'ding', 1174, .28)
E(37.61, 'shimmer', .25); E(38.4, 'whoosh', 1.6, .25, True); E(40.39, 'impact', .35); E(41.7, 'whoosh', .8, .25, True); E(41.75, 'impact', .3); E(43.01, 'chime', .38); E(43.05, 'sparkle', .8, .2)
E(44.21, 'chime', .4); E(44.3, 'shimmer', .25)
E(46.39, 'pop', 540, .3); E(48.0, 'whoosh', .9, .25, True)
for i in range(10): E(48.3 + i * .22, 'tick', .16, (i % 5 - 2) * .2, 1500 + 100 * i)
E(51.92, 'pop', 600, .3); E(52.4, 'impact', .35); E(52.42, 'ding', 880, .25)
for i in range(8): E(54.24 + i * .27, 'tick', .14, (i - 3.5) * .15, 1900)
E(56.4, 'whoosh', .8, .25, False); E(58.43, 'ding', 784, .25); E(59.52, 'pop', 620, .3); E(60.36, 'pop', 700, .3)
E(61.26, 'pop', 680, .3)
for i in range(3): E(61.3 + i * .2, 'tick', .18, 0, 2400)
E(63.78, 'pop', 560, .3); E(64.5, 'ding', 988, .28); E(65.6, 'whoosh', 1.2, .22, True)
for i in range(8): E(67.0 + i * .2, 'tick', .15, 0, 2000)
for i in range(8): E(69.0 + i * .13, 'tick', .15, 0, 1300 - 60 * i)
E(70.8, 'chime', .38); E(70.85, 'shimmer', .25); E(71.96, 'whoosh', .6, .22, True); E(72.44, 'impact', .4)
E(74.34, 'swell', 1.6, .25); E(75.18, 'pop', 520, .3); E(76.73, 'shimmer', .25); E(79.3, 'whoosh', 1.2, .22, True)
for i in range(10): E(79.4 + i * .12, 'tick', .14, (i - 4.5) * .15, 1600 + 90 * i)
E(80.08, 'chime', .4); E(81.9, 'ding', 1046, .28)
E(83.8, 'pop', 540, .3); E(85.8, 'pop', 520, .3); E(86.4, 'ding', 784, .25); E(87.0, 'pop', 600, .3)
E(89.28, 'whoosh', 1.0, .25, True)
for i in range(10): E(89.4 + i * .1, 'tick', .15, 0, 1500 + 100 * i)
E(89.8, 'pop', 600, .3); E(91.5, 'whoosh', .9, .22, True); E(93.06, 'pop', 560, .3)
typing(94.67, 96.63, 26); typing(96.86, 100.98, 38)
E(101.42, 'ding', 784, .25)
for i in range(8): E(101.5 + i * .16, 'tick', .14, 0, 2000)
for i, t in enumerate([103.4, 103.65, 103.9]): E(t, 'ding', 988 + 100 * i, .28)
for i in range(5): E(105.2 + i * .28, 'pop', 560, .18)
for i in range(8): E(107.08 + i * .1, 'tick', .14, 0, 1200 - 50 * i)
E(108.6, 'whoosh', .9, .22, False); E(109.87, 'shimmer', .25); E(112.4, 'whoosh', .8, .22, False); E(113.3, 'ding', 1046, .28); E(114.9, 'chime', .38)
E(116.0, 'pop', 580, .3); E(116.3, 'ding', 880, .25)
for t in [117.64, 121.96, 126.01]: E(t, 'pop', 580, .32); E(t + .05, 'ding', 1046, .22)
for t in [118.97, 123.2, 127.47]: E(t, 'tick', .22, 0, 2000)
E(131.9, 'swell', 1.2, .28); E(132.2, 'sparkle', 1.0, .22)
for i in range(14): E(132.6 + i * .15, 'tick', .14, (i % 5 - 2) * .2, 2000 + 80 * i)
E(133.9, 'pop', 620, .32); E(134.5, 'chime', .42); E(134.52, 'impact', .25)
E(135.6, 'pop', 540, .3)
for i in range(4): E(136.4 + i * .3, 'pop', 560 + 50 * i, .25)
E(137.8, 'pop', 660, .32)
E(140.2, 'impact', .3); E(140.22, 'shimmer', .25)
for t in [140.76, 142.1, 142.8, 143.7, 144.3, 145.7]: E(t, 'pop', 600, .3)
E(145.75, 'ding', 1174, .25); E(146.94, 'pop', 600, .3)
for t in [147.3, 148.0, 148.7]: E(t, 'pop', 560, .32); E(t + .05, 'ding', 1046, .2)
E(150.81, 'swell', 1.4, .3); E(150.95, 'chime', .42); E(151.05, 'shimmer', .25); E(151.5, 'pop', 620, .3)

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
