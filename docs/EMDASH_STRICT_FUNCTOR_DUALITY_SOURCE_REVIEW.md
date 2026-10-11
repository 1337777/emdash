# Strict-default and duality migration: source boundary

Date: 2026-10-11
Status: SF-0 owner audit with a non-library SF-1 implementation pilot
Authority: [living plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md),
active v3.2 source and [Lambdapi SOP](../emdash2/AGENTS.md).

Continuation qualification: the
[evaluation-profile audit](EMDASH_STRICT_FUNCTOR_EVALUATION_PROFILE_REVIEW.md)
constructs naturality equalities from the capped strictness rule and legacy
Cartesian evaluation. The local conversion negatives below are insufficient
to claim preservation of general lax transfors under blanket promotion.
The required next owner change is the Cartesian/Gray coefficient distinction.

## Source and qualification boundary

This work starts from main `f8af1fca472657ff1598c639eb29c0566e7b2ec0` in
`goal/strict-functor-duality-v3.2`. It keeps the current v3.2 owners and
public names. There is no separately maintained strict copy of the library.
At launch, `checks.json` contains 792 core and 596 reviewer files. The final
migration must account for their affected dependency closure; excluding a
broken dependent is not qualification of the repository.

The prior action-profile integration `8ea6c86b` supplies selective history,
not a revert target. Its normalization, intrinsic-action, resource and
consumer fixes remain useful. The source owner hashes are pinned in the
[first audit](../emdash2/audits/strict-default-action-boundary/README.md).
The research donor `cc08dbff` supplies the consolidated plan only; no scratch
tree or older strict-v1 implementation was imported.

TypeScript source pins remain review signals. Changing a pin will not count
as transferring a changed owner or qualifying its higher action. The eventual
consumer sweep must explicitly report the existing bounded profiles and
affected tests; it does not authorize a new bulk-transfer project.

## Owner decisions

| Owner | Current source contract | Selected treatment |
| --- | --- | --- |
| `Functor_cat`, `Functor`, `fapp0`, `fapp1_func`, `fapp1_fapp0` in the nucleus | Normal identity; arbitrary composition retains intrinsic laxity | Keep names/carriers and restore strict composition at all native action levels. |
| `hom_int`, `hom_con_int`, represented post/pre action | Stable blended F owners; arbitrary-F accumulation partly retired | Keep both heads and F; adapt strict laws and final duality signatures together. |
| `tapp*`, `fdapp*`, `tdapp*` | Whole action with extracted directed comparisons | Retain the non-strict transfor profiles. Strict component functors do not imply strict naturality. |
| `functord_laxity_transf`, `fapp1_compositor` | Defined from `fdapp1_comma_projection_transf` and identity-transfor action | Preserve the extraction. Strict-default identities belong at its actual action owner, not at a newly supplied witness. |
| `StrictFunctor`, `strict_functor`, `make_strict_functor` in `gray_profiles` | Opaque classified strict views of ambient maps | Migrate consumers, derive old properties where useful, then retire redundant object wrappers. No parallel strict action API. |
| `StrictFunctor_cat` versus `GrayHom_lax` | Same strict objects, different transfor profiles | Preserve the higher-profile distinction; matching object sets do not justify identifying categories. |
| `Op_cat`, `Op_func`, internal `op`, `Functor_cat_func` | Legacy mixed dimension conventions | Replace through the selected T/R/O whole-action design. The first strict-action pilot does not qualify this legacy variance. |
| `Functor_catd`, `Hom_catd`, transformation-backed `Pi_cat`, `homd_int`, `homd_` | Existing native ladder with known variance defects | Implement the selected Q-coefficient construction and retain blended FF and the direct projection ladder. |
| `Prof_cat`, `Prof_reindex`, `Companion_prof`, `Conjoint_prof` | Native profunctor owners using the old Op and endpoint convention | Adapt their corrected variance and use their existing owner relationships for the selected covariant Q convention. |

The chosen Q signature and the C2-indexed whole Homd target remain in the
living plan. Full omega coefficient/interchange and represented-lift
qualification are still required. This audit does not infer them from the
strictness of functor objects, nor restart a combined-context or primitive-Pi
architecture.

## Preserving the weaker interface without adding a prerequisite

The first pass implements the strict public default and lax transfors. A
new public `LaxFunctor`/`LaxCat` carrier is not required in this pass: the user
kept that extension at the shared-design stage. The extraction machinery
stays native and active for transfors; its former nonidentity-functor
specialization remains recoverable at the exact source pin and audit.
Future explicit lax action must have a distinct discriminator so it cannot
inherit generic strict-default rules accidentally.

No strict-to-lax or lax-to-strict coercion is added by this pilot. In
particular, weak objects must not silently become ordinary Cat objects.
The future inclusion and native weak Hom design are already recorded in
the plan; they do not delay the present migration.

## First implementation result

The [replay](../emdash2/audits/strict-default-action-boundary/README.md)
separates four requirements rather than conflating them:

1. Capped strict functor composition, including action in the next Hom.
2. Whole post/pre strict functor endpoint comparison.
3. Identity computation of the actual extracted whole compositor.
4. The post/pre projection joins after the whole comparison has already
   been evaluated.

The full-file candidate and an unchanged profile-owner consumer pass with
subject reduction enabled and ordinary resource limits. Arbitrary transfor
naturality remains non-strict in the controls. The old `IsStrictFunctor(F)`
is then derivable for an unwrapped default F; its evidence is an output,
not an operational argument. Thus the late strictness property need not be
used to define the upstream Functor carrier.

The intermediate failures concern two distinct normal-form issues: raw
composition versus the retained represented head, and whole-first versus
cap-first evaluation. The final pilot fixes the latter at the existing
semantic owners. Neither failure is evidence of a mathematical obstruction.

No candidate rule is promoted yet. The added warning families, constructor
specializations, transfor-profile consumers, ordinary Hom accumulation and
corrected coefficient signatures require the next qualification slice.
This is a computational feasibility result for the initial native strict
action, not completion of SF-0, SF-1, or the dependent-Hom milestone.
