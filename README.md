# Rodrigo Santana — AI Engineer Portfolio

Portafolio personal estilo terminal/dashboard, single-file HTML. Cero dependencies, deploy en cualquier plataforma estática.

---

## 🚀 Deploy rápido a Vercel

```bash
# Opción 1: con Vercel CLI
npm i -g vercel
vercel
# → confirma el deploy, listo en ~10 segundos

# Opción 2: arrastra y suelta
# Ve a vercel.com/new → drag & drop esta carpeta
```

Para que tome dominio limpio (`rodrigosantana.dev` o similar):
1. Compra el dominio (Namecheap / Cloudflare ~$12 USD/año)
2. Vercel → Project → Settings → Domains → Add
3. Apunta los DNS según las instrucciones de Vercel

## 🐙 Deploy a GitHub Pages (gratis)

```bash
cd portfolio
git init
git add .
git commit -m "feat: initial portfolio"
git branch -M main
git remote add origin https://github.com/rodrigost1455-hub/portfolio.git
git push -u origin main
```

Luego en GitHub: **Settings → Pages → Source: main / root**. Live en `rodrigost1455-hub.github.io/portfolio`.

---

## ✏️ Qué editar antes de publicar

Abre `index.html` y busca/reemplaza:

| Placeholder | Dónde está | Qué poner |
|---|---|---|
| `mailto:rodrigo@example.com` | sección contact | tu email real |
| `https://linkedin.com` (×2) | sidebar + contact | URL real de tu LinkedIn |
| `/cv.pdf` | botón download cv | sube tu CV como `cv.pdf` en la raíz |
| Métricas en `#stats` | sección 01 | ajusta números si quieres ser más conservador |

## 🎨 Decisiones de diseño

- **Estética**: CRT terminal + dashboard observability. Scanlines, noise grain, monoespaciada, accent phosphor verde (#4ade80).
- **Tipografía**: JetBrains Mono (display + body) + Instrument Serif italic (headings) — combo que se lee como código pero respira con elegancia editorial.
- **Layout**: sidebar fijo estilo IDE + área principal scrollable. Status bar superior con clock en vivo.
- **Anti-AI-slop**: nada de gradientes morados, nada de Inter, nada de Tailwind defaults. Compromiso total con la estética.

## 📁 Estructura

```
portfolio/
├── index.html      # todo el portafolio, single-file
├── cv.pdf          # ⚠️ tú lo agregas aquí
└── README.md       # esto
```

## 🧠 Por qué cada sección está donde está

1. **Hero** — pitch en 2 segundos: AI Engineer con backbone de quality engineering (tu unique angle).
2. **Metrics** — números reales y verificables (98% faster, 1.8K SKUs, 100% precision). Antes de proyectos porque los reclutadores skiman.
3. **Projects** — 3 case studies con problema → stack → impacto. Cada uno con badge `● production` o `● deployed` (anti-vaporware).
4. **Stack** — matrix con dots de proficiencia, agrupado por dominio. AI/LLM primero (lo que estás vendiendo).
5. **Experience** — timeline corto, dual (Axionix + Yazaki) + máster en curso.
6. **Contact** — CTA directo: "I'm ready to ship", links a email/GitHub/LinkedIn/CV.

---

Built by Rodrigo Santana · 2026
