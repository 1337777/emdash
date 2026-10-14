# Strict Cartesian core with explicit lax interfaces

Date: 2026-10-14
Status: strict-functor/lax-transfor default retained; shared Cartesian family
coefficient now selected for Homd; earlier alternatives retained below
Plan: [foundations goal](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Previous comparison: [design matrix](EMDASH_FOUNDATION_PROFILE_DESIGN_MATRIX.md)

Latest accepted candidate: the
[Cartesian-family/lax-section outline](EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
keeps the lax default and Pi alias, while both E and represented Hom land
in Cat_cart. It prioritizes Cartesian Q and a strict canonical outer root
to qualify, with only the represented Q operations needed by Homd. This is
distinct from making the public Transf strict. The user explicitly accepted
this common family restriction after the broader-input review below.

Recovery evidence supplied by the user: response 0046,
`infinity-codex:01a12a87-a47e-73f1-9351-1159597be30d:01a13b16-fb5a-74a3-93cb-2002064837a5`,
and response 0048,
`infinity-codex:01a12a87-a47e-73f1-9351-1159597be30d:01a13b4a-ff3a-7580-9712-5a40b0ac48fb`.
The interface outline below incorporates the subsequent same-family-type
and explicit-Gray-universe directions, rather than treating those responses
as a final implementation specification.

## Latest reassessment: Pi must retain the default Transf

The user's subsequent clarification requires Pi(E) to remain the default
Transf(const(1),E), rather than selecting a separate lax section operation
while the default Transf becomes strict. Together with the intended ordinary
sections of constant families, this rules out the proposed strict-Transf
default. The alias alone is not inconsistent with strict Transf: it would
instead classify strict sections and change the intended constant-family
meaning. For example, a nonconstant functor (0->1)->B needs a directed
component arrow and is not a strict transformation const(1)=>const(B).

The recommended default is therefore again strict functors with lax
transfors, with the existing selected one-leg convention and with

```text
Hom_Cat(A,B) = Functor_cat(A,B)
Pi_cat(E)   = Transf_cat(const(1),E)
E, I_x      : Functor(K,Cat)
I_x[y]      = Hom_K(x,y).
```

The whole higher constant-family comparison must still be qualified; the
object argument does not prove every current Pi/Functord comparison rule.
In this arrangement Cat_lax is a descriptive name for the public default,
not a required second universe with the same profile. Cat_cart remains a
useful stricter coefficient. The checked Cartesian covariance/represented
Hom owners apply to that restricted coefficient and are retained. They
do not automatically admit every E of the restored default family type.

Common typing of E and I_x does not force every nested Q mapping category
to use the identical higher transformation convention. Named ordinary Hom
constructors may still have their justified stronger computation. The
necessary issue is the action of a variable E on higher base cells.

Write L(A,B)=Functor_cat(A,B) with the selected conventional lax higher
interpretation. The unmodified candidate

```text
Q(A,B) = L(A,L(T(B),Cat))
```

has a local obstruction before composition in Q is involved. The existing
[mixed three-cell review](../emdash2/audits/strict-default-action-boundary/homd_mixed_three_cell_review.md)
uses strict E, strict transports and external FF=id. E maps a base two-cell
to a lax transformation. Combining its coherence with a fibre two-cell
provides kappa:t=>s, whereas the prescribed source-u action into the inner
standard lax mapping category requires s=>t. The reverse is absent in the
finite model. Re-running its unchanged executable on this continuation
confirmed that result and the invertible-input control. This is a scoped
semantic obstruction, not a native Empty derivation or a proof that every
possible lax transformation convention fails.

Latest follow-up: the user explicitly keeps both strict-transfor and
lax-transfor Q alternatives open and asks that feasibility decide between
them. Keep the existing Cartesian native work as the concrete comparison,
without silently changing the common general family input to Cat_cart.
The strict-inner-Q finite model also re-runs successfully: E[alpha] has a
lawful directed noncommuting square, while the proposed strict inner
naturality would identify its distinct boundaries. This is a dimension-two
obstruction for that unchanged action, independently of the dimension-three
obstruction for nested standard lax Homs. Neither is a no-go for every
corrected interface using the respective mapping category.

Consequently compare the two Q options on the required whole source-u
action before further work on general Q composition. The current evidence is:

| Q option | Simpler/working part | Unresolved general-family requirement |
| --- | --- | --- |
| Nested strict-transfor Homs | Cartesian covariance and represented Hom compute for E into Cat_cart. | For general E into the public lax universe, the unchanged u-action asks a noncommuting square to commute. |
| Nested conventional lax-transfor Homs | Retains the directed square and has prior conditional native whole-ladder computations. | Its unchanged higher u-action requires a reverse three-cell in the recorded standard interpretation. |

A transported inner convention is a third correction to assess, not an
exclusive replacement already selected. The linked review uses existing
operations to define

```text
M(A,B) = T(Hom_Cat_oplax(T(A),T(B)))
Q(A,B) = L(A,M(T(B),Cat)).
```

M is a transported oplax mapping category, not a supplied comparison or
equality-proof parameter. Its strict-functor objects have the usual A->B
view through actual transpose/involution operations. At fixed y,v the
closure argument supplies the required T(E[x])->M(T(I),Cat) action, with
I=Hom_K(x,y), without reversing kappa. Its first comparison has the familiar
lax orientation; the higher profile differs. Compatibility with the public
lax coefficient, whole v/y assembly, Q representation/composition and the
x-root are still open. Do not relabel this local argument as a completed
whole Homd or silently replace the default higher profile by M.

The direct ladder remains the objective. Under this candidate its y-component
would be E[y]->M(T(I),Cat); its fixed-v observation uses the canonical
transpose view to expose the same functor T(I)->Cat and the same leaf
`Hom_E[y](E[f](u),v)`. This is an actual duality operation to qualify, not a
path cast or an uncurry over a larger (y,v,f) context.

Q composition is a second issue. A local Hom alias gives no composite of
two profunctors. Ordinary composition integrates over their intermediate
category; right composition with a represented map reduces to reindexing.
The earlier native Q candidate supplied only selected represented/unit
computations, with general coherence explicitly unqualified. Homd can focus
on the represented operations it consumes, but its left comparison and
whole diagram action still need actual operations. Neither this obligation
nor the local mixed-cell obstruction is resolved just by choosing lax
transfors in both nested Homs. The accepted controlled universe carrier
remains a computational option, distinct from either missing construction.

The remainder of this document retains the Cartesian alternative and its
qualified consumers as comparison history. Its strict-default recommendation
and separately selected Pi_lax no longer govern the general milestone.

## Updated priority and the Hom clarification

The user explicitly prioritizes corrected duality/Op over any fixed choice
of strict/lax defaults. Strict ordinary Hom actions are permitted even when
other maps are lax. This supersedes treating the earlier default-lax-transfor
choice as an immutable requirement.

For a strict omega-category C, its usual Hom and composition actions can
have their Cartesian strict profiles. The earlier examples did not require
these ordinary Hom actions to be lax: they used noncommuting higher action
admitted in E, and the attempted interchange of the source-u and Hom-index
parameters. Restricting E's coefficient is a uniform way to remove those
inputs. A different issue is a derived mate or section comparison: it must
not be declared strict solely because the ordinary Hom used to build it is
strict.

In retrospect, the earlier migrations coupled distinct ambitions: admitting
lax transformations, admitting lax ordinary functors, and retaining the old
Cartesian closure/section identifications. They need not have the same
default. A strict Cartesian core with explicit weaker interfaces is a
principled alternative and is now the preferred direction to assess for
the immediate duality repair. This is not a claim that the historical
globally strict kernel, including its old Pi and opposite contracts, was
already correct or can simply be reverted wholesale.

## Core and extension interfaces

The following are proposed meanings, not new installed declarations:

```text
Cat_cat                         Cartesian strict-category universe
Hom_Cat_cat(A,B) = Functor_cat(A,B)
Obj(Functor_cat(A,B)) = Functor(A,B)
Hom_Functor_cat(F,G) = Transf_cat(F,G)

Functor                         strict omega-functor
Transf                          Cartesian strict transformation profile
```

Both ordinary equations can retain their spellings because Functor_cat
itself would now have the Cartesian higher profile. The current separate
Cat_cart/Functor_cart prototype would provide implementation material for
the core rather than forcing users to annotate every foundational family.
Strict here does not mean identity or invertibility of component arrows.

| Interface | Map objects | Higher maps / structure | Role |
| --- | --- | --- | --- |
| Functor_cat(A,B) | Strict functors | Cartesian strict transformations | Default Hom, composition, evaluation and family foundation. |
| GrayHom_lax(A,B) | The same strict functors | Explicit conventional lax higher transformations | Directed transformations and the corresponding Gray closure. |
| GrayHom_oplax(A,B) | The same strict functors | Explicit oplax higher transformations | The other Gray closure where a consumer requires it. |
| LaxFunctor(A,B) | Genuinely lax functors | Separate coherent map/transform profile to qualify | Broader maps, without changing the default core. |

The first three have established strict-omega mapping-category semantics.
A complete mapping-category implementation around the fourth is not supplied
by its name or by the current raw action prototype. LaxFunctor between
strict objects can be developed first; the proposed native weak-object
extension and strict-to-weak inclusion remain future shared design.

This arrangement supports strict functors with lax transformations without
making ordinary functors lax. The standard Gray internal Homs have strict
functor objects, and the Cartesian Hom includes into each of them. See
[Ara--Guetta v1, paragraphs 21 and 33](https://arxiv.org/html/2503.08832v1#S2).

## Latest requirement: the same classifier for E and represented Hom

The user now requires the prototypical family I_x=Hom_K(x,-) and an admitted
variable E to have the same whole family type. For the proposed strict core,

```text
E, I_x : Functor(K,Cat_s)
Cat_s = the proposed Cartesian public Cat_cat
Hom_Cat_s(A,B) = Cart(A,B) = the proposed public Functor_cat(A,B).
```

There is no separate annotation or supplied strictness proof on E. Its
transports and higher family maps have the same Cartesian profile as I_x.
The separate Cat_cart spelling remains an experimental implementation name.
The checked covariance consumer already respects this shared typing.

A weaker view must also be applied to both families through the same whole
inclusion. A canonical Hom can have stronger computational laws than a
variable of the shared type; common typing does not require arbitrary maps
to acquire those constructor-specific laws. Conversely, merely identifying
their object fibres is not enough to meet this requirement.

## Explicit Cat_lax and proposed Homd interface outline

Latest user direction, 2026-10-14: organize the weaker transformations under
an explicit Cat_lax, and keep Gray-specific names out of the foundational
interface. The user also proposes using the existing Cat carrier with its
accepted controlled inconsistency instead of adding a GrayUniverse sort.
The recommended computational presentation to assess is now:

```text
Cat_lax : Cat
Obj(Cat_lax) = Cat
Hom_Cat_lax(A,B) = the strict-functor / lax-transfor mapping category
Obj(Hom_Cat_lax(A,B)) = Functor(A,B).
```

These are proposed interface meanings, not new installed public declarations.
The existing experimental sf_cart_cat and ambient Cat_cat already provide
the respective Cartesian and lax carrier roles. A distinct public universe
sort is not a prerequisite for continuing their computation. Use iterated
Homs of Cat_lax instead of public GrayDiagram/GrayLaxTransf constructors.
LaxTransfor can be a derived readable alias, not an independent default.

There are two different qualifications. Cat:Cat suppresses the size hierarchy.
Treating Cat_lax as an ordinary Cat also exposes it to generic Cartesian
composition, whose existing adverse consumer derives equality of the two
boundaries of an arbitrary lax naturality square. That is an additional
structural compromise, not a consequence resolved merely by size impredicativity.
It does not establish that the retained comparison cell reduces to identity
or that evaluation diverges. Under the user's tolerance for controlled
inconsistency, continue with the native carrier while using the intended
tensor-based composition/evaluation owners and recording this known route.
Do not cite this presentation as a qualified strict Cartesian model of the
lax universe. A separate semantic classifier remains an option if required
by an actual consumer, rather than an immediate universe-hierarchy project.

The whole inclusion j from the strict core into Cat_lax remains required.
Tensor order and lax/oplax convention stay in the implementation/semantic
notes. This first Cat_lax still has strict functor objects. A possible later
Cat_lax_lax with genuinely lax 1-cells is a separate design, not an alias.

For fixed B, write L_K(B)=Hom_Cat_lax(K,B). A section convention
can be specified without a primitive Pi:

```text
Pi_lax(E) = Hom_{L_K(Cat_s)}(const(1),E).
```

This uses the ordinary Hom of the strict omega-category L_K(Cat_s). It
classifies whole lax sections of the Cartesian-valued E. It is distinct
from strict Functord(E,D)=Hom_{Cart(K,Cat_s)}(E,D). Consequently the previous
Pi=Functord(const(1),E) identification cannot remain unconditional. The
constant-family whole comparison must be derived with its actual higher
profile; do not silently equate it with the new Cartesian Cart(K,B).

The direct Homd construction starts with the already checked whole
covariance, writing D=Cart(K,Cat_s):

```text
c_E(x,u) : Hom_D(I_x,E)
C_E,x    : E[x] -> Hom_D(I_x,E)
c_E(x,u)[y][f] = E[f](u).
```

Its intended curried coefficient Hom is

```text
Q(A,B) = Cart(A,Cart(T(B),Cat_s)).
```

For a strict F:A->B, the covariant represented arrow has value
iota(F)[a][b]=Hom_B(b,F[a]). The opposite-direction represented arrow
F^*:B -/-> A has value F^*[b][a]=Hom_B(F[a],b). Applying this second
construction to c_E(x,u)[y] gives the required local body directly.
The existing product-based Prof endpoint convention need not be renamed.
Calling this a represented mate does not make the later general adjunction
library a prerequisite: its canonical observations use Hom action, identities
and composition. Their whole coherence still requires construction.

Here an important qualification remains: this formula defines a local
mapping category, not a complete coefficient universe Q. Joint composition,
unit/coend normalization and higher coherence must be constructed at their
actual strict or Gray structural type. In particular neither Q:Cat nor
Q:GrayUniverse follows from the local alias. A coherent representation
may need more than literal coend composition, whose ordinary associativity
is initially an isomorphism. The outline does not silently import the old
unqualified Q universe.

Conditional on that coefficient/diagram construction, let

```text
S_E(x) = LaxNatCat^Q_K(iota E, iota I_x).
```

In the chosen native carrier presentation this means the iterated Hom

```text
S_E(x) = Hom_{Hom_Cat_lax(K,Q)}(iota E,iota I_x).
```

This makes the proposed type explicit without a new section primitive.
Its coefficient/diagram interpretation is still to be qualified: declaring
Q:Cat under the controlled carrier convention supplies a syntactic carrier,
not a derivation of its intended higher composition or mate coherence.

The proposed direct projection ladder is

```text
homd_id_src_func(E,x)       : T(E[x]) -> S_E(x)
homd_id_src_sec(E,x,u)      : Obj(S_E(x))
homd_id_tgt_func(E,x,u,y)   : E[y] -> Cart(T(Hom_K(x,y)),Cat_s)
homd_id_(E,x,u,y,v)         : T(Hom_K(x,y)) -> Cat_s
homd_id_(E,x,u,y,v)[f]      = Hom_{E[y]}(E[f](u),v).
```

The y projection is the component of the whole transformation in S_E(x),
and v/f are the ordinary curried projections of Q(E[y],I_x[y]). No
combined (y,v,f) base, final uncurry/curry reconstruction, standalone
comparison input or operational equality-proof payload is proposed.
For q:y->z the section retains the directed comparison

```text
iota(I_x[q]) o h_y  =>  h_z o iota(E[q]).
```

This is extracted action of the whole transformation. It is not identity
in general, even though both original families are Cartesian. The terminal
family example below explains why.

For the whole x/u root, the candidate target has fibres H_E[x]=T(S_E(x)).
Its p:x->x' action is induced by composing with the represented arrow
obtained from precomposition I_x'=>I_x. Its higher action must be supplied
by that same whole operation, not by a list of object declarations. The
native-carrier specification to qualify is

```text
H_E : Functor(K,Cat_lax)
homd_id_int(E) : Obj(Hom_{Hom_Cat_lax(K,Cat_lax)}(j E,H_E))
homd_id_int(E)[x] = T(homd_id_src_func(E,x)).
```

Here j is the whole Cartesian-to-lax-universe view. Both the diagram and
transformation types use the same Cat_lax Hom interface; there is no extra
public GrayDiagram/GrayLaxTransf classifier. All-dimensional closure and
the actual canonical higher action remain implementation obligations.
If the canonical H_E and this root admit Cartesian lifts, their stronger
types should be used; that must be derived, not inferred from strict E.
The displayed formula is therefore a root specification to qualify, not
a claim that renaming Cat to Cat_lax finishes x-assembly.

The desired Sigma-Hom comparison retains the objects (f,a) with
`a:E[f](u)->v`. For I=Hom_K(x,y) and H=homd_id_(E,x,u,y,v):T(I)->Cat_s,
the right side is the appropriate contravariant total of H over I. Its
first arrow has alpha:f->g and a fibre arrow `a->H[alpha](b)`. This states
the variance obligation explicitly; it is not permission to pass H to
the current covariant Sigma_cat at an incompatible base. Qualifying the
whole iterated-Hom comparison remains part of the milestone.

The first-cell composition of Sigma for strict E is still
(q,b) o (p,a)=(qp,b o E[q][a]). Full omega-level action, the contravariant
Hom total and their computation must agree. Default strict family maps FF
can then act by actual composition, with relative leaf
`Hom_{E[y]}(E[f](u),FF[y](v))` for FF:D=>E. Explicit weaker FF is a later
extension; it must not re-enter through an untyped coercion.

This outline separates established strict transport from the remaining
coefficient, section and root realization. It does not count a native
carrier declaration as a completed Homd construction or a consistency proof.

## Integration without cloning the whole theory

Share category objects and strict functor objects. In particular,

```text
Obj(GrayHom_lax(A,B)) = Functor(A,B)
LaxTransfor(F,G) = Obj(Hom_GrayHom_lax(F,G)).
```

A strict transformation has a one-way lax view. There is no automatic
conversion of arbitrary lax transformations back to the strict core.
Likewise, a strict functor has a view as a lax functor with identity
compositors; an arbitrary lax functor does not become a strict one.

Reuse object/arrow projections, identities, composition and fixed
whiskering through their shared action machinery and the relevant whole
inclusions. Keep the public default fapp/tapp names for the strict core.
Where the types differ, explicit lax operations can be thin views of a
shared internal action layer rather than copies of Hom, Sigma, Pi and
every downstream theorem. A profile-indexed implementation is one option;
introducing a large generic profile framework before a concrete consumer
needs it is not a prerequisite.

Some extra heads are necessary because the types and lawful equations
differ. “No duplicated theory” cannot mean that an operation has the same
type in incompatible closures. The useful sharing boundary is the generic
action/projection calculus, while each profile owns its actual computation
laws. No operational equality evidence is required of user terms.

The current source already contains LaxTransfor, StrictTransfor, whole
inclusions, selected GrayHom and intrinsic extraction. But its
`lax_transfor : LaxTransfor(F,G) -> Transf(F,G)` currently targets a broader
ambient carrier. If public Transf becomes strict, that view must be retargeted
to an appropriate internal broader carrier or replaced by the explicit
lax projection interface. Leaving it unchanged would allow strict rules
to erase the lax comparison. Reusing the current code means reorganizing
its carrier/owner boundary, not merely changing a label.

Strict default rewrite laws may be unconditional on the public strict
operations. Shared internal owners must still distinguish strict views
from lax ones. The existing native constructor/profile mechanism is usable
for that distinction; it does not require proof arguments in core symbols.

## LaxFunctor and extracted coherence

LaxFunctor should preserve the existing design in which the compositor is
extracted from whole internal action. Its informal observable law is

```text
F[g] ∘ F[f] ⇒ F[gf],
```

with the chosen unit/higher coherence, not a new independently supplied
mu_F cell. Keep strict Hom_C as an ordinary core operation; composition
with a genuinely lax F belongs to an appropriately lax mapping interface.
It must not inherit strict computation simply because its output is
Cat-valued or because the extra F parameter was unbundled.

The current lax implementation is useful source material but is not already
a qualified complete LaxFunctor theory. In particular, the strict-default
pre/right accumulation rule specialized to id_F forces F's composition to
be strict. That rule must not apply unconditionally to LaxFunctor. The
transformation theory between lax functors must account for their retained
compositors as well. These obligations are independent of making ordinary
Hom and ordinary core functors strict.

The first explicit lax layer needed for the duality milestone is therefore
transformations/sections between strict functors. General lax functors and
weak category objects should not become prerequisites for that repair.

## Two foundational uses of laxness must remain explicit

First, restoring strict Transf while retaining
Pi(E)=Transf(const(1),E) would make Pi classify strict sections. Even over
the walking arrow, a nonconstant functor into B is not a strict natural
transformation const(1)=>const(B). Thus the current constant-family section
contract would fail.

Use an explicit section profile if those sections are retained. Moreover,
the whole mapping profile matters: all standard lax higher transformations
between lax sections need not give the Cartesian Functor_cat(K,B) as the
constant-family section category. A proposal that keeps strict maps between
sections should encode that choice too.

A general construction to assess uses Cartesian diagrams into a lax arrow
category, with their endpoint diagrams fixed. For example, with
Gamma_lax(B)=Hom_oplax(D1,B) in the reference tensor convention, objects of
Cart(K,Gamma_lax(B)) with endpoints F,G classify lax transformations F=>G,
while their higher maps have the Cartesian diagram profile. This is a
uniform shape/closure construction, not a primitive Diag_Pi or a list of
equations supplied to each section. Its native endpoint classifier and
bootstrap order still need implementation. The relation between Cartesian
maps into cylinders and Gray transformations is discussed in
[Ara--Guetta v1, paragraphs 21 and 34](https://arxiv.org/html/2503.08832v1#S2).

Second, the currently selected profunctor Homd presentation itself uses a
directed section comparison even for strict E. Ordinary strict Hom does
not make that mate comparison strict.

Here is a small ordinary example, using the convention
Q(A,B)=Cart(A,Cart(T(B),Cat)). Let K=(0->1), x=1 and E be constant at the
terminal category 1. Then

```text
I_x(0)=Empty,   I_x(1)=1.
```

The components of the canonical Homd mate h:iota(E)=>iota(I_x) are
profunctors h_0:1 -/-> Empty and h_1:1 -/-> 1. At q:0->1,

```text
iota(I_x(q)) o h_0      is the empty profunctor 1 -/-> 1,
h_1 o iota(E(q))        is the unit profunctor 1 -/-> 1.
```

The first composite has an empty intermediate index; the second has value
1. The required lax comparison Empty->1 exists, whereas equality does not.
This calculation uses ordinary profunctor composition by coend; see
[Shulman v2, Example 2.6](https://arxiv.org/pdf/0706.1286v2). The example is
our application of that construction, not a theorem about this kernel in
the reference. It rules out simply relabelling this particular Homd
y-section as a strict transformation. It does not refute every possible
strict presentation of dependent Hom.

Consequently an explicit lax section interface may be part of the early
Homd foundation, even with strict core defaults. The canonical transport
map c_E:I_x=>E can still be strict; taking its profunctor mate is the step
where the directed comparison appears. The current work on Cartesian
families and c_E remains relevant to this architecture.

## Cat_lax is not automatically an ordinary strict universe

For fixed strict A,B, GrayHom_lax(A,B) is a strict omega-category. The
collection of categories with these Homs is instead a Gray/skew-Gray
category: its joint composition has directed interchange. Declaring that
collection to be an ordinary Cat and letting generic strict Cartesian
composition apply would revive the existing collapse route.

Therefore Cat_lax must expose its appropriate composition profile or have
a distinct structural classifier. The latest user direction selects that
whole interface as the organizing owner, even when only its local mapping
operations are initially implemented. A complete theory of weak category
objects is still not a prerequisite. The distinction is explicit in
[Ara--Guetta v1, paragraphs 27--29](https://arxiv.org/html/2503.08832v1#S2).

## Recommended sequence and qualifications

1. Reassess the public core as Cartesian: strict Functor and strict Transf,
   retaining their current names and Hom_Cat=Functor_cat. Use the checked
   Cat_cart work as the implementation basis rather than a blanket revert.
2. Specify the explicit Gray-universe interface and its derived section/
   transform operations needed by Pi and the selected profunctor Homd
   construction. Keep E and I_x in the same family classifier. Preserve
   intrinsic action/extraction; do not route lax values through the newly
   strict Functord by an accidental coercion.
3. Finish the corrected T/R/O duality and direct whole Homd ladder under
   this organized boundary. Strictness does not itself repair variance or
   turn higher component arrows into identities.
4. Reconnect explicit Gray operations through shared functor objects and
   the appropriate inclusions. Keep broader LaxFunctor development staged;
   preserve its native action/extraction design without pretending its
   remaining coherence work has already been completed.

This is now a stronger architectural recommendation than preserving lax
Transf as the default at all costs. It preserves expressive lax interfaces
while simplifying the structural core. It still requires Pi/section
reprofiling, Q composition/coherence, native inclusion and projection joins,
and downstream migration. Neither old passing counts nor the new default
choice is a proof of the complete corrected foundation.
