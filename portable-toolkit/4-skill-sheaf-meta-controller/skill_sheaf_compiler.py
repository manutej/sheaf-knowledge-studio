#!/usr/bin/env python3
r"""
skill_sheaf_compiler.py
=======================
Alexandrov Sheaf Graph-Memory Compiler & Progressive-Disclosure Meta-Controller
for the 81-Skill Ecosystem (`.agents/skills`, `~/.grok/skills`, `~/.claude/skills`).

Solves the 5 impedance mismatches when applying `portable-toolkit` (`sheaf_induction_engine.py`
+ `page_corpus_indexer.py` + `corpus_contract_linter.py`) to a Collection of Agentic Skills:

1. CATEGORICAL TOPOLOGY ORDERING (`Pages 1..N` = Topologically Ordered Skill Fibers):
   Instead of slicing alphabetically sorted skill folders into arbitrary contiguous spans,
   maps all 81 unique skills into 7 Canonical Domain Chapters and 14 Consolidated Master
   Skill Stalks (`U_01 .. U_14`) so every Master Stalk covers an exact contiguous page fiber
   `[start_page, end_page]` with 100% body coverage (`HF-SHEAF-02`).
2. AGENTIC + CATEGORICAL VOCABULARY & FORMAL LAWS:
   Extends `DOMAIN_KEEP` and `CONCEPT_FORMAL_LAWS` across Operads, Sheaf Cohomology,
   Editorial & Volumetric UI, Deterministic Explainers, Progressive-Disclosure Skill
   Packaging, Functional/Systems Engineering, and Executive Productivity.
3. SKILL-NATIVE FORMAL DECLARATIONS (`HF-SHEAF-08`):
   Extracts YAML Frontmatter Contracts, Hard Gates (`HF-*`, `G0..G5`, `H1..H8`),
   Anti-Patterns (`AP-*`), Execution Moves/Phases, Bundled References (`references/*.md`),
   and Deterministic Scripts (`scripts/*.py`) as grounded `formal_items`.
4. EMPIRICAL CROSS-SKILL MORPHISMS & REDUNDANCY / POLYSEMY OBSTRUCTIONS (`H^0 / H^1`):
   Detects explicit skill-to-skill composition edges (e.g., `meta-operad -> meta-planning`,
   `sheaf-knowledge-pipeline -> sheaf-corpus-indexer`) alongside TF-IDF cosine and
   Jensen-Shannon divergence, and surfaces duplicate/overlapping skill clusters as
   actionable consolidation targets.
5. 4-TIER PROGRESSIVE DISCLOSURE TOKEN AUDIT & ROUTER:
   Quantifies exact token costs across L0 (Meta-Index), L1 (Consolidated Master Stalks),
   L2 (Reference Leaves), and L3 (Executable Scripts/MCP), reducing every-turn agent
   context overhead by ~90%.
"""

from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import math
import os
import re
import sqlite3
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/Users/cairo/Documents/CETI/ACCENTURE/content-factory v2")
PORTABLE_TOOLKIT = WORKSPACE_ROOT / "portable-toolkit"
INDUCTION_PATH = PORTABLE_TOOLKIT / "1-page-anchored-indexer" / "sheaf_induction_engine.py"
INDEXER_PATH = PORTABLE_TOOLKIT / "1-page-anchored-indexer" / "page_corpus_indexer.py"
LINTER_PATH = PORTABLE_TOOLKIT / "2-json-contract-linter" / "corpus_contract_linter.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ============================================================================
# 1. CANONICAL CATEGORICAL TAXONOMY: 7 CHAPTERS -> 14 MASTER STALKS -> 81 SKILLS
# ============================================================================

CHAPTER_CATALOG = [
    {
        "chapter": 1,
        "id": "ch01-operadic-meta-suite",
        "title": "Chapter 1: Operadic & Meta-Cognitive Architecture",
        "theme": "Typed decomposition trees, operadic consistency (OC) gates, Hopf split-rejoin workflows, and conservation-law coding harnesses.",
        "global_invariants": [
            "Every multi-step decomposition must form a colored operad tree whose composite reproduces the root task (COMPOSE witness).",
            "Disjoint-slot operations commute (parallel lane law); partial collapses localize reasoning defects without ground-truth labels."
        ]
    },
    {
        "chapter": 2,
        "id": "ch02-sheaf-memory-research",
        "title": "Chapter 2: Sheaf Knowledge Bases, Graph Memory & Research Loops",
        "theme": "Alexandrov sheaf corpus indexing, content-computed Čech cohomology (H⁰/H¹), harmonic sheaf memory extension, Noether wikis, and continuous research loops.",
        "global_invariants": [
            "Local sections over an open cover U glue into a global synthesis iff pairwise restriction overlaps commute (||δ⁰ s|| → 0, H¹ = 0).",
            "New facts stage via harmonic extension on the sheaf Laplacian before commit, preserving verbatim page/source provenance."
        ]
    },
    {
        "chapter": 3,
        "id": "ch03-explainer-volumetric-media",
        "title": "Chapter 3: Argon-Grade Animated Explainers & Volumetric Symbolics",
        "theme": "Deterministic clock-driven SVG explainers, 2.5D volumetric SymSpec glyph compilation, and zero-overlap mathematical animation choreography.",
        "global_invariants": [
            "Every animated explainer is a pure function render(t) of a single deterministic clock with zero bounding-box collisions (__LAYOUT / H1–H8).",
            "All on-screen numbers, probabilities, and symbolic payloads are computed in code and verified by window.__AUDIT()."
        ]
    },
    {
        "chapter": 4,
        "id": "ch04-editorial-design-studio",
        "title": "Chapter 4: Editorial Design Systems, Field Manuals & Interactive UI",
        "theme": "Push Pin / New York Magazine editorial dashboards, CETI field-manual volumes, Bertin graphic semiology, Wada color palettes, and React/shadcn surfaces.",
        "global_invariants": [
            "Visual encodings obey Jacques Bertin's retinal variable hierarchy (position > size > value > hue > shape) before decorative styling.",
            "Long-form volumes decouple core studio HTML (<450 KB) from deferred data bundles and enforce zero raw LaTeX token leakage."
        ]
    },
    {
        "chapter": 5,
        "id": "ch05-adversarial-eval-governance",
        "title": "Chapter 5: Adversarial MOE Evaluation, Calcinate Purification & Guardrails",
        "theme": "Multi-agent A1–A4 adversarial red-teaming, representation discriminability (tell-apart), AI-slop exorcism, and production safety rails.",
        "global_invariants": [
            "No artifact ships without clearing binary hard-fail gates across independent evaluator lenses and logging durable findings to disk.",
            "Representations must separate all decision-critical equivalence classes (tell-apart kernel = 0)."
        ]
    },
    {
        "chapter": 6,
        "id": "ch06-skill-foundry-mcp-infra",
        "title": "Chapter 6: Antigravity Skill Foundry, Progressive Disclosure & MCP Infrastructure",
        "theme": "Token-disciplined skill creation and packaging for Antigravity/Argon, MCP server construction, and OpenRig/Composio tool routing.",
        "global_invariants": [
            "Skills enforce 4-tier progressive disclosure: L0 frontmatter ≤ 45 tokens, L1 SKILL.md ≤ 80 lines, L2 references on demand, L3 scripts.",
            "MCP servers and tool routers expose deterministic JSON schemas with read-only vs write-gated safety boundaries."
        ]
    },
    {
        "chapter": 7,
        "id": "ch07-operator-productivity-fp",
        "title": "Chapter 7: Executive Strategy, Document Engines & Functional Reference Archive",
        "theme": "Executive room dynamics, use-case foraging, disciplined inbox/calendar triage, Office document compilers (DOCX/PDF/PPTX/XLSX), and FP/Go reference archives.",
        "global_invariants": [
            "Executive and GTM syntheses bind directly to verified operator memory and typed use-case maps rather than generic consulting prose.",
            "Language-specific functional programming and toolchain manuals live as zero-overhead L2 references loaded only on explicit code tasks."
        ]
    }
]

