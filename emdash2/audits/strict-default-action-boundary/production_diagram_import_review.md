# Whole diagram reindexing across the adjunction-view import

Date: 2026-10-18 (UTC)
Predecessor: `9cc46e71`
Status: import-order reindexing regression checked; ordinary-target walking-arrow observation remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_diagram_import_verification.json)

The diagram-evaluation module checks on its own. Preloading the original
adjunction-family views reproduces the central diagnostic failure: the whole
reindexing comparison tries to identify its arbitrary parameter category B
with `Functor_cat I C` and its arbitrary D with an identity.

The interfering view was unrestricted congruence for two
`comp_prod_fapp1_fapp0` expressions. Corresponding input equality is a
sufficient condition, but it is inappropriate as the selected decomposition
of different whiskering factorizations. The existing whole reindexing rule
already compares those factorizations correctly. This was a unification
interaction, not evidence that the reindexing theorem needs a smaller domain.

Removing the congruence altogether exposes its legitimate original consumer:
the adjunction transpose formula has the same two actual cells, h and an
identity, with different endpoint presentations. The replacement therefore
matches the same category triple and the same two cell payloads, and compares
only the endpoint pairs. It cannot decompose the different cells introduced
by reindexing. The old broad clause is retained as inactive comparison text
with an explicit restoration condition.

No diagram-evaluation declaration, whole reindexing formula, ordinary-target
guard, runtime rule or mathematical constructor changed. The original
adjunction-view definitions and diagram-evaluation module both check in the
previously failing import context. The original diagram reviewer retains
its ten positive/three negative checks. One additional whole comparison
specializes B to the mapping category itself while retaining an arbitrary
nonidentity endofunctor D. This tests the case that a shared-intermediate-
category guard alone would not address. No pointwise replacement of the
whole claim is used.

The complete original adjunction-view reviewer is also staged. Its additional
image/coimage dependencies advance beyond diagram reindexing and stop in
`emdash3_2_walking_arrow_native_observation.lp`. The fresh central diagnostic
run reaches the same new boundary. They are failed positive integration
obligations, not passing reviewer gates.

That consumer passes the corrected general oplax evaluator to
`one_cat_lax_transfor`, which expects an ordinary transformation. Its existing
OneCat assumption is retained, but does not make `OddDual_cat C` equal to C.
Next qualify a real ordinary-target evaluation view under that assumption,
reusing the existing fixed evaluation and mixed action. Prefer an existing
whole construction where available; if a guarded whole owner is needed,
state its structural status and retain the complete projection/action ladder.
Preserve the public ordinary diagram input and the selected generator value.
Do not erase duality wrappers, identify the general lax/oplax classifiers, or
change this consumer to a different diagram carrier merely to make it type.
This concerns an existing baseline consumer, not resumption of the separate
application-equivalence goal.

The standalone owner passes in about 38s at 300s/4GiB/o=20. The focused
preloaded-view regression passes in about 96s at 600s/4GiB/o=5. These are
different import/runtime profiles, not a performance comparison. The central
gate reaches its new type boundary in about 110s under the latter profile.
The diagram warning bodies match the earlier failing run with the same
preloaded views (202 bodies); comparing with the smaller standalone import
would instead mix different warning environments. The changed view owner has
no new warning bodies or unreviewed LHS slots. Exact inputs, further carried
and refreshed qualification, and resource measurements are in the verification.
The coupled profile/locality gate also passes again in about 125s under the
reviewed integration profile, with its 2658 warning bodies unchanged. Its
changed imported view was checked fresh; the unchanged core receipt is
carried only after all input hashes match.

Core source is unchanged from the preceding qualified checkpoint. Whole
remaining library/diagnostic migration, redundant strict-functor-wrapper
retirement, production promotion, and final gates remain required.
