# Native kernel, boundary and homology families

Date: 2026-10-18 (UTC)
Predecessor: `9077c9b3`
Status: shared whole family owner and all original observations checked in staging; ordinary comparison layer remains open
Plan: [foundations migration](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_homology_family_verification.json)

The original family owner still used the ordinary walking-diagram category,
while its native K/Q structures and terminal-arrow introduction had already
migrated to the oplax profile. Its whole inputs now agree with those owners:

```
D : B → Functor_oplax_cat(WalkingArrow,C)
h : J ∘ A ⇒ D
K-family = K ∘ D
boundary = K[h] ∘ unit[A]
H-family = Q ∘ boundary-diagram.
```

The actual P, Q, A, D and h are retained. h remains a general lax
transformation; neither B nor C acquires a new ordinary-category hypothesis.
The initial-object parameter keeps the original total-dual meaning, now
spelled `TotalOp_cat`. Reversing 24 diagram-profile occurrences and that
one name change recovers the complete original owner modulo whitespace.
Every definition still uses the original compositions and adjunction data;
there is no new operational symbol or supplied comparison.

The reviewer uses the existing oplax whole evaluation for endpoints and the
generator. Its two arrow-component observations use the actual encoded
transformation profile on OddDual(WalkingArrow) and OddDual(C); the actual
base arrow is unchanged. All eleven original observations remain. The former
lax-functor composition negative is now a positive, as required by the new
public strict-functor default. The unrelated-arrow negative remains.

## Identity projection repair

After those interface substitutions, the owner and all earlier observations
checked, but the next-Hom identity assertion failed. A Hom of the oplax
diagram category has an EvenDual source. Its identity had already reduced
to the underlying category's identity, hiding the literal source tag from
the generic strict-functor identity rule.

Two source-identity joins at the existing alternating-duality owner are the
counterparts of the core's existing Op/CoAbove2/CoAt2 joins. They retain the
actual functor and point and apply only to the known projected identity.
The paired Odd/Even cases follow the alternating Hom recursion. No
transformation is made strict by these rules, and the core source itself
is unchanged.

Direct controls check both joins and reject collapsing arbitrary
endomorphisms. The actual homology-family next-Hom assertion now passes.
The inherited diagram evaluation controls and original diagram reviewer
also pass on the same source.

## Evidence and remaining work

The original homology-family reviewer passes 10 positive and 1 negative
assertions in 49.366s with maximum child RSS 2272800 KiB. The alternating
identity driver passes its two positive/two negative controls together with
the inherited diagram controls in 46.648s. Both use the existing
300s/4GiB/o=20 profile. The core's 281/81 regression receipt is carried only
after confirming its exact input bytes are unchanged. Subject reduction,
serial execution, file limits and no-swap containment remain enabled.

Owning-file LHS audits report no unreviewed candidates. Each dual source
pattern is an annotated discriminator for the erased identity tag.
There are 178 added warning bodies: 106 overlaps with named first-action
projections, 20 with source-identity normalization, and 52 with higher
projections, whiskering, dual actions and profile views. The canonical joins,
noncollapse controls and real next-Hom consumer are qualified. This does not
establish global confluence across every nested duality or constructor.

The ordinary whole homology comparison and its point observations remain
unmigrated. Their diagram profiles and reflection/reconstruction consumers
must be reviewed at their actual uses, retaining all chosen maps and inverse
data. Terminal/initial zero-column integration, remaining libraries,
redundant strict wrappers, production promotion and the final
central/catalogue/health/CI/source-pin gates remain required. The separate
application-equivalence goal remains paused.
