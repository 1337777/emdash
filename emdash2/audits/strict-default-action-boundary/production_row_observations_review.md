# Native row cancellation and zero-cone observations

Date: 2026-10-21 UTC
Status: qualified non-library staged slice; full column reviewer and production promotion remain open
Predecessor: `c98aac92`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Retained construction

This slice migrates the original four short-exact row cancellation laws and
thirteen zero-cone row-family declarations. It preserves the actual P/Q
adjunctions, chosen inverses, incoming/outgoing maps, whole square laws and
original OneCat hypotheses. The complete original cancellation reviewer
retains its four positive and two negative assertions. No new runtime rule,
unification rule, operational primitive or caller evidence is introduced.

The kernel reconstruction proof now passes through the existing
`kernel_family_mate_projection_view` between the raw and canonical
inverse-mate applications. That derived helper's type and body are unchanged;
only `protected` is removed so the original cancellation owner can use it.
This avoids duplicating its proof. The checker source distinguishes visibility
from opacity: `src/parsing/scope.ml:16–24`, `src/core/sig_state.ml:148–152` and
`src/core/term.ml:168` explain the rejected foreign protected reference.
The fresh combined check includes all three prior kernel reviewers as well
as this new caller. The predecessor receipt for the changed helper file is
historical, not silently reused at its new hash.

The row-family owner uses the native oplax diagram coefficient and evaluation
owners. Its vertex-map action uses the existing `comp_cat_cov_fapp1_func`
projection with the actual R, S and m. Its incoming restriction proof uses
the existing whole `one_cat_whiskering_path` with raw composite endpoints;
the former convenience wrapper retained a represented evaluation endpoint
that did not join the required source projection. Outgoing restriction uses
the existing native reindexing theorem. These are local derivation repairs,
not new action laws or strengthened transformation profiles.

## Qualification

The [combined cancellation driver](production_row_cancellation_regression.lpfragment)
passes **36 positive and five negative assertions**, including imported
checks, plus all declaration bodies: **84.786 seconds / 1,542,004 KiB**.
Receipt: `20261021T085650Z-073b9e3321f94ff3958835c858fe7ad7`.

The [row observation selector](production_zero_cone_row_original_controls.lpfragment)
retains original column-reviewer assertions **1–4 and 11**, unchanged, with
their [source hash and line provenance](production_zero_cone_row_original_controls.json).
These check the two whole squares, the source/vertex components and retention
of arbitrary row-map data. The scope passes **seven positive and one negative
assertions**, including three imported positives: **92.540 seconds /
1,615,676 KiB**. Receipt:
`20261021T091031Z-9be0f09c73ee42e08d1236a267da94be`.
This selector does not qualify or count as the complete column reviewer.

Both checks use explicit 180s/2GiB/o=20 guards, source loading, subject
reduction, warnings, serial execution, file limits and no swap. The isolated
checker remains the one qualified in the
[checker boundary review](production_checker_boundary_review.md); installed
toolchain promotion is still open. All emitted mathematical inputs match
the fresh receipts; the tracked driver fragments match their checked inputs.

The combined cancellation scope has 2,154 warning bodies, exactly the
predecessor combined kernel multiset. The row scope has 2,158: six added and
two absent bodies relative to cancellation, at existing diagram evaluation
and transformation-graph owners. Every added body already occurs in the
prior full staged-library receipt. This is a scope/order comparison, not a
global confluence certificate. Exact evidence, origins and hashes are in the
[verification record](production_row_observations_verification.json).

The complete preceding central and library input sets (170 and 346 files)
rehash unchanged, including drivers and package descriptor. Those scopes do
not import the changed helper owner. New modules contain definitions only;
the helper's visibility change is checked fresh with its actual consumers.
The earlier broad evidence therefore carries at its exact input scope;
no unchanged aggregate is rerun for reassurance.

Coverage reaches **260 library/core files and 95 complete reviewers**. The
staged full central diagnostic is an additional file with the same five
runtime exclusions, not a complete pass. Of the registry, **531 core/library
files and 501 reviewers remain unstaged**. File counts measure migration
coverage, not estimated remaining effort.

## Development failures and continuation

The first cancellation attempt stopped at raw/canonical inverse-mate
classifiers; its next attempt stopped at foreign protected visibility.
The first row attempt stopped at the generic vertex action's represented
endpoints; the next stopped at the incoming whiskering wrapper's represented
evaluation. The final proofs above resolve these failures without new rules.
Their receipts are retained in the verification record.

The full column run subsequently passes these owners and fails at
`freyd_raw_native_row_first_whole_path` in
`emdash3_2_commutative_algebra_freyd_native_row_paths.lp` (receipt
`20261021T091420Z-f767131a076841b8b5db4eeb3e5e5b52`, 110.082 seconds /
1,704,600 KiB). Its residual compares the original constant transformation
with a composition-action projection. Next inspect the existing constant
transformation views and partial action owners at this actual consumer.
No new rule or architectural change is justified by this failure alone.

Full columns, the five terminal Homd runtime positives, remaining migration,
normalization/toolchain qualification and production gates remain required.
The separate nerve goal stays paused. Replay is through
`production_owner_migration.py`; the tracked focused drivers run against its
emitted package. Recheck affected consumers if an owner, source pin, rule,
checker or runtime profile changes.
