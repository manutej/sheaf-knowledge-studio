---
id: pullbacks-and-fiber-products
title: "Pullbacks (Fiber Products) & Constraint Solving"
type: SheafStalk
chapter: 3
section: "3.2.1"
pdf_pages: "88–101"
symbol: "X ×_Z Y"
layer: "Limits & Colimits in Set"
extracted_declarations: 21
restricts_to: [products-and-projections, commutative-diagrams]
glues_with: [spans-experiments-matrices, currying-exponentials-subobjects, graphs-and-paths, universal-limits-and-cones, data-migration-delta-sigma-pi, sheaves-and-local-to-global-gluing]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Pullbacks (Fiber Products) & Constraint Solving (`X ×_Z Y`)

> **Sheaf Stalk Location:** Chapter 3 (Fundamental Considerations in Set: Limits, Colimits & Universal Constructions) · Section `3.2.1` · **PDF Pages 88–101**

## 1. Epistemic Worldview & Intuition

Given a cospan X --f--> Z <--g-- Y, the pullback (fiber product) X ×_Z Y consists of all compatible pairs (x, y) that map to the same element f(x) = g(y) in the overlap target Z. In databases, pullbacks are inner joins; in sheaf theory, pullbacks test overlap compatibility and perform fiber-product prediction.

## 2. Formal Categorical Core

X ×_Z Y = {(x, y) in X × Y | f(x) = g(y)}. Universal Property (Prop 3.2.1.15, p. 96): Any cone A -> X, A -> Y making the outer square commute over Z factors uniquely through A -> X ×_Z Y.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[P]`** — *a compatible pair (x, y) in X ×_Z Y*
- **`[X]`** — *an element x in X*
- **`[Y]`** — *an element y in Y*
- **`[Z]`** — *a shared attribute z in Z*

### Functional Aspects (Morphisms)
- **`[P]` $\xrightarrow{\text{projects left via p₁ to}}$ `[X]`**
- **`[P]` $\xrightarrow{\text{projects right via p₂ to}}$ `[Y]`**
- **`[X]` $\xrightarrow{\text{maps via f to}}$ `[Z]`**
- **`[Y]` $\xrightarrow{\text{maps via g to}}$ `[Z]`**

### Commutative Path Facts ($p \simeq q$)
- Commutative Pullback Square: f ∘ p₁ = g ∘ p₂ (Definition 3.2.1.1, p. 90).
- Pasting Lemma for Pullbacks (Prop 3.2.1.17, p. 98): Two adjacent pullback squares paste to form a composite pullback rectangle.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-07` (subobject_of_product)** $\to$ [[products-and-projections]] (*Products & Universal Pairing in Set*, p. 68–79): Pullback X ×_Z Y is the equationally constrained subset of X × Y where f(x)=g(y) — `X ×_Z Y ↪ X × Y`
- **`rho-08` (universal_commuting_square)** $\to$ [[commutative-diagrams]] (*Commutative Diagrams & Path Equations*, p. 44–46): Pullback square f ∘ p₁ = g ∘ p₂ is terminal among commuting squares over f, g — `f ∘ p₁ = g ∘ p₂`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-09` (composes_via_pullback)** $\leftarrow$ [[spans-experiments-matrices]] (*Spans, Scientific Experiments, Equalizers & Finite Limits*, p. 102–109): Spans X <- R -> Y <- S -> Z compose by taking the pullback R ×_Y S — `R ∘_Span S = R ×_Y S`
- **`rho-12` (classifies_subsets_via_pullback)** $\leftarrow$ [[currying-exponentials-subobjects]] (*Currying, Exponentials, Subobject Classifier & Relative Sets*, p. 128–159): Every subset U ⊆ X is the pullback of true : 1 -> Ω along χ_U — `U ≅ X ×_Ω {true}`
- **`rho-16` (iterated_fiber_product_paths)** $\leftarrow$ [[graphs-and-paths]] (*Graphs, Path Categories & Homomorphisms*, p. 201–220): Length-n paths Path_n(G) are the iterated pullback A ×_V A ×_V … ×_V A — `Path_2(G) = A ×_{tgt,V,src} A`
- **`rho-31` (generalizes_Set_limits)** $\leftarrow$ [[universal-limits-and-cones]] (*Universal Limits, Cones & Terminal Objects in Cat*, p. 392–428): Cones and universal limits in Cat generalize products, pullbacks, and equalizers in Set — `lim_J D |_Set = {compatible tuples}`
- **`rho-38` (Pi_computes_fiber_products)** $\leftarrow$ [[data-migration-delta-sigma-pi]] (*Categorical Data Migration: Δ_F, Σ_F (Left Kan) & Π_F (Right Kan)*, p. 481–492): Right Kan migration Π_F computes fiber products / inner joins over comma categories (d ↓ F) — `Π_F(I)(d) = lim_{(d ↓ F)} I`
- **`rho-44` (gluing_and_prediction_via_pullback)** $\leftarrow$ [[sheaves-and-local-to-global-gluing]] (*Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom*, p. 518–522): Binary sheaf gluing O(U∪V) ≅ O(U) ×_{O(U∩V)} O(V) and sheaf prediction are fiber products — `O(U∪V) ≅ O(U) ×_{O(U∩V)} O(V)`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-02` — The Sheaf-Presheaf-Pullback Equalizer Triangle** ([[sheaves-and-local-to-global-gluing]], [[presheaves-representables-yoneda]], [[pullbacks-and-fiber-products]]): Restricting a sheaf O : Open(X)^op -> Set to a binary cover {U, V} exhibits O(U ∪ V) as the fiber product O(U) ×_{O(U ∩ V)} O(V). *[H^0 Exact (Zero Obstruction)]*
- **`tau-04` — The Kan Data Migration Adjoint Triple Triangle** ([[data-migration-delta-sigma-pi]], [[adjoint-functors-hom-iso]], [[pullbacks-and-fiber-products]]): Right Kan migration Π_F is right adjoint to pullback Δ_F (Δ_F ⊣ Π_F) and computes universal limits/fiber products over comma categories. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 88–101)

