---
id: universal-limits-and-cones
title: "Universal Limits, Cones & Terminal Objects in Cat"
type: SheafStalk
chapter: 6
section: "6.1.1–6.1.3"
pdf_pages: "392–428"
symbol: "lim_{← J} D"
layer: "Universal Constructions in Cat"
extracted_declarations: 73
restricts_to: [pullbacks-and-fiber-products]
glues_with: [grothendieck-construction-comma, adjoint-functors-hom-iso, sheaves-and-local-to-global-gluing]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Universal Limits, Cones & Terminal Objects in Cat (`lim_{← J} D`)

> **Sheaf Stalk Location:** Chapter 6 (Fundamental Considerations of Categories: Universal Limits, Colimits & Grothendieck Construction) · Section `6.1.1–6.1.3` · **PDF Pages 392–428**

## 1. Epistemic Worldview & Intuition

Generalizing products, pullbacks, and equalizers to any category C: given an indexing category J and diagram functor D : J -> C, a cone over D is an apex object W with maps w_j : W -> D(j) commuting with all D(f). The limit lim_J D is the terminal cone in Cone(D).

## 2. Formal Categorical Core

Definition 6.1.3.2 (p. 418): A cone (W, w_j) over D : J -> C is a natural transformation from the constant functor const_W to D. The limit of D is a terminal object in the category Cone(D): every cone (W, w_j) factors uniquely through a single mediating morphism W -> lim D.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[W]`** — *an arbitrary cone apex W over D*
- **`[Lim]`** — *the universal limit object lim D*
- **`[Dj]`** — *a diagram vertex D(j) in C*
- **`[Dk]`** — *a diagram vertex D(k) in C*

### Functional Aspects (Morphisms)
- **`[W]` $\xrightarrow{\text{factors uniquely via u : W -> lim D to}}$ `[Lim]`**
- **`[Lim]` $\xrightarrow{\text{projects via leg π_j to}}$ `[Dj]`**
- **`[Lim]` $\xrightarrow{\text{projects via leg π_k to}}$ `[Dk]`**
- **`[Dj]` $\xrightarrow{\text{maps via diagram arrow D(f) to}}$ `[Dk]`**

### Commutative Path Facts ($p \simeq q$)
- Cone Commutativity: D(f) ∘ π_j = π_k for every morphism f : j -> k in J.
- In Sheaf Theory, the sheaf condition on an open cover {V_i} of U states that O(U) is the limit (equalizer/pullback) of the diagram of local sections O(V_i) over overlaps O(V_i ∩ V_j)!

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-31` (generalizes_Set_limits)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Cones and universal limits in Cat generalize products, pullbacks, and equalizers in Set — `lim_J D |_Set = {compatible tuples}`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-34` (comma_categories_index_Kan_limits)** $\leftarrow$ [[grothendieck-construction-comma]] (*Opposite Categories, Grothendieck Construction ∫I & Comma Categories*, p. 439–460): Comma categories (F ↓ d) and (d ↓ F) serve as the indexing diagrams for Kan extensions Σ_F and Π_F — `(F ↓ d) -> C`
- **`rho-36` (RAPL_preserves_limits)** $\leftarrow$ [[adjoint-functors-hom-iso]] (*Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges*, p. 461–480): Right adjoints preserve all limits (RAPL); left adjoints preserve all colimits (LAPC) — `R(lim D) ≅ lim R(D)`
- **`rho-55` (sheaf_gluing_as_equalizer_limit)** $\leftarrow$ [[sheaves-and-local-to-global-gluing]] (*Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom*, p. 518–522): The sheaf gluing axiom over any open cover U = ⋃ V_i is a universal limit (equalizer cone) in Set — `O(U) ≅ lim_{←} (∏ O(V_i) ⇉ ∏ O(V_i ∩ V_j))`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-07` — The Poset-Topology-Sheaf Triangle** ([[sheaves-and-local-to-global-gluing]], [[orders-lattices-hierarchies]], [[universal-limits-and-cones]]): Open(X) is a poset category whose meets are intersections U ∩ V; sheaves turn joins (open covers ∪ V_i) in Open(X) into limits (equalizers) in Set. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 392–428)

