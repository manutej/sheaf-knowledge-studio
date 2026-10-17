---
name: meta-notebook
description: Run the complete FEDERATION-NOTEBOOK PIPELINE on any domain — research a corpus, extract a persistent wiki under conservation-law discipline, then build a five-volume interactive editorial arc (LAWS → CORPUS OBSERVED → PROSPECTS → ASSAY → YIELD) whose plate order IS the argument, wired to a federated router with a GROW protocol. Every claim is web- or file-verified, every number traces to a measured file, every hypothesis carries an honest verdict stamp. Use whenever someone wants a rigorous, reusable, evidence-grounded treatment, not a one-off doc. Triggers include "meta-notebook", "run the notebook pipeline on X", "five-volume treatment of X", "federation notebook for X domain", "turn this field/practice into a measured wiki and volumes", "prospects-and-assay treatment", "/meta-notebook". Task-agnostic across technical practices, scientific fields, and legal/medical/financial literature (with mandatory educational-not-advice framing). Do NOT use for a single chart, one-screen artifact, or quick summary.
---

# Meta-Notebook: the Federation-Notebook Pipeline

This skill codifies a pipeline that was **actually run end-to-end in one workspace** and
produced a five-volume interactive knowledge arc over a real corpus, backed by a measured
persistent wiki and a federated router. It is the reusable form of that run. Everything
below describes what *worked*, not an idealized process.

The output is not one artifact. It is a **compounding knowledge asset**: a research
registry, a wiki with memory, five editorial volumes whose plate order argues a thesis,
an overlap/assay layer that stakes and then measures hypotheses, and a router that lets
future sessions start warm. The discipline that makes it trustworthy is one rule applied
everywhere: **nothing is asserted that is not verified, and every number traces to a file
you can re-measure.**

**The through-line.** Declare what must stay true → measure it → stake what you don't yet
know as an honest hypothesis → strike the gate with a real number → say what it's worth.
The five volumes are that loop made legible: **LAWS → CORPUS OBSERVED → PROSPECTS → ASSAY
→ YIELD**.

## When to run this (and when not to)

Run it when a subject deserves a durable, evidence-grounded treatment that future work will
reuse: a technical practice you want to teach and maintain, a scientific field you want
mapped and staked, a body of legal/medical/financial literature you want surveyed honestly.
The tell is *persistence + evidence + argument*, not "make me a page."

Do **not** run the full pipeline for a single visual, a one-screen artifact, a quick answer,
or any corpus under ~20 concepts (the Atlas geometry and the volume arc both need density).
For those, use the component skills directly (see Composition).

## Reading order

`SKILL.md` (this file) is enough to run the pipeline at a high level. Drop into references
when you reach that phase:

| When you are… | Read |
|---|---|
| Writing agent prompts, running any phase operationally, verifying | `references/pipeline.md` |
| Building any of the five volumes (what each MEANS, plate archetypes, stamps) | `references/volume-archetypes.md` |
| Deriving the ontology/lenses for a new domain, or handling a regulated one | `references/domain-adaptation.md` |

This skill **composes** two engines it does not replace — read their SKILL.md when you
reach their phase: `noether-wiki` (the wiki engine: lenses, measured loop, merge) and
`field-notebook-craft` (the volume craft: Atlas, plates, single-mutator, counterpoint).

---

## 1. The pipeline as phases

Each phase has an **entry** criterion (do not start until true) and an **exit** criterion
(do not advance until true). The phases are a homomorphism of the wiki's own loop:
propose → measure → stake → strike → deliver. Skipping a phase's exit test is how the
whole thing rots — the exit tests are the conserved quantities of the *pipeline*.

### P0 — Scope & corpus policy

- **Entry:** a domain and a purpose. Nothing else.
- **Do:** In one short message, fix the **scope** (what's in, what's out), the **quality
  bar**, and the **corpus policy**. The corpus policy is the spine of the whole run:

  > **Source-verification rule (non-negotiable).** Every source is either **web-verified**
  > (a real, reachable page/paper you fetched and read) or **file-verified** (a file present
  > on disk you read). A claim whose source cannot be verified is **excluded**, not softened.
  > "Unverifiable = excluded" is a conserved quantity, not a preference. Fabricated citations
  > are the one failure this pipeline exists to prevent.

