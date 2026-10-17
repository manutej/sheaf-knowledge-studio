#!/usr/bin/env python3
r"""
build_studio_html.py (CETI Field-Manual & Meta-Notebook Edition)
================================================================
Compiles the Category Theory Sheaf Knowledge Base & Gemini Notebook Studio using:
  1. CETI `field-notebook-craft` & `meta-notebook` Warm Paper (#F5EFE3) & Deep Ink (#1A1612)
     design system (`Fraunces` italic display, `DM Sans` body, `JetBrains Mono` apparatus,
     5-axis ribbon, `Newcomer | Practitioner | Expert` progressive depth, Light/Dark paper,
     honesty stamps `◆ ratified`, `⚖ measured`, `✓ accept`, `± refine`, `⊘ GATE`,
     `.derived` dark callout cards, `.marginalia`, and `.counterpoint` panels).
  2. Complete Mathematical & LaTeX-to-Typeset-HTML Engine (`convertLatexTokensToHtml`, `renderRichMarkdown`):
     Zero raw LaTeX backslashes leak to the screen. All `$$...$$`, `$...$`, `\mathcal{...}`,
     `\mathbf{...}`, `\text{...}`, `\varprojlim`, `\varinjlim`, `\xrightarrow{...}`,
     `\dashv`, `\simeq`, `\cong`, `\times_Z`, `\sqcup_W`, subscripts, superscripts, and
     symbolic tokens render into crisp mathematical typography.
  3. Instant First Paint (~155 KB core HTML) + Non-blocking `<script defer>` 609-page bundle.
  4. Five Interactive Plates:
     - Plate I   (technology): Query & Sheaf Gluing Architecture (SQLite FTS5 + Alexandrov Sheaf + Gemini/MCP)
     - Plate II  (research):   Gemini Notebook Gluing Studio & Open Cover Selector + 609-Page Reader Drawer
     - Plate III (art):        "Category Theory Illustrated: Through Symbols" Interactive Symbolic Sandbox
     - Plate IV  (science):    The 30 Concept Stalks, 877 Formal Declarations & 3D Alexandrov Poset Atlas
     - Plate V   (teaching):   Course Blueprint & Curriculum Scope ("Category Theory Illustrated: Through Symbols")
"""

import json
import math
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
WORKSPACE_DIR = ROOT_DIR.parent
KB_PATH = ROOT_DIR / "data" / "sheaf_kb.json"
BUNDLE_PATH = ROOT_DIR / "data" / "sheaf_pages_bundle.js"

OUT_MAIN = WORKSPACE_DIR / "Category Theory Sheaf Knowledge Base - Notebook Studio.html"
OUT_LOCAL = ROOT_DIR / "index.html"
OUT_ARTIFACT = Path("/Users/cairo/.gemini/antigravity/brain/109c7092-572c-4cbf-ac55-3677c5ef2652/sheaf_notebook_studio.html")


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en" data-theme="light" data-level="practitioner" data-motion="on">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Sheaf of Ologged Concepts · Category Theory for the Sciences (Field Manual &amp; Notebook Studio)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..600;1,9..40,400&family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* ============================================================================
 * 0. CETI FIELD-NOTEBOOK-CRAFT & META-NOTEBOOK TOKENS
 *    Warm Cream Paper (#F5EFE3) · Deep Ink (#1A1612) · Copper Accent (#A67756)
 * ============================================================================ */
:root {
  /* Raw palette — light paper default */
  --raw-paper: #F5EFE3;
  --raw-paper-soft: #E8DFCB;
  --raw-surface: #F2E6DC;       /* Shy Marshmallow */
  --raw-ink: #1A1612;
  --raw-ink-2: #3A312A;
  --raw-ink-3: #6B5F53;
  --raw-rule: #C8C9CB;          /* Kilim Grey */
  --raw-copper: #A67756;        /* Browning Copper */
  --raw-rust: #8C4A2E;
  --raw-sage: #799070;          /* Grass Hopper */
  --raw-plum: #4A3A5C;
  --raw-slate: #3B6E8F;
  --raw-crimson: #7A2E4A;

  /* Semantic layer */
  --paper: var(--raw-paper);
  --paper-soft: var(--raw-paper-soft);
  --surface: var(--raw-surface);
  --ink: var(--raw-ink);
  --ink-2: var(--raw-ink-2);
  --ink-3: var(--raw-ink-3);
  --rule: var(--raw-rule);
  --rule-hair: rgba(26, 22, 18, 0.14);
  --accent: var(--raw-copper);
  --accent-text: var(--raw-rust);
  --accent-soft: rgba(166, 119, 86, 0.14);
  --good: #3F5E39;
  --good-soft: rgba(63, 94, 57, 0.14);
  --warn: #8C4A2E;
  --bad: #8E2A22;

  /* Five axes */
  --ax-research: var(--raw-plum);
  --ax-technology: var(--raw-slate);
  --ax-art: var(--raw-crimson);
  --ax-science: #4A6344;
  --ax-teaching: #8C4A2E;

  /* Typography */
  --f-serif: 'Fraunces', 'Iowan Old Style', 'Palatino', Georgia, serif;
  --f-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --f-mono: 'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, monospace;
  --f-math: 'STIX Two Math', 'Cambria Math', 'Latin Modern Math', 'Fraunces', Georgia, serif;

  /* Fluid type scale */
  --s-hero: clamp(2.15rem, 1.5rem + 2.4vw, 3.6rem);
  --s-h1: clamp(1.55rem, 1.2rem + 1.3vw, 2.25rem);
  --s-h2: clamp(1.18rem, 1.02rem + 0.65vw, 1.48rem);
  --s-body: clamp(0.96rem, 0.92rem + 0.18vw, 1.05rem);
  --s-small: clamp(0.82rem, 0.79rem + 0.12vw, 0.90rem);
  --s-mono: clamp(0.73rem, 0.70rem + 0.10vw, 0.80rem);

  /* Spacing & Grid */
  --pad: clamp(1.2rem, 3.2vw, 3.2rem);
  --gap: clamp(1rem, 2vw, 2rem);
  --col-w: 1240px;
}

/* Dark Paper Mode — warm charcoal paper, cream ink */
html[data-theme="dark"] {
  --paper: #1A1612;
  --paper-soft: #241F1A;
  --surface: #2B241E;
  --ink: #F3ECDF;
  --ink-2: #D4C8B4;
  --ink-3: #9A8E7B;
  --rule: #3E362E;
  --rule-hair: rgba(243, 236, 223, 0.14);
  --accent: #C8926D;
  --accent-text: #DBA882;
  --accent-soft: rgba(219, 168, 130, 0.16);
  --good: #96B08C;
  --good-soft: rgba(150, 176, 140, 0.16);
  --warn: #DBA882;
  --bad: #E07A70;
  --ax-research: #B8A4CF;
  --ax-technology: #7FB2D4;
  --ax-art: #D4849F;
  --ax-science: #96B08C;
  --ax-teaching: #DBA882;
}
html[data-theme="dark"] .hero-figure svg,
html[data-theme="dark"] #symDiagramSvgWrap svg,
html[data-theme="dark"] #gluedOlogSvgWrap svg {
  background: #F5EFE3;
  border-radius: 3px;
  padding: 6px;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
html[data-motion="off"] *, html[data-motion="off"] *::before, html[data-motion="off"] *::after {
  animation: none !important; transition: none !important;
}

*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; overflow-x: hidden; max-width: 100%; }
body {
  margin: 0;
  overflow-x: hidden;
  max-width: 100%;
  background-color: var(--paper);
  background-image:
    radial-gradient(ellipse at 18% 0%, rgba(166,119,86,0.08), transparent 60%),
    radial-gradient(ellipse at 88% 100%, rgba(121,144,112,0.07), transparent 55%);
  color: var(--ink);
  font-family: var(--f-sans);
  font-size: var(--s-body);
  line-height: 1.62;
  font-feature-settings: "kern" 1, "liga" 1, "onum" 1;
  -webkit-font-smoothing: antialiased;
}

/* ============================================================================
 * 1. TYPOGRAPHY & HONESTY APPARATUS (Stamps, Marginalia, Counterpoints)
 * ============================================================================ */
h1, h2, h3, .serif {
  font-family: var(--f-serif);
  font-weight: 350;
  letter-spacing: -0.015em;
  line-height: 1.15;
  margin: 0;
  font-variation-settings: "SOFT" 50, "WONK" 1;
}
h1 em, h2 em, h3 em, .serif em {
  font-style: italic;
  font-weight: 300;
  color: var(--accent-text);
}
p { margin: 0 0 0.9em 0; max-width: 68ch; color: var(--ink-2); }
a { color: var(--accent-text); text-decoration: underline; text-decoration-color: var(--accent); text-underline-offset: 3px; }
a:hover { color: var(--ink); }

.mono, code, .num {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  font-variant-numeric: tabular-nums;
}
.eyebrow {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-3);
  display: flex;
  align-items: center;
  gap: 0.65ch;
  flex-wrap: wrap;
}
.eyebrow::before {
  content: "";
  display: inline-block;
  width: 14px;
  height: 1px;
  background: var(--accent);
}
.u-copper {
  background-image: linear-gradient(transparent 78%, rgba(166,119,86,0.34) 78%, rgba(166,119,86,0.34) 93%, transparent 93%);
  padding: 0 2px;
}

/* Axis tags & Verdict stamps (Glyph + Label — never color alone) */
.ax-tag {
  font-family: var(--f-mono);
  font-size: 0.69rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 2px;
  border: 1px solid currentColor;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  line-height: 1.35;
  white-space: nowrap;
}
.ax-tag::before { content: ""; width: 5px; height: 5px; border-radius: 50%; background: currentColor; }
.ax-research   { color: var(--ax-research); }
.ax-technology { color: var(--ax-technology); }
.ax-art        { color: var(--ax-art); }
.ax-science    { color: var(--ax-science); }
.ax-teaching   { color: var(--ax-teaching); }

.stamp {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 2px;
  border: 1px solid var(--rule);
  background: var(--paper);
  color: var(--ink-2);
  display: inline-flex;
  align-items: center;
  gap: 4px;
  white-space: nowrap;
}
.stamp.ratified { border-color: var(--accent); color: var(--accent-text); background: rgba(166,119,86,0.09); }
.stamp.measured { border-color: var(--good); color: var(--good); background: rgba(121,144,112,0.11); }
.stamp.accept   { border-color: var(--ax-technology); color: var(--ax-technology); background: rgba(59,110,143,0.09); }
.stamp.refine   { border-color: var(--warn); color: var(--warn); background: rgba(140,74,46,0.08); }
.stamp.gate     { border-style: dashed; color: var(--ink-3); }

/* Glossary hover terms */
abbr[data-gloss] {
  text-decoration: none;
  border-bottom: 1px dotted var(--accent);
  cursor: help;
  position: relative;
  color: var(--ink);
}
abbr[data-gloss]:hover::after {
  content: attr(data-gloss);
  position: absolute;
  left: 0;
  bottom: calc(100% + 6px);
  width: min(310px, 78vw);
  padding: 8px 11px;
  background: var(--ink);
  color: var(--paper);
  font-family: var(--f-sans);
  font-size: 0.78rem;
  line-height: 1.42;
  border-radius: 3px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.22);
  z-index: 80;
  pointer-events: none;
}

/* Audience progressive disclosure (`Newcomer | Practitioner | Expert`) */
[data-depth="2"], [data-depth="3"] { transition: opacity 0.2s ease; }
html[data-level="newcomer"] [data-depth="2"],
html[data-level="newcomer"] [data-depth="3"] { display: none !important; }
html[data-level="practitioner"] [data-depth="3"] { display: none !important; }

/* ============================================================================
 * 2. MATHEMATICAL NOTATION & SYMBOLIC RENDERING TYPOGRAPHY
 *    Clean typeset math spans, display equations, commutative fractions, arrows
 * ============================================================================ */
.math-expr {
  font-family: var(--f-math);
  font-size: 1.03em;
  color: var(--ink);
  background: rgba(166, 119, 86, 0.08);
  border: 1px solid rgba(166, 119, 86, 0.22);
  padding: 1px 6px;
  border-radius: 3px;
  display: inline-block;
  line-height: 1.38;
  white-space: normal;
  overflow-wrap: anywhere;
  max-width: 100%;
}
.math-display {
  font-family: var(--f-math);
  font-size: 1.08rem;
  color: var(--ink);
  background: var(--paper-soft);
  border-left: 3px solid var(--accent);
  border-top: 1px solid var(--rule-hair);
  border-right: 1px solid var(--rule-hair);
  border-bottom: 1px solid var(--rule-hair);
  padding: 0.75rem 1.05rem;
  margin: 0.75rem 0;
  border-radius: 2px;
  overflow-x: auto;
  max-width: 100%;
  line-height: 1.55;
  text-align: center;
}
.m-cal {
  font-family: 'Fraunces', 'STIX Two Math', Georgia, serif;
  font-style: italic;
  font-weight: 500;
  color: var(--accent-text);
  letter-spacing: 0.02em;
}
.m-cat {
  font-family: var(--f-sans);
  font-weight: 700;
  font-size: 0.92em;
  letter-spacing: 0.01em;
  color: var(--ink);
}
.m-op {
  font-family: var(--f-mono);
  font-size: 0.86em;
  color: var(--ax-research);
  font-weight: 500;
}
.m-arrow {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  vertical-align: middle;
  margin: 0 4px;
  line-height: 1;
}
.m-arrow-label {
  font-family: var(--f-math);
  font-size: 0.72em;
  color: var(--accent-text);
  margin-bottom: -3px;
  padding: 0 3px;
}
.m-arrow-body {
  font-size: 1.05em;
  color: var(--ink);
}
.m-lim {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  vertical-align: middle;
  line-height: 1.05;
  margin: 0 3px;
}
.m-lim-top {
  font-family: var(--f-mono);
  font-size: 0.82em;
  font-weight: 600;
  color: var(--ax-technology);
}
.m-lim-sub {
  font-size: 0.68em;
  color: var(--ink-3);
}
.cite-pill {
  font-family: var(--f-mono);
  font-size: 0.72rem;
  color: var(--accent-text);
  background: var(--surface);
  border: 1px solid var(--accent);
  border-radius: 2px;
  padding: 4px 8px;
  min-height: 29px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  margin: 2px;
  vertical-align: baseline;
  transition: background 0.12s, color 0.12s;
}
.cite-pill:hover {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}
.inline-code {
  font-family: var(--f-mono);
  font-size: 0.84em;
  background: var(--paper-soft);
  border: 1px solid var(--rule-hair);
  padding: 1px 5px;
  border-radius: 2px;
  color: var(--ink);
  overflow-wrap: anywhere;
}

/* ============================================================================
 * 3. STICKY AXIS RIBBON & FIELD CONTROLS CHROME
 * ============================================================================ */
.axis-ribbon {
  position: sticky;
  top: 0;
  z-index: 60;
  background: color-mix(in oklab, var(--paper) 93%, transparent);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--rule-hair);
}
.axis-ribbon-inner {
  max-width: var(--col-w);
  margin: 0 auto;
  padding: 8px var(--pad);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}
.brand-mark {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 10px;
}
.brand-mark .dot {
  width: 8px;
  height: 8px;
  background: var(--accent);
  display: inline-block;
  transform: rotate(45deg);
  flex-shrink: 0;
}
.plate-nav {
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
}
.plate-nav a {
  font-family: var(--f-mono);
  font-size: 0.71rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--ink-2);
  padding: 4px 8px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.plate-nav a:hover {
  border-color: var(--accent);
  color: var(--ink);
  background: var(--paper-soft);
}
.field-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-family: var(--f-mono);
  font-size: 0.70rem;
}
.ctrl-group {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--rule);
  border-radius: 2px;
  overflow: hidden;
  background: var(--paper-soft);
}
.ctrl-group .ctrl-label {
  padding: 5px 7px;
  color: var(--ink-3);
  border-right: 1px solid var(--rule);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.ctrl-btn {
  appearance: none;
  border: 0;
  background: transparent;
  color: var(--ink-2);
  font: inherit;
  padding: 5px 9px;
  min-height: 29px;
  cursor: pointer;
  letter-spacing: 0.04em;
  white-space: nowrap;
}
.ctrl-btn:hover { color: var(--ink); }
.ctrl-btn[aria-pressed="true"] {
  background: var(--ink);
  color: var(--paper);
}
.drawer-toggle-btn {
  appearance: none;
  border: 1px solid var(--accent);
  background: var(--surface);
  color: var(--accent-text);
  font-family: var(--f-mono);
  font-size: 0.71rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 5px 10px;
  min-height: 30px;
  border-radius: 2px;
  cursor: pointer;
  font-weight: 600;
  white-space: nowrap;
}
.drawer-toggle-btn:hover {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}

/* ============================================================================
 * 4. FRONTISPIECE & EDITORIAL PLATE ARCHITECTURE
 * ============================================================================ */
.page-wrap {
  max-width: var(--col-w);
  width: 100%;
  margin: 0 auto;
  padding: 0 var(--pad);
  overflow-x: clip;
}
header.frontispiece {
  padding: clamp(2rem, 4.5vw, 4rem) 0 clamp(1.8rem, 3.5vw, 3rem);
  border-bottom: 2px solid var(--ink);
  position: relative;
}
.frontispiece-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: var(--gap);
  align-items: end;
}
.frontispiece-grid > * { min-width: 0; max-width: 100%; }
@media (max-width: 900px) {
  .frontispiece-grid { grid-template-columns: 1fr; }
}
.hero-title {
  font-size: var(--s-hero);
  font-weight: 300;
  line-height: 1.04;
  letter-spacing: -0.025em;
  margin: 0.35rem 0 0.9rem;
}
.hero-lede {
  font-size: clamp(1.02rem, 0.96rem + 0.32vw, 1.18rem);
  line-height: 1.55;
  color: var(--ink-2);
  max-width: 58ch;
}
.frontispiece-meta {
  margin-top: 1.4rem;
  padding-top: 0.9rem;
  border-top: 1px solid var(--rule-hair);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 0.75rem;
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  color: var(--ink-3);
}
.frontispiece-meta dt { text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.67rem; }
.frontispiece-meta dd { margin: 2px 0 0; color: var(--ink); font-weight: 500; }

.hero-figure {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: 1rem 1.15rem 0.8rem;
  position: relative;
  min-width: 0;
  max-width: 100%;
}
.hero-figure figcaption {
  font-family: var(--f-mono);
  font-size: 0.71rem;
  color: var(--ink-3);
  margin-top: 0.5rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 4px;
  border-top: 1px solid var(--rule-hair);
  padding-top: 0.45rem;
}

/* Table of Contents bar */
nav.toc {
  padding: 0.95rem 0;
  border-bottom: 1px solid var(--rule-hair);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(195px, 1fr));
  gap: 0.5rem 1.2rem;
  font-family: var(--f-mono);
  font-size: var(--s-mono);
}
nav.toc a {
  text-decoration: none;
  color: var(--ink-2);
  display: flex;
  justify-content: space-between;
  padding: 4px 0;
  border-bottom: 1px dotted var(--rule);
}
nav.toc a:hover { color: var(--accent-text); border-bottom-color: var(--accent); }
nav.toc .toc-num { color: var(--accent-text); margin-right: 0.5ch; }

/* Plates */
section.plate {
  padding: clamp(2.4rem, 5vw, 4.2rem) 0;
  border-bottom: 1px solid var(--rule);
  position: relative;
}
.plate-head {
  display: grid;
  grid-template-columns: 230px 1fr;
  gap: var(--gap);
  margin-bottom: clamp(1.4rem, 2.6vw, 2.2rem);
  align-items: baseline;
}
.plate-head > * { min-width: 0; max-width: 100%; }
@media (max-width: 900px) {
  .plate-head { grid-template-columns: 1fr; gap: 0.5rem; }
  .plate-folio { position: static !important; }
}
.plate-folio {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  color: var(--ink-3);
  border-top: 2px solid var(--ink);
  padding-top: 0.5rem;
  position: sticky;
  top: 56px;
}
.plate-folio .num {
  font-family: var(--f-serif);
  font-style: italic;
  font-size: 1.9rem;
  color: var(--ink);
  display: block;
  line-height: 1;
  margin-bottom: 0.25rem;
}
.plate-title {
  font-size: var(--s-h1);
  margin: 0.25rem 0 0.55rem;
}
.plate-sub {
  font-size: clamp(1rem, 0.95rem + 0.22vw, 1.12rem);
  color: var(--ink-2);
  max-width: 64ch;
}
.plate-body {
  display: grid;
  grid-template-columns: 230px 1fr;
  gap: var(--gap);
}
.plate-body > * { min-width: 0; max-width: 100%; }
@media (max-width: 900px) {
  .plate-body { grid-template-columns: 1fr; }
}
.marginalia {
  font-size: var(--s-small);
  color: var(--ink-3);
  border-top: 1px solid var(--rule-hair);
  padding-top: 0.75rem;
  line-height: 1.5;
  min-width: 0;
  max-width: 100%;
}
.marginalia > strong:first-child,
.marginalia div > strong:first-child {
  font-family: var(--f-mono);
  font-size: 0.70rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-2);
  display: block;
  margin-bottom: 0.3rem;
}
.marginalia cite {
  font-style: normal;
  font-family: var(--f-mono);
  font-size: 0.71rem;
  color: var(--accent-text);
  display: block;
  margin-top: 0.4rem;
}

/* Instrument frame, `.derived` callout, `.counterpoint` */
.instrument {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: clamp(1rem, 2.2vw, 1.75rem);
  position: relative;
  min-width: 0;
  max-width: 100%;
}
.instrument-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
  padding-bottom: 0.75rem;
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--rule-hair);
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  color: var(--ink-3);
}
.derived {
  margin-top: 1rem;
  padding: 0.9rem 1.1rem;
  background: var(--ink);
  color: var(--paper);
  font-family: var(--f-mono);
  font-size: var(--s-small);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  border-radius: 2px;
}
.derived .d-main { color: var(--paper); line-height: 1.45; }
.derived .d-main em {
  font-family: var(--f-serif);
  font-style: italic;
  color: #E8C3A4;
  font-size: 1.06em;
}
.derived .d-sub { font-size: 0.72rem; opacity: 0.78; }

.counterpoint {
  margin-top: 1.15rem;
  padding: 0.85rem 1.1rem;
  border-left: 3px solid var(--accent);
  background: color-mix(in oklab, var(--surface) 65%, var(--paper));
  font-size: var(--s-small);
  color: var(--ink-2);
}
.counterpoint .cp-head {
  font-family: var(--f-mono);
  font-size: 0.70rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent-text);
  margin-bottom: 0.25rem;
  display: flex;
  align-items: center;
  gap: 6px;
}

/* ============================================================================
 * 5. PLATE I: ARCHITECTURE PIPELINE RAIL
 * ============================================================================ */
.pipe-rail {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  margin-bottom: 1.2rem;
}
.pipe-rail > * { min-width: 0; max-width: 100%; }
@media (max-width: 820px) {
  .pipe-rail { grid-template-columns: 1fr; }
}
.pipe-node {
  appearance: none;
  text-align: left;
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.85rem 0.9rem;
  cursor: pointer;
  font: inherit;
  color: var(--ink);
  position: relative;
  transition: transform 0.12s ease, border-color 0.12s ease;
}
.pipe-node:hover { border-color: var(--accent); transform: translateY(-1px); }
.pipe-node[aria-selected="true"] {
  background: var(--surface);
  border-color: var(--ink);
  box-shadow: inset 0 3px 0 var(--accent);
}
.pipe-node .p-num {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  color: var(--ink-3);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  display: flex;
  justify-content: space-between;
}
.pipe-node .p-name {
  font-family: var(--f-serif);
  font-size: 1.08rem;
  margin: 0.22rem 0 0.2rem;
  display: block;
}
.pipe-node .p-gate {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  color: var(--accent-text);
}
.pipe-inspector {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1.15rem;
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 1.25rem;
}
.pipe-inspector > * { min-width: 0; max-width: 100%; }
@media (max-width: 820px) {
  .pipe-inspector { grid-template-columns: 1fr; }
}

/* ============================================================================
 * 6. PLATE II: GEMINI NOTEBOOK GLUING STUDIO
 * ============================================================================ */
.studio-split {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 1.15rem;
  align-items: start;
}
.studio-split > * { min-width: 0; max-width: 100%; }
@media (max-width: 960px) {
  .studio-split { grid-template-columns: 1fr; }
}
.cover-panel {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.9rem;
  max-height: 760px;
  overflow-y: auto;
  min-width: 0;
  max-width: 100%;
}
.cover-stat-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px;
  margin: 0.55rem 0 0.75rem;
}
.cover-stat {
  background: var(--paper-soft);
  border: 1px solid var(--rule-hair);
  padding: 6px;
  text-align: center;
}
.cover-stat .v {
  font-family: var(--f-serif);
  font-size: 1.25rem;
  color: var(--accent-text);
  line-height: 1.1;
}
.cover-stat .k {
  font-family: var(--f-mono);
  font-size: 0.64rem;
  color: var(--ink-3);
  text-transform: uppercase;
}
.preset-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 0.75rem;
}
.preset-btn {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  padding: 5px 9px;
  min-height: 29px;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  cursor: pointer;
  border-radius: 2px;
  display: inline-flex;
  align-items: center;
}
.preset-btn:hover, .preset-btn.active {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}
.stalk-item {
  display: flex;
  align-items: flex-start;
  gap: 7px;
  padding: 6px 7px;
  border: 1px solid transparent;
  border-bottom: 1px dotted var(--rule-hair);
  cursor: pointer;
  font-size: 0.83rem;
}
.stalk-item:hover { background: var(--paper-soft); }
.stalk-item.in-cover {
  background: rgba(166, 119, 86, 0.11);
  border-color: rgba(166, 119, 86, 0.35);
}
.stalk-item.focused {
  box-shadow: inset 3px 0 0 var(--accent-text);
}
.stalk-check {
  width: 14px;
  height: 14px;
  border: 1px solid var(--ink-3);
  border-radius: 2px;
  margin-top: 2px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--f-mono);
  font-size: 10px;
}
.stalk-item.in-cover .stalk-check {
  background: var(--accent-text);
  border-color: var(--accent-text);
  color: var(--paper);
}

.notebook-main {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1.15rem;
  min-width: 0;
  max-width: 100%;
  overflow-x: hidden;
}
.query-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 0.85rem;
}
.query-input {
  flex: 1;
  min-width: 0;
  max-width: 100%;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: 9px 12px;
  font-family: var(--f-sans);
  font-size: 0.92rem;
  color: var(--ink);
  border-radius: 2px;
}
.query-input:focus { outline: 1px solid var(--accent); background: var(--paper); }
.btn-copper {
  background: var(--ink);
  color: var(--paper);
  border: 1px solid var(--ink);
  font-family: var(--f-mono);
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 8px 14px;
  min-height: 32px;
  cursor: pointer;
  border-radius: 2px;
}
.btn-copper:hover { background: var(--accent-text); border-color: var(--accent-text); }

.inv-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 1rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--rule-hair);
}
.inv-pill {
  font-family: var(--f-mono);
  font-size: 0.71rem;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  padding: 6px 10px;
  min-height: 30px;
  border-radius: 2px;
  cursor: pointer;
  text-align: left;
}
.inv-pill:hover { border-color: var(--accent); color: var(--ink); }
.inv-pill.active {
  background: var(--surface);
  border-color: var(--accent-text);
  color: var(--ink);
  font-weight: 600;
}

.gluing-banner {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  border-left: 3px solid var(--good);
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.synthesis-prose { min-width: 0; max-width: 100%; overflow-wrap: break-word; }
.synthesis-prose h2, .synthesis-prose h3 {
  font-size: 1.25rem;
  margin: 0.8rem 0 0.5rem;
  color: var(--ink);
}
.synthesis-prose h4 {
  font-family: var(--f-mono);
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  color: var(--accent-text);
  margin: 1.1rem 0 0.45rem;
  border-bottom: 1px solid var(--rule-hair);
  padding-bottom: 3px;
}
.synthesis-prose ul {
  margin: 0.4rem 0 0.9rem 1.2rem;
  padding: 0;
  color: var(--ink-2);
}
.synthesis-prose li { margin-bottom: 0.45rem; }

/* ============================================================================
 * 7. PLATE III: INTERACTIVE SYMBOLIC SANDBOX ("Category Theory Illustrated")
 * ============================================================================ */
.sym-selector {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 7px;
  margin-bottom: 1.1rem;
}
.sym-selector > * { min-width: 0; max-width: 100%; }
@media (max-width: 860px) {
  .sym-selector { grid-template-columns: repeat(2, 1fr); }
}
.sym-btn {
  appearance: none;
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.65rem 0.75rem;
  text-align: left;
  cursor: pointer;
  color: var(--ink);
  transition: border-color 0.12s;
}
.sym-btn:hover { border-color: var(--accent); }
.sym-btn[aria-selected="true"] {
  background: var(--surface);
  border-color: var(--ink);
  box-shadow: inset 0 3px 0 var(--ax-art);
}
.sym-btn .s-glyph {
  font-family: var(--f-math);
  font-size: 1.15rem;
  color: var(--accent-text);
  display: block;
}
.sym-btn .s-title {
  font-family: var(--f-mono);
  font-size: 0.70rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--ink-2);
}

