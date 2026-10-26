# Native nerve adaptation: receiver evidence

Status: non-library NF-1 candidate on the corrected foundations.
Owner: [adaptation plan](../../../docs/EMDASH_NATIVE_NERVE_FOUNDATIONS_ADAPTATION_PLAN.md).
Receiver baseline: `e8ffc4d0`; legacy donor: `280e7a03`.

## Whole walking observer and tensor coordinate family

[`walking_observer.lp`](walking_observer.lp) is a fresh receiver construction,
not a copy of the legacy oplax classifier. It contains definitions and
focused observations only: no new axiom, rewrite rule or unification rule.

Writing I for WalkingArrow, G(C)=Functor_oplax_cat(I,C) and
N(C)=LaxArrow_cat(C), it constructs

```text
Observe_C : G(C) → N(C)
L_B       : B → G(I⊗ᴿB)
Observe_(I⊗ᴿB) ∘ L_B : B → N(I⊗ᴿB).
```

The first map is the existing native graph applied to the current whole
oplax-diagram evaluator. Its LaxTransfor admission is derived from the default
pre/right computation, rather than supplied by the caller. The original
input diagram's generator is recovered using the existing admission-carrier
path. This path is proof-only comparison data; no operational map takes an
equality certificate as an argument.

The whole first action computes to the existing native square constructor,
with both side arrows and the typed `gray_transf_standard_cell` retained.
That cell is already defined from internal post/left laxity; it is not a new
filler. The next Hom is a functor obtained by applying the same observer's
generic action again. General post/left naturality is not made strict.

L_B is constructed from right coevaluation, the existing Gray-Hom inclusion,
and the current mixed exchange. It requires none of the legacy candidate's
separately supplied strict-object admission properties. At B=I the resulting
native coordinate family recovers both original outer-coordinate edges of
the Gray walking square. This is a concrete whole tensor consumer, not yet
the whole closure map for arbitrary tensor diagrams.

## Exact boundaries

The construction inherits the existing graph, right-closure, duality and
evaluation interfaces at the pinned receiver source. It does not prove an
independent semantic model of those structural declarations.

Still required:

- general native universal-arrow realization and both whole walking inverse
  laws (the isolated realization candidate below now supplies the forward
  construction; its prerequisite is not promoted);
- comparison of the observed tensor square's filler with the separately named
  `gray_interchanger`, including its higher observation;
- whole opposite closure in arbitrary tensor diagrams and its reverse map;
- all subsequent NF cube, simplex, common-index and degeneracy obligations.

The raw expanded generator assertion failed through the retained admission
view. Replacing it with typed reflexivity alone also failed. The accepted
object comparison uses the already available whole admission-carrier theorem
and equality action; no expression-fold rule was introduced.

A hand-expanded square assertion failed while checking its inline cell's
endpoint presentations. The retained assertion uses the existing typed cell
owner and checks the complete square. Its underlying internal-action body is
unchanged. This does not qualify arbitrary inlining of that body; retain the
failed source snapshot if such an expanded view later becomes a real consumer.

## Replay and evidence

From the repository root, use the supported checker with the usual guard:

```bash
nerve_checker_dir="$(python3 scripts/verification-toolchain.py batch-path)"
PATH="$nerve_checker_dir:$PATH" OCAMLRUNPARAM=o=20,v=1024 \
  EMDASH_LAMBDAPI_WARNINGS=1 \
  python3 emdash2/scripts/run_lambdapi.py --no-colors --quiet \
    --timeout-ms 90000 audits/native_nerve_foundations/walking_observer.lp
```

The [verification record](verification.json) retains source/checker hashes,
the original diagram-evaluation baseline, failed hypotheses, retained replay,
resource measurements and warning comparison. Logs and exact input blobs
remain in the receiver's ignored receipt store. No production owner or check
registry entry is added by this non-library checkpoint.

## Native realization and whole generator recovery

[`walking_realization.lpfragment`](walking_realization.lpfragment) constructs
`Realize_C : N(C) → G(C)` using the existing transformation-to-walking-diagram
operation. It adds one structural owner, the native universal transformation
`U_C : src ⇒ tgt`, with six projection rules. Its point component is the
stored native arrow, its whole right Hom action is existing postcomposition
after source action, and its extracted post/left cell recovers the original
native square filler. The unit rules are specific to this projection; general
lax naturality remains nonidentity. A protected typed identity view uses an
existing postcomposition comparison without a new unification rule or an
equality argument.

