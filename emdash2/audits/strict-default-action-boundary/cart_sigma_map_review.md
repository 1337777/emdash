# Cartesian-family total maps through corrected intrinsic Homd

Date: 2026-10-15
Status: non-library whole interface, derived Hom action and focused consumers
checked; expanded general arrow-composition and public migration remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [current Homd interface](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owner: [total-map declarations](cart_sigma_map.lpfragment)
Controls: [native consumers](cart_sigma_map_controls.lpfragment)
Replay: [integrated source](cart_sigma_map_replay.py)
Evidence: [verification](cart_sigma_map_verification.json)

## Whole totalization and the actual Hom action

The family coefficient remains Cat_cart. FF:E=>D is a default lax
transformation across K; no strict-FF wrapper, supplied comparison or
equality payload is introduced. The selected coefficient already gives
strict fibre functors and Cartesian naturality inside those fibres.

```text
Sigma_func(K) : Functor(Functor_cat(K,Cat_cart),Cat)
Sigma_map(FF) : Functor(Sigma(E),Sigma(D))
Sigma_map(FF)[(x,u)] = (x,FF[x](u)).
```

The whole first Hom is a definition through the same corrected negative
Sigma total used to form the Sigma Hom. Let H_E and H_D be the existing
Homd presheaves at (x,u),(y,v) and their FF-images. Intrinsic Homd supplies
an actual Cartesian transformation U_FF:H_E=>H_D. Then

```text
Sigma_map_hom(FF,x,u,y,v) = Sigma_con_map(U_FF)
Sigma_con_map(U) = O_func(Sigma_map(strict_view(O_fib_map(U)))).
```

O_fib_map is the component action of a structural whole functor
`R(Cart(K,Cat_cart))->Cart(R(K),Cat_cart)`. Its component at x is the
existing total dual of U[x]. Components retain their functor direction;
higher diagram dimensions are reversed. This is required by the actual
negative-total map, not a second primitive Sigma theory.

Both whole-first and capped-first observations compute

```text
(p,a) |-> (p, intrinsic_FF(p,a)).
```

The second component is the existing Homd action, not a newly supplied
cell or a reconstructed independent formula. A canonical transport arrow
`(p,id)` maps to `(p,laxity_FF(p,u))`, retaining its endpoint `FF[y](E[p]u)`.
The control that substitutes `D[p](FF[x]u)` for that endpoint fails as intended.
Identity total arrows compute after expanding the Hom body first: over an
identity base arrow the intrinsic action is the ordinary FF[x] Hom action.

A general total two-cell `(kappa,eta)` is mapped through this recursive
whole Hom body. Its first projection computes to kappa, without using an
outer projection-composed-with-total-map shortcut. Thus this consumer
retains actual higher base data and checks more than the object formula.

The second parameter Hom maps a modification theta:FF=>GG to an ambient
transformation between the total maps. Its component is the vertical total
arrow `(id_x,theta[x][u])`; units and composition of these parameter maps
compute through the native action owners.

## Composition and normalization boundary

Identity and composition of family maps have the expected whole Sigma-map
normal forms. The intrinsic fixed-p action of GG o FF also compares with
the composite of the two intrinsic Hom functors, using a typed reflexivity
consumer of a narrowly scoped unification rule.

This comparison is proof-time only. Runtime decomposition first at the
presheaf projection and then at the Hom projection disrupted the existing
ordinary/mate laxity extraction controls. Those alternatives were removed;
the verification record pins their failed receipts. The unification clause
must use the canonical `comp_fapp0 Cat_cat` head, rather than its reducible
`comp_cat_fapp0` alias. The typed consumer failed before that correction.
There is no operational path argument and no global strict-naturality rule.

The whole totalization and diagram-duality owners remain structural
declarations with qualified projections. This slice does not establish a
complete semantic model or claim every expanded computation joins.
In particular, comparing the fully expanded image of a general composite
total arrow with the composite of its two images remains a required next
consumer, along with remaining higher-naturality and downstream checks.
No additional Q operation, general coend construction or balance experiment
was introduced.

The ordinary and higher Grothendieck functoriality discussed in
[Ara--Guetta, section 7](https://arxiv.org/html/2503.08832v1#S7) provides
profile/orientation context. It is not evidence that this native interface
already implements all of that paper's functoriality.

## Validation and continuation

Receipt `20261015T083840Z-d4916b4ea4aa43b498238da115b47b98` passes with
subject reduction enabled in 5.589s, maximum child RSS 323,196KiB. Limits
remain the serial default 90s/2GiB/64MiB with OCAMLRUNPARAM=o=20.
The baseline was replayed and checked fresh at the same source pin.

Critical-pair diagnostics change 1541->1636, with 95 added bodies and none
removed. Replaceable-pattern warnings remain 66. Exact grouped-body digests
and participating rule families are recorded for intrinsic identity-base
action (14), Sigma roots (26), object projections (14), Cartesian diagram
duality (13), Hom projections (10), and parameter modifications (18).
Typed consumers cover the stated computations; this is not global
confluence. The LHS audit reports zero unreviewed compound slots.

These are non-library owner-position candidates, so production catalog,
health and aggregate gates are unchanged. Full source integration and its
downstream validation remain required by the living goal.

```bash
python3 audits/strict-default-action-boundary/cart_sigma_map_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_sigma_map/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_sigma_map/candidate.lp --strict
```
