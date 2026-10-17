---
id: orders-lattices-hierarchies
title: "Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces"
type: SheafStalk
chapter: 4
section: "4.4"
pdf_pages: "221–244"
symbol: "(P, ≤) ∈ PrO"
layer: "Pre-Categorical Models"
extracted_declarations: 48
restricts_to: [products-and-projections, coproducts-and-injections]
glues_with: [categories-objects-morphisms, sheaves-and-local-to-global-gluing]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces (`(P, ≤) ∈ PrO`)

> **Sheaf Stalk Location:** Chapter 4 (Categories and Functors, Without Admitting It: Monoids, Groups, Graphs, Orders & Databases) · Section `4.4` · **PDF Pages 221–244**

## 1. Epistemic Worldview & Intuition

Orders formalize hierarchies, taxonomies, causal structure, and open-set lattices Open(X). A preorder (P, <=) is a reflexive, transitive relation—equivalent to a category with at most one morphism between any two objects. Meets (greatest lower bounds) are categorical products; joins (least upper bounds) are categorical coproducts.

## 2. Formal Categorical Core

Preorder: x <= x (reflexive) and x <= y & y <= z => x <= z (transitive) (Def 4.4.1.1, p. 223). Partial order adds antisymmetry (x <= y & y <= x => x = y). Monotone map f : P -> Q satisfies x <= y => f(x) <= f(y) (functor between thin categories). Open(X) of a topological space is a partial order under subset inclusion U <= V.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[U]`** — *an open subregion U in Open(X)*
- **`[V]`** — *a larger open region V in Open(X)*
- **`[Meet]`** — *their overlap intersection U ∧ V = U ∩ V*
- **`[Join]`** — *their union cover U ∨ V = U ∪ V*

### Functional Aspects (Morphisms)
- **`[Meet]` $\xrightarrow{\text{is included in (≤)}}$ `[U]`**
- **`[Meet]` $\xrightarrow{\text{is included in (≤)}}$ `[V]`**
- **`[U]` $\xrightarrow{\text{is included in (≤)}}$ `[Join]`**
- **`[V]` $\xrightarrow{\text{is included in (≤)}}$ `[Join]`**

### Commutative Path Facts ($p \simeq q$)
- In a poset category (P, ≤), categorical product is Meet (x ∧ y) and categorical coproduct is Join (x ∨ y) (Sec 4.4.2, p. 231).
- The opposite order P^op reverses ≤, turning inclusions U ⊆ V into restriction morphisms V -> U for presheaves Open(X)^op -> Set.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-18` (poset_meet_as_product)** $\to$ [[products-and-projections]] (*Products & Universal Pairing in Set*, p. 68–79): In a preorder (P, ≤), categorical product is greatest lower bound (meet x ∧ y) — `x ×_P y = x ∧ y`
- **`rho-19` (poset_join_as_coproduct)** $\to$ [[coproducts-and-injections]] (*Coproducts & Disjoint Unions in Set*, p. 80–87): In a preorder (P, ≤), categorical coproduct is least upper bound (join x ∨ y) — `x ⊔_P y = x ∨ y`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-23` (thin_category)** $\leftarrow$ [[categories-objects-morphisms]] (*Categories: Objects, Morphisms, Identities & Composition*, p. 267–284): A category with at most one morphism between any two objects is a preorder — `PrO ↪ Cat`
- **`rho-43` (site_is_open_set_poset)** $\leftarrow$ [[sheaves-and-local-to-global-gluing]] (*Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom*, p. 518–522): The base site Open(X) is a partial order under inclusion U ⊆ V with meets U ∩ V and joins U ∪ V — `Open(X) ∈ PrO`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-07` — The Poset-Topology-Sheaf Triangle** ([[sheaves-and-local-to-global-gluing]], [[orders-lattices-hierarchies]], [[universal-limits-and-cones]]): Open(X) is a poset category whose meets are intersections U ∩ V; sheaves turn joins (open covers ∪ V_i) in Open(X) into limits (equalizers) in Set. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 221–244)

