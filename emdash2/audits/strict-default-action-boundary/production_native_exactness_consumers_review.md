# Original native exactness consumers

Date: 2026-10-23 UTC
Status: qualified non-library continuation; standing completion gates remain
Predecessor: `c4feb3fd`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

This continuation follows the original homology-window exact inputs through
source and middle exactness and the native comparison kernels. It retains
23 original owners and 11 complete reviewers, all 165 original declarations
and 47 positive/eight negative assertions. Two derived ordinary proof views
are added. No formal rule, operational primitive or caller hypothesis is added.

The profile substitutions retain the original maps, selected K/Q, actual
inverse data, supplied normality and short-exactness hypotheses. Walking-arrow
diagrams and their whole evaluation use the qualified oplax owners. All 220
old `Op(C)` occurrences are initial-object hypotheses and use `TotalOp(C)`.

The boundary-representative cover and cancellation proof need the original
quotient-zero law at the endpoints of their actual quotient diagram. Write
`I = K_arrow ∘ Φ`, where Φ is the original boundary diagram, and write
`Γ(I) = Arrow(E₁(I), Q(I), q_I)`. The caller spells the same whole diagram
`Arrow(U, Coim(Φ), q_I)`. Four typed whole comparisons verify these endpoints
and the diagram itself, both in a small import context and at the owner.
Directly inserting the former proof nevertheless leaves dependent-type
constraints. Component reflection and native endpoint argument substitution
were tested and rejected; neither repaired this consumer.

`one_cat_quotient_cokernel_zero_native_path` is the existing theorem viewed at
its native graph endpoints. `one_cat_boundary_quotient_zero_path` uses existing
equality elimination along the checked whole diagram comparison to view that
ordinary zero proof at the original caller's endpoints. Both are definitions,
not new axioms. They transport only an ordinary equality proof: no map,
inverse, operational family or new caller input is transported. Cover and
cancellation share that same derived proof. The actual complete owner passes.

The biproduct-injection reindex proof exposes a second presentation issue.
As in the already qualified copair counterpart, its whole transpose mate
must be compared before applying the original input. An existing whole
proof-time comparison, followed by `eq_ap`, replaces the deeply nested
reflexivity step. The complete owning module passes; no declaration or rule
is introduced for this change.

The complete group passes **50 positive and eight negative checks**, including
three inherited positives, in 321.720s at 3,007,072KiB RSS under
900s/4GiB/o=20 with subject reduction and warnings enabled. Receipt:
`20261023T194037Z-012bbb02bea64e6b89c6a36d7fcc28a4`.
The actual boundary owner and biproduct reindexing owner also pass separately.
The latter takes 215.268s at 2,670,888KiB. The earlier full-group failure takes
533.522s; differing import contexts and host conditions have not been
separated, so no performance improvement is attributed to the proof change.

All 222 checked inputs match the final replay. All 695 predecessor source
hashes and every input of six parent integration receipts remain byte-identical.
The slice adds fresh defined proof heads without new rules, so predecessor
evidence is carried at its recorded profiles. No unchanged successful broad
aggregate is repeated. The isolated checker is unchanged and has not replaced
the installed toolchain.

All 2,269 warning bodies occur in previously reviewed contexts; R07/R12 remain
open and no global confluence claim is made. All 34 source-pin drift controls
and exact durable replay comparisons pass. The
[verification](production_native_exactness_consumers_verification.json)
records every retained declaration/assertion, the two added derived views,
exact input hashes, failed experiments, resource settings and warning scope.

Qualification reaches **729 files: 480 core/library and 249 reviewers**.
There remain 311 core/library files and 347 reviewers outside this snapshot,
the same five terminal runtime obligations, normalization/toolchain work and
production qualification. Next follow the original target-exactness and
public exact-pair consumers. The separate nerve goal remains paused;
production is not promoted.
