# Migrated foundations: main and parallel-worktree handoff

Date: 2026-10-28
Status: integrated local main continuation baseline; not a release or whole-goal completion
Owner: [consolidated foundations plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Source branch: `goal/strict-functor-duality-v3.2`
Original main baseline: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`
Last mathematical checkpoint before this maintenance: `fcb03ea4`

The local main worktree was fast-forwarded from `f8af1fca` to maintenance
checkpoint `7044acdd` on 2026-10-28. It was clean afterward; the `join-core`
exact assembly and the 1,388-target registry check also passed directly from
main. The following documentation receipt is fast-forwarded as part of the
same maintenance. No push or publication was performed.

The user authorized updating the correspondence and standing documentation,
preserving relevant auxiliary sources, and fast-forwarding local `main` so
new worktrees can start from these foundations. This includes local preparation
commits and `git merge --ff-only`; it does not authorize pushing, publication,
history rewriting or removing worktrees. The foundations branch remains the
active development lane. The paused legacy nerve branch is reference material,
not a branch to merge automatically.

## Mathematical and qualification boundary

Public functors are strict and ordinary transformations are conventional lax.
`Hom_Cat(A,B)=Functor_cat(A,B)`; admitted families and ordinary Hom land in
`Cat_cart`. T=`Op_cat`, R=`CoAbove2_cat`, O=`TotalOp_cat` and C₂=`CoAt2_cat`
have distinct higher action and shifted family bases. The direct Q/P identity
Homd ladder and defined general-FF extension are installed. The stronger
Cartesian profiles inside coefficients do not make every displayed map
strictly natural across its base.

| Boundary | Authoritative state |
| --- | --- |
| Native migration | Installed at `57e627b9`, with the original 791 library-owner and 596 reviewer coverage recorded in the ledger. Subsequent source changes retain their own scopes. |
| Original frontend migration | Accepted at `f0e22340`: the historical aggregate had 1,837 passes, two subsequently repaired test failures and 63 skips. The focused repair passed; the user waived another aggregate. Do not relabel the original aggregate green. |
| Book and overview article | Local update accepted at `1fe72617`; book 0.10.2-dev and overview 0.4.2-dev. This handoff does not publish either artifact. |
| Later Pi/Sigma correction | Installed at `bc37e5fc`; the forward `sigma_functord_sec_func` replaces the old whole section/displayed-functor identification. Its later frontend adaptation is **unfinished**. |
| Native nerves | Current work is isolated audit code. Whole cubical maps, native recursive simplex levels and the generic terminal-join cone are present; the remaining whole inverse, successor-action and index laws are open. Audit refinements are not silently installed production rules. |
| Health report | Refreshed source inventory only, using `check_metrics.py --no-check`. No new full-library typecheck is inferred from that report. |

The [current obligation ledger](EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
owns the outstanding gates. In particular, this is a **development baseline**,
not a claim that the full frontend/native cross-layer suite or the nerve goal
is finished. A new TypeScript task must read the
[elaborator handoff](TYPESCRIPT_ELABORATOR_V3_2_HANDOFF.md) and retain source-pin
failures as evidence. The later
[18-file frontend candidate](../emdash2/audits/pi_sigma_section_profile/frontend_candidate.json)
and its patch are tracked, marked incomplete, and must be adapted and qualified
rather than applied blindly or accepted by advancing hashes.

## Tracked sources and auxiliary inventory

| Material | Location / recovery |
| --- | --- |
| Mathematical authority | `emdash2/emdash3_2.lp`, registered extension owners, `checks.json`, diagnostics and reviewers. Registry review finds 1,388 targets with 1,388 source dependencies. |
| Standing explanations | Root and `emdash2` READMEs/AGENTS, Foundations, canonical syntax and current-status report. All seven were reviewed against the migrated profiles. |
| Correspondence draft | `emdash2/tmp/EMAIL.md` is intentionally tracked despite its directory name. Both long and short versions now state the current Homd, negative Sigma-Hom, strict default, dualities and open qualification boundaries. It remains unsent. |
| Living work and decisions | Consolidated plan, follow-up ledger, native adaptation plan and implementation outline. Historical plan/ledger snapshots preserve rejected designs without making them current instructions. |
| Current native replay | `emdash2/audits/native_nerve_foundations/simplex_core/{replay.py,verification.json}`. The current closure has 42 active source pins and 110 tracked artifacts, including parent-relative artifacts. `join-core` and `recursive-core` reconstruct exact isolated inputs. |
| Other native evidence | The surrounding `native_nerve_foundations` audit contains the walking, mixed-evaluation, cubical and pending-face sources and source-pinned recipes. Follow the current review documents; historical modes can intentionally stop on source drift. |
| Checker source patch | `toolchains/lambdapi-batch-snapshot.patch`, pinned by `toolchains/verification.json`, including upstream/patched hashes for all three changed source files. |
| Checker installation/build | `scripts/verification-toolchain.py` and its 12 passing unit tests; guard/runner/registry under `emdash2/scripts/`; CI selects the same tracked patch and manifest. |
| Workspace setup | `scripts/bootstrap-worktree.sh`, `scripts/pnpmw`, root pnpm lock and manifests. This migration does not change the package/lock graph relative to the old main baseline. |
| Recovery hook | Root `.codex/hooks.json` and `scripts/infinity_codex.py`. The hook definition is unchanged by this migration; no second nested hook is introduced. |
| Previously uncommitted experiments | Eight original files are now inventoried in [retained authoring](../emdash2/audits/strict-default-action-boundary/RETAINED_AUTHORING.md). They are historical, unselected sources, not library targets or portable current replay commands. |

The batch profile is pinned to Lambdapi commit
`db4f7809961b8c107247613067fb567491fb0b84` with patch SHA-256
`fe854f84a61a02b31b5eaa85cd9375f370d7388ac71c9ccdeae88ff565b813d9`.
The reviewed local binary has SHA-256
`94dc55766ec793e137cba7936f40e56074f4d92a02259cae8de9474c65e4677f`.
The patch releases unused CLI rollback roots in the selected batch case;
it does not turn off subject reduction or change formal rewrite semantics.
Actual build and dependency verification passed during this preparation.
Other machines must verify their own build identity; do not edit audit binary
pins merely to silence a mismatch.

Ignored logs, immutable input snapshots, generated probes, compiler objects,
node_modules and toolchain caches are not source dependencies to commit.
Recorded run IDs and hashes remain historical evidence; a new worktree can
produce fresh receipts from tracked inputs. Optional Infinity conversation
archives are not required to reconstruct the current selected code or plan.
This thread's archive is in the original main worktree; a fresh worktree may
legitimately have no archive until a session runs there.

A fresh export of 154 tracked files (2,009,110 bytes), obtained from Git rather
than the dirty worktree, successfully reconstructed the exact `join-core`,
`recursive-core` and `join-projection-proof` input scopes. No previous probe,
log, compiler cache or conversation archive was copied. This validates source
assembly portability; it is not another formal typecheck or a binary-build
reproducibility claim. Registry, workspace contract, patch/dependency checks,
toolchain unit tests, source-health inventory and document hygiene also pass.

## Starting from the fast-forwarded main

Create a new worktree only when authorized for its particular task, then run
the repository bootstrap there. Never copy or symlink another worktree's
mutable node_modules graph. With the pinned opam environment already active:

```bash
./scripts/bootstrap-worktree.sh
python3 scripts/verification-toolchain.py build-batch
python3 scripts/verification-toolchain.py verify-batch
python3 emdash2/scripts/check_registry.py
python3 emdash2/audits/native_nerve_foundations/simplex_core/replay.py --mode join-core --assemble-only
```

`--assemble-only` verifies the exact tracked recipe without invoking the
checker or requiring any previous probe directory. Omit it for the bounded
formal check after the local toolchain is built. To continue the preceding
native recursion use `--mode recursive-core`; the current next task is the
whole geometric successor action in apex and diagram. The join's actual
cell-image conversion remains a separate recorded obligation.

For fresh verification dependencies, follow [DevOps](DEVOPS.md#ci-and-reproducibility)
and the installer help rather than replacing an existing opam switch.
Build caches are reproducible and worktree-local by default. Disk space was
about 6.5 GiB during preparation, so this handoff avoids duplicating caches or
running broad aggregates for reassurance. It makes no cleanup changes.

Before and after the fast-forward, verify that main is clean, that its old
head is an ancestor, and that its final head equals the selected foundations
commit. No commit is reset or rewritten. Preserve all other branches and
worktrees. The focused native replay passed again during this preparation
in 60.436s; this is evidence for its scope, not a substitute for the ledger's
remaining integration gates.
