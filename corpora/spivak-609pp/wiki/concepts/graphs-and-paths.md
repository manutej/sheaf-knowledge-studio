---
id: graphs-and-paths
title: "Graphs, Path Categories & Homomorphisms"
type: SheafStalk
chapter: 4
section: "4.3"
pdf_pages: "201–220"
symbol: "G = (V, A, src, tgt)"
layer: "Pre-Categorical Models"
extracted_declarations: 36
restricts_to: [pullbacks-and-fiber-products, monoids-and-actions]
glues_with: [database-schemas-instances, categories-objects-morphisms]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Graphs, Path Categories & Homomorphisms (`G = (V, A, src, tgt)`)

> **Sheaf Stalk Location:** Chapter 4 (Categories and Functors, Without Admitting It: Monoids, Groups, Graphs, Orders & Databases) · Section `4.3` · **PDF Pages 201–220**

## 1. Epistemic Worldview & Intuition

A directed multigraph G consists of a set of vertices V, a set of arrows A, and source/target functions src, tgt : A -> V. Every graph generates a free category of finite paths Path(G), where length-0 paths are identity morphisms and concatenation is composition.

## 2. Formal Categorical Core

A graph G = (V, A, src, tgt) is a functor from the schema {A ==src,tgt==> V} to Set (Def 4.3.1.1, p. 203). Path_n(G) is the iterated fiber product A ×_V A ×_V ... ×_V A; Path(G) = coproduct_{n>=0} Path_n(G) (Def 4.3.2.1, p. 211).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[A]`** — *an arrow a in A*
- **`[V]`** — *a vertex v in V*
- **`[P]`** — *a composable path p in Path(G)*

### Functional Aspects (Morphisms)
- **`[A]` $\xrightarrow{\text{has source vertex src}}$ `[V]`**
- **`[A]` $\xrightarrow{\text{has target vertex tgt}}$ `[V]`**
- **`[A]` $\xrightarrow{\text{includes as length-1 path into}}$ `[P]`**
- **`[P]` $\xrightarrow{\text{starts at endpoint}}$ `[V]`**
- **`[P]` $\xrightarrow{\text{ends at endpoint}}$ `[V]`**

### Commutative Path Facts ($p \simeq q$)
- Length-2 paths are the pullback A ×_{tgt, V, src} A (p. 211).
- Path concatenation is associative with trivial length-0 paths [v] acting as identities.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-16` (iterated_fiber_product_paths)** $\to$ [[pullbacks-and-fiber-products]] (*Pullbacks (Fiber Products) & Constraint Solving*, p. 88–101): Length-n paths Path_n(G) are the iterated pullback A ×_V A ×_V … ×_V A — `Path_2(G) = A ×_{tgt,V,src} A`
- **`rho-17` (bouquet_of_loops)** $\to$ [[monoids-and-actions]] (*Monoids, Agent Actions & Finite State Machines*, p. 160–191): A 1-vertex graph is an alphabet Σ whose path category Path(G) is the free monoid List(Σ) — `Path(Bouquet_Σ) ≅ List(Σ)`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-20` (underlying_graph_and_paths)** $\leftarrow$ [[database-schemas-instances]] (*Categorical Databases: Schemas (G, ≃) & Table Instances*, p. 245–266): A database schema C = (G, ≃) is a graph G equipped with a congruence on Path(G) — `U(G, ≃) = G`
- **`rho-24` (free_path_category)** $\leftarrow$ [[categories-objects-morphisms]] (*Categories: Objects, Morphisms, Identities & Composition*, p. 267–284): Every graph G freely generates a category Path(G); every category has an underlying graph — `Path : Grph ⇄ Cat : U`

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 201–220)

### `Definition 4.3.1.1` — [PDF Page 203]
> Definition 4.3.1.1. A graph G consists of a sequence G ≔ (V, A, src, tgt), where V is a set, called the set of vertices of G (singular: vertex); A is a set, called the set of arrows of G; src: A → V is a function, called the source function for G; tgt: A → V is a function, called the target function for G. Given an arrow a ∈ A we refer to src(a) as the source vertex of a and to tgt(a) as the target vertex of a. To draw a graph, first draw a dot for every element of V. Then for every element a ∈ A, draw an arrow connecting dot src(a) to dot tgt(a).

### `Definition 4.3.2.1` — [PDF Page 211]
> Definition 4.3.2.1. Let G = (V, A, src, tgt) be a graph. A path of length n in G, denoted p∈PathG(n) , is a head-to-tail sequence p=(v0→a1v1→a2v2→a3⋯→anvn)(4.4) of arrows in G, denoted [ a1,a2,…,an ]v0 . A path is a list of arrows, so we use a variant of list notation, but the extra subscript at the beginning, which indicates the source vertex, reminds us that this list is actually a path. We have canonical isomorphisms PathG(1)≅A and PathG(0)≅V : a path of length 1 is an arrow, and a path of length 0 is a vertex. We refer to the length 0 path [ ]v on vertex v as the trivial path on v. We denote by PathG the set of paths (of any length) in G,

### `Definition 4.3.3.1` — [PDF Page 214]
> Definition 4.3.3.1. Let G = (V, A, src, tgt) and G′ = (V′, A′, src′, tgt′) be graphs. A graph homomorphism f from G to G′, denoted f : G → G′, consists of two functions f0: V → V′ and f1: A → A′ such that the diagrams in (4.5) commute:

### `Definition 4.3.3.9` — [PDF Page 216]
> Definition 4.3.3.9. Let X be a set. A binary relation on X is a subset R ⊆ X × X. If X = ℕ is the set of integers, then the usual defines a binary relation on X:

### `Example 4.3.1.2` (Graph) — [PDF Page 203]
> Example 4.3.1.2 (Graph). Here is a picture of a graph G = (V, A, src, tgt): We have V = {v, w, x, y, z} and A = {f, g, h, i, j, k}. The source and target functions src, tgt: A → V are expressed in the following table (left-hand side):

### `Example 4.3.1.3` — [PDF Page 204]
> Example 4.3.1.3. Every olog has an underlying graph, in the sense of Definition 4.3.1.1. An olog has additional information, namely, information about which pairs of paths are declared equivalent as well as text that has certain English- readability rules.

### `Example 4.3.1.7` — [PDF Page 206]
> Example 4.3.1.7. Recall from Construction 3.2.2.6 the notion of a bipartite graph, defined to be a span (i.e., pair of functions; see Definition 3.2.2.1) A←fR→gB. Now that we have a formal definition of a graph, we might hope that the notion of bipartite graphs fits in as a particular sort of graph, and it does. Let V = A ⊔ B, and let i: A → V and j : B → V be the inclusions. Let src = i ○ f : R → V, and let tgt = j ○ g : R → V be the composites: Then (V, R, src, tgt) is a graph that would be drawn exactly as specified the drawing of spans in Construction 3.2.2.6.

### `Example 4.3.1.8` — [PDF Page 206]
> Example 4.3.1.8. Let n ∈ ℕ be a natural number. The chain graph of length n, denoted [n], is the following graph: •0→•1→⋯→•n In general, [n] has n arrows and n + 1 vertices. In particular, when n = 0, we have that [0] is the graph consisting of a single vertex and no arrows.

### `Example 4.3.1.9` — [PDF Page 206]
> Example 4.3.1.9. Let G = (V, A, src, tgt) be a graph, Suppose that we want to spread it out over discrete time, so that each arrow does not occur within a given time slice but instead over a quantum unit of time. Let [ℕ] = (ℕ, ℕ, n ↦n, n ↦ n + 1) be the graph depicted: •0→0•1→1•2→2⋯ The discussion of limits in a category (see Chapter 6) clarifies that products can be taken in the category of graphs (see Example 6.1.1.5), so [ℕ] × G will make sense. For now, we construct it by hand. Let T(G) = (V × ℕ, A × ℕ, src′, tgt′) be a new graph, where for a ∈ A and n ∈ ℕ, we have src′(a, n) ≔ (src(a), n) and tgt′(a, n) = (tgt(a), n + 1).

### `Example 4.3.2.2` — [PDF Page 211]
> Example 4.3.2.2. Let G = (V, A, src, tgt) be a graph, and suppose v ∈ V is a vertex. If p: v → v is a path of length |p| ∈ ℕ with src¯(p)=tgt¯(p)=v , we call it a loop of length |p|. For n ∈ ℕ, we write pn : v → v to denote the n-fold concatenation pn ≔ p++p++ ⋯ ++p (where p is written n times).

### `Example 4.3.2.3` — [PDF Page 211]
> Example 4.3.2.3. In diagram (4.3), page 120, we see a graph G. In it, there are no paths from v to y, one path (namely, [ f ]v ) from v to w, two paths (namely, v[f,

### `Example 4.3.3.3` (Graph homomorphism) — [PDF Page 214]
> Example 4.3.3.3 (Graph homomorphism). Let G = (V, A, src, tgt) and G′ = (V′, A′, src′, tgt′) be the graphs drawn in (4.6):

### `Remark 4.3.3.2` — [PDF Page 214]
> Remark 4.3.3.2. The conditions (4.5) may look abstruse at first, but they encode a very important idea, roughly stated “arrows are bound to their endpoints.” Under a map of graphs G → G′, one cannot flippantly send an arrow of G any old arrow of G′: it must still connect the vertices it connected before. Following is an example of a mapping that does not respect this condition: a connects 1 and 2 before but not after: The commutativity of the diagrams in (4.5) is exactly what is needed to ensure that arrows are handled in the expected way by a proposed graph homomorphism.

### `Exercise 4.3.1.4` — [PDF Page 204]
> Exercise 4.3.1.4. a. Draw the graph corresponding to the following tables: b. Write two tables like the ones in part (a) corresponding to the following graph:

### `Exercise 4.3.1.5` — [PDF Page 205]
> Exercise 4.3.1.5. a. Let A = {1, 2, 3, 4, 5} and B = {a, b, c}. Draw them, and choose an arbitrary function f : A → B and draw it. b. Let A ⊔ B be the coproduct of A and B (Definition 3.1.2.1), and let A→i1A⊔B←i2B be the two inclusions. Consider the two functions src, tgt: A → A ⊔ B, where src = i1 and tgt is the composition A→fB→i2A⊔B. Draw the associated graph G ≔ (A ⊔ B, A, src, tgt).

### `Exercise 4.3.1.6` — [PDF Page 205]
> Exercise 4.3.1.6. a. Let V be a set. Suppose we just draw the elements of V as vertices and have no arrows between them. Is this a graph? b. Given V, is there any other canonical or somehow automatic nonrandom procedure for generating a graph with those vertices?

### `Exercise 4.3.1.10` — [PDF Page 207]
> Exercise 4.3.1.10. Let G be the following graph: Draw the graph T(G) defined in Example 4.3.1.9, using ellipses (⋯) if necessary.

### `Exercise 4.3.1.11` — [PDF Page 208]
> Exercise 4.3.1.11. Consider the following infinite graph G = (V, A, src, tgt): a. Write the sets A and V. b. What are the source and target functions A → V?

## 6. Page-by-Page Deep Index (PDF Pages 201–220)
- **Page 201** (`4.3 Graphs`): 4.3 Graphs Unless otherwise specified, whenever I speak of graphs in this book, I do not mean curves in the plane, such as parabolas, or pictures of functions generally, but rather systems of vertices and arrows. Graphs are taken to be directed, meaning that every arrow points from a vertex to a vertex; rather than mer...
- **Page 202** (`4.3 Graphs`): ...
- **Page 203** (`4.3 Graphs`) · **Items:** Definition 4.3.1.1, Example 4.3.1.2: 4.3.1 Definition and examples Definition 4.3.1.1. A graph G consists of a sequence G ≔ (V, A, src, tgt), where V is a set, called the set of vertices of G (singular: vertex); A is a set, called the set of arrows of G; src: A → V is a function, called the source function for G; tgt: A → V is a function, called the targe...
- **Page 204** (`4.3 Graphs`) · **Items:** Example 4.3.1.3, Exercise 4.3.1.4: In fact, all the data of the graph G is captured in these two tables—together they tell us the sets A and V and the functions src and tgt. Example 4.3.1.3. Every olog has an underlying graph, in the sense of Definition 4.3.1.1. An olog has additional information, namely, information about which pairs of paths are decla...
- **Page 205** (`4.3 Graphs`) · **Items:** Exercise 4.3.1.5, Exercise 4.3.1.6, Solution 4.3.1.6: Exercise 4.3.1.5. a. Let A = {1, 2, 3, 4, 5} and B = {a, b, c}. Draw them, and choose an arbitrary function f : A → B and draw it. b. Let A ⊔ B be the coproduct of A and B (Definition 3.1.2.1), and let A→i1A⊔B←i2B be the two inclusions. Consider the two functions src, tgt: A → A ⊔ B, where src = i1 and tgt is the compo...
- **Page 206** (`4.3 Graphs`) · **Items:** Example 4.3.1.7, Example 4.3.1.8, Example 4.3.1.9: Example 4.3.1.7. Recall from Construction 3.2.2.6 the notion of a bipartite graph, defined to be a span (i.e., pair of functions; see Definition 3.2.2.1) A←fR→gB. Now that we have a formal definition of a graph, we might hope that the notion of bipartite graphs fits in as a particular sort of graph, and it does. Let V ...
- **Page 207** (`4.3 Graphs`) · **Items:** Exercise 4.3.1.10, Solution 4.3.1.10: Let G be the following graph: Then T(G) will be the graph The f arrows still take a’s to a’s, and the g arrows still take a’s to b’s, but they always march forward in time. Exercise 4.3.1.10. Let G be the following graph: Draw the graph T(G) defined in Example 4.3.1.9, using ellipses (⋯) if necessary. Solution 4.3.1.10...
- **Page 208** (`4.3 Graphs`) · **Items:** Exercise 4.3.1.11, Exercise 4.3.1.12: Exercise 4.3.1.11. Consider the following infinite graph G = (V, A, src, tgt): a. Write the sets A and V. b. What are the source and target functions A → V? Exercise 4.3.1.12....
- **Page 209** (`4.3 Graphs`) · **Items:** Solution 4.3.1.12, Exercise 3.3.1.11: A graph is a pair of functions A ⇉ V. This sets up the notion of equalizer and coequalizer (see Definitions 3.2.3.1 and 3.3.3.1). a. What feature of a graph G is captured by the equalizer of its source and target functions? b. What feature of a graph G is captured by the coequalizer of its source and target functions? ...
- **Page 210** (`4.3 Graphs`): ...
- **Page 211** (`4.3 Graphs`) · **Items:** Definition 4.3.2.1, Example 4.3.2.2, Example 4.3.2.3: 4.3.2 Paths in a graph One usually has some idea of what a path in a graph is, especially if one is is told that a path must always follow the direction of arrows. The following definition makes this idea precise. In particular, one can have paths of any finite length n ∈ ℕ, even length 0 or 1. Also, we want to be able...
- **Page 212** (`4.3 Graphs`) · **Items:** Exercise 4.3.2.4, Exercise 4.3.2.5: g] and [ f,h ]v ) from v to x, and infinitely many paths {[i]y q1++[j,k]y r1++⋯++[i]y qn ++[j,k]yrn|n,q1,r1,…,qn,rn∈ℕ} from y to y. There are other paths as well in G, including the five trivial paths. Exercise 4.3.2.4. How many paths are there in the following graph? •1→f•2→g•3 Exercise 4.3.2.5. Let G be a graph, and ...
- **Page 213** (`4.3 Graphs`): ...
- **Page 214** (`4.3 Graphs`) · **Items:** Definition 4.3.3.1, Remark 4.3.3.2, Example 4.3.3.3: 4.3.3 Graph homomorphisms A graph (V, A, src, tgt) involves two sets and two functions. For two graphs to be comparable, their two sets and their two functions should be appropriately comparable. Definition 4.3.3.1. Let G = (V, A, src, tgt) and G′ = (V′, A′, src′, tgt′) be graphs. A graph homomorphism f from G to G′, d...
- **Page 215** (`4.3 Graphs`) · **Items:** Exercise 4.3.3.4, Exercise 4.3.3.5, Solution 4.3.3.5, Exercise 4.3.3.6: The colors indicate the choice of function f0: V → V′. Given that choice, condition (4.5) imposes in this case that there is a unique choice of graph homomorphism f : G → G′. In other words, where arrows are sent is completely determined by where vertices are sent, in this particular case. Exercise 4.3.3.4. a. Where ar...
- **Page 216** (`4.3 Graphs`) · **Items:** Exercise 4.3.3.7, Solution 4.3.3.7, Definition 4.3.3.9: a. Explain how this works. b. Is it the case that for every n ∈ ℕ, the function Path(f) carries Path(n)(G) to Path(n)(G′), or can path lengths change in this process? c. Suppose that f0 and f1 are injective (meaning no two distinct vertices in G are sent to the same vertex (resp. for arrows) under f). Does this imply t...
- **Page 217** (`4.3 Graphs`) · **Items:** Exercise 4.3.3.10, Exercise 4.3.3.11: given (m, n) ∈ ℕ × ℕ, we put (m, n) ∈ R iff m n. As a table it might be written as in the left-hand table in (4.8): The middle table is the relation {(m, n) ∈ ℕ × ℕ | n = 5m} ⊆ ℕ × ℕ, and the right-hand table is the relation {(m, n) ∈ ℕ × ℕ | |n − m| 1} ⊆ ℕ × ℕ. Exercise 4.3.3.10. A relation on ℝ is a subset of ℝ × ℝ, ...
- **Page 218** (`4.3 Graphs`) · **Items:** Solution 4.3.3.11: Solution 4.3.3.11. a. We have two projections π1, π2 : S × S → S, and we have an inclusion i: R ⊆ S × S. Thus we have a graph R⇉π2○iπ1○iS The idea is that for each row in the table, we draw an arrow from the first column’s value to the second column’s value. b. It is R, which one could call “the number of rows in the t...
- **Page 219** (`4.3 Graphs`) · **Items:** Exercise 4.3.3.12, Exercise 4.3.3.13: Exercise 4.3.3.12. a. If (V, A, src, tgt) is a graph, find a natural way to make a binary relation R ⊆ V × V from it. b. For the left-hand graph G in (4.6), and write out the corresponding binary relation in table form. Exercise 4.3.3.13. a. Given a binary relation R ⊆ S × S, you know from Exercise 4.3.3.11 how to cons...
- **Page 220** (`4.3 Graphs`): ...
