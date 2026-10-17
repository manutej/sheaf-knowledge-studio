# Birkhoff's Representation Theorem & Power-Set Lattices (`U_11`)

- **Chapter:** 4 (`§4.2`)
- **Page Fiber:** `pp. 148–152`
- **Layer:** Order & Hierarchy

## Summary

Every finite distributive lattice (such as divisibility of square-free integers or color mixing) is order-isomorphic to a lattice of sets ordered by subset inclusion ⊆ (Birkhoff's Representation Theorem).

## Formal Categorical Core

$$L \;\text{distributive lattice} \implies L \cong \mathcal{O}(\mathrm{Irr}(L)) \subseteq \mathcal{P}(X)$$

## Local Olog (`types` & `aspects`)

- **Type `distLat`:** Finite Distributive Lattice L
- **Type `joinIrr`:** Poset of Join-Irreducible Atoms Irr(L)
- **Type `subLat`:** Subset Inclusion Lattice P(Irr(L))
- **Aspect:** `distLat` —*extracts prime/atomic elements*→ `joinIrr`
- **Aspect:** `distLat` —*is order-isomorphic via Birkhoff map to*→ `subLat`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-17` → [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Lattice meets ∧ and joins ∨ are categorical products and coproducts in a thin category (`$\rho_{17}: (a \wedge b, a \vee b) \mapsto (a \times_P b, a +_P b)$`)
- **Outgoing `rho-27` → [heyting-and-boolean-algebras-bicartesian-closed](heyting-and-boolean-algebras-bicartesian-closed.md):** Classical Boolean algebras are Heyting algebras satisfying P ∨ ¬P = ⊤ (`$\rho_{27}: \mathbf{BoolAlg} \hookrightarrow \mathbf{HeytingAlg}$`)
- **Incoming `rho-15` ← [orders-hasse-diagrams-and-lattices](orders-hasse-diagrams-and-lattices.md):** Finite distributive lattices are isomorphic to downset lattices of join-irreducibles (`$\rho_{15}: (L, \wedge, \vee) \xrightarrow{\sim} (\mathcal{O}(\mathrm{Irr}(L)), \cap, \cup)$`)

## Extracted Definitions, Theorems & Tasks (4)

- **Theorem-4.19** (`[p. 148]` · *Visual Theorem 19*): the join operation of two sets in an inclusion order is their union, andthe meet operation is their set intersection.
- **Theorem-4.20** (`[p. 150]` · *Visual Theorem 20*): Each distributive lattice is isomorphic to an inclusion order of its join-irreducible elements.
- **Task-4.28** (`[p. 151]` · *Interactive Task 4 (The partial order of numbers by division)*): Prove that all finite lattices are bounded. Order isomorphisms We mentioned order isomorphisms several times already so this is about time toelaborate on what they are. Given two sets (we will use partial order of numbers by division and the primeinclusion order as an example) an isomorphism between them is comprised ofthe following two functions:
- **Definition-4.38** (`[p. 152]` · *Such functions are called order-preserving functions.*): An isomorphism between two orders is an invertible function betweentheir underlying sets, such that applying this function (let’s call it )to any two elements that have a certain order in one set (let’s callthem  and ) should result in two elements that have a correspondingorder in the other set (i.e.  if and only if ). F a b a≤b F(a)≤F(b)
