# Original factor and whole-H reviewers at native diagram profiles

Date: 2026-10-21 UTC
Status: qualified non-library staging; unchanged staged library sources
Predecessor: `01ba9f3d`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Retained observations

Five complete original reviewers now use the existing native diagram and
Hom classifiers. Their original assertions and two reviewer-side proof
helpers are retained. No library definition, runtime rule, unification rule,
primitive, selected map or hypothesis changes.

The image/coimage factor-reconstruction reviewer uses native Hom categories
for its mate comparison and native fixed evaluation for components. Its
original proof still reconstructs the actual arrow through the selected
image/coimage factors. The separate factor reviewer retains all eight
endpoint computations and both whole next-Hom observations of arbitrary
native diagram maps.

The raw chain-pair reviewer encodes the outgoing diagram only where a native
consumer expects it. Its final ordinary generator assertion stays ordinary.
The two whole-H reviewers retain source formation before selection, the
supplied input map, the original boundary mate, global H action and the
actual boundary diagram passed to Q. Literal walking diagrams receive the
same encoding already used by those native producers.

The [bounded adapter](production_factor_h_reviewers_migration.py) records
source hashes and exact replacement counts. It reuses the existing profile
and observation helpers; the ordinary generator suffix has an explicit
source boundary. All five emitted reviewers match the checked source bytes.

## Qualification

The individual reconstruction reviewer passes its two original assertions
plus three imported assertions in **86.646s / 1,235,536 KiB RSS** under 90s/2GiB:
`20261021T141158Z-c11810029dd140d19ef1dbfaf3a5fc52`.

The [combined driver](production_factor_h_reviewers_regression.lpfragment)
passes **28 positive assertions**: all 25 original assertions across the five
reviewers and three imported assertions. Both original reviewer proof bodies
also check. Wall time is **63.316s**, maximum child RSS **1,267,808 KiB**, under
180s/2GiB: `20261021T141459Z-10dfa5e3b55141eb8f47ab7804eca95f`.
All original assertion polarities remain.

Both runs retain subject reduction, warnings, o=20,v=1024, the 64MiB file cap,
serial execution and no-swap guard. The isolated batch-snapshot checker and
its exact hash are recorded; the installed checker and default profiles are
unchanged. The different wall times are not a matched performance improvement.

The old reconstruction-reviewer baseline hit 90s while loading prerequisites,
before checking its assertions. That interrupted import is not evidence of a
specific reviewer type error. The explicit observation import in the adapted
reviewer also changes loading order. Its warning differences occur at
unchanged NType and odd/even-duality owners: 52 added bodies and 26 absent
relative to the incomplete baseline. The two successful scopes have identical
2,284-body warning multisets, all already present in the preceding qualified
record scope. Exact branches remain in immutable logs with bounded hashes in
the verification. No global confluence or normalization-speed claim follows.

All fresh inputs match emission and the tracked driver. All 437 previously
qualified LP files are byte-identical; no library source changes in this slice.
Their earlier receipts retain their original scope/profile. There is no
reason to repeat unrelated core/library aggregates for these reviewer-only
adaptations.

Coverage remains **322 library/core files**, and reaches **120 complete
reviewers**. The full central diagnostic remains separately staged with its
five terminal runtime exclusions. There are 469 registered core/library files
and 476 reviewers still unstaged.

## Continuation

Next migrate the remaining closely related original diagram/mate reviewers:
`examples/one_cat_adjunction_family_zero_inputs.lp`,
`examples/arrow_diagram_point_usability.lp`, and
`examples/walking_arrow_diagram_evaluation.lp`. Their whole and point
observations must be compared against the actual staged owner profiles.

The five terminal Homd runtime obligations, remaining registered migration,
normalization/usability, supported checker/resource profiles and production
source-pin/catalog/health/prose/CI gates remain required. The separate nerve
goal stays paused; no production qualification is claimed here.

Replay with `production_owner_migration.py`, copy the tracked combined driver
into the emitted package as `factor_and_h_reviewers.lp`, and run the recorded
profile. The [verification](production_factor_h_reviewers_verification.json)
retains source/authoring hashes, assertion/declaration inventories, receipts,
warning comparisons and the unchanged prior qualification boundary.