### `Definition 3.2.1.1` (Pullback) — [PDF Page 90]
> Definition 3.2.1.1 (Pullback). Suppose given the following diagram of sets and functions: Its fiber product is the set X×ZY≔{ (x,z,y)|f(x)=z=g(y) }. There are obvious projections π1: X ×Z Y → X and π2 : X ×Z Y → Y (e.g., π2(x, z, y) = y). The following diagram commutes: Given the setup of diagram (3.8), we define a pullback of X and Y over Z to be any set W for which we have an isomorphism W→≅X×ZY. The corner symbol ⌟ in diagram (3.9) indicates that X ×Z Y is a pullback.

### `Definition 3.2.1.12` (Preimage) — [PDF Page 95]
> Definition 3.2.1.12 (Preimage). Let f : X → Y be a function and y ∈ Y an element. The preimage of y under f, denoted f−1(y), is the subset f−1(y) ≔ {x ∈ X | f(x) = y}. If Y′ ⊆ Y is any subset, the preimage of Y′ under f, denoted f−1(Y′), is the subset f−1(Y′) = {x ∈ X | f(x) ∈ Y′}.

### `Proposition 3.2.1.15` (Universal property for pullback) — [PDF Page 96]
> Proposition 3.2.1.15 (Universal property for pullback). Suppose given the diagram of sets and functions as below: For any set A and the following commutative solid-arrow diagram (i.e., functions f : A → X and g : A → Y such that t ○ f = u ○ g), there is a unique function A → X ×Z Y such that the diagram commutes:

