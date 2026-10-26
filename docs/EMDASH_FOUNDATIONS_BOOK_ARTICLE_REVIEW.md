# Foundations book/article manuscript review

Date: 2026-10-26
Plan: [active update plan](EMDASH_FOUNDATIONS_BOOK_ARTICLE_UPDATE_PLAN.md)
Source baseline: `f0e22340`; first manuscript checkpoint: `730cfdff`.

## Focused higher-profile follow-up

The later isolated correction at `414344cb` motivates a bounded exposition
update, prioritized by the user before further implementation. Appendix G
and article §3 now state that displayed modifications have strict fibre
components even though displayed maps remain lax across the base. They
present `sigma_functord_sec_func` as the existing whole forward construction
and distinguish its source from the broader section category. Chapter 5
retains evaluation at the total object `(y,p)` and points to that qualification.
The Foundations/current-status reports no longer present the legacy whole
identification as the intended mathematical contract; both explicitly record
that its production clauses are still present.

The earlier review of all 46 sources and 189 claims is carried forward for
unchanged material. No new checked theorem or evidence ID is introduced.
The direct Homd ladder, Sigma-Hom dualities, ordinary/displayed facade
comparisons and Gray closure are unchanged. The kernel SHA-256 remains
`70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e`.
Draft editions `0.10.1-dev` and `0.4.1-dev` distinguish the revised artifacts
from the completed snapshot below. The snapshot's hashes are historical;
new artifact measurements are recorded separately after export and inspection.

### Refreshed local artifacts

| Artifact | Edition | Pages / fonts | SHA-256 |
| --- | --- | --- | --- |
| [Book PDF](emdash-book.pdf) | 0.10.1-dev | 425 / 18 embedded | `905d588a003b386ec0c00ea2e79d0bbef092aae57386e96f6b282268e3da3622` |
| [Overview PDF](emdash3_2.pdf) | 0.4.1-dev | 20 / 14 embedded | `ed595a77d52365c08e2bb3a54212d94e4fa6e340e060113074ff224ee0b9adc9` |

Both owning release pipelines pass, including the 46-source/189-claim book
check, 3,237 book math spans, all 17 article registry tests, bounded browser
audits, normalized exports and PDF checks. The first book check found a
relative audit link; correcting that source link made the complete pipeline
pass. The first article export passed automation but visual inspection found
the new uncurrying formula crossing its column. Its two-line source correction
passes the repeated article pipeline and the final image inspection; only
the corrected artifact hash above is used for promotion.

Visual review covers book pages 1, 43, 398, 406 and 407; article pages 1, 5,
6, 7 and 10, with pages 5–7 and 10 reinspected after the formula correction.
The final changed displays, Homd ladder, section normalization route and
adjacent table transition are legible without clipping or overlap. The
earlier broad visual review remains evidence for unchanged content, not a
claim that all pages were manually reinspected in this follow-up.

`book:promote` and `article:promote` copy the generated PDF and owning
Markdown sources to the four existing local distribution paths. The logs are
under `emdash2/tmp/probes/book_article_profile_followup/`; no log or temporary
image is tracked. Distribution byte equality, exact diff/links and the
unchanged native source hash are checked before the checkpoint. No native
checker, frontend aggregate, renderer redesign, publication or push is part
of this documentation-only pass. The Pi/Sigma source correction and the
remaining native/integration gates stay open in their existing plans.

## Scope of this review

This is a migration-specific exposition audit, not a fresh proof of every
book theorem. Native declarations and migrated reviewers remain authority.
The full native source qualification and accepted frontend tranche are carried
forward at their recorded scopes; this documentation work changes neither.
The source review distinguishes strict public functors, lax base comparisons,
Cartesian coefficients, duality dimensions, actual inverse data, and supplied
versus derived structures. Mathematical-development and research-boundary
claims do not become checked by appearing in the revised manuscript.

## All manifest sources

