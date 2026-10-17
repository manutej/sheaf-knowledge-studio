---
id: grothendieck-construction-comma
title: "Opposite Categories, Grothendieck Construction ∫I & Comma Categories"
type: SheafStalk
chapter: 6
section: "6.2"
pdf_pages: "439–460"
symbol: "∫_C I → C"
layer: "Universal Constructions in Cat"
extracted_declarations: 26
restricts_to: [database-schemas-instances, universal-limits-and-cones]
glues_with: [presheaves-representables-yoneda]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Opposite Categories, Grothendieck Construction ∫I & Comma Categories (`∫_C I → C`)

> **Sheaf Stalk Location:** Chapter 6 (Fundamental Considerations of Categories: Universal Limits, Colimits & Grothendieck Construction) · Section `6.2` · **PDF Pages 439–460**

## 1. Epistemic Worldview & Intuition

Three structural operations on categories: (1) Opposite category C^op reverses all arrows (turning presheaves C^op -> Set into covariant functors); (2) The Grothendieck construction (category of elements ∫I) flattens a Set-valued functor I : C -> Set into a single category fibred over C (turning a database instance into anRDF-like typed graph with projection pi : ∫I -> C); (3) Slice (C/x) and Comma categories ((F ↓ G)) localize morphisms over a base context.

## 2. Formal Categorical Core

Grothendieck Construction (Def 6.2.2.1, p. 444): Given I : C -> Set, the category of elements integral(I) has objects (c, x) with c in Ob(C) and x in I(c), and morphisms f : (c, x) -> (c', x') given by f : c -> c' in C such that I(f)(x) = x', equipped with a faithful projection functor pi : integral(I) -> C.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[El]`** — *a typed data element (c, x) in Ob(∫I)*
- **`[El2]`** — *a target data element (c', x') in Ob(∫I)*
- **`[ObC]`** — *a schema table c in Ob(C)*

### Functional Aspects (Morphisms)
- **`[El]` $\xrightarrow{\text{transitions via lifted arrow f where I(f)(x)=x' to}}$ `[El2]`**
- **`[El]` $\xrightarrow{\text{projects to its schema type via π : ∫I -> C}}$ `[ObC]`**

### Commutative Path Facts ($p \simeq q$)
- Application 6.2.2.5 (p. 447): The Grothendieck construction bridges relational databases/sheaves (functors I : C -> Set) and RDF triple graphs (the total category ∫I with type projection π).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-33` (flattens_instance_to_elements)** $\to$ [[database-schemas-instances]] (*Categorical Databases: Schemas (G, ≃) & Table Instances*, p. 245–266): Grothendieck construction ∫I flattens a database instance I : C -> Set into an RDF graph over C — `π : ∫_C I -> C`
- **`rho-34` (comma_categories_index_Kan_limits)** $\to$ [[universal-limits-and-cones]] (*Universal Limits, Cones & Terminal Objects in Cat*, p. 392–428): Comma categories (F ↓ d) and (d ↓ F) serve as the indexing diagrams for Kan extensions Σ_F and Π_F — `(F ↓ d) -> C`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-54` (category_of_elements_of_representable)** $\leftarrow$ [[presheaves-representables-yoneda]] (*Functor Categories, Presheaves, Representables & Yoneda's Lemma*, p. 493–517): The Grothendieck category of elements ∫Y_c of a representable functor Y_c = Hom_C(c,-) is the coslice comma category (c ↓ C) — `∫_C Hom_C(c, -) ≅ (c ↓ C)`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-06` — The Yoneda-Grothendieck-Instance Triangle** ([[presheaves-representables-yoneda]], [[grothendieck-construction-comma]], [[natural-transformations-functor-cat]]): Elements of a stalk I(c) correspond bijectively to objects over c in the Grothendieck category of elements ∫I and to natural transformations Y_c ⇒ I. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 439–460)

### `Definition 6.2.1.1` — [PDF Page 441]
> Definition 6.2.1.1. Let C be a category. The opposite category of C, denoted Cop, has the same objects as C, i.e., Ob(Cop)=Ob(C), and for any two objects c, c′, one defines HomCop(c,c′)≔HomC(c′,c).

### `Definition 6.2.2.1` — [PDF Page 444]
> Definition 6.2.2.1. Let C be a category, and let J:C→Set be a functor. The category of elements of J, denoted ∫CJ, is defined as follows: Ob(∫CJ)≔{(C,x)|C∈Ob(C),x∈J(C)};Hom∫CJ((C,x),(C′,x′))≔{f:C→C ′|J(f)(x)=x′}. There is a natural functor πJ:∫CJ→C. It sends each object (C,x)∈Ob(∫CJ) to the object C∈Ob(C). And it sends each morphism f : (C, x) → (C′, x′) to the morphism f : C → C′. We call πJ the projection functor.

