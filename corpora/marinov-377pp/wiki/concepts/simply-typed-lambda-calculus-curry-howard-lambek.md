# Simply Typed Lambda Calculus (STLC) & Curry-Howard-Lambek Rosetta Stone (`U_18`)

- **Chapter:** 6 (`§6.3`)
- **Page Fiber:** `pp. 260–277`
- **Layer:** Type Systems & Computation

## Summary

Sequent contexts Γ ⊢ t : A, lambda abstraction (λx. t) as currying, application as evaluation, and Joachim Lambek's three-way equivalence between Intuitionistic Logic, Simply Typed Lambda Calculus, and Cartesian Closed Categories.

## Formal Categorical Core

$$\frac{\Gamma, x : A \vdash t : B}{\Gamma \vdash (\lambda x.\; t) : A \to B} \;(\to\text{-Intro}) \;\Longleftrightarrow\; \mathrm{Hom}(\Gamma \times A, B) \cong \mathrm{Hom}(\Gamma, B^A)$$

## Local Olog (`types` & `aspects`)

- **Type `stlc`:** Simply Typed Lambda Calculus (Γ ⊢ t : B)
- **Type `ccc`:** Cartesian Closed Category (1, ×, B^A)
- **Type `intLogic`:** Intuitionistic Natural Deduction
- **Aspect:** `stlc` —*compiles terms into morphisms of*→ `ccc`
- **Aspect:** `stlc` —*is isomorphic under Curry-Howard to*→ `intLogic`

## Restriction Morphisms (`1-Simplices`)

- **Outgoing `rho-43` → [programming-endofunctors-pointed-contravariant](programming-endofunctors-pointed-contravariant.md):** Type constructors F : Type → Type and higher-order map in STLC/System F (`$\rho_{43}: \Gamma \vdash \mathrm{map}_F : (A \to B) \to F A \to F B$`)
- **Incoming `rho-33` ← [inductive-types-nat-list-and-church-encodings](inductive-types-nat-list-and-church-encodings.md):** Encoding inductive ADTs inside Simply Typed / Polymorphic Lambda Calculus (`$\rho_{33}: \mathrm{ADT} \hookrightarrow \lambda^{\to,\forall}$`)
- **Incoming `rho-34` ← [implication-currying-and-intuitionistic-bhk](implication-currying-and-intuitionistic-bhk.md):** BHK constructive proofs of P ⇒ Q are lambda terms λx:P. t : P → Q (`$\rho_{34}: (P \Rightarrow Q) \cong (\lambda x:P.\; t : Q)$`)
- **Incoming `rho-35` ← [heyting-and-boolean-algebras-bicartesian-closed](heyting-and-boolean-algebras-bicartesian-closed.md):** Dropping thinness turns a Heyting algebra into a full Bicartesian Closed Category (STLC) (`$\rho_{35}: \mathbf{HeytingAlg} \leadsto \mathbf{CCC} \simeq \mathbf{STLC}$`)
- **Incoming `rho-36` ← [type-theory-russell-and-formation-intro-elim](type-theory-russell-and-formation-intro-elim.md):** Typing rules (Var, Abs, App) generate the syntactic category of STLC (`$\rho_{36}: (\Gamma \vdash t : B) \in \mathrm{Hom}_{\mathbf{Syn}}(\Gamma, B)$`)

## Extracted Definitions, Theorems & Tasks (36)

