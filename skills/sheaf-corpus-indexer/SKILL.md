---
name: sheaf-corpus-indexer
description: Extract, index, and verify any long-form PDF book, textbook, or research monograph (100–1,000+ pages) into an Alexandrov Sheaf Knowledge Base (`sheaf_kb.json`), SQLite FTS5 full-text index (`cattheory_sheaf.db`), deferred browser page bundle (`sheaf_pages_bundle.js`), persistent LLM Wiki (`wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`), and local CLI / Gemini / JSON-RPC 2.0 MCP query server (`query_sheaf_engine.py`). Enforces 12 binary sheaf-cohomology and schema gates (`HF-SHEAF-01` through `HF-SHEAF-12`).
---

# Sheaf Corpus Indexer (`sheaf-corpus-indexer`)

This skill transforms a large PDF book or research corpus into a **mathematically grounded Alexandrov Sheaf Knowledge Base**:
$$\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$$
Rather than slicing a book into flat, context-free vector chunks, this skill indexes:
1. **100% of Verbatim Pages (`1..P`)** with active chapter/section hierarchy and word counts,
2. **All Formal Numbered Declarations** (`Definition`, `Theorem`, `Proposition`, `Lemma`, `Corollary`, `Example`, `Application`, `Remark`, `Exercise`, `Principle`, `Rule`),
3. **20–40 Concept Stalks (`0-Simplices`)** $U_i \in X$, each carrying a local Ontology Log (`olog.types`, `olog.aspects`, `olog.facts`), a symbolic `formal_core`, and an exact page fiber $[p_{\text{start}}, p_{\text{end}}]$,
4. **Restriction Morphisms (`1-Simplices`)** $\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$ defining explicit conceptual overlaps and translation formulas,
5. **Commutative Gluing Triangles (`2-Simplices`)** $\tau = [U, V, W]$ verifying $\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$ (`H^0 Exact`),
6. **Pre-Glued Notebook Investigations** with verified `[p. N]` citations,
7. **SQLite FTS5 Search Database + Deferred Browser Bundle + Native `--mcp` Server**.

---

## 1. Reading & Reference Map

| Phase / Task | Reference / Script |
|---|---|
| JSON Schema Draft 2020-12 Typed Contract | `references/sheaf-schema-contract.json` |
| How to design Stalks, Ologs & Restrictions | `references/olog-and-stalk-extraction-guide.md` |
| End-to-End PDF Extractor & Wiki Builder | `scripts/extract_and_index_pdf.py` |
| Deterministic 12-Gate Contract Validator | `scripts/validate_sheaf_contract.py` |
| Local CLI + Gemini REST + `--mcp` Server | `scripts/query_sheaf_engine.py` |

---

## 2. Operational Workflow (Entry → Action → Exit)

### Step 1: Extract & Index the PDF Corpus
Run `scripts/extract_and_index_pdf.py` (or a domain-customized builder modeled on `cattheory-sheaf-kb/build_sheaf_kb.py`):

```bash
python3 .agents/skills/sheaf-corpus-indexer/scripts/extract_and_index_pdf.py \
  --pdf path/to/book.pdf \
  --out-dir path/to/output-kb \
  --title "Book Title" \
  --author "Primary Author" \
  --year 2026
```

For flagship textbooks (such as Spivak's *Category Theory for the Sciences*), curate the 20–40 Concept Stalks, their local Ologs (`types`, `aspects`, `facts`), the 50+ restriction morphisms $\rho_{U,V}$, and the 5+ pre-glued notebook investigations so that every stalk reflects the book's exact section boundaries and formal theorems.

### Step 2: Validate Against the 12 Binary Sheaf Gates (`HF-SHEAF-01..12`)
Before building any UI volume, run the deterministic validator:

```bash
python3 .agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py \
  --kb path/to/output-kb/data/sheaf_kb.json \
  --db path/to/output-kb/data/cattheory_sheaf.db \
  --wiki path/to/output-kb/wiki \
  --bundle path/to/output-kb/data/sheaf_pages_bundle.js \
  --out path/to/output-kb/data/sheaf_contract_audit.json
```

**All 12 gates are binary (`CLEARED` | `OPEN`). Do not advance if any gate is `OPEN`:**
- `HF-SHEAF-01`: Required top-level schema keys present and `len(pages) == book.total_pages`.
- `HF-SHEAF-02`: 100.0% of body pages covered by at least one Concept Stalk (`uncovered == 0`).
- `HF-SHEAF-03`: Stalk IDs unique (`>= 10` stalks) and page intervals valid (`1 <= start_page <= end_page <= total_pages`).
- `HF-SHEAF-04`: Local Olog referential integrity (`>= 2` types, `>= 1` aspect, `>= 1` fact; every aspect `src` and `dst` declared in `olog.types`).
- `HF-SHEAF-05`: Global poset connectivity (every stalk connected via restriction morphisms; single connected component).
- `HF-SHEAF-06`: Every restriction morphism carries a non-empty symbolic `formula` and semantic `overlap` description.
- `HF-SHEAF-07`: Commutative 2-simplices (`two_simplices`) reference valid connected stalk triples.
- `HF-SHEAF-08`: All extracted formal declarations (`formal_items`) have valid page bounds and non-empty `stalk_ids`.
- `HF-SHEAF-09`: Curated `notebook_investigations` (`>= 3`) have valid `open_cover` stalk IDs and valid `[p. N]` citations.
- `HF-SHEAF-10`: Deferred browser bundle `sheaf_pages_bundle.js` exists and is non-empty.
- `HF-SHEAF-11`: SQLite FTS5 tables (`pages_fts`, `formal_items_fts`) match exact page and declaration counts.
- `HF-SHEAF-12`: Persistent LLM Wiki (`wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`) has 1-to-1 parity with chapters and stalks.

### Step 3: Verify Local CLI & MCP Server Querying
Test both the cohomology gluing audit and a notebook query:

```bash
python3 .agents/skills/sheaf-corpus-indexer/scripts/query_sheaf_engine.py --gluing-audit
python3 .agents/skills/sheaf-corpus-indexer/scripts/query_sheaf_engine.py --ask "Your domain question"
printf '{"jsonrpc":"2.0","id":1,"method":"tools/list"}\n' | python3 .agents/skills/sheaf-corpus-indexer/scripts/query_sheaf_engine.py --mcp
```
