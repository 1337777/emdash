# Computational ownership and normalization review

Date: 2026-10-18 (UTC)
Checkpoint reviewed: `5d2618fb`
Status: source review and matched measurements complete; local consolidations recorded below, broader normalization qualification remains required before production promotion
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_normalization_review_verification.json)
Current follow-up inventory:
[migration regression ledger](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md).
It distinguishes still-open obligations from later resolutions of the dated
findings below, and tracks the terminal alternatives without claiming an
exhaustive search.

## Assessment

The user's concern is supported by the source and measurements. Passing the
current consumers establishes useful implementation feasibility. It does not
establish a satisfactory global normalization policy, termination/confluence,
or production performance. In particular, repeatedly adding comparisons for
different presentations of the same operation can become implementation debt
even when each equation has an ordinary mathematical justification.

The selected categorical design is not rejected by this review. No new
semantic obstruction was found, and no LP declaration, runtime rule,
unification rule or checker setting was changed. The review instead identifies
specific computational owners that need consolidation. It is not appropriate
to dismiss the measured cost simply because it stays inside the resource cap.

## Matched performance

Both sides use the exact pinned pre-goal source or the current emitted
migration, the same installed checker, enabled subject reduction and warnings,
source-only checking, `--record-time --too-long=0.5`, and serial resource guards.
Each row is one matched sample, not a statistical benchmark distribution.

| Corresponding target | Pre-goal wall / peak child RSS | Migrated wall / peak child RSS | Shared profile |
| --- | ---: | ---: | --- |
| `examples/image_coimage_adjunction_families.lp` | 6.792s / 495.3 MiB | 37.143s / 2462.8 MiB | 300s / 4 GiB / `o=20` |
| `emdash3_2_one_cat_homology_family_comparison.lp` | 13.413s / 754.1 MiB | 81.370s / 5518.8 MiB | 300s / 6 GiB / `o=10` |

This is approximately 5.5x and 6.1x elapsed time, and 5.0x and 7.3x peak
memory. Earlier matched core measurements at the
[hygiene checkpoint](production_hygiene_review.md) were 4.442s/326.3 MiB
versus 17.064s/1426.0 MiB. That earlier core measurement is historical and
must not be presented as a fresh measurement of the current checkpoint.

The comparisons retain the original mathematical consumer outlines and
observations, but the migration necessarily changes profiles and some
dependencies. The image/coimage closure has 17 versus 21 input files; the
homology comparison has 67 on each side. These numbers measure end-to-end
migration cost, not the isolated cost of adding a unification rule.

For image/coimage, the import commands account for approximately 6.66s and
36.84s of the respective runs. Its actual final observations are inexpensive.
The reported rewriting timer increases from 4.83s to 32.41s; the solving
timer increases from 0.49s to 1.12s. For homology the corresponding timers
are 10.09s to 74.94s and 1.00s to 2.29s. Allocation traffic also increases
substantially. These timer labels do not isolate the contribution of custom
unification: solving itself can request normalization. They do support
prioritizing expanded terms, repeated conversion and rule interactions over
an unsubstantiated claim that one particular comparison is the root cause.

The largest measured non-import command is the new
[`one_cat_oplax_exchange_at_path`](production_one_cat_oplax_exchange_paths.lpfragment),
at 12.16s. Other concrete sites include its whole exchange-map definition
(2.99s), the represented-comma target link (2.87s), and native diagram
reconstruction (4.70s). Do not sum nested import timings as independent work.
There is enough localization to start a bounded owner review without another
full repository aggregate or an increased resource ceiling.

## Inventory and its limits

The read-only [inventory helper](production_normalization_inventory.py)
examines the 151 corresponding non-example LP files in the current migration
manifest. It excludes old scratch files and standalone reviewer assertions.
It strips comments and inventories complete commands; it is not a Lambdapi
parser or a semantic/confluence checker. Its detailed output remains in the
ignored probe directory and is reproducible from the pinned authoring inputs.

| Scope | Pre-goal runtime rule commands | Migrated | Pre-goal unification commands | Migrated |
| --- | ---: | ---: | ---: | ---: |
| Core | 743 | 991 | 91 | 144 |
| All 151 corresponding files | 981 | 1292 | 172 | 250 |

There are 114 textually changed or added comparisons, including variance and
coefficient edits to existing comparisons; this is not 114 new laws. The
largest changed comparison has 1619 normalized characters. The ordinary
exchange comparison has pattern nesting depth seven. Counts and depth are
review signals, not semantic judgments or performance attribution.

