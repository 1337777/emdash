# Native ordinary zero-arrow family classification

Date: 2026-10-18 (UTC)
Predecessor: `422cf92c`
Status: complete original classification owner and reviewer checked in staging; broader migration remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_zero_family_verification.json)

The original native cone already uses the corrected oplax walking-diagram
category. Its downstream universal transformation and family classifier
still named the ordinary mapping category, causing the first type failure.
The migration now uses that actual native category consistently:

```
J = terminal_arrow_diagram_func : C → Functor_oplax_cat(WalkingArrow,C)
D : B → Functor_oplax_cat(WalkingArrow,C)
h : J ∘ A ⇒ D
Γ(A,D,h) : B → ZeroArrowCone(C,t,T).
```

B remains unrestricted, and OneCat(C) is the original hypothesis. The
native comma, arbitrary A/D/h, both projection comparisons, the whole
triangle modification, its two actual maps and inverse-law proofs are
retained. The reviewer uses objects and Homs of the actual oplax diagram
category for its literal cone data. It does not equate the ordinary and
oplax mapping categories.

The proof needs the corresponding OneCat closure for oplax diagrams.
`one_cat_oplax_functor_category(I,C,C1)` is a new structural closure
declaration, at the same level as the existing ordinary
`one_cat_functor_category`. It requires the actual C1 witness. This is not
claimed to be a theorem derived from the current duality beta rules, and
it adds no caller-supplied naturality, comparison or inverse data. It lives
after the existing oplax diagram constructor, avoiding a core dependency
cycle or a new coefficient universe.

The constructor-visible identity projection of the universal cone
transformation now infers its source from that whole transformation head.
Its old Op category tag referred to the former total opposite and is no
longer a suitable discriminator. Both literal endpoints and the actual
identity remain in the pattern; an arbitrary arrow is not collapsed.

## Selected computation repair

After the owner typechecked, the second original triangle computation
failed. The mapped identity had normal form `id(G ∘ F)`, while the
composition's middle object retained
`hom_precomp_along_fapp0(id,F,G)`. Those are the existing raw and stable
presentations of the same functor. The ordinary category-unit rule retains
an intentional shared-middle-object guard, so it could not match that pair
of runtime presentations.

One typed left-unit instance now recognizes precisely those two
presentations in ordinary transfor composition. Both actual F and G occur
in the stable endpoint and the raw identity. The result retains the actual
incoming transformation. General unit guards, whole horizontal action,
precomposition accumulation, core signatures and unification rules are
unchanged. No operational equality argument or new operational constructor
is introduced.

The direct core control checks the unit computation. A typed `eq_refl`
checks the overlap with the existing right-unit cut at proof time; an
arbitrary endotransformation is a negative control. The actual family
reviewer checks both whole-triangle observations and the retained
modification maps.

## Rejected experiments

An extra identity case on the precomposition-action head did not repair
the actual consumer, before or after changing its source position. A
broader attempt to retain that whole head and expose three projections
regressed the existing successive-prewhiskering and adjunction views.
Extending the old identity-only accumulation and wildcarding inferred
projection classifiers did not resolve the latter view. These experiments
were discarded; their receipt/source hashes and failure locations are in
the verification record. None of those broader precomposition changes is
in the selected source.

The final core diff against the preceding checkpoint consists only of the
selected unit-view fragment. Reversing the diagram-profile substitutions,
the corresponding closure references, the identity-source pattern update
and reviewer carrier annotations recovers all three original source files
modulo whitespace and comments. The derived proof bodies are preserved.

## Validation and continuation

The complete original reviewer passes all 9 positive and 4 negative
assertions in 35.738s, with maximum child RSS 3156448 KiB. The combined core
controls pass 281 positive and 81 negative assertions. The original
matching/glue/affine-glue dependency chain passes on the same final core in
45.467s. Core checks use 240s/2GiB/o=20; library checks use 300s/4GiB/o=20.
Subject reduction, serial execution, file limits and no-swap containment
remain enabled. No resource ceiling was increased.

The changed owners have no unreviewed generic LHS-audit candidates. The
unit rule deliberately discriminates on the ordinary mapping category and
the canonical stable precomposition endpoint; both inferred compound slots
are annotated and were manually reviewed.

There are 27 added warning bodies: unit/identity degenerations, composition
and constructor normalizations, inverse normalizations, alternative identity
classifiers, product mapping-category normalization and component
projection. The typed unit diamond and concrete consumers pass. These
records do not establish global confluence for every constructor or
projection order.

Continue the original ordinary homology and adjunction-family consumers
with their actual corrected diagram profiles. Terminal/initial and native
K/Q zero-column integration remain outstanding. Production promotion,
remaining libraries, redundant strict wrappers, full central checks and
catalogue/health/CI/source-pin qualification remain required. The separate
application-equivalence goal stays paused.
