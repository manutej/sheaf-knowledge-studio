---
id: groups-and-symmetries
title: "Groups, Invertible Symmetries & Orbit Quotients"
type: SheafStalk
chapter: 4
section: "4.2"
pdf_pages: "192–200"
symbol: "G ↷ X → X/G"
layer: "Pre-Categorical Models"
extracted_declarations: 20
restricts_to: [monoids-and-actions, pushouts-and-colimits-set]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Groups, Invertible Symmetries & Orbit Quotients (`G ↷ X → X/G`)

> **Sheaf Stalk Location:** Chapter 4 (Categories and Functors, Without Admitting It: Monoids, Groups, Graphs, Orders & Databases) · Section `4.2` · **PDF Pages 192–200**

## 1. Epistemic Worldview & Intuition

A group is a monoid in which every element has a two-sided inverse—equivalent to a 1-object groupoid. Group actions model reversible transformations and physical/geometric symmetries; their orbits partition the state space into symmetry equivalence classes X/G.

## 2. Formal Categorical Core

A group (G, e, *, (-)^-1) satisfies g * g^-1 = e = g^-1 * g (Def 4.2.1.1, p. 194). Given a group action G × X -> X, the relation x ~ g.x is an equivalence relation whose quotient X/G is the set of orbits (colimit of the action functor).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *a configuration x in state space X*
- **`[G]`** — *a reversible symmetry transformation g in G*
- **`[XG]`** — *a conserved orbit equivalence class [x] in X/G*

### Functional Aspects (Morphisms)
- **`[X]` $\xrightarrow{\text{transforms reversibly under g to}}$ `[X]`**
- **`[X]` $\xrightarrow{\text{quotients to symmetry invariant in}}$ `[XG]`**

