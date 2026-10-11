# Strict-functor and corrected-duality migration: consolidated handoff

Date: 2026-10-11
Plan-ID: STRICT-FUNCTOR-DUALITY-FOUNDATIONS-V3.2
Status: active; SF-0 owner audit and first bounded strict-action qualification in progress

Depends-On: active v3.2 owners and root/nested SOP; completed action-profile
integration; pinned response-0099 coefficient/Homd design and its research
recovery inventory.

Supersedes: the default-lax-functor migration direction and Op/Homd deferral
for this authorized worktree only; earlier F/FF-unbundling and Q_lax proposals.
The completed integration evidence remains valid for its original snapshot.

Side-Task-Ledger: SF-0 through SF-CLOSE and the launch/tranche ledger below;
bounded owner experiments are retained with their replay inputs and outcomes.

Infinity-Codex-Origin: fork session `01a12a87-a47e-73f1-9351-1159597be30d`;
user accepted the prior response and authorized implementation, a dedicated
worktree, persistent goal and validated local checkpoints.

Infinity-Codex-Decision-Responses:
`infinity-codex:01a0f2b4-df23-77f3-bc7c-f7c9ea631a6f:01a12a6e-5c76-7fd3-a96b-da19630da2eb`;
selected design
`infinity-codex:01a0f2b4-df23-77f3-bc7c-f7c9ea631a6f:01a11f8c-e064-7113-9728-9e4ecca6c906`.

Launch: 2026-10-11. The user accepted the consolidated response and explicitly
authorized the new worktree, implementation and persistent goal. The plan
was copied from `cc08dbffe9023b89c049b8f8bedba853eb160355` onto the main pin
below. Existing local-checkpoint authorization continues to apply.

Accepted response: prior-thread 0105, logical ID
`infinity-codex:01a0f2b4-df23-77f3-bc7c-f7c9ea631a6f:01a12a6e-5c76-7fd3-a96b-da19630da2eb`.
Its archive is in the prior main-worktree session. This new conversation is
a fork; discover its archive directory rather than reusing that session ID.

## Current execution contract

The first implementation pass restores STRICT FUNCTORS as the structural
default and implements the selected corrected-duality/profunctor Homd design
together. Retain lax/non-strict transfors and the native blended F/FF owners.
Keep the current lax machinery as the implementation basis for the explicit
weaker interface; this does not require strict wrappers or a duplicated
strict API throughout the new core. Do not replace native laxity with a new
encoding or independently supplied compositors.

The user's broader LaxFunctor-between-weak-categories idea is SHARED DESIGN
ONLY for this first pass. It must guide a compatible boundary without adding
a weak-category implementation prerequisite. The separate application work
is paused and reserved for later rebasing/migration; none of its reconstruction
or equivalence tasks is an acceptance test in this goal.

These directions supersede the earlier handoff at `81e0ab4e` where it made
F/FF unbundling primary or suggested Q_lax, operads/computads and an externally
selected weak-category model. Those are not selected implementation routes.
The Q PROFUNCTOR COEFFICIENT from response 0099 remains selected; it is a
different object from the rejected Q_lax source-resolution detour.

## Pins and active workspace

- Base: main `f8af1fca472657ff1598c639eb29c0566e7b2ec0`.
- Branch: `goal/strict-functor-duality-v3.2`.
- Worktree: `/home/user1/emdash1-strict-functor-duality-v1`.
- Research recovery: `docs/EMDASH_DUALITY_OP_RESEARCH_HANDOFF.md` and its
  pinned artifact inventory on `goal/native-nerve-completion-v3.2`.
- Selected design: response 0099, logical ID
  `infinity-codex:01a0f2b4-df23-77f3-bc7c-f7c9ea631a6f:01a11f8c-e064-7113-9728-9e4ecca6c906`,
  consolidated in `docs/EMDASH_DEPENDENT_HOM_SIMPLIFIED_COVPROF_INTERFACE.md`.
- This workspace was created from main at launch; the research and paused
  application worktrees remain untouched.

The worktree has its own dependency links and passed the frozen-lockfile
bootstrap and workspace contract. Main's Infinity Codex archive verified
1,557 responses at launch. No hook configuration was changed. Use pinned
Git reads for older research rather than copying the entire experimental
tree. Preserve the paused application checkpoint separately.

## Preserve the selected profunctor design

