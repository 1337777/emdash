/* Cokernel presentation over the original selected cokernels. Its witness
   supplies coherent structure; no automatic introduction from old data. */
require open emdash.emdash3_2_kernel_cokernel_adjunctions;
require open emdash.emdash3_2_one_cat_action_paths;
require open emdash.emdash3_2_strict_transfor_component_paths;
require open emdash.emdash3_2_one_cat_transfor_profiles;
require open emdash.emdash3_2_cokernel_maps;

symbol cokernel_presentation_selected [C : Cat] [S : τ (@PreadditiveCategory C)]
  (W : τ (@HasComputationalCokernels C S)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@ComputationalCokernel C S
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
≔ W (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator));

constant symbol CokernelPresentation [C : Cat] (S : τ (@PreadditiveCategory C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  (W : τ (@HasComputationalCokernels C S)) : Grpd;

injective symbol cokernel_presentation_func [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  : τ (Functor (Functor_oplax_cat WalkingArrow_cat C) C);

injective symbol cokernel_presentation_adjunction [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  : τ (@Adjunction (Functor_oplax_cat WalkingArrow_cat C) C
      (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T));

// One-way adapter from the original selected presentation. The new whole
// adjunction interface itself has no selected W/V prerequisite.
symbol cokernel_presentation_structure [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)]
  [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  : τ (@CokernelAdjunctionStructure C S t T)
≔ @cokernel_adjunction_intro C S t T
    (@cokernel_presentation_func C S t T W P)
    (@cokernel_presentation_adjunction C S t T W P);

// Proof-time object observation retains Q[d] for adjunction cuts.
unif_rule
  @fapp0 _ _ (@cokernel_presentation_func $C $S _ _ $W _) $d
  ≡ @sigma_Fst _ _ $chosen
  ↪ [ $chosen ≡ (@cokernel_presentation_selected $C $S $W $d) ];

// The actual whole projection is codomain applied to the adjunction unit.
symbol cokernel_presentation_projection [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  : τ (@Transf (Functor_oplax_cat WalkingArrow_cat C) C
      (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P))
≔ @cokernel_adjunction_projection C S t T
    (@cokernel_presentation_structure C S t T W P);

unif_rule
  @tapp0_fapp0 _ _ _ _ $i
    (@tapp0_fapp0 _ _ _ _ $d
      (@unit_adj_transf _ _ _ _
        (@cokernel_presentation_adjunction $C $S _ _ $W _)))
  ≡ @sigma_Fst _ _ (@sigma_Snd _ _ $chosen)
  ↪ [ $i ≡ walking_arrow_tgt;
      $chosen ≡ (@cokernel_presentation_selected $C $S $W $d) ];

symbol cokernel_presentation_projection_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d))
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C _ _ d (@cokernel_presentation_projection C S t T W P))
      (@computational_cokernel_morphism C S
        (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
        (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
        (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
        (@cokernel_presentation_selected C S W d)))
≔ @eq_refl (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d))
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C _ _ d (@cokernel_presentation_projection C S t T W P));

/* Map usability preserves whole Q action and reuses the original selected colift. */


symbol cokernel_presentation_selected_object [C : Cat] [S : τ (@PreadditiveCategory C)]
  (W : τ (@HasComputationalCokernels C S)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) : τ (Obj C)
≔ @computational_cokernel_object C S
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d)
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d)
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@cokernel_presentation_selected C S W d);

symbol cokernel_presentation_object_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  : τ (@= (Obj C) (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d)
      (@cokernel_presentation_selected_object C S W d))
≔ @eq_refl (Obj C) (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d);

// Actual strict naturality of eta supplies the existing postcomposition
// factor, so no separate square/reconstruction input is added.
symbol profiled_cokernel_presentation_map_semantic [C : Cat] [S : τ (@PreadditiveCategory C)]

  (W : τ (@HasComputationalCokernels C S))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (PE : τ (@IsStrictTransfor (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 d0 eta))
  : τ (Hom C (@cokernel_presentation_selected_object C S W d0)
      (@cokernel_presentation_selected_object C S W d1))
≔ @computational_cokernel_map C S
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0)
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@cokernel_presentation_selected C S W d0) (@cokernel_presentation_selected C S W d1)
    (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta)
    (@hom_postcomp_factor_intro C
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@comp_fapp0 C _ _ _
        (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta)
        (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0 d1 eta)
      (@eq_sym (Obj (Hom_cat C (@fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0 walking_arrow_src) (@fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 walking_arrow_tgt))) _ _ (@strict_component_naturality_path (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 d0 eta PE walking_arrow_tgt walking_arrow_src walking_arrow_generator)));

/* The earlier generic map-unifier depended on unqualified strict naturality.
// The selected colift unfolds to two Sigma projections of its contractible
// factor space. Capture their inferred types, then check the exact semantic
// result as a side condition; do not pattern-match an alias or raw W application.
unif_rule
  @fapp1_fapp0 _ _ (@cokernel_presentation_func $C $S _ _ $W _) $d0 $d1 $eta
  ≡ @sigma_Fst $A $B (@sigma_Fst $D $E $factor)
  ↪ [ (@sigma_Fst $A $B (@sigma_Fst $D $E $factor))
        ≡ (@cokernel_presentation_map_semantic $C $S $W $d0 $d1 $eta) ];

*/

/* Audit: the existing generic same-arrow congruence is being tested
   in place of this selected metadata instance.
// Proof-time metadata agreement at the selected target. Match linearly
// before checking the actual arrows; this changes no composition law.
unif_rule
  @comp_fapp0 $C0 $X $Y
    (@fapp0 _ _ (@cokernel_presentation_func $C $S $t $T $W $P) $d) $g $f
  ≡ @comp_fapp0 $D $X1 $Y1 $Z1 $g1 $f1
  ↪ [ $C0 ≡ $C; $D ≡ $C; $X1 ≡ $X; $Y1 ≡ $Y;
      $Z1 ≡ (@fapp0 (Functor_oplax_cat WalkingArrow_cat $C) $C
        (@cokernel_presentation_func $C $S $t $T $W $P) $d);
      $g1 ≡ $g; $f1 ≡ $f ];
*/

symbol cokernel_presentation_evaluation_path [C : Cat]
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta))
≔ @eq_refl (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta);

