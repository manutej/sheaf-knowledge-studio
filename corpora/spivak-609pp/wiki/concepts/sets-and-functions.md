---
id: sets-and-functions
title: "The Category Set: Sets, Functions & Isomorphisms"
type: SheafStalk
chapter: 2
section: "2.1"
pdf_pages: "26–43"
symbol: "Set"
layer: "Set-Theoretic Grounding"
extracted_declarations: 33
restricts_to: []
glues_with: [ologs-ontology-logs, commutative-diagrams, products-and-projections, coproducts-and-injections, monoids-and-actions]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# The Category Set: Sets, Functions & Isomorphisms (`Set`)

> **Sheaf Stalk Location:** Chapter 2 (The Category of Sets, Commutative Diagrams, and Ologs) · Section `2.1` · **PDF Pages 26–43**

## 1. Epistemic Worldview & Intuition

The foundational category Set whose objects are sets (collections of distinct elements) and whose morphisms are functions f : X -> Y assigning to each x in X a unique f(x) in Y, equipped with associative composition and identity functions.

## 2. Formal Categorical Core

Ob(Set) = sets; Hom_Set(X, Y) = {f : X -> Y}. Composition (g o f)(x) = g(f(x)) satisfies (h o g) o f = h o (g o f) and id_Y o f = f = f o id_X. A function f : X -> Y is an isomorphism (X ~= Y) iff there exists g : Y -> X with g o f = id_X and f o g = id_Y.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[X]`** — *an element x of domain X*
- **`[Y]`** — *an element y of codomain Y*
- **`[Z]`** — *an element z of target Z*

### Functional Aspects (Morphisms)
- **`[X]` $\xrightarrow{\text{maps via f to}}$ `[Y]`**
- **`[Y]` $\xrightarrow{\text{maps via g to}}$ `[Z]`**
- **`[X]` $\xrightarrow{\text{maps via composite g ∘ f to}}$ `[Z]`**

### Commutative Path Facts ($p \simeq q$)
- Path equivalence: for every x in X, applying f then g yields (g ∘ f)(x) = g(f(x)).
- Isomorphism (Def 2.1.2.14, p. 38): f : X -> Y has inverse g : Y -> X iff f is both injective and surjective (bijective).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-02` (semantics_in_Set)** $\leftarrow$ [[ologs-ontology-logs]] (*Ologs (Ontology Logs): Functional Worldviews*, p. 47–67): Every olog Type is a set; every Aspect is a function f : X -> Y — `I : Olog -> Set`
- **`rho-04` (evaluates_paths)** $\leftarrow$ [[commutative-diagrams]] (*Commutative Diagrams & Path Equations*, p. 44–46): Diagram commutes in Set iff composite functions agree pointwise — `(g ∘ f)(x) = (k ∘ h)(x)`
- **`rho-05` (constructs_in_Set)** $\leftarrow$ [[products-and-projections]] (*Products & Universal Pairing in Set*, p. 68–79): Ordered pairs (x, y) and projection functions π₁, π₂ — `X × Y = {(x,y)}`
- **`rho-06` (constructs_in_Set)** $\leftarrow$ [[coproducts-and-injections]] (*Coproducts & Disjoint Unions in Set*, p. 80–87): Disjoint unions X ⊔ Y and inclusion injections i₁, i₂ — `Hom(X⊔Y, Z) ≅ Hom(X,Z)×Hom(Y,Z)`
- **`rho-13` (acts_on_Set)** $\leftarrow$ [[monoids-and-actions]] (*Monoids, Agent Actions & Finite State Machines*, p. 160–191): Monoid action M × S -> S represents each m in M as an endofunction S -> S — `M -> End_Set(S)`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 26–43)

### `Definition 2.1.2.14` (Isomorphism) — [PDF Page 38]
> Definition 2.1.2.14 (Isomorphism). Let X and Y be sets. A function f : X → Y is called an isomorphism, denoted f : X→≅Y, if there exists a function g : Y → X such that g ○ f = idX and f ○ g = idY. Figure 2.4 An isomorphism X→≅Y.

### `Definition 2.1.2.23` (Cardinality of finite sets) — [PDF Page 42]
> Definition 2.1.2.23 (Cardinality of finite sets). Let A be a set and n ∈ ℕ a natural number. We say that A has cardinality n, denoted |A|=n, if there exists an isomorphism of sets A ≅ n. If there exists some n ∈ ℕ such that A has cardinality n, then we say that A is finite. Otherwise, we say that A is infinite and write |A| ∞.

### `Proposition 2.1.2.18` — [PDF Page 39]
> Proposition 2.1.2.18. The following facts hold about isomorphism. 1. Any set A is isomorphic to itself; i.e., there exists an isomorphism A→≅A. 2. For any sets A and B, if A is isomorphic to B, then B is isomorphic to A.

