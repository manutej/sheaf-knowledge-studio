# Partial Orders, Hasse Diagrams, Divisibility & Color Lattices (`U_10`)

- **Chapter:** 4 (`§4.1`)
- **Page Fiber:** `pp. 131–147`
- **Layer:** Order & Hierarchy

## Summary

Binary relations (reflexivity, antisymmetry, transitivity, totality); visual Hasse diagrams via transitive reduction; total orders vs. partial orders (subset inclusion, color mixing, integer divisibility); meets (greatest lower bounds) and joins (least upper bounds).

## Formal Categorical Core

$$(P, \le) : a \le a \;(\text{Refl}), \quad a \le b \wedge b \le c \Rightarrow a \le c \;(\text{Trans}), \quad a \le b \wedge b \le a \Rightarrow a = b \;(\text{Antisym})$$

## Local Olog (`types` & `aspects`)

- **Type `posetP`:** Partially Ordered Set (P, ≤)
- **Type `hasse`:** Transitive-Reduced Hasse Diagram
- **Type `lattice`:** Bounded Lattice (P, ∧, ∨, ⊥, ⊤)
- **Aspect:** `posetP` —*is visualized minimally as*→ `hasse`
- **Aspect:** `lattice` —*equips every pair with meet ∧ & join ∨ in*→ `posetP`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-15` → [birkhoff-representation-and-boolean-lattices](birkhoff-representation-and-boolean-lattices.md):** Finite distributive lattices are isomorphic to downset lattices of join-irreducibles (`$\rho_{15}: (L, \wedge, \vee) \xrightarrow{\sim} (\mathcal{O}(\mathrm{Irr}(L)), \cap, \cup)$`)
- **Outgoing `rho-16` → [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Viewing order relations a ≤ b as unique morphisms a → b in a thin category (`$\rho_{16}: (a \le b) \mapsto \mathrm{Hom}_{P}(a,b) = \{*\}$`)
- **Incoming `rho-14` ← [sets-subsets-empty-singleton](sets-subsets-empty-singleton.md):** Subset containment A ⊆ B defines the prototypical partial order and lattice (`$\rho_{14}: (\mathcal{P}(X), \subseteq) \mapsto (P, \le)$`)

## Extracted Definitions, Theorems & Tasks (10)

- **Definition-4.33** (`[p. 131]` · *Visual Definition 33*): An order is a set of elements, together with a binary relation betweenthese elements, denoted with  (“bigger or equal to”) that obeyscertain laws. ≤
- **Definition-4.34** (`[p. 133]` · *Visual Definition 34*): A linear order is a set of elements, together with a binary relationbetween these elements, that obeys the laws of reflexivity,transitivity, antisymmetry, totality.
- **Task-4.25** (`[p. 136]` · *Interactive Task 1 (Orders)*): Previously, we covered a relation that is pretty similar to this. Do youremember it? What is the difference? Task 2: Think about some orders that you know about and figure out whetherthey are partial or total. Partial orders are actually much more interesting than linear/total orders. Butbefore we dive into them, let’s say a few things about numbers. The ord
- **Task-4.26** (`[p. 136]` · *Interactive Task 2 (Orders)*): Think about some orders that you know about and figure out whetherthey are partial or total. Partial orders are actually much more interesting than linear/total orders. Butbefore we dive into them, let’s say a few things about numbers. The order of natural numbers Natural numbers form a linear order under the operation bigger or equal to (thesymbol of which 
- **Definition-4.35** (`[p. 138]` · *Visual Definition 35*): An partial order is a set of elements, together with a binary relationbetween those elements, that obeys the laws of reflexivity, transitivityand antisymmetry.
- **Definition-4.36** (`[p. 142]` · *a b c*): The join of objects  and  is an object , such that: 1. It is bigger than both of these objects, so  and .2. It is smaller than any other object that is bigger than them, so forany other object  such that  and  then we shouldalso have . A B G A≤G B≤G
- **Task-4.27** (`[p. 143]` · *Interactive Task 3 (Orders)*): Which concept in category theory reminds you of joins? Meets
- **Theorem-4.17** (`[p. 145]` · *Visual Theorem 17*): In the color-mixing order, the join of any two colors is the color thatthey make up when mixed.
- **Theorem-4.18** (`[p. 146]` · *a ba b 2×5=102 5 10 310*): The partial order of numbers by division
We saw that when we order numbers by “bigger or equal to”, they form a linearorder. But numbers can also form a partial order, for example they form apartial order if we order them by which divides which, i.e. if  divides , then is before  e.g. because ,  and
- **Definition-4.37** (`[p. 147]` · *Visual Definition 37*): The inclusion order of a given collection of sets (usually sets thatcontain some common elements) is an order, based on the followingbinary relation:  comes before  if  includes , or in other wordsif  is a subset of .A BA BB A
