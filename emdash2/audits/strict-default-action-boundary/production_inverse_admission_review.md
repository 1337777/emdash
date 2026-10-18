# Native strictness and admission of the retained inverse maps

Date: 2026-10-18 (UTC)
Predecessor: `578a17bc`
Status: both original inverse maps admitted; Cartesian whole cancellation and locality integration remain open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_inverse_admission_verification.json)

The actual left inverse now satisfies the full native `IsStrictTransfor`
property, including agreement with its extracted post/left naturality cell.
The earlier endpoint-only result is no longer the admission boundary. The
proof uses the original whole cancellation law, the checked represented
composite, reflection through the retained equivalence, and the default
pre/right identity convention. It adds no inverse-assembly assumption.

The existing inverse-uniqueness theorem then gives a path between the two
original whole inverse choices. Transporting the proved property along that
path admits the selected right inverse as well. The defined
`pointwise_cart_left_inverse` and `pointwise_cart_right_inverse` use the
existing `make_strict_transfor` constructor. Their underlying observations
compute to the respective original maps; neither choice is replaced by the
other. The admission certificate is confined to the existing profile/proof
interface. Homd and its operational consumers acquire no equality payload.

Three proof-time comparisons support this derivation:

1. The whole canonical extraction after represented strict precomposition is
   the existing fixed-postcomposition image of the original extracted cell.
   Both modification arguments are constrained to their canonical intrinsic
   actions. This is a selected whole computation of the existing intrinsic
   composite, not a theorem inferred from scalar beta rules alone. It does
   not introduce an independent naturality cell or compute arbitrary input
   modifications.
2. Core-inclusion images are compared by congruence across endpoint
   presentations. The comparison still checks both endpoints and the actual
   path. It supplies neither reflection of arbitrary arrows into the Core
   nor an equation between distinct paths.
3. The already-selected mapped Hom square has a direct comparison between
   its two stable object-action heads. This avoids transitive unifier search
   through `Hom_fapp0` and retains the actual middle arrow.

One existing definition also needed adjustment. The arbitrary-action
`fdapp1_project_section_arrow` previously expanded an alternative target
family into its component annotations. At a composite action this obstructed
the root-first projection. It now infers those annotations from the actual
whole modification, exactly as the checked `fdapp1_int_comp_section` does.
The arbitrary modification, all output data, and the projection ladder are
retained. No new stable projection primitive or runtime rule was introduced.

The combined check verifies the native component-first computation and its
proof-time agreement with whole extraction. It rejects replacement of the
middle arrow and either intrinsic modification. The inherited core regression
also retains post/left laxness and now rejects distinct Core paths and an
arbitrary arrow substituted for a path image. It passes 276 positive and
79 negative assertions. These are projection and retention checks, not a
claim that every whole comparison is a runtime fold.

The intermediate failed checks remain execution evidence: a directly
reframed strict-cell certificate failed inside its path-image field;
inlining local lets did not solve that issue. The Core congruence comparison
resolved it. A scalar endpoint presentation required the direct mapped-Hom
square comparison, and the root-first extraction exposed the component
annotation issue above. Two control elaboration errors (an insufficiently
specified classifier argument and a reserved identifier) and an omitted
proof-module import were corrected. None is counted as a successful
negative control or a semantic impossibility result.

The inherited pointwise-to-whole assembly and its whole cancellation paths
remain their original supplied contracts. This result is derived relative
to those native contracts and the selected whole computation. It is not a
new semantic justification of arbitrary pointwise assembly, and it does not
upgrade the older literal strict-2-category diagnostic to a model of native
path-based strictness.

**Remaining consumer:** the two raw cancellation paths still live in the
ordinary mapping category. An `OmegaEquivAlong` in `Functor_cart_cat` also
requires cancellation paths for the actual classified composite and identity.
Admitting its two inverse arrows is not that whole equivalence. Next qualify
the equality/admission comparison at those actual classifier constructors,
retaining both chosen maps, then replay the original locality assembly. Do
not substitute an ordinary-category inverse law, add the rejected generic
Cartesian assembly assumption, or reopen the Homd interface design.

The complete combined admission check passes in about 34 seconds at the
reviewed 300s/4GiB/o=20 profile, with subject reduction. Its closure includes
the original inverse laws, Eq1 inverse uniqueness, native path-image action,
both represented-extraction orders and the modification-retention controls.
The core regression passes in about 26 seconds at 240s/2GiB/o=20. An earlier
2GiB extraction import exhausted its allocation cap; about 15GiB of host
memory was available before selecting the existing 4GiB import profile.
Defaults, serial execution, file limits and no-swap containment are unchanged.
Warning bodies and exact input hashes are recorded in the verification.

This remains non-library staged implementation. Remaining library migration,
redundant strict-functor-wrapper retirement, production promotion and final
catalogue/health/CI/source-pin qualification are still required.
