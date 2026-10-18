# Bounded migration SOP and performance review

Date: 2026-10-18 (UTC)
Predecessor: `c809b9c9`
Status: review and local corrections checked; broader migration remains active
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_hygiene_review_verification.json)

The user requested an overall checkpoint review for local rule, projection
and performance problems, while preserving the migration scope. The review
covered the advisory inferred-slot audit across 76 changed source files,
transparent-name patterns in the core, the changed unification interfaces,
and matched source timing. It found one failed runtime computation and
three redundant strictness rules. These are local implementation changes;
no signature, primitive or unification rule is added or changed.

## Rule ownership and retained computation

The raw composition rules for `Op_prof_func`, `Prof_imply_cov_func2` and
`Prof_imply_cov_func` are literal instances of the restored generic strict
functor law. The earlier runtime review had already tested their removal
but left actual-consumer qualification open. Their removal now passes the
current weighted/profunctor consumer. Projected reindexing, transfor action
and strict-transfor rules remain: those can lose the generic pattern during
projection and are not redundant for the same reason.

The whole fixed-weight implication definition remains opaque, preserving
its stable action head before its defining product pipeline unfolds. Its
existing object projection remains unchanged. Only stale comments about
the old lax default are updated.

The core scan found two transparent names inside runtime patterns. The
`id_funcd` instance in Pi identity computation passes its intended direct
check and is retained. The represented-Sigma fold involving `hom_int_view`
fails its intended whole runtime comparison. That is a migration defect,
not a new requirement for categorical structure.

`hom_int_view` is a defined composition of the Cartesian inclusion and the
stable `hom_int` owner. Expanding only that alias in the pattern still
fails: existing normalization first reassociates the inclusion to the
left. The final correction matches that actual normalized composition at
the original Sigma composition owner. The original RHS and every actual
argument, including the outer functor F, remain unchanged. No new runtime
associativity rule, conversion between coefficient universes or operational
cast is introduced.

The qualified controls check the whole Sigma fold, object-first evaluation,
the retained Pi identity, and failure when the outer F is replaced by a
different functor. Together with the inherited core controls they pass
279 positive and 80 negative assertions. The new proof-time interfaces are
unchanged, including the distinctions between ordinary and Cartesian maps
and between dimension-one and total duality.

## Audit scope and limits

After the correction, the generic inferred-slot audit reports zero
unreviewed candidates across 1109 runtime commands in the 76 changed files.
That scanner does not cover every owner-specific argument; the two alias
patterns and the changed Sigma owner were inspected and exercised directly.
The new Sigma pattern uses the actual inclusion and stable Hom head; it
does not pattern on a transparent convenience alias.

The core has 141 unification rules, 70 textually changed from the pre-goal
source. The review inspected the long stable-head comparisons and the two
variable-sided conclusions. Those two conclusions are unit laws with
explicit endpoint and identity constraints, not unrestricted equations.
The large displayed-Hom point comparison keeps its stable left head and
proof-time semantic reading. No unsupported global strict naturality or
operational equality payload was added by this review. This bounded audit
is not a proof of confluence or semantic consistency for the full source.

The weighted consumer's warning multiset drops from 2415 to 2367: 48 bodies
removed and none added. The Sigma pattern repair itself changes no warning
bodies. Its effect is demonstrated by the previously failing whole consumer,
which is why a zero-candidate advisory audit alone would have been insufficient.

## Matched performance evidence

Both cores were checked source-only with the same checker, subject reduction,
warnings, `--record-time --too-long=0.05`, 240s/2GiB and
`OCAMLRUNPARAM=o=20,v=1024`.

| Source | Wall time | Peak child RSS | Rewriting timer | Warning bodies |
| --- | ---: | ---: | ---: | ---: |
| Pre-goal core at the pinned commit | 4.442s | 326.3 MiB | 3.10s | 648 |
| Current migrated core after the review | 17.064s | 1426.0 MiB | 14.36s | 1963 |

The runtime rule-command counts are 743 and 990; the corresponding unification
counts are 91 and 141. The migrated core performs more normalization and
overlap work. The rewriting timer includes checker normalization and
conversion; it is not solely application evaluation. Individual measured
commands top out at 0.49s and are distributed across existing rules and
derived declarations. The trace does not identify one runaway command.

These are single matched samples, not a benchmark distribution. The small
before/after cleanup timing difference is not claimed as a robust speedup.
The exact overlap reduction and restored Sigma computation are the concrete
improvements. The larger aggregate's retained import footprint remains an
integration constraint; this review does not claim that a 6 GiB central
check has become unnecessary or that full performance qualification is done.

## Consumer continuation

The final weighted/profunctor consumer passes in 23.221s. The original
commutative-algebra locality owner passes in 25.601s, and the affine-atlas
dependency closure passes in 48.540s. These retain the complete original
library sources and use the current migrated core. The affine-atlas closure
does not include matching or glue; those remain the next algebra consumers.

Continue with those focused owners and the remaining central imports.
Avoid repeating the entire cumulative aggregate for every small adjustment;
the final central, catalogue/health/CI and production-promotion gates remain
required. Optional foundational redesign, a general coefficient-theory
expansion and the separate application-equivalence goal remain outside this
review. Unrelated worktree changes were preserved.
