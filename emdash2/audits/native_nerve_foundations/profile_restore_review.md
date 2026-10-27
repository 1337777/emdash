# Whole profile reconstruction and second-factor maps

Date: 2026-10-27
Status: qualified non-library whole profile restoration and fixed second-factor tensor map/identity; further face work is not the current priority
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [profile-restore and tensor-right replay modes](reverse_verification.json)

Write A:L(B,C)→GrayHom_lax(B,C) for canonical admission and
J:GrayHom_lax(B,C)→L(B,C) for the existing inclusion. The
[profile proof](profile_restore.lpfragment) derives

```text
A ∘ J ≐ id_GrayHom_lax(B,C).
```

This is a whole endofunctor path. It is not a newly supplied comparison axiom.
At the identity target functor, the previously recorded right-closure target
naturality says that a curried diagram is fixed by A∘J. Curry/uncurry
reconstruction extends this to any complete family K:X→GrayHom_lax(B,C).
Specializing K to the identity gives the whole path above.

The opposite composite J∘A is not claimed to be the identity whole functor
on L(B,C). In particular, this result is not used to identify the two mapping
categories. A raw profiled transformation is preserved through the ordinary
view, while the negative runtime test still rejects erasing an arbitrary raw
profile term to its readmitted presentation. No operational map receives a
proof or new laxity cell.

The [fixed second-factor map](tensor_right_action.lpfragment) is

```text
preᵍ_F = admit ∘ precompose(F) ∘ include,
R_A(F) = uncurry_R(preᵍ_F ∘ coevaluation(A,D))
       : A⊗ᴿB → A⊗ᴿD,             F:B→D.
```

Its whole curried readback and identity law are derived. The identity proof
uses the whole profile restoration above. Ordinary fixed pre/postcomposition
interchange follows through the two existing Hom factorizations. Composition
of the second-factor maps and their complete varying-F profile are not yet
qualified; no unrestricted interchange of lax transformations is assumed.

The profile scope passes on 19 inputs in 73.938s / 303,880 KiB. The fixed-map
scope passes on 20 inputs in 73.506s / 306,524 KiB, both with subject reduction
at 180s / 2 GiB. The scopes add no primitive, rewrite or unification rule.
Their inherited warning categories are 2,282 critical pairs / 181 replaceable
patterns, with no parser issues. Exact source replays are retained.

A larger [face-order experiment](pending_face_order/README.md) passes typing
but is not adopted as a common-index interpretation. Its local left-tensor
ordering still needs comparison with the actual decoder's curry order.
The user has prioritized cubical/simplicial **core feasibility** over further
face/degeneracy expansion; preserve this work and resume it only when that
core boundary warrants it.
