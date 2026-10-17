---
id: coproducts-and-injections
title: "Coproducts & Disjoint Unions in Set"
type: SheafStalk
chapter: 3
section: "3.1.2"
pdf_pages: "80–87"
symbol: "X ⊔ Y"
layer: "Limits & Colimits in Set"
extracted_declarations: 16
restricts_to: [sets-and-functions]
glues_with: [pushouts-and-colimits-set, orders-lattices-hierarchies]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Coproducts & Disjoint Unions in Set (`X ⊔ Y`)

> **Sheaf Stalk Location:** Chapter 3 (Fundamental Considerations in Set: Limits, Colimits & Universal Constructions) · Section `3.1.2` · **PDF Pages 80–87**

## 1. Epistemic Worldview & Intuition

The dual of product: the disjoint union X ⊔ Y equipped with canonical inclusion maps i_1 : X -> X ⊔ Y and i_2 : Y -> X ⊔ Y, allowing piecewise functions on X and Y to be uniquely glued into a single function on X ⊔ Y.

## 2. Formal Categorical Core

Universal Property (Prop 3.1.2.7, p. 82): For any target set Z and functions f : X -> Z, g : Y -> Z, there exists a unique copairing function (f ⊔ g) : X ⊔ Y -> Z such that (f ⊔ g) o i_1 = f and (f ⊔ g) o i_2 = g.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *an economy-class seat in X*
- **`[Y]`** — *a first-class seat in Y*
- **`[XY]`** — *an airplane seat in X ⊔ Y*
- **`[Z]`** — *a price / state in Z*

### Functional Aspects (Morphisms)
- **`[X]` $\xrightarrow{\text{includes via i₁ into}}$ `[XY]`**
- **`[Y]` $\xrightarrow{\text{includes via i₂ into}}$ `[XY]`**
- **`[XY]` $\xrightarrow{\text{evaluates piecewise via [f, g] to}}$ `[Z]`**
- **`[X]` $\xrightarrow{\text{evaluates via f to}}$ `[Z]`**
- **`[Y]` $\xrightarrow{\text{evaluates via g to}}$ `[Z]`**

