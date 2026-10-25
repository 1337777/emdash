/*
  Whole terminal/initial arrow embeddings for the kernel/cokernel interface.

  X↦(X→t) uses TerminalObject(C,t). The direct dual X↦(t→X) uses the
  explicitly supplied TerminalObject(TotalOp(C),t), with its transfor obtained by
  TotalOp_transf. These definitions introduce no new zero-object capability or
  adjunction and do not infer whole dual structure from objectwise proofs.
*/
require open emdash.emdash3_2_arrow_diagram_families;
require open emdash.emdash3_2_terminal_objects;

// J:C→Arr_oplax(C), X↦(X→t), from the existing whole terminal-arrow transformation.
symbol terminal_arrow_diagram_func
  [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject C t))
  : τ (Functor C (Functor_oplax_cat WalkingArrow_cat C))
≔ @transf_arrow_diagram_func C C (@id_func C) (@Const_func C C t)
    (@terminal_arrow_transf C t T);

// The whole dual arrow transformation const_t⇒id_C, through total duality, which retains the default lax profile.
symbol initial_arrow_transf
  [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  : τ (@Transf C C (@Const_func C C t) (@id_func C))
≔ @TotalOp_transf (TotalOp_cat C) (TotalOp_cat C)
    (@id_func (TotalOp_cat C)) (@Const_func (TotalOp_cat C) (TotalOp_cat C) t)
    (@terminal_arrow_transf (TotalOp_cat C) t T);

// Native-C typed component view; the body remains the original dual arrow.
symbol initial_arrow_fapp0
  [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  (x : τ (Obj C))
  : τ (Hom C t x)
≔ @terminal_arrow_fapp0 (TotalOp_cat C) t T x;

// I:C→Arr_oplax(C), X↦(t→X); this is the direct dual, not a second arrow calculus.
symbol initial_arrow_diagram_func
  [C : Cat] [t : τ (Obj C)] (T : τ (@TerminalObject (TotalOp_cat C) t))
  : τ (Functor C (Functor_oplax_cat WalkingArrow_cat C))
≔ @transf_arrow_diagram_func C C (@Const_func C C t) (@id_func C)
    (@initial_arrow_transf C t T);
