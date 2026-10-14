# Strict Cartesian core with explicit lax interfaces

Date: 2026-10-14
Status: recommended architecture to assess under the user's reopened defaults;
not a completed public migration
Plan: [foundations goal](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Previous comparison: [design matrix](EMDASH_FOUNDATION_PROFILE_DESIGN_MATRIX.md)

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

Therefore a future Cat_lax must expose its appropriate composition profile
or have a distinct structural classifier. It need not be implemented as a
complete second universe merely to use GrayHom_lax, lax transformations,
and Gray tensor operations locally. This avoids making a general weak-
category implementation a prerequisite. The distinction is explicit in
[Ara--Guetta v1, paragraphs 27--29](https://arxiv.org/html/2503.08832v1#S2).

## Recommended sequence and qualifications

1. Reassess the public core as Cartesian: strict Functor and strict Transf,
   retaining their current names and Hom_Cat=Functor_cat. Use the checked
   Cat_cart work as the implementation basis rather than a blanket revert.
2. Specify the minimal explicit lax section/transform interface required
   by Pi and the selected profunctor Homd construction. Keep intrinsic
   action/extraction available there; do not route lax values through the
   newly strict Functord by an accidental coercion.
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