### `Definition 6.2.3.1` — [PDF Page 451]
> Definition 6.2.3.1. Let C be a category, and let X⊆Ob(C) be a set of objects in C. The full subcategory of C spanned by X is the category, denoted COb=X, with objects Ob(COb=X)≔X and with morphisms HOMCOb=X(x,x′)≔HOMC(x,x′).

### `Definition 6.2.4.1` — [PDF Page 454]
> Definition 6.2.4.1. Let A→FC←GB be a cospan of categories. The comma category of C morphisms from F to G, denoted (F↓CG) or simply (F ↓ G), is the category with objects Ob(F↓G)={(a,b,f)|a∈Ob(A),b∈Ob(B),f:F(a)→G(b) in C}, and for any two objects (a, b, f) and (a′, b′, f′) the set Hom(F↓G) ((a, b, f), (a′, b′, f ′)) of morphisms (a, b, f) → (a′, b′, f′) is {(q,r)|q:a→a′ in A, r:b→b′ in B, such that f′○F(q)=G(r)○f}. In diagram form, There is a canonical functor (F↓G)→A, called left projecton, sending (a, b, f) to a, and a canonical functor (F↓G)→B, called right projection, sending (a, b, f) to b. A cospan A→FC←GB is reversible, i.e., we can flip

### `Proposition 6.2.1.4` — [PDF Page 441]
> Proposition 6.2.1.4. Let C and D be categories. One has (Cop)op=C. Also one has a canonical isomorphism Fun(C,D)≅Fun(Cop,Dop). This implies that a functor Cop→D can be identified with a functor C→Dop. Proof. This follows straightforwardly from the definitions.

### `Proposition 6.2.5.1` — [PDF Page 458]
> Proposition 6.2.5.1. The following isomorphisms exist for any small categories A,B,and C. A+0¯≅A. A+B≅B+A. (A+B)+C≅A+(B+C). A×0¯≅0¯. A×1¯≅A. A×B≅B×A. (A×B)×C≅A×(B×C). A×(B+C)≅(A×B)+(A×C). A0¯≅1¯. A1¯≅A. 0¯A≅0¯, if A≠0¯. 1¯A≅1¯. AB+C≅AB×AC. (AB)C≅AB×C. (A×B)C≅AC×BC. Proof. These are standard results; see Mac Lane [29]. __________________

### `Slogan 6.2.2.5` — [PDF Page 449]
> Slogan 6.2.2.5. The Grothendieck construction takes structured, tabulated data and flattens it by throwing it all into one big space. The projection functor is then tasked with remembering which box each datum originally came from.

### `Slogan 6.2.4.2` — [PDF Page 454]
> Slogan 6.2.4.2. When two categories A, ℬ can be interpreted in a common setting C, the comma category integrates them by recording how to move from A to B inside

### `Application 6.2.2.3` — [PDF Page 446]
> Application 6.2.2.3. Consider the following schema, first encountered in Example 4.5.2.1: And consider the instance J:C→Set, which we first encountered in (4.12) and (4.14):

### `Example 6.2.1.2` — [PDF Page 441]
> Example 6.2.1.2. If n ∈ ℕ is a natural number and n the corresponding discrete category, then nop = n. Recall the span category I = 2◅ from Definition 6.1.1.8. Its opposite is the cospan category Iop = 2▻, from Definition 6.1.1.23.

### `Example 6.2.1.7` (Simplicial sets) — [PDF Page 442]
> Example 6.2.1.7 (Simplicial sets). Recall from Example 5.3.4.4 the category Δ of linear orders [n]. For example, [1] is the linear order 0 1, and [2] is the linear order 0 1 2. Both [1] and [2] are objects of Δ. There are 6 morphisms from [1] to [2], which could be denoted HomΔ([1],[2])={(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)}. The category Δop turns out to be quite useful in algebraic topology. It is the indexing category for a combinatorial approach to the homotopy theory of spaces. That is, we can represent something like the category of spaces and continuous maps using the functor category Fun(Δop, Set), which is called the category of simpl

### `Example 6.2.2.2` — [PDF Page 444]
> Example 6.2.2.2. Let A be a set, and consider it as a discrete category. We saw in

