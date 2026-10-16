# Profile and first extension consumers of the migrated core

Date: 2026-10-16
Predecessor: `c9962d6e`
Status: staged profile, PathOut and fixed-endpoint Hom consumers pass; broader import closure and public migration remain incomplete
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_profile_consumers_verification.json)

## Preserved defaults and profile boundary

Public Functor remains strict and Transf/Functord remains conventional lax.
The profile extension retains its existing StrictTransfor, StrictFunctord
and extracted-cell property interfaces. This tranche does not reinterpret
Functord, equate it with StrictTransfor, or require a new strict wrapper.

The existing strict_functord_transport_rhs_tele_path now observes the actual
family coefficient Cat_cart and its Functor_cart_cat Hom. Its capped path
is derived from the existing core right-leg agreement, with symmetry to
retain the original statement. The two older profile-only right-leg
unifiers are removed: the selected conventional-lax default already fixes
that leg for every displayed map. This is not a strict left-leg equation.

IsStrictFunctord still constrains the ordinary extracted
functord_laxity_transf through IsStrictCell in Functor_cat. Its property
does not change to a Cartesian Hom merely because the transport telescope
has a Cartesian target. The [replacement path definitions](production_profile_readings.lpfragment)
preserve these different roles. Redundant strict-functor wrappers remain
pending migration and retirement; genuine strict-transfor profiles remain.

## Original PathOut derivations

The shaped fixed-source PathOut bridge needs two annotation changes:
Product_pair_tele_func has its Cartesian mapping-category target, and the
shaped profunctor cell is evaluated in Cat_cart. Its original pullback,
totalization, object computation and next Hom action are unchanged.

The original pathout_transformation_reframing module used the retired
general functord_transport_lhs_agrees statements. Its particular map is
tapp1_con_at_transf(epsilon,y), with y fixed. The chosen conventional
pre/right action does supply the required equality here, even when epsilon
has nonidentity post/left naturality. The [migrated proofs](production_pathout_reframing.lpfragment)
factor through functord_transport_rhs_agrees instead. Cartesian
precomposition computes the source directly. No general left-leg equality
is restored, and no new runtime or unification rule is installed.

The existing path statements are observations, not operational proof
arguments added to Homd or its projections. Direct capped reflexivity did
not join the stable middle-action owner; using the already available
whole comparison and its component resolves that presentation issue.

## Original fixed-endpoint cubical Hom consumer

The existing homdc_target_func now evaluates a component in the admitted
Cartesian Hom, then uses Functor_cart_include before ordinary object
evaluation. This follows the core's existing fibre-covariance pattern.
Its [definition](production_cubical_hom_evaluation.lpfragment) retains the
original input E:T(K1)->Catd(K2), the same whole first-coordinate action,
and the same public result type.

homdc_ uses hom_con_int_view and the represented square uses hom_int_view.
These are the core's existing ordinary views of its Cartesian Hom packages.
No new square operation, primitive, restriction on the external E, or
curry/uncurry substitute is added. The original reviewer still computes

```text
homdc_square_fibre(C,u,v,a,b) = Hom_(Hom_C(x1,y2))(b o u, v o a).
```

Both side-arrow Hom actions remain available, and the original negative
comparison against the differently bounded twisted square remains rejected.
This is migration of an existing foundational consumer, not resumed nerve
reconstruction or new cubical theory.

## Qualification and next boundary

The complete staged core is byte-identical to c9962d6e's checked source.
The profile module passes. Its original reviewer assertion body, imported
directly from its actual profile owner, passes 59 positive and 13 negative
assertions. The shaped PathOut and reframing modules pass. The original
fixed-endpoint cubical reviewer passes seven positive and one negative
assertions, including the leaf and higher-action observations.

Every reported passing receipt matches the final emitted input bytes.
Subject reduction and warnings remain enabled under the serial 90-second,
2-GiB, 64-MiB-file profile with OCAMLRUNPARAM=o=20. The strict LHS audits
report no unreviewed slots. The profile's 2,301 critical-pair bodies are
unchanged from its failing pre-edit baseline; the other affected module
checks retain exactly the checked core's 1,938 bodies. No runtime rules or
unification rules were added. These comparisons do not certify confluence
or a complete semantic model.

The original broader import of examples/gray_profiles.lp remains staged
and required; the isolated profile assertion check does not replace it.
It now reaches emdash3_2_cubical_square_total.lp:23,
sigma_proj1_family_funcd. That declaration still constructs a Catd family
using Sigma_func with public Cat_cat codomain. Continue the original varying
Sigma projection and its actual opposite/totalization consumers, reviewing
their whole coefficient and map profiles before changing the signature.
Do not restore the old same-base fibre opposite or make all displayed maps
strict just to satisfy this annotation.

Public promotion, the remaining original imports/diagnostics/library
consumers, wrapper retirement, consumed compatibility checks and final
catalog/health/CI qualification remain required.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet profile_controls.lp
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet emdash3_2_pathout_transformation_reframing.lp
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet examples/cubical_dependent_hom.lp
```
