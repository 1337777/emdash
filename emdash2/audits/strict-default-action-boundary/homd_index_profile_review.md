# Homd index action: the Cartesian restriction is too strong

Date: 2026-10-15
Status: directed index and general intrinsic projections check; the actual
constant-section F[alpha] computation passes; full coefficient qualification open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Predecessor: `e594bcea5e37c825dc92cd90df53f3b4a277ad5c`

Current continuation after `95d73ac6`: the corrected ordinary Pi index,
general tdapp1 ladder and whole constant-family specialization now check.
The derived C_I,H constructor uses B_I on an actual ordinary functor;
applying A_I computes its whole total-opposite functor. Feeding it F_1 in
the native constant-family case makes the decoded piapp1 action reduce to
F_1, and both that action and the Sigma total retain F[alpha]. The
[section-action review](production_section_action_review.md) distinguishes
this new whole structural compatibility from the old point-only law and
records the remaining evaluation/Q coherence gates.

Continuation after `36fceea2`: Hom_Q(A,B)=Cart(A,P(B)) is now installed in
the staged native owner. The identity/relative direct ladders and the
identity-specialized intrinsic root-to-filler projections check. The expanded
negative-Sigma action independently recovers the same structured arrow as
the capped Sigma-map rule. See the
[current verification](production_intrinsic_verification.json). The full
source then advanced to the old `piapp1_func` section type. The current
continuation above supersedes that constant-action and projection boundary;
consumed Q coherence still needs qualification.

The coefficient view of ordinary curried Hom now has a stable owner with
projections to its explicit M_I-composition body. Unfolding that body inside
represented Q patterns did not compute reliably. Its proof-time whole
comparison checks the actual inclusion; an arbitrary M is rejected. This is
a source-normalization repair, not an operational equality argument. The
displayed component migration also exposes the actual Cartesian fibre Hom,
while retaining lax FF across K and P's directed index transformations.

The convention question does not require changing the default. Reversing
which leg is strict would reverse the first comparison, but also turn the
positive constant-section arrow s[x]->s[y] into s[y]->s[x] along x->y.
It would therefore move the opposite-profile requirement to the retained
Pi(Const B) interface. Keep the negative-index presentation local. In this
presentation homd_tgt_func lands in P; fixed-v homd_ is its T(I)->Cat_cart
view. M_I is internal to canonical constructions and is not a user parameter.

## The concrete consumer

The preceding checkpoint implements the direct identity and defined relative
Homd ladders in a staged copy of the original source. Its coefficient Hom is

```text
Hom_Q(A,B) = Cart(A,Cart(T(B),Cat_cart)).
```

Those computations do not establish the still-unimplemented general
intrinsic action. That consumer now refutes the inner Cartesian restriction.
This is a semantic obstruction, not a Lambdapi normalization failure.

Take the strict walking 2-cell K, with distinct p,q:x→y and a noninvertible
α:p⇒q. Write I=Hom_K(x,y), the walking arrow p→q. Constant families are
admitted Cat_cart-valued families. By the retained constant-section
interface, the strict functor F=id_K gives an allowed terminal-source
displayed map between constant families. Its intrinsic Hom action must
retain the strict functor

```text
F₁ : I → I,
F₁[p]=p, F₁[q]=q, F₁[α]=α.
```

At the relevant fixed endpoints, the old Q profile asks for this action as
a strict transformation

```text
const(1) ⇒ const(I)  in Cart(T(I),Cat_cart).
```

Strict naturality along α in T(I) would identify its two component point
functors, hence p=q. The desired action does not have this type. Neither
strict outer families nor strict transports remove this example: both
families here are constant. Restricting all FF to strict transformations
would instead exclude the section representing this ordinary F and would
require a different section interface. It is not the selected repair.

Simply replacing the inner Cart with default Functor_cat(T(I),Cat_cart)
also fails this example's direction. Default lax naturality over T(I)
requires η_q→η_p; the desired action gives η_p→η_q. The
[finite model](homd_index_profile_model.py) enumerates all pairs of objects
of I: Cartesian admits (p,p),(q,q); default lax over T(I) additionally
admits (q,p); the required negative-index profile instead admits (p,q).
This is a complete finite necessary-condition calculation, not an ω-model.

## Derived candidate, without a new action calculus

Use T=`Op_cat`, R=`CoAbove2_cat`, O=`TotalOp_cat`. The
[candidate definitions](production_homd_index.lpfragment) contain no new
primitive, rewrite rule or unification rule:

