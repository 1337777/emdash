# Pi/Sigma uncurrying: higher-profile audit

Status: correction applied to the active native files; production core and focused consumers pass; frontend and final integration pending.
Owner: [correction plan](../../../docs/EMDASH_SIGMA_SECTION_PROFILE_CORRECTION_PLAN.md).
Baseline: `81157237`; the isolated evidence below retains that original source boundary.

## Native integration

The [frontend candidate record](frontend_candidate.json) and
[patch](frontend_candidate.patch) preserve the unfinished TypeScript work
against `bc37e5fc`. The tested binder/transfor portion passed 13 cases with
one optional native check skipped; later demo edits and the full chain/PathInd
consumer closure remain unqualified. This is not active source or a claimed
frontend migration. The user corrected the scheduling: native nerve work
continues independently of this later frontend integration obligation.

The four active native source/reviewer files now exactly match the qualified
patch outputs. The [integration record](integration.json) pins those bytes,
fresh production core and focused-consumer receipts, unchanged warning
inventory, and the actual frontend consumers still requiring adaptation.
The core passes in 35.016s / 168,656 KiB and the focused Sigma/PathInd/J
consumers in 47.164s, both under 90s/2 GiB with subject reduction. All 141
existing source/package files from the completed central/groupoidal closure
rehash exactly; its 537.190s result is carried-forward content evidence, not
a newly executed aggregate.

Registry, rule-LHS audit, catalog, source TOC and report-header checks pass.
Broad health/final-integration obligations remain open. The TypeScript binder,
displayed-next-Hom and PathInd transfers still use the retired comparison or
folds. Their old pins are not updated by this native installation; the four
passing historical scale tests do not qualify current native semantics.

Historical replay now takes the explicit `--source-revision 81157237` option.
Every source pin still applies, and omitting that option rejects active-source
drift. `--assemble-only` verifies the exact closure without running a checker;
all eight recorded modes passed that assembly check after this extension.

## The mismatch

The source uses `Cat_cart` for family coefficients. In particular,
`tdapp0_fapp0` of a displayed modification returns a `StrictTransfor` between
its fibre functors. Before this correction, it also identified the whole
section category over a Sigma projection with `Functord_cat`, and folded its
object and next-Hom classifiers to the displayed ones.

The terminal-base specialization reveals the problem. Semantically, for
R=const(A), D=const(B) over 1:

```text
Σ₁ R ≅ A
Π_(Σ₁ R) π₁*D ≅ Functor_cat(A,B)          lax transformation maps
Functord₁(R,D) ≅ Functor_cart_cat(A,B)    strict transformation maps
```

These are semantic specializations, not claims that the native checker has
already implemented the terminal equivalences. The canonical forward map
keeps the functor objects and strict fibre transformations, but it does not
cover every lax transformation on the section side. Thus the full canonical
category identification is incompatible with the selected profiles.

