# Original adjunction, general exchange and Cartesian exchange reviewers

Date: 2026-10-21 UTC
Status: qualified non-library staging; unchanged library owners
Predecessor: `d4d9f816`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Preserve the original general family

The original whole-evaluation observations retain
`H : Functor A (Functor_cat B C)`. They now use the existing opposite-profile
exchange `diagram_family_shape_func`, followed by native fixed evaluation.
The whole composite computes to H[a], including the product-target case;
its subsequent whole Hom action is still checked. No Cartesian restriction
is imposed on these original H inputs.

The original opposite-source identity and component observations likewise
use `diagram_family_transf` with general H. The total reversal intended by
the old Op spelling is now `TotalOp_cat`. Their named endpoint is the existing
`OddDual_func` view of `diagram_family_at_func`. The identity and its component
compute, while an arbitrary loop remains a negative control.

Additional blocks retain the direct `sym_func` controls at its actual
Cartesian contract, `H : Functor A (Functor_cart_cat B C)`. This checks a
different owner and does not replace the general observations. The existing
Cartesian target-product reduction keeps the reducible-endpoint stress case
meaningful. Its component uses the existing `strict_transfor` inclusion of
that classified Cartesian arrow; no new admission witness is supplied.

## Adjunction data and computation

Both original triangle computations and the reindexed Hom-profunctor mate
push/pull cancellation remain unchanged. Opposite-adjunction involution uses
`TotalOp_cat` and `TotalOp_func`, matching the actual legacy-named
`Op_adjunction` declaration. The arbitrary named-unit noncollapse test remains.

The constant-postcomposition reviewer is byte-identical to the source pin.
Its selected-value proof-time comparison passes, the wrong-value comparison
fails, and its runtime-negative distinction remains. No proof-time view is
presented as a new runtime fold.

All fourteen original assertions retain their polarity, typing-versus-runtime
kind and original scope. Six additional Cartesian controls make both exchange
contracts explicit. The original whole Hom type query is retained for general
exchange, with a further Cartesian query. No library source, formal rule,
primitive, selected adjunction data or additional operational proof argument
changes.

## Canonical endpoint and remaining normalization boundary

A trial identity comparison used raw fapp0 of the exchanged whole family as
its endpoint. That trial fails runtime conversion. Normal-form inspection
shows identity at a composition versus identity at the stable represented
precomposition form. The exchanged identity and the named fixed-family
endpoint have identical composition normal forms. Using that existing named
projection preserves the intended runtime observation without a new rule or
a proof-time substitute.

The raw-root presentation is not claimed to normalize to the named endpoint.
Its distinct runtime form remains under R06/R12 and must be reviewed if a
concrete consumer needs that extra comparison. The verification retains the
failed variant, normal-form hashes and successful general identity run.

## Qualification

The final combined source passes **15 positive and five negative assertions**
and both whole Hom type queries. Receipt:
`20261021T150206Z-3e5715d491fb4e1c8c57d6533eaa11c9`.
Wall time is **51.250s**, maximum child RSS **279,120 KiB**, under 180s/2GiB.
Subject reduction, warnings, o=20,v=1024, the 64MiB file cap, serial execution
and no-swap guard remain enabled. The isolated batch-snapshot checker and
installed-checker boundary are unchanged.

The earlier Cartesian-only candidate passed but was insufficient to preserve
the old general H scope. The final source therefore retains both profiles.
The original baseline failed inference at the Cartesian sym_func input;
that is distinct from the later raw-endpoint normalization trial.

All 2,084 final warning bodies already occur in the preceding qualified
diagram/mate scope at unchanged library owners. The 484 bodies beyond the
initial failed baseline belong to subsequently reached existing owners, not
new rules. Exact logs and bounded hashes retain the branches. No global
confluence or matched performance improvement is claimed.

All fresh inputs match emission and the tracked driver. All 445 previously
qualified LP files remain byte-identical. Their receipts keep their original
scope and resource profile; no unrelated aggregate is rerun for these
reviewer-only changes.

Coverage remains **322 library/core files** and reaches **127 complete
reviewers**. The full central diagnostic is separately staged with the same
five terminal runtime exclusions. There remain 469 core/library files and
469 reviewers unstaged.

## Continuation

Continue with the original ordinary diagram reconstruction, native square,
slice-path and terminal-adjunction reviewers. These distinct assertions are
not discharged by the exchange and triangle observations here.

The five terminal Homd runtime obligations, remaining registered migration,
normalization/usability, supported checker/resource profiles and production
source-pin/catalog/health/prose/CI gates remain required. The separate nerve
goal stays paused; no production qualification is promoted.

Replay with `production_owner_migration.py`; copy the [combined driver](production_adjunction_reviewers_regression.lpfragment)
into its package as `adjunction_reviewers.lp` and use the recorded profile.
The [verification](production_adjunction_reviewers_verification.json) retains
original/current assertion inventories, scope dispositions, source/authoring
hashes, receipts, normal forms and warning comparisons. The [exchange](production_adjunction_exchange_reviewer.lpfragment),
[identity](production_adjunction_op_identity_reviewer.lpfragment) and
[triangle](production_adjunction_triangles_reviewer.lpfragment) fragments expose
the actual checked source; the constant-view source is reused unchanged.
