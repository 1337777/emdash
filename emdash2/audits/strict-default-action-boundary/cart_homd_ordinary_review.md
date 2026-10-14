# Ordinary internal action and the extracted Homd y-comparison

Date: 2026-10-14
Status: non-library definitions and direct projections checked;
represented-source beta and full coherence remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [Cartesian families and lax sections](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owner: [ordinary action and comparison](cart_homd_ordinary.lpfragment)
Controls: [whole and capped consumers](cart_homd_ordinary_controls.lpfragment)
Replay: [integrated candidate](cart_homd_ordinary_replay.py)
Evidence: [exact verification](cart_homd_ordinary_verification.json)
Predecessor: [relative/intrinsic action](cart_homd_relative_review.md)

## Ordinary internalization is constructed

For an ordinary strict functor F:A->B, define

```text
D_F,x = Hom_B(F[x],-) o F : A -> Cat_cart
fapp1_at(F,x) = c_(D_F,x)(x,id_F[x]).
```

Here c is the existing whole Cartesian covariance map. This definition has
the strict transformation type `Hom_A(x,-) => D_F,x`; its whole y-component
computes to F_1(x,y). No new admission witness is needed.

For a default lax epsilon:F=>G, fixed postwhiskering by Hom_B(F[x],-)
followed by this F-action defines

```text
tapp1_at(epsilon,x)
  : Hom_A(x,-) => Hom_B(F[x],G[-]).

tapp1_at(epsilon,x)[y]
  = postcomp(epsilon[y]) o F_1(x,y).
```

The component is a whole functor. Its first Hom retains epsilon[y] and F's
actual action on alpha:f=>g. Identity epsilon returns the canonical strict
F-action. This does not admit arbitrary epsilon as strict.

Runtime keeps the represented postcomposition head. A narrow proof-time
comparison relates its capped pre/right action to the existing tapp1
middle. The older raw-composition comparison did not chain through that
normalized middle; this failed observation and the correction are recorded
in the receipt ledger. Typed reflexivity validates the new comparison, and
runtime nonconversion is retained separately.

Identity whiskering also exposed a difference between the represented and
raw composite family endpoints. The only new runtime clause normalizes
postcomposition by the named Cartesian Hom family to its actual reindexing
body. It does not fold arbitrary Hom-postcomposition to raw composition.
The overlapping nested-reindexing routes agree at whole-functor type.

## The y-comparison is an extraction, not an input

Feed the positive internalization into the existing corrected Homd intrinsic
action. Evaluate its forward laxity at the source identity. This defines
the ordinary directed comparison

```text
G[p] o epsilon[x]  =>  epsilon[y] o F[p].
```

Apply that same definition to the actual Homd section h_E(x,u), whose
codomain is Q. It gives the whole comparison

```text
iota(I_x[q]) o h_y  =>  h_z o iota(E[q]).
```

The code's `sf_cq_homd_y_comparison` and its v/k projections are all
definitions. The right endpoint computes to the already implemented mate
action. At v:E[y] and k:x->z the comparison is a functor

```text
(iota(I_x[q]) o h_y)[v][k]
  -> Hom_E[z](E[k](u), E[q](v)).
```

Its whole Q-Hom type supplies the strict v/k naturality from the nested
Cartesian Homs, while the y-direction remains lax. The reverse-direction
consumer is rejected. General epsilon's two naturality endpoints are not
identified by the proof-time pre/right bridge.

This qualifies an extraction route through the existing structural
tdapp1/fdapp1 owner. It does not derive that owner's complete coherence.
In particular, the left represented composite has not been expanded or
silently equated to the right endpoint.

## Remaining consumed computation

The next Q operation is the represented composite on the source of the
displayed functor above. Its generating observation should send

```text
beta:k=>qf, a:E[f](u)->v
  |-> E[q][a] o E[beta][u].
```

This must be obtained through the actual represented composition and
connected to the extracted comparison, not installed as a disconnected
pointwise function. The earlier represented unit/counit constructions are
possible donors, subject to their Cartesian coefficient and current owner
types. Only these consumed operations are required; a full general
profunctor/coend library is not a prerequisite. Unit/composition coherence,
Sigma-Hom and production migration remain required after that connection.

## Validation

Receipt `20261014T200728Z-f87d4b0830084e1b9d72f3e72863ab84` passes with subject
reduction in 2.483s, with maximum child RSS 219,920KiB. The unchanged default
resource profile is 90s/2GiB/64MiB, serial, with OCAMLRUNPARAM=o=20. Replay
and evidence pin the authoring inputs and emitted source.

Critical-pair diagnostics change 1170->1174. All four added bodies concern
the named represented-family normalization and existing composition rules;
the whole reindexing comparison and identity specialization are checked.
The 66 replaceable-variable warnings are unchanged. Three expected
negative-control diagnostics are inventoried separately; none were removed.
The LHS audit reports zero unreviewed slots. This is focused computation
evidence, not a global confluence or semantic-model certificate.

```bash
python3 audits/strict-default-action-boundary/cart_homd_ordinary_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_homd_ordinary/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_homd_ordinary/candidate.lp --strict
```