- For **regulated domains** (legal, medical, financial), also fix the **educational-not-advice
  framing** now — see `references/domain-adaptation.md`. Every volume in a regulated domain
  carries the disclaimer block; decide the wording at P0.
- **Exit:** a written scope note stating in/out, quality bar, corpus policy, and (if regulated)
  the disclaimer. State assumptions and proceed if unattended; confirm only if genuinely
  ambiguous.

### P1 — Research fan-out

- **Entry:** P0 scope note exists.
- **Do:** Fan out research agents across sources (see the research-agent skeleton in
  `references/pipeline.md`; compose `meta-research`). Each agent returns claims **with real
  citations only** — a claim without a verifiable source is dropped by the agent, not
  passed up for you to launder. Consolidate into two artifacts:
  - **`corpus.json`** — the structured corpus. One record per concept: `slug, title, tier,
    eyebrow, what, source, depends_on, enables, tension_with, see_also` (the
    field-notebook-craft schema). Compact keys for embedding later.
  - **`SOURCES.md`** — the source registry: one row per source with a stable id (`S1, S2…`),
    the URL or file path, verification method (web/file), date verified, and a one-line
    what-it-supports. Every citation in `corpus.json` and every future volume points here.
- **Exit:** `corpus.json` has ≥20 concepts with tiers; `SOURCES.md` has every source
  verified (web or file) with a method stamp; zero uncited substantive claims. **No invented
  data survives this phase** — spot-check three random citations by re-fetching/re-reading.

### P2 — Wiki EXTRACT under the measured loop

- **Entry:** `corpus.json` + `SOURCES.md` exist and passed P1 exit.
- **Do:** Run `noether-wiki` in **EXTRACT** mode (its §9 quickstart, Tier L2). This is the
  federation's persistent core — the thing that gives future sessions a warm start. Concretely:
  1. **Design the domain ontology** — a small table: 4–8 entity **types** and the **relations**
    between them, drawn from the corpus, never imposed (see `references/domain-adaptation.md`).
  2. **Set the lens registry** — defaults: `link.integrity`, `entity.unique`, `sync.index`,
    `prov.coverage` (exact-ish); `graph.orphans`, `page.stub-ratio` (soft); `prov.faithful`
    (shadow). Keep **3–7 gating lenses**.
  3. `python scripts/wikictl.py init <dir> --name <name>`, edit `wiki.yaml`, register sources.
  4. Extract in batches through the inner loop: PROPOSE → `wikictl.py measure` → DECIDE →
    REPAIR (k≤3, violations must strictly shrink) → COMMIT (append a LEDGER row) → ESCALATE.
- **Exit:** a full `measure` is **exact-clean** (the exact-clean requirement is absolute —
  never commit or deliver with exact violations) and within the drift budget; the LEDGER
  has a row per committed step. The wiki folder is the deliverable, not conversation context.

### P3 — The volume arc (I–V)

- **Entry:** an exact-clean wiki (P2) whose pages and graph are the source of truth for
  every plate.
- **Do:** Build five single-file HTML volumes with `field-notebook-craft` (parallel volume
  builders — one agent per volume — see `references/pipeline.md`). Each volume is a lens on
  the same corpus; together they are one argument. The **plate-mapping** — what each volume
  MEANS for an arbitrary domain — is the load-bearing translation:

  | Vol | Title (one noun) | For an arbitrary domain, this is… | Stamp regime |
  |---|---|---|---|
  | **I** | THE **LAWS** | the domain's **invariants / doctrines** — what must stay true; plates *enact* the laws they state | ◆ ratified · ◐ partial |
  | **II** | THE CORPUS **OBSERVED** | the **real graph measured** — patterns, symmetries, the gravitational center found by measurement, not asserted | ± refine introduced |
  | **III** | THE **PROSPECTS** | **staked hypotheses / strategies** not yet ratified — each with a verdict stamp and an honest **⊘ GATE** for anything unmeasured | ✓ accept · ± refine · ? speculative · ⊘ gate |
  | **IV** | THE **ASSAY** | **outcomes measured against reality** — gates struck to MEASURED with real numbers from a measure script; the ⚖ stamp | ⊘ GATE → ⚖ measured |
  | **V** | THE **YIELD** | the **so-what / decision map** — plate ORDER is the argument (finding → meaning → build → agenda → honest value ledger) | ⚖ · ✓ · ◆ · ◐ in a live ledger |

  The domain nouns change; the *movement* does not. Read `references/volume-archetypes.md`
  for each volume's plate archetypes, instrument patterns, stamp usage, and continuity tokens
  before building it. Vols III and IV are connected by the prospect→assay format (the
  SYMMETRY-PROSPECTS/PREFLIGHT pair — see `references/pipeline.md`).
