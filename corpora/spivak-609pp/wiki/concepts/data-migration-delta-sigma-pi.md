---
id: data-migration-delta-sigma-pi
title: "Categorical Data Migration: Δ_F, Σ_F (Left Kan) & Π_F (Right Kan)"
type: SheafStalk
chapter: 7
section: "7.1.4"
pdf_pages: "481–492"
symbol: "Σ_F ⊣ Δ_F ⊣ Π_F"
layer: "Categories at Work"
extracted_declarations: 11
restricts_to: [adjoint-functors-hom-iso, pullbacks-and-fiber-products, pushouts-and-colimits-set]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Categorical Data Migration: Δ_F, Σ_F (Left Kan) & Π_F (Right Kan) (`Σ_F ⊣ Δ_F ⊣ Π_F`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.1.4` · **PDF Pages 481–492**

## 1. Epistemic Worldview & Intuition

Given a schema translation functor F : C -> D, precomposition defines the pullback data migration functor Delta_F : D-Inst -> C-Inst (sending J : D -> Set to J o F : C -> Set). Remarkably, Delta_F has BOTH a left adjoint Sigma_F (Left Kan Extension: disjoint unions + Skolem labeled nulls) and a right adjoint Pi_F (Right Kan Extension: fiber products / SQL inner joins).

## 2. Formal Categorical Core

Theorem / Proposition 7.1.4.4 (p. 483): For any functor F : C -> D, the pullback functor Delta_F : D-Set -> C-Set has a left adjoint Sigma_F : C-Set -> D-Set and a right adjoint Pi_F : C-Set -> D-Set, forming an adjoint triple Sigma_F -| Delta_F -| Pi_F. Pointwise formulas: Sigma_F(I)(d) = colim_{(F ↓ d)} I and Pi_F(I)(d) = lim_{(d ↓ F)} I.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[CInst]`** — *an instance I : C -> Set on source schema C*
- **`[DInst]`** — *an instance J : D -> Set on target schema D*
- **`[Sig]`** — *the Left Kan migrated instance Σ_F(I) (union/Skolem)*
- **`[Pi]`** — *the Right Kan migrated instance Π_F(I) (fiber join)*

### Functional Aspects (Morphisms)
- **`[DInst]` $\xrightarrow{\text{pulls back along F via Δ_F(J) = J ∘ F to}}$ `[CInst]`**
- **`[CInst]` $\xrightarrow{\text{pushes forward liberally via left adjoint Σ_F to}}$ `[Sig]`**
- **`[CInst]` $\xrightarrow{\text{pushes forward conservatively via right adjoint Π_F to}}$ `[Pi]`**

### Commutative Path Facts ($p \simeq q$)
- Adjoint Triple Law: Σ_F ⊣ Δ_F ⊣ Π_F (Proposition 7.1.4.4, p. 483).
- In our Sheaf Knowledge Base, Δ_F is the restriction map ρ_{U,V} along open inclusions, Σ_F aggregates sub-stalks into a union cover, and Π_F computes the glued global section H⁰!

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-37` (adjoint_triple_migration)** $\to$ [[adjoint-functors-hom-iso]] (*Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges*, p. 461–480): Pullback migration Δ_F sits in an adjoint triple Σ_F ⊣ Δ_F ⊣ Π_F — `Σ_F ⊣ Δ_F ⊣ Π_F`
- **`rho-38` (Pi_computes_fiber_products)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Right Kan migration Π_F computes fiber products / inner joins over comma categories (d ↓ F) — `Π_F(I)(d) = lim_{(d ↓ F)} I`
- **`rho-39` (Sigma_computes_colimit_unions)** $\to$ [[pushouts-and-colimits-set]] (*Equivalence Relations, Pushouts & Gluing in Set*, p. 110–127): Left Kan migration Σ_F computes colimits / disjoint unions with Skolem nulls over (F ↓ d) — `Σ_F(I)(d) = colim_{(F ↓ d)} I`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-04` — The Kan Data Migration Adjoint Triple Triangle** ([[data-migration-delta-sigma-pi]], [[adjoint-functors-hom-iso]], [[pullbacks-and-fiber-products]]): Right Kan migration Π_F is right adjoint to pullback Δ_F (Δ_F ⊣ Π_F) and computes universal limits/fiber products over comma categories. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 481–492)

### `Proposition 7.1.4.12` — [PDF Page 490]
> Proposition 7.1.4.12. Left adjoints are closed under composition, as are right adjoints. That is, given adjunctions, C⇄RLD⇄R′L′ℰ their composite is also an adjunction: C⇄R○R′L′○Lℰ. Proof. This is a straightforward calculation. For any objects c∈Ob(C) and e ∈ Ob(E) we have adjunction isomorphisms: Homℰ(L′(L(c)),e)≅HomD(L(c),R′(e))≅HomC(c,R(R′(e))) whose composite is the required adjunction isomorphism. It is natural in our choice of objects c and e.

