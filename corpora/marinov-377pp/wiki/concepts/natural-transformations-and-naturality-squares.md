# Natural Transformations α : F ⇒ G & Naturality Squares (`U_22`)

- **Chapter:** 8 (`§8.1`)
- **Page Fiber:** `pp. 319–341`
- **Layer:** Higher 2-Categorical Synthesis

## Summary

Saunders Mac Lane's motivation for category theory: a natural transformation α : F ⇒ G is a family of component morphisms α_A : F(A) → G(A) indexed by objects A ∈ C such that every morphism f : A → B induces a commuting naturality square.

## Formal Categorical Core

$$\alpha : F \Rightarrow G \iff \forall (A \xrightarrow{f} B) \in \mathcal{C}, \quad G(f) \circ \alpha_A = \alpha_B \circ F(f)$$

## Local Olog (`types` & `aspects`)

- **Type `functorPair`:** Parallel Functors F, G : C → D
- **Type `compAlpha`:** Component Family α_A : F(A) → G(A)
- **Type `natSquare`:** Commuting Naturality Square G(f) ∘ α_A = α_B ∘ F(f)
- **Aspect:** `compAlpha` —*bridges object images between*→ `functorPair`
- **Aspect:** `compAlpha` —*must commute for every arrow f in*→ `natSquare`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-46` → [polymorphic-functions-and-categorical-equivalence](polymorphic-functions-and-categorical-equivalence.md):** Polymorphic functions ∀a. F a → G a are natural transformations; invertible ones yield equivalence (`$\rho_{46}: \mathrm{Nat}(F, G) \cong \forall a.\; F\;a \to G\;a$`)
- **Outgoing `rho-48` → [functor-categories-vertical-horizontal-2-categories](functor-categories-vertical-horizontal-2-categories.md):** Composing natural transformations vertically and horizontally inside the 2-category Cat (`$\rho_{48}: (\mathcal{C}, F, \alpha) \in \mathbf{2Cat}$`)
- **Incoming `rho-44` ← [functors-structure-preserving-maps](functors-structure-preserving-maps.md):** Natural transformations α : F ⇒ G are morphisms between parallel functors F, G : C → D (`$\rho_{44}: (F, G) \mapsto \mathrm{Nat}(F, G)$`)
- **Incoming `rho-45` ← [programming-endofunctors-pointed-contravariant](programming-endofunctors-pointed-contravariant.md):** Transforming container endofunctors F A → G A while commuting with .map(f) (`$\rho_{45}: \mathrm{map}_G(f) \circ \alpha_A = \alpha_B \circ \mathrm{map}_F(f)$`)

## Extracted Definitions, Theorems & Tasks (13)

- **Definition-8.151** (`[p. 321]` · *Categorical isomorphisms are not isomorphism-invariant*): A property is called isomorphism-invariant when if there are two ormore objects that are isomorphic to one another, and one of them hasa given property, then the rest of them would to also have thisproperty as well.
- **Definition-8.152** (`[p. 326]` · *Visual Definition 152*): Two preorders are equivalent precisely when the preorders made oftheir equivalence classes are isomorphic.
- **Definition-8.153** (`[p. 327]` · *Visual Definition 153*): An order isomorphism is essentially an isomorphism between the orders’underlying sets (invertible function). However, besides their underlyingsets, orders also have the arrows that connect them, so there is onemore condition: in order for an invertible function to constitute anorder isomorphism it has to respect those arrows, in other words itshould be order
- **Task-8.71** (`[p. 328]` · *Interactive Task 1 (We begin with the definition of set isomorphism:)*): Check if that definition is valid. Believe it or not, this definition, is just one find-and-replace operation awayfrom the definition of equivalence. We get there only by replace equality withisomorphism (so,  with ). DEFINITION: Two sets  and  are isomorphic (or ) if there exist functions and its reverse , such that  and.
- **Definition-8.154** (`[p. 328]` · *Visual Definition 154*): Two sets  and  are isomorphic (or ) if there exist functions and its reverse , such that  and. A B A≅Bf:A→B g:B→A f∘g=IDBg∘f=IDA DEFINITION: Two categories  and  are isomorphic (or ) if there existfunctors  and its reverse , such that and .
- **Definition-8.155** (`[p. 328]` · *A B A≅Bf:A→B g:B→A f∘g=IDBg∘f=IDA*): Two categories  and  are isomorphic (or ) if there existfunctors  and its reverse , such that and . A B A≅Bf:A→B g:B→Af∘g=IDB g∘f=IDA = ≅ DEFINITION:
- **Definition-8.156** (`[p. 328]` · *= ≅*): Two categories  and  are equivalent (or ) if there existfunctors  and its reverse , such that and . A B A≃Bf:A→B g:B→Af∘g≅IDB g∘f≅IDA
- **Task-8.72** (`[p. 331]` · *Interactive Task 2 (We begin with the definition of set isomorphism:)*): When exactly would the mapping encompass all objects? Morphism mapping mapping The morphism part might seem hard… until we realize that, once theconnections between the object mappings are already established, there is onlyone way to connect the morphisms — we take each morphism of the sourcecategory and connect the two morphisms given by the two functors, i
- **Definition-8.157** (`[p. 332]` · *Visual Definition 157*): Let  and  be two functors that have the same type signature (so and  for some categories  and ). Atransformation between them is a family of morphisms in the targetcategory  (denoted ) one for each object in , that mapeach object of the target of the functor  (or the image of  in  asit is also called) to some objects of the image of . F GF:C→D G:C→D C D D α:
- **Definition-8.158** (`[p. 332]` · *D α:F⇒G CF F DG*): A transformation is natural when every morphism  in  is mapped tomorphisms  by  and to  by  in such a way, that we have i.e. when this diagram commutes. f CF(f) F G(f) Gα∘F(f)=G(f)∘α
- **Definition-8.159** (`[p. 335]` · *Visual Definition 159*): Two categories  and  are equivalent (or ) if there existfunctors  and its reverse , such that and . A B A≃Bf:A→B g:B→Af∘g≅IDA g∘f≅IDB
- **Definition-8.160** (`[p. 340]` · *Visual Definition 160*): Two functors  and  that have the same type signature (so and  for some categories  and ), and afamily of morphisms in the target category  (denoted )one for each object in . Morphisms that map each object of thetarget of  (or the image of  in  as it is also called) to someobject in the target of . F GF:C→D G:C→D C DD α:F⇒GCF F DG Set DEFINITION:
- **Definition-8.161** (`[p. 340]` · *Set*): Two functors generic types  and  that have the same typesignature and a family of morphisms in  (denoted )one for each object in , that map each target object of the functor (or the image of  in  as it is also called) to some target objectsof functor . F GSet α:Set⇒SetSetF F DG Set SetSet a alpha:∀a.Fa→Ga
