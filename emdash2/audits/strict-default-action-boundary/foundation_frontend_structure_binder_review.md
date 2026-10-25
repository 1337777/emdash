# Displayed product structure and binder composition

Date: 2026-10-25. Status: focused/native slice qualified; higher displayed
transformation, Pi/Homd and final integration remain open.

The six existing displayed-structure declarations and fifteen computation
clauses now use the admitted coefficient product. Whole projection action
lands in Cartesian mapping categories and uses the native
`comp_cat_con_cart_func`; the ordinary pair of already-formed functor objects
is retained where its object classifier is the required one. Point, capped
and whole projection/pairing consumers pass. Lax displayed FF across the base
is retained.

The public full-action observation now reports the actual Cartesian target,
rather than an ordinary lax mapping category with the same objects. This is
a type correction, not an additional strictness witness or runtime category
identification.

The following binder layer keeps its existing two declarations and Sigma/Pi
proof comparison. Its displayed-composition component rule uses `Cat_cart`.
The native coefficient composition projection is added at this first consumer:

```text
comp_fapp0(Cat_cart,A,B,C,G,F)
  → comp_fapp0(Cat_cat,A,B,C,G,F).
```

That is composition of the same strict functor objects, not equality of the
two universes or of their higher Homs. It lets the retained ordinary functor
application rule compute the composition point. The binder now has three
runtime clauses; no generic LF engine or native mathematical rule changes.

Validation:20 structure/binder/demo tests pass;27 contract/metadata tests pass.
Three native tests pass at60s/2GiB, including the **actual emitted whole
projection action** and its capped observation, pairing, point/beta/raw-reindex
controls, and binder identity/composition/classifier compatibility. Typecheck
and changed-file lint pass. Direct/nested classifier compatibility stays
proof-time; the raw reindex non-conversion control is preserved.
[Verification](foundation_frontend_structure_binder_verification.json)
records exact inputs and receipts. This does not qualify the remaining
displayed-transformation or whole frontend scope.

Next, follow the native `tdapp0_func`/`tdapp0_fapp0` declarations: their fibre
carrier is the Cartesian Hom/`StrictTransfor`, with an ordinary observation
through the already-transferred `strict_transfor` view when needed. Do not
redeclare that native carrier as an arbitrary lax transformation, or make
all displayed FF strict across the base. Continue through its actual
consumers under the [frontend plan](../../../docs/EMDASH_FOUNDATIONS_FRONTEND_MIGRATION_PLAN.md).
