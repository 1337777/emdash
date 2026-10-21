# Adjunction records and original H-map record consumers

Date: 2026-10-21 UTC
Status: qualified non-library staging; production promotion remains open
Predecessor: `d9729564`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Original construction retained

The original kernel/cokernel cancellation and ordinary-record derivations now
consume native oplax diagrams. They reuse the existing native reflection and
fixed-evaluation operations, keeping their selected K/Q, lift/colift centres,
reconstruction proofs and all-test contractions. The record constructors and
fields are not redesigned; `HomologyRecord` and its raw annihilator input
remain byte-identical to the source pin.

The two arbitrary-diagram zero-input adapters retain the actual supplied
diagram. Their original ordinary reconstruction maps and inverse are mapped
through the existing `one_cat_diagram_oplax_include_func`. The ordinary diagram
is decoded for that map action, and the intermediate walking diagram is
encoded for the native coefficient. No equality cast, new selected diagram,
new primitive or caller coherence is introduced. Both original endpoint
runtime assertions still reduce to the supplied arrow b.

Seven expressions in the chain-pair record owner and reviewer needed the same
ordinary-to-native outgoing-diagram encoding already used by the upstream
`chain_pair_native_transf`. Its producer remains ordinary; only its native
consumer positions change. The whole H object, original pair indices, actual
boundary and original record endpoints remain. The H-map action and its next
Hom action continue through the original whole functor.

This slice retains all 27 original declarations across eight newly staged
library files, and all seven complete original reviewers. Two library files
and the model-observation reviewer are unchanged. No runtime or unification
rule, operational primitive, stronger hypothesis or additional supplied
comparison is introduced. Ordinary record/path evidence is retained from the
original library; it is not added to foundational operational symbols.

The [adapter](production_homology_records_migration.py) uses the existing
bounded profile and point-observation authoring helpers with source hashes and
exact replacement counts. The [zero-input fragment](production_zero_diagram_record_inputs.lpfragment)
keeps its two mapped reconstruction bodies explicit. Emitted LP is checked
at the original owner positions; the authoring script is not a proof checker.

## Validation

The [combined original reviewer driver](production_homology_record_regression.lpfragment)
passes **35 positive assertions and all imported declaration bodies**:
32 original assertions across the seven reviewers and three imported
assertions. All original polarities are retained. These include runtime
object/map/centre projections, raw boundary reconstruction, all-test uniqueness,
record endpoints and whole H-map/next-Hom action.

Receipt: `20261021T140005Z-43ebdd748a4743f0945feab797a0df1b`.
Wall time: **109.275s**. Maximum child RSS: **754,816 KiB**.
The explicit profile is 180s/2GiB with `o=20,v=1024`, subject reduction,
warnings, the 64MiB file cap, serial execution and no-swap guard. The isolated
batch-snapshot checker is used; the installed checker and normal defaults
remain unchanged. This is a smaller consumer scope than the preceding large
column check, not a matched claim that overall normalization has improved.

The recorded failures distinguish the old cancellation profile, a missing
direct observation import in the adapter, and an ordinary outgoing diagram
passed without its native encoding. The zero-input and adjunction-record
reviewers had already passed before the last of these failures. Their original
assertions remain in the final combined run.

The final run has 2,300 warning bodies. All three earlier development scopes
have the same 2,284 bodies; the sixteen additional bodies arise when checking
previously unreached Freyd composition/addition representation action. They
are existing action-versus-identity overlaps, already present verbatim in the
preceding qualified native column scope, with byte-identical source owners.
Exact logs and bounded hashes retain the branches. This is not a new-rule or
global-confluence claim.

Every fresh input matches emission, including the tracked combined driver.
All 422 files from the preceding qualified scope remain byte-identical. The
new library owners contain no formal rules, so previous core/library receipts
retain their original scope and runtime profiles; they are not reported as
fresh checks of the expanded library. The new consumer run qualifies this
addition. No unrelated aggregate is rerun merely for reassurance.

Coverage reaches **322 library/core files and 115 complete reviewers**.
The full central diagnostic is an additional staged file with the same five
terminal runtime exclusions. There remain 469 registered core/library files
and 481 reviewers unstaged. These are coverage counts, not effort estimates.

## Continuation

Continue with `examples/one_cat_image_coimage_factor_reconstruction.lp`, which
uses the now-qualified semantic boundary-factor observations. Its separate
whole factor programs and reconstruction assertions need their own migration
qualification; the earlier general image/coimage work does not replace them.

The five terminal Homd runtime obligations, remaining migration,
normalization/usability, supported checker/resource profiles and production
source-pin/catalog/health/prose/CI gates remain required. The separate nerve
goal remains paused. No production source or final qualification is promoted.

Replay with `production_owner_migration.py`; copy the tracked combined driver
to `homology_record_regression.lp` in the emitted package and run it with the
recorded profile. The [verification record](production_homology_records_verification.json)
retains exact receipt/source/authoring hashes, declarations, original assertion
polarities, failed variants and warning comparisons. Recheck affected boundaries
when their source, checker or runtime profile changes.
