# Corrected Sigma-Hom with the shared Cartesian family coefficient

Date: 2026-10-15
Status: non-library Sigma formation, Hom presentation, arrow composition and
recursive projection checked; total-map and public migration remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [current Homd interface](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owner: [Sigma and coefficient duality](cart_sigma.lpfragment)
Controls: [actual consumers](cart_sigma_controls.lpfragment)
Replay: [integrated candidate](cart_sigma_replay.py)
Evidence: [exact verification](cart_sigma_verification.json)

## One total constructor and the corrected Hom

The admitted input is the same E:K->Cat_cart used by the direct Homd ladder.
For I=Hom_K(x,y), its fixed-y/v leaf is the whole presheaf

```text
H = homd_(E,x,u,y,v) : T(I) -> Cat_cart
H[f] = Hom_E[y](E[f](u),v).
```

Write T=Op_cat, R=CoAbove2_cat and O=TotalOp_cat=R(T(-)). Whole fibre duality
is the actual composite

```text
O_fib(H) = total_op_cart o R(H) : O(I) -> Cat_cart.
```

The candidate retains one covariant Sigma constructor. Its negative total is
a definition, and its Hom presentation consumes the existing Homd leaf:

```text
Sigma_con_I(H) = O(Sigma_(O(I))(O_fib(H)))

Hom_(Sigma E)((x,u),(y,v)) = Sigma_con_I(H).
```

Both the base and the fibres are dualized. For a constant family at C, the
explicit RHS computes to
`Hom_K(x,y) x Hom_C(u,v)`. This check observes the Hom expression directly;
it does not allow Sigma(Const(C))->K x C to bypass an incorrect Hom rule.
The reversed-fibre alternative is rejected. Forward noninvertible fibre
two- and three-cell consumers check in that explicit RHS.

This reuses the constructor architecture of the earlier
[total-opposite Sigma audit](sigma_total_op_verification.json), but its
old public-universe coefficient identification is not inherited. The
current candidate is checked with separate Cat_cart, default lax Transf,
and the actual corrected Q/Homd source.

## Whole duality and native arrows

The Cartesian coefficient has a whole total-duality operation
`R(Cat_cart)->Cat_cart`, with first Hom
`O(Cart(A,B))->Cart(O(A),O(B))`. Its strict-transformation image has the
existing ambient TotalOp_transf as its ordinary view. The whole first-Hom
action of O_fib(E) and an actual transfor component are checked.

A bare comparison of the opposite-Hom component encounters the known
checker inference limitation. A typed diagnostic view using the canonical
`Obj(Hom_cat(...))` carrier checks and computes. No extra operational cast,
equality argument or comparison rule was introduced to force that query.

The old forward-arrow interface is retained:

```text
(p,a) : (x,u) -> (y,v),       a:E[p](u)->v
(q,b) o (p,a) = (qp, b o E[q][a]).
```

Strict family composition needs its existing law at the surviving ordinary
functor-composition owner after the Cartesian coefficient has projected.
Whole and capped joins are checked for variable E and the represented
family Hom_K(w,-). This does not impose strictness on arbitrary displayed FF.

The arbitrary-endpoint arrow constructor, base/fibre projections and its
composition follow the production architecture. A constant total becomes a
product before these consumers act. The named arrow constructor therefore
has the corresponding product component beta rules; both base projection
and fibre-of-composition check in that observation order. The general
constructors remain available without requiring object or arrow eta.

## Iterated Hom and the first projection

A general total two-cell has data

```text
kappa:p=>q,  eta:a -> H[kappa](b).
```

Its constructor typechecks as the actual dependent pair in the computed Hom.
The first projection's initial Hom owner remains stable; its next action is
the total dual of the inner Sigma projection. Whole-first and capped-first
observations both return the original kappa. This is an internal recursive
projection, not a separately supplied base map.

For orientation context, [Ara--Guetta v1, section 7](https://arxiv.org/html/2503.08832v1#S7)
describes Grothendieck constructions with Cartesian coefficients and makes
its total-dual convention explicit. It is a semantic cross-check, not
evidence for this native implementation or permission to identify distinct
base profiles. The native constant-family and directed-cell controls above
are the evidence for the selected presentation.

## Validation and continuation

Receipt `20261015T080124Z-9bf6de46e18846379438be514dca41fd` passes with subject
reduction enabled in 5.163s and maximum child RSS 304,632KiB. Limits remain
the serial default 90s/2GiB/64MiB with OCAMLRUNPARAM=o=20. Replay and evidence
pin the exact source, authoring inputs, raw logs and resource settings.

Critical-pair diagnostics change 1269->1541; replaceable-variable warnings
remain 66. Added groups are basic duality (6), Cartesian total duality (29),
projected strict-family transport (221), Sigma arrows (5), and Sigma
projections (11). Grouped exact-body digests and participant inventories are
recorded with the pinned logs. The measured transport endpoint guards and
shared-family projection guards are retained; the LHS audit reports zero
unreviewed slots. No global confluence claim follows from these checks.

This is a working Sigma-Hom formation/projection candidate under the selected
structural owners. It is not the public kernel migration. The whole total-map
parameter action, its actual transport/map consumers, and downstream/source
integration still need qualification. No new Q composition operation or
general balancing/coend theory was used. The optional balance experiment
remains outside this continuation.

```bash
python3 audits/strict-default-action-boundary/cart_sigma_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_sigma/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_sigma/candidate.lp --strict
```
