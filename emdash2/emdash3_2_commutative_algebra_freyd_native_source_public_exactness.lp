/* Public adjacent pair at the source of the original native δ. */
require open emdash.emdash3_2_one_cat_family_public_pair_exactness;
require open emdash.emdash3_2_commutative_algebra_freyd_native_delta_comparison;
require open emdash.emdash3_2_commutative_algebra_freyd_native_column_homology_paths;
require open emdash.emdash3_2_commutative_algebra_freyd_raw_window_exactness;

// Derived ordinary-proof view of the existing projection comparison.
// Conversion is checked before concrete coefficient specialization. The body
// returns the existing proof; all operational maps and public inputs remain.
symbol one_cat_native_window_projection_comparison_view [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [Prod :
  τ (Functor (Product_cat C C) C)] [t : τ (Obj C)] (A : τ (@AdditiveCategory C Prod t)) (T0 : τ (@TerminalObject
  (TotalOp_cat C) t)) (P : τ (@KernelAdjunctionStructure C (@additive_preadditive C Prod t A) t
  (@additive_terminal_object C Prod t A))) (Q : τ (@CokernelAdjunctionStructure C (@additive_preadditive C Prod t
  A) t T0)) (N : τ (@OneCatAdjunctionNormality C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q)) (Rm R0 R1 R2 : τ (Functor B (@ZeroArrowCone_cat C t
  (@additive_terminal_object C Prod t A)))) (mm : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object
  C Prod t A)) Rm R0)) (m0 : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object C Prod t A)) R0 R1))
  (m1 : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object C Prod t A)) R1 R2)) (upper_zero : τ (@=
  (@Transf B C (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) Rm
  walking_arrow_src) (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R1
  walking_arrow_src)) (@comp_fapp0 (Functor_cat B C) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) Rm walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R0 walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R1 walking_arrow_src) (@zero_cone_row_family_vertex_map B C t
  (@additive_terminal_object C Prod t A) R0 R1 m0 walking_arrow_src) (@zero_cone_row_family_vertex_map B C t
  (@additive_terminal_object C Prod t A) Rm R0 mm walking_arrow_src)) (@zero_arrow_family_zero_transf B C t
  (@additive_terminal_object C Prod t A) T0 (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C
  Prod t A) Rm walking_arrow_src) (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  R1 walking_arrow_src)))) (lower_zero : τ (@= (@Transf B C (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R0 walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R2 walking_arrow_src)) (@comp_fapp0 (Functor_cat B C)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R0 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R1 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R2 walking_arrow_src)
  (@zero_cone_row_family_vertex_map B C t (@additive_terminal_object C Prod t A) R1 R2 m1 walking_arrow_src)
  (@zero_cone_row_family_vertex_map B C t (@additive_terminal_object C Prod t A) R0 R1 m0 walking_arrow_src))
  (@zero_arrow_family_zero_transf B C t (@additive_terminal_object C Prod t A) T0
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R0 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R2 walking_arrow_src)))) (Em : τ
  (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t
  A) T0 P Q Rm)) (E0 : τ (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q R0)) (E1 : τ (@OneCatZeroConeShortExactFamily B C
  (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q R1)) (E2 : τ
  (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t
  A) T0 P Q R2))
 (xw : τ (Obj B)) (obj_a obj_b : τ (Obj C))
 (map0 : τ (Hom C (@fapp0 B C (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) xw) obj_a))
 (map1 : τ (Hom C (@fapp0 B C (@one_cat_native_window_source_homology_func B C
  (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1
  upper_zero lower_zero Em E0 E1 E2) xw) obj_b))
 (public_arrow : τ (Hom C obj_a obj_b))
 (comparison : τ (@= (Hom C (@fapp0 B C (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  Rm walking_arrow_src) (@zero_cone_middle_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_middle_column_input B C C1 t (@additive_terminal_object C Prod t A) T0 Rm R0 R1 mm m0 upper_zero)) xw) obj_b) (@comp_fapp0 C (@fapp0 B C (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  Rm walking_arrow_src) (@zero_cone_middle_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_middle_column_input B C C1 t (@additive_terminal_object C Prod t A) T0 Rm R0 R1 mm m0 upper_zero)) xw) (@fapp0 B C (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) Rm
  walking_arrow_tgt) (@zero_cone_right_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_right_column_input B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 mm m0 upper_zero Em)) xw) obj_b map1 (@tapp0_fapp0 B C (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  Rm walking_arrow_src) (@zero_cone_middle_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_middle_column_input B C C1 t (@additive_terminal_object C Prod t A) T0 Rm R0 R1 mm m0 upper_zero)) (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) Rm
  walking_arrow_tgt) (@zero_cone_right_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_right_column_input B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 mm m0 upper_zero Em)) xw (@one_cat_row_triple_outgoing_homology_map B C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 mm m0 upper_zero Em E0 E1))) (@comp_fapp0 C (@fapp0 B C (@homology_adjunction_family_func B C (@additive_preadditive C Prod t A) t (@additive_terminal_object C Prod t A) T0 P Q (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  Rm walking_arrow_src) (@zero_cone_middle_column_outgoing_func B C t (@additive_terminal_object C Prod t A) R0 R1 m0)
  (@one_cat_zero_cone_middle_column_input B C C1 t (@additive_terminal_object C Prod t A) T0 Rm R0 R1 mm m0 upper_zero)) xw) obj_a obj_b public_arrow map0)))
 : τ (@= (Hom C (@fapp0 B C (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) xw) obj_b) (@comp_fapp0 C (@fapp0 B C (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) xw) (@fapp0 B C (@one_cat_native_window_source_homology_func B C
  (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1
  upper_zero lower_zero Em E0 E1 E2) xw) obj_b map1 (@tapp0_fapp0 B C (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) (@one_cat_native_window_source_homology_func B C
  (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1
  upper_zero lower_zero Em E0 E1 E2) xw (@one_cat_native_window_homology_projection B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1 E2))) (@comp_fapp0 C (@fapp0 B C (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) xw) obj_a obj_b public_arrow map0))
≔ comparison;

// Derived whole-family source-exactness view. The body is the existing
// theorem; its existing native input is exposed in the type before model
// specialization. No new premise, map, inverse or computation rule.
symbol one_cat_native_window_source_exact_family_view [B C : Cat] (C1 : τ (IsNCat (cat_succ cat_zero) C)) [Prod :
  τ (Functor (Product_cat C C) C)] [t : τ (Obj C)] (A : τ (@AdditiveCategory C Prod t)) (T0 : τ (@TerminalObject
  (TotalOp_cat C) t)) (P : τ (@KernelAdjunctionStructure C (@additive_preadditive C Prod t A) t
  (@additive_terminal_object C Prod t A))) (Q : τ (@CokernelAdjunctionStructure C (@additive_preadditive C Prod t
  A) t T0)) (N : τ (@OneCatAdjunctionNormality C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q)) (Rm R0 R1 R2 : τ (Functor B (@ZeroArrowCone_cat C t
  (@additive_terminal_object C Prod t A)))) (mm : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object
  C Prod t A)) Rm R0)) (m0 : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object C Prod t A)) R0 R1))
  (m1 : τ (@Transf B (@ZeroArrowCone_cat C t (@additive_terminal_object C Prod t A)) R1 R2)) (upper_zero : τ (@=
  (@Transf B C (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) Rm
  walking_arrow_src) (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R1
  walking_arrow_src)) (@comp_fapp0 (Functor_cat B C) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) Rm walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R0 walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R1 walking_arrow_src) (@zero_cone_row_family_vertex_map B C t
  (@additive_terminal_object C Prod t A) R0 R1 m0 walking_arrow_src) (@zero_cone_row_family_vertex_map B C t
  (@additive_terminal_object C Prod t A) Rm R0 mm walking_arrow_src)) (@zero_arrow_family_zero_transf B C t
  (@additive_terminal_object C Prod t A) T0 (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C
  Prod t A) Rm walking_arrow_src) (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A)
  R1 walking_arrow_src)))) (lower_zero : τ (@= (@Transf B C (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R0 walking_arrow_src) (@zero_cone_row_family_vertex_func B C t
  (@additive_terminal_object C Prod t A) R2 walking_arrow_src)) (@comp_fapp0 (Functor_cat B C)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R0 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R1 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R2 walking_arrow_src)
  (@zero_cone_row_family_vertex_map B C t (@additive_terminal_object C Prod t A) R1 R2 m1 walking_arrow_src)
  (@zero_cone_row_family_vertex_map B C t (@additive_terminal_object C Prod t A) R0 R1 m0 walking_arrow_src))
  (@zero_arrow_family_zero_transf B C t (@additive_terminal_object C Prod t A) T0
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R0 walking_arrow_src)
  (@zero_cone_row_family_vertex_func B C t (@additive_terminal_object C Prod t A) R2 walking_arrow_src)))) (Em : τ
  (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t
  A) T0 P Q Rm)) (E0 : τ (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q R0)) (E1 : τ (@OneCatZeroConeShortExactFamily B C
  (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q R1)) (E2 : τ
  (@OneCatZeroConeShortExactFamily B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t
  A) T0 P Q R2))
 : τ (@OneCatAdjunctionExactFamily B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t
  A) T0 P Q (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0
  m1 upper_zero lower_zero Em E0 E1 E2) (@transf_arrow_diagram_func B C
  (@one_cat_native_window_source_homology_func B C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1 E2)
  (@one_cat_native_window_target_homology_func B C (@additive_preadditive C Prod t A) C1 t
  (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1 E2)
  (@one_cat_native_window_connecting_transf B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em
  E0 E1 E2)) (@one_cat_kernel_family_input B C C1 t (@additive_terminal_object C Prod t A) T0
  (@one_cat_native_window_middle_source_homology_func B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0 m1
  upper_zero lower_zero Em E0 E1 E2) (@transf_arrow_diagram_func B C (@one_cat_native_window_source_homology_func
  B C (@additive_preadditive C Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1
  upper_zero lower_zero Em E0 E1 E2) (@one_cat_native_window_target_homology_func B C (@additive_preadditive C
  Prod t A) C1 t (@additive_terminal_object C Prod t A) T0 P Q Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1
  E2) (@one_cat_native_window_connecting_transf B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0 m1 upper_zero
  lower_zero Em E0 E1 E2)) (@one_cat_native_window_homology_projection B C C1 Prod t A T0 P Q N Rm R0 R1 R2
  mm m0 m1 upper_zero lower_zero Em E0 E1 E2) (@one_cat_native_window_connecting_projection_zero B C C1 Prod
  t A T0 P Q N Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1 E2)) N)
≔ @one_cat_native_window_source_exact_omega B C C1 Prod t A T0 P Q N Rm R0 R1 R2 mm m0 m1 upper_zero lower_zero Em E0 E1 E2;

symbol freyd_native_source_public_input [K : Cat] [R : τ CommRing]
  (M : τ (FreydAdjunctionModel R))
  (N : τ (@FreydAdjunctionModelNormality R M))
  [Am : τ (@CommRingPresentation R)]
  [Bm : τ (@CommRingPresentation R)]
  [Dm : τ (@CommRingPresentation R)]
  [A0 : τ (@CommRingPresentation R)]
  [B0 : τ (@CommRingPresentation R)]
  [D0 : τ (@CommRingPresentation R)]
  [A1 : τ (@CommRingPresentation R)]
  [B1 : τ (@CommRingPresentation R)]
  [D1 : τ (@CommRingPresentation R)]
  [A2 : τ (@CommRingPresentation R)]
  [B2 : τ (@CommRingPresentation R)]
  [D2 : τ (@CommRingPresentation R)]
  (im : τ (@CommRingPresentationMorphism R Am Bm))
  (pm : τ (@CommRingPresentationMorphism R Bm Dm))
  (cm : τ (@CommRingFreydChainPair R Am Bm Dm im pm))
  (xm : τ (@FreydRawNativeRowShortExact K R M Am Bm Dm im pm cm))
  (i0 : τ (@CommRingPresentationMorphism R A0 B0))
  (p0 : τ (@CommRingPresentationMorphism R B0 D0))
  (c0 : τ (@CommRingFreydChainPair R A0 B0 D0 i0 p0))
  (x0 : τ (@FreydRawNativeRowShortExact K R M A0 B0 D0 i0 p0 c0))
  (i1 : τ (@CommRingPresentationMorphism R A1 B1))
  (p1 : τ (@CommRingPresentationMorphism R B1 D1))
  (c1 : τ (@CommRingFreydChainPair R A1 B1 D1 i1 p1))
  (x1 : τ (@FreydRawNativeRowShortExact K R M A1 B1 D1 i1 p1 c1))
  (i2 : τ (@CommRingPresentationMorphism R A2 B2))
  (p2 : τ (@CommRingPresentationMorphism R B2 D2))
  (c2 : τ (@CommRingFreydChainPair R A2 B2 D2 i2 p2))
  (x2 : τ (@FreydRawNativeRowShortExact K R M A2 B2 D2 i2 p2 c2))
  (am : τ (@CommRingPresentationMorphism R Am A0))
  (bm : τ (@CommRingPresentationMorphism R Bm B0))
  (dm : τ (@CommRingPresentationMorphism R Dm D0))
  (fm : τ (@CommRingFreydHomologyChainMap R Am Bm Dm A0 B0 D0 im pm i0 p0 am bm dm))
  (a0 : τ (@CommRingPresentationMorphism R A0 A1))
  (b0 : τ (@CommRingPresentationMorphism R B0 B1))
  (d0 : τ (@CommRingPresentationMorphism R D0 D1))
  (gm : τ (@CommRingFreydHomologyChainMap R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0))
  (a1 : τ (@CommRingPresentationMorphism R A1 A2))
  (b1 : τ (@CommRingPresentationMorphism R B1 B2))
  (d1 : τ (@CommRingPresentationMorphism R D1 D2))
  (jm : τ (@CommRingFreydHomologyChainMap R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1))
  (upper : τ (@CommRingFreydChainPair R Bm B0 B1 bm b0))
  (lower : τ (@CommRingFreydChainPair R B0 B1 B2 b0 b1))
 (source_chain : τ (@CommRingFreydChainPair R Dm D0 D1 dm d0))
 (target_chain : τ (@CommRingFreydChainPair R A0 A1 A2 a0 a1)) (x : τ (Obj K))
 (unused_left_chain : τ (@CommRingFreydChainPair R Am A0 A1 am a0))
 (column_map : τ (@CommRingFreydHomologyChainMap R Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1))
≔ @native_family_public_pair_input
  K
  (@CommRingFreydPresentation_cat R)
  (@additive_preadditive
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R)
  (@comm_ring_zero_presentation R)
  (@additive_terminal_object (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@freyd_adjunction_model_initial R M)
  (@one_cat_native_window_middle_source_homology_func K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_source_homology_func
  K (@CommRingFreydPresentation_cat R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_target_homology_func K (@CommRingFreydPresentation_cat
  R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1
  x2)
  (@one_cat_native_window_homology_projection K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2)
  (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_transf K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper)
  (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_projection_zero K
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func
  R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M)
  (@freyd_adjunction_model_kernels R M) (@freyd_adjunction_model_cokernels R M) N
  (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0
  c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1 c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2
  p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  x
  (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper)
  (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain)
  (@freyd_adjunction_model_object R M A0
  A1 A2 a0 a1 target_chain)
  (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map)
  (@freyd_raw_native_window_connecting_at K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2
  B2 D2 im pm cm xm i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower
  source_chain target_chain x)
  (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x)
  (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain)
  (@freyd_raw_native_left_column_homology_map K R M A0 B0
  D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 c0 c1 c2 a0 b0 d0 a1 b1 d1 gm jm lower x2 x target_chain)
  (@freyd_raw_native_middle_column_homology_equiv K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0
  c1 am bm dm a0 b0 d0 fm gm upper x)
  (@one_cat_native_window_projection_comparison_view K (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm) (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm) (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2 x (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper) (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain) (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x) (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain) (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map) (@eq_sym _ _ _ (@freyd_native_column_outgoing_homology_path K R M Am
  Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper xm x0 x1 x
  unused_left_chain source_chain column_map)))
  (@eq_sym _ _ _
  (@freyd_native_window_connecting_comparison_path K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2 B2 D2 im pm cm xm
  i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower source_chain
  target_chain x));

symbol freyd_native_source_public_input_equiv [K : Cat] [R : τ CommRing]
  (M : τ (FreydAdjunctionModel R))
  (N : τ (@FreydAdjunctionModelNormality R M))
  [Am : τ (@CommRingPresentation R)]
  [Bm : τ (@CommRingPresentation R)]
  [Dm : τ (@CommRingPresentation R)]
  [A0 : τ (@CommRingPresentation R)]
  [B0 : τ (@CommRingPresentation R)]
  [D0 : τ (@CommRingPresentation R)]
  [A1 : τ (@CommRingPresentation R)]
  [B1 : τ (@CommRingPresentation R)]
  [D1 : τ (@CommRingPresentation R)]
  [A2 : τ (@CommRingPresentation R)]
  [B2 : τ (@CommRingPresentation R)]
  [D2 : τ (@CommRingPresentation R)]
  (im : τ (@CommRingPresentationMorphism R Am Bm))
  (pm : τ (@CommRingPresentationMorphism R Bm Dm))
  (cm : τ (@CommRingFreydChainPair R Am Bm Dm im pm))
  (xm : τ (@FreydRawNativeRowShortExact K R M Am Bm Dm im pm cm))
  (i0 : τ (@CommRingPresentationMorphism R A0 B0))
  (p0 : τ (@CommRingPresentationMorphism R B0 D0))
  (c0 : τ (@CommRingFreydChainPair R A0 B0 D0 i0 p0))
  (x0 : τ (@FreydRawNativeRowShortExact K R M A0 B0 D0 i0 p0 c0))
  (i1 : τ (@CommRingPresentationMorphism R A1 B1))
  (p1 : τ (@CommRingPresentationMorphism R B1 D1))
  (c1 : τ (@CommRingFreydChainPair R A1 B1 D1 i1 p1))
  (x1 : τ (@FreydRawNativeRowShortExact K R M A1 B1 D1 i1 p1 c1))
  (i2 : τ (@CommRingPresentationMorphism R A2 B2))
  (p2 : τ (@CommRingPresentationMorphism R B2 D2))
  (c2 : τ (@CommRingFreydChainPair R A2 B2 D2 i2 p2))
  (x2 : τ (@FreydRawNativeRowShortExact K R M A2 B2 D2 i2 p2 c2))
  (am : τ (@CommRingPresentationMorphism R Am A0))
  (bm : τ (@CommRingPresentationMorphism R Bm B0))
  (dm : τ (@CommRingPresentationMorphism R Dm D0))
  (fm : τ (@CommRingFreydHomologyChainMap R Am Bm Dm A0 B0 D0 im pm i0 p0 am bm dm))
  (a0 : τ (@CommRingPresentationMorphism R A0 A1))
  (b0 : τ (@CommRingPresentationMorphism R B0 B1))
  (d0 : τ (@CommRingPresentationMorphism R D0 D1))
  (gm : τ (@CommRingFreydHomologyChainMap R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0))
  (a1 : τ (@CommRingPresentationMorphism R A1 A2))
  (b1 : τ (@CommRingPresentationMorphism R B1 B2))
  (d1 : τ (@CommRingPresentationMorphism R D1 D2))
  (jm : τ (@CommRingFreydHomologyChainMap R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1))
  (upper : τ (@CommRingFreydChainPair R Bm B0 B1 bm b0))
  (lower : τ (@CommRingFreydChainPair R B0 B1 B2 b0 b1))
 (source_chain : τ (@CommRingFreydChainPair R Dm D0 D1 dm d0))
 (target_chain : τ (@CommRingFreydChainPair R A0 A1 A2 a0 a1)) (x : τ (Obj K))
 (unused_left_chain : τ (@CommRingFreydChainPair R Am A0 A1 am a0))
 (column_map : τ (@CommRingFreydHomologyChainMap R Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1))
≔ @native_family_public_pair_equiv
  K
  (@CommRingFreydPresentation_cat R)
  (@additive_preadditive
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R)
  (@comm_ring_zero_presentation R)
  (@additive_terminal_object (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@freyd_adjunction_model_initial R M)
  (@one_cat_native_window_middle_source_homology_func K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_source_homology_func
  K (@CommRingFreydPresentation_cat R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_target_homology_func K (@CommRingFreydPresentation_cat
  R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1
  x2)
  (@one_cat_native_window_homology_projection K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2)
  (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_transf K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper)
  (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_projection_zero K
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func
  R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M)
  (@freyd_adjunction_model_kernels R M) (@freyd_adjunction_model_cokernels R M) N
  (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0
  c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1 c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2
  p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  x
  (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper)
  (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain)
  (@freyd_adjunction_model_object R M A0
  A1 A2 a0 a1 target_chain)
  (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map)
  (@freyd_raw_native_window_connecting_at K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2
  B2 D2 im pm cm xm i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower
  source_chain target_chain x)
  (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x)
  (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain)
  (@freyd_raw_native_left_column_homology_map K R M A0 B0
  D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 c0 c1 c2 a0 b0 d0 a1 b1 d1 gm jm lower x2 x target_chain)
  (@freyd_raw_native_middle_column_homology_equiv K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0
  c1 am bm dm a0 b0 d0 fm gm upper x)
  (@one_cat_native_window_projection_comparison_view K (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm) (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm) (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2 x (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper) (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain) (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x) (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain) (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map) (@eq_sym _ _ _ (@freyd_native_column_outgoing_homology_path K R M Am
  Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper xm x0 x1 x
  unused_left_chain source_chain column_map)))
  (@eq_sym _ _ _
  (@freyd_native_window_connecting_comparison_path K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2 B2 D2 im pm cm xm
  i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower source_chain
  target_chain x))
  (@freyd_raw_native_right_column_homology_equiv K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm
  i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper xm x source_chain)
  (@freyd_raw_native_left_column_homology_equiv K R M A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 c0 c1
  c2 a0 b0 d0 a1 b1 d1 gm jm lower x2 x target_chain);

symbol freyd_native_source_public_exact [K : Cat] [R : τ CommRing]
  (M : τ (FreydAdjunctionModel R))
  (N : τ (@FreydAdjunctionModelNormality R M))
  [Am : τ (@CommRingPresentation R)]
  [Bm : τ (@CommRingPresentation R)]
  [Dm : τ (@CommRingPresentation R)]
  [A0 : τ (@CommRingPresentation R)]
  [B0 : τ (@CommRingPresentation R)]
  [D0 : τ (@CommRingPresentation R)]
  [A1 : τ (@CommRingPresentation R)]
  [B1 : τ (@CommRingPresentation R)]
  [D1 : τ (@CommRingPresentation R)]
  [A2 : τ (@CommRingPresentation R)]
  [B2 : τ (@CommRingPresentation R)]
  [D2 : τ (@CommRingPresentation R)]
  (im : τ (@CommRingPresentationMorphism R Am Bm))
  (pm : τ (@CommRingPresentationMorphism R Bm Dm))
  (cm : τ (@CommRingFreydChainPair R Am Bm Dm im pm))
  (xm : τ (@FreydRawNativeRowShortExact K R M Am Bm Dm im pm cm))
  (i0 : τ (@CommRingPresentationMorphism R A0 B0))
  (p0 : τ (@CommRingPresentationMorphism R B0 D0))
  (c0 : τ (@CommRingFreydChainPair R A0 B0 D0 i0 p0))
  (x0 : τ (@FreydRawNativeRowShortExact K R M A0 B0 D0 i0 p0 c0))
  (i1 : τ (@CommRingPresentationMorphism R A1 B1))
  (p1 : τ (@CommRingPresentationMorphism R B1 D1))
  (c1 : τ (@CommRingFreydChainPair R A1 B1 D1 i1 p1))
  (x1 : τ (@FreydRawNativeRowShortExact K R M A1 B1 D1 i1 p1 c1))
  (i2 : τ (@CommRingPresentationMorphism R A2 B2))
  (p2 : τ (@CommRingPresentationMorphism R B2 D2))
  (c2 : τ (@CommRingFreydChainPair R A2 B2 D2 i2 p2))
  (x2 : τ (@FreydRawNativeRowShortExact K R M A2 B2 D2 i2 p2 c2))
  (am : τ (@CommRingPresentationMorphism R Am A0))
  (bm : τ (@CommRingPresentationMorphism R Bm B0))
  (dm : τ (@CommRingPresentationMorphism R Dm D0))
  (fm : τ (@CommRingFreydHomologyChainMap R Am Bm Dm A0 B0 D0 im pm i0 p0 am bm dm))
  (a0 : τ (@CommRingPresentationMorphism R A0 A1))
  (b0 : τ (@CommRingPresentationMorphism R B0 B1))
  (d0 : τ (@CommRingPresentationMorphism R D0 D1))
  (gm : τ (@CommRingFreydHomologyChainMap R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0))
  (a1 : τ (@CommRingPresentationMorphism R A1 A2))
  (b1 : τ (@CommRingPresentationMorphism R B1 B2))
  (d1 : τ (@CommRingPresentationMorphism R D1 D2))
  (jm : τ (@CommRingFreydHomologyChainMap R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1))
  (upper : τ (@CommRingFreydChainPair R Bm B0 B1 bm b0))
  (lower : τ (@CommRingFreydChainPair R B0 B1 B2 b0 b1))
 (source_chain : τ (@CommRingFreydChainPair R Dm D0 D1 dm d0))
 (target_chain : τ (@CommRingFreydChainPair R A0 A1 A2 a0 a1)) (x : τ (Obj K))
 (unused_left_chain : τ (@CommRingFreydChainPair R Am A0 A1 am a0))
 (column_map : τ (@CommRingFreydHomologyChainMap R Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1))
≔ @native_family_public_pair_exact
  K
  (@CommRingFreydPresentation_cat R)
  (@additive_preadditive
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R)
  (@comm_ring_zero_presentation R)
  (@additive_terminal_object (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@freyd_adjunction_model_initial R M)
  (@one_cat_native_window_middle_source_homology_func K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_source_homology_func
  K (@CommRingFreydPresentation_cat R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_target_homology_func K (@CommRingFreydPresentation_cat
  R) (@additive_preadditive (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R))
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_zero_presentation R) (@additive_terminal_object
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation R)
  (@comm_ring_freyd_additive R)) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels R
  M) (@freyd_adjunction_model_cokernels R M) (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1
  x2)
  (@one_cat_native_window_homology_projection K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2)
  (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_transf K (@CommRingFreydPresentation_cat R)
  (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm)
  (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0
  D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper)
  (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  (@one_cat_native_window_connecting_projection_zero K
  (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func
  R)
  (@comm_ring_zero_presentation R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M)
  (@freyd_adjunction_model_kernels R M) (@freyd_adjunction_model_cokernels R M) N
  (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0
  c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1 c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2
  p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm)
  (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm)
  (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2)
  x
  (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper)
  (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain)
  (@freyd_adjunction_model_object R M A0
  A1 A2 a0 a1 target_chain)
  (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map)
  (@freyd_raw_native_window_connecting_at K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2
  B2 D2 im pm cm xm i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower
  source_chain target_chain x)
  (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x)
  (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain)
  (@freyd_raw_native_left_column_homology_map K R M A0 B0
  D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 c0 c1 c2 a0 b0 d0 a1 b1 d1 gm jm lower x2 x target_chain)
  (@freyd_raw_native_middle_column_homology_equiv K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0
  c1 am bm dm a0 b0 d0 fm gm upper x)
  (@one_cat_native_window_projection_comparison_view K (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm) (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm) (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2 x (@freyd_adjunction_model_object R M Bm B0 B1 bm b0 upper) (@freyd_adjunction_model_object R M Dm D0 D1 dm d0 source_chain) (@freyd_raw_native_middle_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1
  D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper x) (@freyd_raw_native_right_column_homology_map K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1
  am bm dm a0 b0 d0 fm gm upper xm x source_chain) (@freyd_adjunction_model_map R M Bm B0 B1 Dm D0 D1 bm b0 dm d0 pm p0 p1 upper
  source_chain column_map) (@eq_sym _ _ _ (@freyd_native_column_outgoing_homology_path K R M Am
  Bm Dm A0 B0 D0 A1 B1 D1 im pm i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper xm x0 x1 x
  unused_left_chain source_chain column_map)))
  (@eq_sym _ _ _
  (@freyd_native_window_connecting_comparison_path K R M N Am Bm Dm A0 B0 D0 A1 B1 D1 A2 B2 D2 im pm cm xm
  i0 p0 c0 x0 i1 p1 c1 x1 i2 p2 c2 x2 am bm dm fm a0 b0 d0 gm a1 b1 d1 jm upper lower source_chain
  target_chain x))
  (@freyd_raw_native_right_column_homology_equiv K R M Am Bm Dm A0 B0 D0 A1 B1 D1 im pm
  i0 p0 i1 p1 cm c0 c1 am bm dm a0 b0 d0 fm gm upper xm x source_chain)
  (@freyd_raw_native_left_column_homology_equiv K R M A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 c0 c1
  c2 a0 b0 d0 a1 b1 d1 gm jm lower x2 x target_chain)
  (@freyd_adjunction_model_kernels R M)
  (@freyd_adjunction_model_cokernels R M)
  N
  (@one_cat_native_window_source_exact_family_view K (@CommRingFreydPresentation_cat R) (@comm_ring_freyd_cat_is_one_cat R) (@comm_ring_freyd_direct_sum_func R) (@comm_ring_zero_presentation
  R) (@comm_ring_freyd_additive R) (@freyd_adjunction_model_initial R M) (@freyd_adjunction_model_kernels
  R M) (@freyd_adjunction_model_cokernels R M) N (@freyd_raw_native_row_family K R Am Bm Dm im pm cm) (@freyd_raw_native_row_family K R A0 B0 D0 i0 p0 c0) (@freyd_raw_native_row_family K R A1 B1 D1 i1 p1
  c1) (@freyd_raw_native_row_family K R A2 B2 D2 i2 p2 c2) (@freyd_raw_native_row_map K R Am Bm Dm A0 B0 D0 im pm i0
  p0 am bm dm cm c0 fm) (@freyd_raw_native_row_map K R A0 B0 D0 A1 B1 D1 i0 p0 i1 p1 a0 b0 d0 c0 c1 gm) (@freyd_raw_native_row_map K R A1 B1 D1 A2 B2 D2 i1 p1 i2 p2 a1 b1 d1 c1 c2 jm) (@freyd_raw_native_row_middle_zero K R (@freyd_adjunction_model_initial R M) Am Bm Dm A0 B0 D0 A1 B1 D1
  im pm
  i0 p0 i1 p1 am bm dm a0 b0 d0 cm c0 c1 fm gm upper) (@freyd_raw_native_row_middle_zero K R
  (@freyd_adjunction_model_initial R M) A0 B0 D0 A1 B1 D1 A2 B2 D2 i0 p0 i1 p1 i2 p2 a0 b0 d0 a1 b1 d1 c0
  c1 c2
  gm jm lower) xm x0 x1 x2);
