# Sigma sections: preserve the higher mapping profile

Date: 2026-10-26
Status: reviewed native correction installed; production core and focused consumers pass; affected frontend adaptation and final integration remain open
Parent: [foundations goal](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Application: [native nerve continuation](EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md)
Baseline: `81157237`, core SHA-256 `70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e`
Evidence: [profile audit](../emdash2/audits/pi_sigma_section_profile/README.md)

## Reason for this correction

The native section reconstruction exposed a retained uncurrying identification:

```text
Pi_cat(Sigma_cat(R), Sigma_proj1_pullback_catd(R,D)) ≐ Functord_cat(R,D).
```

With the current `Cat_cart` coefficients, displayed modifications have strict
fibre components. General transformations between the Sigma sections have a
broader profile. The finite audit gives 38 strict and 47 lax transformations
between the same ten walking-arrow functors, and a representable-family
extension exhibits the same missing fibre naturality. This rules out the
unrestricted canonical whole-category identification under the intended
semantics. It does not refute the forward uncurrying functor or the native
nerve comparison.

The identification predates the migration: the old coefficient was `Cat_cat`
and `tdapp0_fapp0` returned an ordinary `Transf`. The migration changed the
coefficient to `Cat_cart` and the component to `StrictTransfor`, while retaining
the old whole-category/object/next-Hom identifications. This is a local
profile correction, not a new strict-versus-lax default decision.

## Selected interface

Retain the existing whole forward functor and its computational ladder:

```text
sigma_functord_sec_func(R,D)
  : Functord_cat(R,D) → Pi_cat(Sigma_cat(R), Sigma_proj1_pullback_catd(R,D)).
```

Retire the unrestricted category comparison, object-classifier fold and
next-Hom fold that identify the two sides. Section morphisms keep their Sigma
base. A caller that has a displayed map uses `sigma_functord_sec` explicitly.
The ordinary defaults, lax base comparisons of FF, Cartesian family
coefficients, dualities and identity/relative Homd interface remain as selected.

## Work and acceptance

| Stage | Required work | Evidence / remaining boundary |
| --- | --- | --- |
| SP-0 | Check the finite profile witness and inventory the exact inherited clauses | Finite strict 2-category laws and lax coherence pass; source history confirms the coefficient change. No Empty derivation or global consistency claim. |
| SP-1 | Correct the owning core in isolation | Three broad identifications removed; path induction returns the existing forward section constructor; its reflexive proof is simplified and the obsolete comparison removed. Full core passes with subject reduction. |
| SP-2 | Preserve actual consumers and reject implicit retyping | Projection, recursive Sigma-Hom and transitivity reviewers pass; whole forward Hom action remains; implicit category/carrier retyping is rejected. The previously failing generic section identity view now passes. |
| SP-3 | Replay the current native consumer | The common totalization prefix passes with the corrected core, a plain typed identity view and no added section-identity comparison. The native inverse remains unresolved. |
| SP-4 | Qualify central and affected library/reviewer scopes | Complete central/groupoidal gate passes in 537.190s / 2,550,112 KiB under 900s/4 GiB. Central assertions remain 2,441 (2,158 positive/283 negative). The two earlier failures and all focused repairs are retained. |
| SP-5 | Integrate the qualified native correction and its consumers | Four native files exactly match the checked outputs; fresh core/focused consumers, registry, LHS audit, catalog, TOC and report headers pass. All 141 original central source/package inputs rehash. Frontend adaptation remains required; old pins and deferred final-integration obligations are retained. |
| SP-5F | Adapt the affected frontend semantics, separately from native NF-1 | An incomplete 18-file candidate is preserved with partial 13-pass/1-skip evidence. Finish explicit forward construction, actual chain/PathInd consumers, conformance and aggregate qualification when resuming this integration task. It is not a prerequisite of the native inverse. Requalify source pins only after semantic review. |
| SP-6 | Update the affected exposition and later resume the native inverse | Clarification and installed-source status complete in book 0.10.2-dev / overview 0.4.2-dev, with owning checks and visual review. Frontend/final integration and native reconstruction remain open. |

The direct lexical inventory names the core, central checks, cubical square
total, structured groupoidal J and path-induction transitivity. The cubical
owner already uses the forward constructor. This is a starting inventory;
the central import closure and actual failed consumers decide any additional
scope.

The central test changes have specific meanings: unqualified whole-category
and carrier identifications become rejection controls; the section Hom keeps
its Sigma base; path-induction values use the explicit forward constructor.
These negatives do not claim that every guarded special case lacks an
equivalence. Any stronger special-case comparison needs its own profile and
actual maps. Existing leaf transport and composition observations are retained.

The completed [warning review](../emdash2/audits/pi_sigma_section_profile/warning_comparison.json)
finds four removed critical-pair warnings and no added rule families. The
native replay has the same four-warning reduction. Neither count is a
confluence theorem. Exact source assembly for every retained replay mode is
verified independently of running another checker.

The [targeted prose inventory](../emdash2/audits/pi_sigma_section_profile/prose_inventory.json)
finds that the article's `(y,p)` section-evaluation route already agrees with
the corrected interface. The current manuscript update clarifies the higher
profile and explicit forward constructor, and replaces the legacy whole
equality as the Foundations report's expository contract. The subsequent native
installation is recorded separately from frontend/final integration. No broad
chapter redesign is indicated.

## Boundaries

- Native integration is recorded in [the exact source/gate record](../emdash2/audits/pi_sigma_section_profile/integration.json).
  Earlier audit results retain their original source pins; historical replay
  explicitly uses `--source-revision 81157237`. No frontend or aggregate
  qualification is inferred from the native installation.
- Keep source-generation and native inverse laws distinct. This correction
  supplies neither `s_U ≐ τ` nor `Observe ∘ Realize ≐ id`.
- Do not introduce an inverse to forward uncurrying on all higher cells, a new
  weak-category universe, global strictness for transformations, or operational
  equality-proof arguments.
- The earlier book/article drafts remain historical snapshots. Their limited
  uncurrying-profile update is complete in the [refreshed local artifacts](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md#refreshed-local-artifacts);
  no publication has occurred.
- Resource limits remain explicit, serialized and without swap. Broad health
  optimization and unrelated frontend work remain deferred.

The previous goal turn completed the prioritized book/article revision and is
classified as progress. This continuation applies the qualified native fix.
The frontend inventory is a concrete consequence of the removed native rules,
not authorization for unrelated frontend redesign. Its initial scale check
passes four tests with one live-acquisition test skipped, but still compiles
the old encoded rule; that result is explicitly insufficient for this profile.
