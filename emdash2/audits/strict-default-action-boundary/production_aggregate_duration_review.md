# Cumulative library replay duration

Date: 2026-10-23 UTC
Status: qualified guard/runner/registry extension; mathematical aggregate pending
Source checkpoint: `aa8f8a35`

The user clarified that a repository-wide aggregate can reasonably take many
minutes and that 900 seconds has no special mathematical significance. The
existing SOP already applies bounds to each checker invocation, not to the
sum of all children in a suite. The current foundations library replay is a
single process importing hundreds of modules, so it needs a cumulative bound
appropriate to that scope.

The explicit supported ceiling becomes 1800 seconds. The selected replay uses
1800s/4GiB/o=20; the normal 90s/2GiB defaults, every named profile and the
8GiB maximum memory ceiling are unchanged. Serialization, file/core limits,
no-swap containment, hard termination and subject reduction are unchanged.
This is aggregate-scope headroom under the user's direction, not a permanent
workaround for transient host load or a claim that slow individual commands
are acceptable. No checker binary or mathematical source changes in this
slice. The earlier 900-second review remains historical evidence.

The focused tests cover the new upper boundary, rejection above it, duration
syntax, runner/registry agreement, unchanged defaults and existing resource
containment. Fifteen guard/runner tests, ten registry tests, thirteen DevOps
tests and the 1,388-target registry inventory pass. The three existing formal
smoke targets pass under their unchanged named profiles. Their exact outcomes,
profiles and source snapshots are recorded in the
[verification](production_aggregate_duration_verification.json). The registry
and its named profiles remain byte-identical to the preceding checkpoint.

Performance remains a separate R12 obligation. A matched isolated
`zero_arrow_family_action_paths` check passes on both the preceding qualified
snapshot and the current mathematical candidate. Allocation rises from about
12.34 to 18.08 billion words. Removing the new prewhiskering-metadata comparison
in a private diagnostic barely changes that allocation, so the removal is not
adopted. This rules out that one comparison as the dominant isolated cost; it
does not settle the broader import-context cost or the effect of host load.

The full-library scope and its assertions remain intact. Qualification still
requires completion of that scope and exact-input/warning review. A successful
longer run will prove execution of the selected scope, not mathematical
confluence, acceptable performance of every owner, or production readiness.
