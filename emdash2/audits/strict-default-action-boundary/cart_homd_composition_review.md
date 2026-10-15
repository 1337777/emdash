# Represented-composition beta for the extracted Homd comparison

Date: 2026-10-15
Status: non-library whole/capped generator beta and first higher action checked;
consumed whole-action checks, Sigma-Hom and production migration remain open
Plan: [foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Outline: [Cartesian families and lax sections](../../../docs/EMDASH_CARTESIAN_FAMILIES_LAX_TRANSFORS_HOMD_OUTLINE.md)
Owners: [projection and generator computation](cart_homd_composition.lpfragment), [strict functor law](cart_homd_composition_functor.lpfragment)
Controls: [actual consumers](cart_homd_composition_controls.lpfragment)
Replay: [integrated candidate](cart_homd_composition_replay.py)
Evidence: [exact verification](cart_homd_composition_verification.json)
Predecessor: [ordinary internalization](cart_homd_ordinary_review.md)

## The implemented computation

The actual extracted Homd y-comparison now computes on the represented
composite's generator:

```text
q:y->z, f:x->y, k:x->z
beta:k=>qf, a:E[f](u)->v

comparison(q)[v][k](intro(beta,a))
  -> E[q][a] o E[beta][u].
```

The comparison is still obtained from the intrinsic tdapp1/fdapp1 action,
through ordinary transformation internalization. Neither the constructor nor
its caller takes a separately supplied comparison cell or equality proof.
The tested expression starts with `sf_cq_homd_y_comparison_vk`, rather than
an independently declared local map with matching endpoints.

The more general whole beta uses a Cartesian diagram map U:E=>D. At
d:D[y], e:E[y], e':E[z], its generator has category

```text
Hom_E[z](e', E[q](e)) x Hom_D[y](U[y](e), d).
```

The generator is introduced into the actual Q composite
`iota(E[q]) o U[y]*`. The extracted mate comparison maps it by the whole
functor `(beta,r) |-> D[q][r] o U[z][beta]`. That functor is an actual
composition of the two Hom-action functors, product projections and
ordinary composition. U's strict naturality supplies the middle endpoint
agreement. Substituting `U=c_E(x,u)` gives the displayed Homd formula.

This introduces structural generation and beta laws for the selected Q/mate
construction. It does not derive those laws from an arbitrary category
having the same Hom objects, or construct general coend universality. The
introduction is restricted to the represented cospan consumed by the mate;
the existing general Prof convention and library are untouched.

## Stable native projections resolve the computational issue

An initial attempt folded the fully expanded scalar extraction. Subject
reduction required endpoint guards, and those guards stopped matching when
canonical components reduced. The failed recipes and their immutable input
receipts are retained as development evidence; those guards are not in the
selected source.

The selected implementation uses the existing architectural pattern:

```text
tdapp1_int[theta]
  -> at x
  -> at u: section modification
  -> at y: Q-Hom transformation
  -> at v: index transformation
  -> at p: whole filler functor.
```

Each step has a stable projection head reached from its typed parent.
`theta` is the original modification FF=>GG, not a laxity witness. The
ordinary comparison remains a definition using theta=id_FF and the source
identity filler. The canonical mate comparison and its two local component
rungs are then stable projections of that extraction. Both a general mate
and the actual Homd specialization reach these heads by runtime conversion.

The new data/projection symbols are not declared injective. In particular,
the generator does not assert injectivity that could conflict with later
balancing relations. Identity-map normalization is retained on every new
intrinsic rung, without collapsing general lax FF's naturality boundaries.

## Strict computation and higher action

The Homd beta also needs E to preserve composition expressed at the stable
ordinary Hom-postcomposition head. The new strict-default rule maps that
head to postcomposition of F's images. It is inserted immediately after the
existing postcomposition object projection, before its subsequent consumers.
It preserves the represented runtime head; it does not globally equate
precomposition, postcomposition and raw composition.

The rule is valid under the selected strict Functor default. Its identity,
constant and composite-functor consumers check. A separate narrowly guarded
proof-time naturality comparison is validated by typed reflexivity for
Cartesian U; the inherited general-lax FF rejection control still passes.

The generator beta checks as a whole functor and at the literal Homd leaf.
Its first Hom also checks in both relevant orders: observing the whole
composite first, and mapping a higher generator input before applying the
comparison. The latter needed the corresponding whole/capped first-Hom
projection clauses. The higher input is retained in the resulting actual
Hom-action functor.

## Validation and remaining boundary

Receipt `20261015T070112Z-cbb9afe835b14daea2919add2947636c` passes with subject
reduction enabled in 9.200s, maximum child RSS 250,776KiB. Resource limits
remain the serial default 90s/2GiB/64MiB with OCAMLRUNPARAM=o=20. Replay
pins the checked source and all authoring inputs. The LHS audit has zero
unreviewed slots.

Critical-pair diagnostics change 1174->1269; replaceable-variable warnings
remain 66. The added bodies group as 68 strict-functor preservation, 11
projected Q units, 20 intrinsic projection/unit, and 6 higher-generator beta
diagnostics. Ten old bodies are replaced by changed diagnostics at the same
overlap terms; they are not ten resolved pairs. Exact hashes and replacement
pairs are recorded. These focused typed consumers do not establish global
confluence or a complete model of Q.

The generator beta alone does not establish that every element of the
opaque composite is generated or prove a complete model of Q. The user's
subsequent scope clarification keeps such general balancing/coend work out
of the prerequisite path: composition remains synthetic, as in production
Prof_tensor. Check the unit/composition interactions demanded by actual
Homd/Sigma consumers. Sigma-Hom and public/downstream migration remain
required; the optional balancing-image experiment is not a blocker.

```bash
python3 audits/strict-default-action-boundary/cart_homd_composition_replay.py
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  scripts/probe.sh tmp/probes/cart_homd_composition/candidate.lp
python3 scripts/audit_rule_lhs.py tmp/probes/cart_homd_composition/candidate.lp --strict
```
