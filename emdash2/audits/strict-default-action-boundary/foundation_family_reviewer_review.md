# Family reviewers: corrected coefficient and opposite-reindexing views

Status: four complete original reviewers pass in a non-library candidate;
production adoption and broader qualification remain pending. Parent checkpoint:
`bc13656f`. The [replay](foundation_family_reviewer_followup.py) validates every
source pin before changing an idle candidate. The
[verification](foundation_family_reviewer_verification.json) retains the exact
sources, receipts, failed predecessor and warning comparison.

The four files retain all original assertions and add one whole-inclusion type
check: 32 positive and nine negative assertions in total.

- `higher_sieve_classifier` uses its existing Cartesian classifier. The
  ordinary presheaf category retains lax maps and its existing whole inclusion;
  sharing objects does not identify their mapping categories.
- `join_cross_computation` uses `Cat_cart` for family action and the ordinary
  `hom_int_view` where the original internal-action consumer requires it.
- `sigma_section_projection_views` compares fibre transpose over `CoAt2(K)`
  and reindexes through the actual `CoAt2_func` of the supplied composite.
  Its different-family negative is retained.
- `sigma_total` corrects two component coefficients. Sigma totalization still
  lands in public `Cat_cat`; its whole-map/runtime distinction is unchanged.

The Sigma section consumer exposes one existing unifier whose right pattern
contained `CoAt2_func(comp(F,G))`. Strict functoriality normalizes that argument
before matching. Its replacement matches the resulting composite of the two
actual images. It retains the original family and both maps. This replaces
one existing comparison at its owner; it adds no primitive, runtime rule,
folding rule or supplied equality argument.

The complete focused source check passes cold with subject reduction enabled:
`20261025T025126Z-f4828c099ad849cb86949ddeb145f6d5`, 53.789 seconds and
168,960 KiB maximum child-process RSS, at 90s/2GiB/o=20. The matched warning
body sets are identical (1,704 each); the rule audit has zero unreviewed slots
and 79 annotated slots across 53 clauses. Manual review of the changed unifier
is separate from that generic rewrite audit. Exact replay reproduces all six
outputs byte-for-byte without compiled objects.

The subsequent 74-reviewer traversal passes these earlier family consumers
and stops at an old `Cat_cat` annotation in path induction:
`20261025T025602Z-abdd7ea190374c37acc1e2009e3469fb`, 53.474s/214,984KiB.
The cumulative target had explicit 180s headroom following the prior 85.529s
partial traversal; the memory cap stayed 2GiB. It is a typing failure, not a
resource stop. Continue the original reviewer migration at that owner.

The qualified production package, its counts, the five terminal Homd runtime
requirements and the normalization/performance gates are unchanged. This
checkpoint records a passing bounded continuation, not completed migration.
