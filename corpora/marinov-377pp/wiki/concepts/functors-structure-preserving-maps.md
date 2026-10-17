# Functors F : C → D — Structure-Preserving Maps Between Categories (`U_19`)

- **Chapter:** 7 (`§7.1`)
- **Page Fiber:** `pp. 278–295`
- **Layer:** Functorial Bridges

## Summary

Generalizing order-embeddings and group homomorphisms to arbitrary categories: a functor F : C → D maps objects to objects and morphisms to morphisms while preserving identities and composition triangles.

## Formal Categorical Core

$$F : \mathcal{C} \to \mathcal{D}, \quad F(\mathrm{id}_A) = \mathrm{id}_{F(A)}, \quad F(g \circ f) = F(g) \circ F(f)$$

## Local Olog (`types` & `aspects`)

- **Type `srcCat`:** Source Category C
- **Type `dstCat`:** Target Category D
- **Type `funcF`:** Functor F = (F_Ob, F_Hom)
- **Aspect:** `funcF` —*reads commutative triangles in*→ `srcCat`
- **Aspect:** `funcF` —*reconstructs commuting images in*→ `dstCat`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-38` → [functors-across-monoids-orders-logic](functors-across-monoids-orders-logic.md):** Specializing F : C → D to 1-object categories (monoids) and thin categories (posets) (`$\rho_{38}: F \mapsto (f_{\mathrm{mon}}, f_{\mathrm{poset}})$`)
- **Outgoing `rho-41` → [programming-endofunctors-pointed-contravariant](programming-endofunctors-pointed-contravariant.md):** Endofunctors F : Type → Type on the category of programming types (`$\rho_{41}: F : \mathbf{Type} \to \mathbf{Type}$`)
- **Outgoing `rho-44` → [natural-transformations-and-naturality-squares](natural-transformations-and-naturality-squares.md):** Natural transformations α : F ⇒ G are morphisms between parallel functors F, G : C → D (`$\rho_{44}: (F, G) \mapsto \mathrm{Nat}(F, G)$`)
- **Outgoing `rho-50` → [functor-categories-vertical-horizontal-2-categories](functor-categories-vertical-horizontal-2-categories.md):** Functors C → D become the objects of the functor category [C, D] (`$\rho_{50}: \mathrm{Ob}([\mathcal{C}, \mathcal{D}]) = \mathrm{Fun}(\mathcal{C}, \mathcal{D})$`)
- **Incoming `rho-37` ← [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Functors F : C → D are homomorphisms preserving categorical composition and identities (`$\rho_{37}: (\mathcal{C}, \mathcal{D}) \mapsto \mathrm{Fun}(\mathcal{C}, \mathcal{D})$`)

## Extracted Definitions, Theorems & Tasks (11)

- **Task-7.53** (`[p. 281]` · *Interactive Task 1 (Functors)*): There are just two more categories that have 2 objects and at most onemorphism between two objects, draw them. 2
- **Definition-7.135** (`[p. 283]` · *Visual Definition 135*): Two sets  and  are isomorphic (or ) if there exist functions and its reverse , such that  and. A B A≅Bf:A→B g:B→A f∘g=IDAg∘f=IDB DEFINITION: An isomorphism between two orders is an invertible function betweentheir underlying sets, such that applying this function (let’s call it )to any two elements that have a certain order in one set (let’s callthem  and ) 
- **Definition-7.136** (`[p. 283]` · *A B A≅Bf:A→B g:B→A f∘g=IDAg∘f=IDB*): An isomorphism between two orders is an invertible function betweentheir underlying sets, such that applying this function (let’s call it )to any two elements that have a certain order in one set (let’s callthem  and ) should result in two elements that have a correspondingorder in the other set (i.e.  if and only if ). F a b a≤b F(a)≤F(b)
- **Definition-7.137** (`[p. 284]` · *Visual Definition 137*): Given two categories, an isomorphism between them is an invertiblemapping between the underlying sets of objects, and an invertiblemapping between the morphisms that connect them, which maps eachmorphism from one category to a morphism with the same signature.
- **Task-7.54** (`[p. 285]` · *Interactive Task 2 (Categorical isomorphisms)*): What is the morphism mapping for orders? However, when we can have more than one morphism between two givenobjects, we need to make sure that each morphism in the source category has acorresponding morphism in the target one, and for this reason we need notonly a mapping between the categories’ objects, but one between theirmorphisms. By the way, what we jus
- **Definition-7.138** (`[p. 286]` · *xx*): chapter, where we will also devise a more apt way to define a two-wayconnection between categories.
But first, we need to examine one-way connections between them, i.e.functors.
PS: Categorical isomorphisms are also very rare in practice — the only one thatcomes to mind is the Curry-Howard-Lambek is
- **Definition-7.139** (`[p. 288]` · *A AA*): A function is a relationship between two sets that matches eachelement of one set, called the source set of the function, with exactlyone element from another set, called the target set of the function. A B
- **Definition-7.140** (`[p. 289]` · *So this definition translates to the following two functor laws*): A category is a collection of objects (we can think of them as points)and morphisms (arrows) that go from one object to another, where: 1. Each object has to have the identity morphism.2. There should be a way to compose two morphisms with anappropriate type signature into a third one, in a way that isassociative. DEFINITION: A functor between two categories
- **Definition-7.141** (`[p. 289]` · *Visual Definition 141*): A functor between two categories (let’s call them  and ) consists oftwo mappings — a mapping that maps each object in  to an object in and a mapping that maps each morphism between any objects in to a morphism between objects in , in a way that preserves thestructure of the category: A BAB AB
- **Definition-7.142** (`[p. 291]` · *aFa b Fba→bFa→Fb*): The composition of two functions  and  is a third function  definedin such a way that this diagram commutes.f g h
- **Definition-7.143** (`[p. 293]` · *Visual Definition 143*): A diagram is comprised of one finite category (called an indexcategory) and a functor from it to some other category.
