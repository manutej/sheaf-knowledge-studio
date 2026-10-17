---
id: categorical-equivalence-cat-sch
title: "Equivalence of Categories & Theorem Cat ≃ Sch"
type: SheafStalk
chapter: 5
section: "5.3.4–5.4"
pdf_pages: "371–391"
symbol: "Cat ≃ Sch"
layer: "Core Category Theory"
extracted_declarations: 29
restricts_to: [database-schemas-instances, natural-transformations-functor-cat]
glues_with: [sheaf-of-ologged-concepts-descent]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Equivalence of Categories & Theorem Cat ≃ Sch (`Cat ≃ Sch`)

> **Sheaf Stalk Location:** Chapter 5 (Basic Category Theory: Categories, Functors, Natural Transformations & Cat ≃ Sch) · Section `5.3.4–5.4` · **PDF Pages 371–391**

## 1. Epistemic Worldview & Intuition

Two categories C and D are equivalent (C ≃ D) if there exist functors F : C -> D and G : D -> C whose composites GF ≅ id_C and FG ≅ id_D are naturally isomorphic to identities. Spivak proves the landmark theorem Cat ≃ Sch: the category of small categories is equivalent to the category of database schemas.

## 2. Formal Categorical Core

Equivalence of categories (Def 5.3.4.1, p. 371): F : C -> D is an equivalence iff it is fully faithful and essentially surjective. Theorem 5.4.2.5 (p. 389): The category Cat of small categories and the category Sch of schemas (G, ~) and schema morphisms are equivalent via Path_~ : Sch -> Cat and Grph_~ : Cat -> Sch.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Sch]`** — *a database schema / olog (G, ≃) in Sch*
- **`[Cat]`** — *a small category C in Cat*
- **`[Inst]`** — *a database instance I on (G, ≃)*
- **`[Func]`** — *a Set-valued functor F : C -> Set*

### Functional Aspects (Morphisms)
- **`[Sch]` $\xrightarrow{\text{presents category via L : Sch -> Cat}}$ `[Cat]`**
- **`[Cat]` $\xrightarrow{\text{extracts canonical schema via R : Cat -> Sch}}$ `[Sch]`**
- **`[Inst]` $\xrightarrow{\text{corresponds 1-to-1 with}}$ `[Func]`**

### Commutative Path Facts ($p \simeq q$)
- L ∘ R ≅ id_Cat and R ∘ L ≅ id_Sch (Section 5.4.2, p. 386–391).
- This equivalence legitimizes treating every olog or database schema as a category and every dataset as a presheaf/copresheaf.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-29` (equivalence_of_schemas_and_categories)** $\to$ [[database-schemas-instances]] (*Categorical Databases: Schemas (G, ≃) & Table Instances*, p. 245–266): Every schema (G, ≃) presents a category and every category is presented by a canonical schema — `Cat ≃ Sch (Sec 5.4)`
- **`rho-30` (invertible_up_to_natural_iso)** $\to$ [[natural-transformations-functor-cat]] (*Natural Transformations & The Category of Database Instances*, p. 338–370): Equivalence of categories F : C ⇄ D : G requires natural isomorphisms GF ≅ id_C, FG ≅ id_D — `GF ≅ id_C, FG ≅ id_D`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-46` (glues_categorical_schemas)** $\leftarrow$ [[sheaf-of-ologged-concepts-descent]] (*Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data*, p. 521–526): Each stalk O(v) is an olog/schema (~= category), glued along restriction schema morphisms O(v)->O(u) — `ρ_{v,u} ∈ Hom_Sch(O(v), O(u))`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-01` — The Schema-Category-Instance Gluing Triangle** ([[categorical-equivalence-cat-sch]], [[database-schemas-instances]], [[functors-structure-maps]]): Translating a category C to a schema R(C) and taking instances agrees with taking Set-valued functors Fun(C, Set). *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 371–391)

### `Definition 5.3.4.1` (Equivalence of categories) — [PDF Page 371]
> Definition 5.3.4.1 (Equivalence of categories). Let C and C′ be categories. A functor F:C→C′ is called an equivalence of categories and denoted F:C→≃C′16 if there exists a functor F′:C′→C and natural isomorphisms α:idC→ ≅ F′○F and α ′:idC′→ ≅ F○F′. In this case we say that F and F′ are mutually inverse equivalences. Suppose we are given functors F:C→C′ and F′:C′→C. We want to know something about the round-trips on C and on C′; we want to know the same kind of information about each round-trip, so let’s concentrate on the C side. We want

