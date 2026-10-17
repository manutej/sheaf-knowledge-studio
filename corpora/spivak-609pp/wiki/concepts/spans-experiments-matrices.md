---
id: spans-experiments-matrices
title: "Spans, Scientific Experiments, Equalizers & Finite Limits"
type: SheafStalk
chapter: 3
section: "3.2.2–3.2.3"
pdf_pages: "102–109"
symbol: "X ← R → Y"
layer: "Limits & Colimits in Set"
extracted_declarations: 14
restricts_to: [pullbacks-and-fiber-products]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Spans, Scientific Experiments, Equalizers & Finite Limits (`X ← R → Y`)

> **Sheaf Stalk Location:** Chapter 3 (Fundamental Considerations in Set: Limits, Colimits & Universal Constructions) · Section `3.2.2–3.2.3` · **PDF Pages 102–109**

## 1. Epistemic Worldview & Intuition

A span X <--f-- R --g--> Y models many-to-many relationships, scientific experiments (recording both input state X and observed outcome Y for each trial R), and matrices of path counts. Composing spans via pullbacks yields matrix multiplication.

## 2. Formal Categorical Core

Given spans X <-- R --> Y and Y <-- S --> Z, their composite span is X <-- R ×_Y S --> Z (Def 3.2.2.3, p. 104). Equalizer Eq(f, g) = {x in X | f(x) = g(x)} (Def 3.2.3.1, p. 107). Every finite limit in Set is built from products and equalizers (or terminal objects and pullbacks).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[R]`** — *an experimental run r in R*
- **`[X]`** — *a controlled input parameter x in X*
- **`[Y]`** — *a measured response y in Y*
- **`[S]`** — *a downstream analysis event s in S*
- **`[RS]`** — *a chained trial pair (r, s) in R ×_Y S*

### Functional Aspects (Morphisms)
- **`[R]` $\xrightarrow{\text{had input parameter}}$ `[X]`**
- **`[R]` $\xrightarrow{\text{yielded measurement}}$ `[Y]`**
- **`[RS]` $\xrightarrow{\text{first stage run}}$ `[R]`**
- **`[RS]` $\xrightarrow{\text{second stage analysis}}$ `[S]`**

### Commutative Path Facts ($p \simeq q$)
- Span composition via pullback corresponds to relational join and matrix multiplication (Application 3.2.2.5, p. 105).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-09` (composes_via_pullback)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Spans X <- R -> Y <- S -> Z compose by taking the pullback R ×_Y S — `R ∘_Span S = R ×_Y S`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 102–109)

### `Definition 3.2.2.1` — [PDF Page 102]
> Definition 3.2.2.1. Given sets A and B, a span on A and B is a set R together with functions f : R → A and g : R → B.

### `Definition 3.2.2.3` — [PDF Page 102]
> Definition 3.2.2.3. Let A, B, and C be sets, and let A←fR→gB and B←f′R′→g ′C be spans. Their composite span is given by the fiber product R ×B R′ as in this diagram:

### `Definition 3.2.3.1` — [PDF Page 107]
> Definition 3.2.3.1. Suppose given two parallel arrows X⇉gfY.(3.14) The equalizer of f and g is the set Eq(f,g)≔{ x∈X|f(x)=g(x)} which is a subset of X. Writing p: Eq(f, g) → X for the inclusion, we have a commutative diagram Eq(f,g)→pX⇉gfY with f ○ p = g ○ p.

### `Application 3.2.2.2` — [PDF Page 102]
> Application 3.2.2.2. Think of A and B as observables and R as a set of experiments performed on these two variables. For example, let’s rename variables and say that T is the set of possible temperatures of a gas in a fixed container and that P is the set of possible pressures of the gas, so we have the span T←fE→gP. We perform 1,000 experiments in which we change and record the temperature, and we simultaneously record the pressure. The results might look like this: Experiment E ID Temperature Pressure 1 100 72 2 100 73 3 100 72 4 200 140 5 200 138 6 200 141 ⋮ ⋮ ⋮

### `Application 3.2.2.4` — [PDF Page 103]
> Application 3.2.2.4. Let’s look back at the lab’s experiment in Application 3.2.2.2, which resulted in a span T←fE→gP. Suppose we notice that something looks a little wrong. The pressure should be linear with the temperature but it does not appear to be. We hypothesize that the volume of the container is increasing under pressure. We look up this container online and see that experiments have been done to measure the volume as the interior pressure changes. That data gives us a span P←f′E′→g′V. The composite of our lab’s span with the online data span yields a span T ← E″ → V, where E″ ≔ E ×P E′. What information does this span give us? In ex

### `Construction 3.2.2.6` — [PDF Page 105]
> Construction 3.2.2.6. Given a span A←fR→gB, one can draw a bipartite graph with each element of A drawn as a dot on the left, each element of B drawn as a dot on the right, and each element r ∈ R drawn as an arrow connecting vertex f(r) on the left to vertex g(r) on the right.

### `Example 3.2.3.2` — [PDF Page 107]
> Example 3.2.3.2. Suppose one has designed an experiment to test a theoretical prediction. The question is, When does the theory match the experiment? The answer is given by the equalizer of the following diagram: The equalizer is the set of all inputs for which the theory and the experiment yield the same output.

