# Ordinary-target mapping comparison and diagram-family reflection

Date: 2026-10-18 (UTC)
Predecessor: `a44fe813`
Status: staged whole construction and component observation checked; downstream integration remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_one_cat_family_reflection_verification.json)

The original family-reflection proof exchanges two parameters, applies the
existing walking-diagram reflection, and exchanges back. Its inputs are
ordinary mapping categories with an existing OneCat target hypothesis.
After the migration, Cartesian exchange requires the Cartesian mapping
profile at both levels. Admitting only the outer transformation does not
change the inner mapping category.

The selected structural comparison is

```
J_AC : Functor_cat(A,C) → Functor_cart_cat(A,C)
R_AC : Functor_cart_cat(A,C) → Functor_cat(A,C),   OneCat(C).
```

`one_cat_mapping_comparison` declares their whole computational isomorphism.
Its inverse has a whole proof-time reading as the existing inclusion. Its
forward action is compared with the existing, derived OneCat strict
admission. This is a structural whole constructor, not a theorem inferred
from identical object sets. The actual maps and arbitrary input
transformations are retained; the two mapping classifiers are not equated.

The family maps and exchange are definitions through that comparison and
the existing Cartesian postcomposition/exchange:

```
L_BI = Post_cart(J_IC) ∘ J_B,[I,C]
R_BI = R_B,[I,C] ∘ Post_cart(R_IC)
S_BI = R_IB ∘ sym_cart ∘ L_BI.
```

Both family inverse paths are derived from these actual factors using
existing associativity and the selected inverse laws. A generic proof-only
reflection lemma applies the actual inverse to an equality and transports
the identity functor's reflection property along its whole inverse law.
No new inverse-assembly assumption or operational equality argument is
introduced by these definitions.

The original `one_cat_diagram_family_map_path` retains arbitrary raw
F,G,h,k and its two whole endpoint-transformation equality premises. Those
premises now use the ordinary exchange projections. Its proof follows the
original exchange/reflection/exchange-back outline, with reflection through
the two actual profile maps inserted around Cartesian exchange. It does not
replace whole transformation equality with pointwise equality premises.

The double object projection computes directly. The double component
observation is a **derived path**, not a new runtime erasure of strict views.
Normalizing the actual exchange gives the original component surrounded by
two canonical admissions. `one_cat_family_exchange_component_path` compares
those admissions in order and applies the existing component evaluations.
Its proof has no extra caller-supplied comparison. Higher action remains
the action of the actual whole maps; this observation does not manufacture
a pointwise assembly operation.

Development failures are retained in the verification. Demanding one large
reflexivity comparison for the nested component failed, although the two
individual admission readings are available. Explicit sequential equality
composition gives the required observation without adding another runtime
rule. Expanding the entire derived strictness certificate in a runtime
projection was rejected: critical-pair output reached the 64 MiB file guard
after about 75 seconds, with maximum child RSS about 3.72 GiB. The selected
stable action and proof-time readings avoid that expansion. The focused
construction/observation check returned to about 40 seconds at 4 GiB/o=20.
No resource cap was raised for the rejected variant.

Two constructor-scoped whole first-Hom comparisons join the actual inverse
laws when composition's Hom action projects before the DefIso cut. They
retain the same comparison and endpoint functors. The ordinary-view reading
retains its input transformation; controls reject a different map and a
global identification of mapping classifiers. The inferred-slot audit and
manual review cover the four runtime clauses and five proof-time clauses.
Twelve new warning bodies concern the two identity-observation orders and
their inherited duality/family representations. These scoped checks do not
claim global confluence.

The complete core source is unchanged and its exact regression closure
still matches the carried receipt. This remains non-library staging. The
central check now passes the original whole family-reflection owner and
stops at `one_cat_arrow_family_comparison_to` in
`emdash3_2_one_cat_arrow_family_isomorphisms.lp`. It still supplies raw
walking-diagram maps to Cartesian exchange and expects the old ordinary
target of the now-oplax general `transf_arrow_diagram_func`. Its existing
OneCat hypothesis permits a guarded ordinary presentation using the whole
exchange above; that next consumer has not yet been migrated. Preserve its
actual to/from modification choices and inverse-law proofs. The central
failure is a positive integration obligation, not a negative control.

The original downstream callers, central diagnostics, remaining library
migration, redundant strict-functor wrappers, production promotion, and
final catalogue/health/CI/source-pin checks remain required. The separate
application-equivalence goal remains paused.
