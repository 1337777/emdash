# Whole represented-comma target comparison and original reviewer

Date: 2026-10-17
Predecessor: `d71a28be`
Status: whole source/target construction and original reviewer qualified in the migration source; downstream library migration and public promotion incomplete
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Result and retained contract

The original represented-comma module now typechecks completely. For an
ordinary lax eta:J∘A⇒D it constructs the same whole Gamma:K→RepresentedComma(J):

```text
Gamma[x] = (A[x], D[x], eta[x])
Gamma[p] = (A[p], D[p], lambda_eta(p))

p∘Gamma ≅ A
q∘Gamma ≅ D       when Y satisfies the original OneCat premise
```

K and X remain arbitrary category inputs. Both selected source inverse maps,
the target's fixed-forward inverse data, and the original whole laws remain.
The ordinary eta wrappers keep their types and use tapp1_int_cart internally;
eta itself is not made strict. Generic Theta inputs use the established strict
x-profile while their displayed y-components remain lax.

The complete original reviewer retains 24 positive and seven negative
assertions. It checks object/arrow data, the selected inverse components and
laws, source action through higher cells, and the generic admitted Theta
interface. The original whole constant-base-change runtime-negative remains
negative. A separate rejection checks that a nonidentity displayed map is
not erased as an identity reframe.

## Coupled migration

Total and section constructions use O(K); internal-Hom inputs still use T(K).
The existing Cartesian Sigma projection is used through its ordinary displayed
view where required. The four former whole projection comparisons now have
corrected counterparts at their existing owner: reindexing, canonical base
change, Sigma parameter maps, and the identity graph. The invalid old
same-base Op clauses remain inactive. Their three old point-action clauses
remain audit candidates for subsequent real consumers.

The old Sigma-composition comparison needed its inferred composite endpoint
tags relaxed. Its actual base, three families and both displayed maps remain.
A direct whole reindexing/associativity comparison retains all original bases
and functors. A narrow projected-Sigma comparison handles the identity
reframe in the original target proof. None asserts Cart=ordinary mapping
categories or discards a general comparison/map.

The higher triangle observation now passes the existing ordinary inclusion
of the represented Cartesian family to the local homdc_fibre interface. Its
triangle data and the original observation are retained.

## Constant-target Sigma projection

Tracing the first target-component failure exposed a product-projection
order problem: snd(F[q]) selected the function component before the Sigma
object beta could run. Point-only joins fixed the forward observation but
left the selected inverse observations stuck at composed maps.

The selected canonical projection owner is

```text
sigma_const_target_func(FF:E⇒const(C)) : Sigma(E) → C
sigma_const_target_func(FF) ≐ pi₂ ∘ Sigma(FF)
sigma_const_target_func(FF)[q] = FF[pi₁(q)](pi₂(q)).
```

It is a declared structural projection with its whole composition view and
projections, not a separately supplied map or caller comparison. No equality
proof is an operational argument. The whole Hom and capped arrow readings
are proof-time comparisons with the existing Sigma action. Their generic
fapp1 heads stay stable so ordinary identity/composition/accumulation cuts
continue to match. Eager first-Hom expansion failed the whole/capped join;
eager capped expansion failed the image-composition observation. Both trials
were retired rather than installing compensating global equations.

Constructor-visible projections of composed Sigma maps preserve their actual
component maps. The base-change action uses exactly the conventional pre/right
route: base change at the target family after the pulled-back Sigma map.
No strict equality with the retained post/left comparison is assumed.
The whole constant-base-change projection retains its runtime head.

Focused controls check arbitrary total objects, constant families, both
projection orders, whole/capped action, identity and composition, and the
whole/Hom/capped Sigma readings. Negatives retain the map's value, the second
composed displayed map and the actual reindexing functor. The source-category
guard on the remaining point rule was tested with `_` and removed.

## Explicit structural boundary

The existing OneCat(Y) premise must also describe O(Y) in the migrated proof.
discrete_total_op is declared closure of the existing discrete-category
classifier under total duality. one_cat_total_op is defined homwise from it.
This is not claimed to derive new inverse computation for Core_incl_func
from the presently qualified dual-functor beta rules. It adds no new caller
premise or chosen Gamma inverse. The same existing ordinary-target boundary
is retained in the public comparison.

## Validation, resources and next owner

The [verification](production_comma_target_verification.json) records exact
source/log hashes and the failed-before diagnostics. The combined core and
projection check passes with 268 positive and 66 negative assertions. The
combined reviewer/guard check includes all 24 original positives, seven
original negatives and the new reframe negative. Subject reduction stays
enabled. LHS audits have zero unreviewed candidates; owner-specific nested
product guards and retained residual comparisons were also reviewed.

Final warning bodies are exactly unchanged: 1953 in the core and 2608 in
the comma import. This is a warning comparison, not a confluence certificate.
An overly broad kernel-level reframe comparison exhausted 3GiB with o=20
and timed out at 90s with o=5. It was removed. The selected narrower view
lives at its comma consumer. Keeping the generic capped head stable also
removes the trial's additional identity/profile overlap family.

Normal defaults remain 90s/2GiB. The core regression passes in about 21s at
2GiB/o=20. The combined reviewer needed an explicit 4GiB profile after a
3GiB allocation failure; it passes in about 42s. Host headroom was checked,
and serial execution, file limits, no swap and all guards remain enabled.
The broader Hom-comparison import also failed allocation at 3GiB; at 4GiB it
reaches a real type mismatch after about 45s. These per-target measurements
are not a global memory-limit increase or a claim about arbitrary imports.

The next owner is prof_defiso_at_to_path in
emdash3_2_prof_defiso_evaluation_paths.lp: its old Cat_cat evaluation tags
disagree with the actual Cat_cart profunctor coefficient. Migrate both
selected inverse evaluations with the same original comparison data. The
external one_cat_transf_from_hom_action admission remains a further required
consumer; do not silently narrow its arbitrary source base or add a premise.
The independent presheaf/direct-cover route, other library migration,
strict-wrapper retirement, public promotion and final catalog/health/CI/
source-pin qualification remain open. The persistent goal stays active.

Replay after relevant changes: regenerate production_owner_migration.py;
check sigma_projection_regression_controls.lp at 2GiB and
comma_target_guard_controls.lp at the measured 4GiB profile. The latter
imports the complete original reviewer. Run the recorded broader import
when advancing its actual next owner; no unchanged aggregates are required.
