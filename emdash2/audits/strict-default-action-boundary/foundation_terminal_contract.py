"""Adopt the approved five whole terminal Homd comparisons in diagnostics.

No mathematical owner changes. Original runtime assertions are retained in
the input ledger as historical distinctions, not acceptance requirements.
Run only on a disposable, idle package; generation is not qualification.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
INPUTS = json.loads((HERE / 'foundation_terminal_contract_inputs.json').read_text())
HEADER = '// Original public Homd ladder, at the selected Q/index types.'
END = '// catalog-area: Categorical-universe direct equality-valued'


def assertions(text):
    return re.findall(r'(?m)^assert\b.*?;', text, re.S)


def comparisons():
    blocks = assertions((HERE / 'production_terminal_homd_comparison_controls.lpfragment').read_text())[:5]
    assert len(blocks) == len(INPUTS['cases']) == 5
    for block, case in zip(blocks, INPUTS['cases']):
        assert hashlib.sha256(block.encode()).hexdigest() == case['wholeComparisonSha256']
    return blocks


def apply(package):
    path = package / 'emdash3_2_checks.lp'
    before = path.read_text()
    text = before
    for case, new in zip(INPUTS['cases'], comparisons()):
        old = case['formerRuntimeAssertion']
        assert (text.count(old), text.count(new)) in ((1, 0), (0, 1))
        text = text.replace(old, new, 1)
    start = text.index(HEADER)
    end = text.index(END, start)
    public = (HERE / 'production_public_homd_controls.lpfragment').read_text().rstrip() + '\n\n'
    assert assertions(text[start:end]) == assertions(public)
    text = text[:start] + public + text[end:]
    assert len(assertions(text)) == len(assertions(before))
    assert not re.search(r'(?m)^// R01-R03 unresolved runtime obligation:', text)
    blocks = assertions(public)
    terminal = comparisons()
    general = [block for block in blocks if block not in terminal]
    assert len(blocks) == 19 and len(general) == 14
    prefix = 'require open emdash.emdash3_2;\n'
    outputs = {
        'emdash3_2_checks.lp': text,
        'central_public_homd_controls.lp': prefix + public,
        'central_public_homd_general_controls.lp': prefix + '\n\n'.join(general) + '\n',
        'central_public_homd_terminal_obligations.lp':
            '// Accepted whole proof-time contract; all five remain positive.\n'
            + prefix + '\n\n'.join(terminal) + '\n',
        'terminal_homd_comparison_controls.lp': prefix
            + (HERE / 'production_terminal_homd_comparison_controls.lpfragment').read_text(),
        'central_full_context.lp': text,
        # Retain old driver imports without retaining their five omissions.
        'central_full_context_except_terminal.lp':
            '// Legacy audit filename; now includes every accepted central assertion.\n'
            'require open emdash.central_full_context;\n',
    }
    driver = package / 'central_migration_regression.lp'
    if driver.exists():
        body = driver.read_text()
        old = 'require open emdash.central_public_homd_general_controls;'
        new = 'require open emdash.central_public_homd_controls;'
        assert (body.count(old), body.count(new)) in ((1, 0), (0, 1))
        outputs[driver.name] = body.replace(old, new)
    for name, body in outputs.items():
        (package / name).write_text(body)
    return {name: hashlib.sha256(body.encode()).hexdigest()
        for name, body in outputs.items()}