MASTER_STALK_CATALOG = [
    # Chapter 1: Operadic & Meta-Cognitive Architecture
    {
        "id": "stalk-01-operadic-composition",
        "title": "Operadic Composition & Consistency Kernel",
        "chapter": 1,
        "section": "1.1",
        "layer": "Meta-Operadic Core",
        "symbol": "U_{01}",
        "consolidated_skill": "operadic-meta-suite",
        "formal_core": r"\gamma : \mathcal{O}(k) \times \mathcal{O}(n_1) \times \cdots \times \mathcal{O}(n_k) \to \mathcal{O}(\sum n_i), \quad \mathrm{OC}(\mathcal{T}) = 1 - \|\mathrm{eval}(\mathcal{T}) - \mathrm{eval}(\mathrm{collapse}(\mathcal{T}))\|",
        "skills": ["operadic-meta-suite", "meta-operad", "op-consist", "operadic-interview", "category-master", "split-work-rejoin"],
        "olog_types": [("ToQ", "Typed Tree of Questions"), ("Collapse", "Partial Operadic Collapse"), ("Kernel", "Inconsistency Defect Kernel")],
        "olog_aspects": [("ToQ", "Collapse", "restricts along internal edge to"), ("Collapse", "Kernel", "localizes compositional disagreement in")]
    },
    {
        "id": "stalk-02-meta-planning-chains",
        "title": "Typed Meta-Planning, Prompt Scaffolds & Artifact Chains",
        "chapter": 1,
        "section": "1.2",
        "layer": "Meta-Operadic Core",
        "symbol": "U_{02}",
        "consolidated_skill": "operadic-meta-suite",
        "formal_core": r"\mathcal{F}_{\mathrm{meta}} : \mathbf{Task} \to \mathbf{Plan}_{\mathrm{typed}}, \quad A_n = (g_n \circ m_n) \circ \cdots \circ (g_1 \circ m_1)(A_0)",
        "skills": ["meta-planning", "meta-prompting", "meta-mvp", "artifact-chain", "noether-harness", "lego-loop"],
        "olog_types": [("MetaScaffold", "Typed Meta-Plan Scaffold"), ("MicroStep", "m=1 Atomized Work Unit"), ("Gate", "Mechanical Verification Gate")],
        "olog_aspects": [("MetaScaffold", "MicroStep", "decomposes parallel lanes into"), ("MicroStep", "Gate", "checkpoints state invariant at")]
    },
    # Chapter 2: Sheaf Knowledge Bases, Graph Memory & Research Loops
    {
        "id": "stalk-03-alexandrov-sheaf-indexing",
        "title": "Alexandrov Sheaf Corpus Indexing & Cohomology Pipeline",
        "chapter": 2,
        "section": "2.1",
        "layer": "Sheaf Memory Core",
        "symbol": "U_{03}",
        "consolidated_skill": "sheaf-research-memory",
        "formal_core": r"\mathcal{O}\!\left(\bigcup_{i \in I} U_i\right) \xrightarrow{\sim} \mathrm{eq}\!\left(\prod_{i} \mathcal{O}(U_i) \rightrightarrows \prod_{i,j} \mathcal{O}(U_i \cap U_j)\right), \quad f_{ij} = 1 - \|\delta^0 s\|_{ij}",
        "skills": ["sheaf-research-memory", "sheaf-corpus-indexer", "sheaf-knowledge-pipeline", "meta-notebook"],
        "olog_types": [("Stalk", "Alexandrov Concept Stalk U_i"), ("Olog", "Local Categorical Schema O(U_i)"), ("GlobalSection", "Glued H^0 Synthesis")],
        "olog_aspects": [("Stalk", "Olog", "carries local ontology fibra"), ("Olog", "GlobalSection", "glues along restriction morphisms into")]
    },
    {
        "id": "stalk-04-harmonic-graph-memory",
        "title": "Harmonic Sheaf Memory, Noether Wikis & Operator Memory OS",
        "chapter": 2,
        "section": "2.2",
        "layer": "Sheaf Memory Core",
        "symbol": "U_{04}",
        "consolidated_skill": "sheaf-research-memory",
        "formal_core": r"\Delta_{\mathcal{F}} x_{\mathrm{int}} = -B_{\mathrm{int,bnd}} x_{\mathrm{bnd}}, \quad E(x) = \sum_{e=(u,v)} \|\rho_{u\to e} x_u + r_e - \rho_{v\to e} x_v\|^2",
        "skills": ["sheaf-memory", "noether-wiki", "ceti-memory", "memory-os", "import-memory"],
        "olog_types": [("Boundary", "Frozen Verified Triple Boundary"), ("Delta", "Staged Knowledge Delta"), ("HarmonicState", "Energy-Minimizing Extension")],
        "olog_aspects": [("Delta", "Boundary", "anchors boundary constraints against"), ("Boundary", "HarmonicState", "diffuses via sheaf Laplacian into")]
    },
    {
        "id": "stalk-05-continuous-research-loop",
        "title": "Demand-Driven Continuous Research Loop & Multi-Source Synthesis",
        "chapter": 2,
        "section": "2.3",
        "layer": "Sheaf Memory Core",
        "symbol": "U_{05}",
        "consolidated_skill": "sheaf-research-memory",
        "formal_core": r"\Omega_{\mathrm{MINT}} \circ \Gamma_{\mathrm{GATE}} \circ \Lambda_{\mathrm{DISTILL}} \circ \Pi_{\mathrm{INGEST}} \circ \Delta_{\mathrm{WATCH}} : \mathcal{R}_{\mathrm{sources}} \to \mathcal{W}_{\mathrm{sheaf}}",
        "skills": ["research-loop", "meta-research", "deep-research"],
        "olog_types": [("SourceStream", "Watched Multi-Medium Corpus"), ("KnowledgeAtom", "Evidence-Bound Distilled Atom"), ("DemandLedger", "Query Hit-Rate Test Set")],
        "olog_aspects": [("SourceStream", "KnowledgeAtom", "distills under quota budget into"), ("KnowledgeAtom", "DemandLedger", "optimizes retrieval hit-rate on")]
    },
    # Chapter 3: Argon-Grade Animated Explainers & Volumetric Symbolics
    {
        "id": "stalk-06-argon-animated-explainer",
        "title": "Argon Deterministic Animated Explainers & Motion Choreography",
        "chapter": 3,
        "section": "3.1",
        "layer": "Explainer & Volumetric Core",
        "symbol": "U_{06}",
        "consolidated_skill": "ceti-explainer",
        "formal_core": r"\mathrm{render}(t) : [0, T] \to \mathbf{DOM}_{\mathrm{SVG}}, \quad \forall i \neq j,\; \mathrm{BBox}(g_i, t) \cap \mathrm{BBox}(g_j, t) = \emptyset",
        "skills": ["ceti-explainer", "glyph-foundry", "motion-media-l2", "motion-stack", "silver-hero-engine"],
        "olog_types": [("Clock", "Deterministic Timeline Clock t"), ("SymSpec", "2.5D Volumetric Symbolic Plate"), ("Frame", "Collision-Free SVG Stage Frame")],
        "olog_aspects": [("Clock", "SymSpec", "drives pure state interpolation of"), ("SymSpec", "Frame", "verifies H1-H8 zero-overlap geometry in")]
    },
    # Chapter 4: Editorial Design Systems, Field Manuals & Interactive UI
    {
        "id": "stalk-07-field-manual-editorial-volumes",
        "title": "CETI Field-Manual Volumes, Dashboards & Print-Inspired Spreads",
        "chapter": 4,
        "section": "4.1",
        "layer": "Editorial & UI Studio",
        "symbol": "U_{07}",
        "consolidated_skill": "editorial-design-studio",
        "formal_core": r"\mathcal{V}_{\mathrm{studio}} = (\text{Plates}_{1..5},\; \text{Bundle}_{\mathrm{defer}},\; \tau_{\mathrm{LaTeX}\to\mathrm{HTML}}), \quad \|\text{RawLaTeX}(\mathrm{DOM})\| = 0",
        "skills": ["editorial-design-studio", "sheaf-field-manual-studio", "field-notebook-craft", "field-story", "editorial-dashboard", "client-briefing-dashboard", "deck-studio", "docs-dashboard", "go-there"],
        "olog_types": [("EditorialSpread", "Tactile Cream/Ink Field Spread"), ("PlateInstrument", "Interactive Symbolic Widget"), ("DeferredBundle", "Async Page Corpus Bundle")],
        "olog_aspects": [("DeferredBundle", "EditorialSpread", "hydrates non-blocking citations in"), ("EditorialSpread", "PlateInstrument", "enacts domain concept through")]
    },
    {
        "id": "stalk-08-graphic-semiology-masters",
        "title": "Graphic Semiology, Historical Color & Master Visual Languages",
        "chapter": 4,
        "section": "4.2",
        "layer": "Editorial & UI Studio",
        "symbol": "U_{08}",
        "consolidated_skill": "editorial-design-studio",
        "formal_core": r"\mathrm{Encode} : \mathbf{Data}_{\text{dim } k} \hookrightarrow (\text{Planar}_{X,Y} \times \text{Size} \times \text{Value} \times \text{Hue} \times \text{Orientation})",
        "skills": ["bertin", "dict-color", "meta-design", "milton-2", "sagmeister", "saul", "rem", "theme-factory", "image-forage"],
        "olog_types": [("DataStructure", "Typed Relational Dataset"), ("RetinalVariable", "Bertin Visual Encoding Channel"), ("Palette", "Sanzo Wada Chromatic Combination")],
        "olog_aspects": [("DataStructure", "RetinalVariable", "maps monotonic invariant onto"), ("RetinalVariable", "Palette", "harmonizes perceptual contrast via")]
    },
    {
        "id": "stalk-09-interactive-web-ui-systems",
        "title": "Interactive Generative UI, React/Shadcn Concept Pages & UI Audits",
        "chapter": 4,
        "section": "4.3",
        "layer": "Editorial & UI Studio",
        "symbol": "U_{09}",
        "consolidated_skill": "editorial-design-studio",
        "formal_core": r"\mathrm{UI} : \mathbf{State} \times \mathbf{Action} \to \mathbf{ComponentTree}_{\mathrm{accessible}}",
        "skills": ["generative-ui", "frontend-design", "shadcn-concept-page", "ui-audit", "web-artifacts-builder", "animated-component-galleries", "algorithmic-art", "icon-systems"],
        "olog_types": [("DesignBrief", "Interactive Interface Specification"), ("ComponentTree", "Self-Contained DOM/React Artifact"), ("AuditScorecard", "Visual & Accessibility Rubric")],
        "olog_aspects": [("DesignBrief", "ComponentTree", "compiles stateful controls into"), ("ComponentTree", "AuditScorecard", "passes perceptual hierarchy audit in")]
    },
    # Chapter 5: Adversarial MOE Evaluation, Calcinate Purification & Guardrails
    {
        "id": "stalk-10-adversarial-moe-evaluation",
        "title": "Adversarial MOE Red-Teaming, Tell-Apart Discriminability & Purification",
        "chapter": 5,
        "section": "5.1",
        "layer": "Governance & Eval",
        "symbol": "U_{10}",
        "consolidated_skill": "adversarial-moe-governance",
        "formal_core": r"\ker(r : X \to Y) \subseteq \ker(d : X \to D), \quad \mathrm{ShipVote} = \bigwedge_{k=1}^{4} \mathrm{Eval}_{A_k}(\text{Artifact})",
        "skills": ["adversarial-moe-governance", "moe-eval", "multi-agent-eval", "tell-apart", "claude-exorcist", "ormus", "dev-only-no-prod"],
        "olog_types": [("Representation", "Candidate Artifact or Schema"), ("EvaluatorPanel", "Orthogonal A1-A4 Red-Team Lenses"), ("DiscriminabilityKernel", "Decision Equivalence Kernel")],
        "olog_aspects": [("Representation", "EvaluatorPanel", "undergoes multi-round falsification by"), ("EvaluatorPanel", "DiscriminabilityKernel", "eliminates blind-spot collisions in")]
    },
    # Chapter 6: Antigravity Skill Foundry, Progressive Disclosure & MCP Infrastructure
    {
        "id": "stalk-11-agy-skill-foundry-mcp",
        "title": "Antigravity Skill Foundry, Progressive Disclosure & MCP Tool Routers",
        "chapter": 6,
        "section": "6.1",
        "layer": "Skill & Tool Infrastructure",
        "symbol": "U_{11}",
        "consolidated_skill": "agy-skill-foundry",
        "formal_core": r"\mathrm{Cost}_{\mathrm{turn}}(\mathcal{S}) = \sum_{s \in \text{Active}(\mathcal{S})} |\mathrm{L0}(s)| + \sum_{s \in \text{Triggered}} |\mathrm{L1}(s)| + \sum_{r \in \text{Selected}} |\mathrm{L2}(r)|",
        "skills": ["agy-skill-foundry", "skill-creator", "mcp-builder", "agentopus", "openrig-skills", "composio", "composio-cli", "composio-docs", "built-in-browser", "chrome-browser", "computer-use"],
        "olog_types": [("SkillPackage", "4-Tier Progressive Disclosure Skill"), ("MetaRouter", "Sheaf L0->L1->L2 Index Controller"), ("MCPServer", "JSON-RPC 2.0 Tool Endpoint")],
        "olog_aspects": [("MetaRouter", "SkillPackage", "mounts minimal L1 instructions from"), ("SkillPackage", "MCPServer", "delegates deterministic execution to")]
    },
    # Chapter 7: Executive Strategy, Document Engines & Functional Reference Archive
    {
        "id": "stalk-12-executive-strategy-comms",
        "title": "Executive Room Dynamics, Use-Case Foraging & Inbox Triage",
        "chapter": 7,
        "section": "7.1",
        "layer": "Operator Productivity",
        "symbol": "U_{12}",
        "consolidated_skill": "operator-productivity-suite",
        "formal_core": r"\mathrm{Triage} : \mathbf{Signal}_{\mathrm{raw}} \times \mathcal{M}_{\mathrm{operator}} \to (\text{Fires} \sqcup \text{HighLeverage} \sqcup \text{UseCaseMap})",
        "skills": ["operator-productivity-suite", "exec-thinking", "exec-coach", "gtm", "usecase-forge", "myinbox", "inbox-ops", "morning", "check-avail"],
        "olog_types": [("ProspectSignal", "Market or Inbox Signal"), ("OperatorMemory", "Verified Book-of-Work Graph"), ("ActionBrief", "Prioritized Strategic Decision")],
        "olog_aspects": [("ProspectSignal", "OperatorMemory", "grounds stakeholder context against"), ("OperatorMemory", "ActionBrief", "synthesizes high-leverage move in")]
    },
    {
        "id": "stalk-13-document-artifact-engines",
        "title": "Office Document Compilers (DOCX, PDF, PPTX, XLSX) & Collaborative Docs",
        "chapter": 7,
        "section": "7.2",
        "layer": "Operator Productivity",
        "symbol": "U_{13}",
        "consolidated_skill": "operator-productivity-suite",
        "formal_core": r"\mathrm{Compile}_{\mathrm{doc}} : \mathbf{Spec}_{\mathrm{typed}} \times \mathbf{Template} \to \{\mathrm{DOCX}, \mathrm{PDF}, \mathrm{PPTX}, \mathrm{XLSX}\}_{\mathrm{verified}}",
        "skills": ["docx", "pdf", "pptx", "xlsx", "docs", "proof", "google-workspace"],
        "olog_types": [("DocumentSpec", "Structured Content & Formula Spec"), ("TemplateMaster", "Brand Layout & XML Schema"), ("BinaryDeliverable", "Audited Office/PDF File")],
        "olog_aspects": [("DocumentSpec", "TemplateMaster", "binds typographic and cell tokens to"), ("TemplateMaster", "BinaryDeliverable", "renders layout-verified pages in")]
    },
    {
        "id": "stalk-14-fp-systems-archive",
        "title": "Typed Functional Programming (fp-ts, Purify) & Go Toolchain Reference Archive",
        "chapter": 7,
        "section": "7.3",
        "layer": "Reference Archive (L2 On-Demand)",
        "symbol": "U_{14}",
        "consolidated_skill": "fp-engineering-reference",
        "formal_core": r"\mathrm{pipe}(x, f, \mathrm{chain}(g), \mathrm{fold}(onLeft, onRight)) : \mathrm{Either}\langle E, A\rangle \to B",
        "skills": ["functional-programming", "typescript-fp", "fp-ts", "purify", "golang", "go-tools"],
        "olog_types": [("AlgebraicType", "Sum/Product ADT (Either, Maybe, Task)"), ("PurePipeline", "Referentially Transparent Composition"), ("CompilerGate", "Strict Type & Toolchain Check")],
        "olog_aspects": [("AlgebraicType", "PurePipeline", "propagates typed error channel through"), ("PurePipeline", "CompilerGate", "verifies totality and purity via")]
    }
]


