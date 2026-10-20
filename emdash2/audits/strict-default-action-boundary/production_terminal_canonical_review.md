# Canonical terminal Homd contraction review

Date: 2026-10-20
Predecessor: `7bdeb7f8213bd7361b882339f15c947230d582fd`
Status: rejected implementation; selected mathematical source unchanged

The [exact experiment record](production_terminal_canonical_review_verification.json)
retains the owner-position patches, diagnostics, source hashes and guarded
checker receipts. This is a non-library audit. Replay only when revisiting
R01–R03 or changing the relevant terminal/constant-section owners.

## Narrower hypothesis

The earlier constant-transport rule matched an arbitrary neutral unit value
u. This attempt instead matches the literal canonical point:

```text
Conjoint(1,I,Const(I,1,*)) → Const(1,P(I),terminal-presheaf).
```

It keeps `Conjoint(1,1,id₁)`, the actual Q unit, distinct. The two composition
orientations retain the intermediate functor and its value G[*] where needed.
The original terminal identity y-component, both Q units, both tested
conjoint-composition cases and a neutral-u noncollapse control pass in the
bounded candidate. This improves on the previous attempt, but does not
qualify the whole projection ladder or settle the other four obligations.

## Where qualification fails

Contracting the whole ordinary `hom_con_int` into a constant terminal Hom
requires its existing whole and capped postcomposition projections to agree.
Those first projections can be joined by corresponding owner rules, but the
next component fails. The isolated diagnostic separates four typing checks
from the conversion: all four types check in both snapshots; the conversion
passes in selected source and fails in the candidate.

The candidate's left normal form uses the existing constant-family section
view of an identity transformation. It is a constant functor whose value
still contains ordinary application of that identity section. The attempted
right normal form is `id_func Terminal_cat`. The recorded normal forms
identify this interface crossing; the failure is not a malformed test and
does not establish a new semantic restriction on E or FF.

Making terminal postcomposition the identity on its incoming neutral arrow
does not repair the implementation. It breaks the existing computation on
actual inverse data:

```text
postcomp(i⁻¹)(i) → id.
```

The unchanged snapshot passes that control. The candidate returns the retained
forward map instead of cancelling it and fails. The warning comparison also
locates overlaps with unit and mapped-arrow cuts. These are grounds to reject
the proposed rule family, not grounds to erase neutral unit terms globally.

The separate raw terminal right-unit assertion fails in both snapshots. It
is therefore **not** counted as a new regression. Earlier investigation of
the warning alone was insufficient to distinguish that inherited boundary
from the independently confirmed inverse regression.

## Disposition and next owner review

No candidate rule is selected. The emitter completed successfully and restored
the selected core hash. All 131 combined-regression, 58 affected-consumer and
90 library receipt inputs rehash exactly; their prior green evidence carries.
No production file, original assertion or terminal exclusion is changed.

The pre-goal kernel owned terminal normalization directly at the stable
`homd_src_func` and `homd_tgt_func` projections. The current Q presentation
exposes constituent mate/conjoint and ordinary Hom computations. Thus copying
the old endpoint formula into a constituent's global normalizer has a larger
effect than copying a local Homd projection rule. The next review must inspect
the constant-section identity observation and the appropriate native owner
before another whole terminal contraction. Restoring a stable Homd owner is
an alternative only with its actual semantic comparison and full projections;
merely naming the failing expression would not qualify it.

All five runtime obligations remain required. Their existing whole proof-time
comparisons remain available, without being counted as the old reductions.
This review neither exhausts the alternatives nor proves impossibility of a
local terminal repair. It adds no general Q/coend theory or new prerequisite.

The later [matched identity-section review](production_terminal_identity_section_review.md)
isolates the same component boundary without any candidate contraction and
finds it in the exact pre-goal kernel too. That qualifies its origin; it does
not make this rejected implementation or the five runtime obligations pass.
