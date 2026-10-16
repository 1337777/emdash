# Whole intrinsic identities and composition units

Date: 2026-10-16
Predecessor: `d07139e7`
Status: native identity and its ladder compute; both expanded composition bodies satisfy whole unit comparisons; triple associativity and expanded cell factorization remain open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](production_intrinsic_unit_verification.json)

## Qualified computation

The fixed-postcomposition image of the public Catd identity now computes to
the identity of the ordinary diagram category. Consequently the actual
Homd_target_map(id_E) and homd_int(id_E) reach their identity target map and
the ordinary view of homd_id_int(E).

The [native intrinsic owner](production_intrinsic_composite.lpfragment)
now has its literal displayed-identity computation:

```text
eta_id_E = id_h_E,

h_E = strict_transfor(homd_id_int(E)).
```

The guard is id_(Catd(K))(E), not an arbitrary identity-looking carrier. In
particular an ordinary functor viewed as a terminal-source section is not
made strictly natural by this rule. The inherited noninvertible constant-
section and ordinary identity-functor loop controls still pass.

The [projection joins](production_intrinsic_unit_projection.lpfragment)
compute the existing section, y-component and index identity heads. The
[reviewer](production_intrinsic_unit_controls.lpfragment) follows the actual
whole identity through x/u, y, v and p and compares it with those heads.
No new primitive or second identity ladder is introduced.

Write comp_eta(F,G) for the defined body installed in the previous
checkpoint. The following **whole proof-time comparisons** now check:

```text
comp_eta(FF,id_D) = eta_FF
comp_eta(id_E,FF) = eta_FF.
```

These tests deliberately start from the expanded composition body. Merely
forming eta_(id o FF) and allowing its argument to contract first would not
test the composition rule's unit overlap. The comparisons are typed
reflexivity consumers of the whole modification; runtime conversion of the
two expanded bodies is not claimed.

## Required presentation compatibility

The remaining unit obstruction was in identity and associativity
presentations, not a need to make an arbitrary FF strict. The
[coherence views](production_displayed_unit_coherence.lpfragment) retain:

- proof-time unit comparisons with an actual identity as a side condition;
- identity action after the product identity has become a literal pair,
  including its actual result category and both product endpoints;
- comparison of displayed and ordinary diagram composition with the same
  two operands;
- the identity-family precomposition reading with every map constrained;
- associativity when an inner composition uses the ordinary diagram facade;
- the actual displayed left-unit whiskering and its right-unit ordinary-view
  counterpart.

The [runtime identity-pair computation](production_composition_identity_pair.lpfragment)
is restricted to displayed composition. It matches both literal identities
and both input pairs. The broader experiment that discarded these endpoint
patterns is not selected. Extra identity rules at the recursive Hom action
were also unnecessary and remain unselected.

The diagram-composition comparison was correctly omitted from the previous
two-map checkpoint, where its removal passed. The new whole unit consumer
fails without it. Its admission here records that new consumer rather than
revising the old result retroactively.

Proof-time unit comparisons retain the generic categorical form. Narrowing
their patterns to the displayed classifier caused an inference failure in
the actual whole consumer. They do not change runtime identity computation.
Two typed negative controls reject erasing either arbitrary modification
loop; another rejects replacing the third map in the mixed-facade
associativity comparison. No equality proof becomes a construction input.

## Validation and continuation

The final intrinsic_unit_prefix.lp passes with warnings and subject
reduction enabled in 10.742 seconds under the normal serial 90-second,
2-GiB and 64-MiB limits. It includes 202 positive and 48 negative assertions;
the unit reviewer adds ten positives and three negatives. The strict LHS
audit has zero unreviewed clauses or slots.

The critical-pair inventory changes from 1829 to 1856, with 36 added and
nine removed reports. The exact body groups are recorded in the evidence.
The added groups concern identity-pair/whiskering computation and native
identity projection orders. The whole unit and projection consumers qualify
the stated interfaces; they are not a global confluence certificate.

The full original-source migration still fails at Op_prof's old coefficient
in section 18b. Every original downstream declaration remains in the emitted
source. Production is not promoted. Whole triple/mapped-composite coherence,
the expansion of Phi_GG[lambda_FF] into the two named extracted cells,
remaining Q/mate/index and duality/inverse compatibility, the later source
pass and all public/downstream final gates remain required.

The accompanying [strict-Functord assessment](strict_functord_reassessment_2026_10_16.md)
is brainstorming only. It records the user's distinction between the maps
admitted by Functord and the expressivity of a theory that retains ambient
lax Transf. The chosen default is unchanged.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet intrinsic_unit_prefix.lp
python3 scripts/audit_rule_lhs.py --strict \
  tmp/probes/production_owner_migration/package/intrinsic_unit_prefix.lp
```
