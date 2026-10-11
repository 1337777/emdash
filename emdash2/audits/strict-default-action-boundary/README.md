# Strict-default action owner audit

Status: non-library implementation pilot; no production rule is promoted.
Plan: [SF-0 / SF-1](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
Source: main `f8af1fca472657ff1598c639eb29c0566e7b2ec0`; the replay pins the
core and profile source hashes and inserts at unique original owner anchors.

The question is whether the public native action can regain strict functor
computation while retaining arbitrary transfor comparison data and the
existing intrinsic compositor extraction. All candidate rules are in full
copies of the nucleus, before later owners. The first real consumer imports
an unchanged copy of `emdash3_2_gray_profiles.lp` from an isolated package.

| Variant | Expected result | What it isolates |
| --- | --- | --- |
| `baseline` | pass | Original composition and whole endpoint comparisons remain negative; retained action controls pass. |
| `capped` | pass | The single restored composition cut gives strict capped and iterated-Hom action; whole endpoint comparison remains negative. |
| `whole` | pass | Whole post/pre strict functor laws identify the actual endpoints; the extracted compositor is still not identity. |
| `intrinsic` | pass | The actual whole-action projection computes to identity, with the existing defined accessor unchanged. |
| `raw_endpoint` | expected assertion failure | A capped-only patch does not identify the stable represented-composition history with raw composition. This is not a semantic counterexample. |
| `projection` | expected assertion failure | Whole-first evaluation passes, but the already capped postcomposition history needs its own projection join. Both compared terms first typecheck in the same Hom. |
| `joined` | pass | Both post/pre cap-first histories agree after their semantic-owner clauses are added. |
| `profile_consumer` | pass | The existing `IsStrictFunctor(F)` property is derivable without an admission input; different transfor classifiers remain distinct. |

The final full-file pilot has 19 positive and three negative assertions.
The latter compare the two naturality routes and the off-diagonal action of
an arbitrary transfor; each term is separately typechecked. No proof/path is
an argument to an action operation. The compatibility theorem in the profile
consumer produces a proof of the old late property; it is not a new input
contract for default functors.

The candidate does not qualify corrected Op, Q, Homd, every constructor's
strict action, or global confluence. Its warning inventory increases from
648 to 796 unjoinable-pair reports. The 148 additional reports, including
Op, identity, composition, evaluation, products, Hom and family projections,
are promotion obligations. Adding the intrinsic-cell clause itself adds no
warning beyond the whole endpoint laws in this replay. Counts are diagnostic
evidence, not a judgment of which pairs are harmless.

## Replay

From `emdash2`, emit the exact source copies into the already ignored
`tmp/probes/strict_default_action/` tree:

```bash
python3 audits/strict-default-action-boundary/replay.py
```

Check any positive full-file variant with the standard bounded guard:

```bash
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  tmp/probes/strict_default_action/joined.lp
```

The real profile consumer resolves imports exclusively in its generated
package; no installed kernel, main worktree, or cache is modified:

```bash
EMDASH_LAMBDAPI_WARNINGS=1 OCAMLRUNPARAM=o=20 \
  python3 scripts/run_lambdapi.py --quiet \
  --package-root tmp/probes/strict_default_action/package_joined \
  profile_consumer.lp
```

`raw_endpoint.lp` and `projection.lp` must fail at the documented assertions,
not at a declaration, parse, resource, or subject-reduction check. Their
failure establishes the missing computation in that intermediate variant,
not impossibility of the final design. `verification.json` records the
exact emitted hashes, receipts, outcomes, warning counts and measurements.
Raw logs and complete generated source copies stay ignored; fragments and
the replay remain tracked for recovery.

Replay trigger: any edit to the action, composition, represented Hom,
intrinsic-cell or profile owners, or before promoting these clauses. Source
pin changes require review. Retire this experimental builder after a
qualified library promotion and retain its evidence in Git.
