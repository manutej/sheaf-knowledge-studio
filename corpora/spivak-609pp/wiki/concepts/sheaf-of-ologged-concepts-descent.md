---
id: sheaf-of-ologged-concepts-descent
title: "Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data"
type: SheafStalk
chapter: 7
section: "7.2.3.6 & 7.2.3.11–7.2.3.14"
pdf_pages: "521–526"
symbol: "O : Open(Alx(X^op))^op → Sch"
layer: "Sheaf & Topos Layer"
extracted_declarations: 8
restricts_to: [sheaves-and-local-to-global-gluing, categorical-equivalence-cat-sch, ologs-ontology-logs]
glues_with: []
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Sheaf of Ologged Concepts, Alexandrov Sites & Descent Data (`O : Open(Alx(X^op))^op → Sch`)

> **Sheaf Stalk Location:** Chapter 7 (Categories at Work: Adjoint Functors, Data Migration, Sheaves, Monads & Operads) · Section `7.2.3.6 & 7.2.3.11–7.2.3.14` · **PDF Pages 521–526**

## 1. Epistemic Worldview & Intuition

The theoretical heart of our Sheaf Knowledge Base (Section 7.2.3.11, p. 523–524): Spivak upgrades sheaves of sets to a SHEAF OF OLOGGED CONCEPTS (a sheaf of categories/schemas O : Open(X)^op -> Sch). Given a simplicial complex X of agents or conceptual domains, each vertex v holds a local worldview olog O(v), and each higher simplex u holds the common-ground olog O(u) with restriction schema morphisms O(v) -> O(u). Applying the Alexandrov functor Alx(X^op) yields a topological space whose sheaf of categories glues local ologs into a globally consistent worldview!

## 2. Formal Categorical Core

