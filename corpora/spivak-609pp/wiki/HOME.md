---
id: cattheory-sheaf-wiki-home
title: "Sheaf Knowledge Base: Category Theory for the Sciences (David I. Spivak)"
type: SheafSiteRoot
total_pages: 609
total_formal_declarations: 877
total_concept_stalks: 30
total_restriction_morphisms: 55
total_2_simplices: 8
---

# Sheaf Knowledge Base — *Category Theory for the Sciences* (David I. Spivak)

Welcome to the **Sheaf Knowledge Base & Deep LLM Wiki** for David I. Spivak's *Category Theory for the Sciences* (MIT Press, 2014, 609 PDF pages).

## Why a Sheaf Knowledge Base Instead of a Flat Graph?

Following **Section 7.2.3.11 (*Sheaf of ologged concepts*, PDF p. 523–524)** of Spivak's book:
1. **Simplicial Conceptual Complex $X$ & Alexandrov Site $\mathcal{X} = \text{Alx}(X^{\text{op}})$:** Every core conceptual domain is a vertex $v \in X_0$, overlapping syntheses are higher simplices $u \in X_n$, and open sets $U \in \text{Open}(\mathcal{X})$ are conceptual covers.
2. **Stalks as Local Ologs ($\mathcal{O}(v) \in \mathbf{Sch} \simeq \mathbf{Cat}$):** Each of the **30 Concept Stalks** carries a formal **Olog** (typed boxes, deterministic functional aspect arrows, and commutative path equations) grounded in exact PDF pages and numbered definitions.
3. **Restriction Morphisms ($\rho_{U \to V} : \mathcal{O}(U) \to \mathcal{O}(V)$):** 52 explicit restriction maps and 8 commutative 2-simplices verify how general categorical structures specialize and agree on overlaps.
4. **Global Section Querying ($H^0(\mathcal{U}, \mathcal{O})$):** Asking a Gemini Notebook-style question over any selected open cover $\mathcal{U} = \{U_1, \dots, U_k\}$ retrieves the local sections $s_i \in \mathcal{O}(U_i)$, checks overlap compatibility $\rho_{U_i, U_i \cap U_j}(s_i) = \rho_{U_j, U_i \cap U_j}(s_j)$, and glues them into a cited global section.

## Chapters (Macro Open Covers)

- [[ch1-introduction]] — **Chapter 1: Introduction: Science as Agreement & The Categorical Pipeline** (PDF Pages 11–25)
- [[ch2-category-of-sets]] — **Chapter 2: The Category of Sets, Commutative Diagrams, and Ologs** (PDF Pages 26–67)
- [[ch3-fundamental-set]] — **Chapter 3: Fundamental Considerations in Set: Limits, Colimits & Universal Constructions** (PDF Pages 68–159)
- [[ch4-pre-categorical-models]] — **Chapter 4: Categories and Functors, Without Admitting It: Monoids, Groups, Graphs, Orders & Databases** (PDF Pages 160–266)
- [[ch5-basic-category-theory]] — **Chapter 5: Basic Category Theory: Categories, Functors, Natural Transformations & Cat ≃ Sch** (PDF Pages 267–391)
- [[ch6-fundamental-cat]] — **Chapter 6: Fundamental Considerations of Categories: Universal Limits, Colimits & Grothendieck Construction** (PDF Pages 392–460)
- [[ch7-categories-at-work]] — **Chapter 7: Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads** (PDF Pages 461–584)

## Complete Atlas of the 30 Concept Stalks ($\mathcal{F}_v$)

