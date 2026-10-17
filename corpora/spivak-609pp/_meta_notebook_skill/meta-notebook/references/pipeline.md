# Pipeline — operational detail & agent-prompt skeletons

The phase-by-phase mechanics, the parameterized agent prompts distilled from the run that
worked, and the verification checklist every agent must run. `{braces}` are slots the
coordinator fills. The coordinator stays thin: it fills slots, spawns, and integrates —
it does not read corpora or write volumes itself.

## Table of contents

- P0 scope note format
- P1 research fan-out + research-agent skeleton
- P2 wiki extractor skeleton + the domain-ontology table
- P3 volume-builder skeletons (one per volume) + prospect/assay pair
- P4 map-builder skeleton
- P5 router CLAUDE.md skeleton + GROW protocol
- The verification checklist (run by every agent)

---

## P0 — Scope note format

A short written block the coordinator produces and every downstream agent receives verbatim:

```
DOMAIN: {domain}
PURPOSE: {who reads the asset and what decision it serves}
IN SCOPE: {bullet list}     OUT OF SCOPE: {bullet list}
QUALITY BAR: {e.g. "a domain authority would recognize it as serious work"}
CORPUS POLICY: every source web-verified (fetched+read) or file-verified (on disk+read);
  a claim whose source cannot be verified is EXCLUDED, not softened. No fabricated citations.
REGULATED: {none | legal | medical | financial}  → if set, disclaimer block = {text}
```

## P1 — Research fan-out

Spawn N research agents (compose `meta-research`), one per sub-question or source cluster.
Consolidate their returns into `corpus.json` (concept records) and `SOURCES.md` (registry).

**`SOURCES.md` row format** — the trust ledger every citation resolves to:

```markdown
- **[S3]** — {URL or absolute file path} — {web|file}-verified {YYYY-MM-DD} — {one line: what it supports}
```

**`corpus.json` record** (field-notebook-craft schema; compact keys `s/t/T/e/w/d/n/x/r/S`
when embedding):

```json
{ "slug":"kebab-id", "title":"Title Case", "tier":"classification",
  "eyebrow":"~150-char definition", "what":"200-400 word explanation",
  "source":"[S3][S7]", "depends_on":["slug"], "enables":["slug"],
  "tension_with":["slug"], "see_also":["slug"] }
```

### Research-agent skeleton

```
You are a research agent for the meta-notebook pipeline. {P0 scope note}
SUB-QUESTION: {one focused question or source cluster}
DO:
1. Find sources that answer it. For EACH source, VERIFY it: web sources must be fetched and
   read (WebFetch/WebSearch); file sources must be read from disk. Record URL/path, the
   verification method, and today's date.
2. Extract concepts as records: {slug,title,tier,eyebrow,what,source,depends_on,enables,
   tension_with,see_also}. Cite a source id on every substantive claim.
3. DROP any claim whose source you could not verify. Do not pass unverifiable claims up —
   exclusion is the rule, not softening.
RETURN: (a) concept records as JSON, (b) SOURCES.md rows for every source you verified,
   (c) a one-line note on anything you dropped and why. Absolute paths only.
```

**P1 exit check:** ≥20 concepts with tiers; every `SOURCES.md` row has a verification method
+ date; zero uncited substantive claims; re-verify 3 random citations before advancing.

## P2 — Wiki extractor

One extractor agent runs `noether-wiki` EXTRACT (read that skill's SKILL.md §9 and
LENS-CATALOG). First design the **domain ontology table**, then extract in batches.

**Domain-ontology table** (goes in `wiki.yaml`, drawn from the corpus, never imposed):

```
TYPES (4–8):      {Type} — {what entities of this type are}          × 4–8 rows
RELATIONS:        {predicate} : {domain-type} → {range-type}         × the edges that matter
LENS REGISTRY:    exact:  link.integrity, entity.unique, sync.index, prov.coverage(≥0.9)
                  soft:   graph.orphans, page.stub-ratio
                  shadow: prov.faithful
                  (keep 3–7 GATING; everything else shadow)
```

### Wiki-extractor skeleton

```
You are the wiki extractor for the meta-notebook pipeline. {P0 scope note}
INPUTS: corpus.json at {path}, SOURCES.md at {path}.
DO (noether-wiki EXTRACT, Tier L2):
1. Propose the ontology table (4–8 types + relations) FROM the corpus. State it.
2. `python {noether}/scripts/wikictl.py init {wiki-dir} --name {name}`; edit wiki.yaml with
   the ontology + lens registry (defaults above). Register every source in SOURCES.md first.
3. Extract in batches of 3–10 pages through the inner loop: PROPOSE pages+graph rows →
   `wikictl.py measure {wiki-dir} --baseline {snap}` → if exact violations, REPAIR only what
   the measure output names (k≤3, violation multiset must strictly shrink; if it doesn't,
   ESCALATE) → COMMIT + append one LEDGER row. Entities first, then relations, then hubs.
4. EXACT-CLEAN is absolute: never commit with exact violations. Every non-obvious claim
   cites a [Sn] that exists in SOURCES.md.
RETURN: the wiki dir path, final measure output (must be exact-clean + within budget), the
   ontology table, the LEDGER tail. Absolute paths.
```

