# Total opposite on the public conventional-lax mapping category

Date: 2026-10-14
Status: non-library owner candidate; selected whole/action consumers checked; no production promotion
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact inputs, receipts and warning inventory](conventional_total_op_verification.json)
Replay: [conventional_total_op_replay.py](conventional_total_op_replay.py)

## Contract and semantic source

This candidate retains `Hom_cat Cat_cat A B = Functor_cat A B`, strict
functor objects, and the conventional-lax transformation convention selected
by the user. It contains no `Functor_cart_cat`. In the migration's current
source names, T is `Op_cat`, R is `CoAbove2_cat`, and O is the defined
`TotalOp_cat = R(T(-))`. This does not reuse the old total-Op meaning of the
name Op_cat.

The whole structural map is declared directly:

```text
TotalOp_func_func(A,B) : O(Functor_cat(A,B)) → Functor_cat(O(A),O(B))
total_op              : R(Cat) → Cat.
```

It is not manufactured by composing whole T/R operations on arbitrary lax
transformations. Those operations have no such qualified profile here.
The mathematical reference is the compatibility of total duality with the
Gray mapping categories and the shifted coefficient source in
[Ara--Guetta v1, paragraphs 35–40](https://arxiv.org/html/2503.08832v1#S2).
This motivates structural declarations; the native tests do not derive the
existence of the whole map from its object formula.

The existing strict-functor R action and the category duality rules are
reused from pinned fragments, excluding their old Cartesian mapping action.
TotalOp_transf is the structural first projection of TotalOp_func_func.
Its whole next-Hom map TotalOp_transf_func is defined by generic fapp1_func,
so higher action is retained rather than replaced with a point operation.

For epsilon:F=>G, write L=G[p] o epsilon[x] and R=epsilon[y] o F[p]. The
default middle is R, with a retained comparison L=>R. Total opposite gives
epsilon^O:G^O=>F^O. Its selected middle, read as an underlying original
arrow, is L rather than the original R. Total reversal reverses the
comparison as well as exchanging its two boundary readings. The whole
off-diagonal rule therefore uses the original post-boundary functor,
defined by actual precomposition and G's Hom action. It does not copy the
old middle or supply an independent comparison cell.

## Actual whole family consumer

The family operation is a definition:

```text
TotalOp_catd(E) := total_op o R(E) : R(K) → Cat.
```

Its object, base-arrow and base-two-cell observations compute through that
composition. In particular, a potentially non-strict E[alpha] is mapped to
TotalOp_transf(E[alpha]) with the reversed direction. No extra family
admission argument is used. No same-profile operator on arbitrary family
transformations is declared by this construction.

The whole identity/composition action of an ordinary functor, already
present in section 17d of the pinned nucleus, is moved unchanged to its
earlier composition owner in the emitted candidate. The replay verifies
its exact equality with the pinned source. Without that move the actual
family base-two-cell consumer fails. Separate source-identity joins are
needed after R and O have erased the original identity's category tag.

## Projection-order comparisons

Two measured failures require proof-time readings between existing rigid
heads:

1. Projecting the outer total-dual action before cancelling the double
   transformation opposite leaves precomposition in O(B). Reading that as
   the original pre/right boundary gives the original middle. Both typed
   reflexivity orientations check. The rule checks the actual dual category
   and all endpoints; it does not identify B with O(B).
2. In family transport composition, distributing O over a functor composite
   and first contracting E's strict action leave different runtime terms.
   The comparison reflects composition in the image of O to the original
   functor composition. That typed comparison checks, whereas direct runtime
   conversion remains a negative control. There is no runtime fold inverse
   to the existing distribution rule.

These are diagnostic equality observations, not equality proofs passed to
operational symbols. An unrelated original functor cannot satisfy the
second comparison, and the original post/left boundary is still distinct
from the middle at both runtime and proof time. An arbitrary modification
component is also not identified with an identity.

## Checks and limits

The warning-enabled candidate passes **31 positive and 10 negative
assertions**, including the inherited ordinary controls, plus **three new
typed comparison definitions**. Its check used 4.316s and 131,296 KiB maximum
child RSS under the normal 90s/2GiB guard with subject reduction enabled.
The exact receipt is in the verification file; resource measurements must
not be reused for another target or profile.

Seven adverse variants fail at the intended observations:

| Variant | First rejected consumer |
| --- | --- |
| no_offdiagonal | Original-post boundary of whole dual action |
| wrong_middle | Negative rejecting the copied original middle |
| no_source_units | Identity action over R(K) |
| no_total_source_unit | Identity in the total-opposite next Hom |
| no_whole_action | The derived family's base-two-cell action |
| no_involution_reading | Projection-before-involution typed comparison |
| no_composition_reading | Whole family transport composition comparison |

The LHS audit has zero unreviewed slots, with 22 annotated slots in 15
clauses. Against the pinned ordinary conventional-lax donor, critical-pair
reports change from 495 to 652: 158 bodies added and one removed. The
verification ledger records each added body's hash, participant heads and
owner family. This is owner classification, not a proof that every symbolic
overlap joins. The two new proof-time readings do not change the runtime
critical-pair bodies compared with the resumed failing candidate.

The replay's final extra removal variant changed its authoring hash but
re-emitted the checked candidate and other variants byte-for-byte. Their
receipts are retained only after verifying those exact hashes.

Remaining work includes the whole functor-level inverse/coherence,
family-map profiles, further overlap qualification, the coupled joint
composition/evaluation migration, lax Q, and the complete direct Homd
ladder. The donor still includes legacy joint Cartesian composition;
these local noncollapse observations do not certify consistency of that
snapshot. Neither the old Cartesian Homd result nor this whole-duality
candidate is completion of the new public-universe milestone.

## Replay trigger

Replay after changes to the conventional-lax donor, duality normal forms,
ordinary whole action owners, or any of this candidate's authoring inputs.
From emdash2:

```bash
python3 audits/strict-default-action-boundary/conventional_total_op_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/conventional_total_op/candidate.lp
python3 scripts/audit_rule_lhs.py \
  tmp/probes/conventional_total_op/candidate.lp --strict
```

Run adverse variants serially through the same resource guard and verify
their failure sites. Generated LP and logs remain ignored; the fragments,
replay and bounded qualification record are retained as non-library evidence.
