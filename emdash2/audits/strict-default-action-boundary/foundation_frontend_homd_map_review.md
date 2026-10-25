# Defined Homd target map and total-dual displayed Hom action

Date: 2026-10-25. This continues the native foundation transfer after
`9551fb64`; it does not change the Lambdapi source or introduce a new
mathematical rule. Exact acquisition and execution evidence are recorded in
[the verification record](foundation_frontend_homd_map_verification.json).

## Native relative target map

`Homd_target_con_func` now has its actual checked composition body, replacing
the former signature-only view. It uses the first Hom action of the target
index functor and the transpose of the strict Hom-action functor induced by
coefficient postcomposition. It never transposes an arbitrary lax FF directly.
The source remains `Op_cat(Transf_cat(K,Cat_cart,D,E))`; the result is the
Cartesian map category between H_E and H_D.

The needed ordinary opposite-Hom rule is now transferred in the common
source-prior duality fragment. Its later copy in the direct mixed-source
fragment is removed. The native `hom_postcomp_func` signature is likewise
source-prior and shared; weakening no longer redeclares it. Two existing
object projections compute postcomposition through to `Homd_coeff_diagram`.
These are native projection rules, not new type-comparison equations.

Declaration phases now install source-prior owners, their required native
projections, and then the actual target-map/relative-root bodies. All five
late declarations retain their native status: the identity root is opaque;
Homd_target_con_func, Homd_target_map, homd_rel_cart_int and homd_int have
checked definitions. No operational equality or supplied comparison argument
is added.

## Displayed Hom and frontend consumers

The existing Hom_catd base-action ladder keeps its three injective heads and
nine runtime clauses. Its negative section is now over CoAbove2_cat(K), in
TotalOp_catd(E), and its whole action targets the Cartesian functor category
between the Hom fibres. Identity/composition, full-to-capped and capped-to-point
projections, and Transf_catd specialization remain separately checked.
Ordinary composition of the resulting functors still belongs to Cat_cat;
the family coefficient Cat_cart is not substituted at that owner.

The remaining generic telescope and text fixtures use total-dual negative
Hom/Transf sections. Their early-accessor observations use the already migrated
section-weakening owner rather than the retired projection-pullback expansion.
This changes neither the depth/layer test coverage nor the computed result.

## Validation boundary

The focused runs qualify 63 distinct cases across the recorded scopes,
including native duality, the actual target-map body/whole higher consumer,
and all nine displayed-Hom action projections. The stronger old-section
negative control passes in the final native replay, whose retained source
keeps the correct fibre-Hom result classifier. Its receipt is
`20261025T231514Z-030d4212845f477ea71ceda29dad55b2`, 24.448s/169,072KiB under
60s/2GiB with subject reduction and warnings. The earlier weaker negative is
not used as variance evidence.

Workspace, registration, typecheck and lint pass. The full TypeScript
aggregate reaches actual test execution, then its 900-second bound expires.
The partial stream contains 2,174 completed test/suite events and 55 failure
events across 16 files. The [pending inventory](foundation_frontend_pending_test_inventory.json)
is an explicit continuation checklist, not a complete suite report or permission
to alter historical evidence. Ordinary Hom, PathOut, demo/authoring and audit
consumers require focused source review. No global source-pin refresh is selected.

The last reported MCP cancellation/reaping case passes in isolation (26.1ms;
all five owning cases pass). Its position in the partial event stream does
not establish the cause of the aggregate stall. The test worker remained
CPU-active with roughly 2GiB RSS before the aggregate deadline; do not infer
host fault or a rewrite loop from those observations. Preserve this evidence,
fix the actual scoped failures, and investigate any repeated aggregate runtime
problem before extending its deadline. No worker code, runtime defaults or
host settings are changed.

## Remaining computation

The full transferred comparison

```text
homd_index_presheaf(homd_tgt_func(FF,x,u,y)[v]) ≐ homd_(FF,x,u,y,v)
```

still reports `not-equal` in the current TypeScript runtime (wave297, 1,024-step
budget), while the native kernel comparison remains qualified. The former
opaque target-map body is now resolved. Next inspect the consumed identity
covariance/mate and represented coefficient projections; transfer their native
owners and computation rather than adding a shortcut comparison or changing
the Homd contract. Full relative endpoint computation remains an acceptance
requirement. Higher profile/source-pin integration and production health also
remain open; book/article and legacy nerves remain subsequent stages.
