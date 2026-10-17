---
id: database-schemas-instances
title: "Categorical Databases: Schemas (G, ≃) & Table Instances"
type: SheafStalk
chapter: 4
section: "4.5"
pdf_pages: "245–266"
symbol: "C = (G, ≃), I : C → Set"
layer: "Pre-Categorical Models"
extracted_declarations: 31
restricts_to: [graphs-and-paths, ologs-ontology-logs]
glues_with: [functors-structure-maps, natural-transformations-functor-cat, categorical-equivalence-cat-sch, grothendieck-construction-comma]
source_book: "David I. Spivak — Category Theory for the Sciences (MIT Press, 2014)"
---

# Categorical Databases: Schemas (G, ≃) & Table Instances (`C = (G, ≃), I : C → Set`)

> **Sheaf Stalk Location:** Chapter 4 (Categories and Functors, Without Admitting It: Monoids, Groups, Graphs, Orders & Databases) · Section `4.5` · **PDF Pages 245–266**

## 1. Epistemic Worldview & Intuition

Spivak's unified theory of data and knowledge: a relational database schema is a graph G equipped with a congruence (path equivalence relation ≃) declaring which foreign-key chains must commute. A database instance I on C populates each vertex with a set of rows and each arrow with a column function obeying all declared path equations.

## 2. Formal Categorical Core

A congruence ~ on Path(G) is an equivalence relation respecting endpoints and path concatenation: if p ~ q then r o p o s ~ r o q o s (Def 4.5.2.3, p. 253). A schema is C = (G, ~). An instance I on C assigns a set I(v) to each vertex v and a function I(a) : I(v) -> I(w) to each arrow a : v -> w such that I(p) = I(q) whenever p ~ q (Def 4.5.3.1, p. 261).

## 3. Local Olog Schema ($\mathcal{O}(U) \in \mathbf{Sch} \simeq \mathbf{Cat}$)

### Types (Boxes)
- **`[Emp]`** — *an employee e in Employee table*
- **`[Dept]`** — *a department d in Department table*
- **`[Str]`** — *a string s in String attribute table*

### Functional Aspects (Morphisms)
- **`[Emp]` $\xrightarrow{\text{works under manager}}$ `[Emp]`**
- **`[Emp]` $\xrightarrow{\text{works in department}}$ `[Dept]`**
- **`[Dept]` $\xrightarrow{\text{has secretary}}$ `[Emp]`**
- **`[Emp]` $\xrightarrow{\text{has first name}}$ `[Str]`**

### Commutative Path Facts ($p \simeq q$)
- Path Equivalence Rule (Example 4.5.2.1, p. 252): worksIn ∘ manager ≃ worksIn (every employee works in the same department as their manager) and worksIn ∘ secretary ≃ id_Dept.

## 4. Sheaf Restriction Morphisms ($\rho_{U \to V}$) & Overlap Gluing

### Outgoing Restrictions ($\rho_{U,V} : \mathcal{F}(U) \to \mathcal{F}(V)$)
- **`rho-20` (underlying_graph_and_paths)** $\to$ [[graphs-and-paths]] (*Graphs, Path Categories & Homomorphisms*, p. 201–220): A database schema C = (G, ≃) is a graph G equipped with a congruence on Path(G) — `U(G, ≃) = G`
- **`rho-21` (identifies_olog_and_schema)** $\to$ [[ologs-ontology-logs]] (*Ologs (Ontology Logs): Functional Worldviews*, p. 47–67): An olog is precisely a database schema with natural-language type/aspect labels — `Olog = Sch`

