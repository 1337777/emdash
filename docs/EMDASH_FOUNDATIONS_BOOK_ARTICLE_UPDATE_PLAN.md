# Book and overview article: current foundations revision

Date: 2026-10-26
Plan-ID: EMDASH-FOUNDATIONS-BOOK-ARTICLE-UPDATE
Status: comprehensive local draft revision and focused Pi/Sigma clarification complete; refreshed local artifacts checked; implementation follow-ups remain separate
Parent: [strict-functor/duality foundations goal](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Worktree: `/home/user1/emdash1-strict-functor-duality-v1`
Branch: `goal/strict-functor-duality-v3.2`
Implementation checkpoint: `f0e22340`

## Direction and scope

The subsequent native correction is now installed. A status-only follow-up
updates Appendix G and article §3 to distinguish native installation from the
remaining frontend/final integration. Local drafts `0.10.2-dev` and
`0.4.2-dev` pass their owning gates and changed-page inspection, recorded in
[the artifact review](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md#native-correction-status-synchronization).
This preserves the completed comprehensive exposition; it does not reopen
chapter design or claim that the whole foundation goal is complete.

Priority reaffirmed, 2026-10-26: the comprehensive book/article revision was
completed at `1fe72617`. A later review, checkpoint `414344cb`, identified a
retained Pi/Sigma higher-profile mismatch. The current documentation-only
follow-up clarifies the strict fibre components of displayed modifications,
the existing whole forward uncurrying functor, and section evaluation at
the actual total object. It distinguishes the qualified isolated correction
from production, which is unchanged. Refresh the local drafts to book
`0.10.1-dev` and overview `0.4.1-dev` through the existing exporters.
No native implementation, semantic redesign, health aggregate or performance
work belongs to this pass. Carry forward the earlier 46-source/189-claim
review for unchanged material; validate the affected sources and artifacts.

The user now prioritizes the book and shorter overview article over further
production-health/performance work. That decision supersedes the earlier
requirement to finish production health before starting documentation. The
native implementation and the accepted frontend tranche supply the source
baseline. Outstanding health and final-integration obligations remain recorded;
they are not blockers to this exposition work and are not declared complete.

Update the existing mathematical story comprehensively. Preserve its theorem-led
WalkingEnd/Nat organization, later applications, supplied hypotheses, actual
inverse data and formal-status distinctions. Correct the existing narrative
at its owning sections rather than accumulate migration notices over obsolete
claims. Do not redesign the kernel, renderer, category semantics or article
structure beyond what the foundation changes require.

Local documentation edits, validation, generated artifacts and checked Git
checkpoints are authorized. Historical publication instructions are ownership
history, not current authorization to push, merge, publish, tag or release.
Do not edit generated Markdown/PDFs by hand.

## Authoring owners and baseline

- `emdash2/book/book.json` orders 46 source files and currently names draft
  edition 0.9.3-dev; `book/expansion.json` owns its architecture.
- `book/STYLE.md`, `book/RELEASE.md`, and `emdash2/print/AGENTS.md` own prose,
  evidence, generated-source and render policy.
- `book/evidence.json` initially had 187 claims. The baseline `book:check` assembles
  successfully but reports ten stale evidence references: retired strict
  functor wrappers, the relocated strict-transfor owner, the retired curry
  strictness witness, and renamed terminal-family evidence.
- The authored article is
  `emdash2/print/public/emdash-v3-2-overview.md`, registered in
  `emdash2/print/documents.json`. Public `docs/emdash3_2.*` and
  `docs/emdash-book.*` are distribution copies produced by the owning tools.
- The initial inventory is saved at
  `emdash2/tmp/probes/kernel_boundary_continuation/book_article_foundations_inventory.json`.
  It is a search aid, not proof that every semantic occurrence has been reviewed.

The native core SHA-256 is
`70b7a550b6d932dcfca561300b3ac0cf37f28dfca14afc2429249141eff5182e`.
Use current native declarations and original migrated reviewers before older
prose. The last frontend aggregate and passing focused repair are accepted
under the user's repeat waiver; do not call that aggregate green.

## Mathematical contract to explain

| Topic | Current source contract | Expository consequence |
| --- | --- | --- |
| Public functors | `Functor` is strict; `Hom_cat Cat_cat A B` is `Functor_cat A B`. | Remove the ambient-lax-functor default and redundant strict-functor admission story. Retain actual extracted action owners where still present. |
| Transformations | Default transfors are conventional lax; the pre/right leg computes strictly and the post/left comparison can be noninvertible. | State the selected direction explicitly. Do not equate both naturality routes for arbitrary transfors. |
| Families and Hom | `Catd(K)` classifies `K → Cat_cart`, and representable Hom families use the same coefficient. `Cat_cart` has Cartesian mapping Homs. | Distinguish the public universe from the coefficient used by dependent families. The profile belongs to the type, not external equality arguments. |
| Structural evaluation | Joint evaluation/currying uses Cartesian mapping categories; fixed evaluation accepts ordinary mapping categories. | Preserve the meaningful lax mapping interface and state the stronger joint-input requirement. |
| Dualities | `T=Op_cat` reverses dimension 1; `R=CoAbove2_cat` reverses dimensions ≥2; `O=TotalOp_cat` reverses all positive dimensions; `CoAt2_cat` reverses exactly dimension 2. | Review every opposite occurrence by its owner. No global textual replacement of “op”. Preserve ordinary one-category specializations. |
| Fibre duality | `Op_catd(E)` is over `CoAt2_cat(K)`; `TotalOp_catd(E)` is over `R(K)`. Ordinary fibre transpose of maps has its qualified strict-transfor input. | Show the base shift and distinguish it from ordinary functor duality. Do not pass arbitrary lax FF through a fibrewise transpose. |
| Sections | Π remains transformation-backed, with default lax section action; it is not redefined using globally strict transfors. | Keep directed transport comparisons and the WalkingEnd decoder's normalization cell. |
| Identity Homd | Let `P(I)=T(Functor_cat(I,T(Cat_cart)))`, with fixed-object presheaf view `T(I)→Cat_cart`. Let `Hom_Q(A,B)=Cart(A,P(B))` and `S_E(x)=Transf(K,Q)(iE,iHom_K(x,−))`. | Explain the actual whole y-section and the direct x/u/y/v/f ladder. The root's x-fibre is `T(S_E(x))`; only its object carrier is identified with that of `S_E(x)`. Do not claim their higher mapping categories agree. |
| Relative Homd | The public FF-blended root is a defined composite with identity Homd; FF remains lax. | Preserve the public names and explain the value `Hom_E[y](E[f](u),FF[y](v))` without introducing a second primitive theory or operational equality proofs. |
| Sigma Hom | The category normal form is `O(Σ_{O(I)} O_fib(H))`, where `I=Hom_K(x,y)` and `H:T(I)→Cat_cart` is the identity Homd presheaf. | Retain the intuitive arrow pair `(f,α)` but distinguish that object reading from the full higher-category formula. Explain why the dualized total restores fibre directions. |
| Q and profunctors | Q supplies structural/represented operations consumed by Homd; existing product-form Prof retains its convention. | Do not claim a derived unrestricted coend/bicategory model, or identify curried Q Homs with every ordinary profunctor classifier. |
| Normalization | Five terminal Homd presentations have accepted whole proof-time comparisons; runtime leaves/higher/inverse observations remain separate. | Do not reintroduce the rejected literal constant runtime claims. Explain the distinction near the formal computation account. |
| Qualification | Native source/reviewer scopes and selected frontend computations are checked; production health and global metatheory are separate. | Replace stale “duality repair pending” statements with the actual current contracts and honest remaining boundaries. |

## Work packages

| Stage | Owning sources | Deliverable and acceptance |
| --- | --- | --- |
| B0: source/evidence review | All 46 book sources, 187 claims, article, current native owners/reviewers | Record affected and unaffected dispositions. Baseline evidence failures are specific review inputs, not permission to substitute nearby symbol names. |
| B1: foundational introduction | Chapters 2, 9, 11; notation appendix; corresponding evidence | Present strict functors/lax transfors, Cat_cart families, direct identity/relative Homd and Sigma-Hom. Give one coherent introduction that can replace the former dependent-hom story. Preserve the WalkingEnd prerequisites. |
| B2: variance and structural applications | Chapters 12–17, 28–30 and affected portions of 0–8, 10, 18–27, 31 | Review Hom/Prof, adjunction duality, presheaves, total maps, Gray closure, simplexes, Cartesian/indexed structure and homology against their actual owners. Correct only necessary assumptions/formulas; do not claim unfinished nerve equivalences. |
| B3: formal and status account | Appendices A, D–G, frontmatter, README, STYLE notation, relevant current reports | Synchronize the exact symbols, profiles, projection ladder, runtime/proof-time distinctions and research boundaries. Remove retired-wrapper claims; keep ordinary HoTT strictness terminology distinct. |
| B4: shorter article | Authored overview article and its existing source/evidence links | Give the revised foundations and Homd story concisely, retain the article's broader research argument, and align every selected application claim with the revised book. It must not become a migration log. |
| B5: validation and artifacts | Evidence/architecture/manifests and owning assembly/render tools | Run book/article checks and bounded renders after coherent edits; inspect representative rendered mathematics and changed diagrams. Generate local PDFs and deterministic artifact checks when the manuscript revision settles. Promote local distribution copies only through owning tools; no publication. |
| B6: documentation completion audit | This plan and the parent goal ledger | Account for every source/evidence claim touched by the migration, all ten initial evidence failures, article consistency and render results. Retain deferred production-health/final-integration obligations and the later legacy-nerve review. |

B1's core exposition is now drafted, together with the affected B2/B3 and
article passages. Chapter 2 has a stable new dependent-Hom subsection; the
formal appendix and article give the same whole projection ladder. Chapters
9, 11, 14, and 28 now distinguish strict functors, conventional lax transfors,
Cartesian coefficients, and the corrected dualities. This is a manuscript
checkpoint in progress, not completion of B0–B6.

## Validation and editorial constraints

- Prose leads with mathematics. Keep kernel identifiers in concise formal-status
  notes and preserve stable anchors/links.
- Change checked claim statements and their evidence owners/reviewers together.
  Locate real migrated consumers; do not weaken the evidence checker to pass.
- Never identify fibre object agreement with whole categorical equivalence.
  Keep hypotheses and actual inverse/comparison data visible where they matter.
- Use `book:typography` and `book:check` at coherent chapter boundaries;
  `article:check` for article changes. Use the bounded `book:render` and
  `article:render` gates for final manuscript layout. Renderer behavior and
  package dependencies are outside this revision unless a concrete defect
  blocks the requested documents.
- Generated book contents/evidence appendix, assembled Markdown and PDFs are
  produced by their owning tools. No manual artifact edits or new document
  glob discovery.
- Preserve existing external-source attribution. New third-party adaptation
  requires its source/provenance review; this pass primarily explains current
  native code and does not require a new literature survey.
- Chapter 29 may describe the migrated existing simplex/nerve substrate, but
  completion of the separate legacy nerve work remains its later explicit
  mathematical task.
- The single health measurement running at the priority change finished at
  its existing bound; the parent plan records its timeout. Launch no further
  health or performance work as a prerequisite to this document revision.

## First manuscript tranche, 2026-10-26

The revised foundation is propagated through the introduction, WalkingEnd
prerequisites, Hom/Prof and presheaf notation, groupoidal/Gray account, Sigma
simplexes, slice-family base shifts, formal appendix, glossary and status
matrix. The overview article now has the same whole identity/relative Homd
story and explicit Sigma–Hom category formula. Existing anchors, mathematical
application boundaries and attribution are preserved. No native rule,
frontend implementation, package, renderer or validation profile was changed.

Source review produced three corrections that a blanket terminology pass
would miss:

- Weighted colimits use **T** and product-swap `Op_prof`; their preservation
  theorem transposes the actual whole Hom comparison. The separate
  `Op_adjunction` package uses **O**. Neither contract substitutes for the other.
- `SliceSigma_catd` and `SliceDependentProduct_catd` are families over
  `CoAt2_cat(C)`; chosen base change is over `Op_cat(C)`. Their first-arrow
  formulas remain the familiar Σ/u*/Π chain.
- The groupoidification unit compositor now has a checked identity value;
  the nonidentity Gray interchanger comes from a general lax transformation.

All ten baseline evidence-reference failures have been corrected against the
actual declarations and reviewers. The terminal/initial family reviewer uses
oplax walking-arrow presentations and checks both actual inverse directions;
its claim now says so. Two new entries record the whole dependent Hom and
Sigma–Hom, bringing the register to 189 claims. A passing evidence checker
establishes reference hygiene, not completion of the semantic manuscript audit.

Validation before the downstream propagation: `wave508_book_foundations_check`
passes assembly, evidence (189), typography/KaTeX (3,208 spans), source and
registered-paper checks. `wave509_article_foundations_check` passes the 17
registry tests and article-source validation. New changes require the final
owning checks/render results recorded below; no native/TypeScript aggregate
is needed for this documentation-only tranche.

Remaining review includes the application and frontend examples at their exact
profiles, the complete 46-source/claim disposition, representative rendered
mathematics and diagrams, final book/article PDFs and distribution artifacts.
Keep source review distinct from keyword search; preserve the unmodified
book's broader theorem/hypothesis boundaries. Remaining health/final-integration
and later legacy nerve work stay in the parent goal.

### Checkpoint validation and next slice

The tranche revises 26 manifest sources (plus README, STYLE and evidence) and
the authored overview. Existing theorem statements outside the reviewed
foundational passages are not treated as re-proved by this revision.

- `wave510_book_foundations_render`: source/evidence/typography checks and
  bounded browser rendering pass, 424 pages.
- Final source review corrected two remaining weighted-colimit sentences
  that still referred to applying `Op_adjunction`. The final owning replay
  `wave513_book_final_source_render` passes the same checks and 424-page
  render, including 189 evidence entries and 3,230 checked math spans.
- `wave511_article_sources`: 17 registry tests and article validation pass.
  `wave512_article_render`: bounded render passes, 20 pages, using the same
  built manuscript snapshot. Both documents have no reported console, page,
  request, math, horizontal-overflow or internal-link errors. Preview processes
  exited through the existing cleanup path. Vite retains its advisory large-
  chunk warnings; no renderer redesign is part of this tranche.
- `git diff --check` passes. The native source SHA remains unchanged. No
  Lambdapi, TypeScript aggregate, new profile or health run was launched for
  the documentation work. Generated Markdown was assembled by its owner;
  neither PDFs nor distribution copies were hand-edited or published.

The next slice is **the remaining manuscript/claim consistency review**, with
special attention to application diagram categories (Chapters 19–24 and 31),
frontend examples in Appendix G/article, and any residual family/mapping
profile assumptions. Review Chapters 1, 3, 7, 10, 12, 15 and 26 for affected
interfaces while retaining their ordinary/groupoidal theorem boundaries.
Preface/reader guide and backmatter need the final edition audit. Finish the
complete 46-source disposition before metadata/PDF/distribution promotion.
Then generate and visually inspect the final artifacts under the owning tools.
This keeps the active work on documentation; it does not reopen the migration.

## Complete manuscript disposition and draft artifacts

The [46-source review](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md) records each
manifest source, the 15 changed and two new evidence entries, the 172 retained
claim contracts, the article/frontend profile review, and unchanged attribution.
It is an exposition audit against current owners, not a new consistency or
model theorem. The book's native homology category is now explicitly oplax,
and the source ordinary reconstruction premise is distinguished from its
whole derived oplax-family image.

Visual inspection of the first PDF found a remaining simplex paragraph that
still allowed an arbitrary functor compositor. The manuscript now distinguishes
ordinary strict ordinal maps from nonidentity dependent fillers and from the
separately qualified native join-built shapes. This changes neither native
nerve code nor its deferred completion task. The final export replaces that
intermediate artifact; no intermediate hash is used for promotion.

The local draft versions are book `0.10.0-dev` and overview `0.4.0-dev`, both
dated 2026-10-26. Metadata changes distinguish the revised foundation from the
previous draft. Existing owning exporters perform generation, checks and local
distribution copies; no publication, tag, merge or push is performed.

The PDF skill is used for image-based artifact inspection, with repository
exporters taking precedence over generic PDF authoring advice. The artifact
operation marker ran successfully once for the two requested outputs. Poppler
and the existing pdf-lib checks provide rendering/text/metadata inspection;
no dependency installation or renderer modification is needed.

Two browser-reviewer assumption captions still name the old ordinary mapping
category for joint evaluation/exchange; the actual transfer uses Cartesian
mapping categories. This small frontend-caption follow-up is recorded in the
review and parent ledger. It does not alter the corrected manuscript examples
or reopen the waived frontend aggregate during this documentation stage.

## Completion boundary

The focused profile follow-up is complete in local drafts `0.10.1-dev` and
`0.4.1-dev`. Its [review and artifact record](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md#refreshed-local-artifacts)
contains the owning gates, visual scope, hashes and production-status boundary.
The earlier B0–B6 disposition below remains the comprehensive baseline. No
source promotion or native inverse is claimed by this documentation checkpoint.

B0–B4 are accounted for by the [source/claim review](EMDASH_FOUNDATIONS_BOOK_ARTICLE_REVIEW.md),
covering all 46 manifest sources and the overview. B5 passes the final owning
book/article release pipelines and the recorded visual review. B6 records the
actual hashes, local promotion, unchanged native source boundary, retained
semantic hypotheses and deferred parent-goal obligations in that review.
The current tracked artifacts are [book](emdash-book.pdf) and
[overview](emdash3_2.pdf), with their generated/authored Markdown copies.

This completes SF-BOOK/SF-ARTICLE as **local draft updates**, not publication
or the entire persistent goal. The next authorized substantial continuation
is the separate review and proposed subplan for adapting the legacy nerve
work. Do not substitute a new miscellaneous health/performance sequence for
that review; retain the unsatisfied final-integration obligations explicitly.
