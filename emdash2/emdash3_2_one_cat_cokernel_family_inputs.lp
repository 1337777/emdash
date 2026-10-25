/* Whole cokernel inputs from an internally supplied annihilation cell.
   Realize one native square in Functor_cat(B,C), then exchange back. For an
   arbitrary original diagram family, first use the accepted whole shape
   reconstruction there. No pointwise naturality data or new diagram is
   substituted for the original universal-operation input. */
require open emdash.emdash3_2_one_cat_diagram_family_paths;
require open emdash.emdash3_2_one_cat_diagram_family_reconstruction;
require open emdash.emdash3_2_one_cat_arrow_diagrams;

// Canonical whole zero through the original initial/terminal family arrows.
symbol zero_arrow_family_zero_transf [B C : Cat] [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (X Y : τ (Functor B C)) : τ (@Transf B C X Y)
≔ @comp_fapp0 (Functor_cat B C) X (@Const_func B C t) Y
    (@diagram_oplax_family_transf B WalkingArrow_cat C
      (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
      walking_arrow_src walking_arrow_tgt walking_arrow_generator)
    (@diagram_oplax_family_transf B WalkingArrow_cat C
      (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
      walking_arrow_src walking_arrow_tgt walking_arrow_generator);

// Form a whole map Arr(k)⇒I∘Y from one whole annihilation cell u∘k=0.
symbol one_cat_cokernel_family_introduced_input [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (X A Y : τ (Functor B C)) (k : τ (@Transf B C X A)) (u : τ (@Transf B C A Y))
  (z : τ (@= (@Transf B C X Y) (@comp_fapp0 (Functor_cat B C) X A Y u k)
    (@zero_arrow_family_zero_transf B C t T T0 X Y)))
  : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) (@transf_arrow_diagram_func B C X A k)
      (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y))
≔ @comp_fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C))
    (@transf_arrow_diagram_func B C X A k)
    (@transf_arrow_diagram_func B C (@Const_func B C t) Y
      (@diagram_oplax_family_transf B WalkingArrow_cat C
        (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
        walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
    (@one_cat_oplax_diagram_family_reconstruction_to B C C1 (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y))
    (@one_cat_family_oplax_exchange_map WalkingArrow_cat B C C1
      (@walking_arrow_func (Functor_cat B C) X A k)
      (@walking_arrow_func (Functor_cat B C) (@Const_func B C t) Y
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
        X (@Const_func B C t) A Y k
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator) u
        (@path_to_hom (Hom_cat (Functor_cat B C) X Y)
          (@comp_fapp0 (Functor_cat B C) X A Y u k) (@zero_arrow_family_zero_transf B C t T T0 X Y) z)));

// General original diagram family: construct the same map while retaining D.
symbol one_cat_cokernel_family_input [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C))) (Y : τ (Functor B C))
  (u : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y))
  (z : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) Y)
      (@comp_fapp0 (Functor_cat B C)
        (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
        (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y u
        (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@zero_arrow_family_zero_transf B C t T T0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
        Y)))
  : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) D
      (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y))
≔ @comp_fapp0 (Functor_cat B (Functor_oplax_cat WalkingArrow_cat C)) D
    (@transf_arrow_diagram_func B C
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt)
      (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
    (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
    (@one_cat_cokernel_family_introduced_input B C C1 t T T0
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
      (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y
      (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator) u z)
    (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D);

// Introduced input retains the original u as its whole target map.
symbol one_cat_cokernel_family_introduced_target_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (X A Y : τ (Functor B C)) (k : τ (@Transf B C X A)) (u : τ (@Transf B C A Y))
  (z : τ (@= (@Transf B C X Y) (@comp_fapp0 (Functor_cat B C) X A Y u k)
    (@zero_arrow_family_zero_transf B C t T T0 X Y)))
  : τ (@= (@Transf B C A Y)
      (@diagram_oplax_family_map_at B WalkingArrow_cat C (@transf_arrow_diagram_func B C X A k) (@comp_cat_fapp0 B C
        (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
        (@one_cat_cokernel_family_introduced_input B C C1 t T T0 X A Y k u z) walking_arrow_tgt) u)
≔ let F0 : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)) ≔ (@transf_arrow_diagram_func B C X A k) in
  let G0 : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)) ≔ (@transf_arrow_diagram_func B C (@Const_func B C t) Y
      (@diagram_oplax_family_transf B WalkingArrow_cat C
        (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
        walking_arrow_src walking_arrow_tgt walking_arrow_generator)) in
  let H0 : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)) ≔ (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y) in
  let V0 : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) G0 H0) ≔ (@one_cat_oplax_diagram_family_reconstruction_to B C C1 (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)) in
  let U0 : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) F0 G0) ≔ (@one_cat_family_oplax_exchange_map WalkingArrow_cat B C C1
      (@walking_arrow_func (Functor_cat B C) X A k)
      (@walking_arrow_func (Functor_cat B C) (@Const_func B C t) Y
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
        X (@Const_func B C t) A Y k
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator) u
        (@path_to_hom (Hom_cat (Functor_cat B C) X Y)
          (@comp_fapp0 (Functor_cat B C) X A Y u k) (@zero_arrow_family_zero_transf B C t T T0 X Y) z))) in
  let p0 : τ (@Transf B C Y Y) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C G0 H0 V0 walking_arrow_tgt) in
  let q0 : τ (@Transf B C A Y) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C F0 G0 U0 walking_arrow_tgt) in
  @eq_trans (@Transf B C A Y) (@diagram_oplax_family_map_at B WalkingArrow_cat C F0 H0 (@one_cat_cokernel_family_introduced_input B C C1 t T T0 X A Y k u z) walking_arrow_tgt) (@comp_fapp0 (Functor_cat B C) A Y Y p0 q0) u
    (@one_cat_oplax_family_evaluation_comp_path B WalkingArrow_cat C C1 walking_arrow_tgt F0 G0 H0 V0 U0)
    (@eq_trans (@Transf B C A Y) (@comp_fapp0 (Functor_cat B C) A Y Y p0 q0) q0 u
      (@eq_ap (@Transf B C Y Y) (@Transf B C A Y)
        (λ v : τ (@Transf B C Y Y), @comp_fapp0 (Functor_cat B C) A Y Y v q0)
        p0 (@id (Functor_cat B C) Y) (@one_cat_oplax_reconstruction_to_tgt_path B C C1 H0))
      (@one_cat_oplax_exchange_at_path WalkingArrow_cat B C C1 (@walking_arrow_func (Functor_cat B C) X A k) (@walking_arrow_func (Functor_cat B C) (@Const_func B C t) Y
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)) (@one_cat_square_diagram_transf (Functor_cat B C) (@one_cat_functor_category B C C1)
        X (@Const_func B C t) A Y k
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator)
        (@diagram_oplax_family_transf B WalkingArrow_cat C
          (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@terminal_arrow_diagram_func C t T) X)
          walking_arrow_src walking_arrow_tgt walking_arrow_generator) u
        (@path_to_hom (Hom_cat (Functor_cat B C) X Y)
          (@comp_fapp0 (Functor_cat B C) X A Y u k) (@zero_arrow_family_zero_transf B C t T T0 X Y) z)) walking_arrow_tgt));

