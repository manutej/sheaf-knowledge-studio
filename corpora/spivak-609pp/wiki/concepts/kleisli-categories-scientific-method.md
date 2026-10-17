---
id: kleisli-categories-scientific-method
title: "Kleisli Categories C_T & Reconciling the Scientific Method Olog"
type: SheafStalk
chapter: 7
section: "7.3.3–7.3.5"
pdf_pages: "540–556"
symbol: "Hom_{C_T}(X, Y) = Hom_C(X, T(Y))"
layer: "Context & Operadic Layer"
extracted_declarations: 24
restricts_to: [scientific-agreement-worldviews, monads-and-contextual-computation, adjoint-functors-hom-iso]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Kleisli Categories C_T & Reconciling the Scientific Method Olog (`Hom_{C_T}(X, Y) = Hom_C(X, T(Y))`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.3.3–7.3.5` · **PDF Pages 540–556**

## 1. Epistemic Worldview & Intuition

Given a monad (T, eta, mu) on Set, its Kleisli category Set_T has the same objects as Set, but a morphism X -> Y in Set_T is a contextual function X -> T(Y) in Set! Composition in Set_T chains X -> T(Y) with Y -> T(Z) via X -> T(Y) -> T(T(Z)) --mu_Z--> T(Z). In Example 7.3.3.10 (p. 544), Spivak resolves the Chapter 1 paradox of Figure 1.1: the scientific method olog (Observation -> Hypothesis -> Prediction -> Experiment -> Observation) is a valid commutative diagram in the Kleisli category of the expert-experimentation monad!

## 2. Formal Categorical Core

Definition 7.3.3.1 (p. 540): Given a monad (T, eta, mu) on Set, the Kleisli category Set_T has Ob(Set_T) = Ob(Set), Hom_{Set_T}(X, Y) = Hom_Set(X, T(Y)), identity id^K_X = eta_X : X -> T(X), and Kleisli composition g o_K f = mu_Z o T(g) o f. Proposition 7.3.5.1 (p. 553): Every adjunction L -| R induces a monad T = R o L on the domain of L.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *an input type X (e.g., a prediction)*
- **`[TY]`** — *a contextualized intermediate T(Y) (e.g., expert-dependent experiment)*
- **`[TTZ]`** — *a nested context T(T(Z))*
- **`[TZ]`** — *a flattened contextual output T(Z) (e.g., resulting observation)*

### Functional Aspects (Morphisms)
- **`[X]` $\xrightarrow{\text{maps via Kleisli arrow f : X -> T(Y) to}}$ `[TY]`**
- **`[TY]` $\xrightarrow{\text{lifts second stage via T(g) to}}$ `[TTZ]`**
- **`[TTZ]` $\xrightarrow{\text{flattens context via μ_Z to}}$ `[TZ]`**
- **`[X]` $\xrightarrow{\text{composes in Set_T via g ∘_K f to}}$ `[TZ]`**

### Commutative Path Facts ($p \simeq q$)
- Kleisli Composition Formula: g ∘_K f = μ_Z ∘ T(g) ∘ f (Definition 7.3.3.1, p. 540).
- Closing the Book's Arc (Example 7.3.3.10, p. 544): Figure 1.1 from page 11 is rigorously valid as an olog in the Kleisli category Set_T.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-48` (resolves_Figure_1_1_paradox)** $\to$ [[scientific-agreement-worldviews]] (*Science as Agreement & Categorical Worldviews*, p. 11–25): Example 7.3.3.10 resolves Chapter 1's Figure 1.1 scientific method olog inside the Kleisli category Set_T — `Fig 1.1 ∈ Diag(Set_T)`
- **`rho-49` (kleisli_category_of_monad)** $\to$ [[monads-and-contextual-computation]] (*Monads (T, η, μ): Formalizing Experimental & Computational Context*, p. 527–539): Kleisli arrows X -> Y in C_T are contextual morphisms X -> T(Y) composed via μ — `g ∘_K f = μ_Z ∘ T(g) ∘ f`
- **`rho-50` (adjunction_induces_monad)** $\to$ [[adjoint-functors-hom-iso]] (*Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges*, p. 461–480): Every adjunction L ⊣ R generates a monad T = R ∘ L, and every monad factors through its Kleisli adjunction — `T = R ∘ L`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-05` — The Scientific Method Kleisli Closure Triangle (Ch 1 -> Ch 2 -> Ch 7)** ([[kleisli-categories-scientific-method]], [[ologs-ontology-logs]], [[scientific-agreement-worldviews]]): Figure 1.1's informal scientific method cycle fails as a pure Set-olog (Ch 2) due to expert context, but commutes rigorously as a Kleisli olog in Set_T (Ex 7.3.3.10). *[H^1 Obstruction in pure Set -> Resolved in H^0(Set_T) via Monad Context]*
- **`tau-08` — The Adjunction-Monad-Kleisli Triangle** ([[kleisli-categories-scientific-method]], [[monads-and-contextual-computation]], [[adjoint-functors-hom-iso]]): Every adjunction L ⊣ R generates a monad (T = R∘L, η, μ = RεL), and the Kleisli category C_T is the initial adjunction realizing T. *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 540–556)

### `Definition 7.3.3.1` — [PDF Page 540]
> Definition 7.3.3.1. Let T=(T,η,µ) be a monad on Set. Form a new category, called the Kleisli category for T, denoted Kls(T), with sets as objects, Ob(Kls(T))≔Ob(Set), and with HomKls(T)(X,Y)≔HomSet(X,T(Y)) for sets X, Y. The identity morphism idX : X → X in Kls(T) is given by η : X → T(X) in Set. The composition of morphisms f : X → Y and g : Y → Z in Kls(T) is given as follows. Writing them as functions, we have f : X → T(Y) and g : Y → T(Z). The first step is to apply the functor T to g, giving T(g) : T(Y) → T(T(Z)). Then compose with f to get T(g) ○ f : X → T(T(Z)). Finally, compose with µZ : T(T(Z)) → T(Z) to get the required function X →

### `Definition 7.3.5.1` — [PDF Page 553]
> Definition 7.3.5.1. Let C and D be categories, and let L:C→D and R:D→C be functors with adjunction isomorphism αc,d:HomD(L(c),d)→ ≅ HomC(c,R(d)) for any objects c∈Ob(C) and d∈Ob(D) (see Definition 7.1.1.1). The unit η:idC→R○L (resp. the counit ϵ:L○R→idD) of the adjunction is a natural transformation defined as follows. Given an object c∈Ob(C), we apply α to idL(c) : L(c) → L(c) to get the c component ηc:c→R○L(c) of η. Similarly given an object d∈Ob(D) we apply α−1 to idR(d) : R(d) → R(d) to get the d component ϵd:L○R(d)→d. One checks that these components are natural. Later we see how to use the unit and counit of any adjunction to make a mon

### `Definition 7.3.2` — [PDF Page 554]
> Definition 7.3.2.1 can be generalized to arbitrary categories C by simply replacing every occurrence of the string Set with the string C. Similarly, the definition of Kleisli categories (Definition 7.3.3.1) considers only the case C=Set, but again the generalization to arbitrary categories C is straightforward.

### `Application 7.3.4.4` — [PDF Page 550]
> Application 7.3.4.4. Every star emits a spectrum of light, which can be understood as a distribution on the electromagnetic spectrum. Given an object B on earth, different parts of B will absorb radiation at different rates. Thus B produces a function from the electromagnetic spectrum to distributions of energy absorption. In the context of the probability distributions monad, we can record data on the schema •star→ emits •wavelengths→ absorbed by B •energies The composition formula for Kleisli categories is the desired one: to each star we

### `Example 7.3.3.4` — [PDF Page 540]
> Example 7.3.3.4.

### `Example 7.3.3.2` — [PDF Page 540]
> Example 7.3.3.2. Recall the monad T for partial functions, T(X) = X ⊔ {☺}, from

### `Example 7.3.2.4` — [PDF Page 540]
> Example 7.3.2.4. The Kleisli category Kls(T) has sets as objects, but a morphism f : X → Y means a function X → Y ⊔ {☺}, i.e., a partial function. Given another morphism g : Y → Z, the composition formula in Kls(T) ensures that g ○ f : X → Z has the appropriate behavior.

### `Example 7.3.3.4` — [PDF Page 541]
> Example 7.3.3.4. In this example we return to the setting laid out in Application 7.3.1.3, where we had a set A of experimenters and assumed that the person doing the experiment might affect the outcome. We use the monad T=(T,η,µ) from

### `Example 7.3.2` — [PDF Page 541]
> Example 7.3.2.6 and hope that Kls(T) will conform to the understanding of how to manage the effect of the experimenter on data. The objects of Kls(T) are ordinary sets, but a map f : X → Y in Kls(T) is a function X → YA. By currying, this is the same as a function X × A → Y, as desired. To compose f with g : Y → Z in Kls(T), we follow the formula from (7.13). It turns out to be equivalent to the following. We have a function X × A → Y and a function Y × A → Z. Multiplying by idA, we have a function X × A → Y × A, and we can now compose to get X × A → Z. What does this say in terms of experimenters affecting data gathering? It says that if we 

### `Example 7.3.3.8` — [PDF Page 543]
> Example 7.3.3.8. Let A be any preorder. We speak of A throughout this example as though it were the linear order given by time; however, the mathematics works for any A ∈ Ob(PrO). There is a monad T=(T,η,µ) that captures the idea that a function f : X → Y occurs in the context of time in the following sense: The output of f is determined not only by the element x ∈ X on which it is applied but also by the time at which it was applied to x; and the output of f occurs at another time, which is not before the time of input. The functor part of the monad is given on Y ∈ Ob(Set) by T(Y)={p:A→A×Y| if p(a)=(a′,y) then aa′}. The unit ηY : Y → T(Y) se

### `Example 7.3.3.8` — [PDF Page 543]
> Example 7.3.3.8. Given any set A, the usual state monad of type A is obtained by giving A the indiscrete preorder (see Example 4.4.4.5). More explicitly, it is a monad with functor part X↦(A×X)A

### `Example 7.3.3.10` — [PDF Page 544]
> Example 7.3.3.10. We reconsider Figure 1.1 reproduced as Figure 7.3. Figure 7.3 An olog whose arrows do not denote functions. It should be interpreted using a monad. It looks like an olog, and all ologs are database schemas (see Section 4.5.2.15). But how is “analyzed by a person yields” a function? For it to be a function, there must be only one hypothesis corresponding to a given observation. The very name of this arrow belies the fact that it is an invalid aspect in the sense of Section 2.3.2.1, because given an observation, there may be more than one hypothesis yielded, corresponding to which person is doing the observing. In fact, all th

### `Example 7.3.4.1` — [PDF Page 548]
> Example 7.3.4.1. Let T=(T,η,µ) be the monad for partial functions (see Example 7.3.1.1). Given any schema C, we can represent a Kleisli T-instance I:C→Kls(T) in tabular format. For every object c∈Ob(C) we have a set I(c) of rows, and given a column f : c → c′, applying f to a row either produces a value in I(c′) or fails to produce a value; this is the essence of partial functions. We might denote the absence of a value using ☺. Consider the schema indexing graphs As discussed in Section 5.2.1.21, an ordinary instance on C represents a graph:

### `Example 7.3.4.3` (Markov chains) — [PDF Page 550]
> Example 7.3.4.3 (Markov chains). Let Loop be the loop schema as in Example 4.5.2.10. A Dist-instance on Loop is equivalent to a time- homogeneous Markov chain. To be explicit, a functor δ : Loop → Kls(Dist) assigns to the unique object s ∈ Ob(Loop) a set S = δ(s), called the state space, and to f : s → s a function δ(f) : S → Dist(S), which sends each element x ∈ S to some probability distribution on elements of S. For example, the left-hand table δ (having states δ(s) = {a, b, c, d}) corresponds to the right-hand Markov matrix M: As one might hope, for any natural number n ∈ ℕ, the map fn : S → S in Kls(Dist) corresponds to the matrix Mn, wh

### `Example 7.3.5.2` — [PDF Page 553]
> Example 7.3.5.2. Consider the adjunction Set⇄UFMon between sets and monoids. Let T = U ○ F : Set → Set; this will be the functor part of the monad, and we have seen that T = List. The unit of the adjunction, η : idSet → U ○ F is

### `Example 7.3.5.3` — [PDF Page 554]
> Example 7.3.5.3. Let A ∈ Ob(Set) be a set, and recall the currying adjunction Set⇄ Y↦YA X↦X×A Set, discussed briefly in Example 7.1.1.8. The corresponding monad StA is typically called the state monad of type A in programming language theory. Given a set X, we have StA(X)=(A×X)A. In the Kleisli category Kls(StA) a morphism from X to Y is a function of the form X → (A × Y)A, but this can be curried to a function A × X → A × Y. As discussed in Remark 7.3.3.9, this monad is related to holding onto an internal state variable of type A. Under the state monad StA, every morphism written X → Y, when viewed as a function, takes as input not only an e

### `Remark 7.3.3.3` — [PDF Page 541]
> Remark 7.3.3.3. For any monad T=(T,η,µ) on Set, there is a functor i:Set→Kls(T), given as follows. On objects we have Ob(Kls(T))=Ob(Set), so take i = idOb(Set). Given a morphism f : X → Y in Set, we need a morphism i(f) : X → Y in Kls(T), i.e., a function i(f) : X → T(Y). We assign i(f) to be the composite X→fY→ηT(Y). The functoriality of this mapping follows from the unit law for monads.

### `Remark 7.3.3.9` — [PDF Page 543]
> Remark 7.3.3.9. One of the most important monads in computer science is the state monad. It is used when one wants to allow a program to mutate state variables (e.g., in the program if x 4, then x ≔ x + 1 else Print “done” x is a state variable). The state monad is a special case of the monad discussed in

## 6. Page-by-Page Deep Index (PDF Pages 540–556)
- **Page 540** (`7.3 Monads`) · **Items:** Example 7.3.3.4, Definition 7.3.3.1, Example 7.3.3.2, Example 7.3.2.4: 7.3.3 Kleisli category of a monad We are on our way to understanding how monads are used in computer science and how they may be useful for formalizing methodological context. There is only one more stop along the way, called the Kleisli category of a monad. For example, when we apply this Kleisli construction to the p...
- **Page 541** (`7.3 Monads`) · **Items:** Remark 7.3.3.3, Example 7.3.3.4, Example 7.3.2, Exercise 7.3.3.5, Exercise 7.3.2: Note how this monad allows us to make explicit a context in which all functions are assumed partial and then hide this context from our notation. Remark 7.3.3.3. For any monad T=(T,η,µ) on Set, there is a functor i:Set→Kls(T), given as follows. On objects we have Ob(Kls(T))=Ob(Set), so take i = idOb(Set). Given a morph...
- **Page 542** (`7.3 Monads`) · **Items:** Solution 7.3.3.5, Exercise 7.3.3.6, Solution 7.3.3.6, Exercise 7.3.3.7: Solution 7.3.3.5. a. A morphism A → B in Kls(T) is a function f : A → ℙ(B) in Set. From such a function we need to obtain a binary relation, i.e., a subset R ⊆ A × B. Recall that for any set X (e.g., X = B or X = A × B), we can identify the subsets of X with the functions X → Ω = {True, False}, using the characteristic...
- **Page 543** (`7.3 Monads`) · **Items:** Example 7.3.3.8, Remark 7.3.3.9, Example 7.3.3.8: closed under binary coproducts, i.e., every pair of objects A,B∈Ob(Kls(T)) has a coproduct in Kls(T). What is the coproduct of A = {1, 2, 3} and B = {a, b}? Example 7.3.3.8. Let A be any preorder. We speak of A throughout this example as though it were the linear order given by time; however, the mathematics works for ...
- **Page 544** (`7.3 Monads`) · **Items:** Example 7.3.3.10, Figure 7.3: (see Example 7.3.5.3). Example 7.3.3.10. We reconsider Figure 1.1 reproduced as Figure 7.3. Figure 7.3 An olog whose arrows do not denote functions. It should be interpreted using a monad. It looks like an olog, and all ologs are database schemas (see Section 4.5.2.15). But how is “analyzed by a person yields” a functi...
- **Page 545** (`7.3 Monads`): scientist to be modified by each function (i.e., the person is changed when analyzing an observation to yield a hypothesis)? These are all interesting possibilities. One reasonable choice would be to use the state monad of type A, where A is the set of scientific models. This implies the following context. Every morphi...
- **Page 546** (`7.3 Monads`): X → Y between sets X and Y, as objects in Kls(ℙ), becomes a binary relation on X and Y rather than a function (see Exercise 7.3.3.5). So in that context, the arrow in (7.14) becomes valid. An olog in which arrows correspond to mere binary relations rather than functions might be called a relational olog....
- **Page 547** (`7.3 Monads`): ...
- **Page 548** (`7.3 Monads`) · **Items:** Example 7.3.4.1: 7.3.4 Monads in databases This section discusses how to record data in the presence of a monad. The idea is quite simple. Given a schema (category) C, an ordinary instance is a functor I:C→Set. But if T=(T,η,µ) is a monad, then a Kleisli T-instance on C is a functor J:C→Kls(T). Such a functor associates to every object...
- **Page 549** (`7.3 Monads`): A Kleisli T-instance on C represents graphs in which edges can fail to have a source vertex, fail to have a target vertex, or both: The context of these tables is that of partial functions, so we do not need a reference for ☺ in the vertex table. Mathematically, the morphism J(src) : J(Arrow) → J(Vertex) in Kls(T) need...
- **Page 550** (`7.3 Monads`) · **Items:** Example 7.3.4.3, Application 7.3.4.4: ′) = 0 for x′ ≠ x. Its multiplication µ : Dist(Dist(X)) → Dist(X) is given by weighted sum: given a finitary probability distribution w : Dist(X) → [0, 1] and x ∈ X, put µ(w)(x) = Σp∈Supp(w) w(p)p(x). Example 7.3.4.3 (Markov chains). Let Loop be the loop schema as in Example 4.5.2.10. A Dist-instance on Loop is equival...
- **Page 551** (`7.3 Monads`): associate the weighted sum of energy absorption rates over the set of wavelengths emitted by the star....
- **Page 552** (`7.3 Monads`): ...
- **Page 553** (`7.3 Monads`) · **Items:** Definition 7.3.5.1, Example 7.3.5.2: 7.3.5 Monads and adjunctions There is a strong connection between monads and adjunctions: every adjunction creates a monad, and every monad comes from an adjunction. For example, the List monad (Example 7.3.2.2) comes from the free forgetful adjunction between sets and monoids Set⇄UFMon (see Proposition 7.1.1.2). That ...
- **Page 554** (`7.3 Monads`) · **Items:** Definition 7.3.2, Example 7.3.5.3: precisely the unit of the monad: for any set X ∈ Ob(Set) the component ηX : X → List(X) is the function that takes x ∈ X to the singleton list [x] ∈ List(X). The monad also has a multiplication map µX : T(T(X)) → T(X), which amounts to concatenating a list of lists. This function comes about using the counit ϵ, as foll...
- **Page 555** (`7.3 Monads`): very useful (Moggi [33]). In much the same way, monads on Set might be useful in databases (see Section 7.3.4). Another, totally different way to use monads in databases is by using a mapping between schemas to produce in each one an internal model of the other. That is, for any functor F:C→D, i.e., mapping of database...
- **Page 556** (`7.3 Monads`): ...
