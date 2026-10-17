---
id: adjoint-functors-hom-iso
title: "Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges"
type: SheafStalk
chapter: 7
section: "7.1.1–7.1.3"
pdf_pages: "461–480"
symbol: "Hom_D(L(c), d) ≅ Hom_C(c, R(d))"
layer: "Categories at Work"
extracted_declarations: 19
restricts_to: [currying-exponentials-subobjects, universal-limits-and-cones]
glues_with: [data-migration-delta-sigma-pi, kleisli-categories-scientific-method]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges (`Hom_D(L(c), d) ≅ Hom_C(c, R(d))`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.1.1–7.1.3` · **PDF Pages 461–480**

## 1. Epistemic Worldview & Intuition

When two categories C and D have different levels of structure (e.g., Sets vs. Monoids, Graphs vs. Categories, Preorders vs. Topological Spaces), an adjunction L : C <-> D : R provides the optimal two-way translation dictionary. Left adjoints L are 'liberal/free' and preserve colimits (LAPC); right adjoints R are 'conservative/constrained' and preserve limits (RAPL).

## 2. Formal Categorical Core

Definition 7.1.1.2 (p. 467): L : C -> D is left adjoint to R : D -> C (written L -| R) if there is a bijection alpha_{c,d} : Hom_D(L(c), d) ~= Hom_C(c, R(d)) natural in both c in C and d in D. Equivalently characterized by unit eta : id_C => R o L and counit epsilon : L o R => id_D satisfying the triangle identities. Proposition 7.1.3.1 (p. 478): Right adjoints preserve limits (RAPL); left adjoints preserve colimits (LAPC).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[HomD]`** — *a structured morphism L(c) -> d in D*
- **`[HomC]`** — *a base morphism c -> R(d) in C*
- **`[ColimC]`** — *a colimit gluing colim c_i in C*
- **`[LimD]`** — *a limit constraint lim d_j in D*

### Functional Aspects (Morphisms)
- **`[HomD]` $\xrightarrow{\text{bijects naturally via adjunction α_{c,d} with}}$ `[HomC]`**
- **`[ColimC]` $\xrightarrow{\text{is preserved by Left Adjoint L (LAPC)}}$ `[HomD]`**
- **`[LimD]` $\xrightarrow{\text{is preserved by Right Adjoint R (RAPL)}}$ `[HomC]`**

### Commutative Path Facts ($p \simeq q$)
- Naturality of α_{c,d} in both variables (Definition 7.1.1.2, p. 467).
- Every universal property (product, coproduct, limit, colimit, currying, free monoid, path category, Alexandrov space, sheafification) is an instance of adjoint functors (Section 7.1.2, p. 475).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-35` (generalizes_currying)** $\to$ [[currying-exponentials-subobjects]] (*Currying, Exponentials, Subobject Classifier & Relative Sets*, p. 128–159): Hom_D(L(c), d) ≅ Hom_C(c, R(d)) generalizes the Set currying bijection — `L ⊣ R`
- **`rho-36` (RAPL_preserves_limits)** $\to$ [[universal-limits-and-cones]] (*Universal Limits, Cones & Terminal Objects in Cat*, p. 392–428): Right adjoints preserve all limits (RAPL); left adjoints preserve all colimits (LAPC) — `R(lim D) ≅ lim R(D)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-37` (adjoint_triple_migration)** $\leftarrow$ [[data-migration-delta-sigma-pi]] (*Categorical Data Migration: Δ_F, Σ_F (Left Kan) & Π_F (Right Kan)*, p. 481–492): Pullback migration Δ_F sits in an adjoint triple Σ_F ⊣ Δ_F ⊣ Π_F — `Σ_F ⊣ Δ_F ⊣ Π_F`
- **`rho-50` (adjunction_induces_monad)** $\leftarrow$ [[kleisli-categories-scientific-method]] (*Kleisli Categories C_T & Reconciling the Scientific Method Olog*, p. 540–556): Every adjunction L ⊣ R generates a monad T = R ∘ L, and every monad factors through its Kleisli adjunction — `T = R ∘ L`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-04` — The Kan Data Migration Adjoint Triple Triangle** ([[data-migration-delta-sigma-pi]], [[adjoint-functors-hom-iso]], [[pullbacks-and-fiber-products]]): Right Kan migration Π_F is right adjoint to pullback Δ_F (Δ_F ⊣ Π_F) and computes universal limits/fiber products over comma categories. *[H^0 Exact (Zero Obstruction)]*
- **`tau-08` — The Adjunction-Monad-Kleisli Triangle** ([[kleisli-categories-scientific-method]], [[monads-and-contextual-computation]], [[adjoint-functors-hom-iso]]): Every adjunction L ⊣ R generates a monad (T = R∘L, η, μ = RεL), and the Kleisli category C_T is the initial adjunction realizing T. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 461–480)