### `Definition 6.1.1.8` — [PDF Page 400]
> Definition 6.1.1.8. Let C be a category, and let X,Y∈Ob(C) be objects. A span on X and Y consists of three constituents (Z, p, q), where Z∈Ob(C) is an object, and where p : Z → X and q : Z → Y are morphisms in C. A product of X and Y is a span X←π1X×Y→π2Y, such that for any other span X←pZ→qY there exists a unique morphism tp,q : Z → X × Y such that the following diagram commutes:3

### `Definition 6.1.1.23` — [PDF Page 407]
> Definition 6.1.1.23. Let C be a category, and let X,Y∈Ob(C) be objects. A cospan on X and Y consists of three constituents (Z, i, j), where Z∈Ob(C) is an object, and where i : X → Z and j : Y → Z are morphisms in C. A coproduct of X and Y is a cospan X→ι1X⊔Y←ι2Y, such that for any other cospan X→iZ←jY there exists a unique morphism si,j : X ⊔ Y → Z such that the following diagram commutes:6

### `Definition 6.1.2.1` (Diagrams) — [PDF Page 411]
> Definition 6.1.2.1 (Diagrams). Let C and I be categories. An I-shaped diagram in C is simply a functor d:I→C. In this case I is called the indexing category for the diagram.7 Here are some rules for drawing diagrams as in Definition 6.1.2.1. Rules of good practice 6.1.2.2. Suppose given an indexing category I and an I- shaped diagram X:I→C. One draws this as follows: (i) For each object in q ∈ I, draw a dot labeled by X(q); if several objects in I point to the same object in C, then several dots are labeled the same way. (ii) For each morphism f : q → q′ in I, draw an arrow between dots X(q) and X(q′), and label it X(f) in C. Again, if severa

### `Definition 6.1.2.8` — [PDF Page 413]
> Definition 6.1.2.8. Let I ∈ Ob(Cat) be a category. The left cone on I, denoted I◅, is the category defined as follows. On objects we put Ob(I◅) = {LCI} ⊔ Ob(I), and we call the new object LCI the cone point of I◅. On morphisms we add a single new morphism sb : LCI → b for every object b ∈ Ob(I); more precisely, HomI◅(a,b)={HomI(a,b)if a,b∈Ob(I),{sb}if a=LCI,b∈Ob(I), {idLCI}if a=b=LCI∅if a∈Ob(I),b=LCI. The composition formula is in some sense obvious. To compose two morphisms both in I, compose as dictated by I; if one has LCI as source, then there will be a unique choice of composite. There is an obvious inclusion of categories, I→I◅.(6.4)

### `Definition 6.1.2.13` — [PDF Page 415]
> Definition 6.1.2.13. Let I ∈ Ob(Cat) be a category. The right cone on I, denoted I▻, is the category defined as follows. On objects we put Ob(I▻) = Ob(I) ⊔ {RCI}, and we call the new object RCI the cone point of I▻. On morphisms we add a single new morphism tb : b → RCI for every object b ∈ Ob(I); more precisely, HomI▻(a,b)={HomI(a,b)if a,b∈Ob(I),{tb}if a∈Ob(I),b=RCI, {idRCI}if a=b=RCI,∅if a=RCI,b∈Ob(I). The composition formula is in some sense obvious. To compose two morphisms both in I, compose as dictated by I; if one has RCI as target, then there will be a unique choice of composite. There is an obvious inclusion of categories I → I▻.

### `Definition 6.1.3.2` — [PDF Page 418]
> Definition 6.1.3.2. Let C be a category. An object a∈Ob(C) is called initial if, for all objects c∈Ob(C), there exists a unique morphism a → c, i.e., |HomC(a,c)|=1. An object z∈Ob(C) is called terminal if, for all objects c∈Ob(C), there is exists a unique morphism c → z, i.e., |HomC(c,z)|=1.

### `Definition 4.1.1` — [PDF Page 420]
> Definition 4.1.1.15) considered as a category via the functor Mon → Cat (see

### `Definition 6.1.3.20` — [PDF Page 424]
> Definition 6.1.3.20. Let C be a category, let I be a category. Let I◅ be the left cone on I, and let i : I → I◅ be the inclusion. Suppose that X:I→C is an I-shaped diagram in C. The slice category of C over X, denoted C/X, is the category whose objects and morphisms are as follows: Ob(C/X)={S:I◅→C|S○i=X}; HomC/X(S,S′)={α:S→S′|α○i=idX}. A limit of X, denoted limI X or lim X, is a terminal object in C/X.

### `Theorem 5.4.2.3` — [PDF Page 414]
> Theorem 5.4.2.3.

### `Theorem 5.2.1` — [PDF Page 420]
> Theorem 5.2.1.3). a. Does M have an initial object? b. Does M have a terminal object? c. Which monoids M, considered as one-object categories, have initial (resp. terminal) objects?

### `Proposition 5.2.1` — [PDF Page 419]
> Proposition 5.2.1.13). a. What is the initial object in ℙ(X)? b. What is the terminal object in ℙ(X)?

