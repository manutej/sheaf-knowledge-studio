# From Internal Pairs to External Categorical Products (A × B) (`U_04`)

- **Chapter:** 2 (`§2.1`)
- **Page Fiber:** `pp. 52–68`
- **Layer:** Categorical Foundations

## Summary

Constructing Cartesian products A × B first internally as grids of pairs (a,b), then externally (point-free) purely via projection morphisms π₁ : A × B → A, π₂ : A × B → B and the universal mediating arrow ⟨f, g⟩.

## Formal Categorical Core

$$\forall (C \xrightarrow{f} A, C \xrightarrow{g} B), \; \exists! \langle f, g \rangle : C \to A \times B \text{ s.t. } \pi_1 \circ \langle f,g \rangle = f \;\wedge\; \pi_2 \circ \langle f,g \rangle = g$$

## Local Olog (`types` & `aspects`)

- **Type `apexC`:** Candidate Object C
- **Type `prodAB`:** Universal Product A × B
- **Type `compAB`:** Component Objects A and B
- **Aspect:** `apexC` —*unique factorizer ⟨f, g⟩*→ `prodAB`
- **Aspect:** `prodAB` —*canonical projections π₁, π₂*→ `compAB`
- **Aspect:** `apexC` —*test morphisms f, g*→ `compAB`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-04` → [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Reversing all product arrows in C yields the Coproduct in C^op (`$\rho_{04}: (A \times B, \pi_i) \xrightarrow{\mathrm{op}} (A + B, \iota_i)$`)
- **Outgoing `rho-07` → [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Universal product cones live in any category C obeying associativity and identity (`$\rho_{07}: (A \times B)_{\mathbf{Set}} \mapsto (A \times B)_{\mathcal{C}}$`)
- **Outgoing `rho-19` → [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Universal product cone in a thin category collapses to greatest lower bound (meet ∧) (`$\rho_{19}: A \times B \mapsto a \wedge b$`)
- **Outgoing `rho-22` → [propositional-logic-as-category](propositional-logic-as-category.md):** Categorical Product A × B corresponds to Logical Conjunction P ∧ Q (`$\rho_{22}: (A \times B, \pi_1, \pi_2) \mapsto (P \wedge Q, \wedge\text{-Elim})$`)
- **Incoming `rho-03` ← [functions-bijections-isomorphisms](functions-bijections-isomorphisms.md):** Replacing internal ordered pairs (a,b) with external projection functions π₁, π₂ (`$\rho_{03}: (a,b) \mapsto (\pi_1, \pi_2)$`)

## Extracted Definitions, Theorems & Tasks (8)

- **Task-2.10** (`[p. 53]` · *Interactive Task 1 (From Sets toCategories)*): Why is this called a product? Hint: How many elements does it have? Naturally, the product comes equipped with two functions, one for eachproperty, which allow you to take a pair and extracts the value of theproperty, DEFINITION: The Cartesian product (or tuple) of sets  and  (denoted ) isthe set of ordered pairs that contain one element of the set  and onee
- **Definition-2.13** (`[p. 53]` · *Visual Definition 13*): The Cartesian product (or tuple) of sets  and  (denoted ) isthe set of ordered pairs that contain one element of the set  and oneelement of the set . Or formally speaking:  where ( means “is an element of”). A B A×BAB A×B=(a,b)a∈A,b∈B∈
- **Theorem-2.9** (`[p. 55]` · *Visual Theorem 9*): The two ways of combining three sets into a triple product areisomorphic, .(A×B)×C≅A×(B×C)
- **Definition-2.14** (`[p. 61]` · *Visual Definition 14*): The product of  and , denoted , is a set such that: 1. There exist two “projection” functions  and… A B A×B A×B→AA×B→B
- **Definition-2.15** (`[p. 64]` · *f1:A×B→A f2:A×B→BA×B×X A Bf1∘g f2∘g A×B×XA B*): The product of  and , denoted , is a set such that: 1. There exist two “projection” functions  and .2. For any impostor product , that also has such projection functions(  and ), there must also exist a unique function(called universal morphism) with the type signature , that converts the impostor product to the real product, such thatthe projections of the 
- **Definition-2.16** (`[p. 64]` · *g I*): That is, if we dub this function  and let  and
be the projections of the product (  and ),then, the arrow that connects the triple  to  and  are just the
compositions  and . It is almost as if  is only connectedto  and  because of this function.
More formally, we can define the product in the follow
- **Theorem-2.10** (`[p. 65]` · *A B A×B IA×B*): If a set  satisfies a given universal property (such as being theproduct of  and ), then any set isomorphic to  would also satisfyit. CA B C′ C′ C
- **Definition-2.17** (`[p. 66]` · *Defining sums in terms of sets—internaldefinition*): The sum of two sets  and , denoted  is a set that containsall elements from  combined with all elements from .A B A+BA B
