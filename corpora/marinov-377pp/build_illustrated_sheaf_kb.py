#!/usr/bin/env python3
"""
Builds the complete Alexandrov Sheaf Knowledge Base, SQLite FTS5 Index,
Deferred Page Bundle, and Persistent LLM Wiki for:
Boris Marinov (Jencel Panic) — "Category Theory Illustrated" (377 pages).
"""
import json
import pathlib
import re
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
WIKI_DIR = ROOT / "wiki"
RAW_PAGES_JSON = DATA_DIR / "raw_pages_377.json"
PDF_PATH = ROOT / "category-theory-illustrated.pdf"

CHAPTERS = [
    {
        "chapter": 1,
        "id": "ch01-sets-and-functions",
        "title": "Chapter 1: Prologue & Sets — Collections, Functions & Isomorphisms",
        "start_page": 3,
        "end_page": 51,
        "theme": "Abstract theories as languages for defining tools; sets as unstructured collections of colored balls; functions as many-to-one maps; hom-sets, injections, surjections, bijections, isomorphisms, and currying.",
        "global_invariants": [
            "Lawvere Epigraph (p. 3): Visual abstraction as the bridge from internal elements to external relationships.",
            "Empty Set Initiality (p. 22): There is a unique function ! : ∅ → A to any set A.",
            "Singleton Terminality (p. 24): There is a unique function ! : A → 1 from any set A to a singleton set.",
            "Set Isomorphism (p. 48): f : A → B is an isomorphism iff g ∘ f = id_A and f ∘ g = id_B."
        ]
    },
    {
        "chapter": 2,
        "id": "ch02-from-sets-to-categories",
        "title": "Chapter 2: Categories — External Definitions, Products, Coproducts & Duality",
        "start_page": 52,
        "end_page": 94,
        "theme": "Shifting from internal set elements to external point-free arrows; universal products (A × B), categorical duality (reversing arrows), coproducts (A + B), initial/terminal objects, and the formal definition of a category.",
        "global_invariants": [
            "External Point-Free Principle (p. 52, p. 82): Objects are opaque points; all structure is encoded in morphisms and their composition.",
            "Universal Product & Coproduct Duality (p. 69): Reversing all arrows in the Product cone (π₁, π₂, ⟨f,g⟩) yields the Coproduct cocone (ι₁, ι₂, [f,g]).",
            "Category Laws (p. 82, p. 92): Associativity h ∘ (g ∘ f) = (h ∘ g) ∘ f and Identity id_B ∘ f = f = f ∘ id_A."
        ]
    },
    {
        "chapter": 3,
        "id": "ch03-monoids-and-groups",
        "title": "Chapter 3: Monoids & Groups — Single-Object Categories & Symmetries",
        "start_page": 95,
        "end_page": 130,
        "theme": "A monoid as a category with one object where elements become composable arrows; magmas, semigroups, monoids, and groups; rotational symmetries of geometric figures (C₃, D₃); Cayley's theorem and free monoids.",
        "global_invariants": [
            "Delooping / Single-Object Equivalence (p. 115): Every monoid (M, ⋆, e) is canonically a one-object category BM with Hom(•, •) = M.",
            "Group Invertibility (p. 104): A group is a category with one object in which every morphism is an isomorphism (an invertible symmetry).",
            "Universal Property of Free Monoids (p. 129): Lists [A] are the free monoid on A; any map A → M extends uniquely to a monoid homomorphism fold : [A] → M."
        ]
    },
    {
        "chapter": 4,
        "id": "ch04-orders-and-lattices",
        "title": "Chapter 4: Orders & Lattices — Thin Categories, Posets & Birkhoff Duality",
        "start_page": 131,
        "end_page": 161,
        "theme": "Binary relations, preorders, partial orders, and total orders; Hasse diagrams; color-mixing and divisibility posets; Birkhoff's representation theorem; thin categories where |Hom(a,b)| ≤ 1; meets and joins as categorical limits/colimits.",
        "global_invariants": [
            "Thin Category Realization (p. 156): A preorder (P, ≤) is a thin category where Hom(a, b) has one arrow iff a ≤ b and is empty otherwise.",
            "Meets & Joins as Products & Coproducts (p. 145): In a poset category, the categorical product is greatest lower bound (meet a ∧ b) and the coproduct is least upper bound (join a ∨ b).",
            "Antisymmetry as Skeletal Isomorphism (p. 155): In a preorder, a ≅ b iff a ≤ b and b ≤ a (an equivalence relation)."
        ]
    },
    {
        "chapter": 5,
        "id": "ch05-logic-and-proofs",
        "title": "Chapter 5: Logic — Propositions as Objects, Proofs as Morphisms & Heyting Algebras",
        "start_page": 162,
        "end_page": 211,
        "theme": "Categorifying deductive logic: propositions as objects, proofs/entailments P ⊢ Q as morphisms; conjunction (∧) as categorical product, disjunction (∨) as coproduct, implication (P ⇒ Q) as exponential object; classical Boolean vs. intuitionistic BHK Heyting logic.",
        "global_invariants": [
            "Logical Product & Coproduct (p. 165): Conjunction P ∧ Q is the universal product (elimination projections + pairing); Disjunction P ∨ Q is the universal coproduct (introduction injections + case analysis).",
            "Implication Adjunction / Currying (p. 180): R ∧ P ⊢ Q iff R ⊢ (P ⇒ Q), making implication the internal hom / exponential in a Heyting algebra.",
            "Intuitionistic BHK vs. Classical Excluded Middle (p. 184, p. 203): Constructive logic corresponds to bicartesian closed categories (Heyting algebras) where ¬¬P → P is not assumed without a witness."
        ]
    },
    {
        "chapter": 6,
        "id": "ch06-types-and-lambda-calculus",
        "title": "Chapter 6: Types — Curry-Howard-Lambek, ADTs & Simply Typed Lambda Calculus",
        "start_page": 212,
        "end_page": 277,
        "theme": "Russell's paradox and type hierarchy; type formation, introduction, elimination, and computation rules; Unit (1), Void (0), Maybe, Nat (Zero/Succ), List (Nil/Cons), Sum/Product ADTs, Church encodings, and Simply Typed Lambda Calculus (STLC) as a Cartesian Closed Category.",
        "global_invariants": [
            "Type Definition Quartet (p. 234): Every type constructor is specified by Formation, Introduction (constructors), Elimination (pattern-matching/destructors), and Computation (β/η laws).",
            "Curry-Howard-Lambek Isomorphism (p. 260): Types are Objects/Propositions, Programs/Terms Γ ⊢ t : B are Morphisms/Proofs, and β-reduction is diagram commutativity.",
            "Church Encoding Universality (p. 257): Every inductive ADT is encoded by its universal elimination signature (e.g., Bool ≡ ∀a. a → a → a)."
        ]
    },
    {
        "chapter": 7,
        "id": "ch07-functors",
        "title": "Chapter 7: Functors — Structure-Preserving Maps Across Mathematical Worlds",
        "start_page": 278,
        "end_page": 318,
        "theme": "Functors F : C → D as homomorphisms between categories preserving identity and composition; unifying monoid homomorphisms, monotone poset maps, logical translations, and programming type constructors (List, Maybe, .map); contravariant and pointed functors.",
        "global_invariants": [
            "Functoriality Laws (p. 289–290): F(id_A) = id_{F(A)} and F(g ∘ f) = F(g) ∘ F(f).",
            "Cross-Domain Unification (p. 301): A functor between single-object categories is a monoid homomorphism; a functor between thin categories is a monotone order-preserving function.",
            "Programming Endofunctors (p. 306–308): In functional programming, a type constructor F : Type → Type equipped with map : (a → b) → (F a → F b) is an endofunctor."
        ]
    },
    {
        "chapter": 8,
        "id": "ch08-natural-transformations-and-2-categories",
        "title": "Chapter 8: Natural Transformations, Categorical Equivalence & 2-Categories",
        "start_page": 319,
        "end_page": 377,
        "theme": "Saunders Mac Lane's vision: categories and functors exist to define natural transformations α : F ⇒ G; naturality squares G(f) ∘ α_A = α_B ∘ F(f); polymorphic functions (reverse, head, take1); natural isomorphisms, categorical equivalence, and 2-categories.",
        "global_invariants": [
            "Naturality Square Law (p. 319, p. 348): For every f : A → B in C, transforming first then mapping equals mapping first then transforming: G(f) ∘ α_A = α_B ∘ F(f).",
            "Parametric Polymorphism as Naturality (p. 350): Every polymorphic function α : ∀a. F a → G a (such as reverse : [a] → [a] or safeHead : [a] → Maybe a) satisfies the naturality square as a free theorem.",
            "2-Categorical Hierarchy (p. 329, p. 369): Categories (0-cells), Functors (1-cells), and Natural Transformations (2-cells) assemble into the strict 2-category Cat, enabling true categorical equivalence C ≃ D."
        ]
    }
]

