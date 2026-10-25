# Frontend admitted-family views and Sigma base change

Date: 2026-10-25. Status: focused implementation qualified; displayed
products, varying-base Pi and Homd integration remain open.

The rich surface view of `Obj(Catd_cat K)` now has target `Cat_cart`, matching
the native family classifier. The shared coefficient helper constructs a
reference to the existing normal LF declaration `dttlf_Cat_cart`; the directed
continuation owns its declaration and native backend binding. It adds neither
an intrinsic owner nor a checker conversion. Public `Cat_cat` is unchanged.

Family fibre, transport and displayed-action observations in the existing
program/surface layers now supply that coefficient. The Sigma-arrow and
pullback-total transfer uses the same correction. Its existing object/arrow
computation remains `(a,u) ↦ (F[a],u)` and `(p,α) ↦ (F[p],α)`. No path,
equality-proof argument, new native owner or unification rule is introduced.

Validation:

- 55 focused/boundary tests pass, including closed sections, fibre maps,
  heterogeneous transport, actual Sigma object/arrow computation, the
  comprehension demo, release policy, and wrong-family/base controls.
- Two native checks pass at unchanged 60-second/2GiB limits. One checks the
  **actual emitted** family/section/transport terms. The other checks Sigma
  pullback object and canonical arrow computation. Each takes about 33s.
- Typecheck and changed-file lint pass. Only the reviewed comprehension
  transfer's source pin is refreshed.

The first native attempt is retained as a failed attempt: the emitted-term
test omitted inherited serializer references, and the other check timed out
while importing the core. The serializer test now composes references from
the complete prerequisite chain and rejects any leaked internal names. The
unchanged-limit native retry passes; no resource policy change is made from
that isolated timeout. [Verification](foundation_frontend_family_verification.json)
retains the exact source hashes and receipts.

## Next native dependency

Displayed products must use `Product_cat_coeff_func`, whose type is
`Functor Cat_cart (Functor_cart_cat Cat_cart Cat_cart)`, and its corresponding
partial owner. The public product constructor is a different whole profile.
Review the existing product transfer against the native Cartesian action:
the coefficient's first action is a strict transformation internally, with
its ordinary component exposed through the existing `strict_transfor` view.
Do not relabel the old public-Cat whole action or collapse mapping categories.
The family remains the existing transparent uncurry/product-pair composite;
no new `Product_catd` head or parallel product theory is required.

The [frontend plan](../../../docs/EMDASH_FOUNDATIONS_FRONTEND_MIGRATION_PLAN.md)
keeps those consumers, varying-base Pi, and the corrected whole Homd ladder
as required continuation. The complete TypeScript gate is not yet green.
