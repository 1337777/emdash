# Derived first-factor tensor action

Date: 2026-10-27
Status: qualified non-library whole action; later target-naturality extension derives composition; common-index coherence remains open
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [tensor-left replay mode](reverse_verification.json)

The [naturality continuation](right_closure_naturality_review.md) now derives
composition from an explicit structural target-naturality contract and
exercises it on whole coordinate-collapse maps. The original action and its
qualification below are unchanged.

## Actual construction

The [defined whole map](tensor_left_action.lpfragment) has type

```text
T_left(A,D,B) : L(A,D) → L(A⊗ᴿB,D⊗ᴿB),
```

where L is the ordinary Functor_cat. It uses the existing right closure:

```text
L(A,D)
  → L(A,GrayHom_lax(B,D⊗ᴿB))                 postcompose coevaluation
  → GrayHom_lax(A,GrayHom_lax(B,D⊗ᴿB))       canonical profile admission
  → GrayHom_lax(A⊗ᴿB,D⊗ᴿB)                 right uncurry
  → L(A⊗ᴿB,D⊗ᴿB).                          existing inclusion
```

At an actual F:A→D its map is

```text
tensor_left(F) = uncurry_R(coevaluation(D,B) ∘ F).
```

Both the whole map and its ordinary Hom action in F are defined composites;
no tensor-action primitive or separately supplied strictness proof is needed.
This is one needed shape-action operation for the common-index nerve work.
It does not assert an entire tensor bifunctor or monoidal structure.

## Derived laws and computation boundary

The existing right-closure paths prove

```text
tensor_left(id_A) ≐ id_(A⊗ᴿB),
curry_R(tensor_left(F)) ≐ coevaluation(D,B) ∘ F.
```

The readback is a whole A-diagram, including F's higher action. These are
proof-time paths, not newly installed runtime identity/curry cuts. They rely
on the right-closure beta/eta paths already supplied by its owner; that
foundational status is unchanged.

Direct reflexivity for the whole object body failed at nested admission and
represented composition. A second attempt put the comparison directly under
uncurry and still failed. The final proof first establishes the existing
represented-postcomposition/raw-composition comparison at its own type, then
maps that named proof through uncurry with explicit endpoints. No rewrite,
unification rule, opaque operational wrapper or global normalization change
is added.

The 16-input owning check passes with subject reduction in **95.445s /
309,836 KiB**, at 180s / 2 GiB. All input hashes are retained. Its 2,282
critical-pair reports / 181 replaceable-pattern reports come from the
unchanged imported rule set; no new rule family or parser issue is introduced.
The earlier failed combined check is recorded as failed. Its imported zero
and mixed-diagram sources were unchanged by the proof-only correction; no
unnecessary combined aggregate was repeated.

`replay_reverse.py --mode tensor-left --assemble-only` reconstructs the
checked scope. The other replay modes keep their exact earlier snapshots.

## Remaining work

Composition of successive first-factor maps is now derived by the linked
continuation. The other tensor factor, selected face/degeneracy maps and their
common-index laws remain required.
The existing right-closure inverse paths alone are not silently treated as a
complete naturality/monoidal interface. This action does not prove the
[internal mixed-exchange inverse](mixed_diagram_reconstruction_review.md) or
the native walking second inverse. Keep those exact obligations while
extending the actual shape maps.
