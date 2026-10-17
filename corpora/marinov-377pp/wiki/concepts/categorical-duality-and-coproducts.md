# Categorical Duality, Coproducts (A + B) & Initial/Terminal Objects (`U_05`)

- **Chapter:** 2 (`§2.2`)
- **Page Fiber:** `pp. 69–81`
- **Layer:** Categorical Foundations

## Summary

The principle of Categorical Duality: reversing every arrow in the external diagram of Product yields Coproduct (disjoint union / sum A + B with injections ι₁, ι₂ and co-pairing [f, g]), and reversing Terminal Object 1 yields Initial Object 0.

## Formal Categorical Core

$$\forall (A \xrightarrow{f} C, B \xrightarrow{g} C), \; \exists! [f, g] : A + B \to C \text{ s.t. } [f,g] \circ \iota_1 = f \;\wedge\; [f,g] \circ \iota_2 = g$$

## Local Olog (`types` & `aspects`)

- **Type `partsAB`:** Summand Objects A and B
- **Type `coprodAB`:** Universal Coproduct A + B
- **Type `targetC`:** Target Object C
- **Aspect:** `partsAB` —*canonical injections ι₁, ι₂*→ `coprodAB`
- **Aspect:** `coprodAB` —*unique case-analysis [f, g]*→ `targetC`
- **Aspect:** `partsAB` —*branch handlers f, g*→ `targetC`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-06` → [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Abstracting objects, morphisms, associative composition, and identity laws (`$\rho_{06}: (\mathbf{Set}, \circ) \mapsto (\mathcal{C}, \circ, \mathrm{id})$`)
- **Outgoing `rho-20` → [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Universal coproduct cocone in a thin category collapses to least upper bound (join ∨) (`$\rho_{20}: A + B \mapsto a \vee b$`)
- **Outgoing `rho-23` → [propositional-logic-as-category](propositional-logic-as-category.md):** Categorical Coproduct A + B corresponds to Logical Disjunction P ∨ Q (`$\rho_{23}: (A + B, \iota_1, \iota_2) \mapsto (P \vee Q, \vee\text{-Intro})$`)
- **Outgoing `rho-30` → [type-theory-russell-and-formation-intro-elim](type-theory-russell-and-formation-intro-elim.md):** Type Introduction rules (arrows in) and Elimination rules (universal arrows out) (`$\rho_{30}: (\iota, [f,g]) \mapsto (\text{Intro}, \text{Elim})$`)
- **Incoming `rho-04` ← [external-products-and-projections](external-products-and-projections.md):** Reversing all product arrows in C yields the Coproduct in C^op (`$\rho_{04}: (A \times B, \pi_i) \xrightarrow{\mathrm{op}} (A + B, \iota_i)$`)
- **Incoming `rho-05` ← [sets-subsets-empty-singleton](sets-subsets-empty-singleton.md):** Empty set ∅ as Initial Object 0 and Singleton {•} as Terminal Object 1 (`$\rho_{05}: (\emptyset, 1) \mapsto (0_{\mathcal{C}}, 1_{\mathcal{C}})$`)

## Extracted Definitions, Theorems & Tasks (9)

- **Definition-2.18** (`[p. 69]` · *Visual Definition 18*): The sum of  and , denoted , is a set, such that: 1. There exists two “projection” functions  and.2. For any impostor sum , that also has such projection functions ( and ), there must also exist a unique function withthe type signature , that converts the real sum tothe impostor sum, such that the projections of the impostor sum bejust the composition of  wit
- **Theorem-2.11** (`[p. 73]` · *So, our example set would look like this.*): Each element of a set  is isomorphic to a function  (where means the singleton set).X 1→X 1
- **Theorem-2.12** (`[p. 74]` · *Visual Theorem 12*): There is a unique function from any set to any singleton set. 1 X→1X ∀X∃!(X→1) ∃!
- **Definition-2.19** (`[p. 76]` · *Visual Definition 19*): The singleton set  is one such that there exist a unique functionsfrom any other set to it i.e. we have , then  is thesingleton set. 1 ∀X∃!X→1 1
- **Task-2.11** (`[p. 77]` · *Interactive Task 2 (Here is the definition:)*): Why exactly does it follow (check the definition)?
- **Task-2.12** (`[p. 78]` · *Interactive Task 3 (Defining the empty set externally)*): why is the function from the empty set unique? Observant readers will notice the similarities between the diagrams depictingthe initial and terminal object (yes the two concepts are, of course, dual ofeach other). THEOREM: There is a unique function from the empty set to any other set.
- **Theorem-2.13** (`[p. 78]` · *Visual Theorem 13*): There is a unique function from the empty set to any other set. DEFINITION: The empty set is a set such that there exists a function from it to anyother set.
- **Definition-2.20** (`[p. 78]` · *There is a unique function from the empty set to any other set.*): The empty set is a set such that there exists a function from it to anyother set.
- **Theorem-2.14** (`[p. 81]` · *Visual Theorem 14*): Let  be an element of set , let the function  representthat element, and let  be any function from  to someother set. Then, the composition of the two functions is exactly the function that would represent the element which is theresult of calling the function  with the value of  as an argument. g X g:1→Xf:X→Y Xf∘g:1→Y f gf(g)
