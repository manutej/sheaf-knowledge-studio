# Groups, Geometric Rotations (C₃, D₃) & Invertible Symmetries (`U_08`)

- **Chapter:** 3 (`§3.2`)
- **Page Fiber:** `pp. 104–114`
- **Layer:** Algebraic Symmetries

## Summary

Adding inverses turns a monoid into a group (G, ⋆, e, inv): rotational symmetries of an equilateral triangle (0°, 120°, 240° = C₃), reflections (D₃), cyclic groups Z_n, and product groups.

## Formal Categorical Core

$$\forall g \in G, \; \exists g^{-1} \in G \text{ s.t. } g \star g^{-1} = e = g^{-1} \star g$$

## Local Olog (`types` & `aspects`)

- **Type `triangle`:** Geometric Figure (Equilateral Triangle)
- **Type `rotGroup`:** Rotation Group C₃ = {0°, 120°, 240°}
- **Type `invLaw`:** Inverse Symmetry g⁻¹
- **Aspect:** `rotGroup` —*acts by symmetries on*→ `triangle`
- **Aspect:** `rotGroup` —*guarantees every action has*→ `invLaw`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-11` → [monoids-as-single-object-categories-free-monoids](monoids-as-single-object-categories-free-monoids.md):** Groups are single-object categories (groupoids) where every arrow is an isomorphism (`$\rho_{11}: G \mapsto \mathbf{B}G$`)
- **Incoming `rho-10` ← [monoids-semigroups-magmas](monoids-semigroups-magmas.md):** Equipping every monoid element with a two-sided inverse g⁻¹ yields a Group (`$\rho_{10}: (M, \star, e) \hookrightarrow (G, \star, e, (-)^{-1})$`)

## Extracted Definitions, Theorems & Tasks (8)

- **Definition-3.28** (`[p. 106]` · *Visual Definition 28*): Groups and monoids that have an object that is capable of generatingall other objects by its repeated application, are called cyclic groups.The group’s “main” object is called the generator. +1 +1 −1 12
- **Task-3.18** (`[p. 107]` · *Interactive Task 6 (Groups of rotations)*): Show that there are no other groups with 3 objects, other than . 1(mod12)=1 1/12=0 12(mod12)=2 13(mod12)=1 13/12=1 1 14(mod12)=215(mod12)=3 3
- **Definition-3.29** (`[p. 108]` · *Visual Definition 29*): An isomorphism between two groups is an isomorphism ( ) betweentheir respective sets of elements, such that for any  and  we have. fa bf(a∘b)=f(a)∘f(b) Z3 Z1
- **Definition-3.30** (`[p. 109]` · *Z3Z1 Z2*): Given any two groups, we can combine them to create a third group,comprised of all possible pairs of elements from the two groups and ofthe sum of all their actions.
- **Task-3.19** (`[p. 111]` · *Interactive Task 7 (VV)*): Show that the two representations are isomorphic. Here are some examples of how elements of the Klein four-group are combined. (i.e. horizontal/vertical rotations cancel each other out, while a horizontalrotation doesn’t cancel out a vertical one.)
- **Theorem-3.15** (`[p. 113]` · *Visual Theorem 15*): All finite commutative groups are either cyclic or products of cyclicgroups.
- **Task-3.20** (`[p. 114]` · *Interactive Task 8 (Commutative product groups)*): Prove that this group is indeed not commutative. Task 9: Besides having two main actions, what is the defining factor thatmakes this and any other group non-commutative? Groups that represent the set of rotations and reflections of any 2D shape arecalled dihedral groups. Groups/monoids as categories
- **Task-3.21** (`[p. 114]` · *Interactive Task 9 (Commutative product groups)*): Besides having two main actions, what is the defining factor thatmakes this and any other group non-commutative? Groups that represent the set of rotations and reflections of any 2D shape arecalled dihedral groups. Groups/monoids as categories Now it’s the place for the grand reveal — groups/monoids are categories. Moreprecisely, monoids are a specific type 
