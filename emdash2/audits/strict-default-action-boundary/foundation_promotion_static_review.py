"""Replay static migration checks; not a type/confluence/semantic certificate."""
import argparse
from collections import Counter
from dataclasses import asdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_rule_lhs import candidates, rule_commands, split_top_level, strip_comments
from generate_check_catalog import parse_checks, read_lines


def review(package):
    registry = json.loads((ROOT / 'checks.json').read_text())
    owners = [n for n in registry['core'] if n != 'emdash3_2_checks.lp']
    lhs, prior_lhs, entries, added_heads, heads = Counter(), Counter(), [], 0, []
    for name in owners:
        found, kept = candidates(package / name)
        before, prior_kept = candidates(ROOT / name)
        lhs.update(unreviewed=len(found), annotated=len(kept))
        prior_lhs.update(unreviewed=len(before), annotated=len(prior_kept))
        if found or before:
            entries.append({'file': name, 'candidate': [asdict(c) for c in found],
                            'production': [asdict(c) for c in before]})
        old = strip_comments((ROOT / name).read_text())
        new = strip_comments((package / name).read_text())
        names = lambda s: set(re.findall(r'\binjective\s+symbol\s+(\w+)', s))
        added = names(new) - names(old)
        added_heads += len(added)
        if not added:
            continue
        for line, rule in rule_commands(new):
            left, right = rule.split('↪', 1)
            left = re.sub(r'^\s*rule\s+', '', left).strip()
            parts = split_top_level(left)
            if parts and parts[0].lstrip('@') in added and all(
                    p == '_' or re.fullmatch(r"\$[A-Za-z_][\w']*", p) for p in parts[1:]):
                heads.append({'file': name, 'line': line, 'lhs': left, 'rhs': right.strip()})
    before, after, deltas = Counter(), Counter(), []
    files = registry['core'] + registry['reviewers']
    for name in files:
        a = Counter(c.first_line.split()[0] for c in parse_checks(read_lines(ROOT / name)))
        b = Counter(c.first_line.split()[0] for c in parse_checks(read_lines(package / name)))
        before.update(a)
        after.update(b)
        if a != b:
            deltas.append({'file': name, 'before': dict(a), 'after': dict(b),
                           'totalDelta': sum(b.values()) - sum(a.values())})
    return {'owners': len(owners), 'candidateLHS': dict(lhs), 'productionLHS': dict(prior_lhs),
            'unreviewedLHS': entries, 'addedInjectiveHeads': added_heads,
            'unguardedNewHeadRules': heads, 'registeredFiles': len(files),
            'beforeAssertions': dict(before), 'afterAssertions': dict(after), 'assertionDeltas': deltas}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = review(args.package.resolve())
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k not in
        ('unreviewedLHS', 'unguardedNewHeadRules', 'assertionDeltas')}))
