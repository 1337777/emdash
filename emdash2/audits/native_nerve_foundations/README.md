# Native nerve adaptation: receiver evidence

Status: non-library NF-1 reconstruction and NF-2C cube construction on the corrected foundations.
Owner: [adaptation plan](../../../docs/EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md).
Receiver baseline: `e8ffc4d0`; legacy donor: `280e7a03`.

## Geometric maps in every dimension

The [degree-zero continuation](geometric_degree_zero_review.md) now combines
actual terminal evaluation/constants with the positive recursion. Whole
encoder and decoder maps exist at every degree, with whole Hom action at a
variable dimension. The first zero round trip and whole parameter-family
recovery pass; reverse terminal reconstruction remains open already in the
ordinary mapping profile.

The final **69-input** qualification passes in **108.523s / 615,940 KiB**.
`zero`, `all-degrees`, and `zero-eta-pending` replay modes retain the positive
and failed scopes separately. This extends map formation; it does not close
the inverse, common-index or degeneracy requirements below.

## Whole reindexing and the remaining exchange equation

The [reindexing/reflection extension](exchange_cancellation_review.md) checks
whole evaluator naturality, both family reindexing directions and reflection
through the existing double exchange. It reduces the first internal exchange
inverse to one explicit universal-evaluation equation. The reduction passes
in **84.410s / 603,372 KiB** across 65 inputs; the equation itself still fails
its proof attempt and is not supplied as an axiom or operational argument.
The new `reindex`, `reflection` and `evaluation-pending` replay modes retain
both boundaries. Previous reverse-map replay modes retain their exact source.

## Whole reverse geometric maps

The [reverse construction](reverse_review.md) now supplies whole maps from
native cubes to geometric cubes in every positive dimension. Two uses of
mixed exchange put the universal curried diagram into the existing right
uncurry interface. No tensor-action or reverse-closure primitive is needed.
The explicit older lax classifier has a canonical admission from the current
default; ordinary transformations and their higher cells are retained.

The final **61-input** check passes in **85.162s / 583,624 KiB** with subject
reduction. It includes the earlier forward construction, whole-family
readbacks, and profile unit/composition controls. Staging the existing OddDual
composition theorem proves the entire mixed-exchange object readback.

