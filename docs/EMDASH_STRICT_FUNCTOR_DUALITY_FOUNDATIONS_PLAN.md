# Corrected foundations and native nerve continuation

Date: 2026-10-27
Plan-ID: STRICT-FUNCTOR-DUALITY-FOUNDATIONS-V3.2
Status: active consolidated goal; foundations installed, original frontend and local book/article revisions accepted; native NF-1/NF-2C construction active; later integration gates remain open
Depends-On: active v3.2 source, root/nested AGENTS, source-pinned qualification
Supersedes: accumulated execution narrative, not its evidence or required outcomes; earlier default-lax and unshifted-duality contracts
Side-Task-Ledger: [current obligations and dispositions](EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
Infinity-Codex-Origin: session `01a12a87-a47e-73f1-9351-1159597be30d`
Infinity-Codex-Decision-Responses: prior-thread 0099/0105 design and launch decisions retained in the historical plan; later explicit user directions and accepted terminal contract recorded below

## Current execution contract

Follow the [implementation outline](EMDASH_NATIVE_NERVE_IMPLEMENTATION_OUTLINE.md)
for the user-requested broader construction pass. The whole Nat-recursive
iterated-walking cube maps and concrete degree-two tensor consumer now check.
The composition comparison and first whole round trip are derived at every
dimension. The [structural postcomposition candidate and derived forward geometric decoder](../emdash2/audits/native_nerve_foundations/postcomposition_review.md)
now check at every positive dimension, with both iteration-shift inverses.
The 54-input scope passes in 97.488s / 595,020 KiB at 180s / 2 GiB.
Next construct the reverse geometric closure/encoder and their consumers,
while retaining whole-section reconstruction and the native reverse inverse
as required proof obligations. Raw nested higher projection and Cat_cart
specialization limits remain documented promotion obligations; they must not
become the sole next task. The new whole postcomposition is structural;
no missing inverse or closure equivalence is supplied by the recursion.
All inverse laws, same-index action and degeneracies remain required.

The [actual moving-cell/map experiment](../emdash2/audits/native_nerve_foundations/actual_action_pending/README.md)
has positive focused evidence, but its constant-family overlap and final
integration are unfinished. Its candidate is preserved separately; the checked
broader construction uses qualified `85b30c5e`.
Do not let this individual overlap become the sole next task. The standing
reference refresh and plan consolidation remain complete.

Do not restart completed book/article work, the original frontend migration,
or strict-versus-lax design brainstorming. The later Pi/Sigma frontend repair
and production-health/final-integration gates remain required, but are not
prerequisites of this native construction. A new source change must still
update its affected consumers and documentation at its own boundary.

This plan is the current resumption contract. The [complete previous plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN_HISTORY_THROUGH_2026-10-27.md)
and [previous ledger](EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER_HISTORY_THROUGH_2026-10-27.md)
preserve every earlier decision and receipt link. Their dated instructions
are history. Do not prepend successive full status narratives here; update
these current sections and keep experiment detail at the owning audit.

## Pins and active workspace

- Worktree: `/home/user1/emdash1-strict-functor-duality-v1`.
- Branch: `goal/strict-functor-duality-v3.2`.
- Original main baseline: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`.
- Previous mathematical audit checkpoint: `84f0539e`; current selected
  [moving-boundary candidate](../emdash2/audits/native_nerve_foundations/moving_verification.json).
- Standing-reference update: `f74e14f6`; plan consolidation: `fba40ae2`.
- Installed core SHA-256:
  `fe85009da18343b8e5a0d70f7661a385af5b8f66cbdfb8d6d453a2cf59bee21e`.
- Supported batch checker SHA-256:
  `94dc55766ec793e137cba7936f40e56074f4d92a02259cae8de9474c65e4677f`;
  [build/qualification](../emdash2/audits/strict-default-action-boundary/foundation_supported_checker_review.md).
- Legacy donor: `/home/user1/emdash1-native-nerves-legacy-v1`,
  `goal/native-nerve-legacy-completion-v3.2`, pinned `280e7a03`.
  Its separate thread remains paused; receiver adaptation is authorized here.

Inspect current Git state and baseline ancestry on continuation. The baseline
is comparison evidence, never permission to reset the descendant worktree.
Preserve unrelated health-report changes and historical untracked audit files.
The selected native audit below is non-library source, not production.

## Installed contracts

The [Foundations](../emdash2/reports/EMDASH_FOUNDATIONS.md),
[current architecture](../emdash2/reports/REPORT_EMDASH_V3_2_CURRENT_STATUS_AND_SOP_2026-05-26.md)
and [canonical syntax](../emdash2/reports/REPORT_EMDASH_V3_2_CANONICAL_SURFACE_SYNTAX_2026-06-05.md)
now describe these contracts in place. Active declarations/rules outrank
surviving old source comments and archived designs.

### Public defaults and removal of redundant strict wrappers

Public `Functor` and `fapp*` are strict. Ordinary `Transf` is conventional lax:
the pre/right leg is strict; the post/left comparison may be noninvertible.
`Hom_cat Cat_cat A B = Functor_cat A B`. Do not replace the public Hom by Cart
or impose strictness on every Cat-valued transformation.

The separate coefficient `Cat_cart` has `Functor_cart_cat` Homs. Both admitted
families E and ordinary represented Hom use `K → Cat_cart`. Their transports
and coefficient-level higher maps have the Cartesian profile. `Functord`
remains lax across the base; its fibre functors are strict. `Transfd` has the
declared strict fibre components. `StrictTransfor`/`StrictFunctord` remain real
refinements. The redundant `StrictFunctor` admission/view grammar is retired;
`IsStrictFunctor` is descriptive evidence, not a second functor carrier.

### Duality and whole dependent Hom

Use T=`Op_cat` (dimension 1), R=`CoAbove2_cat` (dimensions ≥2),
O=`TotalOp_cat` (all positive dimensions), C₂=`CoAt2_cat` (dimension 2).
`Op_catd(E)` is over C₂(K); `TotalOp_catd(E)` is over R(K).
Cartesian diagram-map restrictions on fibre duality are part of their types;
do not silently apply `Op_funcd` to arbitrary base-lax FF.

The selected coefficient and direct ladder are:

```text
P(I) = T(Functor_cat(I,T(Cat_cart)))
Hom_Q(A,B) = Cart(A,P(B))
S_E(x) = Transf_(K,Q)(iota(E),iota(Hom_K(x,−)))
H_E[x] = T(S_E(x))

homd_id_int(E) : Hom_(Cart(K,Cat_cart))(E,H_E)
homd_id_src_func(E,x) : T(E[x]) → S_E(x)
homd_id_src_sec(E,x,u) : Obj(S_E(x))
homd_id_tgt_func(E,x,u,y) : E[y] → P(Hom_K(x,y))
homd_id_(E,x,u,y,v) : T(Hom_K(x,y)) → Cat_cart.
```

The canonical identity root is strict without a caller proof. General
FF:D⇒E enters the **defined** relative composite, retaining its lax base
comparison and public blended names. Its fixed endpoint is
`Hom_(E[y])(E[f](u),FF[y](v))`. Ordinary `hom_int(F)` retains its primitive
strict-F parameter. No enlarged `(y,v,f)` base or final curry defines the
Homd telescope. Q uses only the structural represented/unit operations its
actual consumers need; a full profunctor/coend theory is not a prerequisite.

The whole Sigma–Hom is the negative-index total
`O(Sigma_(O(I))(TotalOp_catd(H)))`, where I=Hom_K(x,y) and
H=homd_(id_E,x,u,y,v). Its arrow objects remain `(f,alpha:E[f](u)→v)`.
Pi remains the ordinary transformation-backed section category.

The [Pi/Sigma correction](EMDASH_SIGMA_SECTION_PROFILE_CORRECTION_PLAN.md)
retains explicit forward `sigma_functord_sec_func`; it removes the unrestricted
whole-category, carrier and next-Hom identifications with displayed functors.
Do not restore those folds to close a native inverse.

## Completed stages and exact boundaries

| Stage | Accepted evidence | Qualification limit |
| --- | --- | --- |
| Foundations source migration | `57e627b9`: 648 changed and 740 unchanged original registered LP files; all 791 owners and 596 reviewers covered; central 2,441 assertions pass. [Promotion](../emdash2/audits/strict-default-action-boundary/foundation_production_promotion_review.md). | Source qualification at that snapshot; not final health/CI or later native promotion. |
| Terminal Homd contract | Five whole proof-time comparisons adopted and checked in the complete central diagnostics. | Literal constant runtime forms are not required; runtime leaf, higher and inverse controls remain. |
| Original TypeScript migration | `f0e22340`: 1,837 pass / 2 fail / 63 skip aggregate, followed by test-only corrections and 13 pass / 1 optional skip in owning scopes. | User waived an immediate aggregate repeat. The failed aggregate is not called green, and future substantive changes still need their gates. |
| Book and overview | `1fe72617` completed the comprehensive local revision; later correction yields book 0.10.2-dev / overview 0.4.2-dev. [Review/artifacts](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md). | Local drafts, no publication. New mathematical results must update their claims later. |
| Native adaptation start | `e8ffc4d0`, donor inventory and receiver NF plan. | Donor audit evidence is not receiver qualification or production code. |
| Pi/Sigma native correction | `bc37e5fc`: four native files installed, core/focused gates fresh, complete central/groupoidal source inputs rehashed. [Record](../emdash2/audits/pi_sigma_section_profile/integration.json). | This later correction creates new frontend adaptation; it does not undo original frontend acceptance. |
| Native NF-1 progress | First inverse; higher original-filler recovery; whole totalization; graph factorization; represented transport and Sigma inclusion, through `84f0539e`. | Isolated early-owner prefix, not whole second inverse or production/full-module qualification. |
| Standing references | `f74e14f6`, [substantive refresh](EMDASH_FOUNDATIONS_REFERENCE_REFRESH_REVIEW.md). | Documentation only; source pins and PDFs unchanged. |

### Terminal Homd acceptance decision — 2026-10-25

The user chose whole comparisons for original public assertions 8, 9, 13, 14,
and 15. The [adoption review](../emdash2/audits/strict-default-action-boundary/foundation_terminal_adoption_review.md)
and [decision inputs](../emdash2/audits/strict-default-action-boundary/foundation_terminal_contract_inputs.json)
preserve the replaced runtime assertions and retained higher/inverse controls.
This is an accepted contract, not five still-failing completion obligations.
Do not reintroduce eager terminal contractions that broke represented units.

## Required continuation

The [native adaptation plan](EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md)
owns mathematical NF stages. The [follow-up ledger](EMDASH_STRICT_FUNCTOR_DUALITY_FOLLOWUP_LEDGER.md)
owns remaining integration and regression dispositions. All rows below remain
in scope until actually achieved or explicitly reassigned by the user.

| Stage | Required outcome | Current next boundary |
| --- | --- | --- |
| NF-1 | Whole walking Observe/Realize with both actual inverses, original noninvertible filler and next-Hom action | Simultaneous moving-boundary comparison; native second inverse; owning qualification/promotion |
| NF-2C | Whole variable-dimensional cube decoder and encoder, including degree zero | Wₙ/NCₙ whole maps and encode-after-decode are checked at variable n; geometric closure, reverse round trip, geometric zero and shift/face coherence remain. Retain bracketing and coordinate order. |
| NF-3C | Native/geometric semicubical nerves on one face index | Whole inverse transformations and coherent face action |
| NF-4C | Cubical degeneracies | Native/geometric identity insertion and all face/degeneracy relations |
| NF-2S | Independent all-flags native simplexes and selected higher shapes | Moving vertices/flags, actual triangle/tetrahedron data, whole terminal-join/cone universality and inverses |
| NF-3S | Same-index semisimplicial equivalence | Common augmented index and vertex convention, whole inverse transformations and face coherence |
| NF-4S | Simplicial degeneracies | Higher-shape identity insertion and required index/unit laws |
| SP-5F | Frontend adaptation to the later Pi/Sigma correction | Resume preserved 18-file candidate, semantic review, actual PathInd/chain consumers, conformance and affected aggregate |
| R14 / NF-CLOSE | Production integration and final qualification | Remaining warning/normalization/health gates, source-pin review, registration, owning CI and updated book/article claims for new nerve results |

Proceed cubical-first after common prerequisites. Exercise the cube-step
consumer early; do not spend repeated tranches only on scalar graph controls.
Independent higher simplex totals must not be defined as the geometric mapping
category or as Path of an object package. Same-index comparisons require
actual whole maps, inverse data and coherent index action.

### Consolidated continuation authorized 2026-10-25

Later explicit user directions expanded the original foundational goal to the
book/article update and import/adaptation/completion of legacy nerves here.
They supersede the launch prompt's old exclusion of applications. The separate
donor goal stays paused; no automatic merge is authorized. Local checkpoint
authorization continues. Completed stages above must not be restarted because
an old prompt or historical paragraph still calls them next.

## Native resumption at the present checkpoint

Put G(C)=Functor_oplax_cat(WalkingArrow,C), N(C)=LaxArrow_cat(C).
Observe:G→N and Realize:N→G are whole constructions. Qualified isolated
comparisons give

```text
Realize ∘ Observe ≐ id_G
Observe ∘ Realize ≐ Graph(U) ≐ Tot(s_U)
Tot(τ) ≐ id_N.
```

The missing requirement is actual reconstruction of the universal graph
section `s_U` against the tautological section τ, or a justified equality of
their whole totals. Fixed-boundary filler recovery and component agreement
are insufficient. Preserve both changing boundaries and all original cells.

At `84f0539e`, the [58-input audit](../emdash2/audits/native_nerve_foundations/transport_verification.json)
passes in 127.501s / 598,308 KiB. It qualifies whole extracted transport
`a ↦ (y′,v∘a)` and Sigma fibre inclusion's whole/capped/next-Hom action.
Nine added identity-overlap reports have canonical typed comparisons;
generic runtime identities remain distinct. Full-module/promotion gates and
inherited warning dispositions remain open.

### Qualified moving-boundary baseline and pending extension

The [selected candidate](../emdash2/audits/native_nerve_foundations/README.md#canonical-moving-boundary-cells-and-whole-filler-inclusion)
proves a whole family/category comparison with the represented native Hom
presentation. In that canonical category, independently varying A and B plus
Γ:(v▹A)∘alpha⇒beta∘(B◃u) form a typed cell. A whole filler functor derives
from existing Sigma inclusions and total duality; its value comparison and
both boundary projections pass, with a distinct-Γ rejection control.

Two constructor-scoped Sigma postcomposition beta rules and one proof-time
total-Hom family view are added only to the isolated candidate. Removing the
beta rules breaks the required consumer. The 68-input prefix passes in
128.850s / 597,312 KiB at 180s / 2 GiB. Four new warning bodies have typed
unit/composition reduct comparisons; no global confluence claim follows.
[Source pins, receipts and replay modes](../emdash2/audits/native_nerve_foundations/moving_verification.json)
replace reliance on the earlier ignored WIP path.

At qualified `85b30c5e`, the direct actual-native constructor still fails at
expanded transport/Hom conversion. The [pending extension](../emdash2/audits/native_nerve_foundations/actual_action_pending/README.md)
subsequently checks that constructor and its whole filler inclusion, but its
constant-family overlap and full qualification remain open. Whole-section
reconstruction still fails. The canonical-category comparison is not an
operational cast or a completed inverse. Full-tuple runtime conversion and
bare Γ-projection inference retain their recorded limits; next-Θ readback was
not reached. Preserve these obligations while the independent cube skeleton
advances. No boundary-extraction primitive or native inverse axiom is adopted;
production/full-module and later integration gates remain.

## Validation, permissions and checkpoint discipline

Follow [root AGENTS](../AGENTS.md), [native SOP](../emdash2/AGENTS.md) and the
[persistent Git workflow](PERSISTENT_GOAL_GIT_EXPERIMENTATION.md). Read the
current plan and targeted source before archived conversation. Use `rg` to
locate owners; preserve staged/unstaged and unrelated work separately.

For semantic changes use intended owner-position copies, subject reduction,
actual consumers, meaningful variance/noncollapse controls and warning review.
Prefer whole owners and projection ladders. Never replace a required whole
comparison by object checks or rename supplied contracts as derived theorems.
Keep actual inverses, generic parameters and noninvertible higher cells.

Run Lambdapi serially with the supported checker and explicit resource guard.
Normal defaults are 90s / 2 GiB. The user's standing authorization permits
reviewed, measured extensions through the supported 3600s / 8 GiB limits,
without repeated permission requests; file limits and no-swap remain.
Aggregates include imports and may take many minutes. Monitor progress,
allocation and host conditions; temporary load does not justify permanent
script/SOP changes or formal normalization changes. Reuse exact green scope
evidence when unchanged. Do not repeat a long aggregate for reassurance.

Documentation-only work uses exact diff, links and owning document lints,
not kernel, TypeScript, browser or PDF aggregates. Semantic promotion receives
the actual affected registry/catalog/health/CI gates; audit-prefix success
alone is insufficient. No source pin may be refreshed just to silence drift.

Implementation and validated local commits on this dedicated branch are
authorized. Pushing, merging to main, PRs, publication, history rewriting,
branch/worktree removal and other-worktree cleanup are not authorized.
Checkpoint only owned files after proportional validation and ledger updates.
Do not mark the consolidated goal complete while any required row remains.

## Deferred design and historical recovery

Future native weak categories/LaxFunctor, strict-public-Functord alternatives,
full Q/coend theory, global Prof endpoint changes, broad core reorganization,
connections/permutations, general Gray monoidality and Kan/Segal/Rezk results
are not prerequisites. Preserve their analysis in the historical records.
Necessary local repairs still belong at actual failed consumers; optional
redesign does not become required merely because it is available.

The research handoff `docs/EMDASH_DUALITY_OP_RESEARCH_HANDOFF.md` and
response-0099 interface `docs/EMDASH_DEPENDENT_HOM_SIMPLIFIED_COVPROF_INTERFACE.md`
remain available by pinned Git reads at
`cc08dbffe9023b89c049b8f8bedba853eb160355` on the earlier research branch.
They are not files in this receiver. They are design history, superseded where
current source/decisions differ; use the historical plan's pins for recovery.

<a id="lax-q-gray-uncurry-and-strict-sigma-maps-consumer-review-2026-10-14"></a>
The earlier Q/Sigma consumer review is preserved at its [historical anchor](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN_HISTORY_THROUGH_2026-10-27.md#lax-q-gray-uncurry-and-strict-sigma-maps-consumer-review-2026-10-14).
Existing incoming audit links remain valid; that dated review is not today's
selected coefficient or Sigma-map contract.

The persistent prompt delegates specifics to this living plan. A future prompt
refresh should describe this consolidated foundations-to-nerves scope and
permissions, rather than restore the launch prompt's obsolete phase boundary.
The active goal remains active; this documentation consolidation creates no
new goal and closes no mathematical obligation.
