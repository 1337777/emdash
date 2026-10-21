# Native square and kernel/cokernel/homology family actions

Date: 2026-10-21 UTC
Status: qualified non-library staging; broader native column homology paths and production qualification remain open
Predecessor: `20dee463`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Original constructions retained

The whole square-family map now uses the existing native oplax exchange of
its original whole square. The source/target observations use the existing
whole exchange-at paths. The actual u/v/a/b maps and original square equation
remain; no pointwise substitute or additional caller coherence is introduced.
All three original declarations check with the existing OneCat target guard.

The original kernel/cokernel family actions retain their selected adjunctions,
inverse mates, whole maps and projection/naturality arguments. Diagram
coefficients and evaluation-composition helpers use their native profiles.
Two raw/canonical mate comparisons in each proof are joined by the existing
kernel/cokernel mate-projection views. No new comparison rule is added.
The cokernel view becomes public for this actual caller; its type and body
are unchanged. The original cokernel reconstruction reviewer checks fresh
alongside the new family-map consumer.

`ProductPathFamily_catd` now targets `Cat_cart` in its existing path-lift body,
matching the already-migrated `Catd` classifier. All other groupoidal closure
and structured-transport constructions are retained. The homology-family map
and its quotient relation then use the original constructions at those native
profiles. No operational equality cast or new primitive is introduced.

All 65 original declarations across ten newly staged library files are
retained. The visibility change is in one already-staged proof owner. Four
original reviewers enter the staged suite; their assertion polarities remain.
The unit-view reviewer's kernel example required its native diagram/total-dual
annotations, while the two product reviewers are unchanged from the source pin.

## Inherited comparison rules

Four newly loaded original owners contain eighteen proof-time views:

- Two functor-category unit views retain the category, unit endpoints and
  actual arrow.
- Nine product-family views retain the observed coordinate, original factors,
  or all endpoint/component/parameter data as appropriate.
- Five product-action views describe the actual diagonal Hom action, identity
  application, native projected composition and same-operand congruence.
- Two mate views retain the same selected adjunction, forward/inverse choice
  and input, comparing only their endpoint presentations.

Those rule files are byte-identical to the pre-migration source. No runtime
rule or arbitrary naturality/extensionality principle is added. Projection
views may forget the unobserved product coordinate; they retain the data of
the coordinate being compared. The existing typed reflexivity and negative
controls remain actual consumers. The LHS script reports zero candidates,
but it does not inventory these unification clauses; this manual review is
required in addition to that output.

Because these views are newly loaded into the expanded staged context, and
because a previous proof-owner file changes visibility, fresh core and full
staged-library regressions are used here. Old aggregate input hashes are not
silently updated to stand for those checks.

## Qualification

All checks are serial, with subject reduction and warnings enabled, the
64 MiB file cap and no-swap guard. The focused check uses 300s/3 GiB; the
fresh core and complete staged-library checks use 600s/4 GiB. All use
`OCAMLRUNPARAM=o=20,v=1024` and the isolated batch-snapshot checker recorded
in the verification file; the installed checker remains unchanged.

| Scope | Positive / negative assertions | Wall time | Peak RSS | Receipt |
| --- | --- | --- | --- | --- |
| Original family-map, cokernel reconstruction and unit/product controls | 33 / 21 | 159.639s | 1,669,928 KiB | `20261021T123357Z-c57dcc642528464a91fba64c46f905fe` |
| Fresh core regression | 2,227 / 317 | 332.147s | 2,115,380 KiB | `20261021T123750Z-a52fb116a6f249bdb7338b782c4fb473` |
| Complete current staged library | 1,082 / 193 | 345.419s | 2,156,452 KiB | `20261021T124323Z-7d5a8cb0917a4a0f92fe71db62cfd559` |

The core keeps the five previously recorded terminal runtime exclusions.
The library scope contains all currently staged registered files except the
full central diagnostic, which is qualified separately only at its recorded
subset. Counts include imports and are not disjoint totals.

The development failures remain recorded: the old square exchange profile,
the product-path family coefficient, ordinary evaluation-composition calls,
raw/canonical kernel and cokernel mate presentations, and stale annotations
in the unit-view reviewer. They are separate typing failures, not semantic
impossibility claims. The existing shared owners resolve them without
inventing another square, adjunction or homology theory.

The focused warning multiset is unchanged at 2,162 bodies. Relative to the
preceding corresponding regression scopes, the core reports 2,455 bodies
(24 added, 18 absent) and the library 2,521 (65 added, 53 absent). Every
reported runtime owner in these differences has the same input hash.
The changed core cases, and the remaining library cases described below,
involve existing odd/even-duality action, identity and composition overlaps.

Twenty-seven sheafification and two monad warning pairs have exactly the
same initial critical term and the same two rewrite clauses, but different
printed normal forms. In particular, they expose existing `sigma_map_obj`
versus raw `fapp0(sigma_map_func ...)` presentations. Their arbitrary-object
join is proof-time, not an unconditional runtime rewrite. The two earlier
pullback/sheaf-identity peaks are not emitted in the new context; that fact
alone does not show they now converge.

This is recorded as import/elaboration-context sensitivity under R07/R12,
with successful current consumers, not a global confluence result or a claim
that all differences are formatting. The verification stores changed-body
hashes, origins, multiplicities and initial-term/rule-pair hashes. Exact
expanded bodies remain recoverable from the immutable receipt logs; they
are not duplicated as large tracked artifacts.

All fresh inputs match the emitted source and tracked drivers. The normal
resource defaults and installed checker remain unchanged. These measured
costs remain relevant to R12; a larger permitted deadline is not a usability
certificate.

Coverage reaches 295 library/core files and 106 complete reviewers. The full
central diagnostic remains an additional staged file with exactly five
runtime exclusions. There remain 496 registered core/library files and 490
reviewers unstaged. These counts describe migration coverage, not remaining
work estimates.

## Continuation

Resume `examples/freyd_native_column_homology_paths.lp` and its original
middle-column, point-action and diagram/homology-path dependencies. Its initial
baseline stopped at the square-family owner; this slice qualifies that shared
chain but does not claim the complete native column homology-path reviewer.
No final-source run of that larger target is substituted by the focused tests.

The five terminal Homd runtime obligations, remaining library/diagnostic
migration, normalization/usability, supported checker/resource profiles and
production gates remain required. The separate nerve goal stays paused.
Production source, catalog and health claims are not promoted by this audit.

Replay uses `production_owner_migration.py` and the tracked
[focused](production_family_actions_regression.lpfragment),
[core](production_family_actions_core_regression.lpfragment) and
[library](production_family_actions_library_regression.lpfragment) drivers.
The [verification record](production_family_actions_verification.json) retains
exact inputs, checker/profile hashes, inherited-rule and declaration inventory,
warning comparisons and failed variants. Recheck affected boundaries when an
owner, source pin, checker or runtime profile changes.
