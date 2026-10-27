#!/usr/bin/env python3
"""Replay the structural parameter action and derived positive cube decoder.

Non-library qualification: this introduces the stated whole postcomposition
owner, not an inverse or an assumed tensor-closure equivalence.
"""
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
    parser.add_argument('--mode', choices=('interactions', 'decoder', 'shift', 'pre-view', 'qualification'), default='qualification')
    parser.add_argument('--assemble-only', action='store_true')
    args = parser.parse_args()
    record = json.loads((HERE / 'postcomposition_verification.json').read_text())
    for name, expected in record['artifacts'].items():
        if digest(HERE / name) != expected:
            raise SystemExit(f'postcomposition artifact drift: {name}')
    parent = subprocess.run([
        sys.executable, str(HERE / record['baseReplay']), '--mode', 'interface', '--assemble-only',
    ], cwd=REPO, capture_output=True, text=True, check=True)
    match = re.search(r'Exact retraction interface assembly verified: (.+)', parent.stdout)
    if not match:
        raise SystemExit('parent replay did not report its exact package')
    package = Path(match.group(1))
    core_path = package / 'emdash3_2.lp'
    if digest(core_path) != record['parentCoreSha256']:
        raise SystemExit('parent core differs from the reviewed insertion owner')
    core = core_path.read_text()
    for insertion in record['coreInsertions']:
        anchor = insertion['before']
        if core.count(anchor) != 1:
            raise SystemExit(f'core insertion anchor is not unique: {anchor!r}')
        fragment = insertion['fragment']
        body = (HERE / fragment).read_text() + record.get('fragmentSuffixes', {}).get(fragment, '')
        core = core.replace(anchor, body + anchor, 1)
    core_path.write_text(core)
    for name, expected in record['additionalSources'].items():
        source = ROOT / name
        if digest(source) != expected:
            raise SystemExit(f'postcomposition dependency drift: {name}')
        target = package / name
        if target.exists() and digest(target) != expected:
            raise SystemExit(f'postcomposition dependency conflicts with parent: {name}')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    for name, fragment in record['programs'].items():
        (package / name).write_bytes((HERE / fragment).read_bytes()
            + record.get('fragmentSuffixes', {}).get(fragment, '').encode())
    mode = record['modes'][args.mode]
    if input_hashes([Path(mode['target'])], package) != mode['expectedInputs']:
        raise SystemExit('postcomposition closure differs from the checked snapshot')
    print(f'Exact postcomposition {args.mode} assembly verified: {package}', flush=True)
    if args.assemble_only:
        return 0
    checker_dir = subprocess.check_output([
        sys.executable, str(REPO / 'scripts/verification-toolchain.py'), 'batch-path',
    ], cwd=REPO, text=True).strip()
    if digest(Path(checker_dir) / 'lambdapi') != record['checker']['sha256']:
        raise SystemExit('checker differs from the recorded postcomposition checks')
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
