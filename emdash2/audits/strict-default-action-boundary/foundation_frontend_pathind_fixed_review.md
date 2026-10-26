# Fixed-source PathInd and Cartesian covariance migration

Date: 2026-10-26. Continuation of `0bef0f95`; active native source is unchanged.
The [acquisition](foundation_frontend_pathind_fixed_acquisition.json) identifies
the eleven selected native owners. The [verification](foundation_frontend_pathind_fixed_verification.json)
records exact input hashes, native receipt and focused results.

## Contract and computation

FibCov_target_catd now uses the native Cartesian mapping category
Cart(K,Cat_cart). Its value at x is the Hom from Rep_K(x) to E in that category.
The three existing covariance projection owners are retained. Their value is
viewed as an ordinary transformation through strict_transfor when extracting
a component or computing path induction on a Sigma-projection pullback motive.
The public ambient Functord remains lax; this does not strengthen arbitrary FF.

All eleven native signatures and all six transparent bodies are checked by the
native consumer. PathInd's component, transported point, pullback motive and
reflexive-arrow section retain their actual computations. The final rho-section
comparison now computes to the canonical arrow in TypeScript as it does natively;
its old not-equal expectation belonged to the previous limited transfer.
Wrong source, motive, fibre and evaluation endpoints remain rejected.

The closure contains five opaque declarations, six checked definitions and ten
local runtime clauses. One old decoded-type presentation runtime fold is removed.
The exact pathout_refl_eval_func body instead uses the already-qualified
proof-only category presentation rule under its LF parameters. Its operational
body is unchanged, and no path/proof argument is added. A duplicate hom_con
object projection is also removed: the earlier dependent-target fragment already
owns precisely that action. The final focused tests pass without either rule.
No generic compiler or checker change was required in this tranche.

## Historical reviews and active authorization

The early PathInd proposal had imported its supposedly frozen predecessor
revision/counts from the live PathOut transfer. Likewise, the internalized
proposal imported the live fixed-source revision/counts. Those historical
contracts are now pinned to their actual 550316a and a361dc3 snapshots, preserving
the old mathematical evidence and rejection controls. Their passing validators
do not qualify the current migration. The active transfer names this goal as
its current authorization and retains the historical review identifier separately.
Current native and consumer evidence supplies qualification of this scope.

## Validation and remaining work

The native run passes 27 assertions (eleven signatures, six bodies and ten
computations) in37.518s/168,580KiB with subject reduction and warnings enabled,
under60s/2GiB. The eighteen-case run includes this native check. After removing
the duplicate local projection, the final TypeScript replay passes17 cases;
its native opt-in is carried from that unchanged-signature/body consumer.
Historical proposal/review checks pass27 cases. Root typecheck and lint pass.
A development run rejected nonconsecutive clause metadata after duplicate
removal; renumbering that group's clauses resolved it without a semantic change.

Whole internalized PathInd, transitivity, the full Homd P-index endpoint
comparison and remaining authoring/audit integration are not qualified here.
The previous full TypeScript aggregate remains inconclusive. Production health,
final integration and later book/article/legacy-nerve stages remain required.
