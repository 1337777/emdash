# Ordinary adjunction introduction: coefficient migration

Date: 2026-10-17
Predecessor: `fddadd33`
Status: complete original owner and reviewer qualified in non-library staging; remaining migration and promotion open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The original one_cat_adjunction_from_hom_comparison remains its existing
structural constructor. Its input is the same whole ProfComparison, with
the original OneCat(A/B) premises, forward map and selected inverse. The
seven scoped proof-time comparisons retain the native mate and unit/counit
runtime heads. This migration does not relabel that structural introduction
as a theorem derived from the earlier opaque Adjunction classifier.

All 20 Cat_cat tags in the owner and six in its reviewer occur at
profunctor-component or evaluated-inverse coefficient positions. They become
Cat_cart, matching the actual profunctors and the previously qualified
evaluation paths. The recipe matches those product-base coefficient slots
explicitly and checks their counts. The original whole unit/counit agreement
proofs and reviewer observations all pass: 25 positive and eight negative assertions.

The initial unmodified-owner baseline imported the migrated Hom-comparison
module successfully, then failed allocation at the 4GiB cap before checking
the owner declarations. That is a resource result, not a mathematical
rejection. The corrected-source trial uses o=5 instead of o=20 at the same
600s/4GiB limits, with per-command timing, subject reduction and the normal
serial/file/no-swap safeguards. No host power setting or global default is
changed.

The o=5 trial reached the first actual comparison in 539.8s. Its diagnostic
distinguishes the native mate, a defiso_fmap image through Cat_cart_include,
from the raw Cartesian evaluated component. Each transpose/untranspose
proof now first uses the existing defiso_fmap_to/from_path, then follows the
original input-agreement and profunctor-component paths. Both selected maps
and the original i survive. No runtime decoder or new comparison rule is
introduced. The focused prefix retains the original constructor and seven
comparison rules while checking these two paths before the larger consumer.

Both repaired mate paths pass the focused owner-prefix check. The complete
original reviewer also passes, including whole unit/counit agreement, whole
and point inverse cancellation, higher action and the original negative
controls. The [verification](production_adjunction_introduction_verification.json)
records exact checked inputs and receipts. Final warning bodies match the
preceding completed import/owner prefix exactly (2650); this is not a
confluence certificate. The full check took 91.2s at 600s/4GiB/o=5, while the
focused views took 25.3s at 300s/4GiB/o=20. The normal defaults are unchanged.

The owning-file LHS audit has zero unreviewed candidates. The new source has
no additional rewrite or unification rules; the original comparison rules
are retained. Replay the generator and examples/one_cat_adjunction_introduction.lp
under the recorded profile after coefficient or mate/evaluation changes.
Next resume the presheaf/direct-cover route at the existing Yoneda and
canonical Sigma-family interfaces. Preserve raw presheaf maps and review
the actual slice variance before changing its duality presentation. Remaining
library migration, strict-wrapper retirement, production promotion and final
qualification stay open.
