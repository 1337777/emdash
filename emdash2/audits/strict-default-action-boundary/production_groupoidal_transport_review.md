# General diagram evaluation in groupoidal transport

Date: 2026-10-16
Predecessor: `d5802c78`
Status: qualified staged owner and original structured-J reviewer
Evidence: [verification](production_groupoidal_transport_verification.json)

The old `groupoidal_fibre_transport_equiv` uses a general classified functor
`D : StrictFunctor(C,Cat_cat)`. Its conclusion only needs the categories D[x],
D[y] and the actual transport D[f]. The migrated `Fibre_cat` facade instead
expects an admitted Cat_cart-valued family. Changing D to land in Cat_cart
would unnecessarily restrict this theorem.

The implementation therefore expands the two old fibre expressions to
`fapp0 C Cat_cat (strict_functor D)`. The selected transport and inverse, all
parameters, and the complete proof body are unchanged. The input remains a
general Cat-valued diagram; retiring its legacy StrictFunctor wrapper remains
part of the later consumer migration.

The original structured-J reviewer needs three related notation/view updates:

- Its raw diagram evaluations use the same explicit fapp0 expressions.
- The canonical covariance map now has a strict-transfor carrier. Its comparison
  with the ordinary path-induction section uses the existing `strict_transfor`
  inclusion, matching the already qualified kernel fold.
- Its separate admitted-family identity test uses Cat_cart for D's actual
  arrow action, and the common `Functor` object classifier for the result.
  This avoids trying to identify the two coefficient universes through the
  universe-Hom facade. Their functor objects agree; their higher maps do not.

No new symbol, runtime rule, unification rule, strictness condition or supplied
comparison is added. All 19 positive and 2 negative original assertions remain
with their original polarity. The reviewer passes in 25.059 seconds with
warnings and subject reduction under 90s/2GiB/serial/no-swap safeguards.

The matched broader-import warning streams have exactly the same 2337 pair
bodies. The smaller reviewer imports fewer modules, so its warning count is
not used to claim a reduction. The broader original import now reaches
`diagram_evaluation_func`, whose unrestricted exchange type needs a genuine
transformation-profile correction. The [separate review](production_diagram_evaluation_review.md)
records that next boundary. The whole foundation goal is not complete.
