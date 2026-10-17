# The Formal Definition of a Category & Point-Free Epistemology (`U_06`)

- **Chapter:** 2 (`§2.3`)
- **Page Fiber:** `pp. 82–94`
- **Layer:** Categorical Foundations

## Summary

The Rosetta dictionary between Set Theory (internal elements) and Category Theory (external morphisms); objects, morphisms, composition (∘), identity arrows (id_A), commutative diagrams, and why associativity + identity are the exact laws of composition.

## Formal Categorical Core

$$\mathcal{C} = (\mathrm{Ob}(\mathcal{C}), \mathrm{Hom}_{\mathcal{C}}, \circ, \mathrm{id}) \quad \text{with} \quad h \circ (g \circ f) = (h \circ g) \circ f$$

## Local Olog (`types` & `aspects`)

- **Type `obC`:** Objects Ob(C) (Opaque Points)
- **Type `homC`:** Morphisms Hom(A, B) (Directed Arrows)
- **Type `compLaw`:** Associative Composition g ∘ f
- **Aspect:** `homC` —*has source and target in*→ `obC`
- **Aspect:** `homC` —*composes associatively via*→ `compLaw`
- **Aspect:** `obC` —*assigns identity arrow id_A in*→ `homC`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-09` → [monoids-semigroups-magmas](monoids-semigroups-magmas.md):** Associativity and identity laws of categorical composition specialize to monoid laws (`$\rho_{09}: (\circ, \mathrm{id}) \mapsto (\star, e)$`)
- **Outgoing `rho-13` → [monoids-as-single-object-categories-free-monoids](monoids-as-single-object-categories-free-monoids.md):** Restricting a category C to |Ob(C)| = 1 recovers a monoid (`$\rho_{13}: \mathcal{C}_{|\mathrm{Ob}|=1} \simeq \mathbf{B}M$`)
- **Outgoing `rho-18` → [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Truncating hom-sets to at most one arrow |Hom(a,b)| ≤ 1 yields Preorders (`$\rho_{18}: \mathcal{C}_{|\mathrm{Hom}|\le 1} \simeq \mathbf{Preord}$`)
- **Outgoing `rho-37` → [functors-structure-preserving-maps](functors-structure-preserving-maps.md):** Functors F : C → D are homomorphisms preserving categorical composition and identities (`$\rho_{37}: (\mathcal{C}, \mathcal{D}) \mapsto \mathrm{Fun}(\mathcal{C}, \mathcal{D})$`)
- **Incoming `rho-06` ← [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Abstracting objects, morphisms, associative composition, and identity laws (`$\rho_{06}: (\mathbf{Set}, \circ) \mapsto (\mathcal{C}, \circ, \mathrm{id})$`)
- **Incoming `rho-07` ← [external-products-and-projections](external-products-and-projections.md):** Universal product cones live in any category C obeying associativity and identity (`$\rho_{07}: (A \times B)_{\mathbf{Set}} \mapsto (A \times B)_{\mathcal{C}}$`)
- **Incoming `rho-08` ← [functions-bijections-isomorphisms](functions-bijections-isomorphisms.md):** Set bijections generalize to categorical isomorphisms g ∘ f = id_A, f ∘ g = id_B (`$\rho_{08}: \mathrm{Bij}(A,B) \mapsto \mathrm{Iso}_{\mathcal{C}}(A,B)$`)

## Extracted Definitions, Theorems & Tasks (6)

- **Definition-2.21** (`[p. 86]` · *Formally, this requirement sounds like this:*): signature, as we like to say) does not in any way make them equivalent to oneanother.
There are some types of categories that have only one morphism between twoobjects (in each direction), but we will talk about them in a later chapter.
Composition
The most important requirement for a structure to b
- **Task-2.13** (`[p. 88]` · *Interactive Task 4 (Category Theory Set theory)*): What is the identity morphism in the category of sets? The law of associativity Composition is special not only because you can take any two morphisms withappropriate signatures and make a third, but because you can do soindefinitely, i.e. for each  successive arrows, each of which has as a sourceobject the target object of the previous, we can draw one (exa
- **Definition-2.22** (`[p. 88]` · *negatesquareadd one*): The identity morphisms of each object , , denoted , etc. are such that for any  we haveAB IDA:A→AIDB:B→B f:A→Bf∘IDA=IDB∘f=f n n
- **Definition-2.23** (`[p. 89]` · *Visual Definition 23*): An operation is associative if given 3 sequential morphisms   ,combining  and  with it and then combining the end result with should be the same as combining  to the result of  and :). fghh g fh g f(h∘g)∘f=h∘(g∘f)
- **Definition-2.24** (`[p. 91]` · *Visual Definition 24*): A category is a collection of objects (we can think of them as points)and morphisms (arrows) that go from one object to another, where: 1. Each object has to have an identity morphism.2. There should be a way to compose two morphisms with anappropriate type signature into a third one, in a way that isassociative. DEFINITION: The product of  and , denoted , i
- **Definition-2.25** (`[p. 91]` · *Visual Definition 25*): The product of  and , denoted , is a set an object, suchthat: 1. There exists two “projection” functions morphisms  and.2. For any impostor product , that also has such projection functionsmorphisms (  and ), there must also exist a uniquefunction morphism with the type signature , thatconverts the impostor product to the real product, such that theabove two
