# TYPED META-PROMPT CONTRACT: End-to-End Alexandrov Sheaf Knowledge Base, Persistent Wiki & CETI Field-Manual Studio

**Contract ID:** `CETI-SHEAF-PIPELINE-V2.0`  
**Status:** RATIFIED (`◆ 24/24 Binary Gates Cleared`)  
**Reference Implementation:** David I. Spivak, *Category Theory for the Sciences* (`cattheory.pdf`, 609 pp., 96 sections, 877 formal declarations, 30 concept stalks, 52 restriction morphisms, 8 commutative 2-simplices)  
**Skills Composed:**
1. [`sheaf-corpus-indexer`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-corpus-indexer/SKILL.md) — PDF Extraction, Alexandrov Topology, Local Ologs, SQLite FTS5, Persistent Wiki & MCP Server
2. [`sheaf-field-manual-studio`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-field-manual-studio/SKILL.md) — CETI `field-notebook-craft` & `meta-notebook` Interactive HTML Studio, LaTeX/Math Typesetter & Symbolic Visual Sandbox
3. [`sheaf-knowledge-pipeline`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-knowledge-pipeline/SKILL.md) — End-to-End Orchestrator & 3-Round A1–A4 MOE Adversarial Loop

---

## 0. Purpose & Architectural Law

This document is a **complete, self-contained Typed Contract and Executable Meta-Prompt** for transforming **any long-form technical book, scientific monograph, textbook, or regulatory/research PDF (`100–1,000+ pages`)** into:

1. **An Alexandrov Sheaf Knowledge Base ($\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$):**
   - Unlike flat vector RAG—which slices a book into arbitrary 500-token windows and destroys logical dependencies—this contract models a corpus as a topological poset $X$ of **Concept Stalks** ($U_i$), where each stalk carries a local categorical schema (**Olog**), a formal mathematical/logical core, and an exact **Page Fiber** ($p^{-1}(U_i) \subseteq \{1, \dots, P\}$).
   - **Restriction Morphisms ($\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$)** explicitly encode how terminology, definitions, and theorems translate across overlapping stalks $U \cap V$.
   - **The Sheaf Equalizer Gluing Law:** A multi-concept synthesis over an open cover $\mathcal{U} = \{U_i\}_{i \in I}$ is valid if and only if all local sections agree on pairwise intersections:
     $$\mathcal{O}\Bigl(\bigcup_{i \in I} U_i\Bigr) \xrightarrow{\sim} \text{eq}\Biggl( \prod_{i \in I} \mathcal{O}(U_i) \rightrightarrows \prod_{i, j \in I} \mathcal{O}(U_i \cap U_j) \Biggr)$$
2. **A Dual-Index Persistence Layer (`data/` + `wiki/`):**
   - `data/sheaf_kb.json` (canonical sheaf topology, stalks, Ologs, restrictions, 2-simplices, and verbatim pages),
   - `data/sheaf_pages_bundle.js` (deferred non-blocking browser bundle for `< 20ms` first paint on `file://` and `http://`),
   - `data/cattheory_sheaf.db` (SQLite FTS5 full-text search index over all verbatim pages and formal declarations),
   - `wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md` (persistent LLM Wiki with 1-to-1 stalk parity),
   - `query_sheaf.py` (deterministic local CLI + optional Gemini 2.5 live API synthesis + native JSON-RPC 2.0 `--mcp` stdio server).
