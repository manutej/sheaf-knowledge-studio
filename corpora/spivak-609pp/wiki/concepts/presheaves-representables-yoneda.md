---
id: presheaves-representables-yoneda
title: "Functor Categories, Presheaves, Representables & Yoneda's Lemma"
type: SheafStalk
chapter: 7
section: "7.2.1–7.2.2"
pdf_pages: "493–517"
symbol: "Hom_{C-Set}(Y_c, I) ≅ I(c)"
layer: "Sheaf & Topos Layer"
extracted_declarations: 32
restricts_to: [natural-transformations-functor-cat, currying-exponentials-subobjects, grothendieck-construction-comma]
glues_with: [sheaves-and-local-to-global-gluing]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Functor Categories, Presheaves, Representables & Yoneda's Lemma (`Hom_{C-Set}(Y_c, I) ≅ I(c)`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.2.1–7.2.2` · **PDF Pages 493–517**

## 1. Epistemic Worldview & Intuition

The functor category C-Set (and presheaf category PSh(C) = C^op-Set) behaves like an enriched universe of sets (a topos) with its own products, coproducts, exponentials, and subobject classifier Omega. For each object c in C, the representable functor Y_c = Hom_C(c, -) encodes c's entire web of outgoing perspectives; Yoneda's Lemma proves that natural transformations Y_c => I biject naturally with elements of the stalk I(c).

## 2. Formal Categorical Core

Representable functor Y_c : C -> Set sends d |-> Hom_C(c, d) (Def 7.2.1.14, p. 505). Yoneda's Lemma (Prop 7.2.1.16 / Sec 7.2.1.3, p. 506): For any functor I : C -> Set and object c in Ob(C), evaluation at id_c induces a natural bijection Hom_{C-Set}(Y_c, I) ~= I(c). Consequently, Y : C^op -> C-Set is fully faithful.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[ObC]`** — *a schema object c in Ob(C)*
- **`[Rep]`** — *its representable perspective functor Y_c = Hom_C(c, -)*
- **`[Nat]`** — *a natural transformation α : Y_c ⇒ I in C-Set*
- **`[Stalk]`** — *an element x = α_c(id_c) in the stalk I(c)*

### Functional Aspects (Morphisms)
- **`[ObC]` $\xrightarrow{\text{embeds via Yoneda functor Y into}}$ `[Rep]`**
- **`[Nat]` $\xrightarrow{\text{evaluates at identity id_c to yield}}$ `[Stalk]`**
- **`[Stalk]` $\xrightarrow{\text{uniquely determines natural transformation}}$ `[Nat]`**

### Commutative Path Facts ($p \simeq q$)
- Yoneda Isomorphism: Hom_{C-Set}(Hom_C(c, -), I) ≅ I(c) (p. 506).
- Topos Subobject Classifier (Sec 7.2.1.4, p. 508): In C-Set, the subobject classifier Ω(c) is the set of sieves on c, generalizing Boolean truth {true, false} to contextual/modal truth.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-40` (yoneda_embeds_via_Nat)** $\to$ [[natural-transformations-functor-cat]] (*Natural Transformations & The Category of Database Instances*, p. 338–370): Yoneda's lemma identifies natural transformations Hom_{C-Set}(Y_c, I) with stalk elements I(c) — `Nat(Hom_C(c,-), I) ≅ I(c)`
- **`rho-41` (topos_subobject_classifier)** $\to$ [[currying-exponentials-subobjects]] (*Currying, Exponentials, Subobject Classifier & Relative Sets*, p. 128–159): The functor category C-Set has exponential objects and sieve subobject classifier Ω — `Sub_{C-Set}(I) ≅ Hom(I, Ω)`
- **`rho-54` (category_of_elements_of_representable)** $\to$ [[grothendieck-construction-comma]] (*Opposite Categories, Grothendieck Construction ∫I & Comma Categories*, p. 439–460): The Grothendieck category of elements ∫Y_c of a representable functor Y_c = Hom_C(c,-) is the coslice comma category (c ↓ C) — `∫_C Hom_C(c, -) ≅ (c ↓ C)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-42` (sheaf_is_glued_presheaf)** $\leftarrow$ [[sheaves-and-local-to-global-gluing]] (*Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom*, p. 518–522): A sheaf is a presheaf O : Open(X)^op -> Set satisfying the equalizer gluing condition on all covers — `Sh(X) ↪ PSh(X)`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-02` — The Sheaf-Presheaf-Pullback Equalizer Triangle** ([[sheaves-and-local-to-global-gluing]], [[presheaves-representables-yoneda]], [[pullbacks-and-fiber-products]]): Restricting a sheaf O : Open(X)^op -> Set to a binary cover {U, V} exhibits O(U ∪ V) as the fiber product O(U) ×_{O(U ∩ V)} O(V). *[H^0 Exact (Zero Obstruction)]*
- **`tau-06` — The Yoneda-Grothendieck-Instance Triangle** ([[presheaves-representables-yoneda]], [[grothendieck-construction-comma]], [[natural-transformations-functor-cat]]): Elements of a stalk I(c) correspond bijectively to objects over c in the Grothendieck category of elements ∫I and to natural transformations Y_c ⇒ I. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 493–517)

