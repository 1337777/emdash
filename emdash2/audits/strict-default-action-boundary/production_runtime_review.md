# Runtime and rule review after the time-limit approval

Date: 2026-10-16
Status: qualified adjunction inferred-slot repair and measured diagnosis; weighted inverse computation remains open
Plan: [strict-functor/duality migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Predecessor: `8700b64c`
Evidence: [source pins, receipts and warning comparison](production_runtime_verification.json)

## Scope and resource policy

The user approved the pending 300-second experiment and requested that future
measured, bounded resource adjustments not need separate permission. The root
and nested AGENTS and DevOps guide now state that policy. The default remains
90 seconds / 2 GiB. All experiments here keep 2 GiB, the serial lock, no-swap
scope, 64 MiB file limit and subject reduction. No compiled objects, checker
patch, host power change or unrelated process termination is involved.

Memory containment protects the host applications. The deadline detects hangs
and unusable cost; increasing it is diagnostic headroom, not a performance fix.
The registry already contains measured 180- and 300-second profiles. The guard
supports up to 600 seconds / 8 GiB, but those ceilings do not select a profile
automatically. Memory increases require measured need and host headroom.

## Identical-source timeouts and fresh measurements

The timed-out core imports and the earlier successful owner import have the
same core SHA, `0fe8e804096779b4abce40d9241c4aa8ce966238c51f89c749fbc782a257d5ea`.
The last emitted warning locations in the timed-out runs vary from line 13812
to 18677; they do not identify one repeatedly stuck command. A prior live
sample found the busy checker on a CPU reporting about 400 MHz. That is an
observation, not a diagnosis of throttling or power policy.

After approval, the unchanged final weighted driver reached its assertions in
24.49 seconds, then failed its new public-result inverse assertion. Thus the
resource obstruction had hidden an unqualified computation; it had not proved
that computation correct. No extra time was needed on this run.

The source comparison uses the pinned original core at
`f8af1fca472657ff1598c639eb29c0566e7b2ec0`, not an approximate historical copy.
Both cores were checked serially with the same binary, warnings and SR enabled,
`o=20,v=1024`, `--record-time --too-long=0.5`, 300 seconds and 2 GiB.

| Source | Wall seconds | Peak child RSS, MiB | Reported rewriting seconds | Unjoinable pair reports |
| --- | ---: | ---: | ---: | ---: |
| Original core | 6.27 | 326.9 | 4.43 | 648 |
| Migrated core before the guard fix | 21.38 | 1118.1 | 17.71 | 1938 |
| Isolated removal of three duplicate raw composition rules | 20.36 | 1094.6 | 16.80 | 1890 |

The third run lowers the reporting threshold to 0.05 seconds. These are single
runs, not a benchmark distribution; the small wall-time difference is not a
robust speedup claim. The structural overlap reduction is exact. The original
and migrated cores have 743/964 runtime rule commands and 91/114 unification
rules respectively; a command can contain several clauses.

The installed checker's matching source was inspected at
`/home/user1/.opam/default/.opam-switch/sources/lambdapi`, commit
`db4f7809961b8c107247613067fb567491fb0b84`. In `src/handle/command.ml`, rule
handling checks SR, updates decision trees and checks local confluence. The
`Rewriting` timer in `src/core/eval.ml` covers normalization/conversion calls;
it does not isolate only application evaluation or only critical pairs.
The top individual commands in the finer trace take 0.27–0.50 seconds and are
distributed over rule checking and derived declarations. Consequently the
evidence supports increased normalization/overlap cost, not one demonstrated
infinite loop. It does not fully explain the earlier greater-than-90s runs.

## Concrete migration defect: reducible inferred guards

The mechanical Op-to-total-Op adjunction migration retained patterns such as:

```text
rule @Op_adjunction (TotalOp_cat B) (TotalOp_cat A) _ _
       (@Op_adjunction A B _ _ adj) ↪ adj
```

Previously `Op_cat` was a primitive pattern head. `TotalOp_cat` is now a defined
alias. Its occurrence in these inferred slots prevents canonical involution
from computing; the failing query also triggers irrelevant unification search.
The same inferred slots occur in the unit/counit rules.

Replacing just those four inferred slots by `_ _ _ _` in each of the three
clauses repairs the consumer. The inner `Op_adjunction` retains the semantic
discriminator and all original RHS data. Types, lax unit/counit admissibility,
T/O distinction and the selected inverse data do not change. This is the SOP's
existing pattern discipline applied to a missed owner-specific head. The
generic LHS audit had reported zero candidates because this head is outside
its list; the SOP now makes that limitation explicit.

The full owning source plus canonical involution and unit/counit observations
passes in the isolated copy. Warning comparison removes nine old pair bodies
and adds three nested-adjunction overlap bodies (1938 to 1932). The
[focused controls](production_adjunction_guard_controls.lpfragment) also check
typed package-first and expanded projection-first readings of those overlaps.
The complete emitted core and inherited controls pass 255 positive and 60
negative assertions in 13.740 seconds at 90s/2GiB. This includes six new
focused observations; exact regenerated input bytes match the successful
receipt. No speedup is inferred from this unprofiled run versus profiled runs.

## Inherited defect: composite inverse normalization

The new weighted public-result inverse test fails after the imports complete.
A [smaller reproducer](production_defiso_composite_failure.lpfragment) using
only the original core also fails. It is an intentionally failing non-library
audit, not a positive reviewer or an intended mathematical counterexample. If `i:x≃y` and
`j:y≃z` are `DefIso` values and `r:w→x`, postcomposing by the forward composite
and then its inverse normalizes to a term with the shape:

```text
post(i⁻¹ ∘ (j⁻¹ ∘ (j ∘ i)), r)
```

The available adjacent inverse cuts cannot see through this bracketing.
Associativity is deliberately a proof-time comparison, not runtime
reassociation. Even typed reflexivity does not chain the required comparisons
in this reproducer. This is a computational closure gap of the existing
`DefIso`/postcomposition owners, not a new mathematical obstruction to Homd or
a failure of the T-versus-O repair.

The weighted result has a larger instance of the same problem. Its normalized
expression also expands the new automatic legacy `IsStrictFunctor` adapter
inside retained mapped-inverse terms. That is a reason to prioritize the
already planned strict-wrapper retirement: a default-strict functor should
map the comparison directly, with the old classified API as a compatibility
view if still consumed. It is not a reason to introduce more caller evidence.

Do not conceal the failed test by making the theorem opaque or by asserting a
weighted-colimit-specific inverse cut. Trace and repair the shared inverse
owner's projection order first. A global runtime associativity rewrite would
be a separate normal-form migration and is not justified by this review.
The final weighted inverse controls remain failing/pending; the original
weighted reviewer itself completed successfully within the later diagnostic
import. No completed weighted slice or full foundation migration is claimed.

## Redundancy review and next boundary

The raw `Op_prof_func`, `Prof_imply_cov_func2` and fixed-weight
`Prof_imply_cov_func` composition clauses are literal instances of the restored
generic strict functor law. Their isolated removal passes the full core and
reduces overlap reports, but does not remove most of the added cost. Their
retirement still needs their actual consumers; the experiment is not promoted.
Keep projected rules such as `Prof_reindex_transf` separate: projecting away
`fapp1_fapp0` can erase the generic rule's matching head, so those are not
automatically redundant. Keep strict-transfor rules separate too; strict
functors do not make arbitrary transfors strict.

Continue with the narrow adjunction guard correction, then the shared inverse
normalization/wrapper boundary consumed by the weighted proof. The review gives
no reason to restart the selected Homd/duality design. Remaining source cost
and known nonconfluent observations require explicit qualification; a passing
core or a longer timeout is not a consistency or usability certificate.

## Replay

From `emdash2`, emit the qualified source and run its bounded consumer:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20,v=1024 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet rule_hygiene_full_controls.lp
```

For matched source timing, check `emdash3_2.lp` in the emitted `baseline_package`
and `package` serially with `EMDASH_LAMBDAPI_FLAGS='--record-time --too-long=0.5'`.
Use the same runtime and limits for both. The expected-failure inverse fixture
can be copied to `inverse_review.lp` in the baseline package and checked through
that package root. Its final typed reflexivity assertion should fail at the
recorded source pin; a future success is a signal to revisit the diagnosis.
Do not rerun these comparisons during unrelated work or treat the deliberately
failing fixture as a required positive library gate.