3. **A CETI Field-Manual & Gemini Notebook Studio HTML Volume (`index.html`):**
   - Built on the CETI `field-notebook-craft` & `meta-notebook` design system: Warm Cream Paper (`#F5EFE3`), Deep Ink (`#1A1612`), Browning Copper (`#A67756`), `Fraunces` + `DM Sans` + `JetBrains Mono` typography, 5-axis ribbon, `Newcomer | Practitioner | Expert` progressive disclosure, `Cream | Ink` paper switcher, `.marginalia`, `.derived` bars, `.counterpoint` panels, and non-color-alone verdict stamps (`◆`, `⚖`, `✓`, `±`, `⊘`).
   - Includes a **7-Stage LaTeX & Symbolic Notation Typesetter** (`convertLatexTokensToHtml` + `renderRichMarkdown`) guaranteeing **zero raw LaTeX backslashes** in rendered output.
   - Features **5 Interactive Editorial Plates**:
     - **Plate I (`technology`):** Interactive 5-Stage Sheaf Query & Gluing Pipeline Rail,
     - **Plate II (`research`):** Open-Cover Gemini Notebook Gluing Studio + Dynamic Commutative Fiber-Product Olog SVG + Slide-Over Verbatim Book Reader,
     - **Plate III (`art`):** Interactive Symbol $\leftrightarrow$ Diagram Visual Sandbox (*"Illustrated Through Symbols"*),
     - **Plate IV (`science`):** Concept Stalks Encyclopedia + Formal Declarations Browser + On-Demand 3D Alexandrov Poset Fiber Bundle,
     - **Plate V (`teaching`):** Self-Contained Interactive Course & Curriculum Blueprint.

---

## 1. Typed Data Contracts (TypeScript / JSON Schema Specification)

Every artifact produced by this workflow MUST conform strictly to the following TypeScript / JSON Schema interfaces (enforced mechanically by `.agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py` and `.agents/skills/sheaf-corpus-indexer/references/sheaf-schema-contract.json`):

