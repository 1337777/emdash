# Supplied Hom actions and one-way lax currying

Date: 2026-10-17
Predecessor: `a2b7ae37`
Status: complete original Hom-comparison owner and reviewer qualified in the staged migration; remaining library migration and public promotion open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The original ordinary-target reconstruction accepts an arbitrary source I,
strict functors F,G:I→C, the original OneCat(C) premise and a supplied ordinary
lax Hom action. Its graph construction requires a strict x-profile. The new
admission obtains that profile without adding a source-base truncation or a
caller-provided naturality witness.

For the target family y↦Hom_C(F[b],G[y]), OneCat(C) gives discrete fibres.
The added discrete_functord_category is an explicit structural closure/model
obligation, parallel to the pre-existing discrete_functor_category: maps into
a fibrewise discrete family form a discrete category. It is not derived from
component beta rules. It implies discreteness only of the particular Hom
categories consumed by the admission; Catd(I) itself is not declared ordinary.

Using that closure, one_cat_hom_action_is_strict is a definition applying
discrete_cell_is_strict to the supplied alpha's existing extracted post/left
and pre/right cells. The existing make_strict_transfor admits the same alpha.
The exact underlying-action projection checks, and an unclassified raw alpha
is still rejected as a strict transformation. The original reconstruction
body continues through the same represented graph and its chosen source and
target comparisons. All operational parameters remain the original ones.

The next original consumer curries a general lax ProfMap. Its former use of
the now-Cartesian curry_func_func cannot typecheck at that profile. The added
curry_lax_func_func is a one-way strict functor between the ordinary mapping
categories:

```
Functor_cat(A×B,C) → Functor_cat(A,Functor_cat(B,C)).
```

Its object is the existing Cartesian curry followed by Functor_cart_include.
The native whole operation is declared structurally. Its semantic justification
is restriction along the tensor-to-product projection followed by closed-Hom
adjunctions; this is an inference from
[Ara–Guetta v1, §§12 and 21](https://arxiv.org/html/2503.08832v1).
No tensor-to-product implementation or native derivation of that adjunction
is claimed here. No lax Cartesian uncurry or equivalence is added.

The first-Hom and transformation projections retain the supplied eta. At a,
the whole component is its original prewhiskering by (a,-). A whole component
functor comparison retains every next-Hom input. Identity and composition
join after projection. The controls check those operations and reject both
replacement of eta and automatic strict-transformation typing.

The leaf of that prewhiskering contains evaluation of the identity on the
constructed product-pair functor. The original Hom-comparison module already
proves its equality through staged identity paths. An initial stronger
runtime-collapse test failed; inspection recovered this original intermediate
expression. That stronger test was not an existing production contract. The
selected implementation reuses the original proof and adds no product beta
solely to force a shorter leaf. The replacement controls concern the whole
prewhiskered component and reject a different input at that same component.

The existing represented-curry comparison receives two contextual proof-time
views through the ordinary inclusion. Both retain the supplied profunctor
and its left/right endpoint functors. Their typed reflexivity controls pass;
arbitrary profunctors and changed left endpoints are rejected. These views
are installed at the actual Hom-comparison consumer, with standalone replay
controls after the core import. Whole runtime heads remain stable.

The original module's 68 coefficient annotations, 12 ordinary Hom views and
43 uses of the product-pair telescope are adapted together. The latter use
the actual ordinary inclusion of the Cartesian telescope. The supplied
comparison and selected inverse are retained throughout the original source.
The separate ordinary modification owner changes only its displayed
coefficient tag from Cat_cat to Cat_cart; its original reviewer passes.
Fourteen Cat_cat occurrences in two generic ordinary-functor inverse helpers
retain their original types. They are not consumers of the profunctor's
Cat_cart inverse package. An initial blanket retag reached those helpers
unnecessarily; a proposed extra inverse-cut instance was withdrawn after
the use inventory showed that preserving the original helpers was sufficient.

The complete replay subsequently accepted reconstruction and the unit/counit
declarations, then exposed a precise proof adaptation: the new curry's
component evaluates one fibre identity, whereas the original proof expected
two nested evaluations. The protected pair-identity lemma and component proof
now apply the existing fapp1_id_path directly to that fibre, followed by the
unchanged transformation-identity beta. The component statement and original
I1/C1/r parameters are preserved. Those exact owner definitions pass in the
focused replay; the complete original reviewer now passes.

The full replay accepted that repaired component theorem and next reached
the unit's classified/raw action comparison. A derived admitted-action
component path now applies the existing make_strict_transfor_carrier_path
under the two component evaluations, then composes with the raw-curry
component theorem. The unit, counit and reconstruction point proofs consume
this observation. It introduces no runtime equality cut or operational
proof argument. Both its focused owner check and the complete original
reviewer pass.

The combined inherited-core and curry reviewer passes 274 positive and 70
negative assertions with subject reduction. Current owning-file LHS audits
have no unreviewed candidates. Fourteen additional core warning bodies concern
the new curry projection versus generic identity/accumulation/composition cuts
and specialized identity normalizations. Typed unit/composition/higher-action
controls qualify the intended profile, not every specialized normalization
or global confluence. The full original reviewer passes all 12 positive/four
negative assertions: identity images, reconstruction action, both triangle
modifications/paths and the selected-comparison noncollapse checks. The final
2650 warning bodies match the preceding late-prefix check exactly. Exact
inputs and receipts are in the [verification](production_hom_comparison_admission_verification.json).

Performance diagnosis distinguishes unchanged source from new comparison
cost. Two 90s trials stopped during core import. The local-placement trial
used the exact core bytes, checker, runner and runtime settings of an earlier
26.5s successful run. The checker used one CPU and less than 0.8GiB RSS at
87s, while sampled CPU frequencies were around 400MHz and pressure counters
were negligible. The 180s/2GiB timed run completed in 162.5s. The subsequent
combined core check completed in 28.3s, indicating variable host throughput.
No host power setting, memory default, serial/file guard or swap policy was
changed. Consumer-specific deadline extensions remain diagnostic headroom,
not a performance certificate. The original reviewer passed in 397.4s under
the reviewed 600s/4GiB/o=20 profile after the 300s import timeout. The 4GiB
cap was retained throughout these larger import checks.

Replay: regenerate production_owner_migration.py; run
hom_action_admission_controls.lp, lax_curry_regression_controls.lp and the
original examples/one_cat_hom_comparison_data.lp with their recorded limits.
Next migrate/check one_cat_adjunction_introduction and its original reviewer;
its profunctor component/evaluated-inverse tags still need review. The
independent presheaf/direct-cover route, remaining library migration,
strict-functor wrapper retirement, production promotion and final
qualification remain required.
