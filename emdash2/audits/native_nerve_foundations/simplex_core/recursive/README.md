# Internal native simplex-level recursion

Date: 2026-10-28
Status: qualified isolated recursive native coefficients and filler functors; geometric successor, index structure and equivalences remain open
Parent: [simplex core](../README.md)
Evidence: [exact scopes and receipts](../verification.json)

## Whole construction

Write T=Op_cat, R=CoAbove2_cat, O=TotalOp_cat, N=LaxArrow_cat and
P_C=PathOut_cat_func(C). The [step](step.lpfragment) uses

```text
S⁻_K(E) = O(Σ_(R K) TotalOp_catd(E))
Step(H)(C) = S⁻_(T C)(H ∘ P_C).
```

Negative Sigma is an actual derived coefficient functor
`Functor_cart_cat(K,Cat_cart) → Cat_cart`. Its action and negative base change
use existing Sigma/duality owners. For F:C→D, the step map is the composite

```text
S⁻(H ∘ P_C) → S⁻((H ∘ P_D) ∘ T(F)) → S⁻(H ∘ P_D).
```

The first map uses H on the whole PathOut family map; the second changes the
base. Its base and fibre observations retain F, H and the whole fibre object.

Two structural internalizations are explicit: the Cartesian PathOut family
map, whose components are the existing `pathout_map_func`, and the whole
coefficient step. Their higher parameter profiles are not inferred merely
from point agreement. The step has a stable first-Hom ladder in C and in H;
its coefficient-transformation component is a defined negative Sigma map.
At the existing source/target arrow coefficients those components recover the
already checked whole triangle faces 01 and 02.

The [internal Nat recursion](coefficients.lpfragment) is

```text
H₀ = N_coeff
Hₙ₊₁ = Step(Hₙ)
NS₀(C) = C
NSₙ₊₁(C) = Hₙ(C).
```

This preserves the existing degree-one action. It does not assume the whole
coefficient equation Step(id)=N_coeff. Degrees zero, one and two compute to
C, N(C) and the previous independent triangle total. The variable-n map and
its whole first-Hom action are actual internal terms, with unit/composition
comparisons and both first-action projection orders checked. No external
boundary certificates or equality proofs are inputs to these maps.

## Higher-cell consumer

The [filler functors](filler_functors.lpfragment) construct whole inclusions
from the triangle and tetrahedron filler categories. They use `homd_` before
fibrewise total reversal; using the dual fibre instead would preserve filler
objects but reverse the higher-cell direction.

A whole functor takes genuine C 3-cells Ω:c∘a⇒b to NS₃(C). This consumer fixes
the three terminal vertices, while the generic tetrahedron-filler inclusion
has arbitrary outgoing-path objects and arrows. Its object computation gives
the existing native 3-simplex constructor, and replacing Ω by an unrelated Ψ
is rejected. These are [checked computations](qualification.lpfragment), not
an object-only declaration or a geometric definition of the native source.

One generic strict-functor composition view is needed to type the whole
filler-image functor. Its [proof](composition_proof.lpfragment) passes on the
unchanged production core without the new rule (31.727s / 168,388 KiB).
The [view](composition_view.lpfragment) matches the actual composite and both
functor-image heads, retaining every original arrow and endpoint. Removing
only it restores the expected filler-functor typing failure.

The [deep nested readback](deep_readback_pending.lpfragment) remains an
explicit failing inference experiment, including after the composition view.
It is not used as the constructor or as the accepted whole filler-functor
consumer. No new rule was added merely to force that projection chain.

## Qualification and remaining scope

The selected 39-input scope passes in 92.337s / 237,192 KiB with subject
reduction, the explicit 180s/2GiB profile and the existing GC setting. The
35-input existing-owner baseline passed in 99.317s. The selected 1,942
critical-pair and 178 replaceable-variable warnings have a clean parser
inventory; 18 critical-pair warnings are added relative to that baseline.
They concern the new step coefficient/operator action and generic
identity/composition/projection owners. Whole comparisons and actual
projection orders pass; complete literal constructor-unit/composite
normalization and confluence are not claimed. The receiver's production
sources and frontend pins are unchanged.

This is an internal Nat-indexed family of whole native constructions. It is
not yet a simplicial functor with all faces/degeneracies, a uniform geometric
realization, or a proved nerve equivalence. The degree-one coefficient
compatibility, geometric successor, whole comparison maps/inverses, remaining
triangle boundary identifications and promotion gates stay open.

Replay from the repository root using the parent `replay.py` and modes
`recursive-core`, `recursive-dependencies`, `recursive-composition-proof`,
`recursive-filler-omission`, or `recursive-deep-readback-pending`.

## Next geometric feasibility slice

Review the existing terminal join against the checked higher triangle and a
nonidentity cross-cell consumer. Active `Prof_transf_cat` is a `Functord_cat`
over a product base; older “ordinary simplex” comments alone do not establish
either a truncation or the needed higher mapping-category universality.
`join_mapping_recursion` currently distinguishes its object mapping data
from a whole mapping-category equivalence. Preserve that qualification.

The abstract of [Ara–Maltsiniotis, version 4](https://arxiv.org/abs/1607.00668v4)
distinguishes strict ∞-categorical joins from ordinary joins up to truncation
and qualifies higher lax/oplax functoriality. Only its abstract/version metadata
were consulted here; no exact theorem or formal implementation is imported.
The next task is to settle the actual cone/terminal-join profile and its
whole comparison with Step, using concrete higher cells. Do not supply a
nerve inverse or infer the result from the name of an existing join owner.