```typescript
/**
 * ============================================================================
 * CETI SHEAF KNOWLEDGE BASE — CANONICAL TYPED CONTRACT (v2.0)
 * ============================================================================
 */

export type StampVerdict =
  | "◆ ratified"
  | "⚖ measured"
  | "✓ accept"
  | "± refine"
  | "◐ partial"
  | "⊘ GATE";

export type AxisType = "research" | "technology" | "art" | "science" | "teaching";

export interface BookMetadata {
  title: string;                 // Full title of the book or monograph
  author: string;                // Primary author(s)
  year: number;                  // Publication year (1500..2100)
  publisher?: string;            // Publisher name
  source_url?: string;           // Canonical URL if fetched from web
  source_pdf: string;            // Relative path to local PDF on disk
  total_pages: number;           // Exact page count P of the PDF (must equal pages.length)
  total_sections: number;        // Count of extracted structural sections
  total_formal_items: number;    // Count of extracted numbered declarations (must equal formal_items.length)
  sheaf_definition: string;      // Formal sheaf functor signature, e.g. "O : Open(Alx(X^op))^op -> Sch ~ Cat"
}

export interface ChapterSpine {
  chapter: number;               // 1-indexed chapter number
  id: string;                    // Kebab-case slug, e.g. "ch7-sheaves-adjunctions"
  title: string;                 // Chapter title
  start_page: number;            // First PDF page of chapter
  end_page: number;              // Last PDF page of chapter
  theme: string;                 // 1-2 sentence synthesis of chapter scope
  global_invariants: string[];   // Conserved domain laws established in this chapter (>= 1)
}

export interface OlogType {
  id: string;                    // Short symbolic node ID within the local Olog (e.g. "S", "I", "Set")
  label: string;                 // Noun-phrase type label following Spivak's Olog rules ("a database schema")
}

export interface OlogAspect {
  src: string;                   // Must reference an existing OlogType.id in the same OlogSchema
  dst: string;                   // Must reference an existing OlogType.id in the same OlogSchema
  label: string;                 // Verb-phrase functional morphism label ("has canonical instance")
}

export interface OlogSchema {
  types: OlogType[];             // Minimum 2 typed objects per stalk
  aspects: OlogAspect[];         // Minimum 1 functional aspect arrow per stalk
  facts: string[];               // Minimum 1 path-equivalence equation or commuting invariant with [p. N]
}

export interface ConceptStalk {
  id: string;                    // Unique kebab-case identifier (0-simplex in Alexandrov poset X)
  title: string;                 // Human-readable concept stalk title
  chapter: number;               // Parent chapter number
  section: string;               // Book section identifier (e.g. "7.2.2")
  start_page: number;            // Lower bound of page fiber p^{-1}(U_i)
  end_page: number;              // Upper bound of page fiber p^{-1}(U_i)
  layer: "Foundations" | "Structure" | "Universal" | "Categorical" | "Synthesis" | string;
  symbol: string;                // LaTeX symbol for stalk (e.g. "U_{27}")
  summary: string;               // 2-4 sentence self-contained synthesis
  formal_core: string;           // Canonical LaTeX equation/signature enacted by this stalk
  olog: OlogSchema;              // Local categorical Ontology Log O(U_i)
  keywords: string[];            // Search & routing tokens (>= 2)
  extracted_items_count: number; // Number of formal declarations in this stalk's page fiber
  formal_items: FormalDeclaration[]; // Subset (or full list) of formal declarations in this stalk
  pos3d?: [number, number, number];  // Cylindrical 3D coordinates for the Alexandrov Poset Fiber Bundle
}

export interface RestrictionMorphism {
  id: string;                    // Unique morphism ID (e.g. "rho-42")
  source: string;                // Source ConceptStalk.id (U)
  target: string;                // Target ConceptStalk.id (V)
  kind: "specialization" | "adjunction-bridge" | "functorial-encoding" | "restriction" | string;
  overlap: string;               // Explicit description of shared structure in O(U ∩ V) (>= 10 chars)
  formula: string;               // LaTeX morphism formula (e.g. "\\rho_{U,V} : \\mathcal{O}(U) \\to \\mathcal{O}(V)")
}

export interface TwoSimplex {
  id: string;                    // Unique 2-simplex ID (e.g. "tau-01")
  title: string;                 // Name of commutative triangle
  vertices: [string, string, string]; // Ordered triple [U, V, W] of valid ConceptStalk.id values
  law: string;                   // Commutativity law: rho_{V,W} o rho_{U,V} = rho_{U,W}
  cohomology_status: string;     // Must verify "H^0 Exact (Zero Obstruction)"
}

export interface CitationRef {
  page: number;                  // Verbatim PDF page number (1 <= page <= book.total_pages)
  item: string;                  // Formal declaration ID (e.g. "Definition 7.2.2.2")
  label: string;                 // Concept or theorem label
}

export interface NotebookInvestigation {
  id: string;                    // Kebab-case investigation ID
  question: string;              // Deep cross-chapter research question
  open_cover: string[];          // Array of >= 2 ConceptStalk.id values forming the open cover U
  cohomology: {
    h0_coherence: number;        // Measured coherence score in [0.0, 1.0]
    h1_obstruction: number;      // Cocycle obstruction (must be 0.0 for ratified global sections)
    gluing_status: string;       // Status banner text
  };
  synthesis_markdown: string;    // Multi-section synthesis with $...$, $$...$$, and [p. N] citations
  citations: CitationRef[];      // Grounded page & theorem citations
}

export interface FormalDeclaration {
  id: string;                    // e.g. "Definition 7.2.2.2" or "Theorem 4.5.1.6"
  kind: "Definition" | "Theorem" | "Proposition" | "Lemma" | "Corollary" | "Example" | "Application" | "Remark" | "Exercise" | string;
  number: string;                // Hierarchical number string, e.g. "7.2.2.2"
  title?: string;                // Optional named title of declaration
  page: number;                  // Exact PDF page where declaration begins (1..P)
  chapter: number;               // Chapter number
  section: string;               // Section header string
  stalk_ids: string[];           // Non-empty array of ConceptStalk.id values containing this item
  text: string;                  // Verbatim extracted statement text
  references: string[];          // Cross-referenced item numbers within statement
}

export interface VerbatimPage {
  p: number;                     // 1-indexed PDF page number (1..P)
  ch: number;                    // Active chapter number
  sec: string;                   // Active section header
  wc: number;                    // Word count on page
  stalks: string[];              // ConceptStalk.id values covering this page
  items: string[];               // FormalDeclaration.id values starting on this page
  refs: string[];                // Cross-references detected on this page
  txt: string;                   // Full verbatim extracted text of the PDF page
}

export interface SheafKnowledgeBase {
  book: BookMetadata;
  chapters: ChapterSpine[];
  stalks: ConceptStalk[];
  restriction_morphisms: RestrictionMorphism[];
  two_simplices: TwoSimplex[];
  notebook_investigations: NotebookInvestigation[];
  formal_items: FormalDeclaration[];
  pages: VerbatimPage[];
}
```