### `Definition 4.4.1.1` — [PDF Page 223]
> Definition 4.4.1.1. Let S be a set and R ⊆ S × S a binary relation on S; if (s, s′) ∈ R, we write s s′. Then we say that R is a preorder if, for all s, s′, s″ ∈ S, we have Reflexivity: s s, and Transitivity: if s s′ and s′ s″, then s s″. We say that R is a partial order if it is a preorder and, in addition, for all s, s′ ∈ S, we have Antisymmetry: If s s′ and s′ s, then s = s′. We say that R is a linear order if it is a partial order and, in addition, for all s, s′ ∈ S, we have Comparability: Either s s′ or s′ s. We denote such a preorder (or partial order or linear order) by (S, ).

### `Definition 4.4.1.14` — [PDF Page 227]
> Definition 4.4.1.14. Let (S, ) be a preorder. A clique is a subset S′ ⊆ S such that for each a, b ∈ S′, one has a b.

### `Definition 4.4.2.1` — [PDF Page 231]
> Definition 4.4.2.1. Let (S, ) be a preorder, and let s, t ∈ S be elements. A meet of s and t is an element w ∈ S satisfying the following universal property: w s and w t, for any x ∈ S, if x s and x t, then x w. If w is a meet of s and t, we write w ≅ s ∧ t. A join of s and t is an element w ∈ S satisfying the following universal property: s w and t w, for any x ∈ S, if s x and t x, then w x. If w is a join of s and t, we write w ≅ s ∨ t. That is, the meet of s and t is the biggest thing that is smaller than both, i.e., a greatest lower bound, and the join of s and t is the smallest thing that is bigger than both, i.e., a least upper bound. N

### `Definition 4.4.3.1` — [PDF Page 235]
> Definition 4.4.3.1. Let S≔(S,) be a preorder. The opposite preorder, denoted Sop, is the preorder (S, op) having the same set of elements but where s op s′ iff s′ s.

### `Definition 4.4.4.1` — [PDF Page 237]
> Definition 4.4.4.1. Let S≔(S,) and S′≔(S′,′) be preorders (resp. partial orders or linear orders). A morphism of preorders (resp. partial orders or linear orders) f from S to S′, denoted f:S→S′, is a function f:S→S′ such that, for every pair of elements s1, s2 ∈ S, if s1 s2, then f(s1) ′ f(s2).

### `Slogan 4.4.1.11` — [PDF Page 226]
> Slogan 4.4.1.11. A graph generates a preorder: v w if there is a path v → w.

### `Application 4.4.1.6` — [PDF Page 224]
> Application 4.4.1.6. Classically, we think of time as linearly ordered. A model is (ℝ, ), the usual linear order on the set of real numbers. But according to the theory of relativity, there is not actually a single order to the events in the universe. Different observers correctly observe different orders on the set of events.

### `Application 4.4.4.3` — [PDF Page 237]
> Application 4.4.4.3. It is often said that a team is only as strong as its weakest member. Is this true for materials? The hypothesis that a material is only as strong as its weakest constituent can be understood as follows. Recall from the beginning of Section 4.4 (page 132) that we can put several different orders on the set M of materials. One example is the order given by constituency (m C m′ if m is an ingredient or constituent of m′). Another order is given by strength: m S m′ if m′ is stronger than m (in some fixed setting). Is it true that if material m is a constituent of material m′, then the strength of m′ is less than or equal to 

### `Example 4.4.1.3` (Partial order not linear order) — [PDF Page 223]
> Example 4.4.1.3 (Partial order not linear order). The following is an olog for playing cards:

### `Example 4.4.1.5` (Preorder, not partial order) — [PDF Page 224]
> Example 4.4.1.5 (Preorder, not partial order). Every equivalence relation is a preorder, but rarely are they partial orders. For example, if S = {1, 2} and we put R = S × S, then this is an equivalence relation. It is a preorder but not a partial order (because 1 2 and 2 1, but 1 ≠ 2, so antisymmetry fails).

### `Example 4.4.1.7` (Finite linear orders) — [PDF Page 225]
> Example 4.4.1.7 (Finite linear orders). Let n ∈ ℕ be a natural number. Define a linear order [n] = ({0, 1, 2, … , n}, ) in the standard way. Pictorially, [ n ]≔•0→•1→•2→⋯→•n Every finite linear order, i.e., linear order on a finite set, is of the preceding form. That is, though the labels might change, the picture would be the same. This can be made precise when morphisms of orders are defined (see Definition 4.4.4.1)