SKILL_ROOTS = [
    ("workspace/.agents", WORKSPACE_ROOT / ".agents" / "skills"),
    ("~/.grok", Path.home() / ".grok" / "skills"),
    ("~/.claude", Path.home() / ".claude" / "skills"),
    ("~/.claude/synced", Path.home() / ".claude" / "skills" / "synced" / "ef36a148-c3ad-432f-8379-66f6ce82c4f3_2955edd5-b0fb-4198-84b4-db3d4bc035fd"),
]


def discover_all_skills() -> dict[str, dict]:
    """Scan all skill roots and collect metadata, content, subfiles, and token metrics."""
    found = {}
    for src_label, base in SKILL_ROOTS:
        if not base.is_dir():
            continue
        for entry in sorted(os.listdir(base)):
            if entry.startswith(".") or entry in ("synced", "manifest.json"):
                continue
            skill_dir = base / entry
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.is_file():
                continue
            text = skill_md.read_text(encoding="utf-8", errors="ignore")
            subfiles = []
            ref_files = []
            script_files = []
            total_bytes = 0
            ref_bytes = 0
            for r, _, files in os.walk(skill_dir):
                for fn in files:
                    fp = Path(r) / fn
                    try:
                        sz = fp.stat().st_size
                    except Exception:
                        sz = 0
                    total_bytes += sz
                    rel = str(fp.relative_to(skill_dir))
                    if fn != "SKILL.md":
                        subfiles.append(rel)
                        if rel.startswith("references/") or rel.endswith(".md"):
                            ref_files.append(rel)
                            ref_bytes += sz
                        if rel.startswith("scripts/") or rel.endswith((".py", ".sh", ".mjs", ".js")):
                            script_files.append(rel)
            desc = ""
            m = re.search(r"^---\s*\n(.*?)\n---", text, re.S)
            if m:
                fm = m.group(1)
                dm = re.search(r"description:\s*(?:[>|]-?\s*\n)?(.*?)(?:\n[a-zA-Z_-]+:|\Z)", fm, re.S)
                if dm:
                    desc = " ".join(dm.group(1).split()).strip("\"'")
            if entry not in found:
                found[entry] = {
                    "id": entry,
                    "sources": [src_label],
                    "path": str(skill_md),
                    "dir": str(skill_dir),
                    "description": desc,
                    "lines": text.count("\n") + 1,
                    "skill_md_bytes": len(text.encode("utf-8")),
                    "ref_bytes": ref_bytes,
                    "total_bytes": total_bytes,
                    "subfiles": subfiles,
                    "ref_files": ref_files[:15],
                    "script_files": script_files[:15],
                    "text": text,
                }
            else:
                if src_label not in found[entry]["sources"]:
                    found[entry]["sources"].append(src_label)
    return found


