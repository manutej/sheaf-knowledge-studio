---
id: universal-colimits-and-cocones
title: "Universal Colimits, Cocones & Interconnected Gluing"
type: SheafStalk
chapter: 6
section: "6.1.3"
pdf_pages: "429–438"
symbol: "colim_{→ J} D"
layer: "Universal Constructions in Cat"
extracted_declarations: 15
restricts_to: [pushouts-and-colimits-set]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Universal Colimits, Cocones & Interconnected Gluing (`colim_{→ J} D`)

> **Sheaf Stalk Location:** Chapter 6 (Fundamental Considerations of Categories: Universal Limits, Colimits & Grothendieck Construction) · Section `6.1.3` · **PDF Pages 429–438**

## 1. Epistemic Worldview & Intuition

The dual of a limit: given a diagram D : J -> C, a cocone under D is a nadir object W receiving maps w_j : D(j) -> W commuting with all D(f). The colimit colim_J D is the initial cocone—the canonical quotient gluing all pieces D(j) along the shared transitions D(f).

## 2. Formal Categorical Core

Definition 6.1.3.17 (p. 429): A cocone (W, w_j) under D : J -> C satisfies w_k o D(f) = w_j for all f : j -> k in J. The colimit colim D is the initial object in Cocone(D). Example 6.1.3.21 (p. 436): Gluing two hemispheres D^2 along their boundary equator S^1 via a pushout in Top yields the 2-sphere S^2.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Dj]`** — *a local component D(j)*
- **`[Dk]`** — *an overlapping component D(k)*
- **`[Colim]`** — *the universal glued colimit colim D*
- **`[W]`** — *any compatible target cocone W*

### Functional Aspects (Morphisms)
- **`[Dj]` $\xrightarrow{\text{maps via glue instruction D(f) to}}$ `[Dk]`**
- **`[Dj]` $\xrightarrow{\text{injects via ι_j into}}$ `[Colim]`**
- **`[Dk]` $\xrightarrow{\text{injects via ι_k into}}$ `[Colim]`**
- **`[Colim]` $\xrightarrow{\text{induced uniquely via u : colim D -> W to}}$ `[W]`**

### Commutative Path Facts ($p \simeq q$)
- Cocone Commutativity: ι_k ∘ D(f) = ι_j.
- Figure 6.1 (p. 436): Topological pushout of two disks along a circle glues into a sphere.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-32` (generalizes_Set_colimits)** $\to$ [[pushouts-and-colimits-set]] (*Equivalence Relations, Pushouts & Gluing in Set*, p. 110–127): Cocones and universal colimits in Cat generalize coproducts, pushouts, and coequalizers in Set — `colim_J D |_Set = (⊔ D(j))/~`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 429–438)

### `Definition 6.1.3` — [PDF Page 429]
> Definition 6.1.3.20, and the category of relative sets over B? b. What is the limit of the functor B : 1 → Set?

### `Definition 6.1.3.31` — [PDF Page 430]
> Definition 6.1.3.31. Let C be a category, let I be a category; let I▻ be the right cone on I, and let i : I → I▻ be the inclusion. Suppose that X:I→C is an I-shaped diagram in C. The coslice category of C over X, denoted CX/, is the category whose objects and morphisms are as follows: Ob(CX/)={S:I⊳→C|S○i=X};HomCX/(S,S′)={α:S→S′|α⋄i=idX}. A colimit of X, denoted colimI X or colim X, is an initial object in CX/.

### `Theorem 6.1.3.28` — [PDF Page 429]
> Theorem 6.1.3.28. Let I be a category and let F : I → Set be a functor. Then its limit set limI F ∈ Ob(Set) exists and one can find its elements as follows. An element of the set limI F is given by choosing an element of xi ∈ F (i) for each object i ∈ Ob(I) such that, for each f : i → i′ one has F(f)(xi) = xi′. Proof. See [29].

