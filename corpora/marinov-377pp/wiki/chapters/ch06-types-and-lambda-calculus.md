# Chapter 6: Types — Curry-Howard-Lambek, ADTs & Simply Typed Lambda Calculus

**Page Span:** `pp. 212–277`

**Theme:** Russell's paradox and type hierarchy; type formation, introduction, elimination, and computation rules; Unit (1), Void (0), Maybe, Nat (Zero/Succ), List (Nil/Cons), Sum/Product ADTs, Church encodings, and Simply Typed Lambda Calculus (STLC) as a Cartesian Closed Category.

## Global Invariants

- Type Definition Quartet (p. 234): Every type constructor is specified by Formation, Introduction (constructors), Elimination (pattern-matching/destructors), and Computation (β/η laws).
- Curry-Howard-Lambek Isomorphism (p. 260): Types are Objects/Propositions, Programs/Terms Γ ⊢ t : B are Morphisms/Proofs, and β-reduction is diagram commutativity.
- Church Encoding Universality (p. 257): Every inductive ADT is encoded by its universal elimination signature (e.g., Bool ≡ ∀a. a → a → a).

## Concept Stalks in this Chapter

- [Type Theory, Russell's Paradox & Formation / Intro / Elim Rules](../concepts/type-theory-russell-and-formation-intro-elim.md) (`§6.1`, `pp. 212–239`): How Bertrand Russell resolved naive set-theoretic self-reference via stratified Types; defining types constructively through Type Formation, Term Introduction (constructors), Term Elimination (pattern matching), and Computation (β/η reduction), illustrated with Bool, Unit, Void, and Maybe.
- [Inductive Types (Nat, List), Algebraic Data Types & Church Encodings](../concepts/inductive-types-nat-list-and-church-encodings.md) (`§6.2`, `pp. 240–259`): Recursive inductive types: Natural numbers (Zero : 1 → Nat, Succ : Nat → Nat), Lists (Nil, Cons), Product types (Pair), Sum types (Either), and Alonzo Church's encodings representing data purely by its universal elimination function.
- [Simply Typed Lambda Calculus (STLC) & Curry-Howard-Lambek Rosetta Stone](../concepts/simply-typed-lambda-calculus-curry-howard-lambek.md) (`§6.3`, `pp. 260–277`): Sequent contexts Γ ⊢ t : A, lambda abstraction (λx. t) as currying, application as evaluation, and Joachim Lambek's three-way equivalence between Intuitionistic Logic, Simply Typed Lambda Calculus, and Cartesian Closed Categories.