STALKS = [
    # Chapter 1 (3 stalks: pp. 3..51)
    {
        "id": "visual-abstraction-modes-of-knowledge",
        "title": "Visual Abstraction & Lawvere's Perspective",
        "chapter": 1,
        "section": "1.1",
        "start_page": 3,
        "end_page": 12,
        "layer": "Epistemological Base",
        "symbol": "U_01",
        "summary": "Dedication to F. William Lawvere and Bertrand Russell's definition of abstract theories as meta-languages for defining tools through visual diagrams rather than domain-bound formulas.",
        "formal_core": "\\text{Abstract Theory} : \\text{Concrete Domains} \\xrightarrow{\\text{Diagrammatic Abstraction}} \\mathbf{Cat}",
        "keywords": ["Lawvere", "Bertrand Russell", "abstract theory", "visual diagrams", "modes of knowledge"],
        "olog": {
            "types": [
                {"id": "concrete", "label": "Concrete Domain Theory (Biology, Physics)"},
                {"id": "abstract", "label": "Abstract Meta-Theory (Sets, Categories)"},
                {"id": "diagram", "label": "Commutative Visual Diagram"}
            ],
            "aspects": [
                {"src": "concrete", "dst": "abstract", "label": "generalizes via"},
                {"src": "abstract", "dst": "diagram", "label": "is expressed spatially as"}
            ],
            "facts": [
                "Instead of deducing from fixed assumptions, abstract theory asks what general structural principles unify distinct concrete domains (Russell, p. 11)."
            ]
        }
    },
    {
        "id": "sets-subsets-empty-singleton",
        "title": "Sets, Subsets, Empty Set (∅) & Singleton (1)",
        "chapter": 1,
        "section": "1.2",
        "start_page": 13,
        "end_page": 27,
        "layer": "Set-Theoretic Grounding",
        "symbol": "U_02",
        "summary": "Cantor's definition of sets as unstructured collections of distinct elements (illustrated as colored balls); subsets as spatial containment; singleton sets (1) and the unique empty set (∅); functions as many-to-one mappings and hom-sets.",
        "formal_core": "\\forall A \\in \\mathbf{Set}, \\quad \\exists! \\; \\emptyset \\to A \\quad \\text{and} \\quad \\exists! \\; A \\to 1, \\quad \\mathrm{Hom}(A,B) = B^A",
        "keywords": ["Cantor", "set", "subset", "singleton", "empty set", "function", "hom set", "identity function"],
        "olog": {
            "types": [
                {"id": "empty", "label": "Empty Set ∅ (Zero Elements)"},
                {"id": "setA", "label": "General Set A (Colored Balls)"},
                {"id": "singleton", "label": "Singleton Set 1 (One Element)"},
                {"id": "hom", "label": "Hom-Set Hom(A, B)"}
            ],
            "aspects": [
                {"src": "empty", "dst": "setA", "label": "unique absurd map ! : ∅ → A"},
                {"src": "setA", "dst": "singleton", "label": "unique terminal map ! : A → 1"},
                {"id": "id_map", "src": "setA", "dst": "hom", "label": "collects all arrows A → B into"}
            ],
            "facts": [
                "A set contains no internal order or position; two sets with the same elements are the same set (p. 13).",
                "There is a unique function from the empty set ∅ to any set A (p. 22), and a unique function from any set A to a singleton set 1 (p. 24)."
            ]
        }
    },
    {
        "id": "functions-bijections-isomorphisms",
        "title": "Injections, Surjections, Isomorphisms & Currying in Set",
        "chapter": 1,
        "section": "1.3",
        "start_page": 28,
        "end_page": 51,
        "layer": "Set-Theoretic Grounding",
        "symbol": "U_03",
        "summary": "Functions in mathematics vs. programming; function composition g ∘ f; injections (one-to-one), surjections (onto), and bijections; set isomorphisms via invertible arrow pairs; higher-order functions and currying.",
        "formal_core": "f : A \\xrightarrow{\\sim} B \\iff \\exists g : B \\to A \\text{ s.t. } g \\circ f = \\mathrm{id}_A \\;\\wedge\\; f \\circ g = \\mathrm{id}_B",
        "keywords": ["composition", "injection", "surjection", "bijection", "isomorphism", "currying", "programming"],
        "olog": {
            "types": [
                {"id": "domA", "label": "Domain Set A"},
                {"id": "codB", "label": "Codomain Set B"},
                {"id": "iso", "label": "Isomorphism Pair (f, g)"}
            ],
            "aspects": [
                {"src": "domA", "dst": "codB", "label": "bijection f : A → B"},
                {"src": "codB", "dst": "domA", "label": "inverse g : B → A"},
                {"src": "iso", "dst": "domA", "label": "satisfies g ∘ f = id_A on"}
            ],
            "facts": [
                "Isomorphic sets have the exact same cardinality and structural behavior from the perspective of external functions (p. 48)."
            ]
        }
    },

    # Chapter 2 (3 stalks: pp. 52..94)
    {
        "id": "external-products-and-projections",
        "title": "From Internal Pairs to External Categorical Products (A × B)",
        "chapter": 2,
        "section": "2.1",
        "start_page": 52,
        "end_page": 68,
        "layer": "Categorical Foundations",
        "symbol": "U_04",
        "summary": "Constructing Cartesian products A × B first internally as grids of pairs (a,b), then externally (point-free) purely via projection morphisms π₁ : A × B → A, π₂ : A × B → B and the universal mediating arrow ⟨f, g⟩.",
        "formal_core": "\\forall (C \\xrightarrow{f} A, C \\xrightarrow{g} B), \\; \\exists! \\langle f, g \\rangle : C \\to A \\times B \\text{ s.t. } \\pi_1 \\circ \\langle f,g \\rangle = f \\;\\wedge\\; \\pi_2 \\circ \\langle f,g \\rangle = g",
        "keywords": ["Cartesian product", "projection", "external definition", "universal property", "product isomorphism"],
        "olog": {
            "types": [
                {"id": "apexC", "label": "Candidate Object C"},
                {"id": "prodAB", "label": "Universal Product A × B"},
                {"id": "compAB", "label": "Component Objects A and B"}
            ],
            "aspects": [
                {"src": "apexC", "dst": "prodAB", "label": "unique factorizer ⟨f, g⟩"},
                {"src": "prodAB", "dst": "compAB", "label": "canonical projections π₁, π₂"},
                {"src": "apexC", "dst": "compAB", "label": "test morphisms f, g"}
            ],
            "facts": [
                "Products are associative and commutative up to canonical isomorphism: (A × B) × C ≅ A × (B × C) and A × 1 ≅ A (p. 55)."
            ]
        }
    },
    {
        "id": "categorical-duality-and-coproducts",
        "title": "Categorical Duality, Coproducts (A + B) & Initial/Terminal Objects",
        "chapter": 2,
        "section": "2.2",
        "start_page": 69,
        "end_page": 81,
        "layer": "Categorical Foundations",
        "symbol": "U_05",
        "summary": "The principle of Categorical Duality: reversing every arrow in the external diagram of Product yields Coproduct (disjoint union / sum A + B with injections ι₁, ι₂ and co-pairing [f, g]), and reversing Terminal Object 1 yields Initial Object 0.",
        "formal_core": "\\forall (A \\xrightarrow{f} C, B \\xrightarrow{g} C), \\; \\exists! [f, g] : A + B \\to C \\text{ s.t. } [f,g] \\circ \\iota_1 = f \\;\\wedge\\; [f,g] \\circ \\iota_2 = g",
        "keywords": ["duality", "coproduct", "disjoint union", "sum type", "injection", "initial object", "terminal object"],
        "olog": {
            "types": [
                {"id": "partsAB", "label": "Summand Objects A and B"},
                {"id": "coprodAB", "label": "Universal Coproduct A + B"},
                {"id": "targetC", "label": "Target Object C"}
            ],
            "aspects": [
                {"src": "partsAB", "dst": "coprodAB", "label": "canonical injections ι₁, ι₂"},
                {"src": "coprodAB", "dst": "targetC", "label": "unique case-analysis [f, g]"},
                {"src": "partsAB", "dst": "targetC", "label": "branch handlers f, g"}
            ],
            "facts": [
                "Externalizing definitions into arrows reveals exact structural symmetry between Products (projections out) and Sums (injections in) (p. 69)."
            ]
        }
    },
    {
        "id": "categories-objects-morphisms-laws",
        "title": "The Formal Definition of a Category & Point-Free Epistemology",
        "chapter": 2,
        "section": "2.3",
        "start_page": 82,
        "end_page": 94,
        "layer": "Categorical Foundations",
        "symbol": "U_06",
        "summary": "The Rosetta dictionary between Set Theory (internal elements) and Category Theory (external morphisms); objects, morphisms, composition (∘), identity arrows (id_A), commutative diagrams, and why associativity + identity are the exact laws of composition.",
        "formal_core": "\\mathcal{C} = (\\mathrm{Ob}(\\mathcal{C}), \\mathrm{Hom}_{\\mathcal{C}}, \\circ, \\mathrm{id}) \\quad \\text{with} \\quad h \\circ (g \\circ f) = (h \\circ g) \\circ f",
        "keywords": ["category", "object", "morphism", "associativity", "identity law", "point-free", "commutative diagram"],
        "olog": {
            "types": [
                {"id": "obC", "label": "Objects Ob(C) (Opaque Points)"},
                {"id": "homC", "label": "Morphisms Hom(A, B) (Directed Arrows)"},
                {"id": "compLaw", "label": "Associative Composition g ∘ f"}
            ],
            "aspects": [
                {"src": "homC", "dst": "obC", "label": "has source and target in"},
                {"src": "homC", "dst": "compLaw", "label": "composes associatively via"},
                {"src": "obC", "dst": "homC", "label": "assigns identity arrow id_A in"}
            ],
            "facts": [
                "In category theory, an element a ∈ A is replaced by a generalized element — a morphism 1 → A from the terminal object (p. 77, p. 83)."
            ]
        }
    },

    # Chapter 3 (3 stalks: pp. 95..130)
    {
        "id": "monoids-semigroups-magmas",
        "title": "Magmas, Semigroups & Monoids as Composable Actions",
        "chapter": 3,
        "section": "3.1",
        "start_page": 95,
        "end_page": 103,
        "layer": "Algebraic Symmetries",
        "symbol": "U_07",
        "summary": "Algebraic structures built by progressively adding categorical laws to a binary operation: Magmas (closure), Semigroups (associativity), and Monoids (associativity + neutral identity element e), illustrated via color blending, clock arithmetic, and string concatenation.",
        "formal_core": "(M, \\star, e) \\quad \\text{s.t.} \\quad (a \\star b) \\star c = a \\star (b \\star c) \\;\\wedge\\; e \\star a = a = a \\star e",
        "keywords": ["monoid", "semigroup", "magma", "identity element", "associativity", "binary operation"],
        "olog": {
            "types": [
                {"id": "magma", "label": "Magma (M, ⋆) (Closed Operation)"},
                {"id": "semigroup", "label": "Semigroup (Associative Operation)"},
                {"id": "monoid", "label": "Monoid (M, ⋆, e) (With Identity e)"}
            ],
            "aspects": [
                {"src": "monoid", "dst": "semigroup", "label": "forgets identity element to"},
                {"src": "semigroup", "dst": "magma", "label": "forgets associativity law to"}
            ],
            "facts": [
                "Every monoid operation is a function M × M → M obeying the exact same associativity and unit laws as categorical morphism composition (p. 97–101)."
            ]
        }
    },
    {
        "id": "groups-rotations-and-symmetries",
        "title": "Groups, Geometric Rotations (C₃, D₃) & Invertible Symmetries",
        "chapter": 3,
        "section": "3.2",
        "start_page": 104,
        "end_page": 114,
        "layer": "Algebraic Symmetries",
        "symbol": "U_08",
        "summary": "Adding inverses turns a monoid into a group (G, ⋆, e, inv): rotational symmetries of an equilateral triangle (0°, 120°, 240° = C₃), reflections (D₃), cyclic groups Z_n, and product groups.",
        "formal_core": "\\forall g \\in G, \\; \\exists g^{-1} \\in G \\text{ s.t. } g \\star g^{-1} = e = g^{-1} \\star g",
        "keywords": ["group", "inverse", "rotation", "symmetry", "cyclic group", "product group", "120 degrees"],
        "olog": {
            "types": [
                {"id": "triangle", "label": "Geometric Figure (Equilateral Triangle)"},
                {"id": "rotGroup", "label": "Rotation Group C₃ = {0°, 120°, 240°}"},
                {"id": "invLaw", "label": "Inverse Symmetry g⁻¹"}
            ],
            "aspects": [
                {"src": "rotGroup", "dst": "triangle", "label": "acts by symmetries on"},
                {"src": "rotGroup", "dst": "invLaw", "label": "guarantees every action has"}
            ],
            "facts": [
                "Rotating by 120° and 240° are mutual inverses: 120° ⋆ 240° = 0° = id (p. 104, p. 120)."
            ]
        }
    },
    {
        "id": "monoids-as-single-object-categories-free-monoids",
        "title": "Delooping Monoids as One-Object Categories & Free Monoids",
        "chapter": 3,
        "section": "3.3",
        "start_page": 115,
        "end_page": 130,
        "layer": "Algebraic Symmetries",
        "symbol": "U_09",
        "summary": "Shifting perspective from monoid elements as static points to monoid elements as self-arrows on a single object (Cayley representation); free monoids (lists/strings) and their universal property.",
        "formal_core": "\\mathbf{B}M : \\mathrm{Ob}(\\mathbf{B}M) = \\{\\bullet\\}, \\quad \\mathrm{Hom}_{\\mathbf{B}M}(\\bullet, \\bullet) = M, \\quad \\mathrm{Free}(A) = \\mathrm{List}(A)",
        "keywords": ["single-object category", "delooping", "Cayley theorem", "free monoid", "universal property", "fold"],
        "olog": {
            "types": [
                {"id": "genSet", "label": "Generator Alphabet Set A"},
                {"id": "freeMon", "label": "Free Monoid List(A)"},
                {"id": "oneObjCat", "label": "Single-Object Category BM"}
            ],
            "aspects": [
                {"src": "genSet", "dst": "freeMon", "label": "generates all finite words in"},
                {"src": "freeMon", "dst": "oneObjCat", "label": "universally folds into any"}
            ],
            "facts": [
                "A category with one object • is literally a monoid: elements are endomorphisms • → • and composition is the monoid operation (p. 115)."
            ]
        }
    },

    # Chapter 4 (3 stalks: pp. 131..161)
    {
        "id": "orders-hasse-diagrams-and-lattices",
        "title": "Partial Orders, Hasse Diagrams, Divisibility & Color Lattices",
        "chapter": 4,
        "section": "4.1",
        "start_page": 131,
        "end_page": 147,
        "layer": "Order & Hierarchy",
        "symbol": "U_10",
        "summary": "Binary relations (reflexivity, antisymmetry, transitivity, totality); visual Hasse diagrams via transitive reduction; total orders vs. partial orders (subset inclusion, color mixing, integer divisibility); meets (greatest lower bounds) and joins (least upper bounds).",
        "formal_core": "(P, \\le) : a \\le a \\;(\\text{Refl}), \\quad a \\le b \\wedge b \\le c \\Rightarrow a \\le c \\;(\\text{Trans}), \\quad a \\le b \\wedge b \\le a \\Rightarrow a = b \\;(\\text{Antisym})",
        "keywords": ["partial order", "total order", "Hasse diagram", "lattice", "meet", "join", "divisibility", "color mixing"],
        "olog": {
            "types": [
                {"id": "posetP", "label": "Partially Ordered Set (P, ≤)"},
                {"id": "hasse", "label": "Transitive-Reduced Hasse Diagram"},
                {"id": "lattice", "label": "Bounded Lattice (P, ∧, ∨, ⊥, ⊤)"}
            ],
            "aspects": [
                {"src": "posetP", "dst": "hasse", "label": "is visualized minimally as"},
                {"src": "lattice", "dst": "posetP", "label": "equips every pair with meet ∧ & join ∨ in"}
            ],
            "facts": [
                "In the color-mixing partial order, the join a ∨ b is the mixed color and the meet a ∧ b is the shared primary pigment component (p. 145)."
            ]
        }
    },
    {
        "id": "birkhoff-representation-and-boolean-lattices",
        "title": "Birkhoff's Representation Theorem & Power-Set Lattices",
        "chapter": 4,
        "section": "4.2",
        "start_page": 148,
        "end_page": 152,
        "layer": "Order & Hierarchy",
        "symbol": "U_11",
        "summary": "Every finite distributive lattice (such as divisibility of square-free integers or color mixing) is order-isomorphic to a lattice of sets ordered by subset inclusion ⊆ (Birkhoff's Representation Theorem).",
        "formal_core": "L \\;\\text{distributive lattice} \\implies L \\cong \\mathcal{O}(\\mathrm{Irr}(L)) \\subseteq \\mathcal{P}(X)",
        "keywords": ["Birkhoff representation theorem", "distributive lattice", "join-irreducible", "power set", "order isomorphism"],
        "olog": {
            "types": [
                {"id": "distLat", "label": "Finite Distributive Lattice L"},
                {"id": "joinIrr", "label": "Poset of Join-Irreducible Atoms Irr(L)"},
                {"id": "subLat", "label": "Subset Inclusion Lattice P(Irr(L))"}
            ],
            "aspects": [
                {"src": "distLat", "dst": "joinIrr", "label": "extracts prime/atomic elements"},
                {"src": "distLat", "dst": "subLat", "label": "is order-isomorphic via Birkhoff map to"}
            ],
            "facts": [
                "Divisibility of {1, 2, 3, 5, 6, 10, 15, 30}, RGB color mixing, and subsets of a 3-element set are three drawings of the exact same 3D cube lattice (p. 148)."
            ]
        }
    },
    {
        "id": "preorders-equivalence-and-thin-categories",
        "title": "Preorders, Equivalence Relations & Thin Categories",
        "chapter": 4,
        "section": "4.3",
        "start_page": 153,
        "end_page": 161,
        "layer": "Order & Hierarchy",
        "symbol": "U_12",
        "summary": "Dropping antisymmetry yields preorders (reflexive + transitive), which are literally Thin Categories (at most one arrow between any two objects). Adding symmetry yields equivalence relations (thin groupoids).",
        "formal_core": "\\mathbf{Preord} \\simeq \\mathbf{Cat}_{\\mathrm{thin}} = \\{ \\mathcal{C} \\in \\mathbf{Cat} \\mid \\forall a,b,\\; |\\mathrm{Hom}_{\\mathcal{C}}(a,b)| \\le 1 \\}",
        "keywords": ["preorder", "thin category", "equivalence relation", "antisymmetry", "categorical product as meet"],
        "olog": {
            "types": [
                {"id": "preorder", "label": "Preorder (P, ≲) (Refl + Trans)"},
                {"id": "thinCat", "label": "Thin Category (|Hom(a,b)| ≤ 1)"},
                {"id": "equivRel", "label": "Equivalence Relation (Thin Groupoid)"}
            ],
            "aspects": [
                {"src": "preorder", "dst": "thinCat", "label": "is identical in structure to"},
                {"src": "equivRel", "dst": "preorder", "label": "adds symmetry (invertible arrows) to"}
            ],
            "facts": [
                "In a thin category, any diagram automatically commutes because there is at most one arrow between any start and end object (p. 156)."
            ]
        }
    },

    # Chapter 5 (3 stalks: pp. 162..211)
    {
        "id": "propositional-logic-as-category",
        "title": "Categorifying Logic: Propositions as Objects & Proofs as Arrows",
        "chapter": 5,
        "section": "5.1",
        "start_page": 162,
        "end_page": 179,
        "layer": "Logical Deduction",
        "symbol": "U_13",
        "summary": "Viewing deductive logic as a category where objects are propositions, morphisms P → Q are proofs/entailments, identity is tautology P ⊢ P, composition is Modus Ponens / syllogism, Truth ⊤ is Terminal, Falsity ⊥ is Initial, Conjunction ∧ is Product, and Disjunction ∨ is Coproduct.",
        "formal_core": "\\frac{P \\vdash Q \\quad Q \\vdash R}{P \\vdash R} \\;(\\circ), \\quad P \\wedge Q \\equiv P \\times Q, \\quad P \\vee Q \\equiv P + Q, \\quad \\top \\equiv 1, \\quad \\bot \\equiv 0",
        "keywords": ["logic", "proposition", "proof", "conjunction", "disjunction", "initial falsity", "terminal truth"],
        "olog": {
            "types": [
                {"id": "propObj", "label": "Logical Propositions P, Q"},
                {"id": "proofArr", "label": "Deductive Entailment P ⊢ Q"},
                {"id": "connLim", "label": "Universal Connectives (P ∧ Q, P ∨ Q, ⊤, ⊥)"}
            ],
            "aspects": [
                {"src": "propObj", "dst": "proofArr", "label": "are connected by proofs in"},
                {"src": "connLim", "dst": "propObj", "label": "constructs products/coproducts of"}
            ],
            "facts": [
                "Ex falso quodlibet (from contradiction ⊥ anything follows: ⊥ ⊢ P) is the exact logical manifestation of the Initial Object 0 → A (p. 165)."
            ]
        }
    },
    {
        "id": "implication-currying-and-intuitionistic-bhk",
        "title": "Implication (P ⇒ Q), Exponential Currying & Intuitionistic BHK Logic",
        "chapter": 5,
        "section": "5.2",
        "start_page": 180,
        "end_page": 196,
        "layer": "Logical Deduction",
        "symbol": "U_14",
        "summary": "Internalizing entailment as an Implication object P ⇒ Q via the currying adjunction (R ∧ P ⊢ Q iff R ⊢ P ⇒ Q); Brouwer-Heyting-Kolmogorov (BHK) constructive proof interpretation where a proof of P ⇒ Q is a function transforming proofs of P into proofs of Q.",
        "formal_core": "\\mathrm{Hom}(R \\wedge P, Q) \\cong \\mathrm{Hom}(R, P \\Rightarrow Q), \\quad \\mathrm{eval} : (P \\Rightarrow Q) \\wedge P \\to Q",
        "keywords": ["implication", "modus ponens", "currying", "exponential object", "intuitionistic logic", "BHK interpretation", "Brouwer"],
        "olog": {
            "types": [
                {"id": "conjRP", "label": "Conjoined Premise R ∧ P"},
                {"id": "impPQ", "label": "Implication Object (P ⇒ Q)"},
                {"id": "bhkFunc", "label": "BHK Constructive Proof Transformer"}
            ],
            "aspects": [
                {"src": "conjRP", "dst": "impPQ", "label": "transposes via currying to"},
                {"src": "impPQ", "dst": "bhkFunc", "label": "is realized constructively as"}
            ],
            "facts": [
                "Modus Ponens ((P ⇒ Q) ∧ P ⊢ Q) is the categorical evaluation morphism eval : B^A × A → B of an exponential object (p. 181)."
            ]
        }
    },
    {
        "id": "heyting-and-boolean-algebras-bicartesian-closed",
        "title": "Heyting Algebras, Boolean Algebras & Bicartesian Closed Categories",
        "chapter": 5,
        "section": "5.3",
        "start_page": 197,
        "end_page": 211,
        "layer": "Logical Deduction",
        "symbol": "U_15",
        "summary": "Thin bicartesian closed categories are Heyting Algebras (modeling intuitionistic logic where P ∨ ¬P need not hold globally, e.g., open-set topologies); adding Law of Excluded Middle yields Boolean Algebras.",
        "formal_core": "\\mathbf{HeytingAlg} \\simeq \\mathbf{ThinBicartClosedCat}, \\quad \\neg P \\equiv (P \\Rightarrow \\bot)",
        "keywords": ["Heyting algebra", "Boolean algebra", "bicartesian closed category", "excluded middle", "negation", "double negation"],
        "olog": {
            "types": [
                {"id": "bcc", "label": "Bicartesian Closed Category (0, 1, ×, +, B^A)"},
                {"id": "heyting", "label": "Heyting Algebra (Intuitionistic Logic)"},
                {"id": "boolean", "label": "Boolean Algebra (Classical Logic P ∨ ¬P = ⊤)"}
            ],
            "aspects": [
                {"src": "bcc", "dst": "heyting", "label": "collapses to thin poset as"},
                {"src": "boolean", "dst": "heyting", "label": "is the special complemented case of"}
            ],
            "facts": [
                "A category with products, coproducts, initial/terminal objects, and exponentials is Bicartesian Closed — the shared home of logic, sets, and types (Theorem, p. 203)."
            ]
        }
    },

    # Chapter 6 (3 stalks: pp. 212..277)
    {
        "id": "type-theory-russell-and-formation-intro-elim",
        "title": "Type Theory, Russell's Paradox & Formation / Intro / Elim Rules",
        "chapter": 6,
        "section": "6.1",
        "start_page": 212,
        "end_page": 239,
        "layer": "Type Systems & Computation",
        "symbol": "U_16",
        "summary": "How Bertrand Russell resolved naive set-theoretic self-reference via stratified Types; defining types constructively through Type Formation, Term Introduction (constructors), Term Elimination (pattern matching), and Computation (β/η reduction), illustrated with Bool, Unit, Void, and Maybe.",
        "formal_core": "\\frac{\\Gamma \\vdash x : A}{\\Gamma \\vdash \\mathrm{Just}(x) : \\mathrm{Maybe}\\;A} \\;(\\text{Intro}), \\quad \\mathrm{maybe} : b \\to (a \\to b) \\to \\mathrm{Maybe}\\;a \\to b \\;(\\text{Elim})",
        "keywords": ["type theory", "Russell paradox", "type formation", "term introduction", "term elimination", "Maybe", "Bool"],
        "olog": {
            "types": [
                {"id": "formRule", "label": "Type Formation Rule (Signature)"},
                {"id": "introRule", "label": "Term Introduction (Arrows Into Type)"},
                {"id": "elimRule", "label": "Term Elimination (Universal Arrow Out)"},
                {"id": "compRule", "label": "Computation Rule (Commuting Diagram β/η)"}
            ],
            "aspects": [
                {"src": "introRule", "dst": "formRule", "label": "constructs canonical inhabitants of"},
                {"src": "formRule", "dst": "elimRule", "label": "eliminates via universal property"},
                {"src": "compRule", "dst": "elimRule", "label": "assertsElim ∘ Intro commutes in"}
            ],
            "facts": [
                "Type Introduction rules correspond to arrows pointing INTO the object (like coproduct injections), while Elimination rules correspond to universal arrows pointing OUT (p. 234–238)."
            ]
        }
    },
    {
        "id": "inductive-types-nat-list-and-church-encodings",
        "title": "Inductive Types (Nat, List), Algebraic Data Types & Church Encodings",
        "chapter": 6,
        "section": "6.2",
        "start_page": 240,
        "end_page": 259,
        "layer": "Type Systems & Computation",
        "symbol": "U_17",
        "summary": "Recursive inductive types: Natural numbers (Zero : 1 → Nat, Succ : Nat → Nat), Lists (Nil, Cons), Product types (Pair), Sum types (Either), and Alonzo Church's encodings representing data purely by its universal elimination function.",
        "formal_core": "\\mathrm{Nat} \\cong \\forall a.\\; a \\to (a \\to a) \\to a, \\quad \\mathrm{List}\\;A \\cong \\forall r.\\; r \\to (A \\to r \\to r) \\to r",
        "keywords": ["inductive type", "Peano naturals", "List", "Nil", "Cons", "algebraic data type", "Church encoding"],
        "olog": {
            "types": [
                {"id": "adt", "label": "Algebraic Data Type (Nat, List A, Either A B)"},
                {"id": "constructors", "label": "Constructors (Zero/Succ, Nil/Cons)"},
                {"id": "church", "label": "Polymorphic Church Encoding (Universal Fold)"}
            ],
            "aspects": [
                {"src": "constructors", "dst": "adt", "label": "freely generates terms of"},
                {"src": "adt", "dst": "church", "label": "is completely determined by its eliminator"}
            ],
            "facts": [
                "The Church encoding of any data type is literally its universal elimination diagram written as a polymorphic function type (p. 257)."
            ]
        }
    },
    {
        "id": "simply-typed-lambda-calculus-curry-howard-lambek",
        "title": "Simply Typed Lambda Calculus (STLC) & Curry-Howard-Lambek Rosetta Stone",
        "chapter": 6,
        "section": "6.3",
        "start_page": 260,
        "end_page": 277,
        "layer": "Type Systems & Computation",
        "symbol": "U_18",
        "summary": "Sequent contexts Γ ⊢ t : A, lambda abstraction (λx. t) as currying, application as evaluation, and Joachim Lambek's three-way equivalence between Intuitionistic Logic, Simply Typed Lambda Calculus, and Cartesian Closed Categories.",
        "formal_core": "\\frac{\\Gamma, x : A \\vdash t : B}{\\Gamma \\vdash (\\lambda x.\\; t) : A \\to B} \\;(\\to\\text{-Intro}) \\;\\Longleftrightarrow\\; \\mathrm{Hom}(\\Gamma \\times A, B) \\cong \\mathrm{Hom}(\\Gamma, B^A)",
        "keywords": ["Simply Typed Lambda Calculus", "STLC", "Curry-Howard-Lambek", "typing context", "lambda abstraction", "beta reduction"],
        "olog": {
            "types": [
                {"id": "stlc", "label": "Simply Typed Lambda Calculus (Γ ⊢ t : B)"},
                {"id": "ccc", "label": "Cartesian Closed Category (1, ×, B^A)"},
                {"id": "intLogic", "label": "Intuitionistic Natural Deduction"}
            ],
            "aspects": [
                {"src": "stlc", "dst": "ccc", "label": "compiles terms into morphisms of"},
                {"src": "stlc", "dst": "intLogic", "label": "is isomorphic under Curry-Howard to"}
            ],
            "facts": [
                "A typing judgment x₁:A₁, …, xₙ:Aₙ ⊢ t : B is a morphism A₁ × … × Aₙ → B in the syntactic Cartesian Closed Category of types (p. 260–264)."
            ]
        }
    },

    # Chapter 7 (3 stalks: pp. 278..318)
    {
        "id": "functors-structure-preserving-maps",
        "title": "Functors F : C → D — Structure-Preserving Maps Between Categories",
        "chapter": 7,
        "section": "7.1",
        "start_page": 278,
        "end_page": 295,
        "layer": "Functorial Bridges",
        "symbol": "U_19",
        "summary": "Generalizing order-embeddings and group homomorphisms to arbitrary categories: a functor F : C → D maps objects to objects and morphisms to morphisms while preserving identities and composition triangles.",
        "formal_core": "F : \\mathcal{C} \\to \\mathcal{D}, \\quad F(\\mathrm{id}_A) = \\mathrm{id}_{F(A)}, \\quad F(g \\circ f) = F(g) \\circ F(f)",
        "keywords": ["functor", "structure preservation", "object mapping", "morphism mapping", "functor laws", "categorical isomorphism"],
        "olog": {
            "types": [
                {"id": "srcCat", "label": "Source Category C"},
                {"id": "dstCat", "label": "Target Category D"},
                {"id": "funcF", "label": "Functor F = (F_Ob, F_Hom)"}
            ],
            "aspects": [
                {"src": "funcF", "dst": "srcCat", "label": "reads commutative triangles in"},
                {"src": "funcF", "dst": "dstCat", "label": "reconstructs commuting images in"}
            ],
            "facts": [
                "Because functors preserve composition and identities, they automatically preserve commutative diagrams and isomorphisms: if f is an isomorphism, F(f) is an isomorphism (p. 289–290)."
            ]
        }
    },
    {
        "id": "functors-across-monoids-orders-logic",
        "title": "Functors Across Worlds: Monoid Homomorphisms & Monotone Maps",
        "chapter": 7,
        "section": "7.2",
        "start_page": 296,
        "end_page": 305,
        "layer": "Functorial Bridges",
        "symbol": "U_20",
        "summary": "Instantiating the functor laws across Chapters 1–5: functors between one-object categories BM → BN are monoid homomorphisms f(x ⋆ y) = f(x) · f(y); functors between thin poset categories are monotone functions a ≤ b ⇒ F(a) ≤ F(b); forgetful functors strip structure.",
        "formal_core": "\\mathbf{Cat}(\\mathbf{B}M, \\mathbf{B}N) = \\mathbf{Mon}(M, N), \\quad \\mathbf{Cat}((P, \\le), (Q, \\le)) = \\mathbf{Poset}(P, Q)",
        "keywords": ["monoid homomorphism", "monotone function", "order embedding", "forgetful functor", "linear function"],
        "olog": {
            "types": [
                {"id": "genFunctor", "label": "General Categorical Functor F : C → D"},
                {"id": "monHom", "label": "Monoid Homomorphism f : M → N"},
                {"id": "monoMap", "label": "Monotone Order-Preserving Map P → Q"}
            ],
            "aspects": [
                {"src": "genFunctor", "dst": "monHom", "label": "specializes on 1-object categories to"},
                {"src": "genFunctor", "dst": "monoMap", "label": "specializes on thin categories to"}
            ],
            "facts": [
                "The functor law F(g ∘ f) = F(g) ∘ F(f) becomes f(a + b) = f(a) + f(b) on monoids and (a ≤ b ⇒ F(a) ≤ F(b)) on posets (p. 301–304)."
            ]
        }
    },
    {
        "id": "programming-endofunctors-pointed-contravariant",
        "title": "Programming Endofunctors (List, Maybe, .map), Pointed & Contravariant Functors",
        "chapter": 7,
        "section": "7.3",
        "start_page": 306,
        "end_page": 318,
        "layer": "Functorial Bridges",
        "symbol": "U_21",
        "summary": "Functors in software engineering: generic type constructors F<A> equipped with map / fmap lifting functions (A → B) to (F<A> → F<B>); pointed functors (unit/pure : A → F<A>); contravariant functors F : C^op → D reversing arrow direction (predicates, serializers, Hom(-, R)).",
        "formal_core": "\\mathrm{map} : (A \\to B) \\to (F\\;A \\to F\\;B), \\quad F^{\\mathrm{op}} : \\mathcal{C}^{\\mathrm{op}} \\to \\mathcal{D}, \\quad F(g \\circ f) = F(f) \\circ F(g)",
        "keywords": ["endofunctor", "map", "fmap", "List functor", "Maybe functor", "pointed functor", "contravariant functor"],
        "olog": {
            "types": [
                {"id": "typeCat", "label": "Category of Types & Pure Functions"},
                {"id": "endoF", "label": "Endofunctor Container F (List, Maybe, Promise)"},
                {"id": "contraF", "label": "Contravariant Functor C^op → Type"}
            ],
            "aspects": [
                {"src": "endoF", "dst": "typeCat", "label": "lifts functionscovariant via .map in"},
                {"src": "contraF", "dst": "typeCat", "label": "reverses morphism direction in"}
            ],
            "facts": [
                "In TypeScript/Haskell, `a.map(x => x) == a` is the Identity Functor Law and `a.map(f).map(g) == a.map(x => g(f(x)))` is the Composition Functor Law (p. 308)."
            ]
        }
    },

    # Chapter 8 (3 stalks: pp. 319..377)
    {
        "id": "natural-transformations-and-naturality-squares",
        "title": "Natural Transformations α : F ⇒ G & Naturality Squares",
        "chapter": 8,
        "section": "8.1",
        "start_page": 319,
        "end_page": 341,
        "layer": "Higher 2-Categorical Synthesis",
        "symbol": "U_22",
        "summary": "Saunders Mac Lane's motivation for category theory: a natural transformation α : F ⇒ G is a family of component morphisms α_A : F(A) → G(A) indexed by objects A ∈ C such that every morphism f : A → B induces a commuting naturality square.",
        "formal_core": "\\alpha : F \\Rightarrow G \\iff \\forall (A \\xrightarrow{f} B) \\in \\mathcal{C}, \\quad G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f)",
        "keywords": ["natural transformation", "Saunders Mac Lane", "naturality square", "component morphism", "functor morphism"],
        "olog": {
            "types": [
                {"id": "functorPair", "label": "Parallel Functors F, G : C → D"},
                {"id": "compAlpha", "label": "Component Family α_A : F(A) → G(A)"},
                {"id": "natSquare", "label": "Commuting Naturality Square G(f) ∘ α_A = α_B ∘ F(f)"}
            ],
            "aspects": [
                {"src": "compAlpha", "dst": "functorPair", "label": "bridges object images between"},
                {"src": "compAlpha", "dst": "natSquare", "label": "must commute for every arrow f in"}
            ],
            "facts": [
                "Mac Lane: 'I didn't invent categories to study functors; I invented them to study natural transformations' (p. 319)."
            ]
        }
    },
    {
        "id": "polymorphic-functions-and-categorical-equivalence",
        "title": "Parametric Polymorphism (∀a. F a → G a) & Categorical Equivalence",
        "chapter": 8,
        "section": "8.2",
        "start_page": 342,
        "end_page": 359,
        "layer": "Higher 2-Categorical Synthesis",
        "symbol": "U_23",
        "summary": "Polymorphic container functions (`reverse : List a → List a`, `safeHead : List a → Maybe a`, `take1`) as natural transformations that rearrange structure without inspecting element values; natural isomorphisms F ≅ G and weak categorical equivalence C ≃ D.",
        "formal_core": "\\alpha : \\forall a.\\; F\\;a \\to G\\;a \\implies \\mathrm{map}_G(f) \\circ \\alpha_A = \\alpha_B \\circ \\mathrm{map}_F(f), \\quad \\mathcal{C} \\simeq \\mathcal{D} \\iff G \\circ F \\cong \\mathrm{Id}_{\\mathcal{C}} \\;\\wedge\\; F \\circ G \\cong \\mathrm{Id}_{\\mathcal{D}}",
        "keywords": ["parametric polymorphism", "free theorem", "reverse", "head", "natural isomorphism", "categorical equivalence"],
        "olog": {
            "types": [
                {"id": "polyFn", "label": "Polymorphic Function ∀a. F a → G a"},
                {"id": "natIso", "label": "Natural Isomorphism α : F ≅ G"},
                {"id": "catEquiv", "label": "Categorical Equivalence C ≃ D"}
            ],
            "aspects": [
                {"src": "polyFn", "dst": "natIso", "label": "when invertible at every type yields"},
                {"src": "natIso", "dst": "catEquiv", "label": "witnesses round-trip equivalence in"}
            ],
            "facts": [
                "Because a truly polymorphic function ∀a. F a → G a cannot inspect the type a, it is forced to commute with any f : a → b (Wadler's Free Theorems, p. 342–350)."
            ]
        }
    },
    {
        "id": "functor-categories-vertical-horizontal-2-categories",
        "title": "Functor Categories [C, D], Vertical/Horizontal Composition & 2-Categories",
        "chapter": 8,
        "section": "8.3",
        "start_page": 360,
        "end_page": 377,
        "layer": "Higher 2-Categorical Synthesis",
        "symbol": "U_24",
        "summary": "Composing natural transformations vertically (β ∘ α : F ⇒ H) to form the Functor Category [C, D] and horizontally (β * α) across composable functors; assembling 0-cells (Categories), 1-cells (Functors), and 2-cells (Natural Transformations) into the 2-Category Cat.",
        "formal_core": "(\\beta \\circ \\alpha)_A = \\beta_A \\circ \\alpha_A, \\quad (\\beta * \\alpha)_A = \\beta_{G(A)} \\circ F'(\\alpha_A) = G'(\\alpha_A) \\circ \\beta_{F(A)} \\quad \\text{(Interchange Law)}",
        "keywords": ["functor category", "vertical composition", "horizontal composition", "2-category", "interchange law", "whiskering"],
        "olog": {
            "types": [
                {"id": "funCat", "label": "Functor Category [C, D] = D^C"},
                {"id": "vertHoriz", "label": "Vertical (β ∘ α) & Horizontal (β * α) Composition"},
                {"id": "twoCat", "label": "Strict 2-Category Cat (0-cells, 1-cells, 2-cells)"}
            ],
            "aspects": [
                {"src": "vertHoriz", "dst": "funCat", "label": "equips functors with morphism composition in"},
                {"src": "funCat", "dst": "twoCat", "label": "serves as the hom-categories of"}
            ],
            "facts": [
                "In the 2-category Cat, vertical and horizontal composition of natural transformations commute via the Interchange Law (p. 369–374)."
            ]
        }
    }
]