Write T for dimension-one transpose, R for reversal from dimension two
upwards, and O for total reversal. C2 reverses dimension two alone. These
are the current design meanings, not authorization to equate distinct
higher actions. Primitive/derived names can be settled with the final owner
signatures before their consumers are migrated.

Keep Cat-valued strict families and the selected coefficient convention:

```text
Hom_Q(A,B) = [A,[T(B),Cat]]

iota(F:A->B) : A -/-> B
  iota(F)[a][b] = Hom_B(b,F(a))

kappa(F:A->B) : B -/-> A
  kappa(F)[b][a] = Hom_B(F(a),b).
```

Existing Conjoint_prof and Companion_prof supply the opposite-endpoint
views under the current native naming convention. Retain those owner
relationships; no independent supplied adjunction is an input.

For strict E:K->Cat_adm and I_x=Hom_K(x,-), the selected whole section is

```text
S_E(x) = Transf_lax_{K,Q}(iota E, iota I_x).
```

Its y-component is E[y]->[T(Hom_K(x,y)),Cat]. The whole target uses the
covariant represented-index package Gamma_K:C2(K)->D_K with
Gamma_K[p][y]=kappa(f |-> f p), where D_K is the admitted diagram category.
Do not confuse it with the different iota-precomposition package over T(K).

```text
Homd_target(E) = Hom_D_K(iota E,-) o Gamma_K : C2(K)->Cat.
T_fib(E) : C2(K)->Cat,    T_fib(E)[x]=T(E[x]).
```

This is the design to IMPLEMENT and QUALIFY, not a prompt to restart the
ordinary-diagonal, primitive-Pi, combined-context, Kan/adjunction or general
ProfFamily/SigmaProf searches. Response 0099 itself retained the whole omega
coefficient, represented lift and native coherence qualifications. They are
implementation obligations, not grounds to claim that this design has
already been typechecked or fully proved.

## Public defaults and removal of redundant strict wrappers

Reinterpret the public `Functor` object classifier as strict. Keep the names
Functor_cat, fapp0, fapp1_func, fapp1_fapp0 and the ordinary Hom/action owners
for that default. Do not create a parallel fapp0_sfunc/fapp1_sfunc story and
replace every ordinary type by an extra StrictFunctor wrapper.

The target naming contract is

```text
Functor(A,B)          strict default maps
fapp*                 their ordinary native action
hom_int(F), homd_int(FF)  retained blended public owners
LaxFunctor(...)       future weaker interface, reusing native implementation
```

The existing StrictFunctor, make_strict_functor, strict_functor and related
object-view operations become candidates for compatibility aliases/adapters
and then retirement. Migrate their consumers and confirm the required
computation before deleting them. Do not keep an obligatory strict_functor
wrapper as the permanent way to use the new default. Likewise audit the old
IsStrictFunctor properties as potentially derived/redundant on default maps.

This does not make all higher mapping categories identical. The current
StrictFunctor_cat has ambient transfors, whereas GrayHom_lax selects a
particular transfor profile. Only collapse category views whose entire Hom
profile agrees, not those that merely share strict functor objects. The
coefficient projection Hom_cat(Cat_cat,A,B) must have its declared full
profile; an extra object classifier named StrictFunctor is not a solution
to a difference in higher transformations.

## Preserve blended F and FF interfaces

Keep the native stable heads and the projection ladder, including
hom_int(F), hom_con_int(F), homd_int(FF), homd_(FF,...) and the paired
covariant/contravariant action heads. An identity specialization can be a
reference case without becoming the only primitive public interface.
Generic precomposition factorizations remain useful comparisons, not a
mandatory rewrite of every blended owner into a transparent alias.

For the selected strict family profile the blended target is schematically

```text
FF : D => E
homd_int(FF)
  : Functord_C2(K)(T_fib(E), Homd_target(D))
homd_src_func(FF,x) : T(E[x]) -> S_D(x)
homd_src_sec(FF,x,u) : Obj(S_D(x))
homd_tgt_func(FF,x,u,y) : D[y] -> [T(Hom_K(x,y)),Cat]
homd_(FF,x,u,y,v) : T(Hom_K(x,y)) -> Cat
homd_(FF,x,u,y,v)[f] = Hom_E[y](E[f](u),FF_y(v)).
```

