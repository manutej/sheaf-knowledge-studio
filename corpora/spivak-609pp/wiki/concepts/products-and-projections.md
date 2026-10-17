---
id: products-and-projections
title: "Products & Universal Pairing in Set"
type: SheafStalk
chapter: 3
section: "3.1.1"
pdf_pages: "68–79"
symbol: "X × Y"
layer: "Limits & Colimits in Set"
extracted_declarations: 15
restricts_to: [sets-and-functions]
glues_with: [pullbacks-and-fiber-products, currying-exponentials-subobjects, orders-lattices-hierarchies]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Products & Universal Pairing in Set (`X × Y`)

> **Sheaf Stalk Location:** Chapter 3 (Fundamental Considerations in Set: Limits, Colimits & Universal Constructions) · Section `3.1.1` · **PDF Pages 68–79**

## 1. Epistemic Worldview & Intuition

The Cartesian product X × Y of sets equipped with projection maps pi_1 : X × Y -> X and pi_2 : X × Y -> Y, characterized by the universal property that any pair of maps f : A -> X and g : A -> Y factors uniquely through <f, g> : A -> X × Y.

## 2. Formal Categorical Core

X × Y = {(x, y) | x in X, y in Y}. Universal Property (Prop 3.1.1.10, p. 74): For any set A and functions f : A -> X, g : A -> Y, there exists a unique function <f, g> : A -> X × Y such that pi_1 o <f, g> = f and pi_2 o <f, g> = g.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[A]`** — *a test object A*
- **`[XY]`** — *a pair (x, y) in X × Y*
- **`[X]`** — *an element x in X*
- **`[Y]`** — *an element y in Y*

### Functional Aspects (Morphisms)
- **`[A]` $\xrightarrow{\text{uniquely pairs via ⟨f, g⟩ to}}$ `[XY]`**
- **`[XY]` $\xrightarrow{\text{projects via π₁ to}}$ `[X]`**
- **`[XY]` $\xrightarrow{\text{projects via π₂ to}}$ `[Y]`**
- **`[A]` $\xrightarrow{\text{maps via f to}}$ `[X]`**
- **`[A]` $\xrightarrow{\text{maps via g to}}$ `[Y]`**

### Commutative Path Facts ($p \simeq q$)
- π₁ ∘ ⟨f, g⟩ = f and π₂ ∘ ⟨f, g⟩ = g (Proposition 3.1.1.10, p. 74).
- Hom_Set(A, X × Y) ≅ Hom_Set(A, X) × Hom_Set(A, Y).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-05` (constructs_in_Set)** $\to$ [[sets-and-functions]] (*The Category Set: Sets, Functions & Isomorphisms*, p. 26–43): Ordered pairs (x, y) and projection functions π₁, π₂ — `X × Y = {(x,y)}`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-07` (subobject_of_product)** $\leftarrow$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Pullback X ×_Z Y is the equationally constrained subset of X × Y where f(x)=g(y) — `X ×_Z Y ↪ X × Y`
- **`rho-11` (adjunction_with_product)** $\leftarrow$ [[currying-exponentials-subobjects]] (*Currying, Exponentials, Subobject Classifier & Relative Sets*, p. 128–159): Currying is right adjoint to Cartesian product (- × B) ⊣ (-)^B — `Hom(A×B, C) ≅ Hom(A, C^B)`
- **`rho-18` (poset_meet_as_product)** $\leftarrow$ [[orders-lattices-hierarchies]] (*Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces*, p. 221–244): In a preorder (P, ≤), categorical product is greatest lower bound (meet x ∧ y) — `x ×_P y = x ∧ y`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 68–79)

### `Definition 3.1.1.1` — [PDF Page 72]
> Definition 3.1.1.1. Let X and Y be sets. The product of X and Y, denoted X × Y, is defined as the set of ordered pairs (x, y), where x ∈ X and y ∈ Y. Symbolically, X×Y={ (x,y)|x∈X, y∈Y }. There are two natural projection functions, π1 : X × Y → X and π2: X × Y → Y.

### `Proposition 3.1.1.10` (Universal property for product) — [PDF Page 74]
> Proposition 3.1.1.10 (Universal property for product). Let X and Y be sets. For any set A and functions f : A → X and g : A → Y, there exists a unique function A → X × Y such that the following diagram commutes:

### `Application 3.1.1.3` — [PDF Page 73]
> Application 3.1.1.3. A traditional (Mendelian) way to predict the genotype of offspring based on the genotype of its parents is by the use of Punnett squares. If F is the set of possible genotypes for the female parent, and M is the set of possible genotypes of the male parent, then F × M is drawn as a square, called a Punnett square, in which every combination is drawn.

### `Application 3.1.1.5` — [PDF Page 73]
> Application 3.1.1.5. Suppose we are conducting experiments about the mechanical properties of materials, as in Application 2.1.2.2. For each material sample we will produce multiple data points in the set ⌜extension⌝ × ⌜force⌝ ≅ ℝ × ℝ.

### `Example 3.1.1.2` (Grid of dots) — [PDF Page 72]
> Example 3.1.1.2 (Grid of dots). Let X = {1, 2, 3, 4, 5, 6} and Y = {♣, ♢, ♡, ♠}. Then we can draw X × Y as a 6 by 4 grid of dots, and the projections as projections

### `Example 3.1.1.7` — [PDF Page 73]
> Example 3.1.1.7. Let ℝ be the set of real numbers. By ℝ2 we mean ℝ × ℝ. Similarly, for any n ∈ ℕ, we define ℝn to be the product of n copies of ℝ. According to Penrose [35], Aristotle seems to have conceived of space as something like S ≔ ℝ3 and of time as something like T ≔ ℝ. Space-time, had he conceived of it, would probably have been S × T ≅ ℝ4. He, of course, did not have access to this kind of abstraction, which was probably due to Descartes. (The product X × Y is often called Cartesian product, in his honor.)

### `Example 3.1.1.11` (Grid of dots, continued) — [PDF Page 75]
> Example 3.1.1.11 (Grid of dots, continued). It is important that the reader sees the universal property for products as completely intuitive. Recall that if X and Y are sets, say, of cardinalities |X| = m and |Y | = n respectively, then X × Y is an m × n grid of dots, and it comes with two canonical projections X←π1X×Y→π2Y. These allow us to extract from every grid element z ∈ X × Y its column π1(z) ∈ X and its row π2(z) ∈ Y. Suppose that each person in a classroom picks an element of X and an element of Y. Thus we have functions f : C → X and g : C → Y. But is not picking a column and a row the same thing as picking an element in the grid? T

### `Example 3.1.1.12` — [PDF Page 76]
> Example 3.1.1.12. Let ℝ be the set of real numbers, and let 0 ∈ ℝ be the origin. As in Notation 2.1.2.9, it is represented by a function z: {☺} → ℝ, with z(☺) = 0. Thus we can draw functions The universal property for products guarantees a function 〈z, z〉: {☺} → ℝ × ℝ, which represents the origin in (0, 0) ∈ ℝ2.

### `Example 3.1.1.15` — [PDF Page 76]
> Example 3.1.1.15. Suppose given sets X, X′, Y, Y′ and functions m: X → X′ and n: Y → Y′. We can use the universal property for products to construct a function s:

### `Example 3.1.1.17` — [PDF Page 78]
> Example 3.1.1.17. Every car owner owns at least one car, but there is no obvious function ⌜a car owner⌝ → ⌜a car⌝ because he or she may own more than one. One good choice would be the car that the person drives most often, which can be called his or her primary car. Also, given a person and a car, an economist could ask how much utility the person would get out of the car. From all this we can put together the following olog involving products: The composite map O → V tells us the utility a car owner gets out of their primary car.

### `Remark 3.1.1.6` — [PDF Page 73]
> Remark 3.1.1.6. It is possible to take the product of more than two sets as well. For example, if A, B, and C are sets, then A × B × C is the set of triples A×B×C≔{ (a,b,c)|a∈A,b∈B,c∈C }. This kind of generality is useful in understanding multiple dimensions, e.g., what physicists mean by ten-dimensional space. It comes under the heading of limits (see Section 6.1.3).

### `Exercise 3.1.1.4` — [PDF Page 73]
> Exercise 3.1.1.4. How many elements does the set {a, b, c, d} × {1, 2, 3} have?

### `Exercise 3.1.1.8` — [PDF Page 73]
> Exercise 3.1.1.8. Let ℤ denote the set of integers, and let +: ℤ × ℤ → ℤ denote the addition function and ·: ℤ × ℤ → ℤ denote the multiplication function. Which of the following diagrams commute?

### `Exercise 3.1.1.13` — [PDF Page 76]
> Exercise 3.1.1.13. For every set A there is some relationship between the following three sets: HomSet(A,X), HomSet(A,Y), and HomSet(A,X×Y). What is it? Hint: This problem is somewhat recursive in that you will use products in your formula.

### `Exercise 3.1.1.14` — [PDF Page 76]
> Exercise 3.1.1.14. a. Let X and Y be sets. Construct the swap map s: X × Y → Y × X using only the universal property for products. If π1: X × Y → X, π2: X × Y → Y, p1: Y × X → Y, and p2: Y × X → X are the projection functions, write s in terms of the symbols π1, π2, p1, p2, ○, and 〈 , 〉. b. Can you prove that s is an isomorphism using only the universal property for products?

## 6. Page-by-Page Deep Index (PDF Pages 68–79)
- **Page 68** (`2.3 Ologs`): Chapter 3 Fundamental Considerations in Set In this chapter we continue to pursue an understanding of sets. We begin by examining how to combine sets in various ways to get new sets. To that end, products and coproducts are introduced, and then more complex limits and colimits, with the aim of conveying a sense of thei...
- **Page 69** (`2.3 Ologs`): ...
- **Page 70** (`3.1 Products and coproducts`): 3.1 Products and coproducts This section introduces two concepts that are likely to be familiar, although perhaps not by their category-theoretic names: product and coproduct. Each is an example of a large class of ideas that exist far beyond the realm of sets (see Section 6.1.1)....
- **Page 71** (`3.1 Products and coproducts`): ...
- **Page 72** (`3.1 Products and coproducts`) · **Items:** Definition 3.1.1.1, Example 3.1.1.2: 3.1.1 Products Definition 3.1.1.1. Let X and Y be sets. The product of X and Y, denoted X × Y, is defined as the set of ordered pairs (x, y), where x ∈ X and y ∈ Y. Symbolically, X×Y={ (x,y)|x∈X, y∈Y }. There are two natural projection functions, π1 : X × Y → X and π2: X × Y → Y. Example 3.1.1.2 (Grid of dots). Let X =...
- **Page 73** (`3.1 Products and coproducts`) · **Items:** Application 3.1.1.3, Exercise 3.1.1.4, Application 3.1.1.5, Remark 3.1.1.6, Example 3.1.1.7, Exercise 3.1.1.8: Application 3.1.1.3. A traditional (Mendelian) way to predict the genotype of offspring based on the genotype of its parents is by the use of Punnett squares. If F is the set of possible genotypes for the female parent, and M is the set of possible genotypes of the male parent, then F × M is drawn as a square, called a...
- **Page 74** (`3.1 Products and coproducts`) · **Items:** Proposition 3.1.1.10: a. b. c. 3.1.1.9 Universal property for products A universal property is an abstract quality that characterizes a given construction. For example, the following proposition says that the product construction is characterized as possessing a certain quality. Proposition 3.1.1.10 (Universal property for product). Let X a...
- **Page 75** (`3.1 Products and coproducts`) · **Items:** Example 3.1.1.11: We say this function is induced by f and g, and we denote it 〈f,g〉:A→X×Y, where 〈f,g〉(a)=(f(a),g(a)). That is, we have π1 ○ 〈f, g〉 = f and π2 ○ 〈f, g〉 = g, and 〈f, g〉 is the only function for which that is so. Proof. Suppose given f, g as in the proposition statement. To provide a function ℓ: A → X × Y is equivalent to...
- **Page 76** (`3.1 Products and coproducts`) · **Items:** Example 3.1.1.12, Exercise 3.1.1.13, Exercise 3.1.1.14, Example 3.1.1.15: functions f and g induce a unique function C → X × Y. How does this function C → X × Y compare with the original functions f and g? The commutative diagram (3.2) sums up the connection. Example 3.1.1.12. Let ℝ be the set of real numbers, and let 0 ∈ ℝ be the origin. As in Notation 2.1.2.9, it is represented by a functi...
- **Page 77** (`3.1 Products and coproducts`): X × Y → X′ × Y′. The universal property (Proposition 3.1.1.10) says that to get a function from any set A to X′ × Y′, we need two functions, namely, some f : A → X′ and some g : A → Y′. Here we want to use A ≔ X × Y. What we have readily available are the two projections π1: X × Y → X and π2: X × Y → Y. But we also hav...
- **Page 78** (`3.1 Products and coproducts`) · **Items:** Example 3.1.1.17: Suppose that e is another object, and p: e → c and q: e → d are two arrows. By the universal property for products (Proposition 3.1.1.10), p and q induce a unique arrow e → c × d, making the evident diagrams commute. This arrow can be labeled “yields, insofar as it 〈〈p〉〉〈〈c〉〉 and 〈〈q〉〉〈〈d〉〉,”. Example 3.1.1.17. Every c...
- **Page 79** (`3.1 Products and coproducts`): ...