- **Exit:** all five volumes render, every plate has a counterpoint, every number traces to
  `corpus.json` or a measure output, and each volume passes the Playwright verification
  (P3 checklist in `references/pipeline.md`). No volume ships un-verified.

### P4 — Tri-layer / overlap map (optional)

- **Entry:** ≥2 sibling corpora exist (e.g. this domain's wiki + a related one), OR the
  domain has distinct method/capability/knowledge layers worth showing in one section.
- **Do:** Build the overlap deliverable: a **functor table** carrying each law/pattern
  (METHOD) to where it is enforced (CAPABILITY) and where it is independently demonstrated
  (KNOWLEDGE) — plus an interactive tri-layer section with one layer per band. The prose
  version is a "the-map" page; the assay version is a PREFLIGHT (see `references/pipeline.md`).
  Skip this phase for a single-corpus domain.
- **Exit:** every edge in the map is a real triple traceable to a page; overlap verdicts
  (SAME/RELATED/DISTINCT/CONFLICT) are logged, not hidden.

### P5 — Delivery & federation

- **Entry:** volumes verified (P3), wiki exact-clean (P2).
- **Do:**
  - Write a **router `CLAUDE.md`** with the tiered loading law (Tier 0 shortlist → Tier 1
    one-liners → Tier 2 page → Tier 3 the one artifact) so future sessions load only what
    they need. If there are sibling wikis, declare the **federation = repeated merge, never
    shared mutation** rule and the typed `bridges_to` seams.
  - Ship the wiki folder and volumes as zips via SendUserFile.
  - Record the **GROW protocol** in the router: how to fold new material in later (baseline
    measure → add pages+entities+index rows → re-measure → commit only exact-clean → append
    LEDGER drift row → regenerate the Tier 0 block so router and index agree).
- **Exit:** the user can re-open the asset cold and a fresh session can route into it; the
  last LEDGER line records the delivery.

---

## 2. The orchestration contract

This pipeline was produced by **a thin coordinator plus opus subagent trees**, not by one
agent doing everything. The contract that made it work — keep it:

- **The coordinator stays thin.** It plans, spawns, and integrates. It does **not** do bulk
  file reading or file writing itself — that is what subagents are for. A coordinator that
  starts reading whole corpora has already lost the plot; delegate and keep the conclusion,
  not the file dumps.
- **Subagents do the file work.** Research agents fan out; a wiki extractor runs the measured
  loop; **parallel volume builders** build one volume each; a map builder builds P4. Give each
  a context-complete packet (see the skeletons in `references/pipeline.md`).
- **Every instrument is exercised; every volume is Playwright-verified.** Use the Chromium at
  `/opt/pw-browsers/chromium`. A volume is not done until an agent has loaded it, driven every
  interactive plate (the single-mutator instruments), and confirmed no console errors and a
  rendered still — see the P3 checklist. "It probably renders" is not verification.
- **Every number traces to a measured file.** No number appears in any volume, map, or claim
  unless it traces to `corpus.json` or a `measure`-script output on disk. When a volume needs
  a statistic, it reads it from the file — it does not estimate.

### The stamp grammar (mandatory, and never color-alone)

The verdict stamps are the honesty apparatus. Use them consistently across all five volumes:

| Stamp | Means |
|---|---|
| ◆ | ratified / established law |
| ✓ | accept — lens-ready / measured-and-holds |
| ± | refine — real but needs a named unit or a corpus first |
| ? | speculative — plausible, no evidence yet |
| ⊘ | GATE — unmeasured; honestly cannot be assayed yet |
| ◐ | partial |
| ⚖ | measured — a gate struck with a real number |

**Never encode a stamp by color alone** — each stamp is a glyph with a text label, so it
survives grayscale, screen readers, and colorblind readers (WCAG). A ⊘ that later becomes
⚖ is *struck through, not deleted* — the reader sees the gate was closed by measurement.

### Three more non-negotiables carried from the source run

- **Marginalia: real authors only.** Every sourced quote in a plate's marginalia cites a real,
  verifiable author/text. No invented attributions, ever. (The corpus policy again, at the
  plate level.)
- **Honest counterpoint on every plate.** Every plate carries a "when this is the wrong tool /
  where this breaks" panel. A volume with no counterpoints is advocacy, not a notebook.
- **No invented data.** If you don't have the number, stamp it ⊘ GATE and say what measurement
  would strike it — do not fabricate a plausible figure. The GATE is a feature; the fabrication
  is the one unforgivable defect.

---

## 3. Domain adaptation

The pipeline is domain-agnostic because the *movements* are invariant; only the nouns change.
Derive the domain ontology and lenses per `references/domain-adaptation.md`. Three worked
mappings of the volume arc:

| Volume | Technical practice | Scientific field | Legal literature |
|---|---|---|---|
| I LAWS | the practice's invariants / design rules | the field's conservation laws / first principles | **doctrines as conservation laws** (what a ruling must preserve) |
| II CORPUS OBSERVED | the real codebase/tool graph measured | the measured literature/citation graph | the case graph measured (which doctrines cite which) |
| III PROSPECTS | staked refactors / architecture bets | open hypotheses staked against data | litigation/argument **strategies** staked, unratified |
| IV ASSAY | outcomes measured (benchmarks, incidents) | experiments measured against predictions | **cases as assays** — how strategies fared against real rulings |
| V YIELD | what to build / adopt next, honest ledger | what the field should test next | decision map: which arguments are worth making, honestly |

**Regulated domains (legal / medical / financial) — mandatory framing.** These map cleanly
(doctrines-as-laws, cases-as-assays, strategies-as-prospects) but MUST carry an
**educational-not-advice** disclaimer block on every volume and the router: the artifact
explains how the domain reasons, it does **not** give legal/medical/financial advice, is not
a substitute for a licensed professional, and stakes/assays are analytical, not
recommendations. Wording and placement are specified in `references/domain-adaptation.md`.
Do not soften the source-verification rule for these domains — tighten it.

---

## 4. Composition

This skill is an integrator. It calls, and depends on, these skills — run each at its phase:

| Skill | Role in the pipeline |
|---|---|
| **noether-wiki** | P2 wiki EXTRACT + P5 GROW/merge — the persistent measured core |
| **field-notebook-craft** | P3 volume craft — Atlas, plates, single-mutator, counterpoint |
| **meta-research** | P1 research fan-out — decompose, triage by credibility, cross-verify |
| **meta-planning** | P0/orchestration — the coordinator's subagent plan and packets |
| **dataviz** | any chart/gauge/graph inside a plate or the overlap map |
| **wcag-contrast** | verify stamps and palette before shipping — color-plus-glyph, AA text |
| **skill-creator** | if you want to eval this pipeline's outputs or refine the skill itself |

Run tokens/research skills *before* the skills that consume them (research before extract,
extract before volumes). The volumes consume the wiki; the wiki consumes the research; the
research consumes the corpus policy. That ordering is the pipeline.

---

## The smell test (before you deliver)

1. Could a domain authority open any volume and recognize it as serious, honest work?
2. Is there a single number, quote, or claim you cannot trace to a verified source or a
   measured file? If yes, it does not ship — stamp it ⊘ GATE or remove it.
3. Does every prospect have a verdict, every plate a counterpoint, every gate an honest state?
4. Can a fresh session route into the asset cold and grow it via the GROW protocol?

If all four hold: deliver.
