# Direct-cover sheafification migration and normalization repair

Date: 2026-10-18
Status: complete staged owner and original central reviewer checked with the
installed checker; remaining migration and production promotion are open.
Predecessor: `370cc759608abe6bfb6454a4f11762c9574b5a42`.
Original source: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`.

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
owns the overall scope. Exact inputs, successful and failed receipts, warning
inventories and measurements are in the [verification](production_sheafification_verification.json).
The complete original owner and diagnostic tail remain in the staged package;
production files are not promoted by this checkpoint.

## Coefficient and original interface

The central diagnostic passed the imports through cover-completion universality
and then failed subject reduction at the sheafification unit rule. The original
specialization still used Cat_cat, whereas its actual presheaves now have the
Cat_cart coefficient. The installed checker independently reproduces that error.

All 59 literal Cat_cat occurrences in this specialized owner denote that value
coefficient, including V in the generic supplied capability. They migrate to
Cat_cart. The generic arbitrary-V sheaf interface in `emdash3_2_ringed_sites.lp`
is unchanged. The original nine central assertions receive the same coefficient
adjustment; their ambient Obj(Cat_cat) observations stay unchanged.

The original whole inclusion, sheafification functor, adjunction, selected
recursor, unit/counit rules, inverse and both cancellation proofs are retained.
The comparison with the rigid Psh category remains proof-time only, as its
original negative runtime-conversion assertion requires.

## Located normalization problem

The coefficient correction alone allocation-failed at both 4 and 6 GiB. The
isolated rollback-memory patch also failed at 4 GiB, so that checker issue did
not account for this local failure. Prefix checks initially ruled out the
inclusion and its whole Hom declaration. Recording every command then located
the failure at `direct_cover_sheafification_reflector`, after the pointwise
fixed-counit equivalence and both cancellation proofs had passed.

A scoped conversion trace showed repeated comparisons between the same objects
expressed through rigid Psh versus the generic functor-category/package
projections. These comparisons descended into the reflected object's large
locality-proof fields. The trace reached the existing 64 MiB log limit; its
receipt records that diagnostic termination, not a typing result.

Changing only an earlier Hom endpoint, reusing only the named package, or
changing only the reflected object's category annotations did not resolve the
failure. Those incomplete variants were not retained as separate interfaces.

The selected correction routes the existing final observations through the
same generic package projections used by `IsSheafificationReflector`:

- `direct_cover_sheafification_counit_at` calls `sheaf_adjunction_counit_at`;
- `direct_cover_sheafification_reflected_object` applies the generic selected
  sheafify/include functors at their exact generic source presentation;
- both reuse the already-defined `direct_cover_sheafification_adjunction_data`,
  which contains the original chosen functors and adjunction; the final
  reflector/capability references use that same package.

There is no new primitive, rewrite, unifier, supplied strictness requirement or
operational equality argument. All original rules keep their bodies modulo
the coefficient substitution. All inverse choices and cancellation proofs are
unchanged. This is reuse of existing semantic projections at a concrete
consumer, not a new stable-head facade or a general foundation redesign.

## Qualification and remaining limits

The installed checker passes the full owner and all eight original positive
assertions plus their one negative, with one additional inherited positive.
The nine/one closure takes 38.492 seconds and 3065000 KiB peak child RSS under
180s/4GiB/o=20, with warnings and subject reduction. The final reflector and
capability commands each report 0.00 seconds. The matching pre-goal closure
passes in 14.319 seconds and 1103704 KiB under identical settings. Thus this
specific allocation failure is repaired; the overall import/migration cost
still exceeds the pre-goal baseline. These are single samples.

The final warning multiset is identical to the coefficient-only candidate:
2418 bodies overall, including 26 at this owner. The corresponding pre-goal
focused owner has 13. The current owner's groups are eleven identity/projection
overlaps and fifteen composition/action/inverse overlaps; they arise with the
existing migrated core rules. They are inventoried in the verification, not
claimed as a global confluence certificate. The final projection correction
adds no overlap. The owner LHS audit reports zero unreviewed slots; its actual
rule patterns are unchanged apart from the coefficient discriminator.

The exact core/Homd 287/85 and previous interchange snapshots remain unchanged
and are rehashed before carrying their green evidence. No unrelated aggregate
is rerun. Replay after owner/dependency/checker changes by running
`production_owner_migration.py`, then the guarded source runner with the emitted
package as `--package-root`, targeting `direct_cover_sheafification_controls.lp`.
Use the recorded 180s/4096MiB/o=20 profile with `--record-time --too-long=0`,
warnings and subject reduction. The baseline package emits the corresponding
original reviewer for a matched comparison.

Next continue the original import order at groupoidification composition and
interval recovery, then the monad/product/pullback imports and central
observations. Wrapper retirement, remaining normalization/performance review,
production promotion and final catalogue/health/CI/source-pin gates remain
required. The separate application goal stays paused.