### `Definition 5.3.4` — [PDF Page 372]
> Definition 5.3.4.1)?

### `Definition 5.3.4.8` (Full and faithful functors) — [PDF Page 375]
> Definition 5.3.4.8 (Full and faithful functors). Let C and D be categories, and let F:C→D be a functor. For any two objects c,c′∈Ob(C), there is a function HomF(c,c′):HomC(c,c′)→HomD(F(c),F(c′)) guaranteed by the definition of functor. We say that F is a full functor if HomF(c, c ′) is surjective for every c,c′∈Ob(C). We say that F is a faithful functor if HomF(c, c′) is injective for every c, c′. We say that F is a fully faithful functor if HomF(c, c′)

### `Definition 5.4.1.2` (Schema morphism) — [PDF Page 382]
> Definition 5.4.1.2 (Schema morphism). Let G = (V, A, src, tgt) and G′ = (V′, A′, src′, tgt′) be graphs, and let C=(G,≃G) and C′=(G′,≃G′) be schemas. A schema morphism F from C to D, denoted F:C→D, is a graph homomorphism 19 F:G→Paths(G′) that satisfies the following condition for any paths p and q in G: if p≃G q then PathsF(p) ≃G′ PathsF(q).(5.18) Two schema morphisms E,F:C→C′ are considered identical if they agree on vertices (i.e., E0 = F0) and if, for every arrow f in G, there is a path equivalence in G′ E1(f)≃G′F1(f). We now define the category of schemas, denoted Sch, to be the category whose

### `Definition 5.4.1` — [PDF Page 387]
> Definition 5.4.1.2, any other choice will give the identical morphism of schemas. It is easy to show that each round-trip is equal to the identity (again up to the notion of equality of schema morphism given in Definition 5.4.1.2).

### `Definition 4.3.2.1` — [PDF Page 390]
> Definition 4.3.2.1.

### `Theorem 5.4.2.3` — [PDF Page 387]
> Theorem 5.4.2.3. The functors L:Sch⇄Cat:R are mutually inverse equivalences of categories. Sketch of proof. It is clear that there is a natural isomorphism α:idCat→≅L○R; i.e., for any category C, there is an isomorphism C≅L(R(C)). Before giving an isomorphism β:idSch→≅R○L, we look at R(L(G))≕( G′,≃ ′) for a schema G=(G,≃). Write G = (V, A, src, tgt) and G′ = (V ′, A′, src′, tgt′). On vertices we have V = V′. On arrows we have A′ = PathG/≃. The congruence ≃′ for R(L(G)) is imposed in (5.20). Under ≃′, every path of paths in G is made equivalent to its concatenation, considered as a single path of length 1 in G′. There is a natural transformati

### `Proposition 5.3.4.11` — [PDF Page 376]
> Proposition 5.3.4.11. Let C and C′ be categories, and let F:C→C′ be an equivalence of categories. Then F is fully faithful. Sketch of proof. Suppose F is an equivalence, so we can find a functor F′:C′→C and natural isomorphisms α:idC→≅F′○F and α′:idC′→≅F○F′. We need to know that for any objects c,d∈Ob(C), the map HomF(c,d):HomC(c,d)→HomC′(Fc,Fd) is bijective. Consider the following diagram One can check that HomC(αc−1,αd) is bijective, so the vertical function is surjective by Exercise 3.4.5.3. The fact that HomC′((αFC′)−1,αFD′) is bijective implies that the vertical function is injective. Thus we know that HomF′ (Fc, Fd)

### `Slogan 5.4.1.3` — [PDF Page 383]
> Slogan 5.4.1.3. A schema morphism sends vertices to vertices, arrows to paths, and path equivalences to path equivalences.

