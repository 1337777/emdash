# Exact companion-weight Cartesian evaluation restriction

This non-library proposal starts from checked `canonical_lambda/consumers.lp`.
The sole new structural owner is a whole functor at fixed `F:A -> B`:

```text
Hom_S(B,A)(Conjoint(F), reindex(imply(Unit_B,Unit_B),id_B,F))
    -> Hom_S(B,B)(Conjoint(F) tensor_A Companion(F),Unit_B).
```

The bounded implementation and consumers pass. `restriction_controls.lp`
checks 253 positive and 72 negative source obligations, including inherited
controls, in `20261013T162524Z-2d7375366c154c7b8b05bb1c35f7d7b5`.
The selected `consumers.lp`, including the actual curried image, checks 260
positives and 74 negatives in
`20261013T162531Z-0dac98fb26264181a3854dcd544a498f` (6.522 seconds,
435,876 KiB maximum child RSS). The normal serial 90s/2GiB guard and subject
reduction remain enabled. `canonical_eval_verification.json` records exact
source/output hashes, receipts, logs and scope. This qualifies the stated
structural contract's implementation and its constructed consumers, not a
derivation of the contract from the old raw theory.

Its source keeps the stable endpoint already used by the actual classified
`j_F`. The existing implication-reindex comparison provides the canonical
`imply(Unit_B,Companion(F))` presentation when the old raw evaluator needs it.
Evaluation is covariant in this map argument; no extra opposite is inserted.
The guarded raw-object comparison constrains every original evaluation
category, weight, output, source profunctor and the actual included input.

This restricts evaluation on all Cartesian maps in that exact fixed Hom,
which is stronger than admitting only the canonical `j_F` but narrower than
general P/Q/O preservation. The whole functor and its higher action are an
explicit structural profile contract. The original raw evaluator has no
directed Hom-action owner from which they can be derived. Its existing raw
beta and guarded generator computation do not establish this profile.

The retained whole action is on the classified input-map category at fixed
F and fixed A/B. Dependence of the declarations on those parameters does
not supply a whole directed family as F, A or B varies. Constructing that
parameterized family and its coherent action is a separate next obligation
for complete represented-lift coherence; this fixed-F restriction does not
solve that assembly.

The classified counit has an actual definition: apply the restricted whole
evaluator to the already constructed `canonical_lambda_reindex(F)`. It is
not an additional primitive classified map and accepts no independent
equality, inverse, coherence or strictness witness. The whole raw image is
also defined, by composing with the existing inclusion's Hom action.
Its raw agreement is composed through the existing actual lambda/reindex/
evaluation operation. The retained raw counit then supplies the native
canonical-unit-second-leg generator observation by ordinary congruence.

An additional concrete consumer applies `local_cart_prof_curry_func(B,B)`
to the classified counit using its actual `fapp1` action. It is a map in the
existing `local_cart_prof_qhom(B,B)`, between the actual curried tensor and
Unit profunctors. Whole and capped application orders are checked. No new Q
primitive or identification of these endpoints with Q composition/unit is
assumed.

No classified lambda/evaluation beta/eta, identity comparison, mate triangle
or faithfulness of forgetting is added or inferred. Equality terms are
observational theorem outputs and are absent from operational inputs.
Higher raw-evaluation compatibility and directed coherence as F varies are
not supplied by a fixed-F whole functor. Arbitrary two-leg tensor generator
composition, balancing, full Q/Homd structure and production integration
remain separate obligations. Public raw map and evaluation names retain
their original types.

`canonical_eval_migration.py` emits owner, mapping-action, operations and
consumer stages without invoking Lambdapi. `without_raw_view.lp` removes
only the comparison with the retained raw evaluator; no declared operator
or consumer is removed. Source pins and exact hashes are in the manifest.
Any checker success validates this explicit bounded contract and its
constructed consumers, not derivation of the contract from the old raw
theory.

The exact `without_raw_view.lp` removal fails at
`canonical_eval_raw_agreement`: the included value of the restricted whole
evaluator cannot be identified with the original raw evaluator on the
actual included input. Receipt
`20261013T162538Z-ede317ba246440d8a8a54d65ab93ee0a` records that unresolved
whole-map comparison. It is not a syntax failure; the whole owner and its
earlier mapping-action controls remain.

The selected warning inventory is unchanged from the lambda donor at 911
normalized unjoinable critical pairs, with no added or removed blocks.
Existing overlap qualifications remain; no confluence claim follows. The
strict inferred-slot audit reports zero unreviewed rule clauses. The new
higher action remains part of a fixed-F structural mapping contract. No
whole varying-F or varying-A/B family, classified inverse/triangle law,
faithfulness result or Q-composition comparison is qualified here.
