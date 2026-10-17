# Volume archetypes — the five-volume arc, per volume

The arc is one argument in five movements: **LAWS → CORPUS OBSERVED → PROSPECTS → ASSAY →
YIELD**. The domain nouns change; the movement does not. Read the entry for a volume before
you build it. Each entry gives: purpose, plate archetypes, instrument patterns, stamp usage,
counterpoint discipline, the title rule, and the series-continuity tokens.

## Rules common to all five volumes

- **The one-noun title rule.** Every plate title puts the concept's *noun* in italic-serif
  accent color; the rest is roman. Exactly one italic per title. The volume's own name is a
  single noun too: **LAWS, OBSERVED (the corpus), PROSPECTS, ASSAY, YIELD**.
- **Series continuity tokens** (identical across all five, so they read as one work):
  the series name; a running head glyph (one mark, e.g. ❉); the edition line "Vol N of V";
  the shared 3-voice type system (variable serif / sans body / mono) and 5-actor warm palette;
  the meta-block grammar `N plates · N constellations · N relations · after {real authors}`.
  Change these and the five stop being one series.
- **Counterpoint discipline.** Every plate carries a "when this is the wrong tool / where this
  breaks" panel. This is heaviest in Vols I and V (where advocacy is most tempting) and is the
  honesty signature of the whole genre. A volume missing counterpoints reads as a sales deck.
- **Stamps are glyph + label, never color alone.** Full grammar: ◆ ratified · ✓ accept ·
  ± refine · ? speculative · ⊘ GATE (unmeasured) · ◐ partial · ⚖ measured.
- **Numbers trace to files.** Every count/stat reads from `corpus.json` or a measure output.

---

## Vol I — THE LAWS  ("the domain's invariants / doctrines")

**Purpose.** State the domain's conserved quantities — the things that must stay true —
and make each plate *enact* the law it states. This is the method the later volumes observe
and apply. It is foundational, not applied: the reader learns the grammar here.

**Plate archetypes:**
- *The Atlas* — the whole corpus as a celestial chart, tiers as constellations (the hero).
- *One plate per law/doctrine* — each states an invariant and demonstrates it in its own
  layout (a plate about "measure every step" shows a live measurement; a plate about
  "budget drift" shows drift accumulating against a bar).
- *The loop plate* — the domain's core cycle (propose→measure→repair→commit, or the field's
  equivalent) as a single walkable instrument.

**Instrument patterns.** Enactment instruments: the knob changes a parameter and the plate's
own body obeys the law it teaches. Single-mutator throughout — one state, one compute, one
render, many surfaces.

**Stamp usage.** ◆ ratified for established laws; ◐ partial for a law that holds only under
conditions. No ✓/±/? here — those belong to the prospect volumes.

**Counterpoint.** Each law's panel states where the law does *not* apply — the boundary of
its domain. This is what separates a law from dogma.

---

## Vol II — THE CORPUS OBSERVED  ("the real graph measured")

**Purpose.** Turn Vol I's instrument on the actual corpus and *measure* it. Findings come
from measurement, not assertion — e.g. "the gravitational center is the token layer, not the
glamorous artifacts" is a degree-centrality result, not an opinion.

**Plate archetypes:**
- *The census* — counts by type/tier, degree distribution, density (all from a measure output).
- *The center of mass* — which nodes are most connected; the surprising hub.
- *Symmetries found* — patterns that recur across the graph, each shown live.
- *The prospect-seam preview* — where two conserved quantities touch (staked, not yet assayed).

**Instrument patterns.** Measurement instruments: the reader filters/sorts the real graph and
watches the statistic recompute. Every readout is a real number from the corpus.

**Stamp usage.** Introduce **± refine** — a measured pattern that is real but needs a named
unit before it can be a lens. ◆ for the six-or-so already-ratified quantities shown for contrast.

**Counterpoint.** "What this measurement cannot see" — the limits of the graph as evidence.

---

## Vol III — THE PROSPECTS  ("staked hypotheses / strategies, unratified")

