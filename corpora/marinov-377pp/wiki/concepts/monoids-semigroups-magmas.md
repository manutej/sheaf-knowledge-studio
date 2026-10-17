# Magmas, Semigroups & Monoids as Composable Actions (`U_07`)

- **Chapter:** 3 (`§3.1`)
- **Page Fiber:** `pp. 95–103`
- **Layer:** Algebraic Symmetries

## Summary

Algebraic structures built by progressively adding categorical laws to a binary operation: Magmas (closure), Semigroups (associativity), and Monoids (associativity + neutral identity element e), illustrated via color blending, clock arithmetic, and string concatenation.

## Formal Categorical Core

$$(M, \star, e) \quad \text{s.t.} \quad (a \star b) \star c = a \star (b \star c) \;\wedge\; e \star a = a = a \star e$$

## Local Olog (`types` & `aspects`)

- **Type `magma`:** Magma (M, ⋆) (Closed Operation)
- **Type `semigroup`:** Semigroup (Associative Operation)
- **Type `monoid`:** Monoid (M, ⋆, e) (With Identity e)
- **Aspect:** `monoid` —*forgets identity element to*→ `semigroup`
- **Aspect:** `semigroup` —*forgets associativity law to*→ `magma`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-10` → [groups-rotations-and-symmetries](groups-rotations-and-symmetries.md):** Equipping every monoid element with a two-sided inverse g⁻¹ yields a Group (`$\rho_{10}: (M, \star, e) \hookrightarrow (G, \star, e, (-)^{-1})$`)
- **Outgoing `rho-12` → [monoids-as-single-object-categories-free-monoids](monoids-as-single-object-categories-free-monoids.md):** Delooping any monoid M into a one-object category BM with Hom(•,•) = M (`$\rho_{12}: M \xrightarrow{\sim} \mathrm{Hom}_{\mathbf{B}M}(\bullet, \bullet)$`)
- **Incoming `rho-09` ← [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Associativity and identity laws of categorical composition specialize to monoid laws (`$\rho_{09}: (\circ, \mathrm{id}) \mapsto (\star, e)$`)

## Extracted Definitions, Theorems & Tasks (6)

- **Definition-3.26** (`[p. 95]` · *Visual Definition 26*): A monoid is defined by a collection/set of elements  (called themonoid’s underlying set), together with an associative monoidoperation — a rule for combining two elements that produces a thirdelement one of the same kind — . Also, there should be anidentity element , such that  and . A A∘A→AI I∘A=A A∘I=A
- **Task-3.14** (`[p. 98]` · *Interactive Task 1 (Basic monoids)*): Which are the identity elements of those monoids? N{0,1,2,3...} ⟨N,+⟩ 1+1=2
- **Task-3.15** (`[p. 99]` · *Interactive Task 2 (Basic monoids)*): Go through other mathematical operations and verify that they aremonoidal. Task 3: The natural numbers form a monoid under multiplication, but not agroup. Find out why. Monoids and boolean algebra Thinking about operations that we covered, we may remember the booleanoperations and and or. The operation and forms a monoid on the set, consistingof just two val
- **Task-3.16** (`[p. 99]` · *Interactive Task 3 (Basic monoids)*): The natural numbers form a monoid under multiplication, but not agroup. Find out why. Monoids and boolean algebra Thinking about operations that we covered, we may remember the booleanoperations and and or. The operation and forms a monoid on the set, consistingof just two values , in which  is the identity element (thesymbol  means and). The operation or al
- **Task-3.17** (`[p. 99]` · *Interactive Task 4 (Basic monoids)*): Prove that and  is associative by expanding the formula with all possible values. Do the same for or.Task 5: Which are the identity elements of the or operations? Monoid operations in terms of sets We now know what the monoid operation is, and we even saw some simpleexamples. However, we never defined the monoid rule/operation formally i.e.using the language
- **Definition-3.27** (`[p. 102]` · *Visual Definition 27*): A group is a monoid in which every element , has an inverse element,denoted usually as , such that  (where  is theidentity element). A−A A∘−A=I I +Z N {0,1,2,3...}{...−3,−2−1,0,1,2,3...} x+(−x)=0
