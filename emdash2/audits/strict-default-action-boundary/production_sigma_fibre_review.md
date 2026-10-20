# Sigma fibre inclusion and zero-cone observations

Date: 2026-10-20
Status: staged consumer qualified with typed generic observations; bare specialized inference remains limited
Predecessor: `83c5308b11ccc7b5b1c4285d8cfc0de184b4177a`.

This continues the existing-consumer migration under the
[living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
Exact inputs, outcomes and development failures are retained in the
[verification](production_sigma_fibre_verification.json).

## Original construction retained

`sigma_fibre_inclusion_func(E,x)` enters the existing Sigma by constant base
change. Its original source is unchanged and typechecks against the migrated
core. Its first and second arrow projections also compute for a general
family, recovering `id_x` and the supplied fibre arrow.

The original zero-cone fibre inclusion is still the composite of two such
inclusions. The inner family now has the existing Cartesian coefficient
`Cart(B,Cat_cart)`, with B the corrected oplax walking-arrow diagram category.
The outer family is `homdc_op_edge_catd` over `TotalOp_cat(C)`, so its inclusion
is read through `TotalOp_func`. The represented inner parameter remains over
`Op_cat(C)`, the dimension-one transpose. These two uses of duality are not
interchanged by a global replacement.

The original OneCat hypothesis, whole functor, object values and actual fibre
cell remain. No new mathematical owner, primitive, rewrite, unification rule
or operational proof argument is added to the library.

## Projection elaboration boundary

After those profile corrections, the first base projection checks directly.
The bare nested second/third projections fail while inferring their dependent
pair types at the specialized oplax diagram category. Normalizing the mapped
arrow nevertheless produces exactly a nested pair containing `id_a`, `id_d`
and the supplied `alpha`. Two annotations of the intermediate Hom and its
carriers did not solve the specialized inference problem; the failures are
not relabelled as successful runtime checks.

The [generic control](production_sigma_fibre_generic_controls.lpfragment)
uses the same two-stage construction with arbitrary A, B and F:A→B. Both
single-Sigma observations and all three nested projections pass. This locates
the observed failure at specialization/elaboration rather than at a missing
generic projection computation.

The final reviewer uses three
[transparent, generically typed definitions](production_zero_cone_fibre_reviewer_helpers.lpfragment):
the same two-stage functor and its two nested projections. A runtime
whole-functor comparison identifies its specialization with the actual public
zero-cone inclusion. The two projection definitions then specialize and
compute to `id_d` and `alpha`. This avoids asking the checker to reconstruct
their types after the diagram coefficient has unfolded. It introduces no
operational equality transport or extra caller data.

All five original observations are retained in meaning: the first base,
second base, fibre cell, available next Hom action, and object computation.
The two nested observations now go through the generically elaborated bodies;
one additional whole-functor comparison ties those bodies to the actual
public construction. The final reviewer has six positive assertions.
**The original bare nested-query syntax is still an inference limitation.**
This slice does not assert that every unannotated presentation elaborates or
discharge the separate five terminal Homd runtime obligations.

## Evidence and replay

The final reviewer passes in **32.756 seconds / 191,980KiB** under the default
90s/2GiB resource limits, using the isolated checker with subject reduction,
warnings, source-only loading, o=20, serial execution, 64MiB file limits and
no swap. Receipt: `20261020T221247Z-a9c7a15755b54734846c4fa098b8a122`.
The generic five-observation control passes separately in 28.887 seconds.
Their 2,053 critical-pair bodies have the same multiset digest. No new rule
commands occur in the three staged source/reviewer files.

The migration recipe reproduces all checked source bytes exactly. The six
preceding core/library/combined-context/reviewer receipts still rehash: the
new modules have no rules and do not change those older input closures.
Current coverage is 154 registered core files and 61 registered reviewers;
the central diagnostic retains its five explicit exclusions. A further 637
registered core files and 535 reviewers are not yet staged and remain subject
to compatibility inventory/migration.

Replay by emitting `production_owner_migration.py` and checking
`examples/one_cat_zero_cone_fibre_inclusion.lp` in the emitted package with
the recorded isolated checker/profile. Copy the generic control fragment to
`sigma_fibre_generic_controls.lp` there when rechecking this elaboration
boundary. The unchanged generic library source, development normal forms and
failed specialized annotations have their own recorded receipts.

Next continue the existing direct Homd/constant-family consumers, starting
with `emdash3_2_hom_factor_cubical.lp`, without adding new application results.
Production promotion, supported-checker qualification and the remaining
normalization/terminal obligations stay open.
