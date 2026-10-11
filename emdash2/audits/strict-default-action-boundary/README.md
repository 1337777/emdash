# Strict-default action owner audit

Status: non-library implementation pilot; no production rule is promoted.
Plan: [SF-0 / SF-1](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
Source: main `f8af1fca472657ff1598c639eb29c0566e7b2ec0`; the replay pins the
core and profile source hashes and inserts at unique original owner anchors.

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