### `Definition 7.1.1.1` — [PDF Page 466]
> Definition 7.1.1.1. Let B and A be categories.1 An adjunction between B and A is a pair of functors L:B→AandR:A→B together with a natural isomorphism2 whose component for any objects A∈Ob(A) and B∈Ob(B)) is αB,A:HOMA(L(B),A)→≅HOMB(B,R(A)).(7.1) This isomorphism is called the adjunction isomorphism for the (L, R) adjunction, and for any morphism f : L(B) → A in A, we refer to αB,A(f): B → R(A) as the adjunct of f.3 The functor L is called the left adjoint and the functor R is called the right adjoint. We may say that L is the left adjoint of R or that R is the right adjoint of L.4 We often denote this setup L:B⇄A:R(7.2)

### `Proposition 7.1.1.2` — [PDF Page 466]
> Proposition 7.1.1.2. Let L: Set → Mon be the functor sending X ∈ Ob(Set) to the free monoid L(X) ≔ (List(X), [ ], ++), as in Definition 4.1.1.15. Let R: Mon → Set be the functor sending each monoid M ≔ (M, e, ⋆) to its underlying set R(M) ≔ M. Then L is left adjoint to R. Proof. This is precisely the content of Proposition 4.1.4.9.

### `Proposition 7.1.1.11` — [PDF Page 470]
> Proposition 7.1.1.11. Let C and D be categories, let F:C→D be a functor, and let G,G′:D→C also be functors. If both G and G′ are right adjoint (resp. if both are left adjoint) to F, then there is a natural isomorphism ϕ:G→≅G′. Proof. Suppose that both G and G′ are right adjoint to F (the case of G and G′ being left adjoint is similarly proved). We first give a formula for the components of ϕ: G → G′ and its inverse ψ : G′ → G. Given an object d∈Ob(D), we use c = G(d) to obtain two natural isomorphisms, one from each adjunction: HomC(G(d),G(d))≅HomD(F(G(d)),d)≅HomC(G(d),G′(d)). The identity morphism idG(d) is then sent to some morphism G(d) → 

### `Proposition 7.1.3.1` — [PDF Page 478]
> Proposition 7.1.3.1. Let L:B⇄A :R be an adjunction. For any indexing category I and functor D : I → B, if D has a colimit in B, then there is a unique isomorphism L(colim D)≅colim(L○D). Similarly, for any I ∈ Ob(Cat) and functor D:I→A, if D has a limit in A, then there is a unique isomorphism R(limD)≅lim(R○D). Proof. The proof is simple if one knows the Yoneda lemma (Section 7.2.1.14). See Mac Lane [29] for details.

### `Example 7.1.1.3` — [PDF Page 466]
> Example 7.1.1.3. We need to ground the discussion in some concrete mathematics. In Proposition 7.1.1.2 we provided an adjunction between sets and monoids. A set X gets transformed into a monoid by considering lists in X; a monoid M gets transformed into a set by forgetting the multiplication law. So we have a functor for translating each way,

### `Example 7.1.1.5` — [PDF Page 468]
> Example 7.1.1.5. Let L: Set → Mon and R: Mon → Set be the free and forgetful functors from Proposition 7.1.1.2. We know that L is left adjoint to R; however L is not right adjoint to R. In other words, we can show that the necessary natural isomorphism cannot exist. Let X = {a, b}, and let M = 1 be the trivial monoid. Then the necessary natural isomorphism would need to give a bijection HomMon(M,L(X))≅?HomSet({1},X). But the left-hand side has one element, because M is the initial object in Mon (see Example 6.1.3.7), whereas the right-hand side has two elements. Therefore, no isomorphism can exist.