---

## 2. The End-to-End Meta-Prompt (Copy-Pasteable Orchestrator Prompt)

Use the following **Master Meta-Prompt** to execute this entire workflow end-to-end on any new book, textbook, or research PDF:

```markdown
# SYSTEM META-PROMPT: Alexandrov Sheaf Knowledge Base & CETI Field-Manual Studio Builder

You are executing the **CETI Sheaf Knowledge Pipeline (`CETI-SHEAF-PIPELINE-V2.0`)** on a target long-form PDF document.
Your objective is to transform the target PDF into a mathematically verified **Alexandrov Sheaf Knowledge Base**, a **Persistent LLM Wiki**, a **SQLite FTS5 + MCP Query Engine**, and a **CETI Field-Manual & Gemini Notebook Studio HTML Volume** with an interactive **"Illustrated Through Symbols"** visual curriculum.

## INPUT PARAMETERS
- `TARGET_PDF_PATH`: {path_to_pdf_or_url}
- `BOOK_TITLE`: {title}
- `BOOK_AUTHOR`: {author}
- `BOOK_YEAR`: {year}
- `OUTPUT_DIR`: {output_directory_slug}
- `COURSE_TITLE`: "{Domain} Illustrated: Through Symbols & Commuting Diagrams"

## NON-NEGOTIABLE INVARIANTS
1. **100% Verbatim Page & Declaration Fidelity:** Extract every page (1..P) verbatim and every numbered formal declaration (`Definition`, `Theorem`, `Proposition`, `Lemma`, `Example`, `Application`, `Exercise`, `Principle`, `Rule`). Never invent a page number, citation, or theorem.
2. **100% Body-Page Sheaf Coverage (`HF-SHEAF-02`):** Partition the book's body pages into 20–40 Concept Stalks (`0-simplices` $U_i \in X$) so that every body page belongs to at least one stalk ($p^{-1}(U_i)$).
3. **Referentially Intact Local Ologs (`HF-SHEAF-04`):** Every Concept Stalk $U_i$ must carry a valid local Ontology Log (`olog.types` >= 2, `olog.aspects` >= 1 with `src`/`dst` in `types`, `olog.facts` >= 1 with `[p. N]` citation) and a LaTeX `formal_core`.
4. **Connected Restriction Poset & 2-Simplices (`HF-SHEAF-05..07`):** Wire >= |Stalks| restriction morphisms $\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$ with explicit `formula` and `overlap` fields so the poset $X$ is a single connected component, plus >= 5 commutative 2-simplices $[U,V,W]$ verifying $\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$.
5. **Fast-Load Split Bundle (`HF-STUDIO-02`):** Never embed multi-megabyte full-page arrays synchronously inside the main HTML file. Keep the core studio HTML `< 450 KB` and load all verbatim pages + formal declarations asynchronously via `<script defer src="data/sheaf_pages_bundle.js">`.
6. **Zero Raw LaTeX Leakage (`HF-STUDIO-03`):** Route all mathematical strings (`$$...$$`, `$...$`, backticked LaTeX, `formal_core`, `formula`) through the 7-stage `convertLatexTokensToHtml` + `renderRichMarkdown` parser so zero raw LaTeX backslashes (`\mathcal`, `\mathbf`, `\varprojlim`, `\xrightarrow`, `\dashv`, `\simeq`, `\cong`) appear in the rendered DOM.
7. **CETI Field-Manual & FORGE Courseware Craft (`HF-STUDIO-01, 04..08`):**
   - Use Warm Cream Paper (`#F5EFE3`), Deep Ink (`#1A1612`), Browning Copper (`#A67756`), and 3-voice typography (`Fraunces` italic display, `DM Sans` body, `JetBrains Mono` apparatus).
   - Include all 5 Editorial Plates (`I · Architecture`, `II · Notebook Gluing Studio`, `III · Symbolic Visual Sandbox`, `IV · Corpus Observed & 3D Poset`, `V · Course Blueprint`).
   - Every plate title must put its core concept noun in `<em class="u-copper">...</em>`.
   - Every plate must carry a `.marginalia` block (quoting a real author with `<cite>`) and a `.counterpoint` block ("when this is the wrong tool / where this breaks").
   - Every stamp must pair a glyph (`◆`, `⚖`, `✓`, `±`, `⊘`) with a text label (never color alone).
   - Course module cards must use self-contained titles (no `"Module 1"` numbering on learner surfaces), use only `Key Concept` and `Why It Matters` callouts (never `"So What"`), and never stack two `.callout-box` elements without intervening content.

