#!/usr/bin/env python3
"""Replay derived reverse geometric maps and their whole-family consumers."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from check_registry import input_hashes  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('maps', 'readback', 'qualification', 'inverse-review', 'reindex', 'reflection', 'evaluation-pending'), default='qualification')
    parser.add_argument('--assemble-only', action='store_true')
    args = parser.parse_args()
    record = json.loads((HERE / 'reverse_verification.json').read_text())
    for name, expected in record['artifacts'].items():
        if digest(HERE / name) != expected:
            raise SystemExit(f'reverse-construction artifact drift: {name}')
    parent = subprocess.run([
        sys.executable, str(HERE / record['baseReplay']), '--mode', 'qualification', '--assemble-only',
    ], cwd=REPO, capture_output=True, text=True, check=True)
    match = re.search(r'Exact postcomposition qualification assembly verified: (.+)', parent.stdout)
    if not match:
        raise SystemExit('parent replay did not report its exact package')
    package = Path(match.group(1))
    mode = record['modes'][args.mode]
    for insertion in record['ownerInsertions'] + mode.get('extraOwnerInsertions', []):
        owner = package / insertion['owner']
        if digest(owner) != insertion['parentSha256']:
            raise SystemExit(f'parent owner drift: {insertion["owner"]}')
        text = owner.read_text()
        anchor = insertion['before']
        if text.count(anchor) != 1:
            raise SystemExit(f'insertion anchor is not unique: {anchor!r}')
        fragment = insertion['fragment']
        body = (HERE / fragment).read_text() + record.get('fragmentSuffixes', {}).get(fragment, '')
        owner.write_text(text.replace(anchor, body + anchor, 1))
    for name, fragment in record['programs'].items():
        (package / name).write_bytes((HERE / fragment).read_bytes()
            + record.get('fragmentSuffixes', {}).get(fragment, '').encode())
    if input_hashes([Path(mode['target'])], package) != mode['expectedInputs']:
        raise SystemExit('reverse closure differs from the recorded input snapshot')
    print(f'Exact reverse {args.mode} assembly verified: {package}', flush=True)
    if args.assemble_only:
        return 0
    checker_dir = subprocess.check_output([
        sys.executable, str(REPO / 'scripts/verification-toolchain.py'), 'batch-path',
    ], cwd=REPO, text=True).strip()
    if digest(Path(checker_dir) / 'lambdapi') != record['checker']['sha256']:
        raise SystemExit('checker differs from the recorded reverse-map checks')
    env = os.environ.copy()
    env.update({
        'PATH': checker_dir + os.pathsep + env.get('PATH', ''),
        'OCAMLRUNPARAM': 'o=20,v=1024', 'EMDASH_LAMBDAPI_WARNINGS': '1',
        'EMDASH_LAMBDAPI_FLAGS': '--too-long=0.5', 'EMDASH_LP_MEMORY_MIB': '2048',
        'EMDASH_LP_FILE_MIB': '64', 'EMDASH_LP_RESOURCE_BACKEND': 'auto',
    })
    return subprocess.run([
        sys.executable, str(ROOT / 'scripts/run_lambdapi.py'), '--no-colors', '--quiet',
        '--timeout-ms', str(mode['timeoutMs']), '--package-root', str(package), mode['target'],
    ], cwd=REPO, env=env).returncode


if __name__ == '__main__':
    raise SystemExit(main())
