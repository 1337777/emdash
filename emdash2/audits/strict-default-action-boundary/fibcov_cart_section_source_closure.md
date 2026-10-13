# Defined section from canonical strict FibCov

Status: `combined_controls.lp` passes the derived section's native type,
y/v/f projections, and whole/capped R-action controls. Its receipt is
`20261013T184248Z-85bd0860ab6b4e80b8b9b0c9513f624e`; the run completed in
13.757 seconds. All 970 critical-pair warning blocks match the checked
inclusion donor exactly; 137 replaceable-pattern diagnostics are unchanged
in count. The strict LHS audit reports zero unreviewed clauses. The two isolated targets remain
unchecked; no outcome is copied to them. The donor is
`fibcov_cart/inclusion_controls.lp`, SHA-256
`ad80cdac932516476b3f2b895dc4c43acde5637b245c00f596cfe8fd3d7026fa`,
checked by receipt `20261013T183711Z-956a447a115f46d79de5b524be7b69e4`.
The recipe pins the donor and receipt directly.

The sole added owner is a definition:

```text
fibcov_cart_section(E,x,u) : Obj(Homd_section_cat(E,x))
  := Prof_cov_con_lift_transf K I_x E (fibcov_cart_transf E x u)
```

The input is the canonical structural strict-Y FibCov value; the section is
an actual application of the existing whole represented lift. There is no
new section primitive, rule, unifier, supplied comparison, or coend body.
No claim derives the FibCov strict contract from object values alone.

`section_controls.lp` checks the native section type and direction,
its actual y-component as the companion of `fib_cov_tapp0_func`, its whole
v-value as the existing `homd_id_` ordinary Hom leaf, and evaluation at f.
`action_controls.lp` checks the actual whole/capped y-arrow action against
the inherited lift R, its stable postcomposition value, and identity-arrow
normality. `combined_controls.lp` contains both sets.

The donor declarations and old `homd_id_src_sec` remain unchanged.
Equality with an independent old primitive root is not a migration
prerequisite. If these observations pass, replacing an old public name with
the actual definition would be a separate source migration with its own
whole x/u compatibility checks. Component agreement alone is not a whole
equality theorem.

The selected lift is still a structural interface in provisional Q with
globally Cartesian Prof mapping categories. These consumers do not qualify
extracted native laxity, triangle/composition coherence, or integration of
the separate raw-preserving coefficient profile.

`fibcov_cart_section_migration.py --check-authoring --check-evidence`
verifies authoring and recorded evidence hashes without invoking Lambdapi.
Root owns serial checking. The pass does not identify the derived section
with an independent old primitive or migrate the existing Homd root.
