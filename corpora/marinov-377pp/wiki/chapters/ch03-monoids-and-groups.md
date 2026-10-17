# Chapter 3: Monoids & Groups — Single-Object Categories & Symmetries

**Page Span:** `pp. 95–130`

**Theme:** A monoid as a category with one object where elements become composable arrows; magmas, semigroups, monoids, and groups; rotational symmetries of geometric figures (C₃, D₃); Cayley's theorem and free monoids.

## Global Invariants

- Delooping / Single-Object Equivalence (p. 115): Every monoid (M, ⋆, e) is canonically a one-object category BM with Hom(•, •) = M.
- Group Invertibility (p. 104): A group is a category with one object in which every morphism is an isomorphism (an invertible symmetry).
- Universal Property of Free Monoids (p. 129): Lists [A] are the free monoid on A; any map A → M extends uniquely to a monoid homomorphism fold : [A] → M.

## Concept Stalks in this Chapter

- [Magmas, Semigroups & Monoids as Composable Actions](../concepts/monoids-semigroups-magmas.md) (`§3.1`, `pp. 95–103`): Algebraic structures built by progressively adding categorical laws to a binary operation: Magmas (closure), Semigroups (associativity), and Monoids (associativity + neutral identity element e), illustrated via color blending, clock arithmetic, and string concatenation.
- [Groups, Geometric Rotations (C₃, D₃) & Invertible Symmetries](../concepts/groups-rotations-and-symmetries.md) (`§3.2`, `pp. 104–114`): Adding inverses turns a monoid into a group (G, ⋆, e, inv): rotational symmetries of an equilateral triangle (0°, 120°, 240° = C₃), reflections (D₃), cyclic groups Z_n, and product groups.
- [Delooping Monoids as One-Object Categories & Free Monoids](../concepts/monoids-as-single-object-categories-free-monoids.md) (`§3.3`, `pp. 115–130`): Shifting perspective from monoid elements as static points to monoid elements as self-arrows on a single object (Cayley representation); free monoids (lists/strings) and their universal property.
