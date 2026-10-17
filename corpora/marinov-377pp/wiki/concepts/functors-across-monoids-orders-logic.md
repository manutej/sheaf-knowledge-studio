# Functors Across Worlds: Monoid Homomorphisms & Monotone Maps (`U_20`)

- **Chapter:** 7 (`§7.2`)
- **Page Fiber:** `pp. 296–305`
- **Layer:** Functorial Bridges

## Summary

Instantiating the functor laws across Chapters 1–5: functors between one-object categories BM → BN are monoid homomorphisms f(x ⋆ y) = f(x) · f(y); functors between thin poset categories are monotone functions a ≤ b ⇒ F(a) ≤ F(b); forgetful functors strip structure.

## Formal Categorical Core

$$\mathbf{Cat}(\mathbf{B}M, \mathbf{B}N) = \mathbf{Mon}(M, N), \quad \mathbf{Cat}((P, \le), (Q, \le)) = \mathbf{Poset}(P, Q)$$

## Local Olog (`types` & `aspects`)

- **Type `genFunctor`:** General Categorical Functor F : C → D
- **Type `monHom`:** Monoid Homomorphism f : M → N
- **Type `monoMap`:** Monotone Order-Preserving Map P → Q
- **Aspect:** `genFunctor` —*specializes on 1-object categories to*→ `monHom`
- **Aspect:** `genFunctor` —*specializes on thin categories to*→ `monoMap`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-42` → [programming-endofunctors-pointed-contravariant](programming-endofunctors-pointed-contravariant.md):** Free monoid List A and option Maybe A act as covariant endofunctors via .map (`$\rho_{42}: \mathrm{List}(f) = \mathrm{map}(f)$`)
- **Incoming `rho-38` ← [functors-structure-preserving-maps](functors-structure-preserving-maps.md):** Specializing F : C → D to 1-object categories (monoids) and thin categories (posets) (`$\rho_{38}: F \mapsto (f_{\mathrm{mon}}, f_{\mathrm{poset}})$`)
- **Incoming `rho-39` ← [monoids-as-single-object-categories-free-monoids](monoids-as-single-object-categories-free-monoids.md):** Functors BM → BN are exact monoid homomorphisms M → N (`$\rho_{39}: \mathrm{Fun}(\mathbf{B}M, \mathbf{B}N) \cong \mathrm{Hom}_{\mathbf{Mon}}(M, N)$`)
- **Incoming `rho-40` ← [preorders-equivalence-and-thin-categories](preorders-equivalence-and-thin-categories.md):** Functors between thin categories are monotone order-preserving maps (`$\rho_{40}: \mathrm{Fun}(P, Q) \cong \mathrm{Monotone}(P, Q)$`)

## Extracted Definitions, Theorems & Tasks (10)

- **Definition-7.144** (`[p. 297]` · *Visual Definition 144*): Group homomorphism (or monoid homomorphism when we are talkingabout monoids) is a function  between the groups’/monoids’underlying sets that preserves the group operation i.e. (where  and  are the group’s operators). F F(a∗b)=F(a)+F(b) + ∗ n
- **Theorem-7.36** (`[p. 298]` · *mod2 mod11*): equation means modular addition). Because this equation holds, the  functionis a group homomorphism between the group of integers under addition and thegroup of modulo arithmetic with base 11 under modular addition (where you canreplace 11 with any other number).
The groups don’t have to be so simil
- **Task-7.55** (`[p. 299]` · *Interactive Task 3 (Categorical isomorphisms)*): Prove that the first functor law (preservation of identities) of groupscan be proven from the second law. Note that this is valid for groups, but not When we view groups/monoid as one-object categories, a group/monoidhomomorphism is just a functor between these categories. 1 23 +1+2+3 F(a+b)=F(a)×F(b)F(g∙f)=F(g)∙F(f)
- **Definition-7.145** (`[p. 300]` · *Visual Definition 145*): A monotonic function is a function between two orders that *preservesthe order of the objects in the source order, in the target order. So, afunction  is monotonic when for every  and  in the source order, if then .F a ba≤b F(a)≤F(b)
- **Task-7.56** (`[p. 302]` · *Interactive Task 4 (Categorical isomorphisms)*): Show why the law holds. Linear functions OK, enough with this abstract nonsense, let’s talk about “normal” functions —ones between numbers. In calculus, there is this concept of linear functions (also called “degree onepolynomials”):
- **Definition-7.146** (`[p. 302]` · *F(g∘f)=F(g)∘F(f)F*): Linear functions are functions of the form  that contain nooperations other than multiplying the argument by some constant(designated as  in the example). f(x)=xa a
- **Task-7.57** (`[p. 303]` · *Interactive Task 5 (Categorical isomorphisms)*): Why are the graphs of linear functions comprised of straight lines? Another interesting property of these functions is that most of them preserveaddition, that is for any  and , you have . Wealready know that this equation is equivalent to the second functor law. So: As we will see later, they are example of functors in the *category of vectorspaces. x y f(x
- **Theorem-7.37** (`[p. 303]` · *x y f(x)+f(y)=f(x+y)*): Linear functions are just functors between the monoid of naturalnumbers under addition and itself.
- **Task-7.58** (`[p. 304]` · *Interactive Task 6 (Categorical isomorphisms)*): Show that linear functions preserve addition. And if we view that natural numbers as an order, linear functions are alsofunctors as well, as all functions that are plotted with straight lines areobviously monotonic. Note, however, that not all functions that are plotted straight lines preserveaddition — functions of the form  in which  is non-zero, arealso s
- **Definition-7.147** (`[p. 305]` · *f(x)+b+f(y)+b=f(x+y)+b*): A functor between two categories of types (let’s call them A and B)consists of a mapping that maps each object type in A to a type in Band a mapping that maps each morphism function between types in Ato a function between types in B, in a way that preserves thestructure of the category type system.