Whole cancellation of mixed exchange still fails its direct proof. Both
geometric inverse laws remain required; maps in two directions are not yet an
equivalence. Follow the current [outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
and [exact replay record](reverse_verification.json). The earlier sections
below retain their checkpoint boundaries; their old next-step instructions
do not override the current inverse-proof work.

## Forward geometric decoder at every positive dimension

The [new construction and review](postcomposition_review.md) supplies a
structural whole postcomposition owner with ordinary lax parameters. Its
opposite-profile version, walking-first forward curry and positive-dimensional
geometric decoder are defined composites and internal Nat recursion. They
preserve the original tensor order and directed interchanger. The two actual
iteration-shift maps have derived whole inverse laws independent of the
unfinished second walking inverse.

The 54-input combined check passes in **97.488s / 595,020 KiB**, with subject
reduction, whole/capped projections, unit/composition, the explicit next-Hom
component and noncollapse controls. Typed proof-time pre/right controls pass
separately in **71.555s**. [Exact evidence and failed attempts](postcomposition_verification.json)
are recorded separately. `replay_postcomposition.py` reconstructs the checked
sources; `--assemble-only` checks source identity without another checker run.

This is a forward construction relative to the new structural owner, not a
derived closure equivalence. Raw nested next-Hom normalization and the
Cat_cart specialization remain explicit computational limits. Reverse closure,
geometric degree zero, the second native inverse, common-index comparisons,
degeneracies and production promotion remain required. Continue the reverse
geometric construction without making either local normalization issue the
sole next task. The sections below retain the preceding checkpoints.

## Whole first round trip at every dimension

The [composition proof](lift_composition_staged.lpfragment) now stages the
existing Odd-dual composition law before the represented postcomposition cut.
Its specialization gives the required whole G_I composition comparison. No
new unification bridge or runtime rule is needed.

The [Nat-inductive retraction](cube_retraction.lpfragment) derives

```text
encodeₙ ∘ decodeₙ ≐ id_Wₙ(C)
```

for every C and variable n, using the actual recursively defined maps and the
existing first walking inverse. The induction step is proof-only: its induction
hypothesis is not an extra operational argument of decode or encode. The
reverse round trip still needs the native second walking inverse.

The [consumers](cube_retraction_controls.lpfragment) recover complete
K-parameter families and the concrete tensor coevaluation diagram. An unrelated
replacement family is rejected. The 44-input check passes in **131.887s /
595,104 KiB** at 180s / 2 GiB with subject reduction. All five warning-inventory
fields match the preceding retraction check. [Exact evidence](retraction_verification.json)
and `replay_retraction.py` retain `composition`, `retraction`, and `interface`
modes, with exact `--assemble-only` checks. This remains non-library evidence
relative to the existing walking structural interfaces, not a geometric nerve
equivalence or production qualification.

The geometric investigation now has a precise next interface. With
G(A,B)=Functor_oplax_cat(A,B), whole oplax-parameter postcomposition would have

```text
P(I,A,B) : G(A,B) → G(G(I,A),G(I,B)).
```

Its fixed-D Hom component is already [constructed and checked](oplax_postcomp_interface.lpfragment)
by the existing oplax precomposition functor. Its value at i retains the
original component of alpha at D[i]. The walking-first curry consumer of P
also typechecks, while the existing Cartesian parameter map is rejected in
that slot. The 39-input interface check passes in **122.223s**, with unchanged
warning inventory relative to the preceding square consumer.

At this preceding checkpoint P itself was not declared or assumed. The new
[structural owner and forward construction](postcomposition_review.md)
supersede that formation boundary while retaining their listed computational
limits. Neither checkpoint closes the geometric-closure equivalence milestone.
The [outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
records the exact next construction and source-profile boundary.

## Whole iterated-walking cube maps and implementation outline

The user requested an end-to-end construction pass while the local native
reconstruction comparison remains open. The [implementation outline](../../../docs/EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
now separates the geometric tensor bridge from an executable intermediate:

```text
G_I(C) = Functor_oplax_cat(WalkingArrow,C)
W₀(C)=C,       Wₙ₊₁(C)=G_I(Wₙ(C))
NC₀(C)=C,      NCₙ₊₁(C)=N(NCₙ(C))

d₀=e₀=id_C
dₙ₊₁=Observe_NCₙ(C) ∘ G_I(dₙ)
eₙ₊₁=G_I(eₙ) ∘ Realize_NCₙ(C).
```

The [whole recursive maps](cube_walking_iterates.lpfragment) are genuine
internal Nat eliminations. They have no closure-map, strictness-proof or
inverse-law parameters. [Fixed oplax postcomposition and the degree-two maps](cube_curried_maps.lpfragment)
use existing Odd-dual action and ordinary fixed postcomposition. No Cartesian
joint composition of general lax transformations is assumed, and these
particular composites do not require a new native-arrow lifting profile.

The 38-input [square consumer](cube_skeleton_consumer.lpfragment) passes in
**116.183s / 583,852 KiB** under 180s / 2 GiB with subject reduction. Its imported
recursion checks all six degree-zero/one/two equations and has whole first and
next-Hom owners at variable n. The original tensor walking-square coevaluation
is an actual input: its decoded square compares with the native square built
from the existing whole coordinate family, retaining its two edges and arrow.
This does not separately prove equality with the named interchanger constant.

The generic tensor-to-curried map and reverse map remain explicit missing
interfaces. Two conditional composition helpers check their exact consumer
types; neither helper postulates those maps or their inverses. A control rejects
substitution of the differently profiled right Gray curry map. Wₙ is an
independent intermediate, not a redefinition of the geometric mapping category.
Its zero case does not prove geometric terminal-diagram reconstruction.

No primitive, rewrite, unification rule or inverse axiom is added in this
slice. All five warning-inventory fields match the preceding maps-only check.
[Exact evidence](cube_verification.json) pins the added existing library sources,
all new definitions and the import closures. `replay_cube.py` supports `maps`,
`square` and `composition`, each with `--assemble-only`. The last mode preserves
the failed earlier composition proof and returns failure; it is not a green
gate. The first two reconstruct their checked sources exactly.

**Next dependencies:** prove fixed oplax postcomposition's whole composition
comparison at its generic owner, use the first walking inverse for the first
recursive round trip, and construct the correctly ordered geometric closure.
The second walking inverse, complete round trips, same-index action, independent
native simplex totals and both degeneracy extensions remain required. The
[actual-Hom action investigation](actual_action_pending/README.md) is preserved
separately, including its focused progress, unqualified overlap and still-failing
whole-section comparison. It is not a prerequisite of these map definitions
and its pending normalization rules were not used in this check.

## Canonical moving-boundary cells and whole filler inclusion

The [whole family comparison](moving_family_proofs.lpfragment) now identifies
the actual native Hom's a-index family with its represented presentation:

```text
Hom_N(C)((x,y,u),(x′,y′,v)) ≐ Σ(a : Hom_C(x,x′)),
  Hom_PathOut_C(x)((y,u),(y′,v∘a)).
```

This is a proof-time comparison of the entire family, followed by Sigma. It
retains the original functor and fixed endpoint; three controls reject a
different functor, endpoint, or dimension-one replacement of total duality.
It does not add an operational equality cast or erase the actual native owner.

In that canonical presentation, the [moving cell](moving_cell.lpfragment)
accepts independent A:a⇒a′, B:b⇒b′ and the genuine higher filler

```text
Γ : (v▹A) ∘ α ⇒ β ∘ (B◃u).
```

The target uses the existing stable precomposition head. The staged
[raw-composition reading](moving_precomp_raw.lpfragment) explains its ordinary
formula without a global runtime expansion. Earlier direct raw endpoints
failed unification even though the computed fibre has this orientation.
The constructor is the existing nested Sigma pair; no new cell primitive,
strictness premise, inverse, or separately supplied comparison is introduced.

The [whole filler functor](moving_filler_func.lpfragment) is a composite of
[existing Sigma fibre inclusions](moving_fibre_inclusions.lpfragment), with
their actual total dualities. Its value agrees at proof time with the moving
constructor. Both boundary projections compute, and a different Γ is rejected
by the [controls](moving_controls.lpfragment). Literal full-tuple runtime
conversion did not pass. A bare nested Γ-projection comparison stopped during
type inference, so the appended next-Θ observation was not reached. Do not
claim those stronger runtime readbacks from the whole value comparison.

The only new runtime clauses are the two
[constructor-scoped postcomposition rules](moving_sigma_postcomp.lpfragment):
postcomposing a visible total arrow `(p,alpha)` by a vertical fibre inclusion
computes its fibre composite; the same holds after an actual strict functor
into that fibre. Generic pre/postcomposition owners remain stable. The
[whole total-Hom family view](moving_total_hom_view.lpfragment) is proof-time.
Removing the two constructor clauses makes the required canonical moving
consumer fail at its transport comparison.

The complete **68-input** native prefix passes in **128.850s / 597,312 KiB**
at 180s / 2 GiB, preserving the earlier first inverse, totalization, original
filler and graph-factorization checks. [Verification](moving_verification.json)
records all selected source hashes and fifteen exploratory/qualification
outcomes. Exactly four warning bodies are added after line mapping, all at
the vertical-postcomposition owner; ordinary/total-dual units and raw/stable
composition reducts have [typed joins](moving_postcomp_joins.lpfragment).
The [warning review](moving_warning_review.json) retains their scope; it is
not a global confluence proof. The strict LHS audit reports no unreviewed clause.

**Remaining boundary:** the [direct actual-native constructor](moving_actual_candidate.lpfragment)
still fails at its expanded whole transport/Hom comparison. The canonical
construction and family equality do not silently convert that operational
interface or prove the second inverse. Continue that actual higher comparison,
then whole native reconstruction; full-module and production promotion remain
open. All work here is non-library.

`replay_moving.py` supports `family`, `canonical`, `integration`, `without-beta`
and `actual`, each with `--assemble-only`. The latter two reproduce the recorded
failures and return failure; `actual` is an unresolved required construction,
not a green negative gate. The replay uses the previous exact transport
assembly, verifies source/checker hashes, and changes no production source.

## Represented boundary transport and Sigma inclusion

[`transport_native_proof.lpfragment`](transport_native_proof.lpfragment)
compares the **whole extracted** transport in the native Hom family with
its explicit represented form:

```text
T(x,x′,y′,v) : Hom_C(x,x′) → PathOut_C(x)
T(x,x′,y′,v) ≐ inclusion(y′) ∘ postcompose(v).
```

Its object is `(y′,v∘a)`. The input map is the total dual of the existing
fibre-covariance map for the actual `homdc_op_edge_catd` family. This is a
comparison of complete functors, retaining higher variation of a. It does
not replace the native family or take an equality proof as operational input.

The proof uses small [generic comparisons](transport_generic_proofs.lpfragment)
for fixed-object Cartesian evaluation, Cartesian Sigma-map evaluation at a total pair,
and the component of represented precomposition. Primitive duality evaluation
and its other distribution order compute; the represented-component and
precomposition comparisons preserve their runtime heads. Explicit source,
middle and target categories avoid an observed inference failure. The staged
proof avoids the failed attempt to compare one expanded composite by reflexivity.

The [existing Sigma fibre inclusion](transport_sigma_inclusion_hom.lpfragment)
now exposes its whole Hom through the same inclusion in the negative
Sigma-Hom family. Its capped action is `(id_k,h)`. Both projection orders and
the next Hom retain the original h and higher cell Γ; distinct replacements
are rejected. No additional operational primitive is declared.

The identity overlap revealed a missing [Sigma identity comparison](transport_sigma_identity.lpfragment).
The selected proof-time view relates the visible total identity to the pair
of identities while retaining the runtime identity head for generic functor
unit matching. Base and fibre nonidentity substitutions are rejected. The
first, more elaborate inferred-carrier constraint triggered a checker
assertion and is not retained. The successful view uses the typed equality's
inferred carrier and compares both actual entries.

Qualification: the 58-input native prefix passes in **127.501s / 598,308 KiB**
under 180s / 2 GiB, retaining the first inverse, graph factorization and whole
fixed-boundary filler results. The strict LHS audit has zero unreviewed
clauses. Nine additional identity-overlap reports are classified: ordinary,
T, R, O, dimension-two, Catd, terminal, odd and even source presentations.
Their canonical typed comparisons pass, including the separate parity check.
Generic runtime identity/pair equality is deliberately not asserted, and no
global confluence or production-promotion claim follows.

**Remaining boundary:** the [intended moving-boundary constructor](transport_moving_boundary_candidate.lpfragment)
still fails with both Sigma carrier families explicitly annotated. Its last
constraint compares the actual Homd/negative-Sigma fibre with the proposed
ordinary higher-cell family. Thus the failure is not resolved merely by
supplying tuple metadata. This remains an unfinished construction, not a
negative acceptance test or a mathematical nonexistence result. Continue at
that whole family comparison; do not add an inverse or strengthen arbitrary
lax naturality to close it.

The [verification record](transport_verification.json) retains the exact
successful and failed source closures. It also records the discarded eager
total-Hom rules, their unnecessary incoming-unit extension, and the uninstalled
larger boundary-extraction draft. These are not part of the selected source.
`replay_transport.py` supports `generic`, `parity`, `integration` and `moving`
modes, each with `--assemble-only`. The `moving` mode reproduces the failed
constructor and returns failure; it is not a green gate. Production sources,
the completed book work and the separate frontend integration task are untouched.

The semantic review consulted the recursive Hom description of cylinders in
[Ara–Guetta, §§22–26](https://arxiv.org/html/2503.08832v1#S2), which retains both
boundary-cell coordinates. This motivates checking boundary variation beyond
fixed fillers; it supplies no proof of the repository's Sigma presentation or
the missing native inverse.

## Sigma factorization and whole filler readback

The [section postcomposition view](section_postcomp_owner.lpfragment) adds
one proof-time structural comparison with composition in `Catd(K)`. It
retains the original displayed map FF and section s; neither is made strict
or discarded. The no-rule check fails at precisely these two whole heads,
and the retained [comparison controls](section_postcomp_comparison.lpfragment)
reject substitutions of either argument. Runtime computation is unchanged.

Using that view, existing Sigma functoriality and the totalization result
below, [`section_total_postcomp.lpfragment`](section_total_postcomp.lpfragment)
**derives** the whole comparison

```text
Sigma(FF) ∘ total(s) ≐ total(section_postcomp(FF,s)).
```

The [graph factorization](graph_factorization_owner.lpfragment) applies it
twice to the actual represented-comma implementation. The resulting whole
map is total duality applied to: projection base change, Sigma of the
existing base-change displayed map, Sigma of the existing internal-action
displayed map, and totalization of the original represented identity section.
All original maps and the whole internal action remain in this expression.
The [native consumer](graph_factorization_consumer.lpfragment) derives the
same presentation for `Observe ∘ Realize`; no inverse or reconstruction
equation is added.

Separately, [`whole_filler_readback.lpfragment`](whole_filler_readback.lpfragment)
derives the identity of the **entire** filler endofunctor:

```text
ev_id ∘ Whisker(F,G,p,u,v) ≐ id_S,
S = Hom(Hom_B(F[y],G[z]), G[p]∘u, v∘F[p]).
```

This uses the previously checked generic evaluation comparison and its
identity specialization; it adds no rewrite rule. The native specialization
uses arbitrary native q, r, p and their original stored arrows. An arbitrary
replacement endofunctor is rejected. This includes all higher cells inside
that fixed-boundary filler category. It does **not** by itself establish the
comparison when boundary arrows vary, or the identity of the whole native
Hom/Sigma map. Those remain the reconstruction obligation.

The [verification record](factorization_verification.json) pins every source
and all six runs. Generic totalization compatibility passes in 28.940s;
generic whole filler recovery passes in 24.811s. The 49-input native replay
passes in 161.782s / 592,604 KiB under 180s / 2 GiB, retaining the first
inverse and inherited higher-cell controls. All five warning inventory
fields match the preceding candidate after exact line mapping; the strict
LHS audit reports no unreviewed clauses. The inherited overlap and full-module
promotion gates remain open. Production sources are unchanged.

Replay with `replay_factorization.py --mode generic`, `--mode filler`, or
`--mode integration`. Each supports `--assemble-only` to verify its exact
checked closure without repeating validation. Continue with the full
Homd/Sigma action and canonical reassembly, preserving boundary variation;
do not replace that obligation with more fixed-filler observations.

## Whole section totalization through Sigma

The [new candidate](section_sigma_totalization.lpfragment) connects the two
existing whole constructions:

```text
total(s) ≐ Sigma(s) ∘ (id_K, const(*)),   s : Pi(E).
```

This uses one [generic structural presentation law](section_sigma_totalization_owner.lpfragment).
It is an added contract for section totalization, not a theorem inferred
from matching object/arrow projections. Its pattern retains K, E and the
original section; a different section is rejected. Runtime heads are kept,
and operational symbols acquire no equality-proof inputs.

The complete Hom compatibility is then **derived**, using the existing
negative-index total family and `piapp1_func`. The expanded Sigma-map Hom
agrees with the total dual of `Sigma(piapp1_func(s,x,y))` after the product
unit. Equality action on total duality applies the same whole structural
presentation to that section, giving the direct `section_total_func` Hom.
This checks both actual Hom constructions, beyond their arrow objects.

That derivation exposed a missing computation: T and R had no componentwise
action on explicitly paired product-valued functors. Two
[constructor rules](dual_pair_owner.lpfragment) supply it. They preserve both
functors and join the whole-first/Hom-first duality observations and double
duality; an unrelated component is rejected. They add no warning family in
the checked core. The failed pre-repair comparison isolates this exact pair
versus dual-pair mismatch.

The [native consumer](section_sigma_native_consumer.lpfragment) uses the
existing generic projection-pullback interface before specializing C. It
expresses both `Observe ∘ Realize` and the tautological total through this
Sigma-map presentation. Their remaining whole comparison is still required;
no native inverse or graph-section reconstruction law is added. Literal
reflexivity of the expanded Hom remains insufficient: the accepted Hom
comparison uses the stated derivation.

Exact sources, checks and diagnostic failures are recorded in
[`section_sigma_verification.json`](section_sigma_verification.json).
The complete Hom comparison passes in 51.916s / 174,688 KiB; the 45-input
native integration passes in 168.010s / 590,740 KiB under the 180s / 2 GiB
guard. All five warning inventory fields match the preceding native prefix
after mapping unchanged core lines. The inferred-slot audit reports zero
unreviewed clauses. No aggregate or unchanged frontend/book gate is rerun.
Replay with `replay_section_sigma.py --mode generic` or `--mode integration`;
`--assemble-only` verifies the corresponding exact input closure without
repeating the checker. This remains an isolated prefix candidate. Production
promotion, full-module qualification and inherited overlap obligations remain
open.

## Whole walking observer and tensor coordinate family

[`walking_observer.lp`](walking_observer.lp) is a fresh receiver construction,
not a copy of the legacy oplax classifier. It contains definitions and
focused observations only: no new axiom, rewrite rule or unification rule.

Writing I for WalkingArrow, G(C)=Functor_oplax_cat(I,C) and
N(C)=LaxArrow_cat(C), it constructs

```text
Observe_C : G(C) → N(C)
L_B       : B → G(I⊗ᴿB)
Observe_(I⊗ᴿB) ∘ L_B : B → N(I⊗ᴿB).
```

The first map is the existing native graph applied to the current whole
oplax-diagram evaluator. Its LaxTransfor admission is derived from the default
pre/right computation, rather than supplied by the caller. The original
input diagram's generator is recovered using the existing admission-carrier
path. This path is proof-only comparison data; no operational map takes an
equality certificate as an argument.

The whole first action computes to the existing native square constructor,
with both side arrows and the typed `gray_transf_standard_cell` retained.
That cell is already defined from internal post/left laxity; it is not a new
filler. The next Hom is a functor obtained by applying the same observer's
generic action again. General post/left naturality is not made strict.

L_B is constructed from right coevaluation, the existing Gray-Hom inclusion,
and the current mixed exchange. It requires none of the legacy candidate's
separately supplied strict-object admission properties. At B=I the resulting
native coordinate family recovers both original outer-coordinate edges of
the Gray walking square. This is a concrete whole tensor consumer, not yet
the whole closure map for arbitrary tensor diagrams.

## Exact boundaries

The construction inherits the existing graph, right-closure, duality and
evaluation interfaces at the pinned receiver source. It does not prove an
independent semantic model of those structural declarations.

Still required:

- general native universal-arrow realization and both whole walking inverse
  laws (the isolated realization candidate below now supplies the forward
  construction; its prerequisite is not promoted);
- comparison of the observed tensor square's filler with the separately named
  `gray_interchanger`, including its higher observation;
- whole opposite closure in arbitrary tensor diagrams and its reverse map;
- all subsequent NF cube, simplex, common-index and degeneracy obligations.

The raw expanded generator assertion failed through the retained admission
view. Replacing it with typed reflexivity alone also failed. The accepted
object comparison uses the already available whole admission-carrier theorem
and equality action; no expression-fold rule was introduced.

A hand-expanded square assertion failed while checking its inline cell's
endpoint presentations. The retained assertion uses the existing typed cell
owner and checks the complete square. Its underlying internal-action body is
unchanged. This does not qualify arbitrary inlining of that body; retain the
failed source snapshot if such an expanded view later becomes a real consumer.

## Replay and evidence

From the repository root, use the supported checker with the usual guard:

```bash
nerve_checker_dir="$(python3 scripts/verification-toolchain.py batch-path)"
PATH="$nerve_checker_dir:$PATH" OCAMLRUNPARAM=o=20,v=1024 \
  EMDASH_LAMBDAPI_WARNINGS=1 \
  python3 emdash2/scripts/run_lambdapi.py --no-colors --quiet \
    --timeout-ms 90000 audits/native_nerve_foundations/walking_observer.lp
```

The [verification record](verification.json) retains source/checker hashes,
the original diagram-evaluation baseline, failed hypotheses, retained replay,
resource measurements and warning comparison. Logs and exact input blobs
remain in the receiver's ignored receipt store. No production owner or check
registry entry is added by this non-library checkpoint.

## Native realization and whole generator recovery

[`walking_realization.lpfragment`](walking_realization.lpfragment) constructs
`Realize_C : N(C) → G(C)` using the existing transformation-to-walking-diagram
operation. It adds one structural owner, the native universal transformation
`U_C : src ⇒ tgt`, with six projection rules. Its point component is the
stored native arrow, its whole right Hom action is existing postcomposition
after source action, and its extracted post/left cell recovers the original
native square filler. The unit rules are specific to this projection; general
lax naturality remains nonidentity. A protected typed identity view uses an
existing postcomposition comparison without a new unification rule or an
equality argument.

The existing mixed diagram exchange derives a comparison of the **whole**
realized walking family with `walking_arrow_func(src,tgt,U_C)`, and hence
recovers the entire transformation U_C at its generator. These are defined
reflexivity proofs, not new inverse axioms. The new U_C itself is structural
data, not a theorem derived from the previous Sigma projection rules. Neither
whole walking inverse is established by this checkpoint.

The candidate requires the two identity instances in
[`total_dual_postcomp_units.lpfragment`](total_dual_postcomp_units.lpfragment).
They are inserted at the existing postcomposition owner in an isolated copy:
total duality erases the identity's original category tag, so the ordinary
identity pattern does not cover this source presentation. Whole, capped and
higher identity observations pass, with a negative control for an arbitrary
nonidentity arrow. Production sources remain unchanged.

The [realization record](realization_verification.json) pins every input,
the exact patched core, replay artifacts and sixteen measured attempts. The
retained candidate passes in 46.854s / 288,032 KiB with subject reduction and
the 180s / 2 GiB guard. Its eight positive and two negative controls exclude
the inherited observer checks. All five warning inventory fields equal the
patched-import baseline. The two core instances add **31 reported critical
pairs** relative to the unmodified imports, in nine recorded head families;
their full overlap/owner qualification is still a prerequisite to promotion.

A local alternative using generic typed unit views passes subject reduction
without the core instances but fails the actual unit-component check. It is
not adopted. Two earlier 90s timeouts occurred in unchanged imports, before
the new whole comparison; the later timed replay locates 108.15s in the first
import and no candidate command above 0.5s. This is not evidence that the new
comparison itself needs that time, nor a reason to alter resource defaults.

Replay the isolated candidate from the repository root:

```bash
python3 emdash2/audits/native_nerve_foundations/replay_realization.py \
  --timeout-seconds 180 --timing
```

`--mode units-baseline` checks the same imports with the two core instances.
`--mode without-units` retains the failed omission control and its actual
nonzero status. The replay enforces source/checker pins and uses the existing
serial guard. No broad health or integration check is required to retain this
non-library experiment. Next: whole graph reconstruction and the two actual
inverse laws, with the prerequisite boundary kept visible.

## Whole reconstruction of oplax walking families

[`walking_generation.lpfragment`](walking_generation.lpfragment) derives,
for arbitrary K, C and D:K→G(C),

```text
transf_arrow_diagram(eval₀∘D, eval₁∘D, generator(D)) ≐ D.
```

Here `generator(D)` is the entire ordinary-lax transformation obtained by
mixed evaluation of the oplax diagram family. The proof first reconstructs
the whole functor I→Functor_cat(K,C), then applies the existing opposite-profile
exchange and its double-exchange computation. It retains all parameter action;
it is not reconstruction from pointwise equality or a OneCat restriction.

The proof uses one explicit structural source-generation comparison in
[`walking_generation_self.lpfragment`](walking_generation_self.lpfragment):
self-recursion of the walking shape's original edge is its identity functor.
This comparison is inserted before the existing postcomposition cut in the
walking introduction owner. It is not inferred from beta-only Join, and it
is not an Observe/Realize inverse axiom. The current kernel already supplies
the donor's other prerequisite, strict postcomposition of walking recursion,
so no second postcomposition or exchange-congruence rule is copied.

The [verification record](generation_verification.json) pins fifteen receiver
inputs and the retained replay. The no-comparison control fails at exactly
the source-generation proof. The owner-position candidate passes in 126.613s /
274,716 KiB under 180s / 2 GiB, including a negative control for a different
opaque edge. Its import command accounts for 125.66s; no subsequent command
reaches the 0.5s timing threshold. Warning categories, head families, term
heads and parser issues are unchanged; two existing warnings merely move
from owner line 44 to line 54. This slice does not require the realization's
unpromoted core-unit instances.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_generation.py \
  --timeout-seconds 180
```

`--without-generation` reproduces the omitted-law failure. Production sources
are unchanged. The next missing input to the walking inverse derivation is
the native graph's **whole** source, target and universal-transformation
projections. Its currently checked point/square projections do not alone
supply those comparisons; retain that distinction when adapting the donor.

## First whole walking inverse

The [whole generator construction](graph_whole_generator.lpfragment) and
[inverse proof](walking_first_inverse.lpfragment) now derive

```text
Realize_C ∘ Observe_C ≐ id_G(C),
where G(C) = Functor_oplax_cat(I,C).
```

The actual maps are the observer and realization already retained above.
The proof reconstructs the whole realized graph, specializes it to the whole
oplax-diagram evaluator, and uses its existing admission-carrier comparison.
The conclusion is equality of entire functors on G(C), not only their object
values. It uses no OneCat restriction, inverted filler or inverse axiom.

Three structural graph beta comparisons are added: the whole source and
target recover F and G, and prewhiskering the native universal transformation
by `Graph(L)` recovers the original whole `lax_transfor(L)`. The endpoint
clauses are in [their owner-position fragment](graph_endpoint_projections.lpfragment);
their [typed consumers](graph_endpoint_controls.lpfragment) distinguish whole
comparison from the earlier point/square computation. These complete the
selected graph interface; they are not claimed to follow from its old
point-only rules or to derive its represented-Sigma implementation.

The transformation projection uses **fixed precomposition**, retaining
ordinary lax transformations. The donor's joint Cartesian composition formula
is not copied. A protected typed identity view compares its stable endpoint
heads with raw composition using an existing generic comparison. It adds no
runtime rule, endpoint unifier or equality-proof argument. The initial raw
omission control failed while forming its type; the corrected, well-typed
omission control rejects the whole beta before that comparison is introduced.
Further controls keep distinct input transformations and source/target
functors distinct. All inherited original-filler and unit checks still pass.

The [verification record](graph_verification.json) pins the source closure,
three isolated owner patches, four assembled programs and five run receipts.
The retained combined candidate passes in 284.394s / 554,804 KiB under the
explicit 300s / 2 GiB profile. Its first import takes 265.32s, the realization
import 13.44s, and the whole universal-cell comparison 4.69s. A prior 180s
run stopped in imports; the subsequent repaired proof was not timed out.
All five warning inventory fields equal the completed-import baseline.
The inherited 31 core-unit overlap warnings remain an unpromoted prerequisite.
No production source or resource default changes in this checkpoint.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --timeout-seconds 300
```

The replay's assembly has also been checked byte-for-byte against the passing
receipt without rerunning the expensive checker. The **other** composite,
`Observe_C ∘ Realize_C ≐ id_N(C)`, remains open. It requires reconstruction of
the original native total and the universal graph's whole higher action;
the first inverse does not imply it. NF-1, its production qualification and
all subsequent cube/simplex stages remain incomplete.

## Native composite as the original universal graph

The [native-composite derivation](native_composite_graph.lpfragment) now proves

```text
Observe_C ∘ Realize_C ≐ Graph(U_C).
```

U_C is the same whole native universal transformation used to construct
Realize. Its original post/left filler is retained. This comparison does not
identify Graph(U_C) with the native identity; a negative control still rejects
that identification.

The [new owner comparison](graph_reindex_owner.lpfragment) supplies structural
graph reindexing: `Graph(L) ∘ H ≐ Graph(H*L)`. H is strict by the public default;
L remains a general classified lax transformation. The comparison retains
both endpoint functors and the full reindexed carrier as residual obligations.
An unrelated transformation cannot replace L. This is a whole graph
constructor law, not an inverse axiom or a conclusion from point agreement.

Two generic proof definitions compare oplax-family evaluation with fixed
prewhiskering and forget the evaluator's admission before the parameter map
is specialized. The native evaluator proof then composes that result with
the retained whole-generator theorem. Direct reflexivity at the expanded
realization failed, as did a chain that still performed admission-forgetting
only after specialization. Staging that equality action at the generic family
owner resolves both failures without new runtime rules or endpoint unifiers.

The [verification](native_composite_verification.json) records those two
failures and the passing candidate: 123.314s / 536,172 KiB under 300s / 2 GiB.
All five warning inventory fields match the complete-import baseline. The
first inverse and the inherited directed-filler, unit and distinct-input
controls remain checked. The replay extends the existing graph replayer;
assembly of both its old default record and the new record is byte-identical
to their passing inputs, without rerunning either expensive check.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --record native_composite_verification.json --timeout-seconds 300
```

The remaining step is a whole comparison of this original graph with the
tautological Sigma reconstruction. Current source already provides
`tapp1_int_cart` for the source-variable profile and
`represented_comma_family_func` at J=id as a candidate Sigma implementation.
That avoids a new admission premise. Its connection to the public graph and
the actual native reconstruction still need qualification. Prepared Sigma
source-generation fragments remain unqualified scratch work; they do not
supply the missing nerve inverse or change production code.

## Existing represented-Sigma graph consumer

[`native_sigma_graph.lpfragment`](native_sigma_graph.lpfragment) now checks
the existing `represented_comma_family_func` at J=id as a whole map
`B → N(C)` for a general ordinary-lax eta:F⇒G. Its source-variable admission
is the existing `tapp1_int_cart`; no new profile premise is supplied. The
component is the original `(F[x],G[x],eta[x])`, and the native U specialization
has type `N(C)→N(C)`.

This adds two definitions and one component observation, with no rule or
unifier. It does not yet compare that whole map with the public graph or
reconstruct the native total. The [record](sigma_graph_verification.json)
pins the complete 52-input check, including inherited isolated prerequisites.
At 2 GiB it failed during imported transformation-profile allocation; the
identical snapshot passed at 3 GiB in 235.567s / 2,209,972 KiB. Available host
memory was 16,581 MiB before the explicit increase. Defaults, serial execution,
subject reduction and the per-process no-swap guard were preserved.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --record sigma_graph_verification.json --timeout-seconds 300 --memory-mib 3072
```

The next owner-position candidate connects the public graph's whole Hom to
this represented construction and checks its action directly, so the public
square shortcut cannot hide the alternative projection order. Its 300s and
450s attempts both stopped in unchanged imports before the new clause was
loaded. A dependency-minimal prefix through the graph owner omits eight
imports used by the later ordinary-category suffix. Its first 180s / 2 GiB
run also stopped in the existing graph imports. The prefix and its final
distinct-input control now pass at 300s / 2 GiB, as recorded below. This
isolates the actual construction without restricting its general
transformation input. Prefix qualification does not replace the full-module
gate or follow merely from the definition-only consumer above.

## Early-owner prefix: whole Sigma graph implementation

[`graph_sigma_body_owner.lpfragment`](graph_sigma_body_owner.lpfragment)
connects the existing public graph with the actual earlier
`comma_graph_internal_func`, fed by `tapp1_int_cart` of the original lax
carrier. The public graph head remains stable. Its whole `fapp1_func`
projection now delegates to this Sigma implementation, retaining the entire
Hom functor. One proof-time construction view relates the whole maps while
keeping the original families, base change and internal-action section as
residual obligations. This is an explicit implementation contract, not a
theorem inferred from point observations.

The [controls](native_sigma_prefix_controls.lpfragment) evaluate the Sigma
body directly, independently of the public graph's capped shortcut. Both the
original component and the original directed square are recovered. In
particular, `fapp0(fapp1_func(SigmaBody),p)` agrees with the square carrying
the original laxity cell. A different input transformation cannot replace
the selected one in the whole comparison. No new admission premise,
primitive arrow or equality-proof argument is introduced.

The [prefix verification](sigma_implementation_prefix_verification.json)
records the full patched owner before truncation, the exact retained prefix,
the eight omitted suffix imports and all run receipts. The final control
replay passes with subject reduction in **156.370s / 543,148 KiB**, under
300s / 2 GiB. All five warning fields match the completed dependency stream
before the early owner in that same run; no new warning is emitted by this
prefix. The inherited core-unit overlap boundary is unchanged.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --record sigma_implementation_prefix_verification.json --timeout-seconds 300
```

The replay validates the original full source and full patched hash before
applying the recorded prefix restriction. Its assembled result matches the
passing inputs exactly. This is **early-owner qualification only**: the
remaining full-module/reviewer interaction is still required, and the
300s/450s full-scope import timeouts remain failures. Next, compare the
original Graph(U) section with the tautological Sigma section; neither the
second inverse nor Sigma source generation is supplied by this checkpoint.

## Canonical Sigma reassembly

The [generic Sigma consumer](sigma_generation.lpfragment) defines the
tautological section `sigma_functord_sec(id_E)` and reassembles it using the
existing section total and projection base change. Its object computation
already returns the original pair. The whole identity comparison requires
the explicit structural source-generation laws in
[`sigma_generation_owner.lpfragment`](sigma_generation_owner.lpfragment).

One law handles an arbitrary family E. Its constant-family instance is
needed after Sigma(Const) normalizes to Product: the generic-only experiment
passes its whole proof but fails that specialized comparison. Both laws are
proof-time views of the same canonical reassembly. They neither rewrite its
runtime functor to identity nor identify an arbitrary section with the
tautological one; the corresponding controls pass.

The [verification](sigma_generation_verification.json) records the no-law
failure, generic-only failure and final 31.217s / 169,740 KiB pass under
180s / 2 GiB. Categories, participating rule families and term heads are
unchanged; every warning location matches after the exact 17-line insertion.
This check uses the unmodified production core plus these two source laws,
independently of the other experimental nerve prerequisites. The retained
replay reproduces the exact checked owner and consumer bytes.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --record sigma_generation_verification.json --timeout-seconds 180
```

This supplies the canonical identity target for the native-section comparison.
It does **not** identify the original Graph(U) section with that target. The
native totalization experiment must stay at the represented-comma owner to
use its protected helpers. Its first owner-local attempt exposed a raw versus
stable pullback-family comparison after fibre duality expands; a generic
bare section view also fails when the stable classifier exposes displayed
functors. The checked common context below therefore uses existing section action by a
displayed identity, formed while the families remain generic. No new family
normalization or native section-generation law has been added for that gap.

## Common whole section totalization

### Whole native post-comparison

The later [higher-component continuation](#staged-higher-component-recovery)
closes the recorded identity-filler recovery at proof time. The original
runtime failure below remains a boundary; the arbitrary-source-map extension
and whole native inverse are not thereby established.

The [new construction and verification](whisker_verification.json) computes
the native universal transformation's whole intrinsic post-cell on visible
Sigma squares. For a square with stored filler α, it uses the ordinary Hom
postcomposition telescope followed by precomposition with the source Hom
action. The [whole functor in α](whisker_functor.lpfragment) is a defined
composite of existing functors; its capped helper is its object projection.
No comparison cell or equality proof is supplied by the caller.

Two [whole proof-time comparisons](whisker_owner.lpfragment) join the mixed
postcomposition and strict-source-map presentations needed to type that
composite. They keep the existing runtime cuts and retain all maps and arrows.
A generic typed identity view of the existing raw/stable composition joins
then handles the concrete native projection images. The [native owner patch](whisker_native_owner.patch)
adds one structural computation at `fdapp1_comma_projection_transf` for the
already-declared universal transformation. This is a refinement of that
structural owner's computation, not an inverse theorem.

The integrated early-prefix check passes in **122.548s** under 180s/2 GiB,
including the retained first walking inverse, square/filler and identity
controls, and common whole-section totalization. Warning counts and rule
families match the corrected-profile baseline: 181 pattern warnings, 2,151
critical-pair warnings, no newly reported family or parser issue. The strict
LHS audit reports no unreviewed clause; this does not establish confluence or
qualify the omitted module suffix.

The [accepted observations](whisker_controls.lpfragment) recover α at the
represented identity, reject replacement by an unrelated filler, and retain
the next action as an internal morphism. The stronger assertion that its
higher component computes back to γ is **not** established: both runtime and
proof-time attempts fail. The [original failing assertion](whisker_higher_boundary.lpfragment)
is retained. A trial whole precomposition identity cut did not close that
assertion and is excluded from this candidate. Normalization locates the
remaining expression at the Cartesian inclusion and postcomposition-telescope
higher action. Do not describe the well-typed next action as a recovered γ or
as a second walking inverse.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_whisker.py
python3 emdash2/audits/native_nerve_foundations/replay_whisker.py --assemble-only
```

The replay checks the exact 39-input closure, including the prior audit
construction and its corrected Pi/Sigma profile. It changes no production
source. Whole native section reconstruction, the second inverse, full-module
qualification and inherited promotion gates remain open.

### Staged higher-component recovery

The later [general-source continuation](#general-source-higher-recovery) removes
the identity-source restriction of the selected higher-readback consumer.

The [selected continuation](higher_component_verification.json) adds a whole
comparison between evaluating the postcomposition Hom action and the existing
precomposition Hom action. An identity-input component-first comparison covers
the projection order that had erased that whole pattern. It retains both
fillers and the original higher cell. These are structural operator
comparisons, not a native inverse assumption.

The [proof module](higher_component_readback.lpfragment) first proves the
comparison while its right-hand constructor is visible. It then installs the
canonical whole first-Hom identity cut for precomposition and reuses the
already-typed proof. This ordering matters to the incomplete unification
strategy. `nerve_whisker_higher_readback` returns the original γ for the
recorded identity-filler case **as a proof-time equality**. No computation rule
directly replaces that native observation by γ, and its raw runtime equality
remains a negative control. An unrelated δ cannot replace the original γ.

The complete retained native prefix passes in **137.368s / 589,540 KiB**,
preserving the first walking inverse and common Sigma totalization. Removing
only the component-first comparison fails at the staged higher proof, as
expected. [Typed observation consumers](higher_component_instances.lpfragment)
at `Op_cat C` and `Cat_cart` pass in 40.883s / 175,384 KiB. The expanded inline
Op instance failed elaboration and remains recorded; the typed helper has the
same computed body and carries no equality argument.

The identity cut introduces **nine additional untyped critical-pair warnings**
against existing identity presentations: five change the identity's category
tag (`Op_cat`, `CoAbove2_cat`, `CoAt2_cat`, `Cat_cart`, `EqSkeleton_cat`), and
four change its constructor (`Path_cat`, `Terminal_cat`, `Product_cat`,
`Homd_coeff_cat`). Pattern warnings are unchanged and no parser issue appears.
The audit classifies these peaks but does not claim they are joined or that
the global normalizer is confluent. Broader identity-normalization and
promotion qualification remain explicit obligations.

The arbitrary strict source-map extension is still unfinished. Its attempted
prewhiskering projection rules are excluded from the selected candidate:
the consumer leaves a scalar postcomposition/precomposition comparison, while
a raw variant moves the mismatch into included telescope action. The passing
identity-filler theorem must not be reported as that general result or as the
second native inverse.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_higher.py
python3 emdash2/audits/native_nerve_foundations/replay_higher.py --mode instances
# Expected failure at the staged comparison:
python3 emdash2/audits/native_nerve_foundations/replay_higher.py --mode without-bridge
```

All modes also support `--assemble-only`, which verifies the exact recorded
source closure without another checker run. Production sources and the parked
frontend candidate are unchanged.

### General-source higher recovery

The [general-source candidate](general_source_verification.json) now proves
the higher-readback comparison for arbitrary default-strict functors F and G,
an arbitrary base arrow p, and possibly unequal filler endpoints. Its
[defined observation and proof](general_source_readback.lpfragment) reuse the
staged postcomposition unit comparison; no equality proof is an operational
input and no inverse is postulated.

Two [fixed-prewhiskering projections](general_source_prewhisker.lpfragment)
compute whole component evaluation and its component-first next action.
They fix H and preserve the original modification; they do not identify two
jointly varying lax interchange routes. The [scalar image comparison](general_source_image.lpfragment)
joins precomposition along F,p with postcomposition using F[p]. This is the
contravariant counterpart of the existing postcomposition image view, and
retains F, p and the outer arrow rather than inferring p from its image.

The [actual native instance](general_source_controls.lpfragment) uses
`cubical_src_func` and `cubical_tgt_func`, arbitrary native edges q,r and an
arbitrary arrow p:q→r. The original Γ is retained and replacement by an
unrelated Δ is rejected. The integrated prefix passes in **143.479s** under
180s/2 GiB; its warning inventory matches the higher-component parent, with
no new rule family or parser issue. The parent's nine identity-normalization
peaks remain a promotion boundary. The independently assembled no-image
control rehashes to the existing failed receipt, so it was not rerun merely
to obtain the same failure.

The whole section comparison was then rechecked on this improved candidate.
It still fails between `sigma_functord_sec(id)` and the composite mapped
identity section. The scalar retention control completed before that failed
proof and rejects a different outer arrow. The improved local action is
therefore not a whole section reconstruction or the second native inverse.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_general_source.py
python3 emdash2/audits/native_nerve_foundations/replay_general_source.py --assemble-only
```

The replay verifies the exact 42-input closure and leaves production and the
frontend unchanged. Continue at the actual whole section/totalization
constructors; do not add the desired native identity as a rule.

A [definition-only totalization alternative](section_sigma_presentation_candidate.lpfragment)
uses Sigma of the terminal-source displayed map, precomposed with the
constant-`Terminal_obj` product-unit insertion. It typechecks and matches the
existing object and arrow projections. Its [whole Hom comparison](section_sigma_hom_boundary.lpfragment)
still fails, so it is not installed as the semantics of `section_total_func`
or used to infer the native inverse. The earlier opaque `Terminal_func`
insertion failed even the object comparison. All outcomes remain in the
verification record; the actual whole constructor calculation is still open.

Current-profile continuation: [two fresh comparison attempts](current_section_review.json)
use the installed Pi/Sigma correction, so the generic section view is a typed
identity and the former extra section-identity unifier is absent. The direct
whole section equality still fails at its final reflexivity proof. A separate
attempt at the actual Sigma implementation's whole Hom functor likewise fails
to compare with identity, even with visible edge endpoints. They finish in
108.939s and 127.155s under 180s/2 GiB, with roughly 0.53 GiB peak child RSS.
These failures do not show mathematical non-equivalence and add no law. The
next review concerns the complete extracted post-comparison of the native
universal transformation, rather than reintroducing the rejected classifier
identification or inferring a whole inverse from point/square observations.

[`native_section_totalization_owner.lpfragment`](native_section_totalization_owner.lpfragment)
now places the original graph section s_U and the tautological section τ in
the same existing projection-pullback section classifier. Writing Tot_C for
its **defined** totalization context, the checked comparisons are

```text
Observe_C ∘ Realize_C ≐ Graph(U_C) ≐ Tot_C(s_U),
Tot_C(τ) ≐ id_N(C).
```

Tot_C uses section totalization, projection base change and total duality.
It is a logical context returning a whole functor, not a new primitive or
an assumed functor on arbitrary section transformations. The original U and
its whole internal action remain unchanged.

The construction is owner-local because it uses protected represented-comma
helpers. Re-expressing a raw section by a bare carrier identity failed at the
Pi/displayed-functor classifier boundary. The retained construction instead
uses existing section action by a displayed identity, formed at generic
family parameters, then specializes it. Generic totalization similarly
prevents fibre duality from expanding the concrete family too early.

One [proof-time identity view](section_identity_presentation.lpfragment) is
needed for that existing section action across already-equal family
presentations. It retains family equality and the original section as
residual obligations. Runtime owners are preserved; an arbitrary displayed
map is not made identity. No equality argument enters the operational maps.

The [retained controls](native_section_controls.lpfragment) and
[verification](native_section_verification.json) pass in **122.945s /
560,296 KiB**, under 300s / 2 GiB with subject reduction. Warning categories,
term heads and rule families are unchanged; all locations match after the
five-line core insertion. This remains an early-owner prefix qualification,
with the earlier full-suffix and core-unit gates still open.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_graph.py \
  --record native_section_verification.json --timeout-seconds 300
```

The missing comparison is **s_U ≐ τ, or a justified equality of their whole
totals**. Both a direct section proof and an independent direct functor-identity
proof were attempted and failed; their exact inputs are retained in the
verification record. These failures are not mathematical impossibility
results. The native identity remains an explicit unresolved control, not a
new law. Before adding stronger generation rules, review the universal
transformation's complete internal action and the actual Pi/Sigma constructor
laws, including their higher mapping profiles; point/square agreement cannot
replace that work.
