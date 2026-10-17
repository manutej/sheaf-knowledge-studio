# Chapter 5: Logic — Propositions as Objects, Proofs as Morphisms & Heyting Algebras

**Page Span:** `pp. 162–211`

**Theme:** Categorifying deductive logic: propositions as objects, proofs/entailments P ⊢ Q as morphisms; conjunction (∧) as categorical product, disjunction (∨) as coproduct, implication (P ⇒ Q) as exponential object; classical Boolean vs. intuitionistic BHK Heyting logic.

## Global Invariants

- Logical Product & Coproduct (p. 165): Conjunction P ∧ Q is the universal product (elimination projections + pairing); Disjunction P ∨ Q is the universal coproduct (introduction injections + case analysis).
- Implication Adjunction / Currying (p. 180): R ∧ P ⊢ Q iff R ⊢ (P ⇒ Q), making implication the internal hom / exponential in a Heyting algebra.
- Intuitionistic BHK vs. Classical Excluded Middle (p. 184, p. 203): Constructive logic corresponds to bicartesian closed categories (Heyting algebras) where ¬¬P → P is not assumed without a witness.

## Concept Stalks in this Chapter

- [Categorifying Logic: Propositions as Objects & Proofs as Arrows](../concepts/propositional-logic-as-category.md) (`§5.1`, `pp. 162–179`): Viewing deductive logic as a category where objects are propositions, morphisms P → Q are proofs/entailments, identity is tautology P ⊢ P, composition is Modus Ponens / syllogism, Truth ⊤ is Terminal, Falsity ⊥ is Initial, Conjunction ∧ is Product, and Disjunction ∨ is Coproduct.
- [Implication (P ⇒ Q), Exponential Currying & Intuitionistic BHK Logic](../concepts/implication-currying-and-intuitionistic-bhk.md) (`§5.2`, `pp. 180–196`): Internalizing entailment as an Implication object P ⇒ Q via the currying adjunction (R ∧ P ⊢ Q iff R ⊢ P ⇒ Q); Brouwer-Heyting-Kolmogorov (BHK) constructive proof interpretation where a proof of P ⇒ Q is a function transforming proofs of P into proofs of Q.
- [Heyting Algebras, Boolean Algebras & Bicartesian Closed Categories](../concepts/heyting-and-boolean-algebras-bicartesian-closed.md) (`§5.3`, `pp. 197–211`): Thin bicartesian closed categories are Heyting Algebras (modeling intuitionistic logic where P ∨ ¬P need not hold globally, e.g., open-set topologies); adding Law of Excluded Middle yields Boolean Algebras.
