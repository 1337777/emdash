# Ordinary arrow-family isomorphisms after the duality migration

Date: 2026-10-18 (UTC)
Predecessor: `1f38891f`
Status: staged whole isomorphism and original observations checked; diagram-family reconstruction remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_one_cat_arrow_family_verification.json)

The original arrow-family comparison is an ordinary-target consumer. It
already requires OneCat(C), but still used Cartesian exchange directly on
raw transformations and expected the former ordinary target of the general
`transf_arrow_diagram_func`. The latter now has an oplax target. The selected
change uses the existing ordinary-target exchange from the preceding
checkpoint, without equating the general ordinary/oplax profiles.

The ordinary family presentation is a definition:

```
one_cat_transf_arrow_diagram_func(C1, eta)
  = S_WalkingArrow,B(walking_arrow_func(eta))
  : B → Functor_cat(WalkingArrow,C).
```

Both original square maps are retained, including the actual to/from
modifications selected by the input isomorphism. Their ordinary diagram
inverse laws are proved before exchange using the same diagram-reflection
theorem and endpoint identities. Existing strict-functor action on
isomorphism evidence then supplies the inverse laws after exchange. The
public comparison still returns those actual maps, with the same input
parameters and the guarded ordinary family presentation. No new inverse
assembly, naturality witness, or operational equality argument is added.

Naming the two square maps and their laws separately is necessary here for
usable checking. A single let-bound evidence package exhausted the 4 GiB
guard after about 133 seconds. The factored definitions check in about
102 seconds at the same 4 GiB/o=5 setting, with about 2.7 GiB maximum child
RSS. Almost all of that time is the unchanged import closure; the new owner
finishes immediately after it. The mathematics, selected maps and resource
caps are unchanged. The diagnostic `type` query without explicit implicit
arguments failed separately and is not evidence of a formal type failure.

The original reviewer exposed a second, computational requirement: double
exchange must retain its action on a whole transformation. Objects already
computed correctly. Three scoped inverse projections and one component beta
join the same canonical mapping comparison after generic action has
projected. They retain the input map and the same inverse pair. They do not
introduce inverse laws for arbitrary maps or identify the mapping categories.

The postcomposition patterns need the actual classifier endpoints shared
with the primitive DefIso maps. Leaving their endpoints completely inferred
caused subject reduction to confuse Hom(Cat_cart) with Hom(Cat_cat).
Functor-typed alias patterns passed formation but did not close the actual
double-exchange consumer. Calculated classifier guards closed the generic
consumer but exposed product-normalization overlaps. The selected shared
endpoint variables avoid using a reducible classifier expression as a guard;
the actual product specialization is checked explicitly. These are measured
pattern/inference decisions, not a change to the selected universes.

All six original reviewer assertions remain: the four endpoint identities
are runtime observations, and the two evidence projections retain the
chosen comparison maps. They have not been weakened to supplied paths or
pointwise observations. The focused whole double-exchange comparison retains
arbitrary transformation data and rejects replacing it with another input.
The earlier mapping, identity, classifier and component controls are included
in the combined check. Subject reduction and the normal serial/file/no-swap
safeguards remain enabled. Warning bodies and their identity, existing-view,
inverse-overlap and product qualifications are recorded in the verification;
this is not a global confluence certificate. There are seventeen new warning
bodies, rather than the earlier candidate's thirty-three: shared endpoint
variables remove the sixteen product-distribution overlaps. The original
six runtime observations and all focused controls pass together in about
101 seconds at 4 GiB/o=5, with about 2.8 GiB maximum child RSS.

The last central check passes the arrow-family isomorphism owner and reaches
`one_cat_diagram_family_reconstruction_to` in
`emdash3_2_one_cat_diagram_family_reconstruction.lp`. That older proof still
uses raw Cartesian exchange and supplies the now-oplax
`diagram_family_transf` to an ordinary walking-diagram constructor. Its
existing OneCat guard is available for the ordinary presentation. The next
step is to preserve the arbitrary original family D and both reconstruction
maps while adapting that whole evaluation/exchange route. Do not identify
the general oplax profile with the ordinary profile or replace the whole
reconstruction by object observations.

That central receipt retains the preceding calculated-endpoint version.
The final refinement changes only the mapping-profile owner in that import
closure. The final combined gate rechecks that owner, the isomorphism module
and its reviewer, including the explicit product case; no completed central
gate is claimed from the historical failed run.

The work remains staged. Core source is unchanged. Remaining original
library migration, redundant strict-functor wrappers, production promotion
and final catalogue/health/CI/source-pin checks remain required. The separate
application-equivalence goal remains paused.