The external convention check is [Ara–Guetta, v1, introduction and §2](https://arxiv.org/html/2503.08832v1#S2):
their Cartesian universe has strict higher transformations, while the lax
and oplax mapping structures are distinguished. The kernel-specific diagnosis
here is our specialization of its declarations, not a result attributed to
that paper. Repository source and its selected orientation remain authoritative.

## Finite witness

[`semantic_model.py`](semantic_model.py) constructs the strict 2-category

```text
0 ──u──▶ 1
│        │
a        b
▼        ▼
2 ──v──▶ 3

χ : v∘a ⇒ b∘u
```

The two composite arrows remain distinct, and χ is noninvertible. This finite
2-category has four objects, ten arrows and eleven 2-cells. The program checks
all finite unit, associativity and interchange cases. Its walking-arrow
functors have **38 strict** and **47 lax** transformations. In particular,
the functors selecting u and v have the lax transformation with components
(a,b) and comparison χ; those components do not form a strict transformation.
This uses the core's post/left direction G[p]∘η[x] ⇒ η[y]∘F[p].

The model also checks a representable-family witness. For the free 2-globe
p⇒q, its lax under-category has a triangle P,V,Q with a 2-cell VP⇒Q. Two
strict functors send that 2-cell to identities, while a lax transformation
between them uses χ on V. All its composition and 2-cell naturality conditions
are checked. Restriction to the vertical fibre is still non-strict. Therefore
representability alone does not justify the unrestricted identification.

The [recorded output](semantic_model_result.json) is reproducible with:

```bash
python3 emdash2/audits/pi_sigma_section_profile/semantic_model.py
```

This is a finite semantic audit, not a Lambdapi Empty proof, a model of the
entire universe, or a proof of a native nerve inverse. The mismatch concerns
the noninvertible cells required by the current construction.

## Isolated correction

[`profile_correction.patch`](profile_correction.patch) is against the pinned
production source and reviewers. It preserves `sigma_functord_sec_func` and
its object/component/higher-action projections, and removes only the broad
Pi/Sigma category comparison, object fold and next-Hom fold.

The affected path-induction fold now returns
`sigma_functord_sec(fib_cov_transf(...))` through the existing ordinary view.
It no longer treats the displayed map itself as a section over a different
base. The old reflexive comparison for that bare retyping is removed; the
path-category proof compares the actual structured transport expression and
becomes shorter. No new runtime or proof-time rule is added to compensate.

The isolated full core passes. The [focused controls](controls.lpfragment)
also pass with the projection, recursive Sigma-Hom and transitivity reviewers:
the forward functor and its whole Hom action remain, while implicit category
and carrier retyping are rejected. The [generic section view](generic_view.lpfragment)
that failed under the old classifiers now typechecks as the identity between
two presentations of the same pullback family.

The native common-totalization prefix passes on this corrected copy with that
plain identity view and without the experimental section-identity unifier.
The first walking inverse, original square computation and remaining native
identity rejection remain in its checked closure. This preserves the useful
native progress while avoiding the unsafe classifier identification.

Central validation and source integration remain under the plan. No existing
proof receipt is relabelled as a pass on the new core. The remaining native
section reconstruction still needs a derivation with its full higher profile.

For that later step, the same [paper's §7, Remark 82](https://arxiv.org/html/2503.08832v1#S7)
places comparison with Warren's explicit Grothendieck formulas in a separate
work. Its abstract comma construction therefore does not, by citation alone,
discharge the native total's implementation comparison. Keep the current
explicit maps and higher-cell checks as the acceptance evidence.

## Replay and measured scope

[`verification.json`](verification.json) pins the production inputs, the four
patched source/reviewer files, every retained run and the native parent
artifacts. [`replay.py`](replay.py) applies the patch only in an ignored copy
and checks its exact assembled source closure before invoking the normal
serial resource guard. It does not modify production or reuse a receipt as a
new theorem claim.

```bash
python3 emdash2/audits/pi_sigma_section_profile/replay.py --source-revision 81157237 --mode core
python3 emdash2/audits/pi_sigma_section_profile/replay.py --source-revision 81157237 --mode consumers
python3 emdash2/audits/pi_sigma_section_profile/replay.py --source-revision 81157237 --mode generic-view
python3 emdash2/audits/pi_sigma_section_profile/replay.py --source-revision 81157237 --mode native --timeout-seconds 180
```

The core passes in 35.763s, the initial focused consumers in 35.840s, the
generic section view in 37.878s and the native prefix in 134.600s, all at
2 GiB. The [core warning review](warning_comparison.json) and
[native warning review](native_warning_comparison.json) report four removed
critical-pair warnings, no new rule families and no parser issues. Warning
counts alone do not establish confluence.

The [consumer inventory](consumer_inventory.json) records the direct lexical
uses and the 138 production imports completed by the first central run. That
run failed at an old bare-section diagnostic; its positive comparison is now
derived using the existing transport/J theorem. The second run reached nested
PathInd observations that also used the wrong base. They now use `piapp0` at
the actual total object `(y,p)` and retain the same final `q ∘ p` computation.
Both focused repairs and all nine changed profile cases pass. These repairs
add no new core normalization rules and do not weaken the leaf computations.

The complete central/groupoidal gate passes in **537.190s / 2,550,112 KiB**,
under the existing 900s/4 GiB profile. All 2,441 central assertions are retained:
2,158 positive and 283 negative after the four classifier-expectation changes.

```bash
python3 emdash2/audits/pi_sigma_section_profile/replay.py \
  --source-revision 81157237 --mode central --timeout-seconds 900 --memory-mib 4096
```

Its first two failures remain recorded; neither is relabelled as a green
aggregate. The third frozen run supplies the completed evidence. Four rejection controls test absence of
unqualified classifier identification, not mathematical non-equivalence of
every guarded special case. Stronger special-case comparisons require their
own profile and actual maps.

The native files are now installed as recorded above; frontend and final
integration are still pending. The
[targeted prose inventory](prose_inventory.json) identifies the later
clarifications; the article's section evaluation at `(y,p)` is already the
correct route. No book or article artifact was changed by this audit.