RESTRICTION_MORPHISMS = [
    {"id": "rho-01", "source": "visual-abstraction-modes-of-knowledge", "target": "sets-subsets-empty-singleton", "kind": "grounding", "overlap": "Set theory as the first proto-example of an abstract formal language", "formula": "\\rho_{01}: \\text{AbstractLanguage} \\mapsto \\mathbf{Set}"},
    {"id": "rho-02", "source": "sets-subsets-empty-singleton", "target": "functions-bijections-isomorphisms", "kind": "extension", "overlap": "Functions f : A → B and Hom-sets Hom(A,B) between sets", "formula": "\\rho_{02}: (A,B) \\mapsto \\mathrm{Hom}_{\\mathbf{Set}}(A,B)"},
    {"id": "rho-03", "source": "functions-bijections-isomorphisms", "target": "external-products-and-projections", "kind": "externalization", "overlap": "Replacing internal ordered pairs (a,b) with external projection functions π₁, π₂", "formula": "\\rho_{03}: (a,b) \\mapsto (\\pi_1, \\pi_2)"},
    {"id": "rho-04", "source": "external-products-and-projections", "target": "categorical-duality-and-coproducts", "kind": "duality", "overlap": "Reversing all product arrows in C yields the Coproduct in C^op", "formula": "\\rho_{04}: (A \\times B, \\pi_i) \\xrightarrow{\\mathrm{op}} (A + B, \\iota_i)"},
    {"id": "rho-05", "source": "sets-subsets-empty-singleton", "target": "categorical-duality-and-coproducts", "kind": "universal_specialization", "overlap": "Empty set ∅ as Initial Object 0 and Singleton {•} as Terminal Object 1", "formula": "\\rho_{05}: (\\emptyset, 1) \\mapsto (0_{\\mathcal{C}}, 1_{\\mathcal{C}})"},
    {"id": "rho-06", "source": "categorical-duality-and-coproducts", "target": "categories-objects-morphisms-laws", "kind": "axiomatization", "overlap": "Abstracting objects, morphisms, associative composition, and identity laws", "formula": "\\rho_{06}: (\\mathbf{Set}, \\circ) \\mapsto (\\mathcal{C}, \\circ, \\mathrm{id})"},
    {"id": "rho-07", "source": "external-products-and-projections", "target": "categories-objects-morphisms-laws", "kind": "axiomatization", "overlap": "Universal product cones live in any category C obeying associativity and identity", "formula": "\\rho_{07}: (A \\times B)_{\\mathbf{Set}} \\mapsto (A \\times B)_{\\mathcal{C}}"},
    {"id": "rho-08", "source": "functions-bijections-isomorphisms", "target": "categories-objects-morphisms-laws", "kind": "generalization", "overlap": "Set bijections generalize to categorical isomorphisms g ∘ f = id_A, f ∘ g = id_B", "formula": "\\rho_{08}: \\mathrm{Bij}(A,B) \\mapsto \\mathrm{Iso}_{\\mathcal{C}}(A,B)"},
    {"id": "rho-09", "source": "categories-objects-morphisms-laws", "target": "monoids-semigroups-magmas", "kind": "specialization", "overlap": "Associativity and identity laws of categorical composition specialize to monoid laws", "formula": "\\rho_{09}: (\\circ, \\mathrm{id}) \\mapsto (\\star, e)"},
    {"id": "rho-10", "source": "monoids-semigroups-magmas", "target": "groups-rotations-and-symmetries", "kind": "enrichment", "overlap": "Equipping every monoid element with a two-sided inverse g⁻¹ yields a Group", "formula": "\\rho_{10}: (M, \\star, e) \\hookrightarrow (G, \\star, e, (-)^{-1})"},
    {"id": "rho-11", "source": "groups-rotations-and-symmetries", "target": "monoids-as-single-object-categories-free-monoids", "kind": "delooping", "overlap": "Groups are single-object categories (groupoids) where every arrow is an isomorphism", "formula": "\\rho_{11}: G \\mapsto \\mathbf{B}G"},
    {"id": "rho-12", "source": "monoids-semigroups-magmas", "target": "monoids-as-single-object-categories-free-monoids", "kind": "delooping", "overlap": "Delooping any monoid M into a one-object category BM with Hom(•,•) = M", "formula": "\\rho_{12}: M \\xrightarrow{\\sim} \\mathrm{Hom}_{\\mathbf{B}M}(\\bullet, \\bullet)"},
    {"id": "rho-13", "source": "categories-objects-morphisms-laws", "target": "monoids-as-single-object-categories-free-monoids", "kind": "restriction", "overlap": "Restricting a category C to |Ob(C)| = 1 recovers a monoid", "formula": "\\rho_{13}: \\mathcal{C}_{|\\mathrm{Ob}|=1} \\simeq \\mathbf{B}M"},
    {"id": "rho-14", "source": "sets-subsets-empty-singleton", "target": "orders-hasse-diagrams-and-lattices", "kind": "inclusion_order", "overlap": "Subset containment A ⊆ B defines the prototypical partial order and lattice", "formula": "\\rho_{14}: (\\mathcal{P}(X), \\subseteq) \\mapsto (P, \\le)"},
    {"id": "rho-15", "source": "orders-hasse-diagrams-and-lattices", "target": "birkhoff-representation-and-boolean-lattices", "kind": "representation", "overlap": "Finite distributive lattices are isomorphic to downset lattices of join-irreducibles", "formula": "\\rho_{15}: (L, \\wedge, \\vee) \\xrightarrow{\\sim} (\\mathcal{O}(\\mathrm{Irr}(L)), \\cap, \\cup)"},
    {"id": "rho-16", "source": "orders-hasse-diagrams-and-lattices", "target": "preorders-equivalence-and-thin-categories", "kind": "categorification", "overlap": "Viewing order relations a ≤ b as unique morphisms a → b in a thin category", "formula": "\\rho_{16}: (a \\le b) \\mapsto \\mathrm{Hom}_{P}(a,b) = \\{*\\}"},
    {"id": "rho-17", "source": "birkhoff-representation-and-boolean-lattices", "target": "preorders-equivalence-and-thin-categories", "kind": "categorification", "overlap": "Lattice meets ∧ and joins ∨ are categorical products and coproducts in a thin category", "formula": "\\rho_{17}: (a \\wedge b, a \\vee b) \\mapsto (a \\times_P b, a +_P b)"},
    {"id": "rho-18", "source": "categories-objects-morphisms-laws", "target": "preorders-equivalence-and-thin-categories", "kind": "truncation", "overlap": "Truncating hom-sets to at most one arrow |Hom(a,b)| ≤ 1 yields Preorders", "formula": "\\rho_{18}: \\mathcal{C}_{|\\mathrm{Hom}|\\le 1} \\simeq \\mathbf{Preord}"},
    {"id": "rho-19", "source": "external-products-and-projections", "target": "preorders-equivalence-and-thin-categories", "kind": "thin_limit", "overlap": "Universal product cone in a thin category collapses to greatest lower bound (meet ∧)", "formula": "\\rho_{19}: A \\times B \\mapsto a \\wedge b"},
    {"id": "rho-20", "source": "categorical-duality-and-coproducts", "target": "preorders-equivalence-and-thin-categories", "kind": "thin_colimit", "overlap": "Universal coproduct cocone in a thin category collapses to least upper bound (join ∨)", "formula": "\\rho_{20}: A + B \\mapsto a \\vee b"},
    {"id": "rho-21", "source": "preorders-equivalence-and-thin-categories", "target": "propositional-logic-as-category", "kind": "logical_interpretation", "overlap": "Propositional entailment P ⊢ Q forms a preorder / thin category of deductions", "formula": "\\rho_{21}: (a \\le b) \\mapsto (P \\vdash Q)"},
    {"id": "rho-22", "source": "external-products-and-projections", "target": "propositional-logic-as-category", "kind": "rosetta_product", "overlap": "Categorical Product A × B corresponds to Logical Conjunction P ∧ Q", "formula": "\\rho_{22}: (A \\times B, \\pi_1, \\pi_2) \\mapsto (P \\wedge Q, \\wedge\\text{-Elim})"},
    {"id": "rho-23", "source": "categorical-duality-and-coproducts", "target": "propositional-logic-as-category", "kind": "rosetta_coproduct", "overlap": "Categorical Coproduct A + B corresponds to Logical Disjunction P ∨ Q", "formula": "\\rho_{23}: (A + B, \\iota_1, \\iota_2) \\mapsto (P \\vee Q, \\vee\\text{-Intro})"},
    {"id": "rho-24", "source": "propositional-logic-as-category", "target": "implication-currying-and-intuitionistic-bhk", "kind": "internal_hom", "overlap": "Internalizing deduction P ⊢ Q as the implication object P ⇒ Q via currying", "formula": "\\rho_{24}: (R \\wedge P \\vdash Q) \\xrightarrow{\\sim} (R \\vdash P \\Rightarrow Q)"},
    {"id": "rho-25", "source": "functions-bijections-isomorphisms", "target": "implication-currying-and-intuitionistic-bhk", "kind": "currying_bridge", "overlap": "Function currying Hom(R × P, Q) ≅ Hom(R, Q^P) mirrors logical deduction theorem", "formula": "\\rho_{25}: Q^{P} \\leftrightarrow (P \\Rightarrow Q)"},
    {"id": "rho-26", "source": "implication-currying-and-intuitionistic-bhk", "target": "heyting-and-boolean-algebras-bicartesian-closed", "kind": "algebraization", "overlap": "Equipping a bounded lattice with relative pseudocomplements P ⇒ Q yields a Heyting algebra", "formula": "\\rho_{26}: (L, \\wedge, \\vee, \\Rightarrow) \\in \\mathbf{Heyting}"},
    {"id": "rho-27", "source": "birkhoff-representation-and-boolean-lattices", "target": "heyting-and-boolean-algebras-bicartesian-closed", "kind": "specialization", "overlap": "Classical Boolean algebras are Heyting algebras satisfying P ∨ ¬P = ⊤", "formula": "\\rho_{27}: \\mathbf{BoolAlg} \\hookrightarrow \\mathbf{HeytingAlg}"},
    {"id": "rho-28", "source": "propositional-logic-as-category", "target": "heyting-and-boolean-algebras-bicartesian-closed", "kind": "closure", "overlap": "Combining ⊤, ⊥, ∧, ∨, and ⇒ forms a thin Bicartesian Closed Category", "formula": "\\rho_{28}: (\\top, \\bot, \\wedge, \\vee, \\Rightarrow) \\mapsto \\mathbf{BCC}_{\\mathrm{thin}}"},
    {"id": "rho-29", "source": "sets-subsets-empty-singleton", "target": "type-theory-russell-and-formation-intro-elim", "kind": "paradox_resolution", "overlap": "Stratifying naive sets into Types to resolve Russell's paradox and type-check functions", "formula": "\\rho_{29}: x \\in A \\mapsto \\Gamma \\vdash x : A"},
    {"id": "rho-30", "source": "categorical-duality-and-coproducts", "target": "type-theory-russell-and-formation-intro-elim", "kind": "intro_elim_duality", "overlap": "Type Introduction rules (arrows in) and Elimination rules (universal arrows out)", "formula": "\\rho_{30}: (\\iota, [f,g]) \\mapsto (\\text{Intro}, \\text{Elim})"},
    {"id": "rho-31", "source": "type-theory-russell-and-formation-intro-elim", "target": "inductive-types-nat-list-and-church-encodings", "kind": "recursion", "overlap": "Extending Formation/Intro/Elim to recursive inductive types Nat and List A", "formula": "\\rho_{31}: \\mathrm{Maybe}\\;A \\mapsto \\mathrm{List}\\;A = \\mu X.\\; 1 + A \\times X"},
    {"id": "rho-32", "source": "monoids-as-single-object-categories-free-monoids", "target": "inductive-types-nat-list-and-church-encodings", "kind": "free_monoid_adt", "overlap": "The inductive type List A (Nil, Cons) is the Free Monoid on type A", "formula": "\\rho_{32}: \\mathrm{Free}(A) \\cong \\mathrm{List}\\;A"},
    {"id": "rho-33", "source": "inductive-types-nat-list-and-church-encodings", "target": "simply-typed-lambda-calculus-curry-howard-lambek", "kind": "church_encoding", "overlap": "Encoding inductive ADTs inside Simply Typed / Polymorphic Lambda Calculus", "formula": "\\rho_{33}: \\mathrm{ADT} \\hookrightarrow \\lambda^{\\to,\\forall}"},
    {"id": "rho-34", "source": "implication-currying-and-intuitionistic-bhk", "target": "simply-typed-lambda-calculus-curry-howard-lambek", "kind": "curry_howard", "overlap": "BHK constructive proofs of P ⇒ Q are lambda terms λx:P. t : P → Q", "formula": "\\rho_{34}: (P \\Rightarrow Q) \\cong (\\lambda x:P.\\; t : Q)"},
    {"id": "rho-35", "source": "heyting-and-boolean-algebras-bicartesian-closed", "target": "simply-typed-lambda-calculus-curry-howard-lambek", "kind": "lambek_equivalence", "overlap": "Dropping thinness turns a Heyting algebra into a full Bicartesian Closed Category (STLC)", "formula": "\\rho_{35}: \\mathbf{HeytingAlg} \\leadsto \\mathbf{CCC} \\simeq \\mathbf{STLC}"},
    {"id": "rho-36", "source": "type-theory-russell-and-formation-intro-elim", "target": "simply-typed-lambda-calculus-curry-howard-lambek", "kind": "syntactic_category", "overlap": "Typing rules (Var, Abs, App) generate the syntactic category of STLC", "formula": "\\rho_{36}: (\\Gamma \\vdash t : B) \\in \\mathrm{Hom}_{\\mathbf{Syn}}(\\Gamma, B)"},
    {"id": "rho-37", "source": "categories-objects-morphisms-laws", "target": "functors-structure-preserving-maps", "kind": "morphism_of_categories", "overlap": "Functors F : C → D are homomorphisms preserving categorical composition and identities", "formula": "\\rho_{37}: (\\mathcal{C}, \\mathcal{D}) \\mapsto \\mathrm{Fun}(\\mathcal{C}, \\mathcal{D})"},
    {"id": "rho-38", "source": "functors-structure-preserving-maps", "target": "functors-across-monoids-orders-logic", "kind": "domain_instantiation", "overlap": "Specializing F : C → D to 1-object categories (monoids) and thin categories (posets)", "formula": "\\rho_{38}: F \\mapsto (f_{\\mathrm{mon}}, f_{\\mathrm{poset}})"},
    {"id": "rho-39", "source": "monoids-as-single-object-categories-free-monoids", "target": "functors-across-monoids-orders-logic", "kind": "monoid_functor", "overlap": "Functors BM → BN are exact monoid homomorphisms M → N", "formula": "\\rho_{39}: \\mathrm{Fun}(\\mathbf{B}M, \\mathbf{B}N) \\cong \\mathrm{Hom}_{\\mathbf{Mon}}(M, N)"},
    {"id": "rho-40", "source": "preorders-equivalence-and-thin-categories", "target": "functors-across-monoids-orders-logic", "kind": "poset_functor", "overlap": "Functors between thin categories are monotone order-preserving maps", "formula": "\\rho_{40}: \\mathrm{Fun}(P, Q) \\cong \\mathrm{Monotone}(P, Q)"},
    {"id": "rho-41", "source": "functors-structure-preserving-maps", "target": "programming-endofunctors-pointed-contravariant", "kind": "endofunctor_specialization", "overlap": "Endofunctors F : Type → Type on the category of programming types", "formula": "\\rho_{41}: F : \\mathbf{Type} \\to \\mathbf{Type}"},
    {"id": "rho-42", "source": "functors-across-monoids-orders-logic", "target": "programming-endofunctors-pointed-contravariant", "kind": "container_bridge", "overlap": "Free monoid List A and option Maybe A act as covariant endofunctors via .map", "formula": "\\rho_{42}: \\mathrm{List}(f) = \\mathrm{map}(f)"},
    {"id": "rho-43", "source": "simply-typed-lambda-calculus-curry-howard-lambek", "target": "programming-endofunctors-pointed-contravariant", "kind": "higher_kinded_types", "overlap": "Type constructors F : Type → Type and higher-order map in STLC/System F", "formula": "\\rho_{43}: \\Gamma \\vdash \\mathrm{map}_F : (A \\to B) \\to F A \\to F B"},
    {"id": "rho-44", "source": "functors-structure-preserving-maps", "target": "natural-transformations-and-naturality-squares", "kind": "higher_morphism", "overlap": "Natural transformations α : F ⇒ G are morphisms between parallel functors F, G : C → D", "formula": "\\rho_{44}: (F, G) \\mapsto \\mathrm{Nat}(F, G)"},
    {"id": "rho-45", "source": "programming-endofunctors-pointed-contravariant", "target": "natural-transformations-and-naturality-squares", "kind": "container_transform", "overlap": "Transforming container endofunctors F A → G A while commuting with .map(f)", "formula": "\\rho_{45}: \\mathrm{map}_G(f) \\circ \\alpha_A = \\alpha_B \\circ \\mathrm{map}_F(f)"},
    {"id": "rho-46", "source": "natural-transformations-and-naturality-squares", "target": "polymorphic-functions-and-categorical-equivalence", "kind": "parametricity", "overlap": "Polymorphic functions ∀a. F a → G a are natural transformations; invertible ones yield equivalence", "formula": "\\rho_{46}: \\mathrm{Nat}(F, G) \\cong \\forall a.\\; F\\;a \\to G\\;a"},
    {"id": "rho-47", "source": "programming-endofunctors-pointed-contravariant", "target": "polymorphic-functions-and-categorical-equivalence", "kind": "free_theorems", "overlap": "Polymorphic List/Maybe operations (reverse, safeHead) commute with map(f)", "formula": "\\rho_{47}: \\mathrm{reverse} \\circ \\mathrm{map}(f) = \\mathrm{map}(f) \\circ \\mathrm{reverse}"},
    {"id": "rho-48", "source": "natural-transformations-and-naturality-squares", "target": "functor-categories-vertical-horizontal-2-categories", "kind": "2_categorical_assembly", "overlap": "Composing natural transformations vertically and horizontally inside the 2-category Cat", "formula": "\\rho_{48}: (\\mathcal{C}, F, \\alpha) \\in \\mathbf{2Cat}"},
    {"id": "rho-49", "source": "polymorphic-functions-and-categorical-equivalence", "target": "functor-categories-vertical-horizontal-2-categories", "kind": "equivalence_in_2cat", "overlap": "Categorical equivalence C ≃ D is defined by natural isomorphisms η : Id ≅ GF, ε : FG ≅ Id in Cat", "formula": "\\rho_{49}: (\\mathcal{C} \\simeq \\mathcal{D}) \\in \\mathbf{Cat}_2"},
    {"id": "rho-50", "source": "functors-structure-preserving-maps", "target": "functor-categories-vertical-horizontal-2-categories", "kind": "functor_category_objects", "overlap": "Functors C → D become the objects of the functor category [C, D]", "formula": "\\rho_{50}: \\mathrm{Ob}([\\mathcal{C}, \\mathcal{D}]) = \\mathrm{Fun}(\\mathcal{C}, \\mathcal{D})"}
]

