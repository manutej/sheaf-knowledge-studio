# CETI Alexandrov Sheaf Knowledge Base, 4-Act Neural Audio Notebook & Field-Manual Studio

**Contract Version:** `CETI-SHEAF-PIPELINE-V9.0` ([`SPECIFICATION.md`](./SPECIFICATION.md) · [`contracts/TYPED-CONTRACT-SHEAF-META-PROMPT.md`](./contracts/TYPED-CONTRACT-SHEAF-META-PROMPT.md))  
**Audit Status:** **GO (`◆ 30/30 Binary Gates Cleared Across All 3 Builds + 33/33 Negative Mutation Self-Tests PASS + 23-State High-DPI VBM Desktop/Mobile Audit PASS`)**

This repository contains the complete, end-to-end **Alexandrov Sheaf Knowledge Pipeline**:
- **Master Specification & Typed Contract:** [`SPECIFICATION.md`](./SPECIFICATION.md) and [`contracts/TYPED-CONTRACT-SHEAF-META-PROMPT.md`](./contracts/TYPED-CONTRACT-SHEAF-META-PROMPT.md) (`sheaf-schema-contract.json`).
- **3 Composable Agent Skills (`skills/`)** and a **Standalone 3-Tool Portable Corpus Kit (`portable-toolkit/`)**.
- **3 Verified Reference Builds (`studios/` & `corpora/`):**
  1. **David I. Spivak — *Category Theory for the Sciences* (`609 pp.`, `30` stalks, `877` contextualized declarations, `5` × 10-turn 4-Act neural podcasts with `T1..T10` Turn Rail & `🎨 Open Visual ↗` sync)**
  2. **Boris Marinov — *Category Theory Illustrated* (`377 pp.`, `24` stalks, `291` declarations (`165` Definitions, `38` Theorems, `88` Tasks), `14` multi-state visual instruments with state pills, `6` × 10-turn 4-Act neural podcasts)**
  3. **Independent Zero-Shot Agent Run (`377 pp.`, `18` auto-induced stalks, `279` declarations, `4` × 10-turn 4-Act neural podcasts)**
- **Mobile-First, Touch-3D & `1-Plate Focus` UI:** Responsive single-plate focus mode (`All 5 | 1-Plate Focus`), 1-finger mobile touch-orbit on the 3D Alexandrov Poset canvas, Anchored Formal Block Callout Banner in the Slide-Over Page Reader, Interactive Walkable Lab Launchers in Plate V, collapsible mobile Open Cover $\mathcal{U}$ drawer, and floating mobile bottom navigation bar.
- **Self-Contained Release Packages (`releases/`):** Ready-to-download `.zip` and `.skill` archives.

---

## 1. Repository Directory Map

