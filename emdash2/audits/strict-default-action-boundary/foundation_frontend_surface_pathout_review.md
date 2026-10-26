# Ambient Hom views and exact PathOut foundation migration

Date: 2026-10-25. This follows checkpoint `cb7a37ad`. The active Lambdapi
source is unchanged. The [acquisition](foundation_frontend_surface_pathout_acquisition.json)
and [verification record](foundation_frontend_surface_pathout_verification.json)
own the current source and validation boundary.

## Existing interfaces and source bodies

The elementary surface's internal Hom has an ambient Catd_cat result. Its
native bindings therefore use the existing defined `hom_int_view` and
`hom_con_int_view`, whose signatures match that interface. The stronger
`hom_int` / `hom_con_int` free owners remain unchanged in the native transfer.
Both partial projection routes and the reversed-variance rejection are checked
against Lambdapi. Probe serialization accepts explicit imported free-symbol
bindings and rejects a probe declaration shadowing one; it does not silently
replace arbitrary user variables. The dependent demo now uses Cat_cart at its
family/telescope arguments.

PathOut reuses the shared `hom_postcomp_func` and `hom_precomp_along_func`
prerequisites. Represented source actions have their actual Cartesian carriers;
ordinary component observations use the existing strict_transfor view.
The representable family retains the ambient native Hom view. PathOut's whole
contravariant family instead uses the native strong Hom followed by
`Sigma_coeff_func`, landing in Cat_cart. The ordinary Sigma_func remains a
separate existing owner.

All nine PathOut library definitions remain checked definitions. The closure
has four opaque prerequisites, the checked Hom view, fifteen runtime clauses
and two proof comparisons. The Native body/projection consumers retain the
reflexive point, canonical arrow, source transport and wrong-endpoint controls.
The source and policy metadata are updated only for this qualified foundation
scope. The old proposal/review is retained as history. Fixed-source and
internalized path induction and transitivity still stop at their historical
predecessor-review boundary; this checkpoint does not qualify them.

## Why declaration proof typing is needed

Replacing the Hom view's codomain by the ordinary Functor_cat presentation
made runtime-only body checking pass, but the changed body was not runtime-
convertible to the native definition (waves316/318). That attempted spelling
is not adopted. The implementation keeps the exact native Catd_cat codomain.
Its inclusion argument requires the existing proof-only category comparison.

The generic compiler now allows a specifically named definition to use a
compiled proof profile, with exact expected rule IDs. To check an explicit LF
lambda telescope, the checker validates binder annotations and modes, opens
its parameters as fresh opaque assumptions, and uses the existing closed
proof-aware checker. It returns the original body unchanged. Parameter names
avoid both environment and syntax names and do not escape into the stored
environment or term. The allowance cannot persist into later definitions.

This adds no categorical branch to the checker and no mathematical or runtime
rule. Only hom_int_view selects this option here, using
`categorical.dependent-target.category-presentation`. Unused or unexpected
proof allowances fail closed. Tests cover dependent parameters, wrong values
and domains, binder modes, foreign contexts, comparison-budget exhaustion,
unchanged bodies, non-conversion at runtime and absence of allowance leakage.
The existing generic declaration/runtime/proof/visibility tests also pass.

## Validation and remaining work

The native check includes all prerequisite/library signatures, each stored
body, the original six PathOut observations and the represented-source
proof-time comparison. Runtime assertions and proof-time assertions remain
distinct: the latter is checked through the existing equality classifier,
not relabelled as runtime conversion. Native typechecks retain warnings and
subject reduction under the supported checker and explicit 60s/2GiB profile.


The checkpoint replay passes 25 focused cases (one native opt-in is covered by
the separate native receipt). The full `check:ts` attempt completed workspace,
registration, typecheck and lint, then stopped without a terminal test result.
On continuation its process handle was missing and no worker remained; its
last log heartbeat was at450.4s with no completed test events. The exit reason
is unknown. This is an inconclusive integration attempt, not a passing gate or
a recorded900-second timeout. The older aggregate failure inventory remains
applicable except where the focused migration above supplies new evidence.

The complete TypeScript integration attempt and the remaining failure inventory
are recorded separately from these focused results. Full Homd P-index endpoint
computation, downstream profile/audit migration, production health and final
integration remain required. Book/article and legacy nerves remain later stages.
