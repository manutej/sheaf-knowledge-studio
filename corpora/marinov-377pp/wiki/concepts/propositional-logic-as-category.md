# Categorifying Logic: Propositions as Objects & Proofs as Arrows (`U_13`)

- **Chapter:** 5 (`§5.1`)
- **Page Fiber:** `pp. 162–179`
- **Layer:** Logical Deduction

## Summary

Viewing deductive logic as a category where objects are propositions, morphisms P → Q are proofs/entailments, identity is tautology P ⊢ P, composition is Modus Ponens / syllogism, Truth ⊤ is Terminal, Falsity ⊥ is Initial, Conjunction ∧ is Product, and Disjunction ∨ is Coproduct.

## Formal Categorical Core

$$\frac{P \vdash Q \quad Q \vdash R}{P \vdash R} \;(\circ), \quad P \wedge Q \equiv P \times Q, \quad P \vee Q \equiv P + Q, \quad \top \equiv 1, \quad \bot \equiv 0$$

## Local Olog (`types` & `aspects`)

- **Type `propObj`:** Logical Propositions P, Q
- **Type `proofArr`:** Deductive Entailment P ⊢ Q
- **Type `connLim`:** Universal Connectives (P ∧ Q, P ∨ Q, ⊤, ⊥)
- **Aspect:** `propObj` —*are connected by proofs in*→ `proofArr`
- **Aspect:** `connLim` —*constructs products/coproducts of*→ `propObj`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-24` → [implication-currying-and-intuitionistic-bhk](implication-currying-and-intuitionistic-bhk.md):** Internalizing deduction P ⊢ Q as the implication object P ⇒ Q via currying (`$\rho_{24}: (R \wedge P \vdash Q) \xrightarrow{\sim} (R \vdash P \Rightarrow Q)$`)
- **Outgoing `rho-28` → [heyting-and-boolean-algebras-bicartesian-closed](heyting-and-boolean-algebras-bicartesian-closed.md):** Combining ⊤, ⊥, ∧, ∨, and ⇒ forms a thin Bicartesian Closed Category (`$\rho_{28}: (\top, \bot, \wedge, \vee, \Rightarrow) \mapsto \mathbf{BCC}_{\mathrm{thin}}$`)
- **Incoming `rho-21` ← [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Propositional entailment P ⊢ Q forms a preorder / thin category of deductions (`$\rho_{21}: (a \le b) \mapsto (P \vdash Q)$`)
- **Incoming `rho-22` ← [external-products-and-projections](external-products-and-projections.md):** Categorical Product A × B corresponds to Logical Conjunction P ∧ Q (`$\rho_{22}: (A \times B, \pi_1, \pi_2) \mapsto (P \wedge Q, \wedge\text{-Elim})$`)
- **Incoming `rho-23` ← [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Categorical Coproduct A + B corresponds to Logical Disjunction P ∨ Q (`$\rho_{23}: (A + B, \iota_1, \iota_2) \mapsto (P \vee Q, \vee\text{-Intro})$`)

## Extracted Definitions, Theorems & Tasks (10)

- **Definition-5.44** (`[p. 162]` · *Visual Definition 44*): Logic studies the rules by which knowing one thing leads you toconclude (or prove) that some other thing is also true, regardless ofthe things’ domain (e.g. scientific discipline) and by only referring tothe form of the proof ( i.e. “formally”). On top of that, logic tries to organize those rules and arguments inlogical systems (or formal systems as they are
- **Theorem-5.22** (`[p. 164]` · *∧ ∨ or →*): If Socrates is human, then Socrates is mortal. But Socrates is human.
- **Theorem-5.23** (`[p. 165]` · *So, Socrates is mortal.*): If it rains, the ground gets wet. It rains. Therefore the ground gets wet. DEFINITION:
- **Definition-5.45** (`[p. 165]` · *Therefore the ground gets wet.*): Modus ponens is a proposition, comprised of two other propositions,denoted  and , that states that if the proposition  is true, andthat if  implies  , then  is true as well i.e.. A B AA B(A→B) B(A∧(A⇒B))→B AA→BB implies BB CC→B
- **Definition-5.46** (`[p. 167]` · *(A∧(A⇒B))→B*): Propositions that are always true, regardless of are the value of thepropositions that form them, are called tautologies.
- **Definition-5.47** (`[p. 171]` · *Visual Definition 47*): An axiom schema is a formula (containing placeholders), from which wecan derive propositions (by replacing those placeholders withpropositions). THEOREM: Every tautology can be used as an axiom schema.
- **Theorem-5.24** (`[p. 171]` · *Visual Theorem 24*): Every tautology can be used as an axiom schema.
- **Definition-5.48** (`[p. 172]` · *Visual Definition 48*): A logical system (known also as formal system) is a collection of axiomschemas/rules of inference such that by applying them we can produceall possible propositions.
- **Definition-5.49** (`[p. 175]` · *Visual Definition 49*): According to the classical interpretation of logic:
- **Task-5.30** (`[p. 179]` · *Interactive Task 1 (Or we also can say:)*): Draw the diagram for or. Using those tables, we can also prove some axiom schemas we can use later: For And:  and  “If I am tired and hungry, this meansthat I am hungry”.For Or:  and  “If I have a pen this means that I ameither have a pen or a ruler”. The Implies operation
