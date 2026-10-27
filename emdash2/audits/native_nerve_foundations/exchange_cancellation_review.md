# Whole exchange reindexing and cancellation reduction

Date: 2026-10-27
Status: checked non-library reindexing/reflection; the remaining evaluation equation and inverse remain unproved
Owner: [native implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
Evidence: [reverse replay extension](reverse_verification.json)

## General evaluator contract

For a strict F:A→B, the two whole functors below have the same type:

```text
ε_B(C) ∘ F
  ≐ shape_L(precompose_F) : A → G(L(B,C),C).
```

Here L is Functor_cat, G is Functor_oplax_cat, and ε is the existing mixed
evaluation owner. The earlier source did not establish this whole comparison
by typed reflexivity. The isolated source now adds its
[structural naturality comparison](evaluation_shape_naturality.lpfragment)
at that owner. This is an explicit computation contract of whole evaluation,
not a theorem inferred from its object projections.

The comparison matches two rigid normalized expressions, keeps every map
and category parameter, and introduces no runtime unfolding or operational
equality evidence. A different shape map is rejected. The opposite-profile
version is derived by staging the existing OddDual composition theorem;
there is no duplicate opposite-profile rule.

## Derived whole-family results

The [reindexing proofs](shape_reindex_paths.lpfragment) establish both
parameter directions:

```text
shape_L(D ∘ F) ≐ pre_G(F) ∘ shape_L(D)
shape_L(D) ∘ F ≐ shape_L(precompose_F ∘ D).
```

The first follows from fixed precomposition and duality composition. The
second is the concrete whole-family consumer of evaluator naturality. They
retain arbitrary directed families, not just their object values. They are
also relevant to the required common-index action; they do not themselves
establish that action or its degeneracy laws.

The [reflection proof](exchange_reflection.lpfragment) uses the existing two
whole double-exchange computations. Equality after exchanging the complete
families can therefore be reflected back to the original whole functors.
This is a proof-only use of the actual inverse operations, not pointwise
functor extensionality.

Direct reflexivity for the reciprocal internal exchange's transposed
presentation failed. Staging OddDual composition through the two exchange
operations proves that presentation without another rule.

## Exact remaining inverse obligation

Write

```text
Z = G(I,C)
S = L(K,Z)
T = G(I,L(K,C))
M : S → T                 the constructed mixed exchange
Y : T → S                 its constructed reciprocal candidate.
```

The checked [whole reduction](mixed_cancel_reduction.lpfragment) gives

```text
shape_L(Y ∘ M)
  ≐ pre_G(M) ∘ P_G(I,L(K,C),C) ∘ ε_K(C).
```

The missing equation is now explicit, with both sides whole K-families:

```text
pre_G(M) ∘ P_G(I,L(K,C),C) ∘ ε_K(C)
  ≐ ε_K(Z) : K → G(S,Z).
```

Proving it, followed by the checked reflection, would give Y∘M≐id_S.
`NerveMixedEvaluationCoherence` names this equality type only. Its proof-only
implication helper does not provide an inhabitant. No exchange, closure,
encoder or decoder takes this evidence as an operational argument.

The [actual reflexivity attempt](mixed_evaluation_pending.lpfragment) still
fails at this equation. It is recorded as a failed check, separately from
the green reduction. Next investigate this exact compatibility of the whole
postcomposition and evaluator owners. Do not replace it with supplied caller
data, an inverse declaration, or a pointwise readback. Both whole geometric
inverse laws, the second native inverse and the parent plan's later stages
remain required.

## Qualification and replay

The 65-input reduction scope passed in **84.410s / 603,372 KiB**, with subject
reduction at 180s / 2 GiB, including the earlier forward/reverse map and
profile-interaction checks. New declarations are below the 0.5-second
per-command reporting threshold; the measured run is dominated by imports.
The pending equality check failed in 99.281s. Neither result is an aggregate
or production promotion.

All five warning-inventory fields match the preceding 61-input scope after
mapping the fourteen inserted source lines. The LHS audit has no unreviewed
compound inferred slots. This is scoped compatibility evidence, not a global
confluence claim.

The existing `replay_reverse.py` now has `reindex`, `reflection` and
`evaluation-pending` modes. The last intentionally reproduces the failed
proof and is excluded from positive acceptance. Use `--assemble-only` to
verify exact source identity without another checker run. Previous modes
retain their original source snapshots; the new evaluator comparison is
inserted only for these extension modes. No additional replay chain or
production-source mutation is introduced.
