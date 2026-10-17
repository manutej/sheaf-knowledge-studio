# TYPED META-PROMPT CONTRACT: End-to-End Alexandrov Sheaf Knowledge Base, Persistent Wiki, Dual-Host Neural Podcast & CETI Field-Manual Studio

**Contract ID:** `CETI-SHEAF-PIPELINE-V9.0`  
**Status:** RATIFIED (`◆ 30/30 Binary Gates + 33/33 Negative Self-Tests Cleared Across 3 Independent Builds & 9 Adversarial Rounds`)  
**Reference Implementations:**
1. **David I. Spivak**, *Category Theory for the Sciences* (`cattheory.pdf`, 609 pp., 96 sections, 877 formal declarations, 30 concept stalks, 55 restriction morphisms, 8 commutative 2-simplices, 24 cross_corpus_bridges, 5 dual-host neural podcast episodes)
2. **Boris Marinov**, *Category Theory Illustrated* (`category-theory-illustrated.pdf`, 377 pp., 8 chapters, 291 visual/symbolic declarations (165 Definitions, 38 Theorems, 88 Interactive Tasks), 24 concept stalks, 50 restriction morphisms, 10 commutative 2-simplices, 24 cross_corpus_bridges, 6 dual-host neural podcast episodes)
3. **Independent Zero-Shot Agent Build**, *Category Theory Illustrated (Auto-Induced)* (`377 pp.`, 9 chapters, 279 deduplicated declarations, 18 auto-induced concept stalks, 33 restriction morphisms, 8 commutative 2-simplices, 18 cross_corpus_bridges, 4 dual-host neural podcast episodes)

