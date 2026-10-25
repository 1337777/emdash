/* Native ordinary input formation preserves the given arrows. */
require open emdash.emdash3_2_one_cat_zero_arrow_inputs;

// The canonical endpoint view keeps the actual nonidentity side map.
assert [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [X0 X1 Y0 Y1 : τ (Obj C)]
  (u : τ (Hom C X0 Y0)) (v : τ (Hom C X1 Y1))
  (a : τ (Hom C X0 X1)) (b : τ (Hom C Y0 Y1))
  (alpha : τ (Obj (@homdc_square_fibre C X0 X1 Y0 Y1 u v a b))) ⊢
  @tapp0_fapp0 WalkingArrow_cat C _ _ walking_arrow_src
    (@one_cat_square_diagram_transf C C1 X0 X1 Y0 Y1 u v a b alpha) ≡ a;

// The canonical endpoint view keeps the actual nonidentity side map.
assert [C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [X0 X1 Y0 Y1 : τ (Obj C)]
  (u : τ (Hom C X0 Y0)) (v : τ (Hom C X1 Y1))
  (a : τ (Hom C X0 X1)) (b : τ (Hom C Y0 Y1))
  (alpha : τ (Obj (@homdc_square_fibre C X0 X1 Y0 Y1 u v a b))) ⊢
  @tapp0_fapp0 WalkingArrow_cat C _ _ walking_arrow_tgt
    (@one_cat_square_diagram_transf C C1 X0 X1 Y0 Y1 u v a b alpha) ≡ b;

// The kernel-side input retains its incoming arrow and zero tip.
assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B))) ⊢
  @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@terminal_zero_composite_transf C S C1 t T X A B b d zero) ≡ b;

// The kernel-side input retains its incoming arrow and zero tip.
assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B))) ⊢
  @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@terminal_zero_composite_transf C S C1 t T X A B b d zero) ≡ (@preadditive_hom_zero C S t B);

// The cokernel-side input retains its zero tip and outgoing arrow.
assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  [A B X : τ (Obj C)] (d : τ (Hom C A B)) (b : τ (Hom C B X))
  (zero : τ (@= (Hom C A X) (@comp_fapp0 C A B X b d)
    (@preadditive_hom_zero C S A X))) ⊢
  @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_src) _ _ (@initial_zero_composite_transf C S C1 t T A B X d b zero) ≡ (@preadditive_hom_zero C S A t);

// The cokernel-side input retains its zero tip and outgoing arrow.
assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  [A B X : τ (Obj C)] (d : τ (Hom C A B)) (b : τ (Hom C B X))
  (zero : τ (@= (Hom C A X) (@comp_fapp0 C A B X b d)
    (@preadditive_hom_zero C S A X))) ⊢
  @fapp1_fapp0 (Functor_oplax_cat WalkingArrow_cat C) C (@diagram_oplax_evaluation_at_func WalkingArrow_cat C walking_arrow_tgt) _ _ (@initial_zero_composite_transf C S C1 t T A B X d b zero) ≡ b;

// The native cone forms from raw data, with no universal structure in scope.
assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B))) ⊢
  @fapp0 (@ZeroArrowCone_cat C t T) C (@zero_arrow_cone_first_func C t T)
    (@zero_composite_native_cone C S C1 t T X A B b d zero) ≡ X;

assert [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B))
  (zero : τ (@= (Hom C X B) (@comp_fapp0 C X A B d b)
    (@preadditive_hom_zero C S X B))) ⊢
  @fapp0 (@ZeroArrowCone_cat C t T) (Functor_oplax_cat WalkingArrow_cat C)
    (@zero_arrow_cone_diagram_func C t T)
    (@zero_composite_native_cone C S C1 t T X A B b d zero)
  ≡ @OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d);

// An arbitrary composable pair still needs its zero-composite evidence.
assertnot [C : Cat] (S : τ (@PreadditiveCategory C))
  (C1 : τ (IsNCat (cat_succ cat_zero) C))
  [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  [X A B : τ (Obj C)] (b : τ (Hom C X A)) (d : τ (Hom C A B)) ⊢
  @terminal_zero_composite_transf C S C1 t T X A B b d
    (@eq_refl (Hom C X B) (@preadditive_hom_zero C S X B))
  : τ (@Hom (Functor_oplax_cat WalkingArrow_cat C)
      (@fapp0 C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
      (@OddDual_func WalkingArrow_cat C (@walking_arrow_func C A B d)));
