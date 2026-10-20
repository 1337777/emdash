# Final strict-functor wrapper retirement

Date: 2026-10-20
Status: staged implementation; production promotion remains separate.
Predecessor: `566598db`.

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
owns the migration scope. The preceding transparent-alias stage established
the whole mapping profiles and restored required Hom computation at its native
owners. This step removes the compatibility layer from the final emitted LP.
The [verification](production_strict_wrapper_finish_verification.json) records
exact inputs, receipts, source coverage and name dispositions.

## Removed interfaces and preserved data

The replay removes 39 legacy declarations and migrates their active references:

- `StrictFunctor`, its category, make/view/underlying operations and inclusion
  become ordinary `Functor`, `Functor_cat` and the actual input map.
- Named strict identity, constant, Path and profunctor-map wrappers become the
  existing ordinary constructors. Their now-unused admission certificates are
  removed.
- Strict-prefixed DefIso, isomorphism-evidence and Prof-comparison adapters
  become calls to their existing ordinary owners. The selected inverse maps
  and cancellation computations are preserved.
- `gray_curry_R_strict` and `gray_uncurry_R_strict` become the existing whole
  function owners. Coevaluation and evaluation definitions move directly to
  their existing `_func` owners; the retained inverse and beta/eta data stay.
- Strict ring-presheaf facades and one-category admission no longer introduce
  another carrier. Their consumers use the original ordinary carrier/map.

The implementation that maps an equality-valued equivalence through an
ordinary functor is now named `omega_equiv_along_fmap`, with corresponding
law/projection names. This is distinct from `omega_equiv_along_fapp1`, which
derives the next-Hom equivalence of a Cat-level equivalence. These operations
are not identified. `functor_composition_path` and `functor_is_strict` likewise
name existing implementations at their default-map interfaces.

`IsStrictFunctor` and the native compositor-evidence projections remain as
descriptive property/proof interfaces. No operational map constructor requires
that property as an admission argument. `StrictTransfor`, `StrictFunctord` and
the separate transformation Homs of `GrayHom_lax` remain meaningful and are
preserved. Sharing ordinary functor objects does not identify those categories.

## Replay and qualification boundary

The bounded rewrite only handles the inventoried legacy names and their known
application arities. Declaration counts, unsupported syntax and remaining
active references are guarded. The emitted Lambdapi source is the checked
artifact; the Python helper is an authoring tool, not a trusted checker.

The old spellings still occur in historical source and intermediate replay
templates because the replay begins at the pre-goal pin. They do not occur as
active references in the final emitted LP outputs. Older wrapper-specific
observations are expressed through the corresponding ordinary carriers; two
temporary alias-only checks added in the preceding tranche are retired.

This finishes the wrapper/name disposition in the staged theory. The five
terminal runtime obligations, other normalization/overlap work, full original
import execution, source-pin review and production gates remain required.
