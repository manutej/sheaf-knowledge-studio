# Functor Categories [C, D], Vertical/Horizontal Composition & 2-Categories (`U_24`)

- **Chapter:** 8 (`§8.3`)
- **Page Fiber:** `pp. 360–377`
- **Layer:** Higher 2-Categorical Synthesis

## Summary

Composing natural transformations vertically (β ∘ α : F ⇒ H) to form the Functor Category [C, D] and horizontally (β * α) across composable functors; assembling 0-cells (Categories), 1-cells (Functors), and 2-cells (Natural Transformations) into the 2-Category Cat.

## Formal Categorical Core

$$(\beta \circ \alpha)_A = \beta_A \circ \alpha_A, \quad (\beta * \alpha)_A = \beta_{G(A)} \circ F'(\alpha_A) = G'(\alpha_A) \circ \beta_{F(A)} \quad \text{(Interchange Law)}$$

## Local Olog (`types` & `aspects`)

- **Type `funCat`:** Functor Category [C, D] = D^C
- **Type `vertHoriz`:** Vertical (β ∘ α) & Horizontal (β * α) Composition
- **Type `twoCat`:** Strict 2-Category Cat (0-cells, 1-cells, 2-cells)
- **Aspect:** `vertHoriz` —*equips functors with morphism composition in*→ `funCat`
- **Aspect:** `funCat` —*serves as the hom-categories of*→ `twoCat`

## Restriction Morphisms (`1-Simplices`)

- **Incoming `rho-48` ← [natural-transformations-and-naturality-squares](natural-transformations-and-naturality-squares.md):** Composing natural transformations vertically and horizontally inside the 2-category Cat (`$\rho_{48}: (\mathcal{C}, F, \alpha) \in \mathbf{2Cat}$`)
- **Incoming `rho-49` ← [polymorphic-functions-and-categorical-equivalence](polymorphic-functions-and-categorical-equivalence.md):** Categorical equivalence C ≃ D is defined by natural isomorphisms η : Id ≅ GF, ε : FG ≅ Id in Cat (`$\rho_{49}: (\mathcal{C} \simeq \mathcal{D}) \in \mathbf{Cat}_2$`)
- **Incoming `rho-50` ← [functors-structure-preserving-maps](functors-structure-preserving-maps.md):** Functors C → D become the objects of the functor category [C, D] (`$\rho_{50}: \mathrm{Ob}([\mathcal{C}, \mathcal{D}]) = \mathrm{Fun}(\mathcal{C}, \mathcal{D})$`)

## Extracted Definitions, Theorems & Tasks (15)

- **Definition-8.163** (`[p. 360]` · *Visual Definition 163*): For each functor, we have the identity natural transformation (actuallya natural isomorphism) between it and itself. CD E C DD E C→E
- **Task-8.76** (`[p. 363]` · *Interactive Task 6 (Furthermore, this connection is two-way:)*): Show that natural transformations indeed compose i.e. that if you havenatural transformations  and  you have. Whiskering And an interesting special case of horizontal composition is horizontalcomposition involving the identity natural transformation: given a naturaltransformation  involving functors with signature  and some functorwith signature , we can tak
- **Task-8.77** (`[p. 363]` · *Interactive Task 7 (Furthermore, this connection is two-way:)*): Try to extend the natural transformation in the other direction (bytaking  to be identity). So, this is how you compose natural transformations. It’s too bad that this isform of composition is different from the standard categorical composition. So,I guess natural transformations do not form a category, like we hoped theywould… Well, OK, there is actually an
- **Task-8.78** (`[p. 365]` · *Interactive Task 8 (Furthermore, this connection is two-way:)*): identify the function, the three functors, and the two naturaltransformations used in this diagram. Then, we quickly passed to normal external diagrams, where objects are pointsand categories are collections. And now we go one more level further, and show the category of categories,where categories are points and functors are morphisms.
- **Definition-8.164** (`[p. 366]` · *And you can already see the new category that is formed:*): For each two categories  and , there exists a category which hasthe  functors as objects and the natural transformationsbetween those functors as morphisms. C DC→D
- **Task-8.79** (`[p. 368]` · *Interactive Task 9 (Furthermore, this connection is two-way:)*): Draw the paths of the two compositions of the transformations (on thetwo sides of the equation) and ensure that they indeed lead to the same place.
- **Task-8.80** (`[p. 369]` · *Interactive Task 1 (Furthermore, this connection is two-way:)*): Check if that definition is valid. The definition in question is: Two categories  and  are isomorphic (or ) if there existfunctors  and its reverse , such that and . We can check it by expanding the definition of a functor.
- **Task-8.81** (`[p. 370]` · *Interactive Task 2 (Furthermore, this connection is two-way:)*): When exactly would the mapping encompass all objects? As we say above: mapping the two functors’ object components involves nothing morethan specifying a bunch of morphisms in the target category: onemorphism for each object in the source category i.e. each object fromthe image of the first functor, should have one arrow coming from it. So the mapping encomp
- **Task-8.82** (`[p. 370]` · *Interactive Task 3 (Furthermore, this connection is two-way:)*): Draw example naturality squares of the  naturaltransformation. To draw a square of the  natural transformation,we must first: 1. Pick a function,  say .2. Lift it with the functor e.g  adds oneto every number from the list. Then we:
- **Task-8.83** (`[p. 370]` · *Interactive Task 4 (Furthermore, this connection is two-way:)*): Prove the above results, using the formula of the naturality condition. A B A≅Bf:A→B g:B→A f∘g=IDAg∘f=IDA reverse reverse:List a→List a
- **Task-8.84** (`[p. 371]` · *Interactive Task 5 (We want to prove that:)*): Show that the two definitions [of natural transformation] areequivalent. This entails extracting a natural transformation from a functor ,and the other way around. Here,we will describe one direction of this process: As we said, we can split the category  into two subcategories (let’s call
- **Task-8.85** (`[p. 372]` · *Interactive Task 6 (We want to prove that:)*): Show that natural transformations indeed compose i.e. that if you havenatural transformations  and  you have. To show that two transformations compose, we need to find a way, given twonatural transformations with the above signatures, to construct a new one. To do that, we remember that a natural transformation is just a family ofmorphisms, one for each obje
- **Task-8.86** (`[p. 373]` · *Interactive Task 7 (We want to prove that:)*): Try to extend the natural transformation in the other direction (bytaking  to be identity). It works basically the same way and the result is also the same — you get anew natural transformation with a different signature. Task 8: identify the function, the three functors, and the two naturaltransformations used in this diagram. First the functors:  and  are 
- **Task-8.87** (`[p. 373]` · *Interactive Task 8 (We want to prove that:)*): identify the function, the three functors, and the two naturaltransformations used in this diagram. First the functors:  and  are the  functor,  is the  functor. ¯α F G List H ID
- **Task-8.88** (`[p. 374]` · *Interactive Task 9 (We want to prove that:)*): Draw the paths of the two compositions of the transformations (on thetwo sides of the equation) and ensure that they indeed lead to the same place. One option is this: Buy full version Ko-fi
