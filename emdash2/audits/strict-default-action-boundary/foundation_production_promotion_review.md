# Foundations source promotion

Date: 2026-10-25. Status: applied locally; final integration remains open.

The qualified candidate is now installed in the active source paths of
`goal/strict-functor-duality-v3.2`. No merge or publication occurred.
The [verification](foundation_production_promotion_verification.json) records
all 1,388 original registered files: 648 changed and 740 unchanged.
Every promoted source hash matches that record. The initial StrictTransfor
carrier relocation is preserved, and unrelated historical audit files remain
untouched and unstaged.

The three supported-checker receipts jointly cover the complete source:

| Scope | Receipt | Result |
| --- | --- | --- |
| 596 original reviewer files and their dependency closure | `20261025T125439Z-7e8faf12f944433a8d1d626b4fa94346` | Passed; 4,284 positive and 630 negative reviewer assertions; 2,726.236s, 5,511,628KiB. |
| 15 remaining library owners and their dependencies | `20261025T134130Z-9493bf1c091242d5ad568b76b0cd20a7` | Passed; 1,001.482s, 3,296,956KiB. Together with the reviewer closure, covers all 791 library owners. |
| Actual central diagnostic | `20261025T140330Z-b1d00426c42742c2806f4696f1f51bc2` | Passed; all 2,441 assertions, including the five approved terminal comparisons; 500.367s, 2,553,648KiB. |

These runs preserve subject reduction and source checking. The supported
binary is identified in each receipt; its build and checker-boundary controls
are recorded in the [toolchain review](foundation_supported_checker_review.md).
The separate complete-library warning run and its warning dispositions remain
in the [library review](foundation_complete_library_review.md). None of these
checks proves unrestricted confluence or consistency.

Three recorded nonsemantic adjustments followed qualification: a core comment
refresh and whitespace cleanup in two files. The active core then passed
fresh in 35.426s under 90s/2GiB, receipt
`20261025T143049Z-533acc6281664a6c88bd79eb55372231`. The verification retains
both checked and promoted hashes rather than replacing receipt inputs.

Registry, strict catalog, core TOC, inferred-slot and report-lifecycle checks
pass. The central diagnostic now has an explicit 900s/4GiB profile, justified
by its measured runtime and memory above; other profiles and normal defaults
are unchanged. Full production health is running. Its generated report and
the final CI result remain pending, independently of the source qualification.

The TypeScript boundary is substantive: the frozen dependent-target contract
still names `G : Functor(K,Op(Cat_cat))`, while the migrated varying-base
classifier uses `Op(Cat_cart)` and Cartesian diagram maps. A focused baseline
passes the old dependent-target compilation tests but fails the live-authority
hash check (14 passed, 1 failed). This is expected stale-profile evidence, not
qualification of that old contract for the new kernel. Review the source
signatures, rules and consumers before changing pins; do not weaken the check.

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
and [follow-up ledger](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
retain the remaining integration, book/article and subsequent legacy-nerve
continuations. This checkpoint preserves a qualified mathematical source
boundary while those required stages continue.
