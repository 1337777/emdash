# Arrow diagrams through the corrected evaluation profiles

Date: 2026-10-16
Predecessor: `7848669d`
Status: staged original arrow reviewer, focused controls, core and intrinsic evaluation checks pass; terminal/initial arrow integration remains open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification and resource measurements](production_arrow_diagram_verification.json)

## Original owner and corrected contract

The old `transf_arrow_diagram_func` used Cartesian symmetry on a walking
diagram of an arbitrary default-lax transformation. Its asserted target was
Functor_cat(WalkingArrow_cat,C), whose shape naturality has the wrong direction
for that input. The corrected [owner](production_arrow_diagram_families.lpfragment)
uses the same walking diagram and the whole family-shape operation:

```text
eta : Transf(K,C,F,G)
Arr(eta) = family_shape(walking_arrow_func(F,G,eta))
         : K → Functor_oplax_cat(WalkingArrow_cat,C).
```

Eta remains generally lax. No OneCat hypothesis, strict-transformation input,
new comparison cell or equality-proof argument is imposed on it. The point
view decodes an actual functor object with OddDual_func. It is not a coercion
identifying the higher maps of ordinary and oplax diagram categories.
The original point-path theorem is retained on that decoded object, with a
comparison keyed on the actual dual/precomposition and walking constructors.

The [opposite-profile evaluation extension](production_oplax_diagram_evaluation.lpfragment)
is derived by OddDual from the existing evaluation root at OddDual(I),
OddDual(C). Its shape action has the ordinary default-lax transformation
profile. Applying the two exchanges successively recovers the original whole
diagram. This is a declared whole constructor computation at the actual
composition owner, the corrected counterpart of the old symmetry involution;
it is not claimed to follow from object beta alone.

For the walking diagram of eta, its projections compute:

```text
source(Arr(eta))       ↪ F
target(Arr(eta))       ↪ G
differential(Arr(eta)) ↪ eta.
```

These are whole functors and the original whole transformation. Their Hom
actions remain available. The original source/target postcomposition
observations are supplied by the fixed-component and represented-cut
projections of this same double exchange. The original specific sym-head
rules are not copied into an incompatible profile. Nested-parameter callers
remain part of the subsequent original import migration; the arrow reviewer
alone does not establish their coverage.

## Required core projections

The existing Cat-valued postcomposition owner computed as a composed functor;
its precomposition counterpart lacked the corresponding object and Hom
projections. The [new projections](production_cat_precomposition_actions.lpfragment)
follow that same outline and retain the represented precomposition head.
They expose G composed with E[h], including its complete Hom functor. They
do not replace every represented cut by raw composition.

The [fixed-prewhiskering clause](production_fixed_precomposition.lpfragment)
is the counterpart of the existing fixed-postwhiskering composition clause.
Both first transformation legs must be the same literal identity. General
two-leg interchange is not asserted.

The manual inferred-slot review also removes three reducible OddDual_cat
source-endpoint patterns in the exchange clauses. The source is recovered
from the actual dualized functor argument instead. This includes owner-specific
slots beyond the generic-head audit script's inventory.

The identity observation compares two existing normal forms: an identity at
a raw composite functor and an identity at its represented precomposition
view. The original identity assertion is therefore now typed reflexivity,
using the existing comparison. An extra Cat-specific identity clause did not
change this reduction and was rejected. The mixed-arrow observation also uses
an explicit canonical Obj(Hom_cat ...) classifier to avoid prematurely
inverting Hom across a duality; its selected arrow data are unchanged.

## Qualification and resource boundary

The [migrated original reviewer](production_arrow_diagram_reviewer.lpfragment)
retains all 22 positive and two negative observations: points, generator,
base-arrow action, identity/composition, whole source/target/differential,
next Hom action, represented postcomposition and wrong-data controls.
The [focused controls](production_arrow_diagram_controls.lpfragment) separately
cover general double exchange, its next Hom, the genuine profile distinction,
the constructed generator's value and the identity-leg restriction.

The first placement of the new exchange rules preceded the prerequisite
imports. The original reviewer hit the 2 GiB allocation guard with o=20;
o=5 passed on the identical inputs in 56.238s. Owner-only checking with o=5
took 58.241s, locating the extra cost in loading/formation rather than the
reviewer's assertions. Moving the same new definitions/rules after the
prerequisite imports and existing evaluation helpers restored a green o=20
reviewer in 28.529s. The memory ceiling, subject reduction, warnings and
other safeguards were unchanged. No broader memory authorization was used.

Keep the original reviewer and supplementary controls as separate targets.
The combined diagnostic process hit the same cap after completing the
original reviewer. Its failure is retained as resource evidence; assertions
are not deleted from the original reviewer to reduce the target.

A supplementary experiment demanded that an entire generator-image functor
normalize to a chosen constant terminal-source presentation. That is stronger
than the original migration contract and was not used to justify another
kernel rule. A future actual consumer can review this contextual whole join
comparison. The current checks retain the constructed whole functor and
evaluate its generator value, together with the original whole diagram and
transformation observations.

The changed core passes its inherited 258 positive/62 negative controls in
17.374s. The original arrow reviewer passes 22 positive/two negative controls;
the separate focused driver passes five positive/three negative controls.
The previous intrinsic evaluation comparison passes its six positive/three
negative controls on the current source. The latter focused checks take
about 28 seconds with o=20, 90s/2GiB and subject reduction. Warning comparison
adds 22 reports, all belonging to the new precomposition projection/closure
interactions; no inherited report disappears. Typed consumer evidence is not
a global confluence claim.

The broader importer still needs o=5 at the same 2 GiB cap to reach its next
semantic error; its o=20 allocation failure remains recorded. With earlier
collection it reaches terminal_arrow_diagram_func in
emdash3_2_zero_arrow_diagrams.lp and reports the expected ordinary-versus-oplax
diagram-category mismatch. This is a separate target/resource qualification,
not evidence that every broad import now fits o=20.

## Next coupled original owner

Review terminal_arrow_diagram_func, initial_arrow_transf and
initial_arrow_diagram_func together. The current terminal-arrow input is a
general Transf. Its object/arrow cuts make the visible triangle commute, but
do not by themselves qualify its extracted higher cell as a strict transfor.
The current TerminalObject module declares contractibility of the Hom object
groupoid; do not silently replace that statement by strict enriched terminality.
Inventory actual producers before changing the terminal contract.

The original initial-arrow body applies dimension-one Op_transf, now a strict
transfor operation, to that unqualified terminal transfor. A total-dual
presentation can preserve the default lax profile but changes the dual
terminal hypothesis; another profile can change the transformation direction.
Settle these actual types and the whole zero-arrow embeddings before adapting
the supplied kernel/cokernel adjunction packages. Do not globally equate lax
and oplax diagrams, infer OneCat from PreadditiveCategory, or strengthen every
terminal transformation solely to keep the old spelling.

Public promotion, remaining original library callers, strict-wrapper
retirement, catalog/health/CI and source-pin review remain open. This is still
the foundations goal; no separate nerve/equivalence work is being resumed.

Replay from emdash2:

```bash
python3 audits/strict-default-action-boundary/production_owner_migration.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20,v=1024 \
  python3 scripts/run_lambdapi.py \
  --package-root tmp/probes/production_owner_migration/package \
  --no-colors --quiet examples/arrow_diagram_families.lp
```

Use the same guard for arrow_diagram_migration_controls.lp,
diagram_evaluation_naturality_controls.lp and inverse_core_controls.lp.