**P2 exit check:** `wikictl.py measure` exact-clean, within drift budget, LEDGER row per step.

## P3 — Volume builders (parallel, one agent per volume)

All five compose `field-notebook-craft` and read the exact-clean wiki as source of truth.
Read `references/volume-archetypes.md` for each volume's archetypes before building. Shared
packet slots: `{wiki-dir}`, `{corpus.json path}`, `{SOURCES.md path}`, `{palette/tokens}`,
`{series continuity tokens: series name, "Vol N of V", shared running head glyph}`.

### Generic volume-builder skeleton (specialize per volume)

```
You are the Vol {N} builder for the meta-notebook pipeline. {P0 scope note}
SERIES: {series name}, Vol {N} of V — {"THE LAWS"|"THE CORPUS OBSERVED"|"THE PROSPECTS"|
   "THE ASSAY"|"THE YIELD"}. THESIS: {one line — what this volume argues}.
SOURCE OF TRUTH: wiki at {wiki-dir}, corpus.json at {path}. Read pages/ and graph/ — do NOT
   invent content or numbers. Every number in a plate traces to corpus.json or a measure file.
BUILD (field-notebook-craft, single HTML file):
- Frontispiece with the series continuity tokens + meta-block ({N plates · N constellations ·
  N relations · "after {real authors}"}).
- Plates per this volume's archetype list ({from volume-archetypes.md}). Each plate: five-part
  anatomy, one italic noun in the title, the single-mutator instrument, a Derived panel reading
  the state, and a COUNTERPOINT ("when this is the wrong tool"). Marginalia quote REAL authors
  from SOURCES.md only.
- Stamps per this volume's regime ({from the SKILL.md plate-mapping table}); every stamp is a
  glyph + text label, NEVER color alone. A struck gate (⊘→⚖) is struck through, not deleted.
- Honor prefers-reduced-motion; one file, no build.
VERIFY: run the verification checklist (below) with Chromium at /opt/pw-browsers/chromium.
RETURN: the HTML path, a rendered screenshot path, the checklist result. Absolute paths.
```

**Per-volume specialization** (full detail in `volume-archetypes.md`):

- **Vol I — THE LAWS.** Plates *enact* the domain's invariants/doctrines. Each plate's
  instrument demonstrates the law it states. Stamps: ◆ ratified, ◐ partial.
- **Vol II — THE CORPUS OBSERVED.** Plates measure the real graph — degree, density, the
  gravitational center, symmetries found by measurement. Introduce ± refine. Every stat from
  a measure output.
- **Vol III — THE PROSPECTS.** Plates present staked hypotheses/strategies, each with a verdict
  (✓/±/?) and an honest **⊘ GATE** for anything unmeasured. Use the prospect format below.
- **Vol IV — THE ASSAY.** Plates strike gates: each prospect gets a measured number and its
  gate re-stamps ⊘→⚖. Use the assay format below. Numbers trace to a measure script output.
- **Vol V — THE YIELD.** **Plate ORDER is the argument:** finding → meaning → build → agenda →
  honest value ledger. The last plate is an honest ledger (what's real, what's young, what's
  not there yet — including "no revenue / no result yet" if true).

### The prospect format (Vol III connective tissue — the SYMMETRY-PROSPECTS pattern)

A prospect document / plate stakes hypotheses. Front matter: title, author, date, **Status**
(declares the honesty rule: every item measurable-now or explicitly speculative), **Discipline**
(cites the rejection-rule ruleset). Each prospect entry:

```
### {ID} — {short title} — **{VERDICT}**
(1) Hypothesis. {the conserved quantity / staked claim} + evidence bullets, each `claim (file:line or [Sn])`
(2) Where it holds. {scope}
(3) Measurement. {mode: exact|soft} · proposed lens `id` · family · {rejection-rule note; drift_unit if soft}
(4) Break meaning. {what a violation means — structural and practical consequence}
(5) Confidence: {HIGH|MEDIUM|LOW}. Cheap falsification: {a named probe → the finding that kills it}
```

**Verdict key:** `ACCEPT` (lens-ready / measurable now) · `REFINE` (real but needs a named
unit or a corpus first) · `REJECT` (fails a rejection rule; recorded for completeness).
Verdict and confidence are orthogonal axes. Unmeasured-corpus prospects are stamped
`REFINE / speculative (needs data)` and their measurement slot states plainly they fail
rejection rule 1 (no snapshot to measure) — they are **⊘ GATE**, not lenses yet. A ranked
portfolio at the end sequences the gated ones ("high-value, sequence — don't drop"), and a
corpus-availability table (`| Corpus | on disk today | evidence |`) makes absent targets
visible up front.

