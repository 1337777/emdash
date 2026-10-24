# Original presheaf and shape consumers

Date: 2026-10-24
Status: qualified non-library continuation; normalization and production gates remain
Predecessor: `99035271`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

This implements the next original-consumer slice of the [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md): 17 owners and 17 complete reviewers, retaining all 190 declarations, 142 positive assertions and 14 negative assertions. It also rechecks the previously qualified semicubical nerve and every qualified consumer in its reverse import closure. The separate nerve-equivalence goal stays paused.

The source changes are limited to the existing interfaces:

- Semisimplicial realization uses `Path_cat_cart_func` and the `Cat_cart` coefficient already required by public presheaves. Its level, face, map and higher observations remain at their original owners; the rigid facade stays distinct from the raw functor category.
- Tetrahedron faces use the existing default functor and join owners, retiring four redundant underlying views in their reviewer.
- The existing whole `semicubical_nerve_func` now lands in `Cat_cart`, matching its Yoneda/presheaf consumers. The index Homs are path categories of set-valued face codes. This is a selected structural coefficient declaration, not a general coercion of arbitrary `Cat_cat`-valued families. Its object beta retains the same owner with inferred endpoint slots. The selected comparison with the recursive face interpreter stays propositional; its runtime noncollapse assertion still passes.
- The represented decoder exposes its original ordinary functor-category target by composing the whole Hom action with `Functor_cart_include`. Its next Hom action is retained. The Yoneda section exposes the already-classified `fib_cov_transf` through `strict_transfor`; arbitrary displayed maps are not made strict.
- The simplex sieve reviewer observes the current whole `Cat_cart`-valued action and its `Functor_cart_cat` Hom. Its higher-action assertion is retained, with the corrected classifiers.

The existing whole composition path specializes `functor_composition_path`. Direct reflexivity at the concrete coefficient did not join after coefficient composition projected to `Cat_cat`; no extra local comparison rule was added. No primitive, rewrite, unifier, public assumption or operational proof argument is introduced. Ordinary Hom object annotations remain unchanged where their classifier already agrees.

The [source-pinned recipe](production_presheaf_shape_consumer_migration.py) and [complete driver](production_presheaf_shape_consumers_review.lpfragment) reproduce the emitted source. The final cold source check passes as `20261024T194040Z-fb32b76b92404b8195802d7e608ee466`, **55.755 seconds / 203,944 KiB**, at 90 seconds / 2 GiB / `o=20,v=1024`. Subject reduction, serial execution, file limits and no-swap containment remain enabled; no compiled objects participate. All 18 owner LHS audits have zero unreviewed candidates. The subsequent emitter run reproduces the exact checked import maps, so no unchanged full rerun is needed.

Of 1,718 warning occurrences, two bodies are newly inventoried inherited overlaps: the unchanged simplex-shift arrow beta meets lax-profile or strict-profile pre/right accumulation. Both bodies already occur before the nerve coefficient change. The [focused control](production_presheaf_shape_warning_review.lpfragment) checks typed agreement by specialization of the existing generic law and retains two negative runtime-conversion observations. It passes as `20261024T194236Z-cdc7f03d5d1a456386d31550b2f35fbf`. Thus these are explicit runtime-normalization limitations under R07, not ill-sorted substitutions and not a confluence certificate. No warning-silencing rule is installed. The remaining 1,716 occurrences belong to previously reviewed contexts.

All 1,251 unchanged predecessor inputs rehash. The two adjusted parent files and their complete previously qualified reverse import closure have fresh source evidence. The [verification](production_presheaf_shape_consumers_verification.json) preserves the full parent chain, failed experiment outcomes, source hashes, warning bodies and control receipts. Coverage reaches **1,228 original LP files: 771 core/library and 457 complete reviewers**, with 1,289 qualified inputs and 5,305 positive / 738 negative assertions (including the two new audit positives/negatives).

The original limitations remain: object-only Yoneda beta does not establish eta or an equivalence; fixed algebraic 2-horn fillers are not an all-dimensional Kan result; decalage does not supply the deferred varying-HFiber assembly; recursive face actions retain their selected histories. Remaining: 20 original core/library files, 139 reviewers, five terminal Homd runtime obligations, R07/R12 and production promotion/final qualification.
