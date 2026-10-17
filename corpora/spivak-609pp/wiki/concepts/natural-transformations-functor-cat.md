---
id: natural-transformations-functor-cat
title: "Natural Transformations & The Category of Database Instances"
type: SheafStalk
chapter: 5
section: "5.3.1–5.3.3"
pdf_pages: "338–370"
symbol: "α : F ⇒ G ∈ Fun(C, D)"
layer: "Core Category Theory"
extracted_declarations: 54
restricts_to: [functors-structure-maps, database-schemas-instances]
glues_with: [categorical-equivalence-cat-sch, presheaves-representables-yoneda, monads-and-contextual-computation]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Natural Transformations & The Category of Database Instances (`α : F ⇒ G ∈ Fun(C, D)`)

> **Sheaf Stalk Location:** Chapter 5 (Basic Category Theory: Categories, Functors, Natural Transformations & Cat ≃ Sch) · Section `5.3.1–5.3.3` · **PDF Pages 338–370**

## 1. Epistemic Worldview & Intuition

A natural transformation alpha : F => G compares two parallel functors F, G : C -> D by providing a family of component morphisms alpha_x : F(x) -> G(x) in D that commute naturally with every morphism f : x -> y in C. When F, G : C -> Set are database instances, natural transformations are database homomorphisms.

## 2. Formal Categorical Core

