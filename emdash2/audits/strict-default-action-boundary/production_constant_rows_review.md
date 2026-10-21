# Constant-transformation inclusion and whole native Freyd row paths

Date: 2026-10-21 UTC
Status: qualified non-library staging; full columns and production promotion remain open
Predecessor: `b82d5788`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Construction and migration boundary

The original constant-transformation comparison still describes postcomposition
by a fixed functor, with identity in the second horizontal slot. The migrated
`Const_transf` has strict-transformation type. Its old uses in the comparison,
reviewer and three Freyd row paths lacked the existing `strict_transfor`
inclusion into ambient transformations. Adding that inclusion preserves the
original arrow, functor, endpoint data and identity restriction. It does not
strictify arbitrary ambient transformations.

A matched owner experiment changes only this comparison file. The corrected
reviewer with the old rule fails its first positive assertion; the adapted
rule passes that assertion and both original negatives. A different arrow or
a general second transformation is still rejected. All three original whole
Freyd row declarations are retained, with their original reflexivity bodies;
the RHS constant transformations use the inclusion.

The first whole row projection then passes, but the middle projection exposes
a second, separate mismatch. Its whole endpoint is a stable precomposition
of F by const(x), while the required endpoint is const(F[x]). Raw Cat
composition already computes this equation. A direct proof-time view at the
existing constant-comparison owner now compares the exterior categories and
actual F[x]. It preserves the stable runtime head and adds no runtime rewrite.
A typed reflexivity consumer passes, and the corresponding negative keeps a
different selected object distinct. No opaque comparison carrier, new
operational primitive, supplied evidence or extra strictness hypothesis is
introduced. The native row projection ladder is unchanged.

There is one adapted existing unifier and one added constant-input comparison.
The inferred classifier slots on the strict-transformation inclusion are `_`;
Cat/id and the constant/identity constructors are the actual discriminators.
The existing comparison retains its original source/target guards. The new
view retains K, C, F and x through its output constraints. The generic LHS
script reports zero candidates, and this manual review covers the unification
patterns that the script does not inventory. No general pointwise
extensionality or arbitrary lax horizontal collapse is installed.

## Qualification

The [focused driver](production_constant_transformation_controls.lpfragment)
passes **two positive and three negative assertions** in **27.602 seconds /
185,804 KiB**, under 90s/2GiB/o=20. The old-rule control and inclusion-only
repair differ in exactly the owning comparison file. Their 2,036 warning
bodies are identical; the additional constant-object comparison retains that
same multiset.

Fresh [core](production_constant_core_regression.lpfragment) and
[complete staged-library](production_constant_library_regression.lpfragment)
regressions pass **2,204/298** and **993/166** positive/negative assertions,
respectively. Measurements are **294.304s/2,126,148KiB** and
**292.982s/2,147,852KiB**. Exact receipts:
`20261021T094003Z-32fe716c4ed845ba9851307f13cee2aa` and
`20261021T094458Z-583bca667d8c4dadbbfc5f0393504fb4`.
All recorded inputs match the emitted candidate, including the three whole
Freyd row-path proofs and original constant-comparison reviewer.

The broad warning multisets have 2,449 and 2,509 bodies. Relative to their
previous corresponding scopes, core has 20 added/26 absent bodies and library
22 added/36 absent. Every changed pair involves existing alternating-duality
identity/action/composition rules. The diagram source and all reported owners
are unchanged; importing the constant owner earlier changes their overlap
order/scope. The [verification record](production_constant_rows_verification.json)
retains full changed bodies, origins, source hashes and classification. These
are reviewed warning differences, not an assertion of global confluence.


The staged library scope now covers 262 library/core files and 96 complete
reviewers. The additional full central diagnostic file still has exactly five
runtime exclusions. Of the registry, 529 core/library files and 500 reviewers
remain unstaged. Original reviewer polarity is retained. Counts describe
coverage, not remaining effort or completion of the full diagnostic.

The original full column run passes all three whole row paths and then fails
at `one_cat_constant_zero_factor_path` in
`emdash3_2_one_cat_constant_chain_zeros.lp`, whose old constant/diagram profiles
are not yet migrated. Its failed run is not a complete column qualification.
The source retains the original zero and short-exact assumptions and selected
maps; no pointwise replacement is counted as its whole result.

## Resource and continuation boundary

The direct row-file baseline reached its 180s deadline while importing Freyd
operations/usability, before its row proof. It is not a semantic counterexample.
The established full-column import order reaches the next owner in about
112 seconds under its explicit 300s/2GiB profile. That order-sensitive import
cost remains normalization/toolchain evidence. The timeout receipt's small
wrapper RSS is not claimed as the killed checker's peak memory.

The broad regressions use the already reviewed serial 600s/4GiB/o=20 profile,
with recorded host headroom before each target. Subject reduction, warnings,
file limits, source loading and no swap remain enabled. The isolated checker
is unchanged; the installed checker is not promoted. No unchanged broad run
is repeated merely for reassurance.

Next migrate the original constant-chain zero owner and reviewer, followed by
its native row-zero consumer. Their candidate mechanical profile corrections
are prepared only in the ignored continuation workspace and remain untested.
The five terminal Homd runtime obligations, full columns, remaining migration,
normalization/usability, supported checker and production qualification remain
required. The separate nerve goal stays paused.

Replay uses `production_owner_migration.py` and the tracked focused/core/library
drivers. Recheck affected consumers after changes to the owners, source pin,
checker or runtime profile. The production catalog and health evidence are not
advanced from these non-library checks.
