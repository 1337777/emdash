# Groupoidification, monad duality and slice-family migration

Date: 2026-10-18
Status: staged core and reviewed owners qualified with refreshed library and
native-universality regressions. Production promotion and the overall goal remain open.
Predecessor: `a9185d801a7f3093ec92475aafc041e111f0ea6f`.
Original source: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`.

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
owns scope and completion. This tranche follows the remaining original central
imports and their original reviewers. No original source tail is omitted.
Exact source hashes, receipts, discarded variants, warning inventories and
resource profiles are in the [verification](production_final_imports_verification.json).

## Groupoidification

The walking-interval profunctor cell determines its coefficient. Its component
rule therefore drops the obsolete inferred Cat_cat argument instead of adding
a second rule. The generic groupoidification, interval extension and recovery
bodies remain unchanged. The former negative claiming distinct compositor
endpoints becomes the strict-default positive; an additional observation checks
that the same intrinsically extracted compositor computes to identity. Original
nonconstructor and parameter-retention negatives remain.

## Monad/comonad duality

The former Op_transf applications cannot take the retained ambient unit and
multiplication transformations under the corrected dimension-one transpose.
The existing total-duality action does accept that interface. Accordingly:

```
Comonad(A,D) = Monad(O(A),O(D))
O = TotalOp_cat
```

The historical Op_monad/Op_comonad names remain readability views of this total
duality, consistently with the existing Op_adjunction spelling. Unit,
multiplication, counit and comultiplication retain their ambient Transf types.
No new strictness premise or separate comparison cell is supplied.

The raw dual Kleisli functor has total-opposite Hom categories. Applying the
existing TotalOp_func to it gives the intended whole coextension

```
Hom_A(D[X],Y) → Hom_A(D[X],D[Y]).
```

The original point computations and next Hom action are retained. A negative
checks that the raw untransposed whole dual extension does not already have
this type for arbitrary omega-categories.

TotalOp_func is a defined alias. Three existing runtime patterns use its actual
CoAbove2_func(Op_func(-)) constructors; matching the alias itself was inert.
The two adjunction-induced observation rules retain their actual F∘G index
using canonical comp_fapp0. Subject reduction could not recover that index from
the normalized dual witness alone. The corresponding two reviewer applications
also state the existing index explicitly. These are type parameters, not new
witnesses, operations or equality arguments.

## Product and slice conventions

The represented product pairing families use Cat_cart and its existing whole
product constructor. Their original operations and inverse/triangular bodies
are retained. The weighted finite-limit projection observes its original
profunctor cell at that same coefficient.

The established Slice_cat uses the restriction-opposite convention, with an
arrow p carrying a triangle cell `b ∘ p → a`. The corrected core CommaFib uses
the reverse triangle-cell direction. Equating those categories would be wrong
for a general omega-category.

Instead, the original slice convention is preserved by the actual whole
construction

```
SliceSigma_catd(C)
  = op ∘ CoAt2_func(arrow_into_catd(C))
  : CoAt2_cat(C) → Cat_cart.
```

This follows the existing `op : CoAt2_cat(Cat_cart) → Cat_cart` interface. It
changes the direction of base 2-cell action, while retaining the original
objects and ordinary postcomposition functors. The selected dependent-product
family uses the same CoAt2(C) base; the pullback family remains over Op(C).
The choice of adjunctions remains supplied structure, not a newly derived
all-categories existence theorem.

The canonical represented maps now have the strict carrier, and their old
ambient Sigma-map consumers use the existing strict_transfor inclusion. No
parallel Sigma theory or operation family is introduced. The original slice
domain, object, arrow, triangle, mate, and dependent-product operations remain.

## Canonical Hom types and preserved endpoints

Owner-position checks exposed premature inversion of the readable injective
Hom alias. It produced spurious opposite-category constraints and could lose an
independent endpoint when a rectangle or whole mate cut was elaborated.

The affected rectangle and mate declarations now state their existing Hom
types canonically. Semantic mate bodies remain the original unit/counit
composites. The generic capped functor action also uses the same canonical
result as evaluation of its whole Hom action:

```
fapp1_fapp0(F,f) : τ (Obj (Hom_cat B (F[X]) (F[Y]))).
```

Its original `f : τ (Hom A X Y)` input is deliberately retained. Canonicalizing
that input too passed the local suite but lost opposite-domain information in
an existing arrow-diagram inference consumer. The narrower result-only change
passes that consumer and the complete core/Homd regression. Removing the local
canonical types still fails the original rectangle SR check; that attempted
simplification is discarded.

No new primitive, rewrite or unification rule is added. Existing rules receive
the necessary coefficient/duality patterns and two documented endofunctor
index guards. No endpoint equation is imposed, and no operational equality
payload is introduced. The existing reviewer explicitly retains an arbitrary
mate endpoint and checks both triangle/rectangle and mate-composition orders.

## Qualification boundary

The final complete core/Homd regression retains 287 positive and 85 negative
assertions, passing in 19.643 seconds at 1628016 KiB. The refreshed combined
library closure passes 178/27 in 55.084 seconds at 4511532 KiB under 180s/6GiB/o=20.
The larger native zero-column, transpose, mapping and homology regression
passes 139/27 in 91.674 seconds at 6285756 KiB under its existing
300s/8GiB/o=10 profile. All three final snapshots are rehashed against current
emitted sources and use the unchanged installed checker, with subject reduction
and warnings. Eight owner LHS audits have zero unreviewed slots; custom
constructor patterns and their two explicit induced-FG guards are reviewed too.

The matching pre-goal combined library closure passes 176/27 in 22.544 seconds
at 1597160 KiB under the same settings as the current combined run. The changed
counts reflect the strict-default compositor positive and the additional
identity/whole-variance observations. These are single end-to-end measurements,
not an isolated type-normalization benchmark. The migration/import overhead is
still material. Resource ceilings, serial execution, file/core limits and
no-swap containment remain; no normal default or installed toolchain changed.

The first broader candidate passed a 169/26 closure, but its canonical-input
inference regression required the result-only revision. Those earlier receipts
are retained as development evidence, not silently carried as current passes.

The final core warning inventory is 1564 versus 1987 at the preceding core
snapshot: 34 newly printed and 457 removed bodies. Added families concern
existing Core-inclusion composition, product identity projection, and
path-record symmetry/reflexivity rules. This is an elaboration/overlap
inventory, not proof of global confluence or a count of repaired mathematical
bugs. Redundant strict instances and remaining normalization/performance costs
remain part of the required pre-promotion review.

The current combined warning stream has 2404 bodies versus 1315 in the original
closure. The reviewed module families are total-duality/induced-monad index,
triangular product/action, slice triangle/mate, and identity/projection overlaps.
Their owner counts and exact source/log snapshots are recorded. Passing the
reviewers does not settle every symbolic overlap or the entire central import
order. The separate isolated checker-memory patch remains unadopted.

Replay after a relevant owner, dependency or checker change by emitting with
`production_owner_migration.py` and running the guarded source checker on
`join_recursion_controls.lp`, `foundations_library_regression.lp`, and
`native_zero_column_regression_controls.lp`, serially with the recorded profiles.
The baseline package emits the corresponding original library closure.

Next migrate the original central diagnostic assertions, then finish remaining
registered consumers, redundant-wrapper retirement, production promotion and
the final catalogue/health/CI/source-pin gates. The application goal stays paused.
