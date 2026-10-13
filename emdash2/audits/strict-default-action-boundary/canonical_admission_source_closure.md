# Canonical co-Yoneda seed profile proposal

This bounded replay starts from the checked `admission_next` staged reindex
bridge. It proposes one explicitly structural profile refinement: the
existing right-unit co-Yoneda component at `Unit_B` has a Cartesian view.
The view accepts only `B`; it cannot admit an arbitrary raw map and accepts
no independently supplied strictness/equality witness. Its actual inclusion
agrees with the existing raw `Prof_coyoneda_cov_map(Unit_B)`.

The implementation of this structural proposal now passes its bounded
native-owner, seed-owner and actual-consumer checks. The selected
`seed_consumers.lp` has 227 positive and 60 negative controls, including
inherited controls, and passes in 9.722 seconds at 417,896 KiB RSS under the
normal 90s/2GiB serial guard with subject reduction. Its receipt is
`20261013T152042Z-5d0c87ebcad44a82a4c38355258e9d9c`. This validates the
proposed contract and its stated consumers at this source snapshot; it does
not change its status to strictness derived from the old raw theory.
`canonical_admission_verification.json` records exact sources, outputs,
receipts, logs and qualifications.

This is a new canonical-constructor profile contract. It is not a strictness
theorem derived from the old signature or raw beta/eta, and a passing checker
run would not independently prove its mathematical justification. The intended
operation is the same unit/coend evaluation already named by the existing
co-Yoneda owner. The source tensor remains opaque and has no general coend
eliminator. Its current shaped beta specifies a canonical tensor-generator
observation, not both whole strictness cells.

The replay imports unchanged production declarations of `Prof_cell_apply`,
`Prof_func_hom` and `Prof_tensor_hom_hom`, and the unchanged right-unit
co-Yoneda beta. It first checks that native operation on an arbitrary raw
shaped element. The seed's generator observation is then obtained from its
actual inclusion agreement by ordinary `eq_ap`, followed by the native beta.
No new shaped computation or triangle rule is installed.

The derived operations use the existing whole inclusion, lambda, reindex
and evaluation owners. They retain the raw public types. Ordinary congruence
derives agreement of the complete raw chain with the original
`raw_represented_counit` body. Raw closed beta computes
`eval(lambda(seed))` to the seed at the identity specialization.
The checked Cartesian reindex functor also acts directly on the proposed
classified seed; the checked staged reindex theorem supplies its raw-map
agreement without a new admission parameter.

That reindexed seed still has tensor middle `B`; it is not the general
counit whose tensor middle is `A`. The tensor reindex law changes only
exposed endpoints. The exact further profile obligations are:

```text
j_B = lambda_cov(coyoneda_cov(Unit_B))
  must have both whole post/left and pre/right strictness cells.

j_F = reindex_transf(j_B,id_B,F)
  is then classified by the existing actual reindex action.

eval_cov(j_F) : tensor(Conjoint(F),Companion(F)) -> Unit_B
  must again have both whole strictness cells.
```

In the profile extension, `IsStrictTransfor` requires `IsStrictCell` for
both retained cells, including equality of each actual cell with its strict
`path_to_hom` representative. Component equality or endpoint paths alone do
not meet that requirement. The raw lambda/evaluation owners currently have
only their signatures and inverse beta/eta; they provide no component/full
action or Cartesian-preservation body for these specific inputs.

A constructive general evaluation account would need
`(u:b -> F(a), v:F(a) -> b') |-> v o u` on tensor generators, balancing
under the arrows of `A`, and both whole exposed-endpoint actions. The current
opaque tensor/closed declaration closure does not provide that eliminator
or its identification with raw evaluation. This replay therefore does not
declare a classified `j_B`, a classified general counit, a generic Cartesian
lambda/evaluation operation, or an arbitrary-map strictifier. The negative
raw-retyping controls do not claim such classified lifts cannot exist.

`canonical_admission_migration.py` pins the production source and checked
donor, emits native-owner, seed-owner, operation and actual-consumer stages,
and never invokes Lambdapi. `without_seed_view.lp` and
`without_native_coyoneda_beta.lp` remove only their named fragments from
the actual-consumer candidate. The manifest records all exact source blocks
and hashes. Root owns the serial guarded checks.

Both exact removal controls fail at the intended obligations:

- Removing the seed inclusion view leaves the actual included seed versus
  raw co-Yoneda equality unsolved in `canonical_admission_seed_agreement`
  (`20261013T152219Z-344df68bfaaa4ab39b9a68a4e7640897`).
- Removing the unchanged native co-Yoneda beta fails the native shaped
  generator assertion before the seed-dependent consumers
  (`20261013T152225Z-3f2a4c239ae04c5f9468c13d1d2b011a`).

Neither failure is a syntax error. The selected warning inventory remains
879 normalized unjoinable pairs, exactly the checked staged-reindex donor's
inventory, with no additions or removals. The strict inferred-slot audit
reports zero unreviewed rule clauses. Existing overlap qualifications remain;
this is not a confluence certificate.

A follow-up source review finds no native full-action owner for
`Prof_lambda_cov_map`. `Prof_imply_cov_func2` and `Prof_imply_cov_func` vary
the implication's O/Q inputs, not the lambda correspondence. The maintained
`strict_prof_imply_cov_func` classifies a functor on raw Prof categories; it
does not classify the transpose `j_B` as a strict transformation. The
smallest next interface investigation is a Cartesian restriction of the
existing lambda operation at the exact Unit/Unit/Unit closed instance,
consuming the constructed classified seed and retaining the actual raw
forgetting square and higher action. Such a restriction would be another
explicit structural mapping-profile contract unless its whole strictness
cells are derived from an actual native body. It is not a license to admit
arbitrary raw maps. No additional lambda or evaluation declaration is made
in this tranche.
