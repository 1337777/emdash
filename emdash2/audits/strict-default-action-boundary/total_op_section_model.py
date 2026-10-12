#!/usr/bin/env python3
"""Finite direction controls for total-opposite negative sections.

The native implementation still needs its independent owner/projection checks.
This reuses the pinned finite strict-2-category model from the preceding review.
"""
import hashlib
import json
from pathlib import Path
import runpy


def main():
    audit = Path(__file__).resolve().parent
    model = audit / 'mixed_family_profile_models.py'
    prior = json.loads((audit / 'mixed_family_verification.json').read_text())
    assert hashlib.sha256(model.read_bytes()).hexdigest() == prior['authoringInputs'][
        'audits/strict-default-action-boundary/mixed_family_profile_models.py']
    Finite2 = runpy.run_path(str(model))['Finite2']

    r, s = ('a', ('r',)), ('a', ('s',))
    globe = Finite2(('a', 'b'), {'r': ('a', 'b'), 's': ('a', 'b')}, [(r, s)])
    total_cells = {(target, source) for source, target in globe.cells}
    # K has p=>q, while R(K) has q=>p. Total fibre opposite reverses the
    # target 2-cell too, so X[p]=r,X[q]=s is admitted; the old bad choice is not.
    assert (s, r) in total_cells
    assert (r, s) not in total_cells
    assert (r, s) in globe.cells  # required ordinary Hom-family action

    # A genuinely varying family: E[x]=1, E[y]=C; E[p],E[q] select a,b,
    # and E[alpha] is gamma:a->b. Negative and positive section comparisons
    # are both nonidentity 2-cells; neither is inverted in Hom action.
    beta_p = ('u', ('bp',))
    beta_q = ('u', ('bq',))
    gamma_beta_p = ('u', ('bp', 'gamma'))
    delta_p = ('a', ('dp',))
    delta_q_gamma = ('a', ('gamma', 'dq'))
    category = Finite2(('u', 'a', 'b', 'v'),
                      {'bp': ('u', 'a'), 'bq': ('u', 'b'), 'gamma': ('a', 'b'),
                       'dp': ('a', 'v'), 'dq': ('b', 'v')},
                      [(gamma_beta_p, beta_q), (delta_p, delta_q_gamma)])
    hp, hq = ('u', ('bp', 'dp')), ('u', ('bq', 'dq'))
    assert (hp, hq) in category.cells and (hq, hp) not in category.cells
    assert (beta_q, gamma_beta_p) not in category.cells
    assert (delta_q_gamma, delta_p) not in category.cells
    print(json.dumps({
        'constant_fibre': {'correct_total_op_section_admitted': True,
                           'old_transpose_section_excluded': True,
                           'required_Hom_direction_exists': True},
        'varying_fibre': {'required_Hom_direction_exists': True,
                          'reverse_direction_exists': False,
                          'section_comparisons_inverted': False},
        'scope': 'finite strict 2-category direction controls, not a whole omega construction',
    }, indent=2))


if __name__ == '__main__':
    main()
