# Intrinsic displayed action: profile boundary after section adoption

Status: active implementation review. The adopted identity-section ladder
passes its existing consumers. This note concerns the next full-source
intrinsic-action owner, not a retraction of those computations.

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

The current generic Cat-valued action comparison identifies M with L for
an arbitrary ambient FF, while the displayed extraction interface promises
`L_p ⇒ R_p`. Under that comparison the ordinary post observation has
endpoints L→L and the mirror pre observation has endpoints R→L. They do
not provide the promised forward comparison. Object equality M=L also
does not make its post leg the identity.

Raw `Op_transf` must not be described as automatically invalid: transpose
swaps the two ambient skew legs. What it does not do is preserve the
conventional lax subprofile; that profile becomes oplax. The qualified
Cartesian reversal owners do not turn arbitrary FF into strict transfors.

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
