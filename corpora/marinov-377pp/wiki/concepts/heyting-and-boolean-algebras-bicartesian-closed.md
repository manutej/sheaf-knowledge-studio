# Heyting Algebras, Boolean Algebras & Bicartesian Closed Categories (`U_15`)

- **Chapter:** 5 (`§5.3`)
- **Page Fiber:** `pp. 197–211`
- **Layer:** Logical Deduction

## Summary

Thin bicartesian closed categories are Heyting Algebras (modeling intuitionistic logic where P ∨ ¬P need not hold globally, e.g., open-set topologies); adding Law of Excluded Middle yields Boolean Algebras.

## Formal Categorical Core

$$\mathbf{HeytingAlg} \simeq \mathbf{ThinBicartClosedCat}, \quad \neg P \equiv (P \Rightarrow \bot)$$

## Local Olog (`types` & `aspects`)

- **Type `bcc`:** Bicartesian Closed Category (0, 1, ×, +, B^A)
- **Type `heyting`:** Heyting Algebra (Intuitionistic Logic)
- **Type `boolean`:** Boolean Algebra (Classical Logic P ∨ ¬P = ⊤)
- **Aspect:** `bcc` —*collapses to thin poset as*→ `heyting`
- **Aspect:** `boolean` —*is the special complemented case of*→ `heyting`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-35` → [simply-typed-lambda-calculus-curry-howard-lambek](simply-typed-lambda-calculus-curry-howard-lambek.md):** Dropping thinness turns a Heyting algebra into a full Bicartesian Closed Category (STLC) (`$\rho_{35}: \mathbf{HeytingAlg} \leadsto \mathbf{CCC} \simeq \mathbf{STLC}$`)
- **Incoming `rho-26` ← [implication-currying-and-intuitionistic-bhk](implication-currying-and-intuitionistic-bhk.md):** Equipping a bounded lattice with relative pseudocomplements P ⇒ Q yields a Heyting algebra (`$\rho_{26}: (L, \wedge, \vee, \Rightarrow) \in \mathbf{Heyting}$`)
- **Incoming `rho-27` ← [birkhoff-representation-and-boolean-lattices](birkhoff-representation-and-boolean-lattices.md):** Classical Boolean algebras are Heyting algebras satisfying P ∨ ¬P = ⊤ (`$\rho_{27}: \mathbf{BoolAlg} \hookrightarrow \mathbf{HeytingAlg}$`)
- **Incoming `rho-28` ← [propositional-logic-as-category](propositional-logic-as-category.md):** Combining ⊤, ⊥, ∧, ∨, and ⇒ forms a thin Bicartesian Closed Category (`$\rho_{28}: (\top, \bot, \wedge, \vee, \Rightarrow) \mapsto \mathbf{BCC}_{\mathrm{thin}}$`)

## Extracted Definitions, Theorems & Tasks (14)

- **Definition-5.58** (`[p. 197]` · *Visual Definition 58*): A lattice that has a least and greatest elements is called a boundedlattice.
- **Definition-5.59** (`[p. 199]` · *A→B*): The implication object  is an object which is related to objects and  in such a way that such that .A⇒BA B A∧(A⇒B)→B A⇒BA⇒B∧CA⇒B∧C∧D A⇒B A⇒B∧CA⇒B∧C∧DXA∧X→B
- **Definition-5.60** (`[p. 200]` · *Finally, here is a general categorical definition:*): For any two elements in an order  and , the exponential element (called also a relative pseudo-complement of  in respect to ) is the biggest/topmost object  such that the meet of  and  issmaller than , so  (i.e. ). A BA⇒B A BX X AB (A∧X)→B A∧(A⇒B)→B DEFINITION: For any propositions  and , the implication proposition (called also entailment) is the most trivi
- **Definition-5.61** (`[p. 200]` · *A BA⇒B A BX X AB (A∧X)→B A∧(A⇒B)→B*): For any propositions  and , the implication proposition (called also entailment) is the most trivial proposition  for which theformula  (i.e. ) is satisfied. A B A⇒BXA∧X→B A∧(A⇒B)→B DEFINITION: For any objects  and  the exponential object (called also internalhomomorphism object) denoted  is object  such that:A B A⇒B X
- **Definition-5.62** (`[p. 200]` · *A B A⇒BXA∧X→B A∧(A⇒B)→B*): For any objects  and  the exponential object (called also internalhomomorphism object) denoted  is object  such that:A B A⇒B X
- **Definition-5.63** (`[p. 202]` · *Visual Definition 63*): An order that has joins/meets, greatest/least objects and a implicationobject is called a Heyting algebra. DEFINITION: The logical system of intuitionistic logic can be seen as a Heytingalgebra—the “and” and “or” operations are the joins/meets, the values“True” and “False” are the greatest and least objects and theimplication operation is the exponential obj
- **Definition-5.64** (`[p. 202]` · *Visual Definition 64*): The logical system of intuitionistic logic can be seen as a Heytingalgebra—the “and” and “or” operations are the joins/meets, the values“True” and “False” are the greatest and least objects and theimplication operation is the exponential object. DEFINITION:
- **Definition-5.65** (`[p. 202]` · *Visual Definition 65*): As we said, the “logical” orders (those who account for all those conditions)have special names. They are called Heyting algebras.
And then we say…
Formal definition for categories
We phrased the above definition in terms of thin categories (orders), but if weadjust the terminology, they will also b
- **Theorem-5.26** (`[p. 203]` · *Visual Theorem 26*): The logical system of intuitionistic logic can be seen as a BicartesianClosed Category—the “and” and “or” operations are theproduct/coproducts, the values “True” and “False” are theinitial/terminal objects and the implication operation is the exponentialobject. A¬A A∨¬A=1 A∧¬A=0 ⊤
- **Theorem-5.27** (`[p. 204]` · *A∨⊤≅⊤*): For any object  or True is true, i.e. .A A∨⊤=⊤
- **Task-5.36** (`[p. 205]` · *Interactive Task 7 (And then)*): Think of the dual situation, with False. What does it imply, logically? If A implies B, A or B is equal to B Let’s try something else, take two objects  and  such that there is anarrow between them  and find their join. When we are looking for the join of two object, we are looking for the leastupper bound i.e. the lowest object that is equal or bigger than 
- **Theorem-5.28** (`[p. 206]` · *Visual Theorem 28*): For any objects  and , if  implies  ( ), then  or  is ( ).A B A BA→B A BBA∨B=B ⊤ ⊤A A→⊤ A⇒B⇒ A⇒B A→BA B A B A⇒BA⇒A XA∧X→BX(A∧A⇒A)→A True
- **Theorem-5.29** (`[p. 207]` · *This is again a well-known result in logic:*): For any ,  is always true, i.e. everything implies itself(everything follows from itself).AA→A A B A⊨BA B AB A∧X→B XA B A→B⊤
- **Theorem-5.30** (`[p. 208]` · *Visual Theorem 30*): (sometimes called deduction theorem)  implies  in any model, then (), then the statement  will always be true.A BA⊨B (A⇒B) A∧BA∨B A B