### `Construction 5.4.2.1` (From schema to category) — [PDF Page 386]
> Construction 5.4.2.1 (From schema to category). We first define a functor L : Sch → Cat. Let C=(G,≃) be a schema, where G = (V, A, src, tgt). Define L(C) to be the category with Ob(L(C))=V, and with HomL(C)(v1,v2)≔PathG(v,w)/≃, i.e., the set of paths in G modulo the path equivalence relation for C. The composition of morphisms is defined by concatenation of paths, and part (4) of Definition 4.5.2.3 implies that such composition is well defined. We have thus defined L on objects of Sch. Given a schema morphism F:C→C′, where C′=( G′,≃′), we need to produce a functor L(F):L(C)→L(C′). The objects of L(C) and L(C′) are the vertices of G and G′ res

### `Construction 5.4.2.2` (From category to schema) — [PDF Page 386]
> Construction 5.4.2.2 (From category to schema). We first define a functor R : Cat → Sch. Let C=(Ob(C),HomC,dom,cod,ids,comp) be a category (see Exercise 5.1.1.27). Let R(C)=(G,≃), where G is the graph G=(Ob(C),HomC,dom,cod), and with ≃ defined as the congruence generated by the following path equivalence declarations: for any composable sequence of morphisms f1, f2, …, fn (with dom(fi+1) = cod(fi) for each 1 i n − 1), we put [f1,f2,...,fn]dom(f1)≃[fn○⋯○f2○f1]dom(f1), (5.20) equating a path of length n with a path of length 1. This defines R on objects of Cat. A functor F:C→D induces a schema morphism R(F):R(C)→R(D), because vertices are sent 

### `Example 5.3.4.3` — [PDF Page 372]
> Example 5.3.4.3. Let S be a set, and let S × S ⊆ S × S be the complete relation on S, which is a preorder KS. Recall from Proposition 5.2.1.13 that there is a functor i : PrO → Cat, and the resulting category i(KS) is called the indiscrete category on

### `Example 5.3.4.4` — [PDF Page 374]
> Example 5.3.4.4. Consider the category FLin, described in Example 5.1.1.13, of finite nonempty linear orders. For every natural number n ∈ ℕ, let [n] ∈ Ob(FLin) denote the linear order shown in Example 4.4.1.7. Define a category Δ whose objects are given by Ob(Δ) = {[n] | n ∈ ℕ} and with HomΔ([m], [n]) = HomFLin([m], [n]). The difference between FLin and Δ is only that objects in FLin may have odd labels, e.g., •5→ •x→ •“Sam” whereas objects in Δ all have standard labels, e.g., •0→ •1→ •2 Clearly, FLin is a much larger category, and yet it feels as if it is pretty much the same as Δ. Actually, they are equivalent, FLin ≃ Δ. We will find funct

### `Example 5.3.4.7` — [PDF Page 375]
> Example 5.3.4.7. Consider the group ℤ2 ≔ ({0, 1}, 0, +), where 1 + 1 = 0. As a category, ℤ2 has one object ▲ and two morphisms, namely, 0, 1, such that 0 is the identity. Since ℤ2 is a group, every morphism is an isomorphism. Let C=1¯ be the terminal category, as in Exercise 5.1.2.40. One might accidentally believe that C is equivalent to ℤ2, but this is not the case. The argument in favor of the accidental belief is that we have unique functors F:ℤ2→C and F′:C→ℤ2 (and this is true); the round-trip F○F′:C→C is the identity (and this is true); and for the round-trip F′ ○ F : ℤ2 → ℤ2 both morphisms in ℤ2 are isomorphisms, so any choice of morph

### `Example 5.4.1.4` — [PDF Page 383]
> Example 5.4.1.4. Let [2] be the linear order graph of length 2, at the left, and let C denote the diagram at the right: We impose on C the path equivalence declaration a[g, h] ≃a[i] and show that in this case C and [2] are isomorphic in Sch. There is a unique schema morphism F: [2]→C such that 0 ↦a, 1 ↦b, 2 ↦c; it sends each arrow in [2] to a path of length 1 in C. And we have a schema morphism F′:C→[2], which reverses this mapping on vertices; note that F′ must send the arrow i in C to the path 0[f1, f2] in [2], which is okay. The round-trip F ′ ○ F : [2] → [2] is identity. The round-trip F○F ′:C→C may look like it is not the identity; indee

