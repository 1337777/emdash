# Foundation design matrix: families, mapping profiles and strictness

Date: 2026-10-14
Status: user-requested reassessment; strict-core/explicit-Gray direction for
the next specification, with no public default yet migrated
Owner: [living foundations plan](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

Latest steering, 2026-10-14: corrected duality/Op is the priority; the user
is not bound to strict/lax defaults. Strict ordinary Hom actions are allowed
under every candidate. The [strict core / explicit lax extensions review](EMDASH_STRICT_CORE_LAX_EXTENSIONS_REVIEW.md)
now recommends a Cartesian default core with an explicit Cat_lax universe
using Gray composition, including LaxFunctor as a separately staged layer.
The user accepts this direction for the next interface outline and requires
E and I_x=Hom_K(x,-) to share the same whole family classifier. For the strict
core this is Functor(K,Cat_s); weaker views must apply to both consistently.
The review records why Pi and the current profunctor Homd section still need
explicit lax structure, and why the local Q alias does not establish whole
coefficient/diagram coherence. Earlier references below to the default-lax-
transfor requirement describe the previous boundary.

Subsequent carrier/naming clarification: the user requests a Cat_lax-based
native interface and proposes retaining Cat_lax:Cat under the accepted
controlled-inconsistency policy. The review recommends assessing that
computational presentation without a new public GrayUniverse sort. The
generic Cartesian-composition boundary remains a separate documented
structural compromise, not something solved by the Cat:Cat size convention.

## Scope and notation

The user proposes `E : K -> Cat_sfunc_stransf`, asks for a comparison with
strict/lax defaults and the Q alternatives, and observes that extra map
requirements can live in Functord rather than general Transf. This review
treats those as independent design choices. The earlier all-E:K->Cat_cat
requirement is reopened for this comparison, not silently enforced against
the new suggestion or silently removed from the implementation contract.

Use these provisional names:

- `U_cart` / `Cat_cart`: strict category objects, strict functors, and the
  Cartesian strict-transformation profile in every higher dimension.
- `U_lax`: the same category objects and strict functors, with conventional
  lax higher transformations. Its standard semantics is a Gray/skew-Gray
  universe, not a strict Cartesian-enriched universe.
- `U_laxF`: a proposed coefficient admitting genuinely lax functors as
  transports. Its complete higher theory is not qualified by the current
  implementation.
- `Cart(A,B)`: Cartesian internal Hom. `L(A,B)`: conventional Gray-lax
  internal Hom. Both have strict functor objects in the strict-default
  comparison; their transformations differ.
- `T`: dimension-one transpose. `M(A,B)=T(Hom_oplax(T(A),T(B)))` is the
  transported mapping-profile proposal from the latest review.

The preceding migration target used public `Cat_cat` for the U_lax role.
The newly reopened strict-core option gives it the U_cart role instead,
with separately named lax mapping interfaces. Production is still
pre-migration. An existing non-library Cart classifier pilot is available.
No row below is a claim of a globally qualified kernel/model, and the
usual universe-size convention remains separate from local variance checks.

## General type-theoretic principles

1. Put admission in classifiers. A variable family or family map carries
   its allowed action in its type; operational symbols need not carry
   equality proofs or separately supplied comparison cells.
2. Separate the category of objects from its mapping profile. Sharing
   objects does not make two whole mapping categories interchangeable.
   Use an actual inclusion for weaker views, without a reverse coercion.
3. Choose closure uniformly. Cartesian evaluation/currying uses Cartesian
   mapping categories; Gray evaluation/currying uses the corresponding
   Gray mapping categories. Fixed evaluation/whiskering can be more general
   than joint Cartesian evaluation/whiskering.
4. Separate families, maps of families, and sections. Restricting Functord
   need not restrict all Transf or the section classifier defining Pi.
5. Preserve whole owners and their projection ladder. A classifier is
   useful only with the operations and higher action its consumers need.
   An opaque declared whole contract is not a coherence theorem.

These are reusable distinctions. Neither copying large semantic coherence
records into every term nor ignoring a required reverse cell is necessary.
Defaults are ergonomic choices within this architecture; they do not remove
the need to type operations according to their actual closure structure.

## Independent choices

| Axis | Choices | What it controls |
| --- | --- | --- |
| Ordinary functor default | Strict / lax | Which generic fapp identity/composition cuts are legitimate. |
| Ordinary Transf default | Strict / conventional lax / raw two-leg | Which naturality comparisons exist and which may compute to identities. The current selection is conventional lax. |
| Outer E | Strict / normal oplax / normal lax | Base-composition comparison and its orientation. |
| Coefficient of E | U_cart / U_lax / U_laxF | Transport functors and the higher naturality of their comparisons. |
| Q Hom | Nested Cart / nested L / mixed transported profile | The higher action of the direct v/f telescope and its u-parameter. |
| FF | General Transf / a stricter Functord carrier | Maps between already admitted families, independently of E's own higher action. |
| Sections | Lax sections / strict sections | Whether the usual nonconstant constant-family sections remain available. |
| Structural universe | Cartesian / Gray-aware / deliberately unqualified prototype | Whether generic joint composition/evaluation can apply to the universe itself. |

Under a lax functor default, writing E:Functor(K,U_cart) alone does not make
outer E strict. Nor may the Hom objects of U_cart then reduce to the ambient
lax Functor carrier: they must select strict transports. Both conditions
can be packaged in a native family classifier without operational proofs.

## Homd and Sigma comparison

Here “strict E” includes strict base composition; coefficient U_cart adds
strict higher naturality, not identity or invertibility of its components.
“Known failure” refers to the displayed contracts, not every possible theory.
These are representative combinations that separate the known obstructions,
not every row of the Cartesian product of all choices above.

| Design | Evidence / mathematical assessment | Native implementation and anticipated difficulty |
| --- | --- | --- |
| Strict functor/transfor defaults; U_cart and Cart Q; explicit lax interfaces | **Now the preferred architectural candidate to assess for the duality repair.** | Pi and the current profunctor Homd mate need explicit lax section profiles. Preserve weaker interfaces through correct inclusions, rather than forcing their cells to be identities. |
| Strict default; strict E into U_lax; nested Cart Q; FF even identity | **Known failure:** E[alpha]'s noncommuting fibre square would have to commute. | Changing only Q or FF cannot repair this; source admission must change. |
| Strict default; strict E into U_lax; nested L Q; FF even identity | **Known failure under standard Gray higher semantics:** the mixed three-cell example demands a reverse cell. | The direct root/leaf prototype typechecks, but its structural contracts do not establish the intended semantics. |
| Strict default; strict E into U_lax; mixed M inner mapping profile | **Local construction derived:** the transported closure supplies the required local u-action. Whole Q is open. | More mapping-profile views, coefficient composition and whole y/x assembly must be qualified. Avoid treating the local closure as the whole solution. |
| Strict default; strict E into U_cart; nested Cart Q; identity or strict FF | **Strong candidate for the simpler Homd core.** The two recorded counterexample inputs are excluded structurally. | Reuse the classifier and Cart computations, but adapt them to a separate coefficient. The old prototype changed public Hom(Cat), so it is not qualification of this row. Duality/root signs and Q coherence still need work. |
| Same U_cart families; FF lax across K, valued in U_cart | **Useful extension:** FF's extracted comparison is strict-natural in fibre variables while remaining directed across K. | This addresses the fibre-comparison issue without global strict FF. Whole omega-base naturality, Sigma-map action and intrinsic extraction remain to qualify. |
| Lax default; explicitly classified strict E into U_cart; nested Cart Q | **Same sufficient family data as the preceding strict-family rows.** A global strict-functor default is no longer logically forced. | More carrier/view plumbing; generic strict cuts must be guarded. The old lax migration and intrinsic-compositor coherence remain unfinished. |
| Lax default; oplax outer E, strict transports and strict-natural coherent comparisons | **Ordinary-base strict-total construction is supported.** The forward composition uses rho:E[qp]⇒E[q]E[p]. | Full omega-base Homd/sections and the oplax classifier need qualification. Reversing a name or a codomain alone is not that implementation. |
| Lax default; arbitrary normal-lax E, unchanged forward Hom/Sigma formula | **Known direction failure:** the available compositor points the wrong way. | Guarding rewrite rules does not supply a missing composition operation for all admitted inputs. Restrict formation or change the formula/doctrine. |
| Arbitrary lax transports E[p], unchanged strict total and Hom leaf | **Known associativity obstruction**, independent of the outer compositor direction. | A weak total or enlarged/factorization Hom changes the contract substantially. This is a separate research track, not the simplest first milestone. |

The first two failures and the local M proposal are detailed in the
[mixed three-cell review](../emdash2/audits/strict-default-action-boundary/homd_mixed_three_cell_review.md).
The independent outer-composition and transport obstructions are recorded
in the [Sigma profile review](EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md#lax-q-gray-uncurry-and-strict-sigma-maps-consumer-review-2026-10-14).
The standard strict-total reference uses Cartesian coefficients; its Gray
extension has a Gray total. See [Ara–Guetta v1, paragraphs 78 and 90](https://arxiv.org/html/2503.08832v1#S7).

## Functord versus Transf

Yes: extra requirements can belong to Functord. There are at least three
distinct map contracts; they should not be conflated.

| FF interface | Available comparison at p | Consequence |
| --- | --- | --- |
| Transf(K,U_lax,E,D) | D[p]FF[x]⇒FF[y]E[p], potentially lax-natural in the fibre | Component functors being strict does not suffice for a strict total map. |
| Transf(K,U_cart,E,D) | The same directed comparison, now a strict transformation between fibre functors | FF may remain genuinely lax across K. This is a coherent candidate for more general family maps after the identity core. |
| Strict Functord(E,D), included in Transf(K,U,E,D) | Base comparison is identity; boundaries strictly agree | Simplifies relative computation, but does not fix E[alpha], Q or the universe's joint composition. |

A strict Functord can be represented schematically as

```text
Obj(Functord_cat(E,D)) = StrictTransfor(K,U,E,D)
functord_include : Functord_cat(E,D) → Transf_cat(K,U,E,D).
```

The [native comparison](../emdash2/audits/strict-default-action-boundary/strict_displayed_maps_review.md)
already checks this mechanism with no operational proof payload. Its higher
Homs retain ambient modifications between admitted maps. That is a different
choice from the fully Cartesian mapping category; restricting map objects
does not automatically give Cartesian closure at every higher dimension.

If public Functord is narrowed, migrate the current whole/object
identifications with Transf and Catd/Functor categories. Retaining either
direction of automatic general admission would undo the restriction.
The existing stable Functord heads can remain useful; a parallel family of
ordinary fapp0_sfunc-style operations is unnecessary.

Pi then needs an independent choice. To retain general sections, use the
appropriate lax Transf(const(1),E) classifier, and keep the nonconstant
walking-arrow section. Strict Functord(const(1),const(B)) instead gives
strict sections and loses that consumer. Ordinary intrinsic-action
internalizations of lax transformations must likewise remain admitted on
the ambient side. These are real migration dependencies, not a reason
that a separate Functord classifier is impossible.

For U_cart families, do not strengthen FF beyond its coefficient-supplied
profile without a consumer requiring it. A strict-FF reference is useful
for isolating the identity/relative construction; it is not evidence that
all family maps must have identity base comparisons.

## The independent universe/composition issue

This is the largest risk that a Homd-only comparison can miss.

| Whole-theory choice | Assessment and cost |
| --- | --- |
| Strict Functor default; U_lax treated as an ordinary Cat; retain generic Cartesian composition at U_lax | **Known incompatible contracts.** A native countercheck collapses arbitrary lax squares before joint Eval or Homd is used. Cat_cart-valued E does not repair this. |
| A Cartesian structural universe, with lax mapping categories available separately | General and comparatively simple Cartesian foundation. It requires revising the identification of that universe's Hom with the default lax mapping category; this is a public-interface change, not the selected contract yet. |
| Retain U_lax as the public universe, but distinguish its Gray composition profile uniformly | Preserves the intended lax higher maps. Needs a genuine typing/ownership boundary so generic strict Cartesian composition cannot still specialize to U_lax. Replacing only Eval is insufficient. |
| Retain lax functors as default, with U_cart/strict-family classifiers locally | Avoids that particular unconditional strict-functor inference and gives broader types. Still requires coherent lax composition/action and corrected Sigma; the current implementation is not evidence of a completed general-lax theory. |

The [native composition countercheck](../emdash2/audits/strict-default-action-boundary/README.md#coefficient-countercheck-before-evaluation)
uses comp_prod_func(Cat_cat), strict fapp composition, constant functors and
fixed evaluation. It is independent of Q and FF. Thus the combination
“strict default + public Hom(Cat)=lax Functor_cat + unchanged generic
Cartesian composition” cannot be certified merely by finishing Homd.

This is where a general type-theoretic design is needed: uniform structure
classifiers and typed operations, rather than a hardcoded exception on
one occurrence of Cat. The standard mathematical distinction between a
Cartesian strict universe and a Gray universe is explained in
[Ara–Guetta v1, paragraphs 29–38](https://arxiv.org/html/2503.08832v1#S2).
Those facts guide possible models; they do not dictate that the kernel
must copy an external presentation verbatim.

## Failures to anticipate before implementation

| Tempting shortcut | What would go wrong | Decisive consumer to retain |
| --- | --- | --- |
| Make only FF strict | E's own higher action still causes the identity-Homd obstruction. | FF=id with noncommuting E[alpha]. |
| Make all Cat-valued Transf strict | Sections and ordinary internalized lax transformations collapse. | A nonconstant section of const(B) over the walking arrow. |
| Make Cat-valued functors strict while retaining arbitrary lax F and the usual Hom action | Hom_B(F[x],F[-]) detects F's composition at identity. Unbundling F does not remove this composite construction. | Nonidentity lax compositor viewed through representable Hom. |
| Retain the strict-default pre/right accumulation rule after returning to lax F | Specializing the transformation to id_F forces F[g]F[f]=F[gf]. | The actual identity-transformation specialization; guards or a compositor-aware replacement are needed. |
| Give Cart the same higher Homs as the ambient lax mapping category | The first-level restriction does not establish Cartesian higher closure. | A nontrivial higher modification and both evaluation orders. |
| Correct Eval but leave Cartesian comp_prod_func at the public lax universe | The earlier collapse route remains. | The independent coefficient countercheck. |
| Treat Q as only an alias because its objects are curried functors | Transf(K,Q) still uses Q's composition, units and higher action. | The whole represented section/root, not only its leaf. |
| Call Q a strict category while relying only on familiar bicategorical profunctor composition | Associativity/unit isomorphisms are not automatically the selected strict computation. | Retained whole comparisons/inverses and actual composition consumers. |
| Infer the omega profile from a lax square | Mixed higher action may demand an unavailable reverse cell. | The finite mixed three-cell example. |
| Carry strictness only as late property evidence | It may depend on the Homd machinery being constructed and create a bootstrap cycle. | Native carrier/view admission before intrinsic-property extraction. |

Generic fapp/tapp rules and classifier views should remain shared. The
comparison must also review canonical families actually generated by Hom
and intrinsic action: their object values alone do not prove that their
whole action factors through U_cart. No reference to a constant or ordinary
base is a substitute for the required general omega-base qualification.

## Recommendation and bounded next decisions

The later strict-core review linked above supersedes treating the public
lax-transformation Hom equation as immutable. With Functor_cat itself
Cartesian, Hom_Cat=Functor_cat may retain its spelling. The new question
is how to integrate the necessary explicit lax sections, Gray mapping
categories and eventual LaxFunctor without unsafe coercions or cloned
theories. The counterexamples in this matrix remain relevant to their
specific input/operation contracts.

The strongest simpler **Homd candidate** is currently strict families valued
in U_cart, with the Cartesian Q comparison and the direct whole ladder.
The user-proposed coefficient is a meaningful change of admission, and
avoids repairing each mixed dimension separately. It also allows an FF
which is lax across K but has strict-natural fibre comparisons. Keep the
option of stricter Functord at its own classifier when an operation needs it.

This does not yet select the best **entire foundation**. Keep the current
strict-default work as the implementation baseline while comparing the
two uniform universe arrangements above; do not restart the ambient default
merely because another local variant checks. If the unchanged public lax
universe equation is mandatory, its Gray-aware structural boundary is a
required part of the strict-default migration. If a Cartesian structural
universe is acceptable, that is the simpler mathematical organization to
assess against the existing API/consumer cost. Lax defaults remain a viable
alternative with explicit strict families, but require completing their
coherence/guard migration rather than assuming it already works.

Next decisions should be supported by these concrete deliverables:

1. Adapt the existing Cart classifier pilot to one whole admitted family
   and its canonical Hom/internalization consumer, keeping public defaults
   explicit. No proof arguments or duplicate ordinary action calculus.
2. Fix the Functord inclusion and section distinction together, if that
   restriction is selected; retain general ambient intrinsic extraction.
3. Rebuild the direct identity Homd ladder under the selected coefficient,
   with the same leaf and retained higher cells. Then qualify relative FF.
4. Resolve the independent public-universe composition counterexample
   before promoting global strict laws. Do not mark the overall goal done
   from a restricted Homd result.

This review is documentation-only. It reuses the recorded native and finite
evidence; no fresh probe matrix or public semantic migration is introduced.
