---
id: categories-objects-morphisms
title: "Categories: Objects, Morphisms, Identities & Composition"
type: SheafStalk
chapter: 5
section: "5.1.1"
pdf_pages: "267–284"
symbol: "C = (Ob(C), Hom_C, id, ∘)"
layer: "Core Category Theory"
extracted_declarations: 32
restricts_to: [monoids-and-actions, orders-lattices-hierarchies, graphs-and-paths]
glues_with: [functors-structure-maps, operads-and-hierarchical-composition]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Categories: Objects, Morphisms, Identities & Composition (`C = (Ob(C), Hom_C, id, ∘)`)

> **Sheaf Stalk Location:** Chapter 5 (Basic Category Theory: Categories, Functors, Natural Transformations & Cat ≃ Sch) · Section `5.1.1` · **PDF Pages 267–284**

## 1. Epistemic Worldview & Intuition

The central abstraction of modern mathematics: a category C consists of a collection of objects Ob(C), hom-sets Hom_C(x, y) of morphisms for each pair of objects, an identity morphism id_x for each object, and an associative composition formula Hom_C(y, z) × Hom_C(x, y) -> Hom_C(x, z).

## 2. Formal Categorical Core

Definition 5.1.1.1 (p. 271): Constituents (A. Ob(C), B. Hom_C(x,y), C. id_x in Hom_C(x,x), D. o : Hom_C(y,z) × Hom_C(x,y) -> Hom_C(x,z)) subject to: (1) Identity Law: id_y o f = f = f o id_x; (2) Associativity Law: (h o g) o f = h o (g o f). Unifies Set, Mon, Grp, Grph, PrO, Top, Vect, and every database schema.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *an object x in Ob(C)*
- **`[Y]`** — *an object y in Ob(C)*
- **`[Z]`** — *an object z in Ob(C)*
- **`[XY]`** — *a morphism f in Hom_C(x, y)*
- **`[YZ]`** — *a morphism g in Hom_C(y, z)*
- **`[XZ]`** — *a composite morphism g ∘ f in Hom_C(x, z)*

### Functional Aspects (Morphisms)
- **`[XY]` $\xrightarrow{\text{has domain}}$ `[X]`**
- **`[XY]` $\xrightarrow{\text{has codomain}}$ `[Y]`**
- **`[XZ]` $\xrightarrow{\text{has domain}}$ `[X]`**
- **`[XZ]` $\xrightarrow{\text{has codomain}}$ `[Z]`**

### Commutative Path Facts ($p \simeq q$)
- Unitality: id_y ∘ f = f = f ∘ id_x.
- Associativity: (h ∘ g) ∘ f = h ∘ (g ∘ f) (Definition 5.1.1.1, p. 271).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-22` (one_object_category)** $\to$ [[monoids-and-actions]] (*Monoids, Agent Actions & Finite State Machines*, p. 160–191): A category with a single object Ob(C)={★} is a monoid Hom_C(★,★) — `Mon ↪ Cat`
- **`rho-23` (thin_category)** $\to$ [[orders-lattices-hierarchies]] (*Preorders, Partial Orders, Meets/Joins & Alexandrov Spaces*, p. 221–244): A category with at most one morphism between any two objects is a preorder — `PrO ↪ Cat`
- **`rho-24` (free_path_category)** $\to$ [[graphs-and-paths]] (*Graphs, Path Categories & Homomorphisms*, p. 201–220): Every graph G freely generates a category Path(G); every category has an underlying graph — `Path : Grph ⇄ Cat : U`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-25` (morphisms_of_Cat)** $\leftarrow$ [[functors-structure-maps]] (*Functors: Structure-Preserving Maps Between Worldviews*, p. 285–337): Functors F : C -> D are the structure-preserving morphisms between categories — `Hom_Cat(C, D) = Fun(C, D)`
- **`rho-51` (multi_input_generalization)** $\leftarrow$ [[operads-and-hierarchical-composition]] (*Operads, Wiring Diagrams & Hierarchical Self-Similarity*, p. 557–584): A category is an operad restricted to unary (1-input) morphisms O_1(x; y) = Hom_C(x, y) — `Cat ↪ Operad`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 267–284)

