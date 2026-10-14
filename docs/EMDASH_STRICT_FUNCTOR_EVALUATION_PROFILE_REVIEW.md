# Strict defaults require an evaluation-profile migration

Date: 2026-10-11
Status: operation obstruction checked; public Hom(Cat)=Functor_cat and lax Q selected; earlier Cartesian-universe/Q prototypes retained as comparison evidence
Owner: [strict-functor/duality plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [native audit](../emdash2/audits/strict-default-action-boundary/README.md)

User correction, 2026-10-14: the public `Cat_cat` must retain strict default
functors with non-strict transfors, hence `Hom_cat Cat_cat A B` remains
`Functor_cat A B`. The Cartesian-universe replacement below was a stronger
contract, not the agreed migration target. Its measurements and mathematical
counterchecks are retained. They show that unchanged strict Cartesian
evaluation/composition needs correction; they do not authorize solving that
problem by restricting the public universe or adding strict-transfor profile
arguments to foundational operations. Read all earlier "selected" language
below under this later boundary and the living plan's current contract.

Further clarification on the same date: Q itself must retain conventional
lax transformations at both mapping levels. The selected curried target is
`Hom_Q(A,B)=Functor_cat(A,Functor_cat(T(B),Cat))`. Use Gray closure when an
uncurried consumer is needed; the direct Homd telescope can remain curried.
The earlier nested-Cart Q below is a comparison implementation, not the
selected target. Its product-based composition/curry code cannot be copied
unchanged into lax Q. The
[current consumer review](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md#lax-q-gray-uncurry-and-strict-sigma-maps-consumer-review-2026-10-14)
also assesses strict-only Sigma maps without restricting public Functord.

## The stronger check

The first pilot's three conversion negatives do not establish preservation
of general lax transfors. A native check constructs actual equality paths
between their naturality routes using only the restored capped strict
functor-composition law and the existing Cartesian evaluator:

```text
Eval : Functor_cat(A,B) × A → B
Eval[(ε,p)] = ε[p].
```

For arbitrary `ε:F⇒G` and `p:x→y`, factor `(ε,p)` in the product in its two
orders. Strictness of Eval then supplies

```text
G[p] ∘ ε[x] = ε[p]
ε[y] ∘ F[p] = ε[p].
```

The first equality composed with the inverse of the second gives an
equality between both boundary composites. The audit defines all three
paths for variable F, G, ε and p. It uses no Op, directed Sigma-Hom formula,
independent compositor or supplied naturality proof. An equality is stronger
than the directed, potentially noninvertible comparison allowed for a
general lax transfor. The test does not prove that the particular extracted
laxity cell itself is an identity.

This is a profile mismatch in the migration, not a reason to abandon strict
default functors. Cartesian internal Hom uses strict higher transformations;
the Gray internal Homs support lax/oplax higher transformations. Ara–Guetta
separates these constructions in paragraphs 18–21.
[Primary source, arXiv:2503.08832v1](https://arxiv.org/html/2503.08832v1).

## Native interface pilot

### Why the earlier kernel had only one mapping category

Historical source inspection on 2026-10-12 confirms that the pre-migration
kernel used `Hom_cat(Cat,A,B)=Functor_cat(A,B)` and Cartesian evaluation on
`Functor_cat(A,B) × A`, while also installing global strict-naturality rules
for arbitrary ordinary and Cat-valued transfors. Commit `55f91cc7` removed
the ordinary post/left and corresponding Cat-valued component rules;
`c1c9fbcf` removed the remaining pre/right rules. The absence of a separate
Cartesian mapping category in that prototype therefore does not establish
that its operations respected genuinely non-strict transfors.

The selected combination now keeps strict functor objects but permits lax
transfors in Functor_cat. Functor_cart_cat shares those same objects and
restricts its higher cells to the Cartesian strict-transfor profile. The
distinction is required by evaluation/composition before the Q/profunctor
or duality construction uses it. It adds no duplicate fapp action or second
default functor carrier. Fixed evaluation and fixed whiskering still admit
lax transfors, and Functord itself is not globally made strictly natural.

An additional native countercheck now rules out fixing only joint Eval.
Inserted before Eval/curry are declared, it uses Cartesian composition in
Cat, constant transformations and fixed-object evaluation to derive the same
two endpoint equalities. The capped strict-default variant passes; removing
the strictness clause or the Cat composition-component projection rejects
the relevant proof. See the
[coefficient replay and exact evidence](../emdash2/audits/strict-default-action-boundary/README.md#coefficient-countercheck-before-evaluation).
Thus some correction to the coefficient/composition profile is necessary
if strict Cat objects and the existing generic composition architecture are
retained. This does not prove that every broader profile redesign is needed.

Keep the default functor objects and ordinary `fapp*` operations. A distinct
whole category records the stricter transformation profile:

```text
Functor_cart_cat(A,B) : Cat
Obj(Functor_cart_cat(A,B)) ↝ Functor(A,B)
Obj(Hom_{Functor_cart_cat(A,B)}(F,G)) ↝ StrictTransfor(F,G)

cart_include : Functor_cart_cat(A,B) → Functor_cat(A,B)
cart_include[F] ↝ F
cart_include[ε] ↝ strict_transfor(ε).
```

Its higher Hom is not identified with the ambient modification category.
The whole inclusion retains an iterable Hom action, checked on a variable
higher cell. This does not yet give a complete introduction/computation
theory at all levels.

The coefficient profile has

```text
Cat_cart : Cat
Obj(Cat_cart) ↝ Obj(Cat_cat)
Hom_{Cat_cart}(A,B) ↝ Functor_cart_cat(A,B).
```

For variable `E:K→Cat_cart`, the checker reads `E[p]` as a default functor
and the image of a base 2-cell as a strict transfor between transports.
No equality/path or separately supplied comparison is input. Nonidentity
components are still allowed: strict naturality is distinct from being
the identity transformation.

Cartesian and lax evaluation then have different profiles:

```text
Eval_cart : Functor_cart_cat(A,B) × A → B
gray_evaluation_R_func(A,B)
  : GrayTensor_R(GrayHom_lax(A,B),A) → B.
```

The pilot checks the Cartesian projections and rejects the actual raw-
transfor call. The Gray owner already exists with its recorded bounded
qualification. Reusing it does not introduce a new weak-category theory,
functor resolution, or application-nerve task.

## Whiskering is not a blanket strict-transfor requirement

For a lax transfor `alpha:F=>G`, fixed post-whiskering by a strict H and
pre-whiskering by a strict J preserve lax transfors. Their comparison cells
come from applying H to alpha's cells or reindexing those cells along J.
Strict functoriality of these operations, as maps of the relevant mapping
categories, does not say their transfor-valued outputs have strict
naturality. Parameterized whiskering must also respect its actual lax/oplax
orientation; it cannot be recovered by identifying Cartesian and lax Homs.

The baseline nucleus already has named strict computations. In particular,
`fdapp1_int_cell` and `fdapp1_int_hom_fapp0` specialize directly on
`hom_int_precomp_func(id,...)`, with the selected identity arguments, to the
identity at the composite arrow. These rules do not ask for a
`StrictTransfor` wrapper. This is narrower than a theorem that every Homd
transformation is strict. The later profile migration explicitly retired
arbitrary-transfor post/left, pre/right and displayed component-naturality
cuts; those are not restored by the strict-functor goal.

The ongoing migration retains both mechanisms: justified computation on a
known structural head, and a classifier for variables ranging over strict
transformations when an operation needs that restriction. No operational
equality proof is added to a Hom/Homd action. The classifier's declaration
placement is an ownership choice, not an extra strictness premise on every
default functor.

Evaluation at a fixed object `ev_x:[A,B]_lax -> B` remains available on lax
transfors. The profile correction is needed when both the functor and its
argument vary in a Cartesian product. That is the checked collapse route
above, not an objection to fixed evaluation or fixed whiskering.

## The two Cartesian levels of the earlier Q prototype

Clarification requested by the user on 2026-10-14. The prototype uses

```text
Hom_Q(A,B) = Cart(A,Cart(T(B),Cat)).
```

This is the Cartesian curried view of a product profunctor with the existing
endpoints swapped. It was an additional coefficient restriction, not part
of the user's intended Q design. Strict default functors alone do not make
all transfors strict.
The restrictions support the retained Cartesian evaluation, parameterized
composition and product/curry comparison.

The two occurrences have distinct effects. For an object
`P:A→Cart(T(B),Cat)`, the inner Cart makes the action on an arrow of A a
strict transformation in the B variable. Replacing that inner Cart by the
ambient lax mapping category can change the objects: it admits mixed
actions whose interchange square has only a directed comparison. Such an
object cannot in general be uncurried by the old strict Cartesian-product
operation. The outer Cart then restricts the transformations between the
selected P's and their higher cells to the Cartesian profile. For a fixed
codomain, Cart and the ambient mapping category share functor objects;
that fact does not identify nested expressions when the inner codomain
itself changes.

The selected Gray-based replacement retains non-strict mixed interchange
and needs the appropriate closure, composition and duality interfaces. It
is not obtained by replacing the two names while keeping all old operations.
The Cartesian/Gray distinction is supported by Ara--Guetta v1 paragraphs
18 and 21; it does not prove that the prototype's full Q structure has been
qualified. The existing Q coherence and admission obligations remain.

These restrictions do not change `S_E(x)=Transf_{K,Q}(ιE,ιI_x)` into a
Cartesian transformation category, do not classify `homd_id_int(E)` as a
strict transfor, and do not make the public `FF:Functord(D,E)` strict. The
native x-action, general-FF relative composite, and negative profile controls
must continue to respect those distinct levels.

## Required migration

Keep the strict default, native F/FF Hom heads and response-0099 Q design.
Before promotion, reprofile Cartesian evaluation and its curry/uncurry
consumers, and qualify the whole coefficient universe. The proposed
`Cat_adm` in the Homd plan must specify its higher transformation profile.

Place the carrier/inclusion declarations upstream without depending on
late extracted strictness properties. Admission/proof interfaces can stay
later compatibility consumers. Settle the relationship between `Cat_cart`
and public `Cat_cat` at that owner boundary, checking whole Hom/transfor
consumers; shared object classifiers do not justify identifying them.

Unrestricted Eval still exists in production and the strict-action pilot.
The global collapse route is therefore not repaired yet. Promotion requires
the adverse construction to be rejected for the intended profile reason,
while Cartesian evaluation on strict transfors and genuine lax evaluation
remain available. The new pilot supplies a typed boundary, not completion.

An independent normalization regression was also isolated: the represented-
comma owner passes with capped and whole endpoint rules but fails after the
generic intrinsic-compositor identity clause is installed. Changing the
identity's chosen endpoint does not repair it. Its replay is retained; do
not replace the existing inverse-data proof with a declaration.

## Checked upstream implementation slice

The full-file authoring candidate now keeps fixed ambient whiskering on the
existing mapping-constructor action and retypes the Cat-derived parameter
telescopes to Cartesian Homs without replacing their derivations. Evaluation
and ordinary curry/uncurry retain their names and semantic bodies with
Cartesian mapping categories. The expected stable precomposition normal form
of curry is preserved; this migration adds no stronger normalization law.

The exact prefix through that owner passes 15 positive and four negative
controls, including the actual evaluator input rejection, retained lax fixed
whiskering/evaluation and uncurry arrow action. The full source then fails
at the whole opposite-family action, which now needs its coordinated
coefficient/duality repair. The audit's
`cartesian_migration_verification.json` records the successful prefix and
failed full file separately. No production rule from this candidate is
promoted, and the prefix result does not qualify the legacy whole-op owner.

## Mixed-family continuation and necessary profile boundaries

The next review concerns the actual `Functor_catd` body, derived from the
Hom telescope of `Cat_cat`. Under the corrected coefficient Hom its natural
fibre is `Functor_cart_cat(A[k],B[k])`. Its object classifier remains the
public `Functor(A[k],B[k])`. This distinction also makes the existing
`Eval_funcd` component have its actual Cartesian evaluator type. Retaining
the ambient fibre would require a different evaluation and higher-action
doctrine, rather than a mechanical change of type annotations.

Three finite controls are implemented in
`audits/strict-default-action-boundary/mixed_family_profile_models.py`.
They construct finite locally posetal strict 2-categories and check identity,
associativity, whiskering and interchange closure. They are external semantic
countermodels, not Lambdapi proofs or complete omega constructions.

First, take strict functors H,J from the walking arrow to a strict 2-category
with a noncommuting lax square:

```text
J[p] ε₀  ⇒  ε₁ H[p],       J[p] ε₀ ≠ ε₁ H[p].
```

The strict transformation between the two point selectors induces the
prescribed transformation `eval₀ => eval₁` on the ambient mapping category.
It is not strictly natural at ε. Consequently an arbitrary ω-base 2-cell
cannot give that action into Cartesian Hom while the fibre still contains
all lax transformations. The Cartesian fibre excludes precisely this
unsupported input. Fixed evaluation and fixed pre/post-whiskering on ambient
transformations remain meaningful.

This same example also implicates the HIGHER source action of the old whole
`Functor_cat_func`, still present in the authoring candidate. Its fixed
whiskering projections were checked computationally, but that does not
qualify the whole constructor under the new coefficient doctrine. Before
promotion, preserve the valid fixed actions through the correct owners and
repair that parameter interface. Do not use its old declaration alone as
evidence for an ambient mixed-family replacement. This is an additional
upstream obligation, not evidence that fixed whiskering must become strict
on arbitrary transformations.

Second, contravariance in the FAMILY parameter reverses its naturality
square. On a walking-arrow base K, let A'=const(1), A=const(I), and let
`L:A'=>A` over T(K) select L[1]=0 and L[0]=1 with comparison 0->1. The
proposed precomposition transformation over K would require eval₁=>eval₀;
at H=id_I it would give the absent arrow 1->0. The candidate therefore uses
`Functor_cart_cat(T(K),Cat)` for this negative parameter. Its covariant
B-parameter remains ambient `Catd_cat(K)` and accepts general displayed G.
An appropriately opposite naturality profile is a possible broader interface,
but it is not supplied by the legacy same-profile signature.

Third, `Pi_cat(Op_catd(E))` is not a corrected negative-section contract for
the intended canonical Hom action merely because its object components
remain readable. Let K contain p=>q, C contain r=>s:a->b, E=const(C), and
Y=const(b). The strict functor X:C2(K)->T(C) with X[p]=s and X[q]=r is a
valid section of the corrected constant opposite family. The intended Hom
action sends id_b to s along p and to r along q, so it would need s=>r,
which C does not contain. This refutes that prescribed action; it does not
assert that no family with the displayed object fibres can exist.

For constant E, the compatible ordinary input X:T(K)->C instead has the
expected Hom variance. The dependent replacement must supply its genuine
whole section profile. No simple reannotation of the base, identification of
C2(K) with K, or unqualified appeal to an oplax-transfor label repairs the
general interface. Keep this obligation coupled to the selected Q/Homd
construction, rather than introducing a primitive Pi or supplied equality.

The reference distinction is consistent with Ara--Guetta's Cartesian
internal Hom of strict transformations and its separate Gray lax/oplax
internal Homs. Their duality results do not grant arbitrary dimension flips
on Gray transformation profiles. See [paragraphs 18--21 and 35--38](https://arxiv.org/html/2503.08832v1).
The finite counterexamples and migration conclusions above are our own
specializations, not additional theorems attributed to that paper.

## Checked recovery of the whole-constructor boundary

The next prototype recovers fixed ambient precomposition through the Hom
action of existing family pullback at constant families. Its actual owner,
composition computation and non-strict-transfor inputs check without a new
primitive. Whole variable-base diagram formation now derives from native
`hom_int(id_Cat)` and fixed evaluation, giving Cartesian mapping fibres.
The unsupported whole ambient `Functor_cat_func` is removed from this
candidate; its valid fixed-source positive constructor remains.

Variable-base Pi uses the Cartesian inclusion before the existing fixed-base
Pi. Fixed-base Pi and family pullback retain general displayed maps. The
checked mixed prefix has 95 positive/19 negative controls; the full file
still fails at Hom_catd's negative-section projection. These are prototype
results, not production or global consistency qualification.

The total-fibre-opposite candidate has now been checked in the prototype.
`TotalOp_catd(E)` has base R(K), with whole family formation and base action;
the existing Hom_catd negative Pi input uses that family. On a constant fibre
C, the section is R(K)->O(C), which total duality sends to T(K)->C. Its whole
constant-Cat specialization computes to the existing Functor_catd. No new
section classifier was needed for this interface correction.

The corrected Sigma-Hom formula uses total duality on both the index and
the fibre family, preserving the original fibre direction. General total
2-cell and recursive projection controls check. The final copied-source
prefix has 129 positive/27 negative controls; the full file stops at the old
Edge constructor profile. Later action consumers and the complete Q/Homd
implementation remain unqualified, and production has not been promoted.