### `Example 7.1.1.6` — [PDF Page 468]
> Example 7.1.1.6. Preorders have underlying sets, giving rise to a functor U : PrO → Set. The functor U has both a left adjoint and a right adjoint. The left adjoint of U is D : Set → PrO, sending a set X to the discrete preorder on X (the preorder with underlying set X, having the fewest possible ’s). The right adjoint of U is I : Set → PrO, sending a set X to the indiscrete preorder on X (the preorder with underlying set X, having the most possible ’s). See Example 4.4.4.5.

### `Example 7.1.1.8` — [PDF Page 469]
> Example 7.1.1.8. Here are some other adjunctions: Ob: Cat → Set has a left adjoint Disc: Set → Cat given by the discrete category. Ob: Cat → Set has a right adjoint Ind: Set → Cat given by the indiscrete category. The underlying graph functor Cat → Grph has a left adjoint Grph → Cat given by the free category. The inclusion Grp → Mon has a right adjoint Mon→CoreGrp, called the core, that sends a monoid to its subgroup of invertible elements. The functor PrO → Grph, given by drawing edges for ’s, has a left adjoint given by existence of paths. The forgetful functor from partial orders to preorders has a left adjoint given by quotienting out th

### `Example 7.1.1.13` — [PDF Page 471]
> Example 7.1.1.13. In logic or computer science the quantifiers ∃ and ∀ are used to ask whether any or all elements of a set have a certain property. For example,

### `Example 7.1.2.1` — [PDF Page 475]
> Example 7.1.2.1. Let C be a category and t:C→1¯ the unique functor to the terminal category. Then t has a right adjoint if and only if C has a terminal object, and t has a left adjoint if and only if C has an initial object. The proofs are dual, so let’s focus on the first. The functor t has a right adjoint R:1¯→C if and only if for every object c∈Ob(C) there is an isomorphism HomC(c,r)≅Hom1¯(t(c),1), where r = R(1). But Hom1(t(c), 1) has one element. Thus t has a right adjoint iff HomC(c,r) has one element for each c∈Ob(C). This is the definition of r being a terminal object. When colimits and limits were defined in Definitions 6.1.3.31 and 

### `Example 7.1.2.2` — [PDF Page 476]
> Example 7.1.2.2. Let C=Set, and let I = 3. The category Fun(3, Set) is the category of {1, 2, 3}-indexed sets, e.g., (ℤ, ℕ, ℤ) ∈ Ob(Fun(3, Set)) is an object of it. We will obtain the limit, i.e., the product of these three sets 3 → Set using adjoints. In fact, the limit will be right adjoint to a functor Δt: Set → Fun(3, Set), defined as follows. Given a set c ∈ Ob(Set), represented by a functor c: 1 → Set, and define Δt(c) to be the composite c ○ t: 3 → Set; it is the constant functor. That is, Δt(c): 3 → Set is the {1, 2, 3}-indexed set (c, c, c). To say that Δt has a right adjoint called Πt : Fun(3, Set) → Set and that Πt takes limits sho

### `Example 7.1.3.2` — [PDF Page 478]
> Example 7.1.3.2. Since Ob: Cat → Set is both a left adjoint and a right adjoint, it must preserve both limits and colimits. This means that if one wants to know the set of objects in the fiber product of some categories, one can simply take the fiber product of the set of objects in those categories, Ob(A×CB)≅Ob(A)×Ob(C)Ob(B). While the right-hand side might look daunting, it is just a fiber product in Set, which is quite understandable (see Definition 3.2.1.1). This is greatly simplifying. If one thinks through what defines a limit in Cat, one encounters notions of slice categories and terminal objects in them. These slice categories are in 

### `Example 7.1.3.3` — [PDF Page 478]
> Example 7.1.3.3. The path preorder functor L: Grph → PrO given by existence of paths (see Exercise 5.1.2.13) is left adjoint to the functor R: PrO → Grph given by replacing ’s by arrows. This means that L preserves colimits. So taking the union of graphs G and H results in a graph whose path poset L(G ⊔ H) is the union of the path posets of G and H. But this is not so for products, i.e., we do not expect to have an isomorphism L(G × H) ≅? L(G) × L(H).

