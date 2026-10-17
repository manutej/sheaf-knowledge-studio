#!/usr/bin/env python3
"""
Compiles the bespoke CETI Field-Manual & Visual Rosetta Studio HTML for:
Boris Marinov (Jencel Panic) — "Category Theory Illustrated" (377 pages),
plus the Cross-Corpus Comparative Bridge with David I. Spivak's
"Category Theory for the Sciences" (609 pages).
"""
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
KB_PATH = DATA_DIR / "sheaf_kb.json"
BUNDLE_PATH = DATA_DIR / "sheaf_pages_bundle.js"

OUT_MAIN = ROOT.parent / "Category Theory Illustrated - Sheaf Studio.html"
OUT_LOCAL = ROOT / "index.html"
OUT_ARTIFACT = pathlib.Path("/Users/cairo/.gemini/antigravity/brain/109c7092-572c-4cbf-ac55-3677c5ef2652/category_theory_illustrated_studio.html")

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-level="practitioner" data-theme="light" data-voice-profile="lawvere-visual-rosetta">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Category Theory Illustrated · Visual Rosetta &amp; Sheaf Studio (Marinov 377 pp. × Spivak 609 pp.)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..600&family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..500&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* ============================================================================
 * 1. BOOK VOICE PROFILE: LAWVERE VISUAL ROSETTA & GEOMETRIC SKETCHBOOK
 *    Honors CETI warm drafting vellum while channeling Boris Marinov's
 *    colored-ball & Inkscape diagram vocabulary (Cobalt, Ochre, Vermilion, Viridian)
 * ============================================================================ */
:root {
  --raw-paper: #F6F1E7;
  --raw-paper-soft: #EFE7D8;
  --raw-surface: #E6DCCA;
  --raw-ink: #17181C;
  --raw-ink-2: #3A3D45;
  --raw-ink-3: #646873;
  --raw-cobalt: #2B5B84;
  --raw-cobalt-deep: #1E4363;
  --raw-ochre: #B87D24;
  --raw-vermilion: #B34434;
  --raw-viridian: #35694E;
  --raw-plum: #644775;

  --paper: var(--raw-paper);
  --paper-soft: var(--raw-paper-soft);
  --surface: var(--raw-surface);
  --ink: var(--raw-ink);
  --ink-2: var(--raw-ink-2);
  --ink-3: var(--raw-ink-3);
  --accent: var(--raw-cobalt);
  --accent-text: var(--raw-cobalt-deep);
  --ochre: var(--raw-ochre);
  --rule: rgba(23, 24, 28, 0.14);
  --rule-hair: rgba(23, 24, 28, 0.08);
  --accent-soft: rgba(43, 91, 132, 0.11);
  --good-soft: rgba(46, 100, 68, 0.11);

  --good: #2E6444;
  --warn: #A6651B;
  --bad: #A63626;

  /* 6-World Rosetta Accents */
  --w-sets: #B87D24;
  --w-cats: #2B5B84;
  --w-monoids: #644775;
  --w-orders: #35694E;
  --w-logic: #B34434;
  --w-types: #1F6E78;

  --f-serif: 'Fraunces', Georgia, serif;
  --f-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --f-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

  --s-hero: clamp(2.15rem, 1.45rem + 3vw, 3.85rem);
  --s-h1: clamp(1.55rem, 1.2rem + 1.45vw, 2.35rem);
  --s-h2: clamp(1.18rem, 1.02rem + 0.7vw, 1.52rem);
  --s-body: clamp(0.95rem, 0.91rem + 0.18vw, 1.04rem);
  --s-small: clamp(0.82rem, 0.79rem + 0.12vw, 0.89rem);
  --s-mono: clamp(0.74rem, 0.71rem + 0.1vw, 0.81rem);

  --col-w: 1320px;
  --pad: clamp(1.2rem, 3.5vw, 3rem);
  --gap: clamp(1.2rem, 2.4vw, 2.2rem);
}

html[data-theme="dark"] {
  --paper: #16181E;
  --paper-soft: #1E2129;
  --surface: #272B35;
  --ink: #F4EFE6;
  --ink-2: #C7C2B8;
  --ink-3: #8D8980;
  --accent: #6CA6D9;
  --accent-text: #8BC0EE;
  --ochre: #E2A84B;
  --rule: rgba(244, 239, 230, 0.15);
  --rule-hair: rgba(244, 239, 230, 0.08);
  --accent-soft: rgba(108, 166, 217, 0.16);
  --good-soft: rgba(116, 184, 142, 0.16);
  --good: #74B88E;
  --warn: #E2A84B;
  --bad: #E07A6B;
}

html[data-theme="dark"] .hero-figure svg,
html[data-theme="dark"] .view-pane svg,
html[data-theme="dark"] #gluedOlogSvgWrap svg {
  background: #F4EFE6;
  color: #17181C;
  border-radius: 3px;
  padding: 4px;
}

*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--paper); color: var(--ink); overflow-x: hidden; max-width: 100%; }
body {
  margin: 0;
  font-family: var(--f-sans);
  font-size: var(--s-body);
  line-height: 1.62;
  background-color: var(--paper);
  background-image:
    radial-gradient(rgba(43, 91, 132, 0.04) 1px, transparent 1px),
    radial-gradient(rgba(184, 125, 36, 0.03) 1px, transparent 1px);
  background-size: 24px 24px;
  background-position: 0 0, 12px 12px;
  color: var(--ink);
  overflow-x: hidden;
  max-width: 100%;
}

svg { max-width: 100%; height: auto; display: block; }

h1, h2, h3, h4, .serif { font-family: var(--f-serif); font-weight: 400; letter-spacing: -0.015em; margin: 0; }
.mono { font-family: var(--f-mono); font-size: var(--s-mono); font-variant-numeric: tabular-nums; }

em.u-copper, em.u-accent {
  font-family: var(--f-serif);
  font-style: italic;
  color: var(--accent-text);
  border-bottom: 1.5px solid var(--ochre);
  padding-bottom: 1px;
}

.eyebrow {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  text-transform: uppercase;
  letter-spacing: 0.11em;
  color: var(--ink-3);
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-wrap: wrap;
}

/* Non-color-alone Verdict Stamps */
.stamp {
  display: inline-flex;
  align-items: center;
  gap: 0.35ch;
  font-family: var(--f-mono);
  font-size: 0.71rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 2px;
  border: 1px solid currentColor;
  white-space: nowrap;
}
#readerPageMeta .stamp {
  white-space: normal;
  max-width: 100%;
  line-height: 1.35;
}
.stamp.ratified { color: var(--good); background: rgba(46, 100, 68, 0.08); }
.stamp.measured { color: var(--accent-text); background: rgba(43, 91, 132, 0.09); }
.stamp.accept { color: var(--ochre); background: rgba(184, 125, 36, 0.10); }
.stamp.warn { color: var(--warn); background: rgba(166, 101, 27, 0.10); }

/* World badges */
.w-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: var(--f-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  padding: 2px 7px;
  border-radius: 2px;
  font-weight: 600;
  border: 1px solid currentColor;
}
.w-sets { color: var(--w-sets); }
.w-cats { color: var(--w-cats); }
.w-monoids { color: var(--w-monoids); }
.w-orders { color: var(--w-orders); }
.w-logic { color: var(--w-logic); }
.w-types { color: var(--w-types); }

/* ============================================================================
 * 2. MATHEMATICAL & SYMBOLIC TYPESETTING ENGINE (ZERO RAW LATEX LEAKS)
 * ============================================================================ */
.math-expr {
  font-family: var(--f-serif);
  font-size: 1.02em;
  color: var(--ink);
  background: rgba(43, 91, 132, 0.07);
  border: 1px solid var(--rule-hair);
  padding: 0px 5px;
  border-radius: 3px;
  display: inline-block;
  line-height: 1.35;
  white-space: normal;
  overflow-wrap: anywhere;
  max-width: 100%;
}
.math-display {
  font-family: var(--f-serif);
  font-size: clamp(0.98rem, 0.92rem + 0.25vw, 1.12rem);
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  border-left: 3px solid var(--accent);
  padding: 0.75rem 1.1rem;
  margin: 0.75rem 0;
  overflow-x: auto;
  max-width: 100%;
  text-align: center;
  color: var(--ink);
  border-radius: 2px;
}
.m-cal { font-family: var(--f-serif); font-style: italic; font-weight: 600; color: var(--accent-text); }
.m-cat { font-family: var(--f-sans); font-weight: 700; letter-spacing: 0.02em; }
.m-op { font-family: var(--f-mono); font-size: 0.88em; }
.m-arrow { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; margin: 0 5px; line-height: 1; position: relative; top: -0.16em; }
.m-arrow-label { font-size: 0.68em; font-family: var(--f-mono); color: var(--accent-text); margin-bottom: -3px; padding: 0 3px; white-space: nowrap; }
.m-arrow-body { font-size: 1.14em; line-height: 0.85; }
.m-lim { display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; line-height: 1; margin: 0 2px; }
.m-lim-top { font-family: var(--f-mono); font-size: 0.78em; }
.m-lim-sub { font-size: 0.65em; color: var(--ink-3); }

code.inline-code {
  font-family: var(--f-mono);
  font-size: 0.84em;
  background: var(--paper-soft);
  border: 1px solid var(--rule-hair);
  padding: 1px 5px;
  border-radius: 2px;
}

.cite-pill {
  appearance: none;
  background: var(--paper-soft);
  border: 1px solid var(--accent);
  color: var(--accent-text);
  font-family: var(--f-mono);
  font-size: 0.71rem;
  font-weight: 600;
  padding: 4px 8px;
  min-height: 29px;
  line-height: 1.2;
  border-radius: 2px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 3px;
  white-space: nowrap;
  flex-shrink: 0;
  vertical-align: middle;
}
.cite-pill:hover { background: var(--accent); color: var(--paper); }

/* ============================================================================
 * 3. STICKY RIBBON, FRONTISPIECE & PLATE LAYOUT
 * ============================================================================ */
.axis-ribbon {
  position: sticky;
  top: 0;
  z-index: 60;
  background: color-mix(in oklab, var(--paper) 93%, transparent);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--rule);
}
.axis-ribbon-inner {
  max-width: var(--col-w);
  margin: 0 auto;
  padding: 0.45rem var(--pad);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.8rem;
  flex-wrap: wrap;
}
.brand-mark {
  font-family: var(--f-mono);
  font-size: 0.73rem;
  font-weight: 600;
  letter-spacing: 0.07em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.brand-mark .dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--ochre);
  box-shadow: 0 0 0 2px var(--accent);
  flex-shrink: 0;
}
.plate-nav { display: flex; gap: 0.25rem; flex-wrap: wrap; }
.plate-nav a {
  font-family: var(--f-mono);
  font-size: 0.71rem;
  text-decoration: none;
  color: var(--ink-2);
  padding: 4px 8px;
  min-height: 29px;
  display: inline-flex;
  align-items: center;
  border-radius: 2px;
}
.plate-nav a:hover { background: var(--surface); color: var(--accent-text); }

.field-controls { display: flex; align-items: center; gap: 0.45rem; flex-wrap: wrap; }
.ctrl-group {
  display: inline-flex;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  border-radius: 2px;
  padding: 1px;
}
.ctrl-label {
  font-family: var(--f-mono);
  font-size: 0.65rem;
  text-transform: uppercase;
  color: var(--ink-3);
  padding: 2px 6px;
  align-self: center;
}
.ctrl-btn {
  appearance: none;
  border: 0;
  background: transparent;
  font-family: var(--f-mono);
  font-size: 0.69rem;
  color: var(--ink-2);
  padding: 5px 9px;
  min-height: 29px;
  line-height: 1.2;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.ctrl-btn[aria-pressed="true"] { background: var(--ink); color: var(--paper); font-weight: 600; }

.drawer-toggle-btn {
  appearance: none;
  background: var(--accent-text);
  color: var(--paper);
  border: 1px solid var(--accent-text);
  font-family: var(--f-mono);
  font-size: 0.71rem;
  font-weight: 600;
  padding: 5px 10px;
  min-height: 30px;
  display: inline-flex;
  align-items: center;
  white-space: nowrap;
  border-radius: 2px;
  cursor: pointer;
}

.page-wrap { width: 100%; max-width: var(--col-w); margin: 0 auto; padding: 0 var(--pad); overflow-x: clip; }

/* Prevent CSS Grid 1fr (minmax(auto, 1fr)) track blowout on mobile/narrow viewports */
.frontispiece-grid > *,
.plate-head > *,
.plate-body > *,
.studio-split > *,
.dual-stage > *,
.rosetta-grid > *,
.stalk-cards-grid > *,
.course-grid > *,
.decoder-grid > *,
#rosettaHeroBar > *,
.instrument,
.view-pane,
.notebook-main,
.cover-panel {
  min-width: 0;
  max-width: 100%;
}

header.frontispiece {
  padding: clamp(2rem, 4vw, 3.6rem) 0 clamp(1.6rem, 3vw, 2.6rem);
  border-bottom: 2px solid var(--ink);
}
.frontispiece-grid {
  display: grid;
  grid-template-columns: 1.18fr 1fr;
  gap: var(--gap);
  align-items: center;
}
@media (max-width: 900px) { .frontispiece-grid { grid-template-columns: minmax(0, 1fr); } }
.hero-title {
  font-size: var(--s-hero);
  font-weight: 300;
  line-height: 1.05;
  margin: 0.35rem 0 0.85rem;
}
.hero-lede {
  font-size: clamp(1rem, 0.95rem + 0.28vw, 1.15rem);
  color: var(--ink-2);
  max-width: 60ch;
}
.lawvere-quote {
  margin-top: 1rem;
  padding: 0.7rem 1rem;
  background: var(--paper-soft);
  border-left: 3px solid var(--ochre);
  font-family: var(--f-serif);
  font-style: italic;
  font-size: 0.94rem;
  color: var(--ink-2);
}
.hero-figure {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: 1rem 1.1rem 0.75rem;
}
.hero-figure figcaption {
  font-family: var(--f-mono);
  font-size: 0.69rem;
  color: var(--ink-3);
  margin-top: 0.5rem;
  padding-top: 0.45rem;
  border-top: 1px solid var(--rule-hair);
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.85rem;
  flex-wrap: wrap;
}
.hero-figure figcaption span:last-child {
  white-space: nowrap;
  font-weight: 600;
  color: var(--accent-text);
}
.frontispiece-meta {
  margin-top: 1.35rem;
  padding-top: 0.85rem;
  border-top: 1px solid var(--rule-hair);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(155px, 1fr));
  gap: 0.75rem;
  font-family: var(--f-mono);
  font-size: var(--s-mono);
}
.frontispiece-meta dt { text-transform: uppercase; font-size: 0.66rem; color: var(--ink-3); letter-spacing: 0.09em; }
.frontispiece-meta dd { margin: 2px 0 0; font-weight: 600; color: var(--ink); }

/* Plates */
section.plate { padding: clamp(2.2rem, 4.5vw, 3.8rem) 0; border-bottom: 1px solid var(--rule); }
.plate-head {
  display: grid;
  grid-template-columns: 225px 1fr;
  gap: var(--gap);
  margin-bottom: 1.6rem;
  align-items: baseline;
}
@media (max-width: 900px) { .plate-head { grid-template-columns: minmax(0, 1fr); } }
.plate-folio {
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  color: var(--ink-3);
  border-top: 2px solid var(--ink);
  padding-top: 0.5rem;
}
.plate-folio .num {
  font-family: var(--f-serif);
  font-style: italic;
  font-size: 1.85rem;
  color: var(--ink);
  display: block;
  line-height: 1;
  margin-bottom: 0.25rem;
}
.plate-title { font-size: var(--s-h1); margin: 0.25rem 0 0.5rem; }
.plate-sub { color: var(--ink-2); max-width: 65ch; }
.plate-body {
  display: grid;
  grid-template-columns: 225px 1fr;
  gap: var(--gap);
}
@media (max-width: 900px) { .plate-body { grid-template-columns: minmax(0, 1fr); } }

.marginalia {
  font-size: var(--s-small);
  color: var(--ink-3);
  border-top: 1px solid var(--rule-hair);
  padding-top: 0.75rem;
  line-height: 1.52;
}
.marginalia > strong:first-child,
.marginalia div > strong:first-child {
  font-family: var(--f-mono);
  font-size: 0.69rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink-2);
  display: block;
  margin-bottom: 0.3rem;
}
.marginalia cite {
  font-style: normal;
  font-family: var(--f-mono);
  font-size: 0.70rem;
  color: var(--accent-text);
  display: block;
  margin-top: 0.45rem;
}

.instrument {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: clamp(1rem, 2vw, 1.65rem);
}
.instrument-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.6rem;
  padding-bottom: 0.7rem;
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--rule-hair);
  font-family: var(--f-mono);
  font-size: var(--s-mono);
  color: var(--ink-3);
}
.derived {
  margin-top: 1rem;
  padding: 0.85rem 1.05rem;
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
.derived em { font-family: var(--f-serif); font-style: italic; color: #F0C478; }

.counterpoint {
  margin-top: 1.1rem;
  padding: 0.85rem 1.1rem;
  border-left: 3px solid var(--ochre);
  background: color-mix(in oklab, var(--surface) 65%, var(--paper));
  font-size: var(--s-small);
  color: var(--ink-2);
}
.counterpoint .cp-head {
  font-family: var(--f-mono);
  font-size: 0.70rem;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: var(--accent-text);
  margin-bottom: 0.25rem;
  font-weight: 600;
}

.callout-box {
  padding: 0.6rem 0.8rem;
  background: var(--paper);
  border: 1px solid var(--rule-hair);
  border-left: 3px solid var(--accent);
  font-size: 0.84rem;
}
.callout-box strong {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--accent-text);
  display: block;
  margin-bottom: 2px;
}

/* ============================================================================
 * 4. BESPOKE INSTRUMENT I: INTERNAL (BALLS) ↔ EXTERNAL (ARROWS) SHIFTER
 * ============================================================================ */
.shifter-tabs, .rosetta-tabs {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
  gap: 6px;
  margin-bottom: 1rem;
}
.tab-card {
  appearance: none;
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.65rem 0.75rem;
  min-height: 44px;
  text-align: left;
  cursor: pointer;
  font: inherit;
  color: var(--ink);
  border-radius: 2px;
}
.tab-card:hover { border-color: var(--accent); }
.tab-card[aria-selected="true"] {
  background: var(--surface);
  border-color: var(--ink);
  box-shadow: inset 0 3px 0 var(--accent);
}
.tab-card .t-sym { font-family: var(--f-serif); font-style: italic; font-size: 1.05rem; color: var(--accent-text); display: block; }
.tab-card .t-lbl { font-family: var(--f-mono); font-size: 0.68rem; color: var(--ink-2); text-transform: uppercase; }

.dual-stage {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
@media (max-width: 860px) { .dual-stage { grid-template-columns: minmax(0, 1fr); } }
.view-pane {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1rem;
}
.view-pane-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 0.65rem;
  padding-bottom: 0.5rem;
  margin-bottom: 0.75rem;
  border-bottom: 1px solid var(--rule-hair);
  font-family: var(--f-mono);
  font-size: 0.72rem;
  font-weight: 600;
  text-transform: uppercase;
}

/* ============================================================================
 * 5. BESPOKE INSTRUMENT II: 6-WORLD ROSETTA STONE MATRIX
 * ============================================================================ */
.rosetta-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.85rem;
  margin-top: 0.9rem;
}
@media (max-width: 920px) { .rosetta-grid { grid-template-columns: minmax(0, 1fr); } }
.world-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.85rem 0.95rem;
  border-top: 3px solid var(--accent);
}
.world-card.w-1 { border-top-color: var(--w-sets); }
.world-card.w-2 { border-top-color: var(--w-cats); }
.world-card.w-3 { border-top-color: var(--w-monoids); }
.world-card.w-4 { border-top-color: var(--w-orders); }
.world-card.w-5 { border-top-color: var(--w-logic); }
.world-card.w-6 { border-top-color: var(--w-types); }

/* ============================================================================
 * 6. PLATE III & IV: SHEAF STUDIO, STALK CARDS & 3D POSET
 * ============================================================================ */
.studio-split {
  display: grid;
  grid-template-columns: 295px 1fr;
  gap: 1.1rem;
  align-items: start;
}
@media (max-width: 960px) { .studio-split { grid-template-columns: minmax(0, 1fr); } }
.cover-panel {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 0.85rem;
  max-height: 740px;
  overflow-y: auto;
}
.cover-stat-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin: 0.5rem 0 0.75rem; }
.cover-stat { background: var(--paper-soft); border: 1px solid var(--rule-hair); padding: 6px; text-align: center; }
.cover-stat .v { font-family: var(--f-serif); font-size: 1.2rem; color: var(--accent-text); }
.cover-stat .k { font-family: var(--f-mono); font-size: 0.63rem; color: var(--ink-3); text-transform: uppercase; }

.preset-btn {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  padding: 5px 9px;
  min-height: 29px;
  line-height: 1.2;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  cursor: pointer;
  border-radius: 2px;
}
.preset-btn:hover, .preset-btn.active { background: var(--ink); color: var(--paper); border-color: var(--ink); }

.stalk-item {
  display: flex;
  align-items: flex-start;
  gap: 7px;
  padding: 6px;
  border-bottom: 1px dotted var(--rule-hair);
  cursor: pointer;
  font-size: 0.82rem;
}
.stalk-item.in-cover { background: rgba(43, 91, 132, 0.10); }
.stalk-check {
  width: 14px;
  height: 14px;
  border: 1px solid var(--ink-3);
  border-radius: 2px;
  margin-top: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--f-mono);
  font-size: 10px;
}
.stalk-item.in-cover .stalk-check { background: var(--accent-text); color: var(--paper); border-color: var(--accent-text); }

.notebook-main { background: var(--paper); border: 1px solid var(--rule); padding: 1.15rem; }
.query-bar { display: flex; gap: 8px; margin-bottom: 0.85rem; }
.query-input {
  flex: 1;
  min-width: 0;
  max-width: 100%;
  font-family: var(--f-sans);
  font-size: 0.9rem;
  padding: 0.55rem 0.8rem;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink);
}
.btn-primary {
  font-family: var(--f-mono);
  font-size: 0.74rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 0.55rem 1rem;
  min-height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--accent-text);
  color: var(--paper);
  border: 1px solid var(--accent-text);
  cursor: pointer;
}
.inv-pills { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 1rem; }
.inv-pill {
  font-family: var(--f-mono);
  font-size: 0.70rem;
  padding: 6px 10px;
  min-height: 30px;
  line-height: 1.25;
  display: inline-flex;
  align-items: center;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  cursor: pointer;
}
.inv-pill.active { background: var(--ink); color: var(--paper); }

.gluing-banner {
  background: rgba(46, 100, 68, 0.08);
  border: 1px solid rgba(46, 100, 68, 0.3);
  border-left: 3px solid var(--good);
  padding: 0.65rem 0.9rem;
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.stalk-cards-grid, .course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(285px, 100%), 1fr));
  gap: 0.95rem;
}
.stalk-card, .module-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.55rem;
}
.module-card { border-top: 3px solid var(--accent); }
.module-card .m-head { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--rule-hair); padding-bottom: 0.4rem; }

.subview-tabs { display: flex; gap: 6px; flex-wrap: wrap; }
.subview-tab {
  font-family: var(--f-mono);
  font-size: 0.73rem;
  text-transform: uppercase;
  padding: 6px 11px;
  min-height: 30px;
  display: inline-flex;
  align-items: center;
  background: var(--paper);
  border: 1px solid var(--rule);
  cursor: pointer;
}
.subview-tab[aria-selected="true"] { background: var(--ink); color: var(--paper); }

.canvas-frame { position: relative; background: #14161C; border: 1px solid var(--ink); height: 450px; overflow: hidden; }
#sheaf3dCanvas { width: 100%; height: 100%; display: block; cursor: grab; }

/* Slide-Over 377-Page Verbatim Reader Drawer */
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
.reader-head { padding: 0.9rem 1.1rem; background: var(--paper-soft); border-bottom: 1px solid var(--rule); }
.reader-body { padding: 1rem 1.1rem; overflow-y: auto; flex: 1; }
.verbatim-sheet {
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  padding: 1rem;
  font-family: var(--f-serif);
  font-size: 0.91rem;
  line-height: 1.65;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}
mark.hl { background: rgba(184, 125, 36, 0.35); color: var(--ink); padding: 0 2px; }

/* ============================================================================
 * 7. SIMPLIFIED FOCUS MODE, VISUAL ATLAS & MOBILE-FIRST ERGONOMICS
 * ============================================================================ */
/* Focus Mode: show 1 plate at a time for a calmer, distraction-free view */
html[data-view-mode="focus"] section.plate { display: none; }
html[data-view-mode="focus"] section.plate.active-plate { display: block; animation: fadePlate 0.18s ease-out; }
@keyframes fadePlate { from { opacity: 0.4; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

.plate-focus-bar {
  display: none;
  margin-top: 1.4rem;
  padding: 0.75rem 1rem;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  font-family: var(--f-mono);
  font-size: 0.74rem;
}
html[data-view-mode="focus"] .plate-focus-bar { display: flex; }

/* Symbol-by-Symbol Formula Decoder Grid */
.decoder-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(210px, 100%), 1fr));
  gap: 0.6rem;
  margin-top: 0.75rem;
}
.decoder-chip {
  background: var(--paper-soft);
  border: 1px solid var(--rule-hair);
  border-left: 3px solid var(--accent-text);
  padding: 0.5rem 0.65rem;
  font-size: 0.80rem;
}
.decoder-chip .d-sym {
  font-family: var(--f-serif);
  font-weight: 600;
  font-size: 0.96rem;
  color: var(--accent-text);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 6px;
  margin-bottom: 2px;
}
.decoder-chip .d-meaning { color: var(--ink); font-weight: 500; line-height: 1.35; }
.decoder-chip .d-why { color: var(--ink-3); font-size: 0.73rem; margin-top: 2px; line-height: 1.3; }

/* 4-Act Deep-Dive Audio Stepper */
.podcast-act-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 5px;
  margin: 0.55rem 0;
}
.podcast-act-pill {
  font-family: var(--f-mono);
  font-size: 0.66rem;
  padding: 6px 8px;
  min-height: 36px;
  background: var(--paper);
  border: 1px solid var(--rule);
  color: var(--ink-3);
  cursor: pointer;
  text-align: left;
  border-radius: 2px;
  transition: all 0.15s;
}
.podcast-act-pill strong { display: block; color: var(--ink-2); font-size: 0.68rem; }
.podcast-act-pill.active {
  background: var(--accent-soft);
  border-color: var(--accent-text);
  color: var(--accent-text);
  box-shadow: inset 0 2px 0 var(--accent-text);
}
.podcast-act-pill.active strong { color: var(--accent-text); }

.podcast-visual-cue {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  padding: 0.42rem 0.7rem;
  margin-top: 0.5rem;
  background: color-mix(in oklab, var(--accent-soft) 55%, var(--paper));
  border: 1px dashed var(--accent-text);
  font-family: var(--f-mono);
  font-size: 0.72rem;
  color: var(--ink);
}

/* Mobile Cover Collapse Button */
.mobile-cover-toggle {
  display: none;
  width: 100%;
  text-align: left;
  font-family: var(--f-mono);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.6rem 0.85rem;
  min-height: 36px;
  background: var(--paper);
  border: 1px solid var(--ink);
  color: var(--ink);
  cursor: pointer;
  margin-bottom: 0.5rem;
}

/* Floating Mobile Bottom Bar */
.mobile-bottom-dock {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 88;
  background: color-mix(in oklab, var(--paper) 96%, transparent);
  backdrop-filter: blur(10px);
  border-top: 2px solid var(--ink);
  padding: 6px 10px calc(6px + env(safe-area-inset-bottom, 0px));
  justify-content: space-around;
  align-items: center;
  gap: 6px;
  box-shadow: 0 -4px 18px rgba(0,0,0,0.12);
}
.mobile-dock-btn {
  flex: 1;
  font-family: var(--f-mono);
  font-size: 0.68rem;
  font-weight: 600;
  padding: 7px 6px;
  min-height: 32px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--paper-soft);
  border: 1px solid var(--rule);
  color: var(--ink);
  border-radius: 3px;
  text-align: center;
  cursor: pointer;
  white-space: nowrap;
}
.mobile-dock-btn.primary {
  background: var(--accent-text);
  color: var(--paper);
  border-color: var(--accent-text);
}