**Purpose.** Stake candidate conserved quantities / strategies against the corpus — each a
hypothesis *awaiting its assay*. A prospect is not a mine. This volume is the asset's
"escapes file of the future," not its balance sheet. Everything is staked, nothing is proven.

**Plate archetypes:**
- *One plate per prospect* using the 5-slot prospect format (hypothesis + evidence bullets /
  where it holds / measurement + proposed lens / break meaning / confidence + cheap
  falsification). See `pipeline.md` for the exact template.
- *The corpus-availability table* — which corpora are on disk today; unmeasured targets made
  visible up front, honestly.
- *The ranked portfolio* — prospects scored and sequenced; gated ones marked "high-value,
  sequence — don't drop," not buried.

**Instrument patterns.** Each prospect plate lets the reader toggle the verdict and see the
evidence and the "what would falsify this" probe. The instrument makes the honesty tangible.

**Stamp usage.** The full verdict vocabulary: **✓ accept** (lens-ready now) · **± refine**
(real, needs a unit or a corpus) · **? speculative** (plausible, no data) · **⊘ GATE**
(unmeasured — cannot be assayed yet, and says so). Verdict and confidence are separate axes.

**Counterpoint.** Built in as slot (5): the cheap falsification is the counterpoint —
the named probe that would kill the prospect. Every prospect must be falsifiable.

---

## Vol IV — THE ASSAY  ("outcomes measured against reality")

**Purpose.** Strike the gates. Each prospect that was ⊘ GATE gets a real measurement from a
deterministic script over the real corpus, and its gate re-stamps ⊘→⚖ MEASURED. The GATE
stamps are *struck through, not deleted* — the reader sees the gate closed by measurement.
The core question of any assay: one territory, or two that merely touch?

**Plate archetypes:**
- *The strike plates* — one per gate, using the assay-table format (hypothesis restated /
  canonical lens / measure method / actual number with breakdown / verdict stamp). See
  `pipeline.md`.
- *The alignment plate* — ontology/type alignment between corpora (how much overlaps).
- *The overlap split* — SAME / RELATED / DISTINCT / CONFLICT counts.
- *The bridges plate* — the seam: "keep separate, wire the seam" with typed cross-edges.

**Instrument patterns.** Re-run instruments: the reader sees the number and the command that
regenerates it. Every number is two-layer traceable — a JSON key from a named script AND the
schema/protocol clause that justifies measuring it.

**Stamp usage.** ⊘ GATE → ⚖ MEASURED, with the strike-through visible. ✅/⚠ within assay rows.

**Counterpoint.** "What the number does not settle" — the residual uncertainty after
measurement. A struck gate is not a closed question; state what remains open.

---

## Vol V — THE YIELD  ("the so-what / decision map")

**Purpose.** Say what the whole asset is worth — read as a working ledger, not a picture.
This is the resolution volume. **The plate ORDER is the argument.**

**Plate order = the argument (this is the archetype):**
1. *The finding* — the single sharpest measured result (e.g. "two layers share zero direct
   edges; they meet only through method").
2. *The meaning* — what that finding implies (the method layer is the transferable asset).
3. *The build* — what to construct/adopt given the meaning.
4. *The agenda* — what to do next; the sequenced prospects from Vol III/IV.
5. *The honest value ledger* — what is real, what is young, what is **not there yet**. If the
   asset has produced trust and reuse but no revenue/result, *say so*. The final plate's
   honesty is the whole arc's credibility.

**Instrument patterns.** A live yield ledger the reader can weigh — assets vs. liabilities,
proven vs. staked — with every entry stamped.

**Stamp usage.** All stamps carried into one ledger: ⚖ measured, ✓ accept, ◆ ratified,
◐ partial, ⊘ still-gated. The ledger's power is that it shows the gated items honestly beside
the measured ones.

**Counterpoint.** The whole volume is a counterpoint to hype: the last plate must include the
honest downside ("a lot of trust, real reuse, a young flywheel — and so far no revenue"
is the template). Never end on a triumph the numbers don't support.
