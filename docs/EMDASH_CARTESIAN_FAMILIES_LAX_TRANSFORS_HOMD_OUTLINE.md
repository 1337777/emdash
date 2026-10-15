# Cartesian families, lax sections and corrected dependent Hom

Date: 2026-10-14
Status: direct Homd/intrinsic ladders, section-first Pi evaluation and whole
right-represented reindexing check; full qualification remains open
Owner: [living foundations plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Comparison history: [default/profile review](EMDASH_STRICT_CORE_LAX_EXTENSIONS_REVIEW.md)

Continuation after `7dcc1919`: general Pi evaluation now uses the actual
section-first Pi-to-Functord identity view. The old k-first evaluator has
the wrong naturality profile even for a constant family with a genuinely
lax section morphism. The full next-Hom identity and point evaluation check
without restricting those morphisms. Q's fixed right-represented operation
is the whole Cartesian source-reindexing functor; its varying-parameter
comparison is proof-time, retaining the original runtime projections.
The [review](../emdash2/audits/strict-default-action-boundary/production_evaluation_reindex_review.md)
records these interface changes and their limits. Original-source migration
now checks through section 17b; mixed Q/general-FF coherence remains open.

Continuation after `95d73ac6`: piapp1_func now uses the ordinary Pi over the
total-dual Hom index and total-dual Homd fibres. A derived whole constructor
C_I,H:Functor_cat(I,H)->Hom_P(I)(c_1,c_H) supplies the constant-family case
from F's actual Hom functor. The decoded section action reduces to F_1;
both its alpha-action and the Sigma-total second-cell fibre compute F[alpha].
The general tdapp1 modification projections also check and retain arbitrary
epsilon. The [review](../emdash2/audits/strict-default-action-boundary/production_section_action_review.md)
records the new whole structural specialization, its actual bodies and the
remaining evaluation/Q coherence gates. This is not an unrestricted model
or full-goal completion claim.

Current native interface, after `36fceea2`, 2026-10-15:

```text
P(I) = T(Functor_cat(I,T(Cat_cart)))
Hom_Q(A,B) = Cart(A,P(B))
I_x[y] = Hom_K(x,y)
S_E(x) = Transf(K,Q,iota E,iota I_x)
H_E[x] = T(S_E(x))

homd_id_int(E) : Hom_Cart(K,Cat_cart)(E,H_E)
homd_id_src_func(E,x) : T(E[x]) -> S_E(x)
homd_id_src_sec(E,x,u) : Obj(S_E(x))
homd_id_tgt_func(E,x,u,y) : E[y] -> P(Hom_K(x,y))
homd_id_(E,x,u,y,v) : T(Hom_K(x,y)) -> Cat_cart
homd_id_(E,x,u,y,v)[f] = Hom_E[y](E[f](u),v).
```

The fixed-v rung transposes the P-object to its ordinary presheaf view.
The defined relative construction keeps public `homd_int(FF:D=>E)` and
the analogous rungs, with target variable v:D[y] and leaf
`Hom_E[y](E[f](u),FF[y](v))`. Q(A,B), when used as shorthand, means this
Hom_Q(A,B); it is not the former nested Cart expression.

The [native intrinsic projection ladder](../emdash2/audits/strict-default-action-boundary/production_intrinsic_projection.lpfragment)
now checks for arbitrary lax FF through its actual whole section and
direct y/v/f projections. Its final capped result is the retained
`fdapp1_int_hom_fapp0` owner. The expanded negative-Sigma route computes to
the same arrow. The [verification](../emdash2/audits/strict-default-action-boundary/production_intrinsic_verification.json)
records the preceding boundary. Constant-section F[alpha] computation and
general modification projections are now checked by the continuation above;
all consumed Q coherence remains to be qualified. The full source currently
stops in the late evaluation/weakening section.

M_I:Cart(T(I),Cat_cart)->P(I) is a derived implementation map. It reuses
canonical strict Hom constructions; no caller supplies M_I or any equality
evidence. Its object round trips do not identify the two higher mapping
profiles. A stable coefficient Hom view is needed to keep its represented
composition cuts visible; its whole-body comparison and projected action
are checked. A global switch of the conventional strict leg is not selected:
it would also reverse positive constant-section action, conflicting with
the retained Pi(Const B) comparison.

Earlier diagnosis, 2026-10-15: the terminal-source section of an ordinary
strict F must retain F[alpha] for a noninvertible base two-cell. The inner
`Cart(T(I),Cat_cart)` profile below cannot express that intrinsic action;
strict naturality between constant index diagrams would equate its distinct
components. The [index-profile review](../emdash2/audits/strict-default-action-boundary/homd_index_profile_review.md)
records the counterexample and the derived candidate
`P(I)=T(Functor_cat(I,T(Cat_cart)))`. The next Q has proposed Hom
`Cart(A,P(B))`; its outer Cart and the admitted family universe are retained.
The native integration described above supersedes the earlier formation-only
boundary. The concrete index-arrow computation remains open. The all-Cart
formulas below describe the preceding computational reference, not a solution
to the general intrinsic-action requirement.

Native source continuation, 2026-10-15: the selected identity and defined
relative ladders now check inside the staged migration of the original
kernel, using its existing Hom and fibre-covariance owners. The
[owner fragment](../emdash2/audits/strict-default-action-boundary/production_homd_core.lpfragment)
and [verification](../emdash2/audits/strict-default-action-boundary/production_homd_verification.json)
record whole root, source-u, x-naturality and general-FF leaf computations.
Public `homd_int(FF)` is the ordinary Functord view of the Cartesian relative
composite, so callers do not supply a strict wrapper. `Homd_target_section_cat`
names the actual Q-valued transformation category; the former invalid
ordinary-family alias is retired. The full source still stops at the old
intrinsic-action declaration using `Op_funcd(FF)`. Thus the native ladder
has computational evidence, while the intrinsic/y-comparison, Q coherence,
late Sigma/Pi consumers and complete migration remain unqualified. The
prototype history below remains useful, but its names are not a second
public Hom implementation.

## Constraints retained together

The default remains strict functors with conventional lax transfors. Pi is
the default terminal-source transformation category. Both an admitted family
E and its prototypical represented family I_x=Hom_K(x,-) land in the same
Cartesian coefficient universe Cat_cart. Q's outer mapping category remains
Cartesian; the inner index profile needs the correction recorded above.
Earlier all-Cart and fully lax-Q alternatives remain comparison evidence.

There is no global strict-Transf default, Cat-valued strictness exception,
separate Pi_lax replacing Pi, operational proof argument, or standalone
supplied laxity cell. Public foundational names use universes and ordinary
Hom operations; tensor-specific terminology stays in implementation notes.

Standing scope constraint from the user: only the represented Q operations
consumed by Homd are prerequisites. Do not make a complete general profunctor
library, arbitrary coend theory or a new universe hierarchy a prerequisite.
The existing uncurried Prof convention need not be globally renamed.

Clarified 2026-10-15: treat composition synthetically, as production
Prof_tensor does. Local operations on Hom_Q inherit the curried unfolding.
Cross-Hom composition and units are required by the actual whole
Q-valued transformation, but their coend/quotient model need not be
implemented. The supplementary balancing-image check is not a required
milestone; further Q operations require a concrete Homd/Sigma consumer.

## Universes, families and sections

Current choice snapshot, reaffirmed by the user discussion on 2026-10-15:

| Choice | Selected candidate |
| --- | --- |
| Default functors | Strict, with the ordinary public action names |
| Default transformations | Conventional lax: strict pre/right leg, directed post/left comparison |
| Family coefficient | Cat_cart, so fibre functors and transformations inside the coefficient are Cartesian |
| FF across the base | General default lax `Transf(K,Cat_cart,D,E)`, not the earlier strict-Functord sub-classifier |
| Dependent Hom ownership | Independent identity core, followed by a defined relative composition for FF |
| Ordinary blended F | Retained; F is a default strict functor |

The original prototype spells the FF input with `Transf`; the staged native
ladder now also exposes the public Functord facade. Cat_cart does not
make FF strict across K. It makes FF's component functors strict and its
base-comparison transformations strictly natural in fibre variables. The
comparison across a nonidentity base arrow may remain noninvertible.

For an ordinary epsilon:F=>G, the selected conventional direction is
`G[p] o epsilon[x] => epsilon[y] o F[p]`; the pre/right expression is the
strict selected middle action. Reversing this comparison is the oplax
orientation, not a second unconstrained comparison leg.

The strict-Functord alternative remains available for reassessment. If it
were selected, the lax-FF motivation for separating the identity core would
largely disappear, and a blended primitive with strict computations would
be a legitimate candidate. Typing still needs the corresponding native
rules and interaction qualification. The defined relative composite remains
useful in either profile; separation is not a mathematical necessity imposed
on strict FF. No such admission change is selected by this clarification.

Proposed meanings, with names still subject to the focused migration:

```text
Hom_Cat(A,B)      = Functor_cat(A,B)     strict functors, lax transfors
Hom_Cat_cart(A,B) = Cart(A,B)            strict functors, strict transfors

Obj(Cat_cart) = Obj(Cat)
j : Cat_cart -> Cat

E, I_x : Functor(K,Cat_cart)
I_x[y] = Hom_K(x,y).
```

Cart has the Cartesian higher profile at every dimension, not just strict
1-transformation objects followed by arbitrary lax higher modifications.
Its objects share the ordinary strict functor carrier. Components of strict
transformations may be nonidentity and noninvertible.

The family classifiers can keep the existing architectural pattern:

```text
Catd_cat(K)       = Functor_cat(K,Cat_cart)
Functord_cat(E,D) = Hom_Catd_cat(K)(E,D)
                 = Transf_cat(K,Cat_cart,E,D)
Pi_cat(E)        = Functord_cat(const_cart(1),E).
```

Thus Functord and Pi remain lax across K. In contrast, the image E[alpha]
of a base two-cell is a strict transformation between fibre functors, because
it is an arrow in Hom_Cat_cart. These are different levels. The previous
two- and three-dimensional source-u counterexamples have noncommuting fibre
naturality and are excluded by this family type. That removes those local
obstructions, not every remaining coefficient/root qualification.

The precise constant-family whole Pi comparison remains a migration check;
an argument about section objects alone does not qualify all higher equations.

## Ordinary Hom and the canonical transport

Ordinary Hom can already be whole and Cartesian in both endpoints:

```text
Y_K = Hom_int(K) : T(K) -> Cart(K,Cat_cart)
Y_K[x] = I_x.
```

Here T reverses dimension one, R reverses dimensions at least two, and O
reverses all positive dimensions. The candidate source currently spells T
as Op_cat and O as TotalOp_cat; this is an experimental naming boundary.

Let D_K=Cart(K,Cat_cart). The checked canonical covariance has type

```text
C_E,x : E[x] -> Hom_D_K(I_x,E)
c_E(x,u) = C_E,x[u]
c_E(x,u)[y][f] = E[f](u).
```

This map is strict across y. Its represented opposite-direction Hom
construction below can nevertheless have a lax y-comparison.

## Q: Cartesian local Homs and the limited composition needed

```text
Hom_Q(A,B) = Cart(A,Cart(T(B),Cat_cart))

iota(F)[a][b] = Hom_B(b,F[a])             for F:A->B
F*[b][a]     = Hom_B(F[a],b)              an arrow B -/-> A.
```

Cartesian closure gives a whole curry/uncurry presentation by
Cart(A x T(B),Cat_cart). This is simpler than mixed tensor closure, and can
connect to a restricted view of the existing Prof(B,A) with its convention
unchanged. Such bridges are tools for Q operations; the Homd y-section is
not reconstructed by currying an enlarged (y,v,f) base.

The minimal operations to implement and qualify are:

1. The whole represented inclusion iota:Cat_cart->Q, including higher action.
2. Units and right represented composition
   `(P o iota(F))[a][c] = P[F[a]][c]`, implemented by ordinary reindexing.
3. Represented opposite-direction composition
   `V* o U* = (U o V)*`, with coherent chosen represented normal forms or
   actual internal inverse comparisons where required.
4. The canonical directed comparison used by the whole mate/section.

Cartesian closure alone does not make arbitrary coend associators judgmental
identities. Keep the chosen represented computations and the general Q
composition/coherence qualification distinct. Q:Cat remains a structural
computational carrier under the accepted convention, not a proof of a
complete Cartesian model of every profunctor operation.

The required mate comparison has a concrete construction. Put
`h_y(v,f)=Hom_E[y](E[f](u),v)`. For q:y->z, its direction is

```text
iota(I_x[q]) o h_y  =>  h_z o iota(E[q]).
```

Writing the left composite at (v,k) using its intermediate f, its generating
data are beta:k=>qf in Hom_K(x,z) and `a:E[f](u)->v`. The comparison sends

```text
(beta,a)  |->  E[q][a] o E[beta][u]
              : E[k](u) -> E[q](v).
```

Strict E identifies the intervening `E[qf](u)` and `E[q](E[f](u))`. Cartesian
fibre naturality supports the required higher functorial action. The whole
map must factor through the actual represented composition construction;
this generating formula is its beta specification, not a replacement for
the internal operation. No inverse to beta or general adjunction library
is needed to state its direction. The native mate remains a structural
constructor until this whole comparison and coherence are qualified.

The prototype for using Q is the Homd y-component itself:
`h_y : Obj(Hom_Q(E[y],Hom_K(x,y)))`. It is a genuine profunctor, with the
conjoint representation by `f |-> E[f](u)` in the strict identity case.
Fixing v yields the one-slot presheaf below. This representation does not
restrict Q's general inhabitants; projections, restrictions and actual
Homd action determine the needed interface.

At the foundational layer this Hom_Q identification is computational: the
local operations come from the nested mapping categories. Recovering the
former Homd tail and projections in the ordinary 1-categorical
specialization, at matching strictness profiles, is a compatibility
requirement. No separate local Q action calculus is intended.

## Trace to the production Pi-based ladder

Source review, 2026-10-15; this is a mathematical/interface correspondence,
not a newly checked whole-classifier equivalence. First work with an ordinary
base and matching coefficient/transformation profiles. Write

```text
I_y = Hom_K(x,y)             J = I_x[q] : I_y -> I_z
F = E[q] : E[y] -> E[z]      q : y -> z
P_y = [T(I_y),Cat]
M_y = [E[y],P_y]
h_y(v)(f) = Hom_E[y](E[f](u),v).
```

The brackets suppress the selected coefficient/strictness annotations;
they do not identify Cartesian and default mapping categories.

In production `emdash3_2.lp`, `Homd_target_section_catd(E,x)` is defined
using `Functor_catd(E,HomPresheaf(x))`. The whole `Functor_catd` base action
uses `Hom_tele_func`; its capped action uses `Hom_func`. Unfolding their
pre/postcomposition reading gives

```text
M[q^op](H) = precomp(T(J)) o H o F.
M[q^op](h_z)(v)(f) = h_z(F[v])(J[f]).
```

Thus the old target already contains both restrictions needed by the new
comparison: source-fibre restriction by F and presheaf-index restriction
by T(J). The correct canonical Homd action has direction

```text
chi_q : h_y => M[q^op](h_z)
chi_q[v][f](a) = E[q][a].
```

In Q the corresponding cell is

```text
lambda_q : iota(J) o_Q h_y => h_z o_Q iota(F).
```

The right composite is ordinary restriction: it computes to `h_z o F`.
For the left composite, maps from `iota(J) o_Q h_y` into a target R
correspond, in the ordinary profunctor interpretation, to maps from h_y
into `precomp(T(J)) o R`. This is the represented-composition/restriction
correspondence; it is not an equality between that left composite and a
restriction. The ordinary precedent is the base-change/mate calculus in
[Shulman, Sections 4-5](https://arxiv.org/pdf/0706.1286v2#page=17).
No general adjunction or coend implementation is a prerequisite for using
this correspondence as the semantic specification of the consumed operation.

Concretely, restricting lambda_q to its represented identity introduction
at `k=J[f]` recovers chi_q. Its consumed introduction with
`beta:k=>J[f]` and `a:E[f](u)->v` computes by existing target-index action:

```text
(beta,a) |-> h_z(F[v])[beta](chi_q[v][f](a))
         = E[q][a] o E[beta][u].
```

For an ordinary base I_z is discrete, so the beta input carries only the
identity case. At higher bases the second line explains the extra index
action already checked by the current Homd comparison. It does not establish
a general omega-level equivalence of section classifiers. No quotient
representatives or new factorization-based local Hom are required here.

There is a necessary correction to the production comparison. Its
`Pi_cat(M)` uses the positive section action
`M[q^op](h_z) -> h_y`, whereas the required chi_q points the other way.
This is the previously recorded
[Homd target polarity defect](TYPESCRIPT_EMDASH_HOMD_TARGET_POLARITY_DIAGNOSTIC.md),
which already has a walking-arrow control. Consequently the literal old
Pi target is not a qualified semantic reference even after restricting K
to an ordinary category. Reuse its local projections and restriction
owners; preserve the corrected direction in the Q-valued transformation.
Compatibility means a direction-correct section interpretation with matching
profiles, not a new equality to the defective old Pi declaration.

This direction already matters for the identity Homd of a strict family
over `0->1`. Let E[0] be the discrete two-object category {u,v}, E[1] be
terminal, and E[q] the unique functor. With x=y=0, z=1 and f=id_0, the two
values are `h_0(v,id_0)=Empty` and `h_1(E[q]v,q)=Unit`. The correct chi_q
is Empty->Unit; the old positive Pi requests Unit->Empty. This ordinary
semantic example uses neither a general FF nor nonidentity higher cells.

Implementation consequence: the existing `cart_homd_section` right-represented
composition rules, `cart_homd_ordinary` extracted comparison and
`cart_homd_composition` introduction beta cover precisely this dictionary.
Unit and composite-base consumers should use their inherited action and
normal forms. Additional Q laws require a concrete consumer. This source
review adds no native rule, general composition theory or new check suite.

## Direct section and projection ladder

Using default lax transformations into Q:

```text
S_E(x) = Transf_cat(K,Q,iota E,iota I_x)
       = Hom_{Hom_Cat(K,Q)}(iota E,iota I_x).

homd_id_src_func(E,x)       : T(E[x]) -> S_E(x)
homd_id_src_sec(E,x,u)      : Obj(S_E(x))
homd_id_tgt_func(E,x,u,y)   : E[y] -> Cart(T(Hom_K(x,y)),Cat_cart)
homd_id_(E,x,u,y,v)         : T(Hom_K(x,y)) -> Cat_cart
homd_id_(E,x,u,y,v)[f]      = Hom_E[y](E[f](u),v).
```

The source-u functor is the transpose of C_E,x followed by the whole mate
operation. The y projection is the actual transformation component; v/f
use the curried Q Hom directly. A whole postcomposition by j supplies the
ordinary Cat-valued view if a downstream consumer needs it.

For h:u0->u1, the y/v/f observation of source-u action is the whole functor
precomposing by E[f][h]. This is an explicit computational requirement,
not merely a declaration that the source-u map exists.

## Stronger outer root and current native evidence

The user's observation about the outer x is now implemented in the
[experimental root](../emdash2/audits/strict-default-action-boundary/cart_homd_root_review.md):

```text
H_E : Functor(K,Cat_cart)
H_E[x] = T(S_E(x))

homd_id_int(E) : Obj(Hom_Cart(K,Cat_cart)(E,H_E))
homd_id_int(E)[x] = T(homd_id_src_func(E,x)).
```

This selects a strict canonical root while keeping the default Transf lax.
Its ordinary Functord view can use the existing whole inclusion. Do not
infer strictness of every family map FF or of the y-section from this choice.

For p:x->x', precomposition gives pre_p:I_x'=>I_x. The canonical transport
relation is `c_E(x,u) o pre_p = c_E(x',E[p](u))`. Applying represented
composition should give the root's naturality

```text
H_E[p] o homd_id_int(E)[x]
  = homd_id_int(E)[x'] o E[p].
```

The whole-functor equation is checked independently of the root's strict
wrapper. Its diagnostic uses the covariance/mate constructor laws and
ordinary equality congruence; operational symbols carry no proof argument.
The root's base-two-cell component is also computed, with noncollapse
retained. The target H_E is a definition through represented Hom on the
diagram category. An internal dimension-two shift accounts for the T in
the section fibre and returns the family base to K.

This is a checked native constructor/projection candidate under the stated
Q/mate laws. The root check is separate from the later y-comparison and
Sigma-Hom checks below. It does not establish a complete Q model or a public
kernel migration.

## Sigma and relative maps

Public migration boundary, reviewed 2026-10-15:

The reference is the original pre-goal kernel at
`f8af1fca472657ff1598c639eb29c0566e7b2ec0`. Even feasible improvements are
deferred until after migration. Start from its actual owner/rule shapes;
justify departures by a selected Homd/duality/default contract change and
an actual consumer, rather than by the convenience of a new audit.

| Production owner | Migration treatment |
| --- | --- |
| `comp_fapp0(Sigma_cat(E),...)` with `sigma_arrow` / `sigma_arrow_intro` | Preserve the existing direct composition formula; adapt its coefficient and corrected Hom presentation |
| `sigma_map_func` and `fdapp1_int_hom_fapp0` | Preserve the total-map / intrinsic-action projection architecture |
| `sigma_map_transf` | Preserve its existing whole type and vertical component; add projections when an actual migration consumer requires them |
| New `sf_cart_sigma_comp_fibre` audit owner | No literal production counterpart; retain as audit scaffolding, without presuming public promotion |

The composition audit supplies a new structural compatibility law with a
checked consequence. It does not demonstrate that production needs that
new stable helper. The Homd/Sigma/map runtime candidates do not reference
it. Required duality/profile corrections may change signatures and owners,
but optional normalization improvements remain separate from this migration.

The [Sigma-Hom candidate](../emdash2/audits/strict-default-action-boundary/cart_sigma_review.md)
retains objects (f,a), with f:x->y and `a:E[f](u)->v`. For the whole
fixed-v presheaf H:T(I)->Cat_cart, it defines

```text
O_fib(H) = total_op_cart o R(H) : O(I) -> Cat_cart
Sigma_con_I(H) = O(Sigma_(O(I))(O_fib(H)))
Hom_(Sigma E)((x,u),(y,v)) = Sigma_con_I(homd_(E,x,u,y,v)).
```

One Sigma constructor is used. Both base and fibre duality are necessary:
the explicit constant-family RHS computes to
`Hom_K(x,y) x Hom_C(u,v)`, with forward fibre two/three-cell controls.
Strict E gives `(q,b) o (p,a)=(qp,b o E[q][a])`. The arbitrary-endpoint arrow
interface and recursive first projection check, including the constant
total's product reduction.

The [total-map continuation](../emdash2/audits/strict-default-action-boundary/cart_sigma_map_review.md)
now supplies Sigma_func(K):Functor(Functor_cat(K,Cat_cart),Cat). Its first
Hom at FF is the derived negative Sigma map of the existing intrinsic Homd
transformation. Object, arrow, canonical transport, modification and
recursive base-two-cell projections check. Identity computations check;
composite intrinsic Hom action has a proof-time comparison which preserves
the ordinary/mate runtime extractor. The
[whole composition continuation](../emdash2/audits/strict-default-action-boundary/cart_sigma_composition_review.md)
now supplies the structural whole compatibility law and derives the equality
of the two expanded total-arrow routes. Lax FF is retained. The whole
off-diagonal action of mapped modifications and public migration remain.

A general FF:Functord(D,E) can remain lax across K. Its component functors
are strict and its base-comparison transformations are strict in the fibre
variables because the coefficient is Cat_cart. This addresses the earlier
fibre-square obstruction without assuming FF is strict across K. Actual
Sigma-map coherence and relative Homd action still require their consumers.
The accepted identity-core/defined-relative interface remains available;
there is no reason to introduce a second primitive Homd theory for FF.

Admission clarification, 2026-10-15: "general lax FF" here means a
conventional-lax transformation between strict K->Cat_cart families. It
does not mean the old unrestricted K->Cat family profile. Requiring FF
itself to be strict was a stronger sufficient option: it would make its
base comparison cells identities. The selected coefficient instead makes
those extracted comparison cells strictly natural in fibre variables while
allowing them to be nonidentity and noninvertible. The native Sigma-map
candidate has checked projections; its auxiliary whole composition audit
uses an explicit structural law. Neither is a completed general
functoriality theorem derived from the unchanged production kernel.

The [relative/intrinsic continuation](../emdash2/audits/strict-default-action-boundary/cart_homd_relative_review.md)
now implements the relative root as an actual composite for general default
lax FF:D=>E:

```text
target_con_func(D,E)
  : T(Transf_{K,Cat_cart}(D,E)) -> Hom_Cart(K,Cat_cart)(H_E,H_D)

homd_rel_int(FF) = target_con_func(D,E)[FF] o homd_id_int(E).
```

Its stronger outer type comes from ordinary represented Hom on the diagram
category; it does not imply strictness of FF across the original y-base.
The literal x/u/y/v/f projection computes `Hom_E[y](E[f](u),FF[y](v))`.
The identity FF returns the identity core, and modification variance is
retained at the whole target-action functor.

The corrected intrinsic-action projection now defines forward laxity from
the whole action and an identity filler, without an independent witness.
Its identity-map normalization checks. The whole action remains a structural
owner; nonidentity mate-comparison computation and full coherence remain
required. The public family-classifier aliases above are still migration
proposals subject to downstream closure checks.

The [ordinary-action continuation](../emdash2/audits/strict-default-action-boundary/cart_homd_ordinary_review.md)
now connects that extractor to ordinary transformations. The strict F-action
is the canonical covariance of Hom_B(F[x],F[-]) at id_F[x]; default lax
epsilon is internalized by fixed postwhiskering followed by that map. Its
whole component and first higher action compute. Applying the extractor to
the actual Homd section defines the y-comparison displayed above, with direct
v/k projections to the expected target Hom. No additional comparison cell
is supplied. The generating beta on its left represented composite and the
consumed coherence remain open; the typed extraction alone does not supply
them.

The [represented-composition continuation](../emdash2/audits/strict-default-action-boundary/cart_homd_composition_review.md)
now implements that generator beta on the actual extracted comparison.
The literal Homd observation sends `(beta:k=>qf,a)` to
`E[q][a] o E[beta][u]`, through a whole functor whose first Hom also checks
in both observation orders. Stable intrinsic/comparison projection rungs
keep this connected to the original root. The introduction and beta are
structural laws for the selected represented Q composition; balancing,
unit/composition/parameter coherence and Sigma-Hom remain unqualified.
The scope clarification above keeps general balancing/model qualification
outside the implementation prerequisite path; checks of the synthetic
operations actually consumed by Homd/Sigma remain required.