symbol profiled_cokernel_presentation_projection_naturality_path
  [C : Cat] [S : τ (@PreadditiveCategory C)]
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (PI : τ (@IsStrictTransfor (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) (@cokernel_presentation_projection C S t T W P)))
  : τ (@= (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d1))
      (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) d0 (@cokernel_presentation_projection C S t T W P)))
      (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@cokernel_presentation_selected_object C S W d1) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) d1 (@cokernel_presentation_projection C S t T W P)) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta)))
≔ (@strict_component_naturality_path (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) (@cokernel_presentation_projection C S t T W P) PI d0 d1 eta);

symbol profiled_cokernel_presentation_map_path [C : Cat] [S : τ (@PreadditiveCategory C)]

  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (PE : τ (@IsStrictTransfor (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 d0 eta))
  (PI : τ (@IsStrictTransfor (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) (@cokernel_presentation_projection C S t T W P)))
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0)
      (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@profiled_cokernel_presentation_map_semantic C S W d0 d1 eta PE))
≔ @eq_sym _ _ _
    (@computational_cokernel_map_unique_path C S
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0)
    (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@cokernel_presentation_selected C S W d0) (@cokernel_presentation_selected C S W d1)
    (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta)
    (@hom_postcomp_factor_intro C
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0)
      (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@comp_fapp0 C _ _ _
        (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta)
        (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0 d1 eta)
      (@eq_sym (Obj (Hom_cat C (@fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d0 walking_arrow_src) (@fapp0 (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 walking_arrow_tgt))) _ _ (@strict_component_naturality_path (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 d0 eta PE walking_arrow_tgt walking_arrow_src walking_arrow_generator)))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@eq_trans _ _ _ _ (@eq_sym _ _ _ (@eq_ap (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d0)) (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d1)) (λ h : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d0)), (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta) h)) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) d0 (@cokernel_presentation_projection C S t T W P)) (@computational_cokernel_morphism C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@cokernel_presentation_selected C S W d0)) (@cokernel_presentation_projection_path C S t T W P d0)))
        (@eq_trans _ _ _ _ (@profiled_cokernel_presentation_projection_naturality_path C S t T W P d0 d1 eta PI)
          (@eq_trans _ _ _ _ (@eq_ap (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@cokernel_presentation_selected_object C S W d1)) (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d1)) (λ h : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@cokernel_presentation_selected_object C S W d1)), (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@cokernel_presentation_selected_object C S W d1) h (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta))) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) d1 (@cokernel_presentation_projection C S t T W P)) (@computational_cokernel_morphism C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@cokernel_presentation_selected C S W d1)) (@cokernel_presentation_projection_path C S t T W P d1))
            (@eq_ap (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)) (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@cokernel_presentation_selected_object C S W d1)) (λ h : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1)), (@comp_fapp0 C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@cokernel_presentation_selected_object C S W d1) (@computational_cokernel_morphism C S (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) d1) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1) (@tapp0_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d1 (@diagram_oplax_evaluation_transf WalkingArrow_cat C walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@cokernel_presentation_selected C S W d1)) h)) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta) (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) d0 d1 eta) (@cokernel_presentation_evaluation_path C d0 d1 eta))))));

// Ordinary-target wrappers derive both actual profiles; the whole K/Q is unchanged.
symbol cokernel_presentation_map_semantic [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  (W : τ (@HasComputationalCokernels C S))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  : τ (Hom C (@cokernel_presentation_selected_object C S W d0)
      (@cokernel_presentation_selected_object C S W d1))
≔ @profiled_cokernel_presentation_map_semantic C S W d0 d1 eta (@one_cat_transfor_is_strict (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@one_cat_odd_dual C C1) d1 d0 eta);

symbol cokernel_presentation_map_path [C : Cat] [S : τ (@PreadditiveCategory C)]
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0)
      (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@cokernel_presentation_map_semantic C S C1 W d0 d1 eta))
≔ @profiled_cokernel_presentation_map_path C S t T W P d0 d1 eta (@one_cat_transfor_is_strict (OddDual_cat WalkingArrow_cat) (OddDual_cat C) (@one_cat_odd_dual C C1) d1 d0 eta) (@one_cat_transfor_is_strict (Functor_oplax_cat WalkingArrow_cat C) C C1 (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) (@cokernel_presentation_projection C S t T W P));
