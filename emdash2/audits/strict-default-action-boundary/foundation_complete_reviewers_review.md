# Complete original reviewer qualification

Date: 2026-10-25. All **596 original reviewer files pass** on the supported
checker build, with subject reduction and no compiled objects. Receipt
`20261025T125439Z-7e8faf12f944433a8d1d626b4fa94346` records 1,374 exact inputs,
2726.236s and 5,511,628KiB maximum child RSS under
3600s/6144MiB, OCAMLRUNPARAM=o=20,v=1024 and the unchanged64MiB file cap.
The reviewer files contain 4,284 positive and 630 negative assertions.

The preceding warning-enabled attempt was interrupted by the file-output cap
inside an expected-negative diagnostic. This complete retry changes no
mathematical source or assertion. It uses the runner's normal `-w` output
profile, retaining all constraint solving and subject reduction. The full
791-owner warning-enabled log remains separate. This is not a timing comparison
with the earlier incomplete run, nor a claim of global confluence.

The fresh supported executable has hash
`94dc55766ec793e137cba7936f40e56074f4d92a02259cae8de9474c65e4677f`;
[its build/behavior review](foundation_supported_checker_review.md) records
source identity, CLI boundary checks and the debug/build-ID-only differences
from the earlier probe binary. [Exact reviewer evidence](foundation_complete_reviewers_verification.json)
retains the complete input map and actual assertion counts.

The reviewer closure includes 776 library owners. Fifteen original owners
outside that closure are being checked separately on the supported binary;
the actual central diagnostic target is also retained as a separate gate.
The original complete-library and identical-central-copy passes remain evidence
at their recorded executable and scope. Production promotion, authoritative
prose, generated evidence and affected frontend/source-pin qualification are
not implied by this reviewer pass.