### Incoming Gluing Fibers (Higher Open Sets Restricting Here)
- **`rho-26` (instances_as_Set_functors)** $\leftarrow$ [[functors-structure-maps]] (*Functors: Structure-Preserving Maps Between Worldviews*, p. 285–337): A database instance I on schema C is a functor I : C -> Set — `C-Inst ≅ Fun(C, Set)`
- **`rho-28` (instance_homomorphisms)** $\leftarrow$ [[natural-transformations-functor-cat]] (*Natural Transformations & The Category of Database Instances*, p. 338–370): Natural transformations between functors I, J : C -> Set are database instance homomorphisms — `Hom_{C-Inst}(I, J) = Nat(I, J)`
- **`rho-29` (equivalence_of_schemas_and_categories)** $\leftarrow$ [[categorical-equivalence-cat-sch]] (*Equivalence of Categories & Theorem Cat ≃ Sch*, p. 371–391): Every schema (G, ≃) presents a category and every category is presented by a canonical schema — `Cat ≃ Sch (Sec 5.4)`
- **`rho-33` (flattens_instance_to_elements)** $\leftarrow$ [[grothendieck-construction-comma]] (*Opposite Categories, Grothendieck Construction ∫I & Comma Categories*, p. 439–460): Grothendieck construction ∫I flattens a database instance I : C -> Set into an RDF graph over C — `π : ∫_C I -> C`

### 2-Simplex Commutative Gluing Triangles ($\rho_{V,W} \circ \rho_{U,V} = \rho_{U,W}$)
- **`tau-01` — The Schema-Category-Instance Gluing Triangle** ([[categorical-equivalence-cat-sch]], [[database-schemas-instances]], [[functors-structure-maps]]): Translating a category C to a schema R(C) and taking instances agrees with taking Set-valued functors Fun(C, Set). *[H^0 Exact (Zero Obstruction)]*

## 5. Extracted Formal Declarations from `cattheory.pdf` (Pages 245–266)

### `Definition 4.5.2.3` — [PDF Page 253]
> Definition 4.5.2.3.

### `Definition 4.5.2.3` — [PDF Page 253]
> Definition 4.5.2.3. Let G = (V, A, src, tgt) be a graph, and let PathG denote the set of paths in G (see Definition 4.3.2.1). A path equivalence declaration (or PED) is an expression of the form p ≃ q, where p, q ϵ PathG have the same source and target, src(p) = src(q) and tgt(p) = tgt(q). A congruence on G is a relation ≃ on PathG that has the following properties: 1. The relation ≃ is an equivalence relation. 2. If p ≃ q, then src(p) = src(q). 3. If p ≃ q, then tgt(p) = tgt(q). 4. Suppose given paths p, p′: a → b and q, q′: b → c. If p ≃ p′ and q ≃ q′, then (p ++ q) ≃ (p′ ++ q′).

### `Definition 4.5.2.7` — [PDF Page 254]
> Definition 4.5.2.7. A database schema (or simply schema) C consists of a pair C≔(G,≃), where G is a graph and ≃ is a congruence on G.

### `Definition 4.5.3.1` — [PDF Page 261]
> Definition 4.5.3.1. Let C=(G,≃), where G = (V, A, src, tgt). An instance on C, denoted (PK,FK):C→Set, is defined as follows: One announces some constituents (A. primary ID part, B. foreign key part) and shows that they conform to a law (1. preservation of congruence). Specifically, one announces A. a function PK: V → Set, i.e., to each vertex v ∈ V one provides a set PK(v);9 B. for every arrow a ∈ A with v = src(a) and w = tgt(a), a function FK(a): PK(v) → PK(w).10 One must then show that the following law holds for any vertices v, w and paths p = v[a1, a2, …, am] and q = v[a′1, a′2, …, a′n] from v to w: 1. If p ≃ q, then for all x ∈ PK(v), w

### `Definition 4.5.3` — [PDF Page 262]
> Definition 4.5.3.1 hold?

### `Application 4.5.2.11` — [PDF Page 256]
> Application 4.5.2.11. Imagine a deterministic quantum-time universe in which there are discrete time steps. We model it as a discrete dynamical system, i.e., a table of the form (4.17). For every possible state of the universe we include a row in the table. The state in the next instant is recorded in the second column.8

### `Example 4.5.1.1` — [PDF Page 247]
> Example 4.5.1.1. When graphene is strained (lengthened by a factor of x 1), it becomes stressed (carries a force in the direction of the lengthening). The following is a madeup set of data: In the table in (4.11) titled “Graphene Sample,” the rows refer to graphene samples, and the table is so named. Each graphene sample can be observed according to the source supplier from which it came, the strain that it was subjected to, and the stress that it carried. These observations are the columns. In the right-hand table the rows refer to suppliers of various things, and the table is so named. Each supplier can be observed according to its full nam