### `Proposition 2.1.2.25` — [PDF Page 42]
> Proposition 2.1.2.25. Let A and B be finite sets. If there is an isomorphism of sets f : A → B, then the two sets have the same cardinality, |A| = |B|. Proof. If f : A → B is an isomorphism and B ≅ n, then A ≅ n because the composition of two isomorphisms is an isomorphism.

### `Slogan 2.1.2.1` — [PDF Page 33]
> Slogan 2.1.2.1. Given a function f : X → Y, we think of X as a set of things, and Y as a set of bins. The function tells us in which bin to put each thing.

### `Slogan 2.1.2.7` — [PDF Page 35]
> Slogan 2.1.2.7. Given composable functions X→fY→gZ, we have a way of putting every thing in X into a bin in Y, and we have a way of putting each bin from Y into a larger bin in Z. The composite, g ○ f : X → Z, is the resulting way that every thing in X is put into a bin in Z.

### `Application 2.1.2.2` — [PDF Page 33]
> Application 2.1.2.2. In studying the mechanics of materials, one wishes to know how a material responds to tension. For example, a rubber band responds to tension differently than a spring does. To each material we can associate a force- extension curve, recording how much force the material carries when extended to various lengths. Once we fix a methodology for performing experiments, finding a material’s force-extension curve would ideally constitute a function from the set of materials to the set of curves.

### `Application 2.1.2.16` — [PDF Page 39]
> Application 2.1.2.16. There is an isomorphism between the set NucDNA of nucleotides found in DNA and the set NucRNA of nucleotides found in RNA. Indeed, both sets have four elements, so there are 24 different isomorphisms. But only one is useful in biology. Before we say which one it is, let us say there is also an isomorphism NucDNA ≅ {A, C, G, T} and an isomorphism NucRNA ≅ {A, C, G, U}, and we will use the letters as abbreviations for the nucleotides. The convenient isomorphism NucDNA→≅NucRNA is that given by RNA transcription; it sends A↦U, C↦G, G↦C, T↦A. (See also

### `Application 5.1.2.21` — [PDF Page 39]
> Application 5.1.2.21.) There is also an isomorphism NucDNA→≅NucDNA (the matching in the double helix), given by A↦T, C↦G, G↦C, T↦A. Protein production can be modeled as a function from the set of 3-nucleotide sequences to the set of eukaryotic amino acids. However, it cannot be an isomorphism because there are 43 = 64 triplets of RNA nucleotides but only 21 eukaryotic amino acids.

### `Example 2.1.2.4` — [PDF Page 34]
> Example 2.1.2.4. Suppose that X is a set and X′ ⊆ X is a subset. Then we can consider the function X′ → X given by sending every element of X′ to “itself” as an element of X. For example, if X = {a, b, c, d, e, f} and X′ = {b, d, e}, then X′ ⊆ X. We turn that into the function X′ → X given by b ↦ b, d ↦ d, e ↦ e.2 As a matter of notation, we may sometimes say the following: Let X be a set, and let i : X′ ⊆ X be a subset. Here we are making clear that X′ is a subset of X, but that i is the name of the associated function.

### `Example 2.1.2.15` — [PDF Page 39]
> Example 2.1.2.15. If X and Y are sets and f : X → Y is an isomorphism, then the analogue of Figure 2.2 will look like a perfect matching, more often called a one- to-one correspondence. That means that no two arrows will hit the same element of Y, and every element of Y will be in the image. For example, Figure 2.4 depicts an isomorphism X→≅Y between four element sets.

### `Remark 2.1.2.11` — [PDF Page 36]
> Remark 2.1.2.11. Suppose given sets A, B, C and functions A→fB→gC. The classical order for writing their composition has been used so far, namely, g ○ f : A → C. For any element a ∈ A, we write g ○ f(a) to mean g(f(a)). This means “do g to whatever results from doing f to a.” However, there is another way to write this composition, called diagrammatic order. Instead of g ○ f, we would write f; g : A → C, meaning “do f, then do g.” Given an element a ∈ A, represented by a: {☺} → A, we have an element a; f; g. Let X and Y be sets. We write HomSet(X, Y) to denote the set of functions X → Y.3 Note that two functions f, g : X → Y are equal if and 