The existing mixed diagram exchange derives a comparison of the **whole**
realized walking family with `walking_arrow_func(src,tgt,U_C)`, and hence
recovers the entire transformation U_C at its generator. These are defined
reflexivity proofs, not new inverse axioms. The new U_C itself is structural
data, not a theorem derived from the previous Sigma projection rules. Neither
whole walking inverse is established by this checkpoint.

The candidate requires the two identity instances in
[`total_dual_postcomp_units.lpfragment`](total_dual_postcomp_units.lpfragment).
They are inserted at the existing postcomposition owner in an isolated copy:
total duality erases the identity's original category tag, so the ordinary
identity pattern does not cover this source presentation. Whole, capped and
higher identity observations pass, with a negative control for an arbitrary
nonidentity arrow. Production sources remain unchanged.

The [realization record](realization_verification.json) pins every input,
the exact patched core, replay artifacts and sixteen measured attempts. The
retained candidate passes in 46.854s / 288,032 KiB with subject reduction and
the 180s / 2 GiB guard. Its eight positive and two negative controls exclude
the inherited observer checks. All five warning inventory fields equal the
patched-import baseline. The two core instances add **31 reported critical
pairs** relative to the unmodified imports, in nine recorded head families;
their full overlap/owner qualification is still a prerequisite to promotion.

A local alternative using generic typed unit views passes subject reduction
without the core instances but fails the actual unit-component check. It is
not adopted. Two earlier 90s timeouts occurred in unchanged imports, before
the new whole comparison; the later timed replay locates 108.15s in the first
import and no candidate command above 0.5s. This is not evidence that the new
comparison itself needs that time, nor a reason to alter resource defaults.

Replay the isolated candidate from the repository root:

```bash
python3 emdash2/audits/native_nerve_foundations/replay_realization.py \
  --timeout-seconds 180 --timing
```

`--mode units-baseline` checks the same imports with the two core instances.
`--mode without-units` retains the failed omission control and its actual
nonzero status. The replay enforces source/checker pins and uses the existing
serial guard. No broad health or integration check is required to retain this
non-library experiment. Next: whole graph reconstruction and the two actual
inverse laws, with the prerequisite boundary kept visible.

## Whole reconstruction of oplax walking families

[`walking_generation.lpfragment`](walking_generation.lpfragment) derives,
for arbitrary K, C and D:K→G(C),

```text
transf_arrow_diagram(eval₀∘D, eval₁∘D, generator(D)) ≐ D.
```

Here `generator(D)` is the entire ordinary-lax transformation obtained by
mixed evaluation of the oplax diagram family. The proof first reconstructs
the whole functor I→Functor_cat(K,C), then applies the existing opposite-profile
exchange and its double-exchange computation. It retains all parameter action;
it is not reconstruction from pointwise equality or a OneCat restriction.

The proof uses one explicit structural source-generation comparison in
[`walking_generation_self.lpfragment`](walking_generation_self.lpfragment):
self-recursion of the walking shape's original edge is its identity functor.
This comparison is inserted before the existing postcomposition cut in the
walking introduction owner. It is not inferred from beta-only Join, and it
is not an Observe/Realize inverse axiom. The current kernel already supplies
the donor's other prerequisite, strict postcomposition of walking recursion,
so no second postcomposition or exchange-congruence rule is copied.

The [verification record](generation_verification.json) pins fifteen receiver
inputs and the retained replay. The no-comparison control fails at exactly
the source-generation proof. The owner-position candidate passes in 126.613s /
274,716 KiB under 180s / 2 GiB, including a negative control for a different
opaque edge. Its import command accounts for 125.66s; no subsequent command
reaches the 0.5s timing threshold. Warning categories, head families, term
heads and parser issues are unchanged; two existing warnings merely move
from owner line 44 to line 54. This slice does not require the realization's
unpromoted core-unit instances.

```bash
python3 emdash2/audits/native_nerve_foundations/replay_generation.py \
  --timeout-seconds 180
```

`--without-generation` reproduces the omitted-law failure. Production sources
are unchanged. The next missing input to the walking inverse derivation is
the native graph's **whole** source, target and universal-transformation
projections. Its currently checked point/square projections do not alone
supply those comparisons; retain that distinction when adapting the donor.