The target-y component is hom_con_int(F_xu,y) o FF_y, where
`F_xu,y(f)=E[f](u)`. This is compatible with keeping both blended owners.
The whole relative interpretation uses composition with iota(FF); it need
not introduce a second independent Homd theory or an operational comparison
parameter.

Distinguish FF's component functors from its displayed naturality: the
current Functord interface is a transfor classifier too. Strict defaults for
FF_y do not by themselves make the naturality cell lambda(q) an identity.
A selected fully strict displayed profile may have that computation; a lax
transfor profile must retain its original lambda. This affects which laws
are valid, not whether FF may remain a blended argument.

## Preserve the current native lax implementation

The existing `fapp*`, `tapp*`, `fdapp*` and `tdapp*` owners already retain
normal-lax action. In particular the nucleus defines

```text
fapp1_compositor(F,g,f)
  := tapp1_post_laxity_cell(id_transf(F),g,f)
```

through the whole internal action and displayed laxity extraction. The new
explicit LaxFunctor view must preserve that computation and higher action.
A defined accessor may remain, but there is no new primitive mu, independently
supplied compositor, or external record of equality proofs.

The first pass makes the current ordinary carrier/actions the strict public
default and preserves the native lax machinery as the basis for the explicit
weaker interface, reusing implementation wherever possible. The exact
compatibility/export boundary is selected by the owner audit; completing
the weak-category interface is not a prerequisite. It does not rederive
lax functors through Q_lax(A), nor require a new classifying-source theory.
The cited two-dimensional precedent for that alternative did not establish
an arbitrary omega implementation; no answer to that separate problem is
needed for this migration.

Keep the normal identity convention and each original comparator's direction.
Strict views may compute the appropriate intrinsic comparator to identity.
Lax views retain it. Do not install an unqualified lax-to-strict coercion.
Names and kernel views are to be selected in the first owner audit; a clone
of the semantic interface need not duplicate every downstream theorem and
normalization pipeline.

## Shared design only: lax functors between weak categories

The user's intended primary weaker interface is, schematically,

```text
LaxCat                          native weak/lax category profile
as_lax_cat : Cat -> LaxCat       strict-to-weak inclusion
LaxFunctor : LaxCat -> LaxCat -> Grpd.
```

Thus the current lax maps between strict A,B become the specialization
LaxFunctor(as_lax_cat A,as_lax_cat B). This is not a weaker interface forever
restricted to strict endpoints with weak objects bolted on later.

Surface elaboration may eventually omit the inclusion, but its kernel view
must preserve the actual structure and rule discriminators. There is no
reverse coercion sending an arbitrary weak category to the strict Cat
carrier. Otherwise strict composition/Hom rules would apply to it again.
The current strict-base lax implementation should be preserved so it can
serve this specialization; implementation of the full LaxCat carrier is
outside the first-pass prerequisite boundary.

The requested meaning of weakness is native:

- Associativity is not an unconditional unification equation in the weaker
  category profile.
- Its represented Hom/precomposition/postcomposition action is lax rather
  than silently strict.
- Higher comparison cells come from that same native internal action.

Do not substitute an operadic/computadic encoding or an external weak-category
framework for this design. Assess the available native operations and their
coherence directly.

There is real mathematical content to this proposal. If P_w(y)=Hom_C(w,y)
is lax, its intrinsic compositor for g:x->y and h:y->z has a component at
f:w->x with direction

```text
h o (g o f)  ==>  (h o g) o f.
```

The contravariant represented action has the complementary directional
bookkeeping. Their relationship, units and higher compatibility must be
checked in the same internal calculus. Two arrows in opposite directions
are not automatically inverse data. If the intended profile only retains
directed structural comparisons, do not silently describe them as invertible
associators; conversely, identify actual inverse/coherence requirements if
those are desired.

Removing one associativity unifier is not the complete implementation:
strict identity-Hom accumulation and other composition/naturality owners can
also impose associativity. For example, strict postcomposition accumulation,
evaluated at f, compares precisely the two bracketings above. Audit every
such route when the weak layer is eventually implemented. The current lax
functor implementation was built with strict category endpoints, so its
extension to weak endpoints also needs this audit rather than a claim that
one deleted rule supplies all coherence.

This is a shared-design obligation, not authorization to start that extension
before the combined strict-default/duality pass is complete.

## Useful sharing versus unwanted duplication

A native weaker-action layer can serve both:

1. lax maps between weak categories, including the strict-base specialization;
2. lax represented Hom action of the weak categories themselves.

