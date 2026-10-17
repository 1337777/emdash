# Presheaf and higher-sieve mapping profiles

Date: 2026-10-17
Predecessor: `7d17441c`
Status: presheaf/sieve owners and original focused controls qualified in staging; broader import stops at the original fibrewise-Sigma coefficient
Plan: [strict-functor/duality foundations](../../../docs/EMDASH_STRICT_FUNCTOR_DUALITY_FOUNDATIONS_PLAN.md)
Evidence: [verification](production_presheaf_profile_verification.json)

The original Psh_cat facade keeps its ordinary lax family maps and its
proof-time comparison with Catd_cat(T(K)). Yoneda uses hom_con_int_view,
the actual ordinary inclusion of the canonical Cartesian Hom. Its object,
arrow and whole-Hom computations still come from that Hom owner.

The varying arrow-total family uses Sigma_coeff_func(T(K)) after the canonical
Cartesian hom_con_int. This supplies its actual Cat_cart coefficient without
promoting all raw Psh maps to strict parameter maps. The object total remains
Sigma over T(K) of Hom_K(-,U).

The facade exposed an inherited computation issue: the three original
composition clauses repeated the source/target categories on both the outer
fapp operation and the visible composite. Removing only the redundant outer
annotations lets the typed composite supply those parameters when the caller
uses Psh_cat and its body uses Catd_cat. The equations, factors and arguments
are unchanged. Subject reduction and the complete inherited core/curry
regression pass; the actual facade controls check the intended new use.

The migrated core's Catd_catd_con is already the Cartesian varying-base
classifier. Its higher-sieve fibre is consequently

```
Functor_cart_cat(Into_restr_cat(K,U),Cat_cart).
```

Its objects are the original category-valued families. Psh_cat(Slice(K,U))
has those same objects and ordinary lax maps. The old category-equality
assertion is therefore replaced by the full Cartesian category comparison,
an actual whole ordinary inclusion, and a negative against identifying the
two mapping categories. The fixed-fibre inclusion is the existing
Functor_cart_include with a Catd target annotation so the checker can use
the established direct Psh facade comparison. No category equality or
operational equality argument is added.

The slice still uses the dimension-one transpose T of the restriction total.
Its arrow data has base p:dom(q)→dom(r) and a directed filler r∘p⇒q. The
new controls recover both inputs and reject replacing the filler. They do
not impose OneCat(K) or identify arbitrary higher cells. No T/O replacement
was made simply because the earlier total-arrow constructions used O.

Original PSSS-01/PSSS-02 diagnostics are replayed with the actual coefficient
and inclusion views. The presheaf/profile reviewer passes 26 positive/five
negative assertions. The inherited core/curry reviewer passes 274 positive/
70 negative assertions. The ordinary-sieve owner requires one corresponding
arrow-family coefficient correction. Its original PSSS-03a diagnostics,
together with the presheaf controls, pass 35 positive/six negative assertions.
The broader assembly import now passes sieves and sites and stops at
emdash3_2_fibrewise_sigma.lp:53-54, whose original family beta still names
Cat_cat where its family has coefficient Cat_cart. This is a failed
integration gate, not a failure of the focused presheaf/sieve controls.

Warning comparison records 27 added and 23 removed bodies (1991→1995): 22
existing overlap families are reshaped by the inferred-annotation change,
five concern product-swap cancellation and Cartesian/ordinary product-map
views, and one previous constant-coefficient Hom-family overlap disappears.
This classification and typed controls are not a global confluence proof.
Owning-file audits report zero unreviewed clauses in the core, presheaves
and sieves. All three positive check receipts rehash to the current emitted
source closures.

Replay the generator, presheaf_profile_controls.lp, sieve_profile_controls.lp
and the affected inherited core controls. The source and focused presheaf
checks use bounded 240s/2GiB/o=20 profiles (about 28s/24s); the sieve controls
use 300s/4GiB/o=20 (about 31s). Broader imports keep their measured separate
limits (the broader import reached its next type error in about 63s at
600s/4GiB/o=5). Next migrate the original fibrewise-Sigma owner and its
consumers, retaining their actual transport data. Presheaf maps remain lax.
Remaining direct-cover/library
migration, strict-wrapper retirement, promotion and final qualification stay
required.
