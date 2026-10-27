# Derived reverse geometric maps

Date: 2026-10-27
Status: checked non-library whole maps and readbacks; whole inverse laws remain open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [source snapshots and receipts](reverse_verification.json)

## Whole construction

Write L(A,B)=Functor_cat(A,B), G(A,B)=Functor_oplax_cat(A,B), and
I=WalkingArrow. The new [mixed-exchange map](reverse_geometric_maps.lpfragment)
has the complete type

```text
M(K,I,C) : L(K,G(I,C)) → G(I,L(K,C)).
```

Its body uses the checked structural whole postcomposition P and the existing
mixed evaluator. Its opposite-direction candidate is the OddDual image of
that same body at the swapped dual parameters. Neither direction is a newly
postulated inverse. The profile/order agrees with mixed lax/oplax exchange in
[Ara–Guetta v1, §21](https://arxiv.org/html/2503.08832v1#S2); that reference is
a semantic cross-check, not the evidence for a checked emdash inverse.

For an actual whole parameter diagram D:K→G(B,G(I,C)), the construction is:

```text
D
  ↦ B → L(K,G(I,C))                 mixed shape evaluation
  ↦ B → G(I,L(K,C))                 postcompose with M
  ↦ I → L(B,L(K,C))                 mixed shape evaluation
  ↦ I → GrayHom_lax(B,L(K,C))       canonical profile admission
  ↦ GrayTensor_R(I,B) → L(K,C)      existing right uncurry
  ↦ K → G(GrayTensor_R(I,B),C).     mixed shape evaluation
```

Applying this operation to the identity diagram on G(B,G(I,C)) yields the
actual whole reverse map

```text
ρ(I,B,C) : G(B,G(I,C)) → G(GrayTensor_R(I,B),C).
```

This universal parameterization retains higher action. It is not a pointwise
object decoder subsequently labelled as a functor. The abandoned intermediate
idea of introducing a tensor-action primitive is unnecessary. No new tensor
symmetry, associator, left-closure primitive or inverse law is supplied.

With Qₖ=GrayCubePos_R(k), s/t the already qualified iteration-shift maps,
and eₙ:NCₙ(C)→Wₙ(C), the reverse recursion is:

```text
u₀(C) = id_G(I,C)
uₖ₊₁(C) = ρ(I,Qₖ,C) ∘ uₖ(G(I,C)) ∘ tₖ₊₁(C)
Eₖ(C) = uₖ(C) ∘ eₖ₊₁(C) : NCₖ₊₁(C) → G(Qₖ,C).
```

The internal Nat recursion, line/square equations and variable-degree whole
Hom action check. Together with the preceding Dₖ construction this supplies
whole maps in both directions at every positive geometric dimension. It does
not yet prove Eₖ and Dₖ inverse, and does not cover geometric degree zero.

## Canonical admission and computational owners

The older right closure names the explicit GrayHom_lax/LaxTransfor profile.
The current ordinary Transf already has its conventional pre/right strictness.
[Canonical admission](reverse_profile_admission.lpfragment) derives that
property from the existing extracted action, then exposes a stable structural
constructor and whole inclusion into the older profile. Its ordinary view is
the original transformation; its next-Hom action is identity. No operational
symbol asks the caller for a proof, a new cell or stricter naturality.

Directly putting `make_lax_transfor(e,canonical_property)` into the higher
projection failed subject reduction, including with explicit source/target
guards. The stable constructor resolves this carrier-normalization boundary.
The property theorem remains checked, while the operational constructor has
no proof payload. This does not identify the two whole mapping categories or
make arbitrary transformations strict.

Image units and composition have canonical projections. Their ordinary-view
joins use two narrowly typed rules at the existing Gray-Hom inclusion owner.
The current source files are unchanged; these insertions are retained only
in the source-pinned audit package.

One whole comparison completes the structural postcomposition interface:

```text
evaluate_D ∘ P(K,A,B) ≐ precompose_D.
```

It compares both rigid whole owners and constrains every parameter, including
D. It is a structural computation contract of P, not a theorem inferred from
pointwise agreement. Both runtime presentations remain intact. Typed
reflexivity uses the comparison, and substituting an unrelated E is rejected.

## Readbacks and exact remaining proof

The [whole-family readback](reverse_family_readback.lpfragment) shows that
right curry recovers the entire admitted I-family used by the actual reverse
tensor-family construction. It uses the existing right-closure comparison,
including at the universal diagram, without adding a left inverse premise.

The [mixed-exchange readback](mixed_exchange_readback.lpfragment) also recovers
the entire exchanged I-family. Direct reflexivity initially failed where
OddDual distribution competed with represented composition. Staging the
existing duality composition theorem and the checked whole evaluation
comparison proves the result without another unification rule.

The first complete composite of mixed exchange with its reciprocal candidate
still fails direct reflexivity. The [pending proof attempt](mixed_exchange_inverse_pending.lpfragment)
is retained separately. The second inverse declaration in that file was not
reached. No failing theorem is part of the qualified target.

Next derive the whole exchange cancellations and the left closure laws,
then propagate them through the cube recursion. The existing walking first
round trip can support one geometric round trip independently of the still
unfinished second walking inverse. Same-index action, degeneracies, the
independent simplex branch and final production/frontend integration remain
required. Earlier Cat_cart and raw nested-projection limits are retained at
their own source boundaries, not silently marked resolved here.

## Qualification

The final **61-input** scope passes with subject reduction in **85.162s /
583,624 KiB**, at the explicit 180s / 2 GiB profile. It imports the preceding
forward construction and shift-inverse checks, verifies the new whole
readbacks and profile projections, and retains noncollapse controls.
No default resource limit or checking policy changed. The earlier maps-only
run took 132.721s; these measurements do not establish a speed improvement.

The warning inventory has 2,228 critical-pair reports and 181 replaceable
patterns, versus 2,180/181 in the preceding 54-input scope; there are no parser
issues. New families are the profile-admission projection orders, image
unit/composition, and the raw-view composition interaction. Canonical typed
unit/composition and higher-cell controls pass. The explicit underlying view
retains its existing proof-time agreement with the lax view; unrestricted
runtime joins and production confluence are not claimed. The LHS audit has
no unreviewed compound inferred slots.

`replay_reverse.py --assemble-only` reconstructs the exact qualified source.
The `maps`, `readback` and `qualification` modes have fresh imported/whole
coverage. `inverse-review` is a pending failure investigation: its last
failure preceded the later profile unit projections, and its final pinned
assembly is not labelled a completed check. An interrupted earlier wrapper
left a diagnostic log without a receipt; that observation is identified as
unreceipted in the record. No aggregate or production promotion is claimed.