### `Proposition 3.2.1.18` — [PDF Page 98]
> Proposition 3.2.1.18. Consider the diagram: where B′ ≅ B ×C C′ is a pullback. Then there is an isomorphism A ×B B′ ≅ A ×C C′. In other words, there is an isomorphism A×B(B×CC′)≅A×CC′. Proof. We first provide a map ϕ: A×B(B×CC′) → A×CC′. An element of A×B(B×CC ′) is of the form (a, b, (b, c, c′)) such that f(a) = b, g(b) = c and k(c′) = c. But this implies that g ○ f(a) = c = k(c′) so we put ϕ(a, b, (b, c, c′)) ≔ (a, c, c′) ∈ A ×C C′. Now we provide a proposed inverse, ψ : A ×C C′ → A ×B (B ×C C′). Given (a, c, c′) with g ○ f(a) = c = k(c′), let b = f(a) and note that (b, c, c′) is an element of B ×C C′. So we can define ψ(a, c, c′) = (a, b, (

### `Proposition 3.2.1` — [PDF Page 98]
> Proposition 3.2.1.18 can be useful in authoring ologs. For example, the type ⌜a cell phone that has a bad battery⌝ is vague, but we can lay out precisely what it means using pullbacks:

### `Example 3.2.1.8` — [PDF Page 93]
> Example 3.2.1.8. Consider the following two ologs. The one on the right is the pullback of the one on the left.

### `Remark 3.2.1.4` — [PDF Page 92]
> Remark 3.2.1.4. Some may prefer to denote the fiber product in (3.8) by f × Z g rather than X ×Z Y. The former is mathematically better notation, but human- readability is often enhanced by the latter, which is also more common in the literature. We use whichever is more convenient.

### `Remark 3.2.1.9` — [PDF Page 94]
> Remark 3.2.1.9. Note that in diagram (3.11) the upper left box in the pullback could have been (noncanonically named) ⌜a good customer⌝. If it were taken to be the fiber product, then the author would be effectively defining a good customer to be one that is wealthy and loyal.

### `Exercise 3.2.1.2` — [PDF Page 90]
> Exercise 3.2.1.2. Let X, Y, Z be as drawn and f : X → Z and g : Y → Z the indicated functions.

### `Exercise 3.2.1.3` — [PDF Page 91]
> Exercise 3.2.1.3. a. Draw a set X with five elements and a set Y with three elements. Color each element of X and each element of Y red, blue, or green,2 and do so in a random-looking way. Considering your coloring of X as a function X → C, where C = {red, blue, green}, and similarly obtaining a function Y → C, draw the fiber product X ×C Y. b. The universal property for products guarantees a function X ×C Y → X × Y, which will be an injection. This means that the drawing you made of the fiber product can be embedded into the 5 × 3 grid. Draw the grid and indicate this subset.

### `Exercise 3.2.1.5` — [PDF Page 92]
> Exercise 3.2.1.5. Let f : X → Z and g : Y → Z be functions. a. Suppose that Y = ∅; what can you say about X ×Z Y? b. Suppose now that Y is any set but that Z has exactly one element; what can you say about X ×Z Y?

### `Exercise 3.2.1.6` — [PDF Page 92]
> Exercise 3.2.1.6.

### `Exercise 3.2.1.10` — [PDF Page 94]
> Exercise 3.2.1.10. For each of the following, an author has proposed that the right-hand diagram is a pullback. Do you think their labels are appropriate or misleading; that is, is the label in the upper left box of the pullback reasonable given the rest of the olog, or is it suspect in some way? a. b.

### `Exercise 3.2.1.11` — [PDF Page 95]
> Exercise 3.2.1.11. Consider your olog from Exercise 2.3.3.1. Are any of the commutative squares in it actually pullback squares?

### `Exercise 3.2.1.13` — [PDF Page 95]
> Exercise 3.2.1.13. Let f : X → Y be a function and y ∈ Y an element. Draw a pullback diagram in which the fiber product is isomorphic to the preimage f−1(y).

### `Exercise 3.2.1.14` — [PDF Page 95]
> Exercise 3.2.1.14. Consider the function f : ℕ → ℕ, where f(n) = n + 3. Let A = {i ∈ ℕ | i 7}, and let g : A → ℕ be the inclusion, e.g., g(17) = 17. What is the pullback of the

### `Exercise 3.2.1.16` — [PDF Page 97]
> Exercise 3.2.1.16. a. Create an olog whose underlying shape is a commutative square. Now add the fiber product so that the shape is the same as that of diagram (3.12). b. Use your result to devise English labels to the object X ×Z Y, to the projections π1, π2, and to the dotted map A→〈f,g〉ZX×ZY, such that these labels are as canonical as possible. 3.2.1.17 Pasting diagrams for pullback Consider the following diagram, which includes a left-hand square, a right-hand square, and a big rectangle:

### `Exercise 3.2.1.19` — [PDF Page 99]
> Exercise 3.2.1.19. a. Create an olog that defines two people to be “of approximately the same height” if and only if their height difference is less than half an inch, using a pullback. Your olog can include the box ⌜a real number x such that −.5 < x < .5⌝. b. In the same olog, use pullbacks to make a box for those people whose height is approximately the same as a person named “Mary Quite Contrary.”

## 6. Page-by-Page Deep Index (PDF Pages 88–101)
- **Page 88** (`3.2 Finite limits in Set`): 3.2 Finite limits in Set This section discusses limits of variously shaped diagrams of sets. This is made more precise in Section 6.1.3, which discusses arbitrary limits in arbitrary categories....
- **Page 89** (`3.2 Finite limits in Set`): ...
- **Page 90** (`3.2 Finite limits in Set`) · **Items:** Definition 3.2.1.1, Exercise 3.2.1.2: 3.2.1 Pullbacks Definition 3.2.1.1 (Pullback). Suppose given the following diagram of sets and functions: Its fiber product is the set X×ZY≔{ (x,z,y)|f(x)=z=g(y) }. There are obvious projections π1: X ×Z Y → X and π2 : X ×Z Y → Y (e.g., π2(x, z, y) = y). The following diagram commutes: Given the setup of diagram (3.8),...
- **Page 91** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.1.3, Solution 3.2.1.3: What is the fiber product of the diagram X→fZ←gY? Exercise 3.2.1.3. a. Draw a set X with five elements and a set Y with three elements. Color each element of X and each element of Y red, blue, or green,2 and do so in a random-looking way. Considering your coloring of X as a function X → C, where C = {red, blue, green},...
- **Page 92** (`3.2 Finite limits in Set`) · **Items:** Remark 3.2.1.4, Exercise 3.2.1.5, Exercise 3.2.1.6: Note that inside the set of X × Y = 15 possible (x, y) pairs is the set of pairs that agree on color—this is X ×C Y. The grid X × Y is not drawn, but it includes the drawn dots, X ×C Y ⊆ X × Y, as well as eight nondrawn dots such as (3, a), which “couldn’t agree on a color.” Remark 3.2.1.4. Some may prefer to denote th...
- **Page 93** (`3.2 Finite limits in Set`) · **Items:** Example 3.2.1.8: Let S = ℝ3, T = ℝ, and think of them as (Aristotelian) space and time, with the origin in S × T given by the center of mass of MIT at the time of its founding. Let Y = S × T, and let g1 : Y → S be one projection and g2 : Y → T the other projection. Let X = {☺} be a set with one element, and let f1 : X → S and f2 : X → ...
- **Page 94** (`3.2 Finite limits in Set`) · **Items:** Remark 3.2.1.9, Exercise 3.2.1.10: Check from Definition 3.2.1.1 that the label “a customer that is wealthy and loyal” is fair and straightforward as a label for the fiber product A = B ×D C, given the labels on B, C, and D. Remark 3.2.1.9. Note that in diagram (3.11) the upper left box in the pullback could have been (noncanonically named) ⌜a good cust...
- **Page 95** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.1.11, Definition 3.2.1.12, Exercise 3.2.1.13, Exercise 3.2.1.14: c. Exercise 3.2.1.11. Consider your olog from Exercise 2.3.3.1. Are any of the commutative squares in it actually pullback squares? Definition 3.2.1.12 (Preimage). Let f : X → Y be a function and y ∈ Y an element. The preimage of y under f, denoted f−1(y), is the subset f−1(y) ≔ {x ∈ X | f(x) = y}. If Y′ ⊆ Y is any sub...
- **Page 96** (`3.2 Finite limits in Set`) · **Items:** Proposition 3.2.1.15: following diagram? Proposition 3.2.1.15 (Universal property for pullback). Suppose given the diagram of sets and functions as below: For any set A and the following commutative solid-arrow diagram (i.e., functions f : A → X and g : A → Y such that t ○ f = u ○ g), there is a unique function A → X ×Z Y such that the diag...
- **Page 97** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.1.16: Exercise 3.2.1.16. a. Create an olog whose underlying shape is a commutative square. Now add the fiber product so that the shape is the same as that of diagram (3.12). b. Use your result to devise English labels to the object X ×Z Y, to the projections π1, π2, and to the dotted map A→〈f,g〉ZX×ZY, such that these labels ...
- **Page 98** (`3.2 Finite limits in Set`) · **Items:** Proposition 3.2.1.18, Proposition 3.2.1: The right-hand square has a corner symbol indicating that B′ ≅ B ×C C′ is a pullback. But the corner symbol in the leftmost corner is ambiguous; it might be indicating that the left-hand square is a pullback, or it might be indicating that the big rectangle is a pullback. It turns out not to be ambiguous because the le...
- **Page 99** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.1.19, Exercise 3.2.1.20: The category-theoretic fact described here says that since A ≅ B ×D C and C ≅ D ×F E, it follows that A ≅ B ×F E. That is, we can deduce the definition “a cell phone that has a bad battery is defined as a cell phone that has a battery which remains charged for less than one hour.” Exercise 3.2.1.19. a. Create an olog t...
- **Page 100** (`3.2 Finite limits in Set`) · **Items:** Solution 3.2.1.20: such that all squares commute. Solution 3.2.1.20. We redraw the right-hand diagram, with arrows labeled and a new dotted arrow: The commutativity of the right, back, and bottom squares can be written equationally as c′∘g∘a=f∘c∘a=f∘d∘b=d′∘e∘b. Therefore, the universal property for pullbacks (3.2.1.15) allows us to form ...
- **Page 101** (`3.2 Finite limits in Set`): ...
