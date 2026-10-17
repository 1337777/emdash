# Represented-comma source comparison under total duality

Date: 2026-10-17
Predecessor: `3f26489e`
Status: original whole source comparison and its focused reviewer qualified; target comparison and complete migration open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Scope and result

The derived represented-comma constructor now retains the original whole
comparison p∘Gamma ≅ A, with its forward map, reverse map and both laws.
The four original ordinary-lax constructor/source wrappers are moved to
their dependency-ready position. They retain their public types and accept
ordinary lax eta:J∘A⇒D through the canonical tapp1_int_cart admission.
No extra premise, caller comparison or new operational equality payload is
introduced.

The comparison helpers use O for the total/section duality while preserving
T(K) in all nine internal-Hom inputs. Those inputs use the established
strict-x profile, whose components remain ordinary lax displayed maps.
This is not a restriction making eta strict. The original pullback
presentation of represented_comma_family_catd remains selected.

## Necessary computation changes

The three existing proof-time Sigma projection comparisons receive total-dual
instances at their original owner: projection after section, projection after
displayed map, and projection after base change. Their LHSs use the stable
R(T(-)) functor heads rather than a reducible TotalOp alias. Runtime heads and
the actual family, section, displayed map and base-changing functor remain.

One sufficient congruence comparison handles a composite with the total-dual
Sigma projection in two proof-time-equal family presentations. It explicitly
requires equality of the actual bases, whole families and other maps. It
does not assert injectivity of composition or discard those obligations.
The existing whole source proof consumes the positive comparison; negative
controls reject different other maps and replacement of the actual base
functor F by another G.

The constructor checkpoint removed operational identity reframings. Its old
first source-comparison proof reinserted sigma_map(id_reframe), causing an
actual endpoint failure. That step now retains its same endpoints and
selected identity maps directly. The later original mapped comparisons and
their inverse-law construction are unchanged except for the corrected
duality and admitted input. All seven original source observations pass,
including the source/target arrow projections, both inverse components and
both whole inverse laws. The four original rejection cases also pass, with
only the duality in the arbitrary-section case adjusted to O.

## Rejected presentation and validation

Changing represented_comma_family_catd to the comma category's Hom-family
normal form regressed construction of the family section (Y versus X during
unification). That trial was reverted. It is an implementation diagnostic,
not a semantic refutation of the equivalent family presentation. The selected
solution keeps the original construction and compares its actual projection
at the consumed whole expression.

The [verification](production_comma_source_verification.json) records exact
source/log hashes, the source reviewer, affected core and constructor
regressions, warning comparison and the next full-source boundary. The new
source reviewer has seven positive and six negative assertions. Subject
reduction remains enabled; the LHS audit reports no unreviewed candidates.
The existing 90s/2GiB core and 90s/3GiB comma-import profiles are retained with
o=20 and host-headroom inspection. No public source is promoted here.

Replay after relevant changes: regenerate production_owner_migration.py,
then check represented_comma_source_prefix.lp through the bounded runner.
Core changes also require the affected core/constructor checks recorded in
the verification. The original target comparison, its selected inverse data,
full reviewer and external Hom-comparison caller remain required, along with
the other library routes and final migration/promotion gates.
