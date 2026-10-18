# Native diagram exchange and the homology boundary maps

Date: 2026-10-18 (UTC)
Predecessor: `92d28e75`
Status: exchange construction and boundary-map definitions checked in staging; full inverse-law comparison remains incomplete
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_native_exchange_verification.json)

## Composition correction

The first ordinary homology comparison failed because the existing nested
postcomposition unifier fixed its intermediate category before comparing
its whole composite. When the incoming functor was itself composite,
Cat composition reassociated and that intermediate category changed.

The corrected residual compares the two complete composites. It preserves
all actual factors and the existing runtime split into represented cuts;
no new associativity normalization or equality payload is introduced.
The original generic-category case, the composite-input case and rejection
of a changed outer functor pass. The complete carried core regression is
283 positive/82 negative assertions, with exact input hashes rechecked.
The real library consumer now passes its initial triangle and boundary
evidence definitions.

## Whole exchange into the native diagram profile

The two subsequent boundary maps originally used Cartesian symmetry on
raw mapping categories. The migrated native family uses oplax diagrams.
Under the original OneCat(C) hypothesis, the corrected whole exchange is:

```
[A,[B,C]] → Cart(A,Cart(B,C))
          → Cart(B,Cart(A,C))
          → [B,Functor_oplax_cat(A,C)].
```

The first map is the existing ordinary-target admission, the second is the
existing symmetry, and the last applies an actual Cartesian-to-oplax
inclusion. The inclusion is defined using odd duality and ordinary inclusion.
Odd duality on Cartesian mapping categories is the counterpart of the
existing even-duality owner. Its two structural declarations have object,
transformation, component and next-Hom projections; they are not presented
as a derivation of every higher coherence law.

A narrowly typed, whole proof-time comparison identifies this construction
with native shape evaluation on its admitted input. A second comparison
records the existing ordinary admission/inclusion inverse law after the
inverse has been read as inclusion. Runtime owners remain distinct. Neither
comparison identifies mapping classifiers or admits an arbitrary lax map
to the Cartesian classifier.

The whole exchange, its walking-arrow specialization and its two-parameter
component action pass. Different whole input families remain distinct. The
odd-duality controls cover identity, composition, the whole next-Hom
functor, capped action and noncollapse. A diagnostic initially failed by
trying to invert reducible Hom aliases across odd duality; writing its
expected type with canonical `Obj(Hom_cat(...))` resolves that inference
problem without changing an operational rule.

## Source correspondence and the precise remaining failure

Both original `homology_family_comparison_boundary_diagram_to` and
`homology_family_comparison_boundary_diagram_from` now typecheck through
this whole exchange. They still use their original square maps, boundary
cells and inverse choices. All native P/Q/A/D/h parameters remain. The
actual h remains lax, and no new OneCat hypothesis is imposed on B.

The following inverse-law observations now use the native fixed-index
oplax evaluator. Its accessor and composition-path definition follow the
original production outline. Reversing the interface substitutions and
removing the one earlier import restores the complete original comparison
file modulo whitespace. No tail was omitted from its staged source.

The full file still fails at
`homology_family_comparison_diagram_left_source_law`: the evaluated
composite of the new whole maps has not yet been compared with the original
composite of source-endpoint maps. This is a whole transformation-action
obligation. The successful two-parameter component observation does not
settle it. Reflection/reconstruction integration, the rest of the whole
homology comparison and its point consumers therefore remain unqualified.

Next inspect the projection of the actual inclusion/exchange through fixed
oplax evaluation, at those existing owners. Preserve the original inverse
proof bodies and avoid adding caller-specific equations or replacing the
chosen inverse data. A general new profunctor or coherence development is
not a prerequisite.

## Validation boundary

The verification records exact source receipts, unchanged-input checks,
owner audits and warning bodies. New ordinary/oplax exchange comparisons
are proof-time facts, not runtime folds. The seven new odd-duality runtime
projections preserve the canonical strict-transfor view. The new warning
families concern those projections, units, composition and inherited
whiskering overlaps; focused joins do not establish global confluence.

The final combined check passes in 71.162s with maximum child RSS
3007968 KiB (about 2.87 GiB), under the existing 300s/4GiB/o=20 profile.
It includes both existing ordinary reconstruction and arrow-family
isomorphism reviewers. The unchanged-input core receipt passes in 19.511s
under 240s/2GiB/o=20. No limit was increased. Five owning-file LHS audits
report no unreviewed candidates, with separate manual review of the new
owner-specific patterns. The focused warning comparison adds 31 bodies and
removes none; their groups and exact bodies are in the verification.

Only non-library migration authoring and its replay files are checkpointed.
Production source promotion, remaining library migration, redundant-wrapper
retirement and final central/catalogue/health/CI/source-pin gates remain
required. The separate application goal remains paused.
