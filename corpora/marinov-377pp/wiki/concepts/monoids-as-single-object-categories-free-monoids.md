# Delooping Monoids as One-Object Categories & Free Monoids (`U_09`)

- **Chapter:** 3 (`§3.3`)
- **Page Fiber:** `pp. 115–130`
- **Layer:** Algebraic Symmetries

## Summary

Shifting perspective from monoid elements as static points to monoid elements as self-arrows on a single object (Cayley representation); free monoids (lists/strings) and their universal property.

## Formal Categorical Core

$$\mathbf{B}M : \mathrm{Ob}(\mathbf{B}M) = \{\bullet\}, \quad \mathrm{Hom}_{\mathbf{B}M}(\bullet, \bullet) = M, \quad \mathrm{Free}(A) = \mathrm{List}(A)$$

## Local Olog (`types` & `aspects`)

- **Type `genSet`:** Generator Alphabet Set A
- **Type `freeMon`:** Free Monoid List(A)
- **Type `oneObjCat`:** Single-Object Category BM
- **Aspect:** `genSet` —*generates all finite words in*→ `freeMon`
- **Aspect:** `freeMon` —*universally folds into any*→ `oneObjCat`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-32` → [inductive-types-nat-list-and-church-encodings](inductive-types-nat-list-and-church-encodings.md):** The inductive type List A (Nil, Cons) is the Free Monoid on type A (`$\rho_{32}: \mathrm{Free}(A) \cong \mathrm{List}\;A$`)
- **Outgoing `rho-39` → [functors-across-monoids-orders-logic](functors-across-monoids-orders-logic.md):** Functors BM → BN are exact monoid homomorphisms M → N (`$\rho_{39}: \mathrm{Fun}(\mathbf{B}M, \mathbf{B}N) \cong \mathrm{Hom}_{\mathbf{Mon}}(M, N)$`)
- **Incoming `rho-11` ← [groups-rotations-and-symmetries](groups-rotations-and-symmetries.md):** Groups are single-object categories (groupoids) where every arrow is an isomorphism (`$\rho_{11}: G \mapsto \mathbf{B}G$`)
- **Incoming `rho-12` ← [monoids-semigroups-magmas](monoids-semigroups-magmas.md):** Delooping any monoid M into a one-object category BM with Hom(•,•) = M (`$\rho_{12}: M \xrightarrow{\sim} \mathrm{Hom}_{\mathbf{B}M}(\bullet, \bullet)$`)
- **Incoming `rho-13` ← [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Restricting a category C to |Ob(C)| = 1 recovers a monoid (`$\rho_{13}: \mathcal{C}_{|\mathrm{Ob}|=1} \simeq \mathbf{B}M$`)

## Extracted Definitions, Theorems & Tasks (6)

- **Task-3.22** (`[p. 120]` · *Interactive Task 10 (Monoid elements as objects)*): Which are the identity elements of function groups? Task 11: Show that the functions representing inverse group elements are alsoinverse. Cayley’s theorem Let’s recap: in the previous section, we showed how the elements of everygroup/monoid correspond to functions from the monoid’s underlying set toitself (AKA to permutations), and we said that those permuta
- **Task-3.23** (`[p. 120]` · *Interactive Task 11 (Monoid elements as objects)*): Show that the functions representing inverse group elements are alsoinverse. Cayley’s theorem Let’s recap: in the previous section, we showed how the elements of everygroup/monoid correspond to functions from the monoid’s underlying set toitself (AKA to permutations), and we said that those permutations make up amonoid of their own, under functional composit
- **Theorem-3.16** (`[p. 121]` · *Visual Theorem 16*): Any group is isomorphic to its corresponding permutation group. PermPerm(A)≅A A
- **Definition-3.31** (`[p. 123]` · *Visual Definition 31*): A category is a collection of objects (we can think of them as points)and morphisms (arrows) that go from one object to another, where: 1. Each object has to have an identity morphism.2. There should be a way to compose two morphisms with anappropriate type signature into a third one in a way that isassociative.
- **Definition-3.32** (`[p. 124]` · *A→A*): A monoid, any monoid, can be seen as a category with one object—themorphisms of the category are the monoid elements, the identitymorphism is the identity element and the monoid operation iscomposition of morphisms. The converse is also true: any category withone object can be seen as a monoid
- **Task-3.24** (`[p. 130]` · *Interactive Task 14 (The universal property of free monoids)*): Write up the laws of the color-mixing monoid. If we put on our programmers’ hat, we will see that the type of the freemonoid under the set of generators T (which we can denote asFreeMonoid<T>) is isomorphic to the type List<T> and that the intuitionbehind the special property that we described above is actually very simple:keeping objects in a list allows yo
