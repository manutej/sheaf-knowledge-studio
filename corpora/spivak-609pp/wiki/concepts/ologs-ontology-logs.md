---
id: ologs-ontology-logs
title: "Ologs (Ontology Logs): Functional Worldviews"
type: SheafStalk
chapter: 2
section: "2.3"
pdf_pages: "47–67"
symbol: "Olog"
layer: "Epistemic Foundation"
extracted_declarations: 12
restricts_to: [scientific-agreement-worldviews, sets-and-functions, commutative-diagrams]
glues_with: [database-schemas-instances, sheaf-of-ologged-concepts-descent]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Ologs (Ontology Logs): Functional Worldviews (`Olog`)

> **Sheaf Stalk Location:** Chapter 2 (The Category of Sets, Commutative Diagrams, and Ologs) · Section `2.3` · **PDF Pages 47–67**

## 1. Epistemic Worldview & Intuition

Spivak's signature knowledge-representation formalism: an Ontology Log (olog) is a readable, mathematically rigorous category presentation where boxes are noun-phrase Types, arrows are verb-phrase Functional Aspects, and commuting diagrams are Facts.

## 2. Formal Categorical Core

An olog O is a database schema (presentation of a category) with human-readable English labels obeying strict rules: (1) every Type box begins with 'a/an' representing a set of instances; (2) every Aspect arrow x --f--> y reads '[x] [f] [y]' and must be a valid mathematical function (deterministic & total); (3) Facts are declared path equivalences p ~ q.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[P]`** — *a person*
- **`[W]`** — *a woman*
- **`[M]`** — *a man*
- **`[C]`** — *a child*
- **`[BP]`** — *a pair (w, m) of a woman and a man*

### Functional Aspects (Morphisms)
- **`[C]` $\xrightarrow{\text{is}}$ `[P]`**
- **`[P]` $\xrightarrow{\text{has as biological mother}}$ `[W]`**
- **`[P]` $\xrightarrow{\text{has as biological father}}$ `[M]`**
- **`[P]` $\xrightarrow{\text{has as biological parents}}$ `[BP]`**

### Commutative Path Facts ($p \simeq q$)
- Rules 2.3.1.1 (Types, p. 49), Rules 2.3.2.1 (Aspects must be functions, p. 52), Rules 2.3.3.1 (Facts as commuting diagrams / path equations, p. 60).
- Non-functional relationships ('a person eats a food') must be reified into a span / relation table ('an eating event E' with projections to Person and Food).

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-01` (formalizes_worldview)** $\to$ [[scientific-agreement-worldviews]] (*Science as Agreement & Categorical Worldviews*, p. 11–25): Explicit functional boxes-and-arrows replacing informal heuristics — `ρ(Olog) = (Ob(O), Hom(O))`
- **`rho-02` (semantics_in_Set)** $\to$ [[sets-and-functions]] (*The Category Set: Sets, Functions & Isomorphisms*, p. 26–43): Every olog Type is a set; every Aspect is a function f : X -> Y — `I : Olog -> Set`
- **`rho-03` (declares_facts)** $\to$ [[commutative-diagrams]] (*Commutative Diagrams & Path Equations*, p. 44–46): Olog facts are path equations p ≃ q (commuting diagrams) — `Facts(O) ⊆ Path(G) × Path(G)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-21` (identifies_olog_and_schema)** $\leftarrow$ [[database-schemas-instances]] (*Categorical Databases: Schemas (G, ≃) & Table Instances*, p. 245–266): An olog is precisely a database schema with natural-language type/aspect labels — `Olog = Sch`
- **`rho-53` (stalk_evaluation_to_local_olog)** $\leftarrow$ [[sheaf-of-ologged-concepts-descent]] (*Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data*, p. 521–526): Evaluating the sheaf of ologged concepts O : Open(Alx(X^op))^op -> Sch at any vertex v yields a local Set-olog O(v) — `ev_v : O(U) -> O(v) ∈ Olog`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-03` — The Alexandrov Sheaf of Ologs Worldview Triangle** ([[sheaf-of-ologged-concepts-descent]], [[sheaves-and-local-to-global-gluing]], [[ologs-ontology-logs]]): A simplicial complex X of local ologs O(v) glued via schema restriction maps O(v) -> O(u) forms a sheaf of categories over Alx(X^op). *[H^0 Exact (Zero Obstruction)]*
- **`tau-05` — The Scientific Method Kleisli Closure Triangle (Ch 1 -> Ch 2 -> Ch 7)** ([[kleisli-categories-scientific-method]], [[ologs-ontology-logs]], [[scientific-agreement-worldviews]]): Figure 1.1's informal scientific method cycle fails as a pure Set-olog (Ch 2) due to expert context, but commutes rigorously as a Kleisli olog in Set_T (Ex 7.3.3.10). *[H^1 Obstruction in pure Set -> Resolved in H^0(Set_T) via Monad Context]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 47–67)

### `Example 2.3.3.2` (Noncommuting diagram) — [PDF Page 62]
> Example 2.3.3.2 (Noncommuting diagram). In my conception of the world, the following diagram does not commute: The noncommutativity of diagram (2.18) does not imply that no person lives in the same city as his or her father. Rather it implies that it is not the case that every person lives in the same city as his or her father.

### `Example 2.3.3.5` — [PDF Page 63]
> Example 2.3.3.5. Consider the olog To put the fact that diagram (2.21) commutes into English, we first English the two paths: F = “a person has an address which is in a city” and G = “a person lives in a city.” The source of both is s = “a person” and the target of both is t = “a city.” Write:

### `Remark 2.3.2.3` — [PDF Page 54]
> Remark 2.3.2.3. In keeping with Warning 2.3.2.2, the arrows in (2.12*) and (2.13*) may not be wrong but simply reflect that the author has an idiosyncratic worldview or vocabulary. Maybe the author believes that every mechanical pencil uses exactly one piece of lead. If this is so, then ⌜a mechanical pencil⌝→uses⌜a piece of lead⌝ is indeed a valid aspect. Similarly, suppose the author meant to say that each person was once a child, or that a person has an inner child. Since every person has one and only one inner child (according to the author), the map ⌜a person⌝→has as inner child⌜a child⌝ is a valid aspect. We cannot fault the olog for its

### `Remark 2.3.2.5` — [PDF Page 54]
> Remark 2.3.2.5. Note that the map in (2.14) is a valid aspect, but a similarly benign-looking map ⌜a book⌝→has as author⌜a person⌝ would not be valid, because it is not functional. When creating an olog, one must be vigilant about this type of mistake because it is easy to miss, and it can corrupt the olog. Sometimes the label on an arrow can be shortened or dropped altogether if it is obvious from context (see Section 2.3.3). Here is a common example from the way I write ologs.

### `Warning 2.3.2.2` — [PDF Page 53]
> Warning 2.3.2.2. The author of an olog has a worldview, some fragment of which is captured in the olog. When person A examines the olog of person B, person A may or may not agree with it. For example, person B may have the following olog which associates to each marriage a man and a woman. Person A may take the position that some marriages involve two men or two women and thus see B’s olog as wrong. Such disputes are not “problems” with either A’s olog or B’s olog; they are discrepancies between worldviews. Hence, a reader R may see an olog in this book and notice a discrepancy between R’s worldview and my own, but this is not a problem with 

### `Exercise 2.3.2.7` — [PDF Page 57]
> Exercise 2.3.2.7. On page 25, the arrow in (2.12*) was indicated as an invalid aspect:

### `Exercise 2.3.3.1` — [PDF Page 61]
> Exercise 2.3.3.1. Create an olog for human nuclear biological families that includes the concepts of person, man, woman, parent, father, mother, and child. Make sure to label all the arrows and that each arrow indicates a valid aspect in the sense of Section 2.3.2.1. Indicate with check marks (✓) the diagrams that are intended to commute. If the 2-dimensionality of the page prevents a check mark from being unambiguous, indicate the intended commutativity with an equation.

### `Exercise 2.3.3.3` — [PDF Page 62]
> Exercise 2.3.3.3. Create an olog about a scientific subject, preferably one you think about often. The olog should have at least five boxes, five arrows, and one commutative diagram.

### `Exercise 2.3.3.6` — [PDF Page 64]
> Exercise 2.3.3.6. This olog was taken from Spivak [38]. It says that a landline phone is physically located in the region to which its phone number is assigned. Translate this fact into English using the formula from (2.20).

### `Exercise 2.3.3.7` — [PDF Page 64]
> Exercise 2.3.3.7. In olog (2.22), suppose that the box ⌜an operational landline phone⌝ is replaced with the box ⌜an operational cell phone⌝. Would the diagram still commute?

### `Exercise 2.3.3.9` — [PDF Page 65]
> Exercise 2.3.3.9. For each of the following types, write a function for which it is the image, or write “not clearly useful as an image type.” a. ⌜a book⌝ b. ⌜a material that has been fabricated by a working process of type T ⌝ c. ⌜a bicycle owner⌝ d. ⌜a child⌝ e. ⌜a used book⌝ f. ⌜a primary residence⌝ __________________ 1Note that the symbol x′, read “x-prime,” has nothing to do with calculus or derivatives. It is simply notation used to name a symbol that is somehow like x. This suggestion of kinship between x and x′ is meant only as an aid for human cognition, not as part of the mathematics.

### `Solution 2.3.3.1` — [PDF Page 61]
> Solution 2.3.3.1.

## 6. Page-by-Page Deep Index (PDF Pages 47–67)
- **Page 47** (`2.3 Ologs`): 2.3 Ologs In this book I ground the mathematical ideas in applications whenever possible. To that end I introduce ologs, which serve as a bridge between mathematics and various conceptual landscapes. The following material is taken from Spivak and Kent [43], an introduction to ologs....
- **Page 48** (`2.3 Ologs`): ...
- **Page 49** (`2.3 Ologs`): 2.3.1 Types A type is an abstract concept, a distinction the author has made. Each type is represented as a box containing a singular indefinite noun phrase. Each of the following four boxes is a type: Each of the four boxes in (2.8) represents a type of thing, a whole class of things, and the label on that box is what...
- **Page 50** (`2.3 Ologs`): so that the variables (m, w) are clear. Rules of good practice 2.3.1.2. A type is presented as a text box. The text in that box should (i) begin with the word a or an; (ii) refer to a distinction made and recognizable by the olog’s author; (iii) refer to a distinction for which instances can be documented; (iv) be the ...
- **Page 51** (`2.3 Ologs`): ...
- **Page 52** (`2.3 Ologs`): 2.3.2 Aspects An aspect of a thing x is a way of viewing it, a particular way in which x can be regarded or measured. For example, a woman can be regarded as a person; hence “being a person” is an aspect of a woman. A molecule has a molecular mass (say in daltons), so “having a molecular mass” is an aspect of a molecul...
- **Page 53** (`2.3 Ologs`) · **Items:** Warning 2.3.2.2: A person may have no children or may have more than one child, so the first arrow is invalid: it is not a function. Similarly, if one drew an arrow from each mechanical pencil to each piece of lead it uses, one would not have a function. Warning 2.3.2.2. The author of an olog has a worldview, some fragment of which is ...
- **Page 54** (`2.3 Ologs`) · **Items:** Remark 2.3.2.3, Remark 2.3.2.5: Remark 2.3.2.3. In keeping with Warning 2.3.2.2, the arrows in (2.12*) and (2.13*) may not be wrong but simply reflect that the author has an idiosyncratic worldview or vocabulary. Maybe the author believes that every mechanical pencil uses exactly one piece of lead. If this is so, then ⌜a mechanical pencil⌝→uses⌜a pie...
- **Page 55** (`2.3 Ologs`): Neither arrow is readable by the preceding protocol (e.g., “a pair (x, y), where x and y are integers x an integer” is not an English sentence), and yet it is clear what each map means. For example, given (8, 11) in A, arrow x would yield 8 and arrow y would yield 11. The label x can be thought of as a nickname for the...
- **Page 56** (`2.3 Ologs`): considered aspects. Often the word has indicates a relationship—sometimes it is functional, as in ⌜a person⌝→has⌜a stomach⌝, and sometimes it is not, as in ⌜a father⌝→has⌜a child⌝. Clearly, a father may have more than one child. This one is easily fixed by realizing that the arrow should go the other way: there is a fu...
- **Page 57** (`2.3 Ologs`) · **Items:** Exercise 2.3.2.7: For example, Exercise 2.3.2.7. On page 25, the arrow in (2.12*) was indicated as an invalid aspect:...
- **Page 58** (`2.3 Ologs`): Create a valid olog that captures the parent-child relationship; your olog should still have boxes ⌜a person⌝ and ⌜a child⌝ but may have an additional box. Rules of good practice 2.3.2.8. An aspect is presented as a labeled arrow pointing from a source box to a target box. The arrow label text should (i) begin with a v...
- **Page 59** (`2.3 Ologs`): ...
- **Page 60** (`2.3 Ologs`): 2.3.3 Facts In this section I discuss facts, by which I mean path equivalences in an olog. It is the notion of path equivalences that makes category theory so powerful. A path in an olog is a head-to-tail sequence of arrows. That is, any path starts at some box B0, then follows an arrow emanating from B0 (moving in the...
- **Page 61** (`2.3 Ologs`) · **Items:** Exercise 2.3.3.1, Solution 2.3.3.1: commutes, we could either draw a check mark inside the square or write the equation A[f,g]≃A[h,i] above it.6 Either way, it means that starting from A, “doing f, then g” is equivalent to “doing h, then i.” Here is another example: Note how this diagram gives us the established terminology for the various ways in which ...
- **Page 62** (`2.3 Ologs`) · **Items:** Example 2.3.3.2, Exercise 2.3.3.3: Note that neither of the two triangles from child to person commute. To say that they did commute would be to say that “a child and its mother are the same person” and that “a child and its father are the same person.” Example 2.3.3.2 (Noncommuting diagram). In my conception of the world, the following diagram does not...
- **Page 63** (`2.3 Ologs`) · **Items:** Example 2.3.3.5: 2.3.3.4 A formula for writing facts as English Every fact consists of two paths, say, P and Q, that are to be declared equivalent. The paths P and Q will necessarily have the same source, say, s, and target, say, t, but their lengths may be different, say, m and n respectively.7 We draw these paths as P:•a0=s→f1•a1→f2•...
- **Page 64** (`2.3 Ologs`) · **Items:** Exercise 2.3.3.6, Exercise 2.3.3.7: Given x, a person, consider the following. We know that x is a person, who has an address, which is in a city, that we call P(x). We also know that x is a person, who lives in a city that we call Q(x). Fact: Whenever x is a person, we will have P(x) = Q(x). More concisely, one reads olog 2.21 as A person x has an addre...
- **Page 65** (`2.3 Ologs`) · **Items:** Exercise 2.3.3.9: 2.3.3.8 Images This section discusses a specific kind of fact, generated by any aspect. Recall that every function has an image (2.3), meaning the subset of elements in the codomain that are “hit” by the function. For example, the function f : ℤ → ℤ given by f(x) = 2 * x: ℤ → ℤ has as image the set of all even numbers....
- **Page 66** (`2.3 Ologs`): 2This kind of arrow, ↦, is read “maps to.” A function f : X → Y means a rule for assigning to each element x ∈ X an element f(x) ∈ Y. We say that “x maps to f(x)” and write x ↦f(x). 3The notation HomSet(−, −) will make more sense later, when it is seen in a larger context. See especially Section 5.1. 4Canonical, as use...
- **Page 67** (`2.3 Ologs`): ...