### `Example 4.5.2.12` — [PDF Page 384]
> Example 4.5.2.12. Let 1 denote the graph with one vertex and no arrows; consider it a schema. a. Is 1 isomorphic to L1 in Sch? b. Is 1 isomorphic to any (other) Ln?

### `Exercise 5.3.4.2` — [PDF Page 372]
> Exercise 5.3.4.2. Let C and C′ be categories. Suppose that F:C→C′ is an isomorphism of categories. a. Is it an equivalence of categories? b. If not, why? If so, what are the components of α and α′ (with notation as in

### `Exercise 5.1.2` — [PDF Page 373]
> Exercise 5.1.2.40). The category 1 consists of one object, its identity morphism, and nothing else. Let’s think about the difference between isomorphism and equivalence using KS ∈ Ob(Cat). The only way that KS can be isomorphic to 1 is if S has one element.17 On the other hand, there is an equivalence of categories KS≃1¯ for every set S ≠ ∅. So for example, K{1,2,3} from (5.15) is equivalent to the terminal category, 1. In fact, there are many such equivalences, one for each element of S. To see this, let S be a nonempty set, and choose an element s0 ∈ S. For every s ∈ S, there is a unique isomorphism ks:s→ ≅ s0 in KS. Let F : KS → 1 be the o

