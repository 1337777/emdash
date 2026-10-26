# Shared covariance and identity Homd frontend computation

Date: 2026-10-26. Follows `49c1a4c5`. Native source is unchanged.
The [acquisition](foundation_frontend_homd_identity_acquisition.json) pins
eleven native declarations and eight existing runtime commands. The
[verification](foundation_frontend_homd_identity_verification.json) records
input hashes, native receipts and focused consumers.

## Whole identity consumer

The mixed Homd frontend now imports the native conjoint/mate owners and the
defined `homd_id_src_sec`, `homd_id_src_func`, `homd_id_tgt_func` and
`homd_id_` rungs. Starting from the existing `homd_id_int(E)` root, an
explicitly typed consumer projects x/u, then the whole y-section, then v/f.
It computes to:

```
Hom_E[y](E[f](u), v).
```

The test infers each constructed rung, compares the whole source section and
target functor with the native named rungs, and rejects a v from a different
family. Its section remains the actual iterated Hom in `Functor_cat(K,Q)`;
there is no enlarged `(y,v,f)` base, final curry construction, independently
supplied comparison or operational equality-proof parameter.

This qualifies the identity root-to-leaf frontend computation. It does not
qualify every higher action or the general-FF relative endpoint. Those retain
their separate native owners and remain required transfer work.

## Ownership and projection review

The four FibCov declarations move from the later PathInd transfer into this
shared layer with their original Core names. Three covariance projections
move with them; their inferred argument slots follow the native rules. The
old PathInd FibCov object-fold rule is removed: its consumer passes using
the existing transparent definition and generic Hom projections. PathInd now
adds only its two local opaque declarations, six local runtime rules and
five local definitions. Its compatibility linkage references the shared
declarations; it does not declare or compile a second covariance theory.

Ordinary functor-opposite involution and the mate/conjoint projections are
existing native rules. The direct mixed source-action finalization now uses
the actual extended declaration prefix. No generic checker behavior, native
rule, public mathematical contract or FF profile changes.

An existing relative-root spelling comparison needs more beta steps after
the identity root gains computation. Its focused bound is raised from1024
to4096 and the original equality is retained. No default comparison budget
changes. Higher identity and relative action should continue through the
native operation ladder, without direct endpoint shortcuts.

## Evidence and limits

The native counterpart passes20 positive assertions and one wrong-fibre
negative: eleven signatures, five exact definition bodies and four whole
ladder computations. Its first60s run timed out without a reported typing
error. The exact emitted bytes pass a guarded120s replay in40.090s at
170,028KiB maximum child RSS, with subject reduction and the same2GiB cap.
No runner/SOP default changes. All1,886 imported warning blocks are unchanged
from the preceding qualified prewhiskering consumer, including1,704 critical
pair warnings; this is warning preservation, not a confluence certificate.

Focused TypeScript results: six mixed-Homd cases pass; all17 non-native
fixed-source PathInd cases pass; the downstream prewhiskering, mixed source
action and whole PathInd run passes20 cases. Native opt-ins skipped by these
focused runs retain their separate scope and receipts. The verification
preserves initial test-harness/count/budget failures and their repairs.

The previous full TypeScript aggregate remains a failed snapshot with47
failures. This tranche does not supply a new complete aggregate or residual
failure count. General-FF target/diagram action, remaining authoring/source
reviews, production health and final integration are open. Book/article and
adapted legacy nerves follow the consolidated plan's dependency gates.
