# FINDINGS-2026-10-16-ADVERSARIAL-LOCKIN-R1-R3 — 26-Gate Adversarial Lock-In Across 3 Corpora & Dual-Host Neural Podcast Studio

**Date:** 2026-10-16  
**Scope:** Multi-round (`R1 → R2 → R3`) Adversarial MOE Lock-In across 3 independent builds (`Spivak 609 pp.`, `Marinov 377 pp. Curated`, and `Independent Zero-Shot Agent Run 377 pp.`), expanding the core binary contract from `24` to `26` hard-fail gates (`HF-SHEAF-01..13`, `HF-STUDIO-01..11`, `HF-MCP-01`, `HF-CONTRACT-01`).  
**Verdict:** **GO (`26 / 26` Binary Gates Cleared Across All 3 Builds in R2 & R3 + `--selftest` PASS)**

---

## 1. Adversarial Trajectory Summary (`R1 → R2 → R3`)

| Corpus Build | R1 Baseline (Hardened 26-Gate Spec) | R1 Open Hard-Fails Caught | R2 Post-Remediation | R3 Final Lock-In Verification |
|---|---|---|---|---|
| **Spivak (`609 pp.`)** | `24/26` **NO-GO** | `HF-SHEAF-13`, `HF-STUDIO-11` | `26/26` **GO** | `26/26` **GO (`◆ RATIFIED`)** |
| **Marinov Curated (`377 pp.`)** | `24/26` **NO-GO** | `HF-SHEAF-13`, `HF-STUDIO-11` | `26/26` **GO** | `26/26` **GO (`◆ RATIFIED`)** |
| **Independent Zero-Shot Agent (`377 pp.`)** | `23/26` **NO-GO** | `HF-SHEAF-13`, `HF-STUDIO-10`, `HF-STUDIO-11` | `26/26` **GO** | `26/26` **GO (`◆ RATIFIED`)** |

All 9 round logs (`R1`, `R2`, `R3` × 3 builds) are recorded in the append-only [`portable-toolkit/META-LEARNING-LOG.md`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/portable-toolkit/META-LEARNING-LOG.md).

---

## 2. Four New Anti-Patterns Discovered & Mechanically Gated

### 1. `AP-PODCAST-01` — DOM ID Mismatch Between Studio HTML & Podcast Player JS (`HF-STUDIO-11`)
- **Defect Caught in R1:** In `cattheory-illustrated-sheaf-kb/build_illustrated_studio_html.py`, the HTML template declared `#podcastPlayPauseBtn`, `#hostBadgeKore`, `#hostBadgePuck`, and `#geminiTtsConfigDrawer`, whereas the inline JS event listeners bound to `#ttsPlayBtn`, `#hostBadgeA`, `#hostBadgeB`, and `#podcastGeminiDrawer`.
- **Remediation & Gate:** Unified all Podcast Studio DOM IDs across both `compile_field_manual_studio.py` and `build_illustrated_studio_html.py`, and enforced `HF-STUDIO-11` in `audit_rendered_html.py` to verify both HTML ID presence and JS event listener binding.

### 2. `AP-PODCAST-02` — Spoken PDF Kerning Glues, Raw `(p. N)` Citations & Cookie-Cutter Podcast Turns (`HF-SHEAF-13`)
- **Defect Caught in R1:**
  1. In `synthesize_notebook_podcast.py`, the curated Marinov dialogue dictionary used shorthand keys that did not match the actual `notebook_investigations[i].id` slugs (`q-internal-vs-external-lawvere`, `q-six-worlds-rosetta-stone`, `q-birkhoff-cube-trinity`, `q-type-intro-elim-universal`, `q-functors-natural-polymorphism`, `q-marinov-vs-spivak-bridge`), causing Marinov's episodes to fall back to generic 5-turn auto-dialogues with identical Turn-2 prompts and raw `(p. 289–290)` parentheticals.
  2. In `independent-agent-run`, auto-generated podcast scripts inherited raw PDF line-wrap concatenations (`generalizationof`, `weneed`, `ofnumbers`, `andreturn`, `skeletalcategories`, `componentsinvolves`, `targetcategory`), which neural TTS pronounces unnaturally.
- **Remediation & Gate:**
  - Mapped all 6 Marinov investigation IDs to bespoke 6-turn dialogues and expanded all 5 Spivak episodes to 6–7 turns (`74s–104s`, `870 KB–1.22 MB` each).
  - Added `PDF_DEGLUE_MAP` + `deglue_pdf_text()` + natural spoken page conversion (`(p. 289)` $\to$ `on page 289`) in `synthesize_notebook_podcast.py`.
  - Upgraded `build_auto_dialogue_for_investigation()` to produce 6 non-repetitive turns per episode (`variant = idx % 4`).
  - Enforced `HF-SHEAF-13` in `validate_sheaf_contract.py` checking `>= 6` turns, alternating `Kore`/`Puck` hosts, `>= 40 KB` & `>= 25s` neural MP3s, zero duplicate Turn-2/closing prompts, zero PDF kerning glues, and zero raw `(p. N)` parentheticals.

### 3. `AP-PODCAST-03` — Missing Custom-Query Multi-Speaker Script Generator (`HF-STUDIO-11`)
- **Defect Caught in R1:** Pre-rendered MP3 episodes covered the pre-glued investigations, but submitting a custom user query in the Notebook Studio lacked a dynamic 6-turn dialogue generator (`buildCustomPodcastTurns`) to feed the live Gemini `2.5-flash-preview-tts` `multiSpeakerVoiceConfig` synthesizer.
- **Remediation & Gate:** Added `buildCustomPodcastTurns(q, topStalks, coh)` to both Studio compilers and gated it under `HF-STUDIO-11`.

### 4. `AP-STUDIO-BLEED-01` — Residual Cross-Corpus Page Count Strings in Reader Drawer (`HF-STUDIO-10`)
- **Defect Caught in R1:** While hero and masthead strings were dynamically adapted in `compile_field_manual_studio.py`, two reader-drawer literals (`"of 609 ·"` and `"Math.min(609,"`) remained hardcoded when compiling the 377-page `Independent_Agent_Sheaf_Studio.html`.
- **Remediation & Gate:** Added dynamic replacement for `"of 609 ·"` and `"Math.min(609,"` in `adapt_html_template_for_corpus()` and tightened `HF-STUDIO-10` in `audit_rendered_html.py` to fail on any residual `609`/`877`/`30 Stalks` strings when `book.total_pages != 609`.
