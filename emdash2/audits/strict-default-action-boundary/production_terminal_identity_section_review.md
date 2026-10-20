# Terminal identity section: pre-goal and migrated comparison

Date: 2026-10-20
Checkpoint under review: `deedfa1fa665f8ca31db84fe12c9ad6b64a9cd26`
Status: inherited runtime boundary isolated; no mathematical rule adopted
Evidence: [verification](production_terminal_identity_section_verification.json)
Reproducer: [expected-rejection fixture](production_terminal_identity_section.lpfragment)

This follows the [canonical terminal contraction
review](production_terminal_canonical_review.md). That candidate failed an
ordinary Hom component projection after exposing the identity transformation
of the constant terminal family. The new comparison isolates that identity
directly, without the candidate's Hom or conjoint contractions.

## The two readings

For the migrated coefficients C = Cat_cart, let

```text
U = const_K(1)
e = id_[K,C](U).
```

The existing constant-section comparison also types e as a functor K → 1.
Its component as a transformation is expected to be the identity functor
of 1. The two printed runtime forms are instead

```text
component(e,k) → Const_func(1,1,fapp0(e,k))
id₁           → id(Cat,1).
```

The first reading uses the generic constant-family section component rule;
the second is the existing identity functor. The retained application of e
does not reduce to a chosen terminal object. Neither expression introduces
or requires an equality witness as operational input.

The fixture checks the section carrier, its object evaluation and the
transformation component's carrier separately. It then declares both
comparison terms with the same explicit functor carrier. Those declarations
are accepted; the final conversion assertion is rejected. The checker emits
unification diagnostics there, so the record preserves the actual output
and printed normal forms rather than claiming a new logical contradiction.

## Matched pre-goal result

The same fixture, replacing only C = Cat_cart by the pre-goal Cat_cat,
is checked against the exact original kernel at
`f8af1fca472657ff1598c639eb29c0566e7b2ec0`. It accepts the preceding typed
terms and rejects the final comparison too, with the same two runtime
shapes. This boundary therefore predates the strict-functor/duality migration.
It is not evidence that the new coefficient universe creates the mismatch.

This result is narrower than saying that terminal Homd is impossible.
The pre-goal Homd had its own stable projection owners, so its local terminal
normalization did not have to expand this constituent identity-section
presentation. The migrated defined composites expose it. A whole semantic
comparison and a chosen runtime normal form remain different commitments.

## Consequence for the next repair

Do not try to repair this by erasing arbitrary terminal variables, declaring
every map into the terminal category to be a chosen constant, or repeating
the rejected global terminal postcomposition rule. Its actual inverse
cancellation regression remains independently established.

The next native-owner experiment must retain both component orders and the
constant-section reading explicitly. If stable identity-Homd projections
are restored, their comparison with the existing mate/covariance body and
their full projection ladder must be checked; a new name for the failing
expression would be insufficient. The result does not authorize replacing
the five required runtime assertions by the already passing whole
proof-time comparisons. R01–R03 remain open.

No runtime or unification rule, original diagnostic, exclusion or selected
source changes in this review. The four selected receipts from `deedfa1f`
remain reusable at their exact unchanged inputs. Replay the fixture only
when revisiting this terminal/constant-section boundary, using the retained
guarded profiles and source pins; its expected result is rejection of the
last conversion assertion, not a passing library target.