- **Definition-6.112** (`[p. 260]` · *We start with the type formation rule (or the kinding rule).*): Γ⊢True:Bool True Bool DEFINITION: Γ⊢False:Bool
- **Definition-6.113** (`[p. 260]` · *True Bool*): Γ⊢False:Bool False Bool x Ax A DEFINITION:
- **Definition-6.114** (`[p. 260]` · *x Ax A*): Variable typing rule (Var) x:A∈ΓΓ⊢x:A DEFINITION: Lambda type formation rule
- **Definition-6.115** (`[p. 260]` · *x:A∈ΓΓ⊢x:A*): Lambda type formation rule Γ⊢A::Type,Γ⊢B::TypeΓ⊢A→B::Type
- **Definition-6.116** (`[p. 261]` · *Simply-typed Lambda Calculus*): Lambda term introduction rule (Abs) Γ,x:A⊢y:BΓ⊢λz:A→B x A y BA→B DEFINITION:
- **Definition-6.117** (`[p. 261]` · *x A y BA→B*): Lambda term elimination rule (App) Γ⊢z:A→B,Γ⊢x:AΓ⊢zx:B length:string→int DEFINITION:
- **Definition-6.118** (`[p. 261]` · *length:string→int*): Term introduction of “length” Γ,x:string⊢y:intΓ⊢λlength:string→int THEOREM: Term application of “length”
- **Theorem-6.31** (`[p. 261]` · *Γ,x:string⊢y:intΓ⊢λlength:string→int*): Term application of “length” Γ⊢length:string→int,Γ⊢x:stringΓ⊢length x:int
- **Definition-6.119** (`[p. 262]` · *And one for*): The simply-typed Lambda Calculus (STLC) is the type system whichonly has one type constructor — function (lambda), with typing rulesAbs and App (for term introduction and elimination). It also has theVar typing rule. Maybe DEFINITION: Maybe: Type→TypeNothing: ∀a. Maybe[a]Just: ∀a. a→Maybe[a]
- **Definition-6.120** (`[p. 262]` · *Maybe*): Maybe: Type→TypeNothing: ∀a. Maybe[a]Just: ∀a. a→Maybe[a] int DEFINITION: MaybeInt: TypeNoInt: MaybeIntJustInt:int→MaybeInt
- **Definition-6.121** (`[p. 262]` · *int*): MaybeInt: TypeNoInt: MaybeIntJustInt:int→MaybeInt string DEFINITION: MaybeString: TypeNoString: MaybeStringJustString:string→MaybeString
- **Definition-6.122** (`[p. 262]` · *string*): MaybeString: TypeNoString: MaybeStringJustString:string→MaybeString
- **Definition-6.123** (`[p. 263]` · *Type ∗*): Kinding rule in STLC Γ⊢Type Type THEOREM:
- **Theorem-6.32** (`[p. 263]` · *Type*): Γ⊢Bool::Type
- **Definition-6.124** (`[p. 264]` · *Visual Definition 124*): Variable typing rule (Var) x:A∈ΓΓ⊢x:A DEFINITION: Type Variable kinding rule (TVar)
- **Definition-6.125** (`[p. 264]` · *x:A∈ΓΓ⊢x:A*): Type Variable kinding rule (TVar) A::K∈ΓΓ⊢A::K DEFINITION: Lambda type formation rule
- **Definition-6.126** (`[p. 264]` · *A::K∈ΓΓ⊢A::K*): Lambda type formation rule Γ⊢A::Type,Γ⊢B::TypeΓ⊢A→B::Type DEFINITION: Type-level lambda kind formation rule
- **Definition-6.127** (`[p. 264]` · *Γ⊢A::Type,Γ⊢B::TypeΓ⊢A→B::Type*): Type-level lambda kind formation rule ( ) ( )
- **Definition-6.128** (`[p. 265]` · *Maybe*): Type-level lambda type formation rule for Maybe Γ,(α::Type)⊢Maybe[α]::TypeΓ⊢∀(α::Type).Maybe[α]::Type MaybeString DEFINITION:
- **Definition-6.129** (`[p. 265]` · *MaybeString*): A monomorphic function z::string→MaybeString String DEFINITION:
- **Definition-6.130** (`[p. 265]` · *String*): A polymorphic function, using TAbs z′::∀α.α→Maybe α String
- **Definition-6.131** (`[p. 266]` · *Visual Definition 131*): A monomorphic function, using TApp z=z′[String] DEFINITION: Type abstraction (or TAbs)
- **Definition-6.132** (`[p. 266]` · *z=z′[String]*): Type abstraction (or TAbs) Γ,(α::A)⊢z:CΓ⊢(Λα::A.z):∀(α::A).C DEFINITION: Type application (TApp)
- **Definition-6.133** (`[p. 266]` · *Γ,(α::A)⊢z:CΓ⊢(Λα::A.z):∀(α::A).C*): Type application (TApp) Γ⊢z′:∀(α::A).C,Γ⊢(X::A)Γ⊢z′[X]:C[α:=X] DEFINITION: The polymorphic Lambda Calculus (System F) is the type system whichonly has one type constructor — polymorphic lambda, with typing rulesAbs and App (for introduction and elimination of terms) and kindingrules TAbs and TApp (for introduction and elimination of types). It alsohas the Va
- **Definition-6.134** (`[p. 266]` · *Γ⊢z′:∀(α::A).C,Γ⊢(X::A)Γ⊢z′[X]:C[α:=X]*): The polymorphic Lambda Calculus (System F) is the type system whichonly has one type constructor — polymorphic lambda, with typing rulesAbs and App (for introduction and elimination of terms) and kindingrules TAbs and TApp (for introduction and elimination of types). It alsohas the Var typing rule. and TVar kinding rule.
