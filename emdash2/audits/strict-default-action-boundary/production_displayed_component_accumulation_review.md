# Displayed component accumulation

Date: 2026-10-20
Predecessor: `880acb5b356c6432511a3dfbf597f20637c21b6a`
Status: qualified in staged LP; production promotion remains open

The [rules](production_displayed_component_accumulation.lpfragment) restore
the already selected pre/right law after component evaluation has projected
to its native displayed head. The [verification record](production_displayed_component_accumulation_verification.json)
retains exact inputs, focused variants, resource profiles and results.

## Existing law and missing projection order

Let F be evaluation at z on displayed maps, and let ε : F ⇒ G retain the
default conventional-lax profile. For composable modifications f and g,
the pre/right action computes as

```text
ε[f] ∘ F[g] → ε[f ∘ g].
ε[GG] ∘ F[g] → ε[g].
```

The generic owner already implements both equations. Evaluating F[g] first
exposes `tdapp0_fapp0`, so the generic `fapp1_fapp0` pattern is no longer
present. The correction instantiates those same cuts at the native component
owner. No new primitive, semantic definition, unification rule or strictness
assumption is introduced. The whole pre/right operation remains at its
existing generic owner; the two added rules join its capped observations.

The outer codomain argument B is retained exactly as in the generic rule.
Other reconstructible composition endpoints and component-family slots use
underscores. All actual maps, modifications and the base point survive on
the right. The post/left naturality comparison remains non-strict.

## Profile and variant review

The all-wildcard outer composition category passes the focused observations.
Repeating actual B preserves the original generic rule's category dependency.
A further attempt to require a literal `Functor_cart_cat` head fails the
product-valued case: its category reduces to a product presentation before
the cut. That guard is rejected. There is no duplicate product rule and no
change to the product classifier.

The pre-existing `precomposition_point_path` provides a proof-time reading
through the stable precomposition owner. It does not itself restore this
runtime component projection order, so no additional path or unifier is used
to replace the failed conversion observations.

## Qualification boundary

The three original R04 statements become positive assertions, with their
original hypotheses and endpoints. The two nearby post/left mirrors remain
negative controls. The full displayed-transport block changes from 37/8 to
40/5 positive/negative assertions; it retains all 45 statements.

The source-coverage inventory still accounts for all 2440 central assertions
except the same five terminal positives, and retains all original diagnostic
declarations. The full source has 2162 positive and 278 negative assertions.
Selected driver coverage is distinct from original all-import execution.

Fresh core/Homd, combined and library runs pass with subject reduction:
287/85, 2180/286 and 178/27 positive/negative assertions respectively. The
combined run takes 196.263 seconds and 6648.6 MiB under the retained
300-second/7-GiB profile. This is no performance-improvement claim.

The new warning inventory contains 17 added core, 20 combined and 25 library
bodies, with none removed. They concern generic category-composition views,
identity/component projection orders, intrinsic displayed-composite action,
pointwise inverse projections, sheaf composition and library odd/even
duality views. The exact body hashes, source logs and checked consumer
boundaries are recorded in the verification artifact. Symbolic overlaps
remain explicit; passing the consumed cases is not a global confluence claim.
No terminal normalization rule from the previous rejected experiment is
included. R01–R03, the other normalization/resource work and production
qualification remain open.
