# Cartesian structural owners and recursive Sigma base change

Date: 2026-10-15
Predecessor: `e268b24230c05d2e0fafbc4305ea830acb8d6232`
Status: staged original-source migration through section 17d checks;
general Q/mate coherence and public/downstream migration remain open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](production_structural_pullback_verification.json)

## Structural profiles

The [section 17c migration](production_ordinary_structural.lpfragment)
retains the original weakening, exchange and diagonal symbols and their
projection ladders. Displayed weakening uses Cat_cart and the already
qualified Const_func_func. It remains a default lax Functord across K.

Exchange and diagonal have their Cartesian mapping profiles:

```text
sym_func_func(A,B,C)
  : Cart(A,Cart(B,C)) -> Cart(B,Cart(A,C))

diag_func_func(A,C)
  : Cart(A,Cart(A,C)) -> Cart(A,C).
```

Their functor objects are the public strict functors. Transformation
parameters are the Homs of those Cartesian mapping categories. Ordinary
tapp projections observe them through the existing strict_transfor
inclusion; no caller supplies a strictness proof. Default Transf and
Functord are not redefined as strict.

This restriction follows the laws of these particular owners. For a raw
H:A->Functor_cat(B,C), its mixed naturality square has one direction.
Exchanging A and B while keeping the same default comparison convention
needs the reverse square. The directed-square model in the
[preceding review](production_evaluation_reindex_review.md) separates these
directions. The unrestricted same-profile involutive exchange cannot be
retained under that interpretation.

For diagonalization, put D[p]=H[p][y] o H[x][p] for p:x->y. For composable
p,q, the comparison from D[q]D[p] to D[qp] uses the naturality square of
H[p] at q. It is an equality for Cartesian H[p], but only a directed cell
for a general lax H[p]. Thus the old strict diagonal computation also
needs this profile. These are necessary corrections to the existing
Cartesian structural laws, not a construction of a general mixed
lax/oplax exchange or a future lax-functor diagonal.

The [controls](production_ordinary_structural_controls.lpfragment) check
the actual whole functor action, single and double exchange, the two
components of exchanged transformation action, diagonal action and its
transformation component, and higher data after double exchange. Raw lax
inner functors and unclassified lax transformation parameters are rejected.
The inherited general-FF and noninvertible-action controls still pass.

## Whole duality and pullback

Write T=Op_cat, R=CoAbove2_cat, O=TotalOp_cat. For

```text
E : B -> Cat_cart
F : A -> R(B),
```

the [new whole rule](production_total_op_pullback.lpfragment) computes

```text
F*(O_fib(E)) = O_fib((R(F))*E).
```

R(F):R(A)->B is the actual dualized functor. The right-hand family has
base R(R(A))=A. This is the standard compatibility of the existing total
fibre duality with composition/reindexing; it does not transport an
operational equality or create another duality operation.

The first concrete consumer is the source type of recursive Sigma base
change. With I_A=Hom_A(x,y), I_K=Hom_K(Fx,Fy), and
H(f)=Hom_E[Fy](E[f](u),v), its positive presentation uses

```text
O_fib(H) : O(I_K) -> Cat_cart
O(F_1)  : O(I_A) -> O(I_K).
```

The existing sigma_pullback_total_func on those data is then total-dualized
back. The original first-Hom owner remains stable; only its existing next-Hom
projection rules expose this recursive body. There is no new auxiliary
Sigma-composition owner and no replacement of first-Hom action by a capped
point equation.

Before the pullback/duality rule was installed, subject reduction failed
on precisely the whole positive-family comparison. With it, the existing
hom_con reindexing and ordinary strict composition laws close that comparison.
The [section 17d migration](production_pullback_structural.lpfragment)
then checks, including the original exchange/evaluation and adjunction-cut
consumers with the Cartesian mapping coefficients they now consume.

## Actual directed-cell computation

The [consumer controls](production_pullback_structural_controls.lpfragment)
check the whole negative Hom family for a general E before choosing f or
a filler. For a constant family at C, Sigma is A×C and total base change
has the expected arrow action

```text
(p,a) -> (F[p],a).
```

Applying the actual next Hom of that total map to an arbitrary two-cell
(theta,beta) computes

```text
(theta,beta) -> (F_1[theta],beta).
```

Both components are checked independently, with arbitrary directed beta
and theta. The F=id loop control rejects replacing theta by identity.
These observations use the recursive whole functor, not a separately
supplied comparison cell. They supplement the inherited Homd, section,
constant F[alpha], Sigma and general-modification controls.

## Current boundary

The complete original source is retained. It now stops at the old Cat_cat
tag on section_pullback_sec's component in section 17e. That section's
internal Pi action and the later profunctor and extracted-laxity consumers
remain to migrate. General Q/mate coherence, including composed lax-FF
intrinsic actions, remains a separate required consumer qualification.

The authoring replay is a non-library checkpoint. It does not promote the
public kernel, establish global confluence, or complete the downstream,
reviewer, catalog, health and CI gates.
