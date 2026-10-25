# Guard the evaluated-action comparison against unrelated factorizations

Status: focused and matched original-context regression repair pass. The
aggregate subsequently stops at a stale strict-composition reviewer negative;
see the [continuation](foundation_final_composition_review.md). Predecessors:
`73888e52` and static review `b37e6ef6`.
The earlier broad congruence is not selected for adoption.

The 404-input run `20261025T034135Z-54072a183c3e4dbe95607839a2700f8c` fails
after 717.652s/2,558,740KiB in the existing image/coimage proof at
`emdash3_2_one_cat_image_coimage_comparison.lp:401`. This is a real unfinished
proof, not the preceding timeout. Its residual constraints include attempted
identifications of different intermediate diagram categories. The original
proof and its supplied inputs are unchanged.

The proposed generic same-head congruence compared every pair of inputs to
`comp_prod_fapp1_fapp0`. Although equality of those inputs is sufficient for
equality of outputs, it is not necessary for every valid comparison. Applying
that inference strategy to unrelated factorizations can preempt the other
comparison rules. Passing the tail and retaining every argument did not
establish that this broad inference scope was usable in downstream proofs.

The corrected clause repeats **both actual cell components** in its two
`Struct_sigma` patterns. Thus it compares the annotations of the same supplied
mixed-action data. All classifier and endpoint pairs remain explicit residual
comparisons. It does not require unrelated factorizations to have the same
inputs. The separate evaluation comparison is unchanged. No runtime rule,
primitive, user hypothesis or operational equality argument is added.

The 83-input focused run includes the four whole/type controls, both complete
tail reviewers and the previously failing image/coimage owner. It passes cold
with subject reduction:
`20261025T035613Z-f6b1e20fbbf84d9e8ba39b0d6fe40900`, **160.985s/1,998,008KiB**,
at 300s/4GiB/o=20. The rewrite LHS audit remains zero unreviewed slots; review
of the unifier's scope is separate. The two original noncollapse negatives
remain. No proof body was replaced to obtain this result.

The [verification](foundation_final_guard_verification.json) retains the failed
aggregate, passing focused run, source maps, updated authoring pins and exact
21-output replay. The focused and aggregate import contexts differ; this focused
result alone did not establish the whole-context repair. The subsequent matched
full run now supplies that regression evidence, with the guarded clause as its
only changed input. The separate full-group outcome remains pending; check its
actual receipt before adoption.

The earlier [static review](foundation_shared_delta_review.md) remains useful
for data retention and orientation hygiene, but it did not certify inference
scope. Its inventory now records the guarded clause. R07/R10/R12/R14, terminal
Homd runtime obligations and final production qualification remain open.
