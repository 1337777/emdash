# Whole ordinary diagram-family reconstruction

Date: 2026-10-18 (UTC)
Predecessor: `597b6b4c`
Status: staged original owner and all six original observations checked; terminal/initial family presentations remain open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_one_cat_family_reconstruction_verification.json)

The reconstruction still accepts the original arbitrary family
`D : B → Functor_cat(WalkingArrow,C)` and the existing OneCat(C) hypothesis.
B is unrestricted. Both maps are the original ordinary reconstruction
maps at `Functor_cat(B,C)`, followed by exchange. The reconstruction's
previously supplied whole shape-universality comparison is unchanged; no
new reconstruction or inverse-assembly assumption is introduced.

The original implementation used exchange for its fixed endpoint functors
and for its varying shape arrow. The migration therefore uses the qualified
ordinary-target exchange consistently at those positions. Three helpers are
definitions through existing owners:

```
ordinary family evaluation at i = evaluation at i ∘ ordinary exchange
ordinary shape action of D at u = (ordinary exchange(D))[u]
endpoint composition path       = existing strict-functor composition path.
```

The endpoints are the existing `one_cat_family_exchange_at_func` values.
The shape action is `one_cat_diagram_family_transf`; it retains the entire
B-variable and higher action through its actual exchanged functor. The
general `diagram_family_transf` keeps its oplax profile. The new definitions
do not identify those classifiers or require a separately supplied square.

The complete original owner is recovered, modulo whitespace, by undoing
eight interface substitutions. This includes the entire original to/from
definitions, both inverse-law proof bodies, and the evidence constructor.
The arbitrary D, the existing whole reconstruction and its chosen inverse
maps are retained. The reviewer keeps its four runtime endpoint identities
and two actual-map evidence projections; explicit endpoint arguments avoid
the already-recorded inference ambiguity of the exchanged map aliases.

The first candidate passes the original owner and all six reviewer assertions
in about 103 seconds at the existing 600s/4GiB/o=5 profile, using about
2.75 GiB maximum child RSS. There are no new primitive declarations,
rewrite rules or unification rules. All 2705 warning bodies match the
same-import baseline, ignoring source locations. The staged core and the
existing mapping/exchange controls retain their exact previously checked
input closures, including their negative controls. No broad rerun of those
unchanged targets was needed.

The fresh central gate passes reconstruction and stops at
`terminal_adjunction_presented_family` in
`emdash3_2_one_cat_terminal_adjunction_families.lp`. It declares an ordinary
diagram-family output while composing the now-oplax general
`transf_arrow_diagram_func`. The corresponding initial presentation has the
same issue. Their OneCat universality consumers already have the necessary
ordinary-target assumption. Next distinguish the correctly typed general
oplax presentations from their guarded ordinary presentations, retaining
the actual chosen e and F and the existing adjunction data. Review the
coupled observation consumers; do not silently add a general ordinary/oplax
coercion or discard the unguarded general presentation.

This is staged migration, not production promotion. Remaining original
library owners, redundant strict-functor wrappers, catalogue/health/CI,
source-pin review and the final qualification remain required. The separate
application-equivalence goal remains paused.