### `Theorem 6.1.3.35` — [PDF Page 433]
> Theorem 6.1.3.35. Let I be a category and let F : I → Set be a functor. Then its colimit set colimI F ∈ Ob(Set) exists and one can find its elements as follows. An element of the set colimI F is given by choosing any i ∈ Ob(I) and any element of xi ∈ F(i), and then considering two such elements equivalent if there exists f : i → i′ such that X(f)(xi) = xi′. Proof. See [29].

### `Application 6.1.3.40` — [PDF Page 436]
> Application 6.1.3.40. Consider the symmetric graph Gn consisting of a chain of n vertices,

### `Example 6.1.3.38` (Cone as colimit) — [PDF Page 434]
> Example 6.1.3.38 (Cone as colimit). It turns out that Cat is cocomplete, meaning every diagram in C has a colimit. We give an example of a colimit in Cat. Let C be a category, and recall from Example 6.1.3.26 the category C×[1]. The inclusion of the front pane is a functor i0:C→C×[1]. (Similarly, the inclusion of the back pane is a functor i1:C→C×[1].) Finally, let t:C→1¯ be the unique functor to the terminal category (see Exercise 5.1.2.40). We now have a diagram in Cat of the form The colimit (i.e., the pushout) of this diagram in Cat slurps down the entire front pane of C×[1] to a point, and the resulting category is isomorphic to C◅. The 

### `Example 6.1.3.39` — [PDF Page 435]
> Example 6.1.3.39. Consider the category Top of topological spaces. The (unfilled)

### `Remark 6.1.3.32` — [PDF Page 430]
> Remark 6.1.3.32. Perhaps the following diagram will be helpful for understanding colimits. Given a functor X:I→C, what is its colimit? The solid-arrow part of the figure is the data we start with, i.e., the category C, the indexing category I, and the diagram X:I→C, as well as the part we automatically add, the cone I▻ with the inclusion I→iI⊳. The category CX/ is found in the dotted arrow part: its objects are the dotted arrows S:I⊳→C that make the following triangle commute, and its morphisms are the natural transformations α : S → S′ between them:

### `Remark 6.1.3.37` — [PDF Page 433]
> Remark 6.1.3.37. Definition 6.1.3.31 defined what it means to be a colimit in any category; however, in any particular category, some colimits may not exist. It is

### `Exercise 6.1.3.27` — [PDF Page 429]
> Exercise 6.1.3.27. Recall that Section 3.4.6.5 described relative sets. In fact, Definition 3.4.6.6 basically defines a category of relative sets over any fixed set B. Let B : 1 → Set be the functor representing the object B ∈ Ob(Set). a. What is the relationship between the slice category Set/B, as defined in

### `Exercise 6.1.3.29` — [PDF Page 429]
> Exercise 6.1.3.29. Let I be the category given by the following schema:

### `Exercise 6.1.3.33` — [PDF Page 432]
> Exercise 6.1.3.33. Let GrIn be the graph-indexing category (see (5.8)). a. What is GrIn▻? b. Let G : GrIn → Set be the graph from Example 4.3.1.2. Give an example of an object in SetG/.

### `Exercise 6.1.3.34` — [PDF Page 432]
> Exercise 6.1.3.34. Let C be a category, and let I = 0 be the empty category. There is a unique functor X:0¯→C. a. What is the coslice category CX/? b. What is a colimit of X (assuming it exists)?

### `Exercise 6.1.3.36` — [PDF Page 433]
> Exercise 6.1.3.36. Let I be the category given by the following schema: Let X : I → Set be given on objects by X(a) ≔ 2, X(b) ≔ 2, X(c) ≔ 4, X(d) = 3, and given (in sequence notation) on morphisms by X(f) = (1, 2), X(g) = (1, 2, 1), X(h) = (1, 2, 4). What is the colimit colimI X.

### `Solution 6.1.3.34` — [PDF Page 432]
> Solution 6.1.3.34. a. The right cone of 0 is the terminal category 0▻ ≅ 1, and since every diagram

