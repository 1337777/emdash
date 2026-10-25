# Frontend displayed-product coefficient migration

Date: 2026-10-25. Status: focused product implementation qualified;
projections/pairing, Pi/Homd and final integration remain open.

Displayed products retain their transparent construction:

```text
uncurry(Product_cat_coeff_func) ∘ Product_pair(B,C)
```

The public product constructors remain separately available. The transfer
adds the already-native coefficient product/partial-product owners and
`StrictTransfor`/`strict_transfor`. The latter is the ordinary observation of
the coefficient action, whose type already supplies the strict carrier. No
caller supplies strictness evidence, a comparison cell or equality proof.
Only Obj of the Cartesian mapping Hom reduces to `StrictTransfor`; its higher
category is not replaced by the ordinary lax modification category.

Evaluation follows the Cartesian source and uses that transfor observation.
The uncurry object now reduces through the native Cartesian cuts to ordinary
composition of Eval and the fixed-right product map. This removes the old
identity-postcomposition detour in this consumer. The ordinary operations and
their unrelated reductions remain; no `Product_catd` primitive is added.

The fibre computation takes8 steps instead of12, and shared-base transport
takes17 instead of26 in the existing generic evaluator. The coefficient
product action accepts arbitrary component functors. Therefore the migrated
negative control compares transport along p with `Product(B[p],C[q])` for
unrelated parallel p,q; it does not demand that a legitimate coefficient
action on two arbitrary functors be stuck. Both the TypeScript and native
controls retain that non-collapse.

The transferred scope is12 declarations/35 runtime clauses. All local clauses
pass the existing TypeScript subject checks; no generic checker, runtime
compiler, intrinsic owner schema or native mathematical rule is changed.
The active metadata has a separate foundation-migration reference; historical
approval labels do not authorize arbitrary additional operations.

Validation:9 product/demo tests and33 boundary/metadata/program tests pass.
Two native tests pass at60s/2GiB, including the **actual emitted** transport
term and type, its comparison with the componentwise map, the p/q negative,
and the selected general uncurry reduction. Typecheck and changed-file lint
pass. The source pin is refreshed after those checks.
[Verification](foundation_frontend_product_verification.json) records exact
inputs, receipts and scope; no whole frontend/integration pass is claimed.

Next, adapt the existing displayed projection/pairing transfer to this same
coefficient product, the Cartesian full-action targets and
`comp_cat_con_cart_func`. Retain lax displayed FF across the base. This is
the next concrete consumer in the [frontend plan](../../../docs/EMDASH_FOUNDATIONS_FRONTEND_MIGRATION_PLAN.md),
before varying-base Pi and the corrected Homd ladder. The production-health
aggregate remains stopped pending its separate measured resource review.
