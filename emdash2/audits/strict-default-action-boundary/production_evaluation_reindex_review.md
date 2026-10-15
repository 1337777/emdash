# Section evaluation and represented Q reindexing

Date: 2026-10-15
Predecessor: `7dcc1919672657507996ea48106a679a34fe6081`
Status: staged original-source migration through section 17b checks;
remaining Q coherence and public/downstream migration are open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](production_evaluation_reindex_verification.json)

## General section evaluation

The previous source declared

```text
pi_eval_transf(E) : Functord(const(Pi(E)),E).
```

That type is too strong under the selected Cartesian family coefficient.
It requires the evaluation comparison at a base arrow to be strictly
natural in the section variable. Merely forgetting the coefficient to the
ordinary lax-transfor universe does not repair the comparison direction.

For a constant family at B, take sections F,G:K->B and a default lax
eta:F=>G. Its comparison at p:x->y is

```text
G[p] o eta[x]  =>  eta[y] o F[p].
```

The proposed evaluation transformation ev_x=>ev_y, with component F[p]
at F, would instead need

```text
eta[y] o F[p]  =>  G[p] o eta[x].
```

The [finite model](pi_evaluation_profile_model.py) constructs a strict
locally posetal 2-category with exactly a directed square L=>R and no
reverse cell. Its category axioms and horizontal monotonicity are checked.
It admits the first comparison, excludes the reverse, and excludes L=R.
Thus this is a semantic profile correction, not a notation change or an
inference about an arbitrary opaque term. The general distinction between
the two internal Homs and evaluation orders is also explicit in
[Ara–Guetta, paragraph 21](https://arxiv.org/html/2503.08832v1#S2).
The specific counterexample and application to these kernel owners are our
analysis, not a result transferred from that paper.

The [replacement](production_evaluation.lpfragment) keeps all lax sections
in section-first order:

```text
pi_eval_transf(E) : Functor(Pi(E),Pi(E))
pi_eval_transf(E) := id(Pi(E))

Pi(E) ≐ Functord(const(1),E)
pi_eval_transf(E)[s][k](*) = s[k].
```

The historical name is retained, but its type changes. This is the actual
whole Pi-to-section identity view, with no new primitive or projection law.
The source and target both retain the stable Pi head so ordinary identity
computation applies; the existing whole-category comparison supplies the
Functord reading. Using unlike Pi/Functord endpoint heads in the identity
body typechecked but did not compute at the inferred fapp0 call, and was
not retained.

The [controls](production_evaluation_controls.lpfragment) check the whole
next-Hom identity, preservation of arbitrary section morphisms, the original
point evaluation, and the ordinary constant-section F_1 computation. They
reject the former stronger type. This is not an assertion that the old
k-first transformation has been constructed. Any future consumer needing
that order must use an appropriate opposite-profile or tensor evaluator.
The source search finds only the original component diagnostic as an
external direct consumer of this owner; its public diagnostic migration
remains part of the later full-source pass.

Sigma introduction and terminal weakening keep their original declarations
and values, with their admitted-family coefficient tags corrected to
Cat_cart.

## The Q operation actually consumed

Keep the current literal index and coefficient types:

```text
P(C) = T(Functor_cat(C,T(Cat_cart)))
Hom_Q(A,B) = Cart(A,P(B)).
```

For F:A->B, composition with its representation on the right has the
existing object value P o rep(F) = P o F. The
[new whole rule](production_q_reindex.lpfragment) specifies its map as the
actual Cartesian source-reindexing functor

```text
(-) o rep(F) : Cart(B,P(C)) -> Cart(A,P(C))
             = comp_cat_con_cart_func(F).
```

Its whole Hom action and arbitrary map action compute accordingly. The
already-projected unit and constant representations have corresponding
instances. No restriction is put on the inner P(C) maps; the unit case
preserves an arbitrary such component carried by the outer Cart Hom.
An unrelated Q-arrow is not recognized as a representation of F.

For fixed P and varying F, the whole comparison

```text
Q_postcompose(P) o rep_func(A,B)
  ≐ Cart_postcompose(P)
```

is a guarded proof-time unification rule. It checks the actual P and every
endpoint. Its typed comparison passes; replacing P by an unrelated R is
rejected. Removing this unifier fails the same positive consumer. These
are new structural specifications at the whole owners, not theorems
inferred merely from the earlier object law.

The attempted eager runtime fold for this second comparison was rejected:
it broke the inherited Homd y/v/f consumer by leaving an intermediate
P(E[z]) tag on a composition whose actual transport targets E[z]. The
normal-form and failure receipts are retained. The existing Q action stays
the runtime owner, and its established point computations still pass.
The proof-time law does not certify every runtime projection-order overlap.

This qualification is source reindexing, not a construction of general
profunctor composition. It does not introduce equivalence classes, coends,
general left-conjoint evaluation, or strict joint evaluation on P(C).
The remaining mixed coherence, including composition of general lax FF
intrinsic actions, must still be qualified at its actual consumers.

## Original structural owners

The original Const_func_func now has its canonical Cartesian parameter
type B->Cart(A,B), using the already classified Const_transf_func and
Const_transf. It is relocated before its first product-pair telescope
consumer. There is one owner, not a duplicate constant-functor theory.

The Product_pair_tele_func projections now use that Cartesian constant map
and the corresponding Cartesian identity Hom. The larger const_section_func
into Pi(const(A)) remains available with its lax section maps. Their object
values agree; their mapping categories are not identified.

The [constant-map controls](production_constant_map_controls.lpfragment)
check these owners and the actual product telescope projections. The staged
prefix includes all preceding Homd, section, noninvertible higher-action,
Sigma-total and modification controls. The full original tail is retained.
Its first failure is now the old Cat_cat tag in the displayed-weakening
component, section 17c. No production source is promoted by this audit.

## Remaining work

- Continue the original displayed weakening, exchange/contraction and late
  extracted-laxity owners with their correct Cartesian or lax profiles.
- Qualify the remaining Q/mate and general-FF mixed coherence; do not infer
  an unrestricted Cartesian profunctor model from right reindexing.
- Complete the remaining whole duality/inverse consumers, public diagnostics,
  downstream migration, reviewer, catalog, health and CI gates.

No operational equality/proof payload, independent laxity witness, new Pi
constructor, default strictification of FF, or general Q theory is added.
