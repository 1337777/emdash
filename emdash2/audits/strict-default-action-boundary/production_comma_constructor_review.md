# Represented-comma construction through corrected base change

Date: 2026-10-17
Predecessor: `e3a2e121`
Status: derived constructor and object/arrow computations qualified; original comparison helpers and full reviewer incomplete
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Construction and computation

The original section → base change → totalization → duality construction
now has a checked dependency-ready implementation. Its internal Hom input
has the admitted strict x-profile; its y-components remain ordinary lax maps.
The existing canonical admission accepts any ordinary lax eta:J∘A⇒D.
For the resulting functor Gamma:K→RepresentedComma(J), the native checks give

```text
Gamma[x] = (A[x], D[x], eta[x])
Gamma[p] = (A[p], D[p], lambda_eta(p))

lambda_eta(p) : D[p] ∘ eta[x] → eta[y] ∘ J[A[p]].
```

The last component is the existing extracted
tapp1_post_laxity_cell(eta,x,x,y,p,id_x). The implementation does not invoke
the independent gray_transf_graph_func declaration. The preceding F/G graph
into LaxArrow(C) also passes its object and complete square observations.
The generalized constructor retains A[x], not only J[A[x]], as required by
the original represented-comma interface.

## Base-change coefficient

Sigma_pullback_coeff_source is the existing Cartesian reindexing followed by
Sigma_coeff_func. sigma_pullback_coeff_transf is a declared canonical
Cartesian parameter refinement of the existing base-change transformation.
Its component is the original sigma_pullback_total_func(G,E), and forgetting
through the actual coefficient inclusion computes to the original whole
transformation restricted along Functor_cart_include. G and E are retained;
no inverse, comparison cell or naturality proof is new caller data.

Three direct whole comparisons express existing inclusion/reindexing laws
at the consumed composition shapes. They retain all bases and functors and
do not identify Cart with ordinary mapping categories. The combined source
comparison was required by subject reduction because the checker did not
chain the separate inclusion comparisons. The represented-source comparison
qualifies the existing identity reframe without changing runtime composition.

Both total-dual identity reframings still typecheck. The operational base-change
map now uses the same raw map directly at its checked reframed type. Likewise,
the generalized constructor uses its underlying total map directly at the
represented-comma target type. The former compositions with explicit identity
reframings were computationally obstructive and supply no distinct map data.
Their named observations remain present. A trial relaxing global identity
projection patterns restored objects but was insufficient for arrows; it was
reverted. No global identity rule changed in the selected implementation.

## Validation and limits

The [verification](production_comma_constructor_verification.json) records
current source/log hashes and the failed-before diagnostics. Base-change
component, object, whole-view and explicit constant-family checks pass, with
negative controls for a different target object and a nonidentity other
whiskering leg. The two original reframings, the basic whole graph and the
generalized represented-comma constructor typecheck. Both graph consumers
compute their original object and nonidentity-arrow data. The affected core
and previous middle-section regressions also pass with subject reduction.

Focused checks use 90s/2GiB/o=20; the existing comma import profile uses
90s/3GiB/o=20 after host-headroom inspection. Defaults, serial execution,
file limits and no-swap restrictions are unchanged. LHS review reports zero
unreviewed candidates. Three additional core overlap reports involve the
new explicit-forgetting projection and inherited identity-tag normalization
for Path_cat, Terminal_cat and Homd_coeff_cat. These reports are recorded;
the identity and nonidentity-other-leg consumers pass. Global confluence is
not asserted.

Replay after relevant reindexing, base-change, coefficient or totalization
changes: regenerate with production_owner_migration.py, then run affected
sigma_basechange_coefficient_controls.lp, comma_graph_total_prefix.lp or
represented_comma_constructor_prefix.lp through the bounded runner. Core
changes additionally require the recorded core regression. The full source
still has its expected next failure and is not promoted.

## Remaining migration

The full file now stops at represented_comma_hom_action_source_func: that
original comparison helper still declares an unrestricted ordinary Theta
where the constructor now requires the valid x-profile. Migrate the remaining
generic-Theta helpers and the original ordinary eta wrappers together;
ordinary eta must still enter via tapp1_int_cart without an extra premise.
Preserve T(K) in the internal Hom input while reviewing the total-dual bases
of the projection/section helpers individually; do not rename every Op token.

Retain the original source/target inverse data and OneCat target boundary.
The external ordinary-target Hom-comparison caller, full original reviewer,
other library routes, strict-wrapper retirement, public promotion and final
catalog/health/CI/source-pin gates remain required. This checkpoint qualifies
the constructor computations, not those unfinished whole comparisons or the
complete migration.
