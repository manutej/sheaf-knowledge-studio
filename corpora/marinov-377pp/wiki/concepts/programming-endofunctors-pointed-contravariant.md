# Programming Endofunctors (List, Maybe, .map), Pointed & Contravariant Functors (`U_21`)

- **Chapter:** 7 (`§7.3`)
- **Page Fiber:** `pp. 306–318`
- **Layer:** Functorial Bridges

## Summary

Functors in software engineering: generic type constructors F<A> equipped with map / fmap lifting functions (A → B) to (F<A> → F<B>); pointed functors (unit/pure : A → F<A>); contravariant functors F : C^op → D reversing arrow direction (predicates, serializers, Hom(-, R)).

## Formal Categorical Core

$$\mathrm{map} : (A \to B) \to (F\;A \to F\;B), \quad F^{\mathrm{op}} : \mathcal{C}^{\mathrm{op}} \to \mathcal{D}, \quad F(g \circ f) = F(f) \circ F(g)$$

## Local Olog (`types` & `aspects`)

- **Type `typeCat`:** Category of Types & Pure Functions
- **Type `endoF`:** Endofunctor Container F (List, Maybe, Promise)
- **Type `contraF`:** Contravariant Functor C^op → Type
- **Aspect:** `endoF` —*lifts functionscovariant via .map in*→ `typeCat`
- **Aspect:** `contraF` —*reverses morphism direction in*→ `typeCat`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-45` → [natural-transformations-and-naturality-squares](natural-transformations-and-naturality-squares.md):** Transforming container endofunctors F A → G A while commuting with .map(f) (`$\rho_{45}: \mathrm{map}_G(f) \circ \alpha_A = \alpha_B \circ \mathrm{map}_F(f)$`)
- **Outgoing `rho-47` → [polymorphic-functions-and-categorical-equivalence](polymorphic-functions-and-categorical-equivalence.md):** Polymorphic List/Maybe operations (reverse, safeHead) commute with map(f) (`$\rho_{47}: \mathrm{reverse} \circ \mathrm{map}(f) = \mathrm{map}(f) \circ \mathrm{reverse}$`)
- **Incoming `rho-41` ← [functors-structure-preserving-maps](functors-structure-preserving-maps.md):** Endofunctors F : Type → Type on the category of programming types (`$\rho_{41}: F : \mathbf{Type} \to \mathbf{Type}$`)
- **Incoming `rho-42` ← [functors-across-monoids-orders-logic](functors-across-monoids-orders-logic.md):** Free monoid List A and option Maybe A act as covariant endofunctors via .map (`$\rho_{42}: \mathrm{List}(f) = \mathrm{map}(f)$`)
- **Incoming `rho-43` ← [simply-typed-lambda-calculus-curry-howard-lambek](simply-typed-lambda-calculus-curry-howard-lambek.md):** Type constructors F : Type → Type and higher-order map in STLC/System F (`$\rho_{43}: \Gamma \vdash \mathrm{map}_F : (A \to B) \to F A \to F B$`)

## Extracted Definitions, Theorems & Tasks (15)

- **Task-7.59** (`[p. 308]` · *Interactive Task 7 (Identity law:)*): Use examples to convince yourself that the laws are followed. What are functors for Now, that we have seen so many examples of functors, we finally can attemptto answer the million-dollar question, namely what are functors for and whyare they useful? (often formulated also as “Why are you wasting your/my timewith this (abstract) nonsense?”) Well, we saw that
- **Definition-7.148** (`[p. 310]` · *Visual Definition 148*): Endofunctors are functors that have one and the same category assource and target.
- **Definition-7.149** (`[p. 311]` · *Visual Definition 149*): The identity functor, together with all other functors to which theidentity functor can be naturally transformed are called pointedfunctors (i.e. a functor is pointed if there exist a naturaltransformation from the identity functor to it). a→List a
- **Definition-7.150** (`[p. 312]` · *a→[ a ]*): The category of small categories is a category that has small categories(like  - the category of sets, , the category of monoids, ,the category of orders etc) for objects and functors for morphismsSet Mon Ord
- **Task-7.60** (`[p. 313]` · *Interactive Task 8 (Pointed functors)*): Go through the functor definition and see how do functors compose. Task 9: What are the initial and terminal object of the category of smallcategories. Categories all the way down The recursive nature of category theory might sometimes leave us confused: westarted by saying that categories are composed of objects and morphisms, butnow we are saying that ther
- **Task-7.61** (`[p. 313]` · *Interactive Task 9 (Pointed functors)*): What are the initial and terminal object of the category of smallcategories. Categories all the way down The recursive nature of category theory might sometimes leave us confused: westarted by saying that categories are composed of objects and morphisms, butnow we are saying that there are morphisms between categories (functors).And on top of that, there is 
- **Task-7.62** (`[p. 314]` · *Interactive Task 1 (Pointed functors)*): There are just two more categories that have 2 objects and at most onemorphism between two objects, draw them. The answer is this: Isomorphism means equality in category theory, so flipping the arrow from theleft to the right doesn’t count as a new category. For the third category we have to specify what composing the morphism withitself would yield:
- **Task-7.63** (`[p. 314]` · *Interactive Task 2 (Pointed functors)*): What is the morphism mapping for orders? The morphism mapping of orders consist just of mapping the only existingmorphism between a given pair of objects in one order, to the only existingmorphism of their counterparts in the other order. The “order-preserving”
- **Task-7.64** (`[p. 315]` · *Interactive Task 3 (Pointed functors)*): Prove that the first functor law (preservation of identities) of groupscan be proven from the second law i.e. that if  and  are groups and — a group homomorphism, you have . Note thatthis is valid for groups, but not monoids. We know that So (second functor law)
- **Task-7.65** (`[p. 315]` · *Interactive Task 4 (Pointed functors)*): Show why the law holds. In categorical language, the problem states that if we have  and, then . The proof uses the same approach as the one in Task 2: because in orders therecan be just one morphism with a given type signature, two morphisms withequal type signatures must be equal to one another. Then, if we compose those two morphisms in the target order (
- **Task-7.66** (`[p. 316]` · *Interactive Task 5 (Pointed functors)*): Why are the graphs of linear functions comprised of straight lines? A linear function grows with a constant rate, (i.e. their derivative is alwaysconstant). The slope of a function reflects the change in its rate of growth, so in case oflinear functions it is a straight line. Task 6: Show that linear functions preserve addition.
- **Task-7.67** (`[p. 316]` · *Interactive Task 6 (Pointed functors)*): Show that linear functions preserve addition. Let’s say we have a function , such that it multiplies the number by a certainconstant , e.g. we have and If we sum the two we get
- **Task-7.68** (`[p. 317]` · *Interactive Task 7 (Pointed functors)*): Use examples to convince yourself that the laws are followed. The point here is playing a bit to familiarize yourself with the laws, you canuse any set and functions, here is an example: Identity law: [1, 2, 3].map(a => a) == [1, 2, 3]
- **Task-7.69** (`[p. 317]` · *Interactive Task 8 (Pointed functors)*): Go through the functor definition and see how do functors compose. Another trivial exercise, with, perhaps, non-trivial setup. It all comes down togo through the elements a functor consists of and to see how the elements oftwo functors can compose. The two elements of a functor are the object mapping and the morphismmapping. The object mapping is just a func
- **Task-7.70** (`[p. 318]` · *Interactive Task 9 (Pointed functors)*): What are the initial and terminal object of the category of smallcategories. If you remember the concepts of initial and terminal objects from the categoryof sets , you will find out that they are basically the same for the categoryof categories The initial object in  is the empty set, the initial category in  is theempty category. The unique functor from th