.sym-stage {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1.15rem;
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 1.2rem;
  align-items: start;
}
.sym-stage > * { min-width: 0; max-width: 100%; }
@media (max-width: 900px) {
  .sym-stage { grid-template-columns: 1fr; }
}
.token-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 0.75rem 0;
}
.token-chip {
  font-family: var(--f-math);
  font-size: 0.95rem;
  padding: 5px 10px;
  min-height: 30px;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  border-radius: 2px;
  cursor: pointer;
  color: var(--ink);
}
.token-chip:hover, .token-chip.active {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}

/* ============================================================================
 * 8. PLATE IV: STALKS CATALOGUE, 877 DECLARATIONS & 3D POSET CANVAS
 * ============================================================================ */
.subview-tabs {
  display: inline-flex;
  flex-wrap: wrap;
  border: 1px solid var(--rule);
  background: var(--paper);
  margin-bottom: 1rem;
}
.subview-tab {
  appearance: none;
  border: 0;
  background: transparent;
  padding: 6px 13px;
  min-height: 30px;
  font-family: var(--f-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--ink-2);
  cursor: pointer;
  border-right: 1px solid var(--rule);
}
.subview-tab:last-child { border-right: 0; }
.subview-tab[aria-selected="true"] {
  background: var(--ink);
  color: var(--paper);
}
.stalk-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 0.9rem;
}
.stalk-cards-grid > * { min-width: 0; max-width: 100%; }
.stalk-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.95rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-width: 0;
  max-width: 100%;
}
.stalk-card:hover { border-color: var(--accent); }

.canvas-frame {
  background: #161310;
  border: 1px solid var(--rule);
  height: 480px;
  position: relative;
  overflow: hidden;
}
#sheaf3dCanvas {
  width: 100%;
  height: 100%;
  display: block;
  cursor: grab;
}
#sheaf3dCanvas:active { cursor: grabbing; }

/* ============================================================================
 * 9. PLATE V: COURSE BLUEPRINT ("Category Theory Illustrated: Through Symbols")
 * ============================================================================ */
.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 0.95rem;
  margin-top: 1rem;
}
.course-grid > * { min-width: 0; max-width: 100%; }
.module-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1rem 1.1rem;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  min-width: 0;
  max-width: 100%;
}
.module-card .m-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--rule-hair);
  padding-bottom: 0.45rem;
}
.callout-box {
  padding: 0.55rem 0.75rem;
  background: var(--paper-soft);
  border-left: 2px solid var(--accent);
  font-size: 0.83rem;
}
.callout-box strong {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--accent-text);
  display: block;
}

/* ============================================================================
 * 10. SLIDE-OVER 609-PAGE VERBATIM PDF READER DRAWER
 * ============================================================================ */
.reader-drawer {
  position: fixed;
  top: 0;
  right: 0;
  width: min(500px, 94vw);
  height: 100vh;
  background: var(--paper);
  border-left: 2px solid var(--ink);
  box-shadow: -12px 0 36px rgba(0,0,0,0.22);
  z-index: 95;
  transform: translateX(102%);
  transition: transform 0.22s ease;
  display: flex;
  flex-direction: column;
}
.reader-drawer.open { transform: translateX(0); }
.reader-head {
  padding: 0.9rem 1.1rem;
  background: var(--paper-soft);
  border-bottom: 1px solid var(--rule);
}
.reader-body {
  padding: 1rem 1.1rem;
  overflow-y: auto;
  flex: 1;
}
#readerPageMeta .stamp {
  white-space: normal;
  max-width: 100%;
  line-height: 1.3;
}
.verbatim-sheet {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: 1rem;
  font-family: var(--f-serif);
  font-size: 0.91rem;
  line-height: 1.65;
  white-space: pre-wrap;
  overflow-wrap: break-word;
  color: var(--ink);
}
mark.hl {
  background: rgba(166, 119, 86, 0.32);
  color: var(--ink);
  padding: 0 2px;
}

/* ============================================================================
 * 11. SIMPLIFIED FOCUS MODE, 4-ACT PODCAST & MOBILE-FIRST ERGONOMICS
 * ============================================================================ */