### `Definition 7.2.1.4` (Monomorphism, epimorphism) — [PDF Page 497]
> Definition 7.2.1.4 (Monomorphism, epimorphism). Let S be a category, and let f : X → Y be a morphism. We say that f is a monomorphism if it has the following property. For all objects A∈Ob(S) and morphisms g, g′ : A → X in S, if f ○ g = f ○ g′, then g = g′. We say that f : X → Y is an epimorphism if it has the following property. For all objects B∈Ob(S) and morphisms h, h′ : Y → B in S, if h ○ f = h′ ○ f, then h = h′. In the category of sets, monomorphisms are the same as injections, and epimorphisms are the same as surjections (see Proposition 3.4.5.8). The same is true in C–Set: one can check table by table that a morphism of instances is m

### `Definition 7.2.1.7` — [PDF Page 498]
> Definition 7.2.1.7. Let C be a category, and let c∈Ob(C) be an object. The functor HomC(c,−):C→Set, sending d∈Ob(C) to the set HomC(c,d) and acting similarly on morphisms d → d′, is said to be represented by c. If a functor F:C→Set is isomorphic to HomC(c,−), we say that F is a representable functor. To shorten notation we sometimes write Yc≔HomC(c,−).

### `Definition 7.2.1.7` — [PDF Page 502]
> Definition 7.2.1.7.) b. Can you make sense of the statement, “Define (Yf)d by precomposition”? c. If h: d → e is a morphism in C, draw the naturality square for Yf. Does it commute?

### `Definition 7.2.1.24` — [PDF Page 508]
> Definition 7.2.1.24. Let C be a category, let C–Set denote its category of instances, and let 1C∈Ob(C−Set) denote the terminal object. A subobject classifier for C−Set is an object ΩC∈Ob(C−Set) and a morphism t:1C→ΩC with the following property. For any monomorphism f : I → J in C–Set, there exists a unique morphism char(f):J→ΩC such that the following diagram is a pullback in C–Set: That is, for any instance J there is a bijection HomC−Set(J,Ω)≅{I∈Ob(C−Set)|I⊆J}.

### `Proposition 7.2.1.1` — [PDF Page 495]
> Proposition 7.2.1.1. Let C be a category. The category C−Set is closed under colimits and limits. That is, for any category I and functor D:I→C−Set, both the limit and the colimit of D exist in C−Set. Sketch of proof. We rely on the fact that the category Set is complete and cocomplete (see Remark 6.1.3.37), i.e., that it has all limits and colimits (see Theorems 6.1.3.28 and 6.1.3.35 for constructions). Let J be an indexing category and D:J→C−Set a functor. For each object c∈Ob(C), we have a functor Dc:J→Set defined by Dc(j) = D(j)(c). Define a functor L:C→Set by L(c) = limJ Dc, and note that for each f : c → c′ in C there is an induced func

