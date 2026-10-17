# Represented-comma graph: families and action admission

Date: 2026-10-16
Predecessor: `88fde500`
Status: corrected family/Sigma-image prefix qualified; complete graph and action-profile admission incomplete
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

## Implemented prefix

The original source/middle/target family owners now use the existing total
duality consistently. With T=Op_cat and O=TotalOp_cat:

```text
I_B                : T(B) → Cart(B,Cat_cart)
M(F,G)             : T(B) → Cart(B,Cat_cart)
M(F,G)[x][y]       = Hom_C(F[x],G[y])
Source_raw, Mid_raw : T(B) → Cat_cart       (via Sigma_coeff_func)
Source, Mid        : O(B) → Cat_cart       (via TotalOp_catd)
Target             : O(B) → Cat_cart       (via pullback along O(F)).
```

The ordinary view of M uses the existing Functor_cart_include. Ordinary
internal-action inputs use hom_int_view, while the one remaining direct
homdc_edge_catd formation keeps its required Cartesian Hom. These are actual
whole inclusions, not category equalities or objectwise assemblies.

The original comma_graph_sigma_transf is still a definition by ordinary
postcomposition with Sigma_func. It accepts the original general internal
action Theta and produces an ordinary Cat_cat-valued transformation. Its
component computes to sigma_map_func of the actual Theta[x], retaining that
whole displayed map and its subsequent action. Both the family prefix and
this Sigma-image prefix with its component consumer pass with subject
reduction. No new primitive, rewrite or unification rule is installed here.

The whole file remains deliberately unqualified. Its next total-dual call
requires a Cartesian map between the admitted families. The ordinary Sigma
image does not have that type. The emitted source labels this admission
boundary; its failed receipt is expected evidence, not a green library run.

## The arbitrary-Theta contract needs correction

The [finite orientation diagnostic](production_comma_graph_orientation.py)
uses K=(0→1), constant strict F/G, and a strict one-object two-category whose
Hom is the Boolean-square poset with join as composition and bottom as unit.
An arbitrary lax two-variable Theta can have

```text
Theta[0,0](id)=a,  Theta[0,1](p)=m,  Theta[1,1](id)=b,
a → m ← b,
```

where a and b are incomparable. Both nested transformations use the selected
conventional-lax convention; these are the retained comparisons in the
separate y and x directions. The inner comparison is a→m; the outer
comparison is b→m. All inhabited modification squares commute in this thin
model; the potentially mixed corner has empty source Hom_K(1,0). A graph
with the prescribed F/G side arrows would require a→b, which does not exist.
This rejects the unchanged arbitrary-lax Theta contract. It is an external
finite diagnostic, not a model or consistency certificate for the full kernel.

For the actual conventional-lax eta input, its canonical internal action is
Theta[x,y](f)=eta[y]∘F[f]. Strict functor action and the selected pre/right
convention make the x comparison strict. The diagnostic also checks a
canonical case with m=b: the outer comparison is identity while a→b remains
noninvertible. This distinction preserves the intended lax eta input.
It does not by itself implement or qualify the whole native strict-x admission.

## Next required work

Qualify the canonical internal action's x profile using the existing
internal-action and pre/right owners. Then qualify the actual Sigma image
in the coefficient required by TotalOp_funcd, retaining a whole comparison
with the ordinary Sigma image. A proposed refinement must preserve the
original eta and its noninvertible post/left cell, not replace eta with a
strict input or supply a new comparison cell at the caller.

The general Theta helper must state a valid profile explicitly. A strict x
profile includes the canonical input; a reversed outer-comparison profile
is another possible generalization. Neither is to be silently substituted
for a finished graph. The existing gray_transf_graph_func is an independent
structural declaration and must not replace this original derivation while
being reported as derived. Complete sections, totalization, source/target
inverse data and the original full reviewer remain required.

The [verification record](production_comma_graph_verification.json) retains
the exact prefix and failed-full-source receipts, model output and hashes.
Current prefix runs take 33–35s under the previously measured 90s/3GiB/o=20
import profile, with host headroom inspected, subject reduction, serial
execution and no swap. Warning bodies are unchanged from the preceding
import boundary. Four existing green core/consumer receipts still rehash to
their inputs. Public promotion, the direct-cover route and the rest of the
repository migration remain open.
