# Batch-checker boundary and original import-context review

Date: 2026-10-20
Status: isolated checker audit; no installed toolchain or mathematical source change
Predecessor: `42465235749bd88856ba2b2e681ca533202f87d7`.

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
and [follow-up ledger](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
own R10/R12. The mathematical source remains the selected staged migration;
the rejected native-owner/terminal extension is not included. Exact inputs,
receipts and outcomes are in the [verification](production_checker_boundary_verification.json).

## Runtime change under review

The existing [batch-snapshot patch](production_checker_batch_snapshot.patch)
targets checker commit `db4f7809961b8c107247613067fb567491fb0b84`. For a
single command-line input, it releases the unused initial Pure rollback root
and omits the outer batch snapshot. Multi-file checking retains restoration
between files. Interactive states, proof states and their internal snapshots
remain available. Parser, inference, conversion, rewrite, unification and
subject-reduction algorithms are unchanged.

The isolated binary still has SHA-256
`5c82cca90847fb5cc7726f52b3c6b8f2df3a89685abecac48285ae676db6bb69`.
The installed binary remains
`ab493adeb0d79e58fa16c0965e1cb0e5194e212093119dc58f8e401f326c2c0a`.
Both report `3.0.0-90-gdb4f780`; the version string alone does not distinguish
them. No installed executable, package pin or normal runtime default changes.

The earlier [matched memory evidence](production_checker_memory_verification.json)
already compared the two binaries on identical source inputs and found a
large retention difference. This review closes two specific boundary gaps
before using that isolated binary on the current full import context.

## Boundary observations

Both binaries give the same results for three small source-only CLI cases:

- Two separately checked files: the first adds `f x ↪ x`; the second imports
  the same common declaration and verifies that the rule is absent. Both pass.
- One file importing both those files: the second assertion fails, showing
  that ordinary imports within one check are not incorrectly rolled back.
- An ill-typed rewrite in the first of two input files: subject reduction
  rejects it before the second file is checked.

The [Pure API harness](production_checker_pure_boundary.ml) runs against the
isolated checker library. It adds a rule, accepts the corresponding positive
assertion, rejects its opposite, restores the earlier state, checks the
negative assertion, redoes the rule, and opens a fresh file importing the
same common module. This checks actual shared-symbol rollback. It passes
both with the ordinary initial snapshot and with a freshly recreated snapshot
after release. Each mode runs in its own process.

An initial harness setup tried to save a new baseline after installing a
package mapping, then install that mapping again. It was rejected as a
duplicate mapping. Moving the release/recreation case to a fresh process
corrected the harness; no checker patch changed. This does not claim that
releasing a snapshot permits restoring the discarded past state.

The harness is built with `dune build --profile release -j1
audit_boundary/pure_state.exe` in the exact patched checkout, under 300s/4GiB.
Its Dune libraries are `lambdapi.pure`, `lambdapi.core`, `lambdapi.common`, and
`lambdapi.handle`. Both executions and all CLI controls use 90s/2GiB,
`OCAMLRUNPARAM=o=20,v=1024`, serial guards, 64MiB file limits and no swap.
The verification retains fixture texts, exact commands and source hashes.

## Full-context scope

The [selection helper](production_full_context_selection.py) creates
`central_full_context_except_terminal.lp` from the unchanged staged
`emdash3_2_checks.lp`. It matches exactly the five statements in
`central_public_homd_terminal_obligations.lp` and comments them only in this
separate audit target. All five remain positive obligations in the original.

The target retains the original import order, all 66 declarations and 2,435
assertions (2,157 positive and 278 negative). Assertion multisets, declaration
names, import order and both source hashes are checked. The durable helper
reproduces the initial target byte-for-byte in a separate temporary directory.
No compiled objects participate.

The reviewed run uses the isolated binary through a private PATH entry,
600s/4GiB and `o=20`, with subject reduction and warnings. The previous
isolated full-source run reached a genuine source error at about 1.3GiB;
4GiB provides measured headroom for the now larger closure. Approximately
16GiB was available before launch. The installed checker previously exceeded
8GiB on that import route, so repeating its unchanged failure is not useful.

The full-context target **passes** in 219.526 seconds at 1,609,584KiB peak
child RSS (about 1.54GiB), with all 140 recorded source/package inputs stable.
Receipt: `20261020T212451Z-a06c04c03100455cb1d3141ed320e502`.
It reaches and checks every retained assertion after all original imports.
This closes the original combined-context execution gap for that explicitly
scoped target with the isolated binary. It does not claim the excluded five
assertions or all separately registered reviewer targets pass.

The stream contains 2,455 critical-pair bodies; their owner inventory and
multiset digest are retained in the verification. No mathematical rules were
changed. This full-context warning count is not directly comparable to smaller
import-closure counts. Expected failed comparisons inside negative assertions
remain visible in the log. The exit status is success, with subject reduction
enabled.

The check reports 211.01 seconds of rewriting out of 219.23 seconds measured
inside the checker (96%) and about 90.66 billion allocated words. The lower
retained-memory footprint is useful, but this is not evidence that the
mathematical normalization cost is resolved. This current-source run is not
an exact-source speed comparison with the earlier installed-binary failure.

Compiled-object caching was considered but not selected: this pinned checker
uses source/object modification times and does not replay source flags from
objects. A cache path would need its own flag, dependency and loading-order
qualification. Releasing an unused batch snapshot keeps this experiment on
the established source-only path.

This audit is not production promotion. The five terminal obligations,
remaining registered-consumer coverage and supported-toolchain qualification
remain separate. Keep the patch isolated until the supported runtime path and
its identity/pins are deliberately qualified. Continue with required consumers
and the terminal contract; do not repeat this successful combined run without
changed inputs, runtime or a new interaction question.
