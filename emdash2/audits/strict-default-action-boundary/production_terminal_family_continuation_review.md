# Whole terminal-family continuation

Date: 2026-10-21 (UTC)
Status: qualified in the non-library staged replay; production unpromoted
Predecessor: `6a9f27b0aac0b2180fe3b556eaa78e529e5f5d53`.

The [source adapter](production_terminal_family_migration.py) and
[derived reflection](production_oplax_family_reflection.lpfragment) preserve
the original terminal/initial family outline. The
[verification record](production_terminal_family_continuation_verification.json) records
source hashes, original assertions, resources, warnings and earlier failures.

## Preserved construction

The terminal-family universality owner now uses the existing oplax diagram
coefficient and the already implemented
`one_cat_oplax_*_adjunction_family_presentation_*` operations. Initial data
use `TotalOp_cat`. The original maps, chosen inverses, unit/counit observations,
and OneCat hypotheses are retained. This does not supply a new adjunction or
weaken a whole family statement to its point components.

Whole reflection is a derived counterpart at the existing shared owner:
`one_cat_oplax_diagram_family_map_path` assembles the existing fixed-diagram
reflection through `one_cat_modification`, then uses the existing ordinary
target discreteness. Its inputs are the same kind of whole endpoint paths
as in the original family reflection. The existing shape-universality and
ordinary modification introduction remain structural boundaries; this proof
does not derive them from projection rules. No new primitive, runtime rule,
unifier, operational proof payload or caller premise is added.

Its endpoint annotations use composition with the actual fixed-evaluation
functor, exactly as `diagram_oplax_family_map_at` does. The initial attempt
instead annotated them with represented precomposition. For J composed with
A, that representation retained a composite input before the endpoint could
compute. Aligning the annotations resolves the original whole terminal and
initial reflection consumers without a new normalization rule. The existing
`diagram_oplax_family_at_func` owner is unchanged.

The incoming-arrow family similarly retains its declared source J composed
with A in the body. The old `comp_cat_cov_func` action spelling is replaced
with that composite, already required by its input h;
no transport of h is introduced. The original five positive and one negative
incoming observations pass. The generator observation decodes the same
strict diagram object, while arrows between diagrams are observed by whole
fixed evaluation. The incoming interface still admits arbitrary B, C and a
general lax h. OneCat remains a guard only for the reflection/universality
operations that already required it.

## Qualification and performance

The [final combined driver](production_terminal_family_regression.lpfragment)
passes **40 positive and one negative assertions**, including all 22 original
terminal-family assertions, five incoming assertions, the original incoming
noncollapse check, ten existing introduced-input assertions and three
inherited source assertions. All imported declaration bodies also check.

Receipt: `20261021T032137Z-c24b073d903b404b87576fc3a647cef4`.
Time/RSS: **93.192s / 1,052,848KiB**, under 180s/2GiB/o=20, using the isolated
checker ([boundary qualification](production_checker_boundary_review.md))
with subject reduction, warnings, source loading, serial execution,
file limits and no swap. The single terminal reviewer previously took
74.183s and the whole-family path module 81.307s; the combined scope therefore
retains explicit 180s headroom. No default limit or installed binary changes.

The final 2,284 critical-pair bodies are an exact submultiset of the preceding
Freyd-entry check: the only 16 absent bodies belong to its additional Freyd
operations import. Relative to the smaller terminal-only check, the 132
additional bodies come from the existing triangular-product and truncation
imports. The separately loaded family prototype has a different warning
distribution from import order; the exact counts remain recorded. No new
warning body is introduced by the changed owners, which add no formal rules.

The earlier integration, entry and central receipt input sets each differ
only at the shared reflection module. Its entire earlier prefix is preserved
byte for byte; only derived definitions are appended. The prior integration's
append includes the already qualified predecessor definitions as well. This
is explicitly reviewed conservative carry, not automatic reuse of a changed
input hash. The existing introduced-input consumer is freshly checked after
the new definition. Core and full central diagnostic hashes are unchanged.

Coverage reaches **242 registered library/core files and 86 reviewers**,
with the full central diagnostic still excluding exactly the five terminal
Homd runtime positives. Another 549 registered library/core files and 510
reviewers remain unstaged. These are coverage counts, not a percentage of
remaining engineering effort.

The full Freyd-column check progressed beyond the repaired family owner but
hit its 180s deadline while loading existing row/naturality prerequisites
(receipt `20261021T031326Z-26012a2e27cf47aba5c44e11a9e8e698`). It had reported
no new typing failure before termination. Its killed-child RSS accounting is
not a memory-performance conclusion. Next use a measured 300s/2GiB profile
for that same consumer, preserving the memory cap and command timing, then
continue at its first actual failure. The column and middle-column reviewers
remain unqualified. Rewriting still dominates the focused run; no overall
performance fix is claimed.

This staged-only checkpoint does not change the active source registry,
catalog or production health snapshot. Their synchronization, supported
checker qualification, remaining migration and full integration gates remain
required before promotion. The five Homd runtime obligations remain open.

## Replay

From `emdash2`, emit the staged package with
`python3 audits/strict-default-action-boundary/production_owner_migration.py`,
copy the linked combined driver into that package as
`terminal_family_regression.lp`, then run it through `scripts/run_lambdapi.py`
with the exact isolated checker and 180s/2GiB/o=20 profile recorded above.
The source adapters are authoring tools; the emitted LP and receipt are the
qualification boundary.