### `Notation 2.1.1.1` — [PDF Page 30]
> Notation 2.1.1.1. The symbol ∅ denotes the set with no elements (see Figure 2.1), which can also be written as { }. The symbol ℕ denotes the set of natural numbers: ℕ≔{0, 1, 2, 3, 4, …, 877,…}. (2.1) The symbol ℤ denotes the set of integers, which contains both the natural numbers and their negatives, ℤ≔{…,−551,…,−2,−1,0,1,2,…}. (2.2) If A and B are sets, we say that A is a subset of B, and write A ⊆ B, if every element of A is an element of B. So we have ℕ ⊆ ℤ. Checking the definition, one sees that for any set A, we have (perhaps uninteresting) subsets ∅ ⊆ A and A ⊆ A. We can use set-builder notation to denote subsets. For example, the set 

### `Notation 2.1.2.9` — [PDF Page 36]
> Notation 2.1.2.9. Let X be a set and x ∈ X an element. There is a function {☺} → X that sends ☺ ↦ x. We say that this function represents x ∈ X. We may denote it x: {☺} → X.

### `Notation 2.1.2.21` — [PDF Page 41]
> Notation 2.1.2.21. For any natural number n ∈ ℕ, define a set n¯≔{1,2,3,…,n}. (2.4) We call n the numeral set of size n. So, in particular, 2 = {1, 2}, 1 = {1}, and 0 = ∅. Let A be any set. A function f : n → A can be written as a length n sequence f=(f(1),f(2),…,f(n)). (2.5) We call this the sequence notation for f.

### `Exercise 2.1.1.2` — [PDF Page 31]
> Exercise 2.1.1.2. Let A ≔ {1, 2, 3}. What are all the subsets of A? Hint: There are eight. A set can have other sets as elements. For example, the set X≔{{1,2},{4},{1,3,6}} has three elements, each of which is a set.

### `Exercise 2.1.2.3` — [PDF Page 34]
> Exercise 2.1.2.3. Here is a simplified account of how the brain receives light. The eye contains about 100 million photoreceptor (PR) cells. Each connects to a retinal ganglion (RG) cell. No PR cell connects to two different RG cells, but usually many PR cells can attach to a single RG cell. Let PR denote the set of photoreceptor cells, and let RG denote the set of retinal ganglion cells. a. According to the above account, does the connection pattern constitute a function RG → PR, a function PR → RG, or neither one? b. Would you guess that the connection pattern that exists between other areas of the brain are function-like? Justify your answ

### `Exercise 2.1.2.5` — [PDF Page 34]
> Exercise 2.1.2.5. Let f : ℕ → ℕ be the function that sends every natural number to its square, e.g., f(6) = 36. First fill in the blanks, then answer a question. a. 2 ↦ ________ b. 0 ↦ ________ c. −2 ↦ ________ d. 5 ↦ ________ e. Consider the symbol → and the symbol ↦. What is the difference between how these two symbols are used so far in this book? Given a function f : X → Y, the elements of Y that have at least one arrow pointing to them are said to be in the image of f; that is, we have

