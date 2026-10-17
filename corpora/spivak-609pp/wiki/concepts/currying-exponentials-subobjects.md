---
id: currying-exponentials-subobjects
title: "Currying, Exponentials, Subobject Classifier & Relative Sets"
type: SheafStalk
chapter: 3
section: "3.4"
pdf_pages: "128–159"
symbol: "Hom(A×B, C) ≅ Hom(A, C^B)"
layer: "Limits & Colimits in Set"
extracted_declarations: 57
restricts_to: [products-and-projections, pullbacks-and-fiber-products]
glues_with: [adjoint-functors-hom-iso, presheaves-representables-yoneda]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Currying, Exponentials, Subobject Classifier & Relative Sets (`Hom(A×B, C) ≅ Hom(A, C^B)`)

> **Sheaf Stalk Location:** Chapter 3 (Fundamental Considerations in Set: Limits, Colimits & Universal Constructions) · Section `3.4` · **PDF Pages 128–159**

## 1. Epistemic Worldview & Intuition

Internalizing functions and subsets inside Set: currying converts a two-variable function A × B -> C into a single-variable function A -> C^B; the subobject classifier Omega = {true, false} bijectively classifies subsets A <= X via characteristic functions chi_A : X -> {true, false} as pullbacks of true : {1} -> Omega.

## 2. Formal Categorical Core