## EXECUTION PHASES (DO NOT ADVANCE UNTIL EXIT GATES PASS)

### PHASE 1: Corpus Extraction, Alexandrov Sheaf Indexing & Persistent Wiki (`sheaf-corpus-indexer`)
1. Run or customize `build_sheaf_kb.py` / `.agents/skills/sheaf-corpus-indexer/scripts/extract_and_index_pdf.py` to generate:
   - `{OUTPUT_DIR}/data/sheaf_kb.json`
   - `{OUTPUT_DIR}/data/sheaf_pages_bundle.js`
   - `{OUTPUT_DIR}/data/cattheory_sheaf.db` (SQLite FTS5)
   - `{OUTPUT_DIR}/wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`
   - `{OUTPUT_DIR}/query_sheaf.py` (with `--ask`, `--gluing-audit`, `--stalk`, `--page`, and `--mcp` JSON-RPC 2.0 server mode)
2. Run the deterministic contract validator:
   `python3 .agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py --kb {OUTPUT_DIR}/data/sheaf_kb.json`
   **Exit Gate:** `HF-SHEAF-01` through `HF-SHEAF-12` must all be `CLEARED`.

### PHASE 2: CETI Field-Manual Studio & Symbolic Sandbox Compilation (`sheaf-field-manual-studio`)
1. Run or customize `build_studio_html.py` / `.agents/skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py` to compile the 5-Plate interactive HTML volume (`{OUTPUT_DIR}/index.html` and top-level studio HTML).
2. Run the deterministic HTML & LaTeX auditor:
   `python3 .agents/skills/sheaf-field-manual-studio/scripts/audit_rendered_html.py --html {STUDIO_HTML} --kb {OUTPUT_DIR}/data/sheaf_kb.json`
   **Exit Gate:** `HF-STUDIO-01` through `HF-STUDIO-10` must all be `CLEARED`.

### PHASE 3: Recursive A1–A4 MOE Adversarial Evaluation Loop (`sheaf-knowledge-pipeline`)
1. Run the unified 24-gate MOE audit across Evaluators A1 (Depth/Cohomology), A2 (Performance/FTS5/MCP), A3 (Field-Manual/Math/Symbolic Craft), and A4 (Citations/Page-Fibers/Wiki):
   `python3 .agents/skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py`
