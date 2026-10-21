# Original diagram evaluation, point and whole-mate reviewers

Date: 2026-10-21 UTC
Status: qualified non-library staging; unchanged library owners
Predecessor: `0d20474a`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Correct owner profiles and observations

The original walking-arrow evaluation reviewer keeps ordinary diagram inputs
F,G : Functor(WalkingArrow,C), ordinary fixed evaluation, and its source,
target and differential names. The differential has the actual library type
Transf_oplax(Functor_cat(WalkingArrow,C),C), with the encoded components and
mixed action read at the corresponding reversed endpoints. The concrete
identity-diagram component still computes to the original nonidentity walking
arrow, and its endpoint noncollapse assertion remains negative.

The first corrected candidate failed at inferred-type comparison for the
capped mixed-action runtime assertion. The selected observation instead reads
the existing whole `tapp1_func`, applies its existing Even-duality decoder,
and takes `fapp0` at the explicit original Hom classifier. It computes to the
same original right-hand side. The assertion remains runtime conversion,
not a proof-time reflexivity substitute. No new intermediary or formal rule
is introduced. Bare capped inference is not claimed to be repaired.

The point-usability reviewer observes a general transformed-arrow family
through its existing `transf_arrow_diagram_at_func` decoded-object projection.
Its separate OneCat ordinary realization stays ordinary. Both original
positives and the wrong-arrow negative retain their original data.

The whole-mate reviewer uses the native oplax diagram category, its existing
fixed evaluation and the existing OneCat profile for that category. It retains
both original whole input round trips and their component observations,
selected K/Q and original endpoints. No point observation replaces a whole
assertion and no stronger hypothesis is added.

The replay fragments for [walking evaluation][walking], [point usability][point]
and [whole mates][mates] retain the original reviewers with these adjustments.
All three reviewer declarations,
assertion polarities and typing-versus-runtime assertion kinds are preserved.
No library source, runtime rule, unification rule or operational primitive changes.

## Validation

The [combined driver](production_diagram_mate_reviewers_regression.lpfragment)
passes **16 positive and two negative assertions**, including three imported
positives. This covers all thirteen original positive and both original
negative assertions, plus the three reviewer declarations.

Receipt: `20261021T142919Z-698193316bd040759b24e737ad62f2fa`.
Wall time: **47.331s**. Maximum child RSS: **1,197,980 KiB**.
Profile: 180s/2GiB, o=20,v=1024, subject reduction and warnings enabled,
64MiB file cap, serial execution and no-swap guard. The isolated batch-snapshot
checker remains separate from the installed checker; normal defaults remain.

The initial baseline exposes the old ordinary-transformation type on the
oplax differential. The next candidate exposes the separate capped-result
inference limitation; the final whole-action projection resolves this actual
consumer while retaining runtime conversion. Both failures are recorded
separately from the successful final source.

The final run has 2,152 warning bodies. The earlier runs stopped in the first
reviewer with 2,036 bodies. All 116 subsequently reached bodies, and all final
warning bodies, already occur verbatim in the preceding qualified scope at
byte-identical library owners. The added imports include the existing walking
introduction, OneCat transformations, DefIso evaluation, reconstruction,
mate and terminal owners. Exact logs and bounded hashes retain those branches;
this is not a new-rule or global-confluence claim.

All fresh inputs match emission and the tracked driver. All 442 previously
qualified LP files remain unchanged. Their receipts retain their original
scope and profile; no unrelated core/library aggregate is repeated for these
reviewer-only adaptations.

Coverage remains **322 library/core files** and reaches **123 complete
reviewers**. The central diagnostic remains separately staged with the same
five terminal runtime exclusions. There remain 469 core/library files and
473 reviewers unstaged.

## Continuation

Continue the original adjunction reviewers `adjunction_exchange_computation`,
`adjunction_exchange_op_identity`, `adjunction_family_constant_views`, and
`adjunction_triangles`. These are separate original assertions, not discharged
by the mate round trips here.

The five terminal Homd runtime obligations, remaining migration,
normalization/usability, supported checker/resource profiles and production
source-pin/catalog/health/prose/CI gates remain required. The separate nerve
goal stays paused. No production qualification is promoted by this audit.

Replay with `production_owner_migration.py`, copy the combined driver into its
package as `diagram_mate_reviewers.lp`, and use the recorded profile. The
[verification](production_diagram_mate_reviewers_verification.json) retains
source/authoring hashes, original assertion kinds/polarities, receipts,
warning inventories and the unchanged prior qualification boundary.

[walking]: production_walking_evaluation_reviewer.lpfragment
[point]: production_arrow_point_usability_reviewer.lpfragment
[mates]: production_adjunction_zero_inputs_reviewer.lpfragment
