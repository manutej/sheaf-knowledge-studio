# Chapter 7: Functors — Structure-Preserving Maps Across Mathematical Worlds

**Page Span:** `pp. 278–318`

**Theme:** Functors F : C → D as homomorphisms between categories preserving identity and composition; unifying monoid homomorphisms, monotone poset maps, logical translations, and programming type constructors (List, Maybe, .map); contravariant and pointed functors.

## Global Invariants

- Functoriality Laws (p. 289–290): F(id_A) = id_{F(A)} and F(g ∘ f) = F(g) ∘ F(f).
- Cross-Domain Unification (p. 301): A functor between single-object categories is a monoid homomorphism; a functor between thin categories is a monotone order-preserving function.
- Programming Endofunctors (p. 306–308): In functional programming, a type constructor F : Type → Type equipped with map : (a → b) → (F a → F b) is an endofunctor.

## Concept Stalks in this Chapter

- [Functors F : C → D — Structure-Preserving Maps Between Categories](../concepts/functors-structure-preserving-maps.md) (`§7.1`, `pp. 278–295`): Generalizing order-embeddings and group homomorphisms to arbitrary categories: a functor F : C → D maps objects to objects and morphisms to morphisms while preserving identities and composition triangles.
- [Functors Across Worlds: Monoid Homomorphisms & Monotone Maps](../concepts/functors-across-monoids-orders-logic.md) (`§7.2`, `pp. 296–305`): Instantiating the functor laws across Chapters 1–5: functors between one-object categories BM → BN are monoid homomorphisms f(x ⋆ y) = f(x) · f(y); functors between thin poset categories are monotone functions a ≤ b ⇒ F(a) ≤ F(b); forgetful functors strip structure.
- [Programming Endofunctors (List, Maybe, .map), Pointed & Contravariant Functors](../concepts/programming-endofunctors-pointed-contravariant.md) (`§7.3`, `pp. 306–318`): Functors in software engineering: generic type constructors F<A> equipped with map / fmap lifting functions (A → B) to (F<A> → F<B>); pointed functors (unit/pure : A → F<A>); contravariant functors F : C^op → D reversing arrow direction (predicates, serializers, Hom(-, R)).
