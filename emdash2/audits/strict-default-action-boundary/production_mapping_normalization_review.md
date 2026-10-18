# Canonical evaluation and walking-arrow normalization

Date: 2026-10-18 (UTC)
Predecessor: `16aa222c`
Status: constructor/evaluation consolidation checked in staging; broader migration and performance qualification remain open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_mapping_normalization_verification.json)

## Selected normal forms

This slice consolidates the ordinary diagram-exchange comparisons identified
in the preceding [normalization review](production_normalization_review.md).
It adds no primitive, classifier, supplied comparison or unification rule.
Four constructor/projection computations replace three comparison rules.

The existing canonical admission J from ordinary maps to Cartesian maps,
under its existing OneCat(C) hypothesis, now has the whole fixed-evaluation
computation:

```
Cartesian evaluation at a after J  ↝  ordinary evaluation at a.
```

The [owner rules](production_one_cat_mapping_evaluation.lpfragment) reduce
the existing sym_fapp0_func to fapp0_func, and its already-projected first-Hom
owner to tapp0_func. The canonical mapping comparison is the discriminator;
an arbitrary map between those categories is not treated as J. Its original
forward/inverse functors and their cancellation owners remain. The existing
component rule supplies the capped join, so no duplicate point rule is added.

Two [constructor cuts](production_walking_arrow_postcomposition.lpfragment)
belong to the existing walking-arrow introduction:

```
H ∘ walk(f)                     ↝ walk(H[f])
Cartesian exchange(walk(U))[x]  ↝ walk(U[x]).
```

The first retains arbitrary default-strict H and f. The second takes U from
the existing Cartesian Hom, hence a strict transfor, and works for arbitrary
target C. Neither imposes strictness on arbitrary ambient transformations.
Both return the original join constructor, with its actual mapped endpoints
and generator. Patterns use that constructor's normal form, not the reducible
walking_arrow_func alias. No new intermediate head hides the computation.

## Retired comparisons

The two expanded ordinary admission/exchange point comparisons from
`production_one_cat_arrow_point_view.lpfragment` are removed. Their original
source is retained by Git at `5d2618fb`. They matched the direct walking-arrow
point and its embedding under an outer exchange. The existing Cartesian
point unifier in production_cartesian_arrow_point.lpfragment is also removed;
its original typed-reflexivity path remains and now follows the runtime cut.

One previous negative asserted that a canonical ordinary-arrow introduction
and its walking-arrow value stayed distinct at runtime. It deliberately
becomes positive under the stronger constructor computation. The unrelated
generator negative, arbitrary higher-cell/equality negative, actual inverse
choices and every original whole/higher observation remain.

The 151-file inventory now has 247 unification commands instead of 250 and
1296 runtime rule commands instead of 1292. Core counts and its source are
unchanged. The whole Homd ladder, its profiles and generic FF interfaces are
unchanged. Counts describe the consolidation; they do not prove confluence.

## Experiments and validation

The original whole admission/evaluation observation failed at 4 GiB. Its
initial 2 GiB check exhausted memory during imports, before that observation;
it is not a mathematical failure. The whole rule alone passed its own and
object observations but left the earlier first-Hom projection stuck. The
second rule addresses that same owner and projection order.

With both evaluation rules but the old ordinary comparison rules removed,
the original transpose consumer still failed. Its terminal log survived an
interrupted runner, but no execution receipt was finalized; this is retained
as failure-localization evidence only. Adding ordinary postcomposition alone
still left Cartesian evaluation of the walking constructor. The latter cut
closed the actual consumer. No contextual unifier was added to bypass it.

The focused walking-constructor controls preserve endpoints, generator,
identity, composition and the selected transfor component. Changed generators,
transfors, evaluation points and arbitrary noncanonical admissions remain
distinct. The original mapping forward/inverse and first-Hom round trips are
also checked.

The combined zero-column dependency driver passes, including the original
contraction, ordinary transposition and native image/coimage reviewers. The
complete native homology comparison source passes. A further combined driver
passes the original ordinary-arrow reviewer and higher-Hom query, ordinary
reconstruction and arrow-family inverse observations, native exchange controls,
and both original homology whole/point reviewers.

The unchanged complete core's 287-positive/85-negative receipt is carried
only after its exact input hashes are rechecked. Subject reduction remains
enabled. Both changed runtime owners pass the inferred-slot audit; their
owner-specific constructor patterns were inspected manually as well.

An attempted simplification of one_cat_oplax_exchange_at_path to reflexivity
failed its whole-transformation comparison. It is rejected. The original
derived modification/discreteness proof is restored byte-for-byte, and is
used by the final source and reviewer checks. No new equality rule was
introduced to force that shorter proof.

## Warning and performance boundary

The full native homology warning multiset changes from 2913 to 2915 bodies:
two added, none removed. Both new peaks concern a Const_func endpoint of the
Cartesian walking constructor being rewritten first to Const_catd. The
typed constructor/projection and original consumers pass; convergence for
every further constant-family specialization is not established here.

The final zero-column driver passes in 57.535s at 3459.1 MiB maximum child
RSS. The full native owner passes in 114.659s at 5306.1 MiB, compared with
81.370s at 5518.8 MiB in the preceding matched-profile review. Its allocation
traffic decreases from 24,650,002,973 to 23,824,572,510 words, but wall time
increases in these samples. This is not evidence of a speedup. The larger
combined ordinary-arrow/native reviewer passes in 136.463s at 5869.9 MiB.
All use the existing 300s/6GiB/o=10 profile; no limit was raised.

The accepted benefit is a more direct computation contract and removal of
three comparison patches, with preserved real consumers. Performance remains
an explicit pre-promotion task. The large exchange proof is still derived,
and its failed reflexivity experiment does not justify a new primitive or
an added equation. Other composition/Sigma projection concerns from the
normalization review remain recorded. Continue the outstanding native K/Q
transpose and zero-column migration while applying this owner-level policy
at subsequent failures; do not reopen the foundational profile matrix or
grow a general Q theory for this task.

Replay: run production_owner_migration.py, then the bounded
zero_column_dependency_controls.lp and mapping_normalization_regression_controls.lp
targets. Use the full native homology owner for a matched performance sample
when these computations change again. Production promotion, remaining
libraries, redundant-wrapper retirement and final qualification are open.
