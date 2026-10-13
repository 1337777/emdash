# Local Cartesian presentation inverse: bounded qualification

This non-library replay starts from the checked `admission_next` staged
reindex donor. It retains the raw public Prof profile and the actual local
Cartesian presentation maps through product symmetry, precomposition and
curry/uncurry. It does not import the separate canonical-admission proposal
or qualify the whole coefficient universe.

The selected `interaction_prefix.lp` passes 231 positive and 58 negative
controls, including inherited controls, in
`20261013T153235Z-e3f3e5e0d4ce4efb8c73205dc919a17b` (9.099 seconds,
423,352 KiB maximum child RSS). Its base `qualified_controls.lp` passes
229 positive and 58 negative controls in
`20261013T152000Z-cf15fb12cae9496e8eeaffaeca5fae71` (19.651 seconds,
423,076 KiB). These receipts use the normal guarded 90s/2GiB profile and
retain subject reduction. `local_inverse_verification.json` pins the exact
source inputs, generated targets, receipts and raw logs.

The checked corpus covers both direct object round trips, both separately
expanded transformation round trips, identity/composite inputs, arbitrary
raw-map rejection, preservation of the original variable transformation,
and rejection of a variable cell substituted for an identity swap cell.
The selected prefix additionally checks triple-swap overlap and a terminal
product factor. These are the actual definition bodies, not supplied
inverse witnesses or an equality between raw and Cartesian map categories.

Three runtime rule groups are selected:

| Group | Owner and purpose |
| --- | --- |
| `local_inverse_swap_guarded.lpfragment` | Completes double product-symmetry precomposition after both Cartesian transformation actions have expanded into horizontal action. The actual product endpoints are required subject-reduction guards. |
| `local_inverse_swap_identity_guarded.lpfragment` | Joins the identity-input route where the inner horizontal identity has already exposed a raw composite while its endpoints retain stable precomposition. |
| `local_inverse_swap_object.lpfragment` | Joins raw outer composition with the existing stable inner precomposition for the same double symmetry. It does not fold arbitrary precomposition to raw composition. |

Each exact removal is measured against `qualified_controls.lp`:

| Removed group | Observed failure | Receipt |
| --- | --- | --- |
| Guarded swap action | The independent variable-transformation double-swap assertion fails. | `20261013T152204Z-5c95a41308444112b6dd67c8017f1ab7` |
| Guarded identity action | The presentation identity-input assertion fails. | `20261013T152210Z-65774526b719478a9212faaa29319dc7` |
| Stable/raw object join | The retained identity-action clause fails subject reduction at its double-swap endpoint. | `20261013T152216Z-11bb7aed0a274ad383344ef4542475eb` |

The early unguarded swap proposal fails subject reduction in both
`joined_swap.lp` and `joined_inverse.lp`. The early identity proposal also
fails subject reduction; retaining its product guards still needs the object
join. Two attempts to replace this bounded completion by a more generic
horizontal-identity rule, `minimal_controls.lp` and
`pair_identity_controls.lp`, fail subject reduction. They are rejected
experiments, not qualified simplifications.

There is an important historical test correction. The last `assertnot` in
`object_join_controls.lp` replaces one product swap by an arbitrary functor
`H`. Its two proposed operands have different dependent endpoint types.
The checker rejects the test's type comparison; this does not demonstrate
that an inverse computation failed, and it is not a passing noncollapse
control. The source remains preserved as historical evidence. The selected
suite removes only that ill-typed test and uses
`local_inverse_perturbed_controls.lpfragment` instead: its `theta` is
explicitly typed from the swap to itself, the result is checked at the same
endpoints, and the negative equality confirms that the variable cell is not
silently replaced by identity.

Two later failures are genuine outstanding positive obligations:

- `interaction_controls.lp` fails the nested identity case where the input
  functor itself is a stable precomposition
  (`20261013T153001Z-ac95065ed30a4bf6a6ae878e58c2f55f`). The earlier triple
  swap and terminal-factor assertions pass before this failure.
- `interaction_comparison.lp` also fails the corresponding explicitly typed
  reflexivity comparison
  (`20261013T153245Z-11fabd848f2840889cb96dbf7eec5823`).

Both failed sources and their exact hashes are retained. They are not
relabeled as negative controls, mathematical impossibility results, or
successful profile restrictions. The selected corpus therefore does not
establish that all reducible presentations of all inverse computations
normalize successfully, nor does it establish confluence or a complete
omega-level presentation equivalence.

The warning inventory changes from the admission donor's 879 normalized
unjoinable critical pairs to 905: 26 additions and no removals. Exact
term/reduct/participant blocks and hashes are in the verification record.
Their primary owner classification is:

| Primary selected group | Added pairs | Interacting families |
| --- | ---: | --- |
| Stable/raw object join | 4 | Stable precomposition accumulation, its generic/Cat-valued identity cuts, and transformation-component composition. |
| Guarded swap action | 6 | Self-overlap of nested swaps, horizontal identity-pair reduction, and Path/Terminal identity normalization in either swap slot. |
| Guarded identity action | 16 | Path/Terminal identity normalization, raw composition unit/constant/postcomposition reductions, symmetry and symmetry-pullback folds, the selected object join, and stable precomposition accumulation/identity cuts. |

This is a diagnostic classification, not a claim that the pairs are joined.
Triple-swap and terminal-factor consumers cover concrete interactions; the
nested stable-precomposition identity remains failed, and the other warning
families receive no blanket qualification from this finite corpus. Existing
donor warnings also remain in force.

The generated manifest is the authoring source of truth. All 22 available
matching checker receipts agree with the current target hashes. The two
normal-form targets are diagnostic `compute` replays; their successful
checks do not by themselves establish an inverse assertion. No new checker
run, source mutation, production promotion or checkpoint is performed by
this evidence record.
