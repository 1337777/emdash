# Whole homology columns and the encoded diagram-point comparison

Date: 2026-10-24 UTC
Status: qualified non-library migration; aggregate timeout retained explicitly
Predecessor: `099ee9b8`
Original source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

Three original owners and two complete reviewers retain all **22 declarations,
21 positive and four negative assertions**. Their whole first/diagram
projections, expanded Hom-action comparisons, point observations and connecting
transformation remain. No new primitive, runtime-rule count, supplied comparison
cell, operational cast or public assumption is introduced.

## Changes and owning boundaries

The seven original runtime clauses retain their roles. Four whole column
projection clauses now match the current total-dual native projections through
stable `CoAbove2_func`/`Op_func` heads and the existing strict view of the
Cartesian displayed projection. Fully inferred second-projection targets fail
subject reduction; the accepted clauses retain the measured actual
`OddDual_cat(Functor_cat(...))` guard. They do not pattern-match a reducible
`Functor_oplax_cat` or `TotalOp_func` alias. The two object projections and
connecting-transformation component rule retain their original outline.

The four original proof-time comparisons are migrated to the current surviving
Hom-action forms. The first projection retains its total-dual Sigma Hom action;
the left comparison matches both complete composites to avoid reconstructing
the wrong opposite/endpoints. Diagram action retains the actual negative-index
Sigma map, `fdapp1_int_presheaf_arrow`, canonical displayed projection, fixed
identity factor, column endpoints and complete walking diagram. The original
wrong-action negatives remain. Arbitrary displayed maps are not strictified.

One additional proof-time comparison belongs at the existing arrow-diagram
owner: the encoded counterpart of its ordinary fixed-point comparison. It
retains F, G, eta, x and both terminal-domain guards. A typed positive and an
unrelated-arrow negative control accompany it. It introduces no runtime
category identification and no new declared operation. This changes one
previously qualified source, so its predecessor dependency receipts cannot
simply be carried as unchanged.

## Focused evidence

- The first owner run fails without the second-projection target guard:
  `20261024T105311Z-b33b0c702701455784e1bc96138d692e`.
- The immutable guarded owner passes in 131.592s/487,856KiB:
  `20261024T105731Z-3a799c81b5474385b156a697107758c6`.
- The no-old-unifier control passes the whole first-Hom comparison and fails
  its expanded form: `20261024T110023Z-5b9ce5ddd9ce4b439ae3fbaf74ff6213`.
- The adapted right comparison passes; direct comparison of the two left
  composites resolves the remaining frame mismatch. Its exact original
  equality passes in 2.38s after 19.39s of cached dependency loading:
  `20261024T111704Z-8a1c490f7ff34fc8b7038d86c7f30121`.
- Owner-position encoded-point controls pass and isolate the remaining
  intrinsic diagram action. The complete candidate then passes 25 positives/
  five negatives, including inherited checks, in 47.633s/638,388KiB with exact
  cached parents: `20261024T113614Z-d1bdf005a23042ed93c0402533d78980`.

The prematurely launched replay
`20261024T105650Z-56b5ed6d9f454f1da3a147d2f2c7615f` overlapped source preparation
and was terminated and discarded. It supplies no qualification evidence.
All later launches waited for completed preparation. The verification ledger
retains failures and diagnostic/cache boundaries.

The inferred-slot audit reports no unreviewed candidates in the four changed
owners. Its only annotated compounds are the two measured target guards.
Manual review also covers the owner-specific heads, the retained families/maps/
identity/endpoints and actual native extraction. The advisory audit is not a
confluence certificate.

## Complete regression coverage and the cumulative deadline

The cold aggregate imported all 26 previously qualified complete scopes plus
the new consumers. It reached its 1800s cumulative deadline during an original
short-exact normalization reviewer, without reporting a positive typing failure:
`20261024T114527Z-94fac8cc2e0c4587a132c9700f847e8b`.
**That receipt remains a timeout.** Sampled checker RSS reached 5,779,524KiB;
the forced-termination receipt's 83,388KiB statistic is not the checker peak.
The first complete integration scope finished in 1145.36s, compared with
1191.16s in the earlier matched run. Individual command timings vary; no
general performance fix or cause is inferred.

Twenty-three top-level scopes had completed before that deadline. The
[completed-scope verifier](production_completed_scope_evidence.py) records only
their fully started/ended dependency closures: **1,017 source files**, exact
retained input hashes, raw log positions, and the pinned checker code governing
completion. At checker pin `db4f7809961b8c107247613067fb567491fb0b84`,
`compile.ml` emits `End checking` after all `Command.handle` calls return;
the iterator propagates failures, assertions fail fatally, unfinished
definitions fail, and rule handling checks subject reduction. This is evidence
for completed source scopes, not success of the unfinished aggregate.

Negative verifier controls reject the unfinished aggregate, its unfinished
child scope, and a simulated target completion marker with an incomplete
dependency. Diagnostic modified-log results are explicitly ineligible for
qualification. No runner, checker logic, default limit or host setting changes.

The four unfinished complete scopes were then replayed from cold sources at
900s/4GiB/o=20 with subject reduction, warnings and all safeguards:
`20261024T122238Z-f234d973de16430c9aa9ddddab8f0c85`.
They pass **147 positive and 27 negative checks in 878.713s/3,289,492KiB**.
All source inputs are identical across the two runs; neither package contains
compiled objects. The verified completed scopes and this successful replay
together cover every prior complete scope and the new consumers.

The [verification](production_homology_column_consumers_verification.json)
contains the exact coverage union: 1,112 inputs, 4,626 positive and 672 negative
assertions counted once per qualified source file. These counts are tests,
not a count of independent mathematical theorems. All 2,544 warning occurrences in
the combined inventory use bodies from previously reviewed contexts. R07 remains open.

This coverage record is a new baseline. Future conservative continuations
must rehash **`qualifiedInputSha256`**, including its completed-source evidence,
rather than retaining only the successful remainder receipt or claiming the
timed-out aggregate passed. The aggregate outcome and all scope boundaries
remain visible in the evidence.

## Replay and remaining work

Run `python3 production_owner_migration.py` in this audit directory and wait
for successful completion. The guarded runner can then check
`encoded_point_then_columns.lp` for the local consumer group, or the recorded
complete-snapshot and remaining-snapshot drivers in
`tmp/probes/production_owner_migration/package`. Use the recorded checker and
explicit profiles; do not infer a completed aggregate from its deadline.
The source-scoped verifier can reconstruct completed coverage from the pinned
receipt/log and listed scope roots. Source, checker or profile changes trigger
review/revalidation. Production registry/catalog membership is unchanged while
these remain staged non-library sources.

Qualification reaches **1,064 files: 687 core/library and 377 reviewers**.
The original-source inventory leaves 104 core/library files and 219 reviewers.
The five terminal Homd runtime obligations, warning/normalization/toolchain
review and production promotion remain open. The separate nerve goal and
large six-term audit remain paused.
