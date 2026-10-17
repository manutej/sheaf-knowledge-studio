# Master Specification & Architecture Manifest (`CETI-SHEAF-PIPELINE-V4.0`)

**Repository:** `sheaf-knowledge-studio`  
**Contract Version:** `CETI-SHEAF-PIPELINE-V4.0`  
**Verification Status:** **GO (`◆ 26/26 Binary Gates Cleared Across All 3 Builds + 12/12 Negative Mutation Self-Tests PASS`)**

---

## 1. Executive Summary

The **Alexandrov Sheaf Knowledge Base & Field-Manual Studio** transforms any long-form mathematical, scientific, or technical monograph (100–1,000+ pages) into:
1. **A Page-Anchored Alexandrov Sheaf Knowledge Base (`sheaf_kb.json` + SQLite FTS5 `cattheory_sheaf.db` + JSON-RPC 2.0 MCP Server `query_sheaf.py`):**
   - Extracts every page verbatim ($1 \dots N$) and indexes every numbered definition, theorem, lemma, proposition, example, task, and exercise with exact page citations (`[p. N]`).
   - Induces a directed acyclic poset $(X, \le)$ of **Concept Stalks (`0-Simplices`)** with local **Ologs (`types` & subject–verb–object `aspects`)**, **Restriction Morphisms (`1-Simplices`)**, **Commutative Triangles (`2-Simplices`)**, and **Empirical Cohomology Audits ($\dim H^0(\mathcal{U}), H^1(\mathcal{U})$)** that genuinely distinguish connected gluing covers (`PASS`) from disconnected covers (`FAIL`).
2. **A Persistent LLM Wiki (`wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`):**
   - Multi-file Markdown knowledge graph suitable for zero-context agent navigation and persistent memory.
3. **An Interactive, Mobile-First Field-Manual & Notebook Studio (`index.html` + deferred `sheaf_pages_bundle.js`):**
   - **Instant First Paint (`< 450 KB` core HTML)** with asynchronous `<script defer>` hydration of all verbatim book pages and formal declarations.
   - **Calm `All 5 | 1-Plate Focus` View Switcher & Mobile Ergonomics:** Switch between scrolling all 5 editorial plates or focusing on a single plate at a time with `◀ Prev Plate / Next Plate ▶` steppers, collapsible mobile Open Cover $\mathcal{U}$ drawer, swipeable horizontal tab strips, and a floating mobile bottom action dock (`🎨 Visuals` · `▶ Deep Dive` · `🧪 Notebook` · `📖 p.N`).
   - **Zero-Leakage Mathematical Typesetting (`convertLatexTokensToHtml`):** Every LaTeX expression renders into clean semantic HTML/SVG math chips with **0 raw backslash leaks**, paired with a **Symbol-by-Symbol Visual Formula Decoder** that unpacks every symbol into plain visual English.
   - **14 Interactive Inkscape-Style Categorical Instruments (Marinov Build):**
     - **Instrument I-A (`#shifterTabs` · 8 Internal ↔ External Constructs):** Elements as Arrows ($1 \xrightarrow{x} A$), Singleton/Terminal ($!_A : A \to 1$), Empty/Initial ($!^A : 0 \to A$), Product Grid vs. Universal Cone ($\langle f,g \rangle$), Coproduct Pouch vs. Cocone ($[f,g]$), Isomorphism ($g \circ f = \mathrm{id}$), Espresso Machine Zoom-Out ($g \circ f$), and Positive Entry Doors vs. Negative Exit Projections (`Either` $\iota_1,\iota_2$ vs. `Tuple` $\pi_1,\pi_2$).
     - **Instrument I-B (`#visualAtlasInstrument` · 6 Interactive Visual Instruments Beyond Notation):**
       1. *Monoid Loops (`pp. 95, 104, 124`):* CMYK Subtractive Color-Mixing Monoid (White identity ball) & $D_3$ Triangle Rotations as a 1-object category $\mathbf{B}M$.
       2. *3D Birkhoff Hasse Cube (`pp. 145–151`):* Interactive 3-world vertex relabeling proving $\mathrm{Div}(30) \cong \text{CMYK} \cong \mathcal{P}(\{a,b,c\})$.
       3. *Logic Coloring & Heyting Implication Lever (`pp. 171, 184, 198, 204`):* Mechanical two-pan balance beam for $C \wedge A \le B \iff C \le (A \Rightarrow B)$, Coloring-Book Axiom Schemas, and BHK constructive paths.
       4. *Russell's Barber Paradox vs. Inductive Sprouting Trees (`pp. 215, 229, 242, 256`):* Untyped self-swallowing loop ($R \in R \iff R \notin R$) vs. stratified inductive trees (`Nat = 1 + Nat`) and Church numeral loops.
       5. *Cartographic Island Functor & `.map(f)` (`pp. 289, 293, 305`):* Functor $F : \mathcal{C} \to \mathcal{D}$ as an island/subway projection alongside `List.map(f)` and `Maybe.map(f)`.
       6. *3D Naturality Prism & Parametricity (`pp. 344, 348, 357, 362`):* Extrudes $\mathcal{C} \times \mathbf{2} \to \mathcal{D}$ into a 3D prism and contrasts polymorphic `reverse` against the unnatural "red-ball peek" trap.
