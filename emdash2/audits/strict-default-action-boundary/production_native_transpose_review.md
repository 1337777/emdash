# Native-input diagram and K/Q transposition

Date: 2026-10-18 (UTC)
Predecessor: `99eed0bb`
Status: staged native transpose and original K/Q observations checked; zero-column universality integration remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_native_transpose_verification.json)

## Whole construction and canonical column

The [native counterpart](production_one_cat_oplax_transpose.lpfragment)
retains the original exchange/arrow-family/exchange outline. Its inputs are
the actual F,G:B→Functor_oplax_cat(I,C) and h:F⇒G, under the original
OneCat(C) hypothesis. B and I remain arbitrary. The whole result is

```
T_h : I → Functor_cat(B,Functor_oplax_cat(WalkingArrow_cat,C)).
```

The first exchanged transformation is an actual composite: prewhisker the
existing precomposition telescope transformation with the native evaluator.
Its ordinary-target guard is semantically essential; this does not declare
an unrestricted exchange of two lax transformation directions. The remaining
two operations are the existing ordinary arrow-family introduction and the
qualified native exchange. Four definitions are added; no primitive,
rewrite, unifier or supplied comparison is introduced.

For the fixed index i, write e_i for the existing native evaluation functor.
The canonical column view is the existing native graph of

```
e_i ∘ F,  e_i ∘ G,  e_i ⋅ h.
```

It uses comp_cat_fapp0 and comp_cat_cov_fapp1_func. Their declared composition
endpoints compute when a constructed family is substituted for F or G. The
varying-index accessor has a different stable precomposition normal form;
using it here hid those reductions behind an otherwise valid whole view.

This is a defined canonical column view, not a new independent functor
constructor or an objectwise assembly over I. The whole T_h and its shape
action remain the original composed functor. Both positive and changed-h
comparisons explicitly observe fapp0(T_h,i), so the canonical accessor does
not make them tests of its own definition. Root projection agrees with the
column at proof time; runtime root-to-view equality is not claimed.

The native adaptation retains all eight original positive observations and
the changed-map negative: whole column comparison, whole endpoints,
generator, both nonidentity shape components, and next shape/parameter Hom
action. Native diagram components are observed with the existing odd-dual
encoding and reversed underlying endpoints, rather than confusing their
carrier with the ordinary diagram category.

## Original K/Q consumers

The four original kernel-counit/cokernel-unit definitions now use the native
transpose interface and their actual Functor_oplax_cat diagram categories.
The initial-object choice uses TotalOp_cat. The original adjunction cells,
P/Q selections, terminal/initial diagrams and all ten reviewer observations
remain. No pointwise replacement or additional inverse/comparison input is
supplied. In particular the canonical column's covariant composition types
expose K, the constant zero endpoint and the original evaluation functor
without a new kernel comparison rule.

The ordinary transpose interface remains available and its original
eight-positive/one-negative reviewer is included in the combined check.
The new native definitions reuse the same semantic operations; they do not
replace the ordinary interface or duplicate its primitive theory.

## Rejected comparison expansion

The first K/Q type failure compared a stable composite precomposition with
the existing projected kernel functor. An experiment replaced the two
composition-shaped readings by one comparison with an arbitrary requested
value, retaining the complete composite as a residual constraint. The
expanded core passed 288 positive/86 negative controls at 4 GiB, including
an actual inverse-based bare-functor observation and its changed-value
negative. Its initial 2 GiB run allocation-failed. The K/Q definitions then
checked, but their runtime endpoint reviewer still failed.

That experiment is not retained. Choosing the existing covariant owner for
the fixed column solves the actual K/Q consumer with the prior core. Both
precomposition files are restored byte-for-byte to the predecessor. The
final complete core's earlier 287/85 receipt is reused only after checking
its exact source hashes. No global comparison or resource-default expansion
is part of the selected implementation.

## Runtime observations and resource qualification

The initial 300s checks with o=10 and o=20 timed out during imports, before
the new declarations. In the first, the unchanged core alone took about
122s. Source and checker hashes matched the preceding passing snapshot.
Sampled CPU frequencies were 400 MHz and host load was high. Host settings
were left untouched. A 600s/6GiB/o=20 diagnostic then reached the actual
owner and consumer failures; it was diagnostic headroom, not a performance
qualification. Later checks returned to much shorter times. These host
observations do not retrospectively explain every earlier timing difference.

The first native construction and actual whole-column comparison passed,
but its expanded column projection failed the runtime source-endpoint check.
The normalization diagnostic retained that failure's actual terms. A first
canonical view using the varying-index accessor passed the general native
reviewer, but its K/Q instance exposed the same composition barrier. The
selected covariant presentation is checked against both levels.

The final verification records source snapshots, resource settings, warning
evidence and exact receipts. Subject reduction, serial checking, file limits
and no-swap containment remain. No speedup is claimed from these differently
loaded host samples. The implementation adds no runtime or unification rule.

The combined final check passes all 26 positive and two negative
observations in 66.670s at 3545.7 MiB maximum child RSS under
300s/6GiB/o=20. The same K/Q import closure has the identical 2923 warning
bodies before and after the selected fixed-column change. A comparison with
the smaller diagram-only closure includes fifteen pre-existing terminal-arrow
overlaps from additional imports; those are not new rules in this slice.
Both changed owners have zero unreviewed inferred-slot candidates.

## Continuation

Next adapt the original terminal/initial family-presentation evidence and
native zero-column universality consumers. Reuse their existing ordinary
modification evidence, the qualified native arrow-family comparison, and
native reconstruction with the original chosen maps and inverse data.
Those consumers are not completed by the transpose checks.

Remaining library migration, normalization/performance review items,
redundant strict wrappers, production promotion and final catalogue/health/
CI/source-pin qualification remain required. The separate application goal
stays paused.