2. Execute >= 3 recursive evaluation-and-repair rounds (`R1 -> R2 -> R3`), logging every defect found and repaired until `24/24` binary gates are `CLEARED` (`overall_ship_vote == "GO"`).
3. Record durable findings in `wiki/qc-memory/` and append a row to `wiki/LEDGER.md`.
```

---

## 3. Complete 24-Gate Binary Hard-Fail Matrix (`HF-*`)

| Gate ID | Evaluator | Invariant Tested | Verification Method |
|---|---|---|---|
| `HF-SHEAF-01` | **A1** | Top-level schema keys & `len(pages) == book.total_pages` | `validate_sheaf_contract.py` |
| `HF-SHEAF-02` | **A1** | 100.0% of body pages covered by $\ge 1$ Concept Stalk | `validate_sheaf_contract.py` |
| `HF-SHEAF-03` | **A1** | Stalk IDs unique ($\ge 10$) and page intervals valid | `validate_sheaf_contract.py` |
| `HF-SHEAF-04` | **A1** | Local Olog referential integrity (`src`/`dst` in `olog.types`) | `validate_sheaf_contract.py` |
| `HF-SHEAF-05` | **A1** | Global poset connectivity via restriction morphisms $\rho_{U,V}$ | `validate_sheaf_contract.py` |
| `HF-SHEAF-06` | **A1** | Non-empty `formula` and `overlap` on all restriction morphisms | `validate_sheaf_contract.py` |
| `HF-SHEAF-07` | **A1** | Commutative 2-simplices (`two_simplices`) form connected triangles | `validate_sheaf_contract.py` |
| `HF-SHEAF-08` | **A4** | All formal declarations have valid page numbers & `stalk_ids` | `validate_sheaf_contract.py` |
| `HF-SHEAF-09` | **A4** | Pre-glued `notebook_investigations` have valid covers & citations | `validate_sheaf_contract.py` |
| `HF-SHEAF-10` | **A2** | Deferred browser bundle `sheaf_pages_bundle.js` exists & valid | `validate_sheaf_contract.py` |
| `HF-SHEAF-11` | **A2** | SQLite FTS5 tables (`pages_fts`, `formal_items_fts`) row parity | `validate_sheaf_contract.py` |
| `HF-SHEAF-12` | **A4** | Persistent Markdown Wiki (`HOME.md`, `chapters/`, `concepts/`) parity | `validate_sheaf_contract.py` |
| `HF-STUDIO-01` | **A3** | CETI Field-Manual palette (`#F5EFE3`, `#1A1612`, `#A67756`) & fonts | `audit_rendered_html.py` |
| `HF-STUDIO-02` | **A2** | Core HTML `< 450 KB` + `<script defer>` split-bundle architecture | `audit_rendered_html.py` |
| `HF-STUDIO-03` | **A3** | Zero raw LaTeX backslash leaks in static DOM & rendered KB strings | `audit_rendered_html.py` |
| `HF-STUDIO-04` | **A3** | All 5 Editorial Plates (`#plate-1..5`) + `.u-copper` italic nouns | `audit_rendered_html.py` |
| `HF-STUDIO-05` | **A3** | Every Plate has `.marginalia` (with `<cite>`) and `.counterpoint` | `audit_rendered_html.py` |
| `HF-STUDIO-06` | **A3** | Non-color-alone verdict stamps (`◆`, `⚖`, `✓`, `±`, `⊘` + text) | `audit_rendered_html.py` |
| `HF-STUDIO-07` | **A1** | Single-mutator interactive instruments + on-demand 3D Poset loop | `audit_rendered_html.py` |
| `HF-STUDIO-08` | **A3** | FORGE rules (`Key Concept`/`Why It Matters`, no `So What`, no stacked callouts, no `Module N` titles) | `audit_rendered_html.py` |
| `HF-STUDIO-09` | **A2** | Progressive Depth (`Newcomer|Practitioner|Expert`) & Paper switches | `audit_rendered_html.py` |
| `HF-STUDIO-10` | **A4** | Slide-Over Verbatim Book Reader Drawer + `__jumpToPage` citations | `audit_rendered_html.py` |
| `HF-MCP-01` | **A2** | JSON-RPC 2.0 `--mcp` stdio server responds with 3 sheaf tools | `run_sheaf_pipeline_audit.py` |
| `HF-CONTRACT-01` | **A2** | Master Typed Meta-Prompt Contract present & complete on disk | `run_sheaf_pipeline_audit.py` |
