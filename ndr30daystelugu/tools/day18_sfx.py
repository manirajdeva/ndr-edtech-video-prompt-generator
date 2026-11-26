import numpy as np, wave, sys, os
SR = 48000
DUR = 124.8
rng = np.random.default_rng(18)
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


# ---------------- Day 18 events (soft) ----------------
ev = []
def E(t, kind, *a, **k): ev.append((t, kind, a, k))
for t in [3.98, 18.07, 24.98, 28.32, 40.59, 55.59, 64.57, 90.73, 103.86, 112.06]:
    E(t - 0.3, 'whoosh', 0.6, 0.3)
E(0.0, 'riser', 2.0, .2); E(.3, 'pop', 600, .3); E(.9, 'pop', 700, .3); E(2.46, 'pop', 520, .32); E(2.5, 'shimmer', .22)
E(4.2, 'pop', 560, .3); E(5.6, 'pop', 700, .35); E(5.65, 'ding', 1046, .25)
E(6.4, 'whoosh', .8, .22, False)
E(7.93, 'pop', 540, .3); E(8.4, 'pop', 600, .28)
for i in range(10): E(10.3 + i * .25, 'tick', .12, 0, 1100)
E(12.8, 'warn', .2)
E(13.52, 'pop', 540, .28); E(14.0, 'chime', .35); E(16.4, 'whoosh', .8, .22, True); E(16.9, 'ding', 1174, .3); E(16.95, 'sparkle', .8, .2)
E(18.46, 'impact', .4); E(18.5, 'chime', .35); E(20.0, 'pop', 580, .28)
for t in [22.6, 23.0, 23.4]: E(t, 'pop', 560 + (t - 22.6) * 400, .3); E(t + .05, 'ding', 1046, .2)
E(25.16, 'pop', 680, .3); E(26.37, 'chime', .4); E(26.5, 'shimmer', .22)
for t, f in [(28.53, 600), (40.79, 640), (55.81, 680)]: E(t, 'pop', f, .3); E(t + .7, 'impact', .3)
E(30.47, 'pop', 540, .28); E(30.6, 'whoosh', .9, .2, True); E(32.4, 'ding', 988, .28); E(32.5, 'shimmer', .22)
E(34.29, 'pop', 560, .28); E(36.9, 'pop', 620, .28); E(38.9, 'whoosh', .8, .22, True); E(39.8, 'chime', .38)
E(42.83, 'pop', 540, .28)
for i in range(8): E(43.4 + i * .3, 'tick', .12, 0, 1000 + 60 * i)
E(47.35, 'pop', 560, .28); E(49.6, 'chime', .35)
E(51.34, 'warn', .22); E(53.0, 'thud', .28); E(54.0, 'whoosh', 1.0, .22, False); E(54.05, 'sparkle', .8, .18)
E(57.7, 'pop', 560, .28); E(60.0, 'pop', 600, .28)
for i in range(6): E(60.6 + i * .3, 'tick', .12, 0, 1800)
E(63.4, 'chime', .38); E(63.45, 'shimmer', .22)
E(64.78, 'pop', 540, .3); E(64.8, 'ding', 880, .22); E(67.06, 'pop', 520, .28); E(68.8, 'pop', 600, .28)
E(70.8, 'whoosh', 1.4, .22, True)
for i in range(8): E(71.5 + i * .3, 'tick', .1, 0, 1100)
E(75.3, 'ding', 988, .25); E(76.5, 'whoosh', .9, .22, True); E(78.8, 'chime', .4); E(78.85, 'shimmer', .22)
E(81.2, 'whoosh', .9, .22, True); E(83.4, 'chime', .38)
E(85.0, 'pop', 600, .28); E(85.1, 'whoosh', 1.0, .22, True); E(87.4, 'chime', .38); E(87.45, 'shimmer', .22)
E(91.0, 'pop', 580, .3); E(91.25, 'ding', 880, .22)
for t in [93.12, 95.60, 99.71]: E(t, 'pop', 600, .3); E(t + .05, 'ding', 1046, .22)
for t in [94.10, 96.67, 100.89]: E(t, 'tick', .22, 0, 2000)
E(104.0, 'swell', 1.2, .28); E(104.3, 'sparkle', 1.0, .22)
for i in range(18): E(104.8 + i * .1, 'tick', .13, (i % 5 - 2) * .2, 2000 + 70 * i)
E(106.3, 'pop', 620, .3); E(106.8, 'chime', .42); E(106.82, 'impact', .25)
E(107.5, 'pop', 540, .28); E(108.8, 'pop', 600, .28); E(109.1, 'pop', 660, .28); E(109.4, 'whoosh', .8, .2, True); E(110.2, 'pop', 700, .3)
E(112.2, 'impact', .3); E(112.22, 'shimmer', .22)
for t in [113.0, 114.0, 114.6, 115.0, 115.6, 117.2]: E(t, 'pop', 600, .3)
E(117.25, 'ding', 1174, .25); E(118.25, 'pop', 600, .3)
for t in [118.7, 119.4, 120.1]: E(t, 'pop', 560, .32); E(t + .05, 'ding', 1046, .2)
E(121.75, 'swell', 1.4, .3); E(121.9, 'chime', .42); E(122.0, 'shimmer', .22); E(122.4, 'pop', 620, .3)

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