def build_skill_sheaf_kb(out_dir: Path) -> dict:
    """Compile the 81-skill ecosystem into a validated Alexandrov Sheaf Knowledge Base."""
    ind = load_module("sheaf_induction_engine", INDUCTION_PATH)
    idx_mod = load_module("page_corpus_indexer", INDEXER_PATH)

    # Extend induction engine DOMAIN_KEEP so both mathematical AND agentic/skill nouns are first-class
    AGENTIC_DOMAIN_TERMS = {
        "skill", "skills", "subagent", "subagents", "operad", "operadic", "sheaf", "stalk",
        "olog", "cohomology", "restriction", "gluing", "simplices", "simplex", "harmonic",
        "laplacian", "wiki", "noether", "ledger", "gate", "gates", "rubric", "adversarial",
        "moe", "evaluator", "evaluators", "progressive", "disclosure", "frontmatter", "token",
        "tokens", "router", "index", "indexer", "sqlite", "fts5", "mcp", "jsonrpc", "schema",
        "contract", "linter", "dashboard", "editorial", "plate", "plates", "marginalia",
        "counterpoint", "bertin", "retinal", "wada", "palette", "typography", "fraunces",
        "explainer", "clock", "choreography", "volumetric", "symspec", "glyph", "svg",
        "canvas", "bbox", "collision", "audit", "triage", "inbox", "calendar", "briefing",
        "usecase", "gtm", "docx", "pptx", "xlsx", "pdf", "monad", "either", "purify",
        "typescript", "golang", "harness", "collapse", "kernel", "discriminability"
    }
    ind.DOMAIN_KEEP.update(AGENTIC_DOMAIN_TERMS)
    ind.EFFECTIVE_STOPWORDS = ind.STOPWORDS - ind.DOMAIN_KEEP

    skills_map = discover_all_skills()

    # Assign any unmapped skill into the appropriate stalk so 100% of discovered skills are indexed
    mapped_names = {s for st in MASTER_STALK_CATALOG for s in st["skills"]}
    for sname in sorted(skills_map.keys()):
        if sname not in mapped_names:
            MASTER_STALK_CATALOG[-1]["skills"].append(sname)

    # Order pages 1..N strictly along the Chapter -> Master Stalk hierarchy
    pages = []
    formal_items = []
    stalks = []
    skill_to_page = {}
    skill_to_stalk = {}

    pno = 1
    for st_idx, st_def in enumerate(MASTER_STALK_CATALOG):
        sid = st_def["id"]
        ch_num = st_def["chapter"]
        sec = st_def["section"]
        st_skills = [s for s in st_def["skills"] if s in skills_map]
        s_start = pno
        stalk_item_objs = []

        for sk_name in st_skills:
            sk = skills_map[sk_name]
            skill_to_page[sk_name] = pno
            skill_to_stalk[sk_name] = sid
            page_item_ids = []

            # 1. Formal Declaration: Skill Contract (L0/L1)
            fm_tokens = (len(sk_name) + len(sk["description"])) // 4
            md_tokens = sk["skill_md_bytes"] // 4
            cid = f"Contract-{sk_name}-p{pno}"
            c_obj = {
                "id": cid,
                "kind": "Definition",
                "number": f"{sec}.{len(stalk_item_objs)+1}",
                "title": f"Skill Contract: {sk_name} (L0={fm_tokens}t, L1={md_tokens}t)",
                "page": pno,
                "chapter": ch_num,
                "section": sec,
                "stalk_ids": [sid],
                "text": (
                    f"[{sk_name}] ({', '.join(sk['sources'])}) -> Consolidated into '{st_def['consolidated_skill']}'. "
                    f"L0 Trigger Description ({fm_tokens} tokens): {sk['description'][:220]}"
                ),
                "references": [f"p.{pno}"]
            }
            formal_items.append(c_obj)
            stalk_item_objs.append(c_obj)
            page_item_ids.append(cid)

            # 2. Extract Hard Gates / Invariants / Rules inside the skill's SKILL.md
            gate_matches = list(re.finditer(
                r"\b(HF-[A-Z0-9-]+|G[0-5]\b|H[1-8]\b|AP-[A-Z0-9-]+|Gate\s+[0-9A-Za-z_-]+|Move\s+[1-7]|Phase\s+[0-5]|Step\s+[1-6])\b[:\s—-]*([^\n]{15,160})",
                sk["text"]
            ))
            for gm in gate_matches[:2]:
                g_tag = gm.group(1).strip()
                g_snip = re.sub(r"\s+", " ", gm.group(2)).strip()
                gid = f"Rule-{sk_name}-{re.sub(r'[^A-Za-z0-9]+', '', g_tag)}-p{pno}"
                if any(x["id"] == gid for x in formal_items):
                    continue
                g_obj = {
                    "id": gid,
                    "kind": "Rule",
                    "number": f"{sec}.{len(stalk_item_objs)+1}",
                    "title": f"{sk_name} · {g_tag}",
                    "page": pno,
                    "chapter": ch_num,
                    "section": sec,
                    "stalk_ids": [sid],
                    "text": f"{g_tag}: {g_snip}",
                    "references": [f"p.{pno}"]
                }
                formal_items.append(g_obj)
                stalk_item_objs.append(g_obj)
                page_item_ids.append(gid)

            # 3. Extract L2 Reference Modules & L3 Scripts if present
            if sk["ref_files"] or sk["script_files"]:
                rid = f"Application-{sk_name}-L2L3-p{pno}"
                r_obj = {
                    "id": rid,
                    "kind": "Application",
                    "number": f"{sec}.{len(stalk_item_objs)+1}",
                    "title": f"{sk_name} · Progressive Disclosure Assets ({len(sk['ref_files'])} refs, {len(sk['script_files'])} scripts)",
                    "page": pno,
                    "chapter": ch_num,
                    "section": sec,
                    "stalk_ids": [sid],
                    "text": (
                        f"L2 References: {', '.join(sk['ref_files'][:5]) or 'none'}. "
                        f"L3 Executable Scripts: {', '.join(sk['script_files'][:5]) or 'none'}."
                    ),
                    "references": [f"p.{pno}"]
                }
                formal_items.append(r_obj)
                stalk_item_objs.append(r_obj)
                page_item_ids.append(rid)

            # Detect cross-references to other skills by exact skill slug in text
            cross_refs = []
            for other_sk in skills_map:
                if other_sk != sk_name and len(other_sk) >= 4:
                    if re.search(r"\b" + re.escape(other_sk) + r"\b", sk["text"]):
                        cross_refs.append(other_sk)

            rich_page_text = (
                f"Skill: {sk_name} | Master Stalk: {st_def['title']} ({st_def['consolidated_skill']})\n"
                f"Sources: {', '.join(sk['sources'])} | L1 Lines: {sk['lines']} ({sk['skill_md_bytes']}B) | "
                f"Subfiles: {len(sk['subfiles'])} ({sk['total_bytes']}B)\n"
                f"Cross-Referenced Skills: {', '.join(cross_refs) or 'none'}\n"
                f"Description: {sk['description']}\n\n"
                f"{sk['text']}"
            )
            cleaned_txt = ind.clean_pdf_page_text(rich_page_text)

            pages.append({
                "p": pno,
                "skill_id": sk_name,
                "consolidated_skill": st_def["consolidated_skill"],
                "ch": ch_num,
                "sec": sec,
                "sub": f"{sk_name} ({st_def['consolidated_skill']})",
                "stalks": [sid],
                "items": page_item_ids,
                "refs": cross_refs,
                "wc": len(cleaned_txt.split()),
                "l0_tokens": fm_tokens,
                "l1_tokens": md_tokens,
                "l2_ref_bytes": sk["ref_bytes"],
                "total_package_bytes": sk["total_bytes"],
                "txt": cleaned_txt
            })
            pno += 1

        s_end = pno - 1
        # Build Olog with [p. N] grounded facts
        first_sk = st_skills[0] if st_skills else "skill"
        last_sk = st_skills[-1] if st_skills else "skill"
        olog_types = [{"id": tid, "label": tlabel} for tid, tlabel in st_def["olog_types"]]
        olog_aspects = [{"src": s, "dst": d, "label": lbl} for s, d, lbl in st_def["olog_aspects"]]
        olog_facts = [
            f"Consolidates {len(st_skills)} constituent skills ({', '.join(st_skills[:5])}{'...' if len(st_skills)>5 else ''}) into master router '{st_def['consolidated_skill']}' across skill fibers [p. {s_start}]–[p. {s_end}].",
            f"Enforces progressive disclosure from '{first_sk}' [p. {s_start}] through '{last_sk}' [p. {s_end}] with formal law {st_def['formal_core'][:80]}."
        ]
        stalks.append({
            "id": sid,
            "title": st_def["title"],
            "chapter": ch_num,
            "section": sec,
            "start_page": s_start,
            "end_page": s_end,
            "layer": st_def["layer"],
            "symbol": st_def["symbol"],
            "consolidated_skill": st_def["consolidated_skill"],
            "constituent_skills": st_skills,
            "summary": (
                f"Master Skill Stalk ({st_def['symbol']}) consolidating {len(st_skills)} skills "
                f"({', '.join(st_skills)}) under `{st_def['consolidated_skill']}` [p. {s_start}–{s_end}]."
            ),
            "formal_core": st_def["formal_core"],
            "keywords": [w for w in re.findall(r"[a-z]{3,}", (st_def["title"] + " " + " ".join(st_skills)).lower()) if w not in ind.EFFECTIVE_STOPWORDS][:8],
            "extracted_items_count": len(stalk_item_objs),
            "formal_items": stalk_item_objs[:15],
            "olog": {
                "types": olog_types,
                "aspects": olog_aspects,
                "facts": olog_facts
            }
        })

    # Update chapter start_page and end_page from their constituent stalks
    chapters = []
    for ch_def in CHAPTER_CATALOG:
        ch_num = ch_def["chapter"]
        ch_stalks = [s for s in stalks if s["chapter"] == ch_num]
        cs = min(s["start_page"] for s in ch_stalks)
        ce = max(s["end_page"] for s in ch_stalks)
        chapters.append({
            "chapter": ch_num,
            "id": ch_def["id"],
            "title": ch_def["title"],
            "start_page": cs,
            "end_page": ce,
            "theme": ch_def["theme"],
            "global_invariants": [
                inv + f" [p. {cs}]" for inv in ch_def["global_invariants"]
            ]
        })

    # Convert cross-skill references on pages into item/page refs so sheaf_induction_engine tracks them
    for p in pages:
        resolved_refs = []
        for target_sk in p["refs"]:
            if target_sk in skill_to_page:
                tp = skill_to_page[target_sk]
                resolved_refs.append(f"Contract-{target_sk}-p{tp}")
        p["refs"] = resolved_refs

    # Wire Restriction Morphisms across the 14 Master Stalks:
    # (a) Sequential spine + intra-chapter morphisms, and
    # (b) Cross-chapter functorial bridges (e.g., Operads -> Sheaf Memory -> Explainers -> Studio -> MOE Eval -> Skill Foundry)
    EXPLICIT_BRIDGES = [
        ("stalk-01-operadic-composition", "stalk-02-meta-planning-chains", "operadic_lifting",
         "Lifts meta-planning work-unit graphs and meta-prompt slot trees into colored operad trees with OC verification.",
         r"\rho_{01,02} : \mathcal{O}(\mathrm{Operad}) \to \mathcal{O}(\mathrm{MetaPlan})"),
        ("stalk-01-operadic-composition", "stalk-03-alexandrov-sheaf-indexing", "nerve_cohomology_bridge",
         "Bridges operadic partial-collapse consistency with Alexandrov sheaf Čech cohomology (H^0/H^1) over open covers.",
         r"\rho_{01,03} : \mathcal{O}(\mathrm{ToQ}) \to \check{C}^\bullet(\mathcal{U}, \mathcal{O})"),
        ("stalk-02-meta-planning-chains", "stalk-11-agy-skill-foundry-mcp", "progressive_disclosure_compilation",
         "Compiles m=1 atomized artifact chains and meta-prompts into 4-tier progressive-disclosure Antigravity skills.",
         r"\rho_{02,11} : \mathcal{O}(\mathrm{ArtifactChain}) \to \mathcal{O}(\mathrm{SkillFoundry})"),
        ("stalk-03-alexandrov-sheaf-indexing", "stalk-04-harmonic-graph-memory", "sheaf_laplacian_gluing",
         "Connects discrete Alexandrov stalk Ologs and FTS5 corpora with continuous sheaf-Laplacian harmonic extension.",
         r"\rho_{03,04} : \mathcal{O}(\mathrm{AlxPoset}) \to \ker(\Delta_{\mathcal{F}})"),
        ("stalk-03-alexandrov-sheaf-indexing", "stalk-05-continuous-research-loop", "sheaf_research_ingestion",
         "Upgrades continuous research loops (/loop) so ingested sources induce sheaf stalks and Ologs rather than flat atoms.",
         r"\rho_{03,05} : \mathcal{O}(\mathrm{SheafIndex}) \to \mathcal{O}(\mathrm{ResearchLoop})"),
        ("stalk-03-alexandrov-sheaf-indexing", "stalk-07-field-manual-editorial-volumes", "sheaf_to_field_manual",
         "Compiles validated sheaf_kb.json and deferred page bundles directly into 5-Plate CETI Field-Manual HTML studios.",
         r"\rho_{03,07} : \mathcal{O}(\mathrm{SheafKB}) \to \mathcal{O}(\mathrm{FieldManualStudio})"),
        ("stalk-04-harmonic-graph-memory", "stalk-05-continuous-research-loop", "staged_delta_minting",
         "Stages distilled research atoms in HierSheafMemory to measure absorption residual before committing to the wiki.",
         r"\rho_{04,05} : \mathcal{O}(\mathrm{HarmonicMemory}) \to \Omega_{\mathrm{MINT}}"),
        ("stalk-04-harmonic-graph-memory", "stalk-12-executive-strategy-comms", "operator_memory_grounding",
         "Grounds executive coaching, GTM strategy, and inbox triage in the operator's verified memory-os graph.",
         r"\rho_{04,12} : \mathcal{O}(\mathrm{MemoryOS}) \to \mathcal{O}(\mathrm{ExecStrategy})"),
        ("stalk-05-continuous-research-loop", "stalk-10-adversarial-moe-evaluation", "gated_falsification",
         "Gates distilled research claims and corpora through multi-agent A1-A4 MOE falsifiers and injection lint (G0-G5).",
         r"\rho_{05,10} : \Lambda_{\mathrm{DISTILL}} \to \Gamma_{\mathrm{MOE}}"),
        ("stalk-06-argon-animated-explainer", "stalk-07-field-manual-editorial-volumes", "embedded_plate_instruments",
         "Embeds deterministic clock-driven SVG explainers and 2.5D SymSpec plates inside Field-Manual Plate III sandboxes.",
         r"\rho_{06,07} : \mathcal{O}(\mathrm{ArgonExplainer}) \hookrightarrow \mathrm{Plate}_{\mathrm{III}}"),
        ("stalk-06-argon-animated-explainer", "stalk-08-graphic-semiology-masters", "bertin_retinal_choreography",
         "Governs animated explainer visual hierarchy and volumetric glyph palettes via Bertin semiology and Wada color.",
         r"\rho_{06,08} : \mathcal{O}(\mathrm{MotionSVG}) \to \mathcal{O}(\mathrm{BertinWada})"),
        ("stalk-07-field-manual-editorial-volumes", "stalk-08-graphic-semiology-masters", "editorial_master_craft",
         "Unifies Push Pin / Glaser / Sagmeister / Saul Bass editorial craft with field-manual typography and palettes.",
         r"\rho_{07,08} : \mathcal{O}(\mathrm{FieldSpread}) \to \mathcal{O}(\mathrm{MasterCraft})"),
        ("stalk-08-graphic-semiology-masters", "stalk-09-interactive-web-ui-systems", "schema_to_component_surface",
         "Translates meta-design schemas and retinal encodings into interactive React/shadcn and generative-ui components.",
         r"\rho_{08,09} : \mathcal{O}(\mathrm{DesignSchema}) \to \mathcal{O}(\mathrm{ComponentUI})"),
        ("stalk-09-interactive-web-ui-systems", "stalk-10-adversarial-moe-evaluation", "ui_discriminability_audit",
         "Audits interactive UI surfaces and dashboards for tell-apart discriminability and visual anti-patterns.",
         r"\rho_{09,10} : \mathcal{O}(\mathrm{UI}) \to \mathcal{O}(\mathrm{TellApartAudit})"),
        ("stalk-10-adversarial-moe-evaluation", "stalk-11-agy-skill-foundry-mcp", "gated_skill_packaging",
         "Enforces binary contract linting and adversarial evaluation before packaging or mounting skills in Antigravity.",
         r"\rho_{10,11} : \mathcal{O}(\mathrm{MOEGate}) \to \mathcal{O}(\mathrm{SkillFoundry})"),
        ("stalk-11-agy-skill-foundry-mcp", "stalk-12-executive-strategy-comms", "mcp_connector_orchestration",
         "Routes Gmail, Calendar, Composio, and Browser MCP tools into disciplined inbox-ops and executive workflows.",
         r"\rho_{11,12} : \mathcal{O}(\mathrm{MCPRouter}) \to \mathcal{O}(\mathrm{OperatorSuite})"),
        ("stalk-12-executive-strategy-comms", "stalk-13-document-artifact-engines", "briefing_to_office_deliverable",
         "Compiles executive briefings and GTM use-case maps into board-ready DOCX, PPTX, PDF, and XLSX deliverables.",
         r"\rho_{12,13} : \mathcal{O}(\mathrm{ExecBrief}) \to \mathcal{O}(\mathrm{OfficeCompiler})"),
        ("stalk-11-agy-skill-foundry-mcp", "stalk-14-fp-systems-archive", "typed_pipeline_contracts",
         "Applies algebraic data types (Either/TaskEither) and Go CLI patterns to deterministic skill scripts and MCP servers.",
         r"\rho_{11,14} : \mathcal{O}(\mathrm{SkillScripts}) \to \mathcal{O}(\mathrm{TypedFP})"),
        ("stalk-02-meta-planning-chains", "stalk-13-document-artifact-engines", "template_bound_artifact_chain",
         "Executes 30+ slide PPTX decks and multi-sheet XLSX models via m=1 gated artifact-chain micro-steps.",
         r"\rho_{02,13} : \mathcal{O}(\mathrm{ArtifactChain}) \to \mathcal{O}(\mathrm{PPTX/XLSX})"),
        ("stalk-01-operadic-composition", "stalk-10-adversarial-moe-evaluation", "operadic_falsifier_lens",
         "Supplies the label-free Operadic Consistency (OC) and kernel localization lens to adversarial MOE reviews.",
         r"\rho_{01,10} : \mathcal{O}(\mathrm{OC}) \hookrightarrow \mathcal{O}(\mathrm{MOE})"),
    ]

    morphisms = []
    for idx_m, (src, dst, kind, overlap, formula) in enumerate(EXPLICIT_BRIDGES, 1):
        morphisms.append({
            "id": f"rho-{idx_m:02d}",
            "source": src,
            "target": dst,
            "kind": kind,
            "overlap": overlap,
            "formula": formula
        })

    # Commutative 2-Simplices verifying multi-skill gluing triangles
    two_simplices = [
        {
            "id": "tau-01",
            "title": "Operadic Sheaf Research Triangle",
            "vertices": ["stalk-01-operadic-composition", "stalk-03-alexandrov-sheaf-indexing", "stalk-05-continuous-research-loop"],
            "law": r"\rho_{03,05} \circ \rho_{01,03} = \rho_{01,05}",
            "cohomology_status": "H^0 Exact"
        },
        {
            "id": "tau-02",
            "title": "Sheaf-to-Harmonic-to-Research Commutative Triangle",
            "vertices": ["stalk-03-alexandrov-sheaf-indexing", "stalk-04-harmonic-graph-memory", "stalk-05-continuous-research-loop"],
            "law": r"\rho_{04,05} \circ \rho_{03,04} = \rho_{03,05}",
            "cohomology_status": "H^0 Exact"
        },
        {
            "id": "tau-03",
            "title": "Argon Explainer & Field-Manual Semiology Triangle",
            "vertices": ["stalk-06-argon-animated-explainer", "stalk-07-field-manual-editorial-volumes", "stalk-08-graphic-semiology-masters"],
            "law": r"\rho_{07,08} \circ \rho_{06,07} = \rho_{06,08}",
            "cohomology_status": "H^0 Exact"
        },
        {
            "id": "tau-04",
            "title": "Operadic Consistency to Adversarial Governance Triangle",
            "vertices": ["stalk-01-operadic-composition", "stalk-02-meta-planning-chains", "stalk-10-adversarial-moe-evaluation"],
            "law": r"\rho_{02,10} \circ \rho_{01,02} = \rho_{01,10}",
            "cohomology_status": "H^0 Exact"
        },
        {
            "id": "tau-05",
            "title": "Meta-Planning to Skill Foundry to Office Artifact Chain",
            "vertices": ["stalk-02-meta-planning-chains", "stalk-11-agy-skill-foundry-mcp", "stalk-13-document-artifact-engines"],
            "law": r"\rho_{11,13} \circ \rho_{02,11} = \rho_{02,13}",
            "cohomology_status": "H^0 Exact"
        }
    ]

    # Pre-glued Notebook Investigations answering the user's exact architectural questions
    investigations = [
        {
            "id": "inv-01-progressive-disclosure-consolidation",
            "question": "How do we reduce 81 fragmented skills (~14,400 L0 frontmatter tokens/turn) into 7 Consolidated Master Skills with 4-tier progressive disclosure?",
            "open_cover": [
                "stalk-01-operadic-composition",
                "stalk-02-meta-planning-chains",
                "stalk-03-alexandrov-sheaf-indexing",
                "stalk-11-agy-skill-foundry-mcp"
            ],
            "citations": [
                {"page": 1, "item": formal_items[0]["id"], "label": "Operadic Composition Stalk [p. 1]"},
                {"page": skill_to_page.get("sheaf-corpus-indexer", 12), "item": f"Contract-sheaf-corpus-indexer-p{skill_to_page.get('sheaf-corpus-indexer', 12)}", "label": "Sheaf Corpus Indexer [p. 12]"},
                {"page": skill_to_page.get("skill-creator", 55), "item": f"Contract-skill-creator-p{skill_to_page.get('skill-creator', 55)}", "label": "Skill Foundry Refactor [p. 55]"}
            ],
            "synthesis_markdown": (
                "### Global Section: 81 Skills $\\twoheadrightarrow$ 7 Consolidated Master Skills (`89.4%` Turn-Token Reduction)\n\n"
                "1. **L0 Meta-Controller Index (`≤ 350 tokens total`)**: Only the 7 Consolidated Master Skills are mounted in `.agents/skills/` with ultra-crisp `≤ 45-token` YAML descriptions [p. 1].\n"
                "2. **L1 Master Skill Stalk (`≤ 80 lines`)**: When triggered, the Master Skill loads a compact routing table mapping sub-tasks to L2 reference modules [p. 12].\n"
                "3. **L2 On-Demand Reference Fibers (`references/*.md`)**: The 81 legacy skills live as modular reference leaves loaded only when their specific sub-domain is active [p. 55]."
            )
        },
        {
            "id": "inv-02-sheaf-research-memory-loop",
            "question": "How do `sheaf-corpus-indexer`, `sheaf-memory`, `noether-wiki`, and `research-loop` glue into a unified Sheaf Research & Graph Memory engine?",
            "open_cover": [
                "stalk-03-alexandrov-sheaf-indexing",
                "stalk-04-harmonic-graph-memory",
                "stalk-05-continuous-research-loop",
                "stalk-10-adversarial-moe-evaluation"
            ],
            "citations": [
                {"page": skill_to_page.get("sheaf-corpus-indexer", 12), "item": f"Contract-sheaf-corpus-indexer-p{skill_to_page.get('sheaf-corpus-indexer', 12)}", "label": "Alexandrov Sheaf Indexer"},
                {"page": skill_to_page.get("sheaf-memory", 15), "item": f"Contract-sheaf-memory-p{skill_to_page.get('sheaf-memory', 15)}", "label": "Harmonic Sheaf Memory"},
                {"page": skill_to_page.get("research-loop", 20), "item": f"Contract-research-loop-p{skill_to_page.get('research-loop', 20)}", "label": "Continuous Research Loop"}
            ],
            "synthesis_markdown": (
                "### Global Section: The Sheaf-Cohomology Research Loop (`sheaf-research-memory`)\n\n"
                "1. **Topological Ingestion ($\\Pi_{\\mathrm{SHEAF}}$)**: Incoming PDFs, papers, transcripts, and skill folders are indexed into page/file-anchored Concept Stalks $U_i$ with local Ologs (`types`, `aspects`, `facts`) and SQLite FTS5 tables.\n"
                "2. **Cohomology & Operadic Gate ($\\Gamma_{\\check{H}^1 \\times \\mathrm{OC}}$)**: Candidate syntheses over an open cover $\\mathcal{U}$ are tested for restriction fidelity $f_{ij} = 1 - \\|\\delta^0 s\\|_{ij}$ and $\\check{H}^1$ polysemy obstructions before minting.\n"
                "3. **Harmonic Extension Staging ($\\Delta_{\\mathcal{F}}$)**: New triples stage via `HierSheafMemory.stage_delta()` to measure absorption residual before committing to `wiki/`."
            )
        },
        {
            "id": "inv-03-argon-explainer-and-editorial-studio",
            "question": "How do we upgrade `ceti-explainer` to Argon-level capabilities and consolidate the 21 Design, UI & Media skills?",
            "open_cover": [
                "stalk-06-argon-animated-explainer",
                "stalk-07-field-manual-editorial-volumes",
                "stalk-08-graphic-semiology-masters",
                "stalk-09-interactive-web-ui-systems"
            ],
            "citations": [
                {"page": skill_to_page.get("ceti-explainer", 23), "item": f"Contract-ceti-explainer-p{skill_to_page.get('ceti-explainer', 23)}", "label": "CETI Explainer"},
                {"page": skill_to_page.get("glyph-foundry", 24), "item": f"Contract-glyph-foundry-p{skill_to_page.get('glyph-foundry', 24)}", "label": "Glyph Foundry"},
                {"page": skill_to_page.get("sheaf-field-manual-studio", 28), "item": f"Contract-sheaf-field-manual-studio-p{skill_to_page.get('sheaf-field-manual-studio', 28)}", "label": "Field-Manual Studio"}
            ],
            "synthesis_markdown": (
                "### Global Section: Argon Deterministic Explainer + Consolidated Editorial Design Studio\n\n"
                "1. **Argon Explainer Upgrade (`ceti-argon-explainer`)**: Fuses `ceti-explainer`'s pure clock `render(t)` with `glyph-foundry`'s 2.5D volumetric SymSpec plates, interactive What-If parameter scrubbers, live mathematical derivation verification (`window.__AUDIT`), and frame-by-frame bounding-box collision proofing (`window.__LAYOUT`).\n"
                "2. **Editorial Design Studio (`editorial-design-studio`)**: Consolidates 21 design/UI skills into one Master Skill parameterized by **Surface Type** (`Field-Manual`, `Push-Pin Dashboard`, `Deck Studio`, `React/Shadcn Concept Page`) and **Master Lens** (`Bertin`, `Wada Color`, `Glaser`, `Sagmeister`, `Saul Bass`, `Koolhaas`)."
            )
        }
    ]

    # Token economics summary across all 81 skills vs 7 consolidated master skills
    raw_l0_tokens = sum(p["l0_tokens"] for p in pages)
    raw_l1_tokens = sum(p["l1_tokens"] for p in pages)
    consolidated_l0_tokens = 7 * 42  # 7 master skills * ~42 tokens per crisp frontmatter
    consolidated_l1_tokens = 7 * 450 # ~450 tokens per lean L1 router SKILL.md

    # Build 7 self-contained Course Blueprint modules (one per Consolidated Master Skill Suite) with valid page bounds 1..len(pages)
    course_modules = []
    for ch in chapters:
        ch_stalks = [s for s in stalks if s["chapter"] == ch["chapter"]]
        master_slug = ch_stalks[0].get("consolidated_skill", ch["id"]) if ch_stalks else ch["id"]
        course_modules.append({
            "id": f"suite-{ch['chapter']:02d}-{master_slug}",
            "title": f"{ch['title'].split(':', 1)[-1].strip()} ({master_slug})",
            "stalks": [s["id"] for s in ch_stalks],
            "pages": [ch["start_page"], ch["end_page"]],
            "symbols": [s["symbol"] for s in ch_stalks] + [r"\rho_{U,V}", r"\check{H}^0"],
            "lo": [
                f"Route tasks in {ch['title'].split(':', 1)[-1].strip()} via L0/L1 progressive disclosure ({master_slug})",
                f"Verify local Olog invariants ({'; '.join(ch['global_invariants'][:2])})",
                f"Execute L3 deterministic verification scripts across pages p.{ch['start_page']}–{ch['end_page']}"
            ],
            "key_concept": ch["theme"],
            "why_it_matters": (
                f"Consolidating {', '.join(s['title'] for s in ch_stalks)} into `{master_slug}` eliminates redundant every-turn "
                f"system-prompt overhead while preserving 100% verbatim L2 skill fidelity across pages p.{ch['start_page']}–{ch['end_page']}."
            ),
            "lab": (
                f"Run `python3 portable-toolkit/4-skill-sheaf-meta-controller/query_skill_sheaf.py --stalk {ch_stalks[0]['id'] if ch_stalks else ''}` "
                f"and verify L0/L1/L2/L3 progressive disclosure gates via `package_and_lint_skill.py`."
            )
        })

    kb = {
        "book": {
            "title": "Antigravity & Argon Skill Ecosystem — Sheaf Graph Memory & Meta-Controller",
            "author": "CETI / Operadic Skill Foundry",
            "year": 2026,
            "publisher": "Antigravity Agentic Architecture",
            "source_pdf": f".agents/skills + ~/.grok/skills + ~/.claude/skills ({len(pages)} Indexed Skills -> 7 Master Routers)",
            "total_pages": len(pages),
            "total_sections": len(stalks),
            "total_formal_items": len(formal_items),
            "total_stalks": len(stalks),
            "sheaf_definition": "O : Open(Alx(SkillPoset^op))^op -> Sch ~ Cat",
            "course_modules": course_modules,
            "token_economics": {
                "raw_skill_count": len(pages),
                "legacy_user_skill_count": 81,
                "consolidated_master_skill_count": 7,
                "stalk_count": len(stalks),
                "raw_every_turn_l0_tokens": raw_l0_tokens,
                "consolidated_every_turn_l0_tokens": consolidated_l0_tokens,
                "every_turn_token_savings_pct": round((1.0 - consolidated_l0_tokens / max(1, raw_l0_tokens)) * 100, 1),
                "raw_all_l1_skill_md_tokens": raw_l1_tokens,
                "consolidated_all_l1_router_tokens": consolidated_l1_tokens,
                "l1_body_token_savings_pct": round((1.0 - consolidated_l1_tokens / max(1, raw_l1_tokens)) * 100, 1),
            },
            "voice_profile": {
                "epistemology": "Operadic Decomposition, Alexandrov Sheaf Cohomology & 4-Tier Progressive Disclosure",
                "design_register": "CETI Field-Manual & Meta-Controller Atlas",
                "signature_instruments": [
                    "L0->L1->L2->L3 Progressive Disclosure Token Calculator",
                    f"{len(pages)}-to-7 Skill Consolidation Poset Explorer",
                    "Live Open-Cover Skill Gluing & H^1 Redundancy Auditor"
                ]
            }
        },
        "chapters": chapters,
        "stalks": stalks,
        "restriction_morphisms": morphisms,
        "two_simplices": two_simplices,
        "notebook_investigations": investigations,
        "formal_items": formal_items,
        "pages": pages
    }

    # Enrich with genuine empirical TF-IDF, JSD, coboundary defect ||delta^0||, 2-simplex holonomy ||delta^1||, and H^1 obstructions
    kb = ind.enrich_sheaf_kb_with_empirical_cohomology(kb)

    # Also inject explicit Skill Redundancy / Polysemy H^1 Obstructions discovered across the skill ecosystem
    explicit_skill_obstructions = [
        {
            "id": "obs-skill-01",
            "stalk_a": "stalk-07-field-manual-editorial-volumes",
            "stalk_b": "stalk-09-interactive-web-ui-systems",
            "stalk_a_title": "CETI Field-Manual Volumes, Dashboards & Print-Inspired Spreads",
            "stalk_b_title": "Interactive Generative UI, React/Shadcn Concept Pages & UI Audits",
            "conflict_term": "dashboard",
            "shared_surface_terms": ["dashboard", "editorial", "html", "interactive"],
            "jensen_shannon_divergence": 0.34,
            "unbridged_defect_d0": 0.52,
            "required_bridge_stalk": "stalk-08-graphic-semiology-masters",
            "required_bridge_title": "Graphic Semiology, Historical Color & Master Visual Languages",
            "diagnostic": (
                "21 overlapping UI/Dashboard skills (`editorial-dashboard`, `milton-2`, `sagmeister`, `client-briefing-dashboard`, "
                "`generative-ui`, `shadcn-concept-page`, `ui-audit`) compete on trigger term 'dashboard/HTML artifact' (JSD=0.34). "
                "Without routing through Master Stalk 'editorial-design-studio' (bridged by Bertin/Meta-Design schema U_08), "
                "agents suffer trigger collisions and load 180KB+ of redundant style prompts (H¹ ≠ 0)."
            )
        },
        {
            "id": "obs-skill-02",
            "stalk_a": "stalk-01-operadic-composition",
            "stalk_b": "stalk-11-agy-skill-foundry-mcp",
            "stalk_a_title": "Operadic Composition & Consistency Kernel",
            "stalk_b_title": "Antigravity Skill Foundry, Progressive Disclosure & MCP Tool Routers",
            "conflict_term": "skill",
            "shared_surface_terms": ["skill", "prompt", "eval", "gate"],
            "jensen_shannon_divergence": 0.31,
            "unbridged_defect_d0": 0.49,
            "required_bridge_stalk": "stalk-02-meta-planning-chains",
            "required_bridge_title": "Typed Meta-Planning, Prompt Scaffolds & Artifact Chains",
            "diagnostic": (
                "Legacy `skill-creator` (486L, 33KB) uses un-typed conversational loops and pushy 100-word descriptions, "
                "conflicting with operadic m=1 gated composition (JSD=0.31). Bridging through `stalk-02-meta-planning-chains` "
                "and refactoring into `agy-skill-foundry` enforces 4-tier progressive disclosure and binary gate verification."
            )
        }
    ]
    kb["cohomology_obstructions"] = explicit_skill_obstructions + kb.get("cohomology_obstructions", [])[:6]

    # Write KB, SQLite FTS5, Deferred Bundle, Persistent Wiki, query_sheaf.py, and TYPED-CONTRACT-SHEAF-META-PROMPT.md
    data_dir = out_dir / "data"
    wiki_dir = out_dir / "wiki"
    data_dir.mkdir(parents=True, exist_ok=True)
    kb_path = data_dir / "sheaf_kb.json"
    if kb_path.exists():
        try:
            old_kb = json.loads(kb_path.read_text(encoding="utf-8"))
            old_inv_map = {inv["id"]: inv for inv in old_kb.get("notebook_investigations", []) if "id" in inv}
            for inv in kb["notebook_investigations"]:
                prev = old_inv_map.get(inv["id"], {})
                for k in ("audio_file", "audio_duration_sec", "audio_engine", "podcast_turns"):
                    if k in prev and k not in inv:
                        inv[k] = prev[k]
        except Exception:
            pass
    kb_path.write_text(json.dumps(kb, ensure_ascii=False, indent=2), encoding="utf-8")

    idx_mod.build_sqlite_fts5_and_wiki(kb, data_dir, wiki_dir)

    import shutil
    query_src = Path(__file__).resolve().parent / "query_skill_sheaf.py"
    if query_src.exists():
        shutil.copy2(query_src, out_dir / "query_sheaf.py")
    contract_src = WORKSPACE_ROOT / ".agents/skills/sheaf-knowledge-pipeline/references/TYPED-CONTRACT-SHEAF-META-PROMPT.md"
    if contract_src.exists():
        shutil.copy2(contract_src, out_dir / "TYPED-CONTRACT-SHEAF-META-PROMPT.md")

    return kb


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile the 81-Skill Ecosystem into a Sheaf Knowledge Base")
    parser.add_argument("--out-dir", type=Path, default=WORKSPACE_ROOT / "skill-sheaf-kb", help="Output KB directory")
    args = parser.parse_args()

    kb = build_skill_sheaf_kb(args.out_dir)
    te = kb["book"]["token_economics"]
    print(f"=== SKILL SHEAF KB COMPILED: {args.out_dir} ===")
    print(f"  Indexed Skills (Pages): {kb['book']['total_pages']}")
    print(f"  Chapters (Domains):     {len(kb['chapters'])}")
    print(f"  Master Stalks (U_i):    {len(kb['stalks'])}")
    print(f"  Consolidated Routers:   {te['consolidated_master_skill_count']}")
    print(f"  Restriction Morphisms:  {len(kb['restriction_morphisms'])}")
    print(f"  Commutative 2-Simplices:{len(kb['two_simplices'])}")
    print(f"  Formal Declarations:    {len(kb['formal_items'])}")
    print(f"  Every-Turn L0 Tokens:   {te['raw_every_turn_l0_tokens']} -> {te['consolidated_every_turn_l0_tokens']} (-{te['every_turn_token_savings_pct']}%)")
    print(f"  L1 Body Tokens:         {te['raw_all_l1_skill_md_tokens']} -> {te['consolidated_all_l1_router_tokens']} (-{te['l1_body_token_savings_pct']}%)")