### `Proposition 7.1.4` — [PDF Page 491]
> Proposition 7.1.4.12, the composite Σa ○ Δa is left adjoint to ΠaΔa. The goal is to see currying arise out of the adjunction isomorphism HomSet(ΣaΔa(B),C)≅HomSet(B,ΠaΔa(C)).(7.5) By definition, Δa(B): A → Set assigns to each element a ∈ A the set B. Since ΣA takes disjoint unions, we have a bijection Σa(Δa(B))=(∐a∈AB)≅A×B. Similarly, Δa(C): A → Set assigns to each element a ∈ A the set C. Since ΠA takes products, we have a bijection Πa(Δa(C))=(∐a∈AC)≅CA. The currying isomorphism HomSet(A × B, C) ≅ HomSet(B, CA) falls out of (7.5).

### `Slogan 7.1.4.4` — [PDF Page 482]
> Slogan 7.1.4.4. If I get my information from you, then your information becomes my information. Consider the following functor F:C→D:6 Recall how to read schemas. In schema C there are leaf tables SSN, First, Last, Salary, which represent different kinds of basic data. More interestingly, there are two fact tables. The first is called T1, and it relates SSN, First, and Last. The second is called T2, and it relates First, Last, and Salary. The functor F:C→D relates C to a schema D which has a single fact table relating all four attributes: SSN, First, Last, and Salary. We are interested

### `Example 7.1.4.7` — [PDF Page 485]
> Example 7.1.4.7. We again use the functor F:C→D from (7.4): We apply the left pushforward ΣF:C−Set→D−Set to the following instance I:C→Set:

### `Example 7.1.4.10` — [PDF Page 488]
> Example 7.1.4.10. We again use the functor F:C→D from (7.4) and Example 7.1.4.7. We apply the right pushforward ΠF to instance I:C→Set from that example.7

### `Example 7.1.4.13` (Currying via Δ, Σ, Π) — [PDF Page 490]
> Example 7.1.4.13 (Currying via Δ, Σ, Π). This example shows how currying (as in Sections 3.4.2 and 7.1.1.8) arises out of a certain combination of data migration functors. Let A, B, and C be sets. Consider the unique functor a: A → 1 and consider B and C as functors 1¯→BSet and 1¯→CSet respectively.

### `Remark 7.1.4.3` — [PDF Page 482]
> Remark 7.1.4.3. Given a functor F:C→D, which we think of as a schema translation, the functor ΔF:D−Set→C−Set goes the opposite way. The reasoning is simple to explain (we are composing functors) but something about it often seems strange at first. The rough idea of this contravariance is captured by the role-reversal in the following slogan:

### `Notation 7.1.4.1` — [PDF Page 481]
> Notation 7.1.4.1. Let C be a category. The category Fun(C,Set) of functors from C to Set, i.e., the category of instances on C, is denoted C–Set. This section discusses what happens to the resulting instances when different schemas are connected by a functor, say, F:C→D. It turns out that three adjoint functors emerge: ΔF:D−Set→C−Set, ΣF:C−Set→D−Set, and ΠF:C−Set→D−Set, where ΔF is adjoint to both of them: ΣF:C−Set⇄D−Set :ΔFΔF:D−Set⇄C−Set :ΠF. Interestingly, many of the basic database operations are captured by these three functors. For example, ΔF handles the job of duplicating or deleting tables as well as duplicating or deleting columns in

### `Exercise 7.1.4.5` — [PDF Page 484]
> Exercise 7.1.4.5. Consider the schemas and the functor F : [1] → [2] given by sending 0 ↦ 0 and 1 ↦ 2. a. How many possibilities are there for F(f)? b. Suppose I : [2] → Set is given by the following tables: Write the two tables associated to the [1]-instance ΔF(I): [1] → Set.

### `Exercise 7.1.4.8` — [PDF Page 487]
> Exercise 7.1.4.8. Consider the functor F : 3 → 2 given by the sequence (1, 2, 2). a. Write an instance I : 3 → Set. b. Given the description “ΣF performs a parameterized colimit,” make an educated guess about what ΣF(I): 2 → Set is. Give your answer in the form of two sets that are made up from the three sets you already wrote. Here is the actual formula for computing left pushforwards. Suppose that F:C→D is a functor, and let I:C→Set be a set-valued functor on C. Then ΣF(I):D→Set is defined as follows. Given an object d∈Ob(D), we first form the comma category (see Definition 6.2.4.1) for the cospan C→FD←d1¯ and denote it (F ↓ d). There is a 

### `Exercise 7.1.4.11` — [PDF Page 489]
> Exercise 7.1.4.11. Consider the functor F : 3 → 2 given by the sequence (1, 2, 2). a. Write an instance I : 3 → Set. b. Given the description “ΠF performs a parameterized limit,” make an educated guess about what ΠF(I): 2 → Set is. Give your answer in the form of two sets that are made up from the three sets you already wrote down. Here is the actual formula for computing right pushforwards. Suppose that F:C→D is a functor, and let I:C→Set be a set-valued functor on C. Then ΠF(I):D→Set is defined as follows. Given an object d∈Ob(D), we first form the comma category (see Definition 6.2.4.1) for the cospan 1¯→dD←FC and denote it (d ↓ F). There 

