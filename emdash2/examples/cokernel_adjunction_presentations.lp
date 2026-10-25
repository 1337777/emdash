/* Declaration/usability consumer. Runtime retains formal observations;
   explicit equality witnesses compare with the original selected operations. */
require open emdash.emdash3_2_cokernel_adjunction_presentations;

// Proof-time object agreement, not a runtime change of owner.
assert [C : Cat] (S : τ (@PreadditiveCategory C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) ⊢
  @eq_refl (Obj C) (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d)
  : τ (@= (Obj C) (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d) (@cokernel_presentation_selected_object C S W d));

assertnot [C : Cat] (S : τ (@PreadditiveCategory C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) ⊢
  @fapp0 _ _ (@cokernel_presentation_func C S t T W P) d ≡ @cokernel_presentation_selected_object C S W d;

// Nonidentity arrow comparison uses the actual chosen lift/colift.
assert [C : Cat] (S : τ (@PreadditiveCategory C)) (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W))
  (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)) ⊢
  @cokernel_presentation_map_path C S C1 t T W P d0 d1 eta
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@cokernel_presentation_map_semantic C S C1 W d0 d1 eta));

// The comparison is a derived path, not the retired generic map-unifier.
assertnot [C : Cat] (S : τ (@PreadditiveCategory C)) (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W))
  (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)) ⊢
  @eq_refl (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))
    (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@cokernel_presentation_map_semantic C S C1 W d0 d1 eta));

// Normal identity is generic; composition requires the actual capability.
assert [C : Cat] (S : τ (@PreadditiveCategory C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))) ⊢
  @fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d d (@id (Functor_oplax_cat WalkingArrow_cat C) d)
  ≡ @id C (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d);

assert [C : Cat] (S : τ (@PreadditiveCategory C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d0 d1 d2 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)) (theta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d1 d2)) ⊢
  @comp_fapp0 C _ _ _
    (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d1 d2 theta) (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)
  ≡ @fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d2
      (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) d0 d1 d2 theta eta);

// The same raw whole functor has the qualified ordinary composition path.
assert [C : Cat] (S : τ (@PreadditiveCategory C)) (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d0 d1 d2 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1)) (theta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d1 d2)) ⊢
  @eq_sym _ _ _ (@one_cat_composition_path (Functor_oplax_cat WalkingArrow_cat C) C C1 (@cokernel_presentation_func C S t T W P) d0 d1 d2 theta eta)
  : τ (@= (Hom C (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0) (@fapp0 _ _ (@cokernel_presentation_func C S t T W P) d2)) (@comp_fapp0 C _ _ _
    (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d1 d2 theta) (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)) (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d2
      (@comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) d0 d1 d2 theta eta)));

// An unrelated arrow of the same type is not accepted as the selected map.
assertnot [C : Cat] (S : τ (@PreadditiveCategory C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject (TotalOp_cat C) t)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W)) (d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (other : τ (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))) ⊢
  @eq_refl (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))
    (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta)
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0) (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 _ _ (@cokernel_presentation_func C S t T W P) d0 d1 eta) other);

// Further directed Hom action remains available on the whole functor.
type λ C : Cat, λ S : τ (@PreadditiveCategory C), λ t : τ (Obj C),
  λ T : τ (@TerminalObject (TotalOp_cat C) t), λ W : τ (@HasComputationalCokernels C S),
  λ P : τ (@CokernelPresentation C S t T W),
  λ d0 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)), λ d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)),
  λ eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1), λ theta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1),
  @fapp1_func _ _ (@fapp1_func _ _ (@cokernel_presentation_func C S t T W P) d0 d1) eta theta;

/* Actual zero-embedding specialization of the generic Došen rectangle. */


assert (C : Cat) (t : τ (Obj C)) (T : τ (@TerminalObject (TotalOp_cat C) t))
  (S : τ (@PreadditiveCategory C)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W))
  (X X' : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (Y : τ (Obj C))
  (g : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) X X'))
  (f : τ (Hom C (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) X') Y)) ⊢
  @comp_fapp0 C _ _ _
    (@tapp1_fapp0
      C C
      (@comp_cat_fapp0 C (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T))
      (@id_func C)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) X')
      Y
      (@counit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_adjunction C S t T W P))
      f)
    (@fapp1_fapp0
      (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P)
      X
      (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) X'))
      (@tapp1_fapp0
        (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
        (@id_func (Functor_oplax_cat WalkingArrow_cat C))
        (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_func C S t T W P))
        X X'
        (@unit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_adjunction C S t T W P))
        g))
  ≡ @comp_fapp0 C _ _ _ f (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) X X' g);

/* Actual zero-embedding specialization of the generic Došen rectangle. */


assert (C : Cat) (t : τ (Obj C)) (T : τ (@TerminalObject (TotalOp_cat C) t))
  (S : τ (@PreadditiveCategory C)) (W : τ (@HasComputationalCokernels C S))
  (P : τ (@CokernelPresentation C S t T W))
  (X : τ (Obj (Functor_oplax_cat WalkingArrow_cat C)))
  (Y' Y : τ (Obj C))
  (f : τ (Hom (Functor_oplax_cat WalkingArrow_cat C) X (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) Y')))
  (g : τ (Hom C Y' Y)) ⊢
  @comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) _ _ _
    (@fapp1_fapp0
      C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T)
      (@fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) Y'))
      Y
      (@tapp1_fapp0
        C C
        (@comp_cat_fapp0 C (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T))
        (@id_func C)
        Y' Y
        (@counit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_adjunction C S t T W P))
        g))
    (@tapp1_fapp0
      (Functor_oplax_cat WalkingArrow_cat C) (Functor_oplax_cat WalkingArrow_cat C)
      (@id_func (Functor_oplax_cat WalkingArrow_cat C))
      (@comp_cat_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_func C S t T W P))
      X
      (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) Y')
      (@unit_adj_transf (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) (@initial_arrow_diagram_func C t T) (@cokernel_presentation_adjunction C S t T W P))
      f)
  ≡ @comp_fapp0 (Functor_oplax_cat WalkingArrow_cat C) _ _ _ (@fapp1_fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T) Y' Y g) f;

// The higher statement uses actual profiles and does not assume OneCat.
assert [C : Cat] [S : τ (@PreadditiveCategory C)]

  [t : τ (Obj C)] [T : τ (@TerminalObject (TotalOp_cat C) t)] [W : τ (@HasComputationalCokernels C S)]
  (P : τ (@CokernelPresentation C S t T W))
  [d0 d1 : τ (Obj (Functor_oplax_cat WalkingArrow_cat C))] (eta : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C) d0 d1))
  (PE : τ (@IsStrictTransfor (OddDual_cat WalkingArrow_cat) (OddDual_cat C) d1 d0 eta))
  (PI : τ (@IsStrictTransfor (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) (@cokernel_presentation_func C S t T W P) (@cokernel_presentation_projection C S t T W P))) ⊢
  @profiled_cokernel_presentation_map_path C S t T W P d0 d1 eta PE PI
  : τ (@= (Hom C (@cokernel_presentation_selected_object C S W d0)
      (@cokernel_presentation_selected_object C S W d1))
      (@fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@cokernel_presentation_func C S t T W P) d0 d1 eta)
      (@profiled_cokernel_presentation_map_semantic C S W d0 d1 eta PE))
;
