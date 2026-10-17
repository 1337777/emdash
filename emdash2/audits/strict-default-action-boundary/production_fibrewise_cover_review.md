# Fibrewise Sigma and direct-cover consumers

Date: 2026-10-17
Predecessor: `b84f544d`
Status: original owners, completion-HIT reviewers and retained-section derivations qualified in staging; broader import stops at the locality observation's coefficient
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_fibrewise_cover_verification.json)

The original fibrewise dependent sum now reads both families in Cat_cart.
Its constructor, fibre value, base-arrow computation and whole first
projection are unchanged. In particular transport retains E[p](e) and the
actual D-action along the canonical Sigma transport arrow. The displayed
projection keeps its ambient Functord type.

The ordinary-sieve member section previously used fib_cov_transf directly.
That canonical section now has a Cartesian mapping profile. The original
public Psh arrow uses its existing strict_transfor view, retaining the exact
pair (p,member) and the generic higher action. The direct-cover retained-member
comparison reuses this ordinary_sieve_member_section rather than supplying
its old unviewed Cartesian term. No new admission evidence or primitive
section is added.

The cover-question family, matching/section families, internal sheaf structure
and completion HIT keep their original constructors and whole contracts.
Seventeen existing owner coefficient annotations and eight reviewer
annotations move from Cat_cat to Cat_cart. Ordinary functor equalities,
composition, identities and OmegaEquivAlong still use Cat_cat where that is
their actual public type. This is not a blanket replacement of the universe.

The completion's explicit IsStrictFunctord property still constrains its
extracted glue comparison. Default Functord remains lax. The existing whole
extension-comparison and silent contracts retain their declared status;
this migration does not derive those supplied contracts from component betas.
No rewrite/unification rule or primitive constructor is added.

The broader import next reached the original Yoneda precomposition value
proof. Its three component annotations and the 38 component annotations in
the retained-section proofs now use Cat_cart. The latter reuse the same
ordinary member-section view at fifteen occurrences. All fifteen original
derived symbols typecheck, including the final retained-member path, without
adding strictness to the arbitrary matching map or Yoneda section. Undoing
the two specified substitutions reproduces the original retained-section
source byte-for-byte.

The original reviewers pass: fibrewise Sigma (five positives), sieve extension
(eight positives), cover questions plus question families (22 positives and
one negative), internal sheaf structures (eight positives), and completion
HIT (17 positives and two negatives). The combined question reviewer is the
concatenation of the two original reviewers after the stated annotation
changes. No assertion is removed or changed from negative to positive.

The source closures of the previously checked core and presheaf/sieve
boundary remain unchanged. Warning bodies also remain unchanged: 1995 for
the fibrewise/core import and 2397 for the extension/direct-cover imports.
Owning-file inferred-slot audits report zero unreviewed clauses. These are
scoped computation and interaction results, not a global confluence proof.

Fibrewise Sigma passed in about 26s under 240s/2GiB/o=20. The larger focused
imports use the existing 300s/4GiB/o=20 profile and passed in about 27-32s.
Subject reduction and serial/file/no-swap guards remain enabled. The broader
inherited assembly import passes retained sections and the already-migrated
strict-pointwise-equivalence owner, then fails at
emdash3_2_direct_cover_completion_locality.lp:97-141. Its retained-member
observation still uses Cat_cat for the displayed component instead of
Cat_cart. That run took about 67s at the existing 600s/4GiB/o=5 profile.

Next migrate the original locality consumer, retaining its actual selected
inverses and the existing Cartesian displayed pointwise-evidence profile.
Remaining library compatibility, strict-functor wrapper retirement,
production promotion and catalog/health/CI/source-pin qualification remain
required. This is an existing-consumer migration, not new sheafification or
resumption of the paused nerve goal.