### `Proposition 7.2.1` — [PDF Page 496]
> Proposition 7.2.1.1 says that we can add or multiply database instances together. In fact, database instances on C form a topos, which means that just about every consideration we made for sets holds for instances on any schema. Perhaps the simplest schema is , on which the relevant topos is indeed equivalent to Set. But schemas can be arbitrarily complex categories, and it is impressive that all these set-theoretic notions make sense in such generality. Here is a table that compares these domains: Dictionary between Set and C→Set Concept in Set Concept in C–Set Set Object in C–Set Function Morphism in C–Set Element Representable functor Empt

### `Proposition 7.2.1.5` — [PDF Page 497]
> Proposition 7.2.1.5. Let C be a category, let X,Y:C→Set be objects in C−Set, and let f : X → Y be a morphism in C−Set. Then f is a monomorphism (resp. an epimorphism) if and only if for every object c∈Ob(C), the function f(c): X(c) → Y(c) is injective (resp. surjective). Sketch of proof. We first show that if f is mono (resp. epi), then so is f(c), for all c∈Ob(C). Considering c as a functor c:1¯→C, this result follows from the fact that Δc preserves limits and colimits, hence monos and epis. We now check that if f(c) is mono for all c∈Ob(C), then f is mono. Suppose

### `Proposition 7.2.1.15` (Yoneda’s lemma, part 1) — [PDF Page 503]
> Proposition 7.2.1.15 (Yoneda’s lemma, part 1). Let C be a category, c∈Ob(C) an object, and I:C→Set a set-valued functor. There is a natural bijection HomC−Set(Yc,I)→≅I(c). Proof. See Mac Lane [29].

### `Proposition 7.2.1.21` (Yoneda’s lemma, part 2) — [PDF Page 507]
> Proposition 7.2.1.21 (Yoneda’s lemma, part 2). Let C be a category. The assignment c ↦ Yc from Proposition 7.2.1.15 extends to a functor Y:Cop→C−Set, and this functor is fully faithful. In particular, if c,c′∈Ob(C) are objects and there is an isomorphism Yc ≅ Yc′ in C −Set, then there is an isomorphism c ≅ c′ in C. Proof. See Mac Lane [29].

### `Slogan 7.2.1.11` — [PDF Page 501]
> Slogan 7.2.1.11. The functor represented by ⌜a person⌝ simply leaves a placeholder, like 〈person’s name here〉 or 〈person’s height here〉, for every aspect of ⌜a person⌝. In general, there is a representable functor for every type in an olog. The representable functor for type T simply encapsulates the most generic or abstract example of type T, by leaving a placeholder for each of its attributes.

### `Slogan 7.2.1.18` — [PDF Page 505]
> Slogan 7.2.1.18. Yoneda’s lemma says the following. Specifying an actual thing of type T is the

### `Application 7.2.1.2` — [PDF Page 495]
> Application 7.2.1.2. When taking in data about a scientific subject, one often finds that how one thinks about the problem changes over time. We understand this phenomenon in the language of databases in terms of a series of schemas C1,C2, …,Cn+1, perhaps indexed chronologically. The problem is that previously- collected data is held in what may be outdated schemas, and we want to work with it in our current understanding. By finding appropriate functors between these schemas, or possibly with the help of auxiliary schemas, we can make a chain of categories and functors C1←F1D1→G1ℰ1→H1C2←F2D2→G2ℰ2→H2…→Gnℰn→HnCn+1. We can then use the data mig

### `Application 7.2.2.4` — [PDF Page 516]
> Application 7.2.2.4. Geographic data consists of maps of the earth together with various functions on it. For example, for any point on the earth one may want to know the average of temperatures recorded in the past ten years or the precise temperature at this moment. Earth can be considered as a topological space, E. Similarly, temperatures on earth reside on a continuum, say, the space T of real numbers [−100, 200]. Thus the temperature record is a continuous function E → T . Other records such as precipitation, population density, elevation, and so on, can all be considered as continuous functions from E to some space. Agencies like the U.