### `Exercise 3.2.2.5` — [PDF Page 104]
> Exercise 3.2.2.5. Let A = {1, 2} and B = {1, 2, 3}, and consider the span A←fR→gB given by the table R ID f : A g : B 1 1 2 2 1 2 3 1 3 4 2 1 5 2 2 6 2 3 7 2 3 8 2 3 So R = 8. a. What is the matrix corresponding to this span? b. If R′ ⊆ A×B is a subset, with corresponding span A←f′R′→g′B given by projections, what can you say about the numbers in the corresponding matrix?

### `Exercise 3.2.2.7` — [PDF Page 105]
> Exercise 3.2.2.7. a. Draw the bipartite graph (as in Construction 3.2.2.6) corresponding to the span T←fE→gP in Application 3.2.2.2 (assuming the ellipses are vacuous, i.e., assuming that |E| = 6). b. Now make up your own span P←f′E′→g′V (with |E′| 2), and write it out in database form as in Application 3.2.2.2 and in bipartite graph form. c. Draw the composite span T ← E ×P E′ → V as a bipartite graph. d. Describe in words how the composite span graph (for T ← E ×P E′ → V ) relates to the graphs of its factors (T ← E → P and P ← E′ → V ).

### `Exercise 3.2.3.3` — [PDF Page 107]
> Exercise 3.2.3.3. Create an olog that uses equalizers in a reasonably interesting way. Alternatively, use an equalizer to specify those published authors who have published exactly one paper. Hint: Find a function from authors to papers; then find another.

### `Exercise 3.2.3.4` — [PDF Page 107]
> Exercise 3.2.3.4. Find a universal property enjoyed by the equalizer of two arrows f : X → Y and g : X → Y, and present it in the style of Propositions 3.1.1.10, 3.1.2.7, and

### `Exercise 3.2.3.5` — [PDF Page 108]
> Exercise 3.2.3.5. a. A terminal set is a set S such that for every set X, there exists a unique function X → S. Find a terminal set. b. Do you think that the notion terminal set belongs here in Section 3.2, i.e., in the same world as products, pullbacks, and equalizers? Why? Another way to ask this is, If products, pullbacks, and equalizers are all limits, then what do limits have in common?

### `Exercise 2.1.2` — [PDF Page 108]
> Exercise 2.1.2.13, part (a). b. The notion of a terminal set does fit well into Section 3.2 because it has a similar kind of universal property. Namely, for any other set S′ that might fill the position of S, there is a unique map S′ → S. See Section 6.1.3.

### `Solution 3.2.3.5` — [PDF Page 108]
> Solution 3.2.3.5. a. Let S = {☺}. Then S is a terminal set. So is S = {43}. This was the content of

## 6. Page-by-Page Deep Index (PDF Pages 102–109)
- **Page 102** (`3.2 Finite limits in Set`) · **Items:** Definition 3.2.2.1, Application 3.2.2.2, Definition 3.2.2.3: 3.2.2 Spans, experiments, and matrices Definition 3.2.2.1. Given sets A and B, a span on A and B is a set R together with functions f : R → A and g : R → B. Application 3.2.2.2. Think of A and B as observables and R as a set of experiments performed on these two variables. For example, let’s rename variables and say th...
- **Page 103** (`3.2 Finite limits in Set`) · **Items:** Application 3.2.2.4: Application 3.2.2.4. Let’s look back at the lab’s experiment in Application 3.2.2.2, which resulted in a span T←fE→gP. Suppose we notice that something looks a little wrong. The pressure should be linear with the temperature but it does not appear to be. We hypothesize that the volume of the container is increasing und...
- **Page 104** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.2.5: is the cardinality of its preimage, |p−1(a, b)|, i.e., the number of elements in R that are sent by p to (a, b). Suppose we are given two (A, B) spans, i.e., A ← R → B and A ← R′ → B; we might think of these has having the same dimensions, i.e., they are both |A| × |B| matrices. We can take the disjoint union R ⊔ R′, a...
- **Page 105** (`3.2 Finite limits in Set`) · **Items:** Construction 3.2.2.6, Exercise 3.2.2.7: Construction 3.2.2.6. Given a span A←fR→gB, one can draw a bipartite graph with each element of A drawn as a dot on the left, each element of B drawn as a dot on the right, and each element r ∈ R drawn as an arrow connecting vertex f(r) on the left to vertex g(r) on the right. Exercise 3.2.2.7. a. Draw the bipartite gr...
- **Page 106** (`3.2 Finite limits in Set`): ...
- **Page 107** (`3.2 Finite limits in Set`) · **Items:** Definition 3.2.3.1, Example 3.2.3.2, Exercise 3.2.3.3, Exercise 3.2.3.4: 3.2.3 Equalizers and terminal objects Definition 3.2.3.1. Suppose given two parallel arrows X⇉gfY.(3.14) The equalizer of f and g is the set Eq(f,g)≔{ x∈X|f(x)=g(x)} which is a subset of X. Writing p: Eq(f, g) → X for the inclusion, we have a commutative diagram Eq(f,g)→pX⇉gfY with f ○ p = g ○ p. Example 3.2.3.2. Suppo...
- **Page 108** (`3.2 Finite limits in Set`) · **Items:** Exercise 3.2.3.5, Solution 3.2.3.5, Exercise 2.1.2: 3.2.1.15. Exercise 3.2.3.5. a. A terminal set is a set S such that for every set X, there exists a unique function X → S. Find a terminal set. b. Do you think that the notion terminal set belongs here in Section 3.2, i.e., in the same world as products, pullbacks, and equalizers? Why? Another way to ask this is, If pro...
- **Page 109** (`3.2 Finite limits in Set`): ...
