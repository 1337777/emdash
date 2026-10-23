# Terminal Homd: runtime contract reassessment

Date: 2026-10-23 UTC
Source checkpoint: `cfb68f91`
Status: checked contract analysis; no mathematical rule or required assertion changed

The five legacy constant-functor normal forms concern three operations:
source-u action (R01), the identity y-component (R02), and relative y-components
for a general section (R03). The current selected core rejects all five
runtime conversions, while their existing whole proof-time comparisons and
the previously qualified higher-action/inverse consumers still pass.

The new checks examine the requested constant expressions directly. They do
not install the rejected terminal normalizers, change the coefficient profile,
add a primitive, or require a stricter family/FF.

## Direct target-action witness (R02)

Let 1 = Terminal_cat, I = Hom_K(x,y), and let H be the current identity Homd
y-functor for the constant terminal family, with source object Terminal_obj.
Let H₀ be exactly the requested constant functor at the terminal presheaf.
Both have the same declared carrier 1 → P(I).

For a chosen i : DefIso₁(*,*), evaluate their first Hom action at i⁻¹, then
its index component at f : I, then apply the resulting functor 1 → 1 to i:

```text
current H:     i⁻¹ ∘ i  ⇝  id₁(*)
constant H₀:   id₁[i]   ⇝  i.
```

The first reduction and the second reduction both pass. The assertion that
the constant version instead reduces to id₁(*) is rejected. The
[complete typed witness](production_terminal_target_action_contract.lpfragment)
uses the actual public identity Homd y-functor and exactly the proposed
Obj_func expression, through the existing index/transformation projections.
No separately supplied comparison or toy replacement action is used.

Consequently, making H and H₀ runtime-convertible while retaining both
projection computations requires the two presently distinct terminal terms
i and id₁(*) to join. A local whole-functor contraction cannot coherently
preserve all these current normal forms unchanged. This is a conflict between
runtime requirements, not a new semantic counterexample to terminality.

## Source-u action (R01)

The [source-action witness](production_terminal_source_action_contract.lpfragment)
compares the current whole source-u functor with the exact Obj_func requested
by the first two legacy assertions. The current projection retains the
existing precomposition owner with both selected maps of i. The constant
functor's action returns the incoming inverse map directly. Their runtime
forms are distinct.

An initial probe also asked the retained precomposition head to cancel that
inverse pair directly. It does not do so in the unchanged core; this is the
already recorded pre/post normalization boundary, not a new regression or a
proved source-side cancellation law. The final witness checks the actual
precomposition normal form and preserves that qualification. The independent
target-action witness above supplies the positive cancellation contrast.

## Relative leaf (R03)

For a general section s, its component F_s = Fibre_func(s,y) is a strict
functor 1 → E[y]. With a neutral v : Obj(1), the
[relative leaf check](production_terminal_relative_leaf_contract.lpfragment)
computes

```text
Hom_E[y](E[f](u), F_s[v]).
```

At v = Terminal_obj it computes

```text
Hom_E[y](E[f](u), piapp0(s,y)).
```

The first expression at arbitrary v does not runtime-convert to the second.
The proposed constant whole relative component would force that additional
normalization. Strict functoriality alone does not install this terminal-source
η rule. This issue is separate from whether s is lax across K; no new
strictness assumption on s is proposed.

## Mathematical meaning and decision boundary

Semantically, a terminal category has unique cells, and these terminal forms
agree. The selected calculus intentionally retains neutral unit terms and
chosen inverse constructors rather than making all such equality judgmental.
Its whole proof-time terminal comparisons therefore remain meaningful.
The witnesses do not prove that every conceivable terminal implementation is
impossible. They identify which existing computations must change if literal
constant-functor normal forms remain mandatory.

Recommended normalization contract: retain the current whole internal Homd
construction and its actual leaf/higher/inverse computations; retain the five
terminal constant expressions as whole proof-time compatibility comparisons.
This recommendation changes the five old runtime acceptance criteria, so it
is presented for an explicit decision. No assertion is removed or reclassified
in the selected source or living requirements by this report.

The alternative is to prioritize literal constant terminal normal forms and
review the conflicting terminal-only normalization/data-retention contracts
explicitly. That is broader than adding a missing local projection rule.
It must not be presented as a harmless primitive-head replacement or as
preserving all currently checked higher computations.

The goal remains active. R01–R03 remain required pending the contract decision;
other registered-consumer migration and final production qualification remain
independent work. No broad regression rerun is needed for this analysis:
all selected mathematical sources and the 494 qualified-file hashes are
unchanged. The [verification](production_terminal_contract_reassessment_verification.json)
records the fresh bounded probes, the unsuccessful exploratory source inverse
query and the exact unchanged-source boundary.