### `Application 7.2.2.5` — [PDF Page 516]
> Application 7.2.2.5. Application 7.2.2.4 discussed using topological database instances to model geographical data. Other scientific disciplines could use the same kind of tool. For example, in studying the mechanics of materials, one may want to consider the material as a topological space M and measure values such as energy as a continuous map M → E. Such observations could be modeled by databases with target category Top or Vect rather than Set.

### `Example 7.2.1.8` — [PDF Page 498]
> Example 7.2.1.8. Given a category C and an object c∈Ob(C), we get a representable functor Yc. If we think of C as a database schema and c as a table, then what does the representable functor Yc:C→Set look like in terms of databases? It turns out that the following procedure will generate it. Begin by writing a new row, say, “☺,” in the ID column of table c. For each foreign key column f : c → c′, add a row in the ID column of table c′ called “f(☺)” and record that result, “f(☺),” in the f column of table c. Repeat as follows: for each table d, identify all rows r that have a blank cell in column g : d → e. Add a new row called “g(r)” to table

### `Example 7.2.1.16` — [PDF Page 503]
> Example 7.2.1.16. Consider the category C drawn as follows:

### `Example 7.2.1.19` — [PDF Page 506]
> Example 7.2.1.19. Example 4.1.1.27 discussed the cyclic monoid M generated by the symbol Q and subject to the relation Q7 = Q4, depicted as Here is the mathematical foundation for this picture. Since M is a category with one object, ▲, there is a unique representable functor (up to isomorphism) Y≔Y▲:M→Set. Any functor M→Set can be thought of as a set with an M action (see Section 5.2.1.1). In the case of Y , the required set is Y(▲)=HomM(▲,▲)≅{Q0,Q1,Q2,Q3,Q4,Q5,Q6}, and the action is pretty straightforward (it is called the principal action). For example, . We might say that (7.6) is a picture of this principal action of M. However, we can go

### `Example 7.2.1.25` — [PDF Page 509]
> Example 7.2.1.25. Consider the following category C≅[3]:

