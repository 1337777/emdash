# Recursive displayed-chain frontend migration

Date: 2026-10-25. Focused/native scope qualified; complete frontend integration remains.

Family fibres, transports and displayed-cell signatures now use the native
`Cat_cart` coefficient. The earlier `Const_func` declaration and object action
are reused. The checked `Obj_func` mirror remains the existing bounded
presentation; this migration does not redesign it. Native Sigma map/section
owners retain general displayed FF and their internalized arrow action.

Recursive weakening uses `section_weaken_funcd`, including its native
base-arrow projection. The removed runtime conversion from generic projection
pullback to `Sigma_proj1_pullback_catd` is not restored. Chain authoring
explicitly selects the stable projection-pullback owner when forming its
context, with exact native head, plicity, base and total-source checks. Raw Core
pullback terms and arbitrary substitutions retain their original presentation.

## Fresh checking with native proof comparisons

Reindexing a displayed map still produces the generic pullback presentation.
Composing it with a map in the selected stable context therefore needs the
existing native projection-pullback comparison during fresh checking. The
same-index instance of that native rule is transferred as proof-only data;
the fully heterogeneous spelling was rejected by the generic proof-rule
subject checker and was not admitted unchecked.

`createCoreLfProofCheckingChecker` applies an explicitly selected checked proof
program only to closed type comparisons. It validates the exact authority and
runtime prefix plus opaque user declarations. It records used comparison rules,
leaves the emitted term unchanged, and reports budget exhaustion as a limit
rather than a type mismatch. The ordinary checker and runtime evaluator are
unchanged. The chain frontend opts into its one native comparison; no equality
witness is carried by an operational symbol. The matching family slots of the
ordinary reindexing component rule use native wildcards, so a proof-equal
annotation does not prevent its projection from computing.

The independent generic fixture rejects the application without the selected
proof profile, accepts it with the actual comparison, preserves the exact term
and runtime non-conversion, rejects wrong arguments and foreign contexts, and
reports a zero-budget comparison limit. All17 generic runtime tests pass.

All14 chain consumer/transfer/demo tests and50 metadata/review tests pass.
The metadata negative-count mutation was updated to remain invalid after
removing the duplicate rule; historical approval snapshots are unchanged. Native conformance checks actual
serialized recursive maps, point computations and internalized cells with
general FF, ignored-variable independence, and raw/stable pullback runtime
non-conversion. It passes with warnings and subject reduction at60s/2GiB.
[Verification](foundation_frontend_chain_verification.json) records the source
and runtime evidence. The local transfer has5 prerequisite declarations,
1 section owner,5 prerequisite runtime clauses and7 local runtime clauses.
The inherited ordinary section-pullback links remain available to existing
Pathind consumers; removing those export entries exposed an import regression
which was corrected before the final aggregate attempt.

Workspace, registration, typecheck and lint pass. The complete TypeScript gate
now reaches the unmigrated chain-2A product internal-cell rule, which still
uses the old coefficient. That is the next migration boundary. No full-suite,
production-health or overall-goal completion is claimed.
