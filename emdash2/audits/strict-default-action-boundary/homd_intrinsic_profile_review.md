# Intrinsic displayed action: profile boundary after section adoption

Status: active semantic review. The adopted identity-section ladder passes
its existing consumers under the stronger Cartesian coefficient prototype.
That is conditional comparison evidence, not qualification of the requested
public universe. This note also records the Cat-valued strictness review.

## Two meanings of laxity must remain distinct

Write

```text
L_p = D[p] ∘ FF[x]
R_p = FF[y] ∘ E[p]
M_p = tapp1(FF,p).
```

The ambient transfor machinery retains two skew legs, `L_p ⇒ M_p` and
`R_p ⇒ M_p`. The admitted conventional lax profile is
`IsLaxTransfor = IsPreStrictTransfor`; its pre/right leg is identity and
M=R. The conventional oplax profile is
`IsOplaxTransfor = IsPostStrictTransfor`; its post/left leg is identity and
M=L. These are different from full strict naturality. See the profile
owners in [emdash3_2_gray_profiles.lp](../../emdash3_2_gray_profiles.lp).

The pre-scope prototype's generic Cat-valued action comparison identified M
with L for an arbitrary ambient FF, while the displayed extraction interface promises
`L_p ⇒ R_p`. Under that comparison the ordinary post observation has
endpoints L→L and the mirror pre observation has endpoints R→L. They do
not provide the promised forward comparison. Object equality M=L also
does not make its post leg the identity.

The two-skew observation about raw `Op_transf` is that transpose swaps its
two legs. At the level of a conventional two-dimensional naturality square,
this exchanges the lax and oplax readings. Neither observation certifies
the same statement for standard Gray transformations in all dimensions;
the distinction below matters. The qualified Cartesian reversal owners do
not turn arbitrary FF into strict transfors.

## Why the checked Op_funcd takes a strict transfor

The production source still has the legacy general-FF declaration. The
selected [Cartesian opposite fragment](displayed_op_cartesian.lpfragment)
instead implements the action of `Op_catd_func` on strict transformations:

```text
Op_funcd : StrictTransfor_K,Cat(E,D)
       → Functord_C2(K)(T_fib(E),T_fib(D)).
```

This is the qualified profile of that operator, not a restriction of public
`Functord` or `homd_int(FF)`. Under the conventional normal-lax reading,
fibrewise dimension-one transpose changes

```text
D[p] ∘ FF[x] ⇒ FF[y] ∘ E[p]
```

into the oppositely oriented comparison

```text
T(FF[y]) ∘ T(E[p]) ⇒ T(D[p]) ∘ T(FF[x]).
```

