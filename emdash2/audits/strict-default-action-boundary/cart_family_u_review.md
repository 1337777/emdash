# Whole u-action of Cartesian covariance

Date: 2026-10-14
Status: non-library covariance continuation checked; Homd remains open
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Owner: [native declarations and projections](cart_family_u.lpfragment)
Replay: [single candidate](cart_family_u_replay.py)
Evidence: [exact verification](cart_family_u_verification.json)

## What this implements

For E:K->Cat_cart and I_x=Hom_K(x,-), the preceding checkpoint supplied
the canonical strict transformation c_E(x,u):I_x=>E. This continuation
internalizes u in the actual Cartesian diagram Hom:

```text
C_E,x : E[x] → Hom_Cart(K,Cat_cart)(I_x,E)
C_E,x[u] ↪ c_E(x,u).
```

This is the Cartesian-profile version of the existing core covariance
ladder, not the final dependent Homd construction. Its component at y is
the whole functor

```text
T_E,x,y : E[x] → Cart(Hom_K(x,y),E[y])
T_E,x,y[u][f] ↪ E[f](u).
```

Cartesian component evaluation is a definition using the existing whole
mapping inclusion and ordinary tapp0. Its composite with C_E,x folds to
T_E,x,y. There is no primitive Pi, larger y/u/f context or operational
equality proof.

The first-Hom projection sends h:u->v to a classified strict transformation
between the two index functors, with f-component E[f][h]. The whole
Hom-level f-observation is E[f]'s actual first Hom. Its capped-first
counterpart sends a fibre two-cell theta:h=>k to E[f][theta]. The complete
fibre-cell direction is retained, and a variable higher endomorphism does
not become identity.

The whole covariance and transport_u functors are structural canonical
owners. Their object and Hom projection computations are checked here;
the slice is not a derivation of a complete independent coefficient model
or a completed higher coherence/confluence proof.

## Projection order and computation

The first owner check exposed a genuine missing bridge: taking u-action
before evaluating the y-component retained the Cartesian inclusion's
first Hom. A scoped tapp0_hom projection on the canonical covariance
constructor now joins it to the same transport_u map.

The analogous next-Hom bridge at f preserves the fibre two-cell action.
Both bridges use the measured expanded body of the component evaluator,
not a generic commuting rule for arbitrary terms. Identity/composition
of projected transport maps and their ambient component views agree in
the focused consumers.

An initial composition pattern carried the reducible fibre expression
in its Cartesian category discriminator and omitted explicit family
arguments on rule RHSs. It exhausted the 90-second guard while processing
overlaps. Repeating the full reducible expression is unnecessary: the
stable Cartesian profile plus the canonical map constructors suffice.
The accepted pattern uses that profile and explicit K/Cat_cart arguments
on the RHS. It checks in the normal small-resource range; no timeout or
memory limit was increased. This is a rewrite/inference engineering result,
not a mathematical counterexample to covariance.

## Evidence and limits

The final candidate passes with subject reduction enabled in 1.730s and
163,640KiB maximum child RSS, under the default 90s/2GiB limits. Its durable
replay reproduces the already checked source byte for byte. The LHS audit
reports zero unreviewed slots.

Warnings change 897->918 with none removed. The 21 added bodies concern
projected transport identities, ordinary/dual identity presentations,
the two capped component bridges, and projected composition versus units.
The evidence records their hashes and the relevant failed development
runs. No new removal matrix or repository aggregate was run.

The prior Cartesian admission/noncollapse controls remain included. The
new controls observe the whole u/y projection, object leaf, fibre-arrow
action, whole Hom-level f-projection, capped-before-y projection, actual
fibre two-cell computation, identity/composition and higher noncollapse.

This does not implement the Q mate or its lax y-section, the whole x-root
of Homd, Sigma-Hom, or the public strict-core migration. The pending strict
core/explicit lax interface decision is recorded in the
[architecture review](../../../docs/EMDASH_STRICT_CORE_LAX_EXTENSIONS_REVIEW.md).
The previous public-universe composition countercheck remains independent.

Next use this actual Cartesian covariance functor in the represented
diagram/mate construction. In particular its representable specialization
has the correct first-Hom type for a Cartesian Yoneda package
T(K)->Cart(K,Cat_cart). Preserve the direct projection ladder and keep the
derived profunctor mate's necessary lax section profile explicit.

From emdash2:

```bash
python3 audits/strict-default-action-boundary/cart_family_u_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_family_u/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_family_u/candidate.lp --strict
```