### `Example 4.4.1.16` — [PDF Page 228]
> Example 4.4.1.16. Let X be a set and R ⊆ X × X a relation. For elements x, y ∈ X, we say there is an R-path from x to y if there exists a natural number n ∈ ℕ and elements x0, x1, … , xn ∈ X such that 1. x = x0; 2. xn = y; 3. for all i ∈ ℕ, if 0 i n − 1, then (xi, xi+1) ∈ R. Let R¯ denote the relation where (x,y)∈R¯ if there exists an R-path from x to y. We call R¯ the preorder generated by R. and note some facts about R¯: Containment. If (x, y) ∈ R, then (x,y)∈R¯. That is, R⊆R¯. Reflexivity. For all x ∈ X, we have (x,x)∈R¯. Transitivity. For all x, y, z ∈ X, if (x,y)∈R¯ and (y,z)∈R¯ , then (x,z)∈R¯. Let’s write x y if (x,y)∈R¯ . To check the

### `Example 4.4.2.5` (Trees) — [PDF Page 232]
> Example 4.4.2.5 (Trees). A tree, i.e., a system of nodes and branches, all of which emanate from a single node called the root, is a partial order but generally not a linear order. A tree (T, ) can either be oriented toward the root (so the root is the largest element of the partial order) or away from the root (so the root is the smallest element); let’s only consider the former.

### `Example 4.4.3.2` — [PDF Page 235]
> Example 4.4.3.2. Consider the preorder N≔(ℕ,divides), where a divides b if “a goes into b evenly,” i.e., if there exists n ∈ ℕ such that a * n = b. So 5 divides 35, and so on. Then Nop is the set of natural numbers but where m n iff m is a multiple of n. So 6 2 and 6 3, but 6 ≰ 4.

### `Example 4.4.4.2` — [PDF Page 237]
> Example 4.4.4.2. Let X and Y be sets, and let f : X → Y be a function. Then for every subset X′ ⊆ X, its image f(X′) ⊆ Y is a subset (see Exercise 2.1.2.8). Thus we have a function F : ℙ(X) → ℙ(Y), given by taking images. This is a morphism of partial orders (ℙ(X), ⊆) → (ℙ(Y), ⊆). Indeed, if a ⊆ b in ℙ(X), then f(a) ⊆ f(b) in ℙ(Y).

### `Example 4.4.4.5` — [PDF Page 237]
> Example 4.4.4.5. Let S be a set. The smallest preorder structure that can be put on S is to say a b iff a = b. This is indeed reflexive and transitive, and it is called the discrete preorder on S. The largest preorder structure that can be put on S is to say a b for all a, b

### `Example 4.4.5.8` — [PDF Page 242]
> Example 4.4.5.8. Let U = {(x, y) ∈ ℝ2 | x > 0}. To see that U is open, define the following sets: for any a, b ∈ ℝ, let S(a, b) be the square parallel to the axes, with side length 1, where the upper left corner is (a, b). Note that S(a, b) is a closed curve, so if we let S′(a, b) be the interior of S(a, b), then each S′(a, b) is a basic open set. Now U is the union of S′(a, b) over the collection of all a > 0 and all b, U=∪a,b∈ℝ,a>0 S′(a,b), so U is open.

### `Example 4.4.5.9` — [PDF Page 242]
> Example 4.4.5.9. The idea of open sets extends to spaces beyond ℝ2. For example, on the earth one could define a basic open set to be the interior of any region one can draw a closed curve around (with a metaphorical pen), and define open sets to be unions of these basic open sets.

