# Foundation reviewers: coefficient and telescope continuation

Status: focused continuation and the existing core regression pass; not
production adoption. Parent checkpoint: `7c39e44f`. The
[replay](foundation_reviewer_followup.py) applies a pinned delta to an idle
`telescope` candidate from the preceding displayed-action replay.

Four complete reviewers retain all 27 assertions (22 positive, five negative):

- Displayed identity uses the actual `Cat_cart` family coefficient.
- Product evaluation/curry uses the Cartesian mapping categories. Fixed
  evaluation includes the existing map into the ambient functor category.
- Hom-profunctor curry compares the native Cartesian whole functors. Its
  arbitrary-profunctor and runtime-nonfolding negatives remain.
- Four former telescope noncomputation assertions become positive under the
  restored strict-default laws. Both wrong-profile negatives remain. The
  existing composition proofs and their explicit inputs are unchanged.

The last reviewer exposed a stale comparison pattern in the kernel: the old
precomposition point head now reduces to ordinary composition. The two existing
Hom-curry unifiers are migrated to that actual whole composite. They retain the
supplied profunctor and both endpoint functors; the source duality is a residual
condition rather than an inverse inference through a reducible `Op_cat` pattern.
No primitive, rewrite rule or operational proof argument is added by this delta.

The first four-reviewer run passes the first three files and fails at the old
Hom-curry pattern. With the two owner-position corrections, the complete focused
run passes cold: `20261025T015323Z-7fe35de7d91d4b8a96f43cf571b1d68a`,
55.243s/185,728KiB, 90s/2GiB/o=20, subject reduction enabled. The matched warning
body sets are identical (1,769 each). Exact replay reproduces all six changed
outputs without compiled objects.

The preceding core regression failed at a stale negative telescope assertion:
`20261025T013626Z-c0d9390a89854ca38570fbb1c79f9093`, 556.918s. After correcting
that contract, the same 245-input core regression passes cold:
`20261025T020300Z-8656e38ab9074ede9a8b454c689921a2`, 771.773s and 2,631,900KiB
maximum child-process RSS at the previously measured 900s/4GiB/o=20 profile.
This is an aggregate result, not a claim that foundational normalization is
cheap or that global confluence has been established.

The [verification](foundation_reviewer_followup_verification.json) preserves
the source pins, receipts, failure, exact replay and warning comparison. The
production-emitter package and its existing qualification counts are unchanged.
The remaining original reviewers, broader affected-library gates, R07/R12,
the five terminal Homd runtime obligations and production promotion remain open.

Next original-reviewer traversal reaches the higher-sieve classifier. Its
ordinary-view annotations and the already selected strict/lax mapping boundary
must follow the actual owner. That separate family-reviewer continuation is
not included in this tranche's passing result.