### `Example 4.5.1.3` — [PDF Page 248]
> Example 4.5.1.3. Consider the bookkeeping necessary to run a department store. We keep track of a set of employees and a set of departments. For each employee e, we keep track of E.1 the first name of e, which is a FirstNameString, E.2 the last name of e, which is a LastNameString, E.3 the manager of e, which is an Employee, E.4 the department that e works in, which is a Department. For each department d, we keep track of D.1 the name of d, which is a DepartmentNameString, D.2 the secretary of d, which is an Employee. We can suppose that E.1, E.2, and D.1 are data columns (referring to names of various sorts), and E.3, E.4, and D.2 are foreig

### `Example 4.5.1.6` — [PDF Page 249]
> Example 4.5.1.6. Consider again Example 4.5.1.3. Note that first names and last names have a particular type, which we all but ignored. We could cease to ignore them by adding three tables, as follows:

### `Example 4.5.2.1` — [PDF Page 252]
> Example 4.5.2.1. In Examples 4.5.1.3 and 4.5.1.6, the conceptual layout for a department store was given, and some example tables were shown. We were instructed to keep track of employees, departments, and six types of data (E.1, E.2, E.3, E.4, D.1, and D.2), and to follow two rules (Rule 1, Rule 2). All of this is summarized in the following picture: The five tables from (4.12) and (4.14) are seen as five vertices; this is also the number of primary ID columns. The six foreign key columns from (4.12) and (4.14) are seen as six arrows; each points from a table to a foreign table. The two rules from (4.13) are seen as declarations at the top o

### `Example 4.5.2.8` — [PDF Page 255]
> Example 4.5.2.8. Pictured in (4.15) is a graph with two PEDs; these generate a congruence, as discussed in Remark 4.5.2.4. Thus this constitutes a database schema. A schema can be converted into a system of tables, each with a primary key and some number of foreign keys referring to other tables, as discussed in Section 4.5.1. Definition 4.5.2.7 gives a precise conceptual understanding of what a schema is, and the following rules describe how to convert it into a table layout. Rules of good practice 4.5.2.9. Converting a schema C=(G,≃) into a table layout should be done as follows: (i) There should be a table for every vertex in G, and if the

### `Example 4.5.2.10` (Discrete dynamical system) — [PDF Page 255]
> Example 4.5.2.10 (Discrete dynamical system). Consider the schema in which the congruence is trivial (i.e., generated by the empty set of PEDs.) This schema is quite interesting. It encodes a set s and a function f: s → s. Such a thing is called a discrete dynamical system. One imagines s as the set of states, and for any state x ∈ s, the function f encodes a notion of next state f(x) ∈ s. For example,

### `Example 4.5.2.12` (Finite hierarchy) — [PDF Page 256]
> Example 4.5.2.12 (Finite hierarchy). The schema Loop can also be used to encode hierarchies, such as the manager relation from Examples 4.5.1.3 and 4.5.2.1, One problem with this, however, is if a schema has even one loop, then it can have infinitely many paths (corresponding, e.g., to an employee’s manager’s manager’s manager’s … manager). Sometimes we know that in a given company that process eventually terminates, a famous example being that at Ben and Jerry’s ice cream company, there were only seven levels. In that case we know that an employee’s eighth-level manager is equal to his or her seventh-level manager. This can be encoded by the

### `Example 4.5.2.16` — [PDF Page 257]
> Example 4.5.2.16. Consider the olog We can document some instances of this relationship using the following table:

### `Example 4.5.3.3` (Monoid action table) — [PDF Page 262]
> Example 4.5.3.3 (Monoid action table). In Example 4.1.2.9 we saw how a monoid M could be captured as an olog with only one object. As a database schema, this means there is only one table. Every generator of M would be a column of the table. The notion of database instance for such a schema (see Definition 4.5.3.1) matches perfectly with the notion of action table from Section 4.1.3. Note that a monoid can act on itself, in which case this action table is the monoid’s multiplication table, as in Example 4.1.3.2, but it can also act on any other set, as in Example 4.1.3.1. If M acts on a set S, then the set of rows in the action table will be 

