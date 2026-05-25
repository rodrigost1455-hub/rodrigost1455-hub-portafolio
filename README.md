# Portfolio — Rodrigo Santana

> AI Engineer · Founding Engineer · Durango, MX
> Mechatronics engineer turned AI Engineer. Automotive quality discipline (IATF 16949) applied to production systems with Claude · LangChain · FastAPI.

---

## 🌐 Live Deployment

View the live portfolio hosted on Netlify:
👉 **[https://rodrigostorrecillas.netlify.app](https://rodrigostorrecillas.netlify.app)**

---

## 📦 Project Content

| File | Description |
|---|---|
| **`Portfolio v2.html`** | Current version. **CRT / terminal-phosphor** aesthetic featuring a boot overlay, command palette (⌘K), live ops widget, case studies with SVG architecture, and an experience timeline. |
| **`Portfolio v1.html`** | First iteration. Kept as a reference and linked from the v2 sidebar. |
| **`Direction Memo.html`** | Design direction memo — rationale, mood, typography, and color decisions that led to v2. |
| **`uploads/`** | Uploaded assets (images, reference materials). |

---

## 🚀 How to Open It

It is pure static HTML — no build step or server required.

```bash
# Option 1 — Open directly in the browser
open "Portfolio v2.html"

# Option 2 — Local server (recommended so fonts load via CDN without warnings)
python3 -m http.server 8000
# → http://localhost:8000/Portfolio%20v2.html
```

> Works offline once the browser caches the Google Fonts (JetBrains Mono + Instrument Serif).

---

## 🧱 Structure of `Portfolio v2.html`

A single page with vertical scrolling, divided into anchored sections:

1. **Hero** — `whoami`, large headline, proof bar (9+ apps, 1.8K SKUs, 100% precision), and the live-ops widget on the right.
2. **`// 01` Metrics that matter** — 4 stat cards with sparklines.
3. **`// differentiator` The unfair advantage** — the pitch in a single sentence.
4. **`// 02` Case studies** — three projects featuring **context / decision / architecture / impact** blocks, a war-log, a hero metric, and an SVG diagram:
   - Axionix POS (multi-tenant SaaS)
   - QIR & 8D (Yazaki — internal automotive quality platform)
   - Watson ML Classifier (Decision Tree, 100% precision on current sensors)
5. **`// 03` Stack** — skill matrix in 3 columns (AI/LLM · Backend · Frontend/Infra) with proficiency bars.
6. **`// 04` Experience** — timeline (Axionix · Yazaki · M.Sc. AI Tecmilenio).
7. **Contact** — final CTA + footer with build info.

---

## 🎨 Visual System

| Token | Value | Use |
|---|---|---|
| `--bg` | `#0a0d0c` | Base background (very dark green-black) |
| `--phosphor` | `#4ade80` | Main accent — CRT phosphor green |
| `--amber` | `#fbbf24` | Secondary accent · branches, war-logs |
| `--ink` | `#d6e0dc` | Main text |
| `--ink-dim` / `--ink-faint` | `#8a9a94` / `#4a5854` | Secondary hierarchy |
| `--mono` | JetBrains Mono | Body, UI, code |
| `--serif` | Instrument Serif italic | Headings, large numbers, hero |

**Environmental effects:** CRT scanlines + SVG grain overlays (`body::before` / `body::after`), a cursor glow that follows the mouse (`#ambient`), a boot overlay on load, and a blinking cursor in the hero.

---

## ⌨️ Interactions

- **⌘K / Ctrl+K** — opens the command palette (quick navigation + actions).
- **`/`** — search shortcut (suggested in the hero).
- **Scroll** — the sidebar highlights the active section.
- **Hover on case study** — the commit SHA and `+/−` stats come to life.
- **Live ops widget** — animated p95 latency sparkline using synthetic data.

---

## 🛠️ Customization

All content lives **inline** within each `.html` file (a single file per version). To edit:

- **Text / projects** → search for `<article class="project">` and `<div class="tl-item">`.
- **Metrics** → `.stats-grid` block (`#stats` section).
- **Skills** → `.skills-matrix` grid.
- **Colors** → `:root { --... }` tokens in the top `<style>`.
- **Typography** → change the Google Fonts `<link>` + the `--mono` / `--serif` variables.
- **Status / availability** → `.hire-strip` marquee + `// status` sidebar.

---

## 🧭 Philosophy

> Most AI engineers can wrap an LLM. Few have shipped under IATF 16949 supplier governance.

The portfolio is designed so that the first impression communicates **engineering rigor**, not AI slop: terminal aesthetics, real metrics, honest war-logs, and diagrams that look like internal documentation. Each case study follows the **context → decision → impact** structure — the exact format used to write 8Ds on the manufacturing plant floor.

---

## 📮 Contact

See the final section of the portfolio or the sidebar (`// external`). Open to remote roles as an **AI Engineer / Founding Engineer**.

---

*Build: Static HTML · zero runtime dependencies · served as a flat file.*
