# General displayed maps and intrinsic action for Cartesian-family Homd

Date: 2026-10-14
Status: non-library relative root and intrinsic projection checked;
nonidentity comparison computation and full coherence remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [selected family/section interface](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owners: [relative definitions](cart_homd_relative.lpfragment), [intrinsic action](cart_homd_intrinsic.lpfragment)
Controls: [relative consumers](cart_homd_relative_controls.lpfragment), [intrinsic consumers](cart_homd_intrinsic_controls.lpfragment)
Replay: [one integrated candidate](cart_homd_relative_replay.py)
Evidence: [exact verification](cart_homd_relative_verification.json)

## Defined general-FF action

Let D,E:K->Cat_cart. FF:D=>E remains a default lax transformation across K.
Its diagram image is fixed postcomposition by the whole iota:Cat_cart->Q;
its component is iota(FF[y]). No strict-FF admission or fibrewise opposite
of FF is used.

The target-family parameter is internalized as a whole ordinary Hom functor,
then reindexed along the represented x-package. Its object at iota E is
the existing H_E. Its first Hom supplies

```text
target_con_func(D,E)
  : T(Transf_{K,Cat_cart}(D,E)) -> Hom_Cart(K,Cat_cart)(H_E,H_D).

target_map(FF) = target_con_func(D,E)[FF]
homd_rel_int(FF) = target_map(FF) o homd_id_int(E).
```

Both the whole target action and the relative root are definitions using
ordinary Hom, transpose of strict functors between categories, reindexing
and composition. A modification FF=>GG has the corrected direction
target_map(GG)=>target_map(FF). A negative consumer rejects the unreversed
direction. This does not turn the original FF into a strict family map.

The x-component is whole transposed precomposition on the section category.
The literal root's x/u projection agrees with the direct whole section
composition h_E(x,u) o iota(FF). Its y/v/f projection computes to
`Hom_E[y](E[f](u),FF[y](v))`. The identity FF returns the identity Homd root.
This extends the actual root, not a separate primitive relative Homd theory.

The first literal-leaf consumer exposed a stable-precomposition normal form.
A scoped fold at the Hom-precomposition owner now exposes composition when
its value is the canonical mate. Generic pre/postcomposition owners remain
distinct, and no outer evaluation/inner-cut rule was added. Whole/capped
ordinary postwhiskering and Cartesian prewhiskering component laws are also
qualified by their actual consumers.

## Intrinsic action and extraction

For this paragraph write FF,GG:E=>D. The existing internal-action pattern
has a corrected Cartesian-family type:

```text
B(FF,GG) = homd_rel_view(GG) o FF : E => H_E

tdapp1_int(FF,GG)
  : Hom_Transf(FF,GG) -> Hom_Transf(B(FF,GG),homd_id_view(E)).
```

The ordinary root views are actual inclusions of the canonical strict
roots. The whole intrinsic action remains a structural constructor; its
type does not constitute a derivation of all higher coherence. This is the
adaptation of the native tdapp1/fdapp1 architecture, not a new independently
supplied compositor or laxity witness.

Its projections are definitions. After x and u, the T(S_E) target gives
an arrow in S_E from h_E(x,u) to the corresponding relative section. The
y/v/f projections use the actual Cartesian component functors. They give

```text
Hom_E[y](E[p](u),v)
  -> Hom_D[y](D[p](FF[x](u)),GG[y](v)).
```

For GG=FF, evaluate the whole action at the identity modification of FF.
Then evaluate the projected Hom functor at the identity filler at `E[p](u)`.
This defines forward laxity with type

```text
D[p](FF[x](u)) -> FF[y](E[p](u)).
```

The caller supplies only FF, not an extra comparison cell or proof. The
extractor does not depend on sigma_map_func. A normality clause at the
deep internal-action owner covers the identity displayed map. Its full
projection chain computes to the identity Hom functor and identity laxity
cell. It does not make the identity modification of an arbitrary lax FF
produce identity laxity; the generic two boundary objects remain distinct
in the rejection control.

The new operators provide a typed extraction route and a concrete identity
computation. Nonidentity beta laws for the canonical mate's y-comparison
and complete higher coherence still need qualification. Do not report those
as derived merely because the whole action has been declared.

## Verification and continuation

The candidate passes with subject reduction enabled under the default
90s/2GiB/64MiB serial profile. Source/authoring/receipt/log hashes and resource
measurements are recorded in the evidence. Replay emits the checked bytes;
the LHS audit has zero unreviewed compound slots.

Critical-pair diagnostics change 1158->1170; the 66 replaceable-variable
warnings are unchanged. Added bodies concern Cartesian prewhiskering (2),
dual precomposition (3), the diagram inclusion (4) and intrinsic identity
normality (3). Five expected rejection diagnostics are recorded separately.
No global confluence claim or removal matrix is added.

Next connect the canonical ordinary internalizations to these Cartesian
family inputs and qualify the nonidentity mate comparison computation.
The corrected Sigma-Hom and public migration remain required. Keep the
represented-operation scope: a full general profunctor library is not a
prerequisite.

```bash
python3 audits/strict-default-action-boundary/cart_homd_relative_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_homd_relative/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_homd_relative/candidate.lp --strict
```