The scan found no changed rule that unconditionally rewrites a primitive
head on a tuple consisting only of variables to a semantic body. That is a
bounded negative finding for the user's first warning sign, not a guarantee
that every head or alias has a good design. It found 61 changed clauses whose
RHS returns a newly declared primitive. Many are normal projection or
constructor laws. The deeper cases were inspected explicitly.

## Concrete ownership findings

1. **Several runtime presentations of composition are inherited.** The
   pre-goal core already declared `hom_precomp_along_fapp0` and
   `hom_postcomp_fapp0` as stable cut owners and compared them with raw
   composition at proof time. Their purpose includes retaining computational
   inverse cancellation. The latest
   [precomposition comparison](production_precomposition_association.lpfragment)
   expresses ordinary composition/reassociation and retains every actual
   functor. Its mathematics is not an arbitrary new axiom. Its necessity is
   nevertheless evidence that the canonical-form policy is incomplete: raw
   composition, precomposition and postcomposition can survive in equivalent
   endpoint types and demand additional pairwise bridges. The migration adds
   pressure to a pre-existing design choice.

2. **The ordinary exchange bridge is genuinely brittle.** The second
   [point comparison](production_mapping_normalization_review.md#retired-comparisons),
   present at the checkpoint reviewed here, matches
   an expanded admission/inverse/exchange/walking-arrow pipeline. It has an
   actual consumer and preserves the cross-cell, but depends closely on the
   current unfolding and association order. It should be reviewed as a
   candidate for an owner-level projection design before adding further
   contextual variants. The same exchange family contains the measured
   12.16s definition; this makes it a useful first performance target, not
   proof that this particular unifier caused that cost.

3. **Not every new stable head is an isolated workaround.** In
   [the Homd owner](production_homd_core.lpfragment),
   `fib_cov_tapp0_u_func` has the whole transport parameter, object projection,
   map projection, higher-Hom observation, and identity/composition action.
   `Homd_coeff_rep` is the object image of a whole represented-inclusion
   functor, with a semantic body for its higher action and represented
   composition rules. These are recognizable whole operations. That supports
   keeping the architecture while reviewing their expanded inclusion patterns
   and critical overlaps; it does not prove all their interactions confluent.

4. **One additional projection deserves explicit scrutiny.**
   [`sigma_const_target_func`](production_sigma_constant_projection.lpfragment)
   has runtime object computation, but its agreement with the underlying
   whole/Hom/capped Sigma projection is given partly by unification. Earlier
   eager expansions broke the generic application/composition cuts, as
   recorded in the [target review](production_comma_target_review.md).
   This is an explicit structural projection, not an unexplained supplied
   map. Still, the distinction between a neutral higher action with a
   proof-time reading and a reducing semantic projection must remain visible
   in the computational acceptance criteria. Neither typechecking nor a
   typed-reflexivity observation alone establishes the latter.

5. **Identity/duality joins reveal a repeated pattern.** Core T/R and the
   newer odd/even diagram dualities erase identity annotations before some
   generic action rules match. The latest transfor-unit repair follows that
   pattern. Further nested cases remain warning families. This calls for a
   review of the generic typed identity/projection boundary, rather than an
   indefinite list of new duality-specific joins. Do not mechanically erase
   guards: past broad replacements regressed actual consumers.

The [previous hygiene review](production_hygiene_review.md) already corrected
one noncomputing pattern on a transparent alias and retired three duplicate
strictness rules. Thus there is confirmed implementation debt as well as the
new review candidates. Some comes from the old foundation, some from the
migration's additional coefficient and duality presentations.

## Recommended next scope

Before extending either the composition or exchange comparison family,
review that family as one computational owner:

- state the intended runtime forms, the preserved inverse cuts and the
  whole/object/Hom projection routes;
- distinguish required runtime computation from readable proof-time views;
- try one local consolidation using existing semantic operations and stable
  projections, keeping types, all actual inputs and higher action;
- require the original whole consumers, inverse observations, Homd regression
  and changed-input controls, plus matched time/allocation measurements;
- replace or retire the superseded comparisons only after that slice passes.

Do not convert all comparisons to eager runtime rewrites: that can duplicate
expanded bodies, lose inverse cuts, or create cycles. Do not replace them
with supplied equality arguments or new primitive heads that merely rename
the failing terms. Likewise, proof opacity is not an automatic cure for the
cost of checking the proof's own type.

The selected strict-functor/lax-transfor and coefficient design remains in
force. No general Q theory, new foundational profile matrix, broad file split
or checker redesign is introduced by this review. Redundant strict-wrapper
retirement is already required by the migration and remains a separate
source of overlap reduction to measure.

Computational ownership and measured usability are now explicit
pre-promotion gates. Independent mechanical migration can continue, but new
case-specific bridges in the identified families should trigger this local
consolidation review. Larger alternatives may be documented and deferred;
a demonstrably broken required runtime projection cannot be deferred while
claiming that projection complete.

## Follow-through at `6d2b3771`

The matched measurements above remain measurements of `5d2618fb`, not of
every later checkpoint. On review, all four receipts, their log hashes and
their immutable input blobs were reverified, including matching checker and
resource/GC settings within each pair. No expensive rerun was needed for
this documentation review.

Two subsequent slices provide concrete guidance for this migration:

- `99eed0bb` replaces three expanded comparisons with four computations at
  existing evaluation and walking-arrow owners, without introducing a new
  primitive. The [mapping review](production_mapping_normalization_review.md)
  records the actual runtime improvement and retained higher consumers.
  Its timing measurements do **not** establish a speedup.
- `6d2b3771` rejects a broader precomposition unifier. Selecting the existing
  covariant composition accessor for a fixed-index column instead exposes
  the required endpoint computation. The [transpose review](production_native_transpose_review.md)
  records why the broader comparison was insufficient and was removed.

Consequently, investigate the declared endpoint forms and the existing
projection routes before adding another equation between surviving stable
heads. A stable head is useful when its eliminations retain the operation's
whole and higher action or its inverse cuts. A head that only names an
expanded term, or a typed-reflexivity view that substitutes for required
runtime action, needs correction or an explicitly incomplete contract.
The primitive-expansion scan above is only a syntactic filter; it does not
settle that distinction for every declaration.

The remaining priority is local consolidation of composition presentations,
the Sigma constant-target higher projection contract, and identity/duality
joins. Retain proof-time associativity and genuine presentation comparisons
where intended; do not equate a smaller unifier count with a normalization
theorem. For any selected correction, compare the same whole consumer and
input closure, record allocation and peak memory as well as time, and avoid
combining that correction with an optional foundational redesign. The staged
Homd computations support feasibility, but production computational usability
and a satisfactory normalization policy remain unqualified.

## Batch-checker memory diagnosis after `4abd18cb`

The unchanged original central import order exposed a practical blocker:
the migrated diagnostic exhausted 8 GiB during commutative-algebra presheaf
imports, before its assertions. Both o=10 and o=5 failed. The matched
pre-migration source passed. The
[runtime evidence](production_checker_memory_verification.json) retains the
source snapshots, checker identities, resource settings and failed runs.

Inspection used the installed checker's exact source pin,
`db4f7809961b8c107247613067fb567491fb0b84`, and its Timed 1.1 dependency:

- `src/cli/config.ml` saves the initial Pure rollback state;
- `src/cli/lambdapi.ml:check_cmd` saves another state for restoring between
  input files, even for a single input;
- `src/core/eval.ml:to_tref` creates mutable normalization references; and
- Timed records reference updates while an accessible rollback point exists.
  Its journal can therefore retain otherwise transient evaluation objects.

The isolated [patch](production_checker_batch_snapshot.patch) releases the
unused initial Pure snapshot and skips the outer inter-file snapshot only
for a single-file batch check. It preserves the initial snapshot behavior
for interactive use and the inter-file restore branch for multiple inputs.
Internal tactic/backtracking snapshots remain. It changes no parser,
inference, conversion, rewriting, unification or subject-reduction code.
The installed binary and repository toolchain pin have not been changed.

| Exact original central source; same 600s/8GiB/o=5 settings | Wall | Peak child RSS |
| --- | ---: | ---: |
| Installed checker | 148.446s | 4627.1 MiB |
| Isolated single-file snapshot experiment | 133.937s | 518.9 MiB |

Both runs pass the same 2133 positive and 299 negative assertions and have
identical input hashes and all 1372 warning bodies. An independent invalid
rewrite is rejected by subject reduction with the isolated binary. These
are single samples, not a statistical speed benchmark. The snapshot change
strongly implicates retained rollback history in the large memory footprint;
it does not excuse expensive normalization or establish a clean rule design.

On the unchanged migrated source, the isolated checker proceeds beyond the
old allocation boundary and reaches a genuine coefficient mismatch in
`emdash3_2_walking_end_hit.lp`, in 278.830s at 1274.4 MiB peak RSS. This is a
failed diagnostic locating the next owner, not a passed central gate. The
installed checker separately reproduces the owner migration failures, so
formal corrections need not depend on adopting this experimental binary.

The experiment was built in an ignored checkout of the exact pin with
`dune build --profile release -j 1 src/cli/lambdapi.exe`, under the ordinary
300s/4GiB build guard. Replay by checking out the exact source pin and applying
the zero-context patch with `git apply --unidiff-zero`, then selecting only
that isolated binary for `scripts/run_lambdapi.py`.
Keep source-only checking, subject reduction, warnings and all resource
guards. Do not replace the installed executable or silently reinterpret old
receipts as results of the new checker. A toolchain change still needs its
own review, including the multiple-input and interactive-state boundary.

An additional paired control checks the migrated WalkingEnd owner and its
original reviewers before duplicate-rule retirement: both binaries pass all
64 positive/ten negative observations with identical source/settings and
2453 warning bodies. Peak child RSS is 2307.8 MiB versus 173.9 MiB, while
elapsed time is 31.943s versus 31.360s. The subsequent formal checkpoint is
validated independently by the installed checker. These results reinforce
the distinction between retained heap and normalization work.

The computational-owner review above remains required. In particular,
`Psh_pullback_func` and some simple whole composition observations still
take seconds in this import context. Reduced retained heap is not evidence
that those comparison/normalization costs have been resolved.

## Sheafification final-assembly follow-through, 2026-10-18

The [sheafification review](production_sheafification_review.md) supplies another
concrete case of local presentation cost. The coefficient-corrected whole
construction passed through its pointwise counit equivalence, then exhausted
4 and 6 GiB at final reflector assembly. The isolated checker snapshot patch
did not remove this failure. A conversion trace showed repeated expansion of
large locality-proof fields across rigid/generic endpoint presentations.

Reusing the existing generic package projections at the existing counit and
reflected-object accessors repairs that comparison. The full original reviewer
passes with the installed checker in 38.492s/2993.2MiB at 4GiB, with no new
primitive or rewrite/unification rule and no change to chosen inverse data.
The final assembly reports 0.00s. Warning bodies are unchanged by this fix.
The matched pre-goal run is still cheaper at 14.319s/1077.8MiB; this is a local
repair, not a general performance qualification. Exact receipts and discarded
variants are in the linked verification. Preserve this distinction from the
separate checker-state retention issue.

## Capped-action result and slice endpoint follow-through, 2026-10-18

The [final-import review](production_final_imports_review.md) records an
inference/normalization issue rather than another missing comparison equation.
After correcting the slice family's higher variance, readable Hom aliases
could be inverted before the opposite-Hom computation. Owner-position SR and
runtime observations exposed spurious endpoint constraints and a mate identity
that lost its independent endpoint. Canonical Hom types at the affected
rectangle/mate declarations, together with a canonical result type for the
existing generic capped functor action, restore the original observations.

The generic input stays Hom(A,x,y): canonicalizing that too erased information
needed to infer a dual domain in an existing arrow-diagram consumer. The final
result-only change passes the complete core/Homd, combined library and larger
native-universality regressions. Removing the local canonical types failed SR;
that attempted simplification is not retained.

No core rule text or rule count changes in this step. The changed type affects
elaborated overlap presentations: 34 newly printed and 457 removed bodies,
with 24 added Core-inclusion-composition overlaps, six product-projection
identity overlaps and four path-record symmetry/reflexivity overlaps. The
verification preserves their exact rule identities and log hashes. The
redundant named strict-instance family belongs to the already required
retirement review; counts are not a proof of confluence or a performance result.

## Central diagnostic owner review after `294b5b69`

Date: 2026-10-19 UTC. [Exact evidence](production_central_owners_verification.json).
This is a bounded migration checkpoint, not completion of the central suite.

The original early central diagnostics and ordinary Hom/action section now
check under the selected coefficients. Raw Cat-valued diagrams remain raw:
their objects use fapp0 rather than the stronger Catd/Fibre facade. Admitted
families use Cat_cart. Canonical Hom packages use their Cartesian mapping
categories; their ambient observers use the existing strict_transfor view.
Whole parameterized composition roots have Cartesian parameter classifiers,
whereas the fixed pre/postwhiskering maps still accept ambient lax transfors.
The tests now state that distinction rather than silently equating the two
mapping categories. No new strict-naturality rule is introduced.

The next failure supplied a concrete instance of the user's normalization
concern. Before migration there were two component clauses: one for the raw
capped telescope action, one for its ordinary transfor view. Redirecting their
observations to the same ambient head retained both clauses with different
runtime results, stable precomposition versus product composition. The
original central assertion of the ordinary-view computation then failed.

The repair keeps the original ordinary-view comp_prod computation once, at
the earlier component owner, and removes its later duplicate. The existing
precomposition theorem retains its statement but uses symmetry of the already
defined hom_precomp_along_fapp1_comp_prod_path. Reusing a direct eq_refl at
that site left unresolved implicit product classifiers; the explicit existing
theorem avoids that inference problem. No operational symbol receives a path.
The separate Hom_tele_func factorization comparison also needed the same
Cart classifier correction as its whole owner. It is an edit to the original
comparison, not another equation alongside it.

Core symbol declarations stay at 897, runtime rule commands decrease from
991 to 990, and unification commands stay at 144. These lexical counts exclude
comments; they are an inventory, not a normalization proof. The LHS audit
reports zero unreviewed candidates, and the edited custom Hom comparison
retains all endpoints and both actual represented actions.

The installed checker passes the 823 positive/161 negative assertions of the
two original central sections, plus the fresh core/Homd 287/85 regression.
The entire central file still retains 2133 positives, 299 negatives and its
66 original declarations. No assertion is deleted or has its polarity flipped;
the changed classifier restrictions are identified above. The larger action
driver still fails in its following displayed
family comparison, where an old Cat_cat annotation conflicts with Cat_cart.
The exact previously adapted locality/presheaf/sieve sections are also copied
into the full central file, but that file is not yet qualified end to end.

One matched sample of these central sections takes 9.541s/489.3MiB before the
goal and 37.207s/2069.5MiB after migration, under identical installed-checker,
SR/warnings, 180s/4GiB and o=20 settings. The fresh core takes
29.720s/1591.5MiB. The component correction restores a required computation;
it does not establish a performance improvement. Broader measurements at the
preceding checkpoint remain historical after this core change.

Core critical-pair bodies remain at 1564. Five bodies are replaced at exactly
the same overlap sources: two product component projections and three
intrinsic-action/strict-inclusion observations. Their normalized branch now
uses the selected product-composition component. Exact body hashes and both
logs are retained; general symbolic joins are not claimed. These overlap
families, redundant strict instances and overall normalization cost remain
pre-promotion review work.

Next continue the original displayed-family/product observations and the
remaining central diagnostics. Do not change ambient lax FF to strict merely
to make these observations pass. Wrapper retirement, remaining registered
consumers and final production/catalogue/health/CI/source-pin gates remain
required, with the separate application goal still paused.

## Cartesian product-profile repair after `1f8ffe50`

The original product-pair telescope exposed an inconsistency between two
existing classifier computations. Functor_cart_cat(X,A*B) splits into a
product, so its Hom object classifier becomes a pair of strict-transfor
carriers. The independent StrictTransfor(X,A*B,F,G) carrier remained opaque.
Neither implicit nor fully explicit inclusion parameters joined those types.
This was a missing structural computation, not a reason to add a bespoke
comparison for Product_pair_tele_func.

The [repair](production_cartesian_product_views.lpfragment) adds the matching
product rule to the strict-transfor carrier and computes both product
components of its ordinary inclusion. The whole inclusion head stays visible
for existing strict-naturality rules; it does not expand a neutral input into
a pair. Product is the actual runtime discriminator, with source and endpoint
slots inferred. The classifier-former rule keeps the source and endpoints
needed to form its actual component types. There is no new primitive, unifier
or operational proof argument.

The rules must follow the ordinary Transf_cat product projection. Installing
them earlier failed subject reduction before the output product was available.
A constructor-only pair beta passed the first consumer but introduced a
whole strict-naturality overlap by erasing the head that selects that law.
It was not retained. The selected projections pass the original telescope,
neutral-input whole-inclusion observations, a whole strict-naturality
observation and a negative rejecting admission of a general lax transformation
to the strict product carrier. The [controls](production_cartesian_product_controls.lpfragment)
retain the actual functor inputs and both component transformations.

The same tranche migrates the original general-epsilon Homd projection
diagnostics through the corrected root, Q modification, Cartesian v component
and reversed P-index evaluation. All original identity/filler observations
remain, with no Op_funcd applied to a raw FF. This is further consumer
qualification of the implemented ladder, not a new Homd construction.

[Exact evidence](production_central_intrinsic_product_verification.json)
records fresh installed-checker passes for all migrated central sections,
core/Homd and the combined library closure. The library remains expensive:
93.097 seconds and 4407.8MiB in this sample. No performance improvement is
claimed. All checks retain subject reduction and explicit resource bounds.

Core warning bodies increase from 1564 to 1570. The six new symbolic peaks
are the two projections against included Cartesian composition and against
the canonical pre/post Hom-telescope inclusions. Their hashes and source logs
are retained. The concrete projection, inclusion and naturality consumers
pass; complete symbolic joins remain a normalization-review obligation.
The constructor-only variant's whole-naturality peak is absent from the
selected source. No broad eta or new case-specific unification bridge is added.

## PathOut motive consumers after `81e68dee`

This tranche returns to a later block of the original diagnostics, not to
the PathOut construction itself. The earlier source migration and
PathInd/transitivity checks remain. The new block observes the moving motive
classifier, reindexing, reflexive evaluation, Pi and covariance. Its old
Cat_cat annotations were incompatible with the already selected Cat_cart
coefficient; moving motive maps use Cartesian Homs, while fixed-source
evaluation and Pi still accept ordinary lax maps through their existing
inclusion.

After those type corrections, the original moving-motive fibre computation
still failed. A normal-form trace identified
hom_precomp_along_fapp0 with a Cat_cart coefficient under fapp0. The existing
precomposition evaluator had object, whole-Hom and capped projections for
Cat_cat only. The correction instantiates that same ladder at Cat_cart,
at the same owner. It adds three runtime rules and no unifier or primitive.
It does not unfold the whole stable Hom head or fold a large expression
into an ad hoc PathOut helper. Outer inferred evaluator arguments remain
underscores; the original actual family, arrow and postfunctor are retained.

The pre-goal varying-base Catd fold exposed the raw pullback functor directly.
That whole fold cannot be copied to the corrected Cartesian parameter
category: it would identify its strict maps with the larger lax-map category.
The two whole family presentations therefore use the existing proof-time
comparison. The diagnostic now checks it by typed reflexivity and separately
rejects runtime conversion. This is an explicit change to that observation,
not a claim that its former runtime equation was preserved. Object transport,
whole Hom action and capped arrow action still compute to the original
pullback observations. The large existing Sigma-composition expression and
its identity-fibre proof are retained unchanged.

The [verification](production_central_pathout_motives_verification.json)
records all 36 original assertions plus two higher-action comparisons and
one stable-head boundary. Fresh installed-checker core/Homd, merged central
and library checks pass, with exact input hashes, SR and resource containment.
The library still uses about 4.3GiB; differing single-run times are not evidence
of a normalization improvement. The LHS scan reports no unreviewed candidates,
and the actual core diff is only the coefficient evaluator instance.

Warnings grow from 1570 to 1572. The two added bodies are byte-for-byte the
existing Cat_cat product-projection/evaluator bodies after substituting
Cat_cart. Their exact bodies and hashes are recorded. These are reviewed
symbolic overlaps, not newly proved joins. They remain in the required
normalization work with the six earlier product-profile peaks; no additional
commuting conversion or comparison rule is installed to hide them.

## Displayed component observations after `4b3bce9e`

The original component-action diagnostics now use the actual Cartesian fibre
Homs and ordinary inclusions of their strict-transfor components. General
displayed maps/modifications still retain their base laxness. The standalone
edge/presheaf classifiers have shifted bases, while the corrected Homd target
is the actual Q-diagram transformation category and its transposed family
fibre. These are changes to the observations, not new mathematical owners.

Three original runtime negatives combine an arbitrary conventional-lax
transfor with the canonical displayed component evaluator. The generic
pre/right composition rule expects fapp1(tapp0_func); component projection
first changes that argument to tdapp0_fapp0. Its identity specialization has
the same issue. The ordinary and product-valued examples therefore remain
runtime nonconversion controls, although the selected leg is mathematically
strict. Their comments now make this distinction explicit. The two identity
examples also need canonical composition categories/endpoints: without those
annotations, the changed strict-transfor carrier prevents type inference and
would not provide a legitimate negative conversion test.

Two attempted direct repairs to the diagnostic proof were not retained.
Plain typed reflexivity failed to join the specialized scalar expressions.
Applying the existing whole pre/right functor equation reaches the expected
represented-precomposition endpoints, but the checker still does not join
their specialized raw-composition presentations automatically. Neither
failure licenses a new semantic strictness restriction or demonstrates an
invalid conventional-lax law.

The existing precomposition_point_path in
emdash3_2_direct_cover_completion_retained_sections.lp stages precisely the
generic precomposition reading before specialization. Its reuse and owner
placement are available options for the normalization review; this tranche
does not introduce another theorem, proof payload or case-specific unifier.
The raw projection-order boundary remains recorded rather than being hidden
by an additional rule or described as semantic non-naturality.

The ordinary transport comparison observations use the already implemented
rhs/pre-right owners. One old pointwise rhs nonconversion becomes a positive;
the actual post/left laxness and the separate whole-head runtime distinctions
remain negative. The original Sigma-composition expression is unchanged.

[Exact evidence](production_central_homd_classifiers_verification.json)
records the failed candidates, the final well-typed controls, and fresh
classifier/component and merged-central checks. Mathematical inputs and
warning bodies are unchanged, so the preceding exact core/Homd and library
receipts carry. The specialized comparison/normalization work remains part
of the pre-promotion review, alongside the earlier product peaks and resource
cost; this is not a new confluence claim.

## Public Homd terminal boundary after `104c91a2`

The public ladder uses E as its source and the transposed whole Q-section
category as its target fibre. Its y projection is a Q-valued transformation
component. At v it gives an object of Homd_index_cat(I); the existing
homd_index_presheaf exposes the complete functor T(I) -> Cat_cart. Fourteen
general/root/component/section observations pass, including two whole
relative-composition observations for an arbitrary lax section parameter.
No enlarged base, new curry operation or equality-proof payload is involved.

Five old whole terminal-source shortcuts are still unqualified. These are
not the pointwise fact Hom_1(u,v)=1, which already computes. The source-u
whole functor retains a mate/covariance composite, the identity terminal
y-component retains a conjoint, and a general section parameter retains
composition with its actual fibre functor. The full diagnostic source keeps
the original positive obligations at their corrected types. A separately
named passing driver contains only the fourteen qualified observations;
the five obligations remain outside that driver and inside the full gate.

The owner-position experiments have these outcomes:

- A direct terminal-source rule at fib_cov_src_func passes formation but
  breaks its neutral-unit projection. Covariance still carries the supplied
  unit object; it cannot simply choose Terminal_obj before Hom forgets it.
- A canonical terminal-map/covariance variant fails subject reduction at
  the higher covariance projection. Its endpoint obligations would identify
  arbitrary unit variables with Terminal_obj. It is not adopted.
- A mate-only variant introduces a terminal mate and unfolds terminal
  conjoints. It passes neutral-input observations, its seventeen adjusted
  ladder observations and the existing core/Homd suite. In that experiment,
  two general-section constant expectations were replaced by their actual
  composites; the pass does not establish all five original shortcuts.
- The mate-only variant fails the independent right-unit consumer after its
  unit has normalized to the constant-functor presentation. The unit itself
  converts to that value, but composition with that value no longer selects
  the existing unit reduction. Fourteen new symbolic warning bodies include
  the erased-unit cases. The unchanged source's native unit presentation
  passes both unit cuts. The experimental normalizers are not adopted.

[The verification](production_public_homd_verification.json) retains exact
source snapshots, receipts and the first outstanding assertion. This is
evidence of a computational owner/normal-form issue; it does not establish
that the selected general Homd interface is mathematically impossible.
The passing generic suite was insufficient to qualify the new terminal
normalizer, so an actual unit consumer took precedence.

The next repair must preserve the whole Q-unit representation and the actual
relative-map input. Prefer the existing native projection owners and their
whole semantic comparisons to an eager unfolding of a represented morphism.
The distinction between the identity core's normalization and composition
with a general lax FF must remain explicit. No candidate here authorizes a
blanket terminal-source eta rule, stronger default naturality, new caller
proof arguments or a general profunctor-composition development.

All mathematical sources, the core warning bodies and the earlier exact
core/Homd/library closures remain unchanged in the selected source. The
public terminal-source obligations, full central gate and production
promotion remain incomplete.

## Terminal alternatives and consolidated follow-up after `708bb2de`

The rejected terminal-mate experiment does not exhaust the available designs.
The [consolidated ledger](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
now separates the five assertions into the identity source-u map, the terminal
identity y-component and the two general-section components. It also tracks
other normalization/projection boundaries, wrappers, performance, original
consumer coverage and promotion. Required corrections are distinguished from
optional redesign and from historical failures resolved by later checkpoints.

A smaller new experiment restricts conjoint normalization to an explicitly
constant transport:

```text
Conjoint(1,I,Const(I,1,u)) → Const(1,P(I),terminal-presheaf).
```

There is one runtime rule and no new primitive or unifier. Unlike the rejected
unrestricted rule, it does not unfold `Conjoint(1,1,id_1)`. The original whole
terminal identity y-component and both native Q-unit cuts pass. A typed
nonterminal control rejects extending this simplification to an arbitrary
target category. The same experiment also verifies formation of the two
represented-inclusion views.

The remaining interaction is concrete: normalizing the constant conjoint
first prevents the existing conjoint-composition rule from matching. The
whole composition assertion fails. The two new warning bodies, 1572 to 1574,
are exactly the two orientations of this overlap. This candidate is not
adopted; passing the terminal component and units is insufficient. The
[alternative evidence](production_terminal_alternatives_verification.json)
records the actual rule, complete controls, successful and failed receipts,
development-test corrections, source pins and warning bodies.

The whole represented-inclusion observation separately fails runtime equality
in the unchanged staging source: one route gives raw composition, the other
`Homd_coeff_rep`. Its existing proof-time comparison passes. This is the
already intended stable-head/body distinction, not a new semantic failure.
It reinforces the need to specify which observations are runtime reductions
and which are whole comparison views.

Prefer preserving represented heads while reviewing their existing projection
and comparison owners. A normalized-unit repair remains an unqualified
alternative, but fixing only the unit would not address the composition
overlap found here. No impossibility claim, global terminal eta, stronger FF
profile, operational proof payload or general profunctor theory follows.
The five original terminal obligations remain required. Production and
selected mathematical authoring sources are unchanged.

## Whole terminal views retaining the runtime heads after `f8755cda`

The next experiment keeps all runtime heads and cuts. It adds two whole
proof-time comparisons at their existing semantic owners:

```text
F : B → C, G : 1 → B
F ∘ G ≐ const₁(F[G[*]])

F : I → 1
Conjoint(1,I,F) ≐ const₁(terminal presheaf on I).
```

The first is the terminal-source composite law for the restored strict
functors. The second uses terminal Hom, whose value is 1 regardless of its
endpoints. These are structural proof-time laws, not newly supplied data or
theorems claimed to follow by the previous beta rules alone. The actual
functors survive in the first rule's selected point. Neither rule changes
unit objects, arbitrary FF naturality, or the runtime conjoint/unit forms.

Both sides use existing rigid heads. The first lives with ordinary constant
functors and is exercised independently of Homd. The second lives beside the
conjoint's existing whole body comparison. This avoids matching expanded
mate/covariance expressions or adding a terminal-mate primitive. The inferred
indices on the ordinary comparison are explicitly justified by its typed
point action; the custom conjoint pattern is reviewed separately from the
generic LHS audit.

All five whole public terminal expressions now pass typed reflexivity
observations. The independent Q-unit and conjoint-composition consumers still
reduce; the rejected eager rules failed those consumers. Negative controls
reject changing the point and applying the terminal-source law to an arbitrary
source. Separate runtime negatives confirm that the new comparisons do not
erase the stable heads. Baseline omission controls fail at the intended
whole comparisons. Exact evidence is in the
[tranche verification](production_terminal_homd_views_verification.json).

The five old runtime assertions remain required, unchanged and unqualified.
The new whole comparisons are kept in a separately named reviewer; they do
not replace those assertions in the full diagnostic. Remaining work must
settle the runtime presentation and required higher projections explicitly.
This tranche does not claim full terminal normalization, global confluence,
performance improvement or production promotion.

Fresh installed-checker passes cover core/Homd 287/85, the qualified central
subset 1336/210 and library closure 178/27. Warning-body multisets are unchanged
at 1572, 1786 and 2412 respectively. The core diff adds only the two comparison
rules and comments; no declaration or runtime cut changes. The source audit
has no unreviewed slots, with manual review of both comparison patterns.
The largest of these runs uses 4409.0MiB under the existing 6-GiB library
profile; this remains a usability concern, not a measured improvement.
Broader receipts are historical after the shared core change unless separately
refreshed. The original full central source still retains its five runtime
terminal obligations and all subsequent diagnostics.

## Original Homd and displayed-Hom diagnostics after `2d55c39a`

The next original blocks now observe the actual P(I) object/presheaf view,
Q-valued section modification, Cartesian component and reversed index
evaluation. Their general FF is unchanged. The intrinsic root's explicit
endpoint annotation must use its computed Homd_target_index_func family;
substituting the alternative expanded Homd_target_catd presentation obstructed
inference. The native annotation passes without changing an owner or equation.

One old negative asserted that the constant-family extracted cell would not
compute to the ordinary arrow. The existing whole constant-index constructor
already makes it compute to F[p]. The migrated observation is positive and
the retained theorem still checks. An arbitrary-loop negative checks that
the actual F[p] is not replaced by identity. No new strictness for general FF
is inferred from that ordinary-functor specialization.

The displayed Hom observations use the actual negative section in O(E) over
R(K), together with Cat_cart coefficients. The inline Unit_prof comparison
keeps its original formula, filler and strict positive section. Both the old
two-identity inference form and direct typed reflexivity after specializing
the strict view failed. The generic comparison with an arbitrary section
passes at the already installed semantic owner. A local proof of that generic
equality, then applied to the original strict section and filler, passes.

This is a diagnostic proof using the existing comparison, not an extra path
argument or cast in Hom_catd, Homd or any library operation. It adds no kernel
unifier or global declaration. It gives another concrete example of checking
a whole generic comparison before projection/profile specialization. It does
not prove that every earlier projected pre/right comparison is resolved.

[Exact evidence](production_central_homd_homcatd_verification.json) retains the
failed candidates, successful generic/specialized checks and final combined
1386/215 pass. The two new blocks contain 38/4 and 12/1 observations. Core
and library input hashes are unchanged and reverified; their existing passes
carry. Combined warning bodies remain 1786. The full source retains its 66
global declarations, all subsequent diagnostics and the five unqualified
terminal runtime assertions. This tranche introduces no mathematical source
or default-profile change and does not establish production qualification.