Section 7.2.3.11 (p. 523–524): Given a simplicial complex X (a sub-poset of P(X_0) ordered by inclusion u <= v), assign to each simplex a schema/olog via a functor O : X -> Sch, where u <= v induces a restriction map of ologs O(v) -> O(u) ('any idea shared among all vertices in v is shared among the subset u'). Under the Alexandrov functor Alx : PrO -> Top on X^op, O extends uniquely to a sheaf of categories/schemas on X = Alx(X^op). Remark 7.2.3.6 (p. 521): When local sensors/experts use different vocabularies on overlaps U_{i,j}, they glue via isomorphic Descent Data p_{i,j} : T_i|_{U_{i,j}} ->~ T_j|_{U_{i,j}} satisfying the cocycle condition.

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Simp]`** — *a simplex u in conceptual complex X*
- **`[OpenX]`** — *an Alexandrov open cover U in Open(Alx(X^op))*
- **`[LocOlog]`** — *a local worldview olog O(v) in Sch*
- **`[OvOlog]`** — *a common-ground overlap olog O(u) in Sch*
- **`[GlobOlog]`** — *the glued global worldview sheaf section H⁰(U, O)*

### Functional Aspects (Morphisms)
- **`[Simp]` $\xrightarrow{\text{generates Alexandrov open set in}}$ `[OpenX]`**
- **`[LocOlog]` $\xrightarrow{\text{restricts via schema morphism ρ_{v,u} : O(v) -> O(u) to}}$ `[OvOlog]`**
- **`[GlobOlog]` $\xrightarrow{\text{projects consistently onto each local worldview}}$ `[LocOlog]`**

### Commutative Path Facts ($p \simeq q$)
- Sheaf of Ologged Concepts Theorem (Sec 7.2.3.11, p. 523–524): A functor O : X -> Sch on a simplicial complex X determines a unique sheaf of categories on the Alexandrov space Alx(X^op).
- Descent Data Isomorphism (Remark 7.2.3.6, p. 521 & Example 7.2.3.12, p. 524): Two communities G₁ and G₂ using different words glue over their overlap H = G₁ ∩ G₂ via translation isomorphisms p_{1,2} : O₁|_H ≅ O₂|_H.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-45` (categorifies_Set_sheaf_to_Sch_sheaf)** $\to$ [[sheaves-and-local-to-global-gluing]] (*Sheaves: Open Covers, Restriction Maps & The Local-to-Global Gluing Axiom*, p. 518–522): Upgrades a sheaf of sets O : Open(X)^op -> Set to a sheaf of ologs/categories O : Open(X)^op -> Sch — `O : Open(Alx(X^op))^op -> Sch`
- **`rho-46` (glues_categorical_schemas)** $\to$ [[categorical-equivalence-cat-sch]] (*Equivalence of Categories & Theorem Cat ≃ Sch*, p. 371–391): Each stalk O(v) is an olog/schema (~= category), glued along restriction schema morphisms O(v)->O(u) — `ρ_{v,u} ∈ Hom_Sch(O(v), O(u))`
- **`rho-53` (stalk_evaluation_to_local_olog)** $\to$ [[ologs-ontology-logs]] (*Ologs (Ontology Logs): Functional Worldviews*, p. 47–67): Evaluating the sheaf of ologged concepts O : Open(Alx(X^op))^op -> Sch at any vertex v yields a local Set-olog O(v) — `ev_v : O(U) -> O(v) ∈ Olog`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-03` — The Alexandrov Sheaf of Ologs Worldview Triangle** ([[sheaf-of-ologged-concepts-descent]], [[sheaves-and-local-to-global-gluing]], [[ologs-ontology-logs]]): A simplicial complex X of local ologs O(v) glued via schema restriction maps O(v) -> O(u) forms a sheaf of categories over Alx(X^op). *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 521–526)

### `Definition 7.2.3` — [PDF Page 523]
> Definition 7.2.3.5 defines what should be called a sheaf of sets. We can discuss sheaves of groups or even sheaves of categories. Here is an application of the latter. Recall the notion of simplicial complexes (see Section 3.4.4.3). They look like this: Given such a simplicial complex X, we can imagine each vertex v ∈ X0 as an entity with a worldview (e.g., a person) and each simplex as the common worldview shared by its vertices. To model this, we assign to each vertex v ∈ X an olog O(v), corresponding to the worldview held by that entity, and to each simplex u ∈ Xn, we assign an olog O(u) corresponding to a common ground worldview. Recall t

### `Application 7.2.3.7` — [PDF Page 521]
> Application 7.2.3.7. Consider outer space as a topological space X. Different amateur astronomers record observations of what they see in X on a given night. Let C = [390, 700] denote the set of wavelengths in the visible light spectrum (written in nanometers). Given an open subset U ⊆ X, let O(U) denote the set of functions U → C. The presheaf O satisfies the sheaf condition; this is the taken- for-granted fact that we can patch together different observations of space. Figure 7.1 (see page 377) shows three views of the night sky. Given a telescope position to obtain the first view, one moves the telescope right and a little down to obtain t

### `Application 7.2.3.9` — [PDF Page 522]
> Application 7.2.3.9. Suppose we have a sheaf for temperatures on earth. For every region U, we have a set of theoretically possible temperature assignments throughout U. For example, we may know that if it is warm in Texas, warm in Arkansas, and warm in Kansas, then it cannot be cold in Oklahoma. With such a sheaf O in hand, one can use facts about the temperature in one region U to predict the temperature in another region V. The mathematics is as follows. Suppose given regions U, V ⊆ X and a subset A⊆O(U) corresponding to what we know about the temperature assignment throughout U. We take the following fiber product: The image of the top co

### `Example 7.2.3.10` — [PDF Page 522]
> Example 7.2.3.10. Exercises 5.2.4.3 and 5.2.4.4 discussed the idea of laws being dictated or respected throughout a jurisdiction. If X is earth, to every jurisdiction U ⊆ X we assign the set O(U) of laws that are dictated to hold throughout U. Given a law on U and a law on V, we can see if they amount to the same law on U ∩ V. For example, on U a law might say, “no hunting near rivers” and on V a law might say, “no hunting in public areas.” It happens that on U ∩ V all public areas are near rivers, and vice versa, so the laws agree there. These laws patch together to form a single rule about hunting that is enforced throughout the union U ∪ V

### `Example 7.2.3.12` — [PDF Page 524]
> Example 7.2.3.12. Imagine two groups of people G1 and G2 each making observations about the world. Suppose there is some overlap H = G1 ∩ G2. Then it may happen that there is a conversation including G1 and G2, and both groups are talking about something (though using different words). H says, “You guys are talking about the same things, you just use different words.” In this case there is an observation being made throughout G1 ∪ G2 that agrees with both those on G1 and those on G2. 7.2.3.13 Time One can use sheaves to model objects in time; Goguen [17] gave an approach to this. For an approach that more closely fits the flow of this book, l

### `Example 7.2.3.14` — [PDF Page 525]
> Example 7.2.3.14. Consider a hospital in which babies are born. In our scenario, mothers enter the hospital, babies are born, mothers and babies leave the hospital. Let C be the schema Consider the eight-hour intervals Shift1≔(Jan 1, 00:00−08:00),Shift2≔(Jan 1, 04:00−12:00),Shift3≔(Jan 1, 08:0 The nurses take shifts of eight hours, overlapping with their predecessors by four hours, and they record in the database only patients that were there throughout their shift or throughout any overlapping shift. Here is the schema: Whether or not this implementation of the sheaf semantics is most useful in practice is certainly debatable. But something 

### `Remark 7.2.3.6` — [PDF Page 521]
> Remark 7.2.3.6. Application 7.2.3.1 said that sheaves help us patch together information from different sources. Even if different temperature-recording devices Ti and Tj registered different temperatures on an overlapping region Ui ∩ Uj, they could be patched together if given a consistent translation system between their results. What is actually needed is a set of isomorphisms pi,j:Ti|Ui,j→≅Tj|Ui,j that translate between them, and that these pi,j’s act in concert with one another. This (when precisely defined) is called descent data. The way it interacts with the definition of sheaf given in Definitions 7.2.3.2 and 7.2.3.5 is buried in the

### `Exercise 7.2.3.8` — [PDF Page 521]
> Exercise 7.2.3.8.

## 6. Page-by-Page Deep Index (PDF Pages 521–526)
- **Page 521** (`7.2 Categories of functors`) · **Items:** Remark 7.2.3.6, Application 7.2.3.7, Exercise 7.2.3.8, Figure 7.1: that cover. Sheaf condition Given a sequence a1, …, an, where each ai∈O(Vi) is a value assignment throughout Vi, suppose that for all i, j, we have ai|Vi∩Vj=aj|Vi∩Vj; then there is a unique value assignment b∈O(U) such that b|Vi=ai. The presheaf O is called a sheaf if it satisfies the sheaf condition for every cover. R...
- **Page 522** (`7.2 Categories of functors`) · **Items:** Application 7.2.3.9, Example 7.2.3.10: Find an application of sheaves in your own domain of expertise. Application 7.2.3.9. Suppose we have a sheaf for temperatures on earth. For every region U, we have a set of theoretically possible temperature assignments throughout U. For example, we may know that if it is warm in Texas, warm in Arkansas, and warm in Ka...
- **Page 523** (`7.2 Categories of functors`) · **Items:** Definition 7.2.3: 7.2.3.11 Sheaf of ologged concepts Definition 7.2.3.5 defines what should be called a sheaf of sets. We can discuss sheaves of groups or even sheaves of categories. Here is an application of the latter. Recall the notion of simplicial complexes (see Section 3.4.4.3). They look like this: Given such a simplicial complex...
- **Page 524** (`7.2 Categories of functors`) · **Items:** Example 7.2.3.12: that any idea shared among the people in v is shared among the people in u. Thus we have a functor O:X→Sch (where we forget the distinction between ologs and databases for notational convenience). To every simplicial complex (indeed every ordered set) one can associate a topological space; in fact, we have a functor Al...
- **Page 525** (`7.2 Categories of functors`) · **Items:** Example 7.2.3.14: Example 7.2.3.14. Consider a hospital in which babies are born. In our scenario, mothers enter the hospital, babies are born, mothers and babies leave the hospital. Let C be the schema Consider the eight-hour intervals Shift1≔(Jan 1, 00:00−08:00),Shift2≔(Jan 1, 04:00−12:00),Shift3≔(Jan 1, 08:0 The nurses take shifts of...
- **Page 526** (`7.2 Categories of functors`): ...
