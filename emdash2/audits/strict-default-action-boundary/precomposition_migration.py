#!/usr/bin/env python3
"""Recover the actual ambient precomposition owner from family pullback.

NON-LIBRARY. Relocate existing prerequisite declarations/comparisons only;
keep the later whole-mapping and Homd profile obligations visible.
"""
import hashlib
import json
from pathlib import Path
import re
import runpy


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    runpy.run_path(str(audit / 'mixed_family_migration.py'), run_name='__main__')
    previous = root / 'tmp/probes/strict_default_mixed_family'
    prior = json.loads((audit / 'mixed_family_verification.json').read_text())
    source = (previous / 'emdash3_2.lp').read_text()
    assert hashlib.sha256(source.encode()).hexdigest() == prior['outputs']['emdash3_2.lp']

    def replace(old, new):
        nonlocal source
        assert source.count(old) == 1, (old, source.count(old))
        source = source.replace(old, new)

    def move(pattern, name):
        matches = list(re.finditer(pattern, source))
        assert len(matches) == 1, (name, len(matches))
        code = matches[0][0]
        replace(code, '// Prerequisite moved before the fixed-whiskering owner: ' + name + '.\n')
        return code

    prerequisites = []
    for name in ('Pullback_catd', 'Pullback_catd_func', 'Const_catd'):
        prerequisites.append(move(r'(?m)^injective symbol ' + name + r'\b[\s\S]*?;\n', name))
    prerequisites.append(move(
        r'(?m)^rule @fapp0 _ _\n      \(@Pullback_catd_func[\s\S]*?;\n',
        'family-pullback object projection'))
    prerequisites.append(move(
        r'(?m)^rule @Pullback_catd \$A \$B \(@Const_catd \$B \$C\) \$F[\s\S]*?;\n',
        'constant-family pullback'))
    prerequisites.append(move(
        r'(?m)^rule @fapp0 \$K Cat_cat \(@Const_catd \$K \$A\) \$_ ↪ \$A;\n',
        'constant-family fibre'))

    # Reuse the direct whole/object/next-Hom comparisons. They stay proof-time
    # comparisons; no equality term becomes an argument of an operation.
    early = source[:source.index('injective symbol Pi_func (K : Cat)')]
    comparisons = [m[0] for m in re.finditer(r'(?m)^unif_rule\b[\s\S]*?↪\s*\[[\s\S]*?\];\n', early)
                   if 'Const_catd' in m[0] and 'Terminal_cat' in m[0]
                   and '@Pi_cat' not in m[0]
                   and ('≡ Obj (Functor_cat' in m[0] or '≡ Functor_cat' in m[0]
                        or '≡ @Transf_cat' in m[0])]
    assert len(comparisons) == 4, len(comparisons)
    for i, code in enumerate(comparisons):
        replace(code, '// Constant-section comparison moved before fixed whiskering.\n')
        prerequisites.append(code)

    component = move(
        r'(?m)^// Constant-family section evaluation follows ordinary functor application\.\n'
        r'// lhs-audit:[\s\S]*?^rule @tapp0_fapp0\n[\s\S]*?;\n',
        'constant-section component')
    prerequisites.append(component)
    anchor = '// Curried postcomposition in Cat, used to build constructor pipelines.'
    replace(anchor, '// Existing family-reindexing prerequisites for fixed ambient whiskering.\n'
            + '\n'.join(prerequisites) + '\n' + anchor)

    m = re.search(r'(?m)^symbol comp_cat_con_func\b[\s\S]*?;\n', source)
    assert m
    declaration = m[0].split('≔', 1)[0]
    replace(m[0], declaration + '''≔ @fapp1_func (Catd_cat Y) (Catd_cat X)
    (@Pullback_catd_func X Y F)
    (@Const_catd Y Terminal_cat) (@Const_catd Y Z);
''')
    old_projection = '''// Applying the source action of the internal mapping constructor precomposes.
rule @fapp0 _ _
      (@tapp0_fapp0 _ _ _ _ $Z
        (@fapp1_fapp0 _ _ Functor_cat_func $Y $X $F)) $G
  ↪ @comp_cat_fapp0 $X $Y $Z $G $F;
'''
    marker = '// Canonical constant-section pullback computation.\n'
    replace(old_projection, marker)
    controls = (audit / 'precomposition_controls.lpfragment').read_text()
    no_join = source.replace(marker, controls + '\n')
    source = source.replace(marker,
        (audit / 'precomposition_rule.lpfragment').read_text() + '\n' + controls + '\n')

    output = root / 'tmp/probes/strict_default_precomposition'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'emdash3_2.lp').write_text(source)
    for filename, text in (('owner_prefix.lp', source), ('no_projection_join.lp', no_join)):
        boundary = re.search(r'(?m)^// 8a\..*$', text)
        assert boundary
        (output / filename).write_text(text[:boundary.start()])
    end = '// Mixed-variance hom family for two sections of a displayed family.'
    (output / 'mixed_prefix.lp').write_text(source[:source.index(end)])
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    files = ('precomposition_migration.py', 'precomposition_rule.lpfragment',
             'precomposition_controls.lpfragment')
    manifest = {
        'status': 'non-library owner-position recovery; whole mapping and Homd remain open',
        'mixedInputSha256': prior['outputs']['emdash3_2.lp'],
        'relocatedPrerequisites': [hashlib.sha256(c.encode()).hexdigest() for c in prerequisites],
        'authoringInputs': {str((audit / f).relative_to(root)):
                           hashlib.sha256((audit / f).read_bytes()).hexdigest() for f in files},
        'outputs': {f: hashlib.sha256((output / f).read_bytes()).hexdigest()
                    for f in ('emdash3_2.lp', 'owner_prefix.lp', 'no_projection_join.lp',
                              'mixed_prefix.lp', 'lambdapi.pkg')},
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted derived ambient precomposition at its actual owner.')


if __name__ == '__main__':
    main()