### Commutative Path Facts ($p \simeq q$)
- Every group element g : X -> X is an isomorphism in Set with inverse g⁻¹.
- Connects directly to Noetherian quotient collapse π : X -> X/G.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-14` (invertible_specialization)** $\to$ [[monoids-and-actions]] (*Monoids, Agent Actions & Finite State Machines*, p. 160–191): Every group is a monoid whose elements all possess two-sided inverses — `Grp ↪ Mon`
- **`rho-15` (orbit_quotient)** $\to$ [[pushouts-and-colimits-set]] (*Equivalence Relations, Pushouts & Gluing in Set*, p. 110–127): Group action orbits X/G are the coequalizer / colimit equivalence classes x ~ g·x — `X ↠ X/G`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 192–200)

### `Definition 4.2.1.1` — [PDF Page 194]
> Definition 4.2.1.1. Let (M, e, ⋆) be a monoid. An element m ∈ M is said to have an inverse if there exists an m′ ∈ M such that mm′ = e and m′m = e. A group is a monoid (M, e, ⋆) in which every element m ∈ M has an inverse.

### `Definition 4.2.1.9` (Group action) — [PDF Page 197]
> Definition 4.2.1.9 (Group action). Let (G, e, ⋆) be a group and S a set. An action of G on S is a function : G × S → S such that for all s ∈ S and g, g′ ∈ G, we have e s = s; g (g′ s) = (g ⋆ g′) s. In other words, considering G as a monoid, it is an action in the sense of

### `Definition 4.1.2.1` — [PDF Page 197]
> Definition 4.1.2.1.

### `Definition 4.2.1.12` — [PDF Page 198]
> Definition 4.2.1.12. Let G be a group acting on a set X. For any point x ∈ X, the orbit of x, denoted Gx, is the set Gx≔{ x′∈X|∃g∈G such that gx=x′ }.

### `Definition 4.2.1.16` — [PDF Page 199]
> Definition 4.2.1.16. Let G and G′ be groups. A group homomorphism f : G → G′ is defined to be a monoid homomorphism G → G′, where G and G′ are being regarded as monoids in accordance with Definition 4.2.1.1.

### `Proposition 4.2.1.2` — [PDF Page 194]
> Proposition 4.2.1.2. Suppose that M≔(M,e,⋆) is a monoid, and let m ∈ M be an element. Then m has at most one inverse.5 Proof. Suppose that both m′ and m″ are inverses of m; we want to show that m′ = m″. This follows by the associative law for monoids: m′=m′(mm″)=(m′m)m″=m″.

### `Application 4.2.1.6` — [PDF Page 194]
> Application 4.2.1.6. In crystallography one is often concerned with the symmetries that arise in the arrangement A of atoms in a molecule. To think about symmetries in terms of groups, we first define an atom arrangement to be a finite

### `Application 4.2.1.13` — [PDF Page 198]
> Application 4.2.1.13. Let S be the surface of the earth, understood as a sphere, and let G = U(1) be the group of angles acting on S by rotation as in Example 4.2.1.10. The orbit of any point p = (x, y, z) ∈ S is the set of points on the same latitude line as p. One may also consider a small band around the earth, i.e., the set A = {(x, y,

### `Example 4.2.1.3` — [PDF Page 194]
> Example 4.2.1.3. The additive monoid (ℕ, 0, +) is not a group because none of its elements are invertible, except for 0. However, the monoid of integers (ℤ, 0, +) is a group. The monoid of clock positions from Example 4.1.1.26 is also a group. For example, the inverse of Q5 is Q7 because Q5 ⋆ Q7 = e = Q7 ⋆ Q5.

### `Example 4.2.1.4` — [PDF Page 194]
> Example 4.2.1.4. Consider a square centered at the origin in ℝ2. It has rotational and mirror symmetries. There are eight of these, denoted { e,ρ,ρ2,ρ3,ϕ,ϕρ,ϕρ2,ϕρ3 }, where ρ stands for 90° counterclockwise rotation and ϕ stands for horizontal flip (across the vertical axis). So relations include ρ4 = e, ϕ2 = e, and ρ3ϕ = ϕρ. This group is called the dihedral group of order eight.

### `Example 4.2.1.5` — [PDF Page 194]
> Example 4.2.1.5. The set of 3 × 3 matrices can be given the structure of a monoid, where the unit element is the 3 × 3 identity matrix, the multiplication formula is given by matrix multiplication. It is a monoid but not a group because not all matrices are invertible. The subset of invertible matrices does form a group, called the general linear group of degree 3 and denoted GL3. Inside of GL3 is the orthogonal group, denoted O3, of matrices M such that M−1 = M⊤. These matrices correspond to symmetries of the two-dimensional sphere centered at the origin in ℝ2. Another interesting group is the Euclidean group E(3), which consists of all isom

### `Example 4.2.1.10` — [PDF Page 197]
> Example 4.2.1.10. When a group acts on a set, it has the character of symmetry. For example, consider the group whose elements are angles θ. This group may be denoted U(1) and is often formalized as the unit circle in ℂ, i.e., the set of complex numbers z = a + bi such that |z| = a2 + b2 = 1. The set of such points is given the structure of a group (U(1), 1 + 0i, ⋆) by defining the unit element to be 1 + 0i and the group law to be complex multiplication. But for those unfamiliar with complex numbers, this is simply angle addition, where we understand that 360° = 0°. If θ1 = 190° and θ2 = 278°, then θ1 ⋆ θ2 = 468° = 108°. In the language of co

### `Exercise 4.2.1.7` — [PDF Page 195]
> Exercise 4.2.1.7. Let X be a finite set. A permutation of X is an isomorphism f:X→≅X. Let Iso(X) ≔ {f : X → X | f is an isomorphism} be the set of permutations of X. Here is a picture of an element in Iso(S), where S = {s1, s2, s3, s4}:

### `Exercise 4.2.1.8` — [PDF Page 196]
> Exercise 4.2.1.8. In Exercise 4.1.1.28 you classified the cyclic monoids. Which of them are groups?

### `Exercise 4.2.1.11` — [PDF Page 198]
> Exercise 4.2.1.11. Let X be a set and consider the group Iso(X) of permutations of X (see

### `Exercise 4.2.1` — [PDF Page 198]
> Exercise 4.2.1.7). Find a canonical action of IsoX on X.

### `Exercise 4.2.1.14` — [PDF Page 199]
> Exercise 4.2.1.14. a. Consider the U(1) action on the sphere S given in Example 4.2.1.10. Describe the set of orbits of this action. b. What are the orbits of the canonical action of the permutation group Iso{1,2,3} on the set {1, 2, 3}? (See Exercise 4.2.1.11.)

### `Exercise 4.2.1.15` — [PDF Page 199]
> Exercise 4.2.1.15. Let (G, e, ⋆) be a group and X a set on which G acts. Is “being in the same orbit” an equivalence relation on X?

## 6. Page-by-Page Deep Index (PDF Pages 192–200)
- **Page 192** (`4.2 Groups`): 4.2 Groups Groups are monoids with the property that every element has an inverse. If we think of these structures in terms of how they act on sets, the difference between groups and monoids is that the action of every group element can be undone. One way of thinking about groups is in terms of symmetries. For example,...
- **Page 193** (`4.2 Groups`): ...
- **Page 194** (`4.2 Groups`) · **Items:** Definition 4.2.1.1, Proposition 4.2.1.2, Example 4.2.1.3, Example 4.2.1.4, Example 4.2.1.5, Application 4.2.1.6: 4.2.1 Definition and examples Definition 4.2.1.1. Let (M, e, ⋆) be a monoid. An element m ∈ M is said to have an inverse if there exists an m′ ∈ M such that mm′ = e and m′m = e. A group is a monoid (M, e, ⋆) in which every element m ∈ M has an inverse. Proposition 4.2.1.2. Suppose that M≔(M,e,⋆) is a monoid, and let m ...
- **Page 195** (`4.2 Groups`) · **Items:** Exercise 4.2.1.7: subset i: A ⊆ ℝ3. A symmetry in this case is an isometry of ℝ3 (see Example 4.2.1.5), say, f : ℝ3 → ℝ3, such that there exists a dotted arrow making the following diagram commute: That is, it is an isometry of ℝ3 such that each atom of A is sent to a position currently occupied by an atom of A. It is not hard to show t...
- **Page 196** (`4.2 Groups`) · **Items:** Solution 4.2.1.7, Exercise 4.2.1.8: a. Devise a unit and a multiplication formula, such that the set Iso(X) of permutations of X forms a monoid. b. Is the monoid Iso(X) always in fact a group? Solution 4.2.1.7. a. We can take the unit to be the identity function idS:S→≅S and the multiplication formula to be a composition of isomorphisms f ⋆ g = f ○ g. Cl...
- **Page 197** (`4.2 Groups`) · **Items:** Definition 4.2.1.9, Definition 4.1.2.1, Example 4.2.1.10: Definition 4.2.1.9 (Group action). Let (G, e, ⋆) be a group and S a set. An action of G on S is a function : G × S → S such that for all s ∈ S and g, g′ ∈ G, we have e s = s; g (g′ s) = (g ⋆ g′) s. In other words, considering G as a monoid, it is an action in the sense of Definition 4.1.2.1. Example 4.2.1.10. When a gr...
- **Page 198** (`4.2 Groups`) · **Items:** Exercise 4.2.1.11, Exercise 4.2.1, Solution 4.2.1.11, Definition 4.2.1.12, Application 4.2.1.13: ℝ3 θ = 45° θ = 90° θ = 100° ⋯ (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) ⋯ (1, 0, 0) (0.71, 0.71, 0) (0, 1, 0) (−0.17, 0.98, 0) ⋯ (0, 1, −4.2) (−0.71, 0.71, −4.2) (−1, 0, −4.2) (−0.98, −0.17, −4.2) ⋯ (3, 4, 2) (4.95, 0.71, 2) (−4, 3, 2) (3.42, −3.65, 2) ⋯ ⋮ ⋮ ⋮ ⋮ ⋱ Since S ⊆ ℝ3 consists of all vectors of length 1, we need...
- **Page 199** (`4.2 Groups`) · **Items:** Exercise 4.2.1.14, Exercise 4.2.1.15, Definition 4.2.1.16: z) | 1.0 x2 + y2 + z2 1.05}. The action of U(1) S extends to an action U(1) A. The orbits are latitude-lines-at-altitude. A simplifying assumption in climatology may be given by assuming that U(1) acts on all currents in the atmosphere in an appropriate sense. Thus, instead of considering movement within the whole spac...
- **Page 200** (`4.2 Groups`): ...