```text
sheaf-knowledge-studio/
├── README.md                                  # Architecture, quickstart, CLI reference & directory map
├── SPECIFICATION.md                           # Master V9.0 specification, 30 gates, 14 visual instruments
├── HANDOFF.md                                 # Cold-resume guide & Round 7 engineering roadmap
├── STATUS.md                                  # 27/27 Binary Gate Ship Board & R1–R6 Lock-In Status
├── Makefile                                   # One-command build, audio synthesis & 30-gate verification
├── verify_all.sh                              # Automated 30-gate + 33/33 negative-mutation selftest suite
├── .gitignore                                 # Clean Python / OS ignore rules
│
├── contracts/                                 # Formal Typed Specifications
│   ├── TYPED-CONTRACT-SHEAF-META-PROMPT.md    # Master Typed Contract & Copy-Pasteable Meta-Prompt
│   └── sheaf-schema-contract.json             # Canonical JSON Schema for SheafKnowledgeBase
│
├── studios/                                   # Self-Contained Interactive HTML Volumes (Open index.html)
│   ├── spivak-category-theory-for-the-sciences/
│   │   ├── index.html                         # Spivak 609-Page Field-Manual & Notebook Studio (411.7 KB)
│   │   ├── data/audio/                        # 5 × 10-Turn 4-Act Neural Podcast MP3s (Kore × Puck, 155s–182s)
│   │   └── data/sheaf_pages_bundle.js         # Deferred 609-page verbatim bundle
│   ├── marinov-category-theory-illustrated/
│   │   ├── index.html                         # Marinov 377-Page Illustrated Sheaf Studio (442.0 KB, 14 Visuals)
│   │   ├── data/audio/                        # 6 × 10-Turn 4-Act Neural Podcast MP3s (Kore × Puck, 175s–203s)
│   │   └── data/sheaf_pages_bundle.js         # Deferred 377-page verbatim bundle
│   └── independent-agent-zero-shot/
│       ├── index.html                         # Independent Zero-Shot Agent Studio (314.6 KB)
│       ├── data/audio/                        # 4 × 10-Turn 4-Act Neural Podcast MP3s (Kore × Puck, 138s–161s)
│       └── data/sheaf_pages_bundle.js         # Deferred 377-page verbatim bundle
│
├── releases/                                  # Standalone Distributable Studio & Skill Zip Archives
│
├── corpora/                                   # Full Sheaf KBs, SQLite FTS5 DBs, Persistent Wikis & MCP Servers
│   ├── spivak-609pp/                          # David I. Spivak — Category Theory for the Sciences (609 pp.)
│   │   ├── data/                              # sheaf_kb.json, cattheory_sheaf.db, sheaf_pages_bundle.js, audio/
│   │   ├── wiki/                              # HOME.md, chapters/*.md, concepts/*.md (30 stalks)
│   │   └── query_sheaf.py                     # CLI & JSON-RPC 2.0 --mcp Server
│   ├── marinov-377pp/                         # Boris Marinov — Category Theory Illustrated (377 pp.)
│   │   ├── data/                              # sheaf_kb.json, cattheory_sheaf.db, sheaf_pages_bundle.js, audio/
│   │   ├── wiki/                              # HOME.md, chapters/*.md, concepts/*.md (24 stalks)
│   │   └── query_sheaf.py                     # CLI & JSON-RPC 2.0 --mcp Server
│   └── independent-agent-377pp/               # Independent Agent Zero-Shot Auto-Induced Run (377 pp.)
│       ├── data/                              # sheaf_kb.json, cattheory_sheaf.db, sheaf_pages_bundle.js, audio/
│       ├── wiki/                              # HOME.md, chapters/*.md, concepts/*.md (18 stalks)
│       └── query_sheaf.py                     # CLI & JSON-RPC 2.0 --mcp Server
│
├── skills/                                    # 3 Composable Antigravity Skills (Source + Packaged Archives)
│   ├── sheaf-corpus-indexer/                  # Skill 1: Auto-Induced PDF Extraction, Cohomology, FTS5, Wiki & MCP
│   ├── sheaf-field-manual-studio/             # Skill 2: CETI Field-Manual HTML Compiler, LaTeX & Neural Podcast TTS
│   ├── sheaf-knowledge-pipeline/              # Skill 3: End-to-End Orchestrator & 30-Gate MOE Adversarial Auditor
│   └── packages/                              # Installable .skill and .zip bundles
│
├── portable-toolkit/                          # Drop-In 3-Tool Corpus Engineering Kit
│   ├── README.md
│   ├── META-LEARNING-LOG.md                   # Append-only R1 -> R2 -> R3 Gate Review Log
│   ├── 1-page-anchored-indexer/               # page_corpus_indexer.py + query_corpus.py
│   ├── 2-json-contract-linter/                # sheaf_contract_linter.py (with --selftest)
│   ├── 3-gate-review-runner/                  # gate_review_runner.py
│   └── portable-corpus-toolkit.zip
│
└── audits/                                    # Adversarial Evaluation Reports & JSON Gate Telemetries
    ├── FINDINGS-2026-10-16-ADVERSARIAL-LOCKIN-R1-R3.md
    ├── FINDINGS-2026-10-16-sheaf-skill-suite.md
    └── ADVERSARIAL-COMPARISON-REPORT.md
```

---

## 2. Quickstart (30 Seconds)

### A. Open Any Interactive Studio in Your Browser
Each folder under `studios/` is 100% self-contained (`< 440 KB` core HTML + deferred page bundle + pre-rendered neural MP3 episodes):
- **Spivak (609 pp.):** `open studios/spivak-category-theory-for-the-sciences/index.html`
- **Marinov Curated (377 pp.):** `open studios/marinov-category-theory-illustrated/index.html`
- **Independent Zero-Shot Agent (377 pp.):** `open studios/independent-agent-zero-shot/index.html`

### B. Run the Full 30-Gate Verification + Negative Mutation Self-Tests
```bash
./verify_all.sh
# or:
make verify
```

### C. Query Any Sheaf Knowledge Base via CLI or JSON-RPC 2.0 MCP Server
```bash
# Search verbatim pages & concept stalks with page-anchored citations
python3 corpora/spivak-609pp/query_sheaf.py --ask "How do adjoint functors relate to database data migration?"

# Run an empirical Čech cohomology gluing audit (returns PASS on connected covers, FAIL on disconnected covers)
python3 corpora/marinov-377pp/query_sheaf.py --audit-cover u01-sets-internal-external u04-products-coproducts

# Launch as a standard JSON-RPC 2.0 MCP stdio server
python3 corpora/spivak-609pp/query_sheaf.py --mcp
```

### D. Index Any New PDF Book End-to-End (Zero Handcoding)
```bash
# 1. Auto-induce chapters, concept stalks, local Ologs, empirical cohomology, SQLite FTS5 & Markdown Wiki
python3 skills/sheaf-corpus-indexer/scripts/compile_sheaf_index.py \
  --pdf /path/to/book.pdf \
  --out-dir corpora/my-new-book \
  --title "Book Title" \
  --author "Author Name"

# 2. Synthesize Dual-Host Neural Podcast MP3s (Host A: Kore × Host B: Puck)
/Users/cairo/.local/bin/uv run --with edge-tts python3 \
  skills/sheaf-field-manual-studio/scripts/synthesize_notebook_podcast.py \
  --kb corpora/my-new-book/data/sheaf_kb.json

# 3. Compile the 5-Plate Interactive Studio HTML
python3 skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py \
  --kb corpora/my-new-book/data/sheaf_kb.json \
  --out studios/my-new-book/index.html \
  --bundle corpora/my-new-book/data/sheaf_pages_bundle.js

# 4. Run the 30-Gate MOE Audit & Contract Self-Test
python3 skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py \
  --kb corpora/my-new-book/data/sheaf_kb.json \
  --html studios/my-new-book/index.html \
  --query-script corpora/my-new-book/query_sheaf.py
```