## 6. Page-by-Page Deep Index (PDF Pages 481–492)
- **Page 481** (`7.1 Adjoint functors`) · **Items:** Notation 7.1.4.1: 7.1.4 Data migration As we saw in Sections 5.2.2 and 5.2.2.6, a database schema is a category C, and an instance is a functor I:C→Set. Notation 7.1.4.1. Let C be a category. The category Fun(C,Set) of functors from C to Set, i.e., the category of instances on C, is denoted C–Set. This section discusses what happens to ...
- **Page 482** (`7.1 Adjoint functors`) · **Items:** Remark 7.1.4.3, Slogan 7.1.4.4: We denote the resulting functor ΔF:D−Set→C−Set and call it pullback along F . An example of this was given in Example 5.3.2.15, which showed how a monoid homomorphism F:M′→M could add functionality to a finite state machine. More generally, we can use pullbacks to reorganize data, copying and deleting tables and column...
- **Page 483** (`7.1 Adjoint functors`): in ΔF:D−Set→C−Set. Suppose given the following database instance I:D→Set on D: How does one get the instance ΔF(I):C→Set? The formula was given: compose I with F . In terms of tables, it is like duplicating table T as T1 and T2 but deleting a column from each in accordance with the definition of C in (7.4). Here is the...
- **Page 484** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.4.5: Exercise 7.1.4.5. Consider the schemas and the functor F : [1] → [2] given by sending 0 ↦ 0 and 1 ↦ 2. a. How many possibilities are there for F(f)? b. Suppose I : [2] → Set is given by the following tables: Write the two tables associated to the [1]-instance ΔF(I): [1] → Set....
- **Page 485** (`7.1 Adjoint functors`) · **Items:** Example 7.1.4.7: 7.1.4.6 Left pushforward: Σ Let F:C→D be a functor. The functor ΔF:D−Set→C−Set has a left adjoint, ΣF:C −Set→D−Set. The rough idea is that ΣF performs parameterized colimits. Given an instance I:C→Set, we get an instance on D that acts as follows. For each object d∈Ob(D), the set ΣF(I)(d) is the colimit (think of union...
- **Page 486** (`7.1 Adjoint functors`): The functor F:C→D sends both tables T1 and T2 to table T. Applying ΣF takes what was in T1 and T2 and puts the union in T. The result, ΣFI:D→Set, is as follows:...
- **Page 487** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.4.8: As one can see, no set salary information for any data comes from table T1, nor does any set SSN information come form table T2. But the definition of adjoint, given in Definition 7.1.1.1, yields the universal response: freely add new variables that take the place of missing information. It turns out that this idea alr...
- **Page 488** (`7.1 Adjoint functors`) · **Items:** Example 7.1.4.10: only briefly; see Spivak [38] for details. Given a morphism g : d → d′, there is an induced functor (F ↓ g): (F ↓ d) → (F ↓ d′) and a commutative diagram of categories: By the universal property for colimits, this induces the required function colim(F↓d) I○π→ΣF(I)(g)colim(F↓d′) I○π′. 7.1.4.9 Right pushforward: Π Let F:...
- **Page 489** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.4.11: The instance ΠF(I) puts data in all five tables in D. In T it puts pairs (t1, t2), where t1 is a row in T1, and t2 is a row in T2, for which the first and last names agree. It copies the leaf tables exactly, so they are not displayed here; the following is the table T for ΠF(I): T ID SSN First Last Salary T1-002T2-A104...
- **Page 490** (`7.1 Adjoint functors`) · **Items:** Proposition 7.1.4.12, Example 7.1.4.13: By the universal property for limits, this induces the required function lim(d↓F)I○π→ΠF(I)(g)lim(d′↓F)I○π′. Proposition 7.1.4.12. Left adjoints are closed under composition, as are right adjoints. That is, given adjunctions, C⇄RLD⇄R′L′ℰ their composite is also an adjunction: C⇄R○R′L′○Lℰ. Proof. This is a straightforwar...
- **Page 491** (`7.1 Adjoint functors`) · **Items:** Proposition 7.1.4: Note that 1–Set ≅ Set, and we elide the difference. We know that Σa is left adjoint to Δa and that Δa is left adjoint to Πa, so by Proposition 7.1.4.12, the composite Σa ○ Δa is left adjoint to ΠaΔa. The goal is to see currying arise out of the adjunction isomorphism HomSet(ΣaΔa(B),C)≅HomSet(B,ΠaΔa(C)).(7.5) By definit...
- **Page 492** (`7.1 Adjoint functors`): ...