### The assay format (Vol IV connective tissue — the PREFLIGHT pattern)

An assay strikes gates to MEASURED. Header: title, `Assay date · corpus · comparison`,
**Status** (`✅ MEASURED — supersedes prior GATE stamps`), **Method** (cites the protocol),
and a blockquoted **Re-run** command naming the generator script. The core is one table whose
row is the reusable assay unit:

```
| {hypothesis restated as a named check} | {canonical lens (exact|soft|≥thr)} | {measure method in one phrase} | {actual number from measurements.json, with breakdown} | {✅ CLEAN | ⚠ note | ⚖ MEASURED} |
```

Every non-clean row gets a prose paragraph below: restate the number, interpret it, cite the
schema/protocol clause that justifies measuring it, and land an ACCEPT/REFINE/REJECT judgment.
**Provenance of each number is two-layer:** a machine source (a JSON key regenerable by the
named script — e.g. `measurements.json → lenses.dead_wikilinks.count`) AND a doctrinal source
(the schema/protocol clause that says why it's measured). When a gate closes, add a
`> **SUPERSEDED**` banner at the old prospect and a dated addendum carrying the numbers —
nothing is silently overwritten; the old protocol is retained as the method of record.

## P4 — Map builder (optional)

### Map-builder skeleton

```
You are the overlap-map builder. {P0 scope note}
INPUTS: sibling wikis at {paths} (or the single wiki's method/capability/knowledge facets).
BUILD:
- A functor table: | Method (law/pattern) | Capability (where enforced) | Knowledge (where
  independently demonstrated) |. Every cell is a real page/triple — cite it. No invented edges.
- An interactive tri-layer HTML section: one band per layer (METHOD/CAPABILITY/KNOWLEDGE),
  layer-toggle pills, edges as real triples. Distinct accent per layer, glyph+label not color-alone.
- If merging siblings: classify entity pairs SAME/RELATED/DISTINCT/CONFLICT (noether-wiki
  MERGE-PROTOCOL); surface conflicts, never hide them; a "zero conflicts" merge is too shallow.
VERIFY with the checklist. RETURN: HTML path, functor table, screenshot. Absolute paths.
```

## P5 — Router CLAUDE.md + GROW protocol

### Router skeleton

```markdown
# {Asset} Router — CLAUDE.md
Load by tiers (metadata → body → resources), never everything at once:
1. Tier 0 — the shortlist surface below (names by constellation). Shortlist 1–2.
2. Tier 1 — one-liners: read {index}#tier-1, only shortlisted sections.
3. Tier 2 — the page: {pages}/<id>.md for 2–3 finalists.
4. Tier 3 — the ONE chosen artifact's own file.

## Tier 0 — shortlist ({N} entries, {M} constellations)
- **{Constellation}** ({n}): {name} · {name} · …

## Sibling wikis (if federated)
Federation = repeated merge, never shared mutation. Each wiki grows under its own registry;
a master is periodically re-derived by merging frozen parents. Typed `bridges_to` seams: {list}.
Pick the layer by the KIND of question; load only that wiki.

## Maintaining this router (noether-wiki GROW)
1. Baseline: `wikictl.py measure {wiki}`.  2. Add page + entities.jsonl row + Tier 0/1 entries.
3. Re-measure; commit only EXACT-CLEAN; append the drift row to _meta/LEDGER.md.
4. Regenerate the Tier 0 block from the index (they must agree — divergence = sync.index violation).
Last measure: {date · N pages · N triples · prov · exact-clean · drift x/B}.
```

**Regulated domains:** put the educational-not-advice disclaimer at the top of the router too.

---

## The verification checklist (every agent runs this before returning)

Non-negotiable. "It probably works" is not a result.

1. **Renders.** Load the HTML in Chromium (`/opt/pw-browsers/chromium`, headless via Playwright).
   Zero console errors. Capture a desktop and a mobile screenshot; confirm the page is not blank.
2. **Every instrument exercised.** Drive each interactive plate's single-mutator: change every
   knob, confirm all bound surfaces update together (the Derived panel, specimen, and CSS-var
   layout all move from one state). A dead knob fails the volume.
3. **Every number traced.** For each statistic/count in the artifact, confirm it exists in
   `corpus.json` or a `measure`-script output on disk. Any untraceable number → remove or ⊘ GATE.
4. **Every claim sourced.** Every marginalia quote cites a real author present in SOURCES.md.
   Every substantive claim resolves to a verified [Sn]. No invented attributions.
5. **Stamps legible without color.** Each stamp is a glyph + text label; struck gates are
   struck through, not deleted. Spot-check in grayscale.
6. **Counterpoint present.** Every plate has its "when this is the wrong tool" panel.
7. **Motion safe.** `prefers-reduced-motion` yields a still frame for every animation.
8. **(Regulated)** The educational-not-advice disclaimer block is present and unmodified.

Return: the artifact path, screenshot path(s), and a pass/fail line per checklist item.
