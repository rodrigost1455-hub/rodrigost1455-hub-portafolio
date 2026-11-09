#!/usr/bin/env python3
"""Generate the DEMO charts used by the portfolio (synthetic data, fixed seed).
Nothing here comes from plant data. Run: python3 tools/gen_demo_charts.py
"""
import random, math, statistics as st, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
BG, LINE, INK, DIM, PH, AMB, RED = "#0a0d0c", "#2d3a37", "#d6e0dc", "#8a9a94", "#4ade80", "#fbbf24", "#f87171"
F = 'font-family="JetBrains Mono, ui-monospace, monospace"'

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">'
            f'<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')

def t(x, y, s, fill=DIM, size=10, anchor="start"):
    return f'<text x="{x}" y="{y}" fill="{fill}" {F} font-size="{size}" text-anchor="{anchor}">{s}</text>'

# ---------- 1) P-Chart demo (QualityHub) ----------
def pchart():
    rnd = random.Random(7)
    n = 24; p0 = 0.032; sub = 400
    ps = [max(0, rnd.gauss(p0, 0.006)) for _ in range(n)]
    ps[17] = 0.058                      # one out-of-control day, on purpose
    ucl = p0 + 3 * math.sqrt(p0 * (1 - p0) / sub)
    W, H, L, R, T, B = 560, 260, 46, 16, 34, 36
    ymax = 0.07
    X = lambda i: L + i * (W - L - R) / (n - 1)
    Y = lambda v: T + (1 - v / ymax) * (H - T - B)
    b = t(L, 18, "P-Chart · demo data (synthetic) · monthly UCL", INK, 11)
    for g in (0, 0.02, 0.04, 0.06):
        b += f'<line x1="{L}" x2="{W-R}" y1="{Y(g):.1f}" y2="{Y(g):.1f}" stroke="{LINE}" stroke-dasharray="2 4"/>' + t(L-6, Y(g)+3, f"{g*100:.0f}%", DIM, 9, "end")
    b += f'<line x1="{L}" x2="{W-R}" y1="{Y(ucl):.1f}" y2="{Y(ucl):.1f}" stroke="{AMB}" stroke-dasharray="5 3"/>' + t(W-R, Y(ucl)-4, "UCL", AMB, 9, "end")
    b += f'<line x1="{L}" x2="{W-R}" y1="{Y(p0):.1f}" y2="{Y(p0):.1f}" stroke="{DIM}"/>' + t(W-R, Y(p0)+11, "p̄", DIM, 9, "end")
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(ps))
    b += f'<polyline points="{pts}" fill="none" stroke="{PH}" stroke-width="1.5"/>'
    for i, v in enumerate(ps):
        c = RED if v > ucl else PH
        b += f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="{4 if v>ucl else 2.5}" fill="{c}"/>'
    b += t(L, H-12, "day of month →", DIM, 9) + t(W-R, H-12, "illustrative only · not plant data", DIM, 9, "end")
    (OUT/"demo-pchart.svg").write_text(svg(W, H, b, "Demo P-Chart with one point above the upper control limit"), encoding="utf-8")

# ---------- 2) EOL paired scatter + Cpk histograms ----------
def gen_pairs(seed):
    rnd = random.Random(seed); n = 46
    bench = [rnd.gauss(27.0, 0.2) for _ in range(n)]
    sd_noise = 0.2 * math.sqrt((1 - 0.83**2)) / 0.83 * 1.0
    stn = [b - 0.47 + rnd.gauss(0, sd_noise) for b in bench]
    return bench, stn

def pearson(a, b):
    ma, mb = st.mean(a), st.mean(b)
    return sum((x-ma)*(y-mb) for x, y in zip(a, b)) / math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))

