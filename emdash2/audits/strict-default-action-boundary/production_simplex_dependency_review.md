# Existing dependent-simplex and chain-pair migration

Date: 2026-10-23 UTC
Predecessor: `85c8fa0e`
Source pin: `f8af1fca472657ff1598c639eb29c0566e7b2ec0`
Status: qualified non-library slice; production promotion remains open

The [exact verification](production_simplex_dependency_verification.json)
qualifies 379 core/library files and 196 complete reviewers (575 files).
All four fresh scopes below match their actual emitted inputs. There is no
claim of whole-goal completion or a general confluence/performance theorem.

This slice migrates the existing dependent-simplex dependencies reached by
the chain-pair/exactness consumers. It does not develop the paused nerve
reconstruction/equivalence goal. The selected-presentation adapters reached
later in that chain remain the next migration boundary.

## Preserved constructions

The thirteen original library modules and nine complete reviewers retain
the recursive triangle/tetrahedron and flagged dimension-three interfaces,
their whole maps and further Hom actions, represented associator, selected
face codes and actual face functors, cycle lifts and exactness reindexing.
Seven files need source adjustments; fifteen are unchanged.

The triangle family now uses the actual total-dual Sigma/Hom presentation:

```text
I = Hom_K(x,y)
H = homd_(id_E,x,u,y,v) : T(I) → Cat_cart
G = TotalOp_catd(H)    : O(I) → Cat_cart
DependentTriangle(E,x,u,y,v) = O(Σ_(O(I)) G).
```

The whole triangle map is the existing first Hom of `sigma_map_func(FF)`.
Its index arrow belongs to `Homd_index_cat(I)`; it is no longer used directly
as an ordinary displayed map. The new **defined**
`dependent_triangle_map_catd` is first-Hom action of
`Homd_index_total_family_func(I)` on that same arrow. The recursive reviewer
uses this actual displayed map to read the next dependent component. General
lax FF remains admitted; no new comparison or strictness evidence is input.

The represented-associator definitions use the existing ordinary
`Rep_transport_func` view of their canonical Cartesian Hom action. Selected
face realizations use public strict functors directly. The six redundant
join wrappers/property declarations are retired locally, while their actual
join maps and selected face data remain. Of 128 original named declarations,
122 remain, with the one defined family-action view added. The not-yet-staged
`emdash3_2_tetrahedron_faces.lp` still has legacy join-wrapper consumers to
migrate; this is not a claim that every original source is already migrated.

## Two existing core owners

The original compositor reviewer exposed a missing capped covariant
projection. The whole `fapp1_at_transf(F,x)` compositor already computes to
an identity under the strict-functor default. The new `fdapp1_int_cell`
instance reads that same identity, paralleling the existing contravariant
instance. It keys on the named action constructor and leaves all inferred
family slots open. It does not make arbitrary FF strict or add a supplied
compositor witness.

The original dimension-three `sigma_Fst`/`sigma_Snd` queries exposed an
inference failure comparing nested postcomposition with precomposition by a
base composite. A generically typed projection helper did not resolve it.
Broadening the existing identity-family pre/post comparison first passed the
simplex group, but regressed `emdash3_2_commutative_algebra_affine_glue.lp` in
the central run. That candidate is rejected. Converting both sides immediately
to raw composites also failed. The narrower candidate preserves the original
two-arrow rule and adds its three-arrow nested instance: the same incoming
arrow followed by the same pair of base arrows. Its side conditions retain
every arrow and endpoint. Its first version checked whether the base arrow
was that composite in a side condition. The final version matches the consumed
literal `comp_fapp0` constructor directly, then compares its two actual arrows.
This avoids attempting the new rule on unrelated precomposition inputs. The
final focused and shared-owner scopes pass, as recorded below.

This adds one runtime projection and one proof-time three-arrow instance;
it does not add a primitive, a nested-projection rewrite, a new associativity
law or a runtime unfolding of either represented head. The original bare
dimension-three projection queries now pass unchanged. A separate typed
reflexivity check, runtime nonconversion control and wrong-incoming-arrow
control exercise the comparison. The advisory LHS audit reports zero
unreviewed candidates; the two changed clauses were also reviewed manually.

The saved failures are exact removal controls. Removing only the new
three-arrow clause reproduces the core hash of
`20261023T012356Z-e3a1c689325240ee9015f8e122994c53`, which fails the original
dimension-three projection query. Removing the covariant clause as well
reproduces `20261023T012134Z-cdc715cd3a4d4eeab1109b7c79b5638b`, which stops
at the original compositor extraction assertion. No extra projection helper
is present in the selected source.

## Validation and boundary

