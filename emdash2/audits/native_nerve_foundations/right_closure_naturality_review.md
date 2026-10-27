# Right-closure naturality and tensor composition

Date: 2026-10-27
Status: qualified non-library structural target-naturality contract and derived shape-map laws; remaining internal/index coherence stays open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [exact naturality/composition/collapse replay modes](reverse_verification.json)

The [later split-map construction](geometric_first_faces_review.md) now
separates the first-coordinate face and projection, and derives the uniform
whole geometric face-degeneracy identity. The collapse-only boundary below
records this checkpoint; the full common-index and native compatibility
requirements remain open.

## What is structural and what is derived

The pre-existing right closure provides curry/uncurry and inverse paths at
fixed A,B,C. Those paths alone do not specify naturality between different
targets. The attempted whole reflexivity proof fails in that source. An
arbitrary choice of inverse bijections at each parameter would retain the
two inverse equations without necessarily commuting with target maps.

The [new interface](right_closure_naturality.lpfragment) explicitly supplies
target naturality for the selected canonical right closure. This is an
additional **structural contract**, not a theorem proved from the former
point projections or inverse paths. Right-closure naturality is part of the
usual adjunction specification; see [Ara–Guetta v1, §5](https://arxiv.org/html/2503.08832v1#S1).
The semantic choice is the canonical closure, not arbitrary independently
chosen mapping equivalences. The checker validates the typed interface and
its consumers; it does not by itself construct an external semantic model.

Write L for Functor_cat and G₀ for the existing explicit GrayHom_lax profile.
The ordinary view of curry is the actual composite

```text
C_R(A,B,C) : L(A⊗ᴿB,C) → L(A,G₀(B,C))
           = include ∘ curry_R ∘ admit.

P_B(H) : G₀(B,C) → G₀(B,D)
       = admit ∘ postcompose(H) ∘ include.
```

The declared structural path is the whole functor equality

```text
C_R(A,B,D) ∘ postcompose(H)
  ≐ postcompose(P_B(H)) ∘ C_R(A,B,C).
```

It retains all input-diagram action at fixed H:C→D. The canonical admission
and inclusion remain explicit; their whole categories are not identified.
No caller supplies this law, and no operational map accepts an equality or
coherence argument. No rewrite or unification rule is added.

From this one structural path, the [proof definitions](tensor_left_composition.lpfragment)
derive coevaluation naturality, source naturality for each complete H,
reflection through the existing curry/uncurry inverses, and

```text
tensor_left(G) ∘ tensor_left(F) ≐ tensor_left(G∘F).
```

The first-factor action itself is unchanged. The derived source relation is
a path for each complete tensor diagram H; assembly of the whole
source-naturality square on its mapping category is not claimed here.
Neither a mixed-exchange inverse nor a native nerve inverse is supplied.

## Concrete coordinate-collapse consumer

The [collapse construction](tensor_coordinate_collapse.lpfragment) is a whole
functor A→L(A⊗ᴿB,A⊗ᴿB), formed by constant-functor introduction and the
already defined first-factor tensor action. At a it is Cₐ=tensor_left(const(a)).
The new composition theorem derives

```text
Cₐ ∘ Cᵦ ≐ Cₐ,                 hence Cₐ ∘ Cₐ ≐ Cₐ.
curry_R(Cₐ) ≐ const_A(coevaluation(A,B)[a]).
```

Thus the whole B-diagram selected at a survives. The source/target endpoints
of WalkingArrow give actual collapses of every walking-first tensor shape.
These are coordinate-collapse endomorphisms; their factorization into the
separate face and degeneracy maps remains required. They are not labelled
as a completed cubical-index action.

## Qualification

The naturality/composition scope passes on 19 inputs in **78.899s /
309,896 KiB**. The concrete collapse scope passes on 21 inputs in **94.662s /
312,820 KiB**. Both use subject reduction at 180s / 2 GiB. All five warning
inventory fields match the prior tensor-action check: 2,282 critical-pair
reports and 181 replaceable patterns, with no parser issues.

Controls reject replacing H by an unrelated target functor in the structural
law and preserve the original lax cell through profile postcomposition. An
unrelated cell and the wrong retained collapse endpoint are rejected. The
derived tensor composition also specializes correctly at identity.

The failed pre-contract proof has its own exact `curry-naturality-pending`
replay. `tensor-composition` and `tensor-collapse` retain the positive scopes;
`--assemble-only` checks exact source identity without another checker run.
The source naturality assembly, other tensor factor, common-index
face/degeneracy laws, mixed-evaluation equation, native walking reconstruction
and production promotion remain open.
