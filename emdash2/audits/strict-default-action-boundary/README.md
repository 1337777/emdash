# Strict-default action owner audit

Status: non-library implementation pilot; no production rule is promoted.
Plan: [SF-0 / SF-1](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
Source: main `f8af1fca472657ff1598c639eb29c0566e7b2ec0`; the replay pins the
core and profile source hashes and inserts at unique original owner anchors.

## General intrinsic action needs a weaker index profile, 2026-10-15

The [review](homd_index_profile_review.md) records a semantic obstruction to
the preceding all-Cart inner Q Hom. An ordinary strict functor, viewed as a
terminal-source section, must retain noninvertible base-cell action; strict
index naturality between constant diagrams would collapse its components.
Default lax naturality over the transposed index has the reverse direction.

The [derived candidate](production_homd_index.lpfragment) defines
`P(I)=T(Functor_cat(I,T(Cat_cart)))`, its whole Cartesian inclusion and a
negative total using existing operations. There are no new primitives or
rules. The [controls](production_homd_index_controls.lpfragment),
[finite direction check](homd_index_profile_model.py) and
[verification](production_homd_index_verification.json) delimit the evidence.
The next proposed Q has `Hom_Q(A,B)=Cart(A,P(B))`; it is not yet integrated.

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package index_profile.lp
```

The full emitted core is unchanged from `e594bcea`. Its old direct ladder
checks remain valid for the stated computational contract, while the general
intrinsic extension of that all-Cart profile is rejected. Next qualify the
index-arrow action and integrate the weaker index into the existing Q/Homd
and intrinsic projection owners. Do not add supplied laxity or another Sigma.

## Native Q/Homd source ladder, 2026-10-15

The [native Homd owner](production_homd_core.lpfragment) now replaces the
invalid ordinary-Pi target in the original-source migration. It uses the
existing Hom and fibre-covariance owners, with no parallel `sf_cart_hom*`
primitives. The identity core is independent; public `homd_int(FF)` is the
ordinary displayed view of a defined relative composite, retaining lax FF.
The [whole consumers](production_homd_controls.lpfragment) check root-to-leaf,
source-u and higher action, whole x-naturality, and the general-FF relative
section/leaf. The [verification](production_homd_verification.json) records
the final exact source, normalization fixes and remaining full-source failure.

Current passing replay from `emdash2`:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package homd_prefix.lp
```

This target also carries the preceding foundation/Pi/Sigma/mixed-family
controls. The full emitted source stops at `tdapp1_int_func_transfd`'s old
use of `Op_funcd(FF)`. The index-profile correction above must precede its
corrected intrinsic direction and extracted projections, then late consumers.
Q's represented laws remain structural contracts, not a derived complete
composition/coherence theory. The full goal and public promotion remain open.

One invalid helper name, `Homd_target_section_catd`, is replaced by the actual
`Homd_target_section_cat`. All other original declarations remain, with
explicit dependency relocations. No later source section is truncated.

## Pi, Sigma and mixed-family source continuation, 2026-10-15

The current [recipe](production_owner_migration.py) checks through section
10 of the migrated original source. The
[verification](production_sections_verification.json) records the current
`mixed_prefix.lp` target and full-source failure separately. The previously
failing varying-base Pi declaration now consumes the actual
[Cartesian family-parameter constructor](production_family_classifier.lpfragment).
Its component includes these parameters into the existing lax diagram
category before applying Pi. The [section controls](production_sections_controls.lpfragment)
retain lax FF and the existing whole constant-section comparison.

Corrected total-fibre duality now feeds the original Sigma-Hom and recursive
projection owners. The mixed `Functor_catd` uses Cartesian coefficient Homs;
its positive parameter remains lax, while contravariant parameter maps are
Cartesian. `Hom_catd` retains the original Pi architecture with its shifted
negative section. No auxiliary Sigma composition theory or new section
primitive is introduced.

Replay the currently passing boundary from `emdash2`:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package mixed_prefix.lp
```

The complete emitted kernel now fails at the legacy `Edge_catd_func`, whose
same-base transpose assumption must be replaced together with the Q/Homd
target and ladder. General-FF intrinsic action and downstream qualification
remain open. All later sections are retained. Two named declarations move
after their Hom dependency; the source manifest records those exceptions
instead of claiming unchanged declaration order.

The direct carrier coercion between constant-section arrows and ordinary
transfors also fails in the original pre-goal source. This checkpoint keeps
the passing whole-category comparison and records that normalization limit
without adding an unrelated rule. Earlier records below are historical.

## Coupled family/Hom source prefix, 2026-10-15

The current [production recipe](production_owner_migration.py) changes the
original family/Hom, duality and Cartesian closure owners together. Its
prefix through section 8b passes the [focused controls](production_foundations_controls.lpfragment).
The [verification record](production_foundations_verification.json) pins
the exact prefix, predecessor warning comparison and full-source failure.
The full emitted kernel currently fails at the varying-base `Pi_int_funcd`;
the earlier passing reviewer receipts below are historical, not current.
Public sources and the completed Homd milestone are not claimed by this
non-library checkpoint.

Replay this boundary from `emdash2`:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package foundations_prefix.lp
```

The recipe also emits the complete original-source migration. Checking its
`emdash3_2.lp` currently fails as recorded; no tail has been removed. Every
original named declaration remains in order, while necessary type/body
replacements are recorded by owner rather than described as insert-only.
The baseline warning prefix was cut before section 8c from the exact
`90d10b39` source input blob named in the verification record. Generated LP,
logs and source blobs remain ignored.

The prefix retains ordinary lax transformations, with Cartesian profiles
only at the selected coefficient and joint Cartesian operations. It checks
shifted-family higher action and excludes raw lax input from same-profile
transpose/evaluation. Higher coefficient and adjunction coherence, varying-
base Pi, Q/Homd/Sigma integration, general-FF intrinsic action and downstream
qualification remain open. Continue with the existing varying-base section
owners; optional alternative foundational designs stay deferred.

## Conventional-lax production-source continuation, 2026-10-15

The same [production recipe](production_owner_migration.py) now includes
the selected default pre/right action and its intrinsic identity cell.
The [current verification](production_conventional_lax_verification.json)
pins its passing original reviewer and whole/capped/extracted-cell controls,
while retaining post/left non-strictness observations. The
[precomposition comparison](production_conventional_pre_reading.lpfragment)
repairs the actual original pathout consumer. The comma proof retains its
forward maps and now carries the actual inverse evidence through its
[base-change composition](production_comma_basechange_equivalence.lpfragment).

At checkpoint `90d10b39`, replay used the package-local commands below. This extends `f691a846`; its
earlier record remains pinned historical evidence. The old whole-opposite,
family/Homd/Sigma and joint Cartesian signatures still require their coupled
migration. Passing these source checks does not qualify those old contracts.

## Original-source migration checkpoint, 2026-10-15

The [production source recipe](production_owner_migration.py) now stages
the full pre-goal nucleus and the original profile reviewer/import closure.
It preserves every original nucleus line and uses the existing public owner
names. The strict-default upstream additions and required proof adaptations
pass the staged reviewer and [focused controls](production_owner_controls.lpfragment).
The [verification record](production_owner_verification.json) pins the exact
package inputs, warning comparison and rejected alternatives. No production
file is replaced; the coupled family/Op/Homd/Pi/Sigma and closure migration
remains open in the [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md#current-execution-contract).

The original comma comparison keeps its forward construction. Its
[inverse-evidence helpers](production_comma_equivalence.lpfragment) and
[adapted target proof](production_comma_target_equivalence.lpfragment) are
definitions through existing operations, with no new rewrite/unification
rules or stricter FF admission. Alternative Sigma-map normalization rules
were rejected and are absent. Optional improvements remain deferred.

The earlier full-source checkpoints used these package-local checks. On the
current recipe they encounter the recorded incomplete source migration;
use the prefix command above for its currently passing boundary:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package examples/gray_profiles.lp
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --no-colors --quiet \
  --package-root tmp/probes/production_owner_migration/package owner_controls.lp
```

Replay when this recipe, its pinned authoring inputs or an affected original
consumer changes. The prior outer `probe.sh` runs checked staged sources but
inventoried imports against the outer package; their dependency snapshots
are not exact staged-package evidence. Generated LP, logs and diagnostics
stay ignored. The separate auxiliary Sigma-composition owner is not used.

## Public-contract qualification, 2026-10-14

The user reaffirmed `Hom_cat Cat_cat A B = Functor_cat A B`: strict default
functors and non-strict transfors. The Cartesian-universe variants catalogued
below are comparison evidence, not the selected public contract. Their
passing Homd counts are conditional on that stronger universe. Explicit
strict-transfor input packages are not accepted as the foundational Op/Homd
repair. The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md#current-execution-contract)
owns this superseding boundary. Preserve the evaluator/composition
counterchecks while correcting the operations under the agreed public
contract; do not reinterpret those failures as permission to narrow FF.

Later decision on the same date: the user explicitly selected conventional
lax transformations as the default, with the existing extracted pre/right
leg globally identity and the post/left comparison retained. The
[conventional-lax owner candidate](conventional_lax_review.md) now checks
ordinary action and that deep cell without a profile wrapper. This replaces
the broader raw two-leg default as the migration target, while preserving
the public Hom and Transf/Functord interfaces. Its focused checks do not
qualify the legacy Cartesian operations or the whole Homd construction.

Latest Q follow-up: the user now keeps both nested-Cart and lax Q open for
comparison against the direct Homd milestone, without changing the public
Hom(Cat)=Functor_cat contract. The
[canonical transport-map consumer](strict_fibcov_review.md) checks the first
whole-family use of the strict displayed-map classifier and records a
finite comparison of their different higher-action requirements. Its
65 positive/27 negative controls do not complete the Homd root.

The subsequent [represented section candidate](strict_homd_section_review.md)
checks the direct whole-y section, fixed-x u action and a defined strict-FF
relative section on raw Q. Its 96 positive/33 negative controls are
conditional on explicitly declared Q/mate structure; general coefficient
coherence and the outer root are not certified. The direct Cart substitution
has a recorded formation failure and is not confused with an adapted Cart
implementation. Both Q designs remain open under the current plan.

The [coordinated transposed-target root](homd_transposed_target_review.md)
now checks the whole identity root and its full x/u/y/v/f observation,
using the actual represented x-package and a whole target family over K.
The same defined target action accepts raw lax FF; strict-FF conveniences
wrap it. Its 122 positive/42 negative controls do not certify Q coherence,
intrinsic extraction, Sigma-Hom or production migration. The relative root
has a proof-time whole-section comparison with a directly computable
compositional view; the identity-root leaf itself computes directly.

The [intrinsic-action projection continuation](homd_intrinsic_projection.lpfragment)
now reaches filler transport and the extracted forward laxity cell through
that root. The whole action remains structural, with higher coherence and
whole-u laxity assembly open. Its [single-candidate replay](homd_intrinsic_projection_replay.py)
and [evidence](homd_intrinsic_projection_verification.json) preserve that boundary.

The subsequent [mixed three-cell review](homd_mixed_three_cell_review.md)
finds a semantic obstruction to the unchanged double-Gray-lax Q/source-u
package, even for identity FF. Its finite model and transported inner-Hom
proposal delimit that broader candidate. The native receipts above are conditional
typing evidence; do not promote the unchanged Q or replace it with nested
Cart without addressing the already recorded family-admission obstruction.

Following the user's separate-coefficient proposal, the
[Cart-family comparison](cart_family_review.md) now checks a whole coefficient
inclusion, canonical Hom family and the fixed-u whole map Hom_K(x,-)=>E.
Variable admitted families have strict fibre naturality, and a represented
base two-cell is recovered by actual computation. The public lax Hom and
general FF remain distinct. Full coefficient/Q coherence and the Homd
ladder under this new input type are not yet qualified.

The [whole-u covariance continuation](cart_family_u_review.md) adds the
actual E[x]-parameter functor into Cartesian diagram maps. Its y/f
projections compute on objects, arrows and a fibre two-cell, with both
whole-first and capped-first observations. This is a reusable input to
the Homd mate construction, not the full Homd or public migration.

The [Cartesian represented-Hom continuation](cart_represented_hom_review.md)
uses that covariance as the actual first Hom of Cartesian Yoneda. The
target-first represented Hom is then a defined composite; its local Homd
v/f projections and actual index action compute with Cat_s coefficients.
Whole y-section and x-root assembly remain separate required work.

The [Cartesian-family whole Homd section](cart_homd_section_review.md) now
uses an actual iterated-Hom section category and a defined source-u functor.
Its direct y/v/f projections, source-u arrow action and pre/right y-action
compute under structural Q/mate contracts. Default Transf remains lax;
the shared E/I_x coefficient is Cartesian. The outer root, extracted
comparison coherence and Sigma-Hom remain open.

The [Cartesian-family whole root](cart_homd_root_review.md) adds the defined
Cartesian target H_E and canonical strict root. The complete direct
x/u/y/v/f ladder, an independent whole-functor naturality comparison and
the actual base-two-cell component all pass. Q/mate compatibility remains a
structural contract; extracted y-comparison coherence, Sigma-Hom and public
promotion are still required.

The [general-FF relative/intrinsic continuation](cart_homd_relative_review.md)
defines the whole target action and relative root for default lax FF between
Cartesian families. The literal section/leaf and identity specialization
compute. Its corrected whole internal-action type projects to a filler map
and forward laxity; identity-map normality is checked without collapsing
general lax FF boundaries. Nonidentity comparison coherence and Sigma-Hom
remain open.

The [ordinary internalization continuation](cart_homd_ordinary_review.md)
defines the canonical F-action and the positive lax-transformation action
using covariance and fixed postwhiskering. The actual Homd y-comparison is
then extracted through the native intrinsic action, with direct v/k
projections and the expected target Hom. Its represented-source beta and
full coherence remain open; no new comparison witness is supplied.

The [represented-composition beta](cart_homd_composition_review.md) connects
the extracted Homd y-comparison to its concrete generator computation and
first higher action. Stable native projection rungs replace the unsuccessful
expanded-endpoint matching approach. The represented introduction/beta are
structural computation laws, without establishing a general Q model.
Continuation follows actual Homd/Sigma consumers; public migration remains.

The [current Cartesian-family Sigma-Hom candidate](cart_sigma_review.md)
consumes the direct Homd leaf through a derived total-dual negative Sigma.
The explicit constant-family Hom, forward higher fibre cells, arbitrary
arrow interface and recursive base projection check. This uses the current
separate Cartesian coefficient and introduces no additional Q composition
operation. The [total-map continuation](cart_sigma_map_review.md) derives its
whole first Hom from the negative total of the existing intrinsic Homd map.
General lax FF, mapped transport/laxity, modification components, identity
action and recursive preservation of the base two-cell check. The
[whole composition continuation](cart_sigma_composition_review.md) qualifies
the structural whole intrinsic-composition law and its derived expanded
total-arrow comparison, including identity/constant-family controls.
Its additional stable composition helper has no production counterpart and
is audit scaffolding, not an automatically selected public-kernel addition.
The next step follows actual production owners and required consumers;
public/downstream migration remains and general lax FF is still admitted.

Earlier Q clarification, superseded by the current shared-Cartesian-family
candidate above: both curried mapping levels then used the conventional
lax default, with Gray uncurry when needed. Nested-Cart Q was not selected
at that stage. The plan's historical
[Q/Sigma consumer review](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md#lax-q-gray-uncurry-and-strict-sigma-maps-consumer-review-2026-10-14)
assesses strict-only Sigma maps and records why this need not restrict the
upstream intrinsic Homd extractor. No production restriction is installed.

The [public-universe total-duality candidate](conventional_total_op_review.md)
now checks whole mapping/transformation projections and the derived family's
object, arrow and base-two-cell action. Projection-before-involution and
family-composition typed comparisons pass; seven adverse variants reject
the corresponding missing or wrong clauses. Its 31 positive/10 negative
controls include inherited checks. This is non-library evidence with an
explicit warning ledger, not the completed lax Q/Homd construction.

The [Gray evaluation comparison](conventional_gray_eval_review.md) retains
ordinary fixed evaluation while changing the joint source to Gray and
preserving distinct mixed paths. Its checked slice is retained while the
user-requested comparison with corrected lax defaults is assessed. Neither
this nor the total-duality candidate has been promoted to production.

The [strict displayed-map comparison](strict_displayed_maps_review.md)
checks the proposed strict-map/ambient-section separation using native
carrier and action owners. Its 54 positive/22 negative assertions include
the preceding donors. The public Functord contract remains unchanged;
the review records the coupled migration still required if this alternative
is selected.

Continuation qualification: the stronger
[evaluation-profile review](../../../docs/EMDASH_STRICT_FUNCTOR_EVALUATION_PROFILE_REVIEW.md)
shows that the unchanged Cartesian evaluator plus even the capped strictness
rule derives equalities between arbitrary transfor naturality routes. The
first pilot's conversion negatives do not qualify global retention of lax
transfors. The profile migration is now a promotion prerequisite.

The question is whether the public native action can regain strict functor
computation while retaining arbitrary transfor comparison data and the
existing intrinsic compositor extraction. All candidate rules are in full
copies of the nucleus, before later owners. The first real consumer imports
an unchanged copy of `emdash3_2_gray_profiles.lp` from an isolated package.

| Variant | Expected result | What it isolates |
| --- | --- | --- |
| `baseline` | pass | Original composition and whole endpoint comparisons remain negative; retained action controls pass. |
| `capped` | pass | The single restored composition cut gives strict capped and iterated-Hom action; whole endpoint comparison remains negative. |
| `whole` | pass | Whole post/pre strict functor laws identify the actual endpoints; the extracted compositor is still not identity. |
| `intrinsic` | pass | The actual whole-action projection computes to identity, with the existing defined accessor unchanged. |
| `raw_endpoint` | expected assertion failure | A capped-only patch does not identify the stable represented-composition history with raw composition. This is not a semantic counterexample. |
| `projection` | expected assertion failure | Whole-first evaluation passes, but the already capped postcomposition history needs its own projection join. Both compared terms first typecheck in the same Hom. |
| `joined` | pass | Both post/pre cap-first histories agree after their semantic-owner clauses are added. |
| `profile_consumer` | pass | The existing `IsStrictFunctor(F)` property is derivable without an admission input; different transfor classifiers remain distinct. |
| `constructors` | expected assertion failure | The original pilot lacks the Grpd-valued evaluation/composition join. |
| `evaluated` | pass | Adds Grpd/Cat evaluation joins and guarded opposite-valued composition; 26 positives and three conversion negatives. |
| `evaluation_naturality_capped` | adverse construction passes | The capped-only patch and old Eval derive the undesired naturality equalities. This is evidence against blanket promotion. |
| `cartesian_profile` | interface pilot passes | Shares default functor objects, preserves the distinct higher profile, classifies family transport and rejects the raw-transfor evaluator call. |

The final full-file pilot has 19 positive and three negative assertions.
The latter compare the two naturality routes and the off-diagonal action of
an arbitrary transfor; each term is separately typechecked. No proof/path is
an argument to an action operation. The compatibility theorem in the profile
consumer produces a proof of the old late property; it is not a new input
contract for default functors.

The candidate does not qualify corrected Op, Q, Homd, every constructor's
strict action, or global confluence. Its warning inventory increases from
648 to 796 unjoinable-pair reports. The 148 additional reports, including
Op, identity, composition, evaluation, products, Hom and family projections,
are promotion obligations. Adding the intrinsic-cell clause itself adds no
warning beyond the whole endpoint laws in this replay. Counts are diagnostic
evidence, not a judgment of which pairs are harmless.

## Replay

From `emdash2`, emit the exact source copies into the already ignored
`tmp/probes/strict_default_action/` tree:

```bash
python3 audits/strict-default-action-boundary/replay.py
```

Check any positive full-file variant with the standard bounded guard:

```bash
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  tmp/probes/strict_default_action/joined.lp
```

The real profile consumer resolves imports exclusively in its generated
package; no installed kernel, main worktree, or cache is modified:

```bash
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  --package-root tmp/probes/strict_default_action/package_joined \
  profile_consumer.lp
```

`raw_endpoint.lp` and `projection.lp` must fail at the documented assertions,
not at a declaration, parse, resource, or subject-reduction check. Their
failure establishes the missing computation in that intermediate variant,
not impossibility of the final design. `verification.json` records the
exact emitted hashes, receipts, outcomes, warning counts and measurements.
Raw logs and complete generated source copies stay ignored; fragments and
the replay remain tracked for recovery.

Replay trigger: any edit to the action, composition, represented Hom,
intrinsic-cell or profile owners, or before promoting these clauses. Source
pin changes require review. Retire this experimental builder after a
qualified library promotion and retain its evidence in Git.

## Constructor and integration replay

`integration_replay.py` emits the adverse construction and complete source-
only packages for the represented-comma bisection and nucleus diagnostic,
and stages the proposed Cartesian profile interface:

```bash
python3 audits/strict-default-action-boundary/integration_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  tmp/probes/strict_default_action/evaluation_naturality_capped.lp
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  --package-root tmp/probes/strict_default_action/package_evaluated \
  cartesian_profile.lp
```

The baseline owner (identical to the `comma_baseline` inputs), `comma_capped`
and `comma_whole` pass. `comma_intrinsic` and the stronger pilot fail at its
target-component comparison. Strict candidates adapt only the earlier
`one_cat_composition_path` proof to reflexivity; the adjacent transfor-
naturality proof is preserved. Exact proof and source inputs are replayable.

`diagnostic_evaluated` contains the nucleus diagnostic's 140-file closure.
Use its existing registered profile (6 GiB/180 seconds, `o=20,v=1024`)
explicitly for this isolated package. An earlier 2 GiB replay exhausted
memory; the correctly profiled replay exposed the represented-comma failure.
Default limits are unchanged and the full diagnostic is not reported green.

`verification.json` preserves checkpoint-1162eac2 evidence with its original
authoring hashes. Those emitted LP outputs remain byte-identical.
`continuation_verification.json` records the additional controls, profile
prototype and integration findings at their exact source hashes.

## Coefficient countercheck before evaluation

Restricting only joint Eval is insufficient. The whole construction in
`coefficient_naturality_audit.lpfragment` is inserted before the evaluation
and curry owners. It instantiates strict composition on the composite of
`comp_prod_func Cat_cat` and fixed-object evaluation, using constant functors
and `Const_transf(p)`. The two product factorizations give actual paths

```text
G[p] o epsilon[x] = epsilon[p] = epsilon[y] o F[p].
```

The fragment does not invoke joint Eval, curry, opposite or Homd. It adds
no independent naturality comparison. Passing is adverse evidence for the
unchanged coefficient Hom after strict default functor composition is
restored; it is not a library theorem to adopt.

```bash
python3 audits/strict-default-action-boundary/coefficient_boundary_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_coefficient/capped.lp
```

The full-file capped variant passes in 4.607s at the normal resource limits.
`baseline.lp` rejects the generic strictness lemma. `no_cat_component.lp`
retains that lemma but rejects the first specific naturality path when the
Cat horizontal-composition component beta is omitted. These are checked
typing failures, not parse/resource failures. Exact source hashes, logs and
three receipts are in `coefficient_boundary_verification.json`.

Replay this boundary when changing Cat's whole Hom/composition, Cartesian
evaluation or the strict-default action laws. With strict Cat objects and
the existing generic composition architecture retained, its lax mapping
category cannot also be Cat's Cartesian Hom with the unchanged horizontal
projection. A coefficient/profile correction is therefore a migration
dependency. The audit does not by itself qualify the complete Cartesian
replacement or its downstream typing/computation.

`cartesian_migration.py` retains that unfinished full-file candidate. Its
fixed-whiskering views use the existing mapping constructor; the generic
Cat-derived parameter telescopes retain their original derivations with
Cartesian input Homs. `cartesian_whiskering_controls.lpfragment` distinguishes
the two, including rejection of the adverse raw Cat-composition input.
These controls run at their owners; a later failure still makes the whole
candidate unqualified. No new supplied whiskering theorem is introduced.

The upstream prefix now also contains `cartesian_evaluation_controls.lpfragment`.
It passes 15 positive/four negative controls across both fragments in 1.850s.
The full file fails later at `fapp1_func(Op_catd(E),x,y)`, after 2.340s.
Both exact inputs and outcomes are retained in
`cartesian_migration_verification.json`. The old whole-op declaration is
still in the prefix: this is a local migration check, not a variance or
consistency qualification.

```bash
python3 audits/strict-default-action-boundary/cartesian_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  --package-root tmp/probes/strict_default_profiles owner_prefix.lp
```

The generated `emdash3_2.lp` in the same package is the full-file target and
is expected to fail at the recorded unresolved family owner. Do not register
the prefix as a replacement core target. Replay on action, coefficient,
whiskering, product, evaluation or duality owner changes; promotion still
requires the complete source/consumer and warning gates.

## Whole transpose and fixed-family continuation

`duality_migration.py` starts from the exact checked Cartesian output and
changes the existing whole opposite/family owners together. The retained
main `Op_cat` means dimension-one transpose. Accordingly, `op` now has source
`CoAt2_cat Cat_cat`, and `Op_catd(E)` has base `CoAt2_cat K`. The genuine
whole family body is `op o CoAt2_func(E)`, with the existing stable head and
projection ladder. This is not the retired strict-v1/Reverse12 construction.

```bash
python3 audits/strict-default-action-boundary/duality_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  --package-root tmp/probes/strict_default_duality family_prefix.lp
```

The head prefix passes 13 positive/three negative controls in 0.595s. The
family prefix passes 38 positive/nine negative controls in 3.962s, including
the prior upstream controls. The tests retain nonidentity base/higher cells,
check the E-parameterized formation as a whole composition, and reject the
wrong unchanged base and wrong transfor input profile. These are native
functor/whole-action constructions; no operational comparison proof is an
input. A source-category annotation resolves an inference ambiguity without
changing the theory. The whole formation fold uses the existing left-
associated Cat-composition normal form.

The full `emdash3_2.lp` target fails at the later `Op_funcd` identity rule;
that operation's base and higher transfor profile are not yet migrated.
Do not turn the positive prefixes into a full opposite/Homd qualification,
identify the shifted and original bases, or force all FF strict. The exact
source hashes and three receipt outcomes are retained in
`duality_migration_verification.json`. Replay when these owners or the pinned
Cartesian stage change; retire the builder after qualified promotion.

## Displayed transpose, products and evaluation

`displayed_op_migration.py` continues the pinned duality candidate with the
Cartesian transformation action of fibrewise transpose. The finite
`op_funcd_profile_model.py` control shows why the old same-profile operation
cannot be applied to arbitrary lax FF even when its component functors and
all family transports are strict. This model is an ordinary semantic
counterexample, not a Lambdapi proof or a full omega dual-action construction.

The candidate `Op_funcd` raw view accepts a classified strict transformation;
its boxed result is a native projection of the whole family operator. This
is an upstream component only. The general blended `homd_int(FF)` and
`fdapp1_int_transfd(FF)` contract is not solved by restricting this input.
No arbitrary FF is reclassified and no supplied equality/comparison is added.

```bash
python3 audits/strict-default-action-boundary/displayed_op_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_displayed_op/owner_prefix.lp
```

The prefix passes 50 positives and 11 negatives. `no_projection_join.lp`
must fail at its cap-first object comparison; the selected construction
joins both object and transformation formation orders at the existing
postcomposition and composition-action owners. The latter clause retains
two product endpoints required by the measured subject-reduction check.
Warnings rise from 658 to 694 (36 normalized blocks added, none removed),
so full integration and warning qualification remain required.
`displayed_op_verification.json` records exact receipts and intermediate
failed controls. Its full-file target proceeds to the old product action.

`displayed_product_migration.py` adapts that first existing consumer and its
adjacent section/transport evaluations. Product inputs remain arbitrary
displayed transformations; the two product betas still return the original
FF/GG. The evaluation definitions retain their composition bodies through
the existing Cartesian inclusion, with no new Pi primitive.

```bash
python3 audits/strict-default-action-boundary/displayed_product_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_displayed_product/evaluation_prefix.lp
```

The product prefix passes 59 positives/12 negatives; the evaluation prefix
passes 64/13, including nonidentity base-2-cell action. The full file fails
at `Functor_catd`'s whole action: its Hom(Cat)-derived body now produces
Cartesian mapping Homs while its old fibre and intermediate types remain
ambient. The correct mixed-family profile needs review; neither identifying
these categories nor making all FF strictly natural is an accepted fix.
`displayed_product_verification.json` records this boundary and the preceding
evaluation-inclusion failure. Existing legacy Sigma declarations in the
prefix have not thereby been semantically qualified.

Replay when the strict action, Cat Hom, duality, displayed component, product,
Pi or transport-evaluation owners change. These are non-library checkpoints;
generated sources/raw logs remain ignored, and a passing prefix never
replaces the required full source, consumer and CI validation.

## Mixed-family owner and parameter boundary

`mixed_family_profile_models.py` supplies three finite semantic controls:

- ambient lax mapping fibres do not admit the prescribed strictly natural
  precomposition action of a general base 2-cell;
- contravariance in a family parameter reverses its naturality square; and
- a section of the shifted `Op_catd(E)` does not automatically have the
  variance required by the intended canonical `Hom_catd` action.

The models validate finite strict 2-category composition and whiskering.
They neither prove an Empty inhabitant in the native kernel nor supply a
complete omega replacement. The third control concerns the prescribed Hom
action, not mere existence of a family with the same object fibres.

```bash
python3 audits/strict-default-action-boundary/mixed_family_profile_models.py
python3 audits/strict-default-action-boundary/mixed_family_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_mixed_family/parameter_prefix.lp
```

The candidate corrects the existing Hom(Cat)-derived `Functor_catd` to
Cartesian mapping fibres, preserving its functor objects and Hom-action
owners. Its whole negative-family parameter uses the existing Cartesian
transformation classifier; its positive-family parameter retains arbitrary
displayed transformations. The adjacent product/composition components use
the matching coefficient types. The fixed owner prefix passes 70 positives
and 14 negatives; the parameter/structural prefix passes 79/15. Both retain
subject reduction at the default resource limits. The strict inferred-slot
audit reports zero unreviewed compounds.

Three of the final positives typecheck an explicit recovery candidate:
ambient fixed precomposition is the Hom action of `Pullback_catd_func(F)`
between the constant terminal and constant C families. It preserves
arbitrary transfor inputs and needs no new primitive. These controls are at
a dependency-complete position; moving that body to the actual whiskering
owner and checking its computation remain the next implementation step.

The full file fails next at `Hom_catd`'s unchanged `piapp0` base annotation.
The finite control shows why merely changing that annotation is not a
semantic repair. The higher source action of the old whole raw
`Functor_cat_func` is another affected upstream contract, despite the earlier
successful fixed-whiskering controls. Keep those valid fixed actions and
repair the whole parameter profile before promotion. Neither issue
authorizes blanket strictness for FF or a primitive replacement Pi.

`mixed_family_verification.json` records exact replay hashes, receipts,
counts, warning inventories and the full-file failure. The
[profile review](../../../docs/EMDASH_STRICT_FUNCTOR_EVALUATION_PROFILE_REVIEW.md#mixed-family-continuation-and-necessary-profile-boundaries)
states the models and their implications. Replay after changing mapping,
mixed-family or negative-section owners; this remains a non-library audit.

## Actual precomposition owner and corrected whole diagram constructor

`precomposition_migration.py` relocates existing family-reindexing and
constant-section prerequisites, then defines `comp_cat_con_func` by the
Hom action of `Pullback_catd_func` at constant families. Its canonical object
projection computes to ordinary composition. No new primitive replaces the
old derived operation. The owner prefix passes 34 positives/eight negatives;
the mixed prefix passes 85/16. `no_projection_join.lp` fails at the intended
first object comparison. Exact receipts are in `precomposition_verification.json`.

`mapping_constructor_migration.py` retires the unsupported whole ambient
`Functor_cat_func`, retains its valid fixed-source covariant operation, and
derives `Catd_cat_func` from the existing `hom_int(id_Cat)` and fixed
evaluation. Variable-base diagram formation has Cartesian mapping fibres;
ordinary family objects and ambient fixed-base pullback/Pi maps remain.
The variable-base Pi components use the existing inclusion.

```bash
python3 audits/strict-default-action-boundary/mapping_constructor_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_mapping_constructor/mixed_prefix.lp
```

The constructor prefix passes 75 positives/16 negatives; the later mixed
prefix passes 95/19, including the nonidentity source-2-cell direction and
retained raw displayed maps for fixed-base Pi. The corrected ambient whole
precomposition/pullback comparison is checked with typed reflexivity and a
negative runtime-conversion control. `no_comparison.lp` must fail at that
reflexivity consumer. No operational equality argument is added.

`mapping_constructor_verification.json` retains hashes and receipts. The
mixed warning stream drops from 742 to 732 reports (no added normalized
blocks, ten removed). Full-file integration remains incomplete at the known
Hom_catd negative-section mismatch. The next total-fibre-opposite candidate
is recorded in the living plan; no positive prefix is a substitute for its
implementation or for the required Q/Homd/Sigma qualification.

Replay after changes to mapping classifiers, reindexing, constant-section
comparisons, whole diagram formation or Pi. Generated copies and raw logs
remain ignored; production promotion still requires the complete SOP gates.

## Total fibre opposite and the existing Pi/Hom/Sigma structure

`total_op_migration.py` introduces primitive `CoAbove2_cat` and derives total
`TotalOp_cat = CoAbove2_cat o Op_cat`, retaining the existing dimension-one
`Op_cat` and dimension-two `CoAt2_cat`. The whole functor and family actions
use the corresponding Cartesian mapping profiles. The existing `Hom_catd`
negative input is `Pi_cat(TotalOp_catd(E))` over R(K); no new Pi is introduced.
Its whole constant-Cat specialization computes to `Functor_catd(A,B)`.

```bash
python3 audits/strict-default-action-boundary/total_op_section_model.py
python3 audits/strict-default-action-boundary/total_op_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_total_op/hom_prefix.lp
```

The head/family/Hom prefixes pass 27/6, 57/13 and 123/25 positive/negative
controls. The finite model includes varying transports and two nonidentity
section comparisons; its forward Hom cell uses neither inverse. It remains
a finite semantic control, not the native omega implementation.
`total_op_verification.json` records the separate native checks.

`bare_action_assertion.lp` retains a checker diagnostic: the untyped-result
equality query rejects two opposite-Hom result types that have identical
normal forms. Primitive expansion does not resolve it. The explicitly typed
consumer in the head controls checks and computes using the same theory.
No extra theory unifier or operational proof argument was added.

`sigma_total_op_migration.py` corrects the Hom of Sigma using the same Sigma
constructor and total duality of both base and fibre:

```text
H:T(I)->Cat  gives  O(Sigma(O(I), TotalOp_catd(H))).
```

Its explicit constant-family RHS reduces to `I × Hom_C(u,v)`, preserving
noninvertible fibre arrows. A general total 2-cell has kappa:p=>q and a
forward filler eta:a=>H[kappa][b]. Both the facade projection and the actual
whole-first recursive projection compute to kappa.

```bash
python3 audits/strict-default-action-boundary/sigma_total_op_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_sigma_total_op/hom_prefix.lp
```

The final prefix passes 129 positives/27 negatives; the strict LHS audit is
clear. The normalized warning stream has one removed block and none added
at the same Hom-family boundary. The full source stops later at the old
Edge/presheaf constructor profile. Later Homd-dependent action consumers
remain unmigrated. Exact evidence is in `sigma_total_op_verification.json`;
these remain non-library checkpoints rather than a completed Homd migration.

The separate `relocation_resource_continuation.json` records a resource gap
in the production carrier-move health gate. Its failed aggregate is not
reported green and is not replaced by the successful prototype prefixes.

## Ordinary representation and corrected whole Edge/presheaf interfaces

`representation_migration.py` moves the existing Unit_prof and its ordinary
Hom actions before Cartesian curry and defines `Rep_cart_func` from that
native curry. It retains public ambient `hom_int`. Canonical computation joins
compare the whole representation, whole Hom action, capped arrow and component
with existing represented Hom owners. This does not curry a combined dependent
context or replace the requested Homd ladder.

`edge_presheaf_migration.py` uses that representation in the existing Edge and
presheaf definitions. Their whole sources retain the actual C2 base shifts;
the negative family parameter is Cartesian. The obsolete unshifted signatures
are rejected. A source 2-cell control checks the C2 direction without an
inverse argument.

```bash
python3 audits/strict-default-action-boundary/edge_presheaf_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_edge_presheaf/owner_prefix.lp
```

The representation and Edge prefixes pass 141/27 and 149/29 positive/negative
controls respectively. Their verification JSON files record exact sources,
receipts, failed intermediate comparisons and the warning inventories.
The full file must currently fail at the old `Homd_target_section_catd`:
its ordinary mixed-family body requires C2(K)=K. The selected Q/profunctor
construction, whole Homd and general FF consumers remain unimplemented.

The LHS audits are clear, but generic identity/composition and legacy
Op-adjunction overlaps remain promotion obligations. Replay this audit after
changes to Unit_prof, Cartesian curry, represented Hom, opposite-family action,
presheaf formation or the coupled Homd target. It is a non-library checkpoint,
not a full-source, confluence or production qualification.

## Candidate whole Q/Homd ladder and retained general FF

`q_homd_migration.py` replaces the invalid ordinary Homd target with the
selected Q-valued transformation category and adapts the existing direct
projection ladder. Q has Cartesian curried module Homs; its K-diagrams use
the existing ambient transformation category. The coefficient inclusion and
whole contravariant diagram lift are explicit structural candidates, not
theorems derived from the existing opaque Prof_tensor.

The source-fixed section now has the actual type
`Transf(K,Q,iota(D),iota(Hom_K(x,-)))`. Its ordinary y-component is directly
the v/f functor. The whole-first x/u/y/v/f application reaches
Hom(E[y], E[f][u], FF[y][v]). The represented x-action uses the companion of
precomposition, and a nonidentity base 2-cell has the correct index direction.
Identity/composite represented inputs and both index-action observation
orders are included. No operational proof/equality payload is an input.

The derived Homd_target_map(FF) acts on section targets without transposing
FF. Its whole type, x-component, identity and composition check for the
original raw Functord input. Agreement of its composite with the blended
homd_int(FF) remains an explicit coefficient-composition obligation.

```bash
python3 audits/strict-default-action-boundary/q_homd_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_homd/ladder_prefix.lp
python3 audits/strict-default-action-boundary/ff_source_image_profile.py
```

The prefix passes 176 positives/32 negatives at the normal bounds. Its LHS
audit is clear. The 26 added warning reports and exact source/receipt pins
are recorded in `q_homd_verification.json`. Replay these separate boundaries
serially when changing the relevant owners:

- `no_action_joins.lp` must fail the target-map identity comparison when the
  required ordinary represented-precomposition joins are removed.
- `coefficient_unit.lp` and `coefficient_composition.lp` are positive runtime
  obligations that currently fail after projecting the structural inclusion.
  They expose incomplete coefficient computation; do not count them as
  successful negative controls or infer the whole coefficient is qualified.
- The full `emdash3_2.lp` copy currently fails at the old internal-action
  target's use of same-profile Op_funcd on general FF.

The finite FF model has a walking-arrow base and constant fibres, with strict
transports and strict component functors but nonidentity naturality. The old
source-image root would require a functor from a terminal category to an
empty category. Its opposite, oplax direction exists. This is a finite
profile counterexample, not a model or qualification of the whole omega
construction. It justifies correcting the intrinsic-action profile while
retaining general FF; globally strictifying Functord is not the selected fix.

These are non-library interface/action checkpoints. Coefficient units and
composition, whole lift coherence, intrinsic extraction, later consumers and
production qualification remain required.

## Represented coefficient unit/composition computation

`q_represented_migration.py` continues the checked Q/Homd copy. Native equality
proofs specialize the structural inclusion's strict functor laws before any
new conversion rule. The new runtime joins give the curried unit Hom as the
coefficient identity and compose represented arrows by their original
functors. They do not independently derive Q or a coend tensor model.

```bash
python3 audits/strict-default-action-boundary/q_represented_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_represented/owner_prefix.lp
```

The prefix passes 190 positive/32 negative controls, including arbitrary-module
left/right units, represented composite values, proof-time associativity and
the terminal unit after opposite normalization. The 26 new identity-observation
warning reports are inventoried; higher interaction qualification remains open.
The LHS audit has zero unreviewed compound slots.

Two separate controls must fail: `no_laws.lp` at the projected unit comparison,
and `without_endpoint_guards.lp` at represented composition. The latter retains
an elaboration failure mode: insufficient type information changes the endpoint
categories in the generated RHS despite its initial SR check. The selected
two Cartesian codomain guards fix it; deeper curry endpoint guards were
successfully removed. Exact sources and receipts are in
`q_represented_verification.json`.

The full emitted source still fails at the old general-FF internal-action
profile. Replay after changing coefficient identities/composition, representation
heads or their ordinary postcomposition owners. This remains a prototype
checkpoint, with whole coefficient/lift coherence, intrinsic extraction and
production qualification outstanding.

## Existing closed profunctor core and the lift counit

`q_closed_migration.py` moves the needed existing product-prof classifiers,
opposite, represented reindexing, tensor/map and covariant closed owners before
Homd. Prof_cat retains product-functor objects and uses Cartesian vertical
module transformations for the coefficient role. This does not restrict raw
displayed FF; later prof-map consumers still need migration.

The represented Yoneda specialization of Prof_imply_cov identifies its value
on Unit_B and Companion(F) with Conjoint(F). The canonical counit is then
defined as Prof_eval_cov_map applied to the represented identity. Its
abstraction round trip checks. This uses the existing closed core, with no
separately supplied laxity cell or general adjunction input.

The actual curried bridge uses Op_prof_func and Cartesian curry/uncurry.
Whole unit/conjoint/companion comparisons pass. A whole tensor-view operation,
a proposed composition body on arbitrary curried modules and the curried
counit are also constructed. The latter currently has the curried legacy
tensor as source; it is not yet the required native Q-composite counit.

```bash
python3 audits/strict-default-action-boundary/q_closed_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_closed/owner_prefix.lp
python3 audits/strict-default-action-boundary/q_closed_counit_model.py
```

The prefix passes 209 positives/34 negatives. The LHS audit is clear; the
sixteen added warning reports remain inventoried interaction obligations.
The three separate boundary files are positive obligations that currently
fail: roundtrip_boundary.lp, composition_boundary.lp and counit_boundary.lp.
They must not be counted as successful negative controls. The full copied
source retains the general-FF intrinsic-action mismatch.

The finite model checks the canonical Empty->Terminal counit fibre for
Terminal->[1] selecting 0 and its naturality. The same example is a strict
input square whose represented lift has a noninvertible comparison. It is
a finite direction/noninvertibility control, not an omega model.

q_closed_verification.json pins sources, receipts, the alternate unselected
projection experiment and the exact unfinished boundaries. Replay after
changes to Cartesian module-map profiles, opposite/reindexing, the closed
prof core or the Q composition/presentation interface. No production
promotion or full milestone completion is claimed by this checkpoint.

## Cartesian presentation inverses and native Q composition

`q_presentation_migration.py` extends the pinned q_closed source. It adds
structural Cartesian beta/eta computation on the existing derived bodies,
the whole product-prof swap involution, and the concrete tensor-derived body
of Q composition. No alternate curry/uncurry API or proof-carrying input is
introduced. The primitive Q coherence contract is not derived from the
legacy opaque tensor by these clauses.

Both generic whole bridge composites and generic module round trips check,
including identity, constant, product-target and terminal cases at the
relevant owners. Recoverable Cartesian/opposite arguments stay inferred so
that their earlier normalization does not block matching. Subject reduction
requires the remaining recorded composition/triangle endpoint guards.

The existing counit is still defined from closed evaluation at a represented
identity. Its source now checks as native `iota(F) o kappa(F)` and its target
as `id_Q(B)`. Whole composition and its full/capped transformation projections
use the existing tensor through the actual presentation maps.

```bash
python3 audits/strict-default-action-boundary/q_presentation_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_presentation/owner_prefix.lp
```

The prefix passes 234 positives/36 negatives. The three former q_closed
obligations are among its controls. The current positive obligations in
action_boundary.lp, conjoint_boundary.lp and companion_boundary.lp still
fail: separately expanded transformation action and the represented inverse
specializations do not yet join. Full-source checking still stops at the
raw-FF/strict-Op_funcd intrinsic-action mismatch. These failed obligations
are explicitly distinct from the successful negative/noncollapse controls.

The no_inverse, no_swap_inverse and no_composition variants show that the
new computation is needed; without_endpoint_guards fails subject reduction.
All are bounded and pinned in q_presentation_verification.json. The strict
LHS audit is clear. Warning blocks change from 895 to 898, with three added
Q-composition projection overlaps and none removed. This does not establish
global confluence, a completed Q/lift model or production qualification.
Replay after modifying ordinary curry/evaluation/product normalization,
the product-prof/curried bridge, or native Q composition projections.

## Represented inverse observations

`q_inverse_views_migration.py` continues the pinned q_presentation source.
Two inverse normal-form clauses return ordinary represented pre/postcomposition
through the existing Prof_reindex owner. The actual presentation maps stay
unchanged. Their extra Cartesian inferred arguments were removed after a
successful native minimization check.

The existing generic full-Hom identity/composition rules and neutral endpoint
reindexing rule move to their earlier consumers without changes to their
bodies. A Unit/Unit represented-implication clause joins the identity case
after reindexing normalizes. Direct closed-evaluation formation checks that
case; the corresponding no-rule variant fails.

```bash
python3 audits/strict-default-action-boundary/q_inverse_views_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_inverse_views/owner_prefix.lp
```

The prefix passes 244 positives/37 negatives, including both represented
inverses, identity/composite cases, their distinct fibre orientations and a
direction noncollapse control. The LHS audit is clear. Warning blocks change
from 898 to 903 (seven added, two removed); exact differences, moved-owner
hashes and six checked receipts are pinned in q_inverse_views_verification.json.

The expanded transformation inverse remains a failed positive obligation.
Full-source checking still stops at the general-FF opposite-profile mismatch.
These results do not qualify the complete coefficient/lift or production
migration. Replay after changes to represented Hom, the two presentation maps,
ordinary Hom-action computation or identity reindexing/closed evaluation.

## Canonical unit and whole lift steps

`q_unit_migration.py` derives the represented unit using the existing
Prof_tensor_hom_hom applied to the existing Prof_func_hom twice. Its curried
view has native type id_Q(A) => kappa(F) o iota(F). No supplied unit,
comparison, equality argument or operational presentation cast is used.
The moved shaped-cell classifiers now use Hom(Prof_cat), consistently with
its selected Cartesian vertical-map profile. Raw displayed FF is retained.

The whole unit/counit mate steps in q_lift_mate.lpfragment check, including
their component observations. The final composition remains a failed positive
obligation because the middle whole functors do not yet compare. This is
explicitly different from declaring the desired whole comparison as input.

The same consumer qualifies fixed ambient pre/post-whiskering projections
at their actual current bodies, including full off-diagonal action and
negative strict-naturality controls for raw transfors. Constant-section Hom
needs explicit category and Obj views, checked by typed reflexivity. Q's
whole identity-whiskering rules recover their object from Unit_prof(T);
the rejected inferred-endpoint variant is retained as a failing control.

```bash
python3 audits/strict-default-action-boundary/q_unit_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_q_unit/owner_prefix.lp
python3 audits/strict-default-action-boundary/q_unit_model.py
```

The prefix passes 263 positives/42 negatives. The mate_unit_projection and
mate_counit_projection targets each add a passing whole-step component check.
The LHS audit is clear. Warning blocks change from 903 to 916 (thirteen
added, none removed); exact blocks, sources and thirteen receipts are in
q_unit_verification.json. The no_strict_squares, no_hom_units,
inferred_identity_object, no_ambient_views, no_ambient_obj_view and
no_ambient_whiskering files are necessity/rejection controls.

The mate_boundary and action_boundary files remain failed positive obligations,
and the full source retains the general-FF/Op_funcd mismatch. The finite
unit control shows a noninvertible Empty->Terminal fibre for [1]->Terminal;
it does not qualify native tensor evaluation or full omega coherence.
Replay after changing shaped-prof profiles, tensor introduction, unit/counit
operations, identity whiskering, constant-section Hom or ambient whiskering.
No production promotion or completed Homd milestone is claimed.

### Presentation boundary after the canonical-unit checkpoint

This Q implementation is hybrid: curried coefficient Homs reuse the legacy
product Prof theory through explicit swap/curry/uncurry functors. The user
clarified that their earlier comment asked for review rather than a blanket
migration. The active plan now retains both presentations over
shared product-based operations; the curried Homd type needs no separate
profunctor calculus. The expanded conversion inverse remains a prerequisite
where the selected implementation actually uses that conversion. Whole lift
coherence and general-FF action still need qualification. The public FF is a non-strict displayed transformation
with strict functor components; it is distinct from the strict U input of
the represented-lift experiment.

## Alternative direct-curried Prof experiment

`curried_prof_migration.py` explores replacing the earlier Prof carrier,
reindexing and represented block by the covariant curried convention. Prof_cat is the
transparent Cart(A,Cart(T(B),Cat)) alias. Reindexing and its vertical action
are actual compositions of the existing Cartesian whiskering operations.
The ordinary product Hom remains upstream as Hom_prod_func; it is not a
legacy Prof carrier or a conversion in reindexing.

```bash
python3 audits/strict-default-action-boundary/curried_prof_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_curried_prof/map_boundary.lp
```

The real map-component consumer now passes: 181 positives/36 negatives,
including direct nested values, whole inner Hom action, identities, variance
controls and the actual two-level reindexed map component. The strict LHS
audit is clear; six removal/minimization controls reproduce the necessary
projection, comparison and transpose-guard boundaries. Exact evidence and
the downstream consumer inventory are in curried_prof_verification.json.

whole_composition.lp remains a failed positive whole-reindexing obligation;
its fibre comparison passes. This is an alternative-specific obligation,
not a newly required outcome of the selected two-presentation goal. The
complete copied source fails at the old product-specific Op_prof action. legacy_interaction.lp retains a failing old
companion projection after the new generic application rule. Neither failure
is counted as a passing negative. The blanket curried replacement is not
selected. Continue from the q_unit reference with shared product Prof operations and the convenient curried
Q-Hom view. Whole Q/lift coherence, general FF and production integration
remain unfinished. Do not infer any completion percentage from the prefix
assertion count.

The final consumer review also keeps presentation distinct from transformation
profile. The q_unit Cartesian coefficient-map experiment does not establish
that all generic ProfMap or Prof_hom inputs should become strict. Existing
reindexing, shaped PathOut, join and DefIso consumers use their ambient views.
Qualify the coefficient restriction and inclusion at shared owners before
production promotion; do not duplicate a curried Prof theory.

## Cartesian action and expanded presentation inverses

`cart_action_migration.py` extends the selected q_unit copy at the actual
projection owners. Both Cartesian transformation round trips and the actual
product-prof/Q bridge round trips check, with raw-transfor rejection and
non-collapse controls. The existing semantic curry/uncurry definitions remain.
The new inverse clauses complete their whole-beta/eta versus expanded-action
critical pairs; do not describe them as arbitrary transformation extensionality.
The product action and inclusion projections have independent consumers.

```bash
python3 audits/strict-default-action-boundary/cart_action_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/strict_default_cart_action/q_bridge_actions.lp
```

The verification file records exact final inputs, warnings, measurements,
removal/minimization failures and the remaining mate/full-source boundaries.
Replay after Cartesian action, product/inclusion, identity normalization,
presentation-map or represented-lift changes. This is non-library evidence;
production qualification and the public raw/Cartesian Prof boundary remain open.

## Raw represented counit without an implication identification

`raw_represented_counit_migration.py` emits the explicit bounded owner closure
specified by raw_represented_counit_source_closure.md. The actual counit body
uses lambda of co-Yoneda, reindexing, then evaluation. Original raw public map
and shaped-cell profiles remain; no implication-to-Conjoint fold is used.
The constructor, identity and closed-beta controls check. The original
component_boundary remains a failed positive obligation. comparison_variant
passes by retaining the reindex head and using a whole proof-time comparison
whose side conditions handle normalized target inputs. Both its general-law
and represented-component consumers pass; it remains a separate policy
candidate. The earlier nested-pattern and fibre-only alternatives fail their
respective consumers and are not selected. Cartesian
admission, generator computation, balancing and triangle coherence are open.
See raw_represented_counit_verification.json for exact source/receipt evidence.

## Local Cartesian view with raw public Prof maps

The [local replay](local_cart_prof_migration.py) uses the existing product
Prof convention and defines a local Cartesian mapping-category view, its
actual ambient inclusion, and swap/curry presentation maps. The
[source closure](local_cart_prof_source_closure.md) records measured facade
and evaluation gaps, retained failed alternatives, and the selected
`composition_profile_consumer.lp` and separate projection controls. The
[verification](local_cart_prof_verification.json) pins all 15 receipts and
the four single-removal failures. Public raw maps are not strictly retyped.
Expanded arrow inverses, whole reindexing, and canonical counit admission
remain open; object inverses alone do not qualify those operations.

## Whole represented-lift middle

The [lift replay](lift_middle_migration.py) and its
[source closure](lift_middle_source_closure.md) record the selected whole mate
construction, both middle comparisons and its actual first component. Step
bodies are unchanged; their types share the same defined whole middle. The
[verification](lift_middle_verification.json) retains native normal forms,
negative controls, earlier failures, removal results and warning differences.
The guarded contextual naturality pair is needed by this whole consumer even
though it was redundant for the earlier smaller corpus. No supplied
comparison or operational equality-proof parameter is added. Full lift
action/coherence and raw-preserving coefficient integration remain open.

## Identity Homd core and derived relative interface

The [identity replay](homd_identity_migration.py) owns primitive Homd
computation only at homd_id_int and its direct projection ladder. The early
homd_id_ leaf is defined through ordinary Hom and native fibre transport;
general homd_ substitutes FF[y] into it. Public homd_int and upper relative
projection names are definitions through the existing whole target action.
The [verification](homd_identity_verification.json) records the passing
selected prefix and identity-projection removal failure. It also preserves
the failed full-source intrinsic-action boundary without pretending raw FF
has a strict opposite. Relative leaf normalization is a separate optional
diagnostic, not part of the identity ladder acceptance. Q/lift qualification
and production migration remain open.

```bash
python3 audits/strict-default-action-boundary/homd_identity_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/homd_identity/selected_prefix.lp
```

## Represented arrow action and coordinated identity source

The [lift-action replay](lift_action_migration.py) supplies whole/capped
projections to the constructed right-hand action and qualifies the actual
nonidentity represented x-action. Narrow coefficient unit joins make both
identity endpoints compute; their separate removal controls fail. The
[source closure](lift_action_source_closure.md) and
[verification](lift_action_verification.json) distinguish this progress from
the still-failed mate triangle and companion-composition obligations. The
native extraction-to-mate connection is not yet implemented.

The [coordinated replay](foundation_assembly_migration.py) combines these
additions with identity Homd through seven insertion-only owner blocks.
Its [closure](foundation_assembly_source_closure.md) and
[verification](foundation_assembly_verification.json) record the passing
combined identity/represented-action consumer, warning comparison and the
unchanged full-source `Op_funcd(raw FF)` failure. It retains the provisional
Q coefficient profile; raw-preserving admission and production integration
remain open. Relative leaf computation remains separate from identity
acceptance.

## Raw-preserving whole reindex comparison

The [admission prerequisite replay](admission_next_migration.py) keeps public
Prof maps raw and qualifies their comparison with inclusion of the local
Cartesian reindex action. The selected staged theorem composes two independently
typed comparisons through the actual ambient prewhiskering map. It adds no
proof argument to either operation and claims no new runtime conversion.
The direct-reflexivity variant remains failed. Three removals fail at their
respective endpoint, raw-map and inclusion comparison obligations.

The [source closure](admission_next_source_closure.md) and
[verification](admission_next_verification.json) preserve the exact scope and
original failed attempts. Canonical co-Yoneda/lambda/evaluation admission,
expanded local arrow inverses and triangle coherence are still unqualified.

## Canonical coefficient and local inverse continuation

The [canonical admission proposal](canonical_admission_source_closure.md)
classifies only co-Yoneda(Unit), with an actual raw inclusion comparison.
Its constructor, native action and reindex consumers check. This remains an
explicit structural-profile proposal; lambda and general counit admission
are not derived from it.

The [generator replay](lift_coyoneda_source_closure.md) implements the
reindexed lambda/evaluation cut on tensor introductions. The actual raw
represented counit then reaches existing co-Yoneda beta; the identity-middle
interaction and both required removals are recorded. No mate triangle is
installed.

The [local inverse replay](local_inverse_source_closure.md) checks expanded
variable-map round trips, identity/composition and selected swap interactions.
A nested reindexed identity still fails conversion and direct proof-time
comparison. Recorded warning overlaps remain qualification boundaries.

The [combined coefficient recipe](coefficient_assembly_migration.py) checks
these consumers together after importing the previously omitted, unchanged
nested reindex owner. Its [verification](coefficient_assembly_verification.json)
records the passing raw-preserving assembly and the initial dependency failure.
The selected seed remains a proposed profile contract; complete Q/lift/Homd
coherence and production integration remain open.

## Nested inverse and fixed-parameter canonical chain

The [nested inverse replay](inverse_nested_source_closure.md) closes the
actual typed comparison through two generic owner comparisons. No runtime
rule changes; the separate runtime boundary remains failed. Both removal
controls fail and the same-endpoint perturbation remains visible.

The [lambda restriction](canonical_lambda_source_closure.md) and
[evaluation restriction](canonical_eval_source_closure.md) provide explicit
structural whole-map contracts for the selected instances. The classified
j_B, j_F, counit and its actual curried image have definitions. Their passing
consumers do not derive those profiles from the old raw beta/eta rules or
qualify variation in F/A/B, classified triangles or whole Q coherence.

The [raw companion-composition replay](represented_comp_source_closure.md)
constructs the forward map from existing raw operations and tests its whole
fibre component. A stable tensor-reindex comparison is separately qualified
as a bounded policy candidate. Its [verification](represented_comp_verification.json)
also records the integrated coefficient consumers; the inverse, Cartesian
admission of that forward map and production normalization migration remain
open.

## Native identity Homd consumers

The [initial x-action audit](homd_x_consumer_source_closure.md) tests the
actual Homd root and transported section. The
[native-action successor](homd_native_action_source_closure.md) closes its
source/left-action and raw postcomposition comparisons through two generic
proof-time owner clauses. The selected target and exact removals are pinned
in its [verification](homd_native_action_verification.json); warnings are
unchanged. No root strict-naturality equation is introduced.

Whole structural primitives with appropriate projections remain an allowed
implementation method. Deriving the represented lift from the legacy closed
profunctor calculus is optional comparison work. Its actual profiles, laws
and Homd consumers still require qualification. These checks do not yet
integrate the raw-preserving coefficient reference, implement native root
laxity extraction, or complete production migration.

The [native u-action assembly](homd_u_normalization_source_closure.md)
now checks together with those x consumers. Its
[normalization diagnosis](homd_u_inversion_review.md) isolates premature
Hom-category injectivity in the checker. The selected source delays that
inference, retains explicit fibre indices, and restores ordinary
precomposition accumulation for default-strict functors. The u/y/v/f
projections, whole h-family construction, source laws and two-factor leaf
have concrete consumers. Exact removals, warning changes and the remaining
coefficient/native-laxity boundary are recorded in the
[verification](homd_u_normalization_verification.json).

The [intermediate joins](homd_u_intermediate_join_source_closure.md) check
the y/v identity and composition routes independently. Four native joins
have individual removal controls, and their minimal Cartesian guards retain
the actual source data. The [peak observations](homd_u_peaks_source_closure.md)
use existing proof-time comparisons without new runtime rules.

The [canonical strict FibCov core](fibcov_cart_source_closure.md) retains
whole u-action and derives its actual ambient inclusion. The
[derived section](fibcov_cart_section_source_closure.md) feeds that canonical
map to the existing represented lift and exposes y/v/f plus native y-action.
The [combined replay](homd_native_section_assembly_source_closure.md) checks
these pieces together. Adoption in the existing Homd ladder, whole x/u
compatibility, native laxity and production integration remain open.

The [section adoption](homd_section_adoption_source_closure.md) now gives the
public source-section and target-component names their checked defining
bodies, while retaining the native root/u owners and the raw relative FF
interface. The [intrinsic profile review](homd_intrinsic_profile_review.md)
records why the next whole target needs a profile review: a finite
normal-lax example rejects its old ordinary-lax x-action, and two skew
legs alone do not supply a forward comparison. These examples do not refute
the bare raw carrier or qualify a narrowing of the public FF domain.

The [root-action scope replay](homd_root_action_scope_source_closure.md)
preserves the adopted ladder while removing the generic Cat action
comparison. Only the canonical identity root keeps its selected comparison.
All inherited controls pass, and restoration of the generic comparison
fails a new raw-FF negative. This is non-library owner evidence; full-source
intrinsic action and production integration remain open.
