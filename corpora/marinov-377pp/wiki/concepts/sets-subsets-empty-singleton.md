# Sets, Subsets, Empty Set (∅) & Singleton (1) (`U_02`)

- **Chapter:** 1 (`§1.2`)
- **Page Fiber:** `pp. 13–27`
- **Layer:** Set-Theoretic Grounding

## Summary

Cantor's definition of sets as unstructured collections of distinct elements (illustrated as colored balls); subsets as spatial containment; singleton sets (1) and the unique empty set (∅); functions as many-to-one mappings and hom-sets.

## Formal Categorical Core

$$\forall A \in \mathbf{Set}, \quad \exists! \; \emptyset \to A \quad \text{and} \quad \exists! \; A \to 1, \quad \mathrm{Hom}(A,B) = B^A$$

## Local Olog (`types` & `aspects`)

- **Type `empty`:** Empty Set ∅ (Zero Elements)
- **Type `setA`:** General Set A (Colored Balls)
- **Type `singleton`:** Singleton Set 1 (One Element)
- **Type `hom`:** Hom-Set Hom(A, B)
- **Aspect:** `empty` —*unique absurd map ! : ∅ → A*→ `setA`
- **Aspect:** `setA` —*unique terminal map ! : A → 1*→ `singleton`
- **Aspect:** `setA` —*collects all arrows A → B into*→ `hom`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-02` → [functions-bijections-isomorphisms](functions-bijections-isomorphisms.md):** Functions f : A → B and Hom-sets Hom(A,B) between sets (`$\rho_{02}: (A,B) \mapsto \mathrm{Hom}_{\mathbf{Set}}(A,B)$`)
- **Outgoing `rho-05` → [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Empty set ∅ as Initial Object 0 and Singleton {•} as Terminal Object 1 (`$\rho_{05}: (\emptyset, 1) \mapsto (0_{\mathcal{C}}, 1_{\mathcal{C}})$`)
- **Outgoing `rho-14` → [orders-hasse-diagrams-and-lattices](orders-hasse-diagrams-and-lattices.md):** Subset containment A ⊆ B defines the prototypical partial order and lattice (`$\rho_{14}: (\mathcal{P}(X), \subseteq) \mapsto (P, \le)$`)
- **Outgoing `rho-29` → [type-theory-russell-and-formation-intro-elim](type-theory-russell-and-formation-intro-elim.md):** Stratifying naive sets into Types to resolve Russell's paradox and type-check functions (`$\rho_{29}: x \in A \mapsto \Gamma \vdash x : A$`)
- **Incoming `rho-01` ← [visual-abstraction-modes-of-knowledge](visual-abstraction-modes-of-knowledge.md):** Set theory as the first proto-example of an abstract formal language (`$\rho_{01}: \text{AbstractLanguage} \mapsto \mathbf{Set}$`)

## Extracted Definitions, Theorems & Tasks (14)

- **Definition-1.1** (`[p. 13]` · *G*): A set is a collection of items, that contains no structure, other thanwhich items belong to it.
- **Definition-1.2** (`[p. 14]` · *Y GY G*): is a subset of  when (or ) if every element of the set of is also an element in the set .Y G Y⊆G YG
- **Definition-1.3** (`[p. 15]` · *Visual Definition 3*): A singleton set is a set that contains one element.
- **Definition-1.4** (`[p. 17]` · *Visual Definition 4*): The empty set is a set that contains no elements. ∅ B=W=∅ ∀A→∅⊆A∀
- **Definition-1.5** (`[p. 18]` · *Visual Definition 5*): A function is many-to-one a relationship between two sets: one thatmatches each element of one set, called the source set of the function,with exactly one element from another set, called the target set of thefunction. f RG f:R→G
- **Definition-1.6** (`[p. 20]` · *Visual Definition 6*): The identity function for a set ,  is a function whichmaps every element of  to itself.GIDG:G→GG
- **Theorem-1.1** (`[p. 21]` · *IDG G*): For each set and subset, we can define a function (called the image ofthe subset) that maps each element of the subset to itself.
- **Theorem-1.2** (`[p. 22]` · *Although it doesn’t look like it…*): There is a unique function from the empty set to any other set.
- **Task-1.1** (`[p. 23]` · *Interactive Task 3 (Singleton Sets)*): Is this really valid? Why? Check the definition. If you still aren’t convinced, check this out: 1. There is a function between a subset and a its superset2. The empty set is a subset of any other set. So, evidently, this function has to exist!
- **Task-1.2** (`[p. 23]` · *Interactive Task 4 (Singleton Sets)*): What about the other way around. Are there functions with the emptyset as a target as opposed to its source? Functions and Singleton Sets And another function that we meet often is this one.
- **Task-1.3** (`[p. 24]` · *Interactive Task 5 (Singleton Sets)*): Is this really the only way to connect any set to a singleton set in avalid way? Task 6: Again, what about the other way around? Hom sets Given two sets  and  with a bunch of functions between them (here wedon’t draw the set elements and draw each function as a single arrow)…
- **Task-1.4** (`[p. 24]` · *Interactive Task 6 (Singleton Sets)*): Again, what about the other way around? Hom sets Given two sets  and  with a bunch of functions between them (here wedon’t draw the set elements and draw each function as a single arrow)… …we can construct the function set (usually called hom set) of  to ,containing those functions as elements.
- **Theorem-1.3** (`[p. 24]` · *Visual Theorem 3*): There is a unique function from any set to any singleton set. A B A B
- **Definition-1.7** (`[p. 25]` · *Visual Definition 7*): For objects  and  the homomorphism set of  to , (denoted) is the set containing one element for each function that goesfrom  to . A B A BA⇒BA B B A Z:=…−3−2,−1,0,1,2,3…N:=0,1,2,3…
