# Mathematical & Symbolic Rendering Specification (`sheaf-field-manual-studio`)

This specification governs how all mathematical notation, categorical diagrams, code blocks, and page citations are rendered inside a **CETI Field-Manual & Sheaf Notebook Studio** HTML volume.

---

## 1. Zero Raw LaTeX Leakage Law (`HF-STUDIO-03`)

**Hard Invariant:** No visible DOM text node or rendered synthesis card may ever display raw unparsed LaTeX control sequences (`\mathcal`, `\mathbf`, `\mathrm`, `\text`, `\operatorname`, `\varprojlim`, `\varinjlim`, `\xrightarrow`, `\xleftarrow`, `\dashv`, `\simeq`, `\cong`, `\times_`, `\sqcup_`, `\rightrightarrows`, `$$`, or `$`).

### Required 7-Stage Parsing Pipeline (`renderRichMarkdown` + `convertLatexTokensToHtml`)
1. **Display Math Extraction (`$$...$$`):** Extract all `$$...$$` blocks into indexed placeholders `@@MATH_BLOCK_i@@` *before* markdown line splitting or HTML escaping, and convert each into `<div class="math-display">...</div>`.
2. **Inline Math Extraction (`$...$`):** Extract all `$...$` inline spans into indexed placeholders `@@MATH_INLINE_i@@` and convert each into `<span class="math-expr">...</span>`.
3. **Math-Aware Code Spans (`` `...` ``):** When a markdown backtick span contains LaTeX macros (e.g., `` `\mathcal{O}(U)` `` or `` `f : X \to Y` ``), automatically route it through `convertLatexTokensToHtml()` into `<span class="math-expr">...</span>` instead of leaving raw backslashes inside `<code>`.
4. **Font & Category Macros:**
   - `\mathcal{O}` $\to$ `<span class="m-cal">O</span>` (Fraunces italic copper serif)
   - `\mathbf{Set}` $\to$ `<span class="m-cat">Set</span>` (bold sans categorical font)
   - `\text{Open}`, `\mathrm{Hom}` $\to$ `<span class="m-op">Open</span>` (monospace operator)
5. **Stacked Arrows & Limits:**
   - `\xrightarrow{f}` $\to$ `<span class="m-arrow"><span class="m-arrow-label">f</span><span class="m-arrow-body">&rarr;</span></span>`
   - `\varprojlim_{J}` $\to$ `<span class="m-lim"><span class="m-lim-top">lim&larr;</span><span class="m-lim-sub">J</span></span>`
   - `\varinjlim_{J}` $\to$ `<span class="m-lim"><span class="m-lim-top">colim&rarr;</span><span class="m-lim-sub">J</span></span>`
6. **Recursive Subscripts & Superscripts:** Parse nested `_{...}` and `^{...}` (up to 3 passes) plus single-token `_x` and `^op` into semantic `<sub>` and `<sup>` tags.
7. **Interactive Page Citation Pills (`[p. 520]`):** Convert every `[p. N]` or `[p. N, Def X.Y]` reference into an interactive `<button class="cite-pill" onclick="window.__jumpToPage(N, '')">§ p.N</button>` that opens the slide-over verbatim book reader to page `N`.

---

## 2. Fast-Load Split Bundle Architecture (`HF-STUDIO-02`)

Embedding 600+ verbatim pages directly inside the main `.html` file adds `1.5–2.5 MB` of synchronous parse weight and delays first paint. Every studio build MUST split:
1. **Core Studio HTML (`< 450 KB`):** Contains the CSS tokens, the 5 Plates, the 30 Concept Stalk metadata & local Ologs, the 52 restriction morphisms, the curated investigations, and ~25 seed pages for instant `< 20ms` first paint.
2. **Deferred Page & Declaration Bundle (`data/sheaf_pages_bundle.js` loaded via `<script defer>`):** Asynchronously hydrates all `1..P` verbatim pages and all `800+` formal declarations via `window.__onSheafBundleLoaded(bundle)` with zero CORS issues on both `file://` and `http://`.
3. **On-Demand 3D WebGL/Canvas Loop:** The 3D Alexandrov Poset `requestAnimationFrame` loop runs **only** when the 3D Atlas subview is active (`0%` idle CPU on all other plates).

---

## 3. Five-Plate Editorial Architecture (`HF-STUDIO-04..08`)

Every Field-Manual Studio must include:
- **Sticky Axis Ribbon & Field Controls:** `Depth (Newcomer | Practitioner | Expert)`, `Paper (Cream #F5EFE3 | Ink #1A1612)`, and `📖 Page Reader` drawer toggle.
- **Frontispiece:** Title with one italic `.u-copper` noun, hand-crafted SVG sheaf equalizer figure, provenance meta-block (`Primary Corpus`, `Indexed Topology`, `Extracted Items`, `Query Engine`, `Course Target`), and Table of Plates.
- **Plate I (`technology`) — Query & Sheaf Gluing Architecture:** Interactive 5-stage pipeline rail explaining SQLite FTS5 + Alexandrov Open-Cover Gluing + CLI/Gemini/MCP bridge, with `.derived` bar and `.counterpoint`.
- **Plate II (`research`) — Gemini Notebook Gluing Studio:** Interactive Open Cover selector $\mathcal{U}$, live query bar, preset investigation pills, Sheaf Equalizer Audit banner, typeset synthesis prose, and dynamic Commutative Olog SVG.
- **Plate III (`art`) — Symbolic Visual Sandbox (*"Illustrated Through Symbols"*):** Single-mutator interactive translator across 8 core symbolic primitives where clicking any token in a formula highlights the corresponding geometric arrow/cone in the SVG diagram and displays a concrete finite-set data trace.
- **Plate IV (`science`) — Corpus Observed (Stalks, Declarations & 3D Poset):** Tabbed browser over all Concept Stalks, all Formal Declarations, and the interactive 3D Alexandrov Poset Fiber Bundle.
- **Plate V (`teaching`) — Course Blueprint & Curriculum Scope:** Visual-Symbolic Grammar table + self-contained module cards using strictly `Key Concept` and `Why It Matters` callouts (never `"So What"`, never stacked callouts without intervening context, and never numbered `"Module 1"` headers on learner surfaces).
