#!/usr/bin/env python3
"""Emit the identity-only Homd core and derived public FF interface; no checker."""
import hashlib
import json
from pathlib import Path
import re


def main():
    audit = Path(__file__).resolve().parent
    root = audit.parents[1]
    prior = json.loads((audit / 'cart_action_verification.json').read_text())
    donor = root / 'tmp/probes/strict_default_cart_action/emdash3_2.lp'
    source = donor.read_text()
    digest = lambda data: hashlib.sha256(data).hexdigest()
    assert digest(source.encode()) == prior['outputs']['emdash3_2.lp']
    names = ('homd_identity_core.lpfragment', 'homd_identity_ladder.lpfragment',
             'homd_identity_controls.lpfragment', 'homd_identity_relative_boundary.lpfragment')
    fragments = {n: (audit / n).read_text() for n in names}
    leaf_path = audit / 'homd_identity_leaf.lpfragment'
    leaf = re.search(r'(?m)^injective symbol homd_\b[\s\S]*?;\n', source)
    assert leaf is not None
    source = source[:leaf.start()] + leaf_path.read_text() + source[leaf.end():]
    start = source.index('// `homd_int` is a syntactic constructor package:')
    end = source.index('// 13. Dependent-hom projections and covariant fibre transport', start)
    end = source.rfind('// -------------------------------------------------------------------------------------------------', start, end)
    source = source[:start] + fragments[names[0]] + '\n\n' + source[end:]
    start = source.index('/*\n  Internal dependent-hom projection cascade:')
    end = source.index('// NON-LIBRARY: full telescope consumers of the structural Q/Homd candidate.', start)
    source = source[:start] + fragments[names[1]] + '\n\n' + source[end:]
    # These old downstream identity aliases now have their owners above.
    for name in ('homd_id_src_sec', 'homd_id_tgt_func'):
        matches = list(re.finditer(r'(?m)^symbol ' + name + r'\b[\s\S]*?;\n', source))
        # Only the old defined compatibility alias is removed; the new
        # primitive projection keeps the predecessor's non-injective profile.
        old = [m for m in matches if '≔' in m[0]]
        assert len(old) == 1, (name, len(old))
        m = old[0]
        source = source[:m.start()] + '// ' + name + ' is owned by the identity ladder above.\n' + source[m.end():]
    marker = '// NON-LIBRARY: full telescope consumers of the structural Q/Homd candidate.'
    interface = source[:source.index(marker)]
    controls = fragments[names[2]]
    # Preserve the former generic-FF reductions as a separate diagnostic.
    # The selected identity milestone does not require those stronger runtime
    # observations; its own whole ladder is checked in the migrated source.
    legacy_boundary = source[:source.index('// 14. Section action over dependent homs')]
    legacy_controls = (audit / 'q_homd_controls.lpfragment').read_text()
    assert source.count(legacy_controls) == 1
    source = source.replace(legacy_controls, controls)
    targets = {
        'full_source.lp': source,
        'interface.lp': interface,
        'identity_controls.lp': interface + '\n' + controls,
        'relative_boundary.lp': interface + '\n' + controls + '\n' + fragments[names[3]],
        'legacy_ladder_boundary.lp': legacy_boundary,
        'selected_prefix.lp': source[:source.index('// 14. Section action over dependent homs')],
    }
    first_projection = '''rule @tapp0_fapp0 _ Cat_cat _ _ $x (@homd_id_int $K $E)
  ↪ @homd_id_src_func $K $E $x;'''
    assert targets['identity_controls.lp'].count(first_projection) == 1
    targets['without_identity_projection.lp'] = targets['identity_controls.lp'].replace(first_projection, '')
    output = root / 'tmp/probes/homd_identity'
    output.mkdir(parents=True, exist_ok=True)
    for name, content in targets.items():
        (output / name).write_text(content)
    (output / 'lambdapi.pkg').write_bytes((root / 'lambdapi.pkg').read_bytes())
    manifest = {
        'status': 'non-library identity-core ownership candidate; relative computation and whole Q/lift unqualified',
        'inputSha256': prior['outputs']['emdash3_2.lp'],
        'authoringInputs': {str(p.relative_to(root)): digest(p.read_bytes())
                           for p in (Path(__file__), leaf_path, *(audit / n for n in names))},
        'outputs': {name: digest((output / name).read_bytes())
                    for name in (*targets, 'lambdapi.pkg')},
        'ownership': 'primitive identity root/ladder with an early defined identity leaf; relative root/upper ladder are definitions, and relative fixed-endpoint homd_ substitutes FF[y] into the identity leaf',
    }
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Emitted identity-core Homd and defined relative interface; Lambdapi not run.')


if __name__ == '__main__':
    main()
