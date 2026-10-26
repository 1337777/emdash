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
  laws;
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