def eol():
    best = None
    def fit(b, s):
        mb, ms = st.mean(b), st.mean(s)
        return sum((x-mb)*(y-ms) for x, y in zip(b, s)) / sum((x-mb)**2 for x in b)
    for seed in range(1, 3000):                      # seed whose r is ~0.83 AND slope ~1 (pure offset)
        b, s = gen_pairs(seed); r = pearson(b, s)
        err = abs(r-0.83) + abs(fit(b, s)-1.0)
        if best is None or err < best[0]: best = (err, seed, b, s)
    r = pearson(best[2], best[3]); best = (r, best[1], best[2], best[3])
    r, seed, bench, stn = best
    n = len(bench); mb, ms = st.mean(bench), st.mean(stn)
    slope = sum((x-mb)*(y-ms) for x, y in zip(bench, stn)) / sum((x-mb)**2 for x in bench)
    bias = st.mean(s-b for b, s in zip(bench, stn))
    W, H, L, R, T, B = 360, 300, 48, 14, 34, 40
    lo, hi = 26.2, 27.8
    X = lambda v: L + (v-lo)/(hi-lo)*(W-L-R)
    Y = lambda v: T + (1-(v-lo)/(hi-lo))*(H-T-B)
    b = t(L, 18, "Station vs bench · demo data (synthetic)", INK, 11)
    for g in (26.4, 26.8, 27.2, 27.6):
        b += f'<line x1="{L}" x2="{W-R}" y1="{Y(g):.1f}" y2="{Y(g):.1f}" stroke="{LINE}" stroke-dasharray="2 4"/>' + t(L-6, Y(g)+3, f"{g:.1f}", DIM, 9, "end")
        b += f'<line y1="{T}" y2="{H-B}" x1="{X(g):.1f}" x2="{X(g):.1f}" stroke="{LINE}" stroke-dasharray="2 4"/>' + t(X(g), H-B+14, f"{g:.1f}", DIM, 9, "middle")
    b += f'<line x1="{X(lo):.1f}" y1="{Y(lo):.1f}" x2="{X(hi):.1f}" y2="{Y(hi):.1f}" stroke="{DIM}" stroke-dasharray="5 3"/>' + t(X(27.45), Y(27.75), "y = x", DIM, 9)
    b += f'<line x1="{X(lo):.1f}" y1="{Y(lo-0.47):.1f}" x2="{X(hi):.1f}" y2="{Y(hi-0.47):.1f}" stroke="{AMB}"/>' + t(X(26.35), Y(26.2)-6, "offset −0.47 Ω", AMB, 9)
    for x, y in zip(bench, stn):
        b += f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="2.8" fill="{PH}" fill-opacity=".85"/>'
    b += t(W/2, H-6, "bench measurement (Ω)", DIM, 9, "middle")
    b += f'<text transform="translate(12 {H/2}) rotate(-90)" fill="{DIM}" {F} font-size="9" text-anchor="middle">EOL station (Ω)</text>'
    (OUT/"demo-eol-scatter.svg").write_text(svg(W, H, b, "Demo scatter of EOL station vs bench resistance with a constant offset"), encoding="utf-8")
    return dict(n=n, r=r, slope=slope, bias=bias, seed=seed)

def cpk(xs, lsl, usl):
    m, s = st.mean(xs), st.stdev(xs)
    return min(usl-m, m-lsl)/(3*s)

def hist():
    LSL, USL = 26.32, 27.68
    def sample(seed, mu, sd, n=400):
        rnd = random.Random(seed); return [rnd.gauss(mu, sd) for _ in range(n)]
    best = None
    for seed in range(1, 300):
        a = sample(seed, 27.0-0.47, 0.152); c = sample(seed+1000, 27.0, 0.152)
        ca, cb = cpk(a, LSL, USL), cpk(c, LSL, USL)
        err = abs(ca-0.47)+abs(cb-1.5)
        if best is None or err < best[0]: best = (err, a, c, ca, cb)
    _, a, c, ca, cb = best
    W, H, L, R, T, B = 560, 250, 20, 20, 34, 40
    lo, hi = 26.2, 27.8; bins = 32
    X = lambda v: L + (v-lo)/(hi-lo)*(W-L-R)
    def counts(xs):
        k = [0]*bins
        for v in xs:
            i = int((v-lo)/(hi-lo)*bins)
            if 0 <= i < bins: k[i] += 1
        return k
    ka, kc = counts(a), counts(c); mx = max(max(ka), max(kc))
    base = H-B; bw = (W-L-R)/bins
    b = t(L, 18, "Same resistance, two lines · demo data (synthetic)", INK, 11)
    for k, col, op in ((kc, PH, .55), (ka, AMB, .55)):
        for i, v in enumerate(k):
            h = v/mx*(base-T-8)
            b += f'<rect x="{L+i*bw+1:.1f}" y="{base-h:.1f}" width="{bw-2:.1f}" height="{h:.1f}" fill="{col}" fill-opacity="{op}"/>'
    for v, lab in ((LSL, "LSL"), (USL, "USL")):
        b += f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{T}" y2="{base}" stroke="{RED}" stroke-dasharray="4 3"/>' + t(X(v), T-4, lab, RED, 9, "middle")
    b += f'<line x1="{L}" x2="{W-R}" y1="{base}" y2="{base}" stroke="{LINE}"/>'
    b += t(L+4, H-22, f"■ line B · Cpk {cb:.2f}", PH, 10) + t(L+190, H-22, f"■ line A · Cpk {ca:.2f}", AMB, 10)
    b += t(W-R, H-8, "illustrative only · not plant data", DIM, 9, "end")
    (OUT/"demo-eol-cpk.svg").write_text(svg(W, H, b, "Demo histograms for two lines measuring the same resistance, Cpk about 0.47 versus about 1.5"), encoding="utf-8")
    return dict(cpk_a=ca, cpk_b=cb)

if __name__ == "__main__":
    pchart(); print(eol()); print(hist())
