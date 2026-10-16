# Original profunctor owners and corrected displayed Hom action

Date: 2026-10-16
Predecessor: `d07698b6`
Status: original-source migration through section 18z checks; the full source next fails at CommaFib_catd in section 18zz
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_profunctor_verification.json)

## Migrated existing owners

Op_prof remains pullback along product swap. Op_cat is the selected
dimension-one transpose, so its endpoints and the absence of an extra fibre
opposite remain appropriate. Prof_reindex retains product-map reindexing.
Their object/action annotations now use Cat_cart and its actual first Hom,
Functor_cart_cat. ProfMap and shaped-cell inputs still admit ambient lax
displayed maps. There is no public endpoint-convention swap or new curried
profunctor theory.

Unit_prof retains its original Hom_tele_func/Hom_func action. The ordinary
view of hom_int supplies the existing raw internal-action consumer in
Prof_func_hom. Original comparison, tensor, co-Yoneda, implication and
weighted interfaces remain in place. This migration does not derive a
general profunctor/coend model for their structural contracts.

The original join whole/point cross rules now use the admitted coefficient.
Their existing reviewer checks both projection orders, next-Hom action,
constant endpoints and retained arbitrary cross data. The late pullback
accumulation rule changes only its family codomain, not the ambient category
owning ordinary functor composition.

## Hom_catd keeps its original action ladder

The [action fragment](production_hom_catd_action.lpfragment) adapts the
original Hom_catd_fapp1_func, Hom_catd_fapp1_fapp0 and
Hom_catd_fapp1_fapp0_point owners to the already selected family interface:

```text
E : K -> Cat_cart
X : Pi over R(K) in O(E)
Y : Pi over K in E

c_X(p) : X[y] -> E[p](X[x])
c_Y(p) : E[p](Y[x]) -> Y[y]

Hom_catd(E,X,Y)[p](h) = c_Y(p) o E[p][h] o c_X(p).
```

Both section cells come from the existing intrinsic action. The displayed
Hom action remains a whole functor with its original stable point head; the
expanded Hom_fapp0 formula is a proof-time view, not a runtime expansion.

The old semantic expression used the middle section action as the positive
Hom source. Under the selected conventional-lax pre/right convention that
middle value is Y[y], whereas this source must be `E[p](Y[x])`. The migrated
expression uses the existing transport action at Y[x]. It does not identify
the two objects or make the section strict.

The comparison pattern retains fully explicit native action and component
expressions. Patterning on the reducible Fibre_cat, catd_transport_func,
piapp0 or TotalOp_cat aliases failed to match the normalized observation.
The selected negative category expression is the primitive R(T(...)) form;
TotalOp_catd itself remains the stable family head. The typed comparison
passes and a changed-filler control rejects replacing h by independent h2.

## Necessary type presentation correction

The original result types of tapp0_fapp0 and fdapp1_int_cell were written
through the injective Hom alias. At the actual Cart/public coefficient and
total-opposite consumers, inference decomposed that alias before exposing
the category computation. Independently checking equality of the relevant
types succeeded; checking a variable against the other Hom presentation
failed. The same variable check using Obj(Hom_cat(...)) succeeded.

These two existing declarations now expose Obj(Hom_cat(...)) in their result
types. Those types are definitionally equal to the originals. No operation,
coercion, proof parameter, naturality rule or strictness condition is added.
All inherited Homd/section controls still pass. The original join rewrite
patterns then typecheck without the extra inferred-argument guards tried
in unsuccessful probes; those guard experiments are not selected.

## Evidence and limits

The [reviewer](production_profunctor_controls.lpfragment) reuses the original
opposite/reindex and join consumers with their migrated coefficient tags,
and adds the corrected whole-to-point Hom_catd observation and typed semantic
comparison. Inherited foundation, Homd, section, general-FF composition and
unit controls are included in the generated profunctor_prefix.lp.

Checks retain subject reduction, warnings, the serial 90-second/2-GiB limit,
64-MiB file limit and OCAMLRUNPARAM=o=20. Exact receipt/source hashes and the
warning-family delta are recorded in the verification file. Warning counts
compare the earlier checked section-17 boundary with the larger section-18z
boundary; they are not a confluence certificate or a proof of a Q model.
The strict rule-LHS audit has no unreviewed compound slots.

The complete emitted source preserves the original downstream tail and now
fails at CommaFib_catd, rather than Op_prof. That old expression still
combines the public Cat coefficient, the newly Cartesian whole Hom and a
same-base fibre transpose. Migrate that actual comma/extraction consumer
next, followed by fdapp1_projection_source/target and their original
projections. Do not compensate with a global strictness exception or a new
standalone laxity witness. Remaining public/downstream promotion and final
gates are unchanged.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet profunctor_prefix.lp
python3 scripts/audit_rule_lhs.py --strict \
  tmp/probes/production_owner_migration/package/profunctor_prefix.lp
```
