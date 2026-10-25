# Final reviewer strict-composition correction

Status: complete affected reviewer and final 15-file aggregate pass; broader
library/consumer qualification and adoption remain pending.
Parent: `9cb774e9`. No kernel/library declaration or rule changes in this delta.

The full 404-input run with the same-cell guard reaches the thirteenth original
reviewer: `20261025T040130Z-e0c62e41c7984c63bb701f17475b79d4`,
800.198s/2,834,396KiB at 1800s/4GiB/o=20. The first twelve complete original
reviewers, including native snake inputs and zero observations, finish.
The image/coimage proof that failed previously also finishes in this context.

Compared with the preceding failed 404-input run, input names, checker and
resource settings are identical. The only changed input is the guarded
`emdash3_2_zero_arrow_family_action_paths.lp`. This supplies the matched
original-context regression evidence missing from the earlier focused pass.
It does not make the whole aggregate successful: the run stops later at an
old negative composition assertion.

Assertion 2 in `examples/one_cat_zero_cone_homology.lp` formerly denied
composition preservation of the displayed homology functor. Public functors
now preserve composition by default. The same equation therefore becomes
positive. Its terms, all OneCat/realization inputs and every other assertion
remain unchanged. The wrong-arrow negative at assertion 9 is retained.
The old OneCat proof-time composition witness is checked as before.

The complete corrected reviewer passes cold with subject reduction:
`20261025T041745Z-846172786b0a4e62ba380b4334a648b4`, **101.745s/333,252KiB**,
50 inputs, at 300s/2GiB/o=20. The time allowance follows the measured 150-second
original import baseline. This is a different scope from the large aggregate;
no performance comparison is inferred.

The final 15-file recipe now retains all 60 original assertions as **55 positive
and five negative** observations. Exactly one assertion changes polarity.
Exact replay reproduces the 21 outputs. The
[verification](foundation_final_composition_verification.json) records the
matched aggregate snapshots, completed-file evidence, focused receipt, source
pins and deliberate contract correction.

The [complete-source assembler](foundations_complete_candidate.py) now combines
the existing pinned recipes in a fresh destination. All 1,387 original library
and reviewer files match their current staged candidates byte-for-byte: 791
library owners and 596 reviewers, with no compiled objects. The central
diagnostic is separate and retains its five runtime obligations. The prepared
`all_original_library_owners.lp` driver imports precisely the original owner
registry. The temporary package also contains auxiliary audit sources; do not
promote that directory wholesale or call every auxiliary file qualified.
This assembly is reproducibility evidence, not an additional mathematical pass.

The full 15-reviewer group now passes cold:
`20261025T042241Z-3170b69f31ba4b10b98677e1baf83ddd`, **797.794s/2,838,040KiB**
at 1800s/4GiB/o=20, subject reduction enabled, all 404 inputs retained.
The only changed input since the previous run is the reviewer assertion/comment;
its mathematical sources, checker and resource settings are unchanged.
Every receipt input matches the assembled complete candidate exactly.
Production-emitter qualification counts, the five terminal Homd runtime
requirements and the broader library/integration gates remain open.
