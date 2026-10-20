# Retained reviewers and cokernel-family profile migration

Date: 2026-10-20
Status: staged slice qualified; production and the overall goal remain open
Predecessor: `0d5207e5e84d3e65bb2a5ca35d76736d6eb9ceb8`.

This continues R10/R13 in the
[living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
The [verification](production_retained_reviewers_verification.json) records
the exact selected inputs, source adaptations, failed development variants,
final receipt and registry coverage. The [43-reviewer import target](production_retained_reviewers.lpfragment)
retains original reviewers; it adds no mathematical declarations or assertions.

## Missed dependency and correction

The registered-consumer inventory identified 43 staged reviewers without
execution evidence against the current core. Their first combined run stopped
in `emdash3_2_cokernel_adjunction_families.lp`: its four original definitions
still used the old arrow-diagram category and dimension-one opposite terminal
hypothesis. The upstream cokernel adjunction already used oplax diagrams and
the total opposite. This was an incomplete consumer migration, not a new
foundational obstruction.

The existing four cokernel-family definitions now use
`Functor_oplax_cat WalkingArrow_cat C` and `TerminalObject(TotalOp_cat C,t)`.
Their formulas remain composition with Q, prewhiskered counit, Q applied to
the original cocone, and their composite colift. The two original whole
image/coimage factors receive the same classifier changes and use the
existing oplax diagram evaluations. Actual P/Q selections, units/counits,
mate inputs and the OneCat hypothesis remain intact.

The corresponding `one_cat_adjunction_family_views` reviewer keeps its two
named proofs and all 26 assertions (18 positive, 8 negative). Its kernel and
cokernel observations use the same corrected diagram coefficient and the
existing OneCat closure for that coefficient.

Two final generic shape-action observations require a separate change. Their
input remains `D : B → Functor_cat(I,C)`. The actual `diagram_family_transf`
now returns an oplax transformation across B. Its composition therefore lives
in `Functor_oplax_cat(B,C)`, whose objects encode ordinary functors through
`OddDual_func`. The assertions state those encoded endpoints explicitly;
their fixed evaluations remain ordinary. A blanket evaluator replacement
and a subsequent unencoded endpoint attempt failed and were corrected. The
negative still distinguishes the original v from the independent v₀.

There is no new primitive, rewrite, unification rule, operational equality
argument or strictness premise. Existing proof expressions are retained;
only their classifiers, the relevant evaluation/closure names, and the
explicit encoded endpoints change. The migration recipe reproduces the
checked three files byte-for-byte at their original module positions.

## Validation and scope

The combined target passes all **43 reviewers / 654 assertions**, with subject
reduction and all warning output enabled. Receipt:
`20261020T214300Z-8ae4a93c118a46308c2a940c36f79a5e`.
It uses the already reviewed isolated batch-snapshot checker, source-only
loading, serial execution, 600s/4GiB/o=20, 64MiB file limits and no swap.
Actual use is **91.300s / 1,618,924KiB** (about 1.54GiB). The existing 4GiB
profile was retained from the full-context run; no normal defaults change.

All 152 recorded source/package inputs match the emitted package after the
authoring recipe is updated. The 2,176 critical-pair bodies are inventoried;
none has an owner in the three changed files, which contain no rule commands.
The original first-stop receipt and focused development failures remain
recorded. One mistakenly launched unchanged rerun after a preparation-script
failure was stopped; it supplies no qualification evidence.

The prior core, cubical, combined, library and full-context receipts rehash
exactly: the three corrected files were outside those closures. Together with
the new receipt, they cover all **60 currently staged registered reviewers**
and **152 registered core files**. The remaining staged core file is the
central diagnostic, whose separate all-import target passes with exactly the
five terminal-runtime exclusions. Those five remain required and unresolved.

The full registry contains 792 core files and 596 reviewers. **639 core files
and 536 reviewers are not yet staged by this migration recipe.** This inventory
does not classify them as broken or exclude them from compatibility work.
It does rule out claiming repository-wide migration from the current staged
passes. Their producer/consumer inventory and applicable migration remain
open before any corresponding qualification claim.

Replay after a relevant change: emit with `production_owner_migration.py`, copy
the retained fragment to the emitted package as `remaining_staged_reviewers.lp`,
and run the bounded source checker with the recorded isolated binary/profile.
Do not rerun unchanged qualified scopes for reassurance. Next inspect the
existing Sigma fibre-inclusion/zero-cone consumer route, while keeping the
terminal runtime obligations, supported-checker qualification and production
promotion open. The separate nerve-development goal stays paused.
