# Cartesian path realization for carrier families

Date: 2026-10-18 (UTC)
Predecessor: `9f4751a5`
Status: staged carrier family, core regression and original invertibility-sieve reviewer checked; broader migration and the central gate remain incomplete
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_path_cartesian_verification.json)

The first unmigrated carrier family was the original composite
`Path_cat_func ∘ comm_ring_carrier_func`. The former lands in `Cat_cat`,
whereas the selected family classifier requires `Cat_cart`. The ordinary
path realization is used elsewhere with its existing transformation action;
its entire interface should not be silently retagged.

The new structural whole owner is
`Path_cat_cart_func : Grpd_cat → Cat_cart`. It preserves the path-category
objects and the original actual `path_map_func` for each function. Its
whole Hom action is the existing composite

```
Path(Function(A,B))
  → Path(Functor(Path(A),Path(B)))
  → Cart(Path(A),Path(B)).
```

The first arrow is `path_map_func` applied to the object function
`f ↦ path_map_func(f)`; the second is `Core_incl_func` into the Cartesian
mapping category. Thus equalities between functions and their higher
equalities retain whole internal action. This is a declared structural
realization with computed projections, not a theorem lifting every
Cat-valued family into the Cartesian coefficient. It takes no separately
supplied strictness witness or operational equality argument.

The actual ring family changes only its final coefficient and realization
head. Reversing those two substitutions recovers the complete original
`emdash3_2_commutative_algebra_category.lp` byte for byte. The ring-carrier
functor and its complete Hom action are unchanged.

The first whole-action rule checked, but the capped consumer did not reduce:
the generic `fapp0(fapp1_func(...))` rule can select the capped owner first.
A constructor-specific capped projection now returns the same actual
`path_map_func`. Both orders and reflexive higher action are checked. The
new rules use the stable realization head and wildcard inferred endpoints;
no reducible alias discriminators or outer-eliminator commuting rules are
introduced. The complete staged core's strict LHS audit reports no
unreviewed candidates; the new owner-specific patterns were also inspected.

Seven positive and two negative focused controls pass, including the
original carrier fibre, the transported ring element, the iterable equality
action and the separation of the two mapping profiles. The full staged
core regression passes its 276 positive and 79 negative assertions. The
focused checks take about 27 seconds under the existing limits.

Sixteen added warning bodies comprise one whole/capped overlap, seven
identity or dual-identity patterns, two generic strict-composition
overlaps, two untyped product-projection overlaps, and four inherited
pre/postcomposition or naturality overlaps. The actual projection orders
and reflexive higher action are tested. This records a bounded consumer
qualification, not global confluence of all generic accumulation paths.

The first central run passes the ring category and several subsequent algebra
owners, then reaches its 4 GiB memory cap while importing localization at
zero. That unchanged module passes independently in 35.143s with maximum
child RSS 1645112 KiB. This distinguishes the aggregate's cumulative import
footprint from the local theorem's own cost. A second central run used an
explicit 600s/6GiB/o=5 profile after observing about 14.5 GiB available host
memory. The normal defaults, serial/file restrictions, subject reduction and
no-swap containment remain unchanged.

That 6 GiB run passed the localization modules and reached the original
presheaf total-restriction constructor in 196.169s, with maximum child RSS
4721968 KiB. Its argument was the canonical Cartesian `fib_cov_transf`,
whereas `sigma_map_func` consumes its ambient displayed-map view. Applying
the existing `strict_transfor` inclusion resolves the mismatch without
changing either interface or imposing strictness on general displayed maps.
The original reviewer also needed two `Cat_cat` family-result annotations
changed to `Cat_cart`; the ordinary Cat identity terms remain unchanged.

The complete original reviewer passes all 25 positive and 4 negative
assertions in 47.975s with maximum child RSS 2361888 KiB, at 300s/4GiB/o=20.
This includes literal total restriction and invertibility-sieve computation.
All 2415 warning bodies match its pre-annotation-fix run. Reversing the one
inclusion and the two annotation substitutions recovers the respective
complete original source files byte for byte. The broader central check was
not rerun after this final focused correction and is not claimed green.

At this checkpoint the next bounded review will compare migrated rule
patterns, stable projection owners and slow consumers with the pre-goal
source. The user requested this review on 2026-10-18. Prioritize concrete
local inference, normalization and resource improvements; preserve the
selected migration contracts and defer optional foundational redesign.
Production promotion and final catalogue/health/CI remain outstanding.
