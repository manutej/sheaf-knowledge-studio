# Olog & Alexandrov Stalk Extraction Guide

This reference defines the mathematical and engineering discipline for turning any long-form technical book, scientific monograph, or regulatory/research PDF into an **Alexandrov Sheaf Knowledge Base** ($\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$).

---

## 1. Why a Sheaf Instead of Flat Vector RAG?

Flat RAG slices a 600-page book into arbitrary 500-token chunks, embeds them in $\mathbb{R}^d$, and retrieves top-$k$ cosine neighbors. That breaks down on dense technical and mathematical texts because:
1. **Context Stripping:** A theorem on page 483 depends on a definition on page 253 and a notation convention on page 47.
2. **Broken Commutativity:** Combining two chunks from incompatible assumptions produces hallucinated synthesis.
3. **Zero Structural Audit:** Vector similarity cannot tell you *how* two concepts translate into one another or *where* they agree on their overlap.

In an **Alexandrov Sheaf Knowledge Base**:
- **Base Space ($X$):** A finite poset of **Concept Stalks** ($U_1, \dots, U_N$) ordered by conceptual specialization/dependency.
- **Open Sets ($\text{Open}(\text{Alx}(X^{\text{op}}))$):** Downward-closed subsets $\mathcal{U} \subseteq X$ (any concept stalk automatically pulls in the foundational stalks it depends upon).
- **Local Section ($\mathcal{O}(U_i)$):** Each stalk carries:
  - A **Formal Mathematical/Logical Core** (`formal_core`),
  - A **Local Ontology Log (`olog`)** consisting of typed objects (`types`), functional arrows (`aspects`), and path-equivalence axioms (`facts`),
  - A **Page Fiber** ($p^{-1}(U_i) \subseteq \{1, \dots, P\}$) of verbatim pages and extracted formal declarations (`Definition`, `Theorem`, `Proposition`, `Example`, `Claim`).
- **Restriction Morphisms ($\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$):** Explicit typed translations specifying how two stalks agree on their conceptual intersection $U \cap V$.
- **Sheaf Gluing Condition (Equalizer Axiom):**
  $$\mathcal{O}\Bigl(\bigcup_{i \in I} U_i\Bigr) \xrightarrow{\sim} \text{eq}\Biggl( \prod_{i \in I} \mathcal{O}(U_i) \rightrightarrows \prod_{i, j \in I} \mathcal{O}(U_i \cap U_j) \Biggr)$$
  A notebook synthesis across an open cover $\mathcal{U} = \{U_i\}$ is valid if and only if the local claims agree under all restriction morphisms $\rho_{U_i, U_i \cap U_j}$.

---

## 2. Step-by-Step Extraction Protocol for Any Book

### Step 1: Verbatim Page & Structural Spine Extraction
Run `scripts/extract_and_index_pdf.py` to extract:
1. Every page `1..P` verbatim (`txt`, word count `wc`, active chapter `ch`, active section header `sec`).
2. Every numbered formal declaration via domain-aware regex patterns:
   - **Mathematical / CS Texts:** `Definition`, `Theorem`, `Proposition`, `Lemma`, `Corollary`, `Example`, `Application`, `Remark`, `Exercise`, `Algorithm`.
   - **Scientific / Engineering Manuals:** `Principle`, `Law`, `Protocol`, `Specification`, `Experiment`, `Assay`, `Invariant`, `Case Study`.
   - **Legal / Financial / Regulatory Corpora:** `Statute`, `Section`, `Rule`, `Doctrine`, `Holding`, `Standard`, `Schedule`.

### Step 2: Designing the 20–40 Concept Stalks (`0-Simplices`)
Partition the book's body pages (`start_page` to `end_page` of main content) into **20 to 40 Concept Stalks** so that:
- **100% Body Page Coverage (`HF-SHEAF-02`):** Every body page belongs to at least one Concept Stalk (`covered_body_pages == total_body_pages`).
- **Local Olog Completeness (`HF-SHEAF-04`):** Every stalk $U_i$ defines:
  - `types`: $\ge 3$ typed entities (e.g., `{"id": "S", "label": "a database schema"}`),
  - `aspects`: $\ge 2$ directed functional arrows with source and target existing in `types` (`src`, `dst`, `label`),
  - `facts`: $\ge 1$ prose/symbolic commuting law or domain invariant with a `[p. N]` citation.

### Step 3: Wiring Restriction Morphisms (`1-Simplices`) & `2-Simplices`
- **Connected Poset Graph (`HF-SHEAF-05`):** Every stalk $U_i$ must participate in at least one restriction morphism $\rho_{U,V}$ (`source` or `target`), and the undirected underlying graph of stalks must be a single connected component.
- **Explicit Overlap & Formula (`HF-SHEAF-06`):** Every restriction morphism must specify both `formula` (the symbolic/structural map) and `overlap` (the exact shared concepts in $\mathcal{O}(U \cap V)$).
- **2-Simplex Coherence (`HF-SHEAF-07`):** Define $\ge 5$ commutative triangles (`two_simplices`) $[U, V, W]$ where $\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$ holds with zero cocycle obstruction ($\delta^0 s = 0$).

### Step 4: Compiling Curated Global Section Investigations
Pre-compute $\ge 5$ deep **Notebook Investigations** (`notebook_investigations`) that demonstrate global section gluing across multi-stalk open covers, with inline `[p. N]` citations and typeset LaTeX/symbolic formulas.