## 6. Page-by-Page Deep Index (PDF Pages 429–438)
- **Page 429** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.3.27, Definition 6.1.3, Theorem 6.1.3.28, Exercise 6.1.3.29: It turns out that a natural transformation α : F → G between functors F,G:C→D is the same thing as a functor C×[1]→D such that the front pane is sent via F and the back pane is sent via G. The components are captured by the front-to-back morphisms, and the naturality is captured by the commutativity of the front-to-bac...
- **Page 430** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.3.31, Remark 6.1.3.32: Let X : I → Set be given on objects by X(a) ≔ 2, X(b) ≔ 1, X(c) ≔ 3, X(d) = 2, and given (in sequence notation) on morphisms by X(f) = (1, 1), X(g) = (1, 1, 1), X(h) = (1, 2, 1). What is the limit limI X. 6.1.3.30 Definition of colimit The definition of colimits is appropriately dual to the definition of limits. Instea...
- **Page 431** (`6.1 Limits and colimits`): The colimit of X is the initial object in this category. Pushouts The relevant indexing category for pushouts is the span, I = 2◅ drawn as on the left: An I-shaped diagram in C is a functor X:I→C, which might be drawn as on the right (e.g., X0∈Ob(C)). An object S in the coslice category CX/ is a commutative diagram S:I...
- **Page 432** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.3.33, Exercise 6.1.3.34, Solution 6.1.3.34: A morphism in CX/ is drawn as in right-hand box. An initial object in CX/ is precisely the gateway we want, i.e., the colimit of X is the pushout, X1⊔X0X2. Exercise 6.1.3.33. Let GrIn be the graph-indexing category (see (5.8)). a. What is GrIn▻? b. Let G : GrIn → Set be the graph from Example 4.3.1.2. Give an example o...
- **Page 433** (`6.1 Limits and colimits`) · **Items:** Theorem 6.1.3.35, Exercise 6.1.3.36, Remark 6.1.3.37: commutes, we have an isomorphism Fun(1¯,C)→≅CX/. But by (??), we have an isomorphism C→≅Fun(1¯,C), so in fact C≅CX/. b. A colimit of X is defined to be an initial object in CX/, which is an initial object in C, if it exists. In other words, initial objects in a category give us a canonical example of colimits. This was...
- **Page 434** (`6.1 Limits and colimits`) · **Items:** Example 6.1.3.38: like defining the quotient of any two natural numbers r, s ∈ ℕ by r ÷ s = q if and only if q∗s=r. We have defined what it means to be a quotient, but that doesn’t mean the quotient of any two numbers exists, e.g. if r = 7 and s = 2. The same goes for limits. A category C in which every diagram is guaranteed to have a l...
- **Page 435** (`6.1 Limits and colimits`) · **Items:** Example 6.1.3.39: The category C is shown in the upper left-hand corner of (6.7). The left cone C◅ on C is obtained as a pushout in Cat. We first make a prism C×[1] and then identify the front pane with a point. (Similarly, the pushout of an analogous diagram for i1 would give C▻.) Example 6.1.3.39. Consider the category Top of topologi...
- **Page 436** (`6.1 Limits and colimits`) · **Items:** Application 6.1.3.40, Figure 6.1: circle is a topological space, which people often denote by S1 (for one-dimensional sphere). Topologically, it is equivalent to an oval, as shown in Figure 6.1. The filled-in circle, also called a two-dimensional disk, is denoted D2. The inclusion of the circle into the disk, as its boundary, is continuous, so we have ...
- **Page 437** (`6.1 Limits and colimits`): Think of this as modeling a subway line. There are n-many graph homomorphisms G1 → Gn given by the various vertices. One can create transit maps using colimits. For example, the colimit of the left-hand diagram is the symmetric graph drawn at the right:...
- **Page 438** (`6.1 Limits and colimits`): ...