The earlier focused group passed at receipt
`20261023T013008Z-69259d0ef06b4257b50386009289c125`, before the broad-comparison
regression was discovered. It does not qualify the final narrower source.
It retains all 66 original assertions: 58 positives/eight negatives become
59 positives/seven negatives because the old arbitrary-functor compositor
nonconversion now contradicts the chosen strict default. No assertion is
omitted. The three additional comparison controls contribute one positive
and two negatives. Original type queries, including the recursive projections,
remain. Both the emitted package and all 50 focused dependency files match
the corresponding checked candidate exactly. The side-condition version's combined
affine/simplex run passes in **104.239s / 626,768KiB RSS** at receipt
`20261023T014115Z-5279efc95be8435ea383383087d7d928`. Its earlier 90-second
run passed the previous affine and dimension-three stops before timing out
in unchanged abelian dependencies; the measured extension uses 180s/2GiB
with the other guards unchanged.

That side-condition version's central scope passes in **517.767s / 2,155,136KiB RSS** at receipt
`20261023T014357Z-711bfba089ca4c6e854e4a8d52666965`. Its 2,497 warning bodies
are identical to the prior central inventory. This is a fresh check of the
changed core, not hash-only carry from the earlier snapshot.

The unchanged broad library driver times out at 600 seconds in
Hom-comparison/adjunction dependencies, receipt
`20261023T015237Z-625afea149f742a387ea00211dcb2e8a`. All its source inputs
except the core match the earlier successful scope. The completed local
commands in those dependencies take approximately 17–36 seconds, versus
13–27 seconds previously; its larger import takes 71 seconds versus 55.
This is a performance signal, not a typing counterexample or a completed
library check.

Matched isolated `prof_defiso_evaluation_paths` runs both pass. Removing the
three-arrow rule allocates 11,262,513,608 words; the side-condition version
allocates 12,786,966,355. Their wall times are 66.947s and 51.102s respectively,
so elapsed time alone does not explain the broad timeout. Matching the literal
composite reduces allocation to 11,388,819,965 words and takes 43.612s in its
isolated run, receipt `20261023T021148Z-e777f2e099f242d28b5b5d326a3a7b70`.
The final focused simplex scope passes at
`20261023T021012Z-7d247974d4f44953bbf0e8eca45ffffa`.
This is a targeted matching improvement, not a general normalization or
performance qualification. The final literal-composite full-library check
also reaches its 600-second cap at
`20261023T021441Z-0aaab024b55440f58c3783e0799d7bc6`. The separately validated
[time extension](production_resource_time_extension_review.md), checkpoint
`cb287c01`, admits a measured 900s/4GiB retry. It preserves normal defaults,
all memory/serial/file/no-swap protections and subject reduction. The
unchanged final mathematical source was checked again with that
library deadline; the central and residual profiles stay at 600s/4GiB and
180s/2GiB. The GC variants are not selected for these runs.

The final broad library scope passes **1,403 positive and 241 negative
assertions** in **660.163s / 2,373,224KiB RSS** at receipt
`20261023T024853Z-a22dd35c113b41a4838c55d2063faccc`, under 900s/4GiB/o=20.
Its input hashes match the emitted candidate. The 2,515 warning bodies are
identical to the previous broad library inventory.

The final central scope passes **2,351 positives/350 negatives** in
**507.813s / 2,200,020KiB**, receipt
`20261023T025955Z-8e438f0781474e55a0e427c43081843e`, with the same 2,497
warning bodies as its predecessor. The residual group passes **83/10** in
**172.300s / 505,644KiB**, receipt
`20261023T030824Z-7bdb9757bf39466fb5ae74fa9b08cb41`. The final focused scope
passes **61/9** in **60.585s / 279,352KiB**, receipt
`20261023T021012Z-7d247974d4f44953bbf0e8eca45ffffa`.

The focused inventory has 21 bodies absent from the larger library inventory:
seven original semisimplicial identity specializations, twelve existing
product/terminal context variants and two already recorded NType pre-action
retag variants. Its smaller scope also omits warning bodies from unimported
owners; this is not removal of those rules. The four residual variants are
byte-identical to the earlier kernel-factor inventory's NType pre-action and
inverse-cancellation variants. The exact origin/body differences are retained.
The central and broad-library multisets are unchanged. No symbolic join or
global confluence certificate is inferred from these inventories.

Only `emdash3_2.lp` changes among the 553 prior qualified sources. Because it
changes shared computation/comparison, unchanged-source hashes alone do not
carry their checking evidence: the fresh central, existing broad-library and
residual-consumer checks above requalify them. They retain subject reduction,
warnings, serial execution and resource guards. The central/library profiles
use 600s/4GiB/o=20 for the central scope and the measured 900s/4GiB/o=20
library extension; the residual group uses 180s/2GiB/o=20. These ceilings
are not performance qualification.

The receipt/source reconciliation covers every previous qualified file and
all 22 additions. Coverage is now **379 core/library files and 196 complete
reviewers**, leaving 412 core/library files and 400 reviewers unstaged.
The next concrete migration is the selected kernel/cokernel presentation
adapters, whose ordinary-diagram types must match the already migrated
oplax whole adjunctions. Their supplied data and existing generality/guards
remain requirements, not optional inputs to discard.

The five terminal runtime obligations, remaining registered-source migration,
normalization/warning review, supported-checker qualification and production
source-pin/catalogue/health/prose/CI gates remain required. No production
source is promoted by this non-library slice.
