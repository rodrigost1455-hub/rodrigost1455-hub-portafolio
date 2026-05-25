# Portafolio — Rodrigo Santana

> AI Engineer · Founding Engineer · Durango, MX
> Mecatrónico convertido en AI Engineer. Disciplina de calidad automotriz (IATF 16949) aplicada a sistemas de producción con Claude · LangChain · FastAPI.

---

## 📦 Contenido del proyecto

| Archivo | Descripción |
|---|---|
| **`Portfolio v2.html`** | Versión actual. Estética **CRT / terminal-phosphor** con boot overlay, command palette (⌘K), live ops widget, case studies con arquitectura SVG y timeline de experiencia. |
| **`Portfolio v1.html`** | Primera iteración. Conservada como referencia y enlazada desde la sidebar de v2. |
| **`Direction Memo.html`** | Memo de dirección de diseño — racional, mood, decisiones tipográficas y de color que llevaron a v2. |
| **`uploads/`** | Recursos subidos (imágenes, materiales de referencia). |

---

## 🚀 Cómo abrirlo

Es HTML estático puro — no requiere build ni servidor.

```bash
# opción 1 — abrir directo en el navegador
open "Portfolio v2.html"

# opción 2 — servidor local (recomendado para que carguen las fuentes vía CDN sin warnings)
python3 -m http.server 8000
# → http://localhost:8000/Portfolio%20v2.html
```

> Funciona offline una vez que el navegador cachea las Google Fonts (JetBrains Mono + Instrument Serif).

---

## 🧱 Estructura de `Portfolio v2.html`

Una sola página, scroll vertical, dividida en secciones ancladas:

1. **Hero** — `whoami`, titular grande, proof bar (9+ apps, 1.8K SKUs, 100% precision) y live-ops widget de la derecha.
2. **`// 01` Metrics that matter** — 4 stat cards con sparklines.
3. **`// differentiator` The unfair advantage** — el pitch en una frase.
4. **`// 02` Case studies** — tres proyectos con bloques **context / decision / architecture / impact**, war-log, métrica hero y diagrama SVG:
   - Axionix POS (multi-tenant SaaS)
   - QIR & 8D (Yazaki — plataforma interna de calidad automotriz)
   - Watson ML Classifier (Decision Tree, 100% precision en sensores de corriente)
5. **`// 03` Stack** — matriz de skills en 3 columnas (AI/LLM · Backend · Frontend/Infra) con barras de dominio.
6. **`// 04` Experience** — timeline (Axionix · Yazaki · M.Sc. AI Tecmilenio).
7. **Contact** — CTA final + footer con build info.

---

## 🎨 Sistema visual

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#0a0d0c` | Fondo base (verde-negro muy oscuro) |
| `--phosphor` | `#4ade80` | Acento principal — verde fósforo CRT |
| `--amber` | `#fbbf24` | Acento secundario · branches, war-logs |
| `--ink` | `#d6e0dc` | Texto principal |
| `--ink-dim` / `--ink-faint` | `#8a9a94` / `#4a5854` | Jerarquía secundaria |
| `--mono` | JetBrains Mono | Cuerpo, UI, código |
| `--serif` | Instrument Serif italic | Títulos, números grandes, hero |

**Efectos ambientales:** scanlines CRT + grain SVG superpuestos (`body::before` / `body::after`), glow del cursor que sigue el mouse (`#ambient`), boot overlay al cargar, cursor parpadeante en el hero.

---

## ⌨️ Interacciones

- **⌘K / Ctrl+K** — abre command palette (navegación rápida + acciones).
- **`/`** — atajo de búsqueda (sugerido en el hero).
- **Scroll** — la sidebar resalta la sección activa.
- **Hover en case study** — el SHA del commit y los stats `+/−` cobran vida.
- **Live ops widget** — sparkline de p95 latency animado con datos sintéticos.

---

## 🛠️ Personalizar

Todo el contenido vive **inline** en cada `.html` (un solo archivo por versión). Para editar:

- **Texto / proyectos** → buscar `<article class="project">` y `<div class="tl-item">`.
- **Métricas** → bloque `.stats-grid` (sección `#stats`).
- **Skills** → matriz `.skills-matrix`.
- **Colores** → tokens `:root { --... }` en el `<style>` superior.
- **Tipografía** → cambiar el `<link>` de Google Fonts + las variables `--mono` / `--serif`.
- **Status / disponibilidad** → marquee `.hire-strip` + sidebar `// status`.

---

## 🧭 Filosofía

> Most AI engineers can wrap an LLM. Few have shipped under IATF 16949 supplier governance.

El portafolio está diseñado para que la primera impresión comunique **rigor de ingeniero**, no slop de IA: terminal estética, métricas reales, war-logs honestos, diagramas que parecen documentación interna. Cada case study sigue la estructura **context → decision → impact** — el formato con el que se escriben los 8D en planta.

---

## 📮 Contacto

Ver sección final del portafolio o sidebar (`// external`). Abierto a roles remotos como **AI Engineer / Founding Engineer**.

---

*Build: HTML estático · cero dependencias de runtime · servido como archivo plano.*
