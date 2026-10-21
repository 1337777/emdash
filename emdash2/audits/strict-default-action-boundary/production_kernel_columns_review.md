# Native kernel pullback universality and generic column inputs

Date: 2026-10-21 UTC
Status: qualified non-library staging; full Freyd columns and production remain open
Predecessor: `8cbd9596`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Preserved construction

The original kernel pullback comparison, lift and universality owners retain
the selected P, original diagram D, comparison map, constructed inverse and
whole left/right round trips. Their diagram coefficient/evaluation accessors
and initiality data use the migrated native/total-dual profiles. All 26
original reviewer assertions pass on that first candidate. The original derivations in that chain are retained; no new rule is introduced.

The original slice-path and functor-postcomposition helpers are retained
unchanged. In particular, `one_cat_slice_category` remains its original
structural ordinary-slice profile declaration; this migration does not claim
to derive it. That profile supplies ordinary coherence, not the inverse map.
The latter remains the original actual construction from the chosen kernel.

The adjacent zero-postcomposition and input-recovery proofs also migrate by
profile/accessor changes. Both generic column-zero arguments keep their
original incoming/outgoing square laws and short-exact cancellation. Their
four implicitly reassociated proof joins need six explicit applications of
the already-existing `comp_assoc` theorem. This is a local proof repair: no
primitive helper, global comparison rule, supplied equality field or stronger
naturality assumption is introduced. The outgoing diagrams still precede
kernel/cokernel and short-exact choices; the whole column inputs consume the
same actual maps and zero proofs.

All 38 original declarations across nine library files are retained. The
original ordinary-target guards remain; no ordinary restriction is added to
the arbitrary parameter base B. No arbitrary omega-target universality is
inferred from this guarded construction.

## Reviewer disposition

The complete generic column reviewer is now checked, not only its earlier
row-only selector. Its original assertion 15 changes from negative runtime
conversion to positive runtime conversion. In the migrated source,
`zero_arrow_family_incoming_transf` is explicitly defined by the same
`diagram_oplax_family_map_at` expression on the other side. The former
ordinary symmetric accessor had only a proof-time comparison. Requiring the
new alias pair to remain runtime-distinct would contradict its existing
qualified definition.

No assertion is removed, and only that polarity changes. The other statements
and their migration-adjusted types are retained. The negatives for different
row maps, the changed column map, and different h/h2 transformations still
reject their intended comparisons. The
[polarity record](production_kernel_columns_polarity_changes.json) identifies
the original index, source line/hash, owner and retained noncollapse controls.
This resolves that specific former nonconversion boundary, not the unrelated
R06 inference or terminal-runtime obligations.

## Qualification

The kernel reviewer passes **25 positive/four negative assertions**, including
three imported positives, in **134.540s/1,663,556KiB** under 180s/2GiB/o=20.
The final [combined driver](production_kernel_columns_regression.lpfragment)
passes **37 positive/seven negative assertions** and all declaration bodies
in **112.514s/1,713,372KiB** under the reviewed 300s/2GiB/o=20 profile.
Subject reduction, source loading, warnings, serial execution, file limits
and no swap remain enabled. The isolated qualified checker is unchanged;
installed-toolchain promotion remains open. Receipts:
`20261021T101150Z-442b78a2e1d1469bb0ed7865c3eb0380` and
`20261021T102811Z-3713c85bd0ba44848dfc4570d5164e92`.

All four combined variants have the same 2,162 warning bodies. The first
stopped at the left proof's implicit associations; the second passed that
proof and stopped at the corresponding right proof joins. With both repaired,
all declarations and the earlier reviewer assertions pass; the last assertion
then exposes the obsolete runtime nonconversion expectation. Its recorded
polarity correction yields the final complete reviewer pass.

Every emitted mathematical input matches the successful combined receipt.
Every input of the previous broad core/library and native-zero receipts also
rehashes unchanged (173/361/160 files, including package descriptors and drivers). These new owners
add no rules on prior symbols, and their actual consumers check fresh. The
inherited structural slice declaration retains its original status. No
unchanged broad aggregate is repeated for reassurance.

Coverage reaches 276 library/core files and 99 complete reviewers. The full
central diagnostic is an additional staged file with the same five runtime
exclusions. There remain 515 registered core/library files and 497 reviewers
unstaged. These are coverage counts, not remaining-effort estimates.

## Continuation boundary

The full Freyd column run passes the migrated comparison/lift, zero-family,
input-observation and generic column-input owners. It now stops at
`zero_arrow_family_point_incoming_path` in
`emdash3_2_one_cat_kernel_family_point_paths.lp:21`, whose original point
observation still uses the old diagram profile. Continue there. The failed
full-column receipt is `20261021T103124Z-b8d76cddc2bd4d92ab4335a3f164996a`,
133.090s/1,699,164KiB under 300s/2GiB. Its source assertion inventory does not
qualify the complete Freyd column reviewer.

The five terminal Homd runtime positives, full Freyd columns, remaining
migration, normalization/usability, supported checker and production gates
remain required. The separate nerve goal stays paused. Production source,
catalog and health claims are not promoted from these non-library checks.

Replay uses `production_owner_migration.py` and the
[combined original reviewer driver](production_kernel_columns_regression.lpfragment).
The [verification record](production_kernel_columns_verification.json) retains
source/checker/profile hashes, exact-input carry, declaration and reviewer
inventory, the failed reassociation variants and final warning comparison.
Recheck affected boundaries after an owner, source pin, checker or runtime
profile changes.
