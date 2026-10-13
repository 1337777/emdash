# Raw represented counit: bounded source closure

This is a checked bounded construction experiment, not production qualification. The
builder emits an explicitly bounded owner prefix, constructor boundary, and
first-consumer source. It does not emit or claim a full-source continuation.

The source context is the pinned `strict_default_q_unit/emdash3_2.lp` before
its early `Prof_base` block. That prefix supplies strict default functors,
separate Cartesian and ambient mapping categories, the existing strict-
transfor inclusion, and the migrated `Unit_prof` action. It excludes the
prototype's Cartesian replacement of public `Prof_cat` and every Q owner.

After the prefix, the builder copies these exact existing production owners
without changing their signatures, bodies, or rules:

- The public Prof classifiers, including the raw `Functord_cat` Hom rule,
  `Prof_reindex_base_func`, and `ProfMap`.
- `Prof_reindex`, its fibre projection, and neutral identity reindexing.
- `Hom_prof_along`, `Hom_prof`, `Companion_prof`, and `Conjoint_prof`.
- Raw `Prof_transf_cat`, `Prof_hom_cat`, and `Prof_hom` aliases, so the
  first consumers can check preservation of the public shaped-cell profile.
- `Prof_tensor`, `Prof_imply_cov`, `Prof_eval_cov_map`,
  `Prof_lambda_cov_map`, and the existing closed beta/eta rules.
- The existing implication-reindex rule, `Prof_coyoneda_cov_map`,
  `Prof_reindex_transf`, its whole-fibre component, and identity reindexing.

`Unit_prof` is retained from the qualified strict-default candidate prefix;
its old production declaration and action are not duplicated. No tensor
map package, implication mixed-action package, shaped tensor introduction,
full co-Yoneda transformation package, or profunctor closed theory is added
merely to type this particular construction.

The proposed construction is:

```text
j_B = lambda_cov(coyoneda_cov(Unit_B))
    : Unit_B -> imply_cov(Unit_B, Unit_B)

j_F = reindex_transf(j_B, id_B, F)
    : Conjoint(F) -> imply_cov(Unit_B, Companion(F))

counit_F = eval_cov(j_F)
    : tensor(Conjoint(F), Companion(F)) -> Unit_B
```

The required target of `j_F` follows from the original implication-reindex
rule. The constructor supplies no equality, chosen inverse, map comparison,
or strictness witness. There is no implication-to-conjoint or Unit/Unit
implication rewrite. The identity control uses only neutral endpoint
reindexing and the original `eval(lambda(-))` beta.

The source pins guard the entire donor, production input, package file, and
the recorded q_unit verification file. The latter is checked against the
explicit donor hash by the source-pin set, not treated as qualification of
this new replay. Generated manifests also record each extracted block's
source location and hash, the exact upstream prefix hash, authoring hashes,
output hashes, and proposed control counts. Changed source pins require
review; the builder never updates them automatically.

The raw production blocks are read from the pinned baseline Git object, not
the working file with its still-uncommitted carrier relocation. Review found
all 21 extracted blocks byte-identical across that relocation; switching the
input to the baseline changed source locations but no emitted Lambdapi bytes.
The replay therefore does not depend on that pending production edit.

Run authoring validation without emitting files:

```bash
python3 emdash2/audits/strict-default-action-boundary/raw_represented_counit_migration.py --check-authoring
```

Emission, when requested by the root checker owner:

```bash
python3 emdash2/audits/strict-default-action-boundary/raw_represented_counit_migration.py
```

The builder does not invoke Lambdapi. Checker runs remain serial, bounded,
warning-enabled, and subject-reduction-preserving under `emdash2/AGENTS.md`.
Suggested first targets are `owner_prefix.lp`, `constructor_boundary.lp`,
then `first_consumer.lp` in `tmp/probes/raw_represented_counit/`.

Passing these targets would establish the bounded raw native construction,
identity computation, first whole-fibre consumers, and tested noncollapse
boundaries. It would not establish Cartesian admission, tensor-generator
evaluation, balancing in the middle category, triangle coherence, arbitrary
Q composition, the represented lift, or later production consumers. The
negative strictness check asserts the absence of implicit admission; it does
not assert that the canonical counit is mathematically non-strict.

## Native review boundary

The raw constructor and the identity/lambda/non-collapse consumers pass.
The original-rule whole-component boundary fails because eager implication
reindexing removes the family head needed by the generic component rule.
The separately emitted comparison_variant retains that runtime head and changes
the whole law to proof-time comparison. A single comparison matches rigid
outer heads and compares the reindexed target inputs in side conditions;
these inputs may already have normalized. It keeps j_F's return annotation
at the reindexed family. Both the general and represented comparisons are
tested by typed reflexivity; the
canonical target and whole component then check. All operational bodies are
unchanged. This policy remains a candidate pending downstream qualification.

The earlier nested-pattern comparison plus a specialized Unit/Unit instance
passed the represented component but failed the later general-law test. That
failure is retained as historical evidence, not counted as a passing variant.

The fibre-only comparison variant is a failed smaller attempt, not an
accepted fix. The verification JSON distinguishes this failure, original
component boundary, and removal controls from positive construction evidence.
Cartesian admission, generator/balancing computation and triangle coherence
remain open; the replay supplies no strictness evidence argument.