4. **10-Turn, 4-Act Deep-Dive Neural Audio Notebooks (`Kore` × `Puck`):**
   - 15 pre-rendered multi-speaker neural podcast episodes (`137s–203s` each, `1.61–2.38 MB` MP3s) structured in 4 pedagogical acts (*Act I · Visual Hook & Notation*, *Act II · Walking the Diagram*, *Act III · Edge Cases & Traps*, *Act IV · Decoding the Formula & Lab*) with live visual cues (`#podcastVisualCueBar`), clickable page citations (`[p. N]`), and optional live `gemini-2.5-flash-preview-tts` multi-speaker synthesis.

---

## 2. Complete Repository Directory & File Map

```text
sheaf-knowledge-studio/
├── README.md                                   # Quickstart, architecture overview, and build index
├── SPECIFICATION.md                            # This master specification & complete manifest
├── STATUS.md                                   # Live 26-gate ship board & metrics across all builds
├── HANDOFF.md                                  # Cold-resume engineering handoff & extension guide
├── Makefile                                    # Build, audit, selftest, and MCP server targets
├── verify_all.sh                               # Single-command 26-gate + 12-selftest verification runner
│
├── contracts/                                  # Formal Typed Contracts & JSON Schemas
│   ├── TYPED-CONTRACT-SHEAF-META-PROMPT.md     # End-to-end typed meta-prompt & 26-gate specification
│   └── sheaf_kb.schema.json                    # Draft 2020-12 JSON Schema for sheaf_kb.json
│
├── studios/                                    # Ready-to-Open Interactive HTML Studios (+ Offline Bundles & Audio)
│   ├── marinov-category-theory-illustrated/    # Build 2: Boris Marinov (377 pp., 14 Visual Instruments, 6 Podcasts)
│   │   ├── index.html                          # 442.0 KB Studio HTML (26/26 Gates PASS)
│   │   ├── category-theory-illustrated.pdf     # Original 377-page PDF monograph
│   │   └── data/
│   │       ├── sheaf_pages_bundle.js           # Deferred 377-page + 291-declaration bundle
│   │       └── audio/podcast_*.mp3             # 6 × 10-turn 4-Act neural podcast episodes (175s–203s)
│   ├── spivak-category-theory-for-the-sciences/# Build 1: David I. Spivak (609 pp., 30 Stalks, 5 Podcasts)
│   │   ├── index.html                          # 411.7 KB Studio HTML (26/26 Gates PASS)
│   │   ├── cattheory.pdf                       # Original 609-page PDF monograph
│   │   └── data/
│   │       ├── sheaf_pages_bundle.js           # Deferred 609-page + 877-declaration bundle
│   │       └── audio/podcast_*.mp3             # 5 × 10-turn 4-Act neural podcast episodes (155s–182s)
│   └── independent-agent-zero-shot/            # Build 3: Zero-Shot Auto-Induced Agent Build (377 pp., 4 Podcasts)
│       ├── index.html                          # 314.6 KB Studio HTML (26/26 Gates PASS)
│       └── data/
│           ├── sheaf_pages_bundle.js           # Deferred 377-page + 279-declaration bundle
│           └── audio/podcast_*.mp3             # 4 × 10-turn 4-Act neural podcast episodes (138s–161s)
│
├── corpora/                                    # Indexed Sheaf Corpora (sheaf_kb.json, SQLite FTS5, Wiki, MCP)
│   ├── marinov-377pp/                          # Marinov 377-page KB, SQLite FTS5 DB, Wiki, and builders
│   ├── spivak-609pp/                           # Spivak 609-page KB, SQLite FTS5 DB, Wiki, and builders
│   └── independent-agent-377pp/                # Independent Agent zero-shot KB, SQLite FTS5 DB, Wiki
│
├── skills/                                     # 3 Composable Agent Skills + Packaged .skill / .zip Archives
│   ├── sheaf-corpus-indexer/                   # Skill 1: PDF → Alexandrov Sheaf KB + FTS5 + Wiki + MCP
│   ├── sheaf-field-manual-studio/              # Skill 2: Sheaf KB → 5-Plate HTML Studio + 4-Act Podcast TTS
│   ├── sheaf-knowledge-pipeline/               # Skill 3: E2E Orchestrator & 26-Gate MOE Adversarial Auditor
│   └── packages/                               # Packaged .skill and .zip archives for all 3 skills
│
├── portable-toolkit/                           # Standalone 3-Tool Drop-In Kit for Any New PDF
│   ├── README.md
│   ├── META-LEARNING-LOG.md                    # Round-by-round gate ledger across all builds
│   ├── 1-page-anchored-indexer/                # page_corpus_indexer.py + query_corpus.py
│   ├── 2-json-contract-linter/                 # lint_sheaf_contract.py (with --selftest negative mutations)
│   └── 3-gate-review-runner/                   # gate_review_runner.py (26-gate MOE reviewer)
│
├── audits/                                     # Adversarial Evaluation Reports & Machine-Readable JSON Audits
│   ├── ADVERSARIAL-COMPARISON-REPORT.md        # Independent MOE A1–A4 evaluation & remediation report
│   ├── FINDINGS-2026-10-16-ADVERSARIAL-LOCKIN-R1-R3.md
│   ├── marinov_r3_moe_audit.json
│   ├── spivak_r3_moe_audit.json
│   └── independent_agent_r3_moe_audit.json
│
└── releases/                                   # Self-Contained Distributable Studio & Skill Zip Packages
    ├── Marinov_Category_Theory_Illustrated_Studio_Package.zip
    ├── Spivak_Category_Theory_Sciences_Studio_Package.zip
    ├── Independent_Agent_Zero_Shot_Studio_Package.zip
    ├── portable-corpus-toolkit.zip
    ├── sheaf-corpus-indexer.skill / .zip
    ├── sheaf-field-manual-studio.skill / .zip
    └── sheaf-knowledge-pipeline.skill / .zip
```