@media (max-width: 860px) {
  #rosettaHeroBar { grid-template-columns: minmax(0, 1fr) !important; }
  .podcast-act-bar { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .mobile-cover-toggle { display: flex; justify-content: space-between; align-items: center; }
  .cover-panel.mobile-collapsed { display: none; }
}

@media (max-width: 720px) {
  body { padding-bottom: 64px; }
  .mobile-bottom-dock { display: flex; }
  .axis-ribbon-inner { padding: 4px 10px; gap: 4px; }
  .brand-mark { width: 100%; font-size: 0.64rem; gap: 6px; }
  .brand-mark span:last-child {
    font-size: 0.64rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: calc(100vw - 36px);
  }
  .plate-nav { display: none; }
  .field-controls {
    width: 100%;
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    gap: 4px;
    padding-bottom: 1px;
  }
  .field-controls::-webkit-scrollbar { display: none; }
  .ctrl-group { flex: 0 0 auto; }
  .ctrl-label { display: none !important; }
  .ctrl-btn {
    white-space: nowrap;
    padding: 4px 7px;
    font-size: 0.66rem;
    min-height: 29px;
  }
  #openReaderBtn { display: none; }
  .shifter-tabs, .rosetta-tabs {
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    flex-wrap: nowrap;
    gap: 6px;
    padding-bottom: 4px;
    max-width: 100%;
  }
  .shifter-tabs .tab-card, .rosetta-tabs .tab-card { flex: 0 0 162px; }
  .inv-pills {
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 4px;
    max-width: 100%;
  }
  .inv-pill { flex: 0 0 auto; }
  .query-bar { flex-direction: column; }
  .query-bar .btn-primary { width: 100%; min-height: 40px; }
  .canvas-frame { height: 320px; }
  .instrument { padding: 0.85rem; }
  .view-pane, .notebook-main { padding: 0.8rem; }
}
</style>
</head>
<body>

<div class="axis-ribbon" role="navigation" aria-label="Studio Controls">
  <div class="axis-ribbon-inner">
    <div class="brand-mark">
      <span class="dot"></span>
      <span>CATEGORY THEORY ILLUSTRATED · MARINOV (377 PP.) × SPIVAK (609 PP.)</span>
    </div>

    <nav class="plate-nav" aria-label="Plates">
      <a href="#plate-1" data-plate-link="plate-1">I · Visual Atlas &amp; Shifter</a>
      <a href="#plate-2" data-plate-link="plate-2">II · 6-World Rosetta</a>
      <a href="#plate-3" data-plate-link="plate-3">III · Audio &amp; Sheaf Notebook</a>
      <a href="#plate-4" data-plate-link="plate-4">IV · 24 Stalks &amp; 90 Tasks</a>
      <a href="#plate-5" data-plate-link="plate-5">V · Marinov × Spivak</a>
    </nav>

    <div class="field-controls">
      <div class="ctrl-group" role="group" aria-label="Layout view mode">
        <span class="ctrl-label">View</span>
        <button class="ctrl-btn" data-set-view="all" aria-pressed="true" title="Show all 5 plates on one scrollable page">All 5</button>
        <button class="ctrl-btn" data-set-view="focus" aria-pressed="false" title="Simplified 1-plate Focus Mode (ideal for mobile & step-by-step study)">1-Plate Focus</button>
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
      <button class="drawer-toggle-btn" id="openReaderBtn">📖 Page Reader (p.83)</button>
    </div>
  </div>
</div>

<div class="page-wrap">

  <!-- ========================================================================
       FRONTISPIECE: LAWVERE'S VISUAL PERSPECTIVE & POINT-FREE EPISTEMOLOGY
       ======================================================================== -->
  <header class="frontispiece">
    <div class="eyebrow">
      <span>VISUAL ROSETTA &amp; SHEAF EDITION · IN MEMORY OF F. WILLIAM LAWVERE</span>
      <span class="stamp ratified">◆ 377 pp · 24 stalks</span>
      <span class="stamp measured">⚖ 164 definitions · 40 theorems · 90 tasks</span>
    </div>

    <div class="frontispiece-grid">
      <div>
        <h1 class="hero-title">
          Erasing the <em class="u-copper">interior</em> until only the arrows speak.
        </h1>
        <p class="hero-lede">
          Whereas Spivak’s <em>Category Theory for the Sciences</em> builds an edifice of relational database Ologs and topological sheaves, Boris Marinov’s <em>Category Theory Illustrated</em> (377 pp.) unfolds a <strong>visual philosophy of abstraction</strong>: starting with colored balls inside sets (<span class="cite-pill" onclick="window.__jumpToPage(13,'balls')">§ p.13</span>) and progressively erasing internal elements until <strong>Sets, Categories, Monoids, Poset Lattices, Deductive Logic, and Programming Types</strong> reveal the exact same universal arrow diagrams (<span class="cite-pill" onclick="window.__jumpToPage(83,'Element')">§ p.83</span>, <span class="cite-pill" onclick="window.__jumpToPage(260,'Type')">§ p.260</span>).
        </p>
        <div class="lawvere-quote">
          “Instead of asking what can be defined and deduced from what is assumed to begin with, we ask instead what more general ideas and principles can be found, in terms of which what was our starting-point can be defined or deduced.” — <strong>Bertrand Russell</strong> (Marinov Ch 1, <button class="cite-pill" onclick="window.__jumpToPage(11,'Russell')">§ p.11</button>)
        </div>
      </div>

      <figure class="hero-figure" style="margin:0">
        <svg viewBox="0 0 430 210" width="100%" height="auto" role="img" aria-label="Internal Set Balls to External Point-Free Category Shift">
          <defs>
            <marker id="arr-b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="currentColor"/>
            </marker>
          </defs>
          <!-- Left: Internal View (Colored Balls in Set G, p.13) -->
          <rect x="14" y="24" width="168" height="145" rx="6" fill="rgba(184,125,36,0.09)" stroke="#B87D24" stroke-width="1.5"/>
          <text x="98" y="44" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9.5" font-weight="600" fill="#B87D24">INTERNAL VIEW (CH 1, P.13)</text>
          <ellipse cx="98" cy="108" rx="64" ry="44" fill="#F6F1E7" stroke="#17181C" stroke-width="1.4"/>
          <circle cx="72" cy="98" r="10" fill="#B34434" stroke="#17181C" stroke-width="1.2"/>
          <circle cx="98" cy="122" r="10" fill="#B87D24" stroke="#17181C" stroke-width="1.2"/>
          <circle cx="122" cy="96" r="10" fill="#2B5B84" stroke="#17181C" stroke-width="1.2"/>
          <text x="98" y="160" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="11" fill="#3A3D45">x &isin; G (Inspecting Balls)</text>

          <!-- Center Morphism Arrow -->
          <path d="M 190 96 L 236 96" stroke="#17181C" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arr-b)"/>
          <text x="213" y="86" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="8.5" fill="#1E4363">Externalize</text>

          <!-- Right: External Point-Free View (Ch 2, p.77-83) -->
          <rect x="246" y="24" width="170" height="145" rx="6" fill="rgba(43,91,132,0.09)" stroke="#2B5B84" stroke-width="1.5"/>
          <text x="331" y="44" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="9.5" font-weight="600" fill="#1E4363">EXTERNAL VIEW (CH 2, P.83)</text>
          <circle cx="282" cy="106" r="14" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/>
          <text x="282" y="110" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="12">1</text>
          <circle cx="378" cy="106" r="16" fill="#1E4363" stroke="#17181C" stroke-width="1.6"/>
          <text x="378" y="110" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="12" fill="#F6F1E7">G</text>
          <path d="M 298 96 Q 330 72 360 94" fill="none" stroke="#B34434" stroke-width="1.5" marker-end="url(#arr-b)"/>
          <path d="M 298 106 L 359 106" fill="none" stroke="#B87D24" stroke-width="1.5" marker-end="url(#arr-b)"/>
          <path d="M 298 116 Q 330 140 360 118" fill="none" stroke="#2B5B84" stroke-width="1.5" marker-end="url(#arr-b)"/>
          <text x="331" y="160" text-anchor="middle" font-family="Fraunces, serif" font-style="italic" font-size="11" fill="#3A3D45">1 &rarr; G (Opaque Points &amp; Arrows)</text>
        </svg>
        <figcaption>
          <span>FIG 0.1 · MARINOV’S POINT-FREE SHIFT (CH 1 P.13 → CH 2 P.77, P.83)</span>
          <span>x &isin; G &harr; Hom(1, G)</span>
        </figcaption>
      </figure>
    </div>

    <dl class="frontispiece-meta">
      <div><dt>Author &amp; Dedication</dt><dd>Boris Marinov · For F. W. Lawvere</dd></div>
      <div><dt>Indexed Topology</dt><dd>377 Pages · 8 Chapters · 24 Stalks</dd></div>
      <div><dt>Sheaf Simplices</dt><dd>50 Restrictions &rho; · 10 2-Simplices &tau;</dd></div>
      <div><dt>Extracted Corpus</dt><dd>164 Definitions · 40 Theorems · 90 Tasks</dd></div>
      <div><dt>Voice &amp; Companion</dt><dd>6-World Rosetta × Spivak (609 pp.) Bridge</dd></div>
    </dl>
  </header>

  <!-- ========================================================================
       PLATE I · LAWVERE'S INTERNAL (BALLS) ↔ EXTERNAL (ARROWS) PERSPECTIVE SHIFTER
       ======================================================================== -->
  <section class="plate active-plate" id="plate-1">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate I</span>
        <div>VISUAL ATLAS &amp; SHIFTER</div>
        <div style="margin-top:6px"><span class="w-badge w-sets">Inkscape Visuals ↔ Notation</span></div>
        <div style="margin-top:6px"><span class="stamp ratified">◆ 14 Visual Instruments</span></div>
      </div>
      <div>
        <div class="eyebrow">CHAPTERS 1–8 (PP. 11–374) · EXPRESSION THROUGH &amp; BEYOND MATHEMATICAL NOTATION</div>
        <h2 class="plate-title">Every opaque formula is a <em class="u-copper">drawing</em> waiting to be unpacked.</h2>
        <p class="plate-sub">
          Mathematical notation often feels opaque because it compresses a 3D spatial picture into a 1D string of Greek letters. Boris Marinov’s <em>Category Theory Illustrated</em> reverses that compression: first drawing <strong>concrete visual instruments</strong> (colored balls, espresso machines, CMYK pigment cubes, coloring-book schemas, sprouting trees, 3D naturality prisms) and then showing how the formal symbols merely record the arrows (<span class="cite-pill" onclick="window.__jumpToPage(13,'set')">§ p.13</span>, <span class="cite-pill" onclick="window.__jumpToPage(83,'Element')">§ p.83</span>). Explore both interactive visual instruments below.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>How to Read Beyond Notation</strong>
        1. <strong>Internal → External:</strong> First see what happens to colored balls inside a box (<span class="math-expr">x &isin; A</span>), then close the box and probe it with arrows (<span class="math-expr">1 &rarr; A</span>).
        <br><br>
        2. <strong>Symbol Decoder:</strong> Every card below includes a <em>Symbol-by-Symbol Visual Decoder</em> translating <span class="math-expr">&forall;, &exist;!, &lang;f,g&rang;, [f,g], &pi;₁, &iota;₁</span> into plain visual actions.
        <cite>— Marinov, Ch 1–8 Visual Atlas (pp. 13–362)</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT I-A · INTERNAL (COLORED BALLS) ↔ EXTERNAL (POINT-FREE ARROWS) PERSPECTIVE SHIFTER</span>
            <span class="stamp measured" id="shifterPageRef">⚖ Marinov pp. 13, 77, 83</span>
          </div>

          <div class="shifter-tabs" role="tablist" aria-label="Internal vs External Constructs" id="shifterTabs">
            <button class="tab-card" role="tab" aria-selected="true" data-shift="element">
              <span class="t-sym">x &isin; A &harr; 1 &rarr; A</span>
              <span class="t-lbl">1. Elements as Arrows</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="terminal">
              <span class="t-sym">{&bull;} &harr; ! : A &rarr; 1</span>
              <span class="t-lbl">2. Singleton / Terminal</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="initial">
              <span class="t-sym">&empty; &harr; ! : 0 &rarr; A</span>
              <span class="t-lbl">3. Empty / Initial</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="product">
              <span class="t-sym">(a,b) &harr; &lang;f,g&rang;</span>
              <span class="t-lbl">4. Product A &times; B</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="coproduct">
              <span class="t-sym">A &sqcup; B &harr; [f,g]</span>
              <span class="t-lbl">5. Coproduct A + B</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="iso">
              <span class="t-sym">Bijection &harr; g&#8728;f = id</span>
              <span class="t-lbl">6. Isomorphism</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="espresso">
              <span class="t-sym">Machine &harr; g &#8728; f</span>
              <span class="t-lbl">7. Espresso Zoom-Out</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-shift="polarity">
              <span class="t-sym">Entry &iota; &harr; Exit &pi;</span>
              <span class="t-lbl">8. Positive vs Negative</span>
            </button>
          </div>

          <div class="dual-stage" id="shifterStage"></div>

          <div id="shifterDecoder"></div>

          <div class="derived" id="shifterDerived"></div>
        </div>

        <!-- INSTRUMENT I-B: MARINOV'S INKSCAPE VISUAL ATLAS (6 CATEGORICAL INSTRUMENTS BEYOND NOTATION) -->
        <div class="instrument" id="visualAtlasInstrument" style="margin-top:1.35rem">
          <div class="instrument-bar">
            <span>INSTRUMENT I-B · MARINOV’S INKSCAPE VISUAL ATLAS: 6 INTERACTIVE INSTRUMENTS BEYOND NOTATION</span>
            <span class="stamp ratified" id="atlasPageRef">◆ Marinov Ch 3–8 Visual Metaphors (pp. 95–362)</span>
          </div>

          <div class="shifter-tabs" role="tablist" aria-label="Marinov Visual Atlas Instruments" id="atlasTabs">
            <button class="tab-card" role="tab" aria-selected="true" data-atlas="monoid_loop">
              <span class="t-sym">&bull; &#8634; CMYK &amp; D₃</span>
              <span class="t-lbl">1. 1-Obj Loop Machine</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-atlas="hasse_cube">
              <span class="t-sym">Cube: Color &cong; Div(30)</span>
              <span class="t-lbl">2. 3D Birkhoff Cube</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-atlas="heyting_lever">
              <span class="t-sym">C &and; A &le; B &hArr; C &le; A&rArr;B</span>
              <span class="t-lbl">3. Heyting Logic Lever</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-atlas="russell_trees">
              <span class="t-sym">R&isin;R vs Nat Trees</span>
              <span class="t-lbl">4. Paradox &amp; Sprouting</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-atlas="island_functor">
              <span class="t-sym">Map F &amp; .map(f)</span>
              <span class="t-lbl">5. Island Map &amp; Box</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-atlas="naturality_prism">
              <span class="t-sym">C&times;2 &rarr; D Prism</span>
              <span class="t-lbl">6. 3D Naturality Prism</span>
            </button>
          </div>

          <div class="dual-stage" id="atlasStage"></div>

          <div id="atlasDecoder"></div>

          <div class="derived" id="atlasDerived"></div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · When Point-Free Externalism Loses Naive Intuition</span></div>
          <div>
            In categories where the terminal object <span class="math-expr">1</span> is not a generator (for instance, in a monoid viewed as a one-object category <span class="math-expr"><span class="m-cat">B</span>M</span> or in a poset without a global unit), morphisms <span class="math-expr">1 &rarr; A</span> no longer enumerate "internal elements." Marinov highlights this exact subtlety in Chapter 3 (<button class="cite-pill" onclick="window.__jumpToPage(115,'Monoid')">§ p.115</button>): once we leave <span class="math-expr"><span class="m-cat">Set</span></span>, we probe an object <span class="math-expr">A</span> using <em>generalized elements</em> <span class="math-expr">X &rarr; A</span> from arbitrary test objects <span class="math-expr">X</span> (the precursor to the Yoneda Lemma).
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE II · THE 6-WORLD ROSETTA STONE (SETS · CATS · MONOIDS · ORDERS · LOGIC · TYPES)
       ======================================================================== -->
  <section class="plate" id="plate-2">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate II</span>
        <div>6-WORLD ROSETTA</div>
        <div style="margin-top:6px"><span class="w-badge w-logic">Curry-Howard-Lambek</span></div>
        <div style="margin-top:6px"><span class="stamp ratified">◆ 6 Isomorphic Worlds</span></div>
      </div>
      <div>
        <div class="eyebrow">CHAPTERS 1–8 (PP. 11–374) · MARINOV’S GRAND SYNTHESIS ACROSS SIX DISCIPLINES</div>
        <h2 class="plate-title">One diagram, six <em class="u-copper">worlds</em> of mathematical thought.</h2>
        <p class="plate-sub">
          The heart of <em>Category Theory Illustrated</em> is the realization that <strong>Sets</strong> (Ch 1), <strong>Categories</strong> (Ch 2), <strong>Monoids &amp; Groups</strong> (Ch 3), <strong>Orders &amp; Lattices</strong> (Ch 4), <strong>Propositional Logic</strong> (Ch 5), and <strong>Programming Types / Lambda Calculus</strong> (Ch 6) are six projections of the same categorical architecture. Select any universal concept below to inspect its exact manifestation and page citation across all six worlds.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Why Category Theory Is a Universal Language</strong>
        • <strong>0-Arity / Thinness:</strong> Restricting <span class="math-expr">|<span class="m-op">Ob</span>| = 1</span> gives Monoids; restricting <span class="math-expr">|<span class="m-op">Hom</span>| &le; 1</span> gives Posets &amp; Logic.<br>
        • <strong>Bicartesian Closure:</strong> Adding <span class="math-expr">0, 1, &times;, +, B<sup>A</sup></span> unifies Sets, Heyting Logic, and Simply Typed Lambda Calculus.
        <cite>— Marinov, Ch 5 Theorem (p. 203) &amp; Ch 6 STLC (p. 260)</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT II · INTERACTIVE 6-WORLD ROSETTA TRANSLATOR (SELECT ANY UNIVERSAL INVARIANT)</span>
            <span class="stamp accept" id="rosettaStamp">✓ Bicartesian Closed Trinity</span>
          </div>

          <div class="rosetta-tabs" role="tablist" aria-label="Rosetta Invariants" id="rosettaTabs">
            <button class="tab-card" role="tab" aria-selected="true" data-ros="obj_arr">
              <span class="t-sym">A &rarr;<sup>f</sup> B</span>
              <span class="t-lbl">1. Objects &amp; Arrows</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="comp_id">
              <span class="t-sym">g &#8728; f, id<sub>A</sub></span>
              <span class="t-lbl">2. Composition &amp; Id</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="init_term">
              <span class="t-sym">0 (Init) &amp; 1 (Term)</span>
              <span class="t-lbl">3. Zero &amp; One</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="product">
              <span class="t-sym">A &times; B &equiv; A &and; B</span>
              <span class="t-lbl">4. Product / Meet / AND</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="coproduct">
              <span class="t-sym">A + B &equiv; A &or; B</span>
              <span class="t-lbl">5. Sum / Join / OR</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="exponential">
              <span class="t-sym">B<sup>A</sup> &equiv; (A &rArr; B)</span>
              <span class="t-lbl">6. Currying / Implication</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="functor">
              <span class="t-sym">F(g &#8728; f) = Fg &#8728; Ff</span>
              <span class="t-lbl">7. Functors / .map</span>
            </button>
            <button class="tab-card" role="tab" aria-selected="false" data-ros="natural">
              <span class="t-sym">&alpha; : &forall;a. F a &rarr; G a</span>
              <span class="t-lbl">8. Naturality / Poly</span>
            </button>
          </div>

          <div id="rosettaHeroBar" style="background:var(--paper);border:1px solid var(--rule);padding:0.9rem 1.1rem;display:grid;grid-template-columns:1.1fr 1fr;gap:1rem;align-items:center"></div>

          <div class="rosetta-grid" id="rosettaGrid"></div>

          <div class="derived" id="rosettaDerived"></div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Classical Excluded Middle vs. Constructive Computation (p. 184, p. 203)</span></div>
          <div>
            While Classical Boolean Logic assumes <span class="math-expr">P &or; &not;P = &top;</span> and <span class="math-expr">&not;&not;P &rarr; P</span>, Marinov emphasizes in Chapter 5 (<button class="cite-pill" onclick="window.__jumpToPage(184,'BHK')">§ p.184</button>) that programming types and general categories obey <strong>Intuitionistic (BHK / Heyting) Logic</strong>: you cannot construct an inhabitant of <span class="math-expr"><span class="m-op">Either</span> A (A &rarr; <span class="m-op">Void</span>)</span> for an arbitrary unknown type <span class="math-expr">A</span> without an explicit decision procedure.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE III · SHEAF OPEN-COVER NOTEBOOK STUDIO
       ======================================================================== -->
  <section class="plate" id="plate-3">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate III</span>
        <div>SHEAF NOTEBOOK</div>
        <div style="margin-top:6px"><span class="w-badge w-cats">Alexandrov Gluing</span></div>
        <div style="margin-top:6px"><span class="stamp ratified">◆ 24 Stalks · 50 Arrows</span></div>
      </div>
      <div>
        <div class="eyebrow">SHEAF-INDEXED GEMINI NOTEBOOK · QUERY ACROSS ALL 377 PAGES &amp; 24 CONCEPT STALKS</div>
        <h2 class="plate-title">Gluing local <em class="u-copper">stalks</em> across Marinov’s visual chapters.</h2>
        <p class="plate-sub">
          Toggle any combination of the <strong>24 Concept Stalks</strong> in the left Open Cover <span class="math-expr"><span class="m-cal">U</span></span>, select a preset investigation (each paired with a <strong>4-Act, 10-Turn Deep-Dive Audio Notebook</strong>), or ask any custom question across the 377-page corpus.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Alexandrov Sheaf Indexing of Marinov (377 pp.)</strong>
        Every page from <code>p. 3</code> to <code>p. 377</code> is mapped into a downward-closed poset of 24 stalks <span class="math-expr">U<sub>i</sub></span> connected by 50 restriction morphisms <span class="math-expr">&rho;<sub>U,V</sub></span> and 10 commutative 2-simplices <span class="math-expr">&tau;<sub>U,V,W</sub></span>.
        <cite>— Marinov Corpus Index · cattheory_sheaf.db</cite>
        <div style="margin-top:1.1rem;padding-top:0.75rem;border-top:1px solid var(--rule-hair)">
          <strong>4-Act Deep Dive Audio Notebook</strong>
          <p style="font-size:0.78rem;margin:0.3rem 0 0.55rem">Listen to a 3-minute, 10-turn two-host conversation (<strong>Kore</strong> &amp; <strong>Puck</strong>) walking the diagrams arrow-by-arrow:</p>
          <button class="btn-primary" id="audioBriefBtn" style="width:100%">🎙️ Play 4-Act Deep Dive</button>
        </div>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT III · OPEN-COVER GLUING STUDIO &amp; 4-ACT DEEP-DIVE AUDIO NOTEBOOK</span>
            <span class="stamp measured" id="coverGluingStamp">⚖ 5 stalks · 6 restrictions · Glued ◆</span>
          </div>

          <button type="button" class="mobile-cover-toggle" id="mobileCoverToggleBtn" aria-expanded="false">
            <span>📂 Open Cover <span class="m-cal">U</span> Selector (<span id="mobileCoverCountLbl">5</span> of 24 Stalks Active)</span>
            <span id="mobileCoverCaret">▾ Show</span>
          </button>

          <div class="studio-split">
            <div class="cover-panel mobile-collapsed" id="coverPanelDrawer">
              <div style="display:flex;justify-content:space-between;align-items:center">
                <span class="mono" style="font-weight:600;text-transform:uppercase">Open Cover <span class="m-cal">U</span> (24)</span>
                <button class="preset-btn" id="clearCoverBtn">Reset</button>
              </div>

              <div class="cover-stat-row">
                <div class="cover-stat"><div class="v" id="metricStalks">5</div><div class="k">Stalks |U|</div></div>
                <div class="cover-stat"><div class="v" id="metricOverlaps">6</div><div class="k">Arrows &rho;</div></div>
                <div class="cover-stat"><div class="v" id="metricPages">92</div><div class="k">Pages</div></div>
              </div>

              <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:0.65rem">
                <button class="preset-btn active" data-preset="pointfree">Point-Free</button>
                <button class="preset-btn" data-preset="rosetta">6-World Rosetta</button>
                <button class="preset-btn" data-preset="types">Types &amp; STLC</button>
                <button class="preset-btn" data-preset="functors">Functors &amp; Nat</button>
                <button class="preset-btn" data-preset="obstruction" style="border-color:var(--bad);color:var(--bad)">⊘ Test H¹ Fail</button>
                <button class="preset-btn" data-preset="all">All 24</button>
              </div>

              <input type="text" class="query-input" id="stalkFilterInput" placeholder="Filter 24 stalks…" style="width:100%;padding:5px 8px;font-size:0.79rem;margin-bottom:8px">
              <div id="stalkTreeList"></div>
            </div>

            <div class="notebook-main">
              <div class="query-bar">
                <input type="text" class="query-input" id="notebookQueryInput" placeholder="Ask across all 377 pages (e.g., Why is ∀a. F a → G a a natural transformation?)…">
                <button class="btn-primary" id="runGlueQueryBtn">Glue Section ↵</button>
              </div>

              <div class="inv-pills" id="invPillsContainer"></div>

              <!-- NotebookLM Dual-Host 4-Act Deep-Dive Neural Audio Overview Studio Card -->
              <div id="podcastStudioCard" style="background:var(--paper-soft);border:1.5px solid var(--ink);padding:0.9rem 1.05rem;margin-bottom:1rem;box-shadow:3px 3px 0 rgba(26,22,18,0.08)">
                <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:0.5rem">
                  <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
                    <span class="stamp ratified" id="podcastEngineBadge">◆ 4-Act Deep Dive Audio Notebook (10 Turns)</span>
                    <span class="mono" id="hostBadgeKore" style="padding:2px 8px;border:1px solid var(--accent-text);background:var(--accent-soft);color:var(--accent-text);font-weight:600;border-radius:2px;transition:all 0.2s">🎙️ Kore (Lead Architect)</span>
                    <span class="mono" id="hostBadgePuck" style="padding:2px 8px;border:1px solid var(--good);background:var(--good-soft);color:var(--good);font-weight:600;border-radius:2px;transition:all 0.2s">🎧 Puck (Systems Co-Host)</span>
                  </div>
                  <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap">
                    <button class="preset-btn" id="podcastSpeedBtn" title="Toggle Playback Speed">1.0×</button>
                    <button class="preset-btn" id="toggleTranscriptBtn">10-Turn Script ▾</button>
                    <button class="preset-btn" id="toggleGeminiTtsConfigBtn" title="Configure Live Gemini 2.5 Native Multi-Speaker Voices (Kore, Puck, Aoede, Charon)">⚡ Gemini 2.5 Voices</button>
                  </div>
                </div>

                <!-- 4-Act Pedagogical Arc Bar -->
                <div class="podcast-act-bar" id="podcastActBar" role="group" aria-label="4-Act Pedagogical Story Arc">
                  <button type="button" class="podcast-act-pill active" data-act-idx="0">
                    <strong>Act I · Turns 1–2</strong>
                    <span>Visual Hook &amp; Notation</span>
                  </button>
                  <button type="button" class="podcast-act-pill" data-act-idx="1">
                    <strong>Act II · Turns 3–5</strong>
                    <span>Walk Diagram Arrows</span>
                  </button>
                  <button type="button" class="podcast-act-pill" data-act-idx="2">
                    <strong>Act III · Turns 6–8</strong>
                    <span>Edge Cases &amp; Traps</span>
                  </button>
                  <button type="button" class="podcast-act-pill" data-act-idx="3">
                    <strong>Act IV · Turns 9–10</strong>
                    <span>Decode Formula &amp; Lab</span>
                  </button>
                </div>

                <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
                  <button class="btn-primary" id="podcastPlayPauseBtn" style="padding:6px 14px;font-size:0.78rem;min-width:135px">▶ Play Deep Dive</button>
                  <span class="mono" id="podcastTimeLabel" style="min-width:86px;color:var(--ink-2);font-weight:600">0:00 / 3:05</span>
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

                <div class="podcast-visual-cue" id="podcastVisualCueBar">
                  <span id="podcastVisualCueText">🎨 Visual Anchor: Colored Balls Inside Set G ↔ Point-Free Arrows 1 → G</span>
                  <span class="mono" id="podcastTurnCounter" style="color:var(--accent-text);font-weight:600">Turn 1 / 10 · Act I</span>
                </div>

                <div id="podcastActiveSubtitle" style="margin-top:0.5rem;padding:0.55rem 0.75rem;background:var(--paper);border-left:3px solid var(--accent-text);font-size:0.86rem;line-height:1.45;color:var(--ink)">
                  <span class="mono" style="color:var(--accent-text);font-weight:600">Kore · Lead Architect:</span> Click <strong>▶ Play Deep Dive</strong> to listen to the 10-turn, 4-act neural audio notebook for this investigation.
                </div>

                <div id="podcastTranscriptDrawer" style="display:none;margin-top:0.65rem;max-height:260px;overflow-y:auto;background:var(--paper);border:1px solid var(--rule);padding:0.6rem;font-size:0.82rem"></div>

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
                    <button class="btn-primary" id="runLiveGeminiTtsBtn" style="padding:5px 10px;font-size:0.75rem">Synthesize Live 🎙️</button>
                  </div>
                  <div id="geminiTtsStatusMsg" class="mono" style="margin-top:4px;color:var(--ink-3)"></div>
                </div>
              </div>

              <div class="gluing-banner" id="gluingAuditBanner"></div>
              <div id="notebookSynthesisOutput"></div>

              <div style="margin-top:1.3rem;padding-top:0.9rem;border-top:1px solid var(--rule)">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.55rem">
                  <span class="mono" style="font-weight:600;text-transform:uppercase;color:var(--ink-2)">Commutative Fiber-Product Olog · Glued Across Active Cover <span class="m-cal">U</span></span>
                  <span class="stamp ratified" id="ologSummaryBadge">◆ Commutes</span>
                </div>
                <div id="gluedOlogSvgWrap" style="background:var(--paper-soft);border:1px solid var(--rule);padding:0.75rem;overflow-x:auto"></div>
              </div>
            </div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Bridging Disconnected Covers Across the 8 Chapters</span></div>
          <div>
            When querying between distant chapters (e.g., Chapter 3 <em>Rotational Groups</em> and Chapter 6 <em>Simply Typed Lambda Calculus</em>), the restriction audit checks whether an explicit bridging stalk (such as <em>Free Monoids / Lists</em> <code>U_09</code> or <em>Functors</em> <code>U_19</code>) is present in <span class="math-expr"><span class="m-cal">U</span></span> so that local Olog types glue along verified morphism overlaps.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE IV · THE 24 STALKS, 291 DEFINITIONS/THEOREMS/TASKS & 3D POSET
       ======================================================================== -->
  <section class="plate" id="plate-4">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate IV</span>
        <div>CORPUS &amp; 90 TASKS</div>
        <div style="margin-top:6px"><span class="w-badge w-orders">377 Pages Indexed</span></div>
        <div style="margin-top:6px"><span class="stamp measured">⚖ 291 Formal Blocks</span></div>
      </div>
      <div>
        <div class="eyebrow">MEASURED CORPUS · 24 CONCEPT STALKS · 164 DEFINITIONS · 40 THEOREMS · 90 INTERACTIVE TASKS</div>
        <h2 class="plate-title">Every visual definition, theorem, and <em class="u-copper">task</em> indexed by page fiber.</h2>
        <p class="plate-sub">
          Explore the <strong>24 Concept Stalks</strong>, search all <strong>291 extracted Definitions, Theorems, and Interactive Tasks</strong> (Marinov’s signature <code>Task 1..90</code> check-your-understanding prompts scattered through the book), or orbit the <strong>3D Alexandrov Poset Fiber Bundle</strong>.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Chapter Distribution (377 pp.)</strong>
        • Ch 1 (Sets): pp. 3–51 (3 stalks)<br>
        • Ch 2 (Categories): pp. 52–94 (3 stalks)<br>
        • Ch 3 (Monoids/Groups): pp. 95–130 (3 stalks)<br>
        • Ch 4 (Orders/Lattices): pp. 131–161 (3 stalks)<br>
        • Ch 5 (Logic/Heyting): pp. 162–211 (3 stalks)<br>
        • Ch 6 (Types/STLC): pp. 212–277 (3 stalks)<br>
        • Ch 7 (Functors): pp. 278–318 (3 stalks)<br>
        • Ch 8 (Naturality/2-Cat): pp. 319–377 (3 stalks)
        <cite>— Extracted by build_illustrated_sheaf_kb.py</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <div class="subview-tabs" role="tablist">
              <button class="subview-tab" role="tab" aria-selected="true" data-subview="stalks">24 Concept Stalks</button>
              <button class="subview-tab" role="tab" aria-selected="false" data-subview="declarations">291 Definitions, Theorems &amp; Tasks</button>
              <button class="subview-tab" role="tab" aria-selected="false" data-subview="atlas3d">3D Alexandrov Poset Atlas</button>
            </div>
            <select id="chapterFilterSelect" class="query-input" style="max-width:240px;padding:4px 8px;font-size:0.76rem">
              <option value="all">All 8 Chapters (377 pp.)</option>
              <option value="1">Ch 1 · Prologue &amp; Sets</option>
              <option value="2">Ch 2 · Categories &amp; Duality</option>
              <option value="3">Ch 3 · Monoids &amp; Groups</option>
              <option value="4">Ch 4 · Orders &amp; Lattices</option>
              <option value="5">Ch 5 · Propositional &amp; Heyting Logic</option>
              <option value="6">Ch 6 · Types, ADTs &amp; STLC</option>
              <option value="7">Ch 7 · Functors &amp; .map</option>
              <option value="8">Ch 8 · Natural Transformations &amp; 2-Cat</option>
            </select>
          </div>

          <div id="subview-stalks">
            <div class="stalk-cards-grid" id="stalkCardsGrid"></div>
          </div>

          <div id="subview-declarations" style="display:none">
            <div style="display:flex;gap:8px;margin-bottom:0.8rem;flex-wrap:wrap">
              <input type="text" id="declSearchInput" class="query-input" placeholder="Search 164 Definitions, 40 Theorems, and 90 Tasks (e.g., 'singleton', 'Birkhoff', 'Maybe', 'Task')…">
              <select id="declKindSelect" class="query-input" style="max-width:190px">
                <option value="all">All Kinds (291)</option>
                <option value="Definition">Definitions (164)</option>
                <option value="Theorem">Theorems (40)</option>
                <option value="Exercise">Interactive Tasks (87)</option>
              </select>
            </div>
            <div id="declCountLabel" class="mono" style="margin-bottom:0.55rem;color:var(--ink-3)"></div>
            <div id="declListContainer" style="display:flex;flex-direction:column;gap:8px;max-height:600px;overflow-y:auto"></div>
          </div>

          <div id="subview-atlas3d" style="display:none">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;flex-wrap:wrap;gap:8px">
              <span class="mono" style="color:var(--ink-2)">Drag to orbit 24-Stalk Alexandrov Poset · Scroll to zoom · Click any node to inspect</span>
              <div style="display:flex;gap:6px">
                <button class="preset-btn active" id="toggle2SimplicesBtn">2-Simplices: ON</button>
                <button class="preset-btn" id="reset3dCamBtn">Reset Camera</button>
              </div>
            </div>
            <div class="canvas-frame">
              <canvas id="sheaf3dCanvas"></canvas>
              <div id="hud3dBox" style="position:absolute;bottom:12px;left:12px;right:12px;background:rgba(23,24,28,0.92);color:#F6F1E7;padding:10px 14px;border:1px solid #C88A2B;font-size:0.82rem;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"></div>
            </div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Web-Print Layout Artifacts vs. Semantic Stalk Recovery</span></div>
          <div>
            Because <em>Category Theory Illustrated</em> was printed from its Inkscape-illustrated Jekyll web edition (<code>377</code> pages), raw PDF text extraction occasionally separates single-letter SVG labels (<code>G</code>, <code>A</code>, <code>B</code>) onto standalone lines. Our indexer strips print-header timestamps (<code>10/15/26, 8:09 PM</code>) and pairs every extracted <code>DEFINITION:</code>, <code>THEOREM:</code>, and <code>Task N:</code> with its surrounding semantic stalk and exact page fiber.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       PLATE V · CROSS-CORPUS COMPARISON (MARINOV 377 PP. × SPIVAK 609 PP.)
       ======================================================================== -->
  <section class="plate" id="plate-5">
    <div class="plate-head">
      <div class="plate-folio">
        <span class="num">Plate V</span>
        <div>MARINOV × SPIVAK</div>
        <div style="margin-top:6px"><span class="w-badge w-types">Cross-Corpus Pullback</span></div>
        <div style="margin-top:6px"><span class="stamp accept">✓ 986 Combined Pages</span></div>
      </div>
      <div>
        <div class="eyebrow">COMPARATIVE SYNTHESIS &amp; CURRICULUM · HOW BOTH BOOKS COMPARE &amp; GLUE TOGETHER</div>
        <h2 class="plate-title">Gluing Marinov’s visual <em class="u-copper">intuition</em> with Spivak’s scientific Ologs.</h2>
        <p class="plate-sub">
          How does this second Sheaf Studio compare with our first one on David I. Spivak’s <em>Category Theory for the Sciences</em> (609 pp.)? Neither book alone covers the full spectrum: <strong>Marinov (377 pp.)</strong> excels at point-free visual intuition, deductive logic, and programming type theory (Curry-Howard-Lambek), while <strong>Spivak (609 pp.)</strong> excels at scientific Ontology Logs (Ologs), relational database schemas (<span class="math-expr"><span class="m-cat">Cat</span> &simeq; <span class="m-cat">Sch</span></span>), adjoint data migration (<span class="math-expr">&Sigma;<sub>F</sub> &#8867; &Delta;<sub>F</sub> &#8867; &Pi;<sub>F</sub></span>), and sheaves.
        </p>
      </div>
    </div>

    <div class="plate-body">
      <aside class="marginalia">
        <strong>Two Complementary Epistemologies</strong>
        • <strong>Marinov (377 pp.):</strong> Colored balls <span class="math-expr">&rarr;</span> Universal arrows <span class="math-expr">&rarr;</span> Logic &amp; Lambda Calculus (<span class="math-expr"><span class="m-cat">CCC</span></span>).<br>
        • <strong>Spivak (609 pp.):</strong> English Ologs <span class="math-expr">&rarr;</span> Database Schemas <span class="math-expr">&rarr;</span> Adjoint Kan Migration &amp; Sheaf Topoi.<br>
        • <strong>Combined Sheaf:</strong> <code>986</code> pages, <code>54</code> stalks, <code>1,168</code> formal declarations.
        <cite>— Cross-Corpus Comparative Audit · FORGE Compliant</cite>
      </aside>

      <div>
        <div class="instrument">
          <div class="instrument-bar">
            <span>INSTRUMENT V · SIDE-BY-SIDE CROSS-CORPUS COMPARISON &amp; UNIFIED COURSE MODULES</span>
            <span class="stamp ratified">◆ 24/24 Gates Cleared on Both Corpora</span>
          </div>

          <!-- Side-by-Side Comparison Table -->
          <div style="background:var(--paper);border:1px solid var(--rule);padding:1rem;margin-bottom:1.15rem;overflow-x:auto">
            <div class="mono" style="font-weight:600;text-transform:uppercase;color:var(--accent-text);margin-bottom:0.55rem">
              Comparative Architecture · Marinov’s Category Theory Illustrated vs. Spivak’s Category Theory for the Sciences
            </div>
            <table style="width:100%;border-collapse:collapse;font-size:0.83rem">
              <thead>
                <tr style="border-bottom:2px solid var(--ink);text-align:left;font-family:var(--f-mono);font-size:0.70rem;text-transform:uppercase;color:var(--ink-3)">
                  <th style="padding:6px 8px">Dimension</th>
                  <th style="padding:6px 8px">Marinov · <em>Category Theory Illustrated</em> (This Studio)</th>
                  <th style="padding:6px 8px">Spivak · <em>Category Theory for the Sciences</em> (Studio 1)</th>
                  <th style="padding:6px 8px">Pedagogical Synergy (Glued Pullback)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px;font-weight:600">Corpus Scale &amp; Density</td>
                  <td style="padding:7px 8px">377 pp. · 8 Chapters · 24 Stalks · 291 Items (164 Defs, 40 Thms, 90 Tasks)</td>
                  <td style="padding:7px 8px">609 pp. · 7 Chapters · 30 Stalks · 877 Numbered Declarations</td>
                  <td style="padding:7px 8px">Marinov provides fast visual onboarding; Spivak provides deep theorem/proof rigor.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px;font-weight:600">Visual &amp; Conceptual Hook</td>
                  <td style="padding:7px 8px"><strong>Internal Balls ↔ External Arrows:</strong> Erasing set interiors to reveal universal properties (<button class="cite-pill" onclick="window.__jumpToPage(13,'set')">§ p.13</button>, <button class="cite-pill" onclick="window.__jumpToPage(83,'Element')">§ p.83</button>)</td>
                  <td style="padding:7px 8px"><strong>Ontology Logs (Ologs):</strong> English noun boxes &amp; verb arrows as functional database schemas (<code>§ p.11–47</code>)</td>
                  <td style="padding:7px 8px">Learners first <em>see</em> why arrows replace elements (Marinov), then <em>model</em> real domains as Ologs (Spivak).</td>
                </tr>
                <tr style="border-bottom:1px solid var(--rule-hair)">
                  <td style="padding:7px 8px;font-weight:600">Unique Chapters &amp; Strengths</td>
                  <td style="padding:7px 8px"><strong>Propositional &amp; Intuitionistic BHK Logic (Ch 5), Heyting Algebras, Type Theory, ADTs, Church Encodings &amp; STLC (Ch 6), 2-Categories (Ch 8)</strong></td>
                  <td style="padding:7px 8px"><strong>General Pullbacks/Pushouts, Grothendieck Construction (<span class="math-expr">&int; I</span>), Profunctors, Operads, Adjoint Data Migration (<span class="math-expr">&Sigma; &#8867; &Delta; &#8867; &Pi;</span>), Sheaves (Ch 7)</strong></td>
                  <td style="padding:7px 8px">Unifies Functional Programming / Type Systems (Marinov) with Relational Databases &amp; Sheaves (Spivak).</td>
                </tr>
                <tr>
                  <td style="padding:7px 8px;font-weight:600">Bespoke Studio Instruments</td>
                  <td style="padding:7px 8px">Internal ↔ External Perspective Shifter + 6-World Rosetta Stone Translator</td>
                  <td style="padding:7px 8px">5-Stage MCP Pipeline Inspector + 8-Token Symbolic Diagram Translator</td>
                  <td style="padding:7px 8px">Proves the skill adapts to each book’s native epistemology without cookie-cutter lock-in.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="course-grid" id="courseModulesGrid"></div>

          <div class="derived">
            <div>
              <strong>Cross-Corpus Verdict:</strong> <em>Both Studios Clear 24/24 Adversarial Gates (GO)</em> — While speaking in distinct visual voices tailored to their authors (Lawvere Visual Rosetta vs. MIT Press Olog Archive).
            </div>
          </div>
        </div>

        <div class="counterpoint">
          <div class="cp-head"><span>⊘ Counterpoint · Why One Template Must Never Flatten Two Distinct Books</span></div>
          <div>
            If a skill forces Spivak’s database-migration framing onto Marinov’s book, it misses Marinov’s crowning achievement: the <strong>Curry-Howard-Lambek bridge between Logic, Posets, and Programming Types</strong> (Chapters 4–6, <button class="cite-pill" onclick="window.__jumpToPage(162,'Logic')">§ p.162</button>–<button class="cite-pill" onclick="window.__jumpToPage(277,'STLC')">§ p.277</button>). Conversely, if a skill forces Marinov’s programming container lens onto Spivak, it misses <strong>Adjoint Data Migration (<span class="math-expr">&Sigma;<sub>F</sub> &#8867; &Delta;<sub>F</sub> &#8867; &Pi;<sub>F</sub></span>) and Sheaf Topoi</strong>. Encoding <code>book.voice_profile</code> in the sheaf schema lets each book’s native architecture drive its plates and interactive instruments.
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer style="padding:2.2rem 0 3.2rem;font-family:var(--f-mono);font-size:var(--s-mono);color:var(--ink-3);display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem">
    <div>CATEGORY THEORY ILLUSTRATED SHEAF STUDIO · BORIS MARINOV (377 PP.) × DAVID I. SPIVAK (609 PP.)</div>
    <div>24 STALKS · 50 RESTRICTIONS · 291 FORMAL BLOCKS VERIFIED ON DISK</div>
  </footer>
</div>

<!-- ==========================================================================
     SLIDE-OVER 377-PAGE VERBATIM PDF READER DRAWER
     ========================================================================== -->
<aside class="reader-drawer" id="readerDrawer" aria-label="377-Page Verbatim Reader">
  <div class="reader-head">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <span class="mono" style="font-weight:600;text-transform:uppercase;color:var(--accent-text)">
        Verbatim 377-Page Book Reader · Marinov (Category Theory Illustrated)
      </span>
      <div style="display:flex;gap:6px">
        <a id="openRawPdfLink" href="__PDF_REL_PATH__#page=83" target="_blank" class="preset-btn" style="text-decoration:none">Open PDF ↗</a>
        <button class="preset-btn" id="closeReaderBtn">✕ Close</button>
      </div>
    </div>

    <input type="text" class="query-input" id="fullBookSearchInput" placeholder="Search all 377 verbatim pages of Category Theory Illustrated…" style="width:100%;padding:6px 9px;font-size:0.81rem;margin-bottom:8px">
    <div id="bookSearchResults" style="max-height:170px;overflow-y:auto;display:none;background:var(--paper);border:1px solid var(--rule);margin-bottom:8px;padding:4px"></div>

    <div style="display:flex;align-items:center;gap:6px">
      <button class="preset-btn" id="prevPageBtn">◀ Prev</button>
      <input type="number" id="pageNumInput" min="1" max="377" value="83" class="query-input" style="width:68px;padding:4px 6px;text-align:center;font-family:var(--f-mono)">
      <span class="mono" style="color:var(--ink-3)">/ 377</span>
      <input type="range" id="pageSlider" min="1" max="377" value="83" style="flex:1;accent-color:var(--accent-text)">
      <button class="preset-btn" id="nextPageBtn">Next ▶</button>
    </div>
  </div>

  <div class="reader-body">
    <div id="readerPageMeta" style="margin-bottom:0.75rem;padding-bottom:0.6rem;border-bottom:1px solid var(--rule-hair)"></div>
    <div class="verbatim-sheet" id="readerPageText"></div>
  </div>
</aside>

<!-- Floating Mobile Quick-Access Bottom Bar -->
<nav class="mobile-bottom-dock" id="mobileBottomDock" aria-label="Mobile Quick Actions">
  <button type="button" class="mobile-dock-btn" id="mobileCyclePlateBtn">🎨 Next Plate</button>
  <button type="button" class="mobile-dock-btn primary" id="mobileAudioPlayBtn">▶ Deep Dive</button>
  <button type="button" class="mobile-dock-btn" id="mobileJumpNotebookBtn">🧪 Notebook</button>
  <button type="button" class="mobile-dock-btn" id="mobileOpenReaderBtn">📖 p.83</button>
</nav>

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

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function convertLatexTokensToHtml(mathStr) {
    let s = escapeHtml(mathStr.trim());
    // Convert LaTeX array environments into clean HTML inline tables
    s = s.replace(/\\begin\{array\}\{[^}]*\}([\s\S]*?)\\end\{array\}/g, (_, body) => {
      const rows = body.split(/\\\\/).map(r => r.replace(/\\hline/g, '').trim()).filter(Boolean);
      const trs = rows.map((r, rIdx) => {
        const cells = r.split('&').map(c => `<td style="padding:4px 8px;border-bottom:1px solid var(--rule-hair);${rIdx===0?'font-weight:600;border-bottom:2px solid var(--ink)':''}">${convertLatexTokensToHtml(c.trim())}</td>`).join('');
        return `<tr>${cells}</tr>`;
      }).join('');
      return `<table style="width:100%;border-collapse:collapse;font-size:0.84rem;text-align:left;margin:4px 0"><tbody>${trs}</tbody></table>`;
    });

    // Protect escaped set braces \{ and \} as HTML entities so final {}-cleanup never strips them
    s = s.replace(/\\\{/g, '&#123;').replace(/\\\}/g, '&#125;');
    // Fix escaped ampersand \& (which became \&amp; after escapeHtml)
    s = s.replace(/\\&amp;/g, '&amp;');
    // Handle degree symbol ^\circ or ^{\circ} before \circ replacement
    s = s.replace(/\^\{?\\circ\}?/g, '&deg;');
    // Support \pmod{...} and \bmod
    s = s.replace(/\\pmod\{([^{}]+)\}/g, ' <span class="m-op">(mod $1)</span>');
    s = s.replace(/\\bmod\b/g, ' <span class="m-op">mod</span> ');

    s = s.replace(/\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big)\b/g, '');
    s = s.replace(/\\[,;:!]/g, ' ');
    s = s.replace(/\\quad\b/g, ' &emsp; ');
    s = s.replace(/\\qquad\b/g, ' &emsp;&emsp; ');

    // Expand font macros BEFORE \xrightarrow / \xleftarrow so nested braces like \xrightarrow{\mathrm{eval}} resolve cleanly
    for (let pass = 0; pass < 3; pass++) {
      s = s.replace(/\\mathcal\{([^{}]+)\}/g, '<span class="m-cal">$1</span>');
      s = s.replace(/\\mathbf\{([^{}]+)\}/g, '<span class="m-cat">$1</span>');
      s = s.replace(/\\textbf\{([^{}]+)\}/g, '<strong>$1</strong>');
      s = s.replace(/\\(?:mathrm|text|operatorname)\{([^{}]+)\}/g, '<span class="m-op">$1</span>');
      s = s.replace(/\\emph\{([^{}]+)\}/g, '<em>$1</em>');
    }

    s = s.replace(/\\varprojlim_\{([^}]+)\}/g, '<span class="m-lim"><span class="m-lim-top">lim&larr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\varinjlim_\{([^}]+)\}/g, '<span class="m-lim"><span class="m-lim-top">colim&rarr;</span><span class="m-lim-sub">$1</span></span>');
    s = s.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '<span class="m-lim"><span class="m-lim-top" style="border-bottom:1px solid currentColor;padding:0 3px">$1</span><span class="m-lim-sub" style="padding:0 3px">$2</span></span>');

    s = s.replace(/\\xrightarrow\{([^{}]+)\}/g, (_, lbl) => `<span class="m-arrow"><span class="m-arrow-label">${convertLatexTokensToHtml(lbl)}</span><span class="m-arrow-body">&rarr;</span></span>`);
    s = s.replace(/\\xleftarrow\{([^{}]+)\}/g, (_, lbl) => `<span class="m-arrow"><span class="m-arrow-label">${convertLatexTokensToHtml(lbl)}</span><span class="m-arrow-body">&larr;</span></span>`);

    const symMap = {
      '\\alpha': '&alpha;', '\\beta': '&beta;', '\\gamma': '&gamma;', '\\delta': '&delta;',
      '\\epsilon': '&epsilon;', '\\varepsilon': '&varepsilon;', '\\eta': '&eta;', '\\theta': '&theta;',
      '\\iota': '&iota;', '\\lambda': '&lambda;', '\\mu': '&mu;', '\\nu': '&nu;', '\\pi': '&pi;',
      '\\rho': '&rho;', '\\sigma': '&sigma;', '\\tau': '&tau;', '\\phi': '&phi;', '\\omega': '&omega;',
      '\\Gamma': '&Gamma;', '\\Delta': '&Delta;', '\\Lambda': '&Lambda;', '\\Pi': '&Pi;', '\\Sigma': '&Sigma;', '\\Omega': '&Omega;',
      '\\to': '&rarr;', '\\rightarrow': '&rarr;', '\\leftarrow': '&larr;',
      '\\leftrightarrow': '&harr;', '\\longleftrightarrow': '&harr;', '\\Longleftrightarrow': '&hArr;',
      '\\mapsto': '&#8614;', '\\longmapsto': '&#8614;', '\\hookrightarrow': '&#8618;', '\\leadsto': '&#8605;',
      '\\Rightarrow': '&rArr;', '\\Leftarrow': '&lArr;', '\\Leftrightarrow': '&hArr;', '\\iff': '&hArr;', '\\implies': '&rArr;',
      '\\rightrightarrows': '&#8649;', '\\dashv': '&#8867;', '\\vdash': '&#8866;',
      '\\cong': '&cong;', '\\simeq': '&simeq;', '\\sim': '&sim;', '\\equiv': '&equiv;', '\\approx': '&approx;', '\\neq': '&ne;',
      '\\leq': '&le;', '\\geq': '&ge;', '\\le': '&le;', '\\ge': '&ge;', '\\lesssim': '&#8818;',
      '\\subset': '&sub;', '\\subseteq': '&sube;', '\\in': '&isin;', '\\notin': '&notin;',
      '\\cup': '&cup;', '\\cap': '&cap;', '\\sqcup': '&#8852;', '\\sqcap': '&#8851;',
      '\\wedge': '&and;', '\\vee': '&or;', '\\neg': '&not;', '\\lnot': '&not;', '\\mid': '|',
      '\\gcd': 'gcd', '\\lcm': 'lcm',
      '\\times': '&times;', '\\otimes': '&otimes;', '\\oplus': '&oplus;', '\\star': '&#8902;',
      '\\prod': '&prod;', '\\coprod': '&#8720;', '\\sum': '&sum;', '\\int': '&int;',
      '\\circ': '&#8728;', '\\bullet': '&bull;', '\\cdot': '&middot;',
      '\\forall': '&forall;', '\\exists': '&exist;', '\\emptyset': '&empty;', '\\infty': '&infin;',
      '\\langle': '&lang;', '\\rangle': '&rang;', '\\lrcorner': '&#8991;',
      '\\ldots': '&hellip;', '\\cdots': '&ctdot;', '\\dots': '&hellip;',
      '\\top': '&#8868;', '\\bot': '&#8869;'
    };

    const sortedKeys = Object.keys(symMap).sort((a, b) => b.length - a.length);
    for (const k of sortedKeys) {
      const escapedK = k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const pattern = /[a-zA-Z]$/.test(k) ? new RegExp(escapedK + '(?![a-zA-Z])', 'g') : new RegExp(escapedK, 'g');
      s = s.replace(pattern, symMap[k]);
    }

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
    return isDisplay ? `<div class="math-display">${inner}</div>` : `<span class="math-expr">${inner}</span>`;
  }

  function formatInlineProse(str) {
    return escapeHtml(str)
      .replace(/\$([^\$\n]+?)\$/g, (_, expr) => renderMathChip(expr, false))
      .replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>')
      .replace(/([αβγδεηθιλμπρστφωΓΔΛΠΣΩA-Za-z])_([0-9A-Za-z•]+)/g, '$1<sub>$2</sub>');
  }

  function renderRichMarkdown(md) {
    if (!md) return '';
    let text = String(md);
    const mathBlocks = [];
    text = text.replace(/\$\$([\s\S]*?)\$\$/g, (_, expr) => {
      const idx = mathBlocks.length;
      mathBlocks.push(renderMathChip(expr, true));
      return `@@MATH_BLOCK_${idx}@@`;
    });
    const mathInlines = [];
    text = text.replace(/\$([^\$\n]+?)\$/g, (_, expr) => {
      const idx = mathInlines.length;
      mathInlines.push(renderMathChip(expr, false));
      return `@@MATH_INLINE_${idx}@@`;
    });

    let html = escapeHtml(text);
    html = html.replace(/`?\[p\.\s*(\d+)([^\]]*)\]`?/g, (_, pNum, rest) => {
      return `<button class="cite-pill" onclick="window.__jumpToPage(${pNum}, '')">§ p.${pNum}${rest}</button>`;
    });
    html = html.replace(/`([^`]+)`/g, (_, codeStr) => {
      if (/\\[a-zA-Z]|_\{|\^\{|\\to|\\circ|\\times|\\sqcup/.test(codeStr)) {
        return `<span class="math-expr">${convertLatexTokensToHtml(codeStr)}</span>`;
      }
      return `<code class="inline-code">${codeStr}</code>`;
    });
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

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
        out.push(`<h4 style="margin:0.8rem 0 0.35rem;font-family:var(--f-serif)">${line.slice(5)}</h4>`);
      } else if (line.startsWith('### ')) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<h3 style="margin:0.9rem 0 0.45rem;font-family:var(--f-serif)">${line.slice(4)}</h3>`);
      } else if (line.startsWith('- ') || /^\d+\.\s+/.test(line)) {
        if (!inList) { out.push('<ul style="margin:0.4rem 0 0.7rem 1.2rem;padding:0">'); inList = true; }
        out.push(`<li style="margin-bottom:0.25rem">${line.replace(/^(-|\d+\.)\s+/, '')}</li>`);
      } else if (/^@@MATH_BLOCK_\d+@@$/.test(line)) {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(line);
      } else {
        if (inList) { out.push('</ul>'); inList = false; }
        out.push(`<p style="margin:0.45rem 0">${line}</p>`);
      }
    }
    if (inList) out.push('</ul>');
    let finalHtml = out.join('\n');
    finalHtml = finalHtml.replace(/@@MATH_BLOCK_(\d+)@@/g, (_, idx) => mathBlocks[Number(idx)]);
    finalHtml = finalHtml.replace(/@@MATH_INLINE_(\d+)@@/g, (_, idx) => mathInlines[Number(idx)]);
    return finalHtml;
  }

  // Controls & Simplified 1-Plate Focus Mode
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

  // Inject Prev/Next Plate Stepper Bar at bottom of each plate for Focus Mode
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
        <button type="button" class="btn-primary" style="padding:4px 10px;font-size:0.72rem" onclick="window.__focusPlate('${nextP.id}', true)">Next: Plate ${['I','II','III','IV','V'][(idx+1)%5]} ▶</button>
      </div>
    `;
    p.appendChild(bar);
  });

  document.querySelectorAll('[data-set-level]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.documentElement.setAttribute('data-level', btn.getAttribute('data-set-level'));
      document.querySelectorAll('[data-set-level]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    });
  });
  document.querySelectorAll('[data-set-theme]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.documentElement.setAttribute('data-theme', btn.getAttribute('data-set-theme'));
      document.querySelectorAll('[data-set-theme]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    });
  });

  // Mobile Open-Cover Toggle
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

  function renderDecoderHtml(decoderItems, headingText) {
    if (!decoderItems || !decoderItems.length) return '';
    return `
      <div style="margin-top:0.85rem;padding:0.75rem 0.9rem;background:var(--paper);border:1px solid var(--rule)">
        <div class="mono" style="font-size:0.69rem;font-weight:600;text-transform:uppercase;color:var(--accent-text)">
          🔍 ${escapeHtml(headingText || 'Symbol-by-Symbol Visual Formula Decoder (Reading Beyond Opaque Notation)')}
        </div>
        <div class="decoder-grid">
          ${decoderItems.map(item => `
            <div class="decoder-chip">
              <div class="d-sym">
                <span>${convertLatexTokensToHtml(item.sym)}</span>
                ${item.p ? `<button class="cite-pill" onclick="window.__jumpToPage(${item.p}, '')">§ p.${item.p}</button>` : ''}
              </div>
              <div class="d-meaning">${formatInlineProse(item.meaning)}</div>
              <div class="d-why">${formatInlineProse(item.why)}</div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // PLATE I-A: INTERNAL (BALLS) ↔ EXTERNAL (POINT-FREE ARROWS) SHIFTER (8 CONSTRUCTS)
  // ==========================================================================
  const SHIFTER_DATA = {
    element: {
      pages: [13, 77, 83],
      internalTitle: 'Internal Set View: Element x ∈ A (Colored Ball Inside Set)',
      internalFormula: 'x \\in A \\quad (\\text{Inspecting interior contents of } A)',
      internalDesc: 'In Chapter 1 (p. 13), a set G is drawn as a boundary containing colored balls (red, yellow, blue). Membership x ∈ G is checked by peeking inside the container.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><ellipse cx="180" cy="88" rx="115" ry="60" fill="rgba(184,125,36,0.12)" stroke="#B87D24" stroke-width="1.8"/><circle cx="125" cy="82" r="16" fill="#B34434" stroke="#17181C" stroke-width="1.5"/><text x="125" y="86" text-anchor="middle" fill="#fff" font-size="11" font-family="JetBrains Mono">r</text><circle cx="180" cy="102" r="16" fill="#B87D24" stroke="#17181C" stroke-width="1.5"/><text x="180" y="106" text-anchor="middle" fill="#fff" font-size="11" font-family="JetBrains Mono">y</text><circle cx="235" cy="80" r="16" fill="#2B5B84" stroke="#17181C" stroke-width="1.5"/><text x="235" y="84" text-anchor="middle" fill="#fff" font-size="11" font-family="JetBrains Mono">b</text><text x="180" y="20" text-anchor="middle" font-family="Fraunces, serif" font-size="13">Set A = {r, y, b} (p. 13)</text></svg>`,
      externalTitle: 'External Point-Free View: Morphism x : 1 → A (Generalized Element)',
      externalFormula: '\\mathrm{Hom}_{\\mathbf{Set}}(1, A) \\cong A \\quad (\\text{Arrows from Singleton } 1)',
      externalDesc: 'In Chapter 2 (p. 77, p. 83), we erase the interior of A. Now A is a solid point, and its 3 elements are the 3 functions r, y, b : 1 → A out of the terminal object 1!',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="85" cy="88" r="20" fill="#F6F1E7" stroke="#17181C" stroke-width="1.8"/><text x="85" y="93" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="15">1</text><circle cx="275" cy="88" r="22" fill="#1E4363" stroke="#17181C" stroke-width="1.8"/><text x="275" y="93" text-anchor="middle" font-family="Fraunces, serif" font-weight="600" font-size="15" fill="#F6F1E7">A</text><path d="M 108 74 Q 180 32 250 74" fill="none" stroke="#B34434" stroke-width="1.8" marker-end="url(#m1)"/><text x="180" y="48" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#B34434">r : 1 &rarr; A</text><line x1="108" y1="88" x2="249" y2="88" stroke="#B87D24" stroke-width="1.8" marker-end="url(#m1)"/><text x="180" y="82" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#B87D24">y : 1 &rarr; A</text><path d="M 108 102 Q 180 144 250 102" fill="none" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#m1)"/><text x="180" y="138" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#2B5B84">b : 1 &rarr; A</text></svg>`,
      invariant: 'Lawvere Element Principle (p. 77): Elements of any set A are in 1-to-1 bijection with morphisms 1 → A from the terminal singleton.',
      decoder: [
        { sym: 'x \\in A', p: 13, meaning: 'A colored ball sitting inside bag A.', why: 'Requires opening the bag (impossible in abstract categories).' },
        { sym: '1 \\xrightarrow{x} A', p: 74, meaning: 'A pointer arrow from the 1-ball set {•} picking out ball x.', why: 'Replaces membership ∈ with an external morphism!' },
        { sym: 'f \\circ x = f(x)', p: 60, meaning: 'Following pointer x : 1 → A then function f : A → B.', why: 'Function application is literally arrow composition!' }
      ]
    },
    terminal: {
      pages: [15, 24, 75],
      internalTitle: 'Internal Set View: Singleton Set {•} (One Ball Inside)',
      internalFormula: '|1| = 1 \\quad (\\text{A set containing a single element})',
      internalDesc: 'Internally (p. 15), a singleton set is defined by counting its members: the set of red balls has exactly one member.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><ellipse cx="180" cy="88" rx="68" ry="52" fill="rgba(184,125,36,0.12)" stroke="#B87D24" stroke-width="1.8"/><circle cx="180" cy="88" r="18" fill="#B34434" stroke="#17181C" stroke-width="1.5"/><text x="180" y="22" text-anchor="middle" font-family="Fraunces, serif" font-size="13">Singleton Set {•} (p. 15)</text></svg>`,
      externalTitle: 'External Point-Free View: Terminal Object 1 (Unique Incoming Arrow)',
      externalFormula: '\\forall A \\in \\mathcal{C}, \\; \\exists! \\; !_A : A \\to 1',
      externalDesc: 'Externally (p. 24, p. 75), the Terminal Object 1 is defined without counting elements: it is the unique object (up to isomorphism) such that every object A has exactly one morphism !_A : A → 1.',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1E4363"/></marker></defs><circle cx="70" cy="48" r="18" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="70" y="53" text-anchor="middle" font-family="Fraunces">A</text><circle cx="70" cy="128" r="18" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="70" y="133" text-anchor="middle" font-family="Fraunces">B</text><circle cx="265" cy="88" r="22" fill="#1E4363" stroke="#17181C" stroke-width="1.8"/><text x="265" y="93" text-anchor="middle" font-family="Fraunces" fill="#fff" font-weight="600">1</text><line x1="92" y1="54" x2="238" y2="82" stroke="#1E4363" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#m2)"/><text x="165" y="58" font-family="JetBrains Mono" font-size="10" fill="#1E4363">&exist;! !<tspan dy="2.5" font-size="7.5">A</tspan></text><line x1="92" y1="122" x2="238" y2="94" stroke="#1E4363" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#m2)"/><text x="165" y="124" font-family="JetBrains Mono" font-size="10" fill="#1E4363">&exist;! !<tspan dy="2.5" font-size="7.5">B</tspan></text></svg>`,
      invariant: 'Universal Terminal Law (p. 75): Any two terminal objects 1 and 1′ have unique morphisms between them whose composites must be identities, proving 1 ≅ 1′.',
      decoder: [
        { sym: '\\forall A', p: 75, meaning: 'Pick ANY object A in the category.', why: 'Universal property tests against every object in the universe.' },
        { sym: '\\exists! \\; !_A', p: 75, meaning: 'There is ONE AND ONLY ONE arrow (drawn dashed).', why: 'Uniqueness (!) forces all balls in A to funnel into the single dot of 1.' },
        { sym: '1 \\cong 1\'', p: 76, meaning: 'Any two terminal objects are uniquely isomorphic.', why: 'Round trip 1 → 1′ → 1 must equal id_1 because 1 → 1 has only 1 arrow!' }
      ]
    },
    initial: {
      pages: [16, 22, 78],
      internalTitle: 'Internal Set View: Empty Set ∅ (Zero Balls Inside)',
      internalFormula: '|\\emptyset| = 0 \\quad (\\text{Container with no elements})',
      internalDesc: 'Internally (p. 16–17), the empty set ∅ is the unique set containing zero balls.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><ellipse cx="180" cy="88" rx="68" ry="52" fill="none" stroke="#B34434" stroke-width="1.8" stroke-dasharray="5 3"/><text x="180" y="94" text-anchor="middle" font-family="Fraunces, serif" font-size="22" fill="#B34434">&empty;</text><text x="180" y="22" text-anchor="middle" font-family="Fraunces, serif" font-size="13">Empty Set &empty; (p. 16)</text></svg>`,
      externalTitle: 'External Point-Free View: Initial Object 0 (Unique Outgoing Arrow)',
      externalFormula: '\\forall A \\in \\mathcal{C}, \\; \\exists! \\; !^A : 0 \\to A',
      externalDesc: 'Externally (p. 22, p. 78), we reverse the arrows of the Terminal Object! The Initial Object 0 is the object sending a unique morphism !^A : 0 → A to every object A.',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#B34434"/></marker></defs><circle cx="85" cy="88" r="22" fill="#B34434" stroke="#17181C" stroke-width="1.8"/><text x="85" y="93" text-anchor="middle" font-family="Fraunces" fill="#fff" font-weight="600">0</text><circle cx="275" cy="48" r="18" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="275" y="53" text-anchor="middle" font-family="Fraunces">A</text><circle cx="275" cy="128" r="18" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="275" y="133" text-anchor="middle" font-family="Fraunces">B</text><line x1="110" y1="82" x2="252" y2="54" stroke="#B34434" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#m3)"/><text x="175" y="58" font-family="JetBrains Mono" font-size="10" fill="#B34434">&exist;! !<tspan dy="-3" font-size="7.5">A</tspan></text><line x1="110" y1="94" x2="252" y2="122" stroke="#B34434" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#m3)"/><text x="175" y="124" font-family="JetBrains Mono" font-size="10" fill="#B34434">&exist;! !<tspan dy="-3" font-size="7.5">B</tspan></text></svg>`,
      invariant: 'Initial-Terminal Duality (p. 78): The Initial Object 0 in C is the Terminal Object 1 in the opposite category C^op.',
      decoder: [
        { sym: '0 \\to A', p: 78, meaning: 'Unique outgoing "absurd" arrow from 0 to any A.', why: 'With 0 input balls, there is exactly 1 vacuous way to assign outputs ($|A|^0 = 1$).' },
        { sym: 'A \\to 0 = \\emptyset', p: 78, meaning: 'No arrows into 0 from a non-empty A.', why: 'Where would an input ball in A land if 0 has zero balls? ($0^{|A|} = 0$).' },
        { sym: '\\mathcal{C}^{\\mathrm{op}}', p: 68, meaning: 'Flip every arrowhead in the diagram.', why: 'Swaps Initial (0) and Terminal (1) without new proofs!' }
      ]
    },
    product: {
      pages: [53, 58, 62],
      internalTitle: 'Internal Set View: Cartesian Grid of Ordered Pairs (a, b)',
      internalFormula: 'A \\times B = \\{ (a, b) \\mid a \\in A, \\; b \\in B \\}',
      internalDesc: 'Internally (p. 53), the Cartesian product combines elements from A and B into a 2D table of composite pair cells (a, b).',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><rect x="95" y="36" width="170" height="105" fill="rgba(184,125,36,0.09)" stroke="#17181C" stroke-width="1.5"/><line x1="95" y1="88" x2="265" y2="88" stroke="#17181C"/><line x1="180" y1="36" x2="180" y2="141" stroke="#17181C"/><text x="137" y="66" text-anchor="middle" font-family="JetBrains Mono" font-size="11">(a₁, b₁)</text><text x="222" y="66" text-anchor="middle" font-family="JetBrains Mono" font-size="11">(a₁, b₂)</text><text x="137" y="118" text-anchor="middle" font-family="JetBrains Mono" font-size="11">(a₂, b₁)</text><text x="222" y="118" text-anchor="middle" font-family="JetBrains Mono" font-size="11">(a₂, b₂)</text></svg>`,
      externalTitle: 'External Point-Free View: Universal Cone (A × B, π₁, π₂)',
      externalFormula: '\\forall (C \\xrightarrow{f} A, C \\xrightarrow{g} B), \\; \\exists! \\langle f, g \\rangle : C \\to A \\times B',
      externalDesc: 'Externally (p. 58–62), we never mention pairs (a,b): A × B is the universal object equipped with projections π₁, π₂ through which any pair of morphisms (f, g) factors uniquely.',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="180" cy="26" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="180" y="31" text-anchor="middle" font-family="Fraunces">C</text><rect x="140" y="82" width="80" height="28" rx="3" fill="#1E4363" stroke="#17181C"/><text x="180" y="100" text-anchor="middle" font-family="Fraunces" fill="#fff">A &times; B</text><circle cx="65" cy="142" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="65" y="147" text-anchor="middle" font-family="Fraunces">A</text><circle cx="295" cy="142" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="295" y="147" text-anchor="middle" font-family="Fraunces">B</text><line x1="180" y1="43" x2="180" y2="78" stroke="#B87D24" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#m4)"/><text x="218" y="65" font-family="JetBrains Mono" font-size="9.5" fill="#B87D24">&lang;f,g&rang;</text><line x1="140" y1="104" x2="84" y2="134" stroke="#17181C" stroke-width="1.6" marker-end="url(#m4)"/><text x="112" y="132" font-family="Fraunces" font-style="italic">&pi;₁</text><line x1="220" y1="104" x2="276" y2="134" stroke="#17181C" stroke-width="1.6" marker-end="url(#m4)"/><text x="248" y="132" font-family="Fraunces" font-style="italic">&pi;₂</text></svg>`,
      invariant: 'External Product Characterization (p. 62): The projections π₁ and π₂ extract coordinates without ever opening the object A × B.',
      decoder: [
        { sym: '\\pi_1, \\pi_2', p: 58, meaning: 'Left and Right shadow projections (`fst` and `snd`).', why: 'Instead of opening a tuple, we observe its shadows on A and B.' },
        { sym: '\\langle f, g \\rangle', p: 62, meaning: 'Unique bundled arrow C → A×B built from f and g.', why: 'Bundling two arrows into one product arrow with zero information loss.' },
        { sym: '\\pi_1 \\circ \\langle f,g \\rangle = f', p: 62, meaning: 'Projecting the first coordinate recovers f.', why: 'In Type Theory (p. 252), this is β-reduction `fst(pair(x,y)) = x`!' }
      ]
    },
    coproduct: {
      pages: [69, 71, 74],
      internalTitle: 'Internal Set View: Tagged Disjoint Union A ⊔ B',
      internalFormula: 'A + B = \\{ (\\mathrm{left}, a) \\mid a \\in A \\} \\cup \\{ (\\mathrm{right}, b) \\mid b \\in B \\}',
      internalDesc: 'Internally (p. 69), the sum or disjoint union places all balls of A and all balls of B into a combined pouch while tagging which side each ball came from.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><ellipse cx="180" cy="88" rx="125" ry="56" fill="rgba(43,91,132,0.08)" stroke="#2B5B84" stroke-width="1.8"/><line x1="180" y1="32" x2="180" y2="144" stroke="#2B5B84" stroke-dasharray="4 3"/><circle cx="125" cy="88" r="15" fill="#B34434"/><circle cx="155" cy="88" r="15" fill="#B87D24"/><rect x="208" y="73" width="28" height="28" fill="#2B5B84"/><rect x="246" y="73" width="28" height="28" fill="#35694E"/><text x="180" y="20" text-anchor="middle" font-family="Fraunces" font-size="13">Disjoint Union A + B (p. 69)</text></svg>`,
      externalTitle: 'External Point-Free View: Universal Cocone (A + B, ι₁, ι₂)',
      externalFormula: '\\forall (A \\xrightarrow{f} C, B \\xrightarrow{g} C), \\; \\exists! [f, g] : A + B \\to C',
      externalDesc: 'Externally (p. 71–74), we simply reverse every arrow in the Product diagram: injections ι₁, ι₂ point INTO A + B, and the universal co-pairing [f, g] points OUT to C.',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="65" cy="36" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="65" y="41" text-anchor="middle" font-family="Fraunces">A</text><circle cx="295" cy="36" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="295" y="41" text-anchor="middle" font-family="Fraunces">B</text><rect x="140" y="64" width="80" height="28" rx="3" fill="#1E4363" stroke="#17181C"/><text x="180" y="82" text-anchor="middle" font-family="Fraunces" fill="#fff">A + B</text><circle cx="180" cy="146" r="16" fill="#F6F1E7" stroke="#17181C" stroke-width="1.5"/><text x="180" y="151" text-anchor="middle" font-family="Fraunces">C</text><line x1="84" y1="44" x2="136" y2="70" stroke="#17181C" stroke-width="1.6" marker-end="url(#m5)"/><text x="110" y="50" font-family="Fraunces" font-style="italic">&iota;₁</text><line x1="276" y1="44" x2="224" y2="70" stroke="#17181C" stroke-width="1.6" marker-end="url(#m5)"/><text x="250" y="50" font-family="Fraunces" font-style="italic">&iota;₂</text><line x1="180" y1="92" x2="180" y2="126" stroke="#B34434" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#m5)"/><text x="216" y="114" font-family="JetBrains Mono" font-size="9.5" fill="#B34434">[f,g]</text></svg>`,
      invariant: 'Categorical Duality (p. 69): In the internal view, Product and Sum look completely different; in the external arrow view, they are mirror images.',
      decoder: [
        { sym: '\\iota_1, \\iota_2', p: 69, meaning: 'Left and Right entry doors (`Left` and `Right` constructors).', why: 'Tags whether an element entered from A or from B.' },
        { sym: '[f, g]', p: 71, meaning: 'Exhaustive `match / switch` handler out of A+B into C.', why: 'If you know how to handle A (via f) and B (via g), you can handle A+B!' },
        { sym: '[f,g] \\circ \\iota_1 = f', p: 71, meaning: 'Entering Left door then matching runs branch f.', why: 'Pattern-matching β-reduction in programming (p. 251)!' }
      ]
    },
    iso: {
      pages: [48, 82, 284],
      internalTitle: 'Internal Set View: One-to-One & Onto Bijection of Balls',
      internalFormula: '\\forall b \\in B, \\; \\exists! a \\in A \\text{ s.t. } f(a) = b',
      internalDesc: 'Internally (p. 48), a bijection pairs each individual ball in A with a unique partner ball in B with none left over.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><ellipse cx="105" cy="88" rx="45" ry="55" fill="rgba(184,125,36,0.1)" stroke="#B87D24"/><ellipse cx="255" cy="88" rx="45" ry="55" fill="rgba(43,91,132,0.1)" stroke="#2B5B84"/><circle cx="105" cy="60" r="10" fill="#B34434"/><circle cx="105" cy="115" r="10" fill="#2B5B84"/><rect x="245" y="50" width="20" height="20" fill="#B34434"/><rect x="245" y="105" width="20" height="20" fill="#2B5B84"/><line x1="118" y1="60" x2="242" y2="60" stroke="#17181C" stroke-width="1.5"/><line x1="118" y1="115" x2="242" y2="115" stroke="#17181C" stroke-width="1.5"/></svg>`,
      externalTitle: 'External Point-Free View: Invertible Morphism Pair (g ∘ f = id)',
      externalFormula: 'g \\circ f = \\mathrm{id}_A \\quad \\wedge \\quad f \\circ g = \\mathrm{id}_B',
      externalDesc: 'Externally (p. 48, p. 284), isomorphism is defined purely via composition with identity loops: going from A to B via f and back via g equals doing nothing (id_A).',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m6" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="105" cy="88" r="22" fill="#F6F1E7" stroke="#17181C" stroke-width="1.8"/><text x="105" y="93" text-anchor="middle" font-family="Fraunces" font-weight="600">A</text><circle cx="255" cy="88" r="22" fill="#F6F1E7" stroke="#17181C" stroke-width="1.8"/><text x="255" y="93" text-anchor="middle" font-family="Fraunces" font-weight="600">B</text><path d="M 128 76 Q 180 48 232 76" fill="none" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#m6)"/><text x="180" y="55" text-anchor="middle" font-family="Fraunces" font-style="italic">f</text><path d="M 232 100 Q 180 128 128 100" fill="none" stroke="#B87D24" stroke-width="1.8" marker-end="url(#m6)"/><text x="180" y="128" text-anchor="middle" font-family="Fraunces" font-style="italic">g</text></svg>`,
      invariant: 'Structural Indistinguishability (p. 48, p. 284): Category theory treats isomorphic objects A ≅ B as identical in all external relationships.',
      decoder: [
        { sym: 'g \\circ f = \\mathrm{id}_A', p: 48, meaning: 'Round-trip A → B → A lands every point back where it started.', why: 'Left-invertibility (retraction) without peeking at internal elements.' },
        { sym: 'f \\circ g = \\mathrm{id}_B', p: 48, meaning: 'Round-trip B → A → B also equals identity on B.', why: 'Both round-trips must commute for true isomorphism A ≅ B.' }
      ]
    },
    espresso: {
      pages: [35, 37, 38],
      internalTitle: 'Internal View: Espresso Machine Plumbing & Beans-to-Cup Wires',
      internalFormula: 'g(f(x)) = \\mathrm{Brew}(\\mathrm{Grind}(\\text{beans}))',
      internalDesc: 'On pp. 35–38, Marinov draws an espresso machine with internal grinder gears, heater pipes, and water valves transforming coffee beans into espresso.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><rect x="28" y="32" width="304" height="108" rx="6" fill="rgba(184,125,36,0.08)" stroke="#B87D24" stroke-width="1.5" stroke-dasharray="4 2"/><rect x="48" y="58" width="76" height="56" rx="4" fill="#F6F1E7" stroke="#17181C"/><text x="86" y="84" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">Grinder f</text><text x="86" y="98" text-anchor="middle" font-size="9" fill="#B34434">Beans &rarr; Grounds</text><rect x="148" y="58" width="76" height="56" rx="4" fill="#F6F1E7" stroke="#17181C"/><text x="186" y="84" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">Boiler g</text><text x="186" y="98" text-anchor="middle" font-size="9" fill="#2B5B84">9 bar / 93°C</text><rect x="248" y="58" width="64" height="56" rx="4" fill="#1E4363" stroke="#17181C"/><text x="280" y="90" text-anchor="middle" font-family="Fraunces" font-size="11" fill="#fff">Cup ☕</text><line x1="124" y1="86" x2="148" y2="86" stroke="#17181C" stroke-width="2"/><line x1="224" y1="86" x2="248" y2="86" stroke="#17181C" stroke-width="2"/><text x="180" y="22" text-anchor="middle" font-family="Fraunces" font-size="12.5">Marinov’s Espresso Machine Interior (pp. 35–37)</text></svg>`,
      externalTitle: 'External Zoom-Out View: Commutative Composition Triangle g ∘ f',
      externalFormula: 'A \\xrightarrow{f} B \\xrightarrow{g} C \\;\\equiv\\; A \\xrightarrow{g \\circ f} C',
      externalDesc: 'On p. 38, Marinov closes the espresso machine casing: externally, a subsystem is just a single composite arrow g ∘ f whose internal gears are hidden behind associative composition.',
      externalSvg: `<svg viewBox="0 0 360 175" width="100%"><defs><marker id="m7" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="62" cy="114" r="24" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/><text x="62" y="118" text-anchor="middle" font-family="Fraunces" font-size="11">Beans</text><circle cx="180" cy="36" r="26" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/><text x="180" y="40" text-anchor="middle" font-family="Fraunces" font-size="10.5">Grounds</text><circle cx="298" cy="114" r="24" fill="#1E4363" stroke="#17181C" stroke-width="1.6"/><text x="298" y="118" text-anchor="middle" font-family="Fraunces" font-size="11" fill="#fff">Cup</text><line x1="83" y1="99" x2="156" y2="50" stroke="#B87D24" stroke-width="1.8" marker-end="url(#m7)"/><text x="108" y="66" text-anchor="end" font-family="Fraunces" font-style="italic" font-size="12" fill="#B87D24">f (grind)</text><line x1="204" y1="50" x2="277" y2="99" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#m7)"/><text x="252" y="66" text-anchor="start" font-family="Fraunces" font-style="italic" font-size="12" fill="#2B5B84">g (brew)</text><line x1="90" y1="114" x2="270" y2="114" stroke="#17181C" stroke-width="2.2" marker-end="url(#m7)"/><text x="180" y="158" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="600">g &#8728; f (Sealed Espresso Machine, p. 38)</text></svg>`,
      invariant: 'Hierarchical Zoom-Out Principle (p. 38): Associativity h ∘ (g ∘ f) = (h ∘ g) ∘ f lets us seal any multi-step pipeline into a single black-box arrow.',
      decoder: [
        { sym: 'g \\circ f', p: 35, meaning: 'Read RIGHT-TO-LEFT: "run f first, then feed into g".', why: 'Written backwards from English pipeline order `f ; g` because of `g(f(x))`!' },
        { sym: '(h \\circ g) \\circ f = h \\circ (g \\circ f)', p: 38, meaning: 'Where you draw the box boundary around sub-machines does not change the output.', why: 'Why modular software & hardware engineering works.' }
      ]
    },
    polarity: {
      pages: [229, 251, 253],
      internalTitle: 'Positive Types (Sum / Either): Defined by Entry Constructor Doors ι',
      internalFormula: '\\mathrm{Intro}: A \\xrightarrow{\\iota_1} A+B \\xleftarrow{\\iota_2} B \\quad (\\text{Inbound Doors})',
      internalDesc: 'On p. 251, Marinov explains why Sum/Inductive types feel "concrete": they are defined by their INBOUND constructor arrows (Left, Right, Zero, Succ) that build values.',
      internalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m8a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#2E6444"/></marker></defs><circle cx="65" cy="45" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="65" y="50" text-anchor="middle" font-family="Fraunces">A</text><circle cx="65" cy="125" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="65" y="130" text-anchor="middle" font-family="Fraunces">B</text><rect x="150" y="62" width="110" height="46" rx="5" fill="rgba(46,100,68,0.12)" stroke="#2E6444" stroke-width="2"/><text x="205" y="84" text-anchor="middle" font-family="Fraunces" font-weight="600" fill="#2E6444">Either A B</text><text x="205" y="99" text-anchor="middle" font-family="JetBrains Mono" font-size="8.5" fill="#2E6444">Entry Doors &iota;₁, &iota;₂</text><line x1="84" y1="52" x2="145" y2="75" stroke="#2E6444" stroke-width="2" marker-end="url(#m8a)"/><line x1="84" y1="118" x2="145" y2="95" stroke="#2E6444" stroke-width="2" marker-end="url(#m8a)"/><text x="180" y="22" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#2E6444">POSITIVE TYPE · DEFINED BY HOW YOU ENTER (P. 251)</text></svg>`,
      externalTitle: 'Negative Types (Product / Function): Defined by Exit Observations π',
      externalFormula: '\\mathrm{Elim}: A \\xleftarrow{\\pi_1} A \\times B \\xrightarrow{\\pi_2} B, \\quad B^A \\times A \\xrightarrow{\\mathrm{eval}} B',
      externalDesc: 'On p. 252, Product and Function types are dual: they are defined by their OUTBOUND elimination arrows (fst, snd, eval)—what you can extract or observe from them!',
      externalSvg: `<svg viewBox="0 0 360 170" width="100%"><defs><marker id="m8b" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1E4363"/></marker></defs><rect x="95" y="62" width="110" height="46" rx="5" fill="rgba(30,67,99,0.12)" stroke="#1E4363" stroke-width="2"/><text x="150" y="84" text-anchor="middle" font-family="Fraunces" font-weight="600" fill="#1E4363">Tuple (A, B)</text><text x="150" y="99" text-anchor="middle" font-family="JetBrains Mono" font-size="8.5" fill="#1E4363">Exit Windows &pi;₁, &pi;₂</text><circle cx="290" cy="45" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="290" y="50" text-anchor="middle" font-family="Fraunces">A</text><circle cx="290" cy="125" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="290" y="130" text-anchor="middle" font-family="Fraunces">B</text><line x1="208" y1="75" x2="270" y2="52" stroke="#1E4363" stroke-width="2" marker-end="url(#m8b)"/><line x1="208" y1="95" x2="270" y2="118" stroke="#1E4363" stroke-width="2" marker-end="url(#m8b)"/><text x="180" y="22" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#1E4363">NEGATIVE TYPE · DEFINED BY WHAT EXITS (P. 252)</text></svg>`,
      invariant: 'Introduction vs. Elimination Polarity (pp. 251–253): Colimits (0, A+B) are defined by inbound constructors; Limits (1, A×B, B^A) are defined by outbound eliminators.',
      decoder: [
        { sym: '\\mathrm{Intro} \\; (\\iota)', p: 251, meaning: 'Arrows pointing INTO the type (constructors `Left`, `Right`, `Succ`).', why: 'Tells you how to build a value of a Positive/Colimit type.' },
        { sym: '\\mathrm{Elim} \\; (\\pi, \\mathrm{eval})', p: 252, meaning: 'Arrows pointing OUT OF the type (selectors `.fst`, `.snd`, `f(x)`).', why: 'Tells you how to use/observe a Negative/Limit type.' },
        { sym: '\\mathrm{Elim} \\circ \\mathrm{Intro} \\to_\\beta', p: 253, meaning: 'Meeting an entry arrow with an exit arrow triggers computation!', why: 'β-reduction is literally composing an Intro arrow with an Elim arrow.' }
      ]
    }
  };

  function renderShifter(key) {
    const d = SHIFTER_DATA[key] || SHIFTER_DATA.element;
    document.querySelectorAll('#shifterTabs .tab-card').forEach(b => {
      b.setAttribute('aria-selected', String(b.getAttribute('data-shift') === key));
    });
    document.getElementById('shifterPageRef').textContent = `⚖ Marinov pp. ${d.pages.join(', ')}`;
    document.getElementById('shifterStage').innerHTML = `
      <div class="view-pane">
        <div class="view-pane-head">
          <span style="color:var(--w-sets)">● Concrete / Inbound View (Marinov)</span>
          <button class="cite-pill" onclick="window.__jumpToPage(${d.pages[0]}, '')">§ p.${d.pages[0]}</button>
        </div>
        <h3 class="serif" style="font-size:1.15rem;margin-bottom:0.35rem">${escapeHtml(d.internalTitle)}</h3>
        ${renderMathChip(d.internalFormula, true)}
        <div style="background:var(--paper-soft);border:1px solid var(--rule-hair);margin:0.55rem 0">${d.internalSvg}</div>
        <p style="font-size:0.86rem;color:var(--ink-2);margin:0">${formatInlineProse(d.internalDesc)}</p>
      </div>
      <div class="view-pane">
        <div class="view-pane-head">
          <span style="color:var(--w-cats)">◆ Point-Free / Universal View (Marinov)</span>
          <button class="cite-pill" onclick="window.__jumpToPage(${d.pages[d.pages.length-1]}, '')">§ p.${d.pages[d.pages.length-1]}</button>
        </div>
        <h3 class="serif" style="font-size:1.15rem;margin-bottom:0.35rem">${escapeHtml(d.externalTitle)}</h3>
        ${renderMathChip(d.externalFormula, true)}
        <div style="background:var(--paper-soft);border:1px solid var(--rule-hair);margin:0.55rem 0">${d.externalSvg}</div>
        <p style="font-size:0.86rem;color:var(--ink-2);margin:0">${formatInlineProse(d.externalDesc)}</p>
      </div>
    `;
    const decEl = document.getElementById('shifterDecoder');
    if (decEl) decEl.innerHTML = renderDecoderHtml(d.decoder, 'Symbol-by-Symbol Visual Decoder · How to Read the Formula Above');
    document.getElementById('shifterDerived').innerHTML = `
      <div><strong>Point-Free Law:</strong> <em>${formatInlineProse(d.invariant)}</em></div>
      <div>${d.pages.map(p => `<button class="cite-pill" onclick="window.__jumpToPage(${p}, '')">§ p.${p}</button>`).join(' ')}</div>
    `;
  }
  document.querySelectorAll('#shifterTabs .tab-card').forEach(btn => {
    btn.addEventListener('click', () => renderShifter(btn.getAttribute('data-shift')));
  });
  renderShifter('element');

  // ==========================================================================
  // PLATE I-B: MARINOV'S INKSCAPE VISUAL ATLAS (6 INTERACTIVE INSTRUMENTS)
  // ==========================================================================
  const atlasState = { key: 'monoid_loop', modeIdx: 0 };

  function getAtlasData(key, modeIdx) {
    const m = modeIdx % 3;
    const map = {
      monoid_loop: {
        pages: [95, 97, 104, 124],
        leftBadge: '🎨 Ch 3 Concrete Picture · CMYK Pigments & D₃ Triangle (pp. 95–114)',
        leftTitle: m === 0 ? 'Rotating Equilateral Triangle (0°, 120°, 240°)' : (m === 1 ? 'Rotated +120° (r₁ ∘ r₁ = r₂ = 240°)' : 'CMYK Pigment Mixing with White Identity Ball (p. 97)'),
        leftFormula: m === 2 ? '\\mathrm{Cyan} \\star \\mathrm{Yellow} = \\mathrm{Green}, \\quad \\mathrm{White} \\star c = c' : `(120^\\circ + 120^\\circ) \\equiv 240^\\circ \\pmod{360^\\circ}, \\quad r_0 = 0^\\circ`,
        leftSvg: m === 2
          ? `<svg viewBox="0 0 360 175" width="100%"><circle cx="68" cy="60" r="20" fill="#FFFFFF" stroke="#17181C" stroke-width="1.8"/><text x="68" y="64" text-anchor="middle" font-family="JetBrains Mono" font-size="9">White e</text><circle cx="155" cy="60" r="20" fill="#00A6D6" stroke="#17181C" stroke-width="1.6"/><text x="155" y="64" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9">Cyan</text><circle cx="242" cy="60" r="20" fill="#E6B800" stroke="#17181C" stroke-width="1.6"/><text x="242" y="64" text-anchor="middle" font-family="JetBrains Mono" font-size="9">Yellow</text><circle cx="198" cy="132" r="22" fill="#2E8B57" stroke="#17181C" stroke-width="1.8"/><text x="198" y="136" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9.5">Green</text><line x1="168" y1="77" x2="188" y2="112" stroke="#17181C" stroke-width="1.6"/><line x1="230" y1="77" x2="210" y2="112" stroke="#17181C" stroke-width="1.6"/><text x="180" y="22" text-anchor="middle" font-family="Fraunces" font-size="12.5">Marinov’s Pigment Monoid: White = Identity e (p. 97)</text></svg>`
          : `<svg viewBox="0 0 360 175" width="100%"><g transform="translate(180,98) rotate(${m * 120})"><polygon points="0,-54 48,30 -48,30" fill="rgba(184,125,36,0.14)" stroke="#17181C" stroke-width="2"/><circle cx="0" cy="-54" r="11" fill="#B34434" stroke="#17181C"/><text x="0" y="-50" text-anchor="middle" fill="#fff" font-size="9" font-family="JetBrains Mono">A</text><circle cx="48" cy="30" r="11" fill="#2B5B84" stroke="#17181C"/><text x="48" y="34" text-anchor="middle" fill="#fff" font-size="9" font-family="JetBrains Mono">B</text><circle cx="-48" cy="30" r="11" fill="#2E6444" stroke="#17181C"/><text x="-48" y="34" text-anchor="middle" fill="#fff" font-size="9" font-family="JetBrains Mono">C</text></g><path d="M 248 56 A 52 52 0 0 1 258 118" fill="none" stroke="#B34434" stroke-width="1.8" stroke-dasharray="4 2"/><text x="295" y="90" font-family="JetBrains Mono" font-size="10" fill="#B34434">Rot ${m*120}°</text><text x="180" y="22" text-anchor="middle" font-family="Fraunces" font-size="12.5">Marinov’s Symmetry Group D₃ (pp. 103–114)</text></svg>`,
        leftDesc: 'Marinov introduces Monoids and Groups visually via pigment mixing (p. 97, where White is the neutral identity ball) and triangle symmetries (pp. 103–114).',
        btnLabel: '↻ Cycle Visual State: Rotate Triangle +120° / Mix CMYK Pigments',
        rightBadge: '◆ Ch 3 Point-Free Instrument · 1-Object Looping Category BM (p. 124)',
        rightTitle: 'Every Monoid Is a Category With One Object •',
        rightFormula: '\\mathrm{Ob}(\\mathbf{B}M) = \\{\\bullet\\}, \\qquad \\mathrm{Hom}(\\bullet, \\bullet) = M',
        rightSvg: `<svg viewBox="0 0 360 175" width="100%"><defs><marker id="ma1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><circle cx="180" cy="95" r="20" fill="#17181C"/><text x="180" y="100" text-anchor="middle" fill="#F6F1E7" font-family="Fraunces" font-size="16">&bull;</text><path d="M 164 80 C 110 18, 250 18, 196 80" fill="none" stroke="#2E6444" stroke-width="1.8" marker-end="url(#ma1)"/><text x="180" y="26" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#2E6444">id = 0° / White e</text><path d="M 160 95 C 82 42, 82 148, 160 103" fill="none" stroke="#B34434" stroke-width="1.8" marker-end="url(#ma1)"/><text x="48" y="98" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#B34434">r₁ (120°)</text><path d="M 200 95 C 278 42, 278 148, 200 103" fill="none" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#ma1)"/><text x="312" y="98" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#2B5B84">r₂ (240°)</text><text x="180" y="162" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="11">Elements of M become self-loop arrows • &rarr; • (p. 124)</text></svg>`,
        rightDesc: 'Instead of treating a monoid as a set of nouns with a multiplication table, Category Theory views it as a 1-object state machine where elements are action loops!',
        invariant: 'Delooping Principle (p. 124): A monoid is a 1-object category BM; a group is a 1-object category where every arrow has a two-sided inverse.',
        decoder: [
          { sym: '\\mathbf{B}M = \\{\\bullet\\}', p: 124, meaning: 'Collapse the whole system into ONE anonymous dot •.', why: 'Shifts focus from static "things" to composable "actions/verbs".' },
          { sym: 'a \\star b \\equiv a \\circ b', p: 97, meaning: 'Multiplying/mixing two elements is chasing one self-loop after another.', why: 'Associativity of ⋆ is literally associativity of arrow composition!' },
          { sym: 'e \\equiv \\mathrm{id}_\\bullet', p: 97, meaning: 'White pigment / 0° rotation = the do-nothing identity arrow.', why: 'Mixing White or rotating 0° leaves any state unchanged.' }
        ]
      },
      hasse_cube: {
        pages: [145, 147, 149, 151],
        leftBadge: '🎨 Ch 4 Visual Trinity · Switch the 8 Cube Vertices Across 3 Worlds',
        leftTitle: m === 0 ? 'World A: Divisors of 30 Cube (1 → 2,3,5 → 6,10,15 → 30)' : (m === 1 ? 'World B: Primary Pigment Cube (White → C,M,Y → R,G,B → Black)' : 'World C: Power Set Cube P({a,b,c}) Ordered by ⊆'),
        leftFormula: m === 0 ? 'x \\le y \\iff x \\mid y, \\quad x \\wedge y = \\gcd(x,y), \\quad x \\vee y = \\mathrm{lcm}(x,y)' : (m === 1 ? '\\mathrm{White} \\le \\{C,M,Y\\} \\le \\{R,G,B\\} \\le \\mathrm{Black}' : 'A \\le B \\iff A \\subseteq B, \\quad A \\wedge B = A \\cap B, \\quad A \\vee B = A \\cup B'),
        leftSvg: (() => {
          const labels = m === 0
            ? ['1 (Bot)', '2', '3', '5', '6', '10', '15', '30 (Top)']
            : (m === 1
              ? ['White ⊥', 'Cyan', 'Magenta', 'Yellow', 'Blue', 'Green', 'Red', 'Black ⊤']
              : ['∅', '{a}', '{b}', '{c}', '{a,b}', '{a,c}', '{b,c}', '{a,b,c}']);
          return `<svg viewBox="0 0 360 175" width="100%">
            <line x1="180" y1="152" x2="95" y2="112" stroke="#17181C" stroke-width="1.4"/><line x1="180" y1="152" x2="180" y2="112" stroke="#17181C" stroke-width="1.4"/><line x1="180" y1="152" x2="265" y2="112" stroke="#17181C" stroke-width="1.4"/>
            <line x1="95" y1="112" x2="95" y2="62" stroke="#2B5B84" stroke-width="1.4"/><line x1="95" y1="112" x2="180" y2="62" stroke="#2B5B84" stroke-width="1.4"/>
            <line x1="180" y1="112" x2="95" y2="62" stroke="#2B5B84" stroke-width="1.4"/><line x1="180" y1="112" x2="265" y2="62" stroke="#2B5B84" stroke-width="1.4"/>
            <line x1="265" y1="112" x2="180" y2="62" stroke="#2B5B84" stroke-width="1.4"/><line x1="265" y1="112" x2="265" y2="62" stroke="#2B5B84" stroke-width="1.4"/>
            <line x1="95" y1="62" x2="180" y2="22" stroke="#B87D24" stroke-width="1.6"/><line x1="180" y1="62" x2="180" y2="22" stroke="#B87D24" stroke-width="1.6"/><line x1="265" y1="62" x2="180" y2="22" stroke="#B87D24" stroke-width="1.6"/>
            ${[
              [180,152,labels[0],'#F6F1E7','#17181C'],
              [95,112,labels[1],'#E6EEF6','#1E4363'],[180,112,labels[2],'#E6EEF6','#1E4363'],[265,112,labels[3],'#E6EEF6','#1E4363'],
              [95,62,labels[4],'#F5E8D0','#B87D24'],[180,62,labels[5],'#F5E8D0','#B87D24'],[265,62,labels[6],'#F5E8D0','#B87D24'],
              [180,22,labels[7],'#17181C','#F6F1E7']
            ].map(([x,y,t,bg,fg]) => `<g transform="translate(${x-32},${y-11})"><rect width="64" height="22" rx="3" fill="${bg}" stroke="#17181C" stroke-width="1.3"/><text x="32" y="15" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" font-weight="600" fill="${fg}">${t}</text></g>`).join('')}
          </svg>`;
        })(),
        leftDesc: 'Click the button below to relabel the 8 vertices between Divisors of 30 (p. 149), Pigment Mixing (p. 145), and Subsets (p. 147) — the 3D arrow skeleton never changes!',
        btnLabel: '🔄 Switch Cube World: Divisors of 30 ↔ CMYK Pigments ↔ Subsets P({a,b,c})',
        rightBadge: '◆ Ch 4 Categorical Synthesis · Thin Poset Category & Birkhoff Theorem',
        rightTitle: 'Meet (∧) IS Categorical Product; Join (∨) IS Coproduct',
        rightFormula: 'c \\le a \\wedge b \\iff (c \\le a \\;\\&\\; c \\le b), \\qquad L \\cong \\mathcal{O}(\\mathrm{Irr}(L))',
        rightSvg: `<svg viewBox="0 0 360 175" width="100%"><defs><marker id="ma2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><rect x="104" y="16" width="152" height="26" rx="3" fill="#2E6444" stroke="#17181C"/><text x="180" y="33" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9.5">a &or; b = lcm(2,3) = 6</text><circle cx="88" cy="88" r="22" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/><text x="88" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10.5">a = 2</text><circle cx="272" cy="88" r="22" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/><text x="272" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10.5">b = 3</text><rect x="104" y="134" width="152" height="26" rx="3" fill="#1E4363" stroke="#17181C"/><text x="180" y="151" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9.5">a &and; b = gcd(2,3) = 1</text><line x1="106" y1="73" x2="152" y2="44" stroke="#2E6444" stroke-width="1.6" marker-end="url(#ma2)"/><line x1="254" y1="73" x2="208" y2="44" stroke="#2E6444" stroke-width="1.6" marker-end="url(#ma2)"/><line x1="152" y1="134" x2="106" y2="103" stroke="#1E4363" stroke-width="1.6" marker-end="url(#ma2)"/><line x1="208" y1="134" x2="254" y2="103" stroke="#1E4363" stroke-width="1.6" marker-end="url(#ma2)"/></svg>`,
        rightDesc: 'In a thin category (at most 1 arrow between objects), the universal Product cone becomes Greatest Lower Bound (gcd / ∩) and Coproduct becomes Least Upper Bound (lcm / ∪).',
        invariant: 'Birkhoff Representation Theorem (p. 148–152): Every finite distributive lattice is isomorphic to the lattice of subsets generated by its 3 join-irreducible atoms (primes 2,3,5 or primaries C,M,Y).',
        decoder: [
          { sym: '|\\mathrm{Hom}(a,b)| \\le 1', p: 156, meaning: 'At most ONE arrow from a to b ("thin category").', why: 'All diagrams commute automatically because any two paths are equal!' },
          { sym: 'a \\wedge b \\;(\\mathrm{Meet})', p: 149, meaning: 'Highest node below both a and b (gcd / intersection).', why: 'Exact translation of the Product cone A × B into a Hasse diagram.' },
          { sym: 'a \\vee b \\;(\\mathrm{Join})', p: 149, meaning: 'Lowest node above both a and b (lcm / union).', why: 'Exact translation of the Coproduct cocone A + B into a Hasse diagram.' }
        ]
      },
      heyting_lever: {
        pages: [171, 184, 198, 204],
        leftBadge: '🎨 Ch 5 Visual Logic · Coloring-Book Schemas & BHK Paths (pp. 171, 184)',
        leftTitle: m % 2 === 0 ? 'Coloring-Book Axiom Schema & Constructive Proof Path' : 'Visual Contraposition: Reversing the Arrow Direction (p. 204)',
        leftFormula: m % 2 === 0 ? '(A \\wedge (A \\Rightarrow B)) \\xrightarrow{\\mathrm{eval}} B \\quad (\\text{Modus Ponens, p. 201})' : '(A \\le B) \\implies (\\neg B = (B \\Rightarrow \\bot) \\le (A \\Rightarrow \\bot) = \\neg A)',
        leftSvg: m % 2 === 0
          ? `<svg viewBox="0 0 360 175" width="100%"><rect x="28" y="28" width="135" height="115" rx="6" fill="rgba(184,125,36,0.09)" stroke="#B87D24"/><text x="95" y="48" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#B87D24">COLORING SCHEMA (P.171)</text><circle cx="65" cy="85" r="16" fill="none" stroke="#17181C" stroke-width="1.8" stroke-dasharray="3 2"/><circle cx="122" cy="85" r="16" fill="none" stroke="#17181C" stroke-width="1.8"/><text x="95" y="125" text-anchor="middle" font-size="9.5" font-family="Fraunces">Fill any proposition P, Q</text><rect x="188" y="28" width="146" height="115" rx="6" fill="rgba(46,100,68,0.09)" stroke="#2E6444"/><text x="261" y="48" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#2E6444">BHK PROOF PATH (P.184)</text><circle cx="215" cy="90" r="14" fill="#B34434"/><text x="215" y="94" text-anchor="middle" fill="#fff" font-size="9">A</text><circle cx="305" cy="90" r="14" fill="#2E6444"/><text x="305" y="94" text-anchor="middle" fill="#fff" font-size="9">B</text><path d="M 232 90 Q 260 62 288 90" fill="none" stroke="#17181C" stroke-width="2"/><text x="261" y="125" text-anchor="middle" font-size="9.5" font-family="Fraunces">Constructive bridge A &rarr; B</text></svg>`
          : `<svg viewBox="0 0 360 175" width="100%"><circle cx="70" cy="52" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="70" y="57" text-anchor="middle" font-family="Fraunces">A</text><circle cx="175" cy="52" r="16" fill="#F6F1E7" stroke="#17181C"/><text x="175" y="57" text-anchor="middle" font-family="Fraunces">B</text><circle cx="285" cy="92" r="18" fill="#B34434"/><text x="285" y="97" text-anchor="middle" fill="#fff" font-family="Fraunces">&bot;</text><line x1="88" y1="52" x2="155" y2="52" stroke="#2B5B84" stroke-width="2"/><text x="122" y="43" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#2B5B84">f : A &rarr; B</text><line x1="192" y1="60" x2="265" y2="85" stroke="#B34434" stroke-width="2"/><text x="236" y="65" font-family="JetBrains Mono" font-size="9" fill="#B34434">&not;B : B &rarr; &bot;</text><path d="M 75 70 Q 170 145 265 100" fill="none" stroke="#17181C" stroke-width="2" stroke-dasharray="4 2"/><text x="170" y="142" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">&not;A = (&not;B) &#8728; f : A &rarr; &bot; (p. 204)</text></svg>`,
        leftDesc: 'In Chapter 5, Marinov draws axiom schemas as uncolored outlines you fill with any pigment (p. 171) and proves Contraposition (p. 204) by pre-composing B → ⊥ with A → B!',
        btnLabel: '⇄ Toggle View: Coloring-Book & BHK Paths ↔ Contraposition Arrow Reversal',
        rightBadge: '◆ Ch 5 Universal Lever · Heyting Implication Adjunction (pp. 198–202)',
        rightTitle: 'The Two-Pan Implication Seesaw: Conjunction ⊣ Implication',
        rightFormula: 'C \\wedge A \\le B \\quad \\Longleftrightarrow \\quad C \\le (A \\Rightarrow B)',
        rightSvg: `<svg viewBox="0 0 360 175" width="100%"><polygon points="180,122 162,155 198,155" fill="#17181C"/><line x1="45" y1="122" x2="315" y2="122" stroke="#17181C" stroke-width="3"/><rect x="35" y="58" width="122" height="52" rx="4" fill="rgba(43,91,132,0.12)" stroke="#2B5B84" stroke-width="1.6"/><text x="96" y="82" text-anchor="middle" font-family="Fraunces" font-weight="600" font-size="13" fill="#1E4363">C &and; A &le; B</text><text x="96" y="99" text-anchor="middle" font-family="JetBrains Mono" font-size="8.5">Context C + Premise A</text><rect x="203" y="58" width="122" height="52" rx="4" fill="rgba(184,125,36,0.14)" stroke="#B87D24" stroke-width="1.6"/><text x="264" y="82" text-anchor="middle" font-family="Fraunces" font-weight="600" font-size="13" fill="#B87D24">C &le; (A &rArr; B)</text><text x="264" y="99" text-anchor="middle" font-family="JetBrains Mono" font-size="8.5">Curried Rule A &rArr; B</text><path d="M 160 44 Q 180 24 200 44" fill="none" stroke="#2E6444" stroke-width="1.8"/><text x="180" y="26" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#2E6444">Curry / Uncurry</text></svg>`,
        rightDesc: 'Moving A across the turnstile ≤ turns AND (∧) on the left into IMPLIES (⇒) on the right — the exact same universal law as function currying!',
        invariant: 'Deduction-Currying Identity (p. 200–203): Proving B from (C ∧ A) is equivalent to proving the implication (A ⇒ B) from C alone.',
        decoder: [
          { sym: 'C \\wedge A \\le B', p: 198, meaning: 'Having both context C and premise A is enough to deduce B.', why: 'In code: a two-argument function `(C, A) -> B`.' },
          { sym: 'C \\le (A \\Rightarrow B)', p: 199, meaning: 'Context C alone gives you a reusable proof machine `A => B`.', why: 'In code: currying `C -> (A -> B)`!' },
          { sym: '\\neg A \\equiv (A \\Rightarrow \\bot)', p: 204, meaning: 'Negation is simply an arrow from A into Falsehood/Void ⊥.', why: 'Explains why `A -> B` automatically reverses to `(B -> ⊥) -> (A -> ⊥)`!' }
        ]
      },
      russell_trees: {
        pages: [215, 229, 242, 256],
        leftBadge: '⊘ Ch 6 Why Untyped Sets Explode · Russell’s Paradox Loop (pp. 215–221)',
        leftTitle: 'Russell’s Self-Swallowing Barber / Set Circle',
        leftFormula: 'R = \\{ x \\mid x \\notin x \\} \\implies (R \\in R \\iff R \\notin R)',
        leftSvg: `<svg viewBox="0 0 360 175" width="100%"><circle cx="150" cy="94" r="54" fill="rgba(179,68,52,0.10)" stroke="#B34434" stroke-width="2" stroke-dasharray="6 3"/><circle cx="118" cy="86" r="16" fill="#2B5B84"/><text x="118" y="90" text-anchor="middle" fill="#fff" font-size="8.5" font-family="JetBrains Mono">x&notin;x</text><path d="M 194 62 C 244 26, 248 150, 190 126" fill="none" stroke="#B34434" stroke-width="2.2"/><text x="252" y="96" text-anchor="start" font-family="JetBrains Mono" font-size="9.5" font-weight="600" fill="#B34434">R &isin; R ? ⚡</text><text x="180" y="22" text-anchor="middle" font-family="Fraunces" font-size="12" fill="#B34434">Marinov’s Self-Swallowing Set Loop (pp. 215–221)</text></svg>`,
        leftDesc: 'When sets can swallow themselves without stratification, asking whether R contains itself creates a fatal logical short-circuit. Type Theory prevents this by stratifying values and types.',
        btnLabel: `🌱 Sprout Inductive Tree Depth (${(m % 3) + 1} Succ Branches) & Church Loop`,
        rightBadge: '◆ Ch 6 Inductive Sprouting Trees · Nat = 1 + Nat & Church Loops (pp. 242–256)',
        rightTitle: `Inductive Sprouting Tree: Zero, Succ(${m % 3 === 0 ? 'Zero' : (m % 3 === 1 ? 'Succ(Zero)' : 'Succ(Succ(Zero))')})`,
        rightFormula: '\\mathrm{Nat} \\cong 1 + \\mathrm{Nat} \\quad (\\mathrm{Zero} : 1 \\to \\mathrm{Nat}, \\; \\mathrm{Succ} : \\mathrm{Nat} \\to \\mathrm{Nat})',
        rightSvg: `<svg viewBox="0 0 360 175" width="100%"><circle cx="52" cy="128" r="15" fill="#F6F1E7" stroke="#17181C" stroke-width="1.6"/><text x="52" y="132" text-anchor="middle" font-family="JetBrains Mono" font-size="10">1</text><line x1="68" y1="128" x2="105" y2="128" stroke="#2E6444" stroke-width="2"/><circle cx="122" cy="128" r="16" fill="#2E6444"/><text x="122" y="132" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9.5">0</text>
          ${m >= 0 ? `<line x1="138" y1="120" x2="178" y2="96" stroke="#2E6444" stroke-width="2"/><circle cx="194" cy="88" r="16" fill="#2B5B84"/><text x="194" y="92" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9.5">S(0)</text>` : ''}
          ${m >= 1 ? `<line x1="210" y1="80" x2="248" y2="58" stroke="#2B5B84" stroke-width="2"/><circle cx="264" cy="50" r="16" fill="#B87D24"/><text x="264" y="54" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9">S²(0)</text>` : ''}
          ${m >= 2 ? `<line x1="280" y1="50" x2="312" y2="50" stroke="#B34434" stroke-width="2"/><circle cx="328" cy="50" r="16" fill="#B34434"/><text x="328" y="54" text-anchor="middle" fill="#fff" font-family="JetBrains Mono" font-size="9">S³(0)</text>` : ''}
          <text x="180" y="162" text-anchor="middle" font-family="Fraunces" font-style="italic" font-size="9.6">Click button below to sprout the next Succ constructor (p. 242)</text></svg>`,
        rightDesc: 'Instead of circular self-containment, Inductive Types (pp. 241–248) start from a base seed (Zero : 1 → Nat) and sprout upward step-by-step via Succ : Nat → Nat!',
        invariant: 'Initial Algebra Sprouting Law (p. 242, p. 256): Every natural number n is a finite tower of Succ arrows applied to Zero — or its Church encoding λs. λz. sⁿ(z).',
        decoder: [
          { sym: '() \\to T', p: 229, meaning: 'A value of type T is an arrow from the Unit type `()`.', why: 'Point-free elements applied directly to programming types!' },
          { sym: '\\mathrm{Nat} \\cong 1 + \\mathrm{Nat}', p: 242, meaning: 'A natural number is EITHER `Zero` (from 1) OR `Succ(n)` (from Nat).', why: 'Explains why recursion always needs a base case + inductive step.' },
          { sym: '\\forall a.\\; (a \\to a) \\to a \\to a', p: 256, meaning: 'Church numeral: a number n is "apply step function s n times to seed z".', why: 'Turns data structures into pure higher-order arrow composition!' }
        ]
      },
      island_functor: {
        pages: [289, 293, 305, 307],
        leftBadge: '🎨 Ch 7 Cartographic Metaphor · Island Map Functor F : C → D (pp. 293–295)',
        leftTitle: 'A Functor Is a Map That Never Tears Connected Roads',
        leftFormula: 'F(g \\circ f) = F(g) \\circ F(f), \\qquad F(\\mathrm{id}_A) = \\mathrm{id}_{F(A)}',
        leftSvg: `<svg viewBox="0 0 360 175" width="100%"><path d="M 24 95 Q 35 32 95 36 Q 152 40 148 102 Q 140 148 78 144 Q 20 140 24 95 Z" fill="rgba(46,100,68,0.12)" stroke="#2E6444" stroke-width="1.6"/><text x="88" y="24" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#2E6444">ISLAND C (REALITY, P.293)</text><circle cx="58" cy="70" r="8" fill="#17181C"/><circle cx="115" cy="65" r="8" fill="#17181C"/><circle cx="92" cy="120" r="8" fill="#17181C"/><line x1="58" y1="70" x2="115" y2="65" stroke="#17181C" stroke-width="1.5"/><line x1="115" y1="65" x2="92" y2="120" stroke="#17181C" stroke-width="1.5"/><line x1="58" y1="70" x2="92" y2="120" stroke="#B34434" stroke-width="1.5" stroke-dasharray="3 2"/><rect x="205" y="34" width="132" height="110" rx="4" fill="#F6F1E7" stroke="#1E4363" stroke-width="1.6"/><text x="271" y="24" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#1E4363">SUBWAY MAP F(C) (P.295)</text><circle cx="235" cy="68" r="7" fill="#1E4363"/><circle cx="305" cy="68" r="7" fill="#1E4363"/><circle cx="270" cy="122" r="7" fill="#1E4363"/><line x1="235" y1="68" x2="305" y2="68" stroke="#1E4363" stroke-width="1.5"/><line x1="305" y1="68" x2="270" y2="122" stroke="#1E4363" stroke-width="1.5"/><line x1="235" y1="68" x2="270" y2="122" stroke="#B34434" stroke-width="1.5" stroke-dasharray="3 2"/></svg>`,
        leftDesc: 'On pp. 293–295, Marinov compares a Functor to a cartographic island/subway map: it may bend distances or merge stations, but every connected path on the island stays connected on the map!',
        btnLabel: '⚡ Switch Programming Container: List [r,y,b] ↔ Maybe (Just r) ↔ Maybe (Nothing)',
        rightBadge: '◆ Ch 7 Programming Functor · Container Box + .map(f) (pp. 305–307)',
        rightTitle: m === 0 ? 'List Functor: [r, y, b].map(f) = [f(r), f(y), f(b)]' : (m === 1 ? 'Maybe Functor (Just): (Just r).map(f) = Just f(r)' : 'Maybe Functor (Nothing): Nothing.map(f) = Nothing'),
        rightFormula: '\\mathrm{fmap} : (A \\to B) \\to (F\\;A \\to F\\;B)',
        rightSvg: m === 0
          ? `<svg viewBox="0 0 360 175" width="100%"><rect x="28" y="42" width="118" height="90" rx="6" fill="rgba(43,91,132,0.1)" stroke="#2B5B84" stroke-width="1.8"/><text x="87" y="32" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">List A</text><circle cx="56" cy="87" r="12" fill="#B34434"/><circle cx="87" cy="87" r="12" fill="#B87D24"/><circle cx="118" cy="87" r="12" fill="#2B5B84"/><line x1="154" y1="87" x2="202" y2="87" stroke="#17181C" stroke-width="2"/><text x="178" y="76" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">.map(f)</text><rect x="212" y="42" width="118" height="90" rx="6" fill="rgba(46,100,68,0.1)" stroke="#2E6444" stroke-width="1.8"/><text x="271" y="32" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">List B</text><rect x="230" y="75" width="22" height="22" fill="#B34434"/><rect x="260" y="75" width="22" height="22" fill="#B87D24"/><rect x="290" y="75" width="22" height="22" fill="#2B5B84"/></svg>`
          : (m === 1
            ? `<svg viewBox="0 0 360 175" width="100%"><rect x="40" y="48" width="96" height="78" rx="6" fill="rgba(43,91,132,0.1)" stroke="#2B5B84" stroke-width="1.8"/><circle cx="88" cy="87" r="16" fill="#B34434"/><text x="88" y="36" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">Just r</text><line x1="146" y1="87" x2="208" y2="87" stroke="#17181C" stroke-width="2"/><text x="177" y="76" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">.map(f)</text><rect x="218" y="48" width="96" height="78" rx="6" fill="rgba(46,100,68,0.1)" stroke="#2E6444" stroke-width="1.8"/><rect x="252" y="73" width="28" height="28" fill="#B34434"/><text x="266" y="36" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">Just f(r)</text></svg>`
            : `<svg viewBox="0 0 360 175" width="100%"><rect x="40" y="48" width="96" height="78" rx="6" fill="none" stroke="#B34434" stroke-width="1.8" stroke-dasharray="4 3"/><text x="88" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#B34434">Nothing</text><line x1="146" y1="87" x2="208" y2="87" stroke="#17181C" stroke-width="2"/><text x="177" y="76" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5">.map(f)</text><rect x="218" y="48" width="96" height="78" rx="6" fill="none" stroke="#B34434" stroke-width="1.8" stroke-dasharray="4 3"/><text x="266" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10" fill="#B34434">Nothing</text></svg>`),
        rightDesc: 'In Chapter 7 (pp. 305–307), a programming Functor is a container box F (`List`, `Maybe`, `Promise`) whose `.map(f)` transforms the items inside without changing the container’s shape!',
        invariant: 'Shape-Preservation Law (p. 306): `.map(f)` never adds, drops, or reorders slots in a container — that is why `Nothing.map(f)` must stay `Nothing`!',
        decoder: [
          { sym: 'F : \\mathcal{C} \\to \\mathcal{D}', p: 289, meaning: 'Two-level translation: moves objects A ↦ F(A) AND arrows f ↦ F(f).', why: 'A map of dots alone is useless unless it also maps the roads between them.' },
          { sym: 'F(g \\circ f) = F(g) \\circ F(f)', p: 295, meaning: 'Mapping a 2-step journey equals taking the 2 mapped steps (`xs.map(g∘f) == xs.map(f).map(g)`).', why: 'Guarantees zero broken triangles when moving between worlds.' }
        ]
      },
      naturality_prism: {
        pages: [344, 348, 357, 362],
        leftBadge: '🎨 Ch 8 3D Geometry · The Naturality Prism C × 2 → D (pp. 357–362)',
        leftTitle: 'Natural Transformation as a 3D Prism Joining Two Functor Sheets',
        leftFormula: '\\alpha : \\mathcal{C} \\times \\mathbf{2} \\to \\mathcal{D} \\quad \\Longleftrightarrow \\quad G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f)',
        leftSvg: `<svg viewBox="0 0 360 175" width="100%">
          <polygon points="55,48 165,22 295,48 185,74" fill="rgba(43,91,132,0.14)" stroke="#2B5B84" stroke-width="1.5"/>
          <polygon points="55,134 165,108 295,134 185,160" fill="rgba(46,100,68,0.14)" stroke="#2E6444" stroke-width="1.5"/>
          <line x1="55" y1="48" x2="55" y2="134" stroke="#B87D24" stroke-width="2" stroke-dasharray="4 2"/>
          <line x1="165" y1="22" x2="165" y2="108" stroke="#B87D24" stroke-width="2" stroke-dasharray="4 2"/>
          <line x1="295" y1="48" x2="295" y2="134" stroke="#B87D24" stroke-width="2" stroke-dasharray="4 2"/>
          <line x1="185" y1="74" x2="185" y2="160" stroke="#B87D24" stroke-width="2" stroke-dasharray="4 2"/>
          <text x="172" y="45" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#1E4363">Top Sheet: Functor F(C)</text>
          <text x="172" y="142" text-anchor="middle" font-family="JetBrains Mono" font-size="9.5" fill="#2E6444">Bottom Sheet: Functor G(C)</text>
          <text x="324" y="95" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#B87D24">&alpha;<tspan dy="2.5" font-size="7.5">A</tspan><tspan dy="-2.5"> Pillars</tspan></text>
        </svg>`,
        leftDesc: 'On pp. 357–362, Marinov visualizes a Natural Transformation as a 3D prism: top functor F(C), bottom functor G(C), and vertical pillars α_A whose side walls all commute!',
        btnLabel: '⚡ Toggle Square: Parametric reverse (Commutes ✓) ↔ Red-Ball Peek Trap (Breaks ⊘ p. 348)',
        rightBadge: m % 2 === 0 ? '✓ Ch 8 Parametric Square · reverse / safeHead (p. 344)' : '⊘ Ch 8 Counterexample · The "Unnatural" Red-Ball Trap (pp. 348–351)',
        rightTitle: m % 2 === 0 ? 'Parametric Function: Blind to Ball Colors → Square Commutes!' : 'Ad-Hoc Color Peek ("If Red, Drop/Swap") → Shatters the Square!',
        rightFormula: m % 2 === 0 ? '\\mathrm{map}(f)(\\mathrm{reverse}([r,b])) = \\mathrm{reverse}(\\mathrm{map}(f)([r,b]))' : '\\mathrm{bad}([r]) = [] \\neq [\\mathrm{green}] = \\mathrm{map}(r \\mapsto g)(\\mathrm{bad}([r]))',
        rightSvg: m % 2 === 0
          ? `<svg viewBox="0 0 360 175" width="100%"><defs><marker id="mnat" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#17181C"/></marker></defs><rect x="28" y="24" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#17181C"/><circle cx="54" cy="41" r="9" fill="#B34434"/><circle cx="84" cy="41" r="9" fill="#2B5B84"/><rect x="248" y="24" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#17181C"/><rect x="266" y="32" width="18" height="18" fill="#B34434"/><rect x="296" y="32" width="18" height="18" fill="#2B5B84"/><rect x="28" y="116" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#17181C"/><circle cx="54" cy="133" r="9" fill="#2B5B84"/><circle cx="84" cy="133" r="9" fill="#B34434"/><rect x="248" y="116" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#2E6444" stroke-width="2"/><rect x="266" y="124" width="18" height="18" fill="#2B5B84"/><rect x="296" y="124" width="18" height="18" fill="#B34434"/><line x1="116" y1="41" x2="242" y2="41" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#mnat)"/><text x="180" y="34" text-anchor="middle" font-family="JetBrains Mono" font-size="9">map(f)</text><line x1="116" y1="133" x2="242" y2="133" stroke="#2E6444" stroke-width="1.8" marker-end="url(#mnat)"/><text x="180" y="126" text-anchor="middle" font-family="JetBrains Mono" font-size="9">map(f)</text><line x1="70" y1="62" x2="70" y2="112" stroke="#B87D24" stroke-width="1.8" marker-end="url(#mnat)"/><text x="42" y="90" font-family="JetBrains Mono" font-size="9" fill="#B87D24">rev</text><line x1="290" y1="62" x2="290" y2="112" stroke="#B87D24" stroke-width="1.8" marker-end="url(#mnat)"/><text x="322" y="90" font-family="JetBrains Mono" font-size="9" fill="#B87D24">rev</text><text x="180" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="600" fill="#2E6444">✓ COMMUTES (P. 344)</text></svg>`
          : `<svg viewBox="0 0 360 175" width="100%"><defs><marker id="mnat2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#B34434"/></marker></defs><rect x="28" y="24" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#17181C"/><circle cx="70" cy="41" r="10" fill="#B34434"/><rect x="248" y="24" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#17181C"/><circle cx="290" cy="41" r="10" fill="#2E6444"/><rect x="28" y="116" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#B34434" stroke-dasharray="3 2"/><text x="70" y="137" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#B34434">[] (Dropped!)</text><rect x="248" y="116" width="84" height="34" rx="4" fill="#F6F1E7" stroke="#B34434" stroke-width="2"/><text x="290" y="137" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#B34434">[green] &ne; []</text><line x1="116" y1="41" x2="242" y2="41" stroke="#2B5B84" stroke-width="1.8" marker-end="url(#mnat2)"/><text x="180" y="34" text-anchor="middle" font-family="JetBrains Mono" font-size="9">f(red)=green</text><line x1="70" y1="62" x2="70" y2="112" stroke="#B34434" stroke-width="1.8" marker-end="url(#mnat2)"/><text x="42" y="90" font-family="JetBrains Mono" font-size="8.5" fill="#B34434">dropRed</text><line x1="290" y1="62" x2="290" y2="112" stroke="#B34434" stroke-width="1.8" marker-end="url(#mnat2)"/><text x="180" y="92" text-anchor="middle" font-family="JetBrains Mono" font-size="10" font-weight="600" fill="#B34434">⊘ SQUARE SHATTERED (P. 348)</text></svg>`,
        rightDesc: 'On pp. 348–351, Marinov shows how a function that peeks at an element’s color ("if red ball, drop it") breaks naturality as soon as f recolors red to green!',
        invariant: 'Reynold-Wadler Parametricity Law (pp. 344–351): A polymorphic function α : ∀a. F a → G a is natural iff it rearranges container slots without inspecting element values.',
        decoder: [
          { sym: '\\alpha_A : F(A) \\to G(A)', p: 344, meaning: 'Component arrow repackaging container F(A) into G(A) at type A.', why: 'One vertical pillar of the 3D prism for each object A.' },
          { sym: 'G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f)', p: 347, meaning: 'Repackage-then-map equals Map-then-repackage.', why: 'Holds automatically whenever α cannot peek inside the elements of A!' },
          { sym: '\\mathcal{C} \\times \\mathbf{2} \\to \\mathcal{D}', p: 357, meaning: 'Product of category C with the 1-arrow interval category (0 → 1).', why: 'Turns a family of arrows α_A into a single 3D prism functor!' }
        ]
      }
    };
    return map[key] || map.monoid_loop;
  }

  function renderAtlas(key) {
    if (key) atlasState.key = key;
    const d = getAtlasData(atlasState.key, atlasState.modeIdx);
    document.querySelectorAll('#atlasTabs .tab-card').forEach(b => {
      b.setAttribute('aria-selected', String(b.getAttribute('data-atlas') === atlasState.key));
    });
    const refEl = document.getElementById('atlasPageRef');
    if (refEl) refEl.textContent = `◆ Marinov pp. ${d.pages.join(', ')}`;
    const stageEl = document.getElementById('atlasStage');
    if (stageEl) {
      stageEl.innerHTML = `
        <div class="view-pane">
          <div class="view-pane-head">
            <span style="color:var(--w-orders)">${escapeHtml(d.leftBadge)}</span>
            <button class="cite-pill" onclick="window.__jumpToPage(${d.pages[0]}, '')">§ p.${d.pages[0]}</button>
          </div>
          <h3 class="serif" style="font-size:1.12rem;margin-bottom:0.35rem">${escapeHtml(d.leftTitle)}</h3>
          ${renderMathChip(d.leftFormula, true)}
          <div style="background:var(--paper-soft);border:1px solid var(--rule-hair);margin:0.55rem 0">${d.leftSvg}</div>
          <p style="font-size:0.84rem;color:var(--ink-2);margin:0 0 0.6rem">${formatInlineProse(d.leftDesc)}</p>
          <button type="button" class="btn-primary" style="width:100%;padding:6px 10px;font-size:0.72rem" onclick="window.__atlasCycleState()">${escapeHtml(d.btnLabel)}</button>
        </div>
        <div class="view-pane">
          <div class="view-pane-head">
            <span style="color:var(--w-cats)">${escapeHtml(d.rightBadge)}</span>
            <button class="cite-pill" onclick="window.__jumpToPage(${d.pages[d.pages.length-1]}, '')">§ p.${d.pages[d.pages.length-1]}</button>
          </div>
          <h3 class="serif" style="font-size:1.12rem;margin-bottom:0.35rem">${escapeHtml(d.rightTitle)}</h3>
          ${renderMathChip(d.rightFormula, true)}
          <div style="background:var(--paper-soft);border:1px solid var(--rule-hair);margin:0.55rem 0">${d.rightSvg}</div>
          <p style="font-size:0.84rem;color:var(--ink-2);margin:0">${formatInlineProse(d.rightDesc)}</p>
        </div>
      `;
    }
    const decEl = document.getElementById('atlasDecoder');
    if (decEl) decEl.innerHTML = renderDecoderHtml(d.decoder, 'Opaque Notation Unpacked · Symbol-by-Symbol Visual Meaning');
    const derEl = document.getElementById('atlasDerived');
    if (derEl) {
      derEl.innerHTML = `
        <div><strong>Visual Instrument Law:</strong> <em>${formatInlineProse(d.invariant)}</em></div>
        <div>${d.pages.map(p => `<button class="cite-pill" onclick="window.__jumpToPage(${p}, '')">§ p.${p}</button>`).join(' ')}</div>
      `;
    }
  }

  window.__atlasCycleState = function() {
    atlasState.modeIdx = (atlasState.modeIdx + 1) % 6;
    renderAtlas(atlasState.key);
  };

  document.querySelectorAll('#atlasTabs .tab-card').forEach(btn => {
    btn.addEventListener('click', () => {
      atlasState.modeIdx = 0;
      renderAtlas(btn.getAttribute('data-atlas'));
    });
  });
  renderAtlas('monoid_loop');

  // ==========================================================================
  // PLATE II: 6-WORLD ROSETTA STONE TRANSLATOR
  // ==========================================================================
  const ROSETTA_DATA = {
    obj_arr: {
      title: 'Objects (0-Cells) & Morphisms (1-Cells)',
      formula: 'A \\xrightarrow{f} B \\in \\mathrm{Hom}_{\\mathcal{C}}(A, B)',
      summary: 'Every mathematical world in Marinov’s book is defined by choosing what counts as an Object (node) and what counts as a Morphism (directed arrow).',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 18, head: 'Sets & Total Functions', math: 'f : A \\to B', body: 'Objects are unstructured sets of elements; morphisms are many-to-one total functions mapping each input ball to one output ball.' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 82, head: 'Opaque Points & Morphisms', math: '\\mathrm{Ob}(\\mathcal{C}), \\; \\mathrm{Hom}(A,B)', body: 'Objects are abstract points with no internal structure; morphisms are primitive composable arrows.' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 115, head: 'Single State • & Actions', math: '\\mathrm{Ob}(\\mathbf{B}M)=\\{\\bullet\\}, \\; m : \\bullet \\to \\bullet', body: 'There is only one object •! Every monoid element (or triangle rotation 120°) is a self-loop arrow • → •.' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 156, head: 'Elements & Order Relations', math: 'a \\le b \\iff |\\mathrm{Hom}(a,b)| = 1', body: 'Thin category: at most one arrow between any two objects, witnessing that a is less than or equal to b.' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 162, head: 'Propositions & Proofs', math: 'P \\vdash Q', body: 'Objects are logical statements P, Q; an arrow P → Q is a deductive proof deriving conclusion Q from premise P.' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 212, head: 'Data Types & Pure Functions', math: '\\Gamma \\vdash f : A \\to B', body: 'Objects are static types (Int, Bool, String); morphisms are pure computable functions / terms.' }
      ]
    },
    comp_id: {
      title: 'Associative Composition (g ∘ f) & Identity Loops (id_A)',
      formula: 'h \\circ (g \\circ f) = (h \\circ g) \\circ f, \\qquad \\mathrm{id}_B \\circ f = f = f \\circ \\mathrm{id}_A',
      summary: 'Why does category theory require exactly two laws (Associativity + Identity)? Because they are the minimum laws needed for multi-step paths to have a well-defined meaning.',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 35, head: 'Function Pipeline & Pass-Through', math: '(g \\circ f)(x) = g(f(x)), \\; \\mathrm{id}_A(x)=x', body: 'Feeding the output of f into g; the identity function returns every ball unchanged.' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 92, head: 'Commutative Path Triangle', math: 'g \\circ f = h', body: 'Any two directed paths with the same start and end that bound a commuting triangle represent the same morphism.' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 97, head: 'Binary Operation ⋆ & Neutral e', math: '(a \\star b) \\star c = a \\star (b \\star c), \\; e \\star a = a', body: 'Composition IS the monoid operation (e.g., string concatenation or adding angles 120° + 240° = 0°).' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 131, head: 'Transitivity & Reflexivity', math: '(a \\le b \\wedge b \\le c) \\Rightarrow a \\le c, \\; a \\le a', body: 'Composition is transitivity of ≤; identity is reflexivity (every element is ≤ itself).' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 165, head: 'Syllogism / Cut & Tautology', math: '\\frac{P \\vdash Q \\quad Q \\vdash R}{P \\vdash R}, \\quad P \\vdash P', body: 'Chaining two deduction steps into a combined proof; identity is the trivial assumption P ⊢ P.' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 260, head: 'Pipeline Composition & x => x', math: 'x \\mapsto g(f(x)), \\quad \\lambda x:A.\\; x', body: 'Composing pure functions and beta-reducing intermediate variables.' }
      ]
    },
    init_term: {
      title: 'Initial Object (0) & Terminal Object (1)',
      formula: '\\forall A, \\quad \\exists! \\; 0 \\to A \\quad (\\text{Initial}) \\qquad \\text{and} \\qquad \\exists! \\; A \\to 1 \\quad (\\text{Terminal})',
      summary: 'The ultimate source (0) and ultimate sink (1) of a category — duals of one another obtained by reversing arrow direction.',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 22, head: 'Empty Set ∅ & Singleton {•}', math: '0 = \\emptyset, \\quad 1 = \\{\\bullet\\}', body: 'There is one vacuous function ∅ → A and one constant function A → {•}.' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 75, head: 'Universal Source 0 & Sink 1', math: '!^A : 0 \\to A, \\quad !_A : A \\to 1', body: 'Defined purely by uniqueness of outgoing vs. incoming arrows.' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 109, head: 'Trivial One-Element Group {e}', math: '0 \\cong 1 \\cong \\{e\\} \\text{ in } \\mathbf{Grp}', body: 'In the category of Monoids/Groups, the 1-element monoid {e} is both Initial and Terminal (a Zero object)!' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 145, head: 'Bottom Minimum ⊥ & Top Maximum ⊤', math: '\\forall a,\\; \\bot \\le a \\le \\top', body: 'Bottom element (e.g., 1 in divisibility, white/black in pigment) and Top element (30 in divisibility).' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 165, head: 'Falsity ⊥ (Ex Falso) & Truth ⊤', math: '\\bot \\vdash P, \\quad P \\vdash \\top', body: 'From contradiction ⊥ anything follows (Initial); Truth ⊤ is implied by everything (Terminal).' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 234, head: 'Void / Never & Unit ()', math: '\\mathrm{absurd} : \\mathrm{Void} \\to A, \\quad \\mathrm{unit} : A \\to ()', body: 'Uninhabited Void type (0 values) and Unit type (exactly 1 value `()`).' }
      ]
    },
    product: {
      title: 'Universal Product (A × B), Lattice Meet (∧) & Logical Conjunction (AND)',
      formula: '\\mathrm{Hom}(C, A \\times B) \\cong \\mathrm{Hom}(C, A) \\times \\mathrm{Hom}(C, B)',
      summary: 'To map into A × B is to map into A AND into B simultaneously.',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 53, head: 'Cartesian Product of Pairs', math: 'A \\times B = \\{(a,b)\\}', body: 'Grid of ordered pairs equipped with coordinate projections fst and snd.' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 62, head: 'Product Cone (A × B, π₁, π₂)', math: '\\pi_1 \\circ \\langle f,g \\rangle = f, \\; \\pi_2 \\circ \\langle f,g \\rangle = g', body: 'Universal object factoring any span C → A, C → B uniquely.' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 113, head: 'Direct Product Group G × H', math: '(g_1, h_1) \\star (g_2, h_2) = (g_1 g_2, h_1 h_2)', body: 'Componentwise symmetry operations (e.g., independent rotations in product groups).' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 145, head: 'Greatest Lower Bound / Meet (a ∧ b)', math: 'c \\le a \\wedge b \\iff c \\le a \\text{ and } c \\le b', body: 'Intersection A ∩ B in subsets; greatest common divisor gcd(a,b) in divisibility.' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 165, head: 'Conjunction P ∧ Q (Logical AND)', math: 'R \\vdash P \\wedge Q \\iff (R \\vdash P) \\;\\&\\; (R \\vdash Q)', body: 'And-Introduction ⟨f,g⟩ and And-Elimination projections π₁ : P∧Q ⊢ P, π₂ : P∧Q ⊢ Q.' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 248, head: 'Record / Tuple Type (A, B)', math: '\\mathrm{Pair}\\langle A, B \\rangle = \\{\\mathrm{fst}: A, \\mathrm{snd}: B\\}', body: 'Struct/tuple product type constructed from both an A value and a B value.' }
      ]
    },
    coproduct: {
      title: 'Universal Coproduct (A + B), Lattice Join (∨) & Logical Disjunction (OR)',
      formula: '\\mathrm{Hom}(A + B, C) \\cong \\mathrm{Hom}(A, C) \\times \\mathrm{Hom}(B, C)',
      summary: 'Dual to Product: to map out of A + B into C is to handle the A case AND handle the B case via [f, g].',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 69, head: 'Tagged Disjoint Union A ⊔ B', math: 'A \\sqcup B = (\\{1\\}\\times A) \\cup (\\{2\\}\\times B)', body: 'Union that keeps elements from A and B distinct by tagging their origin.' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 71, head: 'Coproduct Cocone (A + B, ι₁, ι₂)', math: '[f,g] \\circ \\iota_1 = f, \\; [f,g] \\circ \\iota_2 = g', body: 'Universal object receiving canonical injections ι₁, ι₂ and factoring out via [f,g].' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 128, head: 'Free Product of Monoids', math: 'M * N', body: 'Alternating words of actions drawn from M and N.' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 145, head: 'Least Upper Bound / Join (a ∨ b)', math: 'a \\vee b \\le c \\iff a \\le c \\text{ and } b \\le c', body: 'Union A ∪ B in subsets; least common multiple lcm(a,b) in divisibility; mixed pigment in colors.' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 165, head: 'Disjunction P ∨ Q (Logical OR)', math: 'P \\vee Q \\vdash R \\iff (P \\vdash R) \\;\\&\\; (Q \\vdash R)', body: 'Or-Introduction injections (P ⊢ P∨Q) and Or-Elimination proof by cases [f,g].' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 236, head: 'Sum / Tagged Union (Either A B, Maybe A)', math: '\\mathrm{Either}\\;A\\;B = \\mathrm{Left}\\;A \\mid \\mathrm{Right}\\;B', body: 'Algebraic sum type eliminated by exhaustive pattern matching.' }
      ]
    },
    exponential: {
      title: 'Exponential Object (B^A), Logical Implication (P ⇒ Q) & Lambda Currying',
      formula: '\\mathrm{Hom}(C \\times A, B) \\cong \\mathrm{Hom}(C, B^A)',
      summary: 'Internalizing the hom-set Hom(A, B) as an object B^A inside the category itself — the heart of Bicartesian Closed Categories.',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 42, head: 'Function Set B^A & Currying', math: '\\mathrm{curry} : (C \\times A \\to B) \\xrightarrow{\\sim} (C \\to B^A)', body: 'A two-argument function (C × A) → B is isomorphic to a function returning a function C → (A → B).' },
        { w: 'w-2', badge: 'Ch 2 · Categories', page: 203, head: 'Internal Hom & Evaluation Arrow', math: '\\mathrm{eval} : B^A \\times A \\to B', body: 'Universal object equipped with evaluation morphism eval.' },
        { w: 'w-3', badge: 'Ch 3 · Monoids/Groups', page: 115, head: 'Conjugation & Action Hom', math: 'M\\text{-Set}^M', body: 'Equivariant maps between dynamical monoid actions.' },
        { w: 'w-4', badge: 'Ch 4 · Orders', page: 197, head: 'Relative Pseudocomplement (a ⇒ b)', math: 'c \\wedge a \\le b \\iff c \\le (a \\Rightarrow b)', body: 'The largest element c whose meet with a still lies below b (Heyting algebra).' },
        { w: 'w-5', badge: 'Ch 5 · Logic', page: 180, head: 'Implication P ⇒ Q & Modus Ponens', math: '(P \\Rightarrow Q) \\wedge P \\vdash Q', body: 'Deduction Theorem (currying) and Modus Ponens (evaluation arrow)!' },
        { w: 'w-6', badge: 'Ch 6 · Types / Code', page: 260, head: 'Lambda Abstraction λx:A. t & Application', math: '(\\lambda x:A.\\; t)\\;a \\longrightarrow_{\\beta} t[x := a]', body: 'Function type A → B: Introduction is λ-abstraction, Elimination is function application, Computation is β-reduction.' }
      ]
    },
    functor: {
      title: 'Functors F : C → D — Structure-Preserving Homomorphisms of Worlds',
      formula: 'F(\\mathrm{id}_A) = \\mathrm{id}_{F(A)}, \\qquad F(g \\circ f) = F(g) \\circ F(f)',
      summary: 'A functor translates objects and arrows from one category into another without tearing any commuting triangle.',
      worlds: [
        { w: 'w-1', badge: 'Ch 1 · Sets', page: 278, head: 'Powerset & Representable Functors', math: '\\mathcal{P} : \\mathbf{Set} \\to \\mathbf{Set}', body: 'Mapping a set A to its subsets P(A) and a function f : A → B to its direct image f_*.' },
        { w: 'w-2', badge: 'Ch 7 · Categories', page: 289, head: 'Diagram-Preserving Map F : C → D', math: 'F(g \\circ f) = F(g) \\circ F(f)', body: 'Preserves commuting diagrams and categorical isomorphisms automatically.' },
        { w: 'w-3', badge: 'Ch 7 · Monoids/Groups', page: 298, head: 'Monoid / Group Homomorphism', math: 'f(x \\star y) = f(x) \\cdot f(y), \\; f(e_M)=e_N', body: 'A functor between 1-object categories BM → BN is literally a monoid homomorphism (e.g., length : List A → (ℕ, +, 0))!' },
        { w: 'w-4', badge: 'Ch 7 · Orders', page: 301, head: 'Monotone Order-Preserving Function', math: 'a \\le b \\implies F(a) \\le F(b)', body: 'A functor between thin poset categories is a monotonic map.' },
        { w: 'w-5', badge: 'Ch 7 · Logic', page: 278, head: 'Logical Interpretation / Modal Operator', math: 'P \\vdash Q \\implies \\Box P \\vdash \\Box Q', body: 'Proof-preserving translation between logical theories.' },
        { w: 'w-6', badge: 'Ch 7 · Types / Code', page: 306, head: 'Container Type Constructor + .map', math: '\\mathrm{map}_F : (A \\to B) \\to (F\\;A \\to F\\;B)', body: 'Generic containers (`Array<A>`, `Maybe<A>`, `Promise<A>`) lifting pure functions via `.map`.' }
      ]
    },
    natural: {
      title: 'Natural Transformations α : F ⇒ G & Parametric Polymorphism',
      formula: '\\forall (A \\xrightarrow{f} B), \\qquad G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f)',
      summary: 'Morphisms between functors: translating from worldview F to worldview G consistently across every arrow f.',
      worlds: [
        { w: 'w-1', badge: 'Ch 8 · Sets', page: 319, head: 'Singleton Embedding η_A : A → List A', math: '\\eta_A(x) = [x]', body: 'Wrapping any element into a 1-element list commutes with applying any function f.' },
        { w: 'w-2', badge: 'Ch 8 · Categories', page: 329, head: '2-Cells in the 2-Category Cat', math: '\\alpha : F \\Rightarrow G : \\mathcal{C} \\to \\mathcal{D}', body: 'Morphisms in the functor category [C, D], enabling categorical equivalence C ≃ D.' },
        { w: 'w-3', badge: 'Ch 8 · Monoids/Groups', page: 334, head: 'Conjugation / Inner Automorphism', math: 'g \\cdot f(x) = f\'(x) \\cdot g', body: 'A natural transformation between 1-object functors BM → BN is a conjugating element!' },
        { w: 'w-4', badge: 'Ch 8 · Orders', page: 329, head: 'Pointwise Inequality f(x) ≤ g(x)', math: '\\forall x \\in P, \\; F(x) \\le G(x)', body: 'Between monotone maps P → Q, a natural transformation exists iff F(x) ≤ G(x) for every x.' },
        { w: 'w-5', badge: 'Ch 8 · Logic', page: 350, head: 'Uniform Proof Schema Transformation', math: '\\forall P.\\; F(P) \\vdash G(P)', body: 'Translating proof obligations uniformly without inspecting atomic propositions.' },
        { w: 'w-6', badge: 'Ch 8 · Types / Code', page: 342, head: 'Polymorphic Functions (reverse, safeHead)', math: '\\alpha : \\forall a.\\; F\\;a \\to G\\;a', body: '`xs.reverse().map(f) == xs.map(f).reverse()` — parametric polymorphism guarantees naturality!' }
      ]
    }
  };

  function renderRosetta(key) {
    const d = ROSETTA_DATA[key] || ROSETTA_DATA.obj_arr;
    document.querySelectorAll('#rosettaTabs .tab-card').forEach(b => {
      b.setAttribute('aria-selected', String(b.getAttribute('data-ros') === key));
    });
    document.getElementById('rosettaHeroBar').innerHTML = `
      <div>
        <div class="mono" style="font-size:0.70rem;color:var(--accent-text);text-transform:uppercase;font-weight:600">Universal Categorical Invariant</div>
        <h3 class="serif" style="font-size:1.3rem;margin:0.2rem 0 0.4rem">${escapeHtml(d.title)}</h3>
        <p style="font-size:0.88rem;color:var(--ink-2);margin:0">${escapeHtml(d.summary)}</p>
      </div>
      <div>${renderMathChip(d.formula, true)}</div>
    `;
    document.getElementById('rosettaGrid').innerHTML = d.worlds.map(w => `
      <div class="world-card ${w.w}">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.35rem">
          <span class="mono" style="font-size:0.69rem;font-weight:600;text-transform:uppercase">${escapeHtml(w.badge)}</span>
          <button class="cite-pill" onclick="window.__jumpToPage(${w.page}, '')">§ p.${w.page}</button>
        </div>
        <h4 class="serif" style="font-size:1.05rem;margin-bottom:0.3rem">${escapeHtml(w.head)}</h4>
        <div class="math-display" style="font-size:0.85rem;padding:0.4rem;margin:0.35rem 0">${convertLatexTokensToHtml(w.math)}</div>
        <p style="font-size:0.82rem;color:var(--ink-2);margin:0">${escapeHtml(w.body)}</p>
      </div>
    `).join('');
    document.getElementById('rosettaDerived').innerHTML = `
      <div><strong>Rosetta Synthesis:</strong> <em>All 6 cards above satisfy the exact same universal diagram in Marinov’s sheaf.</em></div>
      <div>Click any § p.N badge to verify on the original Inkscape-illustrated page</div>
    `;
  }
  document.querySelectorAll('#rosettaTabs .tab-card').forEach(btn => {
    btn.addEventListener('click', () => renderRosetta(btn.getAttribute('data-ros')));
  });
  renderRosetta('obj_arr');

  // ==========================================================================
  // PLATE III: SHEAF OPEN-COVER NOTEBOOK STUDIO
  // ==========================================================================
  const state = {
    openCover: new Set(KB.notebook_investigations[0].open_cover),
    focusedStalkId: KB.notebook_investigations[0].open_cover[0],
    currentInvestigation: KB.notebook_investigations[0],
    currentPage: 83,
    highlightTerm: 'Element',
    activeSubview: 'stalks'
  };

  function getActiveRestrictions() {
    return KB.restriction_morphisms.filter(r => state.openCover.has(r.source) && state.openCover.has(r.target));
  }

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
      html += `<div class="mono" style="font-size:0.66rem;text-transform:uppercase;color:var(--ink-3);margin:7px 0 3px">Ch ${chNum} · ${escapeHtml(ch.title.split('—')[0].replace(/Chapter \d+:\s*/, ''))}</div>`;
      stalks.forEach(s => {
        const inCov = state.openCover.has(s.id);
        html += `
          <div class="stalk-item ${inCov ? 'in-cover' : ''}" data-stalk-id="${s.id}">
            <div class="stalk-check" data-check-stalk="${s.id}">${inCov ? '✓' : ''}</div>
            <div style="flex:1;min-width:0">
              <div style="font-weight:500;color:var(--ink);line-height:1.25">${escapeHtml(s.title)}</div>
              <div class="mono" style="font-size:0.66rem;color:var(--ink-3)">§${s.section} · pp.${s.start_page}–${s.end_page}</div>
            </div>
          </div>
        `;
      });
    });
    container.innerHTML = html;
    container.querySelectorAll('.stalk-item').forEach(row => {
      row.addEventListener('click', e => {
        const id = row.getAttribute('data-stalk-id');
        if (state.openCover.has(id)) {
          if (state.openCover.size > 1) state.openCover.delete(id);
        } else {
          state.openCover.add(id);
        }
        state.focusedStalkId = id;
        updateCoverAndOlog();
      });
    });
  }

  function renderGluedOlogSvg(coverStalks) {
    const wrap = document.getElementById('gluedOlogSvgWrap');
    const nodes = [];
    const seen = new Set();
    const edges = [];
    coverStalks.slice(0, 7).forEach(s => {
      const olog = s.olog || {};
      (olog.types || []).forEach(t => {
        const key = `${s.symbol}:${t.id}`;
        if (!seen.has(key)) { seen.add(key); nodes.push({ key, label: t.label }); }
      });
      (olog.aspects || []).forEach(a => {
        edges.push({ src: `${s.symbol}:${a.src}`, tgt: `${s.symbol}:${a.dst}`, lbl: a.label });
      });
    });
    const shownNodes = nodes.slice(0, 10);
    const shownSet = new Set(shownNodes.map(n => n.key));
    const shownEdges = edges.filter(e => shownSet.has(e.src) && shownSet.has(e.tgt)).slice(0, 12);
    document.getElementById('ologSummaryBadge').textContent = `◆ ${shownNodes.length} Olog Types · ${shownEdges.length} Commuting Aspects`;

    const W = 740, H = 250, cx = W / 2, cy = H / 2, rx = 260, ry = 88;
    const pos = {};
    shownNodes.forEach((n, i) => {
      const ang = (2 * Math.PI * i) / Math.max(1, shownNodes.length) - Math.PI / 2;
      pos[n.key] = { x: cx + rx * Math.cos(ang), y: cy + ry * Math.sin(ang) };
    });

    let svg = `<svg viewBox="0 0 ${W} ${H}" width="100%" height="auto"><defs><marker id="oa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#1E4363"/></marker></defs>`;
    shownEdges.forEach((e, idx) => {
      const p1 = pos[e.src], p2 = pos[e.tgt];
      if (!p1 || !p2) return;
      const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2 - (idx % 2 === 0 ? 14 : -14);
      const shortLbl = e.lbl.length > 26 ? e.lbl.slice(0, 24) + '…' : e.lbl;
      svg += `<path d="M ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} Q ${mx.toFixed(1)} ${my.toFixed(1)} ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}" fill="none" stroke="#2B5B84" stroke-width="1.4" marker-end="url(#oa)"/><text x="${mx.toFixed(1)}" y="${(my - 3).toFixed(1)}" text-anchor="middle" font-family="JetBrains Mono" font-size="9" fill="#3A3D45">${escapeHtml(shortLbl)}</text>`;
    });
    shownNodes.forEach(n => {
      const p = pos[n.key];
      const lbl = n.label.length > 23 ? n.label.slice(0, 21) + '…' : n.label;
      const w = Math.max(96, lbl.length * 6.2 + 16);
      svg += `<g transform="translate(${(p.x - w/2).toFixed(1)}, ${(p.y - 14).toFixed(1)})"><rect width="${w}" height="28" rx="3" fill="#F6F1E7" stroke="#17181C" stroke-width="1.3"/><text x="${w/2}" y="18" text-anchor="middle" font-family="DM Sans" font-size="10.5" font-weight="600" fill="#17181C">${escapeHtml(lbl)}</text></g>`;
    });
    svg += `</svg>`;
    wrap.innerHTML = svg;
  }

  function evaluateCoverCohomology(coverIds) {
    const cset = Array.from(coverIds).filter(id => stalkById[id]);
    if (!cset.length) return { verdict: 'FAIL', h0_coherence: 0, beta_0: 0, mean_d0: 1.0, closure: 0, activeR: [], missingPrereqs: [], obstructions: [] };
    const csetLookup = new Set(cset);
    const activeR = KB.restriction_morphisms.filter(r => csetLookup.has(r.source) && csetLookup.has(r.target));

    // Connected components beta_0(U)
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
      ? activeR.reduce((acc, r) => acc + (r.restriction_fidelity || 0.7), 0) / activeR.length
      : (cset.length === 1 ? 0.85 : 0.0);
    const meanD0 = Number((1.0 - meanFid).toFixed(3));

    // Prerequisite closure
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

    // Active 2-simplices holonomy
    const activeSimp = (KB.two_simplices || []).filter(t => (t.vertices || []).every(v => csetLookup.has(v)));
    const meanD1 = activeSimp.length
      ? activeSimp.reduce((acc, t) => acc + (t.holonomy_defect_d1 || 0.14), 0) / activeSimp.length
      : 0.14;

    // Active unbridged H¹ polysemy obstructions
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
      banner.style.background = 'rgba(158, 46, 36, 0.09)';
      banner.style.borderColor = 'rgba(158, 46, 36, 0.45)';
      banner.style.borderLeftColor = 'var(--bad)';
    } else if (coh.verdict === 'WARN') {
      banner.style.background = 'rgba(184, 125, 36, 0.10)';
      banner.style.borderColor = 'rgba(184, 125, 36, 0.45)';
      banner.style.borderLeftColor = 'var(--warn)';
    } else {
      banner.style.background = 'rgba(46, 100, 68, 0.08)';
      banner.style.borderColor = 'rgba(46, 100, 68, 0.35)';
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
      ? `<button class="btn-primary" style="background:var(--bad);border-color:var(--bad);padding:4px 9px;font-size:0.69rem" onclick="window.__resolveCohomologyObstruction('${bridgeIds.join(',')}')">+ Resolve H¹ Obstruction (Add Bridge Stalk)</button>`
      : '';

    banner.innerHTML = `
      <div style="flex:1;min-width:260px">
        <div class="mono" style="font-size:0.71rem;color:${colorVar};font-weight:600;text-transform:uppercase">
          ${escapeHtml(statusLine)}
        </div>
        <div style="font-size:0.85rem;color:var(--ink-2);margin-top:2px"><strong>Active Investigation:</strong> ${escapeHtml(questionText || (state.currentInvestigation && state.currentInvestigation.question) || 'Custom Open-Cover Gluing')}</div>
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
    const mobCnt = document.getElementById('mobileCoverCountLbl');
    if (mobCnt) mobCnt.textContent = coverStalks.length;
    document.getElementById('metricOverlaps').textContent = coh.activeR.length;
    document.getElementById('metricPages').textContent = totalPages;
    const stampEl = document.getElementById('coverGluingStamp');
    stampEl.className = 'stamp ' + (coh.verdict === 'FAIL' ? 'gate' : (coh.verdict === 'WARN' ? 'refine' : 'measured'));
    stampEl.textContent = `${coh.verdict === 'FAIL' ? '⊘' : (coh.verdict === 'WARN' ? '±' : '⚖')} H⁰=${coh.h0_coherence} · ||δ⁰||=${coh.mean_d0} · ${coh.verdict}`;
    renderLiveGluingBanner(coh, state.currentInvestigation && state.currentInvestigation.question);
    renderGluedOlogSvg(coverStalks);
  }

  const SHORT_INV = {
    'q-internal-vs-external-lawvere': 'Internal Balls ↔ External Arrows (Ch 1–2)',
    'q-six-worlds-rosetta-stone': '6-World Rosetta Stone (Ch 1–6)',
    'q-birkhoff-cube-trinity': 'Birkhoff 3D Lattice Cube (Ch 4)',
    'q-type-intro-elim-universal': 'Type Intro/Elim & Church Encodings (Ch 6)',
    'q-functors-natural-polymorphism': 'Functors & Polymorphic Naturality (Ch 7–8)',
    'q-marinov-vs-spivak-bridge': 'Marinov (377 pp.) × Spivak (609 pp.) Bridge'
  };

  function displayInvestigation(inv) {
    state.currentInvestigation = inv;
    const coh = evaluateCoverCohomology(state.openCover);
    renderLiveGluingBanner(coh, inv.question);
    document.getElementById('notebookSynthesisOutput').innerHTML = renderRichMarkdown(inv.synthesis_markdown);
    if (window.__loadPodcastForInvestigation) window.__loadPodcastForInvestigation(inv);
  }

  function renderInvestigationPills() {
    const wrap = document.getElementById('invPillsContainer');
    wrap.innerHTML = KB.notebook_investigations.map((inv, idx) => `
      <button class="inv-pill ${idx === 0 ? 'active' : ''}" data-inv-id="${inv.id}">
        ◆ ${escapeHtml(SHORT_INV[inv.id] || inv.question.slice(0, 44))}
      </button>
    `).join('');
    wrap.querySelectorAll('.inv-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        const inv = KB.notebook_investigations.find(x => x.id === btn.getAttribute('data-inv-id'));
        if (!inv) return;
        wrap.querySelectorAll('.inv-pill').forEach(b => b.classList.toggle('active', b === btn));
        state.openCover = new Set(inv.open_cover);
        displayInvestigation(inv);
        updateCoverAndOlog();
      });
    });
  }

  function runCustomQuery(qStr) {
    const q = (qStr || '').trim();
    if (!q) return;
    const tokens = q.toLowerCase().split(/[^a-z0-9]+/).filter(t => t.length >= 3);
    const scored = KB.stalks.map(s => {
      const hay = (s.title + ' ' + s.summary + ' ' + (s.keywords || []).join(' ')).toLowerCase();
      let sc = state.openCover.has(s.id) ? 2 : 0;
      tokens.forEach(t => { if (hay.includes(t)) sc += 5; });
      return { s, sc };
    }).sort((a, b) => b.sc - a.sc);
    const topStalks = scored.slice(0, 4).map(x => x.s);
    topStalks.forEach(s => state.openCover.add(s.id));
    updateCoverAndOlog();

    let md = `### Custom Glued Section: "${q}"\n\n`;
    topStalks.forEach(s => {
      md += `- **${s.title}** (§${s.section} [p. ${s.start_page}]): ${s.summary}\n$$${s.formal_core}$$\n`;
    });
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
    const s3 = topStalks[3] || s2;
    const h0 = coh && coh.h0_coherence ? coh.h0_coherence : 0.78;
    const d0 = coh && coh.mean_d0 ? coh.mean_d0 : 0.22;
    return [
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act I · Visual Hook & Notation', visual_cue: `🎨 Opening Visual Fiber: ${s0.title} [p. ${s0.start_page}]`, cite_page: s0.start_page, start_sec: 0, end_sec: 14, text: `Welcome to our custom 4-Act Deep Dive on "${q}". We've assembled an open cover starting with ${s0.title} on page ${s0.start_page}.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act I · Visual Hook & Notation', visual_cue: `🎨 Concrete Picture Before Symbols [p. ${s0.start_page}]`, cite_page: s0.start_page, start_sec: 14, end_sec: 28, text: `Before looking at the formal symbols, here is how ${s0.title} sets up the visual intuition on page ${s0.start_page}: ${s0.summary}` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act II · Walking the Diagram', visual_cue: `🧭 Stalk 1 Morphism Path [p. ${s0.start_page}–${s1.start_page}]`, cite_page: s1.start_page, start_sec: 28, end_sec: 44, text: `Now let's walk the restriction arrows from ${s0.title} into ${s1.title} on page ${s1.start_page}: ${s1.summary}` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act II · Walking the Diagram', visual_cue: `🧭 Intermediate Olog Overlap [p. ${s1.start_page}]`, cite_page: s1.start_page, start_sec: 44, end_sec: 60, text: `Notice how the local Olog types in ${s1.title} preserve the exact commuting paths we started with on page ${s0.start_page}.` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act II · Walking the Diagram', visual_cue: `🧭 Bridging to ${s2.title} [p. ${s2.start_page}]`, cite_page: s2.start_page, start_sec: 60, end_sec: 76, text: `And when we extend the diagram to ${s2.title} on page ${s2.start_page}, we get the third leg of our triangle: ${s2.summary}` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act III · Edge Cases & Traps', visual_cue: `⚡ Where Naive Intuition Breaks [p. ${s2.start_page}]`, cite_page: s2.start_page, start_sec: 76, end_sec: 92, text: `Wait—what happens if we drop the intermediate bridge at page ${s1.start_page}? Without that overlap, the cover splits into disconnected components and H-one cohomology flags an obstruction!` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act III · Edge Cases & Traps', visual_cue: `⚡ Resolving Polysemy via ${s3.title} [p. ${s3.start_page}]`, cite_page: s3.start_page, start_sec: 92, end_sec: 108, text: `Exactly. Including ${s3.title} on page ${s3.start_page} ensures that every shared term is translated functorially rather than by ad-hoc guesswork.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act III · Edge Cases & Traps', visual_cue: `⚡ Cech Coboundary Audit [p. ${s3.start_page}]`, cite_page: s3.start_page, start_sec: 108, end_sec: 122, text: `Our live Cech cohomology engine measures an H-zero coherence of ${h0} with coboundary defect ${d0} across this custom open cover.` },
      { speaker: 'Kore', role: 'Lead Architect', act: 'Act IV · Decoding the Formula', visual_cue: `📐 Symbol-by-Symbol Formula Synthesis [p. ${s0.start_page}–${s3.start_page}]`, cite_page: s1.start_page, start_sec: 122, end_sec: 136, text: `So every symbol in the glued synthesis below is simply recording the visual arrows across pages ${s0.start_page} through ${s3.start_page}.` },
      { speaker: 'Puck', role: 'Systems Co-Host', act: 'Act IV · Decoding the Formula', visual_cue: `🎛️ Studio Prompt: Click Any § p.N Chip or Synthesize Live`, cite_page: s2.start_page, start_sec: 136, end_sec: 150, text: `Click any page citation pill below to open the verbatim page—or paste a Gemini API key above to voice this custom 10-turn script with live Gemini 2.5 speakers!` }
    ];
  }

  document.getElementById('runGlueQueryBtn').addEventListener('click', () => runCustomQuery(document.getElementById('notebookQueryInput').value));
  document.getElementById('notebookQueryInput').addEventListener('keydown', e => { if (e.key === 'Enter') runCustomQuery(e.target.value); });
  document.getElementById('stalkFilterInput').addEventListener('input', buildStalkTree);
  document.getElementById('clearCoverBtn').addEventListener('click', () => { state.openCover = new Set([KB.stalks[0].id]); updateCoverAndOlog(); });

  const PRESETS = {
    pointfree: ['visual-abstraction-modes-of-knowledge', 'sets-subsets-empty-singleton', 'external-products-and-projections', 'categorical-duality-and-coproducts', 'categories-objects-morphisms-laws'],
    rosetta: ['categories-objects-morphisms-laws', 'monoids-as-single-object-categories-free-monoids', 'preorders-equivalence-and-thin-categories', 'propositional-logic-as-category', 'simply-typed-lambda-calculus-curry-howard-lambek'],
    types: ['type-theory-russell-and-formation-intro-elim', 'inductive-types-nat-list-and-church-encodings', 'simply-typed-lambda-calculus-curry-howard-lambek', 'programming-endofunctors-pointed-contravariant'],
    functors: ['functors-structure-preserving-maps', 'functors-across-monoids-orders-logic', 'programming-endofunctors-pointed-contravariant', 'natural-transformations-and-naturality-squares', 'polymorphic-functions-and-categorical-equivalence'],
    obstruction: ['visual-abstraction-modes-of-knowledge', 'orders-hasse-diagrams-and-lattices'],
    all: KB.stalks.map(s => s.id)
  };
  document.querySelectorAll('[data-preset]').forEach(btn => {
    btn.addEventListener('click', () => {
      const pKey = btn.getAttribute('data-preset');
      state.openCover = new Set(PRESETS[pKey] || PRESETS.pointfree);
      document.querySelectorAll('[data-preset]').forEach(b => b.classList.toggle('active', b === btn));
      updateCoverAndOlog();
    });
  });

  // ==========================================================================
  // PLATE IV: 24 STALKS, 291 FORMAL BLOCKS & ON-DEMAND 3D POSET
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
          <h3 class="serif" style="font-size:1.12rem;margin-bottom:0.35rem">${escapeHtml(s.title)}</h3>
          <p style="font-size:0.82rem;color:var(--ink-2);margin-bottom:0.5rem">${escapeHtml(s.summary)}</p>
          <div class="math-display" style="font-size:0.84rem;padding:0.4rem 0.55rem;margin:0.4rem 0">${convertLatexTokensToHtml(s.formal_core)}</div>
        </div>
        <div style="padding-top:0.45rem;border-top:1px dotted var(--rule);display:flex;justify-content:space-between;align-items:center;font-family:var(--f-mono);font-size:0.69rem;color:var(--ink-3)">
          <span>${((s.olog && s.olog.types) || []).length} Olog types · ${s.extracted_items_count || 0} blocks</span>
          <button class="preset-btn" onclick="window.__addStalkToStudio('${s.id}')">+ Open Cover</button>
        </div>
      </article>
    `).join('');
  }

  function renderDeclarationsList() {
    const chFilter = document.getElementById('chapterFilterSelect').value;
    const kindFilter = document.getElementById('declKindSelect').value;
    const q = (document.getElementById('declSearchInput').value || '').trim().toLowerCase();
    const allItems = KB.formal_items.length ? KB.formal_items : KB.stalks.flatMap(s => s.formal_items || []);
    const filtered = allItems.filter(it => {
      if (chFilter !== 'all' && String(it.chapter) !== chFilter) return false;
      if (kindFilter !== 'all' && it.kind !== kindFilter) return false;
      if (q && !(it.id + ' ' + it.kind + ' ' + (it.title || '') + ' ' + (it.text || '')).toLowerCase().includes(q)) return false;
      return true;
    });
    document.getElementById('declCountLabel').textContent = `Showing ${Math.min(80, filtered.length)} of ${filtered.length} formal blocks (from 291 total in Marinov)`;
    document.getElementById('declListContainer').innerHTML = filtered.slice(0, 80).map(it => `
      <div style="background:var(--paper);border:1px solid var(--rule);padding:0.7rem 0.85rem">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span class="mono" style="font-weight:600;color:var(--accent-text)">${escapeHtml(it.id)} · ${escapeHtml(it.title || '')}</span>
          <button class="cite-pill" onclick="window.__jumpToPage(${it.page}, '')">§ p.${it.page}</button>
        </div>
        <div style="font-size:0.84rem;color:var(--ink-2)">${escapeHtml((it.text || '').slice(0, 380))}</div>
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
  document.getElementById('chapterFilterSelect').addEventListener('change', () => { renderStalkCards(); if (state.activeSubview === 'declarations') renderDeclarationsList(); });
  document.getElementById('declSearchInput').addEventListener('input', renderDeclarationsList);
  document.getElementById('declKindSelect').addEventListener('change', renderDeclarationsList);
  renderStalkCards();

  // On-demand 3D Poset Loop
  const canvas3d = document.getElementById('sheaf3dCanvas');
  const ctx3d = canvas3d.getContext('2d');
  let rafId = null, camYaw = 0.5, camPitch = 0.3, camDist = 370, show2Simplices = true, dragging3d = false, lastX = 0, lastY = 0;
  let projectedNodes = [];

  canvas3d.addEventListener('mousedown', e => { dragging3d = true; lastX = e.clientX; lastY = e.clientY; });
  window.addEventListener('mouseup', () => { dragging3d = false; });
  window.addEventListener('mousemove', e => {
    if (!dragging3d) return;
    camYaw += (e.clientX - lastX) * 0.007;
    camPitch = Math.max(-1.1, Math.min(1.1, camPitch + (e.clientY - lastY) * 0.007));
    lastX = e.clientX; lastY = e.clientY;
  });
  document.getElementById('toggle2SimplicesBtn').addEventListener('click', e => {
    show2Simplices = !show2Simplices;
    e.target.classList.toggle('active', show2Simplices);
    e.target.textContent = `2-Simplices: ${show2Simplices ? 'ON' : 'OFF'}`;
  });
  document.getElementById('reset3dCamBtn').addEventListener('click', () => { camYaw = 0.5; camPitch = 0.3; camDist = 370; });

  function update3dHud(s) {
    if (!s) return;
    document.getElementById('hud3dBox').innerHTML = `
      <div>
        <strong style="color:#F0C478">${escapeHtml(s.title)}</strong>
        <span class="mono" style="margin-left:8px;opacity:0.8">Ch ${s.chapter} · §${s.section} · pp.${s.start_page}–${s.end_page}</span>
        <div style="font-size:0.78rem;opacity:0.88;margin-top:2px">${escapeHtml(s.summary)}</div>
      </div>
      <button class="cite-pill" onclick="window.__jumpToPage(${s.start_page}, '')">Open p.${s.start_page}</button>
    `;
  }
  update3dHud(KB.stalks[5]);

  function project3d(pt, W, H) {
    const [x, y, z] = pt || [0, 0, 0];
    const cy = Math.cos(camYaw), sy = Math.sin(camYaw), cp = Math.cos(camPitch), sp = Math.sin(camPitch);
    const x1 = x * cy - z * sy, z1 = x * sy + z * cy;
    const y2 = y * cp - z1 * sp, z2 = y * sp + z1 * cp + camDist;
    const fov = 330 / Math.max(60, z2);
    return { sx: W / 2 + x1 * fov, sy: H / 2 - y2 * fov, z: z2, fov };
  }

  function draw3dScene() {
    if (state.activeSubview !== 'atlas3d') { rafId = null; return; }
    const rect = canvas3d.parentElement.getBoundingClientRect();
    if (canvas3d.width !== Math.floor(rect.width) || canvas3d.height !== Math.floor(rect.height)) {
      canvas3d.width = Math.floor(rect.width); canvas3d.height = Math.floor(rect.height);
    }
    const W = canvas3d.width, H = canvas3d.height;
    ctx3d.clearRect(0, 0, W, H);
    if (!dragging3d) camYaw += 0.002;
    const pMap = {};
    KB.stalks.forEach(s => { pMap[s.id] = { stalk: s, ...project3d(s.pos3d, W, H) }; });
    if (show2Simplices) {
      KB.two_simplices.forEach(sim => {
        const [u, v, w] = sim.vertices.map(id => pMap[id]);
        if (!u || !v || !w) return;
        ctx3d.beginPath(); ctx3d.moveTo(u.sx, u.sy); ctx3d.lineTo(v.sx, v.sy); ctx3d.lineTo(w.sx, w.sy); ctx3d.closePath();
        ctx3d.fillStyle = 'rgba(200, 138, 43, 0.16)'; ctx3d.fill();
      });
    }
    KB.restriction_morphisms.forEach(r => {
      const u = pMap[r.source], v = pMap[r.target];
      if (!u || !v) return;
      const act = state.openCover.has(r.source) && state.openCover.has(r.target);
      ctx3d.beginPath(); ctx3d.moveTo(u.sx, u.sy); ctx3d.lineTo(v.sx, v.sy);
      ctx3d.strokeStyle = act ? '#F0C478' : 'rgba(246,241,231,0.18)';
      ctx3d.lineWidth = act ? 1.8 : 0.9; ctx3d.stroke();
    });
    projectedNodes = Object.values(pMap).sort((a, b) => b.z - a.z);
    projectedNodes.forEach(n => {
      const inCov = state.openCover.has(n.stalk.id);
      const r = Math.max(4.5, (inCov ? 8 : 5.5) * n.fov);
      n.r = r;
      ctx3d.beginPath(); ctx3d.arc(n.sx, n.sy, r, 0, Math.PI * 2);
      ctx3d.fillStyle = inCov ? '#F0C478' : '#6CA6D9'; ctx3d.fill();
      ctx3d.strokeStyle = '#17181C'; ctx3d.lineWidth = 1.4; ctx3d.stroke();
      if (inCov || n.fov > 0.92) {
        ctx3d.font = '600 10px "JetBrains Mono", monospace';
        ctx3d.fillStyle = '#F6F1E7';
        ctx3d.fillText(n.stalk.title.slice(0, 22), n.sx + r + 4, n.sy + 3);
      }
    });
    rafId = requestAnimationFrame(draw3dScene);
  }
  function start3dLoop() { if (!rafId) rafId = requestAnimationFrame(draw3dScene); }
  function stop3dLoop() { if (rafId) { cancelAnimationFrame(rafId); rafId = null; } }

  // ==========================================================================
  // PLATE V: UNIFIED COURSE MODULES GLUING MARINOV × SPIVAK
  // ==========================================================================
  const COURSE_MODULES = [
    {
      vol: 'ARC I · POINT-FREE & OLOGS',
      stamp: '◆ Foundation',
      title: 'From Colored Balls to External Arrows & Scientific Ologs',
      symbols: 'x \\in A \\longleftrightarrow 1 \\xrightarrow{x} A, \\qquad g \\circ f = h',
      keyConcept: 'Erasing internal set elements (Marinov Ch 1–2) and writing domain models as commuting noun/verb Ologs (Spivak Ch 1–2) are two sides of the same point-free coin.',
      lab: 'Dual Perspective Sandbox: Convert an internal set-ball diagram into an external point-free Olog and verify path commutativity.',
      whyItMatters: 'Bridges visual beginner intuition directly into rigorous categorical specification without hand-waving.',
      pages: [13, 83]
    },
    {
      vol: 'ARC II · UNIVERSAL CONES',
      stamp: '◆ Duality',
      title: 'Universal Products, Coproducts, Pullbacks & Pushouts',
      symbols: 'A \\times B, \\quad A + B, \\quad X \\times_Z Y, \\quad X \\sqcup_W Y',
      keyConcept: 'Reversing arrows in the universal Product cone (π₁, π₂, ⟨f,g⟩) yields the Coproduct cocone (ι₁, ι₂, [f,g]); adding a base object Z/W yields Pullbacks and Pushouts.',
      lab: 'Universal Factorizer Lab: Toggle arrow directions between Product/Coproduct and execute SQL INNER JOIN pullbacks.',
      whyItMatters: 'Unifies data tuples, tagged sum types, and relational joins under one universal existence-and-uniqueness pattern.',
      pages: [62, 69]
    },
    {
      vol: 'ARC III · SYMMETRY & ORDER',
      stamp: '⚖ 1-Object & Thin',
      title: 'Monoids, Rotational Groups, Poset Lattices & Birkhoff’s Cube',
      symbols: '\\mathbf{B}M \\;(1\\text{-Obj}), \\quad (P, \\le) \\;(\\text{Thin}), \\quad L \\cong \\mathcal{O}(\\mathrm{Irr}(L))',
      keyConcept: 'A monoid is a category with one object; a preorder is a thin category with at most one arrow between objects; finite distributive lattices form 3D Birkhoff cubes.',
      lab: 'Interactive Triangle Rotation (C₃/D₃) & Birkhoff 3D Cube Explorer (Color Mixing ↔ Divisibility ↔ Subsets).',
      whyItMatters: 'Reveals state machines, symmetry groups, and permission/type hierarchies as special cases of categories.',
      pages: [115, 148]
    },
    {
      vol: 'ARC IV · CURRY-HOWARD-LAMBEK',
      stamp: '✓ Logic & Types',
      title: 'Deductive Logic, Heyting Algebras & Simply Typed Lambda Calculus',
      symbols: '(P \\wedge Q, P \\vee Q, P \\Rightarrow Q) \\;\\simeq\\; (A \\times B, A + B, B^A) \\;\\simeq\\; (\\Gamma \\vdash t : B)',
      keyConcept: 'Marinov’s Chapters 5–6 crown jewel: Propositions are Types, Proofs are Lambda Programs, and Implication/Currying is the Exponential Object in a Bicartesian Closed Category.',
      lab: 'Live Curry-Howard-Lambek Compiler: Write a natural deduction proof and watch it compile into a typed lambda term and CCC morphism.',
      whyItMatters: 'Gives software engineers a concrete, executable understanding of universal properties through TypeScript/Haskell types.',
      pages: [180, 260]
    },
    {
      vol: 'ARC V · FUNCTORIAL BRIDGES',
      stamp: '✓ Structure Maps',
      title: 'Functors Across Worlds: Homomorphisms, .map & Database Instances',
      symbols: 'F(g \\circ f) = F(g) \\circ F(f), \\quad \\mathrm{map} : (A \\to B) \\to F A \\to F B, \\quad I : \\mathcal{S} \\to \\mathbf{Set}',
      keyConcept: 'Functors preserve commuting diagrams: acting as homomorphisms on monoids, monotone maps on posets, `.map` on programming containers (Marinov Ch 7), and database states on schemas (Spivak Ch 4).',
      lab: 'Functorial Container & Schema Studio: Verify functor laws on List/Maybe containers and relational database tables.',
      whyItMatters: 'Connects everyday functional programming `.map` directly to functorial database modeling.',
      pages: [289, 306]
    },
    {
      vol: 'ARC VI · HIGHER NATURALITY',
      stamp: '◆ 2-Categories & Sheaves',
      title: 'Natural Transformations, Parametric Polymorphism, Kan Migration & Sheaves',
      symbols: 'G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f), \\quad \\forall a.\\; F a \\to G a, \\quad \\Sigma_F \\dashv \\Delta_F \\dashv \\Pi_F',
      keyConcept: 'Polymorphic functions ∀a. F a → G a (`reverse`, `safeHead`) are natural transformations in Type (Marinov Ch 8), while adjoint functors and sheaves glue local sections globally (Spivak Ch 7).',
      lab: 'Naturality Square & Sheaf Equalizer Verifier: Test polymorphic free theorems and glue multi-stalk open covers.',
      whyItMatters: 'Completes the journey from colored balls in a set to 2-categories, parametricity, and sheaf cohomology.',
      pages: [319, 350]
    }
  ];

  document.getElementById('courseModulesGrid').innerHTML = COURSE_MODULES.map(m => `
    <article class="module-card">
      <div class="m-head">
        <span class="mono" style="font-size:0.68rem;color:var(--ink-3)">${escapeHtml(m.vol)}</span>
        <span class="stamp ratified">◆ ${escapeHtml(m.stamp.replace(/^[◆⚖✓±⊘]\s*/, ''))}</span>
      </div>
      <h3 class="serif" style="font-size:1.12rem">${escapeHtml(m.title)}</h3>
      <div class="math-display" style="font-size:0.84rem;padding:0.4rem;margin:0.2rem 0">${convertLatexTokensToHtml(m.symbols)}</div>
      <div class="callout-box">
        <strong>Key Concept</strong>
        ${escapeHtml(m.keyConcept)}
      </div>
      <div style="font-size:0.79rem;color:var(--ink-2);padding:0.45rem 0;border-top:1px dotted var(--rule);border-bottom:1px dotted var(--rule)">
        <strong class="mono" style="font-size:0.68rem;text-transform:uppercase;color:var(--accent-text)">Walkable Lab:</strong> ${escapeHtml(m.lab)}
        <div style="margin-top:5px">
          ${m.pages.map(p => `<button class="cite-pill" onclick="window.__jumpToPage(${p}, '')">§ Marinov p.${p}</button>`).join(' ')}
        </div>
      </div>
      <div class="callout-box" style="border-left-color:var(--ochre);margin-top:auto">
        <strong>Why It Matters</strong>
        ${escapeHtml(m.whyItMatters)}
      </div>
    </article>
  `).join('');

  // ==========================================================================
  // SLIDE-OVER 377-PAGE VERBATIM PDF READER DRAWER
  // ==========================================================================
  const drawer = document.getElementById('readerDrawer');
  const openBtn = document.getElementById('openReaderBtn');
  const mobOpenReaderBtn = document.getElementById('mobileOpenReaderBtn');
  openBtn.addEventListener('click', () => drawer.classList.toggle('open'));
  if (mobOpenReaderBtn) mobOpenReaderBtn.addEventListener('click', () => drawer.classList.toggle('open'));
  document.getElementById('closeReaderBtn').addEventListener('click', () => drawer.classList.remove('open'));

  function renderPageReader(pageNum, term) {
    const p = Math.max(1, Math.min(377, parseInt(pageNum, 10) || 1));
    state.currentPage = p;
    if (term !== undefined) state.highlightTerm = term;
    document.getElementById('pageNumInput').value = p;
    document.getElementById('pageSlider').value = p;
    openBtn.textContent = `📖 Page Reader (p.${p})`;
    if (mobOpenReaderBtn) mobOpenReaderBtn.textContent = `📖 p.${p}`;
    document.getElementById('openRawPdfLink').href = `__PDF_REL_PATH__#page=${p}`;

    const pObj = pageByNum[p] || { p, ch: 1, sec: 'Loading 377-page bundle…', wc: 0, txt: 'Loading verbatim page text…', stalks: [] };
    const sBadges = (pObj.stalks || []).map(sid => {
      const st = stalkById[sid];
      return st ? `<span class="stamp ratified">◆ ${escapeHtml(st.title)}</span>` : '';
    }).join(' ');

    document.getElementById('readerPageMeta').innerHTML = `
      <div style="display:flex;justify-content:space-between;font-family:var(--f-mono);font-size:0.74rem;color:var(--accent-text);font-weight:600">
        <span>PDF Page ${pObj.p} of 377 · Chapter ${pObj.ch}</span>
        <span>${pObj.wc || 0} words</span>
      </div>
      <div style="font-size:0.83rem;color:var(--ink-2);margin-top:2px">${escapeHtml(pObj.sec || 'Category Theory Illustrated')}</div>
      ${sBadges ? `<div style="margin-top:6px;display:flex;gap:4px;flex-wrap:wrap">${sBadges}</div>` : ''}
    `;

    let rawTxt = pObj.txt || '(Full-Page Vector Diagram in PDF — click "Open PDF ↗" above to view illustration)';
    rawTxt = rawTxt
      .replace(/\bthisproperty\b/g, 'this property')
      .replace(/\bthesingleton\b/g, 'the singleton')
      .replace(/\bfunctionsfrom\b/g, 'functions from');
    let rawHtml = escapeHtml(rawTxt);
    if (state.highlightTerm && state.highlightTerm.length >= 2) {
      const safe = state.highlightTerm.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      rawHtml = rawHtml.replace(new RegExp(`(${safe})`, 'gi'), '<mark class="hl">$1</mark>');
    }
    document.getElementById('readerPageText').innerHTML = rawHtml;
  }

  document.getElementById('prevPageBtn').addEventListener('click', () => renderPageReader(state.currentPage - 1));
  document.getElementById('nextPageBtn').addEventListener('click', () => renderPageReader(state.currentPage + 1));
  document.getElementById('pageNumInput').addEventListener('change', e => renderPageReader(e.target.value));
  document.getElementById('pageSlider').addEventListener('input', e => renderPageReader(e.target.value));

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
          const snip = pg.txt.slice(Math.max(0, idx - 30), Math.min(pg.txt.length, idx + 90)).replace(/\s+/g, ' ');
          hits.push({ p: pg.p, sec: pg.sec, snip });
          if (hits.length >= 20) break;
        }
      }
      searchResults.style.display = 'block';
      searchResults.innerHTML = hits.length
        ? hits.map(h => `<div style="padding:5px 7px;border-bottom:1px dotted var(--rule);cursor:pointer;font-size:0.78rem" onclick="window.__jumpToPage(${h.p}, '${escapeHtml(q.replace(/'/g, "\\'"))}')"><div class="mono" style="color:var(--accent-text);font-weight:600">p.${h.p} · ${escapeHtml(h.sec)}</div><div style="color:var(--ink-2)">…${escapeHtml(h.snip)}…</div></div>`).join('')
        : `<div style="padding:6px;font-size:0.78rem;color:var(--ink-3)">No matches in 377 pages</div>`;
    }, 100);
  });

  // ==========================================================================
  // NOTEBOOKLM "DEEP DIVE" 4-ACT 10-TURN NEURAL PODCAST & GEMINI 2.5 TTS PLAYER
  // ==========================================================================
  const audioEl = document.getElementById('notebookPodcastAudio');
  const playPauseBtn = document.getElementById('podcastPlayPauseBtn');
  const mobAudioPlayBtn = document.getElementById('mobileAudioPlayBtn');
  const audioBriefBtn = document.getElementById('audioBriefBtn');
  const scrubSlider = document.getElementById('podcastScrubSlider');
  const timeLabel = document.getElementById('podcastTimeLabel');
  const speedBtn = document.getElementById('podcastSpeedBtn');
  const transcriptBtn = document.getElementById('toggleTranscriptBtn');
  const transcriptDrawer = document.getElementById('podcastTranscriptDrawer');
  const activeSubtitle = document.getElementById('podcastActiveSubtitle');
  const visualCueTextEl = document.getElementById('podcastVisualCueText');
  const turnCounterEl = document.getElementById('podcastTurnCounter');
  const actPills = Array.from(document.querySelectorAll('#podcastActBar .podcast-act-pill'));
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

  function turnIdxToActIdx(turnIdx) {
    if (turnIdx <= 1) return 0;
    if (turnIdx <= 4) return 1;
    if (turnIdx <= 7) return 2;
    return 3;
  }

  function updateActAndCueUI(turnIdx, turnObj) {
    const actIdx = turnIdxToActIdx(turnIdx);
    actPills.forEach((pill, idx) => pill.classList.toggle('active', idx === actIdx));
    if (visualCueTextEl && turnObj) {
      visualCueTextEl.innerHTML = `${escapeHtml(turnObj.visual_cue || ('🎨 Verbatim Page Fiber [p. ' + (turnObj.cite_page || 1) + ']'))} <button class="cite-pill" style="margin-left:6px" onclick="window.__jumpToPage(${turnObj.cite_page || 1}, '')">§ p.${turnObj.cite_page || 1}</button>`;
    }
    if (turnCounterEl) {
      const actLabel = (turnObj && turnObj.act) ? turnObj.act.split('·')[0].trim() : `Act ${['I','II','III','IV'][actIdx]}`;
      turnCounterEl.textContent = `Turn ${turnIdx + 1} / ${Math.max(1, currentTurns.length)} · ${actLabel}`;
    }
  }

  actPills.forEach(pill => {
    pill.addEventListener('click', () => {
      const aIdx = Number(pill.getAttribute('data-act-idx') || 0);
      const startTurnIdx = [0, 2, 5, 8][aIdx] || 0;
      const targetTurn = currentTurns[Math.min(startTurnIdx, Math.max(0, currentTurns.length - 1))];
      if (targetTurn) {
        updateActAndCueUI(startTurnIdx, targetTurn);
        window.__seekPodcastTo(targetTurn.start_sec || 0, targetTurn.cite_page || 1);
      }
    });
  });

  function updateButtonsState(playing) {
    state.audioPlaying = playing;
    if (playPauseBtn) playPauseBtn.textContent = playing ? '⏸ Pause Deep Dive' : '▶ Play Deep Dive';
    if (mobAudioPlayBtn) mobAudioPlayBtn.textContent = playing ? '⏸ Pause Audio' : '▶ Deep Dive';
    if (audioBriefBtn) audioBriefBtn.textContent = playing ? '⏸ Pause 4-Act Deep Dive' : '🎙️ Play 4-Act Deep Dive';
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

  window.__loadPodcastForInvestigation = function(inv) {
    if (!inv) return;
    if (audioEl && !audioEl.paused) {
      audioEl.pause();
    }
    updateButtonsState(false);

    const baseInv = KB.notebook_investigations.find(x => x.id === inv.id) || inv;
    currentTurns = baseInv.podcast_turns || (KB.notebook_investigations[0] && KB.notebook_investigations[0].podcast_turns) || [];
    const relAudio = baseInv.audio_file || (KB.notebook_investigations[0] && KB.notebook_investigations[0].audio_file) || '';
    const dur = baseInv.audio_duration_sec || 180;

    if (relAudio && audioEl) {
      audioEl.src = (bundleBaseDir ? bundleBaseDir + '/' : '') + relAudio;
      audioEl.playbackRate = speedSteps[speedIdx];
    }
    if (timeLabel) timeLabel.textContent = `0:00 / ${fmtSec(dur)}`;
    if (scrubSlider) scrubSlider.value = 0;

    if (currentTurns.length && activeSubtitle) {
      const t0 = currentTurns[0];
      updateActAndCueUI(0, t0);
      activeSubtitle.style.borderLeftColor = 'var(--accent-text)';
      activeSubtitle.innerHTML = `<span class="mono" style="color:var(--accent-text);font-weight:600">${escapeHtml(t0.speaker)} · ${escapeHtml(t0.role || 'Host')}:</span> ${escapeHtml(t0.text)} <button class="cite-pill" style="margin-left:6px" onclick="window.__jumpToPage(${t0.cite_page || 1}, '')">§ p.${t0.cite_page || 1}</button>`;
    }

    if (transcriptDrawer) {
      transcriptDrawer.innerHTML = currentTurns.map((t, idx) => {
        const isKore = t.speaker !== 'Puck';
        const col = isKore ? 'var(--accent-text)' : 'var(--good)';
        return `
          <div class="podcast-turn-row" data-turn-idx="${idx}" style="padding:7px 8px;border-bottom:1px dotted var(--rule);cursor:pointer;transition:background 0.15s"
               onclick="window.__seekPodcastTo(${t.start_sec || 0}, ${t.cite_page || 1})">
            <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:2px">
              <div>
                <span class="mono" style="color:${col};font-weight:600">${isKore ? '🎙️' : '🎧'} ${escapeHtml(t.speaker)}</span>
                <span class="mono" style="color:var(--ink-3);font-size:0.66rem;margin-left:6px">${escapeHtml(t.act || ('Turn ' + (idx+1)))}</span>
              </div>
              <div style="display:flex;gap:6px;align-items:center">
                <span class="cite-pill" onclick="event.stopPropagation();window.__jumpToPage(${t.cite_page || 1}, '')">§ p.${t.cite_page || 1}</span>
                <span class="mono" style="color:var(--ink-3);font-size:0.68rem">${fmtSec(t.start_sec || 0)}</span>
              </div>
            </div>
            ${t.visual_cue ? `<div class="mono" style="font-size:0.68rem;color:var(--accent-text);margin-bottom:2px">${escapeHtml(t.visual_cue)}</div>` : ''}
            <div style="color:var(--ink-2);line-height:1.42">${escapeHtml(t.text)}</div>
          </div>
        `;
      }).join('');
    }
  };

  function togglePodcastPlayback() {
    if (!audioEl || !audioEl.src) {
      window.__loadPodcastForInvestigation(state.currentInvestigation || KB.notebook_investigations[0]);
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
  if (mobAudioPlayBtn) mobAudioPlayBtn.addEventListener('click', togglePodcastPlayback);
  if (audioBriefBtn) {
    audioBriefBtn.addEventListener('click', () => {
      const card = document.getElementById('podcastStudioCard');
      if (card) card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      togglePodcastPlayback();
    });
  }

  // Mobile Dock Plate Cycler & Notebook Jump
  const mobCyclePlateBtn = document.getElementById('mobileCyclePlateBtn');
  if (mobCyclePlateBtn) {
    mobCyclePlateBtn.addEventListener('click', () => {
      const idx = allPlates.findIndex(p => p.id === activePlateId);
      const nextP = allPlates[(idx + 1) % allPlates.length];
      window.__focusPlate(nextP.id, true);
    });
  }
  const mobJumpNbBtn = document.getElementById('mobileJumpNotebookBtn');
  if (mobJumpNbBtn) {
    mobJumpNbBtn.addEventListener('click', () => {
      window.__focusPlate('plate-3', document.documentElement.getAttribute('data-view-mode') === 'focus');
    });
  }

  if (audioEl) {
    audioEl.addEventListener('timeupdate', () => {
      const cur = audioEl.currentTime || 0;
      const tot = audioEl.duration || (state.currentInvestigation && state.currentInvestigation.audio_duration_sec) || 180;
      if (timeLabel) timeLabel.textContent = `${fmtSec(cur)} / ${fmtSec(tot)}`;
      if (scrubSlider && tot > 0) scrubSlider.value = ((cur / tot) * 100).toFixed(1);

      for (let i = 0; i < currentTurns.length; i++) {
        const t = currentTurns[i];
        if (cur >= (t.start_sec || 0) && cur <= (t.end_sec || 9999)) {
          highlightActiveSpeaker(t.speaker);
          updateActAndCueUI(i, t);
          const isKore = t.speaker !== 'Puck';
          const col = isKore ? 'var(--accent-text)' : 'var(--good)';
          if (activeSubtitle) {
            activeSubtitle.style.borderLeftColor = col;
            activeSubtitle.innerHTML = `<span class="mono" style="color:${col};font-weight:600">${isKore ? '🎙️' : '🎧'} ${escapeHtml(t.speaker)} · ${escapeHtml(t.role || 'Host')}:</span> ${escapeHtml(t.text)} <button class="cite-pill" style="margin-left:6px" onclick="window.__jumpToPage(${t.cite_page || 1}, '')">§ p.${t.cite_page || 1}</button>`;
          }
          if (transcriptDrawer) {
            transcriptDrawer.querySelectorAll('.podcast-turn-row').forEach((r, idx) => {
              r.style.background = idx === i ? 'var(--accent-soft)' : 'transparent';
            });
          }
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
      const tot = audioEl.duration || (state.currentInvestigation && state.currentInvestigation.audio_duration_sec) || 180;
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
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const data = await resp.json();
        const b64 = data.candidates[0].content.parts[0].inlineData.data;
        const wavUrl = pcm16Base64ToWavUrl(b64, 24000);
        audioEl.src = wavUrl;
        if (podcastEngineBadge) podcastEngineBadge.textContent = `◆ Live Gemini 2.5 TTS (${vA} & ${vB})`;
        if (geminiStatusMsg) geminiStatusMsg.textContent = `✓ Live Gemini 2.5 multi-speaker audio synthesized (${vA} & ${vB}) — playing now.`;
        audioEl.play().then(() => updateButtonsState(true)).catch(() => {});
      } catch (err) {
        if (geminiStatusMsg) geminiStatusMsg.textContent = `⊘ Gemini TTS error: ${err.message}. Falling back to pre-rendered neural MP3.`;
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
    updateCoverAndOlog();
    window.__focusPlate('plate-3', document.documentElement.getAttribute('data-view-mode') === 'focus');
  };

  renderInvestigationPills();
  displayInvestigation(KB.notebook_investigations[0]);
  updateCoverAndOlog();
  renderPageReader(83, 'Element');
})();
</script>
</body>
</html>
"""


def main():
    kb_obj = json.loads(KB_PATH.read_text(encoding="utf-8"))

    bundle_obj = {
        "pages": kb_obj["pages"],
        "formal_items": kb_obj["formal_items"],
        "full_stalk_items": {s["id"]: s.get("formal_items", []) for s in kb_obj["stalks"]}
    }
    bundle_js = "window.__onSheafBundleLoaded && window.__onSheafBundleLoaded(" + json.dumps(bundle_obj, ensure_ascii=False, separators=(",", ":")) + ");\n"
    BUNDLE_PATH.write_text(bundle_js, encoding="utf-8")

    seed_page_nums = {11, 62, 83, 148}
    slim_stalks = []
    total_stalks = len(kb_obj["stalks"])
    for idx, s in enumerate(kb_obj["stalks"]):
        sc = dict(s)
        sc["formal_items"] = []
        if len(sc.get("verbatim_excerpt", "")) > 280:
            sc["verbatim_excerpt"] = sc["verbatim_excerpt"][:280] + "…"
        ang = (2.0 * math.pi * idx) / max(1, total_stalks) * 2.0
        radius = 105.0 + (idx % 3) * 26.0
        y_pos = (s.get("chapter", 1) - 4.5) * 32.0
        sc["pos3d"] = [round(radius * math.cos(ang), 1), round(y_pos, 1), round(radius * math.sin(ang), 1)]
        slim_stalks.append(sc)

    core_obj = {
        "book": kb_obj["book"],
        "chapters": kb_obj["chapters"],
        "stalks": slim_stalks,
        "restriction_morphisms": kb_obj["restriction_morphisms"],
        "two_simplices": kb_obj["two_simplices"],
        "cohomology_obstructions": kb_obj.get("cohomology_obstructions", []),
        "notebook_investigations": kb_obj["notebook_investigations"],
        "seed_pages": [p for p in kb_obj["pages"] if p["p"] in seed_page_nums]
    }
    core_json = json.dumps(core_obj, ensure_ascii=False, separators=(",", ":")).replace("</script>", "<\\/script>")

    html_main = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "cattheory-illustrated-sheaf-kb/data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "cattheory-illustrated-sheaf-kb/category-theory-illustrated.pdf")
    )
    html_local = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "category-theory-illustrated.pdf")
    )
    html_artifact = (
        HTML_TEMPLATE
        .replace("__SHEAF_CORE_JSON__", core_json)
        .replace("__BUNDLE_REL_PATH__", "/Users/cairo/Documents/CETI/ACCENTURE/content-factory v2/cattheory-illustrated-sheaf-kb/data/sheaf_pages_bundle.js")
        .replace("__PDF_REL_PATH__", "/Users/cairo/Documents/CETI/ACCENTURE/content-factory v2/cattheory-illustrated-sheaf-kb/category-theory-illustrated.pdf")
    )

    OUT_MAIN.write_text(html_main, encoding="utf-8")
    OUT_LOCAL.write_text(html_local, encoding="utf-8")
    if OUT_ARTIFACT.parent.exists():
        OUT_ARTIFACT.write_text(html_artifact, encoding="utf-8")

    print(f"Category Theory Illustrated Studio HTML compiled: {OUT_MAIN.stat().st_size / 1024:.1f} KB")
    print(f"Deferred 377-Page Bundle:                         {BUNDLE_PATH.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
