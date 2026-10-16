# Strict versus lax displayed maps after the native Homd implementation

Date: 2026-10-16
Status: design assessment only; retain the selected lax Functord default
Owner: [living foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Scope and recommendation

The user requested a fresh assessment, not another migration. Keep ordinary
Functor strict, ordinary Transf conventional lax, and the admitted family
coefficient Cat_cart. The variable under comparison is whether public
Functord(E,D) admits lax or only strict transformations across the base K.
Strictness of the fibre functors FF[y] is already part of both alternatives.

User clarification later on 2026-10-16: the relevant question is which
actual FF producers and consumers need lax admission, not the expressivity
of arbitrary lax transformations in isolation. The focused inventory and
coherence-scope correction below refine the recommendation. They do not
change the selected classifier or claim downstream migration is complete.

Strict Functord is a feasible alternative classifier and simplifies the
external displayed-map action. It is not established to simplify the full
migration while retaining the current sections and ordinary laxity
extraction. The current route now has working whole identity/relative Homd,
two-map intrinsic composition, classified strict specialization, and a
passing whole-unit candidate. Continue that route. Keep the strict option
available if a remaining obstruction specifically requires nonidentity
FF-naturality; do not infer such an obstruction from a normalization failure
that already occurs for FF=id.

## Evidence that changes the earlier assessment

The [historical classifier comparison](strict_displayed_maps_review.md)
already constructed a whole family-category inclusion, strict displayed-map
objects and retained ambient modifications, with no operational equality
argument. It is bounded evidence at its recorded donor snapshot; it is not
a completed strict-default migration of today's Cat_cart source.

In the current authoring source,
[homd_id_int](production_homd_core.lpfragment) has a Cartesian diagram-map
type. Thus the earlier concern that reinterpreting Functord would necessarily
reject the outer identity root is no longer applicable to this selected
root. Its whole y-section is still an ordinary lax Q-valued transformation;
these are different positions in the ladder.

The current [classified intrinsic computation](production_cartesian_intrinsic.lpfragment)
already gives, for a strict displayed map U and its ordinary view FF:

```text
D[p] o FF[x] = FF[y] o E[p]
Phi_FF(p,u,v) = (FF[y])_1(E[p](u),v)
lambda_FF(p,u) = id_(FF[y](E[p](u))).
```

The whole intrinsic modification need not be identity: its Hom functor can
still be the nontrivial Hom action of FF[y]. Strictness removes the
naturality comparison, not the map's mathematical content.

Conversely, the [current lax two-map construction](production_intrinsic_composite_review.md)
has actual whole and higher-action consumers. The latest unit investigation
encountered displayed/ordinary category presentations and rigid Hom heads
already at an identity displayed map. Restricting all FF to strict maps
would not remove that particular computational issue.

## What semantic expressivity lax Functord adds

For the same fixed admitted E,D:K->Cat_cart, lax FF adds coherent directed
comparison data

```text
lambda_FF(p):D[p] o FF[x] => FF[y] o E[p].
```

Strict FF requires the corresponding strict naturality equality; its
extracted comparison is identity. This is more than alternative syntax for
identical data: arbitrary noninvertible comparisons are lost from that
particular map classifier.

The distinction already appears with ordinary categories. Take K to be
the walking arrow and E=const(A), D=const(B). A lax displayed map consists
of F0,F1:A->B and an ordinary natural transformation theta:F0=>F1. A strict
displayed map only admits the case F0=F1 with the identity comparison.
For A=1, a lax displayed map can therefore contain any arrow b0->b1 of B;
a strict one requires the constant, identity-arrow case. Even identical
component functors can carry a nonidentity comparison loop in the lax
classifier.

This permits directed variation to be internalized in the base while the
fibres and their functors remain strict. The current Pi and intrinsic
laxity constructions exploit exactly that admission. Compatible total-map
and section-postcomposition operations can consume the same comparison
bearing FF when their selected profiles have been qualified.

There is a crucial distinction between expressivity of this interface and
expressivity of the entire theory. If ambient lax Transf and its operations
remain available, strict Functord does not make these data inexpressible:
they live in that ambient classifier instead. What is lost is automatic
admission to operations whose domain has been restricted to Functord. Such
operations need an ambient version or an inclusion-based shared definition
if the same behavior is to remain available.

Thus lax FF is not mathematically necessary for the FF-free identity Homd
or its strict-map specialization. It is useful for the uniform inclusion of
transport-comparison-bearing maps and for retaining the existing binding
and internalization interfaces. The recommendation to retain lax Functord
is not a claim that a strict-Functord foundation with ambient lax Transf
would be intrinsically less expressive overall.

## Strict maps see base arrows

The constant-family example above isolates the additional data admitted by
laxness; it is not a representative usefulness test for strict displayed
maps. For the walking arrow p:0->1, a strict FF:E=>D has a square

```text
E[0] --FF[0]--> D[0]
 | E[p]          | D[p]
 v               v
E[1] --FF[1]--> D[1]

D[p] o FF[0] = FF[1] o E[p].
```

The arrow p imposes this equation. Over the discrete two-object base the
equation is absent and the two components can be chosen independently.
For constant diagrams the equation becomes FF[0]=FF[1], with that common
functor still arbitrary; it does not require the functor to be an identity.
For nonconstant diagrams even the component domains and codomains can
differ. Strict naturality is exact compatibility with transport, not absence
of dependence on the base.

A canonical example in this kernel is fib_cov_transf(E,x,u). For a strict
admitted family it sends f:x->y to `E[f](u)`, and its naturality along p:y->z
is `E[p](E[f](u))=E[pf](u)`. This is nontrivial base transport and is strict.
The staged [FibCov owner](production_homd_core.lpfragment) already places
this map in the Cartesian diagram Hom before its ambient inclusion.

Likewise, for a strict F:A->B, fapp1_at_transf(F,x) sends f:x->y to F[f].
Its strict naturality is F[p] o F[f]=F[pf]. These are useful examples of
strict displayed maps directly involved in the existing dependent theory.

## Inventory of the FFs actually consumed

This is a source review of the original core and direct active extension
call sites, together with the selected staged authoring fragments at
checkpoint d64e31a0. It is not an exhaustive transitive semantic audit of
every library theorem, and a generic Functord binder is not itself evidence
that a concrete construction needs nonidentity comparison cells.

| Producer / consumer | What FF is | Does this use need lax FF? |
| --- | --- | --- |
| Core Hom(Sigma), recursive triangle/simplex Homs, [homdc_int](../../emdash3_2_cubical_internalization.lp), [terminal profunctor normalization](../../emdash3_2_prof_reindex_terminal_normalization.lp) | id_funcd(E) | No. These are identity Homd consumers. The surrounding families and higher cells can still be nontrivial. |
| [pathout_map_func](../../emdash3_2_dependent_simplex_native_dimensions.lp) | fapp1_at_transf(F,x) | Strict F makes this naturality strict. This consumer does not require arbitrary lax FF in the new defaults. Full migrated higher-classifier admission remains an implementation check. |
| [Represented element totalization](../../emdash3_2_commutative_algebra_presheaves.lp) and native path induction | fib_cov_transf(E,x,u) | Strictness suffices for the admitted strict E. The staged owner already has the Cartesian map profile. |
| [Slice Sigma/postcomposition](../../emdash3_2_pullbacks.lp) | hom_con_int_postcomp_func(id,f) | Canonical Hom postcomposition is compatible with the selected strict Hom action. This is not evidence for arbitrary lax FF. |
| [Direct cover glue](../../emdash3_2_direct_cover_completion_hit.lp) | direct_cover_completion_glue_funcd | The producer explicitly supplies direct_cover_completion_glue_is_strict : IsStrictFunctord(...). Its substitution comparison is required to be strict. The existing evidence interface is not automatically a new classifier admission or a judgmental computation. |
| Core piapp1_func, section_total_func and section_weaken_funcd | A section s:const(1)=>E, or its weakening | General sections genuinely use nonidentity base action. Pi may remain on ambient lax Transf under the proposed strict public Functord split, but these existing extractor call sites must then take that ambient input. |
| Core tapp1_post_laxity_transf and [pathout_transf_target_func](../../emdash3_2_pathout_transformation_lift.lp) | tapp1_at_transf(epsilon,x) for an ordinary lax epsilon | General epsilon requires lax admission here. At the represented identity the displayed comparison recovers epsilon's retained post/left naturality. Restricting this FF would restrict epsilon or require an ambient extraction route. The selected strict pre/right leg does not erase the post/left cell. |
| [DependentTriangleImage_catd / dependent_triangle_map](../../emdash3_2_dependent_simplex_bridge.lp) | An arbitrary caller FF | The general statement includes lax maps. Its strict specialization remains mathematically useful; the generic declaration alone does not show non-strict FF is necessary for triangle formation. |
| [shaped_unit_fixed_funcd](../../emdash3_2_shaped_pathout.lp) | Restriction of an arbitrary shaped Prof_hom cell | It inherits the supplied cell's profile. Preserving the unrestricted API needs the ambient route; necessity of laxness for each special application is not established by this binder. |
| General Sigma-map/base-change/comma comparisons | Arbitrary FF, or canonical projection/reframing maps | Generic contracts promise their admitted map class. Canonical projection/reframing profiles need individual migration; do not classify all of them as necessarily lax from their present Functord spelling. |

One inspection correction matters: finding a use of functord_laxity_transf
in the direct-cover module initially suggested a laxness consumer. Reading
its producer shows that the same cell is explicitly required to be strict.
The producer's contract, rather than the extractor's name, determines the
semantic requirement.

For the genuine ordinary-transformation consumer, write
FF_y(f)=epsilon_y o F[f] in the selected conventional-lax convention. Its
comparison along p:y->z is the whiskering of

```text
G[p] o epsilon_y => epsilon_z o F[p].
```

At f=id_y this is the original naturality cell. Making all these FF strict
would therefore make that cell identity. This is a specific dependency of
the current extraction architecture, not a generic expressivity argument.

Consequently, restricting the extra argument of the relative public Homd
would preserve the identity and canonical strict consumers listed above.
It would not preserve every existing shared extractor consumer without a
selective ambient interface. Keeping ambient lax Transf and Pi can preserve
those data, as the user already proposed; one must migrate the actual
extraction and totalization call sites too. The current defined relative
Homd body can be shared through the inclusion, rather than introducing a
second primitive ladder. No such classifier migration is performed here.

For strict FF, the computation remains meaningful:

```text
Phi_FF(p,u,v)[a] = FF[y][a]
lambda_FF(p,u) = id.
```

The fibre functor and its higher Hom action are not identities in general.
The earlier composition-of-lax-FF question is therefore a real optional
interface-design tradeoff, not a choice between useful and useless maps.

User clarification on resumption: because identity Homd is separate, an
ambient lax consumer need not call the public relative alias at all. For
FF:D=>E it can use Homd_target_map(FF) o homd_id_int(E), together with the
intrinsic action required by that consumer. This is the same construction
underlying the alias, not a need for a second primitive Homd ladder.
Homd_target_map has the corrected parameter variance; arbitrary plain
composition with FF in every slot is not being asserted. The target action
and intrinsic comparisons must still be qualified for their ambient inputs.

In particular, tapp1_at_transf(epsilon,x) for a genuinely lax epsilon should
land in ambient lax Transf. There is no independent mathematical reason
that it must inhabit an eventual strict Functord classifier. A future split
can classify exact transport-preserving maps in Functord and comparison-
bearing maps in ambient Transf, keeping Pi ambient. The word "displayed"
alone does not select either profile: the intended preservation contract
does. In the ordinary strict-diagram case, the former preserves chosen
total transport arrows exactly; the latter need not. Extending that
description to all higher total-map operations still requires their actual
profile qualification. Continue the current lax-Functord implementation
while it remains feasible; retain this separation as an explicit alternative.

Further clarification: this alternative can reuse the generic existing
StrictTransfor(K,U,E,D) classifier and strict_transfor inclusion, where U is
the admitted coefficient (currently Cat_cart). It does not require another
bespoke strict-displayed-map grammar. At the object-classifier level one can
use a specialization/alias Functord_s(E,D)=StrictTransfor(K,U,E,D).
Reusing the public name Functord would be a separate API decision. Defining
its entire Hom category still requires choosing between ambient higher
transformations on strict map objects and the fully Cartesian mapping
profile, which restricts higher structure too. The staged Cartesian Hom
already has StrictTransfor as its arrow classifier. The older separate
StrictFunctord property/carrier in the pre-migration profile extension is
historical implementation input, not a requirement to duplicate this generic
classifier. No meaning of public Functord is changed in this tranche.

## Coherence work required by the migration

The phrase "broader Q coherence" in recent status reports was too broad as
a blanket prerequisite. The plan already limits Q to structural operations
consumed by Homd/Sigma and explicitly defers a general profunctor model.
Restore that distinction:

- Native declarations need correct whole types, their projection ladder,
  retained higher action, and computation at the required original consumers.
- Installed rewrite rules need their relevant identity/composition and
  projection overlaps checked. The two-map intrinsic rule overlaps with the
  literal identity rule: the completed whole-unit checks address a concrete
  computational interaction. They are not a request for caller coherence
  proofs or a new semantic library.
- Triple associativity of the expanded intrinsic body is a bounded pending
  compatibility audit of that composition rule and the existing proof-time
  associativity views. It is not a requirement to derive arbitrary omega
  coherence before continuing the later original owners. Proof-time
  equality need not normalize in both directions; a failed typed-reflexivity
  presentation is not by itself a semantic counterexample or a runtime
  critical-pair failure. No computational contradiction has been established.
- Every further Q/mate/index computation must name the actual rule overlap
  or original consumer that requires it. A full profunctor/coend model,
  arbitrary balancing laws and general higher coherence are library/model
  developments, not implicit prerequisites to this migration.

Post-d64 associativity probes remain ignored and unpromoted. Independent
triple roots typecheck and the displayed map arguments compare; the current
failure is comparing their expanded relative-root presentations. Broad
composition-congruence attempts broke otherwise valid endomorphism
associativity, so they must not be added just to make this extra comparison
pass. Resume migration of the existing Op_prof and fdapp1_projection_target
owners; revisit the bounded comparison at its actual dependency or before
claiming the corresponding whole computation qualified. The outstanding
source failures and public/downstream gates remain explicit.

This continuation changes documentation and priority only. It installs no
new Lambdapi rule and performs no new checker probe.

## A clean selective classifier

The existing Functord/Transf comparison cannot remain an equality after
restricting Functord. Nor can the whole Catd_cat(K)/Functor_cat(K,Cat_cart)
comparison remain unchanged if their arrows differ. A coherent selective
interface is schematically:

```text
Obj(Catd_s(K)) = Functor(K,Cat_cart)
Hom_Catd_s(E,D) = Functord_s_cat(E,D)
Obj(Functord_s_cat(E,D)) = StrictTransfor(K,Cat_cart,E,D)

j_K : Catd_s(K) -> Functor_cat(K,Cat_cart)
j_K[E] = E
j_K,1(U) = strict_transfor(U).
```

These are explanatory names, not newly installed declarations. The inclusion
is an operation on a classified input, not a path/naturality proof supplied
alongside that input. Generic fapp/tapp operations are shared.

There are two distinct choices for higher cells:

- Restrict FF objects and retain ambient modifications between their views,
  as in the historical comparison.
- Use the fully Cartesian mapping category Cart(K,Cat_cart), restricting
  higher transformation structure as well.

The second can reuse the present Cart interface directly but is stronger
than merely making FF strict. The first has native classifier evidence but
still needs its full higher consumer closure. Individual strict-FF Op and
Sigma computations do not certify the whole higher operations for either
choice.

The identity core and its defined relative composition can be reused. There
is no implementation reason to reintroduce a second primitive blended Homd
just because strict inputs permit more reductions.

## The section boundary is substantive

Current source identifies

```text
Pi(E) ~ Functord_cat(const(1),E)
      ~ Transf_cat(K,Cat_cart,const(1),E),
Pi(const(B)) ~ Functor_cat(K,B).
```

The current object and Hom projections also use Functord and Transfd, so
changing one comparison alone is insufficient.

For K the walking arrow and q:b0->b1 a nonidentity arrow of B, the ordinary
strict functor F:K->B is a section of the constant family B. Its section
action is q. A strict transformation const(1)=>const(B) instead requires
its two chosen objects to agree and its naturality component to be identity.
It cannot represent this arbitrary F. This is a semantic distinction, not
an inconvenience of Lambdapi notation.

The preferable strict-Functord alternative therefore keeps Pi on the
ambient default Transf side:

```text
Pi(E) ~ Transf_cat(K,Cat_cart,const(1),E).
```

Its old equality with strict Functord, its object projection, its Hom
projection and their consumers would be migrated. The public name Pi need
not change, and no primitive second Pi is needed. Making Pi strict instead
would change constant-section semantics and abandon a current requirement.

The [constant-section reviewer](production_section_action_controls.lpfragment)
also retains F[alpha] for a noninvertible base two-cell. Restricting public
FF cannot discard that behavior while retaining the current section theory.

## Ordinary laxity still has an ambient displayed consumer

The original required kernel tail defines tapp1_post_laxity_transf by
feeding tapp1_at_transf into functord_laxity_transf, and the latter extracts
its data from fdapp1_int_transfd. The pre/right construction uses
the contravariant internalization, whose selected strict leg must be treated
separately. In particular, the retained post/left internalization of a
general ordinary lax transformation cannot automatically be admitted as a
strict displayed map.

After a strict public Functord split, this machinery must therefore continue
to accept ambient Transf(K,Cat_cart,E,D), directly or through an explicit
lax displayed alias. Keeping the current raw implementation underneath a
strict facade is possible and shares most code. It also means the full lax
intrinsic problem has moved to the ambient interface, rather than vanished.
No standalone comparison witness is needed or recommended.

## Comparison for the full migration

| Concern | Current lax Functord | Strict Functord with ambient inclusion |
| --- | --- | --- |
| External FF filler action | Retains and composes lambda_FF; whole two-map action checked | Reduces to the component Hom functor; current strict specialization already checks |
| External Sigma-map computation | Retains intrinsic comparison data for admitted families | Point action simplifies to (p,FF[y][alpha]); full higher profile still matters |
| Identity Homd and corrected duality | Implemented staged ladder; coherence/integration still open | Can reuse the same identity root; variance and Q/mate work remain |
| Pi and arbitrary constant sections | Uses current shared Functord/Transf presentation | Must use ambient Transf and migrate the old Functord/Transfd projections |
| Ordinary laxity extraction | Uses the same displayed interface | Requires ambient lax inputs despite the stricter public classifier |
| Coefficient P(I), inclusion M_I | Needed by present whole intrinsic/section consumers | Not automatically removable while those ambient consumers remain |
| Whole unit/associativity computation | Includes actual comparison data and facade normalization | Less external cell algebra, but identity/facade issues survive |
| Remaining repository work | Continue a substantially exercised route | Feasible selective refactor; additional classifier separation and downstream audit, not yet qualified |

Thus strict Functord is simpler for a restricted external API. It is not
currently demonstrated to be a faster or simpler completion of the full
preserved foundation. No new strict-alternative code probe or public
classifier change was performed for this reassessment.

## Interacting laxness levels and rewriting

The user's intuition is useful as an engineering explanation. A lax functor
F contributes a compositor mu_F(g,f):F[g] o F[f]=>F[gf]. A lax transformation
eta:F=>G contributes naturality cells whose coherence also involves mu_F
and mu_G. Taking F and G strict removes those compositor terms while
retaining eta's directed naturality data. The coefficient Cat_cart separately
controls the naturality of the transformations occurring inside a family.

This is not a theorem that a logical framework with one conversion relation
can express only one categorical layer. Lambdapi has dependent types and
user-defined rewriting; higher cells can be typed data at arbitrarily
iterated Homs. See the [official description](https://lambdapi.readthedocs.io/en/latest/about.html).
The assessment here is that selecting which laws compute by conversion,
while retaining the other comparisons as cells, is the essential design
problem. More modes or named/scoped conversion relations could improve its
organization, but do not by themselves make an arbitrary noninvertible
compositor an identity. Existing classifiers and guarded rules already
provide a form of that separation without operational proof inputs.

Ara–Guetta v1 explicitly works with strict omega-categories and strict
functors while studying oplax/Gray functoriality of comma and Grothendieck
constructions. Its stated motivation concerns those constructions and their
homotopical applications. Our explanation in terms of reducing interacting
coherence and Lambdapi normalization is an implementation interpretation,
not their stated rewriting-framework rationale. Source:
[Lax functorialities of the comma construction for omega-categories, introduction](https://arxiv.org/html/2503.08832v1).
