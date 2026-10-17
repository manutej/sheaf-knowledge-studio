---
name: sheaf-field-manual-studio
description: Compile any validated Sheaf Knowledge Base (`sheaf_kb.json`) into a CETI Field-Manual & Meta-Notebook interactive HTML volume (`index.html` + deferred `sheaf_pages_bundle.js`) with warm cream paper (`#F5EFE3`) / deep ink (`#1A1612`) palette, `Fraunces` + `DM Sans` + `JetBrains Mono` typography, zero-leakage LaTeX/mathematical symbol typesetting, 5 editorial plates (`Architecture`, `Notebook Gluing Studio`, `Symbolic Visual Sandbox`, `Corpus Observed & 3D Poset`, `Course Blueprint`), non-color-alone verdict stamps, `.marginalia`, `.counterpoint`, and a slide-over verbatim book reader. Enforces 10 binary studio gates (`HF-STUDIO-01` through `HF-STUDIO-10`).
---

# Sheaf Field-Manual Studio (`sheaf-field-manual-studio`)

This skill compiles a verified Alexandrov Sheaf Knowledge Base (`sheaf_kb.json`) into an interactive, publication-grade **CETI Field-Manual & Gemini Notebook Studio** HTML volume modeled on `field-notebook-craft` and `meta-notebook`.

---

## 1. Reading & Asset Map

| Asset / Script | Path | Purpose |
|---|---|---|
| Canonical CSS Tokens | `assets/field-manual-tokens.css` | Warm Cream Paper `#F5EFE3`, Deep Ink `#1A1612`, Copper `#A67756`, 5-axis system, Dark Paper mode |
| Math & Symbolic Rendering Spec | `references/math-and-symbolic-rendering-spec.md` | 7-stage LaTeX-to-HTML parser (`convertLatexTokensToHtml`, `renderRichMarkdown`), split-bundle architecture |
| Studio HTML Compiler | `scripts/compile_field_manual_studio.py` | Compiles `sheaf_kb.json` $\to$ `index.html` (`<450 KB`) + `sheaf_pages_bundle.js` (`<script defer>`) |
| Automated Studio Auditor | `scripts/audit_rendered_html.py` | Verifies binary gates `HF-STUDIO-01` through `HF-STUDIO-10` |

---

## 2. Operational Workflow

### Step 1: Compile the Field-Manual Studio & Deferred Bundle
```bash
python3 .agents/skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py
```

### Step 2: Run the 10-Gate Adversarial Studio Audit (`HF-STUDIO-01..10`)
```bash
python3 .agents/skills/sheaf-field-manual-studio/scripts/audit_rendered_html.py \
  --html "Category Theory Sheaf Knowledge Base - Notebook Studio.html" \
  --kb "cattheory-sheaf-kb/data/sheaf_kb.json" \
  --out "cattheory-sheaf-kb/adversarial-eval/studio_html_audit.json"
```

**All 10 Studio Gates must be `CLEARED` before shipping:**
- `HF-STUDIO-01`: CETI Field-Manual Palette (`#F5EFE3`, `#1A1612`, `#A67756`) and 3-voice typography (`Fraunces`, `DM Sans`, `JetBrains Mono`).
- `HF-STUDIO-02`: Fast-Load Split-Bundle Architecture (`< 450 KB` core HTML + `<script defer>` page bundle).
- `HF-STUDIO-03`: Zero Raw LaTeX Backslash Leakage in static markup and across all KB `formal_core` and `synthesis_markdown` strings.
- `HF-STUDIO-04`: All 5 Editorial Plates (`#plate-1`..`#plate-5`) present with `.u-copper` one-italic-noun headings.
- `HF-STUDIO-05`: Every Plate carries both `.marginalia` (with `<cite>` author attribution) and `.counterpoint` ("when this is the wrong tool / where this breaks").
- `HF-STUDIO-06`: Non-color-alone verdict stamps (`◆`, `⚖`, `✓`, `±`, `⊘` + text label).
- `HF-STUDIO-07`: Single-mutator interactive instruments on Plates I, II, III, IV + on-demand 3D Poset RAF loop (`0%` idle CPU when hidden).
- `HF-STUDIO-08`: FORGE courseware compliance (`Key Concept` and `Why It Matters` only; zero `"So What"`; zero `"Module 1"` learner card titles; zero stacked `.callout-box` elements without intervening content).
- `HF-STUDIO-09`: Progressive Depth (`Newcomer | Practitioner | Expert`) and Paper Theme (`Cream | Ink`) switches wired.
- `HF-STUDIO-10`: Slide-Over Verbatim Book Reader Drawer + `window.__jumpToPage(p, term)` citation pills wired.

---

## 3. BookVoiceProfile — Letting Each Book Speak in Its Own Design & Vision

Never lock two different books into identical plate structures or cookie-cutter widgets. Before compiling a studio, read `book.voice_profile` from `sheaf_kb.json` and adapt the accent palette, frontispiece diagram, and bespoke interactive instruments to the author's native epistemology:

| Corpus Archetype | Example Book | Visual Register & Palette | Bespoke Instruments |
|---|---|---|---|
| **Scientific Ologs & Functorial Databases** | David I. Spivak — *Category Theory for the Sciences* (609 pp.) | Archival MIT Press Field Manual (`#F5EFE3` warm cream, `#A67756` copper, `#8C6239` amber) | • **Plate I:** 5-Stage Sheaf-MCP Query Pipeline Inspector<br>• **Plate II:** Sheaf Open-Cover Gluing Studio<br>• **Plate III:** 8-Token Symbolic Diagram Sandbox |
| **Point-Free Visual Abstraction & Curry-Howard-Lambek Rosetta** | Boris Marinov — *Category Theory Illustrated* (377 pp.) | Geometric Inkscape Sketchbook (`#F6F1E7` drafting vellum, `#2B5B84` cobalt, `#B87D24` ochre, `#B34434` vermilion, `#35694E` viridian) | • **Plate I:** Lawvere Internal (Colored Balls) $\leftrightarrow$ External (Point-Free Arrows) Shifter<br>• **Plate II:** 6-World Rosetta Stone Translator (`Sets · Categories · Monoids · Orders · Logic · Types`)<br>• **Plate III:** Sheaf Notebook + Interactive `Task 1..90` Explorer |

