---
id: operads-and-hierarchical-composition
title: "Operads, Wiring Diagrams & Hierarchical Self-Similarity"
type: SheafStalk
chapter: 7
section: "7.4"
pdf_pages: "557–584"
symbol: "O(x₁, …, x_n; y)"
layer: "Context & Operadic Layer"
extracted_declarations: 30
restricts_to: [categories-objects-morphisms, functors-structure-maps]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Operads, Wiring Diagrams & Hierarchical Self-Similarity (`O(x₁, …, x_n; y)`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.4` · **PDF Pages 557–584**

## 1. Epistemic Worldview & Intuition

While a category only allows 1-to-1 morphisms f : x -> y, an operad O generalizes categories to multi-input morphisms f : (x_1, ..., x_n) -> y that can be recursively nested inside one another like hierarchical wiring diagrams, fractal squares (Little Cubes operad), or multi-scale biological materials (collagen fibrils -> fibers -> tendon). An operad algebra F : O -> Set populates each box with a set of possible states and each wiring diagram with a composition operation combining part states into whole-system states.

## 2. Formal Categorical Core

Definition 7.4.1.1 (p. 559): An operad O specifies objects Ob(O), multi-hom sets O_n(x_1,...,x_n; y), identity morphisms id_x in O_1(x; x), and substitution/composition maps O_n(y_1,...,y_n; z) × prod_i O_{k_i}(x_{i,1},...,x_{i,k_i}; y_i) -> O_{sum k_i}(x...; z) obeying identity and associativity laws. Operad algebra (Def 7.4.2.1, p. 567): A functor of operads A : O -> Set.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Sub]`** — *a tuple of subsystem states (s₁, …, s_n) in A(x₁) × … × A(x_n)*
- **`[Wire]`** — *an operad wiring morphism φ in O(x₁, …, x_n; y)*
- **`[Sys]`** — *an assembled macro-system state s in A(y)*

### Functional Aspects (Morphisms)
- **`[Sub]` $\xrightarrow{\text{assembles hierarchically via operad algebra map A(φ) into}}$ `[Sys]`**
- **`[Wire]` $\xrightarrow{\text{specifies multi-input composition grammar for}}$ `[Sys]`**

### Commutative Path Facts ($p \simeq q$)
- Operadic Associativity (Figure 7.6, p. 580): Nesting subsystem wiring diagrams inside larger diagrams commutes regardless of assembly order.
- Connects to Sheaves: While a sheaf glues overlapping spatial/conceptual neighborhoods (1-to-1 restriction), an operad algebra glues multi-ary subsystems into hierarchical wholes.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-51` (multi_input_generalization)** $\to$ [[categories-objects-morphisms]] (*Categories: Objects, Morphisms, Identities & Composition*, p. 267–284): A category is an operad restricted to unary (1-input) morphisms O_1(x; y) = Hom_C(x, y) — `Cat ↪ Operad`
- **`rho-52` (operad_algebras_generalize_instances)** $\to$ [[functors-structure-maps]] (*Functors: Structure-Preserving Maps Between Worldviews*, p. 285–337): An operad algebra A : O -> Set maps multi-input wiring diagrams to product functions A(x₁)×…×A(x_n) -> A(y) — `Alg(O) = Hom_Operad(O, Set)`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 557–584)

### `Definition 7.4.1.1` — [PDF Page 559]
> Definition 7.4.1.1. An operad O is defined as follows: One announces some constituents (A. objects, B. morphisms, C. identities, D. compositions) and shows that they conform to some laws (1. identity law, 2. associativity law). Specifically, one announces A. a collection Ob(O), each element of which is called an object of O; B. for each object y∈Ob(O), finite set n ∈ Ob(Fin), and n-indexed set of objects x:n→Ob(O), a set On(x;y)∈Ob(Set); its elements are called morphisms from x to y in O; C. for every object x∈Ob(O), a specified morphism, denoted idx∈O1(x;x) and called the identity morphism on x.

### `Definition 7.4.1.8` — [PDF Page 564]
> Definition 7.4.1.8. Let O and O′ be operads. An operad functor from O to O′, denoted F:O→O′, is defined as follows. One announces some constituents (A. on-objects part, B. on-morphisms part) and shows that they conform to some laws (1. preservation of identities, 2. preservation of composition). Specifically, one announces A. a function Ob(F):Ob(O)→Ob(O′), sometimes denoted simply F:Ob(O)→Ob(O′); B. for each object y∈Ob(O), finite set n ∈ Ob(Fin), and n-indexed set of objects x:n→Ob(O), a function Fn:On(x;y)→On′(Fx;Fy). One must then show that the following operad functor laws hold: 1. For each object x∈Ob(O), the equation F(idx) = idFx holds

### `Definition 7.4.1.10` (Operad algebra) — [PDF Page 565]
> Definition 7.4.1.10 (Operad algebra). Let O be an operad, and let Sets be the operad from Example 7.4.1.5. An algebra on O is an operad functor A:O→Sets.

### `Application 7.4.2.1` — [PDF Page 567]
> Application 7.4.2.1. Every material is composed of constituent materials, arranged in certain patterns. (In case the material is pure, we consider the material to consist of itself as the sole constituent.) Each of these constituent materials is itself an arrangement of constituent materials. Thus a kind of self-similarity can be modeled with operads. For example, a tendon is made of collagen fibers that are assembled in series and then in parallel, in a specific way. Each collagen fiber is made of collagen fibrils that are again assembled in series and then in parallel, with slightly different specifications. We can continue, perhaps indefin

### `Application 7.4.2.2` — [PDF Page 567]
> Application 7.4.2.2. Suppose we have chosen an operad O to model the structure of materials. Say each object of O corresponds to a certain quality of material, and each morphism corresponds to an arrangement of various qualities to form a new quality. An algebra A:O→Sets on O requires us to choose what substances will fill in for these qualities. For every object x∈Ob(O), we want a set A(x) that will be

### `Application 7.4.2.6` — [PDF Page 569]
> Application 7.4.2.6. Suppose we are trying to model life in the following way. We define an entity as a set of available experiences. We also want to be able to put entities together to form a superentity, so we have a notion of morphism f : (X1, …, Xn) → Y defined as a relation, as in (7.20). The idea is that the morphism f is a way of translating between the experiences available to the subentities and the experiences available to the superentity. The superentity Y consists of some available experiences, like “hunger” ∈ Y. The subentities Xi each have their own set of available experiences, like “U88fh” ∈ X2. The relation R ⊆ X1 × … × Xn × 

### `Application 7.4.2` — [PDF Page 570]
> Application 7.4.2.8 using this algebra.

### `Application 7.4.2.8` — [PDF Page 570]
> Application 7.4.2.8. Following Application 7.4.2.6 we can use Example 7.4.2.7 as a model of survival. Each entity Y survives only for a subset of the phenomena that it can experience. Under this interpretation, the algebra from Example 7.4.2.7 defines survival of an entity as the survival of all parts. Suppose that we understand how the experiences of a superentity Y relate to those of subentities X1, …, Xn in the sense that we have a morphism f : (X1, …, Xn) → Y in R. In the language of Application 7.4.2.6, we have a translation between the set of experiences available across the sub-entities and the set of experiences available to the super

### `Application 7.4.2.14` — [PDF Page 575]
> Application 7.4.2.14. In cognitive neuroscience or in industrial economics, it may be that we want to understand the behavior of an entity such as a mind, a society, or a business in terms of its structure. Knowing the connection pattern (connectome, supply chain) of subentities should help us understand how big changes are generated from small ones.

### `Application 7.4.2.15` — [PDF Page 575]
> Application 7.4.2.15. In [36], Radul and Sussman discuss propagator networks. Their implementation can presumably be understood in terms of wiring diagrams and their algebra of relations.

### `Example 7.4.1.3` (Little squares operad) — [PDF Page 561]
> Example 7.4.1.3 (Little squares operad). An operad commonly used in mathematics is called the little n-cubes operad. We will focus on n = 2 and talk about the little squares operad O. Here the set of objects has only one element, denoted by a square, Ob(O)={▫}. For a natural number n ∈ ℕ, a morphism f : (▫, ▫, …, ▫) → ▫ is a positioning of n nonoverlapping squares inside of a square. Figure 7.5 shows a morphism (X1, X2, X3) → Y, where X1 = X2 = X3 = Y = ▫. The composition formula says that given a positioning of small squares inside a large square, and given a positioning of tiny squares inside each of those small squares, we get a positionin

### `Example 7.4.1` — [PDF Page 561]
> Example 7.4.1.3 exemplifies the kind of self-similarity mentioned on page 362.

### `Example 7.4.1.5` — [PDF Page 563]
> Example 7.4.1.5. Let Sets denote the operad defined as follows. As objects we put Ob(Sets) = Ob(Set). For a natural number n ∈ ℕ and sets X1, …, Xn, Y, put HomSets(X1,…,Xn;Y)≔HomSet(X1×⋯×Xn,Y). Given functions f1:(X1,1×⋯×X1,m1)→Y1 through fn:(Xn,1×⋯×Xn,mn)→Yn and a function Y1 × ⋯ × Yn → Z, the universal property provides a unique function of the form (X1,1×⋯×Xn,mn)→Z, giving rise to the composition formula in Sets. 7.4.1.6 Operads: functors and algebras If operads are like categories, then we can define things like functors and call them operad functors.

### `Example 7.4.2.5` — [PDF Page 568]
> Example 7.4.2.5. Here we describe an operad of relations, denoted R. The objects are sets, Ob(R)=Ob(Set). A morphism f : (X1, X2, …, Xn) → Y in R is a relation

### `Example 7.4.2.7` — [PDF Page 569]
> Example 7.4.2.7. Let R be the operad of relations from Example 7.4.2.5, and

### `Example 7.4.2.10` — [PDF Page 571]
> Example 7.4.2.10. This example discusses wiring diagrams. This operad is denoted W (see [41]). An object of W is just a finite set, Ob(W)=Ob(Fin), elements of which are called wires. A morphism in W is shown in Figure 7.8 (see page 382) and is formalized as follows. Given objects C1, …, Cn, and D, a morphism (C1, …, Cn) → D is a commutative diagram of sets such that p and q are jointly surjective. Composition of morphisms is easily understood in graphic form: Given wiring diagrams inside of wiring diagrams, we can throw away the intermediary circles. In terms of sets, we first take the pushout PO: and then take the composition to be the image

### `Example 7.4.2.12` — [PDF Page 573]
> Example 7.4.2.12. Let’s continue with the operad W of wiring diagrams, and try to form an algebra on it. Taking R to be the operad of relations as described in

### `Example 7.4.2` — [PDF Page 573]
> Example 7.4.2.5, there is an operad functor Q:W→R. It assigns to each C∈Ob(W) the set ℤC∈Ob(R)=Ob(Set). To a morphism G : (C1, …, Cn) → D as in (7.21) it assigns the relation ℤG⊆(∏i∈n¯ℤCi)×ℤD. The idea is that to an entity defined as having a bunch of cables carrying integers, a phenomenon is the same thing as a choice of integer on each cable. A wiring diagram translates between phenomena experienced locally and phenomena experienced globally.

## 6. Page-by-Page Deep Index (PDF Pages 557–584)
- **Page 557** (`7.4 Operads`) · **Items:** Warning 7.4.0.4: 7.4 Operads This section briefly introduces operads, which are generalizations of categories. They often are useful for speaking about self-similarity of structure. For example, we use operads to model agents made up of smaller agents, or materials made up of smaller materials. This association with self-similarity is ...
- **Page 558** (`7.4 Operads`): ...
- **Page 559** (`7.4 Operads`) · **Items:** Definition 7.4.1.1: 7.4.1 Definition and classical examples An operad is like a category in that it has objects, morphisms, and a composition formula, and it obeys an identity law and an associativity law. The difference is that each morphism f in an operad can have many inputs (and one output): The description of composition in an operad...
- **Page 560** (`7.4 Operads`) · **Items:** Remark 7.4.1.2: D. Let s : m → n be a morphism in Fin. Let z∈Ob(O) be an object, let y:n→Ob(O) be an n-indexed set of objects, and let x:m→Ob(O) be an m- indexed set of objects. For each element i ∈ n, write mi ≔ s−1(i) for the pre-image of s under i, and write xi=x|mi:mi→Ob(O) for the restriction of x to mi. Then one announces a func...
- **Page 561** (`7.4 Operads`) · **Items:** Example 7.4.1.3, Example 7.4.1, Exercise 7.4.1.4, Figure 7.5: and how it relates to an action of a symmetric group on each morphism set in the definition of operad. We follow the notation of Definition 7.4.1.1, especially the use of subscripts in the composition formula. Suppose that O is an operad, z∈Ob(O) is an object, y:n→Ob(O) is an n- indexed set of objects, and ϕ : y → z is...
- **Page 562** (`7.4 Operads`) · **Items:** Solution 7.4.1.4: except with three objects: square, circle, equilateral triangle. A morphism is again a nonoverlapping positioning of shapes inside a shape. a. Draw an example of a morphism f from two circles and a square to a triangle. b. Find three other morphisms that compose into f, and draw the composite. Solution 7.4.1.4. a. b....
- **Page 563** (`7.4 Operads`) · **Items:** Example 7.4.1.5, Warning 7.4.1.7: Example 7.4.1.5. Let Sets denote the operad defined as follows. As objects we put Ob(Sets) = Ob(Set). For a natural number n ∈ ℕ and sets X1, …, Xn, Y, put HomSets(X1,…,Xn;Y)≔HomSet(X1×⋯×Xn,Y). Given functions f1:(X1,1×⋯×X1,m1)→Y1 through fn:(Xn,1×⋯×Xn,mn)→Yn and a function Y1 × ⋯ × Yn → Z, the universal property provi...
- **Page 564** (`7.4 Operads`) · **Items:** Definition 7.4.1.8, Exercise 7.4.1.9: operads and morphisms in an operad is confusing. It is similar to what would occur in regular category theory (see Chapter 5) if we replaced the term functor with the term category morphism. Definition 7.4.1.8. Let O and O′ be operads. An operad functor from O to O′, denoted F:O→O′, is defined as follows. One announces...
- **Page 565** (`7.4 Operads`) · **Items:** Definition 7.4.1.10, Remark 7.4.1.11: Definition 7.4.1.10 (Operad algebra). Let O be an operad, and let Sets be the operad from Example 7.4.1.5. An algebra on O is an operad functor A:O→Sets. Remark 7.4.1.11. Every category can be construed as an operad (there is a functor Cat → Oprd), one in which every morphism is unary. That is, given a category C, one ...
- **Page 566** (`7.4 Operads`): ...
- **Page 567** (`7.4 Operads`) · **Items:** Application 7.4.2.1, Application 7.4.2.2: 7.4.2 Applications of operads and their algebras Hierarchical structures seem to be well modeled by operads. A hierarchical structure often has basic building blocks and instructions for how they can be put together into larger building blocks. Describing such structures using operads and their algebras allows one to m...
- **Page 568** (`7.4 Operads`) · **Items:** Exercise 7.4.2.3, Example 7.4.2.5: the set of materials with that quality. For every arrangement, i.e., morphism, f : (x1, …, xn) → y, and every choice a1 ∈ A(x1), …, an ∈ A(xn) of materials, we need to understand what material a′ = A(f)(a1, …, an) ∈ A(y) will emerge when materials a1, …, an are arranged in accordance with f. There may be more than one ...
- **Page 569** (`7.4 Operads`) · **Items:** Application 7.4.2.6, Example 7.4.2.7: R⊆X1×X2×⋯×Xn×Y.(7.20) We use a composition formula similar to that in Definition 3.2.2.3. Namely, to compose relations R1, …, Rn with S, we first form a fiber product, denoted FP: We have an induced function FP→(∏i∈n¯∏j∈mi¯Xi,j)×Z, and its image is the subset we take to be the composite: S○(R1,…,Rn)⊆(∏i∈n¯∏j∈mi¯Xi,j)×Z...
- **Page 570** (`7.4 Operads`) · **Items:** Application 7.4.2, Application 7.4.2.8, Exercise 7.4.2.9: recall that Ob(R)=Ob(Set). Consider the algebra S:R→Sets given by S(X) = ℙ(X) for X∈Ob(R). Given a morphism R ⊆ ∏i Xi × Y and subsets Xi′⊆Xi, we have a subset ∏iXi′⊆∏iXi. We take the fiber product and the image of FP → Y is a subset of Y, as needed. We will continue with Application 7.4.2.8 using this algebra. Applicat...
- **Page 571** (`7.4 Operads`) · **Items:** Example 7.4.2.10: as a 2-ary morphism R1 : (A, B) → M, a 1-ary morphism R2 : (C) → N, and a 2-ary morphism S : (M, N) → Z in the operad R? b. What is the domain and codomain of the composite S ○ (R1, R2)? c. Write the composite S ○ (R1, R2) as a relation. Example 7.4.2.10. This example discusses wiring diagrams. This operad is denoted W...
- **Page 572** (`7.4 Operads`) · **Items:** Exercise 7.4.2.11, Solution 7.4.2.11: Exercise 7.4.2.11. Let C1 = {a, b, m}, C2 = {c, n}, C3 = {m, n, z}, let C = C1 ⊔ C2 ⊔ C3, and let D = {a, c, z}. a. Suppose we draw C1, C2, and C3 as follows: Follow those examples to draw D. b. What set G and functions C→pG←qD in (7.21) correspond to this picture? Solution 7.4.2.11. a. We can draw D = {a, c, z} as fol...
- **Page 573** (`7.4 Operads`) · **Items:** Example 7.4.2.12, Example 7.4.2: b. Here G = {a, b, m, c, n, z}. The functions C→pG←qD are given in the following tables: Example 7.4.2.12. Let’s continue with the operad W of wiring diagrams, and try to form an algebra on it. Taking R to be the operad of relations as described in Example 7.4.2.5, there is an operad functor Q:W→R. It assigns to each C...
- **Page 574** (`7.4 Operads`) · **Items:** Exercise 7.4.2.13: Now recall the algebra S:R→Set from Example 7.4.2.7. We can compose with Q to get Q′≔S○Q:W→Set. Exercise 7.4.2.13. Consider the wiring diagrams operad W from Example 7.4.2.10. Let’s continue with Exercise 7.4.2.11 so that “everything,” i.e., C1, C2, C3, D, G, i, and j, are as in that exercise. By Example 7.4.2.12 we ha...
- **Page 575** (`7.4 Operads`) · **Items:** Application 7.4.2.14, Application 7.4.2.15: what is G(q1, q2, q3) ∈ Q′(D)? Application 7.4.2.14. In cognitive neuroscience or in industrial economics, it may be that we want to understand the behavior of an entity such as a mind, a society, or a business in terms of its structure. Knowing the connection pattern (connectome, supply chain) of subentities should he...
- **Page 576** (`7.4 Operads`) · **Items:** Figure 7.1: Figure 7.1 Three overlapping views of the night sky. Source: NASA, ESA, Digitized Sky Survey Consortium....
- **Page 577** (`7.4 Operads`) · **Items:** Figure 7.2: Figure 7.2 The three overlapping views have been glued together into one coherent view....
- **Page 578** (`7.4 Operads`) · **Items:** Figure 7.4: Figure 7.4 The composition of morphisms f1 and f2 with g....
- **Page 579** (`7.4 Operads`) · **Items:** Figure 7.5: Figure 7.5 A morphism (X1, X2, X3) → Y in an operad with only one object, ▫....
- **Page 580** (`7.4 Operads`) · **Items:** Figure 7.6, Figure 7.7: Figure 7.6 A morphism (X1, X2, X3) → Y and morphisms (W1,1, W1,2) → X1, (W2,1, W2,2, W2,3) → X2, and (W3,1) → X3, each of which is a positioning of squares inside a square. The composition formula is given by scaling and positioning the squares to give (W1,1, W1,2, W2,1, W2,2, W2,3, W3,1) → Y. Figure 7.7 A morphism exp...
- **Page 581** (`7.4 Operads`): from smaller materials....
- **Page 582** (`7.4 Operads`) · **Items:** Figure 7.8: Figure 7.8 Morphisms in a wiring diagram operad W. Composition of wiring diagrams is given by substitution. __________________ 1Throughout this definition, notice that B’s come before A’s, especially in (7.1), which might be confusing. It was a stylistic choice to match with the Babies and Adults discussion. 2The natur...
- **Page 583** (`7.4 Operads`): 5FQL is available on the Internet. See http://categoricaldata.net/fql.html. 6This example was taken from Spivak [38]. 7Repeated for convenience, I:C→Set is 8Technically C has to be small but, as mentioned in Remark 5.1.1.2), we do not worry about that distinction in this book. 9There is a lot of clutter here. Note that...
- **Page 584** (`7.4 Operads`): the Child table of YChild. Assuming that the math follows the meaning, if ☺ points to Amy, where should firstChild(mother(☺)) point? 10Parentheses are used to denote open intervals of real numbers. For example, (6, 9) denotes the set {x ∈ ℝ | 6 < x < 9}. 11This requirement is somewhat stringent, but it can be mitigated...