### Commutative Path Facts ($p \simeq q$)
- [f, g] ∘ i₁ = f and [f, g] ∘ i₂ = g (Proposition 3.1.2.7, p. 82).
- Application 3.1.2.10 (p. 84): Piecewise-defined curves glue on disjoint domains via coproducts (and on overlapping domains via pushouts/sheaves).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-06` (constructs_in_Set)** $\to$ [[sets-and-functions]] (*The Category Set: Sets, Functions & Isomorphisms*, p. 26–43): Disjoint unions X ⊔ Y and inclusion injections i₁, i₂ — `Hom(X⊔Y, Z) ≅ Hom(X,Z)×Hom(Y,Z)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-10` (quotient_of_coproduct)** $\leftarrow$ [[pushouts-and-colimits-set]] (*Equivalence Relations, Pushouts & Gluing in Set*, p. 110–127): Pushout X ⊔_W Y is the quotient of X ⊔ Y by the overlap relation f(w) ~ g(w) — `X ⊔ Y ↠ X ⊔_W Y`
- **`rho-19` (poset_join_as_coproduct)** $\leftarrow$ [[orders-lattices-hierarchies]] (*Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces*, p. 221–244): In a preorder (P, ≤), categorical coproduct is least upper bound (join x ∨ y) — `x ⊔_P y = x ∨ y`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 80–87)

### `Definition 3.1.2.1` — [PDF Page 80]
> Definition 3.1.2.1. Let X and Y be sets. The coproduct of X and Y, denoted X ⊔ Y, is defined as the disjoint union of X and Y, i.e., the set for which an element is either an element of X or an element of Y. If something is an element of both X and Y, then we include both copies, and distinguish between them, in X ⊔ Y. See

### `Proposition 3.1.2.7` (Universal property for coproduct) — [PDF Page 82]
> Proposition 3.1.2.7 (Universal property for coproduct). Let X and Y be sets. For any set A and functions f : X → A and g : Y → A, there exists a unique function X ⊔Y → A such that the following diagram commutes:

### `Slogan 3.1.2.8` — [PDF Page 83]
> Slogan 3.1.2.8. Any time behavior is determined by cases, there is a coproduct involved.

### `Application 3.1.2.10` (Piecewise defined curves) — [PDF Page 84]
> Application 3.1.2.10 (Piecewise defined curves). In science, curves are often defined or considered piecewise. For example, in testing the mechanical properties of a material, we might be interested in various regions of deformation, such as elastic, plastic, or post-fracture. These are three intervals on which the material displays different kinds of properties. For real numbers a b ∈ ℝ, let [a, b] ≔ {x ∈ ℝ | a x b} denote the closed interval. Given a function [a, b]→fℝ and a function [c, d]→gℝ, the universal property for coproducts implies that they extend uniquely to a function [a, b] ⊔ [c, d] → ℝ, which will appear as a piecewise defined 

### `Example 3.1.2.2` — [PDF Page 80]
> Example 3.1.2.2. There are two natural inclusion functions, i1: X → X ⊔ Y and i2: Y → X ⊔ Y.

### `Example 3.1.2.2` — [PDF Page 80]
> Example 3.1.2.2. The coproduct of X ≔ {a, b, c, d} and Y ≔ {1, 2, 3} is X⊔Y≅{ a,b,c,d,1,2,3 }. The coproduct of X and itself is X⊔X≅{ a1,b1,c1,d1,a2,b2,c2,d2 }. The names of the elements in X ⊔ Y are not so important. What is important are the inclusion maps i1, i2 from (3.3), which ensure that we know where each element of X ⊔ Y came from.

### `Example 3.1.2.3` (Airplane seats) — [PDF Page 80]
> Example 3.1.2.3 (Airplane seats).

### `Example 3.1.2.5` (Disjoint union of dots) — [PDF Page 81]
> Example 3.1.2.5 (Disjoint union of dots). Below, X and Y are sets, having six and four elements respectively, and X ⊔ Y is their coproduct, which has ten elements.

### `Example 3.1.2.11` (Airplane seats, continued) — [PDF Page 84]
> Example 3.1.2.11 (Airplane seats, continued). The universal property for coproducts says the following. Any time we have a function X → A and a function Y → A, we get a unique function X ⊔ Y → A. For example, every economy-class seat in an airplane and every first-class seat in an airplane is actually in a particular airplane. Every economy-class seat has a price, as does every first-class seat. The universal property for coproducts formalizes the following intuitively obvious fact:

### `Example 3.1.2.13` — [PDF Page 85]
> Example 3.1.2.13. In the following olog the types A and B are disjoint, so the coproduct C = A ⊔ B is just the union.

### `Example 3.1.2.14` — [PDF Page 85]
> Example 3.1.2.14. In the following olog A and B are not disjoint, so care must be taken to differentiate common elements.

### `Exercise 3.1.2.4` — [PDF Page 81]
> Exercise 3.1.2.4. Would you say that ⌜a phone⌝ is the coproduct of ⌜a cell phone⌝ and ⌜a landline phone⌝?

### `Exercise 3.1.2.9` — [PDF Page 83]
> Exercise 3.1.2.9. Let f : ℤ → ℕ be the function defined by f(n)={nif n0,−nif n<0. a. What is the standard name for f?

### `Exercise 3.1.2.12` — [PDF Page 85]
> Exercise 3.1.2.12. Write the universal property for coproduct, in terms of a relationship between the following three sets: HomSet(X,A), HomSet(Y,A), and HomSet(X⊔Y,A).

### `Exercise 3.1.2.15` — [PDF Page 86]
> Exercise 3.1.2.15. Following Section 3.1.1.16, devise a naming system for coproducts, the inclusions, and the universal maps. Try it out by making an olog (involving coproducts) that discusses the idea that both a .wav file and an .mp3 file can be played on a modern computer. Be careful that your arrows are valid (see Section 2.3.2.1).

### `Solution 3.1.2.12` — [PDF Page 85]
> Solution 3.1.2.12. HomSet(X⊔Y,A)→≅HomSet(X,A)×HomSet(Y,A). To assign an A value to each element of X ⊔ Y, you can delegate responsibility: have one person assign an A value to each element of X, and have another person assign an A value to each element of Y. One function is equivalent to two.

## 6. Page-by-Page Deep Index (PDF Pages 80–87)
- **Page 80** (`3.1 Products and coproducts`) · **Items:** Definition 3.1.2.1, Example 3.1.2.2, Example 3.1.2.2, Example 3.1.2.3: 3.1.2 Coproducts We can characterize the coproduct of two sets with its own universal property. Definition 3.1.2.1. Let X and Y be sets. The coproduct of X and Y, denoted X ⊔ Y, is defined as the disjoint union of X and Y, i.e., the set for which an element is either an element of X or an element of Y. If something is ...
- **Page 81** (`3.1 Products and coproducts`) · **Items:** Exercise 3.1.2.4, Example 3.1.2.5: Exercise 3.1.2.4. Would you say that ⌜a phone⌝ is the coproduct of ⌜a cell phone⌝ and ⌜a landline phone⌝? Example 3.1.2.5 (Disjoint union of dots). Below, X and Y are sets, having six and four elements respectively, and X ⊔ Y is their coproduct, which has ten elements....
- **Page 82** (`3.1 Products and coproducts`) · **Items:** Proposition 3.1.2.7: 3.1.2.6 Universal property for coproducts Proposition 3.1.2.7 (Universal property for coproduct). Let X and Y be sets. For any set A and functions f : X → A and g : Y → A, there exists a unique function X ⊔Y → A such that the following diagram commutes:...
- **Page 83** (`3.1 Products and coproducts`) · **Items:** Slogan 3.1.2.8, Exercise 3.1.2.9: We say this function is induced by f and g, and we denote it1 {fg:X⊔Y→A. That is, we have {fg○i1=f and {fg○i2=g , and {fg is the only function for which that is so. Proof. Suppose given f, g as in the proposition statement. To provide a function ℓ: X ⊔ Y → A is equivalent to providing an element f(m) ∈ A for each m ∈ X...
- **Page 84** (`3.1 Products and coproducts`) · **Items:** Application 3.1.2.10, Example 3.1.2.11: b. In the terminology of Proposition 3.1.2.7, what are A, X, Y, and X ⊔ Y ? Application 3.1.2.10 (Piecewise defined curves). In science, curves are often defined or considered piecewise. For example, in testing the mechanical properties of a material, we might be interested in various regions of deformation, such as el...
- **Page 85** (`3.1 Products and coproducts`) · **Items:** Exercise 3.1.2.12, Solution 3.1.2.12, Example 3.1.2.13, Example 3.1.2.14: If we know how economy-class seats are priced and we know how first- class seats are priced, and if we know that every seat is either economy class or first class, then we automatically know how all seats are priced. To say it another way (and using the other induced map), If we keep track of which airplane every econo...
- **Page 86** (`3.1 Products and coproducts`) · **Items:** Exercise 3.1.2.15: Since ducks can both swim and fly, each duck is found twice in C, once labeled “A”, a flyer, and once labeled “B”, a swimmer. The types A and B are kept disjoint in C, which justifies the name disjoint union. Exercise 3.1.2.15. Following Section 3.1.1.16, devise a naming system for coproducts, the inclusions, and the u...
- **Page 87** (`3.1 Products and coproducts`): ...
