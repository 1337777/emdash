# Nested reindexed identity inverse: owner comparison experiment

This is a non-library proof-time experiment. The independent generic
comparisons and actual nested identity comparison pass with perturbation
controls. Each exact comparison removal fails at that typed consumer, while
the original runtime conversion still fails. It targets the
remaining double-symmetry identity case when the input functor is itself a
stable precomposition. It does not loosen the generic runtime horizontal
identity rule, supply an inverse witness, or install a special inverse law.
Runtime conversion remains a separate positive obligation.

The [builder](inverse_nested_migration.py) uses the checked raw-preserving
coefficient assembly `with_nested_reindex.lp`, SHA-256
`22137af6b253146827ba243d87cc9b4cc92ca6d91c6b925dd009f01d1b4bfd2f`.
[Input pins](inverse_nested_inputs.json) retain that entire donor, its
verification record, the predecessor interaction control, and package file.
The donor includes the qualified local inverse, triple-swap and terminal-
factor consumers, as well as its explicitly qualified canonical-seed and
raw co-Yoneda assumptions. No production source or earlier recipe is read
as a mutable replacement for this donor.

## Measured predecessor boundary

The predecessor's ordinary variable transformation round trips and selected
identity/composition inputs pass. The failed `interaction_controls` and
`interaction_comparison` sources use

```text
F0 = pre_H(F)
swap^*(swap^*(id_F0))  versus  id_F0.
```

Its displayed endpoint pair has already accumulated to
`pre_(H o swap)(F)`, while the actual identity cell retains
`id(comp(pre_H(F),swap))`. The existing single precomposition/raw-composition
view does not automatically compose through that reassociation. The old
two generic endpoint-wildcard runtime attempts fail subject reduction and
remain rejected in [local_inverse_verification.json](local_inverse_verification.json).

## Proposed owners

The [precomposition comparison](inverse_nested_precomp_comparison.lpfragment)
records ordinary associativity in the two visible presentations:

```text
comp(pre_h(f),j) = pre_(h o j)(f).
```

It lives immediately after the existing proof-time raw precomposition views.
The actual f is shared, and the proposed accumulated argument must compare
with the actual composite h o j. This is a generic category-level statement,
not a property of product symmetry or presentation inverses. Runtime keeps
the stable precomposition and raw-composition owners distinct.

The [horizontal comparison](inverse_nested_horizontal_comparison.lpfragment)
is a proof-time reading of the existing horizontal identity-pair rule. It
matches both actual source/target pairs and both actual identity cells, then
compares each displayed endpoint with the corresponding identity object.
Its proposed result must be the identity on the actual composite. A variable
cell does not satisfy the identity pattern. This keeps the constraints lost
by the rejected wildcard runtime attempts, while allowing endpoint agreement
to use the existing proof-time views.

This second comparison lives after the generic horizontal identity owner
and before its later consumers. Neither comparison names swap, local
presentation maps, or the desired inverse. If they qualify the actual
consumer, the existing raw double-swap computation handles the resulting
composite. No runtime `comp_prod_fapp1_fapp0` rule is changed.

## Independent and actual controls

The three candidate comparison targets pass. Other emitted targets remain
unqualified until their own root-run receipts are recorded.

| Target | Intended observation |
| --- | --- |
| `owner_prefix` | Both comparisons at their owners with the complete inherited donor controls. |
| `precomp_baseline`, `precomp_candidate` | Candidate passes generic typed scalar reassociation and a perturbed-arrow negative; baseline has no receipt yet. |
| `horizontal_baseline`, `horizontal_candidate` | Candidate passes typed horizontal identity action with a stable/raw endpoint and variable-cell negative; independent of swap. Baseline has no receipt yet. |
| `nested_baseline`, `nested_comparison` | Candidate passes the actual typed nested identity round trip, same-endpoint perturbed-swap formation, and typed negative. Baseline has no new receipt yet. |
| `without_precomp_comparison`, `without_horizontal_comparison` | Both exact single-comparison removals fail at the first actual typed nested inverse assertion. |
| `runtime_boundary` | Original positive conversion assertion fails; proof-time success is not runtime normalization. |
| `normal_forms` | Native printing of the two actual terms; diagnostic, not equality evidence. |

The actual controls reuse the donor's `local_inverse_swap_action` and
`local_inverse_perturbed_swap` bodies. The perturbation is a variable strict
cell from the swap to itself, so the proposed operands have the same
endpoints before testing noncollapse. The independent horizontal control
uses an identity first functor to isolate endpoint interpretation from swap
cancellation. The actual nested control then exercises the nontrivial swap
case and accumulated precomposition together.

Typed `eq_refl` exercises proof-time unification. Success there must not be
reported as runtime normalization. Conversely, a failure in any emitted
positive boundary is not converted to `assertnot` or counted as a successful
negative. Both removal controls fail at the actual consumer: lines
18259–18276 without the precomposition comparison, and 18248–18265 without
the horizontal comparison. Each group is therefore required by this tested
typed inverse. Independent baseline targets have no new receipts; their
outcomes are not inferred. The runtime assertion fails separately at
18270–18277.

The negative perturbation follows an explicit positive formation check at
the same `StrictTransfor(F0,F0)` endpoints. The typed equality rejects replacing
an arbitrary outer swap cell theta with identity. This retains the actual
cell data; it is not a theorem that every theta is nonidentity or noninvertible.

The full owner copy minus the two exact comparison insertions is byte-identical
to the donor. There are zero new or removed runtime rules, zero new
definitions, and two new proof-time unifiers. The normalized warning inventory
is unchanged at 911 critical-pair blocks, with zero added or removed blocks.
Exact source/log hashes and comparison policy are recorded. This diagnostic
comparison does not establish global confluence.

## Reproduction and qualification limit

```bash
python3 emdash2/audits/strict-default-action-boundary/inverse_nested_migration.py --check-authoring
python3 emdash2/audits/strict-default-action-boundary/inverse_nested_migration.py
```

The recipe validates unique owner anchors and exact source pins, then emits
eleven LP targets and a manifest under `tmp/probes/inverse_nested/`. It never
invokes Lambdapi. Six exact root-run receipts are recorded for the three
passing typed consumers, two failed removals and failed runtime assertion.
The strict static LHS audit reports zero unreviewed slots and 44 annotated
slots in 30 clauses. Checker runs retain the normal serial resource guard
and subject reduction; no no-SR option is used.

[inverse_nested_verification.json](inverse_nested_verification.json) owns
source/output hashes and later receipts. Raw Prof maps remain distinct from
the local Cartesian mapping category. This bounded comparison experiment
does not establish all reducible inverse presentations, global confluence,
whole coefficient/lift coherence, or production qualification.
