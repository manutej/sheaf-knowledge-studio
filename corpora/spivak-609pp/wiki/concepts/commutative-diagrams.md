---
id: commutative-diagrams
title: "Commutative Diagrams & Path Equations"
type: SheafStalk
chapter: 2
section: "2.2"
pdf_pages: "44–46"
symbol: "Diag(C)"
layer: "Set-Theoretic Grounding"
extracted_declarations: 2
restricts_to: [sets-and-functions]
glues_with: [ologs-ontology-logs, pullbacks-and-fiber-products]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Commutative Diagrams & Path Equations (`Diag(C)`)

> **Sheaf Stalk Location:** Chapter 2 (The Category of Sets, Commutative Diagrams, and Ologs) · Section `2.2` · **PDF Pages 44–46**

## 1. Epistemic Worldview & Intuition

Diagrams of objects and morphisms where any two directed paths with the same start and end object compose to the exact same morphism. Commutativity is the categorical replacement for algebraic equations.

## 2. Formal Categorical Core

A diagram D : J -> C commutes if for every pair of parallel paths p, q : x ->* y in J, the induced composite morphisms in C satisfy D(p) = D(q). In Set, a square g o f = k o h commutes iff g(f(x)) = k(h(x)) for all x.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[A]`** — *a source object A*
- **`[B]`** — *an intermediate object B*
- **`[C]`** — *an intermediate object C*
- **`[D]`** — *a target object D*

### Functional Aspects (Morphisms)
- **`[A]` $\xrightarrow{\text{f}}$ `[B]`**
- **`[B]` $\xrightarrow{\text{g}}$ `[D]`**
- **`[A]` $\xrightarrow{\text{h}}$ `[C]`**
- **`[C]` $\xrightarrow{\text{k}}$ `[D]`**

### Commutative Path Facts ($p \simeq q$)
- Commutative Square Law: g ∘ f = k ∘ h (p. 45).
- Application 2.2.1.1 (p. 44): In physical and biological modeling, commuting diagrams assert that two measurement or transformation pipelines yield identical outcomes.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-04` (evaluates_paths)** $\to$ [[sets-and-functions]] (*The Category Set: Sets, Functions & Isomorphisms*, p. 26–43): Diagram commutes in Set iff composite functions agree pointwise — `(g ∘ f)(x) = (k ∘ h)(x)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-03` (declares_facts)** $\leftarrow$ [[ologs-ontology-logs]] (*Ologs (Ontology Logs): Functional Worldviews*, p. 47–67): Olog facts are path equations p ≃ q (commuting diagrams) — `Facts(O) ⊆ Path(G) × Path(G)`
- **`rho-08` (universal_commuting_square)** $\leftarrow$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Pullback square f ∘ p₁ = g ∘ p₂ is terminal among commuting squares over f, g — `f ∘ p₁ = g ∘ p₂`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 44–46)

### `Application 2.2.1.1` — [PDF Page 44]
> Application 2.2.1.1. In its most basic form, the central dogma of molecular biology is that DNA codes for RNA codes for protein. That is, there is a function from DNA triplets to RNA triplets and a function from RNA triplets to amino acids. But sometimes we just want to discuss the translation from DNA to amino acids, and this is the composite of the other two. The following commutative diagram is a picture of this fact Consider the following picture:

### `Application 2.2.1.2` — [PDF Page 45]
> Application 2.2.1.2. Given a physical system S, there may be two mathematical approaches f : S → A and g : S → B that can be applied to it. Either of those results in a prediction of the same sort, f′ : A → P and g′ : B → P. For example, in mechanics we can use either the Lagrangian approach or the Hamiltonian approach to predict future states. To say that the diagram commutes would say that these approaches give the same result. Note that diagram (2.6) is considered to be the same diagram as each of the following: In all these we have h = g ○ f, or in diagrammatic order, h = f; g.

## 6. Page-by-Page Deep Index (PDF Pages 44–46)
- **Page 44** (`2.2 Commutative diagrams`) · **Items:** Application 2.2.1.1: 2.2 Commutative diagrams At this point it is difficult to precisely define diagrams or commutative diagrams in general, but we can get a heuristic idea.5 Consider the following picture: We say this is a diagram of sets if each of A, B, C is a set and each of f, g, h is a function. We say this diagram commutes if g ○ f ...
- **Page 45** (`2.2 Commutative diagrams`) · **Items:** Application 2.2.1.2: We say this is a diagram of sets if each of A, B, C, D is a set and each of f, g, h, i is a function. We say this diagram commutes if g ○ f = i ○ h. In this case we refer to it as a commutative square of sets. More generally, it is a commutative diagram of sets. Application 2.2.1.2. Given a physical system S, there may...
- **Page 46** (`2.2 Commutative diagrams`): ...
