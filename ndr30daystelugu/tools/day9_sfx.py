import numpy as np, wave, sys, os
SR = 48000
DUR = 113.3
rng = np.random.default_rng(9)
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


# ---------------- Day 9 events (transcript-timed) ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
for t in [3.69, 10.0, 18.19, 30.2, 37.07, 44.32, 53.22, 57.70, 63.05, 86.37, 91.24]:
    E(t - 0.3, 'whoosh', 0.7, 0.35)
# S1 question mark assembles
E(0.0, 'riser', 2.5, 0.28); E(0.2, 'pop', 700, .35)
for i in range(16): E(0.35 + i * .11, 'tick', .18, (i % 5 - 2) * .3, 2000 + 120 * i)
E(1.1, 'ding', 1046, .3); E(1.45, 'pop', 520, .4); E(2.54, 'shimmer', .3); E(2.96, 'impact', .5); E(2.9, 'sparkle', .8, .2)
# S2 age
E(3.9, 'pop', 480, .4); E(4.0, 'pop', 600, .3); E(6.9, 'pop', 620, .4); E(7.0, 'ding', 784, .3); E(8.5, 'pop', 700, .4); E(8.6, 'ding', 1046, .3)
E(8.6, 'pop', 900, .35, .3)
for i in range(5): E(8.9 + i * .33, 'pop', 520 + 40 * (i % 2), .25, (-1) ** i * .5)
# S3 wrong fit + tear + glitch
E(10.3, 'pop', 520, .4)
for i in range(9): E(10.6 + i * .22, 'tick', .22, (i % 3 - 1) * .3, 900)
E(11.7, 'pop', 600, .4); E(11.8, 'warn', .35); E(12.78, 'whoosh', .75, .5, False); E(13.0, 'tick', .4, 0, 700)
E(14.23, 'warn', .3)
for i in range(14): E(14.3 + i * .09, 'tick', .2, (i % 5 - 2) * .3, 700 + (i % 4) * 300)
E(16.1, 'pop', 400, .4); E(16.15, 'warn', .35); E(16.5, 'pop', 400, .4); E(17.0, 'chime', .25)
# S4
E(18.5, 'sparkle', 1.2, .22); E(19.9, 'pop', 620, .4); E(20.3, 'pop', 720, .4); E(20.4, 'ding', 1174, .2)
E(23.3, 'chime', .4); E(23.9, 'pop', 600, .35)
for i in range(5): E(26.5 + i * .7, 'pop', 520 + 80 * i, .4, (i - 2) * .25); E(26.55 + i * .7, 'ding', 784 * (1.122 ** i), .2)
# type reveals
def reveal(t, base):
    E(t, 'impact', .35); E(t + .02, 'ding', base, .3); E(t + .4, 'shimmer', .15)
reveal(31.0, 880); E(32.8, 'pop', 620, .4); E(33.5, 'pop', 680, .4); E(34.5, 'pop', 740, .4)
for i in range(6): E(32.0 + i * .7, 'tick', .1, (i % 2 - .5), 2800)
reveal(38.0, 988); E(38.1, 'thud', .45); E(39.1, 'pop', 620, .4); E(40.2, 'pop', 680, .4); E(41.2, 'pop', 740, .4)
for i in range(18): E(39.2 + i * .13, 'key', .13, (i % 3 - 1) * .3)
reveal(45.2, 1174); E(47.4, 'pop', 560, .4); E(47.5, 'whoosh', .8, .25, True)
for i in range(10): E(47.5 + i * .1, 'tick', .18, -.3, 1500 + 100 * i)
E(48.4, 'pop', 640, .4)
for i in range(5): E(48.8 + i * .17, 'tick', .3, .3, 2400)
E(50.3, 'swell', 1.4, .35); E(50.4, 'sparkle', .8, .2)
E(53.46, 'pop', 520, .4); E(54.1, 'ding', 1318, .3); E(54.9, 'thud', .5); E(54.92, 'ding', 1568, .3); E(55.4, 'tick', .5, 0, 800); E(55.42, 'pop', 380, .35)
for i in range(2): E(56.0 + i * .6, 'tick', .25, 0, 1000 + 400 * i)
reveal(58.6, 1397); E(59.5, 'whoosh', .9, .4, True); E(59.6, 'sparkle', 1.2, .25)
for i in range(4): E(59.6 + i * .2, 'pop', 600 + 70 * i, .3, (i - 1.5) * .3)
# S10 banking
E(63.4, 'pop', 580, .4); E(63.5, 'ding', 784, .25)
def col(t0, tc, n, base, nm):
    E(t0, 'pop', 540, .35)
    for i in range(n): E(t0 + .05 + i * .066, 'key', .18, (i % 3 - 1) * .2)
    E(tc, 'lock', .4); E(tc + .1, 'ding', base, .28)
col(65.6, 66.7, 11, 880, 'id'); col(68.0, 69.2, 13, 988, 'name'); col(70.7, 73.6, 8, 784, 'dob')
for i in range(30): E(71.0 + i * .08, 'key', .14, (i % 3 - 1) * .2)
col(74.95, 77.1, 21, 1046, 'ts'); col(78.7, 80.6, 9, 1174, 'act')
E(82.0, 'pop', 520, .4); E(82.4, 'whoosh', .8, .3, True)
for i in range(10): E(82.4 + i * .2, 'pop', 800 + 60 * (i % 4), .2, (i % 5 - 2) * .25)
E(83.0, 'whoosh', .5, .25); E(84.6, 'lock', .45); E(84.7, 'chime', .4); E(84.8, 'sparkle', .9, .22)
# S11 recap
E(86.6, 'pop', 560, .35)
for i in range(5): E(86.6 + i * .08, 'pop', 600 + 60 * i, .25, (i - 2) * .3)
E(87.2, 'whoosh', .8, .3, True); E(88.8, 'riser', 1.0, .25); E(89.6, 'chime', .45); E(89.9, 'shimmer', .3)
# S12
E(91.4, 'sparkle', 1.0, .25); E(91.8, 'pop', 600, .35)
for i in range(9): E(92.4 + i * .17, 'tick', .22, 0, 2300 + 120 * i)
E(93.9, 'ding', 1318, .4); E(93.9, 'pop', 520, .45); E(93.95, 'shimmer', .25)
E(94.7, 'pop', 600, .35)
for i, t in enumerate([95.8, 96.4, 97.1]): E(t, 'pop', 600 + 60 * i, .4, (i - 1) * .3); E(t + .05, 'ding', 880 * (1.12 ** i), .22)
E(101.5, 'impact', .5); E(101.8, 'shimmer', .3); E(102.1, 'pop', 600, .3); E(104.3, 'pop', 600, .4); E(104.5, 'pop', 700, .3); E(105.7, 'pop', 520, .4)
E(107.0, 'whoosh', .5, .25)
for t in [107.6, 108.4, 109.2]: E(t, 'pop', 560, .4); E(t + .05, 'ding', 1046, .25)
E(110.4, 'swell', 1.8, .4); E(110.6, 'whoosh', .6, .3); E(111.1, 'chime', .5); E(111.2, 'shimmer', .3)

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
