# Profunctor inverse evaluation in its actual coefficient

Date: 2026-10-17
Predecessor: `6193e164`
Status: original evaluation paths and selected inverse computations qualified; downstream ordinary-arrow and Hom-comparison migration open
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)

The original prof_defiso_evaluation_paths module now evaluates in Cat_cart,
the actual coefficient of Prof(A,B). Both forward and inverse paths, their
selected package I, the evaluation point z, and both raw cancellation laws
are retained. The public functor-valued observations have the same objects;
no Cat_cart=Cat_cat equality or new inverse choice is introduced.

The two existing evaluated-inverse point cuts needed their Cat_cart instances.
Those instances live beside the original Cat_cat cuts in
emdash3_2_defiso_evaluation_points.lp. They use the same original generic
owners and retain the identical package and point on both sides. This is
not a parallel evaluated-inverse API or a runtime decoder from the stable
evaluation owner to a raw component.

The original focused reviewer retains four positive and four negative checks.
Two additional positive checks exercise both point cancellations. Three
negatives reject replacement of the selected inverse package or mixing two
different points in constant fibres. The combined six positive/seven negative
check passes. The complete represented-comma reviewer and its additional
guard also pass with the modified evaluator dependency.

The [verification](production_prof_defiso_coefficient_verification.json)
records exact sources, receipts and diagnostics. Warning bodies are unchanged
in the focused import and comma regression. Subject reduction stays enabled,
and both owning-file LHS audits report zero unreviewed candidates. No core
source changes are required; its previous exact-input evidence is retained.

The default 2GiB owner run failed allocation during its shared import. The
existing reviewed 90s/4GiB/o=20 import profile reaches the actual consumer:
about 32s for the focused check, 46s for the comma regression and 52s for the
broader import. Host headroom was inspected; normal defaults, serial/file
guards and no swap remain unchanged. Resource failure was not used as a
mathematical diagnosis.

The broader import now stops in one_cat_arrow_diagrams.lp at its old
opposite-source identity observation. Its ordinary-target diagram interface
also needs review against the migrated generic oplax exchange. The existing
OneCat(C) premise already provides one_cat_strict_transfor; investigate that
existing admission with Cartesian exchange to preserve the public ordinary
diagram interface. Do not add a source-base truncation or make default
transformations strict. The external Hom-action admission, remaining library
routes, wrapper retirement, public promotion and final qualification remain
required.

Replay after coefficient/evaluation changes: regenerate
production_owner_migration.py and check prof_defiso_coefficient_controls.lp
with the measured import profile. Changed shared evaluator rules additionally
require the recorded comma regression. These are non-library migration
sources; no production promotion is claimed here.
