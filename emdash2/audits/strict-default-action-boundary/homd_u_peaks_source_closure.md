# Observational ordinary precomposition peaks

The two successors pass: `precomp_observations.lp` under receipt
`20261013T183449Z-03f21619ba0d441396defe6a05aad31d`, and
`curry_observation.lp` under
`20261013T183506Z-3a18963498b24493b0cf728b67c7e10b`. They use the checked
normalization donor and add only assertions. Exact source/receipt/log hashes
are recorded in `homd_u_peaks_verification.json`.

The first target contains three proof-time observations: triple accumulation
via `eq_ap` of ordinary associativity, then generic and Cat-valued
identity-beta absorption via `eq_ap` of the existing identity-family
precomposition/raw-composition comparison. The latter two explicitly map
that ordinary equality through the actual functor's arrow action. They do
not rely on unification propagating the comparison through an arbitrary
outer action.

The independent curry target transports `curry(Eval)=id` through the actual
stable precomposition-by-P context. The path is observational evidence;
none of these operational functors or maps takes an equality argument.

The initial `precomp_controls.lp` remains failed under receipt
`20261013T182459Z-36201fe106644757be405bd611a56254`. Its triple observation
was accepted before the generic identity-beta reflexivity assertion failed:
the existing owner exposes `F[precomp_id(p,q)]`, which is not automatically
identified with `F[q o p]` by reflexivity. That failed source is preserved.

Both passing successors retain all 970 donor critical-pair blocks unchanged.
These are typed proof-time observations of the four ordinary precomposition
warning contexts; no runtime join, rewrite, unification rule, confluence
certificate, or whole-prof/Q qualification is added. The intermediate u-join
source is a separate replay and does not silently include these assertions.