### `Exercise 7.1.1.4` — [PDF Page 467]
> Exercise 7.1.1.4. Let X = {a, b, c}, and let M = (ℕ, 1, *) be the multiplicative monoid of natural numbers (see Example 4.1.3.2). Let g : X → ℕ be the function given by g(a) = 7, g(b) = 2, g(c) = 2, and let βX,M : HomSet(X, R(M)) → HomMon(L(X), M) be as in the proof of Proposition 4.1.4.9. Consider the list [b, b, a, c] ∈ L(X). What is βX,M(g)([b, b, a, c])? Let us look once more at the adjunction between adults and babies. Using the notation of Definition 7.1.1.1, A is the adult category of meaningful words, and B is the baby category of repeated noises. The left adjoint turns every repeated sound into a meaningful word (having free meaning)

### `Exercise 7.1.1.7` — [PDF Page 468]
> Exercise 7.1.1.7. Let U : Grph → Set denote the functor sending a graph to its underlying set

### `Exercise 7.1.1.9` — [PDF Page 469]
> Exercise 7.1.1.9. Let 1 denote the terminal category. There is a unique functor !: Set → 1. a. Does ! have a left adjoint? If so, what is it; if not, why not? b. Does ! have a right adjoint? If so, what is it; if not, why not?

### `Exercise 7.1.1.10` — [PDF Page 469]
> Exercise 7.1.1.10. The discrete category functor Disc: Set → Cat has a left adjoint p: Cat → Set. In this exercise you will work out how to unpack this idea and begin to deduce how p must behave. a. For an arbitrary object X ∈ Ob(Set) and an arbitrary object C∈Ob(Cat), write the adjunction in the style of (7.2), appropriately filling in all the variables (e.g., decide whether B = Cat or B = Set, etc.).

### `Exercise 7.1.1.14` — [PDF Page 472]
> Exercise 7.1.1.14. The national scout jamboree is a gathering of Boy Scouts from troops across the United States. Let S be the set of Boy Scouts in the U.S., and let T be the set of Boy Scout troops in the U.S. Let t: S → T be the function that assigns to each Boy Scout his troop. Let U ⊆ S be the set of Boy Scouts in attendance at this year’s jamboree. a. What is the meaning of the object ∃tU b. What is the meaning of the object ∀tU?

