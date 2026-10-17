# Inductive Types (Nat, List), Algebraic Data Types & Church Encodings (`U_17`)

- **Chapter:** 6 (`§6.2`)
- **Page Fiber:** `pp. 240–259`
- **Layer:** Type Systems & Computation

## Summary

Recursive inductive types: Natural numbers (Zero : 1 → Nat, Succ : Nat → Nat), Lists (Nil, Cons), Product types (Pair), Sum types (Either), and Alonzo Church's encodings representing data purely by its universal elimination function.

## Formal Categorical Core

$$\mathrm{Nat} \cong \forall a.\; a \to (a \to a) \to a, \quad \mathrm{List}\;A \cong \forall r.\; r \to (A \to r \to r) \to r$$

## Local Olog (`types` & `aspects`)

- **Type `adt`:** Algebraic Data Type (Nat, List A, Either A B)
- **Type `constructors`:** Constructors (Zero/Succ, Nil/Cons)
- **Type `church`:** Polymorphic Church Encoding (Universal Fold)
- **Aspect:** `constructors` —*freely generates terms of*→ `adt`
- **Aspect:** `adt` —*is completely determined by its eliminator*→ `church`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-33` → [simply-typed-lambda-calculus-curry-howard-lambek](simply-typed-lambda-calculus-curry-howard-lambek.md):** Encoding inductive ADTs inside Simply Typed / Polymorphic Lambda Calculus (`$\rho_{33}: \mathrm{ADT} \hookrightarrow \lambda^{\to,\forall}$`)
- **Incoming `rho-31` ← [type-theory-russell-and-formation-intro-elim](type-theory-russell-and-formation-intro-elim.md):** Extending Formation/Intro/Elim to recursive inductive types Nat and List A (`$\rho_{31}: \mathrm{Maybe}\;A \mapsto \mathrm{List}\;A = \mu X.\; 1 + A \times X$`)
- **Incoming `rho-32` ← [monoids-as-single-object-categories-free-monoids](monoids-as-single-object-categories-free-monoids.md):** The inductive type List A (Nil, Cons) is the Free Monoid on type A (`$\rho_{32}: \mathrm{Free}(A) \cong \mathrm{List}\;A$`)

## Extracted Definitions, Theorems & Tasks (35)

- **Definition-6.85** (`[p. 240]` · *It allows us to construct one value, called zero*): Zero: N
- **Definition-6.86** (`[p. 241]` · *0*): Succ: N→N Succ n n+1 Succ Succ
- **Definition-6.87** (`[p. 243]` · *Composite types. The list type.*): foldNat:N→a→(a→a)→afoldNat Zero z s = zfoldNat (Succ a) z s =s (foldNat a z s)
- **Definition-6.88** (`[p. 244]` · *Visual Definition 88*): List: Type→TypeNil: ∀a. List[a]Cons: ∀a. a→List[a]→List[a] List Maybe DEFINITION: List: Type→Type
- **Definition-6.89** (`[p. 244]` · *List Maybe*): List: Type→Type List List[Nat]List[Bool]
- **Definition-6.90** (`[p. 245]` · *Visual Definition 90*): Nil: ∀a. List[a] Nil
- **Definition-6.91** (`[p. 246]` · *ConsCons a*): Cons: ∀a. a→List[a]→List[a] Cons SuccSuccCons Succ X→X XCons a→(X→X)a Cons Nil
- **Task-6.37** (`[p. 248]` · *Interactive Task 1 (Term introduction: Cons)*): There is a certain mapping from  to  which is so useful,that some dialects of Lisp have no  type at all and rely just on thismapping. Draw it. DEFINITION: foldList : (b→a→b)→b→List[a]→bfoldList f zNil=zfoldList f z(Cons x xs)=foldList f (f z x) xs List BooleanBoolean
- **Definition-6.92** (`[p. 248]` · *Visual Definition 92*): foldList : (b→a→b)→b→List[a]→bfoldList f zNil=zfoldList f z(Cons x xs)=foldList f (f z x) xs List BooleanBoolean
- **Task-6.38** (`[p. 249]` · *Interactive Task 2 (Term introduction: Cons)*): Define this mapping (between List and Bool) in Haskell. Define it onceby writing a function from scratch, and twice, with using the foldListfunction. f :: (Bool -> a -> Bool) f = undefinedfoldList f False Task 3: I present to you the type  (where  is the singletontype, (a type with one value). Draw the values of  until you run outof space. ListUnit UnitListU
- **Task-6.39** (`[p. 249]` · *Interactive Task 3 (Term introduction: Cons)*): I present to you the type  (where  is the singletontype, (a type with one value). Draw the values of  until you run outof space. ListUnit UnitListUnit
- **Task-6.40** (`[p. 250]` · *Interactive Task 4 (Term introduction: Cons)*): The  type is actually isomorphic to another type that wereviewed here. Find out which. Positive and negative types.Either and Tuples. Now, we will quickly present two more types, (hm… I have the feeling that Iactually have seen those before). Either
- **Definition-6.93** (`[p. 251]` · *a b Lefta Right b*): Either: Type→Type→TypeLeft: ∀ab. a→Either[a b]Right: ∀ab. b→Either[a b] Tuplea b ab
- **Task-6.41** (`[p. 252]` · *Interactive Task 5 (Term introduction: Cons)*): Write a constructor of Tuple. Write a fold function for Either. Positive and negative types The  type is uniquely defined by its introduction rules i.e. theelimination rules can be derived from the introduction rules. , on the other hand, is defined by its elimination rules i.e. theintroduction rules can be derived from them:
- **Definition-6.94** (`[p. 252]` · *Visual Definition 94*): first : ∀ a b.Tuple[a b]→asecond : ∀ a b.Tuple[a b]→b Either DEFINITION: Left: ∀ab. a→Either[a b]Right: ∀ab. b→Either[a b]
- **Definition-6.95** (`[p. 252]` · *Either*): Left: ∀ab. a→Either[a b]Right: ∀ab. b→Either[a b] Tuple DEFINITION: [ ]
- **Definition-6.96** (`[p. 252]` · *Tuple*): [ ]
- **Task-6.42** (`[p. 253]` · *Interactive Task 6 (Term introduction: Cons)*): Besides , there is one very important negative type, which wecovered in this chapter (and in various other places). Conclusion In this section, we started from almost nothing — just the  type. Then wedefined a lot of stuff, very quickly. first : ∀ a b.Tuple[a b]→asecond : ∀ a b.Tuple[a b]→b
- **Definition-6.97** (`[p. 255]` · *Visual Definition 97*): Bool: TypeTrue: BoolFalse: Bool DEFINITION: type Bool=∀a.a→a→afalse:Boolfalse a b=btrue:Booltrue a b=a Bool ∀a.a→a→aa aTrue a False
- **Definition-6.98** (`[p. 255]` · *Bool: TypeTrue: BoolFalse: Bool*): type Bool=∀a.a→a→afalse:Boolfalse a b=btrue:Booltrue a b=a Bool ∀a.a→a→aa aTrue a False ifElse DEFINITION:
- **Definition-6.99** (`[p. 255]` · *ifElse*): ifElse:∀a.Bool→a→a→aifElse v a b =v a b
- **Definition-6.100** (`[p. 256]` · *Maybe*): Maybe: Type→TypeNothing: ∀a. Maybe[a]Just: ∀a. a→Maybe[a] MaybeJust DEFINITION: type Maybe[a]=∀m.m→(a→m)→mnothing:Maybe[a]nothing n j=njust: a→Maybe[a]just val n j =(j val)
- **Definition-6.101** (`[p. 256]` · *MaybeJust*): type Maybe[a]=∀m.m→(a→m)→mnothing:Maybe[a]nothing n j=njust: a→Maybe[a]just val n j =(j val) Maybe 1
- **Task-6.43** (`[p. 257]` · *Interactive Task 7 (Term introduction: Cons)*): Write a Church-encoded version of the natural numbers type DEFINITION: Nothing: ∀a. Maybe[a] DEFINITION:
- **Definition-6.102** (`[p. 257]` · *Visual Definition 102*): Nothing: ∀a. Maybe[a] DEFINITION: ∀m.m→m 1