The strict layer supplies stronger computational laws and canonical views
for the selected strict objects/maps. Shared intrinsic action, projection
ladders, comparator extraction, composition mechanisms and duality bookkeeping
are therefore useful common infrastructure. Separate classifier/action heads
and laws are justified where their contracts differ. Do not merge distinct
profiles through an object-only unifier merely to reduce the line count.

Retain non-strict transfors in the strict core. The category of categories
and its mapping profiles still need honest whole interchange/variance types;
strict functors alone do not turn every lax-transfor universe into an ordinary
strict Cartesian coefficient. Review this in the native interface rather
than introducing a general weak-category implementation as a workaround.

## One coordinated migration, bounded checkpoints

Prefer one coordinated target and one traversal of each affected owner to
two complete repository-wide migrations. An owner should be adapted to its
final strict/lax map profile AND corrected duality signature before migrating
its dependents. This does not mean one enormous unreviewed patch.

The previous action-profile integration deliberately changed both functor
composition and transfor naturality. Under the user's new default choice,
restore the appropriate strict-F preservation/accumulation laws while
retaining the transfor-laxity changes. Use the original owner diffs as a
source, not a blanket Git revert of that integration: it also contains
normalization, profiling, resource and consumer fixes worth preserving.

| Stage | Required first-pass outcome |
| --- | --- |
| SF-0 | Final strict/lax carrier and coefficient signatures; selected response-0099 Q design; blended F/FF retained; weaker shared-design boundary recorded. Inventory the previous migration by semantic owner and choose the actual source/version/qualification boundary. |
| SF-1 | Reinterpret Functor/fapp* as the strict default; migrate and retire redundant strict wrappers where valid; retain lax/oplax transfors and preserve native lax action/extraction for its explicit interface. Break the late-property/bootstrap dependency without a parallel strict API or supplied-compositor calculus. |
| SF-2 | Correct native dualities and their whole action, ordinary Hom, coefficient and represented-index owners. Preserve paired heads and arbitrary directed higher data. Qualify the core before a broad owner sweep. |
| SF-3 | Implement the chosen profunctor-based blended Homd ladder, including the identity specialization, whole x/u and y/v/f projections, and compatible strict-family Sigma/Pi. Correct constant-family Sigma-Hom at whole and higher levels. |
| SF-4 | Migrate the declared foundational ownership/dependency scope to the combined final signatures, including ordinary Hom/precomposition laws and retained explicit lax consumers. Do not perform a second full duality migration afterward. |
| SF-CLOSE | Exact semantic/computational contract, preserved intrinsic laxity, targeted diagnostic repair, completed required validation, and a handoff for separate downstream migration. Weak-category implementation and application equivalence tasks remain outside this first pass. |

Acceptance is foundational: strict identity/composition and higher action;
retained nonidentity lax-transfor cells and recoverable native lax-functor
action/extraction for the future shared-design profile; whole projection and
normalization order; correct Hom variance and duality action; actual native
Homd/Sigma comparisons. Reject the recorded wrong reverse-arrow derivations
for the intended type/variance reason. No theorem about global consistency
of Cat:Cat is claimed from these local repairs.

Existing affected application checks may run as integration gates. This does
not add application reconstruction or equivalence development to the goal.
Do not label the whole repository migrated while excluding broken dependents:
SF-0 must state the foundational qualification boundary and any separately
versioned or explicitly unmigrated interfaces.

## Workflow and launch handoff

Follow current root/nested AGENTS, active source and the completed profile
integration before archived experiments. Use full-file owner-position probes,
subject reduction, serial bounded resources, negative controls, exact warning
review, rule/LHS audits, registration/catalog/health and the required CI gates.
Preserve source-pin failures as review evidence; updating a pin cannot itself
qualify a changed mathematical interface.

Local checkpoints are authorized after bounded green tranches and exact
staged-diff review. Preserve other branches/worktrees. No pushing, merging,
publication, PRs, history rewriting or cleanup is included. The first pass
uses this dedicated worktree; do not recreate or reset it on continuation.

Active persistent objective (launched in the fork session above):