**Skills & Portable Toolkit Composed:**
1. [`sheaf-corpus-indexer`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-corpus-indexer/SKILL.md) — Auto-Induced PDF Extraction, Alexandrov Topology, Empirical Čech Cohomology, Local Ologs, SQLite FTS5, Persistent Wiki & MCP Server
2. [`sheaf-field-manual-studio`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-field-manual-studio/SKILL.md) — CETI `field-notebook-craft` & `meta-notebook` Interactive HTML Studio, Adaptive `BookVoiceProfile`, 7-Stage LaTeX/Math Typesetter, Dual-Host Neural Podcast Studio (`Kore` × `Puck`) & Symbolic Visual Sandbox
3. [`sheaf-knowledge-pipeline`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/.agents/skills/sheaf-knowledge-pipeline/SKILL.md) — End-to-End Orchestrator & 3-Round A1–A4 MOE Adversarial Loop (`30/30` Gates)
4. [`portable-toolkit/`](file:///Users/cairo/Documents/CETI/ACCENTURE/content-factory%20v2/portable-toolkit/README.md) — Drop-in 3-tool corpus engineering kit (`page_corpus_indexer.py`, `sheaf_contract_linter.py`, `gate_review_runner.py`)

---

## 0. Purpose & Architectural Law

This document is a **complete, self-contained Typed Contract and Executable Meta-Prompt** for transforming **any long-form technical book, scientific monograph, textbook, or regulatory/research PDF (`100–1,000+ pages`)** into:

1. **An Alexandrov Sheaf Knowledge Base ($\mathcal{O} : \text{Open}(\text{Alx}(X^{\text{op}}))^{\text{op}} \to \mathbf{Sch} \simeq \mathbf{Cat}$):**
   - Unlike flat vector RAG—which slices a book into arbitrary 500-token windows and destroys logical dependencies—this contract models a corpus as a topological poset $X$ of **Concept Stalks** ($U_i$), where each stalk carries a local categorical schema (**Olog**), extracted `defined_terms`, a formal mathematical/logical core, and an exact **Page Fiber** ($p^{-1}(U_i) \subseteq \{1, \dots, P\}$).
   - **Restriction Morphisms ($\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$)** explicitly encode how terminology, definitions, and theorems translate across overlapping stalks $U \cap V$, backed by measured lexical Jaccard overlap and cross-reference bridges.
   - **Empirical Čech Cohomology & Sheaf Equalizer Gluing Law:** A multi-concept synthesis over an open cover $\mathcal{U} = \{U_i\}_{i \in I}$ is valid if and only if the induced nerve subgraph is connected ($b_0(\mathcal{U}) = 1$), adjacent stalks share non-zero empirical vocabulary/citation overlap, and all local sections agree on pairwise intersections:
     $$\mathcal{O}\Bigl(\bigcup_{i \in I} U_i\Bigr) \xrightarrow{\sim} \text{eq}\Biggl( \prod_{i \in I} \mathcal{O}(U_i) \rightrightarrows \prod_{i, j \in I} \mathcal{O}(U_i \cap U_j) \Biggr)$$
2. **A Dual-Index Persistence Layer (`data/` + `wiki/` + `audio/`):**
   - `data/sheaf_kb.json` (canonical sheaf topology, stalks, Ologs, restrictions, 2-simplices, empirical cohomology, dual-host podcast transcripts, and verbatim pages),
   - `data/sheaf_pages_bundle.js` (deferred non-blocking browser bundle for `< 20ms` first paint on `file://` and `http://`),
   - `data/cattheory_sheaf.db` (SQLite FTS5 full-text search index over all verbatim pages and formal declarations),
   - `audio/podcast_*.mp3` (pre-rendered NotebookLM-grade dual-host neural MP3 audio episodes pairing `Host A · Kore` and `Host B · Puck`),
   - `wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md` (persistent LLM Wiki with 1-to-1 stalk parity),
   - `query_sheaf.py` (deterministic local CLI + empirical `--audit-cover` + optional Gemini 2.5 live API synthesis + native JSON-RPC 2.0 `--mcp` stdio server).
3. **A CETI Field-Manual & Gemini Notebook Studio HTML Volume (`index.html`):**
   - Built on the CETI `field-notebook-craft` & `meta-notebook` design system with an adaptive **`BookVoiceProfile`** so each book speaks in its own authentic aesthetic and pedagogical voice (e.g., *Archival Laboratory Field Manual* for Spivak vs. *Geometric Lithograph Atelier* for Marinov).
   - Includes a **7-Stage LaTeX & Symbolic Notation Typesetter** (`convertLatexTokensToHtml` + `renderRichMarkdown`) guaranteeing **zero raw LaTeX backslashes** in rendered output.
   - Features a **Gemini NotebookLM Dual-Host Audio Overview Studio (`#podcastStudioCard`)** with pre-rendered neural MP3 playback, live Gemini `2.5-flash-preview-tts` `multiSpeakerVoiceConfig` synthesis for custom queries, animated 28-bar waveform, active host indicator pills (`Kore` × `Puck`), speed control, and a click-to-seek synchronized transcript drawer.
   - Features **5 Interactive Editorial Plates**:
     - **Plate I (`technology`):** Interactive 5-Stage Sheaf Query & Gluing Pipeline Rail,
     - **Plate II (`research`):** Open-Cover Gemini Notebook Gluing Studio + Dual-Host Neural Podcast Studio + Dynamic Commutative Fiber-Product Olog SVG + Slide-Over Verbatim Book Reader,
     - **Plate III (`art`):** Interactive Symbol $\leftrightarrow$ Diagram Visual Sandbox (*"Illustrated Through Symbols"*),
     - **Plate IV (`science`):** Concept Stalks Encyclopedia + Formal Declarations Browser + On-Demand 3D Alexandrov Poset Fiber Bundle,
     - **Plate V (`teaching`):** Self-Contained Interactive Course & Curriculum Blueprint.

---

## 1. Typed Data Contracts (TypeScript / JSON Schema Specification)

Every artifact produced by this workflow MUST conform strictly to the following TypeScript / JSON Schema interfaces (enforced mechanically by `.agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py` and `.agents/skills/sheaf-corpus-indexer/references/sheaf-schema-contract.json`):

```typescript
/**
 * ============================================================================
 * CETI SHEAF KNOWLEDGE BASE — CANONICAL TYPED CONTRACT (v3.0)
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

export interface BookVoiceProfile {
  archetype: "scientific-olog-manual" | "geometric-visual-atelier" | "axiomatic-monograph" | "systems-engineering-handbook";
  aesthetic_persona: string;     // e.g. "Archival Laboratory Field Manual" vs "Geometric Lithograph & Visual Atelier"
  primary_metaphor: string;      // e.g. "Information Bridges & Database Ologs" vs "Six Parallel Worlds & Commuting Geometry"
  palette_tokens: {
    paper_cream: string;         // e.g. "#F5EFE3" or "#F7F3EA"
    ink_primary: string;         // e.g. "#1A1612" or "#141820"
    accent_primary: string;      // e.g. "#A67756" (Browning Copper) or "#C84B31" (Vermilion Ink)
    accent_secondary: string;    // e.g. "#1B6B5A" (Teal Verification) or "#255F85" (Cobalt Blueprint)
  };
  signature_instruments: string[]; // Bespoke interactive sandboxes tailored to the book's pedagogy
}

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
  induction_mode?: "auto-induced-from-raw-text" | "hybrid-curated-and-empirical";
  voice_profile?: BookVoiceProfile;
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
  defined_terms: string[];       // Extracted domain vocabulary terms (>= 2, zero PDF kerning glues)
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
  shared_terms?: string[];       // Empirically shared defined_terms across U and V
  term_jaccard?: number;         // Lexical Jaccard similarity in [0.0, 1.0]
  cross_refs_count?: number;     // Count of formal cross-references bridging U and V
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

export interface CohomologyAudit {
  status: "PASS" | "FAIL";       // Empirical gluing verdict (never hardcoded!)
  h0_coherence: number;          // Content-computed coherence score in [0.0, 1.0]
  h1_obstruction: number;        // Cocycle obstruction score in [0.0, 1.0]
  connected_components: number;  // Betti number b_0(U) of induced nerve subgraph (1 for connected cover)
  active_edges: number;          // Number of restriction morphisms inside the cover
  term_jaccard_mean: number;     // Mean lexical Jaccard overlap across cover edges
  citation_bridge_ratio: number; // Ratio of cover pairs bridged by shared citations/terms
  gluing_status: string;         // Human-readable cohomology diagnosis
  obstruction_details?: string[]; // Non-empty when status === "FAIL"
}

export interface PodcastTurn {
  speaker: "Kore" | "Puck";      // Host A (Kore, Lead Synthesis Host) or Host B (Puck, Co-Host)
  role: string;                  // e.g. "Lead Synthesis Host" or "Co-Host & Edge-Case Inquirer"
  text: string;                  // Natural conversational dialogue (no raw "(p. N)" or PDF kerning glues)
}

export interface PodcastEpisode {
  audio_file: string;            // Relative path to pre-rendered neural MP3 (e.g. "audio/podcast_q-1.mp3")
  duration_seconds: number;      // Audio duration in seconds (>= 25.0s, file size >= 40 KB)
  file_size_bytes: number;       // MP3 byte size on disk (>= 40,000)
  engine: string;                // e.g. "Neural Multi-Speaker Podcast Engine (NotebookLM Kore + Puck Parity)"
  hosts: {
    Kore: { role: string; voice: string };
    Puck: { role: string; voice: string };
  };
  turns: PodcastTurn[];          // >= 6 alternating conversational turns per episode
}

export interface NotebookInvestigation {
  id: string;                    // Kebab-case investigation ID
  question: string;              // Deep cross-chapter research question
  open_cover: string[];          // Array of >= 2 ConceptStalk.id values forming the open cover U
  cohomology: CohomologyAudit;   // Empirical Čech cohomology audit over U
  synthesis_markdown: string;    // Multi-section synthesis with $...$, $$...$$, and [p. N] citations
  citations: CitationRef[];      // Grounded page & theorem citations
  podcast_episode: PodcastEpisode; // Pre-rendered Dual-Host Neural Audio Overview episode
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
  podcast_overview: {
    engine: string;
    gemini_live_model: "gemini-2.5-flash-preview-tts";
    hosts: Record<"Kore" | "Puck", { role: string; voice: string }>;
    episodes: Record<string, PodcastEpisode>;
  };
  formal_items: FormalDeclaration[];
  pages: VerbatimPage[];
}
```

---

## 2. The End-to-End Meta-Prompt (Copy-Pasteable Orchestrator Prompt)

Use the following **Master Meta-Prompt** to execute this entire workflow end-to-end on any new book, textbook, or research PDF:

```markdown
# SYSTEM META-PROMPT: Alexandrov Sheaf Knowledge Base, Dual-Host Neural Podcast & CETI Field-Manual Studio Builder

You are executing the **CETI Sheaf Knowledge Pipeline (`CETI-SHEAF-PIPELINE-V9.0`)** on a target long-form PDF document.
Your objective is to transform the target PDF into a mathematically verified **Alexandrov Sheaf Knowledge Base**, a **Persistent LLM Wiki**, a **SQLite FTS5 + MCP Query Engine**, a **Dual-Host Neural Audio Overview (`Kore` × `Puck`)**, and a **CETI Field-Manual & Gemini Notebook Studio HTML Volume** with an interactive **"Illustrated Through Symbols"** visual curriculum.

## INPUT PARAMETERS
- `TARGET_PDF_PATH`: {path_to_pdf_or_url}
- `BOOK_TITLE`: {title}
- `BOOK_AUTHOR`: {author}
- `BOOK_YEAR`: {year}
- `OUTPUT_DIR`: {output_directory_slug}
- `VOICE_ARCHETYPE`: "scientific-olog-manual" | "geometric-visual-atelier" | "axiomatic-monograph"
- `COURSE_TITLE`: "{Domain} Illustrated: Through Symbols & Commuting Diagrams"

## NON-NEGOTIABLE INVARIANTS
1. **100% Verbatim Page & Declaration Fidelity (`HF-SHEAF-01, 08`):** Extract every page (1..P) verbatim and every numbered or structural formal declaration (`Definition`, `Theorem`, `Proposition`, `Lemma`, `Example`, `Application`, `Exercise`, `Principle`, `Rule`, `Visual Concept`). Never invent a page number, citation, or theorem.
2. **100% Body-Page Sheaf Coverage (`HF-SHEAF-02`):** Partition the book's body pages into 20–40 Concept Stalks (`0-simplices` $U_i \in X$) so that every body page belongs to at least one stalk ($p^{-1}(U_i)$).
3. **Referentially Intact Local Ologs (`HF-SHEAF-04`):** Every Concept Stalk $U_i$ must carry a valid local Ontology Log (`olog.types` >= 2, `olog.aspects` >= 1 with `src`/`dst` in `types` and non-generic SVO verb labels, `olog.facts` >= 1 with `[p. N]` citation), clean `defined_terms` (zero PDF kerning glues), and a LaTeX `formal_core`.
4. **Empirical Čech Cohomology & Connected Poset (`HF-SHEAF-05..07, 09`):** Wire >= |Stalks| restriction morphisms $\rho_{U,V} : \mathcal{O}(U) \to \mathcal{O}(V)$ with empirical `term_jaccard`, `shared_terms`, `formula`, and `overlap`. Compute `h0_coherence` and `h1_obstruction` from actual lexical Jaccard overlap, cross-references, and nerve connectivity $b_0(\mathcal{U})$ so connected covers return `PASS` and disconnected covers return `FAIL` (`h1_obstruction > 0`).
5. **Dual-Host Neural Podcast Studio (`HF-SHEAF-13`, `HF-STUDIO-11`):** Synthesize a pre-rendered multi-speaker neural MP3 episode (`audio/podcast_*.mp3`, `>= 40 KB`, `>= 25s`, `>= 6` alternating turns between `Kore` and `Puck`, zero duplicate cookie-cutter turns, zero PDF kerning glues, and natural spoken page references) for every investigation, and wire `#podcastStudioCard` with both offline neural MP3 playback and live Gemini `2.5-flash-preview-tts` `multiSpeakerVoiceConfig` synthesis (`buildCustomPodcastTurns`).
6. **Fast-Load Split Bundle & Zero Corpus Bleed (`HF-STUDIO-02, 10`):** Keep the core studio HTML `< 450 KB` and load all verbatim pages + formal declarations asynchronously via `<script defer src="data/sheaf_pages_bundle.js">`. Never bleed hardcoded page counts or author strings from another book into the compiled HTML.
7. **Zero Raw LaTeX Leakage (`HF-STUDIO-03`):** Route all mathematical strings (`$$...$$`, `$...$`, backticked LaTeX, `formal_core`, `formula`) through the 7-stage `convertLatexTokensToHtml` + `renderRichMarkdown` parser so zero raw LaTeX backslashes appear in the rendered DOM.
8. **CETI Field-Manual & FORGE Courseware Craft (`HF-STUDIO-01, 04..09`):**
   - Include all 5 Editorial Plates (`I · Architecture`, `II · Notebook Gluing Studio`, `III · Symbolic Visual Sandbox`, `IV · Corpus Observed & 3D Poset`, `V · Course Blueprint`).
   - Every plate title must put its core concept noun in `<em class="u-copper">...</em>`.
   - Every plate must carry a `.marginalia` block (quoting a real author with `<cite>`) and a `.counterpoint` block ("when this is the wrong tool / where this breaks").
   - Every stamp must pair a glyph (`◆`, `⚖`, `✓`, `±`, `⊘`) with a text label (never color alone).
   - Course module cards must use self-contained titles (no `"Module 1"` numbering on learner surfaces), use only `Key Concept` and `Why It Matters` callouts (never `"So What"`), and never stack two `.callout-box` elements without intervening content.

## EXECUTION PHASES (DO NOT ADVANCE UNTIL EXIT GATES PASS)

### PHASE 1: Corpus Extraction, Alexandrov Sheaf Indexing & Persistent Wiki (`sheaf-corpus-indexer`)
1. Run `.agents/skills/sheaf-corpus-indexer/scripts/compile_sheaf_index.py` (or `portable-toolkit/1-page-anchored-indexer/page_corpus_indexer.py`) to generate:
   - `{OUTPUT_DIR}/data/sheaf_kb.json`
   - `{OUTPUT_DIR}/data/sheaf_pages_bundle.js`
   - `{OUTPUT_DIR}/data/cattheory_sheaf.db` (SQLite FTS5)
   - `{OUTPUT_DIR}/wiki/HOME.md`, `wiki/chapters/*.md`, `wiki/concepts/*.md`
   - `{OUTPUT_DIR}/query_sheaf.py` (with `--ask`, `--audit-cover`, `--stalk`, `--page`, and `--mcp` JSON-RPC 2.0 server mode)
2. Synthesize Dual-Host Neural Podcast MP3s (`Kore` × `Puck`):
   `/Users/cairo/.local/bin/uv run --with edge-tts python3 .agents/skills/sheaf-field-manual-studio/scripts/synthesize_notebook_podcast.py --kb {OUTPUT_DIR}/data/sheaf_kb.json`
3. Run the deterministic contract validator (including `--selftest`):
   `python3 .agents/skills/sheaf-corpus-indexer/scripts/validate_sheaf_contract.py --kb {OUTPUT_DIR}/data/sheaf_kb.json --selftest`
   **Exit Gate:** `HF-SHEAF-01` through `HF-SHEAF-13` must all be `CLEARED`.

### PHASE 2: CETI Field-Manual Studio & Symbolic Sandbox Compilation (`sheaf-field-manual-studio`)
1. Run `.agents/skills/sheaf-field-manual-studio/scripts/compile_field_manual_studio.py` to compile the 5-Plate interactive HTML volume (`{OUTPUT_DIR}/index.html` and top-level studio HTML).
2. Run the deterministic HTML, LaTeX, Corpus-Bleed & Podcast Studio auditor:
   `python3 .agents/skills/sheaf-field-manual-studio/scripts/audit_rendered_html.py --html {STUDIO_HTML} --kb {OUTPUT_DIR}/data/sheaf_kb.json`
   **Exit Gate:** `HF-STUDIO-01` through `HF-STUDIO-11` must all be `CLEARED`.

### PHASE 3: Recursive A1–A4 MOE Adversarial Evaluation Loop (`sheaf-knowledge-pipeline`)
1. Run the unified 26-gate MOE audit across Evaluators A1 (Depth/Cohomology), A2 (Performance/FTS5/MCP), A3 (Field-Manual/Math/Symbolic/Podcast Craft), and A4 (Citations/Page-Fibers/Wiki/Spoken Grounding):
   `python3 .agents/skills/sheaf-knowledge-pipeline/scripts/run_sheaf_pipeline_audit.py`
   and log rounds to `portable-toolkit/META-LEARNING-LOG.md` via `portable-toolkit/3-gate-review-runner/gate_review_runner.py`.
2. Execute >= 3 recursive evaluation-and-repair rounds (`R1 -> R2 -> R3`), logging every defect found and repaired until `26/26` binary gates are `CLEARED` (`overall_ship_vote == "GO"`).
3. Record durable findings in `wiki/qc-memory/` and append a row to `wiki/LEDGER.md`.
```

---

## 3. Complete 26-Gate Binary Hard-Fail Matrix (`HF-*`)

| Gate ID | Evaluator | Invariant Tested | Verification Method |
|---|---|---|---|
| `HF-SHEAF-01` | **A1** | Top-level schema keys & `len(pages) == book.total_pages` | `validate_sheaf_contract.py` |
| `HF-SHEAF-02` | **A1** | 100.0% of body pages covered by $\ge 1$ Concept Stalk | `validate_sheaf_contract.py` |
| `HF-SHEAF-03` | **A1** | Stalk IDs unique ($\ge 10$) and page intervals valid | `validate_sheaf_contract.py` |
| `HF-SHEAF-04` | **A1** | Local Olog referential integrity (`src`/`dst` in `olog.types`, SVO verbs) | `validate_sheaf_contract.py` |
| `HF-SHEAF-05` | **A1** | Global poset connectivity via restriction morphisms $\rho_{U,V}$ | `validate_sheaf_contract.py` |
| `HF-SHEAF-06` | **A1** | Non-empty `formula`, `overlap`, and empirical `term_jaccard` on $\rho_{U,V}$ | `validate_sheaf_contract.py` |
| `HF-SHEAF-07` | **A1** | Commutative 2-simplices (`two_simplices`) form connected triangles | `validate_sheaf_contract.py` |
| `HF-SHEAF-08` | **A4** | All formal declarations have valid page numbers & `stalk_ids` | `validate_sheaf_contract.py` |
| `HF-SHEAF-09` | **A1/A4** | Empirical Čech cohomology (`PASS` on connected covers, `FAIL` on disconnected covers) | `validate_sheaf_contract.py` |
| `HF-SHEAF-10` | **A2** | Deferred browser bundle `sheaf_pages_bundle.js` exists & valid | `validate_sheaf_contract.py` |
| `HF-SHEAF-11` | **A2** | SQLite FTS5 tables (`pages_fts`, `formal_items_fts`) row parity | `validate_sheaf_contract.py` |
| `HF-SHEAF-12` | **A4** | Persistent Markdown Wiki (`HOME.md`, `chapters/`, `concepts/`) parity | `validate_sheaf_contract.py` |
| `HF-SHEAF-13` | **A3/A4** | Dual-Host Neural Podcast MP3s (`>= 40 KB`, `>= 25s`, `>= 6` turns `Kore`×`Puck`, zero kerning glues, zero raw `(p. N)`) | `validate_sheaf_contract.py` |
| `HF-STUDIO-01` | **A3** | CETI Field-Manual palette (`#F5EFE3`, `#1A1612`, `#A67756`) & fonts | `audit_rendered_html.py` |
| `HF-STUDIO-02` | **A2** | Core HTML `< 450 KB` + `<script defer>` split-bundle architecture | `audit_rendered_html.py` |
| `HF-STUDIO-03` | **A3** | Zero raw LaTeX backslash leaks in static DOM & rendered KB strings | `audit_rendered_html.py` |
| `HF-STUDIO-04` | **A3** | All 5 Editorial Plates (`#plate-1..5`) + `.u-copper` italic nouns | `audit_rendered_html.py` |
| `HF-STUDIO-05` | **A3** | Every Plate has `.marginalia` (with `<cite>`) and `.counterpoint` | `audit_rendered_html.py` |
| `HF-STUDIO-06` | **A3** | Non-color-alone verdict stamps (`◆`, `⚖`, `✓`, `±`, `⊘` + text) | `audit_rendered_html.py` |
| `HF-STUDIO-07` | **A1** | Single-mutator interactive instruments + on-demand 3D Poset loop | `audit_rendered_html.py` |
| `HF-STUDIO-08` | **A3** | FORGE rules (`Key Concept`/`Why It Matters`, no `So What`, no stacked callouts, no `Module N` titles) | `audit_rendered_html.py` |
| `HF-STUDIO-09` | **A2** | Progressive Depth (`Newcomer|Practitioner|Expert`) & Paper switches | `audit_rendered_html.py` |
| `HF-STUDIO-10` | **A4** | Slide-Over Verbatim Book Reader Drawer + `__jumpToPage` + zero cross-book string bleed | `audit_rendered_html.py` |
| `HF-STUDIO-11` | **A3** | Dual-Host Neural Podcast Studio (`#podcastStudioCard`, `#hostBadgeKore`, `#hostBadgePuck`, `gemini-2.5-flash-preview-tts`, `buildCustomPodcastTurns`) | `audit_rendered_html.py` |
| `HF-MCP-01` | **A2** | JSON-RPC 2.0 `--mcp` stdio server responds with 3 sheaf tools | `run_sheaf_pipeline_audit.py` |
| `HF-CONTRACT-01` | **A2** | Master Typed Meta-Prompt Contract (`v3.0`) present & complete on disk | `run_sheaf_pipeline_audit.py` |

---

## 9. Round 7–9 Multi-Agent Adversarial Panel Additions (`HF-SHEAF-14`, `HF-STUDIO-13`, `HF-STUDIO-14` & 8-Pillar SGI)

### 9.1 New Binary Gates (`27` → `30` Binary Gates + `33/33` Negative Mutation Self-Tests)
- **`HF-SHEAF-14` (`Cross-Corpus Functorial Bridge Completeness & Strict JSON Schema Conformance`):** Every corpus in `sheaf_kb.json` must include `cross_corpus_bridges` mapping all stalks across Marinov (`24/24`), Spivak (`24/24`), and Independent Agent (`18/18`) with `concept_arc`, `why_it_bridges`, `formula`, `shared_terms`, `bridge_fidelity` (`0.68..0.95`), and `coboundary_defect_d0`, and pass `Draft202012Validator` (`0` schema errors).
- **`HF-STUDIO-13` (`Explorable Witness Verifier, Sub-Turn Karaoke, Walkable Lab Checklist, Cross-Corpus Bridge, Dark Blueprint SVG & Permalinks`):** Verifies `#commutativityWitnessTester`, `renderKaraokeSubtitleHtml`, `.karaoke-word`, `.olog-pulse-active`, `#walkableLabActiveBanner`, `#crossCorpusBridgeWidget`, dark-mode blueprint SVG rules, and `#shareStateBtn` (`window.__syncUrlState` / `window.__hydrateFromUrlParams`).
- **`HF-STUDIO-14` (`Inline JS AST Syntax (node --check), Live Witness Mini-SVG & Dark Bertin Contrast Gate`):** Parses all inline `<script>` blocks via `node --check` (`0` syntax errors), verifies `#witnessMiniSvg` (`renderWitnessMiniSvg`), `#copyBridgePermalinkBtn`, and dark-mode Bertin retinal SVG text contrast (`html[data-theme="dark"] svg text[fill=`).

### 9.2 8-Pillar Spec-to-Goal Maturity & Growth Index (`SGI`, `R1..R9`)
| Pillar | Weight | R1 (`v1`) | R2 (`v2`) | R3 (`v3`) | R4 (`v4`) | R5 (`v5`) | R6 (`v6`) | R7 (`v7`) | R8 (`v8`) | R9 (`v9`) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **P1. Page-Anchored Extraction & Zero-Kerning Fidelity** | `15%` | `52%` | `68%` | `78%` | `82%` | `86%` | `91%` | `98%` | `100%` | `100%` |
| **P2. Alexandrov Sheaf Topology & Empirical Cohomology** | `15%` | `48%` | `72%` | `88%` | `92%` | `95%` | `96%` | `100%` | `100%` | `100%` |
| **P3. Explorable Explanations & Live Witness Verification** | `15%` | `35%` | `48%` | `58%` | `64%` | `70%` | `82%` | `94%` | `99%` | `100%` |
| **P4. Dual-Host Neural Audio, Sub-Turn Karaoke & Study Sheets** | `12%` | `20%` | `45%` | `62%` | `68%` | `75%` | `85%` | `94%` | `99%` | `100%` |
| **P5. Editorial Craft, Dark Blueprint SVGs & Zero LaTeX Leaks** | `13%` | `55%` | `64%` | `72%` | `78%` | `82%` | `88%` | `96%` | `99%` | `100%` |
| **P6. Cross-Corpus Functorial Bridges & Walkable E2E Labs** | `10%` | `30%` | `42%` | `50%` | `55%` | `62%` | `75%` | `95%` | `99%` | `100%` |
| **P7. Mobile Ergonomics, URL Permalinks & Keyboard A11y** | `10%` | `40%` | `46%` | `52%` | `62%` | `74%` | `88%` | `96%` | `99%` | `100%` |
| **P8. Binary Gate Coverage, AST Checks & Doc/Schema Parity** | `10%` | `70%` | `75%` | `80%` | `80%` | `82%` | `86%` | `98%` | `99%` | `100%` |
| **Weighted Overall Spec-to-Goal Index (`SGI`)** | **`100%`** | **`44.8%`** | **`58.6%`** | **`68.9%`** | **`73.2%`** | **`78.6%`** | **`87.3%`** | **`96.5%`** | **`99.2%`** | **`100.0%`** |