Currying isomorphism (Prop 3.4.2.3, p. 132): Hom_Set(A × B, C) ~= Hom_Set(A, Hom_Set(B, C)), prototypical of adjoint functors (- × B) -| (-)^B. Characteristic function (Def 3.4.4.12, p. 143): Every subset U <= X is the pullback of {true} -> {true, false} along chi_U : X -> {true, false}.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[AB]`** — *a pair (a, b) in A × B*
- **`[C]`** — *an output value c in C*
- **`[A]`** — *a context parameter a in A*
- **`[CB]`** — *a specialized function f_a : B -> C in C^B*
- **`[Sub]`** — *a subset U ⊆ X*
- **`[Chi]`** — *a characteristic predicate χ_U : X -> {true, false}*

### Functional Aspects (Morphisms)
- **`[AB]` $\xrightarrow{\text{evaluates via uncurried f to}}$ `[C]`**
- **`[A]` $\xrightarrow{\text{curries via φ(f) to}}$ `[CB]`**
- **`[Sub]` $\xrightarrow{\text{is classified by pullback of true along}}$ `[Chi]`**

### Commutative Path Facts ($p \simeq q$)
- Currying (Prop 3.4.2.3, p. 132) is the Set-shadow of Cartesian closed adjunction.
- Simplicial complexes (Sec 3.4.4.3, p. 144) and relative sets pi : E -> B (Def 3.4.6.6, p. 156) lay the foundation for fiber bundles and sheaves.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-11` (adjunction_with_product)** $\to$ [[products-and-projections]] (*Products & Universal Pairing in Set*, p. 68–79): Currying is right adjoint to Cartesian product (- × B) ⊣ (-)^B — `Hom(A×B, C) ≅ Hom(A, C^B)`
- **`rho-12` (classifies_subsets_via_pullback)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Every subset U ⊆ X is the pullback of true : 1 -> Ω along χ_U — `U ≅ X ×_Ω {true}`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-35` (generalizes_currying)** $\leftarrow$ [[adjoint-functors-hom-iso]] (*Adjoint Functors (L ⊣ R) & Universal Dictionary Bridges*, p. 461–480): Hom_D(L(c), d) ≅ Hom_C(c, R(d)) generalizes the Set currying bijection — `L ⊣ R`
- **`rho-41` (topos_subobject_classifier)** $\leftarrow$ [[presheaves-representables-yoneda]] (*Functor Categories, Presheaves, Representables & Yoneda's Lemma*, p. 493–517): The functor category C-Set has exponential objects and sieve subobject classifier Ω — `Sub_{C-Set}(I) ≅ Hom(I, Ω)`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 128–159)

### `Definition 3.4.1.1` — [PDF Page 130]
> Definition 3.4.1.1. Suppose given a function f : X → Y and a function g : Y → X such that g ○ f = idX. In this case we call f a retract section and we call g a retract projection.

### `Definition 3.4.4.1` — [PDF Page 140]
> Definition 3.4.4.1. For any set B, define the power-set of B, denoted ℙ(B), to be the set of subsets of B.

### `Definition 3.4.4.4` — [PDF Page 140]
> Definition 3.4.4.4. Let V be a set, let ℙ(V) be its power-set. Since each element x ∈ ℙ(V) is a subset x ⊆ U, we can make sense of the expression x ⊆ x′ for x, x′ ∈ ℙ(V). A subset X ⊆ ℙ(V) is called downward-closed if for every u ∈ X and every u′ ⊆ u, we have u′ ∈ X. We say that X contains all atoms if for every v ∈ V, the singleton set {v} is an element of X. A simplicial complex is a pair (V, X), where V is a set and X ⊆ ℙ(V) is a downward-closed subset that contains all atoms. The elements of X are called simplices (singular: simplex). Any subset u ⊆ V has a cardinality |u|, so we have a function X → ℕ sending each simplex to its cardinali

### `Definition 3.4.4.9` — [PDF Page 143]
> Definition 3.4.4.9. We define the subobject classifier for Set, denoted Ω, to be the set Ω ≔ {True, False}, together with the function {☺} → Ω sending the unique element to True.

### `Definition 3.4.4.12` (Characteristic function) — [PDF Page 143]
> Definition 3.4.4.12 (Characteristic function). Given a subset A ⊆ X, we define its characteristic function of A in X to be the function ψ(A): X → Ω, from (3.25). Let X be any set, and let ℙ(X) be its power-set. By Proposition 3.4.4.10 there is a bijection between ℙ(X) and ΩX. Since Ω has cardinality 2, the cardinality of ℙ(X) is 2|X|, which explains the correct answer to Exercise 3.4.4.2.

### `Definition 3.4.5.1` — [PDF Page 146]
> Definition 3.4.5.1. Let f : X → Y be a function. We say that f is injective if for all x, x′ ∈ X with f(x) = f(x′), we have x = x′. We say that f is surjective if for all y ∈ Y, there exists some x ∈ X such that f(x) = y. We say that f is bijective if it is both injective and surjective. We sometimes denote an injective function X ↪ Y, a surjective function X ↠ Y, and a bijective function X →≅ Y (see Proposition 3.4.5.4).

### `Definition 3.4.5.7` (Monomorphisms, epimorphisms) — [PDF Page 148]
> Definition 3.4.5.7 (Monomorphisms, epimorphisms). Let f : X → Y be a function. We say that f is a monomorphism if for all sets A and pairs of functions g, g′ : A → X, if f ○ g = f ○ g′, then g = g′. We say that f is an epimorphism if for all sets B and pairs of functions h, h′ : Y → B, if h ○ f = h′ ○ f, then h = h′.

### `Definition 3.4.6.2` — [PDF Page 154]
> Definition 3.4.6.2. A multiset is a sequence X ≔ (Oc, N, π), where Oc and N are sets and π : Oc → N is a surjective function. We refer to Oc as the set of occurrences in X, to N as the set of names in X, and to π as the naming function for X. Given a name x ∈ N, let π−1(x) ⊆ Oc be the preimage; the number of elements in π−1(x) is called the multiplicity of x. Suppose that X = (Oc, N, π) and X′ = (Oc′, N′, π′) are multisets. A mapping from X to Y, denoted f : X → Y, consists of a pair (f1, f0) such that f1 : Oc → Oc′ and f0 :

### `Definition 3.4.6.6` (Relative set) — [PDF Page 156]
> Definition 3.4.6.6 (Relative set). Let N be a set. A relative set over N, or simply a set over N, is a pair (E, π) such that E is a set and π : E → N is a function. A mapping of relative sets over N, denoted f : (E, π) → (E′, π′), is a function f : E → E′ such that the following triangle commutes, i.e., π = π′ ○ f:

### `Definition 3.4.6.11` — [PDF Page 157]
> Definition 3.4.6.11. Let A be a set. An A-indexed set is a collection of sets Sa, one for each element a ∈ A; for now we denote this (Sa)a∈A. Each element a ∈ A is called an index. If (Sa')a∈A is another A-indexed set, an A-indexed function from (Sa)a∈A to (Sa')a∈A, denoted (fa)a∈A:(Sa)a∈A→(Sa′)a∈A, is a collection of functions fa : Sa → Sa', one for each element a ∈ A.

### `Proposition 3.4.2.3` (Currying) — [PDF Page 132]
> Proposition 3.4.2.3 (Currying). Let A denote a set. For any sets X, Y there is a bijection ϕ:HomSet(X×A,Y)→≅HomSet(X,YA).(3.22) Proof. Suppose given f : X × A → Y. Define ϕ(f): X → Y A as follows: for any x ∈ X, let ϕ(f)(x): A → Y be defined as follows: for any a ∈ A, let ϕ(f)(x)(a) ≔ f(x, a). We now construct the inverse, ψ : HomSet(X, YA) → HomSet(X × A, Y). Suppose given g : X → Y A. Define ψ(g): X × A → Y as follows: for any pair (x, a) ∈ X × A let ψ(g)(x, a) ≔ g(x)(a).

### `Proposition 3.4.3` — [PDF Page 136]
> Proposition 3.4.3.1 summarizes some properties of products, coproducts, and exponentials, and shows them all in a familiar light, namely, that of elementary school arithmetic. In fact, one can think of the natural numbers as literally being the isomorphism classes of finite sets—that is what they are used for in counting. Consider the standard procedure for counting the elements of a set S, say, cows in a field. One points to an element in S and simultaneously says “one”, points to another element in S and simultaneously says “two”, and so on until finished. By pointing at a cow as you speak a number, you are drawing an imaginary line between

### `Proposition 3.4.3.1` — [PDF Page 136]
> Proposition 3.4.3.1. The following isomorphisms exist for any sets A, B, and C (except for one caveat; see Exercise 3.4.3.2). A + 0 ≅ A A + B ≅ B + A (A + B) + C ≅ A + (B + C) A × 0 ≅ 0 A × 1 ≅ A A × B ≅ B × A (A × B) × C ≅ A × (B × C) A × (B + C) ≅ (A × B) + (A × C) A0 ≅ 1

### `Proposition 3.4.3` — [PDF Page 137]
> Proposition 3.4.3.1 is in some sense about isomorphisms. It says that understanding isomorphisms of finite sets reduces to understanding natural numbers. But note that there is much more going on in Set than isomorphisms; in particular, there are functions that are not invertible. In grade school you probably never saw anything that looked like this: 53×3→5 And yet in Exercise 3.4.2.5 we found a function ev : BA × A → B that exists for

### `Proposition 3.4.4.10` — [PDF Page 143]
> Proposition 3.4.4.10. Let X be a set. There is an isomorphism ϕ:HomSet(X,Ω)→≅ℙ(X). Proof. Given a function f : X → Ω, let ϕ(f) = {x ∈ X | f(x) = True} ⊆ X. We now construct a function ψ : ℙ(X) → HomSet(X, Ω) to serve as the inverse of ϕ. Given a subset A ⊆ X, we define ψ(A):X→Ω by ψ(i)(x)={ Trueif x∈A,Falseif x∉A.(3.25) One checks easily that ϕ and ψ are mutually inverse.

### `Proposition 3.4.5.8` — [PDF Page 146]
> Proposition 3.4.5.8.

### `Proposition 3.4.5.4` — [PDF Page 147]
> Proposition 3.4.5.4. A function f : X → Y is bijective if and only if it is an isomorphism. Proof. Suppose that f is bijective; we define an inverse g : Y → X. For each y ∈ Y, the preimage f−1(y) ⊆ X is a set with exactly one element. Indeed, it has at least one element because f is surjective, and it has at most one element because f is injective. Define g(y) to be the unique element of f−1(y). It is easy to see that f and g are mutually inverse. Note that for every set X, the identity function idX : X → X is bijective. Suppose now that f is an isomorphism, and let g be its inverse. The composition g ○ f = idX is injective, and the compositi

### `Proposition 3.4.5.5` — [PDF Page 147]
> Proposition 3.4.5.5. Let m, n ∈ ℕ be natural numbers. Then m n if and only if there exists an injection m ↪ n. Sketch of proof. If m n, then there is an inclusion {1, 2, …, m} → {1, 2, …, n}. Suppose now that we are given an injection f : m → n; we assume that m > n and derive a contradiction. If m > n, then n + 1 m, and we have already shown that there exists an injection g : n + 1 ↪ m. Composing, we have an injection h ≔ g ○ f : n + 1 ↪ n by Exercise 3.4.5.3. One can show by induction on n that this is impossible.

## 6. Page-by-Page Deep Index (PDF Pages 128–159)
- **Page 128** (`3.4 Other notions in Set`): 3.4 Other notions in Set This section discusses some additional notions in the category Set....
- **Page 129** (`3.4 Other notions in Set`): ...
- **Page 130** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.1.1, Exercise 3.4.1.2: 3.4.1 Retractions Definition 3.4.1.1. Suppose given a function f : X → Y and a function g : Y → X such that g ○ f = idX. In this case we call f a retract section and we call g a retract projection. Exercise 3.4.1.2. Create an olog that includes sets X and Y and functions f : X → Y and g : Y → X such that g ○ f = idX, b...
- **Page 131** (`3.4 Other notions in Set`): ...
- **Page 132** (`3.4 Other notions in Set`) · **Items:** Notation 3.4.2.1, Exercise 3.4.2.2, Proposition 3.4.2.3: 3.4.2 Currying Currying is the idea that when a function takes many inputs, we can input them one at a time or all at once. For example, consider the function that takes a material M and an extension E and returns the force transmitted through material M when it is pulled to extension E. This is a function e: ⌜a materi...
- **Page 133** (`3.4 Other notions in Set`) · **Items:** Exercise 3.4.2.4, Exercise 3.4.2.5, Solution 3.4.2.5: Then for any f ∈ HomSet(X × A, Y), we have ψ ○ ϕ(f)(x, a) = ϕ(f)(x)(a) = f(x, a), and for any g ∈ HomSet(X, YA), we have ϕ ○ ψ(g)(x)(a) = ψ(g)(x, a) = g(x)(a). Thus we see that ϕ is an isomorphism as desired. Exercise 3.4.2.4. Let X = {1, 2}, A = {a, b}, and Y = {x, y}. a. Write three distinct elements of L ≔ HomSet(X ...
- **Page 134** (`3.4 Other notions in Set`) · **Items:** Exercise 3.4.2.6, Example 3.1.1: If n ∈ ℕ is a natural number, recall from (2.4) that there is a set n = {1, 2, …, n}. If A is a set, we often make the abbreviation An≔An¯.(3.24) Exercise 3.4.2.6. Example 3.1.1.7 said that ℝ2 is an abbreviation for ℝ × ℝ, but (3.24) says that ℝ2 is an abbreviation for ℝ2 = HomSet(2, ℝ). Use Exercise 2.1.2.20, Exercise...
- **Page 135** (`3.4 Other notions in Set`): ...
- **Page 136** (`3.4 Other notions in Set`) · **Items:** Proposition 3.4.3, Proposition 3.4.3.1: 3.4.3 Arithmetic of sets Proposition 3.4.3.1 summarizes some properties of products, coproducts, and exponentials, and shows them all in a familiar light, namely, that of elementary school arithmetic. In fact, one can think of the natural numbers as literally being the isomorphism classes of finite sets—that is what th...
- **Page 137** (`3.4 Other notions in Set`) · **Items:** Exercise 3.4.3.2, Solution 3.4.3.2, Exercise 3.4.3.3, Proposition 3.4.3: A1 ≅ A 0A ≅ 0 1A ≅ 1 AB + C ≅ AB × AC (AB)C ≅ AB×C (A × B)C ≅ AC × BC Exercise 3.4.3.2. Everything in Proposition 3.4.3.1 is true except in one case, namely, that of 0¯0¯. In this case we get conflicting answers, because for any set A, including A = ∅ = 0, we have claimed both that A0 ≅ 1 and that 0A ≅ 0. What is the c...
- **Page 138** (`3.4 Other notions in Set`) · **Items:** Exercise 2.1.2.19, Exercise 3.4.3.4, Slogan 3.4.3.5: any sets A, B. This function ev is not an isomorphism, so it somehow does not show up as an equation of natural numbers. But it still has important meaning.6 In terms of mere number, it looks like we are being told of an important function 575 → 5, which is bizarre. The issue here is precisely the one confronted in Exe...
- **Page 139** (`3.4 Other notions in Set`): ...
- **Page 140** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.4.1, Exercise 3.4.4.2, Solution 3.4.4.2, Definition 3.4.4.4: 3.4.4 Subobjects and characteristic functions Definition 3.4.4.1. For any set B, define the power-set of B, denoted ℙ(B), to be the set of subsets of B. Exercise 3.4.4.2. a. How many elements does ℙ(∅) have? b. How many elements does ℙ({☺}) have? c. How many elements does ℙ({1, 2, 3, 4, 5, 6}) have? d. Why it be named ...
- **Page 141** (`3.4 Other notions in Set`) · **Items:** Example 3.4.4.5, Exercise 3.4.4.6: Example 3.4.4.5. Let n ∈ ℕ be a natural number, and let V = n + 1. Define the n- simplex, denoted Δn, to be the simplicial complex ℙ(V) ⊆ ℙ(V), i.e., the whole power-set, which indeed is downward-closed and contains all atoms. We can draw a simplicial complex X by first putting all the vertices on the page as dots. The...
- **Page 142** (`3.4 Other notions in Set`) · **Items:** Exercise 3.4.4.7: In this case X1 consists of elements like {A, B} and {D, K}, but not {D, J}. Write X2, X3, and X4. Hint: The drawing of X is supposed to indicate that X3 should have one element. Exercise 3.4.4.7. The 2-simplex Δ2 is drawn as a filled-in triangle with vertices V = {1, 2, 3}. There is a simplicial complex, often denoted...
- **Page 143** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.4.9, Proposition 3.4.4.10, Slogan 3.4.4.11, Definition 3.4.4.12, Exercise 3.4.4.13: b. Write X = ∂Δ2 as a simplicial complex. In other words, what are the elements of the sets X0, X1, X2, X3, …? 3.4.4.8 Subobject classifier Given a subset A ⊆ X, we can decide for every element of X whether it is in A or not. This is a true/false question for X. Definition 3.4.4.9. We define the subobject classifier fo...
- **Page 144** (`3.4 Other notions in Set`): Let f : X → Ω denote the characteristic function of some subset A ⊆ X, and define A′ = X − A to be its complement, i.e., A′ = {x ∈ X | x ∉ A}. a. What is the characteristic function of A′ ⊆ X? b. Can you phrase it in terms of f and some function Ω → Ω?...
- **Page 145** (`3.4 Other notions in Set`): ...
- **Page 146** (`3.4 Other notions in Set`) · **Items:** Proposition 3.4.5.8, Definition 3.4.5.1, Exercise 3.4.5.2, Exercise 3.4.5.3, Solution 3.4.5.3: 3.4.5 Surjections, injections The classical definition of injections and surjections, given in Definition 3.4.5.1 involves elements. But a more robust notion involves functions; it is given in Proposition 3.4.5.8. Definition 3.4.5.1. Let f : X → Y be a function. We say that f is injective if for all x, x′ ∈ X with f(x)...
- **Page 147** (`3.4 Other notions in Set`) · **Items:** Proposition 3.4.5.4, Proposition 3.4.5.5, Corollary 3.4.5.6, Proposition 3.4.5: b. Let z ∈ Z be an element. The surjectivity of g implies that there is some y ∈ Y with g(y) = z; the surjectivity of f implies that there is some x ∈ X with f(x) = y. c. Let x, x′ ∈ X and suppose that f(x) = f(x′). Because g is a function, g ○ f(x) = g ○ f(x′), and now the injectivity of g ○ f implies that x = x′. d. ...
- **Page 148** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.5.7, Proposition 3.4.5.8: Definition 3.4.5.7 (Monomorphisms, epimorphisms). Let f : X → Y be a function. We say that f is a monomorphism if for all sets A and pairs of functions g, g′ : A → X, if f ○ g = f ○ g′, then g = g′. We say that f is an epimorphism if for all sets B and pairs of functions h, h′ : Y → B, if h ○ f = h′ ○ f, then h = h′. P...
- **Page 149** (`3.4 Other notions in Set`) · **Items:** Proposition 3.4.5.9: ∈ X with h(f(x)) ≠ h′(f(x)), which implies that f(x) = y0. This proves that f is surjective. Finally, suppose that f is surjective, and let h, h′ : Y → B be functions with h ○ f = h′ ○ f. For any y ∈ Y, there exists some x ∈ X with f(x) = y, so h(y) = h(f(x)) = h′(f(x)) = h′(y). This proves that f is an epimorphism. Pr...
- **Page 150** (`3.4 Other notions in Set`) · **Items:** Example 3.4.5.10: We have that g∘q=g∘f′∘m=f∘g′∘m=f∘p=f∘g′∘n=g∘f′∘n=g∘r But we assumed that g is a monomorphism, so this implies that q = r. By the universal property for pullbacks, Proposition 3.2.1.15, we have m = n = 〈q, p〉Y : B → X ×Y A. Example 3.4.5.10. Suppose an olog has a fiber product square such that g is intended to be a mono...
- **Page 151** (`3.4 Other notions in Set`) · **Items:** Corollary 3.4.5.11, Exercise 3.4.5.12, Exercise 3.4.5.13: Corollary 3.4.5.11. Let i: A → X be a monomorphism, and let True: {☺} → Ω be the subobject classifier (see Definition 3.4.4.9). Then there is a fiber product square of the form Proof. Let X′ ⊆ X denote the image of i, and let f : X → Ω denote the characteristic function of X′ ⊆ X, given by Proposition 3.4.4.10. Then it...
- **Page 152** (`3.4 Other notions in Set`): epimorphisms....
- **Page 153** (`3.4 Other notions in Set`): ...
- **Page 154** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.6.2: 3.4.6 Multisets, relative sets, and set-indexed sets In this section we prepare to consider categories other than Set by looking at some categories related to Set. 3.4.6.1 Multisets Consider the set X of words in a given document. If WC(X) is the word count of the document, we do not generally have WC(X) = |X|. The rea...
- **Page 155** (`3.4 Other notions in Set`) · **Items:** Exercise 3.4.6.3, Exercise 3.4.6.4: N → N′ are functions and such that the following diagram commutes: Exercise 3.4.6.3. Suppose that a pseudo-multiset is defined to be almost the same as a multiset, except that π is not required to be surjective. a. Write a pseudo-multiset that is not a multiset. b. Describe the difference between the two notions (multi...
- **Page 156** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.6.6, Exercise 3.4.6.7, Exercise 3.4.6.8, Example 3.4.6.10: Definition 3.4.6.6 (Relative set). Let N be a set. A relative set over N, or simply a set over N, is a pair (E, π) such that E is a set and π : E → N is a function. A mapping of relative sets over N, denoted f : (E, π) → (E′, π′), is a function f : E → E′ such that the following triangle commutes, i.e., π = π′ ○ f: Exe...
- **Page 157** (`3.4 Other notions in Set`) · **Items:** Definition 3.4.6.11, Exercise 3.4.6.12, Exercise 3.4.6.13: each classroom c ∈ C, be a function Pc → Sc.10 Definition 3.4.6.11. Let A be a set. An A-indexed set is a collection of sets Sa, one for each element a ∈ A; for now we denote this (Sa)a∈A. Each element a ∈ A is called an index. If (Sa')a∈A is another A-indexed set, an A-indexed function from (Sa)a∈A to (Sa')a∈A, denote...
- **Page 158** (`3.4 Other notions in Set`): 4The meaning of iff is “if and only if.” In this case we are saying that the pair (x, y) is in R if and only if there exists an arrow connecting x and y. 5Note that the term inclusion is not too good because it seems to suggest that i1 and i2 are injective (see Definition 3.4.5.1) and this is not always the case. The r...
- **Page 159** (`3.4 Other notions in Set`): ...
