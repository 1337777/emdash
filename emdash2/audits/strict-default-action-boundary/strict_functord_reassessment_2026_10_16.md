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
