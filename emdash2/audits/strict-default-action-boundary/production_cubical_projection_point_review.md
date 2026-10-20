# Corrected Sigma projection observations

Date: 2026-10-20
Predecessor: `b42c22435673b9f23a6e48129124df34a169512a`
Status: qualified in staged core and affected consumers; production promotion remains open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification record](production_cubical_projection_point_verification.json)

This completes the disposition of the seven old same-base opposite clauses
inventoried in the [earlier review](production_cubical_total_review.md).
It concerns existing Sigma and cubical consumers, not the paused nerve goal.
All implementation remains in the non-library migration replay.

## Original clauses and corrected contracts

Write T = Op_cat, R = CoAbove2_cat, and O = TotalOp_cat. The original block
is retained in Git at the source pin
`f8af1fca472657ff1598c639eb29c0566e7b2ec0`, in
`emdash2/emdash3_2_cubical_square_total.lp`, between the pointwise-opposite
projection comment and `homdc_inner_total_func`. Its exact hash is retained
in the emitted migration manifest. The old same-base Op types are not valid
contracts for the selected duality.

| Original observation | Corrected disposition |
| --- | --- |
| Project a constructor-visible opposite total arrow | Use O on the canonical Cartesian projection over R(K). Native action reduces the visible pair to its actual base arrow. No special opposite rule is needed. |
| Project after a Sigma parameter map | The same O/R presentation reduces through the native capped Sigma-map projection law. The actual parameter and arbitrary total arrow remain. |
| Project after total base change | The capped law computes through the actual base functor F and canonical Pullback_catd source. The Cartesian-composite source view agrees at proof time; it is not the same runtime normal form. |
| Reindex the whole opposite projection | Existing corrected whole rule uses TotalOp_funcd, R-shifted bases and the actual identity reframe. |
| Project base change on a whole section | Existing corrected section comparison retains F and its reindexed source. |
| Project a whole parameter-map section | Existing corrected section comparison retains the actual parameter map. |
| Project the whole identity graph | Existing corrected comparison yields the identity on O(K). |

The last four rules were already migrated in
[the whole projection fragment](production_cubical_projection_views.lpfragment).
The new work qualifies the first three observations. Retiring their old
commented implementations does not claim that all three old runtime formulas
survive literally: the base-change source-view distinction is explicit.

## Two missing projection orders

The migrated core already has the whole laws

```text
π_D ∘ Σ(FF) → π_E
π_D ∘ total(F,D) → F ∘ π_(F*D).
```

Taking first-Hom action before forming the whole composite leaves nested
`fapp1_fapp0` heads. The whole rules cannot match those heads. The two added
[Sigma-map](production_sigma_map_projection_hom.lpfragment) and
[base-change](production_sigma_basechange_projection_hom.lpfragment) cuts
implement these same laws at that observation order. Both retain the
original constructor-visible total endpoints and arbitrary arrow α. They
do not introduce a new stable head, change FF's laxness, or force an arbitrary
total arrow to be a constructor.

The attempted rule with entirely arbitrary total endpoints fails subject
reduction: its typing needs unprovided endpoint/fibre identifications.
Retaining the original visible endpoints supplies the sufficient guard.
Canonical pullback families stay on the right of the base-change rule;
capturing an alternative source-family presentation did not solve the
remaining comparison and is not selected.

The new controls exercise both whole-composite and capped-first orders.
This is a local computational repair in the migrated core, not a change to
the expected mathematical projection law.

## Source presentation and proof-time comparison

The same reindexing has the named `Pullback_catd(D,F)` and Cartesian
composition `D ∘ F` presentations. Their first-Hom Sigma projections can
retain different source-family heads. The new
[congruence clause](production_sigma_projection_frame_comparison.lpfragment)
compares the same endpoints and the same arrow only after checking both
complete families and both source/target annotations. These are sufficient
congruence conditions, not injectivity inferred from equal projected values.

For the actual base-change consumer, first compare these source projection
arrows by typed reflexivity, then apply the existing equality congruence
`eq_ap` through F's actual Hom action. Direct reflexivity after the outer
F-action does not chain these unification steps. The staged proof is a
diagnostic observation; no equality/proof argument is added to Sigma, Homd,
the parameter map or base change.

The alternative source formula remains an explicit negative conversion
control, while its derived proof-time agreement is positive. An unrelated
arrow comparison is negative. This records the limit instead of installing
a runtime fold between the two source presentations.

## Diagnostic formation and qualification

The [reviewer fragment](production_cubical_projection_point_controls.lpfragment)
adds nine positives and three negatives to the existing square-total
reviewer. Its `cstd_review_` names are transparent test-only abbreviations
for existing whole operations. They are not new kernel owners.

The constructor observation rebuilds a visible pair from the already typed
decoded Hom. An arbitrary neutral total arrow is not assumed to reduce to
its first component. Negative comparisons use canonical
`Obj(Hom_cat(O(A),a,b))` carriers: the readability alias `Hom` otherwise
triggered an endpoint-inversion typing failure before the intended
comparison. Those ill-typed attempts are recorded as diagnostic errors,
not mathematical negative controls.

The selected core passes 287 positive and 85 negative assertions; the
existing cubical reviewers pass 34/7; the combined diagnostics pass 2180/286;
and the library regression passes 178/27. All use the installed checker with
subject reduction. The core/combined/library warning body multisets remain
exactly 1600/2056/2383; the cubical closure has the same bodies as the core.
Both advisory LHS audits report no unreviewed candidates, supplemented by
manual review of the actual patterns and retained arguments.

The combined sample takes 126.538 seconds and 6663.8 MiB; the library sample
takes 57.637 seconds and 4388.3 MiB. The earlier core sample was faster,
while the earlier combined/library samples were slower. The core allocation
count rises by about 1%, with similar peak memory. These measurements do not
establish a speedup or isolate a slowdown's cause. The current combined run
selected a 600s deadline following the slower core run, but finished within
the earlier 300s limit; the library retained 180s. Memory defaults remain
unchanged, and the larger original all-import context is not thereby qualified.

The exact receipts, source hashes, resource settings and warning comparisons
are recorded in the verification artifact. The original central diagnostic
source is byte-identical to the preceding checkpoint, preserving all 2440
statements and its source-coverage inventory.
The five terminal runtime obligations, remaining normalization and
full-context/resource gates, and production promotion remain open.

Replay after changes to the projection owners or their displayed consumers:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LP_TIMEOUT=180s EMDASH_LP_MEMORY_MIB=4096 \
EMDASH_LAMBDAPI_FLAGS='--record-time --too-long=0.5' \
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20,v=1024 \
python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors cubical_migration_controls.lp
```

Upstream rule changes additionally require the recorded core, combined and
library consumers. Reuse receipts only when their exact inputs and runtime
profile still match; source coverage is not execution evidence.
