# Adversarial Evaluators A1–A4 for the Sheaf Knowledge Pipeline

Aligned with `adversarial/eval-spec/EVALUATION-META-PROMPT.md`, `AGENTS.md`, and `meta-notebook`, every Sheaf Knowledge Base & Field-Manual Studio build must pass **4 independent adversarial evaluator lenses (A1–A4)** over at least **3 recursive eval $\to$ fix rounds** before receiving a `GO` ship vote.

---

## 1. The Four MOE Evaluator Lenses

| Agent ID | Lens | Primary Kill Targets | Hard Fail Gates Owned |
|---|---|---|---|
| **A1** | **Mathematical Depth, Olog Completeness & Sheaf Cohomology** | Thin concept stalks; missing or disconnected restriction morphisms $\rho_{U,V}$; broken Olog `src`/`dst` references; uncovered body pages; missing 2-simplices | `HF-SHEAF-01` .. `HF-SHEAF-07`, `HF-STUDIO-07` |
| **A2** | **Performance, Architecture, SQLite FTS5 & MCP Interoperability** | Multi-MB synchronous HTML bloat (`> 450 KB` core HTML); missing `<script defer>` page bundle; always-running 3D `requestAnimationFrame` loop burning CPU; broken SQLite FTS5 or `--mcp` JSON-RPC server | `HF-SHEAF-10`, `HF-SHEAF-11`, `HF-STUDIO-02`, `HF-STUDIO-09` |
| **A3** | **Field-Manual Craft, Math Rendering & Symbolic Pedagogy** | Raw LaTeX backslash leaks (`\mathcal`, `\varprojlim`, `\dashv`); missing CETI warm paper tokens (`#F5EFE3`, `#1A1612`, `#A67756`); missing `.marginalia` or `.counterpoint` on any plate; color-alone stamps; stacked `.callout-box` elements; forbidden `"So What"` or `"Module 1"` learner labels | `HF-STUDIO-01`, `HF-STUDIO-03`, `HF-STUDIO-04`, `HF-STUDIO-05`, `HF-STUDIO-06`, `HF-STUDIO-08` |
| **A4** | **Citation Integrity, Page-Fiber Grounding & Persistent Wiki** | Out-of-bounds `[p. N]` citations; formal declarations missing page fibers; unverified marginalia quotes; mismatch between `sheaf_kb.json` stalks and `wiki/concepts/*.md` | `HF-SHEAF-08`, `HF-SHEAF-09`, `HF-SHEAF-12`, `HF-STUDIO-10` |

---

## 2. Recursive Meta-Improvement Protocol (`>= 3 Rounds`)

```text
Round r ∈ {1, 2, 3}:
  1. Execute A1, A2, A3, A4 deterministic + structural probes (`run_sheaf_pipeline_audit.py`)
  2. Log all OPEN Hard Fails (HF-SHEAF-*, HF-STUDIO-*) and P1 Craft defects
  3. Apply targeted surgical fixes to `build_sheaf_kb.py`, `build_studio_html.py`, or `TYPED-CONTRACT-SHEAF-META-PROMPT.md`
  4. Re-compile artifacts and re-run audit; verify violation multiset strictly shrinks:
       |V(r)| < |V(r-1)|  until  |V(R)| == 0 (EXACT-CLEAN GO)
  5. Append durable findings to `wiki/qc-memory/FINDINGS-*.md` and `wiki/LEDGER.md`
```