## 6. Page-by-Page Deep Index (PDF Pages 371–391)
- **Page 371** (`5.3 Natural transformations`) · **Items:** Definition 5.3.4.1: 5.3.4 Equivalence of categories We have a category Cat of categories, and in every category there is a notion of isomorphism between objects: one morphism each way, such that each round-trip composition is the identity. An isomorphism in Cat, therefore, takes place between two categories, say, C and D: it is a functor ...
- **Page 372** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.4.2, Definition 5.3.4, Solution 5.3.4.2, Example 5.3.4.3: to know something about F′○F:C→C, so let’s name it i:C→C; we want to know that i is a natural isomorphism. That is, for every c∈Ob(C), we want an isomorphism αc:c→ ≅ i(c), and we want to know that these isomorphisms are picked carefully enough that given g : c → c′ in C, the choice of isomorphisms for c and c′ are comp...
- **Page 373** (`5.3 Natural transformations`) · **Items:** Exercise 5.1.2: S; it has objects S and a single morphism between every pair of objects. Here is a diagram of K{1,2,3}: It is easy check that K1, the indiscrete category on one element, is isomorphic to 1, the discrete category on one object, also known as the terminal category (see Exercise 5.1.2.40). The category 1 consists of one o...
- **Page 374** (`5.3 Natural transformations`) · **Items:** Example 5.3.4.4, Exercise 5.3.4.5, Exercise 5.3.4.6: equivalent to 1 for every nonempty set S and that this fact can be witnessed by any element s0 ∈ S. Example 5.3.4.4. Consider the category FLin, described in Example 5.1.1.13, of finite nonempty linear orders. For every natural number n ∈ ℕ, let [n] ∈ Ob(FLin) denote the linear order shown in Example 4.4.1.7. Define a ...
- **Page 375** (`5.3 Natural transformations`) · **Items:** Example 5.3.4.7, Definition 5.3.4.8: We say that two categories C and D are equivalent if there exists an equivalence of categories between them. Show that the relation of being equivalent is an equivalence relation on Ob(Cat). Example 5.3.4.7. Consider the group ℤ2 ≔ ({0, 1}, 0, +), where 1 + 1 = 0. As a category, ℤ2 has one object ▲ and two morphisms, n...
- **Page 376** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.4.9, Exercise 5.3.4.10, Proposition 5.3.4.11: is bijective for every c, c′. Exercise 5.3.4.9. Let 1 and 2 be the discrete categories on one and two objects respectively. There is only one functor F : 2 → 1. a. Is it full? b. Is it faithful? Exercise 5.3.4.10. Let 0 denote the empty category, and let C be any category. There is a unique functor F:0¯→C. a. For gener...
- **Page 377** (`5.3 Natural transformations`) · **Items:** Exercise 5.3.4.12: is bijective. This implies that HomF(c, d) is bijective as well. Exercise 5.3.4.12. Let ℤ2 be the group (as category) from Example 5.3.4.7. Are there any fully faithful functors ℤ2 → 1?...
- **Page 378** (`5.3 Natural transformations`): ...
- **Page 379** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): 5.4 Categories and schemas are equivalent, Cat ≃ Sch Perhaps it is intuitively clear that schemas are somehow equivalent to categories. In fact, this is a reason that so much attention has been given to databases (and ologs). This section makes the equivalence between schemas and categories precise; it is proved in Sec...
- **Page 380** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): ...
- **Page 381** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Exercise 5.4.1.1: 5.4.1 The category Sch of schemas Recall from Definition 4.5.2.7 that a schema consists of a pair C≔(G,≃), where G = (V, A, src, tgt) is a graph and ≃ is a congruence, meaning a kind of equivalence relation on the paths in G (see Definition 4.5.2.3). If we think of a schema as being analogous to a category, what in sch...
- **Page 382** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Definition 5.4.1.2: a. Find a graph homomorphism f : [2] → Paths(Loop) that is injective on arrows (i.e., such that no two arrows in the graph [2] are sent by f to the same arrow in Paths(Loop)). b. The graph [2] has six paths, so Paths([2]) has six arrows. What are the images of these arrows under the graph homomorphism Paths(f): Paths([...
- **Page 383** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Slogan 5.4.1.3, Example 5.4.1.4, Exercise 5.4.1.5: objects are schemas as in Definition 4.5.2.7 and whose morphisms are schema morphisms, as in Definition 5.4.1.2. The identity morphism on schema C= (G,≃G) is the schema morphism idC≔ηG:G→Paths(G), as defined in Equation (5.16). We need only understand how to compose schema morphisms F:C→C′ and F′:C′→C″. On objects thei...
- **Page 384** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Exercise 5.4.1.6, Example 4.5.2.12, Solution 5.4.1.6, Exercise 5.4.1.7: current version of C. a. How many schema morphisms are there [2]→C that send 0 to a? b. How many schema morphisms are there C→[2] that send a to 0? Exercise 5.4.1.6. Consider the graph Loop as follows: and for any natural number n ∈ ℕ, let Ln denote the schema (Loop, ≃n), where ≃n is the PED fn+1 ≃ fn. Then Ln is the “...
- **Page 385** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): ...
- **Page 386** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Construction 5.4.2.1, Construction 5.4.2.2: 5.4.2 Proving the equivalence This section proves the equivalence of categories, Sch ≃ Cat. We construct the two functors Sch → Cat and Cat → Sch and then prove that these are mutually inverse equivalences (see Theorem 5.4.2.3). Construction 5.4.2.1 (From schema to category). We first define a functor L : Sch → Cat. Le...
- **Page 387** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Theorem 5.4.2.3, Definition 5.4.1: composition formula. This defines R on morphisms in Cat. It is clear that R preserves compositions, so it is a functor. Theorem 5.4.2.3. The functors L:Sch⇄Cat:R are mutually inverse equivalences of categories. Sketch of proof. It is clear that there is a natural isomorphism α:idCat→≅L○R; i.e., for any category C, ther...
- **Page 388** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Figure 5.1: Figure 5.1 Finite state machines X and Y with alphabet Σ = {a, b} and three states (left) or six states (right), and their associated action tables. __________________ 1In Society of Mind [32]. 2The reason for the notation Hom and the word hom-set is that morphisms are often called homomorphisms, e.g., in group theory....
- **Page 389** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): 8The topology on ℝ × ℝ is similar; a subset U ⊆ ℝ × ℝ is open if every point x ∈ U has an epsilon-neighborhood (a disk around x of some positive radius) fully contained in U. 9This example may be somewhat crude, in accordance with the crudeness of my understanding of materials science. 10 Let I × I = {(x, y) ∈ ℝ2 | 0 ≤...
- **Page 390** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`) · **Items:** Definition 4.3.2.1: talk about S as though it were still a set, e.g., discussing its elements rather than its objects. This kind of conceptual abbreviation is standard practice in mathematical discussion because it eases the mental burden, but when one says “Let S be an X considered as a Y,” the other may always ask, “How are you consider...
- **Page 391** (`5.4 Categories and schemas are equivalent, Cat ≃ Sch`): ...
