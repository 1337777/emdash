# Internal Pi, canonical evaluation and Cartesian intrinsic action

Date: 2026-10-15
Predecessor: `2334f755`
Status: staged source through section 17e checks; arbitrary-composite
intrinsic coherence and the complete public/downstream pass remain open
Owner: [foundations plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [exact verification](production_section_pullback_verification.json)

## Original section and internal Pi owners

The [section 17e migration](production_section_pullback.lpfragment) retains
section_pullback_func, section_pullback_sec, the existing endpoint theorems,
section_weaken_funcd and the internal Pi action owners. Their admitted-family
observations now use Cat_cart. The original Pi remains the default lax
section category; a general FF has not been made a strict transformation.

The actual internal Pi cell computes to section_pullback_func, both for a
base functor F and for the arrow action G[p] of a whole G:K->T(Cat_cart).
The latter consumes a [whole reindexing comparison](production_cartesian_reindex_view.lpfragment)
between represented precomposition and Pullback_catd. The generic F_1
reading decomposed incompatible endpoint tags before recognizing the
transpose. Retaining the actual T(G) head fixes that computational issue.
Every family, endpoint and mapped base arrow remains constrained; an
unrelated replacement base functor is rejected. This is a proof-time
comparison between existing owners, not equality data passed to Pi.

## Classified Cartesian maps

For U in Hom_Cart(K,Cat_cart)(E,D), write eps_U for its ordinary
strict_transfor view. The [intrinsic rules](production_cartesian_intrinsic.lpfragment)
compute the entire filler functor:

```text
fdapp1_int_hom_func(eps_U,p,u,v)
  = (U[y])_1(E[p](u),v).
```

At the transported identity this is the identity naturality cell. The
same rules apply to the ordinary view of the existing

```text
Op_funcd(U)
  : Hom_Cart(CoAt2(K),Cat_cart)(Op_catd(E),Op_catd(D)).
```

This uses the actual classified map, including its fibre action, rather
than supplying a separate laxity witness. The [Cat_cart naturality views](production_cartesian_naturality.lpfragment)
are instances of the pre-existing public-coefficient rules: pre/right
computation for every default lax map, post/left computation only for the
strict_transfor constructor. The negative controls keep the two routes
distinct for a general FF and retain a nonidentity constant-section loop.

Eval_funcd now has the canonical Cartesian map type

```text
Eval_funcd(I,E) : Hom_Cart(K,Cat_cart)(V_I(E),E)

V_I(E)[k] = Cart(I,E[k]) × I.
```

It is the existing constructor, with its ordinary view supplied by
strict_transfor. Its fibre map remains Eval_func. No second evaluator or
default strict-Functord classifier is introduced. Admitted E has strict
transport and Cartesian coefficient action, so this evaluator is strictly
natural across K. Its shifted Op is now directly well-typed and its actual
component computes to the transpose of that same evaluator.

The existing Op_funcd also now computes a constant Cartesian diagram map
to the constant map of transposed fibres over CoAt2(K). The operation
retains the actual F:A->B and returns T(F):T(A)->T(B).

## General lax data through evaluation

For arbitrary lax FF:R=>V_I(E), the original leading-evaluation composition
rule now checks against the actual evaluator Hom action:

```text
lambda_(Eval o FF)(p,u)
  = Eval_y,1(lambda_FF(p,u)).
```

The source and target of Eval_y,1 are the transported FF[x](u) and
FF[y](R[p](u)). The input lambda_FF is the existing intrinsically extracted
cell; it is retained as data, not replaced by identity or assumed invertible.
This is a concrete general-FF consumer. It does not yet qualify composition
of two arbitrary lax displayed maps.

Three existing normalization interfaces were needed:

- [Rigid Cartesian Hom action](production_cartesian_hom_action.lpfragment)
  has the same consumed-object computation as the public universe, and a
  guarded whole source-identity comparison after the identity projects to
  id_func. Its whole rigid head stays stable.
- The two Cat_cart point-naturality observations above join the existing
  ordinary strict-view and default pre/right computations.
- Eval_func now evaluates a neutral pair z through its actual projections:
  Eval[z]=sigma_Fst(z)[sigma_Snd(z)]. The former literal-pair-only rule
  could not compare the source types of the arbitrary-FF consumer after
  its component had projected. This correction is local to Eval; an
  unrestricted product/Sigma eta conversion remains rejected.

The [controls](production_section_pullback_controls.lpfragment) start from
the actual intrinsic root and follow x/u, y, v, p and the filler. They
also exercise the whole Cartesian filler functor, shifted Op, canonical
evaluation, constant Cartesian duality, internal Pi, and the general-FF
leading composite. All earlier Homd, noninvertible higher action, Sigma and
recursive base-change consumers remain included.

## The retired mirror clauses

Thirteen pre-goal section 17e commands applied Op_funcd to raw Functord
terms while keeping the base unchanged. They are retained verbatim in an
explicitly inactive comparison block. They are not counted as qualified
code and must not be re-enabled to justify a general FF result.

Their ordinary evaluation, pairing, weakening, identity and leading-composite
computations remain active. Valid Cartesian-map intrinsic action is now
handled generically over its actual shifted base; canonical evaluation and
constant Cartesian maps have direct positive consumers. This is not a
claim that every old raw mirror expression has acquired a Cartesian lift.

The later pre-goal fdapp1_projection_target still passes raw FF to Op_funcd.
That observational consumer must be rebuilt from the already corrected
whole intrinsic source/target owners, which use the relative Homd package
and ordinary FF composition. It remains an explicit migration obligation;
commenting the obsolete mirror clauses does not discharge it.

## Next boundary

The full source now reaches section 18b, where Op_prof's component still
uses the old Cat_cat coefficient. No original named declaration or later
section has been omitted. Before broadening that library pass, qualify the
concrete intrinsic action of GG o FF for two general lax displayed maps,
using the current leading-evaluation case as a reference. The intended
cell law retains both cells:

```text
lambda_(GG o FF)(p,u)
  = GG[y][lambda_FF(p,u)] o lambda_GG(p,FF[x](u)).
```

The whole filler-functor and higher-index comparisons must accompany that
cell observation. General Q/mate coherence, later projection/laxity
consumers, whole inverse/duality qualification and the public, reviewer,
catalog, health and CI gates remain required. This audit is a non-library
checkpoint and is not a global confluence or unrestricted Q-model claim.
