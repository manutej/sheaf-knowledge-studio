---
name: sheaf-knowledge-pipeline
description: End-to-end orchestrator and recursive adversarial evaluation pipeline for transforming any large book, textbook, or research PDF into a verified Alexandrov Sheaf Knowledge Base (`sheaf_kb.json` + SQLite FTS5 + `--mcp` server), a persistent LLM Wiki (`wiki/`), a fast-loading CETI Field-Manual & Gemini Notebook Studio (`index.html` + deferred page bundle), and an interactive "Illustrated Through Symbols" visual curriculum. Composes `sheaf-corpus-indexer`, `sheaf-field-manual-studio`, `meta-notebook`, and `noether-wiki` under a 24-gate A1–A4 MOE adversarial loop.
---

# Sheaf Knowledge Pipeline (`sheaf-knowledge-pipeline`)

This master skill orchestrates the complete end-to-end workflow (`P0 → P5`) for converting any long-form book or research monograph into:
1. **An Alexandrov Sheaf Knowledge Base** ($\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$) with 100% body-page coverage, local Ologs, restriction morphisms $\rho_{U,V}$, and commutative 2-simplices,
2. **A Fast Local SQLite FTS5 + Gemini REST + JSON-RPC 2.0 MCP Query Server** (`query_sheaf.py`),
3. **A Persistent Markdown LLM Wiki** (`wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`), and
4. **A CETI Field-Manual & Gemini Notebook Studio HTML Volume** (`#F5EFE3` warm cream paper / `#1A1612` deep ink, zero-leakage LaTeX/Math typesetting, interactive Open-Cover Gluing Studio, Symbol $\leftrightarrow$ Diagram Visual Sandbox, 3D Alexandrov Poset Fiber Bundle, 609-Page Slide-Over Reader, and Course Blueprint).

---

## 1. Composed Skill Suite

| Skill | Responsibility | Hard Gates Enforced |
|---|---|---|
| `sheaf-corpus-indexer` | PDF extraction, Alexandrov stalk topology, local Ologs, SQLite FTS5, persistent Wiki, CLI/MCP server | `HF-SHEAF-01` .. `HF-SHEAF-12`, `HF-MCP-01` |
| `sheaf-field-manual-studio` | CETI Field-Manual HTML compilation, deferred page bundle, LaTeX/Math typesetting, 5 Plates, Symbolic Sandbox | `HF-STUDIO-01` .. `HF-STUDIO-10` |
| `sheaf-knowledge-pipeline` (this skill) | P0–P5 orchestration, Typed Meta-Prompt Contract, A1–A4 MOE Adversarial Loop (`>= 3` rounds), QC memory compounding | All 24 Binary Gates (`HF-SHEAF-*`, `HF-STUDIO-*`, `HF-MCP-01`, `HF-CONTRACT-01`) |

---

## 2. End-to-End Phases (`P0 → P5`)

### P0 — Scope, Corpus Policy & Topology Blueprint
- **Entry:** A target long-form PDF book or research corpus (`100–1,000+ pages`) and pedagogical/research goal.
- **Action:** Define the domain scope note, verify the PDF on disk (`total_pages`), and establish the **Source-Verification Rule**: every claim, theorem, and marginalia quote must trace to an exact `[p. N]` page fiber in the book.
- **Exit:** Written P0 scope block + verified PDF path.

### P1 — Full-Book Verbatim Extraction & Alexandrov Stalk Topology (`sheaf-corpus-indexer`)
- **Entry:** Verified PDF on disk.
- **Action:** Extract all `1..P` verbatim pages and all formal numbered declarations (`Definition`, `Theorem`, `Proposition`, `Example`, `Exercise`). Partition the book into `20–40` **Concept Stalks** (`0-simplices`), wire `>= |Stalks|` **Restriction Morphisms** $\rho_{U,V}$ (`1-simplices`), and verify **Commutative Gluing Triangles** (`2-simplices`).
- **Exit:** `data/sheaf_kb.json` + `data/sheaf_pages_bundle.js` + `data/cattheory_sheaf.db` + `wiki/` passing `HF-SHEAF-01..12`.

### P2 — Local CLI, Gemini Synthesis & MCP Server Verification (`sheaf-corpus-indexer`)
- **Entry:** Validated `sheaf_kb.json` and SQLite FTS5 DB.
- **Action:** Wire `query_sheaf.py` with `--gluing-audit`, `--ask`, and `--mcp` (JSON-RPC 2.0 over stdio exposing `sheaf_query`, `sheaf_inspect_stalk`, `sheaf_read_page`).
- **Exit:** `HF-MCP-01` CLEARED.

### P3 — CETI Field-Manual Studio & Symbolic Sandbox Compilation (`sheaf-field-manual-studio`)
- **Entry:** `HF-SHEAF-01..12` and `HF-MCP-01` CLEARED.
- **Action:** Compile the 5-Plate Field-Manual Studio HTML (`< 450 KB` core HTML + `<script defer>` page bundle) with warm cream paper (`#F5EFE3`), `Fraunces`/`DM Sans`/`JetBrains Mono` typography, 7-stage LaTeX/Math renderer, Open-Cover Notebook Studio, Interactive Symbolic Sandbox, 3D Poset Atlas, and Course Blueprint.
- **Exit:** `HF-STUDIO-01..10` CLEARED.

### P4 — Recursive Adversarial MOE Evaluation Loop (`A1–A4`, `>= 3` Rounds)
- **Entry:** Compiled Studio HTML + Sheaf KB.
- **Action:** Run `scripts/run_sheaf_pipeline_audit.py` across Evaluators `A1` (Depth/Olog/Cohomology), `A2` (Performance/FTS5/MCP), `A3` (Field-Manual/Math/Symbolic Craft), and `A4` (Citations/Page-Fibers/Wiki). Repair any open gates or craft defects across $\ge 3$ iterations until `24/24` gates are `CLEARED`.
- **Exit:** `overall_ship_vote == "GO"` (`24/24` gates cleared).

### P5 — QC Memory Compounding & Skill Packaging
- **Entry:** `GO` ship vote from P4.
- **Action:** Write durable findings to `wiki/qc-memory/FINDINGS-*.md`, append a row to `wiki/LEDGER.md`, and package portable `.skill` archives.