### `Example 4.5.3.7` — [PDF Page 263]
> Example 4.5.3.7. Consider the department store schema from Example 4.5.2.1. More specifically consider the pathEmployee[worksIn, secretary, last] in (4.15), which points from Employee to LastNameString. The instance lets us interpret this path as a function from the set of employees to the set of last names; this could be a useful function to have in real-life office settings. The instance from (4.12) would yield the following function: Employee ID Secr. name 101 Hillbert 102 Russell 103 Hillbert

### `Remark 4.5.2.4` — [PDF Page 253]
> Remark 4.5.2.4. Any set of path equivalence declarations (PEDs) generates a congruence. The proof of this is analogous to that of Proposition 4.1.1.18. We tend to elide the difference between a congruence and a set of PEDs that generates it. The basic idea for generating a congruence from a set R of PEDs is to proceed as follows. First find the equivalence relation generated by R. Then every time there are paths p, p′: a → b and q, q′: b → c with p ≃ p′ and q ≃ q′,

### `Exercise 4.5.2.2` — [PDF Page 252]
> Exercise 4.5.2.2. Create a schema (consisting of dots and arrows) describing the conceptual layout of information presented in Example 4.5.1.1. In order to define schemas, we must first define the notion of congruence for

## 6. Page-by-Page Deep Index (PDF Pages 245–266)
- **Page 245** (`4.5 Databases: schemas and instances`): 4.5 Databases: schemas and instances So far this chapter has discussed classical objects from mathematics. The present section is about databases, which are classical objects from computer science. These are truly “categories and functors, without admitting it” (see Theorem 5.4.2.3)....
- **Page 246** (`4.5 Databases: schemas and instances`): ...
- **Page 247** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.1.1: 4.5.1 What are databases? Data, in particular, the set of observations made during experiment, plays a primary role in science of any kind. To be useful, data must be organized, often in a row-and-column display called a table. Columns existing in different tables can refer to the same data. A database is a collection ...
- **Page 248** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.1.3: change the layout of the left-hand table by adding an appropriate column. This can be accomplished using morphisms of schemas (see Section 5.4.1). 4.5.1.2 Primary keys, foreign keys, and data columns There is a bit more structure in the tables in (4.11) than first meets the eye. Each table has a primary ID column, on t...
- **Page 249** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.1.6: The tables in (4.12) show how such a database might look at a particular moment in time. 4.5.1.4 Business rules Looking at the tables in (4.12), one may notice a few patterns. First, every employee works in the same department as his or her manager. Second, every department’s secretary works in that department. Perhaps...
- **Page 250** (`4.5 Databases: schemas and instances`): In combination, (4.12) and (4.14) form a collection of five tables, each with the property that every column is either a primary key or a foreign key. The notion of data column is now subsumed under the notion of foreign key column. Each column is either a primary key (one per table, labeled ID) or a foreign key column...
- **Page 251** (`4.5 Databases: schemas and instances`): ...
- **Page 252** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.2.1, Exercise 4.5.2.2: 4.5.2 Schemas Pictures here, roughly graphs, should capture the conceptual layout to which the data conforms, without being concerned (yet) with the individual pieces of data that may populate the tables in this instant. We proceed at first by example; the precise definition of schema is given in Definition 4.5.2.7. Ex...
- **Page 253** (`4.5 Databases: schemas and instances`) · **Items:** Definition 4.5.2.3, Definition 4.5.2.3, Remark 4.5.2.4: an arbitrary graph G. Roughly a congruence is an equivalence relation that indicates how different paths in G are related (see Section 4.3.2). A notion of congruence for monoids was given in Definition 4.1.1.17, and the current notion is a generalization of that. A congruence (in addition to being reflexive, symmetric,...
- **Page 254** (`4.5 Databases: schemas and instances`) · **Items:** Exercise 4.5.2.5, Exercise 4.5.2.6, Definition 4.5.2.7: add to R the relation (p ++ q) ≃ (p′ ++ q′). Exercise 4.5.2.5. Suppose given the following graph G, with the PED b[w, x] ≃ b[y, z]: In the congruence generated by that PED, is it the case that a[v, w, x] ≃ a[v, y, z]? Exercise 4.5.2.6. Consider the graph shown in (4.15) and the two declarations shown at the top. They g...
- **Page 255** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.2.8, Example 4.5.2.10: Example 4.5.2.8. Pictured in (4.15) is a graph with two PEDs; these generate a congruence, as discussed in Remark 4.5.2.4. Thus this constitutes a database schema. A schema can be converted into a system of tables, each with a primary key and some number of foreign keys referring to other tables, as discussed in Sectio...
- **Page 256** (`4.5 Databases: schemas and instances`) · **Items:** Application 4.5.2.11, Example 4.5.2.12: Application 4.5.2.11. Imagine a deterministic quantum-time universe in which there are discrete time steps. We model it as a discrete dynamical system, i.e., a table of the form (4.17). For every possible state of the universe we include a row in the table. The state in the next instant is recorded in the second column...
- **Page 257** (`4.5 Databases: schemas and instances`) · **Items:** Exercise 4.5.2.13, Exercise 4.5.2.14, Example 4.5.2.16: Exercise 4.5.2.13. There is a nontrivial PED on Loop that holds for the data in Example 4.5.2.10. a. What is it? b. How many equivalence classes of paths in Loop are there after you impose that relation? Exercise 4.5.2.14. Let P be a chess-playing program, playing against itself. Given any position (where a position in...
- **Page 258** (`4.5 Databases: schemas and instances`) · **Items:** Exercise 4.5.2.17, Exercise 4.5.2.18, Exercise 4.5.2.19: Clearly, this table of instances can be updated as more moons are discovered by the olog’s owner (be it by telescope, conversation, or research). Exercise 4.5.2.17. In fact, Example 4.5.2.16 did not follow rules 4.5.2.9. Strictly following those rules, copy over the data from (4.19) into tables that are in accordance w...
- **Page 259** (`4.5 Databases: schemas and instances`) · **Items:** Solution 4.5.2.19: a. What path equivalence declarations would be appropriate for this olog? You can use y: F → C, t: F → C, and f: C → F for “youngest,” “tallest,” and “father,” if you prefer. b. How many PEDs are in the congruence? Solution 4.5.2.19. a. There are two: F.t.f ≃ F and F.y.f ≃ F, meaning “a father F ’s tallest child has as...
- **Page 260** (`4.5 Databases: schemas and instances`): ...
- **Page 261** (`4.5 Databases: schemas and instances`) · **Items:** Definition 4.5.3.1, Exercise 4.5.3.2: 4.5.3 Instances Given a database schema (G, ≃), an instance of it is just a bunch of tables whose data conform to the specified layout. These can be seen throughout the previous section, most explicitly in the relationship between schema (4.15) and tables (4.12) and (4.14), and between schema (4.16) and table (4.17). F...
- **Page 262** (`4.5 Databases: schemas and instances`) · **Items:** Definition 4.5.3, Example 4.5.3.3, Exercise 4.5.3.4, Exercise 4.5.3.5: a. What is the set PK(⌜an email⌝)? b. What is the set PK(⌜a person⌝)? c. What is the function FK(→is sent by): PK(⌜an email⌝)→PK(⌜a person⌝)? d. Interpret the sentences at the bottom of C as the Englishing of a simple path equivalence declaration (PED). e. Is your PED satisfied by the instance (4.21); that is, does law...
- **Page 263** (`4.5 Databases: schemas and instances`) · **Items:** Example 4.5.3.7, Exercise 4.5.3.8, Exercise 4.5.3.9: 4.5.3.6 Paths through a database Let C ≔ (G, ≃) be a schema, and let (PK, FK): C → Set be an instance on C. Then for every arrow a: v → w in G we get a function FK(a): PK(v) → PK(w). Functions can be composed, so in fact for every path through G we get a function. Namely, if p = v0[a1, a2, …, an] is a path from v0 to v...
- **Page 264** (`4.5 Databases: schemas and instances`): __________________ 1Although the function ⋆: M × M → M is called the multiplication formula, it may have nothing to do with multiplication. It is just a formula for taking two inputs and returning an output. 2 Definition 4.1.2.1 actually defines a left action of (M, e, ⋆) on S. A right action is like a left action exce...
- **Page 265** (`4.5 Databases: schemas and instances`): P(x). We also know that x is a self-email, which is an email, which is sent to a person who we call Q(x). Fact: Whenever x is a self-email, we have P(x) = Q(x)....
- **Page 266** (`4.5 Databases: schemas and instances`): ...