| # | Stalk ID | Concept Stalk Title | Symbol | Sec | PDF Pages | Items |
|---|---|---|---|---|---|---|
| 1 | [[scientific-agreement-worldviews]] | **Science as Agreement & Categorical Worldviews** | `W_sci` | 1.1–1.4 | p. 11–25 | 0 |
| 2 | [[sets-and-functions]] | **The Category Set: Sets, Functions & Isomorphisms** | `Set` | 2.1 | p. 26–43 | 33 |
| 3 | [[commutative-diagrams]] | **Commutative Diagrams & Path Equations** | `Diag(C)` | 2.2 | p. 44–46 | 2 |
| 4 | [[ologs-ontology-logs]] | **Ologs (Ontology Logs): Functional Worldviews** | `Olog` | 2.3 | p. 47–67 | 12 |
| 5 | [[products-and-projections]] | **Products & Universal Pairing in Set** | `X × Y` | 3.1.1 | p. 68–79 | 15 |
| 6 | [[coproducts-and-injections]] | **Coproducts & Disjoint Unions in Set** | `X ⊔ Y` | 3.1.2 | p. 80–87 | 16 |
| 7 | [[pullbacks-and-fiber-products]] | **Pullbacks (Fiber Products) & Constraint Solving** | `X ×_Z Y` | 3.2.1 | p. 88–101 | 21 |
| 8 | [[spans-experiments-matrices]] | **Spans, Scientific Experiments, Equalizers & Finite Limits** | `X ← R → Y` | 3.2.2–3.2.3 | p. 102–109 | 14 |
| 9 | [[pushouts-and-colimits-set]] | **Equivalence Relations, Pushouts & Gluing in Set** | `X ⊔_W Y` | 3.3 | p. 110–127 | 28 |
| 10 | [[currying-exponentials-subobjects]] | **Currying, Exponentials, Subobject Classifier & Relative Sets** | `Hom(A×B, C) ≅ Hom(A, C^B)` | 3.4 | p. 128–159 | 57 |
| 11 | [[monoids-and-actions]] | **Monoids, Agent Actions & Finite State Machines** | `(M, e, ⋆) ↷ S` | 4.1 | p. 160–191 | 61 |
| 12 | [[groups-and-symmetries]] | **Groups, Invertible Symmetries & Orbit Quotients** | `G ↷ X → X/G` | 4.2 | p. 192–200 | 20 |
| 13 | [[graphs-and-paths]] | **Graphs, Path Categories & Homomorphisms** | `G = (V, A, src, tgt)` | 4.3 | p. 201–220 | 36 |
| 14 | [[orders-lattices-hierarchies]] | **Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces** | `(P, ≤) ∈ PrO` | 4.4 | p. 221–244 | 48 |
| 15 | [[database-schemas-instances]] | **Categorical Databases: Schemas (G, ≃) & Table Instances** | `C = (G, ≃), I : C → Set` | 4.5 | p. 245–266 | 31 |
| 16 | [[categories-objects-morphisms]] | **Categories: Objects, Morphisms, Identities & Composition** | `C = (Ob(C), Hom_C, id, ∘)` | 5.1.1 | p. 267–284 | 32 |
| 17 | [[functors-structure-maps]] | **Functors: Structure-Preserving Maps Between Worldviews** | `F : C → D` | 5.1.2–5.2 | p. 285–337 | 112 |
| 18 | [[natural-transformations-functor-cat]] | **Natural Transformations & The Category of Database Instances** | `α : F ⇒ G ∈ Fun(C, D)` | 5.3.1–5.3.3 | p. 338–370 | 54 |
| 19 | [[categorical-equivalence-cat-sch]] | **Equivalence of Categories & Theorem Cat ≃ Sch** | `Cat ≃ Sch` | 5.3.4–5.4 | p. 371–391 | 29 |
| 20 | [[universal-limits-and-cones]] | **Universal Limits, Cones & Terminal Objects in Cat** | `lim_{← J} D` | 6.1.1–6.1.3 | p. 392–428 | 73 |
| 21 | [[universal-colimits-and-cocones]] | **Universal Colimits, Cocones & Interconnected Gluing** | `colim_{→ J} D` | 6.1.3 | p. 429–438 | 15 |
| 22 | [[grothendieck-construction-comma]] | **Opposite Categories, Grothendieck Construction ∫I & Comma Categories** | `∫_C I → C` | 6.2 | p. 439–460 | 26 |
| 23 | [[adjoint-functors-hom-iso]] | **Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges** | `Hom_D(L(c), d) ≅ Hom_C(c, R(d))` | 7.1.1–7.1.3 | p. 461–480 | 19 |
| 24 | [[data-migration-delta-sigma-pi]] | **Categorical Data Migration: Δ_F, Σ_F (Left Kan) & Π_F (Right Kan)** | `Σ_F ⊣ Δ_F ⊣ Π_F` | 7.1.4 | p. 481–492 | 11 |
| 25 | [[presheaves-representables-yoneda]] | **Functor Categories, Presheaves, Representables & Yoneda's Lemma** | `Hom_{C-Set}(Y_c, I) ≅ I(c)` | 7.2.1–7.2.2 | p. 493–517 | 32 |
| 26 | [[sheaves-and-local-to-global-gluing]] | **Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom** | `O : Open(X)^op → Set` | 7.2.3.1–7.2.3.10 | p. 518–522 | 10 |
| 27 | [[sheaf-of-ologged-concepts-descent]] | **Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data** | `O : Open(Alx(X^op))^op → Sch` | 7.2.3.6 & 7.2.3.11–7.2.3.14 | p. 521–526 | 8 |
| 28 | [[monads-and-contextual-computation]] | **Monads (T, η, μ): Formalizing Experimental & Computational Context** | `(T : C → C, η : id ⇒ T, μ : T∘T ⇒ T)` | 7.3.1–7.3.2 | p. 527–539 | 13 |
| 29 | [[kleisli-categories-scientific-method]] | **Kleisli Categories C_T & Reconciling the Scientific Method Olog** | `Hom_{C_T}(X, Y) = Hom_C(X, T(Y))` | 7.3.3–7.3.5 | p. 540–556 | 24 |
| 30 | [[operads-and-hierarchical-composition]] | **Operads, Wiring Diagrams & Hierarchical Self-Similarity** | `O(x₁, …, x_n; y)` | 7.4 | p. 557–584 | 30 |
