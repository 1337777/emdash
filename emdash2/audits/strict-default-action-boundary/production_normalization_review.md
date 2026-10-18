# Computational ownership and normalization review

Date: 2026-10-18 (UTC)
Checkpoint reviewed: `5d2618fb`
Status: source review and matched measurements complete; normalization consolidation remains required before production promotion
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_normalization_review_verification.json)

## Assessment

The user's concern is supported by the source and measurements. Passing the
current consumers establishes useful implementation feasibility. It does not
establish a satisfactory global normalization policy, termination/confluence,
or production performance. In particular, repeatedly adding comparisons for
different presentations of the same operation can become implementation debt
even when each equation has an ordinary mathematical justification.

The selected categorical design is not rejected by this review. No new
semantic obstruction was found, and no LP declaration, runtime rule,
unification rule or checker setting was changed. The review instead identifies
specific computational owners that need consolidation. It is not appropriate
to dismiss the measured cost simply because it stays inside the resource cap.

## Matched performance

Both sides use the exact pinned pre-goal source or the current emitted
migration, the same installed checker, enabled subject reduction and warnings,
source-only checking, `--record-time --too-long=0.5`, and serial resource guards.
Each row is one matched sample, not a statistical benchmark distribution.

| Corresponding target | Pre-goal wall / peak child RSS | Migrated wall / peak child RSS | Shared profile |
| --- | ---: | ---: | --- |
| `examples/image_coimage_adjunction_families.lp` | 6.792s / 495.3 MiB | 37.143s / 2462.8 MiB | 300s / 4 GiB / `o=20` |
| `emdash3_2_one_cat_homology_family_comparison.lp` | 13.413s / 754.1 MiB | 81.370s / 5518.8 MiB | 300s / 6 GiB / `o=10` |

This is approximately 5.5x and 6.1x elapsed time, and 5.0x and 7.3x peak
memory. Earlier matched core measurements at the
[hygiene checkpoint](production_hygiene_review.md) were 4.442s/326.3 MiB
versus 17.064s/1426.0 MiB. That earlier core measurement is historical and
must not be presented as a fresh measurement of the current checkpoint.

The comparisons retain the original mathematical consumer outlines and
observations, but the migration necessarily changes profiles and some
dependencies. The image/coimage closure has 17 versus 21 input files; the
homology comparison has 67 on each side. These numbers measure end-to-end
migration cost, not the isolated cost of adding a unification rule.

For image/coimage, the import commands account for approximately 6.66s and
36.84s of the respective runs. Its actual final observations are inexpensive.
The reported rewriting timer increases from 4.83s to 32.41s; the solving
timer increases from 0.49s to 1.12s. For homology the corresponding timers
are 10.09s to 74.94s and 1.00s to 2.29s. Allocation traffic also increases
substantially. These timer labels do not isolate the contribution of custom
unification: solving itself can request normalization. They do support
prioritizing expanded terms, repeated conversion and rule interactions over
an unsubstantiated claim that one particular comparison is the root cause.

The largest measured non-import command is the new
[`one_cat_oplax_exchange_at_path`](production_one_cat_oplax_exchange_paths.lpfragment),
at 12.16s. Other concrete sites include its whole exchange-map definition
(2.99s), the represented-comma target link (2.87s), and native diagram
reconstruction (4.70s). Do not sum nested import timings as independent work.
There is enough localization to start a bounded owner review without another
full repository aggregate or an increased resource ceiling.

## Inventory and its limits

The read-only [inventory helper](production_normalization_inventory.py)
examines the 151 corresponding non-example LP files in the current migration
manifest. It excludes old scratch files and standalone reviewer assertions.
It strips comments and inventories complete commands; it is not a Lambdapi
parser or a semantic/confluence checker. Its detailed output remains in the
ignored probe directory and is reproducible from the pinned authoring inputs.

| Scope | Pre-goal runtime rule commands | Migrated | Pre-goal unification commands | Migrated |
| --- | ---: | ---: | ---: | ---: |
| Core | 743 | 991 | 91 | 144 |
| All 151 corresponding files | 981 | 1292 | 172 | 250 |

There are 114 textually changed or added comparisons, including variance and
coefficient edits to existing comparisons; this is not 114 new laws. The
largest changed comparison has 1619 normalized characters. The ordinary
exchange comparison has pattern nesting depth seven. Counts and depth are
review signals, not semantic judgments or performance attribution.

The scan found no changed rule that unconditionally rewrites a primitive
head on a tuple consisting only of variables to a semantic body. That is a
bounded negative finding for the user's first warning sign, not a guarantee
that every head or alias has a good design. It found 61 changed clauses whose
RHS returns a newly declared primitive. Many are normal projection or
constructor laws. The deeper cases were inspected explicitly.

