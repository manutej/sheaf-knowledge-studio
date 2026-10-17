# Type Theory, Russell's Paradox & Formation / Intro / Elim Rules (`U_16`)

- **Chapter:** 6 (`§6.1`)
- **Page Fiber:** `pp. 212–239`
- **Layer:** Type Systems & Computation

## Summary

How Bertrand Russell resolved naive set-theoretic self-reference via stratified Types; defining types constructively through Type Formation, Term Introduction (constructors), Term Elimination (pattern matching), and Computation (β/η reduction), illustrated with Bool, Unit, Void, and Maybe.

## Formal Categorical Core

$$\frac{\Gamma \vdash x : A}{\Gamma \vdash \mathrm{Just}(x) : \mathrm{Maybe}\;A} \;(\text{Intro}), \quad \mathrm{maybe} : b \to (a \to b) \to \mathrm{Maybe}\;a \to b \;(\text{Elim})$$

## Local Olog (`types` & `aspects`)

- **Type `formRule`:** Type Formation Rule (Signature)
- **Type `introRule`:** Term Introduction (Arrows Into Type)
- **Type `elimRule`:** Term Elimination (Universal Arrow Out)
- **Type `compRule`:** Computation Rule (Commuting Diagram β/η)
- **Aspect:** `introRule` —*constructs canonical inhabitants of*→ `formRule`
- **Aspect:** `formRule` —*eliminates via universal property*→ `elimRule`
- **Aspect:** `compRule` —*assertsElim ∘ Intro commutes in*→ `elimRule`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-31` → [inductive-types-nat-list-and-church-encodings](inductive-types-nat-list-and-church-encodings.md):** Extending Formation/Intro/Elim to recursive inductive types Nat and List A (`$\rho_{31}: \mathrm{Maybe}\;A \mapsto \mathrm{List}\;A = \mu X.\; 1 + A \times X$`)
- **Outgoing `rho-36` → [simply-typed-lambda-calculus-curry-howard-lambek](simply-typed-lambda-calculus-curry-howard-lambek.md):** Typing rules (Var, Abs, App) generate the syntactic category of STLC (`$\rho_{36}: (\Gamma \vdash t : B) \in \mathrm{Hom}_{\mathbf{Syn}}(\Gamma, B)$`)
- **Incoming `rho-29` ← [sets-subsets-empty-singleton](sets-subsets-empty-singleton.md):** Stratifying naive sets into Types to resolve Russell's paradox and type-check functions (`$\rho_{29}: x \in A \mapsto \Gamma \vdash x : A$`)
- **Incoming `rho-30` ← [categorical-duality-and-coproducts](categorical-duality-and-coproducts.md):** Type Introduction rules (arrows in) and Elimination rules (universal arrows out) (`$\rho_{30}: (\iota, [f,g]) \mapsto (\text{Intro}, \text{Elim})$`)

## Extracted Definitions, Theorems & Tasks (19)

- **Definition-6.66** (`[p. 224]` · *Visual Definition 66*): A type is something that can be the source and/or target of an arrow.
- **Definition-6.67** (`[p. 227]` · *In summary*): A type is defined by defining these three arrows: 1. One type-level arrow (type formation).2. At least one value-level arrow for which the type is the target(term introduction).3. At least one value-level arrow for which it is the source (termelimination).
- **Definition-6.68** (`[p. 229]` · *Unit*): The  type ( ) is the type with one value.Unit 1 DEFINITION: For any types  and , there is a type , called the Lambdatype of  and , which has all arrows that connect  and  asvalues. A B A→BA B A B
- **Definition-6.69** (`[p. 229]` · *The  type ( ) is the type with one value.Unit 1*): For any types  and , there is a type , called the Lambdatype of  and , which has all arrows that connect  and  asvalues. A B A→BA B A B
- **Definition-6.70** (`[p. 230]` · *Visual Definition 70*): Bool: TypeTrue: BoolFalse: Bool Bool:Type True:Bool True Unit
- **Definition-6.71** (`[p. 231]` · *ifElse*): And  creates another such value.
Et voila, we have just defined a type!
Term elimination
Wait, scratch that. We actually haven’t defined a type. Or rather we havedefined one, but it is quite useless. For it would only be useful once we defineat least one arrow, coming from it (otherwise, it will jus
- **Definition-6.72** (`[p. 232]` · *ifElse:∀a. Bool→a→a→aifElse True a b = aifElse False a b = b*): BobbysBool: TypeBobbysTrue: BobbysBoolBobbysFalse: BobbysBool DEFINITION: convert BobbysBool→Boolconvert BobbysTrue = Trueconvert BobbysFalse = False
- **Definition-6.73** (`[p. 232]` · *BobbysBool: TypeBobbysTrue: BobbysBoolBobbysFalse: BobbysBool*): convert BobbysBool→Boolconvert BobbysTrue = Trueconvert BobbysFalse = False
- **Definition-6.74** (`[p. 233]` · *Visual Definition 74*): Ball: TypeOrangeBall: BallRedBall: BallYellowBall: Ball MaybeOption Just[a]Nothing Maybe
- **Definition-6.75** (`[p. 234]` · *Visual Definition 75*): Maybe: Type→TypeNothing: ∀a. Maybe[a]Just: ∀a. a→Maybe[a] Maybe Bool BoolMaybe DEFINITION: Maybe: Type→Type
- **Definition-6.76** (`[p. 234]` · *Maybe Bool BoolMaybe*): Maybe: Type→Type Maybe Maybe Maybe Type→Type Bool Type Bool
- **Definition-6.77** (`[p. 234]` · *Bool*): Type formation
looks a lot like , but, unlike ,  is a polymorphic type,as we can tell by looking at the type formation rule
Maybe is polymorphic i.e. there is not just one , but many ’s —one for each type a . Polymorphic types are arrows from the universe of types,to itself.
This is why the kind of 
- **Definition-6.78** (`[p. 235]` · *Bool Maybe[Bool]*): Nothing: ∀a. Maybe[a] a Bool DEFINITION: Nothing: Maybe[Bool]
- **Definition-6.79** (`[p. 235]` · *a Bool*): Nothing: Maybe[Bool] Nothing Maybe∀
- **Definition-6.80** (`[p. 236]` · *Maybe*): Just: ∀a. a→Maybe[a] DEFINITION: Just: Bool→Maybe[Bool] Just a Maybe[a]Boolean Maybe[Boolean]
- **Definition-6.81** (`[p. 236]` · *Just: ∀a. a→Maybe[a]*): Just: Bool→Maybe[Bool] Just a Maybe[a]Boolean Maybe[Boolean]
- **Definition-6.82** (`[p. 238]` · *Visual Definition 82*): maybe:∀ a b. b →(a→b)→Maybe[a]→bmaybe n f Nothing = nmaybe n f Just[x] = f x Maybe[a] ba→b b
- **Definition-6.83** (`[p. 239]` · *0n n+1*): N: TypeZero: NSucc: N→N DEFINITION: N: Type
- **Definition-6.84** (`[p. 239]` · *N: TypeZero: NSucc: N→N*): N: Type