```text
P(I) = T(Functor_cat(I,T(Cat_cart))).
```

An object H is a strict functor I→T(Cat_cart). Its whole fixed-object
presheaf view is T_func(H):T(I)→Cat_cart. An arrow in P(I) carries the
required first comparison direction. This is the literal derived category;
no equivalence with the usual full ω-category of oplax transformations is
asserted. The standard ω-level lax/oplax dualities use odd/even reversal,
whereas total reversal preserves the mapping profile; dimension-one
transpose alone must not be substituted for those results
([Ara–Guetta, §2](https://arxiv.org/html/2503.08832v1#S2)).

The proposed replacement is limited to the inner index classifier:

```text
Hom_Q(A,B) = Cart(A,P(B)).
```

This is installed by the continuation described above. The Cartesian
fibre-variable profile, default strict functors, default conventional lax
transformations, and E:K→Cat_cart are retained. The direct ladder and
represented operations now use this view; their remaining higher coherence
and section consumers still need qualification.
No general profunctor-composition theory is added as a prerequisite.

There is a derived whole inclusion

```text
M_I : Cart(T(I),Cat_cart) → P(I).
```

Its body transposes a Cartesian mapping category and uses the existing
Cart-to-default mapping inclusion. The fixed-object presheaf view recovers
H after M_I, and M_I recovers every object after that view. These object
round trips are checked; they do not make the view a functor from P(I)
into the old Cartesian mapping category. Its arrow type is weaker.

The same definitions give

```text
A_I : R(P(I)) → Catd_cat(O(I)),
A_I[H][p] = O(H[p]),

B_I : Catd_cat(O(I)) → R(P(I)),

N_I : P(I) → Cat,
N_I = total_op ∘ R_func(Sigma_func(O(I)) ∘ A_I).
```

A_I uses the existing total-op mapping action followed by postcomposition
with total_op_cart. B_I is the corresponding explicit return composite;
no whole inverse or coherence theorem for A_I,B_I is claimed. N_I uses one
existing Sigma and whole duality, rather than declaring another total.
Its formation remains conditional on those existing structural contracts.
At `95d73ac6`, B_I remained diagnostic support. The current C_I,H constructor
now gives it a concrete core consumer. The constant computation is checked;
a general inverse/coherence theorem for A_I,B_I is not claimed.

The direction is also forced by negative-total arrows. For κ:p→q and
an arrow `a→H[κ](b)`, a map U needs

```text
U_p ∘ H[κ] ⇒ H′[κ] ∘ U_q.
```

The ordinary default lax mapping category over T(I) supplies the reverse.
This is why a mere spelling change from Cart to Functor_cat is insufficient.

## Checked scope and next implementation

The [native controls](production_homd_index_controls.lpfragment) check M_I,
both object round trips, the components of included Cartesian arrows, the
fibre of A_I and the whole object expression for N_I. Applying B_I to the
existing constant-section presentation of O_func(F) gives an actual arrow
in P(I). Its component at p, evaluated at the terminal object, computes to
F[p]. Its endpoints are the actual images under B_I of the constant
families; canonical whole constant-endpoint identifications are not assumed.
A raw P(I) arrow is rejected as an arrow in the old Cartesian presheaf Hom.

Still required:

1. Qualify the remaining whole coefficient and parameter coherence beyond
   the now-checked fixed-F index action and its noncollapse.
2. Qualify the remaining consumed Q coherence beyond the checked native
   represented operations and identity/relative x/u/y/v/f computations.
3. Continue the whole extracted-laxity and late consumers from the now-checked
   nonidentity tdapp1_int projections. Do not add an independent laxity cell.
   Retain the negative-total direction in Sigma/Pi.
4. Migrate the consumers of the retired unconditional left-transport=middle
   equation. The native owner now uses the selected right/pre equality,
   retaining the left/post comparison and general lax FF.
5. Qualify the consumed whole coherence and downstream migration before
   public promotion. The original later source remains present.

The [initial verification record](production_homd_index_verification.json)
pins the passing source and finite model at `36fceea2`. That index-only
checkpoint added no warning bodies or rules and left the full staged kernel
at its old intrinsic declaration. The continuation and its changed warning
scope are recorded above. Earlier ladder checks remain evidence
for that stated computational contract, not for the now-refuted general
intrinsic extension of all-Cart Q.
