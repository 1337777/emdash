# Displayed evaluation frontend migration

Date: 2026-10-25. Focused/native qualification complete; higher frontend integration remains.

The native `Functor_catd(A,B)` fibre is
`Functor_cart_cat(A[k],B[k])`. Its family coefficient and the transparent
displayed product use `Cat_cart` and `Product_cat_coeff_func`; Cartesian
curry/uncurry signatures are retained. The object-level functor inputs stay
the same, while the higher mapping category remains distinct from ordinary
`Functor_cat`.

The native `Eval_funcd` has a strict transformation carrier across the base.
Its transferred signature now preserves that carrier. The existing frontend
lowering automatically observes it through `strict_transfor` before composing
with ordinary displayed maps. No caller supplies a strictness witness and
no blanket strictness is imposed on displayed maps FF. The terminal displayed
map keeps its original ordinary interface.

The native conformance checks both object consumers, generic higher action
with its actual Cartesian Hom, variance non-collapse, and a serialized term
produced by the TypeScript contextual evaluator. It passes at60s/2GiB with
warnings and subject reduction. The old ordinary-fibre comparison in the demo
and tests is corrected to the native Cartesian classifier; a separate negative
comparison ensures the ordinary classifier has not been collapsed into it.
Only this reviewed profile's source pin is updated. Eleven focused tests,
typecheck and changed-file lint pass. Inferred family/view slots in the
component pattern use native wildcards with typed checking witnesses, keeping
the expanded product expression out of runtime matching. The final focused
run rechecks that pattern cleanup.

[Verification](foundation_frontend_display_eval_verification.json) records
inputs and receipts. The scope remains three prerequisite declarations, two
existing evaluation/terminal owners and three native projection rules.
No native mathematical rule or generic engine change occurs in this slice.
The complete TypeScript gate and the remaining displayed/mixed/Homd migration
remain open.
