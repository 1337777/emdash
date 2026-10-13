# Native section coexistence assembly

Status: `tmp/probes/homd_native_section_assembly/combined_controls.lp`
passes, receipt `20261013T184800Z-3b807a2755c44fa4b100a20f09e0229c`.
Its source SHA-256 is
`ccaa46ee37b47ad7fd2da196a28f9999b0bc6125317dd56ba4e505a872a93c1d`.
No new LP owner, rule, unifier or observation is authored in this tranche.

The donor is the checked minimally guarded intermediate u-action source,
SHA-256
`a2926ea3d8228cc58961ed143870a10255e9f55a8ee7d9d6cfff244de68eba18`,
receipt `20261013T183333Z-10e0343038b346e7aa46867416ff3978`.
The recipe inserts the unchanged FibCov core, actual ambient inclusion and
defined represented-lift section bodies at their original owner anchor.
It appends the four existing core/inclusion/section/action control fragments
and the two existing precomposition/curry peak observations.

The same section bodies and controls passed in
`fibcov_cart_section/combined_controls.lp`, receipt
`20261013T184248Z-85bd0860ab6b4e80b8b9b0c9513f624e`.
The recipe verifies their literal occurrence in that checked source.
It also pins the checked inclusion and both independent peak sources and
receipts. The assembly result has its own fresh receipt rather than being
inferred from those isolated passes.

This replay checks that the minimally guarded intermediate u-laws coexist
with the canonical structural strict-Y FibCov core, its actual ambient
inclusion, the section defined by the existing lift, and their native
observations. The FibCov whole x-map stays ambient. The added three runtime
projections are copied unchanged from the already checked core.

The selected run completes in 15.862 seconds under the default 90-second/
2-GiB profile, with 740732 KiB maximum child RSS. Its 340 positive and
73 negative assertions include inherited controls. All 986 critical-pair
warning blocks exactly match the intermediate donor; the 137 replaceable
pattern-variable diagnostics are also unchanged in count. The strict LHS
audit reports zero unreviewed clauses, with the inherited 46 annotated slots
across 31 intentional clauses. This comparison is not a confluence claim.

Three source-only removal targets retain all controls and delete exactly
one checked core projection: `without_fibcov_root.lp` removes the whole
core's x-component fold, `without_fibcov_point.lp` removes its u-value fold,
and `without_fibcov_component.lp` removes the strict value's y-component
fold. Their rule texts and hashes are recorded by the recipe. Each removal
fails its corresponding positive native projection consumer:

| Removal | Failed assertion lines | Receipt |
| --- | --- | --- |
| `without_fibcov_root.lp` | 19401–19403: whole core x-component to source functor | `20261013T185152Z-9be88aa93f48418383704e85e8dd4c5c` |
| `without_fibcov_point.lp` | 19405–19408: source functor u-value to strict value | `20261013T185208Z-9c5b44713a384e6b8e1995065b526ecd` |
| `without_fibcov_component.lp` | 19417–19421: strict value y-component to fibre transport | `20261013T185222Z-4d881fa09a1942b6bd2ac21f3c692576` |

All controls remain in each target. These measured failed positives qualify
the projection dependencies of this corpus; they are not negative tests or
proofs that the whole structural constructor is derived. All four emitted
targets now have fresh recorded receipts, with their LP bytes unchanged.

The old `homd_id_src_sec` and all donor owners remain unchanged.
No legacy whole equality is appended or required. Adopting the actual
derived section in the native Homd owners, with whole x/u compatibility,
is the next separate issue.

Provisional Q/global Cartesian Prof and the remaining lift/extracted-laxity
coherence boundaries remain explicit. No coend construction or operational
proof argument is introduced.

`homd_native_section_assembly_migration.py --check-authoring --check-evidence`
checks exact source and future evidence pins without invoking Lambdapi.
Root owns serial checking. Exact warning blocks, receipt/log/output hashes
and the strict LHS audit are pinned in the verification record.