## 6. Page-by-Page Deep Index (PDF Pages 461–480)
- **Page 461** (`6.2 Other notions in Cat`): Chapter 7 Categories at Work The reader should now have an understanding of the basic notions of category theory: categories, functors, natural transformations, and universal properties. As well, we have discussed many sources of examples: orders, graphs, monoids, and databases. This chapter begins with the notion of a...
- **Page 462** (`6.2 Other notions in Cat`): ...
- **Page 463** (`7.1 Adjoint functors`): 7.1 Adjoint functors How far can we take this dictionary analogy? In the common understanding of dictionaries, we assume that two languages (say, French and English) are equally expressive and that a good dictionary will assist in an even exchange of ideas. But in category theory we often have two categories that are n...
- **Page 464** (`7.1 Adjoint functors`): ...
- **Page 465** (`7.1 Adjoint functors`): 7.1.1 Discussion and definition Consider the category of monoids and the category of sets. A monoid (M, e, ⋆) is a set with a unit element and a multiplication formula that is associative. A set is just a set. A dictionary between Mon and Set should not be required to set up an even exchange but rather an exchange that...
- **Page 466** (`7.1 Adjoint functors`) · **Items:** Definition 7.1.1.1, Proposition 7.1.1.2, Example 7.1.1.3: in how they interact, so we put them in different categories. Applying free functor L: Set → Mon to a set X makes every element x ∈ X a word, and these words can be strung together to form more complex words. (Section 4.1.1.12 discussed the free monoid functor L.) Since a set such as X carries no information about the ...
- **Page 467** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.1.4: L:Set→Mon, R:Mon→Set, but an adjunction is more than that: it includes a guarantee about the relationship between these two functors. What is the relationship between L and R? Consider an arbitrary monoid M = (M, e, ⋆). If we want to pick out three elements of the set M, that is the same thing as giving a function {a, ...
- **Page 468** (`7.1 Adjoint functors`) · **Items:** Example 7.1.1.5, Example 7.1.1.6, Exercise 7.1.1.7: these are mappings in the adult category A of the form L(B) → A. And (stretching it) the baby tries to find a mapping (which we might see as emulation) from her set B of repeatable sounds to the set R(A) of the sounds the adult seems to repeat. If there were a global system for making these transformations, that would ...
- **Page 469** (`7.1 Adjoint functors`) · **Items:** Example 7.1.1.8, Exercise 7.1.1.9, Exercise 7.1.1.10: of vertices. This functor has both a left and a right adjoint. a. What functor Set → Grph is the left adjoint of U? b. What functor Set → Grph is the right adjoint of U? Example 7.1.1.8. Here are some other adjunctions: Ob: Cat → Set has a left adjoint Disc: Set → Cat given by the discrete category. Ob: Cat → Set has a...
- **Page 470** (`7.1 Adjoint functors`) · **Items:** Proposition 7.1.1.11: b. For X and C as in part (a), write the adjunction isomorphism in the style of (7.1), appropriately filling in all the variables. c. Let C be the free category on the graph G and let X = {1, 2, 3}. How many elements does the set HomCat(C,Disc(X)) have? d. What can you do to an arbitrary category C∈Ob(Cat) to make a se...
- **Page 471** (`7.1 Adjoint functors`) · **Items:** Example 7.1.1.13: HomC(G′(d),G′(d))≅HomD(F(G′(d)),d)≅HomC(G′(d),G(d)). Again, the identity element idG′(d) is sent to some morphism G′(d) → G(d), which we take to be the d-component ψd. The naturality of the adjunction isomorphisms implies that ϕ and ψ are natural transformations, and it is straightforward to check that they are mutuall...
- **Page 472** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.1.14: one may have a set U of natural numbers and want to know whether any or all are even or odd. Let Y = {even, odd}, and let p:ℕ→Y be the function that assigns to each natural number its parity (even or odd). Because the elements of ℙ(ℕ) and ℙ(Y) are ordered by inclusion of subsets, we can construe these orders as categor...
- **Page 473** (`7.1 Adjoint functors`) · **Items:** Exercise 7.1.1.15: Exercise 7.1.1.15. Let X be an arbitrary set and U ⊆ X a subset. a. Find a set Y and a function f : X → Y such that ∃fU tells you whether U is nonempty. b. What is the meaning of ∀fU for your choice of Y and f? In fact, the idea of quantifiers as adjoints is part of a larger story. Suppose we think of elements of a set...
- **Page 474** (`7.1 Adjoint functors`): ...
- **Page 475** (`7.1 Adjoint functors`) · **Items:** Example 7.1.2.1: 7.1.2 Universal concepts in terms of adjoints This section explores how universal concepts, i.e., initial objects and terminal objects, colimits and limits, are easily phrased in the language of adjoint functors. We say that a functor F:C→D is a left adjoint or has a right adjoint if there exists a functor G:D→C such t...
- **Page 476** (`7.1 Adjoint functors`) · **Items:** Example 7.1.2.2: Example 7.1.2.2. Let C=Set, and let I = 3. The category Fun(3, Set) is the category of {1, 2, 3}-indexed sets, e.g., (ℤ, ℕ, ℤ) ∈ Ob(Fun(3, Set)) is an object of it. We will obtain the limit, i.e., the product of these three sets 3 → Set using adjoints. In fact, the limit will be right adjoint to a functor Δt: Set → Fun...
- **Page 477** (`7.1 Adjoint functors`): ...
- **Page 478** (`7.1 Adjoint functors`) · **Items:** Proposition 7.1.3.1, Example 7.1.3.2, Example 7.1.3.3: 7.1.3 Preservation of colimits or limits One useful fact about adjunctions is that left adjoints preserve all colimits, and right adjoints preserve all limits. Proposition 7.1.3.1. Let L:B⇄A :R be an adjunction. For any indexing category I and functor D : I → B, if D has a colimit in B, then there is a unique isomorphi...
- **Page 479** (`7.1 Adjoint functors`): As an example, let . Then L(G) = L(H) = [1], the linear order of length 1. But the product G × H in Grph looks like the graph Its preorder L(G × H) does not have (a, a) (a, b), whereas this is the case in the preorder L(G) × L(H). So L(G × H) ≇ L(G) × L(H). The left adjoint preservers all colimits, but not necessarily ...
- **Page 480** (`7.1 Adjoint functors`): ...