### `Definition 5.1.1.1` — [PDF Page 271]
> Definition 5.1.1.1. A category C is defined as follows: One announces some constituents (A. objects, B. morphisms, C. identities, D. compositions) and shows that they conform to some laws (1. identity law, 2. associativity law). Specifically, one announces A. a collection Ob(C), elements of which are called objects; B. for every pair x, y ∈ Ob(C), a set HomC(x,y)∈Set; it is called the hom-set from x to y; its elements are called morphisms from x to y;2 C. for every object x∈Ob(C), a specified morphism, denoted idx∈HomC(x,x), and called the identity morphism on x; D. for every three objects x,y,z∈Ob(C), a function ○: HomC(y,z)×HomC(x,y)→HomC(x

### `Definition 4.1.1` — [PDF Page 273]
> Definition 4.1.1.1, and monoid homomorphisms in Definition 4.1.4.1. Every monoid M≔(M,e,⋆M) has an identity homomorphism idM:M→M, given by the identity function idM: M → M. To compose two monoid homomorphisms f:M→M′ and g:M′→M″, we compose their underlying functions f: M → M′ and g: M′ → M″, and check that the result g ○ f is a monoid homomorphism. Indeed, g○f(e)=g(e′)=e″, g○f(m1 ⋆M m2)=g(f(m1)⋆M′ f(m2))=g○f(m1)⋆M″ g○f(m2). It is clear that the two category laws (unit and associativity) hold, because monoid morphisms are special kinds of functions, and functions compose unitally and associatively. So Mon is a category.

### `Definition 5.1.1` — [PDF Page 274]
> Definition 5.1.1.1), or the constituents do not obey the category laws (1, 2). Let G be the following graph: Suppose we try to define a category G by faithfully recording vertices as objects and arrows as morphisms. Will that be a category? Following that scheme, we put Ob(G)={a,b,c}. For all nine pairs of objects we need a hom-set. Since the only things we are calling morphisms are the arrows of G, we put HomG(a,a)=∅HomG(a,b)= {f}HomG(a,c)=∅HomG(b,a)=∅HomG(b,b)=∅HomG(b,c)= {g}HomG(c,a)=∅HomG(c,b)=∅HomG(c,c)=∅(5.1*) If we say we are done, the listener should object that we have given neither identities (C) nor a composition formula (D), and t

### `Definition 5.1.1.19` — [PDF Page 279]
> Definition 5.1.1.19. Let C be a category, and let X,Y∈Ob(C) be objects. An isomorphism f from X to Y is a morphism f: X → Y in C such that there exists a morphism g: Y → X in C with g○f=idX and f○g=idY. In this case we say that the morphism f is invertible and that g is the inverse of f. We may also say that the objects X and Y are isomorphic.

### `Proposition 5.1.1.25` — [PDF Page 280]
> Proposition 5.1.1.25. Let C be a category, and let ≅ be the relation on Ob(C) given by saying X ≅ Y iff X and Y are isomorphic. Then ≅ is an equivalence relation. Proof. The proof of Proposition 2.1.2.18 can be mimicked in this more general setting. 5.1.1.26 Another viewpoint on categories Here is an alternative definition of category, using the work done in Chapter 2.

### `Slogan 5.1.1.12` — [PDF Page 276]
> Slogan 5.1.1.12. If you like joins so much, why don’t you marry them? Morphisms are often billed as preserving all the structure we care about, so it is worth asking whether we want to enforce that constraint on morphisms. That is, suppose f: (X, X) → (Y, Y) is a morphism of preorders. We might want to condition the decision of whether to include f as a morphism in C″ on whether, for any join w = x ∨ x′ in X, it is the case that f(w) = f(x) ∨ f(x′) in Y. Concisely, we could define the morphisms in C″ by HomC(a,b)≔{f∈HomPrO(a,b)|f preserves joins}.

### `Example 5.1.1.3` (The category Set of sets) — [PDF Page 272]
> Example 5.1.1.3 (The category Set of sets). Chapters 2 and 3 were about the category of sets, denoted Set. The objects are the sets and the morphisms are the functions; and the current notation HomSet(X, Y) was used to refer to the set of functions X → Y. The composition formula ○ is given by function composition, and for every set X, the identity function idX: X → X serves as the identity morphism for X ∈ Ob(Set). The two laws clearly hold, so Set is indeed a category.

