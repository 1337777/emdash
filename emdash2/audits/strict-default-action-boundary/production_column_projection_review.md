# Homology projection laws and the complete Freyd column reviewer

Date: 2026-10-21 UTC
Status: qualified non-library staging under explicit 3GiB profiles; broader migration and production qualification remain open
Predecessor: `80fc8490`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

## Preserved construction

The original homology quotient, cancellation and cover map retain their
selected kernel/cokernel data and derivations. Their diagram/evaluation and
initiality annotations use the native/total-dual profiles. General epicity of
the cover remains the original separate short-exact/Abelian-normality
obligation; this slice constructs the same map and proves the original
quotient compatibility.

The four generic point-projection laws retain their whole categorical
naturality arguments. In the first law, the ordinary boundary comparison
passes through the existing `one_cat_diagram_oplax_include_func` before the
same cokernel projection's naturality is applied. This is the actual map
whose image formed the preceding homology comparison. Native fixed evaluation
supplies its endpoint observations. No new naturality assumption, operational
equality cast, supplied comparison, runtime rule or unifier is introduced.

The two concrete Freyd quotient-compatibility proofs need only native
diagram/evaluation annotations. All ten original declarations across four
library files are retained. The strict-transfor component-path dependency is
unchanged from the source pin; it does not impose strictness on ambient
transformations.

## Original reviewer observations

The cover reviewer retains its six positive and two negative assertions. One
stale ordinary-evaluation annotation initially prevented typing its component
observation; selecting native evaluation corrects that annotation.

The full Freyd reviewer retains all eighteen original assertions and their
positive polarity. The bare `sigma_Fst(sigma_Snd(comparison))` expression no
longer infers its family at the specialized native coefficient. The existing
generic introduced-input reviewer already observes this same component by
the whole diagram functor. The concrete reviewer now does likewise, using
explicit source and target objects taken from the actual comparison's type.
Two local defined aliases retain those observations. Four endpoint checks use
native fixed evaluation and the introduced native target diagram.

The whole-arrow observation is still compared against the original introduced
diagram map, and both endpoint identities are still checked. The aliases do
not define the result to be that expected map. They apply the existing whole
functor to the original comparison. No pointwise replacement, removed check
or changed expected polarity is used. Bare nested-Sigma inference remains a
known R06 limitation; no new kernel projection or injectivity rule is claimed.

The final typing repair changes only the reviewer input file relative to the
3GiB typing-failure run. All library inputs remain identical. Both chosen
inverse observations and the two actual quotient-reconstruction applications
remain in the original complete reviewer.

## Qualification and resources

The [combined generic driver](production_homology_cover_projection_regression.lpfragment)
passes **nine positive/two negative assertions**, including three imported
positives, and all generic declaration bodies in **115.312s/1,840,148KiB**
under **180s/3GiB/o=20**. Receipt:
`20261021T112024Z-976b0949560648b8a5e34c0b73817674`.

The complete original `examples/freyd_native_column_comparisons.lp` target
passes **eighteen positives plus three imported positives** and its named
quotient-reconstruction bodies in **147.098s/1,786,068KiB** under
**300s/3GiB/o=20**. Receipt:
`20261021T113609Z-9dbc09b548fc48438a77d8a02b8a5bde`.
Subject reduction, warnings, source loading, serial execution, file limits and
no swap remain enabled. The isolated qualified checker is unchanged.

The 2GiB generic run failed allocation during the late import of unchanged
binary-product code; its cover reviewer had already completed. The identical
input then passed at 3GiB. The 2GiB full run completed all declarations and
failed allocation as its reviewer began. With identical inputs at 3GiB, it
reached the separate bare-projection typing failure described above. Correcting
that reviewer produced the final pass. For each resource pair, memoryMiB is
the only changed setting; mathematical inputs, checker, deadline and other
flags match. Fresh host headroom exceeded 14GiB before the increases.

These measurements remain R12 evidence, not an improvement claim or a blanket
3GiB default. RSS below 2GiB does not imply that the guard's address-space
constraint was unexhausted. Normal limits are unchanged; explicit per-target
profiles and supported-toolchain qualification remain part of promotion.

The final full warning multiset is exactly the same 2,316 bodies as its
allocation and typing-failure variants. The generic successful scope has 2,262
bodies. All fresh inputs match emission and tracked drivers. Every preceding
core/library/native-zero/kernel-column/native-entry input also rehashes
unchanged. New owners add no rules on prior symbols, so earlier exact-scope
evidence carries without another unchanged aggregate.

Coverage reaches **285 library/core files and 102 complete reviewers**. The
full central diagnostic is an additional staged file retaining five runtime
exclusions. There remain 506 registered core/library files and 494 reviewers
unstaged. Counts measure coverage, not remaining effort.

## Continuation

This closes the previously pending original Freyd column comparison/projection
reviewer. Continue with `examples/freyd_native_column_homology_paths.lp`, including
its native middle-column and diagram-map prerequisites. Those are distinct
consumers, not implied by this pass.

The five terminal Homd runtime obligations, remaining migration,
normalization/usability, supported checker/resource profiles and production
gates remain required. The separate nerve goal stays paused. Production
source, catalog and health claims are not promoted by this non-library audit.

Replay uses `production_owner_migration.py` and the original/linked targets.
The [verification record](production_column_projection_verification.json)
retains source/checker/profile hashes, paired resource runs, headroom records,
reviewer dispositions, declaration inventory and exact-input carry. Recheck
affected boundaries after an owner, source pin, checker or runtime profile changes.