## 6. Page-by-Page Deep Index (PDF Pages 493–517)
- **Page 493** (`7.2 Categories of functors`): 7.2 Categories of functors For any two categories C and D,8 Section 5.3.2.1 discussed the category Fun(C,D) of functors and natural transformations between them. This section discusses functor categories a bit more and gives some important applications in mathematics (sheaves) that extend to the real world....
- **Page 494** (`7.2 Categories of functors`): ...
- **Page 495** (`7.2 Categories of functors`) · **Items:** Proposition 7.2.1.1, Application 7.2.1.2, Exercise 7.2.1.3: 7.2.1 Set-valued functors Let C be a category. We have been denoted by C−Set the functor category Fun(C,Set). Here is a nice result about these categories. Proposition 7.2.1.1. Let C be a category. The category C−Set is closed under colimits and limits. That is, for any category I and functor D:I→C−Set, both the limit ...
- **Page 496** (`7.2 Categories of functors`) · **Items:** Proposition 7.2.1: C–Set has an initial object and a terminal object. a. Let A∈Ob(C−Set) be the initial object, considered as a functor A:C→Set. For any c∈Ob(C), what is the set A(c)? b. Let Z∈Ob(C−Set) be the terminal object, considered as a functor Z:C→Set. For any c∈Ob(C), what is the set Z(c)? Proposition 7.2.1.1 says that we can add...
- **Page 497** (`7.2 Categories of functors`) · **Items:** Definition 7.2.1.4, Proposition 7.2.1.5: defined in Section 7.2.1.6. We briefly discuss monomorphisms and epimorphisms first in general (Definition 7.2.1.4) and then in C–Set (Proposition 7.2.1.5). Definition 7.2.1.4 (Monomorphism, epimorphism). Let S be a category, and let f : X → Y be a morphism. We say that f is a monomorphism if it has the following prope...
- **Page 498** (`7.2 Categories of functors`) · **Items:** Definition 7.2.1.7, Example 7.2.1.8: that g, g′ : A → X are morphisms in C–Set such that f ○ g = f ○ g′. Then for every c, we have f ○ g(c) = f ○ g′(c), which implies by hypothesis that g(c) = g′(c). But the morphisms in C–Set are natural transformations, and if two natural transformations g, g′ have the same components, then they are the same. A similar ...
- **Page 499** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.1.9: Then YB:C→Set is given by “morphisms from B to −,” i.e., it is the following instance: To create YB we began with a single element in table B and followed the arrows, putting new entries wherever they were required. One might call this the schematically implied reference spread or SIRS of the element ☺ in table B. Noti...
- **Page 500** (`7.2 Categories of functors`) · **Items:** Solution 7.2.1.9, Exercise 7.2.1.10: Consider the schema for graphs, a. Write the representable functor YAr : GrIn → Set as two tables. b. Write the representable functor YVe as two tables. Solution 7.2.1.9. a. This was done in Exercise 5.3.3.7, although not with the most natural names. Here we rewrite YAr = HomGrIn(Ar, −) as b. Here is YVe = HomGrIn(Ve, ...
- **Page 501** (`7.2 Categories of functors`) · **Items:** Solution 7.2.1.10, Slogan 7.2.1.11: Express the representable functor Ys:Loop→Set in table form. Solution 7.2.1.10. We have Ys=HomLoop(s,−):Loop→Set. On objects, of which there is only Ob(Loop)={s}, we have Ys(s) = {fn | n ∈ ℕ}. The morphism f : s → s acts on Ys(s) by composing. Here is Ys in table form: s ID f ☺ f(☺) f(☺) f2(☺) f2(☺) f3(☺) f3(☺) f4(☺) f...
- **Page 502** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.1.12, Exercise 7.2.1.13, Definition 7.2.1.7, Solution 7.2.1.13: Exercise 7.2.1.12. Recall from Definition 7.2.1.7 that a functor F:C→Set is said to be represented by c if there is a natural isomorphism F≅HomC(c,−). a. There is a functor Ob: Cat → Set (see Exercise 5.1.2.41) sending a category C to its set Ob(C) of objects, and sending a functor to its on-objects part. This functor ...
- **Page 503** (`7.2 Categories of functors`) · **Items:** Proposition 7.2.1.15, Example 7.2.1.16: and it commutes because, for any element g ∈ Yc′(d), the composition c→fc ′→gd→he is associative. More explicitly, going down then right we have (Yf)d(g) = g ○ f and Yc(h)(g ○ f) = h ○ (g ○ f). Going right then down we have Yc ′(h)(g) = h ○ g and (Yf)e(h ○ g) = (h ○ g) ○ f. To reiterate, the associativity of compositio...
- **Page 504** (`7.2 Categories of functors`): There are two representable functors, YChild and YMother. The former, YChild:C→Set, is shown here: The representable functor YChild is the freest instance possible, starting with one element in the Child table and satisfying the constraints. The latter, YMother is the freest instance possible, starting with one element...
- **Page 505** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.1.17, Slogan 7.2.1.18: Yoneda’s lemma (7.2.1.15) is about the set of natural transformations YChild → I. Recall from Definition 5.3.1.2 that a search for natural transformations can get tedious. Yoneda’s lemma makes the calculation quite trivial. In this case there are exactly four such natural transformations, HomC−Set(YChild,I)≅I(Child)≅4¯...
- **Page 506** (`7.2 Categories of functors`) · **Items:** Example 7.2.1.19, Exercise 7.2.1.20: same as filling in all placeholders found in the generic thing of type T. Yoneda’s lemma is considered by many category theorists to be the most important tool in the subject. While its power is probably unclear to students whose sole background in category theory comes from this book, Yoneda’s lemma is indeed extremel...
- **Page 507** (`7.2 Categories of functors`) · **Items:** Proposition 7.2.1.21, Exercise 7.2.1.22: Δc:C−Set→Set and its left adjoint Σc:Set→C−Set (see Section 7.1.4). a. What is the set Δc(I)? b. What is HomSet({☺}, Δc(I))? c. What is HomC−Set(Σc({☺}),I)? d. How does Σc({☺}) compare to Yc, the functor represented by c, as objects in C–Set? Proposition 7.2.1.21 (Yoneda’s lemma, part 2). Let C be a category. The assig...
- **Page 508** (`7.2 Categories of functors`) · **Items:** Definition 7.2.1.24: By the appropriate application of Yoneda’s lemma, we see that there is an isomorphism C×(A+B)≅(C×A)+(C×B) in Fin. The result about natural numbers follows. 7.2.1.23 The subobject classifier Ω∈Ob(C−Set) If C is a category, then the functor category C–Set is a special kind of category, called a topos. Note that when C=1¯...
- **Page 509** (`7.2 Categories of functors`) · **Items:** Example 7.2.1.25: In terms of databases, what this means is that for every schema C, there is some special instance ΩC∈Ob(C−Set) that somehow classifies subinstances of anything. When the schema is the terminal category, C=1¯, instances are sets and according to Definition 3.4.4.9 the subobject classifier is Ω1 = {True, False}. One migh...
- **Page 510** (`7.2 Categories of functors`): To write ΩC, we need to understand the representable functors Yc∈Ob(C−Set), for c = 0, 1, 2, 3, as well as their subobjects. Here is Y0 as an instance: What are the subinstances of this? There is the empty subinstance ∅ ⊆ Y0 and the identity subinstance Y0 ⊆ Y0. But there are three more as well. Note that if we want to...
- **Page 511** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.1.26: The morphism 1→ΩC picks out the yes row of every table. Now that we have constructed ΩC∈Ob(C−Set), we are ready to use it. What makes ΩC special is that for any instance X:C→Set, the subinstances if X are in one-to-one correspondence with the instance morphisms X→ΩC. Consider the following arbitrary instance X, where t...
- **Page 512** (`7.2 Categories of functors`) · **Items:** Exercise 7.2.1.27, Exercise 7.2.1.28: a. Write the blue subinstance A ⊆ X shown in (7.9) as an instance of C, i.e., as four tables. b. This subinstance A ⊆ X corresponds to a map ℓ≔char(A):X→ΩC. For all c∈Ob(C), we have a function ℓ(c):X(c)→ΩC(c). With c = 1, write out ℓ(1):X(1)→ΩC(1). Exercise 7.2.1.27. Let Loop be the loop schema a. What is the subobject...
- **Page 513** (`7.2 Categories of functors`): Let be the indexing category for graphs. a. Write the subobject classifier ΩGrIn ∈ Ob(GrIn–Set) in tabular form, i.e., as two tables. b. Draw ΩGrIn as a graph. c. Let G be the following graph and G′ ⊆ G the blue part. Write G ∈ Ob(GrIn–Set) in tabular form. d. Write the components of the natural transformation char(G′)...
- **Page 514** (`7.2 Categories of functors`): ...
- **Page 515** (`7.2 Categories of functors`): 7.2.2 Database instances in other categories So far we have focused on the category C−Set=Fun(C,Set) of set-valued functors C→Set for arbitrary categories, or database schemas, C. What if we allow the target category Set to change? 7.2.2.1 Representations of groups The classical mathematical subject of representation t...
- **Page 516** (`7.2 Categories of functors`) · **Items:** Application 7.2.2.4, Application 7.2.2.5: 7.2.2.2 Representations of quivers Representation theory also studies representations of quivers. A quiver is just the free category (see Example 5.1.2.33) on a graph. If P is a graph with free category P, then a representation of the quiver P is a functor F:P→Vect. Such a representation consists of a vector space at e...
- **Page 517** (`7.2 Categories of functors`): ...