| Source | Migration disposition |
| --- | --- |
| [edition-notice](../emdash2/book/frontmatter/00-title.md) | Revised strict-default/coefficient/duality convention; draft and nerve boundaries retained. |
| [preface](../emdash2/book/frontmatter/01-preface.md) | Revised functor/transfor distinction; WalkingEnd proof and groupoidal contrast retained. |
| [how-to-read](../emdash2/book/frontmatter/02-how-to-read.md) | Routes readers to the whole Homd and duality account; distinguishes local draft from public editions. |
| [contents](../emdash2/book/frontmatter/03-contents.md) | Generated from the unchanged manifest source order; no manual contents edit. |
| [prologue](../emdash2/book/chapters/00-prologue.md) | WalkingEnd code uses the admitted Cartesian coefficient; theorem scope unchanged. |
| [chapter-1](../emdash2/book/chapters/01-judgments-and-computation.md) | Equality/LF judgments and equality modes are unchanged; no lax-functor admission premise is used. |
| [chapter-2](../emdash2/book/chapters/02-categories-functors-and-families.md) | Revised strict functors, lax maps, admitted coefficients, direct identity/relative Homd and dualized Sigma–Hom. |
| [chapter-3](../emdash2/book/chapters/03-logic-propositions-and-sets.md) | Proposition, set and Nat reasoning remains equality-local; no directed naturality is made an equality. |
| [chapter-4](../emdash2/book/chapters/04-equivalence-and-univalence.md) | Transport over groupoidal sources now uses public strict functors; equivalence/univalence boundaries retained. |
| [chapter-5](../emdash2/book/chapters/05-induction-and-universal-properties.md) | PathOut motives use admitted coefficients; whole induction and composition benchmark retained. |
| [chapter-6](../emdash2/book/chapters/06-directed-hits.md) | Contextual WalkingEnd algebra uses admitted families; its directed generator cell is unchanged. |
| [chapter-7](../emdash2/book/chapters/07-truncation-and-categorical-height.md) | Recursive truncation and categorical height remain separate; no new object-identity claim. |
| [chapter-8](../emdash2/book/chapters/08-walking-endomorphism.md) | Code/representable coefficients and default functor laws corrected; directed normalization precedes discreteness. |
| [chapter-9](../emdash2/book/chapters/09-transfors-and-the-calculus-of-cuts.md) | Hom accumulation, conventional-lax leg, displayed coefficients and computation modes corrected. |
| [chapter-10](../emdash2/book/chapters/10-categories-precategories-and-categorical-identity.md) | Ordinary precategory/univalent-category development remains explicitly distinct from native Cat. |
| [chapter-11](../emdash2/book/chapters/11-functors-transfors-and-functor-categories.md) | Public strict functors, lax transfors and Cartesian joint operations distinguished; ordinary theorem scope retained. |
| [chapter-12](../emdash2/book/chapters/12-adjunctions-and-equivalences.md) | Indexed triangles, whole ordinary Hom comparison and seven scoped introduction views retain their guards/inverses. |
| [chapter-13](../emdash2/book/chapters/13-yoneda-representability-and-profunctors.md) | Native T-variance and Cartesian coefficients stated; product-form Prof remains separate from Homd Q. |
| [chapter-14](../emdash2/book/chapters/14-strictness-dagger-and-duality.md) | T/R/O/C2 and their transformation/family profiles made explicit; dagger remains proposed structure. |
| [chapter-15](../emdash2/book/chapters/15-structure-identity-and-saturation.md) | Prospective dependent structures use admitted families; ordinary SIP and Rezk discussions remain development. |
| [chapter-16](../emdash2/book/chapters/16-weighted-universal-constructions.md) | Weight coefficient corrected; semantic end/Kan formulas remain interpretations, not derived global interfaces. |
| [chapter-17](../emdash2/book/chapters/17-weighted-colimits-duality-and-join.md) | T/product-swap weighted duality distinguished from O-adjunction; actual preservation body described. |
| [chapter-18](../emdash2/book/chapters/18-presheaves-and-sieves.md) | Presheaves are admitted families over T(K); sieve and slice interfaces retain their existing scope. |
| [chapter-19](../emdash2/book/chapters/19-sites-covers-and-descent.md) | Matching/section question families use admitted coefficients; restriction remains lax across the question base. |
| [chapter-20](../emdash2/book/chapters/20-sheafification-by-cover-completion.md) | Whole question coefficients corrected; return/glue, supplied assembly, locality and reflector boundaries retained. |
| [chapter-21](../emdash2/book/chapters/21-commutative-algebra-by-universal-property.md) | Set-carrier ring/localization universal-property interfaces and supplied-existence boundary unchanged. |
| [chapter-22](../emdash2/book/chapters/22-affine-geometry-and-the-sieve-df.md) | Ordinary ring-geometric opposite, literal localization maps and supplied affine-locality contracts retained. |
| [chapter-23](../emdash2/book/chapters/23-schemes-from-covering-charts.md) | Global-first scheme, inherited actual slice/overlap maps and supplied affine realization remain explicit. |
| [chapter-24](../emdash2/book/chapters/24-projective-line-and-boundary.md) | Projective-line package still presupposes global object/overlap/Laurent data; no construction or non-affineness claim added. |
| [chapter-25](../emdash2/book/chapters/25-paths-and-the-groupoidal-shadow.md) | Path-realized compositor distinguished from general noninvertible transfor cell; public functor strictness stated. |
| [chapter-26](../emdash2/book/chapters/26-circle-and-integer-line.md) | Circle dependent loop beta, supplied self-equivalence/monodromy and set-truncated Integer boundary unchanged. |
| [chapter-27](../emdash2/book/chapters/27-free-inversion-and-groupoidification.md) | Unit compositor identity follows current reviewer; mapping property still lacks source-functorial adjunction packaging. |
| [chapter-28](../emdash2/book/chapters/28-laxity-interchange-and-gray-direction.md) | Retired strict-functor wrappers removed; classified lax Homs, selected right closure and nonidentity interchanger retained. |
| [chapter-29](../emdash2/book/chapters/29-simplexes-from-dependent-homs.md) | Whole Sigma–Hom corrected; ordinary strict ordinal maps distinguished from arbitrary dependent fillers and native join-built shape universality; no missing nerve equivalence or degeneracy is inferred. |
| [chapter-30](../emdash2/book/chapters/30-cartesian-structure-and-dependent-products.md) | SliceSigma/Pi use C2(C), base change T(C), and native terminal-family view is oplax; ordinary formulas retained. |
| [chapter-31](../emdash2/book/chapters/31-additive-abelian-and-homological-computation.md) | Native D(C) made explicitly oplax; ordinary reconstruction remains a declared premise and native family view is derived. |
| [appendix-notation](../emdash2/book/appendices/a-notation.md) | Added T/R/O, coefficient, index and whole-section notation; corrected homology diagram profile. |
| [appendix-evidence](../emdash2/book/appendices/b-emdash-evidence.md) | Generated register now has 189 entries; every cited owner/reviewer resolves. |
| [appendix-hott](../emdash2/book/appendices/c-hott-correspondence.md) | WalkingEnd code coefficient corrected; attribution and directed/groupoidal distinction retained. |
| [appendix-glossary](../emdash2/book/appendices/d-glossary-and-index.md) | Strict-default, duality, presheaf/Prof and Gray terms aligned with source. |
| [appendix-computation](../emdash2/book/appendices/e-computation-and-normalization.md) | Default laws and five terminal whole comparisons distinguished from runtime normal forms. |
| [appendix-status](../emdash2/book/appendices/f-status-and-research.md) | Historical variance defects distinguished from current migration; global metatheory and application limits retained. |
| [appendix-formal-presentation](../emdash2/book/appendices/g-formal-presentation.md) | Actual Homd owner ladder, admitted families, default laws and Cartesian exchange types documented. |
| [bibliography](../emdash2/book/references/bibliography.md) | Existing source attribution unchanged; published book DOI does not assert this local revision is published. |
| [book-credits](../emdash2/book/CREDITS.md) | Pinned adaptation ledger/license retained; this revision explains repository code and adds no new third-party adaptation. |
| [book-license](../emdash2/book/LICENSE.md) | Existing CC-BY-SA ownership and license retained without alteration. |

