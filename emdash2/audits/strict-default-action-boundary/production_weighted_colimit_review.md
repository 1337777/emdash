# Weighted colimits through the transposed whole Hom comparison

Date: 2026-10-16
Predecessor: `133e8dc0`
Status: qualified staged inverse action and weighted-colimit consumer; broader migration remains incomplete
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [source pins, receipts and development history](production_weighted_colimit_verification.json)

## Result and unchanged mathematical contract

The original weighted-colimit preservation proof used the legacy
`Op_adjunction`, now correctly a total-opposite operation O. The existing
`WeightedColimit_con` instead uses dimension-one transpose T and product-swap
`Op_prof`. These are distinct higher-dimensional operations.

The [migrated proof](production_weighted_colimit.lpfragment) preserves the
public theorem's signature byte-for-byte and leaves `WeightedColimit_con`
unchanged. It reuses the whole comparison already supplied by the original
adjunction interface:

```text
Hom_B(L(−),−) ≅ Hom_A(−,R(−)).
```

Applying `Op_prof` to its inverse supplies the required comparison:

```text
Hom_T(A)(T(R)(−),−) ≅ Hom_T(B)(−,T(L)(−)).
```

The original three proof steps remain: implication by the fixed weight,
reindexing of the given limit comparison, and the mate at the representing
object. The actual forward/inverse data is retained. This does not construct
another adjunction with transposed unit/counit, identify T with O, or claim
that arbitrary lax unit/counit data alone produce the original Hom-comparison
contract.

Two constructor-constrained proof-time comparisons provide the whole
represented-Hom transpose and its unit specialization. They preserve both
actual endpoint functors. Whole base-arrow action is checked; changed endpoint
functors and replacement of T endpoints by total O are rejected. These are
explicit structural comparisons, not equality inferred only from object beta.

## Shared inverse computation

The final public-result inverse controls exposed a failure that also occurs
in the pinned pre-migration core. The former point rule folded consecutive
represented actions into a raw composite. Expanding `defiso_comp` could then
leave inverse factors behind different bracketings, outside the selected
cancellation patterns.

The [selected repair](production_postcomposition_inverse.lpfragment) reverses
that one existing capped equation:

```text
post(q ∘ p, r) ↝ post(q, post(p,r)).
```

It retains the original identity-family guard, semantic owner and whole
functor-composition fold. The whole-functor and capped observation routes
agree. Keeping the consecutive represented cuts visible lets the existing
`DefIso` and mapped-inverse cancellation rules handle both directions of the
actual weighted preservation result. No weighted-specific inverse rule or
new DefIso constructor is added. Raw composition still has no general runtime
associativity rule.

The first experiment instead changed the mixed raw/represented normalization
and added contextual inverse cuts. It repaired the small example and one
weighted direction, then needed further bracket cases. That approach is
rejected. None of its extra cancellation rules is in the selected source.

The [core controls](production_inverse_cut_controls.lpfragment) check both
composite inverse directions on arbitrary incoming arrows, the whole/capped
projection order, rejection of different inverse packages, and absence of
new global runtime associativity. The original failing fixture remains a
historical reproducer against the pinned original core, not an active expected
failure of the migrated implementation.

## Default functor action, without an evidence adapter

The [inverse-action owner](production_default_inverse_action.lpfragment)
now takes the ordinary default functor:

```text
F : Functor(C,D)
i : DefIso_C(x,y)
defiso_fmap(F,i) : DefIso_D(F[x],F[y]).
```

Its stable forward/inverse heads retain the existing proof-time readings as
F's action on the selected arrows. The original computational rule family is
migrated to this owner; it is not copied into a second classified theory.
`prof_comparison_fmap` is the corresponding defined ProfComparison view.
Ordinary `IsoEvidence` maps by the same arrow action and existing `eq_ap` laws.

Seven legacy `strict_defiso_fmap*` names, plus the old ordinary-evidence and
profunctor-map names, are defined compatibility views. All 33 original named
module declarations remain in order, and twelve original central diagnostic
commands are reused unchanged. The temporary `default_functor_is_strict`
helper and its constructed equality-evidence package are removed from the
weighted proof. The new proof path passes F and the actual comparison, not a
strictness witness. Remaining unrelated strict packages/aliases still require
migration and retirement; this is not a claim that all wrappers are gone.

## Rule interactions and resource placement

The core warning comparison is 1932 to 1934 reports: 29 old bodies are replaced
by 31 bodies headed by `hom_postcomp_fapp0`. They concern the changed action
cut with units, inverse cuts, functoriality and category/coefficient projections.
The unit observation joins by the existing proof-time raw-composition reading.
The interaction with F's strict composition exposes two retained presentations:

```text
post(F[qp], r) ≐ post(F[q], post(F[p],r)).
```

A constrained proof-time comparison records that agreement while retaining all
F, p, q and r data. Its typed positive and changed-r negative controls are in
the [default-action reviewer](production_default_inverse_controls.lpfragment).
No operational equation/proof argument is added to a construction.

Installing this comparison early in the core caused a measured allocation
failure during profile checking at the unchanged 2 GiB cap. It now lives in
the existing late functor-action extension, after the profile import, where
its consumers need it. The same actual weighted consumer passes at 90s/2GiB
with `o=20,v=1024`; no memory increase or checker bypass was used. This is a
placement/resource correction, not a change of its mathematical equation.
The LHS audit reports zero unreviewed generic slots in both owners. The warning
review and typed consumers do not establish global confluence.

## Qualification and continuation

The exact final generated inputs match these immutable receipts:

- Complete emitted core plus inherited and focused controls: 258 positive,
  62 negative; 17.970s, `20261016T200559Z-c2cc0da33f0b45ccabd11cbd86dbd899`.
- Actual imported weighted reviewer (7 positive, 1 negative) and the final
  driver (20 positive, 6 negative): 23.980s,
  `20261016T202403Z-5ce4e6d7ce8b420fa5f6a30b4d2d2711`.

The second check includes both public preservation-result inverse round trips,
all twelve retained central diagnostics, native default-F action, and the
projection-order comparison. The original weighted reviewer is byte-identical
and is imported as a real module; the temporary flattened-import workaround
is retired. Every check keeps warnings, subject reduction, serial execution,
90-second/2GiB limits, file limits and no-swap containment.

The broader original profile import advances beyond this owner and identifies
`groupoidal_fibre_transport_equiv` in `emdash3_2_eq1_hom_action.lp`. Its legacy
Cat-valued diagram is used through `Fibre_cat`, which now requires an admitted
Cat_cart family. This theorem only needs ordinary diagram evaluation: inspect
direct `fapp0` before narrowing its input to Cat_cart. Preserve its original
mathematical scope and continue the remaining strict-wrapper migration.

Public source promotion, remaining library/variance consumers, catalog/health,
CI and source-pin review remain required. This checkpoint does not complete
the foundation goal or resume the paused application goal.
