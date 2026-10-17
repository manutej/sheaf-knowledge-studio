# Implication (P ⇒ Q), Exponential Currying & Intuitionistic BHK Logic (`U_14`)

- **Chapter:** 5 (`§5.2`)
- **Page Fiber:** `pp. 180–196`
- **Layer:** Logical Deduction

## Summary

Internalizing entailment as an Implication object P ⇒ Q via the currying adjunction (R ∧ P ⊢ Q iff R ⊢ P ⇒ Q); Brouwer-Heyting-Kolmogorov (BHK) constructive proof interpretation where a proof of P ⇒ Q is a function transforming proofs of P into proofs of Q.

## Formal Categorical Core

$$\mathrm{Hom}(R \wedge P, Q) \cong \mathrm{Hom}(R, P \Rightarrow Q), \quad \mathrm{eval} : (P \Rightarrow Q) \wedge P \to Q$$

## Local Olog (`types` & `aspects`)

- **Type `conjRP`:** Conjoined Premise R ∧ P
- **Type `impPQ`:** Implication Object (P ⇒ Q)
- **Type `bhkFunc`:** BHK Constructive Proof Transformer
- **Aspect:** `conjRP` —*transposes via currying to*→ `impPQ`
- **Aspect:** `impPQ` —*is realized constructively as*→ `bhkFunc`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-26` → [heyting-and-boolean-algebras-bicartesian-closed](heyting-and-boolean-algebras-bicartesian-closed.md):** Equipping a bounded lattice with relative pseudocomplements P ⇒ Q yields a Heyting algebra (`$\rho_{26}: (L, \wedge, \vee, \Rightarrow) \in \mathbf{Heyting}$`)
- **Outgoing `rho-34` → [simply-typed-lambda-calculus-curry-howard-lambek](simply-typed-lambda-calculus-curry-howard-lambek.md):** BHK constructive proofs of P ⇒ Q are lambda terms λx:P. t : P → Q (`$\rho_{34}: (P \Rightarrow Q) \cong (\lambda x:P.\; t : Q)$`)
- **Incoming `rho-24` ← [propositional-logic-as-category](propositional-logic-as-category.md):** Internalizing deduction P ⊢ Q as the implication object P ⇒ Q via currying (`$\rho_{24}: (R \wedge P \vdash Q) \xrightarrow{\sim} (R \vdash P \Rightarrow Q)$`)
- **Incoming `rho-25` ← [functions-bijections-isomorphisms](functions-bijections-isomorphisms.md):** Function currying Hom(R × P, Q) ≅ Hom(R, Q^P) mirrors logical deduction theorem (`$\rho_{25}: Q^{P} \leftrightarrow (P \Rightarrow Q)$`)

## Extracted Definitions, Theorems & Tasks (14)

- **Definition-5.50** (`[p. 185]` · *Visual Definition 50*): According to the BHK interpretation of logic: A proposition is something that has a proof.A logical operator is a construction that creates proofs from otherproofs.
- **Definition-5.51** (`[p. 186]` · *A B*): According to the BHK interpretation, a proof of  is a product ofa proofs of  and  ( ). A∧BA BA×B A B
- **Task-5.31** (`[p. 187]` · *Interactive Task 2 (Or we also can say:)*): What would be the or operation in this case? The Implies operation Now for the punchline: in the BHK interpretation, the implies operation is justa function between proofs. What is a proof that  implies  then? A proof that  implies  is just anelement of the set of functions that go from  to  i.e. the hom set of — if this set is empty, then there is no proof 
- **Definition-5.52** (`[p. 187]` · *A∧B A∧B*): According to the BHK interpretation, saying that  implies  (), would just mean that there exist an arrow (function) that canconvert a proof of  to a proof of . A BA→B A B A B A BA BA⇒BA B
- **Definition-5.53** (`[p. 187]` · *A B A BA BA⇒BA B*): both proofs exist) then the proof of  can be constructed (and so is “true”).
Task 2: What would be the or operation in this case?
The Implies operation
Now for the punchline: in the BHK interpretation, the implies operation is justa function between proofs.
What is a proof that  implies  then? A pro
- **Theorem-5.25** (`[p. 189]` · *In set theory, the  constant is expressed by the empty set.*): According to the BHK interpretation,  can be read as ¬A A→⊥ ⊥
- **Task-5.32** (`[p. 190]` · *Interactive Task 3 (The If and only if operation)*): Look up the definition of function and verify that there cannot exist afunction from any set to the empty set Task 4: Look up the definition of function and verify that there does exist afunction from the empty set to itself (in fact there exist a function from theempty set to any other set. Logics as categories Aside from being an alternative to classical l
- **Task-5.33** (`[p. 190]` · *Interactive Task 4 (The If and only if operation)*): Look up the definition of function and verify that there does exist afunction from the empty set to itself (in fact there exist a function from theempty set to any other set. Logics as categories Aside from being an alternative to classical logic, the BHK interpretation isinteresting because it provides that higher-level view of logic, that we need inorder t
- **Task-5.34** (`[p. 191]` · *Interactive Task 5 (The If and only if operation)*): There is a special types of programming languages called “proofassistants” that help you verify logical proofs. Install a proof assistant and tryto see how it works. I recommend the Coq Tutorial by Mike Nahas for Coq/Roql,the Natural Numbers Game for Lean or the HoTT Game for Agda. Task 6: We will concentrate on proving that some categories form logics. Butm
- **Task-5.35** (`[p. 191]` · *Interactive Task 6 (The If and only if operation)*): We will concentrate on proving that some categories form logics. Butmeanwhile, you can prove that all logics form categories, using the definition ofa category that we used in the previous chapter. Logics as orders DEFINITION: Some categories can be seen as logical systems: Objects arepropositions and morphisms are proofs.
- **Definition-5.54** (`[p. 191]` · *Logics as orders*): Some categories can be seen as logical systems: Objects arepropositions and morphisms are proofs.
- **Definition-5.55** (`[p. 192]` · *AB*): Some preorders can be seen as logical systems: elements arepropositions and the relationship “bigger than” is taken to mean“implies”, so (  is ).A→BA≤B
- **Definition-5.56** (`[p. 194]` · *meet join*): An order which has meets and joins for all elements is called a lattice. DEFINITION: A lattice is distributive, if for every three objects ,  and , wehave . AB CA∧(B∨C)≅(A∧B)∨(A∧C)
- **Definition-5.57** (`[p. 194]` · *Visual Definition 57*): A lattice is distributive, if for every three objects ,  and , wehave . AB CA∧(B∨C)≅(A∧B)∨(A∧C)
