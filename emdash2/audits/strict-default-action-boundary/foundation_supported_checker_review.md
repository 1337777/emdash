# Supported batch-checker build qualification

Date: 2026-10-25. The tracked verification installer successfully builds and
verifies the reviewed batch checker in its isolated worktree cache. The
installed opam switch, source pin and executable remain unchanged.

The source commit is db4f7809961b8c107247613067fb567491fb0b84; the patch is
byte-identical to the [reviewed rollback-root patch](production_checker_batch_snapshot.patch).
The installer checks the commit, patch hash, exact three changed source files,
all other tracked-source changes, compiler and pinned dependencies. Compilation
uses the unchanged serial/no-swap guard at 300s/4GiB with one Dune job. The
first attempted build was correctly declined while another checker held the
lock; its verified source preparation was resumed after that run terminated.

The fresh executable hash is
`94dc55766ec793e137cba7936f40e56074f4d92a02259cae8de9474c65e4677f`.
The earlier probe hash is
`5c82cca90847fb5cc7726f52b3c6b8f2df3a89685abecac48285ae676db6bb69`.
ELF comparison finds differences only in `.debug_info`, `.debug_line`,
`.debug_line_str` and `.note.gnu.build-id`. All allocated sections other than
the build ID match, including executable code and data. The different full
binary identity is recorded; old execution receipts are not rewritten.

On the new executable, the retained CLI controls pass with their intended
outcomes: two separate input files restore their independent environments;
a single joined import rejects the deliberately false assertion; an ill-typed
rewrite is rejected by subject reduction before the second file. These checks
use 90s/2GiB and the standard guard. The earlier Pure API state harness remains
source/patch evidence at its recorded build, not a fresh execution claim.

[Exact verification](foundation_supported_checker_verification.json) retains
the build record, source identity, CLI commands/results and section comparison.
The full 596-reviewer gate is now running on this supported build. Its prior
warning-enabled run hit the 64MiB output limit while printing an expected
negative check. One earlier expected diagnostic was 34MiB. The retry uses
the runner's normal warning-suppressed output mode, with every assertion and
subject-reduction check retained. No mathematical source, memory cap, timeout
or file cap is changed. The complete791-owner warning log remains separate.
[Output-limit evidence](foundation_complete_reviewer_output_limit.json) does
not claim the failed aggregate passed or infer a typing failure from the
expected-negative diagnostic. Runtime and output profiles remain explicit.

The ordinary verifier now recognizes a selected cache only after validating
its complete source/build/binary record; a version string alone does not
admit it. The existing opam dependency/source-pin checks still apply. CI's
formal jobs build this profile and select its verified PATH inside `opam exec`.
Local replay of that exact environment passes with zero package mismatches.
Twelve installer tests and thirteen DevOps tests pass; workflow YAML and changed
Bash commands parse. No hosted CI run, global installation or publication is
claimed by those local checks.
