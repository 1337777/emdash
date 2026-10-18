# Walking-circle and profiled-interchange migration

Date: 2026-10-18
Status: complete staged owners and original reviewers checked with the installed
checker; production promotion and the remaining migration are open.
Predecessor: `85fdaefc32c9c641eb1971085c4e4f335288d606`.
Original source: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`.

This continues the original central diagnostic import order after WalkingEnd.
The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
owns the overall scope. The [verification](production_circle_interchange_verification.json)
records exact inputs, receipts, warnings and measurements. The production files
remain untouched; `production_owner_migration.py` emits the complete sources.

## Walking circle

`emdash3_2_circle_hit.lp`, `emdash3_2_walking_circle_completion.lp`,
`emdash3_2_walking_circle_restriction.lp` and their two original reviewers are
byte-for-byte the pre-goal sources. They pass against the migrated dependency
closure, including the previously qualified WalkingEnd owner. The two reviewers
contain fifteen positives and two negatives; their closure also contains three
inherited positives. The installed run passes all eighteen/two in 31.533 seconds
at 2359264 KiB peak child RSS under 300s/4GiB/o=20.

## Interchange and Eckmann–Hilton

The first actual failure is a classifier mismatch. The canonical
`hom_postcomp_tele_fapp1_fapp0` now belongs to the Cartesian mapping Hom, whereas
the original profiled interchange theorem expects an ambient transformation.
Its existing ambient view is `hom_postcomp_tele_transf`: the core already reduces
`strict_transfor` of the former to the latter. Thirteen owner occurrences and
one reviewer occurrence move to that existing view. No new view is declared.

That correction alone exposed the original proof's final join: its vertical
path ends at the composite of two telescope transformations, while the stated
result uses the telescope action on the composite input. Both are images under
the same whole functor

```
Functor_cart_include ∘ hom_postcomp_tele_func.
```

The [replacement proof body](production_profiled_interchange.lpfragment) retains
the original `profiled_vertical_both_raw_path`, then applies the strict functor
composition law of that whole functor through `eq_ap`. The law is proved by
reflexivity with an abstract functor before specializing to the actual telescope.
This avoids requiring its distinct stable projections to normalize to the same
expression. It adds no primitive, rewrite, unifier or supplied hypothesis.
The equality term is the result of this existing library theorem, not an
operational argument to Homd, composition or the telescope.

The original theorem signatures retain their PE/PN/PB premises and the remaining
three original proof bodies, modulo the ambient-view substitution. The original
Eckmann–Hilton reviewer retains its OneCat admission and omitted-premise negative.
That negative checks the retained API's arity, not the impossibility of deriving
the canonical premise. Any later simplification of these now-canonical profile
premises is separate from this migration tranche.

## Validation and computational qualifications

- The installed checker reproduces the initial classifier failure. The view-only
  attempt fails specifically at the final telescope composition comparison.
- The final complete owner plus original reviewer passes four positives/one
  negative including inherited checks, with subject reduction and warnings.
  The source snapshot was rehashed after replay; all inputs match the receipt.
- No core or profile rule changes. The exact complete core/Homd 287-positive,
  85-negative snapshot remains identical to its earlier green receipt; it was
  not rerun for reassurance.
- The owner contains no rewrite/unification clauses. Its LHS audit reports zero
  unreviewed slots. All 2421 final warning bodies occur in the already checked
  walking-circle closure. The 63 additional warnings versus the failing owner
  are from the newly reached existing strict-action/OneCat reviewer imports,
  whose source bytes are unchanged. None originates in the new proof.
- The final run uses 111.545 seconds and 2294424 KiB under 300s/4GiB/o=20.
  The owner import takes 102.77 seconds and the subsequent reviewer dependency
  takes 6.72 seconds; no revised theorem command exceeds the 0.5-second reporting
  threshold. The pre-goal reviewer also passes under the same settings; exact
  measurements are 9.832 seconds and 485052 KiB. These are single end-to-end
  samples, not an isolated proof or unifier benchmark; the new proof's cost
  should not be inferred from the total migration/import regression.

This is a derived library agreement, not a new runtime telescope composition
cut. It does not close the broader normalization/performance review. The
previous isolated checker snapshot experiment remains diagnostic only; every
qualification in this tranche uses the unchanged installed checker.

Next continue the original central import frontier after `profiled_interchange`,
then migrate the central observations. Retiring redundant wrappers, reviewing
remaining normalization debt, promoting actual production sources and the final
catalogue/health/CI/source-pin gates remain required. The application goal stays
paused.

Replay when either migrated owner, its dependencies or the selected checker
changes: run `production_owner_migration.py`, then the guarded source runner
with its emitted package as `--package-root`, targeting
`walking_circle_migration_controls.lp` and
`profiled_interchange_migration_controls.lp` serially. The recorded installed
profile is 300s/4096MiB, `OCAMLRUNPARAM=o=20,v=1024`, warnings and subject
reduction enabled, and `--record-time --too-long=0.5 --no-colors`. Expected
outcomes are 18/2 and 4/1 including inherited assertions. Rehash carried core
receipts before reusing them. This remains a non-library replay until promotion.