### `Example 6.2.3.2` — [PDF Page 451]
> Example 6.2.3.2. The following are examples of full subcategories. For example, the category Fin of finite sets is the full subcategory of Set spanned by the finite sets. If X = {s ∈ Ob(Set) | s is finite}, then Fin = SetOb=X. If X = {P ∈ Ob(PrO) | P is a finite linear order)}, then FLin = PrOOb=X. If X = {[n] ∈ FLin | n ∈ ℕ} (see Example 5.3.4.4), then Δ = FLinOb=X. If X = {M ∈ Ob(Mon) | M is a group}, then Grp = MonOb=X. If X={C∈Ob(Cat)|C has one object}, then Mon = CatOb=X. If X = {n ∈ Ob(Fin) | n ∈ ℕ}, then there is an equivalence of categories Fin ≃ FinOb=X. If X = {(V, A, src, tgt) ∈ Ob(Grph) | A = ∅}, then Set ≅ GrphOb=X. If X={C∈Cat|C

### `Example 6.2.3.4` — [PDF Page 451]
> Example 6.2.3.4. Let C be a category, let X⊆Ob(C) be a set of objects, and let COb=X denote the full subcategory of C spanned by X. We can realize this as a fiber product of categories. Indeed, recall that for any set, we can form the indiscrete category on that set (see Example 5.3.4.3). In fact, we have a functor Ind: Set → Cat. Thus the function X→Ob(C) can be converted into a functor between indiscrete categories Ind(X)→Ind(Ob(C)). There is also a unique functor C→Ind(Ob(C)) sending each object to itself. Then the full subcategory of C spanned by X is the fiber product of categories,

### `Example 6.2.4.3` — [PDF Page 455]
> Example 6.2.4.3. Let C be a category and I:C→Set a functor. This example shows that the comma category construction captures the notion of taking the category of elements ∫CI (see Definition 6.2.2.1). Consider the set 1, the category Disc(1), and the functor F : Disc(1) → Set sending the unique object to the set 1. We use the cospan Disc(1¯)→FSet←IC. There is an isomorphism of categories ∫CI≅(F↓I). Indeed, an object in (F ↓ I) is a triple (a, b, f), where a ∈ Ob(Disc(1)), b∈Ob(C), and f : F(a) → I(b) is a morphism in Set. There is only one object in Disc(1), so this reduces to a pair (b, f), where b∈Ob(C) and f : {☺} → I(b). The set of functi

### `Remark 6.2.3.3` — [PDF Page 451]
> Remark 6.2.3.3. A subcategory C⊆D is (up to isomorphism) just a functor i:C→D that happens to be injective on objects and arrows. The subcategory is full if and only if i is a full functor in the sense of Definition 5.3.4.8.

### `Exercise 6.2.1.3` — [PDF Page 441]
> Exercise 6.2.1.3. Let C be the category from Example 6.1.3.18. Draw Cop.

### `Exercise 6.2.1.5` — [PDF Page 441]
> Exercise 6.2.1.5.

## 6. Page-by-Page Deep Index (PDF Pages 439–460)
- **Page 439** (`6.2 Other notions in Cat`): 6.2 Other notions in Cat This section discusses some additional notions about categories. Section 6.2.1 explains a kind of duality for categories, in which arrows are flipped. Reversing the order in a preorder is an example of this duality, as is the similarity between the definitions of limit and colimit. Section 6.2....
- **Page 440** (`6.2 Other notions in Cat`): ...
- **Page 441** (`6.2 Other notions in Cat`) · **Items:** Definition 6.2.1.1, Example 6.2.1.2, Exercise 6.2.1.3, Proposition 6.2.1.4, Exercise 6.2.1.5: 6.2.1 Opposite categories In the early days of category theory, and still today, people would sometimes discuss two different kinds of functors between categories: covariant functors and contravariant functors. Covariant functors are what this book calls functors. The reader may have come across the idea of contravaria...
- **Page 442** (`6.2 Other notions in Cat`) · **Items:** Exercise 6.2.1.6, Example 6.2.1.7: If C is a category and c∈Ob(C) is an initial object, does this imply that c is a terminal object in Cop? Exercise 6.2.1.6. In Exercises 5.2.3.2, 5.2.4.3, and 5.2.4.4 there were questions about whether a certain function Ob(C)→Ob(D) extended to a functor C→D. a. Does the function Open: Ob(Top) → Ob(PrO) extend to a func...
- **Page 443** (`6.2 Other notions in Cat`): ...
- **Page 444** (`6.2 Other notions in Cat`) · **Items:** Definition 6.2.2.1, Example 6.2.2.2: 6.2.2 Grothendieck construction Let C be a database schema (or category), and let J:C→Set be an instance. We have been drawing this in table form, but there is another standard way of laying out the data in J, called the resource descriptive framework, or RDF. Developed for the World Wide Web, RDF is a useful format wh...
- **Page 445** (`6.2 Other notions in Cat`) · **Items:** Exercise 5.3.3: Exercise 5.3.3.4 that a functor S : A → Set is the same thing as an A-indexed set, as discussed in Section 3.4.6.9. We follow Definition 3.4.6.11 and, for each a ∈ A, write Sa ≔ S(a). What is the category of elements of a functor S : A → Set? The objects of ∫A S are pairs (a, s), where a ∈ A and s ∈ S(a). Since A has n...
- **Page 446** (`6.2 Other notions in Cat`) · **Items:** Application 6.2.2.3: transforms a database instance into an RDF triple store. The reason is that the database schema was A, a discrete category that specifies no connections between data (it simply collects the data into bins). So let’s examine a more interesting database schema and instance. This is taken from Spivak [39]. Application 6.2...
- **Page 447** (`6.2 Other notions in Cat`): The category of elements of J:C→Set looks like this:...
- **Page 448** (`6.2 Other notions in Cat`) · **Items:** Exercise 6.2.2.4: In Diagram (6.11) of ∫CJ, ten arrows were omitted for ease of readability, for example, arrow •102 →first •Bertrand was omitted. How do we see the category of elements ∫CJ as an RDF triple store? For each arrow in ∫CJ, we take the triple consisting of the source vertex, the arrow name, and the target vertex. So the tri...
- **Page 449** (`6.2 Other notions in Cat`) · **Items:** Slogan 6.2.2.5, Exercise 6.2.2.6: Devise a schema C for which you can imagine an instance I:C→Set such that the category of elements ∫(I) is the triple store in (6.8). Slogan 6.2.2.5. The Grothendieck construction takes structured, tabulated data and flattens it by throwing it all into one big space. The projection functor is then tasked with rememberi...
- **Page 450** (`6.2 Other notions in Cat`): ...
- **Page 451** (`6.2 Other notions in Cat`) · **Items:** Definition 6.2.3.1, Example 6.2.3.2, Remark 6.2.3.3, Example 6.2.3.4: 6.2.3 Full subcategory Definition 6.2.3.1. Let C be a category, and let X⊆Ob(C) be a set of objects in C. The full subcategory of C spanned by X is the category, denoted COb=X, with objects Ob(COb=X)≔X and with morphisms HOMCOb=X(x,x′)≔HOMC(x,x′). Example 6.2.3.2. The following are examples of full subcategories. For e...
- **Page 452** (`6.2 Other notions in Cat`) · **Items:** Exercise 6.2.3.5: Exercise 6.2.3.5. Recall the sets 0, 1, 2 ∈ Ob(Set) from Notation 2.1.2.21. Including all identities and all compositions, how many morphisms are there in the full subcategory SetOb={0,1,2}?...
- **Page 453** (`6.2 Other notions in Cat`): ...
- **Page 454** (`6.2 Other notions in Cat`) · **Items:** Definition 6.2.4.1, Slogan 6.2.4.2: 6.2.4 Comma categories Category theory includes a highly developed and interoperable catalogue of materials (categories such as [n], GrIn, PrO, etc.) and production techniques for making new categories from old. One such was the full subcategory idea in the previous section—given any category and any subset of objects,...
- **Page 455** (`6.2 Other notions in Cat`) · **Items:** Example 6.2.4.3, Exercise 6.2.4.4, Exercise 6.2.4.5: C. Example 6.2.4.3. Let C be a category and I:C→Set a functor. This example shows that the comma category construction captures the notion of taking the category of elements ∫CI (see Definition 6.2.2.1). Consider the set 1, the category Disc(1), and the functor F : Disc(1) → Set sending the unique object to the set 1. ...
- **Page 456** (`6.2 Other notions in Cat`) · **Items:** Exercise 6.2.4.6: Exercise 6.2.4.6. Let C be a category. a. If c∈C is an initial object, what is the comma category for the cospan 1¯→cC←idCC? b. If d∈C is a terminal object, what is the comma category for the cospan C→idCC←dC?...
- **Page 457** (`6.2 Other notions in Cat`): ...
- **Page 458** (`6.2 Other notions in Cat`) · **Items:** Proposition 6.2.5.1: 6.2.5 Arithmetic of categories Section 3.4.3 summarized some of the properties of products, coproducts, and exponentials for sets, showing that they lined up precisely with familiar arithmetic properties of natural numbers. We can do the same for categories. In the following proposition, we denote the coproduct of two ...
- **Page 459** (`6.2 Other notions in Cat`): 1Given R1 ⊆ X1 × X1, R2 ⊆ X2 × X2, take R1 × R2 ⊆ (X1 × X2) × (X1 × X2). 2The result is not necessarily inspiring, but at least computing it is straightforward. 3The names X × Y and π1, π2 are not mathematically important; they are pedagogically useful. 4Note that (0, 0) is not related to anything else. 5Given R1 ⊆ X1 ...
- **Page 460** (`6.2 Other notions in Cat`): ...
