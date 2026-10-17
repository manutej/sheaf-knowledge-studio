---
id: sheaves-and-local-to-global-gluing
title: "Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom"
type: SheafStalk
chapter: 7
section: "7.2.3.1–7.2.3.10"
pdf_pages: "518–522"
symbol: "O : Open(X)^op → Set"
layer: "Sheaf & Topos Layer"
extracted_declarations: 10
restricts_to: [presheaves-representables-yoneda, orders-lattices-hierarchies, pullbacks-and-fiber-products, universal-limits-and-cones]
glues_with: [sheaf-of-ologged-concepts-descent]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom (`O : Open(X)^op → Set`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.2.3.1–7.2.3.10` · **PDF Pages 518–522**

## 1. Epistemic Worldview & Intuition

A presheaf O : Open(X)^op -> Set assigns to each open region U <= X a set O(U) of valid local sections ('value assignments throughout U') and to each inclusion U' <= U a restriction map rho_{U',U} : O(U) -> O(U') (written a |-> a|_{U'}). A presheaf is a SHEAF if for every open cover U = union_i V_i, any family of local sections a_i in O(V_i) that agree on all pairwise overlaps (a_i|_{V_i n V_j} = a_j|_{V_i n V_j}) glues uniquely into a single global section b in O(U) with b|_{V_i} = a_i.

## 2. Formal Categorical Core

Presheaf (Def 7.2.3.2, p. 519): A functor O : Open(X)^op -> Set. Sheaf Condition (Def 7.2.3.5, p. 520–521): Given an open cover U = union_{i=1}^n V_i and local sections a_i in O(V_i) such that rho_{V_i n V_j, V_i}(a_i) = rho_{V_i n V_j, V_j}(a_j) for all i, j, there exists a unique b in O(U) such that rho_{V_i, U}(b) = a_i for all i. Equivalently, O(U) -> prod_i O(V_i) ==> prod_{i,j} O(V_i n V_j) is an equalizer diagram in Set.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Global]`** — *a global section b in O(U) over U = V₁ ∪ V₂*
- **`[Loc1]`** — *a local section a₁ in O(V₁) over open set V₁*
- **`[Loc2]`** — *a local section a₂ in O(V₂) over open set V₂*
- **`[Ov]`** — *an overlap restriction s in O(V₁ ∩ V₂)*

### Functional Aspects (Morphisms)
- **`[Global]` $\xrightarrow{\text{restricts via ρ_{V₁,U} to}}$ `[Loc1]`**
- **`[Global]` $\xrightarrow{\text{restricts via ρ_{V₂,U} to}}$ `[Loc2]`**
- **`[Loc1]` $\xrightarrow{\text{restricts on overlap via ρ_{V₁∩V₂,V₁} to}}$ `[Ov]`**
- **`[Loc2]` $\xrightarrow{\text{restricts on overlap via ρ_{V₁∩V₂,V₂} to}}$ `[Ov]`**

### Commutative Path Facts ($p \simeq q$)
- Sheaf Gluing Pullback/Equalizer Law (Def 7.2.3.5, p. 520): O(V₁ ∪ V₂) ≅ O(V₁) ×_{O(V₁ ∩ V₂)} O(V₂).
- Fiber-Product Prediction (App 7.2.3.9, p. 522): Given local knowledge A ⊆ O(U), possible sections over another region V are predicted via the fiber-product image im((ρ_{U,X})⁻¹(A) -> O(V)).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-42` (sheaf_is_glued_presheaf)** $\to$ [[presheaves-representables-yoneda]] (*Functor Categories, Presheaves, Representables & Yoneda's Lemma*, p. 493–517): A sheaf is a presheaf O : Open(X)^op -> Set satisfying the equalizer gluing condition on all covers — `Sh(X) ↪ PSh(X)`
- **`rho-43` (site_is_open_set_poset)** $\to$ [[orders-lattices-hierarchies]] (*Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces*, p. 221–244): The base site Open(X) is a partial order under inclusion U ⊆ V with meets U ∩ V and joins U ∪ V — `Open(X) ∈ PrO`
- **`rho-44` (gluing_and_prediction_via_pullback)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Binary sheaf gluing O(U∪V) ≅ O(U) ×_{O(U∩V)} O(V) and sheaf prediction are fiber products — `O(U∪V) ≅ O(U) ×_{O(U∩V)} O(V)`
- **`rho-55` (sheaf_gluing_as_equalizer_limit)** $\to$ [[universal-limits-and-cones]] (*Universal Limits, Cones & Terminal Objects in Cat*, p. 392–428): The sheaf gluing axiom over any open cover U = ⋃ V_i is a universal limit (equalizer cone) in Set — `O(U) ≅ lim_{←} (∏ O(V_i) ⇉ ∏ O(V_i ∩ V_j))`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-45` (categorifies_Set_sheaf_to_Sch_sheaf)** $\leftarrow$ [[sheaf-of-ologged-concepts-descent]] (*Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data*, p. 521–526): Upgrades a sheaf of sets O : Open(X)^op -> Set to a sheaf of ologs/categories O : Open(X)^op -> Sch — `O : Open(Alx(X^op))^op -> Sch`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-02` — The Sheaf-Presheaf-Pullback Equalizer Triangle** ([[sheaves-and-local-to-global-gluing]], [[presheaves-representables-yoneda]], [[pullbacks-and-fiber-products]]): Restricting a sheaf O : Open(X)^op -> Set to a binary cover {U, V} exhibits O(U ∪ V) as the fiber product O(U) ×_{O(U ∩ V)} O(V). *[H^0 Exact (Zero Obstruction)]*
- **`tau-03` — The Alexandrov Sheaf of Ologs Worldview Triangle** ([[sheaf-of-ologged-concepts-descent]], [[sheaves-and-local-to-global-gluing]], [[ologs-ontology-logs]]): A simplicial complex X of local ologs O(v) glued via schema restriction maps O(v) -> O(u) forms a sheaf of categories over Alx(X^op). *[H^0 Exact (Zero Obstruction)]*
- **`tau-07` — The Poset-Topology-Sheaf Triangle** ([[sheaves-and-local-to-global-gluing]], [[orders-lattices-hierarchies]], [[universal-limits-and-cones]]): Open(X) is a poset category whose meets are intersections U ∩ V; sheaves turn joins (open covers ∪ V_i) in Open(X) into limits (equalizers) in Set. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 518–522)

### `Definition 7.2.3.2` — [PDF Page 518]
> Definition 7.2.3.2. Let X be a topological space, let Open(X) denote its partial order of open sets, and let Open(X)op be the opposite category. A presheaf on X is a functor O:Open(X)op→Set. For every open set U ⊆ X, we refer to the set O(U) as the set of value assignments throughout U of O. If V ⊆ U is an open subset, it corresponds to an arrow in Open(X), and applying the functor O yields a function

### `Definition 7.2.3.5` — [PDF Page 520]
> Definition 7.2.3.5. Let X be a topological space, let Open(X) be its partial order of open sets, and let O:Open(X)op→Set be a presheaf. Given an open set U ⊆ X and a cover V1, …, Vn of U, the following condition is called the sheaf condition for

### `Application 7.2.3.1` — [PDF Page 518]
> Application 7.2.3.1. Suppose that X is the topological space corresponding to the earth, and let region mean an open subset U ⊆ X. Suppose that we cover X with 10,000 regions U1, U2, …, U10000, such that some of the regions overlap in a nonempty subregion (e.g., U5 ∩ U9 ≠ ∅). For each i, j, let Ui,j = Ui ∩ Uj. For each region Ui ⊆ X, we have a temperature-recording device, which gives a function Ti : Ui → [−100, 200]. If Ui ∩ Uj ≠ ∅, then two different recording devices give us temperature data for the intersection Ui,j. Suppose we find that they do not give precisely the same data but that there is a translation formula between their results

### `Application 7.2.3.7` — [PDF Page 521]
> Application 7.2.3.7. Consider outer space as a topological space X. Different amateur astronomers record observations of what they see in X on a given night. Let C = [390, 700] denote the set of wavelengths in the visible light spectrum (written in nanometers). Given an open subset U ⊆ X, let O(U) denote the set of functions U → C. The presheaf O satisfies the sheaf condition; this is the taken- for-granted fact that we can patch together different observations of space. Figure 7.1 (see page 377) shows three views of the night sky. Given a telescope position to obtain the first view, one moves the telescope right and a little down to obtain t

### `Application 7.2.3.9` — [PDF Page 522]
> Application 7.2.3.9. Suppose we have a sheaf for temperatures on earth. For every region U, we have a set of theoretically possible temperature assignments throughout U. For example, we may know that if it is warm in Texas, warm in Arkansas, and warm in Kansas, then it cannot be cold in Oklahoma. With such a sheaf O in hand, one can use facts about the temperature in one region U to predict the temperature in another region V. The mathematics is as follows. Suppose given regions U, V ⊆ X and a subset A⊆O(U) corresponding to what we know about the temperature assignment throughout U. We take the following fiber product: The image of the top co

### `Example 7.2.3.4` — [PDF Page 519]
> Example 7.2.3.4. Let X = ℝ be the space of real numbers, and define the following open subsets: U = (5, 10), V1 = (5, 7), V2 = (6, 9), V3 = (8, 10).10 Then V1, V2, V3 collectively cover of U. It has overlaps V12 = V1 ∩ V2 = (6, 7), V13 = V1 ∩ V3 = Ø, V23 = V2 ∩ V3 = (8, 9).

### `Example 7.2.3.10` — [PDF Page 522]
> Example 7.2.3.10. Exercises 5.2.4.3 and 5.2.4.4 discussed the idea of laws being dictated or respected throughout a jurisdiction. If X is earth, to every jurisdiction U ⊆ X we assign the set O(U) of laws that are dictated to hold throughout U. Given a law on U and a law on V, we can see if they amount to the same law on U ∩ V. For example, on U a law might say, “no hunting near rivers” and on V a law might say, “no hunting in public areas.” It happens that on U ∩ V all public areas are near rivers, and vice versa, so the laws agree there. These laws patch together to form a single rule about hunting that is enforced throughout the union U ∪ V

### `Remark 7.2.3.6` — [PDF Page 521]
> Remark 7.2.3.6. Application 7.2.3.1 said that sheaves help us patch together information from different sources. Even if different temperature-recording devices Ti and Tj registered different temperatures on an overlapping region Ui ∩ Uj, they could be patched together if given a consistent translation system between their results. What is actually needed is a set of isomorphisms pi,j:Ti|Ui,j→≅Tj|Ui,j that translate between them, and that these pi,j’s act in concert with one another. This (when precisely defined) is called descent data. The way it interacts with the definition of sheaf given in Definitions 7.2.3.2 and 7.2.3.5 is buried in the

### `Exercise 7.2.3.3` — [PDF Page 519]
> Exercise 7.2.3.3. a. Find four overlapping open subsets that cover the square X ≔ [0, 3] × [0, 3] ⊆ ℝ2. Write a label for each open set as well as a label for each overlap (two-fold, three-fold, etc.). You now have labeled n open sets. What is your n? b. Draw the preorder Open(X). For each of the n open sets, draw a dot with the appropriate label. Then draw an arrow from one dot to another when the first refers to an open subset of the second. This is Open(X). c. Make up and write formulas R1 : X → ℝ and R2 : X → ℝ with R1(x) R2(x) for all x ∈ X, expressing a range of temperatures R1(p) Temp(p) R2(p) that an imaginary experiment shows can exi

### `Exercise 7.2.3.8` — [PDF Page 521]
> Exercise 7.2.3.8.

## 6. Page-by-Page Deep Index (PDF Pages 518–522)
- **Page 518** (`7.2 Categories of functors`) · **Items:** Application 7.2.3.1, Definition 7.2.3.2: 7.2.3 Sheaves Let X be a topological space (see Example 5.2.3.1), such as a sphere. Section 7.2.2.3 discussed continuous functions out of X and their use in science (e.g., recording temperatures on the earth as a continuous map X → [−100, 200]). Sheaves allow us to consider the local-global nature of such maps, taking ...
- **Page 519** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.3.3, Example 7.2.3.4: called the restriction map from U to V and denoted ρV,U:O(U)→O(V). Given a∈O(U), we may denote ρV,U(a) by a|V; it is called the restriction of a to V. The category of presheaves on X is simply Open(X)op–Set (see Definition 5.3.3.1). Exercise 7.2.3.3. a. Find four overlapping open subsets that cover the square X ≔ [0, 3...
- **Page 520** (`7.2 Categories of functors`) · **Items:** Definition 7.2.3.5: Given a presheaf O:Open(X)op→Set, we have sets and functions as in the following diagram A presheaf O on X tells us what value assignments throughout U can exist for each U. Suppose we have a value assignment a1∈O(V1) throughout V1 and another value assignment a2∈O(V2) throughout V2, and suppose they agree as value ass...
- **Page 521** (`7.2 Categories of functors`) · **Items:** Remark 7.2.3.6, Application 7.2.3.7, Exercise 7.2.3.8, Figure 7.1: that cover. Sheaf condition Given a sequence a1, …, an, where each ai∈O(Vi) is a value assignment throughout Vi, suppose that for all i, j, we have ai|Vi∩Vj=aj|Vi∩Vj; then there is a unique value assignment b∈O(U) such that b|Vi=ai. The presheaf O is called a sheaf if it satisfies the sheaf condition for every cover. R...
- **Page 522** (`7.2 Categories of functors`) · **Items:** Application 7.2.3.9, Example 7.2.3.10: Find an application of sheaves in your own domain of expertise. Application 7.2.3.9. Suppose we have a sheaf for temperatures on earth. For every region U, we have a set of theoretically possible temperature assignments throughout U. For example, we may know that if it is warm in Texas, warm in Arkansas, and warm in Ka...
