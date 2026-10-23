# Original connecting-kernel prerequisites: first dependency layers

Date: 2026-10-23 UTC
Status: qualified non-library continuation; standing normalization gates remain
Predecessor: `0a160223`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`

This slice migrates 15 original owners and four complete original reviewers
from the first two missing dependency layers of the original native
connecting-kernel path. It preserves 64 original declarations, 46 positive
and seven negative assertions. Seven files remain byte-identical to the
original source. The original selected maps, adjunctions, inverses, ordinary
category hypotheses and supplied structural capabilities remain.

Ordinary walking-arrow diagram inputs use the established oplax mapping
category and its whole evaluation/accessor owners. All 71 old `Op(C)` uses
in this slice are initial-object hypotheses and now use `TotalOp(C)`.
No extra strictness or operational equality payload is supplied by callers.

Two concrete proof adaptations are needed beyond classifier substitution:

- Cokernel-family annihilation previously invoked the ordinary-family shape
  whiskering helper. The oplax-valued family instead has its own native
  shape action; the corresponding proof step is reflexivity of that existing
  whole action. The theorem and original caller hypotheses are unchanged.
- The image/coimage proofs use `diagram_oplax_family_map_at` in place of the
  Cartesian symmetry accessor. Fourteen terminal-diagram composition
  endpoints use `comp_cat_fapp0`, as do their already qualified mate-input and
  source-observation owners. The selected K/Q postcomposition expressions
  retain the original representation used by the native mate paths.

The first endpoint test fixed six occurrences and passed the first whole
comparison theorem. Extending direct composition to every postcomposition
object expression exposed two differences solely in K/Q endpoint metadata
inside the same horizontal action. That broader rewrite was rejected; the
final candidate restricts the adaptation to the actual terminal-diagram
consumer. No kernel rewrite or unification rule is added for these proofs.
The complete original image/coimage reviewer passes, including factorization,
uniqueness and negative observations, in 108.582s at 2,154,800KiB RSS:
`20261023T161630Z-b92deb5a774e4d0295b24e69918dd746`.

Two further downstream steps reuse existing proof owners: the image-factor
ambient path composes `kernel_family_mate_projection_view` to compare the
literal and raw Hom presentations of the same selected inverse. The
covered-map left-cycle proof makes its reassociation explicit with
`comp_assoc` before applying the original chain-law hypothesis. Neither step
adds caller evidence or changes the theorem.

The only formal rules in the new source scope are the two unchanged original
clauses on `one_cat_binary_product_adjunction`. They project its whole
counit and unit component. `one_cat_product_category` and the selected
binary-product adjunction remain explicitly declared structural model
obligations, not constructions derived from beta observations. Their selected
products and all original downstream tests must pass before qualification.

The complete 19-file batch passes **49 positive and seven negative checks**,
including three inherited positives, in 202.225s at 2,740,140KiB RSS under
600s/4GiB/o=20 with subject reduction and warnings enabled. Receipt:
`20261023T162827Z-d0db21d04fbc4645aacaca3cbf3d968f`.
The emitter reproduces every one of its 139 input hashes. All 620 parent
qualified sources and both parent complete/addition receipt inputs remain
byte-identical. The two original product-adjunction rules match only the new
constructor; no earlier term contains that constructor. Parent evidence is
therefore carried at its recorded profiles; the unchanged large aggregate
was not rerun. The isolated checker remains separate from installed-toolchain
qualification.

The warning inventory has 2,287 bodies. Thirty-six fall outside the reviewed
reference contexts, all at unchanged diagram-evaluation owners: eight concern
NType identity and dual evaluation, 24 concern binary-product projection and
pairing versus dual composition, and four concern terminal-arrow absorption
versus dual composition. Six have the same rule pair as prior references after
alpha-renaming and module-qualification normalization; that is not equality
of the critical reducts. These overlap families remain explicit R07/R12
normalization obligations. No warning originates at the two newly imported
product-adjunction clauses. No global confluence claim or runtime join is
inferred from the passing consumer suite.

The [verification](production_kernel_boundary_prerequisites_verification.json)
records exact source inventories, assertions, receipts, warning hashes and
resource measurements. The replay reproduces all 19 files, rejects drift at
all 19 original source pins, and leaves unrelated files to their owners.
The advisory rule-LHS scan reports no unreviewed compound slots in the
product-adjunction owner; source review and the complete original
product-family reviewer also retain its whole counit and unit projections.

Qualification reaches **639 LP files: 419 core/library and 220 reviewers**.
There remain 372 core/library files and 376 reviewers outside this snapshot,
the same five terminal runtime obligations, normalization/toolchain work and
production qualification. The next dependency layers continue toward the
original connecting-kernel consumer. This checkpoint does not resume the
separate nerve goal or promote the production kernel.
