# Zero-arrow input and native inverse consumer migration

Date: 2026-10-20–21 (UTC)
Status: staged input, chain-map and inverse consumers qualified; production remains open
Predecessor: `3d43c5a7a683fc93592c660fda44ea899b9d3fc6`.

This continues the existing-consumer migration in the
[living plan](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md).
The [verification record](production_zero_arrow_input_verification.json) retains
source hashes, development failures, the final receipt and its exact scope.
The source adapter is [production_zero_arrow_input_migration.py](production_zero_arrow_input_migration.py).
Its emitted LP, at the original module positions, is the formal implementation.
All work remains staged; no production promotion is claimed.

## Retain the actual zero-composite input

Write B = Functor_oplax_cat(WalkingArrow_cat,C), and encode an ordinary strict
walking-arrow functor d by OddDual_func(d). The existing public input names
now return the Homs actually consumed by the migrated adjunctions:

```
terminal_zero_composite_transf : Hom_B(J(X), encode(Arr(d)))
initial_zero_composite_transf  : Hom_B(encode(Arr(d)), I(X)).
```

The original OneCat(C), preadditive structure, terminal/initial data,
nonidentity b and d, and equation d∘b=0 or b∘d=0 remain inputs. Initial data
use the already selected TotalOp(C). The same native square and its original
path_to_hom filler are used before inclusion in B.

The Cartesian body already present inside one_cat_arrow_diagram_func is
factored into the defined one_cat_arrow_cart_diagram_func. The old ordinary
operation includes that body in Functor_cat; the input adapter instead uses
the existing Functor_cart_oplax_include. Decoding the actual J(X)/I(X) object
before inclusion preserves its endpoint presentation. It supplies no equality
transport. Factoring and expanding this definition recovers the predecessor's
entire ordinary-arrow module byte for byte.

An initially tested readmission of the already strict square typechecked but
obscured its component computation. It is not selected. The final route uses
the existing Cartesian action directly; no admission-retraction rewrite,
new strictness premise or arbitrary-transfor strictness is installed.

## Whole observations and retained Homdc frame

The existing zero-cone chain-pair and annihilator observations now project
the whole fixed oplax evaluation functors. Their lower compatibility is the
ordinary-target naturality equation of the whole evaluation transformation,
with its orientation adjusted to preserve the original equation. The upper
compatibility still observes the original universal transformation. The
original OneCat guard is retained throughout.

The chain-map reviewer keeps its original Homdc-frame filler. Its represented
Cartesian family is passed through the actual whole inclusion into Catd.
A [transparent generic reviewer definition](production_zero_arrow_frame_reviewer.lpfragment)
then introduces the same represented map before specializing the coefficient.
All three actual arrows and the original filler remain arguments. A variant
using the native constructor's expanded filler type also passed, but is not
selected: the original Homdc input is retained instead.

This does not repair bare specialized Sigma inference or identify the stable
Homdc action heads with expanded compositions at runtime. Those presentation
limits remain R06. No nested-projection rewrite or added unifier is used.

## Native inverse proofs

The original zero-cone map inverse retains m and its supplied endpoint and
diagram equivalences U,V. Its left/right inverses and both laws retain the
original constructions. The diagram coefficient and its OneCat evidence are
changed together to the existing oplax profile.

The original reconstruction proof's two nested Sigma eliminations did not
infer their binders after specialization. The defined
represented_comma_map_ind checks those same eliminations with a generic
coefficient. Its motive and constructor branch are the ordinary existing
Sigma-induction arguments, not new assumptions. The consuming proof retains
its original branch, using the existing typed zero_cone_native_map for its
three nested constructor occurrences. This is a local elaboration repair,
not a new induction principle or inverse law.

The [represented-map fragment](production_represented_comma_map.lpfragment)
contains this derived eliminator beside its constructor. Removing the new
definition recovers the predecessor's zero-cone module byte for byte. No old
rule or unifier changes. Both shared-owner LHS audits report zero unreviewed
candidates; the three pre-existing ordinary-arrow rules remain unchanged.

## Qualification and resource boundary

The [focused driver](production_zero_arrow_input_regression.lpfragment)
contains 30 positive and five negative original assertions across five
reviewers. They cover ordinary square components and higher action, zero
input components, kernel/cokernel reconstruction and annihilation, three
chain-map projections, and selected inverse components and both laws.
Wrong arrows, missing zero-composite evidence and the wrong truncation
profile remain negative controls.

The final focused inverse development check passes in 57.783s/213104KiB
with subject reduction and warnings, under 180s/2GiB/o=20 using the isolated
checker. Its exact measurement is recorded by the receipt and verification
record; the aggregate below is the final emitted-source qualification.

One preceding 90s run timed out in existing imports, before checking the
changed inverse proof. Its unchanged core import alone took 49.30s. The
measured retry retained 2GiB and increased only the deadline to 180s. Neither
the timeout nor the later pass establishes a normalization-cost explanation.
Installed checker binaries and normal resource defaults remain unchanged.

The final emitted-source integration passes **3,429 assertions** (3,008 positive,
421 negative) in **518.425s / 1,743,264KiB** (about 1.66GiB).
Receipt: `20261021T000708Z-0e253f32641b4aaaa73501f6ec497bad`.
It checks 193 registered library/core files and all 78 staged registered
reviewers, with SR and warnings, source-only loading, serial execution, file
limits and no swap, using the isolated checker under 600s/4GiB/o=20.
The longer profile matches the already reviewed all-import boundary and
accommodates this combined original-consumer scope; defaults are unchanged.

The first integration log also reached the final source-completion marker,
but its command wrapper was interrupted across the tool/turn handoff before
writing a receipt. Its log and hash are retained as supplementary evidence,
not a fabricated successful receipt. The final run used a transient independent
receipt writer with a 630-second outer deadline; the compiler itself retained
the same 600-second resource guard. The final receipt records exit code zero.

The warning inventory contains 2,489 critical-pair bodies. None belongs to a
changed owner. Two newly co-loaded bodies concern the existing NType
composition reading against existing Kleisli/co-Kleisli composition rules.
They are retained in R07; no rule is added to hide them, and a global
confluence claim is not inferred from the passing consumers.

The registry still has 598 library/core files and 518 reviewers not yet
staged. The full registered central diagnostic remains outside this passing
receipt because its five positive terminal obligations are unchanged.

The [integration driver](production_zero_arrow_integration.lpfragment) starts
with the original all-import central selection and then the staged registered
reviewers. It excludes exactly the same five original terminal Homd positives;
the original full diagnostic is unchanged. This is an affected staged
integration boundary, not repository-wide qualification or a replacement for
those five obligations.

The core and full central diagnostic hashes remain respectively
`7ed6b2d06bded69965fc771d447dfb8b9faa26d114aa060b1e5389243ffe7789`
and `f200871da5385aa10ab5af9b97e407f61a8c778a4efd6dd7aa182bfb4ac8a4ce`.
Production promotion, supported checker adoption, remaining consumers and
the terminal Homd computations remain open. Continue with the original
introduced-terminal-input comparison consumer; preserve its actual diagrams,
map and inverse data, and the whole-owner/projection-ladder SOP.
