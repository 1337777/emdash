# Ordinary-target arrow diagrams after the duality migration

Date: 2026-10-17
Predecessor: `5f96019d`
Status: original ordinary-arrow interface and reviewer qualified in the staged migration; broader migration and production promotion remain open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The original public interface is retained:

```
one_cat_arrow_diagram_func(C,C1)
  : LaxArrow_cat(C) → Functor_cat(WalkingArrow_cat,C).
```

The generic lax-transformation exchange now has an oplax diagram target.
This ordinary-target consumer already has OneCat(C), which supplies the
existing one_cat_strict_transfor admission. Its body uses that admission,
the existing Cartesian exchange, and Functor_cart_include to recover the
original ordinary target. The source category stays unrestricted, and the
public OneCat(C) premise is unchanged. No global strict naturality or new
caller-supplied comparison is added.

The original point-introduction unifier is adapted to Cartesian exchange:
its strict input is observed through strict_transfor. A typed reflexivity
definition checks that whole-functor comparison. It remains proof-time;
neither exchanged nor introduced whole runtime head is folded. The admitted
universal arrow receives only its named component projection to the original
universal arrow. The generic admission constructor and whole strict view
remain stable.

Two projection-order repairs belong to the existing exchange owner. Its
identity clause accounts for a total-dual source whose identity annotation
has already normalized. Its composition clause accounts for the Cartesian
inclusion having already projected the two exchanged transformations. The
same H, intermediate object and actual input arrows are retained. This is
the ordinary observation of existing Cartesian composition, not a rule on
arbitrary lax transformations.

The original reviewer retains all nine positive assertions, its negative
against converting arbitrary higher cells into equality, and its higher-Hom
typing query. The additional reviewer checks the actual point comparison,
rejects replacing its generating arrow, and checks that the two whole heads
are still distinct at runtime. Combined: ten positive and three negative
assertions. The original square-component inputs use hom_int_view, the
existing inclusion of the canonical Cartesian Hom family.

The core/projection regression also passes all 268 positive and 66 negative
assertions. Subject reduction stays enabled. Both owning-file LHS audits
have zero unreviewed candidates; the added source/category discriminators
are documented. The [verification](production_one_cat_arrow_verification.json)
records exact receipts, source closures, diagnostics and warning changes.

Warning review is scoped, not a confluence certificate. Relative to the
preceding arrow attempt, there are 26 additional warning bodies: 17 concern
total-dual identities and their existing component/composition observations;
nine concern the included composition clause (six unit overlaps, one
product-codomain normalization, two double-exchange overlaps). The latter
two retain the pre-existing issue of observing generic image composition
after the Cartesian inclusion has erased its application head. The typed
ordinary-arrow identity/composition and retained core controls pass. These
checks do not qualify every nested-duality, product-codomain or included
double-exchange specialization; those warning boundaries remain explicit
for promotion and actual downstream consumers. No unrelated rewrite family
is added to eliminate warnings mechanically.

The original reviewer takes about 36s under the reviewed 90s/4GiB/o=20 import
profile; the core regression takes about 21s under 90s/2GiB/o=20. A separate
full-normalization diagnostic of the expanded arrow constructor exhausted
the 4GiB allocation guard after imports. It is not a failed typing result,
and no larger limit or semantic workaround was used. The original typed
observations pass at the existing limits; unrestricted normalization of
expanded admission evidence is not performance-qualified by this slice.

Replay after changes to Cartesian exchange, its inclusion, total-dual identity
computation or the ordinary-arrow owner: regenerate production_owner_migration.py,
then run one_cat_arrow_profile_controls.lp and the affected core regression.
The broader Hom-comparison import passes this owner and stops at
emdash3_2_one_cat_modifications.lp:27–29: the old internalization rule has
Cat_cat where its family now requires Cat_cart. It reaches that diagnostic
in about 51s at the existing 4GiB profile. Review the original modification
owner next, then the external Hom-action admission; preserve arbitrary source
bases, actual chosen comparisons/inverses and the original allowed laxness.
All sources in this review are non-library migration inputs. Redundant
strict-functor wrapper retirement, remaining library adaptation, production
promotion and final qualification remain required.