### `Proposition 6.1.3.15` — [PDF Page 421]
> Proposition 6.1.3.15. Let C be a category, and let a1,a2∈Ob(C) both be initial objects. Then there is a unique isomorphism f:a1→≅a2. (Similarly, for any two terminal objects in C, there is a unique isomorphism between them.) Proof. Suppose a1 and a2 are initial. Since a1 is initial, there is a unique morphism f : a1 → a2; there is also a unique morphism a1 → a1, which must be ida1. Since a2 is initial, there is a unique morphism g : a2 → a1; there is also a unique morphism a2 → a2, which must be ida2. So g ○ f = ida1 and f ○ g = ida2, which means that f is the desired (unique) isomorphism.

### `Construction 6.1.3.17` (Products) — [PDF Page 422]
> Construction 6.1.3.17 (Products). Let C be a category, and let X1, X2 be objects. We can consider this setup as a diagram X:2¯→C, where X(1) = X1 and X(2) = X2. Consider the category 2◅ = Star2 (see Example 6.1.2.10), the inclusion i : 2 → 2◅ (see (6.4)), and the category of functors Fun(2¯◅,C ). The objects in Fun(2¯◅,C ) are spans in C, and the morphisms are natural transformations between them (see

### `Example 6.1.1.2` — [PDF Page 396]
> Example 6.1.1.2. Given two preorders, X1≔(X1,1) and X2≔(X2,2), we can take their product and get a new preorder X1×X2. Both X1 and X2 have underlying sets (namely, X1 and X2), so we might hope that the underlying set of X1× X2 is the set X1 × X2 of ordered pairs, and this turns out to be true. We have a notion of less-than on X1, and we have a notion of less-than on X2; we need to construct a notion of less-than on X1× X2. So, given two ordered pairs (x1, x2) and (x1′,x2′), when should we say that (x1,x2)1,2(x1′,x2′) holds? A guess is that it holds iff both x11x1′ and x22x2′ hold, and this works:1 X1×X2≔(X1×X2,1,2). Note that the projection f

### `Example 6.1.1.5` — [PDF Page 397]
> Example 6.1.1.5. Given two graphs G1 = (V1, A1, src1, tgt1) and G2 = (V2, A2, src2, tgt2), we can take their product and get a new graph G1 × G2. The vertices are the grid of vertices V1 × V2, so each vertex in G1 × G2 is labeled by a pair of vertices, one from G1 and one from G2. When should an arrow connect (v1, v2) to (v1′,v2′)? Whenever we can find an arrow in G1 connecting v1 to v1′ and we can find an arrow in G2 connecting v2 to v2′. It turns out there is a simple formula for the set of arrows in G1 × G2, namely, A1 × A2. Let’s write G ≔ G1 × G2 and say, G = (V, A, src, tgt). We said that V = V1 × V2 and A = A1 × A2. What should the sou

### `Example 6.1.1.10` — [PDF Page 401]
> Example 6.1.1.10. Example 6.1.1.2 discussed products of preorders. This example discusses products in an individual preorder. That is, by Proposition 5.2.1.13, there is a functor PrO → Cat that realizes each individual preorder as a category. If P=(P,≤) is a preorder, what are products in P? Given two objects a,b∈Ob(P), we first consider {a, b} spans, i.e., a ← z → b. That is some z such that z ≤ a and z ≤ b. The product is a span a ≥ a × b ≤ b, but such that every other spanning object z is less than or equal to a × b. In other words, a × b is as big as possible subject to the condition of being less than a and less than b. This is precisely

### `Example 6.1.1.11` — [PDF Page 401]
> Example 6.1.1.11. Note that the product of two objects in a category C may not exist. Let’s return to preorders to see this phenomenon. Consider the set ℝ2, and say that (x1, y1) ≤ (x2, y2) if there exists ℓ ≥ 1 such that x1ℓ = x2 and y1ℓ = y2; in other words, point p is less than point q if, in order to travel from q to the origin along a straight line, one must pass through p along the way.4 We have given a perfectly good partial order, but p ≔ (1, 0) and q ≔ (0, 1) do not have a product. Indeed, it would have to be a nonzero point that was on the same line through the origin as p and the same line through the origin as q, of which there ar

### `Example 6.1.1.12` — [PDF Page 401]
> Example 6.1.1.12. Note that there can be more than one product of two objects in a category C but that any two choices will be canonically isomorphic. Let’s return once more to preorders to see this phenomenon. Consider the set ℝ2, and say that (x1, y1) ≤ (x2, y2) if x12+y12≤x22+y22, in other words, if the former is closer to the origin. For any point p = (x0, y0), let Cp= {(x,y)∈ℝ2|x2+y2=x02+y02)}, and call it the orbit circle of p. For any two points p, q, there will be lots of points that serve as products p × q: any point a on the smaller of their two orbit circles will suffice. Given any two points a, a′ on this smaller circle, we have a

