# Diagram inverse and boundary-observation migration

Date: 2026-10-20
Status: staged slice qualified; broader migration and production qualification remain open
Predecessor: `732872197d2dc67f5f7d9fe97093c75cbdcdee24`.

This continues the existing-consumer work in the
[living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
The [verification](production_diagram_observation_verification.json) records
original/current hashes, bounded development checks, the final combined
receipt and carried evidence. The
[scoped source adapter](production_diagram_observation_migration.py) emits the
checked LP at the original module positions.

## Original inverse construction

`one_cat_diagram_map_equivalences` and its original eight assertions pass
unchanged. The construction retains the actual original diagrams, forward
transformation, selected endpoint inverses and their two laws, with the
original OneCat hypothesis. This does not add a new equivalence principle or
resume application/nerve equivalence development.

The next existing boundary consumer exposed an unmigrated initial/cokernel
hypothesis: `TerminalObject(Op_cat C,t)` had to follow the upstream structure
to `TerminalObject(TotalOp_cat C,t)`. The whole zero-cone homology formula and
its selected P/Q data remain unchanged.

## Use the existing whole evaluation owners

The diagram inputs of zero-arrow tests, mate observations and raw-input
observations now use the existing `Functor_oplax_cat WalkingArrow_cat C`.
Their component observations use the ordinary strict evaluation functors
`diagram_oplax_evaluation_at_func`, and their arrow observation uses the
existing whole `diagram_oplax_evaluation_transf`.

Thus an arrow in the oplax diagram category is observed by `fapp1_fapp0` of
fixed evaluation, with all actual endpoints and the original arrow retained.
The existing kernel/cokernel semantic-mate comparisons are then observed
through these same functors. No new inverse, square, comparison-cell input or
separately supplied transport law is introduced.

For the ordinary zero equations, naturality is read from the whole evaluation
transformation using the original OneCat hypothesis. The terminal test takes
the symmetric equality to retain its original equation
`outgoing ∘ incoming = tip ∘ terminal`; the initial test uses the forward
equality. This is equality reflection under the existing ordinary-target
guard, not an inversion of arbitrary directed naturality cells. Raw component
projections still accept arbitrary C.

## Point comparison keeps its ordinary target

The two original H-boundary families now supply oplax-profile objects. At the
selected x, their actual functor objects are decoded by the existing
involutive strict-functor operation:

```
d : Functor(OddDual(W),OddDual(C))
OddDual_func(d) : Functor(W,C)
```

where W is the walking-arrow category. The final point map remains an ordinary
`Transf(W,C)` between these two decoded diagrams, and its equivalence uses the
unchanged `one_cat_diagram_map_equiv`. The original boundary diagrams, P,
forward map and identity endpoint data are retained. Local typed definitions
name the two decoded diagrams inside the original bodies; no new library
symbol is required.

This does not identify the ordinary and oplax mapping categories or assert a
new whole K-indexed comparison. It preserves the original point-observation
scope, while returning whole diagram transformations and actual equivalence
data at that point.

## Qualification

The [combined original inverse and migrated boundary reviewers](production_diagram_inverse_boundary_regression.lpfragment)
pass **10 positive assertions** in **42.721s / 205,952KiB** (about 201MiB).
Receipt: `20261020T231913Z-acf24134bec64246a608552ca3d8d2a4`.
The run uses the isolated checker under 90s/2GiB/o=20, with subject reduction,
warnings, source-only loading, serial execution, file limits and no swap.
The source modules' existing constructive proof definitions also typecheck.

All original declaration names and both reviewer assertion counts are
retained. None of the eight new source/reviewer files contains a rewrite or
unification rule. The final 2,254 critical-pair bodies come from unchanged
dependencies and are inventoried; they are not a confluence certificate.
The initial old-hypothesis failure and the intermediate owner checks remain
recorded. Re-emission matches the checked source exactly.

Prior selected core, combined-context, Sigma, Hom-factor and chain-map
receipts still rehash. Current coverage is 188 registered core files and 74
registered reviewers, with the same five central terminal-runtime exclusions.
Another 603 core files and 522 reviewers are not yet staged.

The repair follows the whole-owner/projection SOP: component observations
project existing whole evaluation operations; no compound nested-projection
rewrite, ad-hoc comparison unifier or new operational equality argument is
installed. The earlier bare Sigma-inference limitation remains recorded.

Replay by emitting `production_owner_migration.py`, copying the retained
combined import fragment as `diagram_inverse_boundary_regression.lp`, and
running the recorded bounded source check after a relevant change. Continue
next with `one_cat_zero_arrow_inputs` and the original
`kernel_cokernel_adjunction_observations` reviewer. Preserve the corrected
diagram profiles and the actual existing proof/inverse data. Production,
supported checker qualification, the five terminal Homd reductions and other
remaining migration obligations are still open.
