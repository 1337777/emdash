# Foundational reviewer continuation: unadopted candidate

Date: 2026-10-24
Status: investigation in an isolated package; no production or qualified-package adoption
Predecessor: `4cc4ad4c`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

The [living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md) continues the remaining complete reviewers. The current group comprises 74 files, 37 original declarations, 651 positive and 161 negative assertions. Fifteen native/homology reviewers remain outside this resource group. The qualified package and its 1,361-input evidence map remain unchanged; no new complete-reviewer count is claimed here.

## Findings and candidate changes

The contravariant reviewer distinguishes the general native con-action ladder from its explicit ordinary-opposite presentation. The native ladder still accepts general lax transformations. The direct ordinary-opposite comparison now uses a strict transformation and the existing ordinary inclusion of its opposite. The coefficient and whole family views are updated to their actual `Cat_cart`/`hom_con_int_view` types. Both comparison orientations and the original noncollapse observations are retained.

The whole comparison then exposes a missing congruence through an existing mapping inclusion. The core already compares compositions with a common precomposing functor. The isolated candidate adds its same-postcomposer counterpart at that owner: compare all source/middle/target categories and require equality of the remaining functors. This is sufficient congruence, not cancellation or a runtime fold. With it, the complete nineteen-assertion contravariant reviewer passes from source as `20261024T202330Z-df3da54795804569a59975260fac1aa2`. A separate diagnostic checks that arbitrary input functors are not identified, while existing constant-postcomposer computation remains available. It passes as `20261024T203556Z-b3ad3e8d032846bf9ffbd42fe2533647`, with compiled imports.

The dependent-Hom reviewer now states the already implemented total-dual Sigma–Hom formula. Diagram constant/exchange observations use their actual Cartesian classifiers. General fixed-point evaluation remains on the ordinary lax transformation interface, through the existing whole evaluation functor. Composition observations retain the canonical precomposition owner at runtime and the separate raw composition presentation at proof time. These diagram reviewers complete in the intermediate compiled run `20261024T203232Z-5bd92230984641b6ac415dc3046e0034`, which then fails at the next displayed-evaluation file. That failed aggregate is not reported as a pass.

Redundant strict-functor wrappers in the two remaining affected reviewers are retired in the candidate. The displayed-evaluation source-family and leading-Eval helper have only their initial coefficient/inclusion corrections so far. Its full migration remains unfinished.

## Open displayed-evaluation boundary

Twelve of its original 35 assertions use the retired raw same-base `Op_funcd` contracts. The current `Op_funcd` accepts Cartesian diagram maps and shifts the base by `CoAt2_cat`. In particular, pairing arbitrary lax maps or arbitrary lax sections is not automatically a classified input for that operation. These assertions need a lawful shifted/profiled construction preserving their whole projection-order intent. They must not be discharged by omitting them, replacing them with object checks, or silently strictifying all `Functord`.

An isolated ordinary diagnostic slice distinguishes these twelve obligations from the other 23 assertions. It passes the generic displayed identity computation but fails the terminal specialization (original assertion 18), so it does not qualify even that entire slice. Its one intentional polarity correction is the original general-functor composition negative, which becomes positive under the strict public functor contract; arbitrary section/transformation noncollapse remains required.

The [normal-form trace](foundation_reviewer_candidate_terminal_trace.lpfragment) identifies the remaining expression:

```text
λ K x y p,
  fapp1_fapp0 K Terminal_cat
    (id (Catd_cat K) (Const_catd K Terminal_cat)) x y p
```

Thus the displayed identity has been read as a functor into the terminal category before its arrow action computes. The next experiment should inspect this canonical constructor's action at the actual projection owner, preserving the whole identity head and generic noncollapse. No broad terminal eta, new terminal inverse or replacement Homd theory is justified by this observation.

## Validation boundary and resources

[Evidence](foundation_reviewer_candidate_evidence.json) preserves exact outcomes and snapshots. The shared-core candidate is not covered by earlier source receipts. The existing `selected_presentation_core_regression.lp` diagnostic first reaches its 90-second deadline; a 300-second/2-GiB continuation terminates with allocation failure during OneCat modification imports. After confirming about 21.5 GiB available host memory, a 4-GiB continuation reaches adjunction introduction before 300 seconds. The unchanged diagnostic then passes at 600-second/4-GiB headroom in 314.382 seconds, reporting 2,971,152 KiB maximum child-process RSS (`20261024T204643Z-520f5df8d3964b45a910978e7a06de3e`). No normal default, formal rule or runtime setting is changed to compensate for host load.

For resource planning only, the same named regression has earlier cold evidence at 801.054 seconds and 3,448,592 KiB (`20261023T110127Z-6a89db121d8d436388521669ee625e4c`). Its source snapshot differs, so it is not a matched before/after performance result. Compiled-import runs are intermediate diagnostics; final qualification still requires source-level checks and the affected library scope. A fresh cold replay of the complete contravariant consumer plus the noncancellation/constant controls passes in 35.376 seconds (`20261024T205347Z-5433a151e6174d72a21cb62de141d6a5`). All 1,612 warning occurrences belong to previously reviewed contexts. This bounded source evidence is not full shared-core/library qualification.

## Replay

The [source-pinned builder](foundation_reviewer_candidate.py), [input inventory](foundation_reviewer_candidate_inputs.json), [composition clause](foundation_reviewer_candidate_congruence.lpfragment) and [controls](foundation_reviewer_candidate_controls.lpfragment) reproduce every candidate reviewer, the core change and the full driver. The builder verifies the unchanged qualified parent, refuses an existing output directory and excludes compiled objects. It does not modify the production emitter or certify its output.

From `emdash2`:

```bash
python3 audits/strict-default-action-boundary/foundation_reviewer_candidate.py \
  --out tmp/probes/foundation_reviewer_candidate_replay
```

Then check the chosen target through `scripts/run_lambdapi.py` with the recorded isolated checker and explicit guarded profile. `whole_contravariant_review.lp` is the bounded successful consumer; `original_foundation_reviewers.lp` is the full still-incomplete group. Reproduction was checked byte-for-byte against the isolated candidate, including the core, both drivers and the two displayed diagnostics, with no compiled objects in the replay.

Next: resolve the terminal identity action and migrate the displayed Op cases at their lawful profile; finish every remaining complete reviewer and the cold shared-core/library qualification before adoption. The five terminal Homd runtime obligations, R07/R12 and final production gates remain. Separate application research stays paused.
