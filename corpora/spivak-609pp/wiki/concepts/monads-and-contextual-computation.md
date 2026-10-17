---
id: monads-and-contextual-computation
title: "Monads (T, η, μ): Formalizing Experimental & Computational Context"
type: SheafStalk
chapter: 7
section: "7.3.1–7.3.2"
pdf_pages: "527–539"
symbol: "(T : C → C, η : id ⇒ T, μ : T∘T ⇒ T)"
layer: "Context & Operadic Layer"
extracted_declarations: 13
restricts_to: [natural-transformations-functor-cat]
glues_with: [kleisli-categories-scientific-method]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Monads (T, η, μ): Formalizing Experimental & Computational Context (`(T : C → C, η : id ⇒ T, μ : T∘T ⇒ T)`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.3.1–7.3.2` · **PDF Pages 527–539**

## 1. Epistemic Worldview & Intuition

In pure Set, functions must be total, deterministic, and context-free. In real science and computing, processes may fail (partiality B ⊔ {☺}), produce multiple outcomes (powerset P(B)), carry probabilistic uncertainty (Dist(B)), or depend on an experimental environment (B^E). A monad (T, eta, mu) packages such a context functor T with a unit natural transformation eta (injecting a pure value into a trivial context) and a multiplication natural transformation mu (flattening nested contexts T(T(B)) -> T(B)).

## 2. Formal Categorical Core

Definition 7.3.2.1 (p. 533): A monad on C consists of an endofunctor T : C -> C, a unit natural transformation eta : id_C => T, and a multiplication natural transformation mu : T o T => T obeying: (1) Left/Right Unit Laws: mu o (T eta) = id_T = mu o (eta T); (2) Associativity Law: mu o (T mu) = mu o (mu T).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *a pure value x in X*
- **`[TX]`** — *a contextualized outcome in T(X)*
- **`[TTX]`** — *a doubly-contextualized outcome in T(T(X))*

### Functional Aspects (Morphisms)
- **`[X]` $\xrightarrow{\text{embeds into trivial context via unit η_X}}$ `[TX]`**
- **`[TTX]` $\xrightarrow{\text{flattens nested context via multiplication μ_X}}$ `[TX]`**

### Commutative Path Facts ($p \simeq q$)
- Monad Unit Laws: μ ∘ Tη = id_T = μ ∘ ηT (Definition 7.3.2.1, p. 533).
- Monad Associativity Square: μ ∘ Tμ = μ ∘ μT (flattening 3 nested layers T³ -> T is order-independent).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-47` (endofunctor_monoid_in_Fun)** $\to$ [[natural-transformations-functor-cat]] (*Natural Transformations & The Category of Database Instances*, p. 338–370): A monad (T, η, μ) is an endofunctor T : C -> C with natural transformations η : id ⇒ T and μ : T² ⇒ T — `μ ∘ Tμ = μ ∘ μT`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-49` (kleisli_category_of_monad)** $\leftarrow$ [[kleisli-categories-scientific-method]] (*Kleisli Categories C_T & Reconciling the Scientific Method Olog*, p. 540–556): Kleisli arrows X -> Y in C_T are contextual morphisms X -> T(Y) composed via μ — `g ∘_K f = μ_Z ∘ T(g) ∘ f`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-08` — The Adjunction-Monad-Kleisli Triangle** ([[kleisli-categories-scientific-method]], [[monads-and-contextual-computation]], [[adjoint-functors-hom-iso]]): Every adjunction L ⊣ R generates a monad (T = R∘L, η, μ = RεL), and the Kleisli category C_T is the initial adjunction realizing T. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 527–539)

### `Definition 7.3.2.1` (Monad) — [PDF Page 533]
> Definition 7.3.2.1 (Monad). A monad on Set is defined as follows: One announces some constituents (A. functor, B. unit map, C. multiplication map) and shows that they conform to some laws (1. unit laws, 2. associativity law). Specifically, one announces A. a functor T : Set → Set, B. a natural transformation η : idSet → T, C. a natural transformation µ : T ○ T → T. We sometimes refer to the functor T as though it were the whole monad; we call η the unit map and µ the multiplication map. One must then show that the following monad laws hold: 1. The following diagrams of functors Set → Set commute: 2. The following diagram of functors Set → Set

### `Definition 7.3.2` — [PDF Page 535]
> Definition 7.3.2.1 can be exemplified as follows:

### `Application 7.3.1.3` — [PDF Page 530]
> Application 7.3.1.3. Experiments are supposed to be performed objectively, but suppose we imagine that changing the person who performs the experiment, say, in psychology, may change the outcome. Let A be the set of experimenters, let X be the parameter space for the experimental variables (e.g., X = Age × Income), and let Y be the observation space (e.g., Y = propensity for violence). We want to think of such an experiment as telling us about a function f : X → Y (how age and income affect propensity for violence). However, we may want to make some of the context explicit by including information about who performed the experiment. That is, 

