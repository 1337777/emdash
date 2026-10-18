#!/usr/bin/env python3
"""Read-only structural inventory of the emitted migration and its source pin.

This is a review aid, not an LP parser, termination check or semantic audit.
It inventories production sources in the migration manifest, excluding old
scratch outputs and reviewer assertions. It never invokes the checker.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_rule_lhs import split_top_level, strip_comments

START = re.compile(r'(?m)^(?:(?:protected|private|opaque|injective|constant|sequential)\s+)*(symbol|rule|unif_rule)\b')


def commands(path):
    source = strip_comments(path.read_text())
    result = []
    for match in START.finditer(source):
        depth = 0
        quoted = False
        end = match.start()
        while end < len(source):
            char = source[end]
            if char == '"' and (end == 0 or source[end - 1] != '\\'):
                quoted = not quoted
            if not quoted:
                depth += (char in '([{') - (char in ')]}')
                if char == ';' and depth == 0:
                    break
            end += 1
        assert end < len(source), (path, match.start())
        body = source[match.start():end + 1]
        result.append({'kind': match[1], 'line': source.count('\n', 0, match.start()) + 1,
                       'text': body, 'normalized': ' '.join(body.split())})
    return result


def head(term):
    parts = split_top_level(term.strip())
    return parts[0].removeprefix('@') if parts else ''


def maximum_depth(text):
    depth = maximum = 0
    for char in text:
        depth += (char in '([{') - (char in ')]}')
        maximum = max(maximum, depth)
    return maximum


def main():
    out = ROOT / 'tmp/probes/production_owner_migration'
    manifest = json.loads((out / 'manifest.json').read_text())
    names = sorted({'emdash3_2.lp', 'emdash3_2_gray_profiles.lp'} |
                   {n for n in manifest['originalDependencyInputs']
                    if n.startswith('emdash3_2') and n.endswith('.lp')})
    sources = {}
    declarations = {'baseline': {}, 'migrated': {}}
    for name in names:
        sources[name] = {}
        for profile, directory in [('baseline', 'baseline_package'), ('migrated', 'package')]:
            path = out / directory / name
            cs = commands(path)
            sources[name][profile] = cs
            for c in cs:
                if c['kind'] == 'symbol':
                    symbol = re.search(r'\bsymbol\s+(\S+)', c['text'])[1]
                    declarations[profile][symbol] = {
                        'file': name, 'line': c['line'],
                        'primitive': '≔' not in c['text'],
                        'opaqueDefinition': c['text'].startswith('opaque '),
                    }
    new = set(declarations['migrated']) - set(declarations['baseline'])
    comparisons, expansions, folds, file_stats = [], [], [], []
    for name, profiles in sources.items():
        previous = Counter(c['normalized'] for c in profiles['baseline'])
        changed = []
        for c in profiles['migrated']:
            if previous[c['normalized']]:
                previous[c['normalized']] -= 1
            else:
                changed.append(c)
        counts = {p: dict(Counter(c['kind'] for c in cs)) for p, cs in profiles.items()}
        file_stats.append({'file': name, **counts,
                           'changedOrAdded': dict(Counter(c['kind'] for c in changed)),
                           'sha256': {p: hashlib.sha256((out / d / name).read_bytes()).hexdigest()
                                      for p, d in [('baseline', 'baseline_package'), ('migrated', 'package')]}})
        for c in changed:
            if c['kind'] == 'unif_rule':
                left, residual = c['text'].removeprefix('unif_rule').split('↪', 1)
                first, second = left.split('≡', 1)
                comparisons.append({'file': name, 'line': c['line'],
                    'heads': [head(first), head(second)], 'characters': len(c['normalized']),
                    'patternDepth': maximum_depth(left), 'residualCharacters': len(residual),
                    'rule': c['normalized']})
            if c['kind'] == 'rule':
                for clause in re.split(r'\bwith\s+', c['text'].removeprefix('rule')):
                    if '↪' not in clause:
                        continue
                    lhs, rhs = clause.removesuffix(';').split('↪', 1)
                    lhs_head, rhs_head = head(lhs), head(rhs)
                    args = split_top_level(lhs)[1:]
                    info = {'file': name, 'line': c['line'], 'head': lhs_head,
                            'rhsHead': rhs_head, 'patternDepth': maximum_depth(lhs),
                            'rule': ' '.join(clause.split())}
                    decl = declarations['migrated'].get(lhs_head, {})
                    if decl.get('primitive') and all(re.fullmatch(r'\$[^\s()\[\]{}]+|_', a) for a in args):
                        expansions.append({**info, 'headIntroducedByMigration': lhs_head in new})
                    if rhs_head in new and declarations['migrated'][rhs_head]['primitive']:
                        folds.append(info)
    result = {'scope': 'Corresponding production files in the current migration manifest; heuristic structural review only',
              'sourcePin': manifest['sourcePin'], 'files': file_stats,
              'newDeclarations': {n: declarations['migrated'][n] for n in sorted(new)},
              'changedComparisons': sorted(comparisons, key=lambda x: -x['characters']),
              'changedPrimitiveHeadExpansions': expansions,
              'changedRulesReturningNewPrimitive': sorted(folds, key=lambda x: -x['patternDepth'])}
    (out / 'normalization_inventory.json').write_text(json.dumps(result, indent=2) + '\n')
    for profile in ['baseline', 'migrated']:
        totals = Counter()
        for f in file_stats:
            totals.update(f[profile])
        print(profile, len(names), 'production files', dict(totals))
    print('changed comparisons', len(comparisons), 'new declarations', len(new))
    print('changed generic primitive-head expansions', len(expansions))
    print('rules returning new primitives', len(folds))


if __name__ == '__main__':
    main()