Definition 5.3.1.2 (p. 341): Given functors F, G : C -> D, a natural transformation alpha : F => G assigns to each x in Ob(C) a component alpha_x : F(x) -> G(x) such that for every f : x -> y in C, the naturality square G(f) o alpha_x = alpha_y o F(f) commutes. Functors C -> D and natural transformations form the functor category D^C = Fun(C, D).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Fx]`** — *an element in source instance table F(x)*
- **`[Fy]`** — *an element in source instance table F(y)*
- **`[Gx]`** — *an element in target instance table G(x)*
- **`[Gy]`** — *an element in target instance table G(y)*

### Functional Aspects (Morphisms)
- **`[Fx]` $\xrightarrow{\text{maps along foreign key F(f) to}}$ `[Fy]`**
- **`[Fx]` $\xrightarrow{\text{translates via component α_x to}}$ `[Gx]`**
- **`[Fy]` $\xrightarrow{\text{translates via component α_y to}}$ `[Gy]`**
- **`[Gx]` $\xrightarrow{\text{maps along foreign key G(f) to}}$ `[Gy]`**

### Commutative Path Facts ($p \simeq q$)
- Naturality Square Law: G(f) ∘ α_x = α_y ∘ F(f) for all f : x -> y in C (Definition 5.3.1.2, p. 341).
- Proposition 5.3.3.2 (p. 366): Database instance homomorphisms on schema C are precisely natural transformations between functors C -> Set.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-27` (2_morphisms_between_functors)** $\to$ [[functors-structure-maps]] (*Functors: Structure-Preserving Maps Between Worldviews*, p. 285–337): Natural transformations α : F ⇒ G are morphisms between functors in Fun(C, D) — `Hom_{Fun(C,D)}(F, G) = Nat(F, G)`
- **`rho-28` (instance_homomorphisms)** $\to$ [[database-schemas-instances]] (*Categorical Databases: Schemas (G, ≃) & Table Instances*, p. 245–266): Natural transformations between functors I, J : C -> Set are database instance homomorphisms — `Hom_{C-Inst}(I, J) = Nat(I, J)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-30` (invertible_up_to_natural_iso)** $\leftarrow$ [[categorical-equivalence-cat-sch]] (*Equivalence of Categories & Theorem Cat ≃ Sch*, p. 371–391): Equivalence of categories F : C ⇄ D : G requires natural isomorphisms GF ≅ id_C, FG ≅ id_D — `GF ≅ id_C, FG ≅ id_D`
- **`rho-40` (yoneda_embeds_via_Nat)** $\leftarrow$ [[presheaves-representables-yoneda]] (*Functor Categories, Presheaves, Representables & Yoneda's Lemma*, p. 493–517): Yoneda's lemma identifies natural transformations Hom_{C-Set}(Y_c, I) with stalk elements I(c) — `Nat(Hom_C(c,-), I) ≅ I(c)`
- **`rho-47` (endofunctor_monoid_in_Fun)** $\leftarrow$ [[monads-and-contextual-computation]] (*Monads (T, η, μ): Formalizing Experimental & Computational Context*, p. 527–539): A monad (T, η, μ) is an endofunctor T : C -> C with natural transformations η : id ⇒ T and μ : T² ⇒ T — `μ ∘ Tμ = μ ∘ μT`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-06` — The Yoneda-Grothendieck-Instance Triangle** ([[presheaves-representables-yoneda]], [[grothendieck-construction-comma]], [[natural-transformations-functor-cat]]): Elements of a stalk I(c) correspond bijectively to objects over c in the Grothendieck category of elements ∫I and to natural transformations Y_c ⇒ I. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 338–370)

### `Definition 5.3.1.2` — [PDF Page 341]
> Definition 5.3.1.2. Let C and D be categories, and let F:C→D and G:C→D be functors. A natural transformation α from F to G, denoted α : F → G and depicted is defined as follows. One announces some constituents (A. components) and shows that they conform to a law (1. naturality squares). Specifically, one announces A. for each object X∈Ob(C), a morphism αX : F (X) → G(X) in D, called the X-component of α. One must then show that the following natural transformation law holds: 1. For every morphism f : X → Y in C, the square (5.10), called the naturality square for f, must commute: The set of natural transformations F → G is denoted Nat(F, G).

### `Definition 5.3.2.16` (Whiskering) — [PDF Page 359]
> Definition 5.3.2.16 (Whiskering). Let B,C,D, and E be categories, let G1,G2:C→D be functors, and let α : G1 → G2 be a natural transformation. Suppose that F:B→C (resp. H:D→E) is a functor as depicted here: Then the prewhiskering of α by F, denoted α ◇ F : G1 ○ F → G2 ○ F (resp. the post-whiskering of α by H, denoted H ◇ α : H ○ G1 → H ○ G2), is defined as follows. For each b∈Ob(B) the component (α ◇ F)b : G1 ○ F(b) → G2 ○ F(b) is defined to be αF(b) (resp. for each c∈Ob(C), the component (H ◇ α)c : H ○ G1(c) → H ○ G2(c) is defined to be H(αc)). Checking that the naturality squares commute (in each case) is straightforward.

### `Definition 5.3.2.18` (Horizontal composition of natural transformations) — [PDF Page 360]
> Definition 5.3.2.18 (Horizontal composition of natural transformations). Let B, C, and D be categories, let F1,F2:B→C and G1,G2:C→D be functors, and let α : F1 → F2 and β : G1 → G2 be natural transformations, as depicted here: By pre- and postwhiskering in one order or the other we get the following diagram: It is straightforward to show that this diagram commutes, so we can take the composition to be the definition of the horizontal composition: β◇α:G1○F1→G2○F2.

### `Definition 5.3.3.1` — [PDF Page 364]
> Definition 5.3.3.1. Let C be a schema (or category). The category of instances on C, denoted C−Set, is Fun(C,Set). Its objects are C-instances (i.e., functors C→Set), and its morphisms are natural transformations.

### `Definition 3.4.6` — [PDF Page 365]
> Definition 3.4.6.11 actually gives us the objects and morphisms of a category, say, the category of A-indexed sets, in that it tells us that the objects and morphisms are merely the A-indexed sets and the A-indexed functions. Let us denote the category of A-indexed sets A–Set; this exercise is asking for a category A for which

### `Theorem 5.3.2.20` (Interchange) — [PDF Page 360]
> Theorem 5.3.2.20 (Interchange).

### `Proposition 5.3.1.5` — [PDF Page 342]
> Proposition 5.3.1.5. Let C and D be categories, let F,G:C→D be functors, and for every object c∈Ob(C), let αc:F(c)→G(c) be a morphism in D. Suppose given a path c0→ f1 c1→ f2 ⋯→ fn cn such that for each arrow fi in it, the following naturality square commutes: Then the naturality square for the composite p ≔ fn ○ ⋯ ○ f2 ○ f1 : c0 → cn

### `Proposition 5.3.2.2` — [PDF Page 353]
> Proposition 5.3.2.2. Let C and D be categories. There exists a category, called the category of functors from C to D and denoted Fun(C,D), whose objects are the functors C→D and whose morphisms are the natural transformations, HomFun(C,D)(F,G)={α:F→G|α is a natural transformation}. Under this setup, there are indeed identity natural transformations and a composition formula for natural transformations, so we have defined a questionable category Fun(C,D). The category laws hold, so it is indeed a category. Proof. Exercise 5.3.1.13 showed that for any functor F:C→D, there is an identity natural transformation idF : F → F (its component at c∈Ob(

### `Proposition 5.3.2.12` (Natural isomorphism) — [PDF Page 356]
> Proposition 5.3.2.12 (Natural isomorphism). Let C and D be categories, and let F,G:C→D be functors. A natural transformation α : F → G is an isomorphism in Fun(C,D) if and only if the component αc : F(c) → G(c) is an isomorphism for each object c∈Ob(C). In this case α is called a natural isomorphism. Proof. First, suppose that α is an isomorphism with inverse β : G → F, and let βc : G(c) → F (c) denote its c component. We know that α ○ β = idG and β ○ α = idF. Using the definitions of composition and identity given in Proposition 5.3.2.2, this means that for every c∈Ob(C), we have αc ○ βc = idG(c) and βc ○ αc = idF(c); in other words, αc is a

### `Slogan 5.3.1.1` — [PDF Page 340]
> Slogan 5.3.1.1. What does it mean to say that concatenation of lists is natural with respect to translation? It means that concatenating then translating is the same thing as translating then concatenating. Let’s make this concrete. Let X = {a, b, c}, let Y = {1, 2, 3}, and let f : X → Y assign f(a) = 1, f(b) = 1, f(c) = 2. The naturality condition says the following for any list of lists of X’s, in particular, for [[a, b], [a, c, a, b, c], [c]] ∈ List ○ List(X): The top right path is concatenating then translating, and the left bottom path is translating then concatenating, and one sees here that they do the same thing. Here is how the prece

### `Application 5.3.1.12` — [PDF Page 346]
> Application 5.3.1.12. Figure 4.2 showed a finite state machine on alphabet Σ = {a, b}, and Example 4.1.3.1 shows its associated action table. Imagine this was your model for understanding the behavior of some system when acted on by commands a and b. Suppose a colleague tells you he has a more refined model that fits with the same data. His model has six states rather than three, but it is compatible. What might that mean? Both the original state machine, X, the proposed model, Y, and their associated action tables are shown in Figure 5.1 (see page 247). How are these models compatible? In the table for Y, if one removes the distinction betwe

### `Example 5.3.1.4` — [PDF Page 342]
> Example 5.3.1.4. Consider the following categories C≅[1] and D≅[2]: Consider the functors F, G : [1] → [2], where F(0) = A, F(1) = B, G(0) = A, and G(1) = C. It turns out that there is only one possible natural transformation F → G; we call it α and explore its naturality square. The components of α : F → G are shown in green. These components are α0 = idA : F(0) → G(0) and α1 = g : F(1) → G(1). The naturality square for p : 0 → 1 is shown twice below, once with notation following that in (5.10) and once in local notation: It is clear that this diagram commutes, so the components α0 and α1 satisfy the law of Definition 5.3.1.2, making α a nat

### `Example 5.3.1.6` — [PDF Page 343]
> Example 5.3.1.6. Let C=D=[1] be the linear order of length 1, thought of as a category (by Proposition 5.2.1.13). There are three functors C→D, which we can

### `Example 5.2.2` — [PDF Page 345]
> Example 5.2.2.2). There is exactly one functor S:1¯→Loop. Characterize the natural transformations α : S → S.

### `Example 5.3.1.14` — [PDF Page 348]
> Example 5.3.1.14. Let [1] ∈ Ob(Cat) be the free arrow category described in

### `Example 5.3.1.15` — [PDF Page 349]
> Example 5.3.1.15. Recall that to any graph G we can associate the paths-graph Paths(G) (see Example 5.1.2.25). This is a functor Paths: Grph → Grph. There is also an identity functor idGrph : Grph → Grph. A natural transformation η : idGrph → Paths would consist of a graph homomorphism ηG : idGrph(G) → Paths(G) for every graph G. But idGrph(G) = G by definition, so we need ηG : G → Paths(G). Recall that Paths(G) has the same vertices as G, and every arrow in G counts as a path (of length 1). So there is an obvious graph homomorphism from G to Paths(G). It is not hard to see that the necessary naturality squares commute.

### `Example 5.3.1.16` — [PDF Page 349]
> Example 5.3.1.16. For any graph G we can associate the paths-graph Paths(G), and can do that twice to yield a new graph Paths(Paths(G)). Let’s think through what a path of paths in G is. It is a head-to-tail sequence of arrows in Paths(G), meaning a head-to-tail sequence of paths in G. These composable sequences of paths (or “paths of paths”) are the individual arrows in Paths(Paths(G)). The vertices in Paths(G) and Paths(Paths(G)) are the same as those in G, and all source and target functions are as expected. Clearly, given such a sequence of paths in G, we could compose them to one big path in G with the same endpoints. In other words, for

### `Example 5.3.1.20` (Graph homomorphisms are natural transformations) — [PDF Page 350]
> Example 5.3.1.20 (Graph homomorphisms are natural transformations). As discussed (see diagram (5.8)), there is a category GrIn for which a functor G : GrIn → Set is the same thing as a graph. Namely, we have

## 6. Page-by-Page Deep Index (PDF Pages 338–370)
- **Page 338** (`5.3 Natural transformations`): 5.3 Natural transformations The Big 3 of category theory are categories, functors, and natural transformations. This section introduces the last of these, natural transformations. Category theory was originally invented to discuss natural transformations. These were sufficiently conceptually challenging that they requi...
- **Page 339** (`5.3 Natural transformations`): ...
- **Page 340** (`5.3 Natural transformations`) · **Items:** Slogan 5.3.1.1: 5.3.1 Definition and examples Let’s begin with an example. There is a functor List: Set → Set, which sends a set X to the set List(X) consisting of all lists whose entries are elements of X. Given a morphism f : X → Y, we can transform a list with entries in X into a list with entries in Y by applying f to each entry (...
- **Page 341** (`5.3 Natural transformations`) · **Items:** Definition 5.3.1.2, Remark 5.3.1.3: 5.3.1.2. The categories C and D are both Set, the functor F:C→D is List ○ List, and the functor G:C→D is List. The natural transformation is µ : List○List → List. It can be depicted: Definition 5.3.1.2. Let C and D be categories, and let F:C→D and G:C→D be functors. A natural transformation α from F to G, denoted α : F...
- **Page 342** (`5.3 Natural transformations`) · **Items:** Example 5.3.1.4, Proposition 5.3.1.5: once we know it satisfies Definition 5.3.1.2, we drop the “questionably” part. Example 5.3.1.4. Consider the following categories C≅[1] and D≅[2]: Consider the functors F, G : [1] → [2], where F(0) = A, F(1) = B, G(0) = A, and G(1) = C. It turns out that there is only one possible natural transformation F → G; we call ...
- **Page 343** (`5.3 Natural transformations`) · **Items:** Example 5.3.1.6: also commutes. In particular, the naturality square commutes for every identity morphism idc. Proof. When n = 0, we have a path of length 0 starting at each c∈Ob(C). It vacuously satisfies the condition, so we need to see that its naturality square commutes. But this is clear because functors preserve identities. The r...
- **Page 344** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.1.7, Exercise 5.3.1.8: write as (0, 0), (0, 1), and (1, 1); these are depicted left to right as follows: These are just functors so far. What are the natural transformations say, α : (0, 0) → (0, 1)? To specify a natural transformation, we must specify a component for each object in C. In this case α0 : 0 → 0 and α1 : 0 → 1. There is only on...
- **Page 345** (`5.3 Natural transformations`) · **Items:** Example 5.2.2, Exercise 5.3.1.9, Exercise 5.3.1.10, Exercise 5.3.1.11: Let 1 denote the discrete category on one object, Ob(1) = {1}, and let Loop denote the category with one object Ob(Loop)={s} and HomLoop(s,s)=ℕ (see Example 5.2.2.2). There is exactly one functor S:1¯→Loop. Characterize the natural transformations α : S → S. Exercise 5.3.1.9. Let [1] denote the free arrow category, as ...
- **Page 346** (`5.3 Natural transformations`) · **Items:** Application 5.3.1.12: 3.2.3.5 or Warning 6.1.3.14). If C=[1] is the linear order of length 1, and F:C→Set is any functor, what does it mean to give a natural transformation {d}C→F? Application 5.3.1.12. Figure 4.2 showed a finite state machine on alphabet Σ = {a, b}, and Example 4.1.3.1 shows its associated action table. Imagine this was yo...
- **Page 347** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.1.13: This can only be checked by going through and making sure that certain things match, as specified by (5.11); this is spelled out in detail. The columns that should match are those whose entries are written in blue. These correspond to the left bottom composites being matched with the top right composites in the natural...
- **Page 348** (`5.3 Natural transformations`) · **Items:** Solution 5.3.1.13, Example 5.3.1.14, Exercise 5.1.2: b. What components is he suggesting? c. Are the components natural? Solution 5.3.1.13. a. He is certainly telling us about a natural transformation α : F → F, and he seems to be telling us that it will somehow act like an identity. b. To give a questionably natural transformation, we need to provide, for every c∈Ob(C) ...
- **Page 349** (`5.3 Natural transformations`) · **Items:** Example 5.3.1.15, Example 5.3.1.16: The condition for α to be a natural transformation is that this square commutes. In other words, a functor [1]→D is a morphism in D and a natural transformation between two such functors is just a commutative square in D . Example 5.3.1.15. Recall that to any graph G we can associate the paths-graph Paths(G) (see Examp...
- **Page 350** (`5.3 Natural transformations`) · **Items:** Remark 5.3.1.17, Exercise 5.3.1.18, Exercise 5.3.1.19, Example 5.3.1.20: Remark 5.3.1.17. Example 5.3.1.15 showed that there is a natural transformation comparing each graph to its paths-graph. There is a formal sense in which a category is nothing more than a kind of reverse mapping. That is, to specify a category is the same thing as to specify a graph G together with a graph homomorphism...
- **Page 351** (`5.3 Natural transformations`): A natural transformation of two such functors α : G → G′ involves two components, αAr : G(Ar) → G′(Ar) and αVe : G(Ve) → G′(Ve), and two naturality squares, one for src and one for tgt. This is precisely the same thing as a graph homomorphism, as defined in Definition 4.3.3.1....
- **Page 352** (`5.3 Natural transformations`): ...
- **Page 353** (`5.3 Natural transformations`) · **Items:** Proposition 5.3.2.2: 5.3.2 Vertical and horizontal composition This section discusses two types of compositions for natural transformations. The terms vertical and horizontal are used to describe them; these terms come from the following pictures: We use the symbol ○ to denote vertical composition, so we have β ○ α : F → H in the left-hand...
- **Page 354** (`5.3 Natural transformations`) · **Items:** Notation 5.3.2.3, Example 5.3.2.4, Exercise 5.3.2.5, Notation 5.3.2.6, Exercise 5.3.2.7: Given a natural transformation α : F → G and a natural transformation β : G → H, we need a composite β ○ α. We propose the transformation γ : F → H having components βc ○ αc for every c∈Ob(C). To see that γ is indeed a natural transformation, one simply puts together naturality squares for α and β to get naturality squ...
- **Page 355** (`5.3 Natural transformations`) · **Items:** Example 5.3.2.8, Exercise 5.3.2.9, Exercise 5.3.2.10: Let n ∈ ℕ, and let n be the set with n elements, considered as a discrete category.13 In other words, we write n to mean what should really be called Disc(n). Describe the category Fun(3, 2). Example 5.3.2.8. Let 1 denote the discrete category with one object (also known as the trivial monoid). For any category C, we i...
- **Page 356** (`5.3 Natural transformations`) · **Items:** Proposition 5.3.2.12: Proposition 5.3.2.12 (Natural isomorphism). Let C and D be categories, and let F,G:C→D be functors. A natural transformation α : F → G is an isomorphism in Fun(C,D) if and only if the component αc : F(c) → G(c) is an isomorphism for each object c∈Ob(C). In this case α is called a natural isomorphism. Proof. First, supp...
- **Page 357** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.2.13, Example 5.3.2.15: To complete the proof we need only show that F(h) ○ βc = βc′ ○ G(h). This can be shown by a “diagram chase.” We go through it symbolically, for demonstration. The following three equalities come from the three check marks in the (5.14). F(h)○βc=βc′○αc′○F(h)○βc=βc′○G(h)○αc○βc=βc′○G(h). Exercise 5.3.2.13. Recall from App...
- **Page 358** (`5.3 Natural transformations`): We can compose X and Y with F as in the diagram below to get functors Y ○ F and X ○ F, both of type M′→Set. These would be as follows:14 The map α is what sent both State 1A and State 1B in Y to State 1 in X, and so on. We can see that the same α works now: the p columns of the tables respect that mapping; that is, the...
- **Page 359** (`5.3 Natural transformations`) · **Items:** Definition 5.3.2.16, Exercise 5.3.2.17, Solution 5.3.2.17: whiskering. We used α : Y → X to get a natural transformation Y ○ F → X ○ F . It is a kind of horizontal composition of natural transformation. Definition 5.3.2.16 (Whiskering). Let B,C,D, and E be categories, let G1,G2:C→D be functors, and let α : G1 → G2 be a natural transformation. Suppose that F:B→C (resp. H:D→E) i...
- **Page 360** (`5.3 Natural transformations`) · **Items:** Definition 5.3.2.18, Remark 5.3.2.19, Theorem 5.3.2.20: Definition 5.3.2.18 (Horizontal composition of natural transformations). Let B, C, and D be categories, let F1,F2:B→C and G1,G2:C→D be functors, and let α : F1 → F2 and β : G1 → G2 be natural transformations, as depicted here: By pre- and postwhiskering in one order or the other we get the following diagram: It is stra...
- **Page 361** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.2.21: Given a setup of categories, functors, and natural transformations as shown, we have (β2○β1)◇(α2○α1)=(β2◇α2)○(β1◇α1). Proof. One need only observe that each square commutes in the following diagram, so taking either outer path to get (β2 ○ β1) ◇ (α2 ○ α1) yields the same morphism as taking the diagonal path, (β2 ◇ α2) ...
- **Page 362** (`5.3 Natural transformations`) · **Items:** Solution 5.3.2.21: such that α : F → F′ and β : G → G′ are natural isomorphisms. Show that β◇α : G○F → G′ ○ F′ is a natural isomorphism. Solution 5.3.2.21. Let α′ : F′ → α and β′ : G′ → G be the inverses of α and β respectively. To check that β ◇ α is an isomorphism, we use Theorem 5.3.2.20 (and Exercise 5.3.2.17) to see that (β◇α)○(β′◇α...
- **Page 363** (`5.3 Natural transformations`): ...
- **Page 364** (`5.3 Natural transformations`) · **Items:** Definition 5.3.3.1, Remark 5.3.3.2, Example 5.1.1, Example 5.3.3.3: 5.3.3 The category of instances on a database schema Section 5.2.2 showed that schemas are presentations of categories, and Section 5.4 shows that in fact the category of schemas is equivalent to the category of categories. This section therefore takes license to blur the distinction between schemas and categories. If ...
- **Page 365** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.3.4, Solution 5.3.3.4, Definition 3.4.6: There are 343 natural transformations I → J. Perhaps some of them make more sense than others, e.g., we could hope that the numbers in I corresponded to the numbers after the hyphen in J or perhaps to what seems to be the date in January. Knowing something like this would reduce this to only a few options out of 343 po...
- **Page 366** (`5.3 Natural transformations`) · **Items:** Example 5.3.3.5: there is an isomorphism A−Set→ ≅ Fun(A,Set). And indeed there is. Let A=Disc(A) be the discrete category on A objects. Then a functor S:A→Set is just a set S(a) for every a ∈ A, and a morphism S → S′ is just a component fa : S(a) → S′(a) for each a ∈ A. These coincide exactly with the notions of A-indexed set and of ma...
- **Page 367** (`5.3 Natural transformations`): To give a natural transformation α : I → J, we give two components: one for Arrow and one for Vertex. We need to say where each vertex in I goes in J, and we need to say where each arrow in I goes in J. The naturality squares insist that if we specify that g ↦ j, for example, then we had better specify that w ↦ r and t...
- **Page 368** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.3.6, Exercise 5.3.3.7, Solution 5.3.3.7: Exercise 5.3.3.6. If I,J:G→Set, as in Example 5.3.3.5, how many natural transformations are there J → I? Exercise 5.3.3.7. Let GrIn be the graph-indexing category, and let YA : GrIn → Set denote the following instance: Let I : GrIn → Set be as in Example 5.3.3.5. a. How many natural transformations are there YA → I? b....
- **Page 369** (`5.3 Natural transformations`): How does this works? What might g mean as a natural transformation YA → I? To give a questionably natural transformation α : YA → I, we need to give a component αAr : {a} → {f, g, h} and a component αVe : {v0, v1} → {v, w, x}. Since we have g in mind, let’s put αAr(a) ≔ g. There are 32 choices for αVe, but only one is ...
- **Page 370** (`5.3 Natural transformations`): ...
