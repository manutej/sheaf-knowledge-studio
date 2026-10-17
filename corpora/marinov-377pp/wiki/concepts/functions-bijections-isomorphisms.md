# Injections, Surjections, Isomorphisms & Currying in Set (`U_03`)

- **Chapter:** 1 (`§1.3`)
- **Page Fiber:** `pp. 28–51`
- **Layer:** Set-Theoretic Grounding

## Summary

Functions in mathematics vs. programming; function composition g ∘ f; injections (one-to-one), surjections (onto), and bijections; set isomorphisms via invertible arrow pairs; higher-order functions and currying.

## Formal Categorical Core

$$f : A \xrightarrow{\sim} B \iff \exists g : B \to A \text{ s.t. } g \circ f = \mathrm{id}_A \;\wedge\; f \circ g = \mathrm{id}_B$$

## Local Olog (`types` & `aspects`)

- **Type `domA`:** Domain Set A
- **Type `codB`:** Codomain Set B
- **Type `iso`:** Isomorphism Pair (f, g)
- **Aspect:** `domA` —*bijection f : A → B*→ `codB`
- **Aspect:** `codB` —*inverse g : B → A*→ `domA`
- **Aspect:** `iso` —*satisfies g ∘ f = id_A on*→ `domA`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-03` → [external-products-and-projections](external-products-and-projections.md):** Replacing internal ordered pairs (a,b) with external projection functions π₁, π₂ (`$\rho_{03}: (a,b) \mapsto (\pi_1, \pi_2)$`)
- **Outgoing `rho-08` → [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Set bijections generalize to categorical isomorphisms g ∘ f = id_A, f ∘ g = id_B (`$\rho_{08}: \mathrm{Bij}(A,B) \mapsto \mathrm{Iso}_{\mathcal{C}}(A,B)$`)
- **Outgoing `rho-25` → [implication-currying-and-intuitionistic-bhk](implication-currying-and-intuitionistic-bhk.md):** Function currying Hom(R × P, Q) ≅ Hom(R, Q^P) mirrors logical deduction theorem (`$\rho_{25}: Q^{P} \leftrightarrow (P \Rightarrow Q)$`)
- **Incoming `rho-02` ← [sets-subsets-empty-singleton](sets-subsets-empty-singleton.md):** Functions f : A → B and Hom-sets Hom(A,B) between sets (`$\rho_{02}: (A,B) \mapsto \mathrm{Hom}_{\mathbf{Set}}(A,B)$`)

## Extracted Definitions, Theorems & Tasks (15)

- **Task-1.5** (`[p. 29]` · *Interactive Task 7 (Sets and Functions in Programming)*): What is the type equivalent of subsets in programming? Functions and methods/subroutines Functions in programming (also called methods, subroutines, etc.) kindaresemble mathematical functions — they take an element that belongs to agiven set and return exactly one element which belongs to another set. For example, here is a method that takes an argument of t
- **Theorem-1.4** (`[p. 32]` · *Visual Theorem 4*): For any three sets ,  and  and two functions  and we can define a function , such that, if you followthe  arrow for any element of set  you will get to the sameelement of the set  as the one you will get if you follow the  arrowand then the  arrow. We call  the composition of  and . YP G g:Y→Pf:P→G f∘gf∘g YG gf f∘g g f f∘g f(g(a)
- **Task-1.6** (`[p. 33]` · *Interactive Task 8 (Sets and Functions in Programming)*): Think about which qualities of a function make composition possible,e.g., does it work with other types of relationships, like many-to-many andone-to-many. Composition in everyday life To understand how powerful composition is, consider the following: one setbeing connected to another means that each function from the second set canbe transferred to a corres
- **Task-1.7** (`[p. 36]` · *Interactive Task 9 (Sets and Functions in Programming)*): Think about what would be those functions’ sources and targets. By the way, diagrams that are “zoomed out” that show functions withoutshowing set elements are called external diagrams, as opposed to the ones thatwe saw before, which are internal. Composition and external diagrams Let’s look at the diagram that demonstrates functional composition in which wes
- **Definition-1.8** (`[p. 38]` · *Visual Definition 8*): The composition of two functions  and  is a third function  definedin such a way that all the paths in this diagram are equivalent.f g h
- **Task-1.8** (`[p. 41]` · *Interactive Task 10 (Sets and Functions in Programming)*): Draw the above diagrams as internal diagrams: define three functionsthat compose with one another (you can use the two functions that we definedearlier, you only would have to make a third one) compose them in the twoways shown above and check if the result is the same. Category theory — hints for the definition At this point you might be worried that I had 
- **Theorem-1.5** (`[p. 41]` · *Isomorphism*): Functional composition is associative i.e., for any functions   and with the appropriate type signature  is the same asfg c(f∘g)∘cf∘(g∘c) DEFINITION: Category theory is the study of things that are function-like (thatcompose in an associative way).
- **Definition-1.9** (`[p. 41]` · *Visual Definition 9*): Category theory is the study of things that are function-like (thatcompose in an associative way).
- **Definition-1.10** (`[p. 43]` · *Visual Definition 10*): (Internal) Two sets  and  are isomorphic (or ) if there exista one-to-one relationship between their elements.A B A≅B DEFINITION: (External) Two sets  and  are isomorphic (or ) if there existfunctions  and its reverse , such that and . A B A≅Bf:A→B g:B→Af∘g=IDA g∘f=IDB
- **Definition-1.11** (`[p. 43]` · *Visual Definition 11*): (External) Two sets  and  are isomorphic (or ) if there existfunctions  and its reverse , such that and . A B A≅Bf:A→B g:B→Af∘g=IDA g∘f=IDB
- **Theorem-1.6** (`[p. 44]` · *Visual Theorem 6*): The identity function is an isomorphism. A B AB
- **Theorem-1.7** (`[p. 45]` · *Visual Theorem 7*): Two sets that are both isomorphic to a third one are isomorphic to oneanother.
- **Definition-1.12** (`[p. 49]` · *Visual Definition 12*): An equivalence relation between sets is a relation that obeys the lawsof reflexivity, transitivity, and symmetry. AA=A
- **Theorem-1.8** (`[p. 50]` · *A=B B=A*): Isomorphisms are equivalence relations
- **Task-1.9** (`[p. 51]` · *Interactive Task 11 (Isomorphisms and equivalence)*): One law down, two to go: Go through the previous section and verifythat isomorphisms also satisfy the other equivalence relation laws. What I am trying to say with all this is that it makes sense to treat anyisomorphism as equality. For this reason, the practice of using isomorphisms todefine an equivalence relation is very prominent in category theory where
