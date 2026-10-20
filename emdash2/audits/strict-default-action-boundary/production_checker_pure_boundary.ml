(* Bounded audit of the existing Pure rollback API after the isolated batch
   snapshot patch. This is not part of the installed checker. *)
let command fname text =
  match Pure.parse_text ~fname text with
  | [cmd], None -> cmd
  | _, Some (_, msg) -> failwith ("parse: " ^ msg)
  | _ -> failwith "expected exactly one command"

let step fname state text =
  match Pure.handle_command state (command fname text) with
  | Pure.Cmd_OK (state, _) -> state
  | Pure.Cmd_Error (_, msg) -> failwith ("command: " ^ msg)
  | Pure.Cmd_Proof _ -> failwith "unexpected proof mode"

let rejected fname state text =
  match Pure.handle_command state (command fname text) with
  | Pure.Cmd_Error _ -> ()
  | _ -> failwith "sensitivity control unexpectedly accepted"

let exercise package label =
  let first = Filename.concat package (label ^ "_first.lp") in
  let second = Filename.concat package (label ^ "_second.lp") in
  let initial = Pure.initial_state first in
  let imported = step first initial "require open scope_probe.common;" in
  let ruled = step first imported "rule f $x ↪ $x;" in
  ignore (step first ruled "assert ⊢ f a ≡ a;");
  rejected first ruled "assertnot ⊢ f a ≡ a;";
  ignore (step first imported "assertnot ⊢ f a ≡ a;");
  let redone = step first imported "rule f $x ↪ $x;" in
  ignore (step first redone "assert ⊢ f a ≡ a;");
  let fresh = Pure.initial_state second in
  let reimported = step second fresh "require open scope_probe.common;" in
  ignore (step second reimported "assertnot ⊢ f a ≡ a;");
  Printf.printf "%s: add / reject / rollback / redo / fresh-file passed\n%!" label

let () =
  let package = Sys.argv.(1) in
  let mode = Sys.argv.(2) in
  Common.Library.set_lib_root (Some (Sys.getcwd ()));
  Pure.set_initial_time ();
  (* Each mode starts in a new process before any package mapping. Releasing
     is not an API for restoring a discarded state. *)
  if mode = "recreated" then (Pure.release_initial_time (); Gc.full_major ())
  else if mode <> "normal" then failwith "unknown mode";
  exercise package mode;
  print_endline "Pure state boundary: PASS"
