# Strict defaults require an evaluation-profile migration

Date: 2026-10-11
Status: checked obstruction to blanket restoration; Cartesian profile interface pilot passes
Owner: [strict-functor/duality plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [native audit](../emdash2/audits/strict-default-action-boundary/README.md)

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
