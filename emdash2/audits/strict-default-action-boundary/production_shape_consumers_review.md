# Original cubical and Gray shape-consumer migration

Date: 2026-10-24
Status: qualified non-library continuation; production promotion remains pending
Predecessor: `e70ff0a8`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

This follows the [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md). It migrates existing definitions and their complete original reviewers. It does not resume the paused nerve-equivalence goal or claim new monoidal coherence.

## Scope and changes

The selected dependency closure has fifteen owners and fourteen complete reviewers: finite-arrow-tail truncation, cubical-square pasting and functor action, readable pseudo-functor data, cubical levels, semicubical face codes/action/frames, and the existing recursive Gray-cube observation with its dimension-two interchanger reading.

The original 146 declarations become 144 because two redundant strict-object declarations are retired: `gray_transf_graph_is_strict` and `strict_gray_transf_graph`. Every production caller lies in this closure and now uses the existing whole `gray_transf_graph_func`. The import facade remains. Ordinary `Functor` replaces retired `StrictFunctor` spellings and views; the genuinely lax transformation profile is retained.

One existing proof body changes: `readable_pseudo_post_source_path` now composes its existing stable-action comparison, the generic default functor-composition path, and the reverse stable postcomposition view. This resolves the changed intrinsic endpoint presentation without a new unifier, primitive, helper declaration or caller-supplied proof.

The actual selected pseudo-inverse data are preserved. The declarations of `readable_pseudo_post_cell`, `IsPseudoFunctor`, `pseudo_compositor_equiv`, `pseudo_pre_inverse`, `identity_is_pseudo` and `comp_is_pseudo` are byte-identical to their original declarations. The supplied identity/composition properties retain their status; no canonical inverse replaces the selected one.

The old named `semicubical_nerve_func` composition rule is subsumed by the strict-functor default. The complete original reviewer passes without it, so it is removed. No new comparison rule is introduced. The original 114 positive/twelve negative assertions become 115 positive/eleven negative only because the obsolete opaque strict-wrapper barrier now computes. The other negatives, including distinct faces, dimension rejection and the non-runtime recursive face-action comparison, remain.

## Preserved boundaries

The Gray-cube construction remains an object-level Nat-recursive observation with the original canonical level-shift path. This migration does not supply a whole decoder, inverse decoder, mapping-category equivalence, tensor parameter action, zero-dimensional tensor unit, associator, permutation, connection or Kan result. Existing whole square/graph action and noninvertible interchanger observations are preserved. Potential later redesign of the object decoder is outside this tranche.

## Validation

| Scope | Receipt | Result |
| --- | --- | --- |
| Untouched originals over the current foundations | `20261024T174639Z-b9791e302ed24a7e9f6f8c53302bc9d2` | Stops at the changed readable pseudo-source endpoint comparison. |
| Existing endpoint paths composed | `20261024T175214Z-ce6d814663a54297acacd52b15102d8f` | Passes that owner; reaches the retired `StrictFunctor` name. |
| Complete wrapper-migrated group | `20261024T175849Z-7e11755324bb438fb4837c39c4e92071` | Passes all 29 files. |
| Complete group without the redundant named composition rule | `20261024T180218Z-041c28f607294ed1b714c74969aca6a0` | Passes all original assertions. |
| Final emitted original consumer group | `20261024T181618Z-2620d73b9240446789f56071167de4e5` | Cold pass, 50.033s / 197,704 KiB, 124 positives/13 negatives including inherited inputs. |
| Warning typing-boundary controls | `20261024T182417Z-8ef781a919fd457a91660d1e80a438f5` | Cold pass; three additional sort negatives reject at the intended checks. |

All checks use subject reduction, 90s / 2 GiB, `o=20,v=1024`, the existing serial/file/no-swap guards and the recorded isolated checker pin. The final emitted bytes match the source-pinned recipe; malformed source pins are rejected. All fifteen owner rule audits report zero unreviewed generic inferred-slot candidates. No compiled objects participate in qualification.

Seven additional warning bodies arise at `id SemiCubePlus_cat n ↪ cube_face_identity n`. Their printed generic overlaps use `Cat_cart_include` or an identity functor as a natural-number dimension, or a dimension as a fixed-whiskering functor. The [typing-boundary controls](production_shape_warning_sort_controls.lpfragment) reject those generic substitutions. Original well-typed identity/composition and dimension controls pass. The full bodies and assessments are retained in the [verification](production_shape_consumers_verification.json). No extra rule is installed to silence the warnings; this review does not establish global confluence, and R07 remains open.

## Qualification and continuation

Every one of the predecessor's 1,149 qualified inputs rehashes unchanged. The predecessor's complete cold/completed-source evidence remains referenced by its verification hash; the new source closure and sort controls check fresh. No earlier owner is modified. The newly imported constructor rules are confined to heads from that new closure; the redundant named rule is removed.

The resulting record covers 1,125 original LP sources (720 core/library and 405 complete reviewers), 1,180 qualified inputs, and 4,841 positive/705 negative assertions. Future continuation must retain the whole qualified-input map and the parent verification link, not substitute one representative receipt.

Remaining: 71 original core/library files and 191 reviewers, five terminal Homd runtime obligations, warning/normalization/toolchain usability and production promotion. Unrelated work remains excluded from the checkpoint.