Strict naturality avoids this orientation problem. It is a sufficient
checked input profile, not a proof that no broader replacement exists.
At omega level, calling the replacement "oplax" is not itself enough:
dimension-one transpose is neither monoidal nor anti-monoidal for the
standard Gray tensor. The usual odd, even and total dualities have different
compatibilities; see [Ara--Guetta v1, paragraphs 35–38](https://arxiv.org/html/2503.08832v1).
In particular, the two-dimensional reversed square does not justify a
general omega-level T-operation on Gray lax/oplax transfors. The current
raw two-skew interface is also not thereby identified with a standard Gray
internal Hom. A replacement intrinsic target must qualify its entire
profile and higher action, rather than borrowing either identification.

## Reassessment of global strictness at codomain Cat

The user's 2026-10-14 suggestion is a candidate to assess, not an instruction
to install the rule. A `Cat_cat` codomain guard reaches ordinary functors
through the existing constant-family section identification:

```text
Transf_{K,Cat}(const(1),const(B)) ≃ Functor_cat(K,B).
```

The actual source implements this through `Functord_cat`/`Pi_cat` comparison
rules, constant-family component evaluation, and
`terminal_fdapp1_int_cell_eq`. For F:K→B viewed as such a transformation,
its component at x selects F[x], and its intrinsic displayed comparison at
p:x→y is F[p]. Both family transports are identity functors.

Full strict naturality of this Cat-valued transformation would identify the
two point functors selecting F[x] and F[y]. Evaluating at the terminal object
then gives F[x]=F[y]; making the comparison strict also collapses F[p] to
the corresponding identity. Take K and B to be walking arrows and F their
identity functor: it has distinct endpoints and a nonidentity arrow. This
is an ordinary strict-functor example requiring no Op, Q, lax transports or
weak-category construction.

The finite checker now enumerates this example: three functors K→B, but
only two strict transformations const(1)⇒const(B). The nonconstant functor
is excluded by the proposed global strictness. This is a mathematical
countermodel to the combined contracts, not a newly installed kernel rule.

Thus globally strictifying `Transf(K,Cat,E,D)` while preserving the existing
section calculus is not a local repair of FF. Restricting the spelling to
`Functord` does not avoid the example. Keeping the rule would require changing
which transformation class defines Pi, hence the foundational interface.
Also distinguish strictness of FF from strict naturality of one of its
comparison transformations in a fibre: the latter may have nonidentity
components and is a different condition.

Strict sections are a legitimate alternative meaning for Pi, so this is not
an argument that Pi must always use lax transformations. With strictly
natural higher maps and ordinary K,B, strict sections of const(B) form one
copy of B per connected component of K, rather than Functor(K,B). Choosing
that semantics would retire the third comparison and require migrating its
consumers. A lax section classifier is needed only if the existing all-section
meaning is retained after the default Cat-valued transformations change.

No codomain-only strictness rule has been installed. The following checks
show that reassessing Pi is necessary but not sufficient to preserve ordinary
lax internal action under that exception.

## Cat-valued internalization detects ordinary laxness

For arbitrary F:A->B, the current represented Hom owner has type and action

```text
H = hom_(F,F[x]) : A -> Cat
H[y] = Hom_B(F[x],F[y])
H[p](a) = F[p] o a.
```

If all Cat-valued functors were strict, H[qp]=H[q]oH[p]. Apply this to
id_F[x] to obtain F[qp]=F[q]oF[p]. Thus a blanket Cat-valued-functor exception
does not preserve arbitrary lax F with this unchanged Hom contract.
Writing H as the composite Hom_B(F[x],-) o F rather than blending F into
the head makes no semantic difference. This conclusion concerns the
composition equation, not automatic identity of every retained compositor.

The [finite checker](homd_intrinsic_profile_countermodel.py) realizes the
failure with a one-object strict 2-category whose endomorphism category is
the monoidal poset 0<1, tensor max, unit 0. A normal-lax F from [2] sends
the two generating arrows to 0 and their composite to 1, with comparison
0->1. H[q]oH[p] acts as [0,1], whereas H[qp] acts as [1,1]. The mismatch is
already detected at identity 0; no opposite, Pi, Sigma or Q appears.

For transformations, the existing whole ordinary internalization is

```text
tapp1_at_transf(epsilon,x)
  : Transf_{A,Cat}(Hom_A(x,-), Hom_B(F[x],G[-]))

tapp1_at_transf(epsilon,x)[g][f] = epsilon[gf].
```

Strictness of this Cat-valued transformation forces
G[g] o epsilon[f] = epsilon[gf]. Its fixed-target mirror supplies the
corresponding other-side equality. Together these are incompatible with
retaining the general noncommuting lax square of epsilon.

The [mixed-family checker](mixed_family_profile_models.py) uses strict
walking-arrow functors H,J and a normal-lax epsilon with

```text
left  = J[p] o epsilon[0]
right = epsilon[1] o H[p]
left => right, but left and right are distinct.
```

The prescribed fixed-source internalization at 0 selects epsilon[0] and
right; its target-family action sends epsilon[0] to left. It is not strictly
natural. This is independent of Pi and is already a two-dimensional example.
It rejects retaining both the exception and those internalization contracts;
it does not reject a redesigned genuinely lax/mixed internal classifier.

Reusing the same square as E[alpha] gives a conditional Homd obstruction.
Although E and its transports may be strict, a base 2-cell can still be sent
to a lax transformation between transports. If the inner presheaf mapping
category in the proposed curried Homd has only strict Cat-valued transfors,
the prescribed source-u action would require equality of left and right
when tested at a fixed target and its identity. The checker confirms their
inequality. This is a statement about that specific curried target and
projections; it is not a no-go result for corrected mixed/dual targets.

## Local family restriction versus the selected uniform default

Making E strict controls base composition. Making the 1-cells of its
coefficient strict controls E[p]. With ambient lax defaults these are
independent: a strict family over the walking arrow can have any ambient
functor F as its sole nonidentity transport.

A separate coefficient with strict functors and lax transfors could enforce
the second condition locally, with a strict family classifier enforcing the
first. The existing StrictFunctor_cat is a possible input to that design,
not an implementation of its complete coefficient universe. Its higher
composition must still respect the chosen Gray-style profiles. No path or
equality argument need be passed to Homd operations merely to express the
family's input type.

The user now explicitly requires one universe, Hom_Cat(A,B)=Functor_cat(A,B),
and Homd admission for every E:K->Cat. Under those requirements and the
retained strict-transport Homd/Sigma contract, the walking-arrow example
forces every F to be strict. Consequently the restricted-coefficient option
is outside the selected solution, and the global strict-functor migration
remains selected. This implication does not make Cat-valued transformations
strict; their naturality and the native internalization above remain a
separate design question.

## The old whole target fails even for conventional lax FF

The old [internal displayed-action owner](../../emdash3_2.lp) tries to
form an ordinary-lax whole target with fixed-x component

```text
B_x = homd_src_func(GG,x) ∘ T(FF[x]).
```

This component is a lawful whole functor. Its assembly as the asserted
ordinary-lax transformation across x is not generally lawful.

Take K to be the walking arrow 0→1. Let E be the constant strict family at
the discrete category {u,v}, and D the constant strict family at the poset
a→b. Take FF's strict component functors to be

```text
FF[0](u)=a,  FF[1](u)=b
FF[0](v)=a,  FF[1](v)=a.
```

The normal-lax comparison has components a→b and id_a. It is natural, and
the walking base has no composable pair of nonidentity arrows. Set GG=FF;
the input modification can therefore be its identity.

At outer x=0→1, evaluate at y=1 and the second object v. The hom-index
map `Hom_K(1,1)→Hom_K(0,1)` is the unique isomorphism between terminal
categories, so target-section transport preserves this local value. The
two required values are

```text
B_0(u)[1][v][p]     = Hom_D(a,a) = 1
B_1(E[p](u))[1][v][id_1] = Hom_D(b,a) = Empty.
```

An ordinary-lax x comparison would give a functor 1→Empty. Thus this target
cannot carry the asserted forward ordinary-lax x-action. Identity
specialization of the input modification does not repair that profile.
This is not a refutation of the bare raw `Functord` type: the ambient
carrier is two-skew, and these local endpoints allow an oplax choice with
apex 1 and legs `1→1←Empty`. Nor does this local choice build the complete
omega-level target. In contrast, the actual forward laxity a→b exists:
its extraction evaluates at `v=E[p](u)=u`, a different consumer.

The reversed Empty→1 component exists. That observation supports reviewing
an oplax whole target; it does not construct or qualify an omega-level
oplax package.

## Raw skew data cannot supply a forward comparison either

A separate ordinary example uses the fork a→c←b. Constant source 1 and
constant target this poset permit component functors selecting a and b,
with off-diagonal value c. Both skew legs exist, but no arrow a→b does.
Consequently those two legs alone do not construct a forward
`functord_laxity_transf`. The same example rejects imposing M=L on all
such independently specified skew data. This fork is not a model of every
operation of the repository's raw `Transf` carrier; further internal-action
and closure contracts may constrain its inhabitants. It does not by itself
justify narrowing all raw FF inputs to a conventional subprofile.

The [finite checker](homd_intrinsic_profile_countermodel.py) validates both
examples using thin categories and enumerates all nine normal-lax pairs
in the first example; two fail the proposed whole target, and none of the
four strict pairs does. It is independent semantic evidence, not a
Lambdapi inconsistency proof or an admission theorem for the old encoding.

## Existing wrappers do not provide an independent extractor

`tapp1_post_laxity_*` and `tapp1_pre_laxity_*` call
`functord_laxity_transf`, which uses `fdapp1_int_transfd` through the
self-comma identity section. The Gray graph/interchanger constructions
consume those ordinary laxity functions. `Prof_cell_apply` and
`Prof_transf_cat` use the same Functord interface. Reusing these as the
seed of displayed extraction would retain its dependency cycle.

The current profile extension admits `LaxTransfor`, its view, and its
higher category. It explicitly defers the corresponding oplax package,
view and mirror Gray Hom. No admitted oplax displayed-map classifier or
pseudo/opposite-profile view of the current Homd root is available.
Objectwise agreement does not supply an inverse of its coherence.

## Bounded repairs and remaining scope decision

Preserve the raw relative `homd_int(FF)` interface: its defined target-side
composition does not itself promise forward laxity for every raw FF.
Do not make all displayed maps fully strict.

First isolate the unqualified M=L comparison from the already checked
identity ladder. The `homd_root_action_scope` experiment removes that
comparison for arbitrary FF and retains only the identity Homd constructor's
selected source-action instance. Its old x-action assertions are positive
consumers; arbitrary FF source-action equality is a negative consumer.
This does not identify either skew leg with an identity.

The following profile route remains a candidate, not a selected narrowing
of the public intrinsic-action domain:

1. Give the canonical Homd root the proper whole oplax/post-strict profile,
   with an actual raw view and the already checked section components.
   Selecting a correctly profiled canonical constructor is different from
   deriving a reverse cell for the former independent raw root. Do not
   postulate inverses of arbitrary FF.
2. Investigate forward intrinsic displayed extraction for the conventional
   normal-lax/pre-strict profile. This still includes noninvertible a→b;
   it is not full strict naturality. Raw relative Homd remains available
   more generally. This is an informative subcase, not a replacement for
   the goal's general-FF obligation. Settle the full raw carrier's actual
   internal-action contract before deciding whether its extraction needs a
   corrected target or an explicit input profile. Further higher-profile
   conditions must be qualified, not inferred from this two-dimensional example.
3. Package `B_x` as a whole oplax target and type the intrinsic modification
   in the corresponding higher mapping category. Preserve identity
   specialization and evaluation at the transported identity, so forward
   laxity remains extracted from whole internal action, not a supplied cell.
4. Replace the unqualified generic M=L comparison with justified profile
   or canonical-constructor cases. Normal-lax and oplax projections must
   retain their different directions. The fixed-source ordinary internal
   action's proposed normal-lax view needs its own whole qualification;
   its point formula alone is insufficient.

These are pending interfaces, not implemented carriers or completed
theorems. Exact native types and higher action remain to be established.
No fresh `lambda_FF` witness, operational equality argument, automatic
strictifier, or circular Sigma action/extraction is selected.

Before full-source integration, update both section 15 and the late
`fdapp1_projection_target`, not only the first failing declaration. The
corrected Homd bases are C2(K), and the section targets are the native
`Homd_section_cat` types. The previous same-profile `Op_funcd(raw FF)`
cannot be restored as a shortcut.