// Reconstruction has identity endpoints, so the original-family input retains u.
symbol one_cat_cokernel_family_input_target_path [B C : Cat]
  (C1 : τ (IsNCat (cat_succ cat_zero) C)) [t : τ (Obj C)]
  (T : τ (@TerminalObject C t)) (T0 : τ (@TerminalObject (TotalOp_cat C) t))
  (D : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C))) (Y : τ (Functor B C))
  (u : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y))
  (z : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) Y)
      (@comp_fapp0 (Functor_cat B C)
        (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
        (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y u
        (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator))
      (@zero_arrow_family_zero_transf B C t T T0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src)
        Y)))
  : τ (@= (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y) (@diagram_oplax_family_map_at
    B WalkingArrow_cat C D (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0)
    Y) (@one_cat_cokernel_family_input B C C1 t T T0 D Y u z) walking_arrow_tgt) u)
≔ let R0 : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)) ≔ (@transf_arrow_diagram_func B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator)) in
  let H0 : τ (Functor B (Functor_oplax_cat WalkingArrow_cat C)) ≔ (@comp_cat_fapp0 B C (Functor_oplax_cat WalkingArrow_cat C) (@initial_arrow_diagram_func C t T0) Y) in
  let U0 : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) R0 H0) ≔ (@one_cat_cokernel_family_introduced_input B C C1 t T T0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator) u z) in
  let V0 : τ (@Transf B (Functor_oplax_cat WalkingArrow_cat C) D R0) ≔ (@one_cat_oplax_diagram_family_reconstruction_from B C C1 D) in
  let u0 : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C R0 H0 U0 walking_arrow_tgt) in
  let v0 : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt)) ≔ (@diagram_oplax_family_map_at B WalkingArrow_cat C D R0 V0 walking_arrow_tgt) in
  @eq_trans (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y) (@diagram_oplax_family_map_at B WalkingArrow_cat C D H0 (@one_cat_cokernel_family_input B C C1 t T T0 D Y u z) walking_arrow_tgt) u0 u
    (@eq_trans (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y) (@diagram_oplax_family_map_at B WalkingArrow_cat C D H0 (@one_cat_cokernel_family_input B C C1 t T T0 D Y u z) walking_arrow_tgt)
      (@comp_fapp0 (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y u0 v0) u0
      (@one_cat_oplax_family_evaluation_comp_path B WalkingArrow_cat C C1 walking_arrow_tgt D R0 H0 U0 V0)
      (@eq_ap (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt)) (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y)
        (λ q : τ (@Transf B C (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt)), @comp_fapp0 (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y u0 q)
        v0 (@id (Functor_cat B C) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt)) (@one_cat_oplax_reconstruction_from_tgt_path B C C1 D)))
    (@one_cat_cokernel_family_introduced_target_path B C C1 t T T0 (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_src) (@diagram_oplax_family_at_func B WalkingArrow_cat C D walking_arrow_tgt) Y (@diagram_oplax_family_transf B WalkingArrow_cat C D walking_arrow_src walking_arrow_tgt walking_arrow_generator) u z);