## Claim register

The pre-revision register had 187 entries. Fifteen entries change their
statement or owner/reviewer references, and two entries are added for whole
identity/relative Homd and Sigma–Hom. The other 172 retain their stated status,
hypotheses and original evidence route. Source-reference checking covers all
189 entries; it does not prove a semantic model or broaden the source checks.

The changed entries are:

- `CAT-FUNCTOR-CALCULUS`: statement/evidence aligned with the migrated owner.
- `CAT-HOM-CUTS`: statement/evidence aligned with the migrated owner.
- `CAT-TRANSFOR-CALCULUS`: statement/evidence aligned with the migrated owner.
- `CAT-DIRECTED-FAMILIES`: statement/evidence aligned with the migrated owner.
- `CAT-DISPLAYED-EVALUATION`: statement/evidence aligned with the migrated owner.
- `TRANSF-STRICT-NATURALITY`: statement/evidence aligned with the migrated owner.
- `TRANSF-HORIZONTAL-CALCULUS`: statement/evidence aligned with the migrated owner.
- `OP-DUALITY`: statement/evidence aligned with the migrated owner.
- `WEIGHTED-COLIMIT-PRESERVATION`: statement/evidence aligned with the migrated owner.
- `PATH-PSEUDO-LAXITY`: statement/evidence aligned with the migrated owner.
- `GRAY-COMPUTATIONAL-PROFILE`: statement/evidence aligned with the migrated owner.
- `GRAY-RIGHT-CLOSURE`: statement/evidence aligned with the migrated owner.
- `NATIVE-KERNEL-COKERNEL-UNIVERSALITY`: statement/evidence aligned with the migrated owner.
- `ORDINARY-DIAGRAM-UNIVERSALITY`: statement/evidence aligned with the migrated owner.
- `PRIMARY-TERMINAL-FAMILY-UNIVERSALITY`: statement/evidence aligned with the migrated owner.
- `CAT-DEPENDENT-HOM`: new whole-interface claim.
- `CAT-SIGMA-HOM`: new whole-interface claim.