> Implement and qualify the combined strict-functor-default and corrected-
> duality categorical foundation in /home/user1/emdash1-strict-functor-duality-v1
> on goal/strict-functor-duality-v3.2, based on
> f8af1fca472657ff1598c639eb29c0566e7b2ec0. Follow and evolve
> docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md for the precise stages,
> source/version boundary, assumptions, evidence and acceptance. Preserve the
> existing blended F/FF hom/homd interfaces and implement the selected
> response-0099 profunctor design with corrected whole duality and the direct
> internal projection ladder. Reinterpret Functor/fapp* as the strict default
> and retire redundant strict wrappers after migrating their consumers.
> Preserve current native lax action and intrinsic compositor extraction as
> the basis of the explicit weaker interface, while retaining non-strict
> transfors. Do not add a parallel strict API, standalone laxity witnesses,
> mandatory F/FF unbundling, Q_lax resolutions, operad/computad encodings or operational equality-proof
> payloads. Co-design the future LaxFunctor interface between native weak/lax
> category objects with a strict-to-weak inclusion, but keep its implementation
> outside the first-pass prerequisite boundary. Use one coordinated migration
> through bounded reviewed checkpoints, rather than a blanket revert or two
> independent whole-repository sweeps. Keep this goal foundational and separate
> from the paused application goal. The dedicated branch/worktree,
> implementation and validated local commits are authorized; follow all
> root/nested SOP. Do not push, merge, publish, open PRs, rewrite history,
> clean up other worktrees or resume other goals. Complete the stated
> foundational outcomes and qualification before downstream migration.

Pre-launch review evidence: current source, migration owner history and
response 0099 were read. The compositor's defined intrinsic body and the
surviving strict identity-Hom rules were inspected. The weak-Hom
associativity calculation remains hand analysis, not a checked construction.

## Launch and current tranche ledger

The new worktree is based on the main pin above, not the research branch.
Only this consolidated plan was initially transferred; research remains
available through its pinned Git objects. Bootstrap completed with pnpm
11.16.0 and Node 24.11.1; workspace:check passed. The optional package-manager
update metadata fetch failed after installation, without affecting the
successful bootstrap. No lockfile change was made.

The persistent goal is active in fork session
`01a12a87-a47e-73f1-9351-1159597be30d`, with the objective above and no token
budget requested. Commits/checkpoints are authorized; no remote mutations
or changes to the paused application work are included.

The [source/owner review](EMDASH_STRICT_FUNCTOR_DUALITY_SOURCE_REVIEW.md)
records the current qualification scope and the separation of strict
functor laws from transfor naturality. The
[first implementation pilot](../emdash2/audits/strict-default-action-boundary/README.md)
retains exact fragments, a pinned full-file replay, negative controls and
an unchanged profile-owner consumer. Its final candidate restores capped
and whole functoriality, the actual intrinsic compositor identity and both
post/pre cap-first joins. The source still defines the compositor through
intrinsic action; no new witness or operational proof argument is used.

Validation for this pilot is in its `verification.json`: the final full-file
copy passes 19 positives and three transfor negatives; the unchanged profile
consumer also passes. The two intermediate missing-computation probes fail
at their intended assertions, with their inputs and receipts retained. The
strict LHS audit reports zero unreviewed reconstructible compound slots.
All pilot runs used subject reduction, 90 seconds, 2 GiB, 64 MiB file limits
and scoped `OCAMLRUNPARAM=o=20`; the final full-file run used 6.88 seconds and
344,024 KiB measured child maximum RSS. Warnings rise from 648 to 796, with
148 additional reports and none removed. Their owner/constructor review is
pending, so this is not a promotion or confluence certificate.

The launch `make check` suite selected 634 targets and was intentionally
interrupted after 58 successful fresh checks to return to proportional
owner validation. Its successful nucleus and profile receipts are retained;
the full suite is not reported green. No TypeScript/print aggregate or
source-pin update is warranted by this non-library pilot. Plan lifecycle,
document links and the exact diff are the documentation checkpoint gates.

The default library has not yet been changed. Warning and constructor
qualification, corrected whole duality/coefficient signatures and the
selected Q/Homd implementation remain open. A fresh public weaker carrier
is not a first-pass prerequisite; see the source review for how the old lax
implementation remains recoverable while its native transfor machinery
continues to be used.

Next: qualify the pilot's changed warning/constructor families, especially
identity, opposite, evaluation and represented Hom projections; audit the
unwrapped default against profile consumers; then prepare the first
production slice together with the final core duality signatures. Retain
the generic-transfor negative controls throughout. Do not restart the
rejected Homd architectures or begin the weak-category implementation.
