# Cartesian-family whole Homd root

Date: 2026-10-14
Status: non-library strict-root/projection comparison checked;
full Q/y-comparison coherence, Sigma-Hom and production promotion remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [selected interface](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owner: [native root and represented laws](cart_homd_root.lpfragment)
Controls: [actual consumers](cart_homd_root_controls.lpfragment)
Replay: [one candidate](cart_homd_root_replay.py)
Evidence: [exact verification](cart_homd_root_verification.json)

## Whole target and root

Both E and I_x=Hom_K(x,-) remain K->Cat_cart. Default Transf remains lax;
the preceding whole y-section S_E(x) is not made strict. This continuation
implements the stronger canonical outer target and root:

```text
H_E : K -> Cat_cart
H_E[x] = T(S_E(x))
homd_id_int(E) : Hom_Cart(K,Cat_cart)(E,H_E)
homd_id_int(E)[x] = T(homd_id_src_func(E,x)).
```

The target is a definition using ordinary Cartesian represented Hom, not
an opaque family specified only by its object fibres. Let C=Functor_cat(K,Q).
The represented x-package Gamma has objects iota(I_x), with first Hom equal
to the already checked source-u map for I_x. That first Hom has domain
T(Hom_K(x,x')), so Gamma's source is CoAt2(K), reversing exactly dimension
two. Hom_CoAt2(C) is T(Hom_C), and applying CoAt2 to Gamma returns the base
to K. Thus ordinary Hom in CoAt2(C), composed with CoAt2(Gamma), gives H_E
with its declared Cartesian coefficient.

This dimension shift follows from the actual first-Hom type. It does not
change the input family base, reinterpret total opposite, or import an
unqualified duality on a lax mapping category. Only the category and
ordinary strict-functor CoAt2 owners are reused; the older mapping-category
duality declarations in that source fragment are excluded. A three-cell
typing observation distinguishes this operation from reversal of all
dimensions above one.

The strict root is a canonical constructor whose component and full base
action project through the existing source-u and Cartesian Hom owners.
Its x/u/y/v/f object ladder computes the same dependent-Hom leaf. Its first
base action retains the whole y-section after transporting u by E[p].

## Represented laws and independent naturality

Canonical mates reverse composition of Cartesian diagram maps. Their
component-first observation agrees with composition of the actual defined
opposite-direction represented Homs. The Q clause matches the transposed
functor values, avoiding a requirement to recover an already projected
Op_func constructor. Represented x-package units/composition check.

The root's naturality is tested independently of its strict wrapper:

```text
H_E[p] o T(h_x) = T(h_x') o E[p].
```

The comparison uses whole covariance reindexing and whole mate composition,
not only equality after selecting u. The covariance and mate compatibility
clauses are structural constructor laws; this slice does not derive them
from earlier point beta rules or from a complete independent Q model.

A single typed reflexivity check does not compose the whole comparisons
through the opaque common mate factor. The diagnostic first obtains the
whole covariance equality by typed reflexivity, then applies eq_ap to that
common functor. Its resulting type is checked against the two actual root
routes. These equality terms occur only in controls; no Homd constructor,
projection or action carries a proof argument. The point-u whole-section
comparison has its own narrowly scoped unifier at the opaque mate head.

A negative consumer rejects replacement of the transported u by an unrelated
target object. The independent comparison does not use the root's
StrictTransfor classification to make its two routes agree.

## Higher action and operational evidence

The base-two-cell consumer exposed a missing Cartesian postwhiskering
component projection. A whole Hom-level component fold and its capped-first
counterpart now send that action through E[alpha]'s actual component and the
source-u map. The root does not replace a variable higher endomorphism by
identity. This is a concrete higher-action observation, not a claim of
faithfulness of every induced Hom map.

The final candidate passes with subject reduction enabled under the normal
90s/2GiB/64MiB serial profile. The verification file records timing, memory,
exact source, donor, authoring inputs, receipt and log hashes. Replay emits
the checked bytes. The LHS audit has zero unreviewed compound slots.

Critical-pair diagnostics change 1083->1158, with none removed; the 66
replaceable-variable warnings are unchanged. The 75 added bodies group into
dimension-two category/shifted Hom action (32), ordinary functor dual action
(30), represented x-package projections (12), and Cartesian whiskering (1).
One expected rejection diagnostic is recorded separately. The concrete
unit/composition, component order, whole naturality and higher-action
consumers pass; global symbolic confluence is not claimed.

The complete direct ladder now has a native strict-root candidate under the
selected Q/mate structural contracts. Required work remains on extracted
lax y-comparison computation/coherence, Sigma-Hom, relative consumers and
the public migration. Do not turn the present computational evidence into a
claim that the full foundation or a complete profunctor model is finished.

```bash
python3 audits/strict-default-action-boundary/cart_homd_root_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_homd_root/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_homd_root/candidate.lp --strict
```