html[data-view-mode="focus"] section.plate { display: none; }
html[data-view-mode="focus"] section.plate.active-plate { display: block; animation: fadePlate 0.18s ease-out; }
@keyframes fadePlate { from { opacity: 0.4; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

.plate-focus-bar {
  display: none;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--ink);
  padding: 0.55rem 0.9rem;
  margin-top: 1.25rem;
  font-family: var(--f-mono);
  font-size: 0.75rem;
}
html[data-view-mode="focus"] .plate-focus-bar { display: flex; }

.podcast-act-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 5px;
  margin: 0.55rem 0;
}
.podcast-act-step {
  padding: 6px 8px;
  min-height: 30px;
  background: var(--paper);
  border: 1px solid var(--rule);
  font-family: var(--f-mono);
  font-size: 0.66rem;
  color: var(--ink-3);
  cursor: pointer;
  text-align: left;
  border-radius: 2px;
  transition: all 0.15s;
}
.podcast-act-step.active {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
  font-weight: 600;
}
.podcast-visual-cue {
  margin-top: 0.45rem;
  padding: 0.45rem 0.7rem;
  background: rgba(59, 110, 143, 0.10);
  border-left: 3px solid var(--ax-technology);
  font-family: var(--f-mono);
  font-size: 0.73rem;
  color: var(--ink);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.mobile-cover-toggle {
  display: none;
  width: 100%;
  padding: 9px 12px;
  min-height: 36px;
  background: var(--surface);
  border: 1px solid var(--ink);
  font-family: var(--f-mono);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--ink);
  text-align: left;
  cursor: pointer;
  margin-bottom: 0.55rem;
  justify-content: space-between;
  align-items: center;
}
.mobile-bottom-dock {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 88;
  background: color-mix(in oklab, var(--paper) 96%, transparent);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-top: 1.5px solid var(--ink);
  padding: 6px 8px calc(6px + env(safe-area-inset-bottom, 0px));
  grid-template-columns: repeat(4, 1fr);
  gap: 5px;
  box-shadow: 0 -6px 20px rgba(0,0,0,0.14);
}
.mobile-dock-btn {
  appearance: none;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  border-radius: 3px;
  padding: 7px 4px;
  min-height: 34px;
  font-family: var(--f-mono);
  font-size: 0.66rem;
  font-weight: 600;
  color: var(--ink);
  text-align: center;
  cursor: pointer;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mobile-dock-btn.active {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}

@media (max-width: 860px) {
  .sym-selector {
    display: flex !important;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    padding-bottom: 6px;
    gap: 6px;
  }
  .sym-selector .sym-btn {
    flex: 0 0 215px;
    scroll-snap-align: start;
  }
  .podcast-act-bar { grid-template-columns: repeat(2, 1fr); }
  .mobile-cover-toggle { display: flex; }
  .cover-panel.mobile-collapsed { display: none; }
}

@media (max-width: 720px) {
  body { padding-bottom: 68px; }
  .axis-ribbon-inner {
    padding: 5px 10px;
    gap: 4px;
    flex-wrap: nowrap;
    justify-content: space-between;
  }
  .brand-mark { gap: 6px; min-width: 0; flex: 0 1 auto; }
  .brand-mark span:last-child {
    font-size: 0.62rem;
    max-width: 118px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .plate-nav { display: none; }
  .field-controls {
    width: auto;
    flex-wrap: nowrap;
    gap: 4px;
    overflow-x: auto;
  }
  .ctrl-label { display: none; }
  .ctrl-btn { padding: 4px 6px; font-size: 0.63rem; min-height: 28px; white-space: nowrap; }
  #openReaderBtn { display: none; }
  .query-bar { flex-direction: column; }
  .query-bar .btn-copper { width: 100%; padding: 9px; }
  .mobile-bottom-dock { display: grid; }
}
</style>
</head>
<body>

<!-- ==========================================================================
     STICKY AXIS RIBBON & FIELD CONTROLS
     ========================================================================== -->
<div class="axis-ribbon" role="navigation" aria-label="Field Manual Controls">
  <div class="axis-ribbon-inner">
    <div class="brand-mark">
      <span class="dot"></span>
      <span>CETI · SHEAF FIELD MANUAL · SPIVAK (609 PP.)</span>
    </div>

    <nav class="plate-nav" aria-label="Plates">
      <a href="#plate-1" data-plate-link="plate-1">I · Architecture</a>
      <a href="#plate-2" data-plate-link="plate-2">II · Notebook Studio</a>
      <a href="#plate-3" data-plate-link="plate-3">III · Symbolic Sandbox</a>
      <a href="#plate-4" data-plate-link="plate-4">IV · 30 Stalks &amp; Atlas</a>
      <a href="#plate-5" data-plate-link="plate-5">V · Course Blueprint</a>
    </nav>

    <div class="field-controls">
      <div class="ctrl-group" role="group" aria-label="View mode">
        <span class="ctrl-label">View</span>
        <button class="ctrl-btn" data-set-view="all" aria-pressed="true" title="Scroll all 5 editorial plates">All 5</button>
        <button class="ctrl-btn" data-set-view="focus" aria-pressed="false" title="Calm single-plate focus mode">1-Plate Focus</button>
      </div>
      <div class="ctrl-group" role="group" aria-label="Reading depth">
        <span class="ctrl-label">Depth</span>
        <button class="ctrl-btn" data-set-level="newcomer" aria-pressed="false">Newcomer</button>
        <button class="ctrl-btn" data-set-level="practitioner" aria-pressed="true">Practitioner</button>
        <button class="ctrl-btn" data-set-level="expert" aria-pressed="false">Expert</button>
      </div>
      <div class="ctrl-group" role="group" aria-label="Paper theme">
        <span class="ctrl-label">Paper</span>
        <button class="ctrl-btn" data-set-theme="light" aria-pressed="true">Cream</button>
        <button class="ctrl-btn" data-set-theme="dark" aria-pressed="false">Ink</button>
      </div>
      <button class="drawer-toggle-btn" id="openReaderBtn" title="Open 609-Page Verbatim Book Reader">
        📖 Page Reader (p.520)
      </button>
    </div>
  </div>
</div>

<div class="page-wrap">

  <!-- ========================================================================
       FRONTISPIECE
       ======================================================================== -->
  <header class="frontispiece">
    <div class="eyebrow">
      <span>FIELD MANUAL &amp; SHEAF KNOWLEDGE BASE · VOL I–V COMBINED EDITION</span>
      <span class="stamp ratified">◆ ratified corpus</span>
      <span class="stamp measured">⚖ 609 pp · 877 declarations</span>
    </div>

    <div class="frontispiece-grid">
      <div>
        <h1 class="hero-title">
          The <em class="u-copper">Sheaf</em> of Ologged Concepts, written down.
        </h1>
        <p class="hero-lede">
          Rather than flattening David I. Spivak’s <em>Category Theory for the Sciences</em> into an unstructured vector soup, this studio indexes all <strong>609 pages</strong> and <strong>877 formal declarations</strong> as an <abbr data-gloss="An Alexandrov topology on a poset X^op where open sets U are downward-closed concept neighborhoods.">Alexandrov topology</abbr> <span class="math-expr"><span class="m-cal">O</span> : <span class="m-op">Open</span>(<span class="m-cal">X</span>)<sup>op</sup> &rarr; <span class="m-cat">Sch</span> &simeq; <span class="m-cat">Cat</span></span>. Every query selects an open cover <span class="math-expr"><span class="m-cal">U</span> = {U<sub>i</sub>}</span>, audits restriction morphisms <span class="math-expr">&rho;<sub>U,V</sub></span> on pairwise overlaps, and glues local sections into a global categorical synthesis.
        </p>
      </div>

      <figure class="hero-figure" style="margin:0">
        <svg viewBox="0 0 420 205" width="100%" height="auto" role="img" aria-label="Sheaf Equalizer Gluing Diagram">
          <defs>
            <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="currentColor"/>
            </marker>
          </defs>
          <!-- Open cover circles -->
          <ellipse cx="115" cy="105" rx="76" ry="56" fill="rgba(166,119,86,0.12)" stroke="#A67756" stroke-width="1.4"/>
          <ellipse cx="195" cy="105" rx="76" ry="56" fill="rgba(59,110,143,0.12)" stroke="#3B6E8F" stroke-width="1.4"/>
          <text x="72" y="68" font-family="JetBrains Mono, monospace" font-size="10" fill="#8C4A2E">O(U) Stalk</text>
          <text x="206" y="68" font-family="JetBrains Mono, monospace" font-size="10" fill="#3B6E8F">O(V) Stalk</text>
          <text x="129" y="108" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="12" fill="#1A1612">O(U &cap; V)</text>
          <!-- Restriction arrows -->
          <path d="M 96 105 L 124 105" stroke="#8C4A2E" stroke-width="1.5" marker-end="url(#arr-ink)"/>
          <path d="M 214 105 L 186 105" stroke="#3B6E8F" stroke-width="1.5" marker-end="url(#arr-ink)"/>
          <!-- Gluing arrow to global section -->
          <path d="M 276 105 L 318 105" stroke="#3F5E39" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arr-ink)"/>
          <rect x="324" y="66" width="84" height="78" rx="3" fill="rgba(121,144,112,0.15)" stroke="#3F5E39" stroke-width="1.5"/>
          <text x="366" y="95" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-style="italic" font-size="13" fill="#1A1612">O(U &cup; V)</text>
          <text x="366" y="114" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#3F5E39">Glued Global</text>
          <text x="366" y="127" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#3F5E39">Section ◆</text>
        </svg>
        <figcaption>
          <span>FIG 0.1 · SHEAF EQUALIZER CONDITION (SPIVAK §7.2.2.2, P.520)</span>
          <span>O(U&cup;V) &cong; O(U) &times;<sub>O(U&cap;V)</sub> O(V)</span>
        </figcaption>
      </figure>
    </div>

    <dl class="frontispiece-meta">
      <div><dt>Primary Corpus</dt><dd>David I. Spivak · MIT Press (609 pp.)</dd></div>
      <div><dt>Indexed Topology</dt><dd>30 Stalks · 52 Morphisms · 8 2-Simplices</dd></div>
      <div><dt>Extracted Items</dt><dd>877 Formal Definitions / Theorems / Ologs</dd></div>
      <div><dt>Query Engine</dt><dd>SQLite FTS5 + Alexandrov Gluing + Gemini/MCP</dd></div>
      <div><dt>Course Target</dt><dd>Category Theory Illustrated · Through Symbols</dd></div>
    </dl>
  </header>

  <nav class="toc" aria-label="Table of Plates">
    <a href="#plate-1"><span><span class="toc-num">I.</span>Query &amp; Sheaf Architecture</span><span class="ax-tag ax-technology">tech</span></a>
    <a href="#plate-2"><span><span class="toc-num">II.</span>Gemini Notebook Gluing Studio</span><span class="ax-tag ax-research">research</span></a>
    <a href="#plate-3"><span><span class="toc-num">III.</span>Symbolic Visual Sandbox</span><span class="ax-tag ax-art">art</span></a>
    <a href="#plate-4"><span><span class="toc-num">IV.</span>30 Stalks, 877 Items &amp; 3D Poset</span><span class="ax-tag ax-science">science</span></a>
    <a href="#plate-5"><span><span class="toc-num">V.</span>Course Blueprint: Through Symbols</span><span class="ax-tag ax-teaching">teaching</span></a>
  </nav>

  <!-- ========================================================================
       PLATE I · QUERY & SHEAF GLUING ARCHITECTURE
       Answers: "Is it using a Gemini Notebook MCP or what's the structure?"
       ======================================================================== -->
  <section class="plate" id="plate-1" data-axis="technology">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate I</span>
        <div>QUERY ARCHITECTURE</div>
        <div style="margin-top:6px"><span class="ax-tag ax-technology">technology</span></div>
        <div style="margin-top:6px"><span class="stamp measured">⚖ SQLite FTS5 + Sheaf</span></div>
      </div>
      <div>
        <div class="eyebrow">HOW QUERIES WORK · LOCAL DETERMINISTIC SHEAF GLUING + OPTIONAL GEMINI / MCP BRIDGE</div>
        <h2 class="plate-title">A query is a <em class="u-copper">pullback</em> across an open cover, not a flat cosine search.</h2>
        <p class="plate-sub">
          You asked how the query pipeline is structured and whether it uses a Gemini Notebook MCP. Here is the exact 5-stage architecture on disk: it runs <strong>100% locally and deterministically in under 2ms</strong> using an indexed SQLite FTS5 + Alexandrov Sheaf Open-Cover engine, and includes a CLI/MCP bridge (<code class="inline-code">query_sheaf.py</code>) that can be invoked as a local MCP server or piped to <code class="inline-code">gemini-2.5-flash</code>.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Architectural Honesty</strong>
        Standard RAG chunks a PDF into arbitrary 500-token windows and averages embeddings, destroying commutative diagrams and universal properties.
        <br><br>
        In our sheaf architecture, every page belongs to a formal stalk <span class="math-expr">U<sub>i</sub></span>, and two stalks can only be synthesized together if their restriction morphisms <span class="math-expr">&rho;<sub>U, U&cap;V</sub></span> agree on shared definitions.
        <cite>— Spivak §7.2.2, p.518–524 · build_sheaf_kb.py</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT I · SHEAF QUERY &amp; GLUING PIPELINE (CLICK ANY STAGE TO INSPECT)</span>
            <span class="stamp ratified">◆ 5 deterministic stages</span>
          </div>

          <div class="pipe-rail" role="tablist" aria-label="Query pipeline stages" id="pipeRail">
            <button class="pipe-node" role="tab" aria-selected="true" data-stage="0">
              <span class="p-num"><span>STAGE 01</span><span>⚖ 609 pp</span></span>
              <span class="p-name">Corpus &amp; FTS5</span>
              <span class="p-gate">cattheory_sheaf.db</span>
            </button>
            <button class="pipe-node" role="tab" aria-selected="false" data-stage="1">
              <span class="p-num"><span>STAGE 02</span><span>◆ 30 stalks</span></span>
              <span class="p-name">Alexandrov Cover</span>
              <span class="p-gate">U &sube; Open(Alx(X<sup>op</sup>))</span>
            </button>
            <button class="pipe-node" role="tab" aria-selected="false" data-stage="2">
              <span class="p-num"><span>STAGE 03</span><span>◆ 52 arrows</span></span>
              <span class="p-name">Restriction Audit</span>
              <span class="p-gate">&rho;<sub>U,V</sub> : O(U) &rarr; O(V)</span>
            </button>
            <button class="pipe-node" role="tab" aria-selected="false" data-stage="3">
              <span class="p-num"><span>STAGE 04</span><span>◆ 8 simplices</span></span>
              <span class="p-name">Equalizer Gluing</span>
              <span class="p-gate">O(U) &times;<sub>O(U&cap;V)</sub> O(V)</span>
            </button>
            <button class="pipe-node" role="tab" aria-selected="false" data-stage="4">
              <span class="p-num"><span>STAGE 05</span><span>✓ MCP / API</span></span>
              <span class="p-name">Gemini / MCP Bridge</span>
              <span class="p-gate">query_sheaf.py</span>
            </button>
          </div>

          <div class="pipe-inspector" id="pipeInspector"></div>

          <div class="derived" id="pipeDerived">
            <div class="d-main">
              <strong>Live Pipeline Invariant:</strong> <em id="pipeDerivedTitle">Stage 01 · Verbatim Extraction</em> — <span id="pipeDerivedBody">609 pages, 96 sections, and 877 formal numbered declarations indexed in SQLite FTS5 (`cattheory_sheaf.db`) + deferred browser bundle (`sheaf_pages_bundle.js`).</span>
            </div>
            <div class="d-sub">0 hallucinations · every claim cites [p. N]</div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Where Local Deterministic Sheaf Gluing Breaks</span></div>
          <div>
            The in-browser studio performs <strong>exact structural sheaf gluing</strong> (computing the open cover, verifying restriction morphisms <span class="math-expr">&rho;<sub>U,V</sub></span>, assembling the fiber-product Olog, and retrieving verbatim formal items) without needing an external network call. However, if you ask an open-ended cross-domain question outside the 5 pre-synthesized investigations (e.g., <em>"Design a sheaf-theoretic schema migration for a Kubernetes cluster"</em>), local FTS5 + stalk gluing gives you the exact mathematical building blocks and page citations, while full prose synthesis uses <code class="inline-code">GEMINI_API_KEY=... python3 cattheory-sheaf-kb/query_sheaf.py --ask "..."</code>.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE II · THE GEMINI NOTEBOOK GLUING STUDIO
       Interactive Open Cover Selector + Glued Investigations + Olog Diagram
       ======================================================================== -->
  <section class="plate" id="plate-2" data-axis="research">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate II</span>
        <div>NOTEBOOK STUDIO</div>
        <div style="margin-top:6px"><span class="ax-tag ax-research">research</span></div>
        <div style="margin-top:6px"><span class="stamp ratified">◆ Open-Cover Gluing</span></div>
      </div>
      <div>
        <div class="eyebrow">SHEAF-INDEXED GEMINI NOTEBOOK · SELECT OPEN COVER <span class="math-expr"><span class="m-cal">U</span> &sube; <span class="m-op">Open</span>(<span class="m-cal">X</span>)</span></div>
        <h2 class="plate-title">Every notebook synthesis is a <em class="u-copper">global</em> section glued over your chosen stalks.</h2>
        <p class="plate-sub">
          Toggle concept stalks in the left Open Cover <span class="math-expr"><span class="m-cal">U</span></span>, choose a preset investigation or type any mathematical query, and inspect the resulting <strong>Sheaf Gluing Audit</strong>, typeset mathematical synthesis, and interactive <strong>Commutative Olog Diagram</strong>. Click any <span class="cite-pill">§ p.520</span> badge to inspect the verbatim page in the slide-over reader.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>The Sheaf Gluing Axiom</strong>
        Given an open cover <span class="math-expr"><span class="m-cal">U</span> = {U<sub>i</sub>}<sub>i&isin;I</sub></span> of <span class="math-expr">U</span>, a family of local sections <span class="math-expr">s<sub>i</sub> &isin; <span class="m-cal">O</span>(U<sub>i</sub>)</span> glues to a unique global section <span class="math-expr">s &isin; <span class="m-cal">O</span>(U)</span> iff for every pair <span class="math-expr">(i,j)</span>:
        <div class="math-display" style="font-size:0.88rem;padding:0.45rem;margin:0.5rem 0">
          &rho;<sub>U<sub>i</sub>, U<sub>i</sub>&cap;U<sub>j</sub></sub>(s<sub>i</sub>) = &rho;<sub>U<sub>j</sub>, U<sub>i</sub>&cap;U<sub>j</sub></sub>(s<sub>j</sub>)
        </div>
        <cite>— Spivak, Definition 7.2.2.2 (p. 520)</cite>

        <div style="margin-top:1.2rem;padding-top:0.8rem;border-top:1px solid var(--rule-hair)">
          <strong>NotebookLM Deep Dive Podcast</strong>
          <p style="font-size:0.78rem;margin:0.3rem 0 0.6rem">Listen to a natural two-host neural conversation (<strong>Kore</strong> &amp; <strong>Puck</strong>) unpacking the active glued section:</p>
          <button class="btn-copper" id="audioBriefBtn" style="width:100%">🎙️ Play Deep Dive Podcast</button>
        </div>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT II · ALEXANDROV OPEN COVER <span class="math-expr"><span class="m-cal">U</span></span> &amp; GLOBAL SECTION SYNTHESIZER</span>
            <span class="stamp measured" id="coverGluingStamp">⚖ 5 stalks · 6 restrictions · Glued</span>
          </div>

          <button type="button" class="mobile-cover-toggle" id="mobileCoverToggleBtn" aria-expanded="false">
            <span>📂 Open Cover <span class="m-cal">U</span> Selector (<span id="mobileCoverCount">5</span> Stalks Active)</span>
            <span id="mobileCoverCaret">▾ Show</span>
          </button>

          <div class="studio-split">
            <!-- Left column: Open Cover Selector -->
            <div class="cover-panel mobile-collapsed" id="coverPanelDrawer">
              <div style="display:flex;justify-content:space-between;align-items:center">
                <span class="mono" style="font-weight:600;text-transform:uppercase;letter-spacing:0.06em">Open Cover <span class="m-cal">U</span></span>
                <button class="preset-btn" id="clearCoverBtn">Reset</button>
              </div>

              <div class="cover-stat-row">
                <div class="cover-stat"><div class="v" id="metricStalks">5</div><div class="k">Stalks |U|</div></div>
                <div class="cover-stat"><div class="v" id="metricOverlaps">6</div><div class="k">Arrows &rho;</div></div>
                <div class="cover-stat"><div class="v" id="metricPages">188</div><div class="k">Pages</div></div>
              </div>

              <div class="preset-bar">
                <button class="preset-btn active" data-preset="sheaf">Sheaf Topos</button>
                <button class="preset-btn" data-preset="data">Functorial DB</button>
                <button class="preset-btn" data-preset="universal">Universal Limits</button>
                <button class="preset-btn" data-preset="monad">Monads &amp; Operads</button>
                <button class="preset-btn" data-preset="obstruction" style="border-color:var(--bad);color:var(--bad)">⊘ Test H¹ Fail</button>
                <button class="preset-btn" data-preset="all">Full X (30)</button>
              </div>

              <input type="text" class="query-input" id="stalkFilterInput" placeholder="Filter 30 concept stalks…" style="width:100%;padding:6px 9px;font-size:0.80rem;margin-bottom:8px">

              <div id="stalkTreeList"></div>
            </div>

            <!-- Right column: Query Bar, Curated Investigations, Synthesis, Commutative Olog -->
            <div class="notebook-main">
              <div class="query-bar">
                <input type="text" class="query-input" id="notebookQueryInput" placeholder="Ask across the active open cover (e.g., How do Π and Σ migrate data?)…">
                <button class="btn-copper" id="runGlueQueryBtn">Glue Section ↵</button>
              </div>

              <div class="inv-pills" id="invPillsContainer"></div>

              <!-- NotebookLM Dual-Host Neural Audio Overview Studio Card -->
              <div id="podcastStudioCard" style="background:var(--paper-soft);border:1.5px solid var(--ink);padding:0.9rem 1.05rem;margin-bottom:1rem;box-shadow:3px 3px 0 rgba(26,22,18,0.08)">
                <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:0.65rem">
                  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
                    <span class="stamp ratified" id="podcastEngineBadge">◆ 4-Act 10-Turn Deep Dive</span>
                    <span class="mono" id="hostBadgeKore" style="padding:2px 8px;border:1px solid var(--accent-text);background:var(--accent-soft);color:var(--accent-text);font-weight:600;border-radius:2px;transition:all 0.2s">🎙️ Kore (Lead Architect)</span>
                    <span class="mono" id="hostBadgePuck" style="padding:2px 8px;border:1px solid var(--good);background:var(--good-soft);color:var(--good);font-weight:600;border-radius:2px;transition:all 0.2s">🎧 Puck (Systems Co-Host)</span>
                  </div>
                  <div style="display:flex;gap:6px;align-items:center">
                    <button class="preset-btn" id="podcastSpeedBtn" title="Toggle Playback Speed">1.0×</button>
                    <button class="preset-btn" id="toggleTranscriptBtn">10-Turn Script ▾</button>
                    <button class="preset-btn" id="toggleGeminiTtsConfigBtn" title="Configure Live Gemini 2.5 Native Multi-Speaker Voices (Kore, Puck, Aoede, Charon)">⚡ Gemini 2.5 Voices</button>
                  </div>
                </div>

                <!-- 4-Act Pedagogical Progress Stepper -->
                <div class="podcast-act-bar" id="podcastActBar" role="group" aria-label="4-Act Pedagogical Arc">
                  <button type="button" class="podcast-act-step active" data-act-idx="0">Act I · Visual Hook</button>
                  <button type="button" class="podcast-act-step" data-act-idx="1">Act II · Walk Diagram</button>
                  <button type="button" class="podcast-act-step" data-act-idx="2">Act III · Edge Cases</button>
                  <button type="button" class="podcast-act-step" data-act-idx="3">Act IV · Decode &amp; Lab</button>
                </div>

                <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
                  <button class="btn-copper" id="podcastPlayPauseBtn" style="padding:6px 14px;font-size:0.78rem;min-width:135px">▶ Play Deep Dive</button>
                  <span class="mono" id="podcastTimeLabel" style="min-width:78px;color:var(--ink-2);font-weight:600">0:00 / 2:55</span>
                  <input type="range" id="podcastScrubSlider" min="0" max="100" step="0.1" value="0" style="flex:1;min-width:120px;accent-color:var(--accent-text);cursor:pointer">
                  <div id="podcastWaveform" style="display:flex;align-items:flex-end;gap:2px;height:22px;padding:0 4px" aria-hidden="true">
                    <span style="width:3px;height:6px;background:var(--accent-text);transition:height 0.12s"></span>
                    <span style="width:3px;height:12px;background:var(--accent-text);transition:height 0.12s"></span>
                    <span style="width:3px;height:9px;background:var(--good);transition:height 0.12s"></span>
                    <span style="width:3px;height:16px;background:var(--accent-text);transition:height 0.12s"></span>
                    <span style="width:3px;height:10px;background:var(--good);transition:height 0.12s"></span>
                    <span style="width:3px;height:19px;background:var(--accent-text);transition:height 0.12s"></span>
                    <span style="width:3px;height:8px;background:var(--good);transition:height 0.12s"></span>
                    <span style="width:3px;height:14px;background:var(--accent-text);transition:height 0.12s"></span>
                    <span style="width:3px;height:7px;background:var(--good);transition:height 0.12s"></span>
                    <span style="width:3px;height:11px;background:var(--accent-text);transition:height 0.12s"></span>
                  </div>
                </div>

                <audio id="notebookPodcastAudio" preload="metadata" style="display:none"></audio>

                <!-- Live Visual Diagram Cue Banner -->
                <div class="podcast-visual-cue" id="podcastVisualCueBar">
                  <span id="podcastVisualCueText">👁️ <strong>Visual Cue:</strong> Select an investigation or press Play to walk the diagram step by step.</span>
                  <button type="button" class="cite-pill" id="podcastCuePageBtn" onclick="window.__jumpToPage(520, '')">§ p.520</button>
                </div>

                <!-- Active Turn Subtitle Bar -->
                <div id="podcastActiveSubtitle" style="margin-top:0.45rem;padding:0.55rem 0.75rem;background:var(--paper);border-left:3px solid var(--accent-text);font-size:0.86rem;line-height:1.45;color:var(--ink)">
                  <span class="mono" style="color:var(--accent-text);font-weight:600">Kore · Lead Architect:</span> Click <strong>▶ Play Deep Dive</strong> to listen to the 10-turn, 4-Act neural audio notebook for this investigation.
                </div>

                <!-- Expandable Synchronized Multi-Speaker Transcript -->
                <div id="podcastTranscriptDrawer" style="display:none;margin-top:0.65rem;max-height:260px;overflow-y:auto;background:var(--paper);border:1px solid var(--rule);padding:0.6rem;font-size:0.82rem"></div>

                <!-- Optional Live Gemini 2.5 Multi-Speaker TTS Generator Config -->
                <div id="geminiTtsConfigDrawer" style="display:none;margin-top:0.65rem;padding:0.7rem;background:var(--paper);border:1px dashed var(--accent-text);font-size:0.80rem">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;flex-wrap:wrap;gap:6px">
                    <span class="mono" style="font-weight:600;color:var(--accent-text)">LIVE GEMINI 2.5 FLASH TTS (`multiSpeakerVoiceConfig`)</span>
                    <span class="mono" style="color:var(--ink-3)">Pre-rendered neural MP3s play offline by default; add key to re-synthesize live</span>
                  </div>
                  <div style="display:flex;gap:6px;flex-wrap:wrap;align-items:center">
                    <input type="password" id="geminiApiKeyInput" class="query-input" placeholder="Paste GEMINI_API_KEY for live Gemini 2.5 TTS…" style="flex:1;min-width:180px;padding:4px 8px;font-size:0.78rem">
                    <select id="geminiVoicePairSelect" class="query-input" style="max-width:210px;padding:4px 8px;font-size:0.76rem">
                      <option value="Kore,Puck">Kore &amp; Puck (NotebookLM Default)</option>
                      <option value="Aoede,Charon">Aoede &amp; Charon (Warm Editorial)</option>
                      <option value="Kore,Fenrir">Kore &amp; Fenrir (Deep Studio)</option>
                    </select>
                    <button class="btn-copper" id="runLiveGeminiTtsBtn" style="padding:5px 10px;font-size:0.75rem">Synthesize Live 🎙️</button>
                  </div>
                  <div id="geminiTtsStatusMsg" class="mono" style="margin-top:4px;color:var(--ink-3)"></div>
                </div>
              </div>

              <div class="gluing-banner" id="gluingAuditBanner"></div>

              <div class="synthesis-prose" id="notebookSynthesisOutput"></div>

              <!-- Interactive Commutative Olog Diagram for Active Open Cover -->
              <div style="margin-top:1.4rem;padding-top:1rem;border-top:1px solid var(--rule)">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;flex-wrap:wrap;gap:8px">
                  <span class="mono" style="font-weight:600;text-transform:uppercase;color:var(--ink-2)">
                    Commutative Fiber-Product Olog · Glued Across Active Cover <span class="m-cal">U</span>
                  </span>
                  <span class="stamp ratified" id="ologSummaryBadge">◆ Commutes</span>
                </div>
                <div id="gluedOlogSvgWrap" style="background:var(--paper-soft);border:1px solid var(--rule);padding:0.75rem;overflow-x:auto"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Non-Gluing Covers &amp; Cohomological Obstructions (H¹ &ne; 0)</span></div>
          <div>
            Not every selection of stalks <span class="math-expr"><span class="m-cal">U</span> = {U<sub>i</sub>}</span> automatically glues into a single connected global section. If you select two distant stalks (for example, <em>Scientific Agreement</em> in Ch 1 and <em>Universal Colimits</em> in Ch 6) without including a bridging stalk in <span class="math-expr">U<sub>i</sub> &cap; U<sub>j</sub></span> (such as <em>Ologs</em> or <em>Categories &amp; Functors</em>), the restriction audit flags a <strong>Separated Cover</strong> (<span class="math-expr">&rho; = 0</span> on the missing overlap) and prompts you to add the mediating stalk rather than hallucinating an unsupported link.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE III · INTERACTIVE SYMBOLIC SANDBOX ("Category Theory Illustrated")
       ======================================================================== -->
  <section class="plate" id="plate-3" data-axis="art">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate III</span>
        <div>SYMBOLIC SANDBOX</div>
        <div style="margin-top:6px"><span class="ax-tag ax-art">art · visual</span></div>
        <div style="margin-top:6px"><span class="stamp ratified">◆ 8 Visual Primitives</span></div>
      </div>
      <div>
        <div class="eyebrow">CATEGORY THEORY ILLUSTRATED · UNDERSTANDING THROUGH SYMBOLS &amp; COMMUTING DIAGRAMS</div>
        <h2 class="plate-title">Every <em class="u-copper">symbol</em> is a spatial diagram compressed into a one-dimensional string.</h2>
        <p class="plate-sub">
          Mathematical notation feels opaque only when its symbols are divorced from the spatial gestures they encode. Select any of the <strong>8 core symbolic primitives</strong> below, click individual symbolic tokens (<span class="math-expr">&#8728;</span>, <span class="math-expr">&lang;f,g&rang;</span>, <span class="math-expr">&times;<sub>Z</sub></span>, <span class="math-expr">&#8867;</span>, <span class="math-expr">&rArr;</span>), and watch the symbol, the commuting diagram, and a concrete finite-set data trace illuminate in unison.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Pedagogical Law: Symbol &harr; Diagram Duality</strong>
        In Spivak’s text, every algebraic equation between morphisms (<span class="math-expr">g &#8728; f = k &#8728; h</span>) is literally a topological assertion that two directed paths in a diagram bound a 2-cell that <em>commutes</em>.
        <br><br>
        When learners can click a token inside a formula and see which arrow or universal cone it controls, symbolic fluency becomes visual intuition.
        <cite>— Spivak §2.1.2 (p. 74) &amp; §6.1.3 (p. 418)</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT III · SYMBOL-TO-DIAGRAM INTERACTIVE TRANSLATOR (SINGLE-MUTATOR)</span>
            <span class="stamp accept" id="symSpivakRef">✓ Spivak §2.1.2 · p.74</span>
          </div>

          <div class="sym-selector" role="tablist" id="symSelector">
            <button class="sym-btn" role="tab" aria-selected="true" data-sym="comp">
              <span class="s-glyph">g &#8728; f = h</span>
              <span class="s-title">1. Composition</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="prod">
              <span class="s-glyph">&lang;f, g&rang; : A &rarr; X&times;Y</span>
              <span class="s-title">2. Product</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="coprod">
              <span class="s-glyph">[f, g] : X&sqcup;Y &rarr; Z</span>
              <span class="s-title">3. Coproduct</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="pullback">
              <span class="s-glyph">X &times;<sub>Z</sub> Y</span>
              <span class="s-title">4. Pullback</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="pushout">
              <span class="s-glyph">X &sqcup;<sub>W</sub> Y</span>
              <span class="s-title">5. Pushout</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="nat">
              <span class="s-glyph">&alpha; : F &rArr; G</span>
              <span class="s-title">6. Naturality</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="adj">
              <span class="s-glyph">L &#8867; R</span>
              <span class="s-title">7. Adjunction</span>
            </button>
            <button class="sym-btn" role="tab" aria-selected="false" data-sym="sheaf">
              <span class="s-glyph">O(U&cup;V)</span>
              <span class="s-title">8. Sheaf Gluing</span>
            </button>
          </div>

          <div class="sym-stage">
            <div>
              <div class="mono" style="color:var(--ink-3);text-transform:uppercase;font-size:0.69rem">Click any symbolic token to highlight its geometric role:</div>
              <div class="token-strip" id="symTokenStrip"></div>
              <div id="symDiagramSvgWrap" style="background:var(--paper-soft);border:1px solid var(--rule);padding:0.75rem;min-height:250px;display:flex;align-items:center;justify-content:center"></div>
            </div>

            <div>
              <h3 class="serif" id="symTitle" style="font-size:1.35rem;margin-bottom:0.4rem"></h3>
              <div class="math-display" id="symFormulaDisplay" style="font-size:1.02rem;padding:0.65rem;margin:0.5rem 0"></div>

              <div class="callout-box" id="symTokenInspector" style="margin-bottom:0.75rem"></div>

              <p id="symExplanation" style="font-size:0.90rem;color:var(--ink-2);margin-bottom:0.75rem"></p>

              <div class="callout-box" style="border-left-color:var(--ax-science)">
                <strong>Why It Matters · Concrete Finite-Set Olog Trace</strong>
                <div id="symConcreteTrace" class="mono" style="font-size:0.75rem;margin-top:4px;color:var(--ink);white-space:pre-wrap"></div>
              </div>
            </div>
          </div>

          <div class="derived" id="symDerived">
            <div class="d-main" id="symDerivedText"></div>
            <div class="d-sub">Interactive Symbolic Primitive · Course Prototype</div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Directional Reading Trap (g &#8728; f vs. Path Order)</span></div>
          <div>
            Beginners frequently confuse algebraic composition order <span class="math-expr">g &#8728; f</span> (read right-to-left: "apply <span class="math-expr">f</span> first, then <span class="math-expr">g</span>") with diagrammatic path order <span class="math-expr">X &rarr;<sup>f</sup> Y &rarr;<sup>g</sup> Z</span> (drawn left-to-right). Spivak explicitly notes this notation tension in §2.1.2 (p. 47); our symbolic translator highlights the intermediate object <span class="math-expr">Y</span> when clicking <span class="math-expr">&#8728;</span> so learners anchor composition at the shared codomain/domain seam.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE IV · THE 30 CONCEPT STALKS, 877 FORMAL ITEMS & 3D POSET ATLAS
       ======================================================================== -->
  <section class="plate" id="plate-4" data-axis="science">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate IV</span>
        <div>CORPUS OBSERVED</div>
        <div style="margin-top:6px"><span class="ax-tag ax-science">science · corpus</span></div>
        <div style="margin-top:6px"><span class="stamp measured">⚖ 30 Stalks · 877 Items</span></div>
      </div>
      <div>
        <div class="eyebrow">VOL II ARCHETYPE · THE MEASURED CORPUS OF SPIVAK’S 609 PAGES</div>
        <h2 class="plate-title">Every stalk carries a local <em class="u-copper">olog</em>, restriction arrows, and verbatim declarations.</h2>
        <p class="plate-sub">
          Switch between the <strong>30 Concept Stalks Encyclopedia</strong> (with typeset mathematical cores, local Ologs, and restriction morphisms), the <strong>877 Formal Declarations Browser</strong> (every Definition, Theorem, Proposition, Example, Application, and Exercise), and the on-demand <strong>3D Alexandrov Poset Fiber Bundle</strong>.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Measured Distribution Across 7 Chapters</strong>
        • Ch 1 (Agreement): 1 stalk · 15 pp.<br>
        • Ch 2 (Sets/Ologs): 9 stalks · 82 pp.<br>
        • Ch 3 (Posets/Graphs): 5 stalks · 138 pp.<br>
        • Ch 4 (Categories/Functors): 7 stalks · 108 pp.<br>
        • Ch 5 (Monads/Operads): 3 stalks · 76 pp.<br>
        • Ch 6 (Universal/Limits): 2 stalks · 48 pp.<br>
        • Ch 7 (Adjunctions/Sheaves): 3 stalks · 115 pp.
        <cite>— Spivak Chapters 1–7 · Extracted by build_sheaf_kb.py</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <div class="subview-tabs" role="tablist" style="margin:0">
              <button class="subview-tab" role="tab" aria-selected="true" data-subview="stalks">30 Concept Stalks</button>
              <button class="subview-tab" role="tab" aria-selected="false" data-subview="declarations">877 Formal Declarations</button>
              <button class="subview-tab" role="tab" aria-selected="false" data-subview="atlas3d">3D Alexandrov Poset Atlas</button>
            </div>
            <div style="display:flex;gap:6px;align-items:center">
              <select id="chapterFilterSelect" class="query-input" style="padding:4px 8px;font-size:0.76rem">
                <option value="all">All 7 Chapters</option>
                <option value="1">Ch 1 · Science as Agreement</option>
                <option value="2">Ch 2 · Sets, Functions &amp; Ologs</option>
                <option value="3">Ch 3 · Monoids, Groups, Graphs &amp; Orders</option>
                <option value="4">Ch 4 · Categories, Functors &amp; Schemas</option>
                <option value="5">Ch 5 · Monads, Kleisli &amp; Operads</option>
                <option value="6">Ch 6 · Universal Limits &amp; Colimits</option>
                <option value="7">Ch 7 · Adjunctions, Migration &amp; Sheaves</option>
              </select>
            </div>
          </div>

          <!-- Subview A: 30 Concept Stalks -->
          <div id="subview-stalks">
            <div class="stalk-cards-grid" id="stalkCardsGrid"></div>
          </div>

          <!-- Subview B: 877 Formal Declarations -->
          <div id="subview-declarations" style="display:none">
            <div style="display:flex;gap:8px;margin-bottom:0.85rem;flex-wrap:wrap">
              <input type="text" id="declSearchInput" class="query-input" placeholder="Search 877 Definitions, Theorems, Propositions, Examples (e.g., '7.2.2.2', 'pullback', 'monad', 'Yoneda')…">
              <select id="declKindSelect" class="query-input" style="max-width:190px">
                <option value="all">All Kinds (877)</option>
                <option value="Definition">Definition</option>
                <option value="Theorem">Theorem</option>
                <option value="Proposition">Proposition</option>
                <option value="Example">Example</option>
                <option value="Application">Application</option>
                <option value="Remark">Remark</option>
                <option value="Exercise">Exercise</option>
              </select>
            </div>
            <div id="declCountLabel" class="mono" style="margin-bottom:0.6rem;color:var(--ink-3)"></div>
            <div id="declListContainer" style="display:flex;flex-direction:column;gap:8px;max-height:620px;overflow-y:auto"></div>
          </div>

          <!-- Subview C: 3D Alexandrov Poset Fiber Bundle -->
          <div id="subview-atlas3d" style="display:none">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;flex-wrap:wrap;gap:8px">
              <span class="mono" style="color:var(--ink-2)">Drag to orbit 3D Alexandrov Poset · Scroll to zoom · Click any stalk node to inspect</span>
              <div style="display:flex;gap:6px">
                <button class="preset-btn active" id="toggle2SimplicesBtn">2-Simplices: ON</button>
                <button class="preset-btn" id="reset3dCamBtn">Reset Camera</button>
              </div>
            </div>
            <div class="canvas-frame">
              <canvas id="sheaf3dCanvas"></canvas>
              <div id="hud3dBox" style="position:absolute;bottom:12px;left:12px;right:12px;background:rgba(26,22,18,0.92);color:#F5EFE3;padding:10px 14px;border:1px solid #A67756;font-size:0.82rem;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"></div>
            </div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Page-Granularity vs. Sub-Page Diagram Extraction</span></div>
          <div>
            While all 609 pages and 877 numbered declarations (`Definition`, `Theorem`, `Proposition`, `Example`, `Application`, `Exercise`) are indexed in full text, pure vector TikZ/XY-pic diagrams embedded inside the PDF stream do not carry full ASCII arrow coordinates in raw `pdftotext`. We bridge this gap by curating explicit typed `olog.types` and `olog.aspects` inside all 30 stalks and linking every page directly to the vector PDF via <code class="inline-code">Open PDF ↗</code>.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE V · COURSE BLUEPRINT ("Category Theory Illustrated: Through Symbols")
       ======================================================================== -->
  <section class="plate" id="plate-5" data-axis="teaching">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate V</span>
        <div>COURSE BLUEPRINT</div>
        <div style="margin-top:6px"><span class="ax-tag ax-teaching">teaching · scope</span></div>
        <div style="margin-top:6px"><span class="stamp accept">✓ Ready to Build</span></div>
      </div>
      <div>
        <div class="eyebrow">CURRICULUM ARCHITECTURE · CATEGORY THEORY ILLUSTRATED THROUGH SYMBOLS &amp; DIAGRAMS</div>
        <h2 class="plate-title">Scoping an interactive course where every <em class="u-copper">diagram</em> compiles into live symbols.</h2>
        <p class="plate-sub">
          Building on this Sheaf Knowledge Base and the CETI <code class="inline-code">meta-notebook</code> craft system, here is the complete architectural scope for our interactive visual course: <strong>7 self-contained visual modules</strong> (zero module numbers on learner surfaces per WebAge/FORGE rules), each pairing an interactive single-mutator symbolic instrument with concrete database/scientific Ologs and E2E walkable labs.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Courseware Non-Negotiables (FORGE / WebAge)</strong>
        • <strong>Self-Contained Surfaces:</strong> Never use "Module 1" or "Lab 2" on learner surfaces — cross-reference by descriptive title.<br>
        • <strong>Allowed Callouts Only:</strong> <code class="inline-code">Key Concept</code> and <code class="inline-code">Why It Matters</code> (never "So What" or stacked callouts).<br>
        • <strong>Teach-Not-Cover:</strong> Every symbol is enacted through a visual diagram + concrete finite-set trace before formal axioms.
        <cite>— AGENTS.md &amp; reviewer-qc-standard.md</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT V · INTERACTIVE CURRICULUM ARCHITECT &amp; SYMBOLIC GRAMMAR MAP</span>
            <span class="stamp ratified">◆ 7 Visual Modules · 5 Meta-Notebook Volumes</span>
          </div>

          <!-- Symbolic Grammar Table -->
          <div style="background:var(--paper);border:1px solid var(--rule);padding:1rem;margin-bottom:1.1rem;overflow-x:auto">
            <div class="mono" style="font-weight:600;text-transform:uppercase;color:var(--accent-text);margin-bottom:0.55rem">
              The Visual-Symbolic Grammar · How Every Symbol Is Taught Visually
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:0.84rem">
              <thead>
                <tr style="border-bottom:2px solid var(--ink);text-align:left;font-family:var(--f-mono);font-size:0.71rem;text-transform:uppercase;color:var(--ink-3)">
                  <th style="padding:6px 8px">Symbolic Token</th>
                  <th style="padding:6px 8px">Visual Gesture (SVG Primitive)</th>
                  <th style="padding:6px 8px">Concrete System / Data Analogue</th>
                  <th style="padding:6px 8px">Spivak Grounding</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px"><span class="math-expr">g &#8728; f : X &rarr; Z</span></td>
                  <td style="padding:7px 8px">Path concatenation + associative pipeline slider</td>
                  <td style="padding:7px 8px">Foreign-key join chain / pure function pipe</td>
                  <td style="padding:7px 8px"><button class="cite-pill" onclick="window.__jumpToPage(47,'olog')">§ p.47</button> <button class="cite-pill" onclick="window.__jumpToPage(74,'composition')">§ p.74</button></td>
                </tr>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px"><span class="math-expr">X &times;<sub>Z</sub> Y</span> &amp; <span class="math-expr">X &sqcup;<sub>W</sub> Y</span></td>
                  <td style="padding:7px 8px">Universal cone / cocone factorizer with dashed <span class="math-expr">&exist;! u</span> arrow</td>
                  <td style="padding:7px 8px"><code class="inline-code">INNER JOIN ... ON</code> vs. <code class="inline-code">FULL OUTER UNION</code></td>
                  <td style="padding:7px 8px"><button class="cite-pill" onclick="window.__jumpToPage(90,'pullback')">§ p.90</button> <button class="cite-pill" onclick="window.__jumpToPage(418,'limit')">§ p.418</button></td>
                </tr>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px"><span class="math-expr">F : <span class="m-cal">C</span> &rarr; <span class="m-cat">Set</span></span>, <span class="math-expr">&alpha; : F &rArr; G</span></td>
                  <td style="padding:7px 8px">Schema graph populating live table rows; naturality prism</td>
                  <td style="padding:7px 8px">Relational database instance &amp; schema homomorphism</td>
                  <td style="padding:7px 8px"><button class="cite-pill" onclick="window.__jumpToPage(253,'Category')">§ p.253</button> <button class="cite-pill" onclick="window.__jumpToPage(295,'Natural')">§ p.295</button></td>
                </tr>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px"><span class="math-expr">&Sigma;<sub>F</sub> &#8867; &Delta;<sub>F</sub> &#8867; &Pi;<sub>F</sub></span></td>
                  <td style="padding:7px 8px">3-column adjoint elevator with unit <span class="math-expr">&eta;</span> &amp; counit <span class="math-expr">&epsilon;</span></td>
                  <td style="padding:7px 8px">ETL Data Migration: Disjoint Union, Projection, Join</td>
                  <td style="padding:7px 8px"><button class="cite-pill" onclick="window.__jumpToPage(467,'Adjoint')">§ p.467</button> <button class="cite-pill" onclick="window.__jumpToPage(483,'Kan')">§ p.483</button></td>
                </tr>
                <tr>
                  <td style="padding:7px 8px"><span class="math-expr"><span class="m-cal">O</span>(U&cup;V) &cong; <span class="m-cal">O</span>(U) &times;<sub><span class="m-cal">O</span>(U&cap;V)</sub> <span class="m-cal">O</span>(V)</span></td>
                  <td style="padding:7px 8px">Topological open cover overlap matcher &amp; equalizer gate</td>
                  <td style="padding:7px 8px">Distributed sensor fusion &amp; consistent knowledge graphs</td>
                  <td style="padding:7px 8px"><button class="cite-pill" onclick="window.__jumpToPage(518,'Sheaves')">§ p.518</button> <button class="cite-pill" onclick="window.__jumpToPage(520,'sheaf condition')">§ p.520</button></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 7 Interactive Course Modules -->
          <div class="course-grid" id="courseModulesGrid"></div>

          <div class="derived">
            <div class="d-main">
              <strong>Course Deliverable Architecture:</strong> <em>7 Self-Contained HTML Field-Manual Plates + Walkable Symbolic Labs</em> — Every module pairs a reveal.js / Field-Manual slide deck with an interactive symbol-to-diagram sandbox and Python/SQLite verification lab.
            </div>
            <div class="d-sub">Aligned with CETI FORGE &amp; meta-notebook standards</div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Avoiding Purely Decorative "Visual Math"</span></div>
          <div>
            Many visual category theory explainers draw pretty nodes and arrows but leave the reader unable to read or write a real proof or database migration equation. Our course enforces <strong>bi-directional manipulation</strong>: every time a learner drags an arrow in the diagram, the symbolic equation updates; every time they click a sub-term in <span class="math-expr"><span class="m-op">Hom</span><sub><span class="m-cal">D</span></sub>(L(c),d) &cong; <span class="m-op">Hom</span><sub><span class="m-cal">C</span></sub>(c,R(d))</span>, the corresponding morphism highlights and evaluates on concrete data.
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer style="padding:2.5rem 0 3.5rem;font-family:var(--f-mono);font-size:var(--s-mono);color:var(--ink-3);display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem">
    <div>CETI SHEAF KNOWLEDGE BASE &amp; FIELD MANUAL · BUILT FROM SPIVAK’S <em>CATEGORY THEORY FOR THE SCIENCES</em> (609 PP.)</div>
    <div>ALL 30 STALKS · 52 RESTRICTIONS · 877 DECLARATIONS VERIFIED ON DISK</div>
  </footer>

</div>

<!-- ==========================================================================
     SLIDE-OVER 609-PAGE VERBATIM PDF READER & FULL-TEXT SEARCH DRAWER
     ========================================================================== -->
<aside class="reader-drawer" id="readerDrawer" aria-label="609-Page Verbatim Reader">
  <div class="reader-head">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <span class="mono" style="font-weight:600;text-transform:uppercase;color:var(--accent-text)">
        Verbatim 609-Page Book Reader · Spivak (2014)
      </span>
      <div style="display:flex;gap:6px">
        <a id="openRawPdfLink" href="__PDF_REL_PATH__#page=520" target="_blank" class="preset-btn" style="text-decoration:none">Open PDF ↗</a>
        <button class="preset-btn" id="closeReaderBtn">✕ Close</button>
      </div>
    </div>

    <input type="text" class="query-input" id="fullBookSearchInput" placeholder="Search all 609 verbatim PDF pages…" style="width:100%;padding:6px 9px;font-size:0.82rem;margin-bottom:8px">
    <div id="bookSearchResults" style="max-height:170px;overflow-y:auto;display:none;background:var(--paper);border:1px solid var(--rule);margin-bottom:8px;padding:4px"></div>

    <div style="display:flex;align-items:center;gap:6px">
      <button class="preset-btn" id="prevPageBtn">◀ Prev</button>
      <input type="number" id="pageNumInput" min="1" max="609" value="520" class="query-input" style="width:68px;padding:4px 6px;text-align:center;font-family:var(--f-mono)">
      <span class="mono" style="color:var(--ink-3)">/ 609</span>
      <input type="range" id="pageSlider" min="1" max="609" value="520" style="flex:1;accent-color:var(--accent-text)">
      <button class="preset-btn" id="nextPageBtn">Next ▶</button>
    </div>
  </div>

  <div class="reader-body">
    <div id="readerPageMeta" style="margin-bottom:0.75rem;padding-bottom:0.6rem;border-bottom:1px solid var(--rule-hair)"></div>
    <div class="verbatim-sheet" id="readerPageText"></div>
  </div>
</aside>

<!-- Mobile Quick-Action Bottom Dock -->
<nav class="mobile-bottom-dock" id="mobileBottomDock" aria-label="Mobile Quick Navigation">
  <button type="button" class="mobile-dock-btn" onclick="window.__focusPlate('plate-3', true)">🎨 Symbols</button>
  <button type="button" class="mobile-dock-btn" id="mobileDockPlayBtn" onclick="window.__focusPlate('plate-2', false); document.getElementById('podcastPlayPauseBtn').click()">▶ Deep Dive</button>
  <button type="button" class="mobile-dock-btn" onclick="window.__focusPlate('plate-2', true)">🧪 Notebook</button>
  <button type="button" class="mobile-dock-btn" id="mobileDockReaderBtn" onclick="document.getElementById('openReaderBtn').click()">📖 p.520</button>
</nav>

<!-- ==========================================================================
     CORE SHEAF DATA + DEFERRED 609-PAGE BUNDLE
     ========================================================================== -->
<script id="sheaf-core-data" type="application/json">__SHEAF_CORE_JSON__</script>
<script defer src="__BUNDLE_REL_PATH__"></script>

<script>
(function() {
  const KB = JSON.parse(document.getElementById('sheaf-core-data').textContent);
  KB.pages = KB.seed_pages || [];
  KB.formal_items = [];
  let pageByNum = {};
  KB.pages.forEach(p => { pageByNum[p.p] = p; });

  const stalkById = {};
  KB.stalks.forEach(s => { stalkById[s.id] = s; });

  // Receive deferred 609-page + 877-declaration bundle without blocking first paint
  window.__onSheafBundleLoaded = function(bundle) {
    if (!bundle) return;
    KB.pages = bundle.pages || KB.pages;
    KB.formal_items = bundle.formal_items || [];
    if (bundle.full_stalk_items) {
      KB.stalks.forEach(s => {
        if (bundle.full_stalk_items[s.id]) s.formal_items = bundle.full_stalk_items[s.id];
      });
    }
    pageByNum = {};
    KB.pages.forEach(p => { pageByNum[p.p] = p; });
    renderPageReader(state.currentPage, state.highlightTerm);
    if (state.activeSubview === 'declarations') renderDeclarationsList();
  };

  // ==========================================================================
  // 1. MATHEMATICAL NOTATION & LATEX-TO-TYPESET-HTML PARSER
  //    Guarantees zero raw LaTeX backslashes (\mathcal, \varprojlim, \dashv...)
  // ==========================================================================
  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function convertLatexTokensToHtml(mathStr) {
    let s = escapeHtml(mathStr.trim());

    // Protect escaped set braces \{ and \} and escaped \& before brace stripping
    s = s.replace(/\\\{/g, '&#123;').replace(/\\\}/g, '&#125;');
    s = s.replace(/\\&amp;/g, '&amp;');

    // Remove sizing commands
    s = s.replace(/\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big)\b/g, '');
    s = s.replace(/\\[,;:!]/g, ' ');
    s = s.replace(/\\quad\b/g, ' &emsp; ');
    s = s.replace(/\\qquad\b/g, ' &emsp;&emsp; ');
    s = s.replace(/\^\{\\circ\}/g, '&deg;');
    s = s.replace(/\^\\circ\b/g, '&deg;');
    s = s.replace(/\\pmod\{([^{}]+)\}/g, ' (mod $1)');

    // Labeled arrows: \xrightarrow{...}, \xleftarrow{...}, \overset{...}{\to} BEFORE font macros so recursive convertLatexTokensToHtml(lbl) never double-escapes HTML tags
    s = s.replace(/\\overset\{\\sim\}\{\\to\}/g, '<span class="m-arrow"><span class="m-arrow-label">&sim;</span><span class="m-arrow-body">&rarr;</span></span>');
    s = s.replace(/\\xrightarrow\{((?:[^{}]|\{[^{}]*\})+)\}/g, (_, lbl) => `<span class="m-arrow"><span class="m-arrow-label">${convertLatexTokensToHtml(lbl)}</span><span class="m-arrow-body">&rarr;</span></span>`);
    s = s.replace(/\\xleftarrow\{((?:[^{}]|\{[^{}]*\})+)\}/g, (_, lbl) => `<span class="m-arrow"><span class="m-arrow-label">${convertLatexTokensToHtml(lbl)}</span><span class="m-arrow-body">&larr;</span></span>`);
    s = s.replace(/\\overset\{((?:[^{}]|\{[^{}]*\})+)\}\{\\to\}/g, (_, lbl) => `<span class="m-arrow"><span class="m-arrow-label">${convertLatexTokensToHtml(lbl)}</span><span class="m-arrow-body">&rarr;</span></span>`);

    // Font macros
    for (let pass = 0; pass < 3; pass++) {
      s = s.replace(/\\mathcal\{([^{}]+)\}/g, '<span class="m-cal">$1</span>');
      s = s.replace(/\\mathbf\{([^{}]+)\}/g, '<span class="m-cat">$1</span>');
      s = s.replace(/\\(?:mathrm|text|operatorname)\{([^{}]+)\}/g, '<span class="m-op">$1</span>');
      s = s.replace(/\\emph\{([^{}]+)\}/g, '<em>$1</em>');
    }

    // Limits & Colimits with subscripts
    s = s.replace(/\\varprojlim_\{([^}]+)\}/g, '<span class="m-lim"><span class="m-lim-top">lim&larr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\varprojlim_([A-Za-z0-9]+)/g, '<span class="m-lim"><span class="m-lim-top">lim&larr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\varprojlim\b/g, '<span class="m-op">lim&larr;</span>');

    s = s.replace(/\\varinjlim_\{([^}]+)\}/g, '<span class="m-lim"><span class="m-lim-top">colim&rarr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\varinjlim_([A-Za-z0-9]+)/g, '<span class="m-lim"><span class="m-lim-top">colim&rarr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\varinjlim\b/g, '<span class="m-op">colim&rarr;</span>');

    // Greek letters & Categorical symbols
    const symMap = {
      '\\alpha': '&alpha;', '\\beta': '&beta;', '\\gamma': '&gamma;', '\\delta': '&delta;',
      '\\epsilon': '&epsilon;', '\\varepsilon': '&varepsilon;', '\\eta': '&eta;', '\\theta': '&theta;',
      '\\lambda': '&lambda;', '\\mu': '&mu;', '\\nu': '&nu;', '\\pi': '&pi;', '\\rho': '&rho;',
      '\\sigma': '&sigma;', '\\tau': '&tau;', '\\phi': '&phi;', '\\varphi': '&varphi;',
      '\\psi': '&psi;', '\\omega': '&omega;',
      '\\Gamma': '&Gamma;', '\\Delta': '&Delta;', '\\Theta': '&Theta;', '\\Lambda': '&Lambda;',
      '\\Pi': '&Pi;', '\\Sigma': '&Sigma;', '\\Phi': '&Phi;', '\\Psi': '&Psi;', '\\Omega': '&Omega;',
      '\\to': '&rarr;', '\\rightarrow': '&rarr;', '\\leftarrow': '&larr;',
      '\\leftrightarrow': '&harr;', '\\longleftrightarrow': '&harr;',
      '\\mapsto': '&#8614;', '\\longmapsto': '&#8614;',
      '\\hookrightarrow': '&#8618;', '\\twoheadrightarrow': '&#8608;',
      '\\Rightarrow': '&rArr;', '\\Leftarrow': '&lArr;', '\\Leftrightarrow': '&hArr;',
      '\\iff': '&hArr;', '\\implies': '&rArr;',
      '\\rightrightarrows': '&#8649;',
      '\\dashv': '&#8867;', '\\vdash': '&#8866;',
      '\\cong': '&cong;', '\\simeq': '&simeq;', '\\sim': '&sim;', '\\equiv': '&equiv;',
      '\\approx': '&approx;', '\\neq': '&ne;', '\\leq': '&le;', '\\geq': '&ge;',
      '\\leqslant': '&le;', '\\geqslant': '&ge;',
      '\\subset': '&sub;', '\\subseteq': '&sube;', '\\supset': '&sup;', '\\supseteq': '&supe;',
      '\\in': '&isin;', '\\notin': '&notin;', '\\ni': '&ni;',
      '\\cup': '&cup;', '\\cap': '&cap;', '\\bigcup': '&#8899;', '\\bigcap': '&#8898;',
      '\\sqcup': '&#8852;', '\\bigsqcup': '&#10758;', '\\sqcap': '&#8851;',
      '\\times': '&times;', '\\otimes': '&otimes;', '\\oplus': '&oplus;',
      '\\prod': '&prod;', '\\coprod': '&#8720;', '\\sum': '&sum;', '\\int': '&int;',
      '\\circ': '&#8728;', '\\bullet': '&bull;', '\\cdot': '&middot;',
      '\\forall': '&forall;', '\\exists': '&exist;', '\\nexists': '&#8708;',
      '\\emptyset': '&empty;', '\\varnothing': '&empty;', '\\infty': '&infin;',
      '\\partial': '&part;', '\\nabla': '&nabla;',
      '\\langle': '&lang;', '\\rangle': '&rang;',
      '\\lrcorner': '&#8991;',
      '\\ldots': '&hellip;', '\\cdots': '&ctdot;', '\\dots': '&hellip;',
      '\\mathbb{N}': '&#8469;', '\\mathbb{Z}': '&#8484;', '\\mathbb{Q}': '&#8474;',
      '\\mathbb{R}': '&#8477;', '\\mathbb{C}': '&#8450;',
      '\\top': '&#8868;', '\\bot': '&#8869;',
      '\\mid': ' &#8739; ', '\\parallel': '&#8741;', '\\setminus': '&#8726;',
      '\\neg': '&not;', '\\land': '&and;', '\\lor': '&or;'
    };

    const sortedKeys = Object.keys(symMap).sort((a, b) => b.length - a.length);
    for (const k of sortedKeys) {
      const escapedK = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const pattern = /[a-zA-Z]$/.test(k) ? new RegExp(escapedK + '(?![a-zA-Z])', 'g') : new RegExp(escapedK, 'g');
      s = s.replace(pattern, symMap[k]);
    }

    // Handle nested subscripts & superscripts: _{...} and ^{...}
    for (let pass = 0; pass < 3; pass++) {
      s = s.replace(/_\{([^{}]+)\}/g, '<sub>$1</sub>');
      s = s.replace(/\^\{([^{}]+)\}/g, '<sup>$1</sup>');
    }
    s = s.replace(/_(&[A-Za-z0-9#]+;|[A-Za-z0-9])/g, '<sub>$1</sub>');
    s = s.replace(/\^(&[A-Za-z0-9#]+;|[A-Za-z0-9])/g, '<sup>$1</sup>');

    s = s.replace(/\{([^{}]+)\}/g, '$1');
    return s;
  }

  function renderMathChip(latex, isDisplay) {
    const inner = convertLatexTokensToHtml(latex);
    return isDisplay
      ? `<div class="math-display">${inner}</div>`
      : `<span class="math-expr">${inner}</span>`;
  }

  // Full Markdown + LaTeX + Page Citation Renderer
  function renderRichMarkdown(md) {
    if (!md) return '';
    let text = String(md);

    // 1. Extract display math $$...$$ into placeholders first
    const mathBlocks = [];
    text = text.replace(/\$\$([\s\S]*?)\$\$/g, (_, expr) => {
      const idx = mathBlocks.length;
      mathBlocks.push(renderMathChip(expr, true));
      return `@@MATH_BLOCK_${idx}@@`;
    });

    // 2. Extract inline math $...$ into placeholders
    const mathInlines = [];
    text = text.replace(/\$([^\$\n]+?)\$/g, (_, expr) => {
      const idx = mathInlines.length;
      mathInlines.push(renderMathChip(expr, false));
      return `@@MATH_INLINE_${idx}@@`;
    });

    // 3. Escape HTML on the prose
    let html = escapeHtml(text);

    // 4. Convert Page Citations [p. 520] or `[p. 520, Def 7.2.2.2]` and [CITE-0X] badges
    html = html.replace(/`?\[p\.\s*(\d+)([^\]]*)\]`?/g, (_, pNum, rest) => {
      return `<button class="cite-pill" onclick="window.__jumpToPage(${pNum}, '')">§ p.${pNum}${rest}</button>`;
    });
    html = html.replace(/`?\[(CITE-\d+)\]`?/g, '<span class="stamp ratified" style="font-size:0.65rem;padding:1px 5px">$1</span>');

    // 5. Convert inline code `...` (if it contains LaTeX backslashes or math tokens, render as math chip!)
    html = html.replace(/`([^`]+)`/g, (_, codeStr) => {
      if (/\\[a-zA-Z]|_\{|\^\{|\\to|\\circ|\\times|\\sqcup|\\cong|\\simeq/.test(codeStr)) {
        return `<span class="math-expr">${convertLatexTokensToHtml(codeStr)}</span>`;
      }
      return `<code class="inline-code">${codeStr}</code>`;
    });

    // 6. Bold & Italic
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

    // 7. Block-level Markdown structure (headings, blockquotes, lists, paragraphs)
    const lines = html.split('\n');
    const out = [];
    let inList = false;

    for (let rawLine of lines) {
      const line = rawLine.trim();
      if (!line) {
        if (inList) { out.push('</ul>'); inList = false; }
        continue;
      }
      if (line.startsWith('#### ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<h4>${line.slice(5)}</h4>`);
      } else if (line.startsWith('### ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<h3>${line.slice(4)}</h3>`);
      } else if (line.startsWith('## ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<h3 style="margin-top:0.85rem;margin-bottom:0.35rem;color:var(--accent-text)">${line.slice(3)}</h3>`);
      } else if (line.startsWith('# ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<h2 style="font-size:1.15rem;margin-top:0.4rem;margin-bottom:0.45rem;border-bottom:1px solid var(--rule-hair);padding-bottom:0.3rem">${line.slice(2)}</h2>`);
      } else if (line.startsWith('&gt; ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<blockquote style="border-left:3px solid var(--accent);padding:0.35rem 0.85rem;margin:0.55rem 0;background:rgba(166,119,86,0.06);color:var(--ink-2)">${line.slice(5)}</blockquote>`);
      } else if (line.startsWith('- ') || line.startsWith('* ')) {
        if (!inList) { out.push('<ul>'); inList = true; }
        out.push(`<li>${line.slice(2)}</li>`);
      } else if (/^\d+\.\s+/.test(line)) {
        if (!inList) { out.push('<ul>'); inList = true; }
        out.push(`<li>${line.replace(/^\d+\.\s+/, '')}</li>`);
      } else if (/^@@MATH_BLOCK_\d+@@$/.test(line)) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(line);
      } else {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<p>${line}</p>`);
      }
    }
    if (inList) out.push('</ul>');

    let finalHtml = out.join('\n');

    // Restore math placeholders
    finalHtml = finalHtml.replace(/@@MATH_BLOCK_(\d+)@@/g, (_, idx) => mathBlocks[Number(idx)]);
    finalHtml = finalHtml.replace(/@@MATH_INLINE_(\d+)@@/g, (_, idx) => mathInlines[Number(idx)]);

    // Catch any remaining bare LaTeX sequences outside $...$
    if (/\\(?:mathcal|mathbf|varprojlim|varinjlim|xrightarrow|dashv|simeq|cong|rho|Delta|Sigma|Pi|mid)/.test(finalHtml)) {
      finalHtml = convertLatexTokensToHtml(finalHtml);
    }
    return finalHtml;
  }

  // ==========================================================================
  // 2. FIELD CONTROLS (View Mode, Depth Level, Paper Theme, Slide-Over Reader)
  // ==========================================================================
  const allPlates = Array.from(document.querySelectorAll('section.plate'));
  let activePlateId = 'plate-1';

  function setViewMode(mode, targetPlateId) {
    document.documentElement.setAttribute('data-view-mode', mode);
    document.querySelectorAll('[data-set-view]').forEach(b => {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-set-view') === mode));
    });
    if (targetPlateId) activePlateId = targetPlateId;
    allPlates.forEach(p => {
      p.classList.toggle('active-plate', p.id === activePlateId);
    });
    document.querySelectorAll('[data-plate-link]').forEach(a => {
      const pid = a.getAttribute('data-plate-link');
      a.style.background = (mode === 'focus' && pid === activePlateId) ? 'var(--surface)' : '';
      a.style.color = (mode === 'focus' && pid === activePlateId) ? 'var(--ink)' : '';
    });
  }

  window.__focusPlate = function(plateId, forceFocusMode) {
    activePlateId = plateId;
    const curMode = document.documentElement.getAttribute('data-view-mode') || 'all';
    if (forceFocusMode || curMode === 'focus') {
      setViewMode('focus', plateId);
      const el = document.getElementById(plateId);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      allPlates.forEach(p => p.classList.toggle('active-plate', p.id === plateId));
      const el = document.getElementById(plateId);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  document.querySelectorAll('[data-set-view]').forEach(btn => {
    btn.addEventListener('click', () => setViewMode(btn.getAttribute('data-set-view'), activePlateId));
  });

  document.querySelectorAll('[data-plate-link]').forEach(a => {
    a.addEventListener('click', e => {
      const pid = a.getAttribute('data-plate-link');
      const curMode = document.documentElement.getAttribute('data-view-mode') || 'all';
      if (curMode === 'focus') {
        e.preventDefault();
        window.__focusPlate(pid, true);
      } else {
        activePlateId = pid;
      }
    });
  });

  allPlates.forEach((p, idx) => {
    const prevP = allPlates[(idx - 1 + allPlates.length) % allPlates.length];
    const nextP = allPlates[(idx + 1) % allPlates.length];
    const bar = document.createElement('div');
    bar.className = 'plate-focus-bar';
    bar.innerHTML = `
      <button type="button" class="preset-btn" onclick="window.__focusPlate('${prevP.id}', true)">◀ Plate ${idx === 0 ? 'V' : ['I','II','III','IV','V'][idx-1]}</button>
      <span>Focus Mode · Plate ${['I','II','III','IV','V'][idx]} of V</span>
      <div style="display:flex;gap:6px">
        <button type="button" class="preset-btn" onclick="document.querySelector('[data-set-view=\\'all\\']').click()">Show All 5 Plates</button>
        <button type="button" class="btn-copper" style="padding:4px 10px;font-size:0.72rem" onclick="window.__focusPlate('${nextP.id}', true)">Next: Plate ${['I','II','III','IV','V'][(idx+1)%5]} ▶</button>
      </div>
    `;
    p.appendChild(bar);
  });

  const mobileCoverToggleBtn = document.getElementById('mobileCoverToggleBtn');
  const coverPanelDrawer = document.getElementById('coverPanelDrawer');
  const mobileCoverCaret = document.getElementById('mobileCoverCaret');
  if (mobileCoverToggleBtn && coverPanelDrawer) {
    mobileCoverToggleBtn.addEventListener('click', () => {
      const collapsed = coverPanelDrawer.classList.toggle('mobile-collapsed');
      mobileCoverToggleBtn.setAttribute('aria-expanded', String(!collapsed));
      if (mobileCoverCaret) mobileCoverCaret.textContent = collapsed ? '▾ Show' : '▴ Hide';
    });
  }

  document.querySelectorAll('[data-set-level]').forEach(btn => {
    btn.addEventListener('click', () => {
      const lvl = btn.getAttribute('data-set-level');
      document.documentElement.setAttribute('data-level', lvl);
      document.querySelectorAll('[data-set-level]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    });
  });

  document.querySelectorAll('[data-set-theme]').forEach(btn => {
    btn.addEventListener('click', () => {
      const th = btn.getAttribute('data-set-theme');
      document.documentElement.setAttribute('data-theme', th);
      document.querySelectorAll('[data-set-theme]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    });
  });

  // ==========================================================================
  // 3. PLATE I: QUERY & SHEAF ARCHITECTURE PIPELINE INSTRUMENT
  // ==========================================================================
  const PIPE_STAGES = [
    {
      num: 'STAGE 01',
      title: 'Verbatim PDF Extraction & SQLite FTS5 Index',
      stamp: '⚖ 609 pp · 877 declarations',
      summary: 'Instead of lossy chunking, `build_sheaf_kb.py` extracts all 609 pages of Spivak’s book verbatim, preserving section hierarchy (96 sections) and 877 numbered formal declarations (`Definition`, `Theorem`, `Proposition`, `Example`, `Application`, `Exercise`).',
      math: '\\text{Corpus} = \\{ (p, \\text{sec}(p), \\text{Items}(p)) \\mid p \\in \\{1, \\dots, 609\\} \\}',
      code: 'sqlite3 cattheory-sheaf-kb/data/cattheory_sheaf.db "SELECT id, kind, title, page FROM formal_items_fts WHERE formal_items_fts MATCH \'sheaf\' LIMIT 5;"',
      outputs: [
        'cattheory-sheaf-kb/data/cattheory_sheaf.db (SQLite FTS5 full-text index)',
        'cattheory-sheaf-kb/data/sheaf_kb.json (Complete sheaf topology & stalks)',
        'cattheory-sheaf-kb/data/sheaf_pages_bundle.js (Deferred browser page bundle)'
      ]
    },
    {
      num: 'STAGE 02',
      title: 'Alexandrov Topology & Open Cover Selection',
      stamp: '◆ 30 Concept Stalks',
      summary: 'The 30 core conceptual domains of the book form a poset X ordered by conceptual dependency. Under the Alexandrov topology Alx(X^op), every downward-closed subset U is an open neighborhood carrying a local categorical schema O(U).',
      math: '\\mathcal{U} = \\{ U_i \\}_{i \\in I} \\subseteq \\text{Open}(\\text{Alx}(X^{\\text{op}})), \\quad \\mathcal{O} : \\text{Open}(\\mathcal{X})^{\\text{op}} \\to \\mathbf{Sch} \\simeq \\mathbf{Cat}',
      code: 'python3 cattheory-sheaf-kb/query_sheaf.py --stalk "sheaf-of-ologged-concepts-descent"',
      outputs: [
        '30 Concept Stalks mapped across Chapters 1–7',
        'Local Olog objects (`types`) & typed arrows (`aspects`) inside each stalk O(U_i)',
        'Exact PDF page fibers p^{-1}(U_i) attached to every stalk'
      ]
    },
    {
      num: 'STAGE 03',
      title: 'Pairwise Intersection & Restriction Morphism Audit',
      stamp: '◆ 52 Restriction Arrows',
      summary: 'When you query across multiple stalks U_i and U_j, the engine inspects all 52 restriction morphisms ρ_{U_i, U_j} : O(U_i) → O(U_i ∩ U_j) to verify that local definitions commute on their overlap.',
      math: '\\rho_{U_i, U_i \\cap U_j}(s_i) = \\rho_{U_j, U_i \\cap U_j}(s_j) \\in \\mathcal{O}(U_i \\cap U_j)',
      code: 'python3 cattheory-sheaf-kb/query_sheaf.py --gluing-audit',
      outputs: [
        '52 typed restriction morphisms ρ_{U,V} with explicit formulas & overlaps',
        'Automatic detection of disconnected stalks (requiring a bridging stalk)',
        'Verification of 8 higher-order commutative 2-simplices ρ_{V,W} ∘ ρ_{U,V} = ρ_{U,W}'
      ]
    },
    {
      num: 'STAGE 04',
      title: 'Sheaf Equalizer / Fiber-Product Gluing',
      stamp: '◆ Universal Gluing Axiom',
      summary: 'Once pairwise compatibility holds on all overlaps U_i ∩ U_j, the engine computes the fiber product O(U) ×_{O(U∩V)} O(V), merging the local Olog graphs along their shared conceptual core into a single global section.',
      math: '\\mathcal{O}(U \\cup V) \\cong \\text{eq}\\Bigl( \\prod_i \\mathcal{O}(U_i) \\rightrightarrows \\prod_{i,j} \\mathcal{O}(U_i \\cap U_j) \\Bigr)',
      code: '// In-browser deterministic sheaf gluing (< 2ms):\nconst gluedOlog = renderGluedOlogSvg(activeCoverStalks, activeRestrictions);',
      outputs: [
        'Unified Commutative Olog SVG synthesized dynamically for any chosen open cover',
        'Aggregated formal Definitions, Theorems, and page citations across the cover',
        'Guaranteed zero hallucinated theorems — every node traces to Spivak [p. N]'
      ]
    },
    {
      num: 'STAGE 05',
      title: 'Synthesis Bridge: Local Deterministic + Gemini REST / MCP',
      stamp: '✓ Local + Gemini 2.5',
      summary: 'How does it answer questions? (1) In the browser, it runs 100% locally: matching your query against FTS5 pages + open-cover stalks and gluing the relevant local sections & Ologs. (2) From CLI or MCP, `query_sheaf.py --ask "..."` passes the glued sheaf context to Gemini.',
      math: '\\text{Query}(q, \\mathcal{U}) \\xrightarrow{\\text{Sheaf Glue}} \\Gamma(\\mathcal{U}, \\mathcal{O}) \\xrightarrow{\\text{Local or Gemini}} \\text{Typeset Synthesis}',
      code: '# Run deterministic local sheaf query:\npython3 cattheory-sheaf-kb/query_sheaf.py --ask "How do Kan extensions unify SQL joins?"\n\n# Or pipe glued sheaf context to Gemini API:\nGEMINI_API_KEY=... python3 cattheory-sheaf-kb/query_sheaf.py --ask "How do Kan extensions unify SQL joins?"',
      outputs: [
        'Zero-latency local browser studio (no API key required to explore or query)',
        'CLI & Gemini-ready Python engine (`cattheory-sheaf-kb/query_sheaf.py`)',
        '38 persistent LLM Wiki markdown files (`cattheory-sheaf-kb/wiki/concepts/*.md`)'
      ]
    }
  ];

  function renderPipeStage(idx) {
    const st = PIPE_STAGES[idx] || PIPE_STAGES[0];
    document.querySelectorAll('#pipeRail .pipe-node').forEach((btn, i) => {
      btn.setAttribute('aria-selected', String(i === idx));
    });
    document.getElementById('pipeInspector').innerHTML = `
      <div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.4rem">
          <span class="mono" style="color:var(--accent-text);font-weight:600">${st.num}</span>
          <span class="stamp ratified">◆ ${st.stamp.replace(/^[◆⚖✓±⊘]\s*/, '')}</span>
        </div>
        <h3 class="serif" style="font-size:1.3rem;margin-bottom:0.5rem">${escapeHtml(st.title)}</h3>
        <p style="font-size:0.9rem;margin-bottom:0.75rem">${escapeHtml(st.summary)}</p>
        ${renderMathChip(st.math, true)}
      </div>
      <div style="display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <div class="mono" style="font-size:0.69rem;text-transform:uppercase;color:var(--ink-3);margin-bottom:4px">Executable Command / Implementation</div>
          <pre style="background:var(--paper-soft);border:1px solid var(--rule);padding:0.75rem;font-family:var(--f-mono);font-size:0.74rem;overflow-x:auto;margin:0 0 0.85rem;white-space:pre-wrap;color:var(--ink)">${escapeHtml(st.code)}</pre>
        </div>
        <div class="callout-box">
          <strong>On-Disk Artifacts Verified</strong>
          <ul style="margin:4px 0 0 1rem;padding:0;font-size:0.80rem">
            ${st.outputs.map(o => `<li>${escapeHtml(o)}</li>`).join('')}
          </ul>
        </div>
      </div>
    `;
    document.getElementById('pipeDerivedTitle').textContent = `${st.num} · ${st.title}`;
    document.getElementById('pipeDerivedBody').textContent = st.summary;
  }

  document.querySelectorAll('#pipeRail .pipe-node').forEach(btn => {
    btn.addEventListener('click', () => renderPipeStage(Number(btn.getAttribute('data-stage'))));
  });
  renderPipeStage(0);

  // ==========================================================================
  // 4. PLATE II: GEMINI NOTEBOOK GLUING STUDIO
  // ==========================================================================
  const firstInv = (KB.notebook_investigations && KB.notebook_investigations[0]) || {
    id: 'q-default',
    question: 'Explore the sheaf topology across the opening stalks',
    open_cover: KB.stalks.slice(0, Math.min(3, KB.stalks.length)).map(s => s.id),
    synthesis_markdown: '### Glued Global Section\nSelect concept stalks on the left to inspect restriction fidelity and glued Ologs.'
  };
  const defaultStalk = KB.stalks.find(s => s.id === 'sheaf-of-ologged-concepts-descent') || KB.stalks[Math.min(2, KB.stalks.length - 1)] || KB.stalks[0];
  const defaultPage = (defaultStalk && defaultStalk.start_page <= (KB.book.total_pages || 9999)) ? defaultStalk.start_page : 1;
  const state = {
    openCover: new Set(firstInv.open_cover),
    focusedStalkId: defaultStalk ? defaultStalk.id : (KB.stalks[0] && KB.stalks[0].id),
    currentInvestigation: firstInv,
    currentPage: defaultPage,
    highlightTerm: (defaultStalk && (defaultStalk.keywords || [])[0]) || 'category',
    activeSubview: 'stalks',
    audioPlaying: false
  };

  function buildStalkTree() {
    const q = (document.getElementById('stalkFilterInput').value || '').trim().toLowerCase();
    const container = document.getElementById('stalkTreeList');
    let html = '';

    KB.chapters.forEach(ch => {
      const chNum = ch.chapter;
      const stalks = KB.stalks.filter(s => s.chapter === chNum && (
        !q || s.title.toLowerCase().includes(q) || (s.keywords || []).some(k => k.toLowerCase().includes(q))
      ));
      if (!stalks.length) return;
      html += `<div class="mono" style="font-size:0.67rem;text-transform:uppercase;color:var(--ink-3);margin:8px 0 4px;letter-spacing:0.06em">Ch ${chNum} · ${escapeHtml(ch.title.split(':')[0])}</div>`;
      stalks.forEach(s => {
        const inCov = state.openCover.has(s.id);
        const foc = state.focusedStalkId === s.id;
        html += `
          <div class="stalk-item ${inCov ? 'in-cover' : ''} ${foc ? 'focused' : ''}" data-stalk-id="${s.id}">
            <div class="stalk-check" data-check-stalk="${s.id}">${inCov ? '✓' : ''}</div>
            <div style="flex:1;min-width:0">
              <div style="font-weight:500;color:var(--ink);line-height:1.25">${escapeHtml(s.title)}</div>
              <div class="mono" style="font-size:0.67rem;color:var(--ink-3)">§${s.section} · pp.${s.start_page}–${s.end_page}</div>
            </div>
          </div>
        `;
      });
    });

    container.innerHTML = html;

    container.querySelectorAll('.stalk-item').forEach(row => {
      row.addEventListener('click', e => {
        const id = row.getAttribute('data-stalk-id');
        if (e.target.hasAttribute('data-check-stalk')) {
          if (state.openCover.has(id)) {
            if (state.openCover.size > 1) state.openCover.delete(id);
          } else {
            state.openCover.add(id);
          }
        } else {
          state.focusedStalkId = id;
          state.openCover.add(id);
        }
        updateCoverAndOlog();
      });
    });
  }

  function getActiveRestrictions() {
    return KB.restriction_morphisms.filter(r => state.openCover.has(r.source) && state.openCover.has(r.target));
  }

  function evaluateCoverCohomology(coverIds) {
    const cset = Array.from(coverIds).filter(id => stalkById[id]);
    if (!cset.length) return { verdict: 'FAIL', h0_coherence: 0, beta_0: 0, mean_d0: 1.0, closure: 0, activeR: [], missingPrereqs: [], obstructions: [] };
    const csetLookup = new Set(cset);
    const activeR = KB.restriction_morphisms.filter(r => csetLookup.has(r.source) && csetLookup.has(r.target));

    const adj = {};
    cset.forEach(id => { adj[id] = []; });
    activeR.forEach(r => { adj[r.source].push(r.target); adj[r.target].push(r.source); });
    const visited = new Set();
    let beta_0 = 0;
    cset.forEach(id => {
      if (!visited.has(id)) {
        beta_0++;
        const q = [id];
        visited.add(id);
        while (q.length) {
          const cur = q.shift();
          (adj[cur] || []).forEach(nxt => { if (!visited.has(nxt)) { visited.add(nxt); q.push(nxt); } });
        }
      }
    });

    const meanFid = activeR.length
      ? activeR.reduce((acc, r) => acc + (r.restriction_fidelity || 0.68), 0) / activeR.length
      : (cset.length === 1 ? 0.85 : 0.0);
    const meanD0 = Number((1.0 - meanFid).toFixed(3));

    let totP = 0, satP = 0;
    const missingMap = {};
    cset.forEach(id => {
      ((stalkById[id] && stalkById[id].prerequisites) || []).forEach(pr => {
        totP++;
        if (csetLookup.has(pr.stalk_id)) satP++;
        else missingMap[pr.stalk_id] = pr;
      });
    });
    const closure = totP > 0 ? satP / totP : 1.0;
    const missingPrereqs = Object.values(missingMap);

    const activeSimp = (KB.two_simplices || []).filter(t => (t.vertices || []).every(v => csetLookup.has(v)));
    const meanD1 = activeSimp.length
      ? activeSimp.reduce((acc, t) => acc + (t.holonomy_defect_d1 || 0.13), 0) / activeSimp.length
      : 0.13;

    const obstructions = (KB.cohomology_obstructions || []).filter(obs =>
      csetLookup.has(obs.stalk_a) && csetLookup.has(obs.stalk_b) && !csetLookup.has(obs.required_bridge_stalk)
    );

    let rawCoh = (0.48 * meanFid + 0.32 * closure + 0.20 * (1.0 - meanD1)) / Math.max(1, beta_0);
    if (obstructions.length) rawCoh *= 0.62;
    const h0_coherence = Number(Math.max(0.05, Math.min(0.99, rawCoh)).toFixed(3));

    let verdict = 'PASS';
    if (beta_0 > 1 || obstructions.length > 0 || (cset.length > 1 && activeR.length === 0)) verdict = 'FAIL';
    else if (closure < 0.55 || h0_coherence < 0.58) verdict = 'WARN';

    return { verdict, h0_coherence, beta_0, mean_d0: meanD0, mean_d1: Number(meanD1.toFixed(3)), closure: Number(closure.toFixed(3)), activeR, missingPrereqs, obstructions };
  }

  function renderLiveGluingBanner(coh, questionText) {
    const banner = document.getElementById('gluingAuditBanner');
    if (coh.verdict === 'FAIL') {
      banner.style.background = 'rgba(142, 42, 34, 0.09)';
      banner.style.borderColor = 'rgba(142, 42, 34, 0.45)';
      banner.style.borderLeftColor = 'var(--bad)';
    } else if (coh.verdict === 'WARN') {
      banner.style.background = 'rgba(150, 96, 26, 0.10)';
      banner.style.borderColor = 'rgba(150, 96, 26, 0.45)';
      banner.style.borderLeftColor = 'var(--warn)';
    } else {
      banner.style.background = 'rgba(59, 94, 73, 0.08)';
      banner.style.borderColor = 'rgba(59, 94, 73, 0.35)';
      banner.style.borderLeftColor = 'var(--good)';
    }

    const obs = coh.obstructions[0];
    const bridgeIds = [];
    coh.obstructions.forEach(o => { if (!bridgeIds.includes(o.required_bridge_stalk)) bridgeIds.push(o.required_bridge_stalk); });
    coh.missingPrereqs.slice(0, 2).forEach(p => { if (!bridgeIds.includes(p.stalk_id)) bridgeIds.push(p.stalk_id); });

    const statusLine = coh.verdict === 'FAIL'
      ? `⊘ H¹ GLUING OBSTRUCTION — FAIL (H⁰ Coherence = ${coh.h0_coherence} · β₀ = ${coh.beta_0} components · ||δ⁰|| = ${coh.mean_d0} · Closure = ${Math.round(coh.closure*100)}%)`
      : coh.verdict === 'WARN'
      ? `± PARTIAL SECTION — WARN (H⁰ Coherence = ${coh.h0_coherence} · Missing ${coh.missingPrereqs.length} Prerequisite Stalks · ||δ⁰|| = ${coh.mean_d0})`
      : `◆ H⁰ GLOBAL SECTION GLUED — PASS (H⁰ Coherence = ${coh.h0_coherence} · ||δ⁰|| = ${coh.mean_d0} · ||δ¹|| = ${coh.mean_d1} · Closure = ${Math.round(coh.closure*100)}%)`;

    const colorVar = coh.verdict === 'FAIL' ? 'var(--bad)' : (coh.verdict === 'WARN' ? 'var(--warn)' : 'var(--good)');
    const diagHtml = obs
      ? `<div style="font-size:0.81rem;color:var(--bad);margin-top:4px"><strong>Empirical H¹ Conflict:</strong> ${escapeHtml(obs.diagnostic)}</div>`
      : (coh.beta_0 > 1
        ? `<div style="font-size:0.81rem;color:var(--bad);margin-top:4px"><strong>Topological Disconnection:</strong> Selected open cover splits into β₀=${coh.beta_0} disconnected islands with zero restriction morphisms between them.</div>`
        : '');

    const fixBtnHtml = (coh.verdict !== 'PASS' && bridgeIds.length)
      ? `<button class="btn-copper" style="background:var(--bad);border-color:var(--bad);padding:4px 9px;font-size:0.69rem" onclick="window.__resolveCohomologyObstruction('${bridgeIds.join(',')}')">+ Resolve H¹ Obstruction (Add Bridge Stalk)</button>`
      : '';

    banner.innerHTML = `
      <div style="flex:1;min-width:260px">
        <div class="mono" style="font-size:0.71rem;color:${colorVar};font-weight:600;text-transform:uppercase">
          ${escapeHtml(statusLine)}
        </div>
        <div style="font-size:0.86rem;color:var(--ink-2);margin-top:3px">
          <strong>Notebook Question:</strong> ${escapeHtml(questionText || (state.currentInvestigation && state.currentInvestigation.question) || 'Custom Open-Cover Gluing')}
        </div>
        ${diagHtml}
      </div>
      <div style="display:flex;gap:5px;flex-wrap:wrap;align-items:center">
        ${fixBtnHtml}
        ${Array.from(state.openCover).slice(0, 6).map(cid => {
          const st = stalkById[cid];
          return st ? `<span class="stamp ${coh.verdict === 'FAIL' ? 'gate' : 'ratified'}" style="cursor:pointer" onclick="window.__jumpToPage(${st.start_page}, '')">${coh.verdict === 'FAIL' ? '⊘' : '◆'} ${escapeHtml(st.title.split(' ')[0])} (p.${st.start_page})</span>` : '';
        }).join('')}
      </div>
    `;
  }

  window.__resolveCohomologyObstruction = function(idsCsv) {
    (idsCsv || '').split(',').filter(Boolean).forEach(id => state.openCover.add(id));
    updateCoverAndOlog();
  };

  function updateCoverAndOlog() {
    buildStalkTree();
    const coverStalks = KB.stalks.filter(s => state.openCover.has(s.id));
    const coh = evaluateCoverCohomology(state.openCover);
    let totalPages = 0;
    coverStalks.forEach(s => { totalPages += (s.end_page - s.start_page + 1); });

    document.getElementById('metricStalks').textContent = coverStalks.length;
    document.getElementById('metricOverlaps').textContent = coh.activeR.length;
    document.getElementById('metricPages').textContent = totalPages;

    const stampEl = document.getElementById('coverGluingStamp');
    stampEl.className = 'stamp ' + (coh.verdict === 'FAIL' ? 'gate' : (coh.verdict === 'WARN' ? 'refine' : 'measured'));
    stampEl.textContent =
      `${coh.verdict === 'FAIL' ? '⊘' : (coh.verdict === 'WARN' ? '±' : '⚖')} H⁰=${coh.h0_coherence} · ||δ⁰||=${coh.mean_d0} · ${coh.verdict}`;

    renderLiveGluingBanner(coh, state.currentInvestigation && state.currentInvestigation.question);
    renderGluedOlogSvg(coverStalks, coh.activeR);
  }

  function renderGluedOlogSvg(coverStalks, activeR) {
    const wrap = document.getElementById('gluedOlogSvgWrap');
    const nodes = [];
    const nodeSeen = new Set();
    const edges = [];

    coverStalks.slice(0, 7).forEach(s => {
      const olog = s.olog || {};
      (olog.types || []).forEach(t => {
        const key = `${s.symbol}:${t.id}`;
        if (!nodeSeen.has(key)) {
          nodeSeen.add(key);
          nodes.push({ key, label: t.label, stalk: s.title });
        }
      });
      (olog.aspects || []).forEach(a => {
        edges.push({
          src: `${s.symbol}:${a.src}`,
          tgt: `${s.symbol}:${a.dst}`,
          lbl: a.label
        });
      });
    });

    const shownNodes = nodes.slice(0, 10);
    const shownSet = new Set(shownNodes.map(n => n.key));
    const shownEdges = edges.filter(e => shownSet.has(e.src) && shownSet.has(e.tgt)).slice(0, 12);

    document.getElementById('ologSummaryBadge').textContent =
      `◆ ${shownNodes.length} Olog Types · ${shownEdges.length} Commuting Aspects`;

    const W = 760, H = 265;
    const cx = W / 2, cy = H / 2;
    const rx = 270, ry = 92;
    const pos = {};
    shownNodes.forEach((n, i) => {
      const ang = (2 * Math.PI * i) / Math.max(1, shownNodes.length) - Math.PI / 2;
      pos[n.key] = { x: cx + rx * Math.cos(ang), y: cy + ry * Math.sin(ang) };
    });

    let svg = `<svg viewBox="0 0 ${W} ${H}" width="100%" height="auto" role="img" aria-label="Glued Olog Diagram">
      <defs>
        <marker id="olog-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#8C4A2E"/>
        </marker>
      </defs>`;

    shownEdges.forEach((e, idx) => {
      const p1 = pos[e.src], p2 = pos[e.tgt];
      if (!p1 || !p2) return;
      const mx = (p1.x + p2.x) / 2;
      const my = (p1.y + p2.y) / 2 - ((idx % 2 === 0) ? 15 : -15);
      const shortLbl = e.lbl.length > 26 ? e.lbl.slice(0, 24) + '…' : e.lbl;
      svg += `
        <path d="M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} Q ${mx.toFixed(1)} ${my.toFixed(1)} ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}"
              fill="none" stroke="#A67756" stroke-width="1.4" marker-end="url(#olog-arr)"/>
        <text x="${mx.toFixed(1)}" y="${(my - 3).toFixed(1)}" text-anchor="middle"
              font-family="JetBrains Mono, monospace" font-size="9.5" fill="#6B5F53">${escapeHtml(shortLbl)}</text>
      `;
    });

    shownNodes.forEach(n => {
      const p = pos[n.key];
      const lbl = n.label.length > 23 ? n.label.slice(0, 21) + '…' : n.label;
      const w = Math.max(96, lbl.length * 6.3 + 16);
      svg += `
        <g transform="translate(${(p.x - w/2).toFixed(1)}, ${(p.y - 14).toFixed(1)})">
          <rect width="${w}" height="28" rx="3" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.3"/>
          <text x="${w/2}" y="18" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="10.5" font-weight="600" fill="#1A1612">${escapeHtml(lbl)}</text>
        </g>
      `;
    });

    svg += `</svg>`;
    wrap.innerHTML = svg;
  }

  const SHORT_INV_LABELS = {
    'q-sheaf-olog-worldview': 'Sheaf of Ologged Concepts (§7.2.2)',
    'q-cat-sch-data-migration': 'Functorial DB & Adjoint Migration (Σ ⊣ Δ ⊣ Π)',
    'q-limits-vs-colimits': 'Limits vs Colimits (Pullbacks & Pushouts)',
    'q-monads-scientific-method': 'Monads & Kleisli Scientific Context',
    'q-yoneda-grothendieck-operads': 'Yoneda, Grothendieck (∫I) & Operads'
  };

  function renderInvestigationPills() {
    const wrap = document.getElementById('invPillsContainer');
    wrap.innerHTML = KB.notebook_investigations.map((inv, idx) => `
      <button class="inv-pill ${idx === 0 ? 'active' : ''}" data-inv-id="${inv.id}">
        ◆ ${escapeHtml(SHORT_INV_LABELS[inv.id] || inv.question.slice(0, 48))}
      </button>
    `).join('');

    wrap.querySelectorAll('.inv-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        const inv = KB.notebook_investigations.find(x => x.id === btn.getAttribute('data-inv-id'));
        if (!inv) return;
        wrap.querySelectorAll('.inv-pill').forEach(b => b.classList.toggle('active', b === btn));
        state.openCover = new Set(inv.open_cover);
        state.focusedStalkId = inv.open_cover[0];
        displayInvestigation(inv);
        updateCoverAndOlog();
      });
    });
  }

  function displayInvestigation(inv) {
    state.currentInvestigation = inv;
    const coh = evaluateCoverCohomology(state.openCover);
    renderLiveGluingBanner(coh, inv.question);
    document.getElementById('notebookSynthesisOutput').innerHTML = renderRichMarkdown(inv.synthesis_markdown);
    if (window.__loadPodcastForInvestigation) window.__loadPodcastForInvestigation(inv);
  }

  function runCustomSheafQuery(qStr) {
    const q = (qStr || '').trim();
    if (!q) return;
    const tokens = q.toLowerCase().split(/[^a-z0-9]+/).filter(t => t.length >= 3);

    for (const inv of KB.notebook_investigations) {
      const hay = (inv.id + ' ' + inv.question).toLowerCase();
      if (tokens.length && tokens.every(t => hay.includes(t))) {
        state.openCover = new Set(inv.open_cover);
        displayInvestigation(inv);
        updateCoverAndOlog();
        return;
      }
    }

    const scoredStalks = KB.stalks.map(s => {
      const hay = (s.title + ' ' + s.summary + ' ' + (s.keywords || []).join(' ') + ' ' + s.formal_core).toLowerCase();
      let sc = state.openCover.has(s.id) ? 2 : 0;
      tokens.forEach(t => { if (hay.includes(t)) sc += 5; });
      return { s, sc };
    }).sort((a, b) => b.sc - a.sc);

    const topStalks = scoredStalks.slice(0, 4).map(x => x.s);
    topStalks.forEach(s => state.openCover.add(s.id));
    updateCoverAndOlog();

    const pageHits = [];
    KB.pages.forEach(p => {
      const txtL = (p.txt || '').toLowerCase();
      let sc = 0;
      tokens.forEach(t => { if (txtL.includes(t)) sc += 3; });
      if (sc > 0) pageHits.push({ p, sc });
    });
    pageHits.sort((a, b) => b.sc - a.sc);

    const activeR = getActiveRestrictions();
    let md = `### Custom Glued Global Section: "${q}"\n\n`;
    md += `#### 1. Local Stalk Sections $\\mathcal{O}(U_i)$ Selected Over Cover\n`;
    topStalks.forEach(s => {
      md += `- **${s.title}** (§${s.section} [p. ${s.start_page}]): ${s.summary}\n`;
      md += `$$${s.formal_core}$$\n`;
    });

    md += `#### 2. Restriction Compatibility Audit ($\\rho_{U_i, U_i \\cap U_j}$)\n`;
    if (activeR.length) {
      activeR.slice(0, 5).forEach(r => {
        const u = stalkById[r.source], v = stalkById[r.target];
        md += `- **${u ? u.title : r.source} $\\xrightarrow{${r.formula}}$ ${v ? v.title : r.target}**: ${r.overlap} (Fidelity $f=${r.restriction_fidelity || 0.72}$, $\\|\\delta^0\\|=${r.coboundary_defect_d0 || 0.28}$)\n`;
      });
    } else {
      md += `- Add a bridging stalk in the left Open Cover panel to form a connected restriction overlap.\n`;
    }

    if (pageHits.length) {
      md += `#### 3. Verbatim PDF Page Evidence Across 609 Pages\n`;
      pageHits.slice(0, 5).forEach(h => {
        const snip = h.p.txt.slice(0, 220).replace(/\s+/g, ' ');
        md += `- [p. ${h.p.p}] **${h.p.sec || 'Spivak Text'}**: "${snip}…"\n`;
      });
      renderPageReader(pageHits[0].p.p, tokens[0] || '');
    }

    const cohNow = evaluateCoverCohomology(state.openCover);
    displayInvestigation({
      id: 'custom',
      question: q,
      open_cover: Array.from(state.openCover),
      synthesis_markdown: md,
      podcast_turns: buildCustomPodcastTurns(q, topStalks, cohNow)
    });
  }

  function buildCustomPodcastTurns(q, topStalks, coh) {
    const s0 = topStalks[0] || KB.stalks[0] || { title: 'Foundations', start_page: 1, summary: '' };
    const s1 = topStalks[1] || topStalks[0] || s0;
    const s2 = topStalks[2] || s1;
    const h0 = coh && coh.h0_coherence ? coh.h0_coherence : 0.78;
    const d0 = coh && coh.mean_d0 ? coh.mean_d0 : 0.22;
    return [
      { speaker: 'Kore', role: 'Lead Architect', cite_page: s0.start_page, start_sec: 0, end_sec: 11, text: `Welcome to our custom Deep Dive on "${q}". We've assembled an open cover starting with ${s0.title} on page ${s0.start_page}.` },
      { speaker: 'Puck', role: 'Systems Co-Host', cite_page: s0.start_page, start_sec: 11, end_sec: 23, text: `Let's look at how ${s0.title} frames this question on page ${s0.start_page}: ${s0.summary}` },
      { speaker: 'Kore', role: 'Lead Architect', cite_page: s1.start_page, start_sec: 23, end_sec: 36, text: `And when we follow the restriction morphisms to ${s1.title} on page ${s1.start_page}, we see how the local Olog types connect: ${s1.summary}` },
      { speaker: 'Puck', role: 'Systems Co-Host', cite_page: s2.start_page, start_sec: 36, end_sec: 48, text: `Then on page ${s2.start_page}, ${s2.title} provides the structural bridge across our overlap.` },
      { speaker: 'Kore', role: 'Lead Architect', cite_page: s1.start_page, start_sec: 48, end_sec: 60, text: `Our empirical Cech cohomology audit measures an H-zero coherence of ${h0} with coboundary defect ${d0} across this custom open cover.` },
      { speaker: 'Puck', role: 'Systems Co-Host', cite_page: s2.start_page, start_sec: 60, end_sec: 72, text: `Click any page citation pill in the synthesis below—or paste a Gemini API key above to synthesize this custom dialogue with live Gemini 2.5 voices.` }
    ];
  }

  document.getElementById('runGlueQueryBtn').addEventListener('click', () => {
    runCustomSheafQuery(document.getElementById('notebookQueryInput').value);
  });
  document.getElementById('notebookQueryInput').addEventListener('keydown', e => {
    if (e.key === 'Enter') runCustomSheafQuery(e.target.value);
  });
  document.getElementById('stalkFilterInput').addEventListener('input', buildStalkTree);
  document.getElementById('clearCoverBtn').addEventListener('click', () => {
    state.openCover = new Set([ KB.stalks[0].id ]);
    updateCoverAndOlog();
  });

  function resolvePresetIds(preferredIds, fallbackIndices) {
    const valid = preferredIds.filter(id => stalkById[id]);
    if (valid.length >= 2) return valid;
    return fallbackIndices.map(i => KB.stalks[i % KB.stalks.length] && KB.stalks[i % KB.stalks.length].id).filter(Boolean);
  }
  const firstObs = (KB.cohomology_obstructions && KB.cohomology_obstructions[0]) || null;
  const PRESET_COVERS = {
    sheaf: resolvePresetIds(['sheaf-of-ologged-concepts-descent', 'sheaves-and-local-to-global-gluing', 'ologs-ontology-logs', 'orders-lattices-hierarchies', 'grothendieck-construction-comma'], [0, 1, 2, 3]),
    data: resolvePresetIds(['database-schemas-instances', 'categorical-equivalence-cat-sch', 'natural-transformations-functor-cat', 'adjoint-functors-hom-iso', 'data-migration-delta-sigma-pi'], [3, 4, 5, 6]),
    universal: resolvePresetIds(['products-and-projections', 'coproducts-and-injections', 'pullbacks-and-fiber-products', 'pushouts-and-colimits-set', 'universal-limits-and-cones', 'universal-colimits-and-cocones'], [6, 7, 8, 9]),
    monad: resolvePresetIds(['scientific-agreement-worldviews', 'ologs-ontology-logs', 'monads-and-contextual-computation', 'kleisli-categories-scientific-method', 'operads-and-hierarchical-composition'], [9, 10, 11, 12]),
    obstruction: firstObs ? [firstObs.stalk_a, firstObs.stalk_b] : resolvePresetIds(['scientific-agreement-worldviews', 'pullbacks-and-fiber-products'], [0, Math.max(2, KB.stalks.length - 1)]),
    all: KB.stalks.map(s => s.id)
  };
  document.querySelectorAll('[data-preset]').forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.getAttribute('data-preset');
      state.openCover = new Set(PRESET_COVERS[key] || PRESET_COVERS.sheaf);
      document.querySelectorAll('[data-preset]').forEach(b => b.classList.toggle('active', b === btn));
      updateCoverAndOlog();
    });
  });

  // ==========================================================================
  // 5. PLATE III: INTERACTIVE SYMBOLIC SANDBOX ("Category Theory Illustrated")
  // ==========================================================================
  const SYMBOLIC_PRIMITIVES = {
    comp: {
      title: 'Morphism Composition & Commutative Triangles',
      spivakRef: '✓ Spivak §2.1.2 · p.47, p.74',
      formula: 'g \\circ f = h : X \\xrightarrow{f} Y \\xrightarrow{g} Z',
      explanation: 'Read right-to-left algebraically ("g after f"), or left-to-right geometrically along arrows. Two paths with the same start and end commute when they yield the exact same function.',
      derived: 'Law of Composition: Associativity h ∘ (g ∘ f) = (h ∘ g) ∘ f makes intermediate parentheses unnecessary — every path of arrows has a unique composite.',
      concrete: 'X = {Alice, Bob}, Y = {Dept_Eng, Dept_Math}, Z = {Bldg_4, Bldg_9}\nf(Alice) = Dept_Eng, g(Dept_Eng) = Bldg_4  ⇒  (g ∘ f)(Alice) = Bldg_4 = h(Alice).',
      tokens: [
        { sym: 'X', role: 'Domain Object (Source Set / Type)', highlight: 'node-X' },
        { sym: 'f : X \\to Y', role: 'First Morphism applied to input x ∈ X', highlight: 'edge-f' },
        { sym: '\\circ', role: 'Composition Operator ("after" / pipeline joint at Y)', highlight: 'node-Y' },
        { sym: 'g : Y \\to Z', role: 'Second Morphism receiving f(x) ∈ Y', highlight: 'edge-g' },
        { sym: '= h', role: 'Commutativity Assertion: direct arrow h equals composite path g ∘ f', highlight: 'edge-h' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs>
            <marker id="sa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker>
            <marker id="sa-hi" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#8C4A2E"/></marker>
          </defs>
          <polygon points="75,155 210,45 345,155" fill="rgba(166,119,86,0.12)" stroke="none"/>
          <text x="210" y="122" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">commutes</text>
          <line x1="95" y1="135" x2="188" y2="60" stroke="${hl==='edge-f'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-f'?3.2:1.8}" marker-end="url(#${hl==='edge-f'?'sa-hi':'sa'})"/>
          <text x="128" y="85" font-family="Fraunces, serif" font-style="italic" font-size="15" fill="#8C4A2E">f</text>
          <line x1="232" y1="60" x2="325" y2="135" stroke="${hl==='edge-g'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-g'?3.2:1.8}" marker-end="url(#${hl==='edge-g'?'sa-hi':'sa'})"/>
          <text x="290" y="85" font-family="Fraunces, serif" font-style="italic" font-size="15" fill="#8C4A2E">g</text>
          <line x1="105" y1="155" x2="315" y2="155" stroke="${hl==='edge-h'?'#8C4A2E':'#3F5E39'}" stroke-width="${hl==='edge-h'?3.2:2}" stroke-dasharray="${hl==='edge-h'?'none':'5 3'}" marker-end="url(#sa)"/>
          <text x="210" y="178" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="15" fill="#3F5E39">h = g &#8728; f</text>
          <circle cx="75" cy="155" r="22" fill="${hl==='node-X'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-X'?3:1.6}"/>
          <text x="75" y="160" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="15">X</text>
          <circle cx="210" cy="45" r="22" fill="${hl==='node-Y'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-Y'?3:1.6}"/>
          <text x="210" y="50" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="15">Y</text>
          <circle cx="345" cy="155" r="22" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="345" y="160" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="15">Z</text>
        </svg>`
    },
    prod: {
      title: 'Universal Product & Pairing ⟨f, g⟩',
      spivakRef: '✓ Spivak §2.4.1 · p.79',
      formula: '\\forall (A \\xrightarrow{f} X, A \\xrightarrow{g} Y), \\; \\exists! \\langle f, g \\rangle : A \\to X \\times Y',
      explanation: 'The product X × Y is equipped with projection arrows π₁ : X × Y → X and π₂ : X × Y → Y. Any pair of arrows f : A → X and g : A → Y factors uniquely through a single pairing arrow ⟨f, g⟩.',
      derived: 'Universal Property of Product: Hom(A, X × Y) ≅ Hom(A, X) × Hom(A, Y). Two separate queries out of A pack losslessly into one tuple arrow.',
      concrete: 'For a ∈ A: ⟨f, g⟩(a) = (f(a), g(a)) ∈ X × Y.\nProjecting back recovers the components: π₁(f(a), g(a)) = f(a) and π₂(f(a), g(a)) = g(a).',
      tokens: [
        { sym: 'X \\times Y', role: 'Universal Product Object (Cartesian grid of pairs (x,y))', highlight: 'node-prod' },
        { sym: '\\pi_1, \\pi_2', role: 'Canonical Projections extracting X and Y coordinates', highlight: 'edge-proj' },
        { sym: 'f, g', role: 'Competing test morphisms from any apex object A', highlight: 'edge-fg' },
        { sym: '\\exists! \\langle f, g \\rangle', role: 'Unique Mediating Pairing Morphism A → X × Y', highlight: 'edge-pair' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 215" width="100%" height="auto">
          <defs><marker id="pa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <circle cx="210" cy="36" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="210" y="41" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">A</text>
          <rect x="162" y="108" width="96" height="34" rx="4" fill="${hl==='node-prod'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-prod'?3:1.8}"/>
          <text x="210" y="130" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">X &times; Y</text>
          <circle cx="70" cy="175" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="70" y="180" text-anchor="middle" font-family="Fraunces, serif" font-size="14">X</text>
          <circle cx="350" cy="175" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="350" y="180" text-anchor="middle" font-family="Fraunces, serif" font-size="14">Y</text>
          <path d="M 190 44 Q 95 75 74 152" fill="none" stroke="${hl==='edge-fg'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-fg'?3:1.6}" marker-end="url(#pa)"/>
          <text x="112" y="84" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">f</text>
          <path d="M 230 44 Q 325 75 346 152" fill="none" stroke="${hl==='edge-fg'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-fg'?3:1.6}" marker-end="url(#pa)"/>
          <text x="308" y="84" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">g</text>
          <line x1="210" y1="58" x2="210" y2="104" stroke="#8C4A2E" stroke-width="${hl==='edge-pair'?3.2:2}" stroke-dasharray="4 2" marker-end="url(#pa)"/>
          <text x="246" y="86" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#8C4A2E">&exist;! &lang;f,g&rang;</text>
          <line x1="162" y1="135" x2="92" y2="166" stroke="${hl==='edge-proj'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-proj'?3:1.6}" marker-end="url(#pa)"/>
          <text x="128" y="166" font-family="Fraunces, serif" font-style="italic" font-size="13">&pi;₁</text>
          <line x1="258" y1="135" x2="328" y2="166" stroke="${hl==='edge-proj'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-proj'?3:1.6}" marker-end="url(#pa)"/>
          <text x="292" y="166" font-family="Fraunces, serif" font-style="italic" font-size="13">&pi;₂</text>
        </svg>`
    },
    coprod: {
      title: 'Universal Coproduct & Co-pairing [f, g]',
      spivakRef: '✓ Spivak §2.4.2 · p.84',
      formula: '\\forall (X \\xrightarrow{f} Z, Y \\xrightarrow{g} Z), \\; \\exists! [f, g] : X \\sqcup Y \\to Z',
      explanation: 'Dual to the product: we reverse every arrow! The coproduct X ⊔ Y receives canonical inclusions ι₁ : X → X ⊔ Y and ι₂ : Y → X ⊔ Y, and universal case-analysis [f, g] routes tagged elements into Z.',
      derived: 'Duality Principle: Reversing all arrows in the Product diagram turns projections π into inclusions ι and tuple-packing ⟨f,g⟩ into pattern-matching [f,g].',
      concrete: 'X ⊔ Y = {(1, x) | x ∈ X} ∪ {(2, y) | y ∈ Y}.\n[f, g](1, x) = f(x) and [f, g](2, y) = g(y) — the categorical foundation of tagged unions / sum types.',
      tokens: [
        { sym: 'X \\sqcup Y', role: 'Disjoint Union / Sum Object tagging origin of elements', highlight: 'node-coprod' },
        { sym: '\\iota_1, \\iota_2', role: 'Canonical Inclusion Morphisms injecting X and Y', highlight: 'edge-inc' },
        { sym: '[f, g]', role: 'Unique Case-Analysis / Co-pairing Morphism out of X ⊔ Y', highlight: 'edge-copair' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 215" width="100%" height="auto">
          <defs><marker id="ca" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <circle cx="70" cy="45" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="70" y="50" text-anchor="middle" font-family="Fraunces, serif" font-size="14">X</text>
          <circle cx="350" cy="45" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="350" y="50" text-anchor="middle" font-family="Fraunces, serif" font-size="14">Y</text>
          <rect x="162" y="72" width="96" height="34" rx="4" fill="${hl==='node-coprod'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-coprod'?3:1.8}"/>
          <text x="210" y="94" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">X &sqcup; Y</text>
          <circle cx="210" cy="182" r="20" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="210" y="187" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">Z</text>
          <line x1="92" y1="54" x2="160" y2="82" stroke="${hl==='edge-inc'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-inc'?3:1.6}" marker-end="url(#ca)"/>
          <text x="128" y="62" font-family="Fraunces, serif" font-style="italic" font-size="13">&iota;₁</text>
          <line x1="328" y1="54" x2="260" y2="82" stroke="${hl==='edge-inc'?'#8C4A2E':'#1A1612'}" stroke-width="${hl==='edge-inc'?3:1.6}" marker-end="url(#ca)"/>
          <text x="292" y="62" font-family="Fraunces, serif" font-style="italic" font-size="13">&iota;₂</text>
          <path d="M 74 68 Q 95 145 188 176" fill="none" stroke="#1A1612" stroke-width="1.6" marker-end="url(#ca)"/><text x="112" y="142" font-family="Fraunces, serif" font-style="italic" font-size="14">f</text>
          <path d="M 346 68 Q 325 145 232 176" fill="none" stroke="#1A1612" stroke-width="1.6" marker-end="url(#ca)"/><text x="308" y="142" font-family="Fraunces, serif" font-style="italic" font-size="14">g</text>
          <line x1="210" y1="108" x2="210" y2="158" stroke="#8C4A2E" stroke-width="${hl==='edge-copair'?3.2:2}" stroke-dasharray="4 2" marker-end="url(#ca)"/>
          <text x="248" y="138" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#8C4A2E">&exist;! [f,g]</text>
        </svg>`
    },
    pullback: {
      title: 'Pullback / Fiber Product X ×_Z Y',
      spivakRef: '✓ Spivak §2.5.1 · p.90, §6.1.3 p.418',
      formula: 'X \\times_Z Y = \\{ (x, y) \\in X \\times Y \\mid f(x) = g(y) \\in Z \\}',
      explanation: 'Given a cospan X →f Z ←g Y, the pullback X ×_Z Y selects only those pairs (x, y) whose images agree in the base object Z. The corner mark ⌟ signals a universal commuting square.',
      derived: 'Database & Sheaf Engine Core: Every SQL INNER JOIN on a foreign key Z and every Sheaf Gluing condition O(U) ×_{O(U∩V)} O(V) is literally a pullback square.',
      concrete: 'SQL Equivalent: SELECT x.*, y.* FROM X JOIN Y ON X.f_id = Y.g_id.\nOnly compatible pairs (x,y) that map to the same z ∈ Z survive into the fiber product.',
      tokens: [
        { sym: 'X \\times_Z Y', role: 'Pullback / Fiber Product Object at top-left corner', highlight: 'node-pb' },
        { sym: '\\lrcorner', role: 'Pullback Corner Symbol asserting universal property of the square', highlight: 'corner' },
        { sym: 'f(x) = g(y)', role: 'Compatibility Equation inside common target Z', highlight: 'node-Z' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs><marker id="pba" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <rect x="95" y="32" width="90" height="32" rx="4" fill="${hl==='node-pb'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-pb'?3:1.8}"/>
          <text x="140" y="53" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">X &times;₂ Y</text>
          <polyline points="168,72 182,72 182,58" fill="none" stroke="#8C4A2E" stroke-width="${hl==='corner'?3:2}"/>
          <rect x="265" y="32" width="60" height="32" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="295" y="53" text-anchor="middle" font-family="Fraunces, serif" font-size="14">Y</text>
          <rect x="110" y="142" width="60" height="32" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="140" y="163" text-anchor="middle" font-family="Fraunces, serif" font-size="14">X</text>
          <rect x="265" y="142" width="60" height="32" rx="4" fill="${hl==='node-Z'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-Z'?3:1.8}"/>
          <text x="295" y="163" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">Z</text>
          <line x1="185" y1="48" x2="260" y2="48" stroke="#1A1612" stroke-width="1.6" marker-end="url(#pba)"/><text x="222" y="41" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="13">p₂</text>
          <line x1="140" y1="64" x2="140" y2="137" stroke="#1A1612" stroke-width="1.6" marker-end="url(#pba)"/><text x="125" y="105" font-family="Fraunces, serif" font-style="italic" font-size="13">p₁</text>
          <line x1="170" y1="158" x2="260" y2="158" stroke="#8C4A2E" stroke-width="1.8" marker-end="url(#pba)"/><text x="215" y="175" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">f</text>
          <line x1="295" y1="64" x2="295" y2="137" stroke="#8C4A2E" stroke-width="1.8" marker-end="url(#pba)"/><text x="312" y="105" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">g</text>
        </svg>`
    },
    pushout: {
      title: 'Pushout / Amalgamated Gluing X ⊔_W Y',
      spivakRef: '✓ Spivak §2.5.2 · p.98, §6.2.3 p.444',
      formula: 'X \\sqcup_W Y = (X \\sqcup Y) / \\bigl( f(w) \\sim g(w) \\; \\forall w \\in W \\bigr)',
      explanation: 'Given a span X ←f W →g Y from a shared interface W, the pushout X ⊔_W Y takes the disjoint union X ⊔ Y and quotients (glues) every point f(w) ∈ X to its partner g(w) ∈ Y.',
      derived: 'Topological & System Gluing: Connecting two wiring diagrams along an interface W or merging two Git branches with a common ancestor W is a pushout.',
      concrete: 'If X = {a₁, a₂}, Y = {b₁, b₂}, W = {w} with f(w)=a₂ and g(w)=b₁,\nthen X ⊔_W Y has 3 equivalence classes: {a₁}, {a₂ ≡ b₁} (glued seam!), {b₂}.',
      tokens: [
        { sym: 'W', role: 'Shared Overlap / Interface Object at top-left', highlight: 'node-W' },
        { sym: 'X \\sqcup_W Y', role: 'Glued Pushout Object at bottom-right', highlight: 'node-po' },
        { sym: 'f(w) \\sim g(w)', role: 'Equivalence Relation identifying images of W', highlight: 'seam' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs><marker id="poa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <rect x="110" y="32" width="60" height="32" rx="4" fill="${hl==='node-W'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-W'?3:1.8}"/>
          <text x="140" y="53" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">W</text>
          <rect x="265" y="32" width="60" height="32" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="295" y="53" text-anchor="middle" font-family="Fraunces, serif" font-size="14">Y</text>
          <rect x="110" y="142" width="60" height="32" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="140" y="163" text-anchor="middle" font-family="Fraunces, serif" font-size="14">X</text>
          <rect x="245" y="142" width="95" height="32" rx="4" fill="${hl==='node-po'?'#F2E6DC':'#F5EFE3'}" stroke="#1A1612" stroke-width="${hl==='node-po'?3:1.8}"/>
          <text x="292" y="163" text-anchor="middle" font-family="Fraunces, serif" font-size="14" font-weight="600">X &sqcup;<tspan dy="3" font-size="10">W</tspan><tspan dy="-3"> Y</tspan></text>
          <polyline points="252,134 238,134 238,148" fill="none" stroke="#8C4A2E" stroke-width="2"/>
          <line x1="170" y1="48" x2="260" y2="48" stroke="#1A1612" stroke-width="1.6" marker-end="url(#poa)"/><text x="215" y="41" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="13">g</text>
          <line x1="140" y1="64" x2="140" y2="137" stroke="#1A1612" stroke-width="1.6" marker-end="url(#poa)"/><text x="125" y="105" font-family="Fraunces, serif" font-style="italic" font-size="13">f</text>
          <line x1="170" y1="158" x2="240" y2="158" stroke="#8C4A2E" stroke-width="1.8" marker-end="url(#poa)"/><text x="205" y="175" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#8C4A2E">&iota;₁</text>
          <line x1="295" y1="64" x2="295" y2="137" stroke="#8C4A2E" stroke-width="1.8" marker-end="url(#poa)"/><text x="312" y="105" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#8C4A2E">&iota;₂</text>
        </svg>`
    },
    nat: {
      title: 'Natural Transformation α : F ⇒ G & Naturality Square',
      spivakRef: '✓ Spivak §4.3.1 · p.295',
      formula: '\\forall (c \\xrightarrow{f} c\') \\in \\mathcal{C}, \\quad G(f) \\circ \\alpha_c = \\alpha_{c\'} \\circ F(f)',
      explanation: 'A natural transformation α : F ⇒ G between two functors F, G : C → D assigns a component arrow α_c : F(c) → G(c) to every object c so that translating along α before or after applying F(f)/G(f) yields the exact same result.',
      derived: 'Database Homomorphism: When F and G are two database states on schema C, a natural transformation α : F ⇒ G is a foreign-key-preserving homomorphism of table rows.',
      concrete: 'For every foreign key f : Employee → Department, mapping an employee row e ∈ F(Emp) via α_Emp then looking up G(f) equals looking up F(f)(e) then mapping via α_Dept.',
      tokens: [
        { sym: '\\alpha_c : F(c) \\to G(c)', role: 'Component Morphism at object c', highlight: 'alpha-c' },
        { sym: 'F(f), G(f)', role: 'Functorial images of morphism f : c → c′', highlight: 'fg-f' },
        { sym: 'G(f) \\circ \\alpha_c = \\alpha_{c\'} \\circ F(f)', role: 'Naturality Square Commutativity Condition', highlight: 'square' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs><marker id="na" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <rect x="90" y="34" width="68" height="30" rx="3" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="124" y="54" text-anchor="middle" font-family="Fraunces, serif" font-size="13">F(c)</text>
          <rect x="262" y="34" width="68" height="30" rx="3" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="296" y="54" text-anchor="middle" font-family="Fraunces, serif" font-size="13">G(c)</text>
          <rect x="90" y="144" width="68" height="30" rx="3" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="124" y="164" text-anchor="middle" font-family="Fraunces, serif" font-size="13">F(c&prime;)</text>
          <rect x="262" y="144" width="68" height="30" rx="3" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/><text x="296" y="164" text-anchor="middle" font-family="Fraunces, serif" font-size="13">G(c&prime;)</text>
          <line x1="158" y1="49" x2="257" y2="49" stroke="#8C4A2E" stroke-width="${hl==='alpha-c'?3.2:2}" marker-end="url(#na)"/><text x="210" y="41" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">&alpha;<tspan dy="3" font-size="10">c</tspan></text>
          <line x1="158" y1="159" x2="257" y2="159" stroke="#8C4A2E" stroke-width="2" marker-end="url(#na)"/><text x="210" y="176" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="14" fill="#8C4A2E">&alpha;<tspan dy="3" font-size="10">c&prime;</tspan></text>
          <line x1="124" y1="64" x2="124" y2="139" stroke="#1A1612" stroke-width="${hl==='fg-f'?3:1.6}" marker-end="url(#na)"/><text x="98" y="106" font-family="Fraunces, serif" font-style="italic" font-size="13">F(f)</text>
          <line x1="296" y1="64" x2="296" y2="139" stroke="#1A1612" stroke-width="${hl==='fg-f'?3:1.6}" marker-end="url(#na)"/><text x="322" y="106" font-family="Fraunces, serif" font-style="italic" font-size="13">G(f)</text>
          <text x="210" y="108" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#3F5E39">Naturality Square ◆</text>
        </svg>`
    },
    adj: {
      title: 'Adjunction L ⊣ R & Hom-Set Bijection',
      spivakRef: '✓ Spivak §7.1.1 · p.467, §7.1.2 p.483',
      formula: 'L \\dashv R \\iff \\text{Hom}_{\\mathcal{D}}(L(c), d) \\cong \\text{Hom}_{\\mathcal{C}}(c, R(d))',
      explanation: 'A left adjoint L : C → D and right adjoint R : D → C stand in a natural two-way bijection between arrows out of L(c) in D and arrows into R(d) in C, mediated by the unit η_c : c → R(L(c)) and counit ε_d : L(R(d)) → d.',
      derived: 'Functorial Data Migration Trinity: For any schema functor F : C → D, pullback Δ_F has left adjoint Σ_F (disjoint union / left Kan extension) and right adjoint Π_F (join / right Kan extension): Σ_F ⊣ Δ_F ⊣ Π_F.',
      concrete: 'Currying Adjunction (- × A) ⊣ (-)^A in Set:\nA function L(X) = X × A → Y is exactly the same information as a function X → Y^A = R(Y).',
      tokens: [
        { sym: 'L \\dashv R', role: 'Turnstile symbol: L is Left Adjoint to Right Adjoint R', highlight: 'turnstile' },
        { sym: '\\text{Hom}_{\\mathcal{D}}(L(c), d)', role: 'Morphisms out of free/left-migrated object L(c) in D', highlight: 'hom-L' },
        { sym: '\\text{Hom}_{\\mathcal{C}}(c, R(d))', role: 'Corresponding transposed morphisms into R(d) in C', highlight: 'hom-R' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs><marker id="aa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <rect x="28" y="30" width="150" height="150" rx="6" fill="rgba(166,119,86,0.10)" stroke="#A67756" stroke-width="1.4"/>
          <text x="103" y="50" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#8C4A2E">Category C</text>
          <rect x="242" y="30" width="150" height="150" rx="6" fill="rgba(59,110,143,0.10)" stroke="#3B6E8F" stroke-width="1.4"/>
          <text x="317" y="50" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#3B6E8F">Category D</text>
          <path d="M 155 72 Q 210 42 265 72" fill="none" stroke="#8C4A2E" stroke-width="2" marker-end="url(#aa)"/>
          <text x="210" y="50" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#8C4A2E">L (Left)</text>
          <text x="210" y="108" text-anchor="middle" font-family="Fraunces, serif" font-size="18" fill="#1A1612">&#8867;</text>
          <path d="M 265 138 Q 210 168 155 138" fill="none" stroke="#3B6E8F" stroke-width="2" marker-end="url(#aa)"/>
          <text x="210" y="168" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="13" fill="#3B6E8F">R (Right)</text>
          <text x="103" y="102" text-anchor="middle" font-family="Fraunces, serif" font-size="13">c &rarr; R(d)</text>
          <text x="317" y="102" text-anchor="middle" font-family="Fraunces, serif" font-size="13">L(c) &rarr; d</text>
        </svg>`
    },
    sheaf: {
      title: 'Sheaf Gluing Equalizer O(U ∪ V)',
      spivakRef: '✓ Spivak §7.2.2 · p.520',
      formula: '\\mathcal{O}(U \\cup V) \\xrightarrow{\\sim} \\text{eq}\\Bigl( \\mathcal{O}(U) \\times \\mathcal{O}(V) \\rightrightarrows \\mathcal{O}(U \\cap V) \\Bigr)',
      explanation: 'A presheaf O : Open(X)^op → Set is a sheaf when local sections s_U ∈ O(U) and s_V ∈ O(V) that restrict to the same value on the overlap U ∩ V glue uniquely into a global section s ∈ O(U ∪ V).',
      derived: 'Why This Powers Our Knowledge Base: Every concept stalk is an open set U_i. Our query studio glues local sections across U_i only where restriction morphisms ρ agree on U_i ∩ U_j.',
      concrete: 'If Stalk U defines Functors F : C → D and Stalk V defines Database Instances I : S → Set,\ntheir overlap U ∩ V identifies I as a Set-valued Functor, gluing them into Functorial Data Model.',
      tokens: [
        { sym: '\\mathcal{O}(U \\cup V)', role: 'Glued Global Section over union of open sets', highlight: 'global' },
        { sym: '\\mathcal{O}(U) \\times \\mathcal{O}(V)', role: 'Pair of Local Sections (s_U, s_V)', highlight: 'local' },
        { sym: '\\rightrightarrows \\mathcal{O}(U \\cap V)', role: 'Parallel Restriction Arrows ρ_{U,U∩V} and ρ_{V,U∩V} that must agree', highlight: 'overlap' }
      ],
      svg: (hl) => `
        <svg viewBox="0 0 420 210" width="100%" height="auto">
          <defs><marker id="sha" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1A1612"/></marker></defs>
          <rect x="24" y="80" width="96" height="46" rx="4" fill="#F2E6DC" stroke="#3F5E39" stroke-width="2"/>
          <text x="72" y="107" text-anchor="middle" font-family="Fraunces, serif" font-size="13" font-weight="600">O(U &cup; V)</text>
          <line x1="120" y1="103" x2="158" y2="103" stroke="#3F5E39" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#sha)"/>
          <rect x="162" y="80" width="108" height="46" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="216" y="107" text-anchor="middle" font-family="Fraunces, serif" font-size="13">O(U) &times; O(V)</text>
          <line x1="270" y1="95" x2="314" y2="95" stroke="#8C4A2E" stroke-width="1.8" marker-end="url(#sha)"/>
          <line x1="270" y1="111" x2="314" y2="111" stroke="#3B6E8F" stroke-width="1.8" marker-end="url(#sha)"/>
          <text x="292" y="86" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#8C4A2E">&rho;<tspan dy="2" font-size="7.5">U</tspan></text>
          <text x="292" y="128" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9" fill="#3B6E8F">&rho;<tspan dy="2" font-size="7.5">V</tspan></text>
          <rect x="318" y="80" width="88" height="46" rx="4" fill="#F5EFE3" stroke="#1A1612" stroke-width="1.6"/>
          <text x="362" y="107" text-anchor="middle" font-family="Fraunces, serif" font-size="13">O(U &cap; V)</text>
        </svg>`
    }
  };

  function renderSymbolicSandbox(symKey, tokenIdx = 0) {
    const item = SYMBOLIC_PRIMITIVES[symKey] || SYMBOLIC_PRIMITIVES.comp;
    document.querySelectorAll('#symSelector .sym-btn').forEach(b => {
      b.setAttribute('aria-selected', String(b.getAttribute('data-sym') === symKey));
    });
    document.getElementById('symSpivakRef').textContent = item.spivakRef;
    document.getElementById('symTitle').textContent = item.title;
    document.getElementById('symFormulaDisplay').innerHTML = convertLatexTokensToHtml(item.formula);
    document.getElementById('symExplanation').textContent = item.explanation;
    document.getElementById('symConcreteTrace').textContent = item.concrete;
    document.getElementById('symDerivedText').innerHTML = `<strong>Invariant Enacted:</strong> ${escapeHtml(item.derived)}`;

    const tokStrip = document.getElementById('symTokenStrip');
    tokStrip.innerHTML = item.tokens.map((t, i) => `
      <button class="token-chip ${i === tokenIdx ? 'active' : ''}" data-tok-idx="${i}">
        ${convertLatexTokensToHtml(t.sym)}
      </button>
    `).join('');

    const activeTok = item.tokens[tokenIdx] || item.tokens[0];
    document.getElementById('symTokenInspector').innerHTML = `
      <strong>Selected Symbolic Token: ${convertLatexTokensToHtml(activeTok.sym)}</strong>
      <div style="margin-top:3px">${escapeHtml(activeTok.role)}</div>
    `;
    document.getElementById('symDiagramSvgWrap').innerHTML = item.svg(activeTok.highlight);

    tokStrip.querySelectorAll('.token-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        renderSymbolicSandbox(symKey, Number(btn.getAttribute('data-tok-idx')));
      });
    });
  }

  document.querySelectorAll('#symSelector .sym-btn').forEach(btn => {
    btn.addEventListener('click', () => renderSymbolicSandbox(btn.getAttribute('data-sym'), 0));
  });
  renderSymbolicSandbox('comp', 0);

  // ==========================================================================
  // 6. PLATE IV: 30 CONCEPT STALKS, 877 DECLARATIONS & 3D POSET ATLAS
  // ==========================================================================
  function renderStalkCards() {
    const chFilter = document.getElementById('chapterFilterSelect').value;
    const list = KB.stalks.filter(s => chFilter === 'all' || String(s.chapter) === chFilter);
    document.getElementById('stalkCardsGrid').innerHTML = list.map(s => `
      <article class="stalk-card">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.35rem">
            <span class="stamp ratified">◆ Ch ${s.chapter} · §${s.section}</span>
            <button class="cite-pill" onclick="window.__jumpToPage(${s.start_page}, '')">§ pp.${s.start_page}–${s.end_page}</button>
          </div>
          <h3 class="serif" style="font-size:1.15rem;margin-bottom:0.35rem">${escapeHtml(s.title)}</h3>
          <p style="font-size:0.83rem;color:var(--ink-2);margin-bottom:0.55rem">${escapeHtml(s.summary)}</p>
          <div class="math-display" style="font-size:0.86rem;padding:0.45rem 0.6rem;margin:0.45rem 0">
            ${convertLatexTokensToHtml(s.formal_core)}
          </div>
        </div>
        <div style="padding-top:0.5rem;border-top:1px dotted var(--rule);display:flex;justify-content:space-between;align-items:center;font-family:var(--f-mono);font-size:0.70rem;color:var(--ink-3)">
          <span>${((s.olog && s.olog.types) || []).length} Olog types · ${s.extracted_items_count || 0} items</span>
          <button class="preset-btn" onclick="window.__addStalkToStudio('${s.id}')">+ Open Cover</button>
        </div>
      </article>
    `).join('');
  }

  function renderDeclarationsList() {
    const chFilter = document.getElementById('chapterFilterSelect').value;
    const kindFilter = document.getElementById('declKindSelect').value;
    const q = (document.getElementById('declSearchInput').value || '').trim().toLowerCase();

    const allItems = KB.formal_items.length
      ? KB.formal_items
      : KB.stalks.flatMap(s => s.formal_items || []);

    const filtered = allItems.filter(it => {
      if (chFilter !== 'all' && String(it.chapter) !== chFilter) return false;
      if (kindFilter !== 'all' && it.kind !== kindFilter) return false;
      if (q && !(it.id + ' ' + it.kind + ' ' + (it.title || '') + ' ' + (it.text || '')).toLowerCase().includes(q)) return false;
      return true;
    });

    document.getElementById('declCountLabel').textContent =
      `Showing ${Math.min(80, filtered.length)} of ${filtered.length} formal declarations (from 877 total in Spivak)`;

    document.getElementById('declListContainer').innerHTML = filtered.slice(0, 80).map(it => `
      <div style="background:var(--paper);border:1px solid var(--rule);padding:0.75rem 0.9rem">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span class="mono" style="font-weight:600;color:var(--accent-text)">${escapeHtml(it.id)} ${it.title ? '· ' + escapeHtml(it.title) : ''}</span>
          <button class="cite-pill" onclick="window.__jumpToPage(${it.page}, '${escapeHtml(it.number || '')}')">§ p.${it.page}</button>
        </div>
        <div style="font-size:0.85rem;color:var(--ink-2)">${convertLatexTokensToHtml((it.text || '').slice(0, 420))}</div>
      </div>
    `).join('');
  }

  document.querySelectorAll('.subview-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      const sv = tab.getAttribute('data-subview');
      state.activeSubview = sv;
      document.querySelectorAll('.subview-tab').forEach(t => t.setAttribute('aria-selected', String(t === tab)));
      document.getElementById('subview-stalks').style.display = sv === 'stalks' ? 'block' : 'none';
      document.getElementById('subview-declarations').style.display = sv === 'declarations' ? 'block' : 'none';
      document.getElementById('subview-atlas3d').style.display = sv === 'atlas3d' ? 'block' : 'none';
      if (sv === 'declarations') renderDeclarationsList();
      if (sv === 'atlas3d') start3dLoop(); else stop3dLoop();
    });
  });

  const chSelectEl = document.getElementById('chapterFilterSelect');
  if (chSelectEl && KB.chapters && KB.chapters.length) {
    chSelectEl.innerHTML = `<option value="all">All ${KB.chapters.length} Chapters</option>` +
      KB.chapters.map(c => `<option value="${c.chapter}">Ch ${c.chapter} · ${escapeHtml(c.title.split(':').slice(-1)[0].trim())}</option>`).join('');
  }
  document.getElementById('chapterFilterSelect').addEventListener('change', () => {
    renderStalkCards();
    if (state.activeSubview === 'declarations') renderDeclarationsList();
  });
  document.getElementById('declSearchInput').addEventListener('input', renderDeclarationsList);
  document.getElementById('declKindSelect').addEventListener('change', renderDeclarationsList);
  renderStalkCards();

  // ==========================================================================
  // 7. ON-DEMAND 3D ALEXANDROV POSET FIBER-BUNDLE RENDERER
  // ==========================================================================
  const canvas3d = document.getElementById('sheaf3dCanvas');
  const ctx3d = canvas3d.getContext('2d');
  let rafId = null;
  let camYaw = 0.55, camPitch = 0.32, camDist = 390;
  let show2Simplices = true;
  let dragging3d = false, lastX = 0, lastY = 0;
  let projectedNodes = [];

  canvas3d.addEventListener('mousedown', e => { dragging3d = true; lastX = e.clientX; lastY = e.clientY; });
  window.addEventListener('mouseup', () => { dragging3d = false; });
  window.addEventListener('mousemove', e => {
    if (!dragging3d) return;
    camYaw += (e.clientX - lastX) * 0.007;
    camPitch = Math.max(-1.1, Math.min(1.1, camPitch + (e.clientY - lastY) * 0.007));
    lastX = e.clientX; lastY = e.clientY;
  });
  canvas3d.addEventListener('wheel', e => {
    e.preventDefault();
    camDist = Math.max(190, Math.min(680, camDist + e.deltaY * 0.25));
  }, { passive: false });

  canvas3d.addEventListener('click', e => {
    const rect = canvas3d.getBoundingClientRect();
    const mx = e.clientX - rect.left, my = e.clientY - rect.top;
    for (const n of projectedNodes) {
      if (Math.hypot(mx - n.sx, my - n.sy) <= n.r + 5) {
        state.focusedStalkId = n.stalk.id;
        state.openCover.add(n.stalk.id);
        updateCoverAndOlog();
        update3dHud(n.stalk);
        break;
      }
    }
  });

  document.getElementById('toggle2SimplicesBtn').addEventListener('click', e => {
    show2Simplices = !show2Simplices;
    e.target.classList.toggle('active', show2Simplices);
    e.target.textContent = `2-Simplices: ${show2Simplices ? 'ON' : 'OFF'}`;
  });
  document.getElementById('reset3dCamBtn').addEventListener('click', () => {
    camYaw = 0.55; camPitch = 0.32; camDist = 390;
  });

  function update3dHud(s) {
    if (!s) return;
    document.getElementById('hud3dBox').innerHTML = `
      <div>
        <strong style="color:#E8C3A4">${escapeHtml(s.title)}</strong>
        <span class="mono" style="margin-left:8px;opacity:0.8">Ch ${s.chapter} · §${s.section} · pp.${s.start_page}–${s.end_page}</span>
        <div style="font-size:0.78rem;opacity:0.88;margin-top:2px">${escapeHtml(s.summary)}</div>
      </div>
      <button class="cite-pill" onclick="window.__jumpToPage(${s.start_page}, '')">Open p.${s.start_page}</button>
    `;
  }
  update3dHud(stalkById['sheaf-of-ologged-concepts-descent']);

  function project3d(pt, W, H) {
    const [x, y, z] = pt || [0, 0, 0];
    const cy = Math.cos(camYaw), sy = Math.sin(camYaw);
    const cp = Math.cos(camPitch), sp = Math.sin(camPitch);
    const x1 = x * cy - z * sy;
    const z1 = x * sy + z * cy;
    const y2 = y * cp - z1 * sp;
    const z2 = y * sp + z1 * cp + camDist;
    const fov = 340 / Math.max(60, z2);
    return { sx: W / 2 + x1 * fov, sy: H / 2 - y2 * fov, z: z2, fov };
  }

  function draw3dScene() {
    if (state.activeSubview !== 'atlas3d') { rafId = null; return; }
    const rect = canvas3d.parentElement.getBoundingClientRect();
    if (canvas3d.width !== Math.floor(rect.width) || canvas3d.height !== Math.floor(rect.height)) {
      canvas3d.width = Math.floor(rect.width);
      canvas3d.height = Math.floor(rect.height);
    }
    const W = canvas3d.width, H = canvas3d.height;
    ctx3d.clearRect(0, 0, W, H);
    if (!dragging3d) camYaw += 0.0018;

    const pMap = {};
    KB.stalks.forEach(s => { pMap[s.id] = { stalk: s, ...project3d(s.pos3d, W, H) }; });

    if (show2Simplices) {
      KB.two_simplices.forEach(sim => {
        const [u, v, w] = sim.vertices.map(id => pMap[id]);
        if (!u || !v || !w) return;
        ctx3d.beginPath();
        ctx3d.moveTo(u.sx, u.sy); ctx3d.lineTo(v.sx, v.sy); ctx3d.lineTo(w.sx, w.sy);
        ctx3d.closePath();
        ctx3d.fillStyle = 'rgba(166, 119, 86, 0.16)';
        ctx3d.fill();
      });
    }

    KB.restriction_morphisms.forEach(r => {
      const u = pMap[r.source], v = pMap[r.target];
      if (!u || !v) return;
      const act = state.openCover.has(r.source) && state.openCover.has(r.target);
      ctx3d.beginPath();
      ctx3d.moveTo(u.sx, u.sy); ctx3d.lineTo(v.sx, v.sy);
      ctx3d.strokeStyle = act ? '#DBA882' : 'rgba(245,239,227,0.18)';
      ctx3d.lineWidth = act ? 1.8 : 0.9;
      ctx3d.stroke();
    });

    projectedNodes = Object.values(pMap).sort((a, b) => b.z - a.z);
    projectedNodes.forEach(n => {
      const inCov = state.openCover.has(n.stalk.id);
      const r = Math.max(4.5, (inCov ? 8 : 5.5) * n.fov);
      n.r = r;
      ctx3d.beginPath();
      ctx3d.arc(n.sx, n.sy, r, 0, Math.PI * 2);
      ctx3d.fillStyle = inCov ? '#DBA882' : '#799070';
      ctx3d.fill();
      ctx3d.strokeStyle = '#1A1612';
      ctx3d.lineWidth = 1.4;
      ctx3d.stroke();
      if (inCov || n.fov > 0.92) {
        ctx3d.font = '600 10px "JetBrains Mono", monospace';
        ctx3d.fillStyle = '#F5EFE3';
        ctx3d.fillText(n.stalk.title.slice(0, 22), n.sx + r + 4, n.sy + 3);
      }
    });

    rafId = requestAnimationFrame(draw3dScene);
  }

  function start3dLoop() { if (!rafId) rafId = requestAnimationFrame(draw3dScene); }
  function stop3dLoop() { if (rafId) { cancelAnimationFrame(rafId); rafId = null; } }

  // ==========================================================================
  // 8. PLATE V: COURSE BLUEPRINT MODULES ("Category Theory Illustrated")
  // ==========================================================================
  const DEFAULT_COURSE_MODULES = [
    {
      vol: 'ARC I · LAWS',
      stamp: '◆ Foundation',
      title: 'Sets, Functions & Commutative Ologs',
      symbols: 'f : X \\to Y, \\quad g \\circ f = h, \\quad \\text{id}_X',
      keyConcept: 'Every box-and-arrow ontology log (Olog) is a rigorous mathematical specification in Set where path equivalence equals functional equality.',
      whyItMatters: 'Eliminates ambiguous English requirements by turning domain models into testable commuting equations.',
      lab: 'Walkable Olog Compiler: Draw a 5-object domain schema, populate finite sets, and run an automated commutativity checker.',
      pages: [11, 47]
    },
    {
      vol: 'ARC I · LAWS',
      stamp: '◆ Universal Cones',
      title: 'Universal Constructions Through Symbols: Products, Pullbacks & Gluing',
      symbols: 'X \\times Y, \\quad X \\sqcup Y, \\quad X \\times_Z Y, \\quad X \\sqcup_W Y',
      keyConcept: 'Products/Pullbacks (limits) pack and filter compatible tuples; Coproducts/Pushouts (colimits) tag and glue disjoint parts along shared seams.',
      whyItMatters: 'Unifies SQL INNER JOINs, sum types, and topological space gluing under a single universal arrow existence-and-uniqueness pattern.',
      lab: 'Interactive Pullback & Pushout Builder: Manipulate span/cospan tables and inspect the generated universal mediating morphism u.',
      pages: [79, 90]
    },
    {
      vol: 'ARC II · OBSERVED',
      stamp: '⚖ Order & Paths',
      title: 'Posets, Monoids & Path Categories of Graphs',
      symbols: '(P, \\le), \\quad (M, e, \\star), \\quad \\text{Path}(G)',
      keyConcept: 'A poset is a category with at most one arrow between any two objects; a monoid is a category with a single object; every directed graph generates a free path category.',
      whyItMatters: 'Bridges discrete math (DAGs, state machines, permission lattices) directly into categorical functoriality.',
      lab: 'Graph Congruence Explorer: Add path equivalence equations to a state-machine graph G and compute the quotient category.',
      pages: [118, 173]
    },
    {
      vol: 'ARC III · PROSPECTS',
      stamp: '✓ Functorial DB',
      title: 'Categories, Functors & The Functorial Data Model',
      symbols: 'F : \\mathcal{C} \\to \\mathcal{D}, \\quad I : \\mathcal{S} \\to \\mathbf{Set}, \\quad \\alpha : I \\Rightarrow J',
      keyConcept: 'A database schema S is a finitely presented category; a database state is a Set-valued functor I : S → Set; a schema mapping is a functor F : C → D.',
      whyItMatters: 'Replaces brittle ad-hoc ORM migrations with mathematically verified functorial transformations.',
      lab: 'Functorial Schema Studio: Build a live categorical schema S, populate functor state tables I : S → Set, and validate naturality squares.',
      pages: [253, 271]
    },
    {
      vol: 'ARC III · PROSPECTS',
      stamp: '✓ Compositionality',
      title: 'Profunctors, Kleisli Monads & Operads of Wiring Diagrams',
      symbols: '(T, \\eta, \\mu), \\quad \\mathcal{C}_T, \\quad \\mathcal{O}(c_1, \\dots, c_n; d)',
      keyConcept: 'Monads encapsulate context/effects inside Kleisli composition g ∘_K f; Operads formalize hierarchical zoomed wiring diagrams of interacting systems.',
      whyItMatters: 'Provides compositional semantics for impure data pipelines, probabilistic transitions, and nested cyber-physical architectures.',
      lab: 'Kleisli & Operad Wiring Sandbox: Compose effectful queries and nest hierarchical boxes using operadic substitution.',
      pages: [341, 379]
    },
    {
      vol: 'ARC IV · ASSAY',
      stamp: '⚖ Representability',
      title: 'General Limits, Colimits & The Yoneda Embedding',
      symbols: '\\varprojlim_J D, \\quad \\varinjlim_J D, \\quad \\text{Nat}(\\text{Hom}_{\\mathcal{C}}(c, -), F) \\cong F(c)',
      keyConcept: 'The Yoneda Lemma proves that any object c is completely determined up to isomorphism by the web of relationships Hom(c, -) it maintains with all other objects.',
      whyItMatters: 'Explains why universal properties and RDF/graph triples uniquely characterize complex structures without peeking inside their implementation.',
      lab: 'Visual Yoneda Inspector: Reconstruct a hidden object and its database state purely from its representable functor probe.',
      pages: [418, 460]
    },
    {
      vol: 'ARC V · YIELD',
      stamp: '◆ Topos & Sheaves',
      title: 'Adjoint Data Migration (Σ ⊣ Δ ⊣ Π) & Sheaf Gluing',
      symbols: '\\Sigma_F \\dashv \\Delta_F \\dashv \\Pi_F, \\quad \\int_{\\mathcal{C}} I, \\quad \\mathcal{O}(U \\cup V)',
      keyConcept: 'Every schema functor F induces an adjoint triple (Σ_F, Δ_F, Π_F) for data migration, while sheaves enforce global consistency of local data sections across open covers.',
      whyItMatters: 'Culmination of the course: learners build a working Sheaf Knowledge Graph and execute verified Σ/Δ/Π ETL migrations.',
      lab: 'Capstone Sheaf & Kan Migration Lab: Execute Δ_F, Σ_F, and Π_F queries on a real multi-stalk knowledge base and audit the sheaf equalizer.',
      pages: [467, 520]
    }
  ];

  const maxCorpusPages = (KB.book && KB.book.total_pages) || 609;
  const COURSE_MODULES = (KB.book && Array.isArray(KB.book.course_modules) && KB.book.course_modules.length)
    ? KB.book.course_modules.map((cm, idx) => ({
        vol: `SUITE 0${idx + 1} · CONSOLIDATED ROUTER`,
        stamp: `◆ ${(cm.stalks || []).length} Stalks`,
        title: cm.title,
        symbols: Array.isArray(cm.symbols) ? cm.symbols.join(', \\quad ') : (cm.symbols || 'U_i \\xrightarrow{\\rho} U_j'),
        keyConcept: cm.keyConcept || cm.key_concept || '',
        whyItMatters: cm.whyItMatters || cm.why_it_matters || '',
        lab: cm.lab || '',
        pages: (cm.pages || [1, 2]).map(p => Math.max(1, Math.min(maxCorpusPages, Number(p) || 1)))
      }))
    : DEFAULT_COURSE_MODULES.map(m => ({
        ...m,
        pages: (m.pages || [1]).map(p => Math.max(1, Math.min(maxCorpusPages, Math.round((p * maxCorpusPages) / 609))))
      }));

  document.getElementById('courseModulesGrid').innerHTML = COURSE_MODULES.map(m => `
    <article class="module-card">
      <div class="m-head">
        <span class="mono" style="font-size:0.69rem;color:var(--ink-3)">${escapeHtml(m.vol)}</span>
        <span class="stamp ratified">◆ ${escapeHtml(m.stamp.replace(/^[◆⚖✓±⊘]\s*/, ''))}</span>
      </div>
      <h3 class="serif" style="font-size:1.15rem">${escapeHtml(m.title)}</h3>
      <div class="math-display" style="font-size:0.86rem;padding:0.45rem;margin:0.2rem 0">
        ${convertLatexTokensToHtml(m.symbols)}
      </div>
      <div class="callout-box">
        <strong>Key Concept</strong>
        ${escapeHtml(m.keyConcept)}
      </div>
      <div style="font-size:0.79rem;color:var(--ink-2);padding:0.45rem 0;border-top:1px dotted var(--rule);border-bottom:1px dotted var(--rule)">
        <strong class="mono" style="font-size:0.68rem;text-transform:uppercase;color:var(--accent-text)">Walkable Lab:</strong> ${escapeHtml(m.lab)}
        <div style="margin-top:5px">
          ${m.pages.map(p => `<button class="cite-pill" onclick="window.__jumpToPage(${p}, '')">§ p.${p}</button>`).join(' ')}
        </div>
      </div>
      <div class="callout-box" style="border-left-color:var(--ax-science);margin-top:auto">
        <strong>Why It Matters</strong>
        ${escapeHtml(m.whyItMatters)}
      </div>
    </article>
  `).join('');

  // ==========================================================================
  // 9. SLIDE-OVER VERBATIM CORPUS READER DRAWER
  // ==========================================================================
  const drawer = document.getElementById('readerDrawer');
  const openBtn = document.getElementById('openReaderBtn');
  document.getElementById('openReaderBtn').addEventListener('click', () => drawer.classList.toggle('open'));
  document.getElementById('closeReaderBtn').addEventListener('click', () => drawer.classList.remove('open'));

  function renderPageReader(pageNum, term) {
    const p = Math.max(1, Math.min(maxCorpusPages, parseInt(pageNum, 10) || 1));
    state.currentPage = p;
    if (term !== undefined) state.highlightTerm = term;

    document.getElementById('pageNumInput').value = p;
    document.getElementById('pageSlider').value = p;
    openBtn.textContent = `📖 Page Reader (p.${p})`;
    const mobileReaderBtn = document.getElementById('mobileDockReaderBtn');
    if (mobileReaderBtn) mobileReaderBtn.textContent = `📖 p.${p}`;
    document.getElementById('openRawPdfLink').href = `__PDF_REL_PATH__#page=${p}`;

    const pObj = pageByNum[p] || { p, ch: 0, sec: `Loading ${maxCorpusPages}-page bundle…`, wc: 0, txt: 'Loading verbatim page text…', stalks: [], items: [] };
    const sBadges = (pObj.stalks || []).map(sid => {
      const st = stalkById[sid];
      return st ? `<span class="stamp ratified">◆ ${escapeHtml(st.title)}</span>` : '';
    }).join(' ');

    document.getElementById('readerPageMeta').innerHTML = `
      <div style="display:flex;justify-content:space-between;font-family:var(--f-mono);font-size:0.75rem;color:var(--accent-text);font-weight:600">
        <span>Corpus Page ${pObj.p} of ${maxCorpusPages} · Chapter ${pObj.ch}</span>
        <span>${pObj.wc || 0} words</span>
      </div>
      <div style="font-size:0.84rem;color:var(--ink-2);margin-top:2px">${escapeHtml(pObj.sec || 'Frontmatter / Index')}</div>
      ${sBadges ? `<div style="margin-top:6px;display:flex;gap:4px;flex-wrap:wrap">${sBadges}</div>` : ''}
    `;

    let rawHtml = renderRichMarkdown(pObj.txt || '(Diagram / Blank Page in PDF — click "Open PDF ↗" above to inspect vector graphic)');
    if (state.highlightTerm && state.highlightTerm.length >= 2) {
      const safe = state.highlightTerm.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      rawHtml = rawHtml.replace(new RegExp(`(<[^>]+>)|(${safe})`, 'gi'), (m, tag, hit) => tag ? tag : `<mark class="hl">${hit}</mark>`);
    }
    document.getElementById('readerPageText').innerHTML = rawHtml;
  }

  document.getElementById('prevPageBtn').addEventListener('click', () => renderPageReader(state.currentPage - 1));
  document.getElementById('nextPageBtn').addEventListener('click', () => renderPageReader(state.currentPage + 1));
  document.getElementById('pageNumInput').addEventListener('change', e => renderPageReader(e.target.value));
  document.getElementById('pageSlider').addEventListener('input', e => renderPageReader(e.target.value));

  // Debounced full-corpus search
  let searchTimer = null;
  const searchInput = document.getElementById('fullBookSearchInput');
  const searchResults = document.getElementById('bookSearchResults');
  searchInput.addEventListener('input', () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      const q = searchInput.value.trim().toLowerCase();
      if (q.length < 2) { searchResults.style.display = 'none'; return; }
      const hits = [];
      for (let i = 0; i < KB.pages.length; i++) {
        const pg = KB.pages[i];
        const idx = (pg.txt || '').toLowerCase().indexOf(q);
        if (idx !== -1) {
          const snip = pg.txt.slice(Math.max(0, idx - 35), Math.min(pg.txt.length, idx + 95)).replace(/\s+/g, ' ');
          hits.push({ p: pg.p, sec: pg.sec, snip });
          if (hits.length >= 20) break;
        }
      }
      searchResults.style.display = 'block';
      searchResults.innerHTML = hits.length
        ? hits.map(h => `
            <div style="padding:5px 7px;border-bottom:1px dotted var(--rule);cursor:pointer;font-size:0.78rem"
                 onclick="window.__jumpToPage(${h.p}, '${escapeHtml(q.replace(/'/g, "\\'"))}')">
              <div class="mono" style="color:var(--accent-text);font-weight:600">p.${h.p} · ${escapeHtml(h.sec)}</div>
              <div style="color:var(--ink-2)">…${escapeHtml(h.snip)}…</div>
            </div>
          `).join('')
        : `<div style="padding:6px;font-size:0.78rem;color:var(--ink-3)">No matches in ${maxCorpusPages} pages for "${escapeHtml(q)}"</div>`;
    }, 110);
  });

  // ==========================================================================
  // 8. NOTEBOOKLM "DEEP DIVE" DUAL-HOST NEURAL PODCAST & GEMINI 2.5 TTS PLAYER
  // ==========================================================================
  const audioEl = document.getElementById('notebookPodcastAudio');
  const playPauseBtn = document.getElementById('podcastPlayPauseBtn');
  const marginaliaPlayBtn = document.getElementById('audioBriefBtn');
  const scrubSlider = document.getElementById('podcastScrubSlider');
  const timeLabel = document.getElementById('podcastTimeLabel');
  const speedBtn = document.getElementById('podcastSpeedBtn');
  const transcriptBtn = document.getElementById('toggleTranscriptBtn');
  const transcriptDrawer = document.getElementById('podcastTranscriptDrawer');
  const activeSubtitle = document.getElementById('podcastActiveSubtitle');
  const visualCueText = document.getElementById('podcastVisualCueText');
  const cuePageBtn = document.getElementById('podcastCuePageBtn');
  const actButtons = Array.from(document.querySelectorAll('#podcastActBar .podcast-act-step'));
  const hostBadgeKore = document.getElementById('hostBadgeKore');
  const hostBadgePuck = document.getElementById('hostBadgePuck');
  const waveBars = Array.from(document.querySelectorAll('#podcastWaveform span'));
  const geminiConfigBtn = document.getElementById('toggleGeminiTtsConfigBtn');
  const geminiConfigDrawer = document.getElementById('geminiTtsConfigDrawer');
  const geminiKeyInput = document.getElementById('geminiApiKeyInput');
  const geminiVoiceSelect = document.getElementById('geminiVoicePairSelect');
  const runLiveGeminiBtn = document.getElementById('runLiveGeminiTtsBtn');
  const geminiStatusMsg = document.getElementById('geminiTtsStatusMsg');
  const podcastEngineBadge = document.getElementById('podcastEngineBadge');

  const bundleScriptEl = document.querySelector('script[src*="sheaf_pages_bundle.js"]');
  const bundleBaseDir = bundleScriptEl
    ? bundleScriptEl.getAttribute('src').replace(/\/?sheaf_pages_bundle\.js.*$/, '')
    : 'data';

  let currentTurns = [];
  let waveTimer = null;
  const speedSteps = [1.0, 1.15, 1.25, 1.5];
  let speedIdx = 0;

  try {
    const savedKey = localStorage.getItem('CETI_GEMINI_API_KEY');
    if (savedKey && geminiKeyInput) geminiKeyInput.value = savedKey;
  } catch (e) {}

  function fmtSec(sec) {
    if (!Number.isFinite(sec) || sec < 0) return '0:00';
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }

  function updateButtonsState(playing) {
    state.audioPlaying = playing;
    if (playPauseBtn) playPauseBtn.textContent = playing ? '⏸ Pause Deep Dive' : '▶ Play Deep Dive';
    if (marginaliaPlayBtn) marginaliaPlayBtn.textContent = playing ? '⏸ Pause Deep Dive Podcast' : '🎙️ Play Deep Dive Podcast';
    const mobilePlayBtn = document.getElementById('mobileDockPlayBtn');
    if (mobilePlayBtn) {
      mobilePlayBtn.textContent = playing ? '⏸ Playing' : '▶ Deep Dive';
      mobilePlayBtn.classList.toggle('active', playing);
    }
    if (playing) {
      if (!waveTimer) {
        waveTimer = setInterval(() => {
          waveBars.forEach((b, i) => {
            const h = 5 + Math.floor(Math.abs(Math.sin(Date.now() / 140 + i * 0.9)) * 16);
            b.style.height = `${h}px`;
          });
        }, 90);
      }
    } else {
      if (waveTimer) { clearInterval(waveTimer); waveTimer = null; }
      waveBars.forEach((b, i) => { b.style.height = `${6 + (i % 3) * 4}px`; });
    }
  }

  function highlightActiveSpeaker(speaker) {
    if (!hostBadgeKore || !hostBadgePuck) return;
    const isKore = speaker !== 'Puck';
    hostBadgeKore.style.transform = isKore ? 'scale(1.04)' : 'scale(1.0)';
    hostBadgeKore.style.boxShadow = isKore ? '0 0 0 2px var(--accent-text)' : 'none';
    hostBadgePuck.style.transform = !isKore ? 'scale(1.04)' : 'scale(1.0)';
    hostBadgePuck.style.boxShadow = !isKore ? '0 0 0 2px var(--good)' : 'none';
  }

  window.__seekPodcastTo = function(sec, citePage) {
    if (audioEl && audioEl.src) {
      audioEl.currentTime = Number(sec) || 0;
      audioEl.play().then(() => updateButtonsState(true)).catch(() => {});
    }
    if (citePage) {
      renderPageReader(Number(citePage), '');
    }
  };

  function getTurnActIndex(turn, idx) {
    const actStr = String(turn && turn.act || '');
    if (actStr.includes('Act IV')) return 3;
    if (actStr.includes('Act III')) return 2;
    if (actStr.includes('Act II')) return 1;
    if (actStr.includes('Act I')) return 0;
    if (idx >= 8) return 3;
    if (idx >= 5) return 2;
    if (idx >= 2) return 1;
    return 0;
  }

  function syncActiveTurnUi(turn, idx) {
    if (!turn) return;
    highlightActiveSpeaker(turn.speaker);
    const isKore = turn.speaker !== 'Puck';
    const col = isKore ? 'var(--accent-text)' : 'var(--good)';
    const actIdx = getTurnActIndex(turn, idx);
    actButtons.forEach((b, bIdx) => b.classList.toggle('active', bIdx === actIdx));
    if (visualCueText) {
      const rawCue = turn.visual_cue || `Inspecting ${turn.act || 'diagram'} on page ${turn.cite_page || 1}`;
      const cleanCue = rawCue.replace(/^[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\uFE0F\s]+/u, '');
      visualCueText.innerHTML = `👁️ <strong>${escapeHtml(turn.act || 'Visual Cue')}:</strong> ${escapeHtml(cleanCue)}`;
    }
    if (cuePageBtn) {
      const cp = turn.cite_page || 1;
      cuePageBtn.textContent = `§ p.${cp}`;
      cuePageBtn.setAttribute('onclick', `window.__jumpToPage(${cp}, '')`);
    }
    if (activeSubtitle) {
      activeSubtitle.style.borderLeftColor = col;
      activeSubtitle.innerHTML = `<span class="mono" style="color:${col};font-weight:600">${isKore ? '🎙️' : '🎧'} [Turn ${idx + 1}/${currentTurns.length}] ${escapeHtml(turn.speaker)} · ${escapeHtml(turn.role || 'Host')}:</span> ${escapeHtml(turn.text)} <button class="cite-pill" style="margin-left:6px" onclick="window.__jumpToPage(${turn.cite_page || 1}, '')">§ p.${turn.cite_page || 1}</button>`;
    }
    if (transcriptDrawer) {
      transcriptDrawer.querySelectorAll('.podcast-turn-row').forEach((r, rIdx) => {
        r.style.background = rIdx === idx ? 'var(--accent-soft)' : 'transparent';
      });
    }
  }

  actButtons.forEach((btn, actIdx) => {
    btn.addEventListener('click', () => {
      const targetTurnIdx = [0, 2, 5, 8][actIdx] || 0;
      const t = currentTurns[Math.min(targetTurnIdx, Math.max(0, currentTurns.length - 1))];
      if (t) {
        syncActiveTurnUi(t, targetTurnIdx);
        window.__seekPodcastTo(t.start_sec || 0, t.cite_page || 1);
      }
    });
  });

  function buildCustomPodcastTurns(inv) {
    const covStalks = (inv.open_cover || []).map(id => stalkById[id]).filter(Boolean);
    const sA = covStalks[0] || KB.stalks[0] || { title: 'Opening Stalk', start_page: 1, summary: '', formal_core: '' };
    const sM = covStalks[Math.floor(covStalks.length / 2)] || sA;
    const sB = covStalks[covStalks.length - 1] || sA;
    return [
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act I · Visual Hook & Notation', visual_cue: `Page ${sA.start_page}: ${sA.title}`, start_sec: 0, end_sec: 16, cite_page: sA.start_page, text: `Welcome to the 4-Act Deep Dive for "${inv.question}". We are gluing ${covStalks.length} stalks starting from ${sA.title} on page ${sA.start_page}.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act I · Visual Hook & Notation', visual_cue: `Page ${sA.start_page}: Local Olog Schema`, start_sec: 16, end_sec: 32, cite_page: sA.start_page, text: `On page ${sA.start_page}, ${sA.title} establishes our opening schema: ${sA.summary}` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act II · Walking the Diagram', visual_cue: `Page ${sA.start_page}: Formal Categorical Core`, start_sec: 32, end_sec: 50, cite_page: sA.start_page, text: `Let's walk the arrows in ${sA.title}. Every object in the local Olog carries typed aspect morphisms that must commute across overlaps.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act II · Walking the Diagram', visual_cue: `Page ${sM.start_page}: Intermediate Stalk ${sM.title}`, start_sec: 50, end_sec: 68, cite_page: sM.start_page, text: `Bridging through ${sM.title} on page ${sM.start_page}, we see how the restriction arrows preserve the invariant: ${sM.summary}` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act II · Walking the Diagram', visual_cue: `Page ${sB.start_page}: Target Stalk ${sB.title}`, start_sec: 68, end_sec: 86, cite_page: sB.start_page, text: `And reaching ${sB.title} on page ${sB.start_page}, the fiber product glues both neighborhoods into a single coherent section.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act III · Edge Cases & Traps', visual_cue: `Page ${sB.start_page}: Boundary & Degenerate Case`, start_sec: 86, end_sec: 104, cite_page: sB.start_page, text: `What happens if we drop the intermediate bridge stalk? Then the overlap intersection becomes disconnected and H-zero jumps above 1.` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act III · Edge Cases & Traps', visual_cue: `Page ${sA.start_page}: Cohomological Obstruction Check`, start_sec: 104, end_sec: 122, cite_page: sA.start_page, text: `Exactly—our sheaf gluing audit catches that separation instead of hallucinating a false connection across unbridged chapters.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act III · Edge Cases & Traps', visual_cue: `Page ${sB.start_page}: Summary Invariant`, start_sec: 122, end_sec: 140, cite_page: sB.start_page, text: `And inside ${sB.title} on page ${sB.start_page}: ${sB.summary}` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act IV · Decoding the Formula & Lab', visual_cue: `Page ${sA.start_page}: Formula Symbol Decoder`, start_sec: 140, end_sec: 158, cite_page: sA.start_page, text: `In Act IV, use the Symbolic Sandbox in Plate III to inspect each symbol in ${sA.title} and ${sB.title} piece by piece.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act IV · Decoding the Formula & Lab', visual_cue: `Page ${sB.start_page}: Live Gemini 2.5 TTS Synthesis`, start_sec: 158, end_sec: 175, cite_page: sB.start_page, text: `Click Synthesize Live in the Gemini 2.5 Voices drawer above to voice this custom 10-turn investigation live.` }
    ];
  }

  window.__loadPodcastForInvestigation = function(inv) {
    if (!inv) return;
    if (audioEl && !audioEl.paused) {
      audioEl.pause();
    }
    updateButtonsState(false);

    const baseInv = KB.notebook_investigations.find(x => x.id === inv.id) || inv;
    currentTurns = (baseInv.podcast_turns && baseInv.podcast_turns.length)
      ? baseInv.podcast_turns
      : buildCustomPodcastTurns(baseInv);
    const relAudio = baseInv.audio_file || (KB.notebook_investigations[0] && KB.notebook_investigations[0].audio_file) || '';
    const dur = baseInv.audio_duration_sec || 175;

    if (relAudio && audioEl) {
      audioEl.src = (bundleBaseDir ? bundleBaseDir + '/' : '') + relAudio;
      audioEl.playbackRate = speedSteps[speedIdx];
    }
    if (timeLabel) timeLabel.textContent = `0:00 / ${fmtSec(dur)}`;
    if (scrubSlider) scrubSlider.value = 0;

    if (currentTurns.length) {
      syncActiveTurnUi(currentTurns[0], 0);
    }

    if (transcriptDrawer) {
      transcriptDrawer.innerHTML = currentTurns.map((t, idx) => {
        const isKore = t.speaker !== 'Puck';
        const col = isKore ? 'var(--accent-text)' : 'var(--good)';
        return `
          <div class="podcast-turn-row" data-turn-idx="${idx}" style="padding:7px 8px;border-bottom:1px dotted var(--rule);cursor:pointer;transition:background 0.15s"
               onclick="window.__seekPodcastTo(${t.start_sec || 0}, ${t.cite_page || 1})">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:3px;flex-wrap:wrap;gap:4px">
              <span class="mono" style="color:${col};font-weight:600">${isKore ? '🎙️' : '🎧'} Turn ${idx + 1} · ${escapeHtml(t.speaker)} (${escapeHtml(t.role || 'Host')})</span>
              <div style="display:flex;gap:5px;align-items:center">
                ${t.act ? `<span class="mono" style="font-size:0.63rem;padding:1px 5px;background:var(--surface);border-radius:2px;color:var(--ink-2)">${escapeHtml(t.act)}</span>` : ''}
                <span class="cite-pill" onclick="event.stopPropagation();window.__jumpToPage(${t.cite_page || 1}, '')">§ p.${t.cite_page || 1}</span>
                <span class="mono" style="color:var(--ink-3);font-size:0.68rem">${fmtSec(t.start_sec || 0)}</span>
              </div>
            </div>
            ${t.visual_cue ? `<div class="mono" style="font-size:0.67rem;color:var(--ax-technology);margin-bottom:2px">👁️ ${escapeHtml(t.visual_cue)}</div>` : ''}
            <div style="color:var(--ink-2);line-height:1.42">${escapeHtml(t.text)}</div>
          </div>
        `;
      }).join('');
    }
  };

  function togglePodcastPlayback() {
    if (!audioEl || !audioEl.src) {
      window.__loadPodcastForInvestigation(state.currentInvestigation || firstInv);
    }
    if (!audioEl) return;
    if (!audioEl.paused) {
      audioEl.pause();
      updateButtonsState(false);
    } else {
      audioEl.play().then(() => updateButtonsState(true)).catch(err => {
        console.warn('Audio playback error:', err);
      });
    }
  }

  if (playPauseBtn) playPauseBtn.addEventListener('click', togglePodcastPlayback);
  if (marginaliaPlayBtn) marginaliaPlayBtn.addEventListener('click', () => {
    document.getElementById('podcastStudioCard').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    togglePodcastPlayback();
  });

  if (audioEl) {
    audioEl.addEventListener('timeupdate', () => {
      const cur = audioEl.currentTime || 0;
      const tot = audioEl.duration || (state.currentInvestigation && state.currentInvestigation.audio_duration_sec) || 175;
      if (timeLabel) timeLabel.textContent = `${fmtSec(cur)} / ${fmtSec(tot)}`;
      if (scrubSlider && tot > 0) scrubSlider.value = ((cur / tot) * 100).toFixed(1);

      for (let i = 0; i < currentTurns.length; i++) {
        const t = currentTurns[i];
        if (cur >= (t.start_sec || 0) && cur <= (t.end_sec || 9999)) {
          syncActiveTurnUi(t, i);
          break;
        }
      }
    });
    audioEl.addEventListener('ended', () => updateButtonsState(false));
    audioEl.addEventListener('pause', () => updateButtonsState(false));
    audioEl.addEventListener('play', () => updateButtonsState(true));
  }

  if (scrubSlider && audioEl) {
    scrubSlider.addEventListener('input', () => {
      const tot = audioEl.duration || (state.currentInvestigation && state.currentInvestigation.audio_duration_sec) || 175;
      audioEl.currentTime = (Number(scrubSlider.value) / 100) * tot;
    });
  }

  if (speedBtn && audioEl) {
    speedBtn.addEventListener('click', () => {
      speedIdx = (speedIdx + 1) % speedSteps.length;
      const sp = speedSteps[speedIdx];
      audioEl.playbackRate = sp;
      speedBtn.textContent = `${sp}×`;
    });
  }

  if (transcriptBtn && transcriptDrawer) {
    transcriptBtn.addEventListener('click', () => {
      const open = transcriptDrawer.style.display !== 'none';
      transcriptDrawer.style.display = open ? 'none' : 'block';
      transcriptBtn.textContent = open ? '10-Turn Script ▾' : '10-Turn Script ▴';
    });
  }

  if (geminiConfigBtn && geminiConfigDrawer) {
    geminiConfigBtn.addEventListener('click', () => {
      const open = geminiConfigDrawer.style.display !== 'none';
      geminiConfigDrawer.style.display = open ? 'none' : 'block';
    });
  }

  function pcm16Base64ToWavUrl(b64Data, sampleRate = 24000) {
    const raw = atob(b64Data);
    const numBytes = raw.length;
    const buffer = new ArrayBuffer(44 + numBytes);
    const view = new DataView(buffer);
    const writeStr = (off, s) => { for (let i = 0; i < s.length; i++) view.setUint8(off + i, s.charCodeAt(i)); };
    writeStr(0, 'RIFF');
    view.setUint32(4, 36 + numBytes, true);
    writeStr(8, 'WAVE');
    writeStr(12, 'fmt ');
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, 1, true);
    view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * 2, true);
    view.setUint16(32, 2, true);
    view.setUint16(34, 16, true);
    writeStr(36, 'data');
    view.setUint32(40, numBytes, true);
    const bytes = new Uint8Array(buffer, 44);
    for (let i = 0; i < numBytes; i++) bytes[i] = raw.charCodeAt(i);
    return URL.createObjectURL(new Blob([buffer], { type: 'audio/wav' }));
  }

  if (runLiveGeminiBtn) {
    runLiveGeminiBtn.addEventListener('click', async () => {
      const key = (geminiKeyInput && geminiKeyInput.value || '').trim();
      if (!key) {
        if (geminiStatusMsg) geminiStatusMsg.textContent = '⚠ Please paste a GEMINI_API_KEY to call gemini-2.5-flash-preview-tts live.';
        return;
      }
      try { localStorage.setItem('CETI_GEMINI_API_KEY', key); } catch (e) {}
      const [vA, vB] = ((geminiVoiceSelect && geminiVoiceSelect.value) || 'Kore,Puck').split(',');
      const turnsToSpeak = currentTurns.length ? currentTurns : [
        { speaker: 'Kore', text: 'Welcome to the Deep Dive into ' + (state.currentInvestigation ? state.currentInvestigation.question : 'our active sheaf section') },
        { speaker: 'Puck', text: 'Let us inspect how the local Olog definitions commute across the overlap.' }
      ];
      const scriptText = 'Perform this natural two-host NotebookLM Deep Dive conversation:\n\n' +
        turnsToSpeak.map(t => `${t.speaker === 'Puck' ? vB : vA}: ${t.text}`).join('\n\n');

      if (geminiStatusMsg) geminiStatusMsg.textContent = `⏳ Calling gemini-2.5-flash-preview-tts with multiSpeakerVoiceConfig (${vA} & ${vB})…`;
      runLiveGeminiBtn.disabled = true;
      try {
        const resp = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent?key=${encodeURIComponent(key)}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: scriptText }] }],
            generationConfig: {
              responseModalities: ['AUDIO'],
              speechConfig: {
                multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                    { speaker: vA, voiceConfig: { prebuiltVoiceConfig: { voiceName: vA } } },
                    { speaker: vB, voiceConfig: { prebuiltVoiceConfig: { voiceName: vB } } }
                  ]
                }
              }
            }
          })
        });
        const data = await resp.json();
        if (!resp.ok) throw new Error((data.error && data.error.message) || `HTTP ${resp.status}`);
        const b64 = data.candidates[0].content.parts[0].inlineData.data;
        const wavUrl = pcm16Base64ToWavUrl(b64, 24000);
        audioEl.src = wavUrl;
        if (podcastEngineBadge) podcastEngineBadge.textContent = `◆ Live Gemini 2.5 TTS (${vA} & ${vB})`;
        if (geminiStatusMsg) geminiStatusMsg.textContent = `✓ Synthesized live via Gemini 2.5 Multi-Speaker TTS (${vA} & ${vB})! Playing now…`;
        audioEl.play().then(() => updateButtonsState(true)).catch(() => {});
      } catch (err) {
        if (geminiStatusMsg) geminiStatusMsg.textContent = `⊘ Gemini TTS error: ${err.message}. Playing pre-rendered neural MP3.`;
      } finally {
        runLiveGeminiBtn.disabled = false;
      }
    });
  }

  window.__jumpToPage = function(pageNum, term) {
    drawer.classList.add('open');
    renderPageReader(pageNum, term || '');
  };

  window.__addStalkToStudio = function(stalkId) {
    state.openCover.add(stalkId);
    state.focusedStalkId = stalkId;
    updateCoverAndOlog();
    document.getElementById('plate-2').scrollIntoView({ behavior: 'smooth' });
  };

  // Initialize Studio
  renderInvestigationPills();
  displayInvestigation(firstInv);
  updateCoverAndOlog();
  renderPageReader(state.currentPage, state.highlightTerm);
})();
</script>
</body>
</html>
"""


def adapt_html_template_for_corpus(raw_template: str, kb_obj: dict) -> str:
    """Dynamically adapt static Spivak/609/877/30/52 strings in HTML_TEMPLATE to match any target corpus KB."""
    book = kb_obj.get("book", {})
    total_pages = int(book.get("total_pages", len(kb_obj.get("pages", [])) or 1))
    if total_pages == 609 and "Spivak" in book.get("author", "Spivak"):
        return raw_template

    import re
    book_title = book.get("title", "Indexed Monograph")
    book_author = book.get("author", "Corpus Author")
    author_last = book_author.split()[-1] if book_author.split() else book_author
    book_year = book.get("year", 2026)
    n_stalks = len(kb_obj.get("stalks", []))
    n_morphs = len(kb_obj.get("restriction_morphisms", []))
    n_items = len(kb_obj.get("formal_items", []))
    chapters = kb_obj.get("chapters", [])
    n_ch = len(chapters)
    stalks = kb_obj.get("stalks", [])
    default_stalk = stalks[min(2, len(stalks) - 1)] if stalks else {"start_page": 1}
    default_page = min(total_pages, int(default_stalk.get("start_page", 1)))

    t = raw_template
    # 1. Replace chapterFilterSelect static options with target corpus chapters
    if chapters:
        opts = [f'                <option value="all">All {n_ch} Chapters</option>']
        ch_dist_lines = []
        for ch in chapters:
            cnum = ch["chapter"]
            ctitle = ch["title"].split(":", 1)[-1].strip().replace("&", "&amp;")
            short_ctitle = ctitle.split("&amp;")[0].strip().rstrip(",")
            opts.append(f'                <option value="{cnum}">Ch {cnum} · {ctitle}</option>')
            ch_stalk_cnt = sum(1 for s in stalks if s.get("chapter") == cnum)
            ch_pp = max(1, ch.get("end_page", 1) - ch.get("start_page", 1) + 1)
            ch_dist_lines.append(f"        • Ch {cnum} ({short_ctitle}): {ch_stalk_cnt} stalks · {ch_pp} pp.")
        ch_select_block = '<select id="chapterFilterSelect" class="query-input" style="padding:4px 8px;font-size:0.76rem">\n' + "\n".join(opts) + "\n              </select>"
        t = re.sub(
            r'<select id="chapterFilterSelect"[^>]*>.*?</select>',
            ch_select_block,
            t,
            flags=re.DOTALL
        )
        old_dist_block = (
            "        • Ch 1 (Agreement): 1 stalk · 15 pp.<br>\n"
            "        • Ch 2 (Sets/Ologs): 9 stalks · 82 pp.<br>\n"
            "        • Ch 3 (Posets/Graphs): 5 stalks · 138 pp.<br>\n"
            "        • Ch 4 (Categories/Functors): 7 stalks · 108 pp.<br>\n"
            "        • Ch 5 (Monads/Operads): 3 stalks · 76 pp.<br>\n"
            "        • Ch 6 (Universal/Limits): 2 stalks · 48 pp.<br>\n"
            "        • Ch 7 (Adjunctions/Sheaves): 3 stalks · 115 pp."
        )
        t = t.replace(old_dist_block, "<br>\n".join(ch_dist_lines))
        t = t.replace("Measured Distribution Across 7 Chapters", f"Measured Distribution Across {n_ch} Chapters ({total_pages} pp.)")

    # 2. Clamp any out-of-bounds page numbers in __jumpToPage(N, ...) and p.N labels
    def clamp_jump(m):
        p = int(m.group(1))
        rest = m.group(2)
        p_clamped = min(total_pages, max(1, (p * total_pages) // 609)) if p > total_pages else p
        return f"window.__jumpToPage({p_clamped},{rest})"

    t = re.sub(r"window\.__jumpToPage\((\d+),([^)]+)\)", clamp_jump, t)

    def clamp_sec_pill(m):
        p = int(m.group(1))
        p_clamped = min(total_pages, max(1, (p * total_pages) // 609)) if p > total_pages else p
        return f"§ p.{p_clamped}"

    t = re.sub(r"§ p\.(\d+)", clamp_sec_pill, t)

    # 3. Replace reader default page 520 and max 609
    t = t.replace('max="609" value="520"', f'max="{total_pages}" value="{default_page}"')
    t = t.replace("#page=520", f"#page={default_page}")
    t = t.replace("📖 Page Reader (p.520)", f"📖 Page Reader (p.{default_page})")
    t = t.replace("/ 609</span>", f"/ {total_pages}</span>")

    # 4. Replace corpus title, author, and counts
    n_simpl = len(kb_obj.get("two_simplices", []))
    replacements = [
        ("The Sheaf of Ologged Concepts · Category Theory for the Sciences (Field Manual &amp; Notebook Studio)", f"{book_title} · Sheaf Field Manual &amp; Notebook Studio"),
        ("CETI · SHEAF FIELD MANUAL · SPIVAK (609 PP.)", f"CETI · SHEAF FIELD MANUAL · {book_title.upper()[:42]} ({total_pages} PP.)"),
        ("David I. Spivak’s <em>Category Theory for the Sciences</em>", f"<em>{book_title}</em> ({book_author})"),
        ("David I. Spivak · MIT Press (609 pp.)", f"{book_author} ({total_pages} pp.)"),
        ("BUILT FROM SPIVAK’S <em>CATEGORY THEORY FOR THE SCIENCES</em> (609 PP.)", f"BUILT FROM <em>{book_title.upper()}</em> ({total_pages} PP.)"),
        ("THE MEASURED CORPUS OF SPIVAK’S 609 PAGES", f"THE MEASURED CORPUS OF ALL {total_pages} MONOGRAPH PAGES"),
        ("SPIVAK §7.2.2.2, P.520", f"THM 2.5 · P.{default_page}"),
        ("Verbatim 609-Page Book Reader · Spivak (2014)", f"Verbatim {total_pages}-Page Book Reader · {book_author} ({book_year})"),
        ("Open 609-Page Verbatim Book Reader", f"Open {total_pages}-Page Verbatim Book Reader"),
        ("609-Page Verbatim Reader", f"{total_pages}-Page Verbatim Reader"),
        ("SLIDE-OVER 609-PAGE VERBATIM PDF READER", f"SLIDE-OVER {total_pages}-PAGE VERBATIM READER"),
        ("DEFERRED 609-PAGE BUNDLE", f"DEFERRED {total_pages}-PAGE BUNDLE"),
        ("deferred 609-page + 877-declaration bundle", f"deferred {total_pages}-page + {n_items}-declaration bundle"),
        ("Loading 609-page bundle", f"Loading {total_pages}-page bundle"),
        ("Search all 609 verbatim PDF pages", f"Search all {total_pages} verbatim PDF pages"),
        ("No matches in 609 pages", f"No matches in {total_pages} pages"),
        ("Across 609 Pages", f"Across {total_pages} Pages"),
        ("all 609 pages of Spivak’s book", f"all {total_pages} pages of the monograph"),
        ("all <strong>609 pages</strong> and <strong>877 formal declarations</strong>", f"all <strong>{total_pages} pages</strong> and <strong>{n_items} formal declarations</strong>"),
        ("While all 609 pages and 877 numbered declarations", f"While all {total_pages} pages and {n_items} formal declarations"),
        ("609 pages, 96 sections, and 877 formal numbered declarations", f"{total_pages} pages, {n_stalks} sections, and {n_items} formal declarations"),
        ("1, \\dots, 609", f"1, \\dots, {total_pages}"),
        ("1, \\\\dots, 609", f"1, \\\\dots, {total_pages}"),
        ("609 pp · 877 declarations", f"{total_pages} pp · {n_items} declarations"),
        ("⚖ 609 pp", f"⚖ {total_pages} pp"),
        ("of 609 ·", f"of {total_pages} ·"),
        ("Math.min(609,", f"Math.min({total_pages},"),
        ("from 877 total in Spivak", f"from {n_items} total in the monograph"),
        ("877 numbered formal declarations", f"{n_items} formal declarations"),
        ("877 Formal Definitions / Theorems / Ologs", f"{n_items} Formal Definitions / Theorems / Declarations"),
        ("877 Formal Declarations", f"{n_items} Formal Declarations"),
        ("Search 877 Definitions", f"Search {n_items} Definitions"),
        ("All Kinds (877)", f"All Kinds ({n_items})"),
        ("877 DECLARATIONS", f"{n_items} DECLARATIONS"),
        ("30 Stalks, 877 Items &amp; 3D Poset", f"{n_stalks} Stalks, {n_items} Items &amp; 3D Poset"),
        ("THE 30 CONCEPT STALKS, 877 FORMAL ITEMS & 3D POSET ATLAS", f"THE {n_stalks} CONCEPT STALKS, {n_items} FORMAL ITEMS & 3D POSET ATLAS"),
        ("30 CONCEPT STALKS, 877 DECLARATIONS", f"{n_stalks} CONCEPT STALKS, {n_items} DECLARATIONS"),
        ("30 Stalks · 877 Items", f"{n_stalks} Stalks · {n_items} Items"),
        ("30 Stalks · 52 Morphisms · 8 2-Simplices", f"{n_stalks} Stalks · {n_morphs} Morphisms · {n_simpl} 2-Simplices"),
        ("30 Stalks · 52 Morphisms", f"{n_stalks} Stalks · {n_morphs} Morphisms"),
        ("ALL 30 STALKS · 52 RESTRICTIONS", f"ALL {n_stalks} STALKS · {n_morphs} RESTRICTIONS"),
        ("IV · 30 Stalks &amp; Atlas", f"IV · {n_stalks} Stalks &amp; Atlas"),
        ("Full X (30)", f"Full X ({n_stalks})"),
        ("Filter 30 concept stalks", f"Filter {n_stalks} concept stalks"),
        ("30 Concept Stalks", f"{n_stalks} Concept Stalks"),
        ("30 core conceptual domains", f"{n_stalks} core conceptual domains"),
        ("◆ 30 stalks", f"◆ {n_stalks} stalks"),
        ("all 30 stalks", f"all {n_stalks} stalks"),
        ("52 Restriction Arrows", f"{n_morphs} Restriction Arrows"),
        ("52 restriction morphisms", f"{n_morphs} restriction morphisms"),
        ("52 typed restriction morphisms", f"{n_morphs} typed restriction morphisms"),
        ("◆ 52 arrows", f"◆ {n_morphs} arrows"),
        ("◆ 8 simplices", f"◆ {n_simpl} simplices"),
        ("8 higher-order commutative 2-simplices", f"{n_simpl} higher-order commutative 2-simplices"),
        ("Chapters 1–7", f"Chapters 1–{n_ch}"),
        ("Category Theory Illustrated · Through Symbols", f"{book_title} · Through Symbols"),
        ("Category Theory Illustrated: Through Symbols", f"{book_title}: Through Symbols"),
        ("CATEGORY THEORY ILLUSTRATED · UNDERSTANDING THROUGH SYMBOLS", f"{book_title.upper()} · UNDERSTANDING THROUGH SYMBOLS"),
        ("CATEGORY THEORY ILLUSTRATED THROUGH SYMBOLS", f"{book_title.upper()} THROUGH SYMBOLS"),
        ("Spivak Grounding", "Monograph Grounding (36 pp.)"),
        ("Spivak Text", "Monograph Text"),
        ("Spivak’s text", "this monograph"),
        ("Spivak’s", f"{author_last}’s"),
    ]
    for old_s, new_s in replacements:
        t = t.replace(old_s, new_s)
    return t


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Compile a validated sheaf_kb.json into a Field-Manual & Notebook Studio HTML volume")
    parser.add_argument("--kb", type=Path, default=None, help="Path to sheaf_kb.json")
    parser.add_argument("--out", type=Path, default=None, help="Output HTML file path")
    parser.add_argument("--bundle", type=Path, default=None, help="Output deferred sheaf_pages_bundle.js path")
    args = parser.parse_args()

    kb_path = args.kb if args.kb else KB_PATH
    bundle_path = args.bundle if args.bundle else (kb_path.parent / "sheaf_pages_bundle.js")
    kb_obj = json.loads(kb_path.read_text(encoding="utf-8"))

    # 1. Write deferred full-page & formal-declarations bundle (`sheaf_pages_bundle.js`)
    bundle_obj = {
        "pages": kb_obj["pages"],
        "formal_items": kb_obj["formal_items"],
        "full_stalk_items": {s["id"]: s.get("formal_items", []) for s in kb_obj["stalks"]}
    }
    bundle_json_str = json.dumps(bundle_obj, ensure_ascii=False, separators=(",", ":"))
    bundle_js = (
        "window.SHEAF_PAGES_BUNDLE=" + bundle_json_str + ";"
        "window.__SHEAF_PAGES__=window.SHEAF_PAGES_BUNDLE.pages;"
        "window.__SHEAF_BUNDLE_LOADED__=true;"
        "window.__onSheafBundleLoaded&&window.__onSheafBundleLoaded(window.SHEAF_PAGES_BUNDLE);\n"
    )
    bundle_path.parent.mkdir(parents=True, exist_ok=True)
    bundle_path.write_text(bundle_js, encoding="utf-8")

    # 2. Build lightweight core JSON with 3D poset coordinates & slimmed seed pages (<220 KB total HTML)
    seed_page_nums = {s["start_page"] for s in kb_obj["stalks"]} | {1, 11, 47, 74, 83, 148, 203, 260, 319, 520}
    slim_stalks = []
    total_stalks = len(kb_obj["stalks"])
    for idx, s in enumerate(kb_obj["stalks"]):
        sc = dict(s)
        sc.pop("all_item_ids", None)
        sc.pop("tfidf_signature", None)
        sc.pop("key_items", None)
        sc["formal_items"] = []
        if len(str(sc.get("verbatim_excerpt", ""))) > 260:
            sc["verbatim_excerpt"] = str(sc["verbatim_excerpt"])[:260] + "…"
        ang = (2.0 * math.pi * idx) / max(1, total_stalks) * 2.2
        radius = 110.0 + (idx % 3) * 28.0
        y_pos = (s.get("chapter", 1) - 4.0) * 36.0
        sc["pos3d"] = [round(radius * math.cos(ang), 1), round(y_pos, 1), round(radius * math.sin(ang), 1)]
        slim_stalks.append(sc)

    slim_morphs = []
    for m in kb_obj["restriction_morphisms"]:
        mc = dict(m)
        mc.pop("metrics", None)
        slim_morphs.append(mc)

    slim_seed_pages = []
    for p in kb_obj["pages"]:
        if p["p"] in seed_page_nums and len(slim_seed_pages) < 8:
            pc = dict(p)
            if len(str(pc.get("txt", ""))) > 500:
                pc["txt"] = str(pc["txt"])[:500] + "\n… [Full verbatim page hydrated via sheaf_pages_bundle.js]"
            slim_seed_pages.append(pc)

    core_obj = {
        "book": kb_obj["book"],
        "chapters": kb_obj["chapters"],
        "stalks": slim_stalks,
        "restriction_morphisms": slim_morphs,
        "two_simplices": kb_obj["two_simplices"],
        "cohomology_obstructions": kb_obj.get("cohomology_obstructions", []),
        "notebook_investigations": kb_obj["notebook_investigations"],
        "seed_pages": slim_seed_pages
    }
    core_json = json.dumps(core_obj, ensure_ascii=False, separators=(",", ":")).replace("</script>", "<\\/script>")

    if args.out:
        out_path = args.out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            rel_bundle = bundle_path.resolve().relative_to(out_path.resolve().parent)
        except Exception:
            rel_bundle = Path("data/sheaf_pages_bundle.js")
        pdf_name = kb_obj.get("book", {}).get("source_pdf", kb_obj.get("book", {}).get("pdf_url", "document.pdf"))
        adapted_template = adapt_html_template_for_corpus(HTML_TEMPLATE, kb_obj)
        html_custom = (
            adapted_template
            .replace("__SHEAF_CORE_JSON__", core_json)
            .replace("__BUNDLE_REL_PATH__", str(rel_bundle))
            .replace("__PDF_REL_PATH__", str(pdf_name))
        )
        out_path.write_text(html_custom, encoding="utf-8")
        print(f"Field-Manual Studio HTML compiled: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")
        print(f"Deferred Page Bundle:              {bundle_path} ({bundle_path.stat().st_size / 1e6:.2f} MB)")
        return

    html_main = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "cattheory-sheaf-kb/data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "cattheory-sheaf-kb/cattheory.pdf")
    )
    html_local = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "cattheory.pdf")
    )
    html_artifact = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "/Users/cairo/Documents/CETI/ACCENTURE/content-factory v2/cattheory-sheaf-kb/data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "/Users/cairo/Documents/CETI/ACCENTURE/content-factory v2/cattheory-sheaf-kb/cattheory.pdf")
    )

    OUT_MAIN.write_text(html_main, encoding="utf-8")
    OUT_LOCAL.write_text(html_local, encoding="utf-8")
    if OUT_ARTIFACT.parent.exists():
        OUT_ARTIFACT.write_text(html_artifact, encoding="utf-8")

    print(f"Field-Manual Studio HTML compiled: {OUT_MAIN.stat().st_size / 1024:.1f} KB")
    print(f"Deferred 609-Page Bundle:          {bundle_path.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()

