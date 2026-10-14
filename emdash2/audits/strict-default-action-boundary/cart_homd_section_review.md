# Cartesian-family whole Homd section and source-u action

Date: 2026-10-14
Status: non-library fixed-x ladder checked under structural Q/mate contracts;
outer root and full coherence remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [selected coefficient/section design](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owner: [native declarations](cart_homd_section.lpfragment)
Controls: [actual consumers](cart_homd_section_controls.lpfragment)
Replay: [one candidate](cart_homd_section_replay.py)
Evidence: [verification](cart_homd_section_verification.json)

## Construction and actual computation

The public default in this experimental prefix remains strict functors with
conventional lax transfors. Both E and I_x are K->sf_cart_cat. Q's local Hom
is Cart(A,Cart(T(B),sf_cart_cat)), while its whole y-section uses the ordinary
default Transf(K,Q). This implements the user's latest distinction between
strict fibre naturality and lax naturality across the base.

The represented inclusion's first Hom is defined Cartesian postcomposition
by the previously checked represented Hom. Object and whole first-Hom
projections are retained. Q units, right composition with represented maps,
and the corresponding stable postcomposition view compute to ordinary
reindexing. Represented composition of two strict functors and constant
transports are actual consumers. No general profunctor composition library
is introduced.

The mate of a Cartesian whole map U:E=>D is a structural transformation
iota(D)=>iota(E). Its y-component is the defined represented Hom of U[y].
Its full pre/right y-action is a composite of existing whole Hom action
and the diagram's first Hom; its q/v/f observations compute. The output is
not admitted to the StrictTransfor carrier.

The actual section category and canonical section are

```text
S_E(x) = Hom_{Hom_Cat(K,Q)}(iota E,iota I_x)
homd_src_sec(E,x,u) = mate(c_E(x,u)).
```

The whole mate operation has source T(Hom_Cart(K,Cat_cart)(E,D)). Its
y-component is the Cartesian component functor, transposed and followed by
the represented opposite-direction Hom. A whole component fold and its
capped-first Hom projection agree in the focused consumer.

The source-u map is an actual defined composite:

```text
homd_src_func(E,x) = mate_func(I_x,E) o T(C_E,x)
                  : T(E[x]) -> S_E(x).
```

Applying it at u, then taking the transformation component at y and the
ordinary v/f projections computes to `Hom_E[y](E[f](u),v)`. At a source
arrow h:u0->u1, the same ladder computes to the whole functor precomposing
by E[f][h]. The projected identity computes to identity, while a variable
endomorphism is not converted to identity.

This is an internalized-y section, unlike the preceding local consumer.
It still does not implement the outer x-root. The mate and Q are structural
constructors with qualified projections, not a derived complete model of
their general composition or all higher coherence. The extracted directed
y-comparison and its full coherence remain to qualify. No independently
supplied cell or operational equality-proof payload was introduced.

## Engineering observations

One nested source-u consumer initially failed endpoint inference with
implicit fapp0 classifiers. Naming the actual y and y/v observations with
explicit category/family arguments fixed that consumer; the constructors
and variance rules were unchanged. The observation helpers are definitions
of actual projections, not extra supplied maps.

A constant transport exposed a real normal-form gap: ordinary composition
had already turned its represented functor into a constant functor before
the Q-composition pattern could match. Two scoped clauses at raw Q
composition and its stable postcomposition owner now cover that represented
constant normal form. Both observation orders pass. They do not rewrite
arbitrary constant profunctors as represented ones.

The final source passes with subject reduction enabled in the default
90s/2GiB/64MiB serial profile. The evidence records exact wall time, memory,
source and authoring hashes. Replay reproduces the checked source byte for
byte; the LHS audit has zero unreviewed compound slots.

Critical-pair diagnostics change 945->1083. The 138 added bodies concern
represented inclusion action, Q identity/represented composition normal
forms, constant transports, conjoint action/units and mate component/unit
projections. Four replaceable-variable warnings and two expected rejection
diagnostics are recorded separately. The actual unit, represented composite,
constant and whole/capped component consumers pass. This is not a global
confluence or arbitrary-Q-coherence claim, and no removal matrix was run.

The negative controls preserve the distinction between Cartesian and general
ambient families, between the mate's Cartesian input and raw transformations,
and between its lax output and strict transformations. The inherited
higher-cell controls remain in the emitted prefix.

Next qualify represented opposite-direction composition and the canonical
outer x-naturality relation in the selected outline. Prefer a strict identity
root if its whole higher action checks; retain the lax default for other
transformations. The standing scope remains the Q operations Homd consumes.

```bash
python3 audits/strict-default-action-boundary/cart_homd_section_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_homd_section/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_homd_section/candidate.lp --strict
```