Specific non-mechanical corrections are recorded in the update plan: weighted
colimit T-duality differs from total-opposite adjunctions; slice families shift
their higher base; the unit compositor is strict while the Gray interchanger
is not; native homology uses oplax diagrams. The simplex account also
distinguishes strict ordinary ordinal maps from arbitrary dependent-triangle
fillers and the separately qualified native join-built shape interfaces. The ordinary diagram reconstruction
is still supplied, and its oplax-family image is derived by whole exchange.

## Article and frontend examples

The overview shares the revised whole Homd and Sigma–Hom story and retains its
shorter architectural purpose. Fixed inner evaluation uses ordinary mapping
categories; joint evaluation and exchange use the Cartesian profile. The
actual frontend transfer owners and migrated tests supply those types.
The public reviewer may serve an older edition. Two current reviewer preset
*display labels* still print `Functor_cat` for the joint-evaluation/exchange
assumptions; the compiled transfer uses `Functor_cart_cat`. Record this as a
small frontend-caption follow-up, not a reason to weaken the manuscript types
or rerun the waived full frontend aggregate during documentation work.

## Edition and artifact boundary

Local draft editions are book `0.10.0-dev` and overview `0.4.0-dev`, dated
2026-10-26. Their identifiers distinguish the changed foundation from the
previous artifacts. No new publication, tag, push or release is authorized
or performed. Assembly, PDF export, metadata/font/text checks, and visual
inspection use the existing owning tools. Artifact measurements and checksums
are appended only after their terminal results are verified.

## Earlier local artifact qualification (0.10.0 / 0.4.0)

| Artifact | Edition | Pages / fonts | SHA-256 |
| --- | --- | --- | --- |
| [Book PDF](emdash-book.pdf) | 0.10.0-dev | 425 / 18 embedded | `bb5fdaf87c076cb675ae29248b045444565fa664318cf529cae3539d9b4dab8a` |
| [Overview PDF](emdash3_2.pdf) | 0.4.0-dev | 20 / 14 embedded | `ba4eca1cc106a9b9340f3acd173d502a8d13a6dd149efae91743936161a7f453` |

The book passes its complete local `book:release` pipeline (`wave516`):
assembly, 189-entry evidence check, typography/KaTeX, architecture/source,
registered-document validation, build, bounded browser audit, normalized PDF
export and PDF structure/font/text/metadata checks. The article passes its
own corresponding `article:release` pipeline (`wave518`), including all 17
registry tests. The 20-page article exceeds its advisory 16-page target;
its manifest has no maximum and no page-budget exception was introduced.

Visual review covered the title and all 46 source openings, the revised Homd
and Sigma–Hom displays, the duality table, the formal owner ladder/code, and
a body page of the wide evidence register. All 20 article pages, including
both diagrams, were inspected. The final book update changed only the
Chapter 29 opening image relative to the inspected baseline; that image was
re-inspected. The article's initial Sigma–Hom display crossed a column despite
the browser audit passing. It was split into two lines at the authored source;
only article page 7 changed, and its final 130-dpi image was inspected again.
No clipping, overlap, broken glyphs or raw math was observed in these views.
This records the actual visual scope, not a claim to have manually read every
one of the book's 425 PDF pages.

`book:promote` and `article:promote` (`wave519`, `wave520`) updated only the
four local distribution files. Byte comparisons verify that their PDFs and
Markdown match the current exporter/authoring outputs exactly. Existing local
preview cleanup completed. There was no renderer, package, native rule,
resource-profile or public-site change, and no publish/tag/push operation.

The book/article continuation is complete at this local draft snapshot.
Production-health/final-integration gates and the later legacy-nerve adaptation
remain obligations of the parent goal. The two reviewer-caption corrections
remain a separate small frontend follow-up.
