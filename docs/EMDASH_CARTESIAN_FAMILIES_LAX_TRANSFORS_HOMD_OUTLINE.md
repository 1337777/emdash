# Cartesian families, lax sections and corrected dependent Hom

Date: 2026-10-14
Status: selected next candidate under the user's latest constraints;
strict-root/relative ladders and intrinsic identity projection checked;
nonidentity y-coherence and Sigma-Hom open
Owner: [living foundations plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Comparison history: [default/profile review](EMDASH_STRICT_CORE_LAX_EXTENSIONS_REVIEW.md)

## Constraints retained together

The default remains strict functors with conventional lax transfors. Pi is
the default terminal-source transformation category. Both an admitted family
E and its prototypical represented family I_x=Hom_K(x,-) land in the same
Cartesian coefficient universe Cat_cart. Q uses Cartesian mapping categories
in this leading comparison. The lax-Q alternative remains comparison evidence.

There is no global strict-Transf default, Cat-valued strictness exception,
separate Pi_lax replacing Pi, operational proof argument, or standalone
supplied laxity cell. Public foundational names use universes and ordinary
Hom operations; tensor-specific terminology stays in implementation notes.

Standing scope constraint from the user: only the represented Q operations
consumed by Homd are prerequisites. Do not make a complete general profunctor
library, arbitrary coend theory or a new universe hierarchy a prerequisite.
The existing uncurried Prof convention need not be globally renamed.

## Universes, families and sections

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
Q/mate laws. It is not a derivation of complete Q coherence, the extracted
lax y-comparison or Sigma-Hom, and is not yet a public kernel migration.

## Sigma and relative maps

The desired Hom of Sigma retains objects (f,a), with f:x->y and
`a:E[f](u)->v`. Its whole category must be the correctly oriented total
of the fixed-v presheaf in the ladder; a source/target reversal is not
licensed merely by equality of object carriers. Strict E gives the
first-arrow composition `(q,b) o (p,a)=(qp,b o E[q][a])`; the iterated-Hom
comparison and its higher action remain to be implemented.

A general FF:Functord(D,E) can remain lax across K. Its component functors
are strict and its base-comparison transformations are strict in the fibre
variables because the coefficient is Cat_cart. This addresses the earlier
fibre-square obstruction without assuming FF is strict across K. Actual
Sigma-map coherence and relative Homd action still require their consumers.
The accepted identity-core/defined-relative interface remains available;
there is no reason to introduce a second primitive Homd theory for FF.

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
