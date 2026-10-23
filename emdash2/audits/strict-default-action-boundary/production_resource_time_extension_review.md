# Reviewed time ceiling for the foundations library check

Date: 2026-10-23 UTC
Source checkpoint: `85c8fa0e`
Status: qualified tooling extension; no mathematical promotion

The foundations library scope reached the existing 600-second cap twice,
at receipts `20261023T015237Z-625afea149f742a387ea00211dcb2e8a` and
`20261023T021441Z-0aaab024b55440f58c3783e0799d7bc6`. Both stopped in the
same Hom-comparison/adjunction dependency region without a reported typing
failure. These are incomplete checks, not successful migration evidence.

The library driver and its other mathematical inputs match the earlier
successful scope. Its formerly 13–27 second Hom-comparison commands now take
approximately 17–37 seconds in this full context. Their isolated owner costs
are much smaller. These measurements do not identify a single complete cause
of the full-context slowdown.

Before extending the deadline, the actual comparison rule was made more
selective. Isolated allocation traffic changed from 12.79 billion words for
the loose side-condition pattern to 11.39 billion for the consumed literal
composite pattern, close to the 11.26-billion removal/checkpoint controls.
All of those isolated owner runs pass. Minor-heap experiments reduce
collections but do not materially improve the observed owner runtime. The
large reservation without a domain bound is rejected at startup by the
existing address-space cap; no mathematical check runs in that case.

Under the user's standing authorization for measured per-target extensions,
the shell guard, receipt runner and registry now accept an explicit deadline
of at most **900 seconds**. The immediate consumer is the unchanged full
foundations library driver, to be retried with **900s/4GiB/o=20**. This changes
time only. No registered profile or normal default is changed: the defaults
remain **90 seconds and 2 GiB**, the maximum memory setting remains 8 GiB,
and file/core/no-swap/serial restrictions and subject reduction remain enforced.
The GC experiments are not installed as defaults or selected for this retry.

Focused tests cover the newly accepted boundary, rejection at 901 seconds,
the runner's millisecond boundary, registry bounds, unchanged defaults and
the existing containment/serialization behavior. The registered formal smoke
targets exercise the updated runner on their existing profiles. All fifteen
guard/runner/registry tests, thirteen DevOps tests, the 1,388-target registry
check and all three registered formal smoke targets pass. The
[verification](production_resource_time_extension_verification.json) records
their source hashes, exact receipts, profiles and checker identity. No checker
binary, formal source or mathematical acceptance criterion is changed by
this tooling slice.

The broader normalization/usability investigation remains open. A successful
longer run will establish execution of its exact required scope; it will not
establish acceptable core performance or complete the foundations migration.
