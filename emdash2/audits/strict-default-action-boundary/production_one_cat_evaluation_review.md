# Guarded ordinary evaluation and the native arrow observer

Date: 2026-10-18 (UTC)
Predecessor: `d3ab4277`
Status: ordinary-target evaluator and original observer checked; family reflection's ordinary/Cartesian exchange remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_one_cat_evaluation_verification.json)

The general shape evaluator remains oplax. An ordinary target supplies a
different valid profile: naturality squares of its diagram transformations
commute. The existing native arrow observer already requires that OneCat
hypothesis, so it now uses a guarded ordinary evaluator without changing its
diagram carrier, public signatures, chosen generator, graph construction or
value-path proof.

The additional structural owner is

```
one_cat_diagram_evaluation_func(C1)
  : I → Functor_cat(Functor_cat(I,C), C).
```

This is explicitly a guarded whole constructor, not a claimed derivation of
an ordinary transformation from the general oplax constructor. Its object
projection is the existing fixed evaluator. Its Hom and transfor names are
defined aliases through generic `fapp1_func` and `fapp1_fapp0`; identities and
composition remain owned by the existing strict-functor calculus. There is
one structural head and five projection rules, with no independent laxity
witness or new caller-provided equality data.

The ordinary mixed action is a defined composition of existing operators:

```
alpha:F⇒G  ↦  G[u] ∘ alpha[i].
```

It is compared with the general evaluator's mixed action
`alpha[j] ∘ F[u]` using the existing ordinary-target naturality path extracted
from alpha. The whole mixed-functor comparison then uses the existing
discrete-target theorem, with C1 supplying discreteness of the target Hom.
That theorem's existing structural closure/assembly assumptions remain; no
new general functor extensionality or equality of mapping profiles is added.
The evaluator itself is not constructed from a pointwise family of squares.

The original observer changes only three evaluator occurrences, its scoped
admission reading, and the associated comment. Reversing those edits recovers
the original source byte-for-byte. All five original positive/two negative
observations pass, including the two sides of a nonidentity diagram map,
the complete next-Hom type, generator recovery and retention of the admitted
runtime profile. The supplied walking-arrow reconstruction interface remains
unchanged and checks in the central import; no new reconstruction or nerve
equivalence theorem is introduced.

The focused evaluator controls check the root projection, identity and both
identity observation orders, whole composition and its components, the
entire shape-Hom observation, and an actual modification through mixed
evaluation/postcomposition. The negative controls retain the chosen shape
arrow, reject using the general oplax constructor as an ordinary transfor,
and reject retyping this evaluator as a terminal-source constant-family map.
The final combined gate includes these nine positive/three negative controls,
the original observer reviewer, and the prior general evaluator/import-order
reviewer.

An initial three-head implementation passed its focused checks, but duplicated
identity/composition handling. It is unselected. The final Hom/transfor aliases
retain the generic functor-action owner instead. Its new owner-warning
inventory has 21 additional bodies relative to the old standalone evaluator:
18 crossings with the existing generic/duality/family identity clauses, two
diagram-identity crossings, and one terminal-source interpretation overlap.
The identity observations are checked in both orders. The source-identity
crossings use the same inherited identity owner on the root and the observed
diagram, without adding specialized identity normalizers. The constant-family
negative rejects the other interpretation's endpoint types. These are scoped
qualifications, not a global confluence certificate or a reason to equate
the general profiles. The owner-position LHS audit has no unreviewed slots.

The fresh central diagnostic run advances through the observer, ordinary
diagram reconstruction and diagram-map reflection. Its next failure is
`one_cat_diagram_family_map_path` in
`emdash3_2_one_cat_diagram_family_reflection.lp`: the old proof applies
Cartesian `sym_*` owners to raw ordinary families and transformations.
The existing OneCat target can justify a whole profile comparison, but it
does not make the two classifiers interchangeable by syntax. Both the inner
family carriers and the outer map profiles must be addressed; merely
admitting h and k does not change F and G's codomain. Next inspect a
whole ordinary-target/Cartesian mapping comparison or a corresponding whole
ordinary exchange construction. Preserve the raw F,G,h,k inputs, the two
whole endpoint-path premises, actual maps/inverse data, and the original
OneCat guard. Do not globally identify `Functor_cat` and `Functor_cart_cat`
or reduce this whole reflection claim to point observations.

The final focused checks and integration run keep subject reduction and
source-only replay. The reviewed 300s/4GiB/o=20 focused profile and
600s/4GiB/o=5 integration profile remain explicit; normal defaults and the
serial/file/no-swap safeguards are unchanged. Exact timings, inputs and
warnings are recorded in the verification. Core source is unchanged.
The final coupled evaluator/observer/import-order gate passes in about 113s
under the integration profile. The central gate reaches the new family
reflection boundary in about 116s under that same profile.
Earlier locality evidence retains its original snapshot; its diagram import
has changed and its broader requalification remains a later integration gate.

The work remains staged. Remaining central/library migration, redundant
strict-functor-wrapper retirement, production promotion and final gates are
still required. The separate application-equivalence goal remains paused.