## 6. Page-by-Page Deep Index (PDF Pages 26–43)
- **Page 26** (`1.4 Category theory references`): Chapter 2 The Category of Sets The theory of sets was invented as a foundation for all of mathematics. The notion of sets and functions serves as a basis on which to build intuition about categories in general. This chapter gives examples of sets and functions and then discusses commutative diagrams. Ologs are then int...
- **Page 27** (`1.4 Category theory references`): ...
- **Page 28** (`2.1 Sets and functions`): 2.1 Sets and functions People have always found it useful to put things into bins. The study of sets is the study of things in bins....
- **Page 29** (`2.1 Sets and functions`): ...
- **Page 30** (`2.1 Sets and functions`) · **Items:** Notation 2.1.1.1, Figure 2.1: 2.1.1 Sets You probably have an innate understanding of what a set is. We can think of a set X as a collection of elements x ∈ X, each of which is recognizable as being in X and such that for each pair of named elements x, x′ ∈ X we can tell if x = x′ or not.1 The set of pendulums is the collection of things we agree t...
- **Page 31** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.1.2: be written in many ways, such as {n∈ℤ|n>2}or{n∈ℕ|n>2}or{n∈ℕ|n3}. The symbol ∃ means “there exists.” So we could write the set of even integers as {n∈ℤ|n is even}={n∈ℤ|∃m∈ℤ such that 2m=n}. The symbol ∃! means “there exists a unique.” So the statement “∃!x ∈ ℝ such that x2 = 0” means that there is one and only one numbe...
- **Page 32** (`2.1 Sets and functions`): ...
- **Page 33** (`2.1 Sets and functions`) · **Items:** Slogan 2.1.2.1, Application 2.1.2.2, Figure 2.2: 2.1.2 Functions If X and Y are sets, then a function f from X to Y, denoted f : X → Y, is a mapping that sends each element x ∈ X to an element of Y, denoted f(x) ∈ Y. We call X the domain of the function f, and we call Y the codomain of f. Figure 2.2 A function from a set X to a set Y. Note that for every element x ∈ ...
- **Page 34** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.2.3, Example 2.1.2.4, Exercise 2.1.2.5: Exercise 2.1.2.3. Here is a simplified account of how the brain receives light. The eye contains about 100 million photoreceptor (PR) cells. Each connects to a retinal ganglion (RG) cell. No PR cell connects to two different RG cells, but usually many PR cells can attach to a single RG cell. Let PR denote the set of ph...
- **Page 35** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.2.6, Slogan 2.1.2.7, Exercise 2.1.2.8, Figure 2.3: im(f)≔{y∈Y|∃x∈X such that f(x)=y}. (2.3) The image of a function f is always a subset of its codomain, im(f) ⊆ Y. Exercise 2.1.2.6. If f : X → Y is depicted by Figure 2.2, write its image, im(f) as a set. Given a function f : X → Y and a function g : Y → Z, where the codomain of f is the same set as the domain of g (na...
- **Page 36** (`2.1 Sets and functions`) · **Items:** Solution 2.1.2.8, Notation 2.1.2.9, Exercise 2.1.2.10, Remark 2.1.2.11, Exercise 2.1.2.12: function f ○ i: A → Y. The image of this function is denoted f(A)≔im(f○i), see (2.3) for the definition of image. Let X = Y ≔ ℤ, let A ≔ {−1, 0, 1, 2, 3} ⊆ X, and let f : X → Y be given by f(x) = x2. What is the image set f(A)? Solution 2.1.2.8. By definition of image (see (2.3), we have f(A)={y∈ℤ|∃a∈A such that f○i(a)...
- **Page 37** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.2.13, Solution 2.1.2.13: Let A = {1, 2, 3, 4, 5} and B = {x, y}. a. How many elements does HomSet(A, B) have? b. How many elements does HomSet(B, A) have? Exercise 2.1.2.13. a. Find a set A such that for all sets X there is exactly one element in HomSet(X, A). Hint: Draw a picture of proposed A’s and X’s. How many dots should be in A? b. Find ...
- **Page 38** (`2.1 Sets and functions`) · **Items:** Definition 2.1.2.14, Figure 2.4: To give a function B → X one must answer the question, Where do I send b? for each b ∈ B. Because B has no elements, no questions must be answered in order to provide such a function. There is one way to answer all the necessary questions, because doing so is immediate (“vacuously satisfied”). It is like commanding Joh...
- **Page 39** (`2.1 Sets and functions`) · **Items:** Example 2.1.2.15, Application 2.1.2.16, Application 5.1.2.21, Exercise 2.1.2.17, Proposition 2.1.2.18: In this case we also say that f is invertible and that g is the inverse of f. If there exists an isomorphism X→≅Y, we say that X and Y are isomorphic sets and may write X ≅ Y. Example 2.1.2.15. If X and Y are sets and f : X → Y is an isomorphism, then the analogue of Figure 2.2 will look like a perfect matching, more o...
- **Page 40** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.2.19, Solution 2.1.2.19: 3. For any sets A, B, and C, if A is isomorphic to B, and B is isomorphic to C, then A is isomorphic to C. Proof. 1. The identity function idA: A → A is invertible; its inverse is idA because idA ○ idA = idA. 2. If f : A → B is invertible with inverse g : B → A, then g is an isomorphism with inverse f. 3. If f : A → B ...
- **Page 41** (`2.1 Sets and functions`) · **Items:** Exercise 2.1.2.20, Solution 2.1.2.20, Notation 2.1.2.21, Exercise 2.1.2.22, Solution 2.1.2.22: the same, one should have in hand a specified isomorphism g : A→≅B, such as a ↦ r8, 7 ↦ “Bob”, Q ↦ ♣. Now, given f : B → {1, 2, 3, 4, 5}, there is a canonical function A → {1, 2, 3, 4, 5} corresponding to f, namely, f ○ g. Exercise 2.1.2.20. Find a set A such that for any set X, there is an isomorphism of sets X≅HomSet...
- **Page 42** (`2.1 Sets and functions`) · **Items:** Definition 2.1.2.23, Exercise 2.1.2.24, Proposition 2.1.2.25: Definition 2.1.2.23 (Cardinality of finite sets). Let A be a set and n ∈ ℕ a natural number. We say that A has cardinality n, denoted |A|=n, if there exists an isomorphism of sets A ≅ n. If there exists some n ∈ ℕ such that A has cardinality n, then we say that A is finite. Otherwise, we say that A is infinite and writ...
- **Page 43** (`2.1 Sets and functions`): ...
