---
id: scientific-agreement-worldviews
title: "Science as Agreement & Categorical Worldviews"
type: SheafStalk
chapter: 1
section: "1.1–1.4"
pdf_pages: "11–25"
symbol: "W_sci"
layer: "Epistemic Foundation"
extracted_declarations: 0
restricts_to: []
glues_with: [ologs-ontology-logs, kleisli-categories-scientific-method]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Science as Agreement & Categorical Worldviews (`W_sci`)

> **Sheaf Stalk Location:** Chapter 1 (Introduction: Science as Agreement & The Categorical Pipeline) · Section `1.1–1.4` · **PDF Pages 11–25**

## 1. Epistemic Worldview & Intuition

Science is the pursuit of rigorous agreement—between observation and hypothesis, and between communicating minds. Informal boxes-and-arrows (like Figure 1.1) create an illusion of agreement unless grounded in functions, data, and explicit context.

## 2. Formal Categorical Core

A scientific worldview is formalized as a category C (or schema/olog) together with an instance functor I : C -> Set (empirical data). Interpersonal communication is a functor F : C_1 -> C_2; shared understanding on an overlap is a sheaf gluing condition.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[O]`** — *an observation*
- **`[H]`** — *a hypothesis*
- **`[P]`** — *a prediction*
- **`[E]`** — *an experiment specification*
- **`[Ctx]`** — *an expert-time context (T_M)*

### Functional Aspects (Morphisms)
- **`[O]` $\xrightarrow{\text{analyzed by person yields (in context)}}$ `[H]`**
- **`[H]` $\xrightarrow{\text{analyzed by person produces}}$ `[P]`**
- **`[P]` $\xrightarrow{\text{motivates specification of (Kleisli arrow)}}$ `[E]`**
- **`[E]` $\xrightarrow{\text{when executed results in}}$ `[O]`**

### Commutative Path Facts ($p \simeq q$)
- Naive Figure 1.1 (p. 11) fails to be a valid Set-olog because 'prediction -> experiment' is non-deterministic without an expert context.
- Resolved in Example 7.3.3.10 (p. 544) by embedding Figure 1.1 inside the Kleisli category Set_T of a context monad T.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-01` (formalizes_worldview)** $\leftarrow$ [[ologs-ontology-logs]] (*Ologs (Ontology Logs): Functional Worldviews*, p. 47–67): Explicit functional boxes-and-arrows replacing informal heuristics — `ρ(Olog) = (Ob(O), Hom(O))`
- **`rho-48` (resolves_Figure_1_1_paradox)** $\leftarrow$ [[kleisli-categories-scientific-method]] (*Kleisli Categories C_T & Reconciling the Scientific Method Olog*, p. 540–556): Example 7.3.3.10 resolves Chapter 1's Figure 1.1 scientific method olog inside the Kleisli category Set_T — `Fig 1.1 ∈ Diag(Set_T)`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-05` — The Scientific Method Kleisli Closure Triangle (Ch 1 -> Ch 2 -> Ch 7)** ([[kleisli-categories-scientific-method]], [[ologs-ontology-logs]], [[scientific-agreement-worldviews]]): Figure 1.1's informal scientific method cycle fails as a pure Set-olog (Ch 2) due to expert context, but commutes rigorously as a Kleisli olog in Set_T (Ex 7.3.3.10). *[H^1 Obstruction in pure Set -> Resolved in H^0(Set_T) via Monad Context]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 11–25)

*(Conceptual narrative section — see page-by-page excerpts below.)*

## 6. Page-by-Page Deep Index (PDF Pages 11–25)
- **Page 11** (`Frontmatter`) · **Items:** Figure 1.1: Chapter 1 Introduction The diagram in Figure 1.1 is intended to evoke thoughts of the scientific method. Figure 1.1 An observation analyzed by a person yields a hypothesis, which analyzed by a person produces a prediction, which motivates the specification of an experiment, which when executed results in an observation...
- **Page 12** (`Frontmatter`): the thing she intended to convey? Science is about agreement. When we supply a convincing argument, the result of this convincing is agreement. When, in an experiment, the observation matches the hypothesis—success!—that is agreement. When my methods make sense to you, that is agreement. When practice does not agree wi...
- **Page 13** (`Frontmatter`) · **Items:** Figure 1.1: function of their height. Ologs are discussed in detail throughout this book. Figure 1.1 looks like an olog, but it does not conform to the rules laid out for ologs (see Section 2.3). In an olog, every arrow is intended to represent a mathematical function. It is difficult to imagine a function that takes in prediction...
- **Page 14** (`Frontmatter`): even mentioning this set-theoretic fact? The answer is that when we formalize our ideas, our understanding is clarified. Our ability to communicate with others is enhanced, and the possibility for developing new insights expands. And if we are ever to get to the point that we can input our ideas into computers, we will...
- **Page 15** (`Frontmatter`): ...
- **Page 16** (`1.1 A brief history of category theory`): 1.1 A brief history of category theory The paradigm shift brought on by Einstein’s theory of relativity led to a widespread realization that there is no single perspective from which to view the world. There is no background framework that we need to find; there are infinitely many different frameworks and perspectives...
- **Page 17** (`1.1 A brief history of category theory`): implementation. Eugenio Moggi brought the category-theoretic notion of monads into computer science to encapsulate ideas that up to that point were considered outside the realm of such theory. It is difficult to explain the clarity and beauty brought to category theory by people like Daniel Kan and André Joyal. They ha...
- **Page 18** (`1.1 A brief history of category theory`): ...
- **Page 19** (`1.2 Intention of this book`): 1.2 Intention of this book The world of applied mathematics is much smaller than the world of applicable mathematics. As mentioned, this book is intended to create a bridge between the vast array of mathematical concepts that are used daily by mathematicians to describe all manner of phenomena that arise in our studies...
- **Page 20** (`1.2 Intention of this book`): repeat the experiment—the English language is inadequate to precisely and concisely convey what is being done. The first thought I wish to convey in this book is that reusable methodologies can be formalized and that doing so is inherently valuable. Consider the following analogy. Suppose one wants to add up the area o...
- **Page 21** (`1.2 Intention of this book`): ...
- **Page 22** (`1.3 What is requested from the student`): 1.3 What is requested from the student The only way to learn mathematics is by doing exercises. One does not get fit by merely looking at a treadmill or become a chef by merely reading cookbooks, and one does not learn math by watching someone else do it. There are about 300 exercises in this book. Some of them have so...
- **Page 23** (`1.3 What is requested from the student`): ...
- **Page 24** (`1.4 Category theory references`): 1.4 Category theory references I wrote this book because the available books on category theory are almost all written for mathematicians (the rest are written for computer scientists). One book, Conceptual Mathematics by Lawvere and Schanuel [24], offers category theory to a wider audience, but its style is not approp...
- **Page 25** (`1.4 Category theory references`): ...