## Concrete ownership findings

1. **Several runtime presentations of composition are inherited.** The
   pre-goal core already declared `hom_precomp_along_fapp0` and
   `hom_postcomp_fapp0` as stable cut owners and compared them with raw
   composition at proof time. Their purpose includes retaining computational
   inverse cancellation. The latest
   [precomposition comparison](production_precomposition_association.lpfragment)
   expresses ordinary composition/reassociation and retains every actual
   functor. Its mathematics is not an arbitrary new axiom. Its necessity is
   nevertheless evidence that the canonical-form policy is incomplete: raw
   composition, precomposition and postcomposition can survive in equivalent
   endpoint types and demand additional pairwise bridges. The migration adds
   pressure to a pre-existing design choice.

2. **The ordinary exchange bridge is genuinely brittle.** The second
   [point comparison](production_one_cat_arrow_point_view.lpfragment) matches
   an expanded admission/inverse/exchange/walking-arrow pipeline. It has an
   actual consumer and preserves the cross-cell, but depends closely on the
   current unfolding and association order. It should be reviewed as a
   candidate for an owner-level projection design before adding further
   contextual variants. The same exchange family contains the measured
   12.16s definition; this makes it a useful first performance target, not
   proof that this particular unifier caused that cost.

3. **Not every new stable head is an isolated workaround.** In
   [the Homd owner](production_homd_core.lpfragment),
   `fib_cov_tapp0_u_func` has the whole transport parameter, object projection,
   map projection, higher-Hom observation, and identity/composition action.
   `Homd_coeff_rep` is the object image of a whole represented-inclusion
   functor, with a semantic body for its higher action and represented
   composition rules. These are recognizable whole operations. That supports
   keeping the architecture while reviewing their expanded inclusion patterns
   and critical overlaps; it does not prove all their interactions confluent.

4. **One additional projection deserves explicit scrutiny.**
   [`sigma_const_target_func`](production_sigma_constant_projection.lpfragment)
   has runtime object computation, but its agreement with the underlying
   whole/Hom/capped Sigma projection is given partly by unification. Earlier
   eager expansions broke the generic application/composition cuts, as
   recorded in the [target review](production_comma_target_review.md).
   This is an explicit structural projection, not an unexplained supplied
   map. Still, the distinction between a neutral higher action with a
   proof-time reading and a reducing semantic projection must remain visible
   in the computational acceptance criteria. Neither typechecking nor a
   typed-reflexivity observation alone establishes the latter.

5. **Identity/duality joins reveal a repeated pattern.** Core T/R and the
   newer odd/even diagram dualities erase identity annotations before some
   generic action rules match. The latest transfor-unit repair follows that
   pattern. Further nested cases remain warning families. This calls for a
   review of the generic typed identity/projection boundary, rather than an
   indefinite list of new duality-specific joins. Do not mechanically erase
   guards: past broad replacements regressed actual consumers.

The [previous hygiene review](production_hygiene_review.md) already corrected
one noncomputing pattern on a transparent alias and retired three duplicate
strictness rules. Thus there is confirmed implementation debt as well as the
new review candidates. Some comes from the old foundation, some from the
migration's additional coefficient and duality presentations.

## Recommended next scope

Before extending either the composition or exchange comparison family,
review that family as one computational owner:

- state the intended runtime forms, the preserved inverse cuts and the
  whole/object/Hom projection routes;
- distinguish required runtime computation from readable proof-time views;
- try one local consolidation using existing semantic operations and stable
  projections, keeping types, all actual inputs and higher action;
- require the original whole consumers, inverse observations, Homd regression
  and changed-input controls, plus matched time/allocation measurements;
- replace or retire the superseded comparisons only after that slice passes.

Do not convert all comparisons to eager runtime rewrites: that can duplicate
expanded bodies, lose inverse cuts, or create cycles. Do not replace them
with supplied equality arguments or new primitive heads that merely rename
the failing terms. Likewise, proof opacity is not an automatic cure for the
cost of checking the proof's own type.

The selected strict-functor/lax-transfor and coefficient design remains in
force. No general Q theory, new foundational profile matrix, broad file split
or checker redesign is introduced by this review. Redundant strict-wrapper
retirement is already required by the migration and remains a separate
source of overlap reduction to measure.

Computational ownership and measured usability are now explicit
pre-promotion gates. Independent mechanical migration can continue, but new
case-specific bridges in the identified families should trigger this local
consolidation review. Larger alternatives may be documented and deferred;
a demonstrably broken required runtime projection cannot be deferred while
claiming that projection complete.
