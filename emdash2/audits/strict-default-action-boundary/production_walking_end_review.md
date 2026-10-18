# Walking-end coefficient migration

Date: 2026-10-18 (UTC)
Predecessor: `4abd18cb`
Status: complete owner, original reviewers and duplicate-rule retirement checked in staging; overall migration incomplete
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_walking_end_verification.json)

## Required coefficient correction

The isolated batch-memory diagnostic reached the previously hidden
WalkingEnd failure. The installed checker then reproduced the local failures
and checked the corrections; this migration does not depend on replacing
the installed checker.

The existing contextual eliminator still takes R, D, u and its directed
loop comparison, and returns Functord(R,D). Because R and D now land in
Cat_cart, that comparison belongs to the strict fibre-transformation Hom:

```text
sigma : StrictTransfor(R[base], D[base], D[loop] ∘ u, u ∘ R[loop]).
```

Its naturality in the fibre variable is strict. The comparison arrow remains
directed and need not be invertible; the resulting Functord is not made
strict across WalkingEnd. No additional proof parameter is introduced.
This refines the old input type to match the Hom already required by the
Cat_cart-valued output classifier; arbitrary lax fibre comparisons are not
silently admitted to that stricter Hom.
The component beta reads sigma through the existing strict_transfor
inclusion. The base beta lets the existing constructor determine its source,
coefficient and family arguments instead of retaining the old Cat_cat tag.

The constant-transformation constructor already has the required profile,
so the section and nondependent recursor bodies remain unchanged. Code and
all its observations use Cat_cart. The structured encoder keeps the original
Code Hom action and evaluates it after the existing Cartesian-to-ambient
mapping inclusion; no new evaluation primitive is declared.

## Original spiral and discrete evidence

The original path_lift_non_strict_spiral body, including its explicit kappa
and original derived step equality, is retained. Its target is the based Hom of
WalkingEnd, already known to be discrete from the existing dimension datum.
The existing one_cat_strict_transfor admission therefore supplies the
required strict fibre view, and its ordinary inclusion retains the original
component computation.

The small [discrete-to-OneCat proof](production_discrete_one_cat.lpfragment)
derives the needed property using discrete_core_homwise, its fixed-forward
equivalence and the existing native category-path view. It adds no primitive
or rewrite. The path transport is inside a derived property proof, not an
extra operational argument supplied to the recursor. No weakening of the
opaque WalkingEnd category or identification with BNat is introduced.

## Computational ownership

The named recursor composition rule is an exact instance of the restored
generic strict-functor cut and is retired. The protected recursor head and
its point/generator betas remain. The named composition theorem now uses
the generic rule. This is removal of a redundant strictness instance, not
a new comparison between different runtime presentations.

The original arbitrary-functor composition negative becomes a positive
under the selected strict default. Distinct recursor inputs, the opaque
object/Hom boundaries, and the existing generator-prefix projection-order
negatives remain. No new runtime or unification rule is added.

## Validation and remaining scope

The full source and original WalkingEnd, named-recursion and overlap
reviewers pass before duplicate-rule retirement: 64 positive and ten negative
observations including the imported profile assertions. That installed-checker
run takes 31.943s at 2307.8 MiB maximum child RSS under 300s/4GiB/o=20.
The isolated batch-memory build passes the same source and settings with
identical 2453 warning bodies, at 173.9 MiB; this is a separate runtime
diagnostic, not a new verification-toolchain selection.

The original pre-migration owner checks separately. Its WalkingEnd warning
count is twelve, compared with 32 before retirement in the migrated closure.
The added families are constructor/constant-coefficient overlaps, loop beta
versus ambient accumulation/naturality, named composition versus the newer
duality/coefficient presentations, and BNat identity overlaps with generic
cuts. Retiring the duplicate removes eleven warning bodies and adds none:
the final full count is 2442 and the WalkingEnd owner count is 21. The three
constructor/constant-coefficient and seven BNat identity overlaps remain
additional to the original owner, with one old body removed. Positive typed
consumers do not establish global confluence of these paths.

The final installed-checker run passes all 64 positive/ten negative
observations in 26.909s under the same 300s/4GiB/o=20 safeguards. Both affected
owners pass the inferred-slot audit. The accepted normalization improvement
is the exact duplicate-rule and overlap removal; single timing samples do not
establish a stable speedup. All final receipt source hashes match.

The complete core/Homd 287/85 input snapshot remains unchanged. Remaining
central imports and assertions, wrapper retirement, normalization/performance,
production promotion and final gates remain open. The next original import
is walking-circle completion/restriction. The separate application goal
remains paused.

Replay the authoring script, then walking_end_migration_controls.lp with the
installed checker at the recorded guarded profile.
