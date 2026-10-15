# Homd index action: the Cartesian restriction is too strong

Date: 2026-10-15
Status: necessary profile correction identified; derived candidate checked;
whole Q/Homd integration remains open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Predecessor: `e594bcea5e37c825dc92cd90df53f3b4a277ad5c`

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

This is not yet installed in the staged Q. The Cartesian fibre-variable
profile, default strict functors, default conventional lax transformations,
and E:K→Cat_cart are retained. The existing direct ladder and represented
operations must be transported to this weaker index view and requalified.
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

1. Recover the concrete index-arrow action F[α], with its direction and
   noncollapse, from the existing internal action/extraction owners.
2. Integrate P into Q, its represented inclusion/conjoint/mate operations,
   and the complete direct identity/relative x/u/y/v/f ladder.
3. Adapt the existing tdapp1_int/fdapp1_int projection owners. Do not add an
   independent laxity cell. Retain the negative-total direction in Sigma/Pi.
4. Correct the old unconditional left-transport=middle equation: the
   selected default makes the right/pre route strict, retaining the left/post
   comparison. Update its actual consumers, without strictifying arbitrary FF.
5. Qualify the consumed whole coherence and downstream migration before
   public promotion. The original later source remains present.

The [verification record](production_homd_index_verification.json) pins the
passing source and finite model. The candidate adds no warning bodies or
rules. The full staged kernel is unchanged from the predecessor and still
stops at its old intrinsic declaration. Earlier ladder checks remain evidence
for that stated computational contract, not for the now-refuted general
intrinsic extension of all-Cart Q.