### `Example 5.1.1.4` (The category Fin of finite sets) — [PDF Page 272]
> Example 5.1.1.4 (The category Fin of finite sets). Inside the category Set is a subcategory Fin ⊆ Set, called the category of finite sets. Whereas an object S ∈ Ob(Set) is a set that can have arbitrary cardinality, Fin is defined such that Ob(Fin) includes all (and only) those sets S having finitely many elements, i.e., |S| = n for some natural number n ∈ ℕ. Every object of Fin is an object of Set, but not vice versa. Although Fin and Set have different collections of objects, their notions of morphism are in some sense the same. For any two finite sets S, S′ ∈ Ob(Fin), we can also think of S, S′ ∈ Ob(Set), and we have

### `Example 5.1.1.5` (The category Mon of monoids) — [PDF Page 273]
> Example 5.1.1.5 (The category Mon of monoids). Monoids were defined in

### `Example 5.1.1.9` (Noncategory 1) — [PDF Page 274]
> Example 5.1.1.9 (Noncategory 1). What is not a category? Two things can go wrong: either one fails to specify all the relevant constituents (A, B, C, D from

### `Example 5.1.1.10` (Noncategory 2) — [PDF Page 275]
> Example 5.1.1.10 (Noncategory 2). In this example, we make a faux category F with one object and many morphisms. The problem here is the composition formula. Define F to have one object Ob(F)={☺}, and HomF(☺,☺)=ℕ . Define id ☺= 1 ∈ ℕ. Define the composition formula ○: ℕ × ℕ → ℕ by the usual exponentiation function for natural numbers, m ○ n = mn. This is a perfectly cromulent function, but it does not work right as a composition formula. Indeed, for the identity law to hold, we would need m1 = m = 1m, and one side of this is false. For the associativity law to hold, we would need (mn)p=m(np), but this is also not the case.

### `Example 5.1.1.11` (The category of preorders with joins) — [PDF Page 276]
> Example 5.1.1.11 (The category of preorders with joins). Suppose we are only interested in preorders (X, ) for which every pair of elements has a join. We saw in Exercise 4.4.2.3 that not all preorders have this property. However, we can create a category C in which every object does have this property. To begin, let’s put C≔{(X, )∈Ob(PrO)|(X, ) has all joins} for the set of objects. What about morphisms? One option would be to put in no morphisms (other than identities) and to just consider this collection of objects as having no structure other than a set. In other words, we can take C to be the discrete category on the preceding set Ob(C)=

### `Example 5.1.1.13` (Category FLin of finite linear orders) — [PDF Page 277]
> Example 5.1.1.13 (Category FLin of finite linear orders). We have a category PrO of preorders, and some of its objects are finite linear orders. Let FLin be the full subcategory of PrO spanned by the linear orders. That is, following Definition 4.4.4.1, given linear orders X, Y ∈ Ob(FLin), every morphism of preorders X → Y counts as a morphism in FLin: HomFLin(X,Y)=HomPrO(X,Y).

### `Example 5.1.1.15` (Category of graphs) — [PDF Page 277]
> Example 5.1.1.15 (Category of graphs). Graphs were defined in Definition 4.3.1.1 and graph homomorphisms in Definition 4.3.3.1. To see that these are sufficient to form a category is considered routine to a seasoned category theorist, so let’s see why. Since a morphism from G = (V, A, src, tgt) to G′ = (V′, A′, src′, tgt′) involves two functions f0: V → V′ and f1: A → A′, the identity and composition formulas

### `Example 5.1.1.20` — [PDF Page 279]
> Example 5.1.1.20. If C=Set is the category of sets, then Definition 5.1.1.19 coincides precisely with the one given in Definition 2.1.2.14.

### `Example 5.1.1.28` (Partial olog for a category) — [PDF Page 282]
> Example 5.1.1.28 (Partial olog for a category). Diagram (5.4) is an olog that captures some of the essential structures of a category:

### `Remark 5.1.1.2` — [PDF Page 272]
> Remark 5.1.1.2. There is perhaps much that is unfamiliar about Definition 5.1.1.1, but there is also one thing that is strange about it. The objects Ob(C) of C are said to be a collection rather than a set. This is because we sometimes want to talk about the category of all sets, in which every possible set is an object, and if we try to say that the collection of sets is itself a set, we run into Russell’s paradox. Modeling this was a sticking point in the foundations of category theory, but it was eventually fixed by Grothendieck’s notion of expanding universes. Roughly, the idea is to choose some huge set κ (with certain properties making 

### `Remark 5.1.1.6` — [PDF Page 273]
> Remark 5.1.1.6. The following will be informal, but it can be formalized. Let’s define a questionable category to be the specification of A, B, C, D from Definition 5.1.1.1, without enforcing either of the category laws (1, 2). Suppose that Q is a questionable category and C is a category. If Q sits somehow inside of C, in the precise sense that A. there is a function U:Ob(Q)→Ob(C), B. for all a,b∈Ob(Q), we have an injection U:HomQ(a,b)↪HomC(U(a),U(b)), C. for all a∈Ob(Q), both Q and C have the same version of the identity on a, i.e., U(ida) = idU(a), D. for all f: a → b and g: b → c in Q, both Q and C have the same version of composition g ○

## 6. Page-by-Page Deep Index (PDF Pages 267–284)
- **Page 267** (`4.5 Databases: schemas and instances`): Chapter 5 Basic Category Theory “…We know only a very few—and, therefore, very precious—schemes whose unifying powers cross many realms.”—Marvin Minsky.1 Categories, or an equivalent notion, have already been introduced as ologs, or equivalently, as database schemas. One can think of a category as a graph (as in Sectio...
- **Page 268** (`4.5 Databases: schemas and instances`): ...
- **Page 269** (`5.1 Categories and functors`): 5.1 Categories and functors This section gives the standard definition of categories and functors. These, together with natural transformations (Section 5.3), form the backbone of category theory. It also gives several examples....
- **Page 270** (`5.1 Categories and functors`): ...
- **Page 271** (`5.1 Categories and functors`) · **Items:** Definition 5.1.1.1: 5.1.1 Categories In everyday speech we think of a category as a kind of thing. A category consists of a collection of things, all of which are related in some way. In mathematics a category can also be construed as a collection of things and a type of relationship between pairs of such things. For this kind of thing-re...
- **Page 272** (`5.1 Categories and functors`) · **Items:** Remark 5.1.1.2, Example 5.1.1.3, Example 5.1.1.4: 2. If w, x, y, z ∈ Ob(C) are any objects, and f: w → x, g: x → y, and h: y → z are any morphisms, then the two ways to compose yield the same element in HomC(w,z): (h○g)○f=h○(g○f)∈HomC(w,z). Remark 5.1.1.2. There is perhaps much that is unfamiliar about Definition 5.1.1.1, but there is also one thing that is strange ab...
- **Page 273** (`5.1 Categories and functors`) · **Items:** Example 5.1.1.5, Definition 4.1.1, Remark 5.1.1.6, Exercise 5.1.1.7: HomFin(S,S′)=HomSet(S,S′). That is, a morphism in Fin between finite sets S and S′ is simply a function f: S → S′. Example 5.1.1.5 (The category Mon of monoids). Monoids were defined in Definition 4.1.1.1, and monoid homomorphisms in Definition 4.1.4.1. Every monoid M≔(M,e,⋆M) has an identity homomorphism idM:M→M, give...
- **Page 274** (`5.1 Categories and functors`) · **Items:** Exercise 5.1.1.8, Example 5.1.1.9, Definition 5.1.1: group homomorphisms as morphisms (see Definition 4.2.1.16). Show that the rest of the conditions for Grp to be a category are satisfied. Exercise 5.1.1.8. Suppose we set out to define a category PrO, having preorders as objects and preorder homomorphisms as morphisms (see Definition 4.4.4.1). Show (to the level of deta...
- **Page 275** (`5.1 Categories and functors`) · **Items:** Example 5.1.1.10: HomG(b,c)×HomG(a,b)→HomG(a,c), but the domain is nonempty (it is {(f, g)}) and the codomain HomG(a,c)=∅ is empty; there is no such function. In other words, to satisfy the listener we need to add a composite for the arrows f and g. So again we must make a change, adding an element to make HomG(a,c)= {h}. We can now say...
- **Page 276** (`5.1 Categories and functors`) · **Items:** Example 5.1.1.11, Slogan 5.1.1.12: To fix this problem we must completely revamp the composition formula. It would work to use multiplication, m ○ n = m * n. Then the identity law would read 1 * m = m = m * 1, and that holds; and the associativity law would read (m * n) * p = m * (n * p), and that holds. Example 5.1.1.11 (The category of preorders with ...
- **Page 277** (`5.1 Categories and functors`) · **Items:** Example 5.1.1.13, Exercise 5.1.1.14, Example 5.1.1.15: One can check easily that the identity morphisms preserve joins and that compositions of join-preserving morphisms are join-preserving, so this version of homomorphisms makes C″ a well defined category. These options are by no means comprehensive, and none of these options is better than any other. Which category to us...
- **Page 278** (`5.1 Categories and functors`) · **Items:** Remark 5.1.1.16, Exercise 5.1.1.17: simply arise from the identity and composition formulas for sets. Associativity follow similarly. The only thing that needs to be checked is that the composition of two such morphisms, each satisfying (4.5), will itself satisfy (4.5). For completeness, we check that now. Suppose that f=(f0,f1):G→G′ and g=(g0,g1):G′→G″ ...
- **Page 279** (`5.1 Categories and functors`) · **Items:** Solution 5.1.1.17, Definition 5.1.1.19, Example 5.1.1.20, Exercise 5.1.1.21, Solution 5.1.1.21: Suppose we try to make a category CF as follows. Put Ob(CF)=ℝ2, and for every pair of points x, x′ ∈ ℝ2, let HomCF(x,x′)={C:x→x′}/~, where C: x → x′ is an oriented curve and ∼ means “same line integral,” as explained. Is there an identity morphism and a composition formula that will make CF into a category? Solution 5....
- **Page 280** (`5.1 Categories and functors`) · **Items:** Exercise 5.1.1.22, Exercise 5.1.1.23, Exercise 5.1.1.24, Proposition 5.1.1.25, Exercise 5.1.1.27: Exercise 5.1.1.22. Let C be a category, and let f: X → Y be a morphism. Suppose that both g: Y → X and g′: Y → X are inverses of f. Show that they are the same morphism, g = g ′. Exercise 5.1.1.23. Suppose that G = (V, A, src, tgt) and G′ = (V′, A′, src′, tgt′) are graphs and that f = (f0, f1): G → G′ is a graph homomo...
- **Page 281** (`5.1 Categories and functors`) · **Items:** Solution 5.1.1.27: A category C consists of a sequence (Ob(C),HomC,dom,cod,ids,comp), where Ob(C) is a set;4 HomC is a set, and dom,cod:HomC→Ob(C) are functions; ids: Ob(C)→HomC is a function; comp is a function as depicted in the commutative diagram (5.3) a. Add to diagram (5.3) to express the fact that for any x∈Ob(C), the morphism idx...
- **Page 282** (`5.1 Categories and functors`) · **Items:** Example 5.1.1.28: b. We have idHomC:HomC→HomC and ids○cod:HomC→HomC, and these commute over Ob(C), meaning that for any morphism f: A → B, its codomain is the domain of idB. Thus a unique map 〈idHomC, ids○ cod〉Ob(C):HomC→HomC×Ob(C)HomC is induced (see Proposition 3.2.1.15). Similarly there is a function 〈idids○domHomC, Ob(C)〉: HomC→HomC...
- **Page 283** (`5.1 Categories and functors`) · **Items:** Remark 5.1.1.29: Missing from (5.4) is the notion of identity morphism (as an arrow from ⌜an object of C⌝ to ⌜a morphism in C⌝) and the associated path equivalences, as well as the identity and associativity laws. All of these can be added to the olog, at the expense of some clutter. Remark 5.1.1.29. Perhaps it is already clear that ca...
- **Page 284** (`5.1 Categories and functors`): ...