## 6. Page-by-Page Deep Index (PDF Pages 221–244)
- **Page 221** (`4.4 Orders`): 4.4 Orders People usually think of certain sets as though they come with a canonical order. For example, one might think the natural numbers come with the ordering by which 3 < 5, or that the letters in the alphabet come with the order by which b < e. But in fact we put orders on sets, and some orders are simply more c...
- **Page 222** (`4.4 Orders`): ...
- **Page 223** (`4.4 Orders`) · **Items:** Definition 4.4.1.1, Exercise 4.4.1.2, Example 4.4.1.3: 4.4.1 Definitions of preorder, partial order, linear order Definition 4.4.1.1. Let S be a set and R ⊆ S × S a binary relation on S; if (s, s′) ∈ R, we write s s′. Then we say that R is a preorder if, for all s, s′, s″ ∈ S, we have Reflexivity: s s, and Transitivity: if s s′ and s′ s″, then s s″. We say that R is a part...
- **Page 224** (`4.4 Orders`) · **Items:** Remark 4.4.1.4, Example 4.4.1.5, Application 4.4.1.6: We can put a binary relation on the set of boxes here by saying A B if there is a path A → B. One can see immediately that this is a preorder because length 0 paths give reflexivity, and concatenation of paths gives transitivity. To see that it is a partial order we only note that there are no loops of any length. But ...
- **Page 225** (`4.4 Orders`) · **Items:** Example 4.4.1.7, Exercise 4.4.1.8, Exercise 4.4.1.9, Remark 4.4.1.10: Example 4.4.1.7 (Finite linear orders). Let n ∈ ℕ be a natural number. Define a linear order [n] = ({0, 1, 2, … , n}, ) in the standard way. Pictorially, [ n ]≔•0→•1→•2→⋯→•n Every finite linear order, i.e., linear order on a finite set, is of the preceding form. That is, though the labels might change, the picture woul...
- **Page 226** (`4.4 Orders`) · **Items:** Slogan 4.4.1.11, Exercise 4.4.1.12, Exercise 4.4.1.13: Given a graph G, we can create a binary relation on its set S of vertices as follows. Put a b if there is a path in G from a to b. This relation will be reflexive and transitive, so it is a preorder. If the graph satisfies property 3, then the preorder will be a partial order, and if the graph also satisfies property 4...
- **Page 227** (`4.4 Orders`) · **Items:** Solution 4.4.1.13, Definition 4.4.1.14: b. Repeat this for Q = ∅, R = {1}, and T = {1, 2, 3}. That is, draw the partial orders on ℙ(Q), ℙ(R), and ℙ(T). c. Do you see n-dimensional cubes? Solution 4.4.1.13. a. b. c. Yes. The graph associated to ℙ(n) looks like an n-dimensional cube. Definition 4.4.1.14. Let (S, ) be a preorder. A clique is a subset S′ ⊆ S suc...
- **Page 228** (`4.4 Orders`) · **Items:** Exercise 4.4.1.15, Solution 4.4.1.15, Example 4.4.1.16: Exercise 4.4.1.15. True or false: A partial order is a preorder that has no cliques? (If false, is there a nearby true statement?) Solution 4.4.1.15. False. Every element is always in its own clique, so if X is a partial order with at least one element, then it has a clique. But a nearby statement is true. Let’s define...
- **Page 229** (`4.4 Orders`) · **Items:** Exercise 4.4.1.17, Exercise 4.4.1.18: xn = y and y = y0 y1 … yp = z; then x = x0 x1 … xn y1 … yp = z will be an R-path from x to z. We can turn any relation into a preorder in a canonical way. Here is a concrete case of this idea. Let X = {a, b, c, d} and suppose given the relation {(a, b), (b, c), (b, d), (d, c), (c, c)}. This is neither reflexive nor tra...
- **Page 230** (`4.4 Orders`): ...
- **Page 231** (`4.4 Orders`) · **Items:** Definition 4.4.2.1, Exercise 4.4.2.2: 4.4.2 Meets and joins Let X be any set. Recall from Definition 3.4.4.9 that the power-set of X, denoted ℙ(X), is the set of subsets of X. There is a natural order on ℙ(X) given by the subset relationship, as exemplified in Exercise 4.4.1.13. Given two elements a, b ∈ ℙ(X), we can consider them as subsets of X and take ...
- **Page 232** (`4.4 Orders`) · **Items:** Exercise 4.4.2.3, Solution 4.4.2.3, Exercise 4.4.2.4, Example 4.4.2.5: b. What is the meet of ⌜a black card⌝ and ⌜a queen⌝? c. What is the meet of ⌜a diamond⌝ and ⌜a card⌝? Not every two elements in a preorder need have a meet, nor need they have a join. Exercise 4.4.2.3. a. If possible, find two elements in the partial order from Example 4.4.1.3 that do not have a meet.7 b. If possible, ...
- **Page 233** (`4.4 Orders`) · **Items:** Exercise 4.4.2.6: A tree is pictured as a graph in (4.10). The root is labeled e. In a tree every pair of elements s, t ∈ T has a join s ∧ t (their closest mutual ancestor). On the other hand, if s and t have a join c = s ∨ t, then either c = s or c = t. Exercise 4.4.2.6. Consider the tree drawn in (4.10). a. What is the join i ∨ h? b. ...
- **Page 234** (`4.4 Orders`): ...
- **Page 235** (`4.4 Orders`) · **Items:** Definition 4.4.3.1, Example 4.4.3.2, Exercise 4.4.3.3, Exercise 4.4.3.4: 4.4.3 Opposite order Definition 4.4.3.1. Let S≔(S,) be a preorder. The opposite preorder, denoted Sop, is the preorder (S, op) having the same set of elements but where s op s′ iff s′ s. Example 4.4.3.2. Consider the preorder N≔(ℕ,divides), where a divides b if “a goes into b evenly,” i.e., if there exists n ∈ ℕ such t...
- **Page 236** (`4.4 Orders`): ...
- **Page 237** (`4.4 Orders`) · **Items:** Definition 4.4.4.1, Example 4.4.4.2, Application 4.4.4.3, Exercise 4.4.4.4, Example 4.4.4.5: 4.4.4 Morphism of orders An order (S, ), be it a preorder, a partial order, or a linear order, involves a set and a binary relation. For two orders to be comparable, their sets and their relations should be appropriately comparable. Definition 4.4.4.1. Let S≔(S,) and S′≔(S′,′) be preorders (resp. partial orders or line...
- **Page 238** (`4.4 Orders`) · **Items:** Exercise 4.4.4.6, Exercise 4.4.4.7: ∈ S. This again is reflexive and transitive, and it is called the indiscrete preorder on S. Exercise 4.4.4.6. Let S be a set, and let (T, T) be a preorder. Let D be the discrete preorder on S. a. A morphism of preorders (S, D) → (T, T) is a function S → T satisfying certain properties (see Definition 4.4.4.1). Which fu...
- **Page 239** (`4.4 Orders`): ...
- **Page 240** (`4.4 Orders`) · **Items:** Exercise 4.4.5.2: 4.4.5 Other applications 4.4.5.1 Biological classification Biological classification is a method for dividing the set of organisms into distinct classes, called taxa. In fact, it turns out that such a classification, say, a phylogenetic tree, can be understood as a partial order C on the set of taxa. The typical rankin...
- **Page 241** (`4.4 Orders`) · **Items:** Exercise 4.4.5.3, Exercise 4.4.5.5, Exercise 4.4.5.6: b. If we did not require the phylogenetic partial order to be a tree, what would it mean if two taxa (nodes in the phylogenetic partial order), say, a and b, had meet c with c ≠ a and c ≠ b? Exercise 4.4.5.3. a. In your favorite scientific subject, are there any interesting classification systems that are actually orde...
- **Page 242** (`4.4 Orders`) · **Items:** Example 4.4.5.8, Example 4.4.5.9, Exercise 4.4.5.10, Exercise 4.4.5.11: 4.4.5.7 Spaces and geography Consider closed curves that can be drawn in the plane ℝ2, e.g., circles, ellipses, and kidney-bean shaped curves. The interiors of these closed curves (not including the boundary itself) are called basic open sets in ℝ2. The good thing about such an interior U is that any point p ∈ U is not...
- **Page 243** (`4.4 Orders`) · **Items:** Solution 4.4.5.11, Exercise 4.4.5.12: a. Does the assignment T : S → V amount to a morphism of orders? b. If so, does it preserve meets or joins? Hint: It does not preserve both. Solution 4.4.5.11. a. Suppose s is a subregion of s′, e.g., New Mexico as a subregion of North America. This question is asking whether the range of temperatures recorded througho...
- **Page 244** (`4.4 Orders`): ...
