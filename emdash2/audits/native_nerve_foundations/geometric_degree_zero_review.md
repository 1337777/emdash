# Geometric degree zero and all-degree cube maps

Date: 2026-10-27
Status: checked non-library all-degree maps and first zero round trip; whole terminal reconstruction remains open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [reverse replay extensions](reverse_verification.json)

## Actual zero maps

Write G(A,B)=Functor_oplax_cat(A,B). The
[zero-degree construction](geometric_zero.lpfragment) uses actual maps

```text
d₀ : G(Terminal,C) → C          evaluation at Terminal_obj
e₀ : C → G(Terminal,C)          encoded constant diagrams.
```

The constant map is the OddDual image of ordinary constant-diagram
introduction followed by the existing Cartesian-to-ordinary inclusion.
Its source inside the encoding remains OddDual_cat(Terminal_cat). No equation
OddDual_cat(Terminal_cat)=Terminal_cat or G(Terminal,C)=C is installed.

Object recovery and recovery of an arbitrary original arrow compute. An
unrelated replacement arrow is rejected. The first complete round trip
`d₀ ∘ e₀ ≐ id_C` is derived by staging OddDual composition and the generic
constant/evaluation comparison below. It also recovers an arbitrary whole
K-parameter family D:K→C after encoding and decoding.

## Structural beta and unresolved eta

The [generic whole comparison](constant_evaluation_beta.lpfragment) is

```text
evaluate_i ∘ Cartesian-inclusion ∘ Const_func_func(I,C) ≐ id_C.
```

This is an explicit structural weakening/evaluation beta contract at the
existing constant-functor owner. It was not derivable by the attempted typed
reflexivity from the earlier point computations. The source keeps both
runtime presentations, retains the actual Cartesian inclusion, and applies
only to the constant-diagram constructor. Replacing that constructor with
an arbitrary V:C→Cart(I,C) is rejected. There is no general terminal-source
runtime eta or mapping-category identification.

The opposite-profile reconstruction `e₀ ∘ d₀ ≐ id_G(Terminal,C)` remains
unproved. The [isolated ordinary eta attempt](geometric_zero_eta_pending.lpfragment)
also fails already at

```text
Cartesian-inclusion ∘ Const_func_func(Terminal,C) ∘ evaluate_*
  ≐ id_L(Terminal,C),
```

where L is the ordinary Functor_cat. Thus the current failure is not confined
to the OddDual presentation. The second declaration in the latest pending
file is not reached; the earlier opposite-profile failure has its own receipt.
These are failed proof attempts, not mathematical counterexamples.

Before strengthening an eta contract, inspect the retained transformation
unit action and the complete generic terminal-mapping interface. A point or
arrow readback does not prove whole reconstruction. Do not substitute a new
native inverse axiom or a blanket category fold for that work. The independent
mixed-evaluator compatibility equation from the preceding checkpoint remains
open as well.

## One interface in every dimension

The [all-degree construction](geometric_cube_all_degrees.lpfragment) uses an
independent geometric shape family:

```text
Shape₀ = Terminal
Shapeₙ₊₁ = GrayCubePos_R(n).

Decodeₙ : G(Shapeₙ,C) → CubicalLevel(C,n)
Encodeₙ : CubicalLevel(C,n) → G(Shapeₙ,C).
```

Both maps are internal Nat eliminations. Their zero clauses are the maps
above; successor clauses are the previously constructed positive maps.
All four zero/successor equations and whole Hom action at variable n check.
This is complete dimension indexing of the actual maps, not a redefinition
of native cubes as geometric diagrams. It is also not yet a natural
equivalence over the cube index: common-index action, inverse laws and
degeneracies remain required.

## Qualification

The final **69-input** replay passes with subject reduction in **108.523s /
615,940 KiB**. It includes the earlier positive-dimensional constructions,
whole reindexing/reflection and the new unit controls. A preceding 180-second
run timed out during unchanged imports before reaching the interaction proof.
The final combined scope used explicit 300s / 2 GiB headroom; defaults, file
limits, serialization and the no-swap guard are unchanged. The interaction
was also checked at its smaller owning scope.

Two inherited raw-profile composition overlap reports surfaced in this
import order. A [generic typed join](geometric_zero_interactions.lpfragment)
is proved by staging the raw-view composition equation before substituting
functor images; it covers arbitrary image functors, including core inclusion.
No additional rule was added for those overlaps. The final warning inventory
is 2,230 critical-pair reports and 181 replaceable patterns, versus 2,228/181
in the preceding scope, with no parser issues. The source audit has no
unreviewed compound inferred slots. This is not global confluence qualification.

`replay_reverse.py` adds `zero`, `all-degrees`, and `zero-eta-pending` modes.
The last reproduces the failed ordinary eta proof and is excluded from the
green gates. `--assemble-only` checks exact sources without another Lambdapi
run. Previous modes retain their original snapshots. Production sources,
frontend transfer, health/final CI and manuscript claims are not promoted by
this isolated checkpoint.
