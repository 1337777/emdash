# Frontend Cartesian structure and fixed evaluation

Date: 2026-10-25. Status: focused implementation qualified; displayed/Pi/Homd
and full frontend integration remain open.

The structural transfer now follows the native distinctions. Its 17
declarations contain the original ordinary `Functor_cat`, the added
`Functor_cart_cat` support, and the earlier native fixed evaluation
`fapp0_func`. Joint evaluation, constant abstraction, exchange, diagonal and
Cartesian curry/uncurry have their native Cartesian mapping-category types.
The three runtime clauses are the original ordinary target-product
projection, Cartesian functor-object projection, and Cartesian target-product
projection. No mapping categories are identified merely because their object
classifiers agree.

The actual bracket lowering retains two important cases:

```text
H : X → Cart(A,B),  a : X → A
x ↦ H[x][a[x]]                    uses Cartesian joint evaluation

H : X → Functor_cat(A,B),  a : A fixed
x ↦ H[x][a]                      uses fapp0_func(a) ∘ H
```

The second case preserves an existing valid consumer with lax transformations
in the ordinary mapping category. It is not narrowed to Cart merely to reuse
joint evaluation. Conversely, genuinely varying joint evaluation through
ordinary `Functor_cat` is rejected. Pairing two already-formed functor objects
retains the ordinary functor classifiers used by the native Product_pair
projection; this avoids introducing an extra category-comparison rule.

The public `functorCategory` method remains ordinary. The explicit
`cartesianFunctorCategory` method and `cart A B` text constructor expose the
native Cartesian choice. Their method/constructor inventories are updated.
The existing bracket example now supplies Cartesian functor-valued diagrams
where its joint, diagonal and exchange consumers require them.

The two closed-fibre declarations `Fibre_func` and `functord_transport_func`
now use `Cat_cart` in their fibre types. They and the structural transfer have
new source pins only after type/consumer review and native conformance.

Validation:

- Focused structural, closed-fibre, bracket, program and demo scope: 28 tests
  pass; two native opt-ins are separately exercised.
- Three native tests execute five guarded source checks: structural basis
  acceptance and bad-codomain rejection, the **actual generated** joint and
  fixed evaluation terms (also rejecting the ordinary joint-evaluation type),
  and section/fibre/transport acceptance with wrong-fibre rejection. All three
  tests pass with subject reduction and stable inputs.
- Root typecheck and changed-file lint pass. No generic LF checker, runtime
  compiler, intrinsic owner schema or frozen MVP change is made.
- The broader constructor/review scope has 31 passes and two failures in
  existing displayed consumers. They expose the remaining old family
  coefficient in the rich surface view and in the Sigma-arrow transfer.
  Those failures are retained as F03 work; no whole TypeScript pass is claimed.

[Exact verification](foundation_frontend_structural_verification.json)
records the source hashes, positive/negative receipts and output identities.
The health dispatcher was held only for serial native checking and then
resumed; the held target's child receipt retains actual checker timing.

## Next existing consumers

The failing displayed-family view is concrete:
`coreTypeForCategoryObject(Catd_cat(K))` in `surface.ts` still produces
`Functor K Cat_cat`, and family-fibre/transport construction in
`categorical_program.ts` and `categorical_surface.ts` still supplies that old
coefficient. Migrate those authoring views to the actual declared coefficient
without changing public `Cat_cat` or adding a checker special case. Keep the
coefficient as a normal declaration/reference in the selected LF environment.

`categorical_comprehension_transfer.ts` is the next transfer failure at
`sigma_arrow`; review its family-only coefficient occurrences against native
source. Do not globally replace ordinary universe operations in later files.
The fixed evaluation owner now belongs to the structural prerequisite layer;
the later dependent-target transfer must reuse it, not introduce a second
free declaration for the same qualified symbol. Its Pi/Cartesian-inclusion
and Homd migrations remain separate required parts of the
[frontend subplan](../../../docs/EMDASH_FOUNDATIONS_FRONTEND_MIGRATION_PLAN.md).
