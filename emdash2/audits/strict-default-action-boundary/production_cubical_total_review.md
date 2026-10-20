# Canonical Sigma projection and corrected two-sided total

Date: 2026-10-16
Predecessor: `f0071b11`
Status: staged constructors and original fixed-square/total consumers check; later graph/import migration and public promotion remain incomplete
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_cubical_total_verification.json)

Follow-up, 2026-10-20: the seven inactive opposite clauses discussed below
now have explicit corrected dispositions in the [point-projection
review](production_cubical_projection_point_review.md). Its runtime versus
proof-time boundary supersedes this report's pending point-clause status.
The evidence and other historical boundaries below retain their original
snapshot scope.

## Precise whole coefficients

Write T=Op_cat, R=CoAbove2_cat and O=TotalOp_cat=R(T(-)). The previous
fixed-endpoint homdc_ definition composed the Cartesian hom_con_int with
its ordinary inclusion. Its new totalization consumer needs the stronger
result already provided by that construction. Expose it directly:

```text
E : T(K1) -> Catd_cat(K2)
homdc_(E,x1,u,y1,v)
  : Hom_K1(x1,y1) -> Cart(T(Hom_K2(x2,y2)),Cat_cart).
```

The external E remains unchanged for this fixed-endpoint construction.
Its ordinary fibre and square formula, both higher side actions, and the
negative comparison against the differently bounded twisted square remain
checked. The type of the result is refined; it is not a second Hom theory.

The existing sigma_proj1_family_funcd now has the coefficient and canonical
strict profile its new consumers require:

```text
G : K -> Cart(A,Cat_cart)
sigma_proj1_family_funcd(G)
  : Hom_Cart(K,Cat_cart)(Sigma_coeff_func(A) o G, const(A)).
```

Its component is the original Sigma_proj1_func. This is the original
structural projection owner with a precise profile, not a theorem deriving
that profile from object agreement. Ordinary displayed consumers use the
existing strict_transfor inclusion. No strictness proof or comparison cell
is an input. Its [component rule](production_cubical_sigma_projection.lpfragment)
is the adapted original rule. The old special fdapp1 projection cut is
unnecessary: generic Cartesian intrinsic action and Sigma_proj1_func action
already return an arbitrary inner base arrow q. A distinct q is rejected.

Consequently the fixed-boundary square total uses Sigma_coeff_func on the
actual Cartesian homdc_ result, retaining its broader original E input.

## Two-sided total and native Homd

The whole two-sided total uses a more specific nested-family admission:

```text
E : T(K1) -> Cart(K2,Cat_cart)
A_E = Sigma_coeff_func(K2) o E : T(K1) -> Cat_cart
D_E = TotalOp_catd(A_E) : O(K1) -> Cat_cart

homdc_int(E)       = homd_int(id_D_E)
homdc_total_cat(E) = O(Sigma_(O(K1)) D_E).
```

This nested input is stronger than the old T(K1)->Catd_cat(K2) input. It is
the admission used by the selected Cartesian totalization construction;
this tranche does not prove it necessary for every possible two-sided
doctrine. Canonical hom_int already has this precise type. The ordinary
fixed-endpoint Hom above still accepts its broader input. Public Functord
and the single-family identity/relative Homd interfaces are unchanged.

The [migrated original module](production_cubical_total_duality.lpfragment)
keeps all original named constructors in their order. The root is literally
the native identity Homd of D_E. Reading its lower leaf through O gives

```text
Hom_(Sigma E[x1])((x2,u), (y2,E[a][y2](v))).
```

This is the checked replacement for the old comparison with the opposite
of the ordinary fixed-endpoint inner total. Its Sigma-Hom uses the
corrected negative total. Shared constructor objects do not identify the
two categories' higher actions.

The source projection is total duality applied to the outer Sigma
projection. The target projection uses TotalOp_funcd on the canonical
Cartesian inner projection, then the existing Sigma-map and product
projection, and finally total duality. Its displayed source base is O(K1),
not T(K1). The constructor retains the chosen filler b o u -> v o a.
Both endpoint arrow computations and their identity/composition boundaries
check through the original owners. No independent lax-arrow category,
square, two-sided Sigma, or new comparison witness is introduced.

## Legacy rule boundary and qualification

Seven old same-base Op clauses in cubical_square_total are retained as an
explicitly inactive comment in the staged module. Three were runtime
projection rules; four were proof-time reindexing/section comparisons.
Their old types no longer express the corrected duality. The basic target
projection observation is now checked through the generic whole operations,
without a replacement special opposite rule. Parameter-map/base-change,
reindexing, section and identity-graph observations remain obligations at
their actual later consumers. The inactive block is not qualified code and
must not disappear from the migration ledger merely because this slice passes.

The combined focused check imports the four original reviewers once. It
passes 25 positive and four negative assertions, including the generic
inner-base projection, both higher side actions, actual inner Hom,
directed/noncollapsed fillers, and endpoint composition. The strict LHS
audits have no unreviewed slots. The exact 1,938 inherited core critical-pair
bodies are unchanged; the old module baseline failed before checking its
opposite clauses, so this is not a confluence or legacy-rule certification.
SR, warnings and the serial 90s/2GiB/64MiB-file guard remain enabled with
OCAMLRUNPARAM=o=20. The complete core is unchanged.

The broader original profile import now reaches
gray_interchanger_source_common_path in gray_interchanger_orientation.
It calls the retired functord_transport_lhs_agrees. The selected middle
action is the pre/right route, so simply replacing that name by the right
agreement would equate a generally lax square's endpoints. Continue by
proving the source reading from its actual left telescope while retaining
the separate target reading and the directed interchanger. Then qualify
the remaining represented graph and its total/base-change observations.
That broader failure was recorded before minimizing the canonical projection
rule's reconstructible coefficient slot. The final combined check covers
the minimized rule; the failing interchanger source is unchanged. The
verification records this exact receipt boundary.

Replay the combined slice from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet cubical_migration_controls.lp
```
