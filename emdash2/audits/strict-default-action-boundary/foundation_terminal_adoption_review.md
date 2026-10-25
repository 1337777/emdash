# Accepted terminal Homd whole-comparison contract

Date: 2026-10-25. Status: complete public Homd consumer passes; full central integration pending.

The user explicitly selected “Adopt whole comparisons (Recommended)” for the
five terminal-source Homd cases. This resolves the acceptance choice recorded
as R01–R03. It does not select a new kernel computation or add equality proofs
to any operational symbol.

The preceding exact-current-core replay passes with subject reduction in
27.665 seconds and 168,960KiB at 90s/2GiB, receipt
`20261025T051637Z-2637327ca5bc45d8a6504a591f9c29b0`. It checks the same five
whole comparisons and the actual source/target action, relative leaf,
higher projection and inverse/neutral-unit distinctions. The runtime-negative
observations retain the former normal-form distinctions; they are not a
substitute for positive whole-comparison acceptance.

The public diagnostic fragment retains all 19 assertions. Exactly local
assertions 8, 9, 13, 14 and 15 now use typed reflexivity to exercise the existing
proof-time comparisons. The other fourteen are byte-for-byte unchanged.
Their historical runtime forms and the exact comparison hashes are retained
in [the decision inputs](foundation_terminal_contract_inputs.json).

The complete source replay emits all 2,441 central assertions: 2,162 positive
and 279 negative. Exactly five original central assertion blocks change; all
imports and the remaining assertions are unchanged. `central_full_context.lp`
is the complete diagnostic. The historical `central_full_context_except_terminal.lp`
filename is an import shim to that complete target and omits nothing. The
split migration regression also imports the complete public Homd controls.

All 1,387 original mathematical owners and reviewer files are byte-for-byte
unchanged from the running full-library candidate. Of the 1,388 registered
files, only `emdash3_2_checks.lp` changes. No extra rule, new primitive,
operational proof argument, strictness condition or inverse erasure is added.
The exact replay and source comparison are recorded in
[the integration verification](foundation_terminal_adoption_verification.json).

The complete public Homd consumer and retained action/inverse controls now
pass in 26.231s/168,772KiB at 90s/2GiB, subject reduction enabled, receipt
`20261025T115653Z-3b446413b25f4d869f80ae4c3ac25173`. The warning category and
rule-family inventories match the preceding exact-core replay. Full central
diagnostic integration is running separately with all 2,441 assertions and
no terminal omissions. The complete 791-owner library check also passed;
its mathematical inputs match this accepted candidate exactly.
Production promotion, supported-checker qualification, catalog/health updates
and the consolidated book/article/nerve continuations remain separate stages.
