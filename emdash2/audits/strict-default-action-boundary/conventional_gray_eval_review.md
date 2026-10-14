# Gray evaluation comparison candidate

Date: 2026-10-14
Status: non-library checked owner slice; default architecture under user-requested reassessment
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](conventional_gray_eval_verification.json)
Replay: [authoring script](conventional_gray_eval_replay.py)

## What changes

The existing primitive Eval_func receives the proposed strict-default type

```text
Eval_func(A,B) : GrayTensor_R(Functor_cat(A,B),A) → B.
```

Functor objects are strict and transformations are conventional lax. The
tensor uses object pairs but has no product-Hom equation. Its canonical
coordinate maps are declared whole structural functors. These declarations
target the existing right-oriented Gray tensor; they do not derive its
universal property or independently complete its implementation.

Eval_fapp1_func uses the actual tensor Hom. Its stable object projection
Eval_fapp1_fapp0 accepts a tensor arrow rather than a product pair of arrows.
Both whole and capped evaluation project to that same owner. Along the
first coordinate evaluation computes to tapp0; along the second it computes
to fapp1. Eval_at_func is a definition through the first coordinate, and
the original whole fixed-object evaluator fapp0_func is retained.

Two whole Hom-level coordinate joins preserve iteration to modifications.
A separate identity join handles the order in which Eval's first Hom has
already projected. These are constructor/action observations, not
strict-natural-transformation requirements.

## Mixed paths

The two mixed paths are definitions using the two coordinate functors and
ordinary composition in the tensor. They are not primitive pairs:

```text
left route  = right(G)[p] o left(x)[eta]
right route = left(y)[eta] o right(F)[p].
```

Their evaluator observations compare at proof time with

```text
G[p] o eta[x]
eta[y] o F[p] = eta[p], respectively.
```

The comparisons require the corresponding actual source path. A wrong-path
variant is rejected by the negative control separating the first evaluated
route from the middle. The two source paths also remain distinct at runtime
and in typed reflexivity. No independent interchanger or laxity cell is
supplied. Connecting the tensor's native interchanger and the existing
right-closure interface remains unfinished; these endpoint comparisons alone
do not complete that task.

## Evidence and limits

The warning-enabled source passes 42 positive/16 negative assertions,
including the total-duality donor, plus two new typed path comparisons.
Its check took 4.141s and 136,380 KiB maximum child RSS at the normal
90s/2GiB profile. Eight omission/wrong-path variants fail at their intended
assertions or typed definitions. Subject reduction remains enabled and all
checks ran serially. The source is byte-identical after adding replay variants.

The LHS audit has zero unreviewed slots. There are 15 new critical-pair
bodies, none removed, against the donor's 652. They concern generic/dual
source identities, coordinate identities, and product-valued mapping-category
normalization. The verification ledger classifies each. Selected identity
and whole-coordinate consumers pass; complete overlap qualification,
including the product-codomain specialization, remains open.

The old Cartesian evaluator type and Cartesian-pair arrow input are rejected.
However, the source donor still has the independent legacy Cartesian
composition contract. Thus this slice does not remove every old collapse
route or certify consistency of the whole source. It does not implement
derived curry/uncurry, full Gray coherence, Q or the whole Homd ladder.

The user subsequently requested reconsidering corrected-duality lax functors
and lax transformations as the ambient design, explicitly including
correction of Sigma. No default change has been adopted or production rule
promoted. This candidate remains comparison evidence for the strict-default
alternative, not a commitment to complete that migration irrespective of
the reassessment.

## Replay

From emdash2:

```bash
python3 audits/strict-default-action-boundary/conventional_gray_eval_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/conventional_gray_eval/candidate.lp
python3 scripts/audit_rule_lhs.py \
  tmp/probes/conventional_gray_eval/candidate.lp --strict
```

The verification record names the eight adverse variants and their expected
failure sites. Replay after changes to the donor, tensor/evaluator owners,
or candidate inputs. Generated source and raw receipts stay ignored.