TWO_SIMPLICES = [
    {
        "id": "tau-01",
        "vertices": ["sets-subsets-empty-singleton", "functions-bijections-isomorphisms", "categories-objects-morphisms-laws"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Externalizing set functions into hom-sets and then abstracting bijections into categorical isomorphisms agrees with the direct specialization of C = Set."
    },
    {
        "id": "tau-02",
        "vertices": ["external-products-and-projections", "categorical-duality-and-coproducts", "categories-objects-morphisms-laws"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Dualizing universal product cones (A × B, π_i) into coproduct cocones (A + B, ι_i) commutes with their unified axiomatization inside any category C."
    },
    {
        "id": "tau-03",
        "vertices": ["monoids-semigroups-magmas", "groups-rotations-and-symmetries", "monoids-as-single-object-categories-free-monoids"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Enriching a monoid M with inverses to form a group G and then delooping to BG agrees with delooping M to BM and restricting to invertible endomorphisms Aut(•)."
    },
    {
        "id": "tau-04",
        "vertices": ["categories-objects-morphisms-laws", "monoids-semigroups-magmas", "monoids-as-single-object-categories-free-monoids"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Specializing categorical composition laws to a binary monoid operation ⋆ and then delooping to BM is the identity on 1-object categories."
    },
    {
        "id": "tau-05",
        "vertices": ["orders-hasse-diagrams-and-lattices", "birkhoff-representation-and-boolean-lattices", "preorders-equivalence-and-thin-categories"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Representing a distributive lattice L as a poset of subsets via Birkhoff's theorem and then viewing it as a thin category commutes with directly categorifying (L, ≤)."
    },
    {
        "id": "tau-06",
        "vertices": ["external-products-and-projections", "preorders-equivalence-and-thin-categories", "propositional-logic-as-category"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Restricting universal products A × B to thin categories (meets a ∧ b) and interpreting preorders as logical entailment yields logical conjunction P ∧ Q."
    },
    {
        "id": "tau-07",
        "vertices": ["propositional-logic-as-category", "implication-currying-and-intuitionistic-bhk", "heyting-and-boolean-algebras-bicartesian-closed"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Internalizing deduction P ⊢ Q as exponential implication P ⇒ Q and closing under ∧, ∨, ⊤, ⊥ yields the thin Bicartesian Closed structure of a Heyting algebra."
    },
    {
        "id": "tau-08",
        "vertices": ["type-theory-russell-and-formation-intro-elim", "inductive-types-nat-list-and-church-encodings", "simply-typed-lambda-calculus-curry-howard-lambek"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Defining ADTs via Formation/Intro/Elim rules and Church-encoding them into polymorphic lambda terms commutes with their interpretation inside the syntactic CCC of STLC."
    },
    {
        "id": "tau-09",
        "vertices": ["functors-structure-preserving-maps", "functors-across-monoids-orders-logic", "programming-endofunctors-pointed-contravariant"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Specializing general functors F : C → D to free monoids List(A) and to programming endofunctors Type → Type yields the exact same functorial .map laws."
    },
    {
        "id": "tau-10",
        "vertices": ["natural-transformations-and-naturality-squares", "polymorphic-functions-and-categorical-equivalence", "functor-categories-vertical-horizontal-2-categories"],
        "cohomology_status": "H^0 Exact (Commutes)",
        "commutativity_proof": "Interpreting natural transformations α : F ⇒ G as polymorphic functions ∀a. F a → G a and composing them vertically/horizontally commutes inside the 2-category Cat."
    }
]

NOTEBOOK_INVESTIGATIONS = [
    {
        "id": "q-internal-vs-external-lawvere",
        "question": "How does Marinov shift from the 'Internal Set View' (colored balls inside sets) to Lawvere's 'External Point-Free View' (opaque points and universal arrows)?",
        "open_cover": [
            "visual-abstraction-modes-of-knowledge",
            "sets-subsets-empty-singleton",
            "external-products-and-projections",
            "categorical-duality-and-coproducts",
            "categories-objects-morphisms-laws"
        ],
        "cohomology": {
            "gluing_status": "GLOBAL SECTION GLUED (H^0 Exact · 5 Stalks)",
            "verified_overlaps": 6
        },
        "synthesis_markdown": """### Global Section: From Internal Colored Balls to External Universal Arrows

#### 1. The Internal View (Set Theory, Chapter 1)
In Chapter 1 [p. 13], Marinov introduces a set $G$ by drawing **colored balls inside a boundary**: a set is defined *internally* by inspecting its elements.
- **Empty Set $\\emptyset$ [p. 16]:** Internally, the container with zero balls.
- **Singleton Set $1$ [p. 15]:** Internally, a container with one red ball.
- **Cartesian Product $A \\times B$ [p. 53]:** Internally, a rectangular grid of ordered pairs $(a, b)$.

#### 2. The External Point-Free Shift (Categories, Chapter 2)
When we cross into Category Theory [p. 52] [p. 82], **we erase the interior of every set** — objects become opaque points, and every property must be characterized *externally* purely by the pattern of morphisms pointing into or out of the object [p. 83]:
$$\\text{Internal Elements } x \\in A \\quad \\xrightarrow{\\text{Externalize}} \\quad \\text{Generalized Elements } 1 \\xrightarrow{x} A$$
- **Terminal Object $1$ [p. 75]:** The object receiving a unique morphism $!_A : A \\to 1$ from every object $A$ [p. 24].
- **Initial Object $0$ ($\\emptyset$) [p. 78]:** Dualizing $1$, the object sending a unique morphism $!^A : 0 \\to A$ to every object $A$ [p. 22].
- **Universal Product $A \\times B$ [p. 62] & Coproduct $A + B$ [p. 69]:** Characterized without ever mentioning elements via projections $(\\pi_1, \\pi_2)$ and injections $(\\iota_1, \\iota_2)$:
$$\\mathrm{Hom}(C, A \\times B) \\cong \\mathrm{Hom}(C, A) \\times \\mathrm{Hom}(C, B), \\qquad \\mathrm{Hom}(A + B, C) \\cong \\mathrm{Hom}(A, C) \\times \\mathrm{Hom}(B, C)$$"""
    },
    {
        "id": "q-six-worlds-rosetta-stone",
        "question": "How do the exact same categorical diagrams reappear across Sets, Monoids/Groups, Poset Lattices, Deductive Logic, and Programming Types?",
        "open_cover": [
            "categories-objects-morphisms-laws",
            "monoids-as-single-object-categories-free-monoids",
            "preorders-equivalence-and-thin-categories",
            "propositional-logic-as-category",
            "heyting-and-boolean-algebras-bicartesian-closed",
            "simply-typed-lambda-calculus-curry-howard-lambek"
        ],
        "cohomology": {
            "gluing_status": "GLOBAL SECTION GLUED (H^0 Exact · 6 Stalks)",
            "verified_overlaps": 7
        },
        "synthesis_markdown": """### Global Section: The 6-World Categorical Rosetta Stone (Chapters 1–6)

Marinov's central architectural arc [p. 9] [p. 203] [p. 260] demonstrates that six seemingly unrelated disciplines are **six local stalks of the same categorical sheaf**:

#### 1. Specializing by Object & Hom-Set Cardinality
- **Many Objects, Many Arrows ($\\mathbf{Set}$, Ch 1–2 [p. 83]):** Objects are sets $A, B$; morphisms are functions $f : A \\to B$.
- **One Object, Many Arrows ($\\mathbf{Mon}$ / $\\mathbf{Grp}$, Ch 3 [p. 115]):** Restricting to $|\\mathrm{Ob}(\\mathcal{C})| = 1$ turns objects into a single state $\\bullet$ and morphisms into monoid actions $m \\in M$ (or triangle rotations $0^\\circ, 120^\\circ, 240^\\circ$ when invertible [p. 104]).
- **Many Objects, At Most One Arrow ($\\mathbf{Preord}$ / $\\mathbf{Poset}$, Ch 4 [p. 156]):** Restricting to $|\\mathrm{Hom}(a,b)| \\le 1$ turns arrows into order relations $a \\le b$, products into meets $a \\wedge b$, and coproducts into joins $a \\vee b$ [p. 145].

#### 2. The Curry-Howard-Lambek Trinity (Chapters 5–6)
In a **Bicartesian Closed Category** [p. 203] [p. 260], Logic, Sets, and Programming Types align symbol-for-symbol:
$$\\begin{array}{l|c|c|c}
\\textbf{Categorical Concept} & \\textbf{Set Theory (Ch 1–2)} & \\textbf{Logic (Ch 5)} & \\textbf{Types / STLC (Ch 6)} \\\\ \\hline
\\text{Initial Object } 0 & \\emptyset \\text{ [p. 22]} & \\bot \\text{ (Falsity) [p. 165]} & \\mathrm{Void} / \\mathrm{Never} \\text{ [p. 234]} \\\\
\\text{Terminal Object } 1 & \\{\\bullet\\} \\text{ [p. 15]} & \\top \\text{ (Truth) [p. 165]} & \\mathrm{Unit} / () \\text{ [p. 234]} \\\\
\\text{Product } A \\times B & \\text{Cartesian Pair } (a,b) \\text{ [p. 53]} & P \\wedge Q \\text{ (AND) [p. 165]} & \\text{Tuple } (A, B) \\text{ [p. 234]} \\\\
\\text{Coproduct } A + B & \\text{Disjoint Union } A \\sqcup B \\text{ [p. 69]} & P \\vee Q \\text{ (OR) [p. 165]} & \\mathrm{Either}\\;A\\;B \\text{ [p. 236]} \\\\
\\text{Exponential } B^A & \\text{Function Set } A \\to B \\text{ [p. 24]} & P \\Rightarrow Q \\text{ [p. 180]} & \\text{Lambda } \\lambda x:A.\\; t : B \\text{ [p. 260]}
\\end{array}$$"""
    },
    {
        "id": "q-birkhoff-cube-trinity",
        "question": "Why do subset inclusion, RGB/CMY color mixing, and integer divisibility draw the exact same 3D Hasse cube in Chapter 4?",
        "open_cover": [
            "sets-subsets-empty-singleton",
            "orders-hasse-diagrams-and-lattices",
            "birkhoff-representation-and-boolean-lattices",
            "preorders-equivalence-and-thin-categories"
        ],
        "cohomology": {
            "gluing_status": "GLOBAL SECTION GLUED (H^0 Exact · 4 Stalks)",
            "verified_overlaps": 5
        },
        "synthesis_markdown": """### Global Section: Birkhoff's Representation Theorem & The 3D Order Cube

#### 1. Three Concrete Posets in Chapter 4
1. **Color-Mixing Lattice [p. 145]:** Ordering colors by pigment containment places primary colors at the atoms and composite colors at their joins $a \\vee b$.
2. **Divisibility Lattice of $30$ [p. 146]:** Ordering the divisors $\\{1, 2, 3, 5, 6, 10, 15, 30\\}$ by $a \\mid b$ places primes $\\{2, 3, 5\\}$ at the first level, with meet $a \\wedge b = \\gcd(a,b)$ and join $a \\vee b = \\mathrm{lcm}(a,b)$.
3. **Power-Set Inclusion $\\mathcal{P}(\\{x,y,z\\})$ [p. 147]:** Ordering subsets by $A \\subseteq B$, with meet $A \\cap B$ and join $A \\cup B$.

#### 2. Birkhoff's Representation Isomorphism [p. 148]
By **Birkhoff's Representation Theorem** [p. 148], every finite distributive lattice $L$ is canonically isomorphic to the lattice of downward-closed subsets of its join-irreducible (atomic/prime) elements:
$$L \\xrightarrow{\\sim} \\mathcal{O}(\\mathrm{Irr}(L)), \\qquad x \\mapsto \\{ p \\in \\mathrm{Irr}(L) \\mid p \\le x \\}$$
Because Prime Divisors $\\{2, 3, 5\\}$, Primary Colors $\\{\\text{R}, \\text{Y}, \\text{B}\\}$, and Singleton Subsets $\\{\\{x\\}, \\{y\\}, \\{z\\}\\}$ all have $3$ independent atoms, their Hasse diagrams are **categorically isomorphic 3-cubes** $2^3$."""
    },
    {
        "id": "q-type-intro-elim-universal",
        "question": "How do Type Formation, Introduction, Elimination, and Computation rules in Chapter 6 encode categorical universal properties and Church encodings?",
        "open_cover": [
            "external-products-and-projections",
            "categorical-duality-and-coproducts",
            "type-theory-russell-and-formation-intro-elim",
            "inductive-types-nat-list-and-church-encodings",
            "simply-typed-lambda-calculus-curry-howard-lambek"
        ],
        "cohomology": {
            "gluing_status": "GLOBAL SECTION GLUED (H^0 Exact · 5 Stalks)",
            "verified_overlaps": 5
        },
        "synthesis_markdown": """### Global Section: Universal Cones as Type Introduction & Elimination Rules

#### 1. The Four Rules Defining Any Type [p. 234–238]
In Chapter 6, Marinov shows that every programming data type (`Bool`, `Maybe a`, `Nat`, `List a`) is defined by four categorical rules:
1. **Type Formation [p. 234]:** Declares the object or endofunctor signature (e.g., $\\mathrm{Maybe} : \\mathbf{Type} \\to \\mathbf{Type}$).
2. **Term Introduction [p. 236]:** Canonical constructor arrows pointing *into* the type (e.g., $\\mathrm{Nothing} : 1 \\to \\mathrm{Maybe}\\;a$ and $\\mathrm{Just} : a \\to \\mathrm{Maybe}\\;a$, which are coproduct injections $\\iota_1, \\iota_2$ into $1 + a$).
3. **Term Elimination [p. 238]:** The universal mediating morphism pointing *out* of the type (e.g., $\\mathrm{maybe} : b \\to (a \\to b) \\to \\mathrm{Maybe}\\;a \\to b$, which is co-pairing $[f, g] : 1 + a \\to b$).
4. **Computation ($\\beta / \\eta$) [p. 238]:** The assertion that the elimination arrow composed with each introduction arrow commutes!

#### 2. Church Encodings as Pure Universal Elimination [p. 257]
Because an object in category theory is completely determined up to isomorphism by its universal elimination property, **Alonzo Church's encoding** [p. 257] identifies each type directly with its polymorphic eliminator:
$$\\mathrm{Maybe}\\;a \\;\\cong\\; \\forall b.\\; b \\to (a \\to b) \\to b, \\qquad \\mathrm{Nat} \\;\\cong\\; \\forall a.\\; a \\to (a \\to a) \\to a$$"""
    },
    {
        "id": "q-functors-natural-polymorphism",
        "question": "Why are functors F : C → D the universal bridge between categories, and why is every polymorphic function ∀a. F a → G a a natural transformation?",
        "open_cover": [
            "functors-structure-preserving-maps",
            "functors-across-monoids-orders-logic",
            "programming-endofunctors-pointed-contravariant",
            "natural-transformations-and-naturality-squares",
            "polymorphic-functions-and-categorical-equivalence",
            "functor-categories-vertical-horizontal-2-categories"
        ],
        "cohomology": {
            "gluing_status": "GLOBAL SECTION GLUED (H^0 Exact · 6 Stalks)",
            "verified_overlaps": 8
        },
        "synthesis_markdown": """### Global Section: Functors, Parametric Polymorphism & 2-Categories (Chapters 7–8)

#### 1. Functors Preserve Commuting Diagrams [p. 278–290]
A **functor** $F : \\mathcal{C} \\to \\mathcal{D}$ consists of an object mapping $A \\mapsto F(A)$ and a morphism mapping $(f : A \\to B) \\mapsto (F(f) : F(A) \\to F(B))$ obeying [p. 289–290]:
$$F(\\mathrm{id}_A) = \\mathrm{id}_{F(A)}, \\qquad F(g \\circ f) = F(g) \\circ F(f)$$
- Between one-object categories $\\mathbf{B}M \\to \\mathbf{B}N$, $F$ is a **monoid homomorphism** [p. 298].
- Between thin poset categories $P \\to Q$, $F$ is a **monotone map** [p. 301].
- On $\\mathbf{Type} \\to \\mathbf{Type}$, $F$ is a **container type constructor** (`List`, `Maybe`) with `.map` [p. 306–308].

#### 2. Natural Transformations & Polymorphic Free Theorems [p. 319–350]
A **natural transformation** $\\alpha : F \\Rightarrow G$ assigns a component arrow $\\alpha_A : F(A) \\to G(A)$ to every object $A$ such that for any $f : A \\to B$ [p. 319]:
$$G(f) \\circ \\alpha_A = \\alpha_B \\circ F(f)$$
In programming [p. 342–350], any parametrically polymorphic function $\\alpha : \\forall a.\\; F\\;a \\to G\\;a$ (such as $\\mathrm{reverse} : \\mathrm{List}\\;a \\to \\mathrm{List}\\;a$ or $\\mathrm{take}_1 : \\mathrm{List}\\;a \\to \\mathrm{Maybe}\\;a$) cannot inspect the elements of type $a$; therefore, **mapping $f$ over the container before or after applying $\\alpha$ is guaranteed to commute** [p. 348]."""
    },
    {
        "id": "q-marinov-vs-spivak-bridge",
        "question": "How do Marinov's 'Category Theory Illustrated' (377 pp.) and Spivak's 'Category Theory for the Sciences' (609 pp.) compare and glue together?",
        "open_cover": [
            "visual-abstraction-modes-of-knowledge",
            "categories-objects-morphisms-laws",
            "propositional-logic-as-category",
            "simply-typed-lambda-calculus-curry-howard-lambek",
            "functors-structure-preserving-maps",
            "functor-categories-vertical-horizontal-2-categories"
        ],
        "cohomology": {
            "gluing_status": "CROSS-CORPUS SECTION GLUED (Marinov 377 pp. × Spivak 609 pp.)",
            "verified_overlaps": 6
        },
        "synthesis_markdown": """### Global Section: Cross-Corpus Gluing — Marinov (Visual/CHL) $\\times$ Spivak (Ologs/Sheaves)

Gluing Boris Marinov's *Category Theory Illustrated* (`377 pp.`) with David I. Spivak's *Category Theory for the Sciences* (`609 pp.`) over their shared core ($\\mathbf{Set}$, $\\mathbf{Poset}$, $\\mathbf{Mon}$, $\\mathbf{Cat}$, Functors, and Natural Transformations) reveals a complementary duality:

1. **Pedagogical Entry Point:**
   - **Marinov [p. 11–94]:** Starts with **visual spatial intuition** — colored balls inside sets, gradually erasing internal elements until only external universal arrows remain.
   - **Spivak (Ch 1–2):** Starts with **Ontology Logs (Ologs)** — English noun-phrase boxes and verb-phrase arrows modeling scientific schemas in $\\mathbf{Set}$.
2. **Signature Culmination:**
   - **Marinov (Ch 5–8 [p. 162–374]):** Culminates in the **Curry-Howard-Lambek Rosetta Stone** (Logic $\\simeq$ Types $\\simeq$ Bicartesian Closed Categories), **Church Encodings** [p. 257], **Parametric Polymorphism** (`reverse`, `head` [p. 342–350]), and **2-Categories** [p. 369].
   - **Spivak (Ch 4–7):** Culminates in the **Functorial Data Model** ($\\mathbf{Cat} \\simeq \\mathbf{Sch}$), **Adjoint Data Migration** ($\\Sigma_F \\dashv \\Delta_F \\dashv \\Pi_F$), **Kleisli Monads / Operads**, and **Sheaves on Topological Spaces**.
3. **Why Both Together Form the Complete Curriculum:**
   Marinov makes every symbol **visually self-evident and executable in code** (TypeScript/Haskell ADTs & lambda terms), while Spivak scales those exact same universal constructions to **relational databases, scientific modeling, and sheaf cohomology**."""
    }
]


def clean_page_text(raw: str) -> str:
    lines = []
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.match(r"^\d{1,2}/\d{1,2}/\d{2},\s*\d{1,2}:\d{2}\s*[AP]M\s+Category Theory Illustrated", s):
            continue
        if s.startswith("https://abuseofnotation.github.io/category-theory-illustrated/"):
            continue
        lines.append(s)
    return "\n".join(lines)


def chapter_for_page(pno: int) -> int:
    for ch in CHAPTERS:
        if ch["start_page"] <= pno <= ch["end_page"]:
            return ch["chapter"]
    return 1 if pno < 3 else 8


def stalks_for_page(pno: int):
    matched = [s["id"] for s in STALKS if s["start_page"] <= pno <= s["end_page"]]
    if not matched:
        if pno < 3:
            matched = [STALKS[0]["id"]]
        else:
            matched = [STALKS[-1]["id"]]
    return matched


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "chapters").mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / "concepts").mkdir(parents=True, exist_ok=True)

    raw_pages = json.loads(RAW_PAGES_JSON.read_text(encoding="utf-8"))
    pages_data = []
    formal_items = []
    sections_index = []

    current_section = "Prologue: About Category Theory Illustrated"
    def_idx, thm_idx, task_idx = 0, 0, 0

    for row in raw_pages:
        pno = row["page"]
        txt = clean_page_text(row["text"])
        ch_num = chapter_for_page(pno)
        s_ids = stalks_for_page(pno)
        lines = [l.strip() for l in txt.splitlines() if l.strip()]

        # Detect section headers
        if lines:
            first = lines[0]
            if (
                len(first) < 52
                and not first.endswith(".")
                and not first.startswith("Task ")
                and first not in ("DEFINITION:", "THEOREM:", "Answers")
                and re.match(r"^[A-Z\"][A-Za-z0-9\s,\-–—’'/:?()]+$", first)
            ):
                current_section = first
                sections_index.append({"page": pno, "chapter": ch_num, "title": current_section})

        page_item_ids = []
        # Extract DEFINITION:, THEOREM:, and Task N: blocks on this page
        for i, l in enumerate(lines):
            if l == "DEFINITION:":
                def_idx += 1
                snippet = " ".join(lines[i + 1 : min(len(lines), i + 5)])[:360]
                title_guess = lines[i - 1][:65] if i > 0 and len(lines[i - 1]) < 65 else f"Visual Definition {def_idx}"
                item_id = f"Definition-{ch_num}.{def_idx}"
                page_item_ids.append(item_id)
                formal_items.append({
                    "id": item_id,
                    "kind": "Definition",
                    "number": f"{ch_num}.{def_idx}",
                    "title": title_guess,
                    "page": pno,
                    "chapter": ch_num,
                    "section": current_section,
                    "stalk_ids": s_ids,
                    "text": snippet or txt[:300],
                    "references": [f"p.{pno}"]
                })
            elif l == "THEOREM:":
                thm_idx += 1
                snippet = " ".join(lines[i + 1 : min(len(lines), i + 5)])[:360]
                title_guess = lines[i - 1][:65] if i > 0 and len(lines[i - 1]) < 65 else f"Visual Theorem {thm_idx}"
                item_id = f"Theorem-{ch_num}.{thm_idx}"
                page_item_ids.append(item_id)
                formal_items.append({
                    "id": item_id,
                    "kind": "Theorem",
                    "number": f"{ch_num}.{thm_idx}",
                    "title": title_guess,
                    "page": pno,
                    "chapter": ch_num,
                    "section": current_section,
                    "stalk_ids": s_ids,
                    "text": snippet or txt[:300],
                    "references": [f"p.{pno}"]
                })
            else:
                m_task = re.match(r"^Task\s+(\d+)\s*:\s*(.*)$", l)
                if m_task:
                    task_idx += 1
                    t_num = m_task.group(1)
                    rest = m_task.group(2)
                    more = " ".join(lines[i + 1 : min(len(lines), i + 4)])
                    snippet = (rest + " " + more).strip()[:360]
                    item_id = f"Task-{ch_num}.{task_idx}"
                    page_item_ids.append(item_id)
                    formal_items.append({
                        "id": item_id,
                        "kind": "Exercise",
                        "number": f"{ch_num}.{task_idx} (Task {t_num})",
                        "title": f"Interactive Task {t_num} ({current_section})",
                        "page": pno,
                        "chapter": ch_num,
                        "section": current_section,
                        "stalk_ids": s_ids,
                        "text": snippet or l,
                        "references": [f"p.{pno}"]
                    })

        pages_data.append({
            "page": pno,
            "chapter": ch_num,
            "section": current_section,
            "subsection": current_section,
            "stalk_ids": s_ids,
            "items": page_item_ids,
            "references": [],
            "word_count": len(txt.split()),
            "text": txt
        })

    # Attach formal items to each stalk
    for s in STALKS:
        s_items = [it for it in formal_items if s["id"] in it["stalk_ids"]]
        if not s_items:
            # Synthesize a canonical anchor item from the stalk's formal core if a short page range had no literal marker
            anchor = {
                "id": f"Principle-{s['chapter']}.{s['symbol']}",
                "kind": "Definition",
                "number": s["section"],
                "title": s["title"],
                "page": s["start_page"],
                "chapter": s["chapter"],
                "section": s["title"],
                "stalk_ids": [s["id"]],
                "text": s["summary"],
                "references": [f"p.{s['start_page']}"]
            }
            formal_items.append(anchor)
            s_items = [anchor]
        s["formal_items"] = s_items
        s["extracted_items_count"] = len(s_items)

    # Write Persistent LLM Wiki (HOME.md + 8 Chapter Hubs + 24 Concept Stalk Pages)
    home_md = [
        "# Category Theory Illustrated — Alexandrov Sheaf Wiki (`HOME.md`)\n",
        "**Author:** Boris Marinov (Jencel Panic) · **Pages:** 377 · **Stalks:** 24 · **Restrictions:** 50 · **2-Simplices:** 10 · **Declarations:** " + str(len(formal_items)) + "\n",
        "## Chapter Hubs\n"
    ]
    for ch in CHAPTERS:
        home_md.append(f"- [{ch['title']}](chapters/{ch['id']}.md) (`pp. {ch['start_page']}–{ch['end_page']}`)")
        ch_stalks = [s for s in STALKS if s["chapter"] == ch["chapter"]]
        ch_lines = [
            f"# {ch['title']}\n",
            f"**Page Span:** `pp. {ch['start_page']}–{ch['end_page']}`\n",
            f"**Theme:** {ch['theme']}\n",
            "## Global Invariants\n"
        ]
        for inv in ch["global_invariants"]:
            ch_lines.append(f"- {inv}")
        ch_lines.append("\n## Concept Stalks in this Chapter\n")
        for s in ch_stalks:
            ch_lines.append(f"- [{s['title']}](../concepts/{s['id']}.md) (`§{s['section']}`, `pp. {s['start_page']}–{s['end_page']}`): {s['summary']}")
        (WIKI_DIR / "chapters" / f"{ch['id']}.md").write_text("\n".join(ch_lines) + "\n", encoding="utf-8")

    home_md.append("\n## All 24 Concept Stalks (`0-Simplices`)\n")
    for s in STALKS:
        home_md.append(f"- [{s['title']}](concepts/{s['id']}.md) (`pp. {s['start_page']}–{s['end_page']}`)")
        in_morphs = [r for r in RESTRICTION_MORPHISMS if r["target"] == s["id"]]
        out_morphs = [r for r in RESTRICTION_MORPHISMS if r["source"] == s["id"]]
        c_lines = [
            f"# {s['title']} (`{s['symbol']}`)\n",
            f"- **Chapter:** {s['chapter']} (`§{s['section']}`)",
            f"- **Page Fiber:** `pp. {s['start_page']}–{s['end_page']}`",
            f"- **Layer:** {s['layer']}\n",
            "## Summary\n",
            s["summary"] + "\n",
            "## Formal Categorical Core\n",
            f"$${s['formal_core']}$$\n",
            "## Local Olog (`types` & `aspects`)\n"
        ]
        for t in s["olog"]["types"]:
            c_lines.append(f"- **Type `{t['id']}`:** {t['label']}")
        for a in s["olog"]["aspects"]:
            c_lines.append(f"- **Aspect:** `{a['src']}` —*{a['label']}*→ `{a['dst']}`")
        c_lines.append("\n## Restriction Morphisms (`1-Simplices`)\n")
        for r in out_morphs:
            c_lines.append(f"- **Outgoing `{r['id']}` → [{r['target']}]({r['target']}.md):** {r['overlap']} (`${r['formula']}$`)")
        for r in in_morphs:
            c_lines.append(f"- **Incoming `{r['id']}` ← [{r['source']}]({r['source']}.md):** {r['overlap']} (`${r['formula']}$`)")
        c_lines.append(f"\n## Extracted Definitions, Theorems & Tasks ({len(s['formal_items'])})\n")
        for it in s["formal_items"][:25]:
            c_lines.append(f"- **{it['id']}** (`[p. {it['page']}]` · *{it['title']}*): {it['text']}")
        (WIKI_DIR / "concepts" / f"{s['id']}.md").write_text("\n".join(c_lines) + "\n", encoding="utf-8")

    (WIKI_DIR / "HOME.md").write_text("\n".join(home_md) + "\n", encoding="utf-8")

    # Build SQLite + FTS5 Database
    db_path = DATA_DIR / "cattheory_sheaf.db"
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE chapters (
            chapter INTEGER PRIMARY KEY,
            id TEXT,
            title TEXT,
            start_page INTEGER,
            end_page INTEGER,
            theme TEXT,
            global_invariants_json TEXT
        );
        CREATE TABLE stalks (
            id TEXT PRIMARY KEY,
            title TEXT,
            chapter INTEGER,
            section TEXT,
            start_page INTEGER,
            end_page INTEGER,
            layer TEXT,
            symbol TEXT,
            summary TEXT,
            formal_core TEXT,
            olog_json TEXT,
            formal_items_json TEXT
        );
        CREATE TABLE restriction_morphisms (
            id TEXT PRIMARY KEY,
            source TEXT,
            target TEXT,
            kind TEXT,
            overlap TEXT,
            formula TEXT
        );
        CREATE TABLE pages (
            page INTEGER PRIMARY KEY,
            chapter INTEGER,
            section TEXT,
            subsection TEXT,
            stalk_ids_json TEXT,
            items_json TEXT,
            references_json TEXT,
            word_count INTEGER,
            text TEXT
        );
        CREATE TABLE formal_items (
            id TEXT,
            kind TEXT,
            number TEXT,
            title TEXT,
            page INTEGER,
            chapter INTEGER,
            section TEXT,
            stalk_ids_json TEXT,
            text TEXT,
            references_json TEXT
        );
        CREATE VIRTUAL TABLE pages_fts USING fts5(page UNINDEXED, section, items, text);
        CREATE VIRTUAL TABLE items_fts USING fts5(id, kind, title, page UNINDEXED, section, text);
        CREATE VIRTUAL TABLE formal_items_fts USING fts5(id, kind, title, page UNINDEXED, section, text);
    """)

    for ch in CHAPTERS:
        cur.execute(
            "INSERT INTO chapters VALUES (?, ?, ?, ?, ?, ?, ?)",
            (ch["chapter"], ch["id"], ch["title"], ch["start_page"], ch["end_page"], ch["theme"], json.dumps(ch["global_invariants"]))
        )
    for s in STALKS:
        cur.execute(
            "INSERT INTO stalks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (s["id"], s["title"], s["chapter"], s["section"], s["start_page"], s["end_page"], s["layer"], s["symbol"], s["summary"], s["formal_core"], json.dumps(s["olog"]), json.dumps(s["formal_items"]))
        )
    for m in RESTRICTION_MORPHISMS:
        cur.execute(
            "INSERT INTO restriction_morphisms VALUES (?, ?, ?, ?, ?, ?)",
            (m["id"], m["source"], m["target"], m["kind"], m["overlap"], m["formula"])
        )
    for p in pages_data:
        cur.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (p["page"], p["chapter"], p["section"], p["subsection"], json.dumps(p["stalk_ids"]), json.dumps(p["items"]), json.dumps(p["references"]), p["word_count"], p["text"])
        )
        cur.execute(
            "INSERT INTO pages_fts VALUES (?, ?, ?, ?)",
            (str(p["page"]), p["section"], " ".join(p["items"]), p["text"])
        )
    for it in formal_items:
        cur.execute(
            "INSERT INTO formal_items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (it["id"], it["kind"], it["number"], it["title"], it["page"], it["chapter"], it["section"], json.dumps(it["stalk_ids"]), it["text"], json.dumps(it["references"]))
        )
        cur.execute(
            "INSERT INTO items_fts VALUES (?, ?, ?, ?, ?, ?)",
            (it["id"], it["kind"], it["title"], str(it["page"]), it["section"], it["text"])
        )
        cur.execute(
            "INSERT INTO formal_items_fts VALUES (?, ?, ?, ?, ?, ?)",
            (it["id"], it["kind"], it["title"], str(it["page"]), it["section"], it["text"])
        )
    conn.commit()
    conn.close()

    full_kb = {
        "book": {
            "title": "Category Theory Illustrated",
            "author": "Boris Marinov (Jencel Panic)",
            "publisher": "Illustrated Open Monograph (CC BY-NC 4.0, Drawn in Inkscape, Set in Mell Sans)",
            "isbn": "https://abuseofnotation.github.io/category-theory-illustrated/",
            "pdf_url": "category-theory-illustrated.pdf",
            "total_pages": len(pages_data),
            "total_formal_items": len(formal_items),
            "total_stalks": len(STALKS),
            "total_restriction_morphisms": len(RESTRICTION_MORPHISMS),
            "total_2_simplices": len(TWO_SIMPLICES),
            "voice_profile": {
                "epistemology": "Point-Free Visual Externalism & Curry-Howard-Lambek Rosetta Stone (In Memory of F. William Lawvere)",
                "design_register": "Geometric Inkscape Sketchbook & 6-World Rosetta Atlas",
                "signature_instruments": [
                    "Lawvere Internal (Colored Balls) ↔ External (Universal Arrows) Perspective Shifter",
                    "6-World Rosetta Stone Translator (Sets · Categories · Monoids · Orders · Logic · Types)",
                    "Sheaf Open-Cover Notebook & Interactive Task Explorer",
                    "Cross-Corpus Gluing Bridge: Marinov (377 pp.) × Spivak (609 pp.)"
                ]
            }
        },
        "chapters": CHAPTERS,
        "stalks": STALKS,
        "restriction_morphisms": RESTRICTION_MORPHISMS,
        "two_simplices": TWO_SIMPLICES,
        "sections_index": sections_index,
        "formal_items": formal_items,
        "pages": [
            {
                "p": p["page"],
                "ch": p["chapter"],
                "sec": p["section"],
                "sub": p["subsection"],
                "stalks": p["stalk_ids"],
                "items": p["items"],
                "refs": p["references"],
                "wc": p["word_count"],
                "txt": p["text"]
            }
            for p in pages_data
        ]
    }
    kb_path = DATA_DIR / "sheaf_kb.json"
    existing_podcast_by_id = {}
    if kb_path.exists():
        try:
            old_kb = json.loads(kb_path.read_text(encoding="utf-8"))
            for old_inv in old_kb.get("notebook_investigations", []):
                if old_inv.get("id") and old_inv.get("podcast_turns"):
                    existing_podcast_by_id[old_inv["id"]] = {
                        k: old_inv[k]
                        for k in ("audio_file", "audio_duration_sec", "audio_engine", "podcast_hosts", "podcast_turns")
                        if k in old_inv
                    }
        except Exception:
            pass

    full_kb["notebook_investigations"] = [
        {
            **inv,
            "citations": [
                {
                    "page": p,
                    "label": f"p. {p}",
                    "section": pages_data[p - 1]["section"]
                }
                for p in sorted({
                    int(m) for m in re.findall(r"\[p\.\s*(\d+)", inv["synthesis_markdown"])
                    if 1 <= int(m) <= len(pages_data)
                })
            ],
            **existing_podcast_by_id.get(inv["id"], {})
        }
        for inv in NOTEBOOK_INVESTIGATIONS
    ]

    kb_path.write_text(json.dumps(full_kb, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built Category Theory Illustrated Sheaf KB: {len(pages_data)} pages, {len(STALKS)} stalks, {len(RESTRICTION_MORPHISMS)} restrictions, {len(formal_items)} formal declarations/tasks.")


if __name__ == "__main__":
    main()
