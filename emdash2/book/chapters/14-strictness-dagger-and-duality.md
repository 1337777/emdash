<a id="chapter-14"></a>

# 14. Strictness, Dagger Structure, And Duality

The word *strict* enters category theory by several doors. A HoTT strict
category has a set of objects. An emdash naturality cut is strict when it
selects a runtime normal form. A rewrite is strict in yet another sense when
it is judgmental computation rather than internal equality. None of these
conditions implies either of the others.

The neighboring notion of a dagger illustrates why this vocabulary matters.
A dagger is a *chosen* reversal internal to one category, whereas the
opposite construction reverses any category from the outside. The distinction
is the same one that has guided the book throughout: a generic operation, a
selected structure, and a computational presentation have different owners.

This chapter adapts the strict- and dagger-category discussions of the
[HoTT Book](#ref-hott-book) to the ordinary 1-categorical specialization,
then states the additional coherence a native directed version would need.
Its central checked theorem is opposite duality. The dagger theory is
mathematical development with an explicit implementation boundary.

## 14.1 A Qualified Strictness Vocabulary

The following terms remain separate throughout the book.

| Qualified notion | Meaning | Does not imply |
| --- | --- | --- |
| HoTT strict category | an ordinary precategory whose object type is a set | category univalence |
| HoTT category | an ordinary precategory for which `idtoiso` is an equivalence | that the object type is a set |
| gaunt category | a HoTT category that is also strict | runtime strictness |
| native `IsNCat(n,C)` | recursive finite height of the hom-categories | object identity agrees with isomorphism |
| strict naturality cut | a selected `tapp1` composite reduces to one off-diagonal action | all coherence is judgmental |
| strict public functor | preserves identities and composition through the native action rules; `IsStrictFunctor(F)` records a derived property of its existing compositor | that transformations between functors are strict |
| runtime strictness | an oriented kernel reduction chooses a normal form | object truncation or invertibility |
| dagger category | identity agrees with *unitary* isomorphism | identity agrees with every isomorphism |

In particular, the HoTT phrase *strict category* begins with a
**precategory**, not with a univalent category. Chapter 10’s translation table
uses this definition. A strict precategory may still have nontrivial
automorphisms that cannot come from its proposition-valued object identity.

Public functors are strict by default. The property `IsStrictFunctor`
still describes the compositor extracted from internal action, and canonical
evidence follows from the functor rules; there is no additional admission
through a strict-functor wrapper. Transformations remain conventional lax.
Their strict classifier is useful precisely because strict functors do not
force strictly commuting naturality squares.

<!-- evidence:GRAY-WALKING-INTERCHANGER -->

> **Formal status — checked.** Evidence `GRAY-WALKING-INTERCHANGER` includes
> the selected strict-object/lax-arrow profile and its nonidentity walking-
> square interchanger. The full Crans–Gray monoidal structure remains outside
> the checked boundary.

## 14.2 Strict Categories In Ordinary Univalent Foundations

Let $\mathcal A$ be an ordinary precategory. It is *strict* when
$\operatorname{Obj}(\mathcal A)$ is a set:

$$
\prod_{x,y:\operatorname{Obj}(\mathcal A)}
\operatorname{isProp}(x=y).
$$

This condition says that two proofs of equality between objects agree. It
does not say that every isomorphism comes from equality. For example, the
one-object category associated to a nontrivial group is strict: its object
type is the unit type. It is not a HoTT category, since its nonidentity group
elements are automorphisms while the unique object has only the reflexive
identity path.

A poset on a set-valued carrier gives the contrasting example. Its homs are
propositions and antisymmetry identifies mutual reachability with object
identity, so it is both strict and univalent. More generally, a HoTT category
is strict exactly when it is *gaunt*: its isomorphisms contain no additional
object sameness beyond proposition-valued identity.

Strict categories therefore support a stricter package-level notion of
sameness than categorical equivalence. Equality of their presentations agrees
with isomorphism of the corresponding precategory structures, whereas an
equivalence can still change a presentation by choosing merely equivalent
objects. This can be useful, but it is not the default notion of sameness in
univalent category theory.

<!-- evidence:UCAT-STRICT-CATEGORY -->

> **Formal status — mathematical development.** Evidence
> `UCAT-STRICT-CATEGORY`. The definition and the gauntness comparison belong
> to ordinary univalent 1-category theory. They are not a definition of
> native `Cat` or a theorem about arbitrary finite-dimensional native
> categories.

## 14.3 Three Native Notions That Strict Categories Do Not Control

Finite directed height is the first separate notion. A witness

$$
\operatorname{IsNCat}(n,C)
$$

recurses through native hom-categories. At dimension one it says that every
hom-category is discrete and entails that the object classifier is a
1-type. HoTT strictness instead asks directly that the object classifier be a
set. Neither condition supplies a native identity-to-isomorphism theorem.

The second notion is strict naturality. For the stable view of a classified
strict transfor $\eta:F\Rightarrow G$, the off-diagonal action has two reductions

$$
\begin{aligned}
G[g]\circ\eta[f]&\rightsquigarrow\eta[g\circ f],\\
\eta[f]\circ F[h]&\rightsquigarrow\eta[f\circ h].
\end{aligned}
$$

The phrase *strict transfor* in this book describes this selected two-sided
cut behavior; it is not a new classifier of categories. Ambient ordinary and
displayed transfors retain the post/left directed comparison. Pre/right
computation is the conventional lax default, not an extra functor assumption.

The third notion is runtime strictness itself. The arrow
$t\rightsquigarrow u$ records a chosen normal form in the Lambdapi theory.
An internal equality $t=u$, a proof-time comparison, and a free-form
mathematical equation have different force. A category can have
proposition-valued object identity while none of its interesting operations
compute, or support rich directed higher cells while selected naturality cuts
do compute.

<!-- evidence:CAT-DIMENSION -->
<!-- evidence:TRANSF-STRICT-NATURALITY -->

> **Formal status — checked.** Evidence `CAT-DIMENSION` and
> `TRANSF-STRICT-NATURALITY`. The active theory separately checks recursive
> dimension/object truncation and the two profiled `tapp1` naturality
> reductions. No checked theorem identifies these interfaces.

## 14.4 Dualities At Different Dimensions

An opposite operation must specify which dimensions it reverses. Write

$$
T(C)=\mathsf{Op}(C),\qquad
R(C)=\mathsf{CoAbove2}(C),\qquad
O(C)=R(T(C)).
$$

| Operation | Reversed dimensions | Native owner |
| --- | --- | --- |
| $T$ | dimension 1 only | `Op_cat` |
| $R$ | dimensions 2, 3, … | `CoAbove2_cat` |
| $O$ | every positive dimension | `TotalOp_cat` |
| $C_2$ | dimension 2 only | `CoAt2_cat` |

All preserve the object carrier. Their Hom projections explain the difference:

$$
\begin{aligned}
\operatorname{Hom}_{T(C)}(x,y)&=\operatorname{Hom}_C(y,x),\\
\operatorname{Hom}_{R(C)}(x,y)&=O(\operatorname{Hom}_C(x,y)),\\
\operatorname{Hom}_{O(C)}(x,y)&=O(\operatorname{Hom}_C(y,x)).
\end{aligned}
$$

Thus ordinary Hom uses $T(C)$ in its contravariant object slot. Replacing it
by $O(C)$ would also reverse the higher cells in that slot. For an ordinary
one-category the distinction disappears, since its Homs are discrete. It
cannot be suppressed for a general native category.

These operations are involutive. Their actions on functors retain the same
specified dimensions, but their actions on transformations have different
profiles. Fibre transpose uses strict transformations; total opposite acts
on ordinary lax transformations as well. For example, if $\eta:F\Rightarrow G$,
total duality gives

$$
O(\eta):O(G)\Rightarrow O(F):O(A)\to O(B).
$$

The reversal includes the higher naturality cell. It is not obtained by
reversing component arrows while leaving that cell untouched.

For a family $E:K\to\mathsf{Cat}_{\mathrm{cart}}$, the corresponding whole
fibre operations also change the base:

$$
T_{\mathrm{fib}}(E):C_2(K)\to\mathsf{Cat}_{\mathrm{cart}},\qquad
O_{\mathrm{fib}}(E):R(K)\to\mathsf{Cat}_{\mathrm{cart}}.
$$

Their fibres are respectively $T(E[x])$ and $O(E[x])$. The shifted bases
record the action on transformations between transports, not a change of
fibre objects. Chapter 2 uses total fibre duality in the Sigma–Hom formula.

The native adjunction operation uses total opposite. It sends

$$
F\dashv G:A\rightleftarrows B
\qquad\text{to}\qquad
O(G)\dashv O(F):O(B)\rightleftarrows O(A).
$$

The new unit is the total opposite of the old counit, and conversely.
Applying the operation twice computes back to the original package.

<!-- evidence:OP-DUALITY -->

> **Formal status — checked.** Evidence `OP-DUALITY`. `Op_transf` uses the
> Cartesian transformation profile; `TotalOp_transf` acts on ordinary
> transfors. Despite its retained name, `Op_adjunction` uses `TotalOp_cat`,
> `TotalOp_func`, and `TotalOp_transf`. These are distinct contracts, not
> alternative spellings of one unrestricted opposite.

## 14.5 Dagger Structure Is Chosen Self-Duality

An ordinary †-precategory is a precategory $\mathcal A$ equipped with an
operation

$$
(-)^\dagger:
\operatorname{Hom}_{\mathcal A}(x,y)
\longrightarrow
\operatorname{Hom}_{\mathcal A}(y,x)
$$

satisfying

$$
\begin{aligned}
(\mathrm{id}_x)^\dagger&=\mathrm{id}_x,\\
(g\circ f)^\dagger&=f^\dagger\circ g^\dagger,\\
(f^\dagger)^\dagger&=f.
\end{aligned}
$$

Equivalently, it is an identity-on-objects functor-like map

$$
D:\mathcal A^{\mathrm{op}}\longrightarrow\mathcal A
$$

with a chosen involution law. The word *chosen* is essential. The opposite
construction gives $\mathcal A^{\mathrm{op}}$ for every $\mathcal A$; it
does not give a functor from that opposite back to $\mathcal A$, much less
one that fixes objects and squares to the identity.

## 14.6 Unitary Arrows And Dagger Univalence

An arrow $f:x\to y$ is *unitary* when its dagger is its two-sided inverse:

$$
f^\dagger\circ f=\mathrm{id}_x,
\qquad
f\circ f^\dagger=\mathrm{id}_y.
$$

Every unitary arrow is an isomorphism, but an isomorphism need not be unitary.
Object identity always produces a unitary isomorphism by identity induction,
so there is a canonical map

$$
\operatorname{idtoUnitary}_{\mathcal A}:
(x=y)\longrightarrow(x\cong_\dagger y).
$$

A †-category is a †-precategory for which this map is an equivalence. Its
selected notion of object sameness is unitary isomorphism, not arbitrary
isomorphism.

Two examples separate the notions. In a groupoid, define
$f^\dagger=f^{-1}$; then every arrow is unitary. For finite-dimensional inner
product spaces with arbitrary linear maps, the dagger is the adjoint linear
map. The unitary isomorphisms are the isometries, while many invertible linear
maps are not unitary. Thus this †-category need not be a HoTT category under
ordinary isomorphism.

<!-- evidence:UCAT-DAGGER-CATEGORY -->

> **Formal status — mathematical development.** Evidence
> `UCAT-DAGGER-CATEGORY`. This is the ordinary set-valued-hom theory:
> dagger laws are equalities, unitarity is a property, and dagger univalence
> compares object identity with unitary isomorphism.

## 14.7 Opposite, Duality, And Dagger Compared

The three reversal notions have different input data.

| Construction | Data supplied | Result |
| --- | --- | --- |
| opposite | any category $C$ | a category $C^{\mathrm{op}}$ with arrows reversed |
| categorical duality | a chosen equivalence $C^{\mathrm{op}}\simeq D$ | a comparison between two categories |
| dagger | a chosen identity-on-objects involutive map $C^{\mathrm{op}}\to C$ | a unitary notion internal to $C$ |

A native dagger must first specify which duality is intended. The following
list uses $T(C)$ as the object-direction opposite; a total dagger would use
$O(C)$ instead and require the corresponding higher action. At minimum it
would require:

1. a functor $D:C^{\mathrm{op}}\to C$;
2. identity-on-objects data, with an explicit decision about whether it
   computes or is witnessed coherently;
3. an involution comparison between $D\circ D^{\mathrm{op}}$ and
   $\mathrm{id}_C$;
4. compatibility of that comparison with off-diagonal and higher action;
5. a unitary-arrow classifier whose evidence is stable under identity,
   composition, and the next hom action;
6. a qualified identity-to-unitary-equivalence interface.

The ordinary equations above are a plausible strict specialization of this
design, not a license to erase the higher coherence. In particular,
neither `Op_cat` nor `TotalOp_cat` supplies a chosen map back into $C$.
Neither operation is a native dagger by itself.

<!-- evidence:NATIVE-DAGGER-INTERFACE -->

> **Formal status — research boundary.** Evidence
> `NATIVE-DAGGER-INTERFACE`. No dagger/unitary owner is active. Side task
> `FTTX-S12` remains a specification target, and this chapter does not add
> a prose-only kernel name or infer dagger structure from opposite duality.

## 14.8 Duality As A Proof Method

Opposite duality becomes useful when a theorem has already exposed its
variance. A right adjoint preserves weighted limits because a representable
comparison can be transported through its hom adjunction. Passing to
opposites exchanges:

$$
\begin{aligned}
\text{right adjoint}&\longleftrightarrow\text{left adjoint},\\
\text{weighted limit}&\longleftrightarrow\text{weighted colimit},\\
\text{unit}&\longleftrightarrow\text{counit},\\
\text{upper-star source action}&\longleftrightarrow
  \text{lower-star target action}.
\end{aligned}
$$

Chapter 17 uses dimension-one transpose and product-swap profunctor duality
on the whole Hom comparison. This preserves its weighted-colimit contract
without constructing an opposite adjunction with new unit and counit
profiles. The separate `Op_adjunction` package uses total opposite.
A dagger could internalize a particular self-dual instance of such an
argument, but the general theorem needs only opposite duality. This is why the
book includes dagger structure for conceptual completeness without making it
the foundation of categorical duality.
