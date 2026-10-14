# Cartesian represented Hom and direct local Homd

Date: 2026-10-14
Status: non-library owner/projection continuation checked; whole Homd remains open
Plan: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Owner: [represented Hom](cart_represented_hom.lpfragment)
Consumer: [focused controls](cart_represented_hom_controls.lpfragment)
Replay: [single candidate](cart_represented_hom_replay.py)
Evidence: [verification](cart_represented_hom_verification.json)

## Implemented operations

Write Cat_s for sf_cart_cat, Cart for sf_cart_functor_cat and T for the
candidate's Op_cat. This pinned experimental spelling of Op_cat reverses
dimension one; TotalOp_cat reverses all positive dimensions. It is not the
unrepaired production duality contract.

The preceding whole-u covariance gives the first Hom of Cartesian Yoneda:

```text
Y_K : T(K) -> Cart(K,Cat_s)
Y_K[x] = I_x = Hom_K(x,-)
Y_K1[x',x] = C_(I_x),x'.
```

The new whole owner is sf_cart_hom_int. It uses the existing covariance
constructor instead of a second family-map carrier. Its y-component is
whole ordinary precomposition. Its projected unit and composition reduce
at their canonical covariance constructors. A variable base two-cell
survives the actual Hom of Y_K and the component projections as the existing
postcomposition action. E and I_x retain the same family classifier.

The target-first represented Hom is an actual defined composite:

```text
sf_cart_hom_con_int(F)
  = precomp(T(F)) o Y_(T(B))
  : B -> Cart(T(A),Cat_s)                         for F:A->B.

sf_cart_hom_con_int(F)[b][a] = Hom_B(F[a],b).
```

The first factor uses ordinary Hom action in the Cartesian coefficient.
There is no assumed Q universe or supplied mate comparison in this definition.
The definition at F=id is the actual Y_(T(B)), including its whole type.

Substituting the already defined transport functor gives the direct local
Homd consumer:

```text
sf_cart_homd_tgt(E,x,u,y)
  = sf_cart_hom_con_int(transport(E,x,y,u))
  : E[y] -> Cart(T(Hom_K(x,y)),Cat_s)

sf_cart_homd_(E,x,u,y,v)
  : T(Hom_K(x,y)) -> Cat_s

sf_cart_homd_(E,x,u,y,v)[f] = Hom_E[y](E[f](u),v).
```

For alpha:f=>g, the actual whole index-action functor is precomposition
by the component at u of E[alpha]. That component is extracted from E's
first Hom and the existing Cartesian component evaluator. No independent
cell, equation or proof is an operational input. A variable higher
endomorphism is not rewritten to identity.

These are genuine reusable operations, but y is still an external argument
of this local consumer. This slice does not claim the transformation-backed
whole y-section, source-u mate, whole x-root or Sigma-Hom comparison.

## Computation and qualification

The only failed development consumer checked the base-action projection of
the represented identity section. Its Cartesian coefficient identity had
already become ordinary id_func, hiding the literal generic Hom unit
pattern. Scoped post/precomposition clauses on the normalized Cartesian
coefficient identity now retain the whole unit functor. Both the section
component and the base-action projection pass, as does the represented
F=id whole comparison. No resource increase or global identity rewrite was
needed.

The final candidate passes with subject reduction enabled in 1.775s under
the normal 90s/2GiB/64MiB serial profile, with OCAMLRUNPARAM=o=20. Exact
source, donor, authoring, receipt and log hashes are in the evidence.
The LHS audit reports zero unreviewed compound slots.

Critical-pair diagnostics change 918->945; the 62 replaceable-pattern
warnings are unchanged. The 27 added bodies are inventoried by hash and
owner group: Yoneda projections/identity presentations, generic action
versus naturality/composition, canonical covariance identity projections,
covariance composition/units and normalized coefficient units under Hom
projections. Whole-first/component-first unit and composition, actual
base-two-cell projection and local Homd index action are concrete consumers.
This is not a global confluence proof. Inherited negative-control diagnostics
are separate from these structural warning counts.

The public kernel and its pending owner-relocation edits are unchanged by
this non-library slice. The pre-existing generic Cartesian composition
countercheck for the ambient lax universe remains a qualification; it is
not repaired by the separate coefficient or these successful computations.

Next use these actual Cartesian represented owners in the whole Q-valued
mate/section construction under the explicit Cat_lax interface. The user's
latest carrier/naming direction is recorded in the
[strict-core review](../../../docs/EMDASH_STRICT_CORE_LAX_EXTENSIONS_REVIEW.md).

From emdash2:

```bash
python3 audits/strict-default-action-boundary/cart_represented_hom_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_represented_hom/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_represented_hom/candidate.lp --strict
```
