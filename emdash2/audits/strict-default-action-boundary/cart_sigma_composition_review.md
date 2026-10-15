# Whole composition compatibility for intrinsic Homd and Sigma maps

Date: 2026-10-15
Status: non-library whole comparison and expanded total-arrow consequence checked
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Owner: [composition owner](cart_sigma_composition.lpfragment)
Consumers: [native comparisons](cart_sigma_composition_controls.lpfragment)
Replay: [integrated prefix](cart_sigma_composition_replay.py)
Evidence: [verification](cart_sigma_composition_verification.json)

## Construction

FF:E=>D remains an ordinary conventional-lax transformation across K, where
both families land in Cat_cart. This continuation does not select the older
strict-Functord alternative or change the identity-core/relative Homd split.

For p:x->y and q:y->z, the whole fibre composition is

```text
C_E : Hom_E[y](E[p]u,v) x Hom_E[z](E[q]v,w)
       -> Hom_E[z](E[qp]u,w)
C_E(a,b) = b o E[q][a].
```

Its implementation body uses existing transport, product projections and
ordinary product-form Hom composition. A stable whole owner projects to
that one body at objects and at the next whole/capped Hom. This is an
internalized version of the existing Sigma composition. It introduces no
new Homd section base or Q operation.

Let Phi_FF(p) be the existing intrinsic Homd filler functor. The selected
whole comparison is

```text
Phi_FF(qp) o C_E = C_D o (Phi_FF(p) x Phi_FF(q)).
```

A proof-time unifier records this as a structural computation law of the
declared strict Sigma-map contract. It is not presented as a theorem derived
from the earlier object beta rules alone. Its constraints require the two
actual intrinsic actions, with the same FF and base arrows; it does not
identify the endpoints of FF's noninvertible naturality cells.

The diagnostic `sf_cart_sigma_composite_image_eq` is then derived from the
whole comparison by ordinary equality congruence. Its endpoints are the
two actual expanded operations: map the composite total arrow, or compose
the two mapped total arrows. Both reduce through the existing Sigma/Homd
projection ladders. Equality proofs occur only in these diagnostic theorems;
no operational constructor receives a proof argument.

## Implementation boundaries

The initial whole definitions typechecked, but the expanded nested
composition pattern did not match the intended comparison. A small local
debug run confirmed that no applicable unifier was selected. Retaining a
stable whole composition owner, with its real implementation projections,
gave a bounded comparison with explicit matching constraints.

The identity-FF specialization exposed the pair of product projections.
A scoped unit comparison at this composition owner handles it. No general
product eta or runtime collapse of the two composition routes is installed.
The identity and constant-family positive cases check, while changing the
base arrow q to an unrelated parallel q' in the constant-family case is
rejected. The whole first-Hom projection also reaches the implementation
body, retaining arbitrary higher input cells.

Removing only the whole compatibility unifier leaves an unsolved equality
at the typed-reflexivity theorem. Its failed receipt is recorded separately,
so the new structural law is not mislabeled as already derived behavior.
Earlier unsuccessful expanded-pattern variants remain in pinned checker
input snapshots rather than in the selected source.

## Validation and next consumer

Receipt `20261015T090931Z-30ef794345e046ba8d6b4553a6b0a460` passes with SR
in 4.352s/339,948KiB under the default serial 90s/2GiB/64MiB profile and
OCAMLRUNPARAM=o=20. The focused missing-law control fails as intended in
`20261015T091012Z-19a09b92cbe644e587d5ba16f6a32a81`.

Critical-pair diagnostics change 1636->1642; all six additions are the
stable capped composition projection against inherited generic identity
or postcomposition action. No earlier body is removed; pattern warnings
remain 66. Exact bodies and source/resource hashes are pinned in the
verification file. LHS audit has zero unreviewed slots. This is not global
confluence or production qualification.

Next qualify the whole off-diagonal action of a mapped modification
theta:FF=>GG: it should be the negative Sigma map of the existing general
theta Homd presheaf action, with the already checked vertical component.
Then continue public owner/classifier integration and downstream validation.
Lax FF remains the selected path; no obstruction established here requires
switching its classifier to strict transformations.
