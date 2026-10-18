# Terminal and initial family presentations

Date: 2026-10-18 (UTC)
Predecessor: `bedea259`
Status: staged family owner and eight original endpoint-observation proofs checked; central gate reaches carrier-family coefficient migration
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_terminal_family_verification.json)

The general `terminal_adjunction_presented_family` and
`initial_adjunction_presented_family` retain their original transformation e
and parameter functor F. Their corrected outputs use
`Functor_oplax_cat(WalkingArrow,C)`, matching the existing general
`transf_arrow_diagram_func`. They acquire no OneCat restriction.

The ordinary universality consumers already require OneCat(C). Two defined
counterparts use `one_cat_transf_arrow_diagram_func` under that existing
hypothesis and then compose with the same F. The consumers use these
ordinary presentations and the qualified ordinary family exchange. Their
original adjunction data, chosen maps, inverse data and proof bodies remain.
No new primitive, rewrite rule, unification rule, strictness premise on e
or FF, or operational equality argument is introduced.

Removing the two ordinary helper definitions, restoring the two general
codomains, and reversing six interface substitutions recovers the complete
original family owner modulo whitespace. Reversing those substitutions also
recovers the complete endpoint-observation module. All eight original
endpoint proofs check with their original bodies; these are downstream
derived paths, not equality arguments added to foundational operations.

The observation module passes in 124.888s with maximum child RSS
3554384 KiB under the existing 600s/4GiB/o=5 profile. All 2709 warning bodies
match the preceding central baseline. Subject reduction remains enabled.
The core regression and mapping/exchange control input closures still match
their earlier receipts exactly, so those unchanged checks were carried.

The fresh central check passes this owner and stops at
`comm_ring_carrier_catd` in `emdash3_2_commutative_algebra_category.lp`.
Its original composite with `Path_cat_func` lands in `Cat_cat`, whereas
migrated `Catd` requires `Cat_cart`. That carrier-family coefficient is the
next actual migration boundary; the existing whole ring-carrier action
should be retained. The central run took 134.845s with maximum child RSS
3859308 KiB at the same cap. No resource limit was increased.

The broader `examples/one_cat_terminal_adjunction_families.lp` reviewer also
imports native kernel/cokernel zero-column consumers that remain unmigrated;
it is not claimed green here. This checkpoint qualifies the actual family
owner and its eight endpoint-proof consumers, not that broader closure.
Production promotion, remaining library migration, wrapper retirement,
catalogue/health/CI and source-pin review remain required. The separate
application-equivalence goal stays paused.