### `Example 7.3.1.1` (Partial functions) — [PDF Page 529]
> Example 7.3.1.1 (Partial functions). Partial functions can be modeled by ordinary functions if we add a special “no answer” element to the codomain. That is, the set of partial functions A → B is in one-to-one correspondence with the set of ordinary functions A → B ⊔ {☺}. For example, suppose we want to model the partial function fp(x)≔1x2−1:ℝ→ℝ in this way; we would use the total function ft : ℝ → ℝ ⊔ {☺} defined as: f(x)≔{1x2−1if x≠−1 and x≠1,☺if x=−1,☺if x=1. An ordinary function g : A → B can be considered a partial function because we can compose it with the inclusion B→B⊔{☺}.(7.11) to get A → B ⊔ {☺}. But how do we compose two partial f

### `Example 7.3.2.2` (List monad) — [PDF Page 534]
> Example 7.3.2.2 (List monad). We now go through Definition 7.3.2.1 using the List monad. The first step is to give a functor List: Set → Set, which was done in

### `Example 5.1.2.20` — [PDF Page 534]
> Example 5.1.2.20. Recall that if X = {p, q, r}, then List(X) includes the empty list [ ], singleton lists such as [p], and any other list of elements in X such as [p, p, r, q, p]. Given a function f : X → Y, one obtains a function List(f) : List(X) → List(Y) by entrywise application of f, as in Exercise 5.1.2.22. As a monad, the functor List comes with two natural transformations, a unit map η and a multiplication map µ. Given a set X, the unit map ηX : X → List(X) returns singleton lists as follows: Given a set X, the multiplication map µX : List(List(X)) → List(X) concatenates lists of lists as follows:

### `Example 7.3.2.4` (Partial functions as a monad) — [PDF Page 537]
> Example 7.3.2.4 (Partial functions as a monad). Here is the monad for partial functions, as discussed in Example 7.3.1.1. The functor T : Set → Set sends a set X to the set X ⊔ {☺}. Clearly, given a function f : X → Y, there is an induced function (f ⊔ {☺}) : (X ⊔ {☺}) → (Y ⊔ {☺}), so this is a functor. The natural transformation η : id → T is given on a set X by the component function ηX:X→X⊔{☺} that includes X ↪ X ⊔ {☺}. Finally, the natural transformation µ : T ○ T → T is given on a set X by the component function µX:X⊔{☺}⊔{☺}→X⊔{☺} that collapses both copies of ☺.

### `Example 7.3.2.6` — [PDF Page 538]
> Example 7.3.2.6. Fix a set A. Let T : Set → Set be the functor given by T(X) = XA = HomSet(A, X); this is a functor. For a set X and an element x ∈ X, let cx : A → X be the constant-x function, cx(a) = x for all a ∈ A. Define ηX : X → T(X) to be given by the constant-x function, x ↦ cx. Now we have to specify a natural transformation µ : T ○ T → T, i.e., for each X ∈ Ob(Set), we need to provide an X-component function µX:(XA)A→XA. By currying (see Example 7.1.1.8), this is equivalent to providing a function (XA)A × A → X. For any Y ∈ Ob(Set), we have an evaluation function (see Exercise 3.4.2.5) ev : YA × A → Y. We use it twice and find the d

### `Remark 7.3.2.7` — [PDF Page 538]
> Remark 7.3.2.7. Monads can be defined on categories other than Set. In fact, for any category C, one can take Definition 7.3.2.1 and replace every occurrence of Set with C and obtain the definition for monads on C. We have actually seen a monad (Paths, η, µ) on the category Grph of graphs before, namely, in Examples 5.3.1.15 and 5.3.1.16. That is, Paths: Grph → Grph, which sends a graph to its paths-graph is the functor part. The unit map η includes a graph into its paths- graph using the observation that every arrow is a path of length 1. And the multiplication map µ concatenates paths of paths. The Kleisli category of this monad (see Defini

### `Exercise 7.3.1.2` — [PDF Page 530]
> Exercise 7.3.1.2. a. Let f : ℤ → ℤ ⊔ {☺} be the partial function given by f(n)=1n2−n. Calculate the following: f(−3), f(−2), f(−1), f(0), f(1), and f(2). b. Let g : ℤ → ℤ ⊔ {☺} be the partial function given by g(n)={n2−3if n−1,☺if n<−1 Write f ○ g(n) for −3 n 2.

### `Exercise 7.3.2.3` — [PDF Page 535]
> Exercise 7.3.2.3. Let ℙ : Set → Set be the power-set functor, so that given a function f : X → Y, the function ℙ(f) : ℙ(X) → ℙ(Y) is given by taking images. a. Make sense of the statement, “With η defined by singleton subsets and with µ defined by union, T≔(ℙ,η,µ) is a monad.” b. With X = {a, b}, write the function ηX as a two-row, two-column table. c. With X = {a, b}, write the function µX as a sixteen-row, two-column table (you can stop after five rows if you fully understand it). d. Check that you believe the monad laws from Definition 7.3.2.1.

### `Exercise 7.3.2.5` — [PDF Page 537]
> Exercise 7.3.2.5. Let E be a set with elements refered to as exceptions. We imagine exceptions

### `Solution 7.3.2.3` — [PDF Page 536]
> Solution 7.3.2.3. a. The statement suggests that the components of η : idSet → ℙ can be defined using the concept of singleton subsets and that the components of µ : ℙ ○ ℙ → ℙ can be defined using the concept of union. Given a set X ∈ Ob(Set), we need a function ηX : X → ℙ(X), meaning that for every element x ∈ X, we need a subset of X. The statement suggests we send x to the singleton subset {x} ⊆ X. The statement also suggests that we obtain µX : ℙ(ℙ(X)) → ℙ(X) by sending a set of subsets to their union. For example, if X = {1, 2, 3, 4, 5}, then an element T ∈ ℙ(ℙ(X)) might look like {{1, 2}, Ø, {1, 3, 5}}; the union of these subsets is µX(

## 6. Page-by-Page Deep Index (PDF Pages 527–539)
- **Page 527** (`7.3 Monads`): 7.3 Monads Monads would probably not have been invented without category theory, but they have been useful in understanding algebraic theories, calculating invariants of topological spaces, and embedding nonfunctional operations into functional programming languages. We mainly discuss monads in terms of how they can he...
- **Page 528** (`7.3 Monads`): ...
- **Page 529** (`7.3 Monads`) · **Items:** Example 7.3.1.1: 7.3.1 Monads formalize context Monads can formalize assumptions about the way one does business throughout a domain. For example, suppose we want to consider functions that are not required to return a value for all inputs. These are not valid functions as defined in Section 2.1.2 (because they are not total), but in m...
- **Page 530** (`7.3 Monads`) · **Items:** Exercise 7.3.1.2, Application 7.3.1.3: C⊔{☺}⊔{☺}→C⊔{☺}.(7.12) How should one think about composing partial functions g ○ f? Every element a ∈ A is sent by f either to an element b ∈ B or to “no answer.” If it has an answer f(a) ∈ B, then this again is sent by g either to an element g(f(a)) ∈ C or to “no answer.” We get a partial function A → C by sending a ...
- **Page 531** (`7.3 Monads`): We return to this in Examples 7.3.2.6 and 7.3.3.4....
- **Page 532** (`7.3 Monads`): ...
- **Page 533** (`7.3 Monads`) · **Items:** Definition 7.3.2.1: 7.3.2 Definition and examples What aspects of Example 7.3.1.1 are about monads, and what aspects are about partial functions in particular? Monads are structures involving a functor and a couple of natural transformations. Roughly speaking, the functor for partial functors was B ↦ B ⊔ {☺}, and the natural transformatio...
- **Page 534** (`7.3 Monads`) · **Items:** Example 7.3.2.2, Example 5.1.2.20: Example 7.3.2.2 (List monad). We now go through Definition 7.3.2.1 using the List monad. The first step is to give a functor List: Set → Set, which was done in Example 5.1.2.20. Recall that if X = {p, q, r}, then List(X) includes the empty list [ ], singleton lists such as [p], and any other list of elements in X such ...
- **Page 535** (`7.3 Monads`) · **Items:** Definition 7.3.2, Exercise 7.3.2.3: The naturality of η and µ means that these maps work appropriately well under entrywise application of a function f : X → Y. Finally, the three monad laws from Definition 7.3.2.1 can be exemplified as follows: Exercise 7.3.2.3. Let ℙ : Set → Set be the power-set functor, so that given a function f : X → Y, the function...
- **Page 536** (`7.3 Monads`) · **Items:** Solution 7.3.2.3: Solution 7.3.2.3. a. The statement suggests that the components of η : idSet → ℙ can be defined using the concept of singleton subsets and that the components of µ : ℙ ○ ℙ → ℙ can be defined using the concept of union. Given a set X ∈ Ob(Set), we need a function ηX : X → ℙ(X), meaning that for every element x ∈ X, we n...
- **Page 537** (`7.3 Monads`) · **Items:** Example 7.3.2.4, Exercise 7.3.2.5: {Ø, {b}} {b} {Ø, {a, b}} {a, b} {{a}, {b}} {a, b} {{a, {a, b}}} {a, b} {{b}, {a, b}} {a, b} {Ø, {a}, {b}} {a, b} {Ø, {a}, {a, b}} {a, b} {Ø, {b}, {a, b}} {a, b} {{a}, {b}, {a, b}} {a, b} {Ø, {a}, {b}, {a, b}} {a, b} d. The monad laws hold. One says that if we take all the singleton subsets of X and union them, we get X...
- **Page 538** (`7.3 Monads`) · **Items:** Example 7.3.2.6, Remark 7.3.2.7: as warnings like “overflow!” or “division by zero!” and we imagine that a function f : X → Y outputs either a value or one of these exceptions. Let T : Set → Set be the functor X ↦ X ⊔ E. Follow Example 7.3.2.4 and find a unit map η and a multiplication map µ for which (T, η, µ) is a monad. Example 7.3.2.6. Fix a set A...
- **Page 539** (`7.3 Monads`): ...
