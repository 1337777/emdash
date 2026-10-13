# Canonical strict-target FibCov prototype

Status: `core_controls.lp` and `inclusion_controls.lp` pass the canonical
structural strict-Y core and actual ambient target inclusion controls. The
whole x-map remains ambient. The optional legacy whole equality diagnostic
is unrun and is not a prerequisite for migrating old public names to actual
ambient definitions. This audit uses the checked
`homd_u_normalization/combined_controls.lp` donor, SHA-256
`39ffe519744260512fdcde40cdda0a9cff5f71fa6cbc98057b8c57df48225819`.
The donor's existing FibCov and Homd declarations are unchanged.

For `S = Functor_cart_cat K Cat_cat`, `R = Rep_cart_func K`, the new
target is the actual definition `hom_con S E (Op_cat K) R`. Its fibre at x
has object classifier `StrictTransfor K Cat_cat I_x E`, where
`I_x = hom_ K K id x`.

The whole canonical `fibcov_cart_int` is a structural contract
`E ⇒ fibcov_cart_target(E)`, ambient in x. Its component
`fibcov_cart_src_func(E,x)` is a genuine functor from E[x] into the whole
strict mapping Hom, retaining u and higher u-action. Its object projection
is `fibcov_cart_transf(E,x,u)`; the ambient view of that strict value has
the existing `fib_cov_tapp0_func(E,x,y,u)` as its y-component.
These are three native projection rules. The strict value contract is
justified by the chosen default-strict E interface; it is not presented as
derived from merely matching object values.

The core pass is receipt
`20261013T183602Z-c953eec9b684441d9cf4114808cbb474`, at source SHA-256
`00f2281e3576b538d54179a0e7efff2510bc12d50a4efccf295c97eb43427c98`.
It completed in 13.597 seconds under the default 90-second/2-GiB profile.
The log contains 970 critical-pair warnings, whose blocks exactly match the
normalization donor. This pass does not establish
legacy-root equality or agreement with Homd sections.

The inclusion pass is receipt
`20261013T183711Z-956a447a115f46d79de5b524be7b69e4`; it completed in
13.189 seconds. Its 970 critical-pair blocks also exactly match the donor;
137 replaceable-pattern diagnostics are unchanged in count. The inclusion
target's strict LHS audit reports zero unreviewed clauses. Exact
source/log/output pins are recorded in the verification JSON.

The whole ambient target inclusion is defined from
`fapp1_con_at_transf(cart_functor_include,E)`, then reindexed by
`Op_func(Rep_cart_func)` using the existing whole Hom action of
`Pullback_catd_func`. Its x-component is intended to compute to the actual
`fapp1_func(cart_functor_include,I_x,E)`. No pointwise assembly or new
inclusion primitive is used.

Fresh ambient views are definitions over that inclusion and the whole
canonical core. The controls compare their actual y-components with the
old `fib_cov_transf` components. Equality with the old whole
`fib_cov_int` is a separate optional diagnostic; no rule asserts it from
component agreement. The old public names remain available in their
original ambient profile and may later be migrated to actual ambient
definitions without proving equality between independent primitive roots.

The recipe emits four targets:

- `core_controls.lp`: strict target, whole core, x/u/y projections,
  whole u-action formation, no x-strictness, and raw-FF rejection.
- `inclusion_owner.lp`: whole core plus defined inclusion and ambient views.
- `inclusion_controls.lp`: core controls plus whole inclusion,
  x-component, u-value and old/new y-component agreement.
- `legacy_whole_boundary.lp`: explicit whole compatibility obligation
  against the unchanged legacy constructor.

There is no generic FF admission, proof payload, coend construction, or
extension of Homd sections. The provisional Q/global Cartesian Prof donor
profile remains explicit. Passing formation alone would not supply further
u-action computation, whole x-coherence, or production qualification.

Run `fibcov_cart_migration.py --check-authoring --check-evidence` to verify
the recipe and any future evidence pins. The recipe never invokes Lambdapi;
root owns serial checking and result classification.
