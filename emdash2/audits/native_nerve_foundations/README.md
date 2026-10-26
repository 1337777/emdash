# Native nerve adaptation: receiver evidence

Status: non-library NF-1 candidate on the corrected foundations.
Owner: [adaptation plan](../../../docs/EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md).
Receiver baseline: `e8ffc4d0`; legacy donor: `280e7a03`.

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
