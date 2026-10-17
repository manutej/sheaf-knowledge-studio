# Domain adaptation — ontology, lenses, and regulated domains

The pipeline is domain-agnostic because the *movements* are invariant. What changes per
domain is: (a) the wiki ontology (types + relations), (b) the lenses (which invariants you
gate on), (c) the tiers/constellations, and (d) for regulated domains, a mandatory framing.
This file tells you how to derive each.

---

## 1. Deriving the domain ontology (the wiki's types + relations)

The ontology is the type system of the wiki. Draw it **from the corpus, never impose it**.
If you find yourself reaching for the same types you'd use for any domain, you haven't
looked at the corpus hard enough.

**Method:**
1. Read ~15–20 concept records from `corpus.json`. Cluster them by *what kind of thing* they
   are — not by topic, by role. A concept is usually one of: a **principle/law**, a
   **thing/artifact**, an **actor/agent**, a **process/method**, a **decision/outcome**, or
   an **evidence/source** node. Your 4–8 types are the clusters that actually appear.
3. Name the **relations** — the edges that carry meaning in this domain. Ask of each pair of
   types: what predicate connects them? Keep the set small and typed (domain → range). Typical:
   `depends_on`, `enables`, `tension_with`, `is_a`, `part_of`, `demonstrated_by`, `cites`.
4. Sanity check: if one type holds 80% of concepts and another holds 2, the typing is wrong —
   re-cluster. Balanced-ish types mean you found real structure.

**Worked ontologies (three domains):**

| Domain | Types (4–8) | Key relations |
|---|---|---|
| Technical practice | Principle, Tool, Pattern, Decision, Runbook, Concept | `enforces`, `depends_on`, `composes_with`, `tension_with` |
| Scientific field | Law, Phenomenon, Method, Hypothesis, Result, Instrument | `predicts`, `measured_by`, `supports`, `contradicts` |
| Legal literature | Doctrine, Case, Statute, Argument, Holding, Authority | `cites`, `distinguishes`, `overturns`, `applies` |

**Tiers / constellations** (for the Atlas, ≤12): a tier is a *family* a concept belongs to,
also drawn from the corpus. For a scientific field: sub-fields. For legal: areas of law. If
tier counts come out wildly uneven, the classification is wrong — redo it.

---

## 2. Lens elicitation for non-code domains

Lenses are the conserved quantities you gate on. For a codebase they're obvious
(link-integrity, types). For a field, a literature, a doctrine, they need eliciting. The
one question that elicits them for **any** domain:

> **"What must still be true after this change / claim / strategy — such that if it stopped
> being true, the work is wrong regardless of how good it looks?"**

Ask it of the *domain*, not of one page. The answers are your candidate lenses. Then filter
by the rejection rules (a candidate is not a lens if it can't be measured without the
author's cooperation, if a judge-lens has no written rubric, if a soft lens has no named
drift unit, or if it duplicates an existing lens).

**Universal starter lenses (apply to every domain):**
`link.integrity` (every wikilink resolves), `entity.unique` (no duplicate entities),
`sync.index` (pages ↔ graph agree), `prov.coverage ≥ 0.9` (claims cite verified sources) —
all exact-ish; `graph.orphans`, `page.stub-ratio` — soft; `prov.faithful` — shadow.

**Domain-specific lens examples:**

| Domain | Example domain lens | Elicited from the question above |
|---|---|---|
| Scientific field | `result.reproducible` (every Result cites a Method that could regenerate it) | "a claimed result must stay reproducible" |
| Legal literature | `holding.grounded` (every Argument cites a real Case/Statute) | "an argument must stay grounded in authority" |
| Technical practice | `decision.reversible` (every Decision records its escalation path) | "a decision must stay auditable" |

Keep **3–7 gating lenses**; run the rest in shadow so the outer loop (REFIT) can promote
them on evidence.

---

## 3. Regulated domains — mandatory educational-not-advice framing

Legal, medical, and financial literature map cleanly onto the arc (doctrines-as-conservation-
laws, cases-as-assays, strategies-as-prospects). But because a reader could mistake the asset
for professional advice, **every volume and the router MUST carry a disclaimer block**, and
the source-verification rule is *tightened*, not relaxed. This is a safety requirement, not a
style choice.

**Where it goes:** the frontispiece of every volume, and the top of the router `CLAUDE.md`.
Set the exact wording at P0 so it is identical everywhere.

**Disclaimer block templates** (adapt the profession; keep the four commitments):

*Legal:*
> **Educational, not legal advice.** This volume explains how {area of law} reasons about its
> own doctrines. It is not legal advice, does not create an attorney–client relationship, and
> is no substitute for a licensed attorney in your jurisdiction. Prospects and assays here are
> analytical stakes measured against the literature — not recommendations to take any legal action.

*Medical:*
> **Educational, not medical advice.** This volume explains how {field} reasons about {topic}.
> It is not medical advice, diagnosis, or treatment, and is no substitute for a qualified
> clinician. Nothing here should be used to make a health decision; consult a licensed
> professional.

*Financial:*
> **Educational, not financial advice.** This volume explains how {domain} reasons about
> {topic}. It is not financial, investment, tax, or legal advice, and is no substitute for a
> licensed advisor. Prospects and assays are analytical, not recommendations to buy, sell, or
> hold anything.

**The four commitments every disclaimer keeps** (regardless of profession): (1) names the
artifact as *educational / explanatory*; (2) states plainly it is **not** advice in that
regulated field; (3) says it is **not a substitute** for a licensed professional; (4) reframes
the pipeline's stakes/assays as **analytical, not recommendations**.

**Tightened corpus policy for regulated domains.** Prefer primary sources (statutes, published
rulings, peer-reviewed studies, regulatory filings) over secondary commentary. A prospect in a
regulated domain that cannot be file/web-verified is not merely excluded — it must not be
stated as though plausible. When you cannot measure, stamp ⊘ GATE and say what would strike it;
never fabricate a figure or imply a professional conclusion the sources don't support.
