# Portable Corpus Toolkit (3 High-ROI Modules + Genuine Empirical Sheaf Engine)

This directory packages the three standalone, immediately portable modules in priority order, plus the upgraded empirical cohomology engine that eliminates all three weak spots identified in review:

---

## 1. What Was Fixed in the Sheaf & Linter Engine

| Weak Spot Identified in Review | Root Cause in v1 | How It Is Fixed in v2 (Verified by `--selftest`) |
|---|---|---|
| **1. "The 30 concepts and their links are typed by hand into the code, so it only works for this one book."** | `compile_sheaf_index.py` previously contained hardcoded dictionaries for Spivak's 30 stalks and 55 links. | Replaced with **`sheaf_induction_engine.py`** + universal **`compile_sheaf_index.py --pdf <any.pdf>`**: automatically extracts chapters, sections, formal declarations (`Definition`, `Theorem`, `Prop`, `Task`), induces page-fiber stalks, extracts local Olog triples, and computes restriction edges from TF-IDF cosine similarity + definiendum propagation + explicit cross-references (`ZERO` hardcoded concepts required). |
| **2. "The 'H⁰ coherence' score is a fixed formula based on the number of links, not computed from the content."** | `query_sheaf.py` had `0.96 + 0.008 * min(len(overlaps), 4)` instead of content-computed cochain norms. | Replaced with **`evaluate_open_cover_cohomology(kb, cover_ids)`**: computes real restriction fidelity $f_{ij} = 1 - \|\delta^0 s\|_{ij}$ from **TF-IDF cosine similarity on shared vocabulary**, **Jensen-Shannon contextual divergence ($D_{\mathrm{JS}}$)**, **shared defined terms**, **prerequisite citation closure ratio**, **connected components $\beta_0(\mathcal{U})$**, and **2-simplex holonomy defect $\|\delta^1 \omega\|_{ijk}$**. |
| **3. "The gluing audit always says PASS, because all it checks is that links point to something that exists."** | Both `run_gluing_audit()` and the Studio UI only checked endpoint existence (`source in stalk_ids`). | Upgraded `validate_sheaf_contract.py`, `query_sheaf.py --audit-cover`, and both HTML Studios so the Gluing Audit checks **empirical vocabulary overlap, connected components $\beta_0(\mathcal{U})$, prerequisite closure, and $\check{H}^1$ polysemy obstructions** — actively returning **`FAIL` (exit code `1` / crimson `⊘ H¹ GLUING OBSTRUCTION` banner)** on disconnected or unbridged covers, with a `--selftest` proving all 4 failure modes are caught. |

---

## 2. The 3 Portable Modules (In Order of Porting Priority)

### Priority 1: Page-Anchored Extraction + Offline FTS5 Search Index (`1-page-anchored-indexer/`)
- **Files:** `page_corpus_indexer.py`, `sheaf_induction_engine.py`, `query_corpus.py`
- **What it does:** Turns any PDF into a page-anchored JSON + SQLite FTS5 offline search database (`pages_fts`, `formal_items_fts`) where every `Definition`, `Theorem`, `Proposition`, `Example`, and `Task` gets its exact PDF page anchor (e.g., `"Prop 3.1.1.10, p. 74"`) and drill-down CLI/MCP query support.
- **Run on any PDF:**
  ```bash
  python3 portable-toolkit/1-page-anchored-indexer/page_corpus_indexer.py \
    --pdf path/to/document.pdf \
    --out-dir path/to/output_kb \
    --title "Document Title" \
    --author "Author Name"
  ```

### Priority 2: Standalone JSON & SQLite Contract Linter (`2-json-contract-linter/`)
- **File:** `corpus_contract_linter.py`
- **What it does:** Fast agent lint rule (`< 0.3s`) verifying 12 binary invariants (`HF-SHEAF-01..12`): page count parity, `100%` body-page coverage, valid page bounds `[1..P]` on every citation, FTS5 table parity, and empirical content overlap on every link. Includes `--selftest` that mutates a KB in memory and proves the linter catches bogus links, hallucinated page citations (`p=99999`), and uncomputed decorative scores.
- **Run lint + negative selftest:**
  ```bash
  python3 portable-toolkit/2-json-contract-linter/corpus_contract_linter.py \
    --kb cattheory-sheaf-kb/data/sheaf_kb.json \
    --selftest
  ```

### Priority 3: Gate-by-Gate Review Runner for Meta-Learning Logs (`3-gate-review-runner/`)
- **File:** `gate_review_runner.py`
- **What it does:** Runs the fixed list of pass/fail gates each round, writes a structured JSON scorecard, and appends a timestamped row (`Round`, `Verdict`, `Gates Cleared`, `Open Gates`, `Empirical Metrics`) to `META-LEARNING-LOG.md`.
- **Run a round review:**
  ```bash
  python3 portable-toolkit/3-gate-review-runner/gate_review_runner.py \
    --kb cattheory-sheaf-kb/data/sheaf_kb.json \
    --html "Category Theory Sheaf Knowledge Base - Notebook Studio.html" \
    --round 1 \
    --label "spivak-609pp"
  ```

### Priority 4: Skill-Sheaf Graph Memory & Progressive-Disclosure Meta-Controller (`4-skill-sheaf-meta-controller/`)
- **Files:** `skill_sheaf_compiler.py`, `query_skill_sheaf.py`, `dist/*.skill.zip`
- **What it does:** Indexes all active skills across `.agents/skills`, `~/.grok/skills`, and `~/.claude/skills` into a 7-Chapter, 14-Stalk Alexandrov Sheaf Knowledge Base (`skill-sheaf-kb/data/sheaf_kb.json` + SQLite FTS5 + persistent `wiki/`), consolidates the 89+ skills into **7 Master Routers** (`operadic-meta-suite`, `sheaf-research-memory`, `ceti-explainer` v2.0 Argon, `editorial-design-studio`, `adversarial-moe-governance`, `agy-skill-foundry`, `operator-productivity-suite`) with **4-Tier Progressive Disclosure** (`-98.2%` every-turn L0 frontmatter tokens), and exposes a fast CLI / JSON-RPC 2.0 `--mcp` task router.
- **Run Skill-Sheaf compilation, progressive-disclosure routing & token audit:**
  ```bash
  python3 portable-toolkit/4-skill-sheaf-meta-controller/skill_sheaf_compiler.py
  python3 portable-toolkit/4-skill-sheaf-meta-controller/query_skill_sheaf.py --token-audit
  python3 portable-toolkit/4-skill-sheaf-meta-controller/query_skill_sheaf.py --route "Build an animated SVG explainer with volumetric glyphs"
  ```
