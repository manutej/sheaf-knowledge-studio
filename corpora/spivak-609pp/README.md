# Sheaf Knowledge Base & Gemini Notebook Studio — *Category Theory for the Sciences* (David I. Spivak)

This directory contains the complete **Sheaf Knowledge Base ($\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$)**, **Deep LLM Wiki**, **SQLite + FTS5 Categorical Index**, **Python Gluing Query CLI**, and **Self-Contained Interactive Gemini Notebook Studio** built from all **609 pages** of David I. Spivak's *Category Theory for the Sciences* (MIT Press, 2014).

---

## 1. Mathematical Architecture: Why a *Sheaf* Instead of a Flat Graph?

Directly implementing **Section 7.2.3.11 (*Sheaf of ologged concepts*, PDF p. 523–524)** of Spivak's book:

1. **The Simplicial Conceptual Complex $X$ & Alexandrov Site $\mathcal{X} = \text{Alx}(X^{\text{op}})$:**
   - **0-Simplices (30 Concept Stalks $v \in X_0$):** Core conceptual domains across all 7 chapters (`scientific-agreement-worldviews`, `sets-and-functions`, `commutative-diagrams`, `ologs-ontology-logs`, `products-and-projections`, `coproducts-and-injections`, `pullbacks-and-fiber-products`, `spans-experiments-matrices`, `pushouts-and-colimits-set`, `currying-exponentials-subobjects`, `monoids-and-actions`, `groups-and-symmetries`, `graphs-and-paths`, `orders-lattices-hierarchies`, `database-schemas-instances`, `categories-objects-morphisms`, `functors-structure-maps`, `natural-transformations-functor-cat`, `categorical-equivalence-cat-sch`, `universal-limits-and-cones`, `universal-colimits-and-cocones`, `grothendieck-construction-comma`, `adjoint-functors-hom-iso`, `data-migration-delta-sigma-pi`, `presheaves-representables-yoneda`, `sheaves-and-local-to-global-gluing`, `sheaf-of-ologged-concepts-descent`, `monads-and-contextual-computation`, `kleisli-categories-scientific-method`, `operads-and-hierarchical-composition`).
   - **Local Stalks as Ologs ($\mathcal{O}(v) \in \mathbf{Sch} \simeq \mathbf{Cat}$):** Every stalk carries an explicit **Olog** (`Types`, deterministic `Functional Aspects`, and `Commutative Path Facts` $p \simeq q$), plus all extracted numbered definitions, propositions, theorems, applications, and examples from `cattheory.pdf`.
   - **1-Simplices (52 Restriction Morphisms $\rho_{U \to V} : \mathcal{O}(U) \to \mathcal{O}(V)$):** Explicit schema morphisms, functorial projections, and Kan data migrations ($\Sigma_F \dashv \Delta_F \dashv \Pi_F$) defining how overlapping concepts agree on intersections $U \cap V$.
   - **2-Simplices (8 Commutative Gluing Triangles $\tau_k$):** Higher coherence laws verifying $\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$ ($\delta^0 s = 0$ in Čech cohomology).

2. **Sheaf Gluing Query Protocol ($H^0(\mathcal{U}, \mathcal{O})$):**
   When you ask a Gemini Notebook-style question over a pinned **Open Cover** $\mathcal{U} = \{U_1, \dots, U_k\}$:
   - **Step 1 (Local Sections):** Extracts $s_i \in \mathcal{O}(U_i)$ from the relevant concept stalks and FTS5-indexed PDF pages.
   - **Step 2 (Overlap Restriction Check):** Computes pairwise overlaps $U_i \cap U_j$ and restriction maps $\rho_{U_i, U_i \cap U_j}(s_i) = \rho_{U_j, U_i \cap U_j}(s_j)$.
   - **Step 3 (Global Section Synthesis):** Glues the local sections via fiber products $\mathcal{O}(U \cup V) \cong \mathcal{O}(U) \times_{\mathcal{O}(U \cap V)} \mathcal{O}(V)$ into a globally consistent, page-cited synthesis.

---

## 2. Directory Map

| Path | Description |
|---|---|
| `../Category Theory Sheaf Knowledge Base - Notebook Studio.html` | **Interactive Studio (Root Launcher)** — Self-contained 4-mode Gemini Notebook Q&A + 3D Alexandrov Sheaf Site + Deep LLM Wiki + 609-Page Reader |
| `index.html` | Local copy of the interactive studio inside `cattheory-sheaf-kb/` |
| `cattheory.pdf` | Full 609-page PDF of Spivak's *Category Theory for the Sciences* |
| `data/sheaf_kb.json` | Complete structured JSON Sheaf Knowledge Base (609 pages, 877 formal items, 30 stalks, 52 restriction maps, 8 2-simplices) |
| `data/cattheory_sheaf.db` | SQLite + FTS5 full-text search & categorical database |
| `wiki/HOME.md` | Master entry hub of the Deep Markdown LLM Wiki |
| `wiki/chapters/*.md` | 7 Chapter Open-Cover Hub pages (`ch1`–`ch7`) |
| `wiki/concepts/*.md` | 30 Deep Concept Stalk Wiki pages with YAML frontmatter, Ologs, restriction maps, formal declarations, and page-by-page index |
| `build_sheaf_kb.py` | Reproducible PDF parser, sheaf builder, wiki generator & SQLite FTS5 indexer |
| `query_sheaf.py` | Command-line Gemini Notebook-style Sheaf Gluing Query Engine |
| `build_studio_html.py` | Compiler for the self-contained HTML Studio |

---

## 3. Command-Line Usage (`query_sheaf.py`)

```bash
# 1. Run full Čech cohomology & sheaf gluing audit across all 609 pages
python3 query_sheaf.py --gluing-audit

# 2. Ask a Gemini Notebook-style question across the Sheaf KB
python3 query_sheaf.py --ask "How does Spivak formalize a Sheaf of Ologged Concepts?"

# 3. Query over an explicit Open Cover U = {U_1, ..., U_k}
python3 query_sheaf.py --ask "How do pullbacks relate to right Kan extension Pi_F?" \
  --cover "pullbacks-and-fiber-products,data-migration-delta-sigma-pi"

# 4. Inspect a specific Concept Stalk (0-simplex) and its Olog + Restriction Maps
python3 query_sheaf.py --stalk "sheaves-and-local-to-global-gluing"

# 5. Inspect any exact PDF page (1..609)
python3 query_sheaf.py --page 520

# 6. Look up any of the 877 numbered formal declarations
python3 query_sheaf.py --item "Definition 7.2.3.5"
```
