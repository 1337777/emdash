# Whole-library aggregate time headroom

Status: bounded tooling change tested; the whole-library result remains pending.
Date: 2026-10-25 UTC. Mathematical source and checker binary are unchanged.

The original 791-owner driver has 793 source/package inputs. Its 1800s/6GiB
run `20261025T043855Z-77582cb6abfe41f88cecaa226b16757b` times out after
1800.038 seconds without a typing failure. It finishes 518 owners and reaches
the Freyd native-snake matching imports. The last sampled RSS was
3,571,304KiB at 1780s; the process was CPU-active. The killed run's smaller
child-rusage measurement is not treated as its memory peak. Some dependency
imports take hundreds of seconds; these are not attributed to host load.

The user previously authorized measured time/resource extensions without new
approval requests, and explicitly clarified that a cumulative aggregate's
deadline is not a mathematical threshold. On that authority, the shell guard,
runner and registry accept explicit durations up to **3600 seconds**. This
remains a hard bound. The ordinary default remains **90 seconds/2GiB**; named
profiles and the current aggregate's 6GiB cap are unchanged. File/core limits,
serial execution, no-swap containment and subject reduction remain in force.

Validation passes: all 15 resource-guard tests, five native-pair profile tests,
five GC/profile tests, shell syntax, and the 1,388-target registry inventory.
The tests cover accepted long durations, rejection above the new ceiling,
unchanged defaults, inherited memory/file/core restrictions, hard termination,
detached-descendant containment, serialization and subject-reduction rejection.
They do not wait an hour or allocate the maximum allowed memory.

The longer aggregate is to use the same immutable mathematical snapshot and
checker with only the explicit time headroom changed. New receipts record the
updated runner/guard hashes. Older receipts remain historical evidence at
their original tooling pins. This does not qualify an uncompleted aggregate,
erase slow-construction evidence, or authorize broad unrelated checks.
