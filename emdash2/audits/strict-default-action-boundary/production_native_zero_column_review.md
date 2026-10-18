# Native zero-column universality and mate observations

Date: 2026-10-18 (UTC)
Predecessors: implementation `6d2b3771`, normalization review `0c180e48`
Status: staged whole construction, original observations and shared regressions checked; production migration incomplete
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_native_zero_column_verification.json)

## Retained whole construction

The two native terminal/initial family-presentation evidence definitions reuse
the existing ordinary modification evidence, native arrow-family comparison
and native reconstruction. Their actual J, F, e, h, forward maps and chosen
inverse maps remain. They are definitions returning IsoEvidence, not new
structural witnesses or runtime inverse laws. Their ordinary counterparts
remain available in the same owner.

The original four zero-column/mate definitions retain their composition
bodies with the native diagram profile. For the actual chosen P and Q, write
Z_P and Z_Q for the original zero columns, J for the terminal-arrow embedding,
I for the initial-arrow embedding, and ev_s/ev_t for native evaluation. The
derived comparisons and mate inputs have the original forms:

```text
e_Q : Z_Q ≅ J ∘ ev_s          e_P : Z_P ≅ I ∘ ev_t
unit input   = transpose(unit) ∘ e_Q⁻¹
counit input = e_P ∘ transpose(counit)
```

All retain the original OneCat(C) hypothesis. No ordinary profile on the
parameter category is added. The initial-object inputs use TotalOp_cat,
consistent with the already migrated native K/Q and initial-arrow owners.

## Endpoint types and derived observations

The fixed evaluations in diagram_oplax_family_transf,
diagram_oplax_family_map_at, its composition path and native reconstruction
now expose the canonical raw-composition endpoints. Their defining bodies
are unchanged. Substituting an actual zero column can therefore expose the
same endpoint computation as its canonical column view. Expanding the whole
shape-action body into another prewhiskering expression was rejected earlier:
it lost the existing double-exchange computation.

Eight native presentation endpoint paths and the eight zero-column endpoint
paths are derived from the actual component computations, through the existing
one_cat_modification and discreteness-reflection interface. These are ordinary
observation proofs. No equation is added to unification, and no equality proof
is a new operational argument to the construction.

The remaining mate proof required the whole source/target evaluations of a
native transposed shape map. The two new paths in
[the transpose owner](production_one_cat_oplax_transpose.lpfragment) derive
exactly those equalities under OneCat(C), using the already computing
components. They retain arbitrary B, I, F, G, h and nonidentity u. They do
not assert unrestricted exchange of two lax transformation directions.

[The mate proofs](production_zero_column_mate_paths.lpfragment) preserve the
original composition-path plus identity-endpoint outline. The extra step
uses the derived transpose endpoint path to identify the evaluated transpose
with the original whole differential. The observations are equalities of
whole transformations; their components and Hom action are then obtained
using the original reviewer projections.

## Migration failures and their corrections

The initial exact-text replacement missed two line-wrapped diagram types in
the mate owner and ten in its reviewer. A guarded whitespace-aware
replacement repairs those inputs; identifying ordinary and native diagram
categories would have hidden a migration error.

Once the declarations matched, the original mate proof still compared an
expanded evaluated transpose with the original differential. The derived
whole endpoint paths close this step without a new rewrite or unifier.
Finally, the reviewer itself still quantified ordinary diagrams and maps.
Its six object binders now use the native category; its two map binders use
the native Hom. The underlying component and arrow observations use the
existing odd-dual encoding and reversed source/target order. All eight
original whole/component/Hom/arrow claims remain.

The twelve original selected terminal/initial presentation and zero-column
observations also use the native profile throughout. The original selected
maps are retained, and the ordinary evidence definitions remain checked as
dependencies. No observation is replaced by a test of an unrelated supplied
comparison.

## Validation and remaining scope

The focused twelve-observation reviewer passes, including both new generic
transpose endpoint proofs. The three shared accessor fragments retain their
defining bodies byte-for-byte. The complete core/Homd regression's exact
287-positive/85-negative input snapshot is unchanged. Nine affected owners
pass the inferred-slot audit; this tranche adds no runtime/unification rule
or primitive declaration.

The combined final driver passes 139 positive and 27 negative observations,
including the original eight zero-column, twelve selected-presentation,
native/ordinary transpose, K/Q, ordinary arrow/reconstruction and native
homology whole/point reviewers. All 106 receipt input hashes match the final
emitted source. Removing an unused authoring helper changed no emitted LP.
The four original zero-column construction bodies also match the baseline
byte-for-byte after the listed profile/name substitutions.

The first combined run reached the homology comparison after the new
zero-column and transpose reviewers, then allocation-failed under the
300s/6GiB/o=10 profile. A same-source o=5 retry failed at the same boundary.
Both failed receipts are retained. After checking 21922 MiB available host
memory, the standing resource authorization was used for an explicit
300s/8GiB/o=10 check of this target. It passes in 126.628s at 6147.8 MiB peak
child RSS. Subject reduction, warnings, serial execution, file/core limits
and no-swap containment remain enabled; defaults are unchanged. This is
measured validation headroom, not a normalization or performance fix.

The full warning multiset has 2927 bodies, versus 2923 in the preceding native
transpose closure: four added, none removed. They are existing odd/even
functor-composition overlaps with the two component inverse-cancellation
rules of Adjunction_hom_prof_comparison. The additional import combination
exposes these peaks; the shared source rule inventory is unchanged. Their
bodies and hashes are retained in the verification. General convergence of
these cancellation/duality paths remains part of the recorded normalization
review, not an outcome of the positive consumer checks. No patch rule was
added to suppress these warnings.

Remaining library migration, redundant strict wrappers, production promotion,
normalization/performance qualification and final catalogue/health/CI/source-pin
review remain required. The separate application goal stays paused. Replay
the authoring script followed by native_zero_column_regression_controls.lp;
use the explicit 300s/8GiB/o=10 profile recorded above. Qualification of this
staged slice does not establish the full migration.