---

## 3. The 26 Binary Verification Gates (`A1–A4 MOE`)

| Gate ID | Lens | Invariant Checked | Status Across All 3 Builds |
|---|---|---|---|
| `HF-SHEAF-01` | A4 | **100% Verbatim Page Coverage:** `pages` array covers $1 \dots N$ with zero gaps | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-02` | A4 | **Formal Declaration Extraction:** Every numbered definition/theorem/task indexed with `page` | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-03` | A1 | **Alexandrov Concept Stalk Poset:** $\ge 15$ stalks spanning all chapters | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-04` | A1 | **Local Olog Schema Completeness:** Every stalk has $\ge 3$ `types` and $\ge 2$ `aspects` with valid endpoints | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-05` | A1 | **Restriction Morphism Graph Connectivity:** $\ge 25$ directed restrictions with 0 dangling endpoints | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-06` | A1 | **2-Simplex Cocycle Triangles:** $\ge 5$ commuting triangles $\rho_{ik} = \rho_{jk} \circ \rho_{ij}$ | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-07` | A4 | **Surjective Page Fibers:** Every stalk maps to a valid page interval $[p_{\text{start}}, p_{\text{end}}]$ | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-08` | A4 | **Grounded Notebook Investigations:** Every investigation cites $\ge 3$ valid pages and $\ge 3$ stalks | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-09` | A2 | **SQLite FTS5 Full-Text Index Parity:** `pages_fts` and `formal_items_fts` match `sheaf_kb.json` counts | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-10` | A4 | **Persistent LLM Wiki Completeness:** `wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md` exist | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-11` | A1 | **Empirical Gluing Audit Discrimination:** Connected cover returns `PASS` ($\dim H^0 = 1$); disconnected cover returns `FAIL` ($\dim H^0 \ge 2$) | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-12` | A1 | **Documented $H^1$ Obstruction:** At least 1 documented separated/non-gluing cover in `cohomology_obstructions` | **PASS (`◆ CLEARED`)** |
| `HF-SHEAF-13` | A4 | **Neural Podcast Audio Grounding:** Every `notebook_investigation` has a valid MP3 $> 100\text{ KB}$ on disk + `podcast_turns` with valid `cite_page` | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-01` | A3 | **Field-Manual Paper/Ink & Typography Tokens:** Warm cream paper, deep ink, `Fraunces` + `DM Sans` + `JetBrains Mono` | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-02` | A2 | **Instant First Paint Budget:** Core `index.html` $< 450\text{ KB}$ with `<script defer src="...sheaf_pages_bundle.js">` | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-03` | A3 | **Zero Raw LaTeX Backslash Leakage:** `0` raw LaTeX commands in static markup or rendered KB strings | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-04` | A3 | **5 Editorial Plates & Accent Display Titles:** `#plate-1` through `#plate-5` present | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-05` | A3 | **Marginalia & Counterpoint Honesty Apparatus:** $\ge 5$ `.marginalia` with `<cite>` and $\ge 5$ `.counterpoint` blocks | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-06` | A3 | **Non-Color-Alone Verdict Stamps:** Every `.stamp` includes a leading geometric glyph (`◆`, `⚖`, `✓`, `±`, `⊘`) | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-07` | A3 | **Interactive Instruments & Single-Mutator Discipline:** $\ge 5$ `.instrument` containers, $\ge 3$ `role="tablist"`, on-demand 3D poset | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-08` | A3 | **FORGE Pedagogical Compliance:** Zero `"So What"`, zero `"Module N"` titles, zero stacked callouts | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-09` | A3 | **Audience Depth & Paper Theme Switchers:** `Newcomer | Practitioner | Expert` + `Cream | Ink` + `All 5 | 1-Plate Focus` | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-10` | A4 | **Slide-Over Verbatim Reader & Zero Corpus Bleed:** Reader drawer wired to `window.__jumpToPage(p, term)` with `0` out-of-bounds pages | **PASS (`◆ CLEARED`)** |
| `HF-STUDIO-11` | A3 | **Dual-Host Neural Podcast Deck & Live Gemini 2.5 TTS:** `#podcastStudioCard`, `#podcastActBar`, `#podcastVisualCueBar`, and `multiSpeakerVoiceConfig` wired | **PASS (`◆ CLEARED`)** |
| `HF-MCP-01` | A2 | **JSON-RPC 2.0 MCP Server Compliance:** `query_sheaf.py --mcp` responds to `tools/list` and `tools/call` | **PASS (`◆ CLEARED`)** |
| `HF-CONTRACT-01` | A2 | **JSON Schema Contract Validation:** `validate_sheaf_contract.py` + `4/4` negative mutation self-tests pass | **PASS (`◆ CLEARED`)** |

---

## 4. Reproducing & Verifying Everything From Scratch

```bash
# Run the complete 26-gate + 12-negative-selftest verification suite across all 3 builds:
./verify_all.sh

# Or via Make:
make verify
```
