"""Verify completed source scopes inside a timed-out aggregate without relabeling it.

Version-specific audit evidence only. The aggregate receipt remains incomplete;
only fully started/ended dependency closures are accepted. No runner changes.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

AUDIT = Path(__file__).resolve().parent
ROOT = AUDIT.parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_registry import input_hashes

CHECKER_PIN = 'db4f7809961b8c107247613067fb567491fb0b84'
CHECKER_SHA = '5c82cca90847fb5cc7726f52b3c6b8f2df3a89685abecac48285ae676db6bb69'
SEMANTIC_FILES = (
    'src/handle/compile.ml', 'src/common/debug.ml',
    'src/handle/query.ml', 'src/handle/command.ml',
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_completed_scopes(receipt_id, targets, package, *, log_lines=None):
    receipt_path = ROOT / 'logs/check-runs' / (receipt_id + '.json')
    data = json.loads(receipt_path.read_text())
    assert data['outcome'] == 'timeout' and not data['compileObject']
    assert data['checker']['sha256'] == CHECKER_SHA
    assert '--no-sr-check' not in data['settings']['flags']
    log_path = ROOT / data['log']
    assert sha(log_path) == data['logSha256']
    lines = log_path.read_text().splitlines() if log_lines is None else log_lines
    checker_source = ROOT / 'tmp/probes/checker_rollback_memory/source'
    code = {}
    for name in SEMANTIC_FILES:
        path = checker_source / name
        pinned = subprocess.check_output(['git', 'show', CHECKER_PIN + ':' + name], cwd=checker_source)
        assert path.read_bytes() == pinned, name
        code[name] = hashlib.sha256(pinned).hexdigest()
    package = package.resolve()
    starts, ends = {}, {}
    for number, line in enumerate(lines, 1):
        for prefix, table in (('Start checking "', starts), ('End checking "', ends)):
            if line.startswith(prefix) and line.endswith('"'):
                path = Path(line[len(prefix):-1])
                if path.is_relative_to(package):
                    name = str(path.relative_to(package))
                    assert name not in table, ('duplicate source marker', name)
                    table[name] = number
    assert data['target'] not in ends, 'Do not relabel the unfinished aggregate'
    qualified_inputs, completed_files, scopes = {}, {}, {}
    for target in targets:
        assert target in starts and target in ends, ('incomplete target', target)
        assert starts[target] < ends[target]
        inputs = input_hashes([Path(target)], root=package)
        for name, digest in inputs.items():
            assert data['inputs'].get(name) == digest, ('source drift', name)
            stored = ROOT / data['inputStore'] / digest
            assert sha(stored) == digest
            qualified_inputs[name] = digest
            if name.endswith('.lp'):
                assert name in starts and name in ends, ('incomplete dependency', name)
                assert starts[name] < ends[name] <= ends[target], ('late dependency', target, name)
                completed_files[name] = {'sha256': digest, 'startLogLine': starts[name], 'endLogLine': ends[name]}
        scopes[target] = {
            'startLogLine': starts[target], 'endLogLine': ends[target],
            'sourceCount': sum(n.endswith('.lp') for n in inputs),
            'closureSha256': hashlib.sha256(json.dumps(inputs, sort_keys=True).encode()).hexdigest(),
        }
    return {
        'status': ('completed-source-scope evidence; aggregate receipt remains timeout' if log_lines is None else 'diagnostic modified-log result only; not qualification evidence'),
        'logSource': 'receipt log' if log_lines is None else 'modified diagnostic lines',
        'verifierSha256': sha(Path(__file__)),
        'aggregateReceipt': receipt_id, 'aggregateOutcome': data['outcome'],
        'aggregateReceiptSha256': sha(receipt_path), 'log': data['log'],
        'logSha256': data['logSha256'], 'checker': data['checker'],
        'checkerSourcePin': CHECKER_PIN, 'checkerCompletionCodeSha256': code,
        'justification': 'compile.ml emits End checking after stream_iter has returned from every Command.handle. The iterator propagates failures; query assertions fail fatally, unfinished definitions fail, and rule handling checks subject reduction. No final aggregate success is inferred.',
        'completedScopes': scopes, 'completedFiles': completed_files,
        'qualifiedInputSha256': qualified_inputs,
    }


if __name__ == '__main__':
    receipt_id, target_json, package, output = sys.argv[1:]
    targets = json.loads(Path(target_json).read_text())['finishedTopLevelScopes']
    result = verify_completed_scopes(receipt_id, targets, Path(package))
    Path(output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'aggregate': receipt_id, 'completedScopes': len(result['completedScopes']),
                      'completedSourceFiles': len(result['completedFiles']),
                      'aggregateStillIncomplete': True}))