## 6. Page-by-Page Deep Index (PDF Pages 392–428)
- **Page 392** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): Chapter 6 Fundamental Considerations of Categories This chapter focuses mainly on limits and colimits in a given category C. It also discusses other important and interesting categorical constructions, such as the simple notion of opposite categories and the Grothendieck construction, which gives something like the his...
- **Page 393** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): ...
- **Page 394** (`6.1 Limits and colimits`): 6.1 Limits and colimits Limits and colimits are universal constructions, meaning they represent certain ideals of behavior in a category. When it comes to sets that map to A and B, the A × B grid is ideal—it projects on to both A and B as straightforwardly as possible. When it comes to sets that can interpret the eleme...
- **Page 395** (`6.1 Limits and colimits`): ...
- **Page 396** (`6.1 Limits and colimits`) · **Items:** Example 6.1.1.2, Exercise 6.1.1.3: 6.1.1 Products and coproducts in a category Section 3.1 discussed products and coproducts in the category Set of sets. Now we discuss the same notions in an arbitrary category. For both products and coproducts, we begin with examples and then write the general concept. 6.1.1.1 Products The product of two sets is a grid...
- **Page 397** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.4, Example 6.1.1.5: order A=(A,A) on pieces of art. You are about to be given two pairs (s, a) and (s′, a′), each including a song and an art piece. Does the product partial order S×A provide a reasonable guess for your preferences on these pairs? Exercise 6.1.1.4. Consider the partial order on ℕ given by standard less-than-or-equal-to, s...
- **Page 398** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.6: The product I × J has, as expected, 3 * 4 = 12 vertices and 3 * 4 = 12 arrows: Here is the most important thing to notice. Look at the Arrow table for I × J, and for each ordered pair, look only at the first entry in all three columns; you will see something that matches with the Arrow table for I. For example, in the ...
- **Page 399** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.7: Let [1] denote the linear order graph of length 1, and let P = Paths([1]) be its paths-graph, as in Example 5.1.2.25 (so P should have three arrows and two vertices). Draw the graph P × P. Exercise 6.1.1.7. Recall from Example 4.5.2.10 that a discrete dynamical system (DDS) is a set s together with a function f : s → s...
- **Page 400** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.1.8: 5.3.3.5), which in the case of functors Loop → Set are the morphisms of instances. Do you see clearly that there is a morphism of instances I × J → I and I × J → J? Check that if you look only at the left-hand coordinates in your I × J, you see something compatible with I. In each case what is most important to recogni...
- **Page 401** (`6.1 Limits and colimits`) · **Items:** Remark 6.1.1.9, Example 6.1.1.10, Example 6.1.1.11, Example 6.1.1.12: We often denote the morphism tp,q by 〈p, q〉: Z → X × Y . Remark 6.1.1.9. Definition 6.1.1.8 endows the product of two objects with a universal property. It says that a product of two objects X and Y maps to those two objects and serves as a gateway for all that do the same. “None shall map to X and Y except through me!...
- **Page 402** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.13, Exercise 6.1.1.14, Exercise 6.1.1.15, Exercise 6.1.1.16, Example 6.1.1.17: ≤ a′ and a′ ≤ a. Exercise 6.1.1.13. Consider the preorder P of cards in a deck, shown in Example 4.4.1.3; it is not the whole story of cards in a deck, but take it to be so. Consider this preorder P as a category (by way of the functor PrO → Cat). a. For each of the following pairs, what is their product in P (if it ex...
- **Page 403** (`6.1 Limits and colimits`) · **Items:** Example 6.1.1.19: do exist in Cat, the category of categories. That is, given two categories C and D, there is a product category C×D. We have Ob(C×D)=Ob(C)×Ob(D), and for any two objects (c, d) and (c′, d′), we have HomC×D((c,d),(c′,d′))=HomC(c,c′)×HomC(d,d′). The composition formula is clear. Let [1] ∈ Ob(Cat) denote the linear order ...
- **Page 404** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.20: take their coproduct and get a new preorder X1⊔ X2. Both X1 and X2 have underlying sets (namely, X1 and X2), so we might hope that the underlying set of X1× X2 is the disjoint union X1 ⊔ X2, and that turns out to be true. We have a notion of less-than on X1 and a notion of less-than on X2. Given an element x ∈ X1 ⊔ X2 ...
- **Page 405** (`6.1 Limits and colimits`) · **Items:** Example 6.1.1.21: Suppose you have a partial order A≔(A,≤A) on apples (you prefer some apples to others, but sometimes you cannot compare). And suppose you have a partial order O≔(O,≤O) on oranges. You are about to be given two pieces of fruit from a basket of apples and oranges. Is the coproduct partial order A⊔O a reasonable guess for...
- **Page 406** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.1.22: The coproduct I ⊔ J has, as expected, 3 + 5 = 8 vertices and 3 + 4 = 7 arrows: Here is the most important thing to notice. Look at the Arrow tables and notice that there is a way to send each row in I to a row in I ⊔ J such that all the foreign keys match, and similarly for J. This also works for the vertex tables. The...
- **Page 407** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.1.23: is the loop schema, then a DDS is simply an instance (a functor) I : Loop → Set. We have not yet discussed DDS coproducts but perhaps you can guess how they should work. For example, consider these instances I, J : Loop → Set: Make a guess and tabulate I ⊔ J. Then draw it. In each case (preorders, graphs, DDSs), what i...
- **Page 408** (`6.1 Limits and colimits`) · **Items:** Remark 6.1.1.24, Example 6.1.1.25: The morphism si,j is often denoted {ij :X⊔Y→Z . Remark 6.1.1.24. Definition 6.1.1.8 endows the coproduct of two objects with a universal property. It says that a coproduct of two objects X and Y receives maps from those two objects, and serves as a gateway for all that do the same. “None shall receive maps from X and Y...
- **Page 409** (`6.1 Limits and colimits`) · **Items:** Example 6.1.1.26, Exercise 6.1.1.27, Exercise 6.1.1.28, Exercise 6.1.1.29: Example 6.1.1.26. Consider the set ℝ2 and partial order from Example 6.1.1.11, where (x1, y1) ≤ (x2, y2) if there exists ℓ ≥ 1 such that x1ℓ = x2 and y1ℓ = y2. Again the points p ≔ (1, 0) and q ≔ (0, 1) do not have a coproduct. Indeed, it would have to be a nonzero point that was on the same line through the origin as ...
- **Page 410** (`6.1 Limits and colimits`): ...
- **Page 411** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.2.1, Example 6.1.2.3: 6.1.2 Diagrams in a category Diagrams have illustrated the text throughout the book. What is the mathematical foundation of these illustrations? The answer is functors. Definition 6.1.2.1 (Diagrams). Let C and I be categories. An I-shaped diagram in C is simply a functor d:I→C. In this case I is called the indexing cat...
- **Page 412** (`6.1 Limits and colimits`) · **Items:** Example 6.1.2.4, Exercise 6.1.2.5, Example 6.1.2.6: must respect composition formulas, which implies that diagram (6.2) commutes. We call [1] × [1] the commutative square indexing category. 8 Example 6.1.2.4. Recall from Section 2.2 that not all diagrams commute; one must specify that a given diagram commutes if one wishes to communicate this fact. But then, how is a no...
- **Page 413** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.2.7, Definition 6.1.2.8, Remark 6.1.2.9: where g1 ○ f = g2 ○ f. What is the indexing category for such a diagram? It is the schema (6.3) with the PED E[f, g1] ≃ E[f, g2]. That is, in some sense one sees the indexing category, but the PED needs to be declared. Exercise 6.1.2.7. Let C be a category, A∈Ob(C) an object, and f : A → A a morphism in C. Consider the...
- **Page 414** (`6.1 Limits and colimits`) · **Items:** Theorem 5.4.2.3, Example 6.1.2.10, Exercise 6.1.2.11, Exercise 6.1.2.12, Solution 6.1.2.12: do not distinguish between categories and schemas, since they are equivalent, by Theorem 5.4.2.3. Example 6.1.2.10. For a natural number n ∈ ℕ, define the n-leaf star schema, denoted Starn, to be the category (or schema; see Remark 6.1.2.9) n◅, where n is the discrete category on n objects. The following illustrate the...
- **Page 415** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.2.13, Exercise 6.1.2.14, Exercise 6.1.2.15, Solution 6.1.2.15: Definition 6.1.2.13. Let I ∈ Ob(Cat) be a category. The right cone on I, denoted I▻, is the category defined as follows. On objects we put Ob(I▻) = Ob(I) ⊔ {RCI}, and we call the new object RCI the cone point of I▻. On morphisms we add a single new morphism tb : b → RCI for every object b ∈ Ob(I); more precisely, HomI▻...
- **Page 416** (`6.1 Limits and colimits`): ...
- **Page 417** (`6.1 Limits and colimits`): ...
- **Page 418** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.3.2, Example 6.1.3.3, Example 6.1.3.4, Example 6.1.3.5: 6.1.3 Limits and colimits in a category Let C be a category, let I be an indexing category (which means that I is a category that we use as the indexing category for a diagram), and let D:I→C be an I-shaped diagram (which means a functor). It is in relation to this setup that we can discuss the limit or colimit. In gen...
- **Page 419** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.3.6, Proposition 5.2.1, Example 6.1.3.7, Exercise 6.1.3.8, Example 6.1.3.9: The terminal object in Grph is more interesting. It is the graph with one vertex and one arrow. In fact, there are infinitely many terminal objects in Grph, but all of them are isomorphic to Loop, meaning one can change the names of the vertex (s) and the arrow (f) and get another terminal object. Exercise 6.1.3.6. Let...
- **Page 420** (`6.1 Limits and colimits`) · **Items:** Example 6.1.3.10, Exercise 6.1.3.11, Exercise 6.1.3.12, Definition 4.1.1, Theorem 5.2.1, Exercise 6.1.3.13: 5.2.4.1. The initial object is a proposition that implies all others. It turns out that “FALSE” is such a proposition. The proposition “FALSE” is like “1 ≠ 1”; in logical formalism it can be shown that if “FALSE” is true, then everything is true. The terminal object in Prop is a proposition that is implied by all other...
- **Page 421** (`6.1 Limits and colimits`) · **Items:** Warning 6.1.3.14, Proposition 6.1.3.15: whether the object is initial or terminal. The word final is synonymous with the word terminal, but we will use the latter. Universal properties refer to either initial or terminal objects in a specially- designed category. Colimits end up having an initial sort of universal property, and limits end up having a termina...
- **Page 422** (`6.1 Limits and colimits`) · **Items:** Construction 6.1.3.17, Exercise 6.1.2: The proof for terminal objects is appropriately dual. 6.1.3.16 Examples of limits We are moving toward defining limits and colimits in full generality. We have assembled most of the pieces we will need: indexing categories, their left and right cones, and the notion of initial and terminal objects. Relying on the now f...
- **Page 423** (`6.1 Limits and colimits`) · **Items:** Example 6.1.3.18: Define the category of X spans in C, denoted C/X, to be the category whose objects and morphisms are as follows: Ob(C/X)={S:2¯◅→C|S○i=X}HomC/X(S,S′)={α:S→S′|α◇i=idX}.(6.5) The product of X1 and X2 was defined in Definition 6.1.1.8; we can now recast X1 × X2 as the terminal object in C/X. An object in C/X can be picture...
- **Page 424** (`6.1 Limits and colimits`) · **Items:** Definition 6.1.3.20: Let X:2¯→C be given by X(1) = X1 and X(2) = X2. Then the category of X spans might be drawn 6.1.3.19 Definition of limit A product of two objects X, Y ∈ Ob() is a special case of a limit, namely, one in which the indexing category is 2. To handle arbitrary limits, we replace 2 with an arbitrary indexing category I, and...
- **Page 425** (`6.1 Limits and colimits`) · **Items:** Remark 6.1.3.21: Remark 6.1.3.21. Perhaps the following diagram will be helpful for understanding limits. Given a functor X:I→C, what is its limit? The solid-arrow part of the figure is the data we start with, i.e., the category C, the indexing category I, and the diagram X:I→C, as well as the part we automatically add, the cone I◅ wit...
- **Page 426** (`6.1 Limits and colimits`) · **Items:** Remark 6.1.1, Remark 6.1.3.22, Exercise 6.1.3.23: An object S in the slice category C/X is a commutative diagram S : I◅ → C over X, which looks like the left-hand box: A morphism in C/X is drawn as in the right-hand box. A terminal object in C/X is precisely the gateway we want, i.e., the limit of X is the pullback X0×X2X1 (see Remark 6.1.1.9). Remark 6.1.3.22. Let C ...
- **Page 427** (`6.1 Limits and colimits`) · **Items:** Exercise 6.1.3.24, Solution 6.1.3.24, Example 6.1.3.25: a. What is GrIn◅? b. Let G : GrIn → Set be the graph from Example 4.3.1.2. Give an example of an object in Set/G. Exercise 6.1.3.24. Let C be a category, and let I = 0 be the empty category. There is a unique functor X:0¯→C. a. What is the slice category C/X? b. What is a limit of X? Solution 6.1.3.24. a. The left cone...
- **Page 428** (`6.1 Limits and colimits`) · **Items:** Example 6.1.3.26: which, of course, is the product, XLCn¯=X1×X2×⋯×Xn. Example 6.1.3.26. We have now defined limits in any category, so we have defined limits in Cat. Let [1] denote the category depicted •0→e•1 and let C be an arbitrary category. Naming two categories is the same thing as naming a functor X : 2 → Cat; consider the functo...
