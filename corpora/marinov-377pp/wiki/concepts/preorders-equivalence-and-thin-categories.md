# Preorders, Equivalence Relations & Thin Categories (`U_12`)

- **Chapter:** 4 (`§4.3`)
- **Page Fiber:** `pp. 153–161`
- **Layer:** Order & Hierarchy

## Summary

Dropping antisymmetry yields preorders (reflexive + transitive), which are literally Thin Categories (at most one arrow between any two objects). Adding symmetry yields equivalence relations (thin groupoids).

## Formal Categorical Core

$$\mathbf{Preord} \simeq \mathbf{Cat}_{\mathrm{thin}} = \{ \mathcal{C} \in \mathbf{Cat} \mid \forall a,b,\; |\mathrm{Hom}_{\mathcal{C}}(a,b)| \le 1 \}$$

## Local Olog (`types` & `aspects`)

- **Type `preorder`:** Preorder (P, ≲) (Refl + Trans)
- **Type `thinCat`:** Thin Category (|Hom(a,b)| ≤ 1)
- **Type `equivRel`:** Equivalence Relation (Thin Groupoid)
- **Aspect:** `preorder` —*is identical in structure to*→ `thinCat`
- **Aspect:** `equivRel` —*adds symmetry (invertible arrows) to*→ `preorder`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-21` → [propositional-logic-as-category](propositional-logic-as-category.md):** Propositional entailment P ⊢ Q forms a preorder / thin category of deductions (`$\rho_{21}: (a \le b) \mapsto (P \vdash Q)$`)
- **Outgoing `rho-40` → [functors-across-monoids-orders-logic](functors-across-monoids-orders-logic.md):** Functors between thin categories are monotone order-preserving maps (`$\rho_{40}: \mathrm{Fun}(P, Q) \cong \mathrm{Monotone}(P, Q)$`)
- **Incoming `rho-16` ← [orders-hasse-diagrams-and-lattices](orders-hasse-diagrams-and-lattices.md):** Viewing order relations a ≤ b as unique morphisms a → b in a thin category (`$\rho_{16}: (a \le b) \mapsto \mathrm{Hom}_{P}(a,b) = \{*\}$`)
- **Incoming `rho-17` ← [birkhoff-representation-and-boolean-lattices](birkhoff-representation-and-boolean-lattices.md):** Lattice meets ∧ and joins ∨ are categorical products and coproducts in a thin category (`$\rho_{17}: (a \wedge b, a \vee b) \mapsto (a \times_P b, a +_P b)$`)
- **Incoming `rho-18` ← [categories-objects-morphisms-laws](categories-objects-morphisms-laws.md):** Truncating hom-sets to at most one arrow |Hom(a,b)| ≤ 1 yields Preorders (`$\rho_{18}: \mathcal{C}_{|\mathrm{Hom}|\le 1} \simeq \mathbf{Preord}$`)
- **Incoming `rho-19` ← [external-products-and-projections](external-products-and-projections.md):** Universal product cone in a thin category collapses to greatest lower bound (meet ∧) (`$\rho_{19}: A \times B \mapsto a \wedge b$`)
- **Incoming `rho-20` ← [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Universal coproduct cocone in a thin category collapses to least upper bound (join ∨) (`$\rho_{20}: A + B \mapsto a \vee b$`)

## Extracted Definitions, Theorems & Tasks (7)

- **Definition-4.39** (`[p. 153]` · *a≤b b≤a a≤b b≤a a≤b b≤a*): An preorder is a set of elements, together with a binary relationbetween the elements of the set, that obeys the laws of reflexivityand transitivity.
- **Definition-4.40** (`[p. 157]` · *Visual Definition 40*): A category is a collection of objects (we can think of them as points)and morphisms (arrows) that go from one object to another, where: 1. Each object has to have the identity morphism.2. There should be a way to compose two morphisms with anappropriate type signature into a third one in a way that isassociative.
- **Task-4.29** (`[p. 158]` · *Interactive Task 6 (Preorders as categories)*): Prove this. Partial orders and total orders as categories A≤B DEFINITION:
- **Definition-4.41** (`[p. 158]` · *A≤B*): A preorder, any preorder, can be seen as a category with at most onemorphism between two given objects— for any  and , we say that if then a morphism  exists. The identity morphism existbecause of reflexivity. The converse is also true: any category with nomore than one morphism between two objects can be seen as apreorder. A BA≤B A→B
- **Definition-4.42** (`[p. 160]` · *Visual Definition 42*): The coproduct of  and , denoted , is an object, such that: 1. There exists two “projection” morphisms  and.2. For any impostor coproduct , that also has such projectionmorphisms (  and ), there must also exist a uniquemorphism with the type signature , that convertsthe real coproduct to the impostor, such that the projections ofthe impostor would be just the
- **Definition-4.43** (`[p. 160]` · *g*): The join of objects  and  is an object , such that: 1. It is bigger than both of these objects, so  and .2. It is smaller than any other object that is bigger than them, so forany other object  such that  and  then we shouldalso have . A B G A≤G B≤G
- **Theorem-4.21** (`[p. 161]` · *Visual Theorem 21*): The categorical coproduct in the category of preorders is the joinoperation.
