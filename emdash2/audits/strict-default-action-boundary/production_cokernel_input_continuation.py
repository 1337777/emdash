"""Replay the original whole cokernel-input migration at its source owners.

The LP retains the supplied annihilation cell and ordinary reconstruction
tests. Native endpoint paths are derived whole comparisons, not new cuts.
"""
from pathlib import Path
import hashlib
import re

AUDIT = Path(__file__).resolve().parent


def finish_cokernel_inputs(path, text):
    if path == 'emdash3_2_profile_action_paths.lp':
        # The public strict default proves this original statement directly.
        # Retain the descriptive PF argument for existing clients; the
        # transfor-property theorem below still uses its actual evidence.
        match = re.search(r'(?m)^symbol profile_composition_path\b.*?;', text, re.S)
        assert match and '≔' in match.group()
        replacement = (match.group().split('≔', 1)[0]
                       + '≔ @eq_refl (Hom B (@fapp0 A B F x) (@fapp0 A B F z))\n'
                       + '    (@fapp1_fapp0 A B F x z (@comp_fapp0 A x y z g f));')
        return (text[:match.start()]
                + '// Composition now follows from default strict functor action.\n'
                + '// PF remains a descriptive input for the existing public interface.\n'
                + replacement + text[match.end():])
    if path == 'emdash3_2_zero_arrow_family_action_paths.lp':
        # Keep the old ordinary-exchange congruence clause unchanged. The
        # native observation bodies use their actual fixed-evaluation action.
        marker = '// Generic Hom action of a composite'
        assert text.count(marker) == 1
        prefix, body = text.split(marker, 1)
        for pattern, replacement, expected in (
            (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat', 48),
            (r'\(Op_cat C\)', '(TotalOp_cat C)', 1),
            (r'@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at', 4),
            (r'@diagram_family_evaluation_func', '@diagram_oplax_family_evaluation_func', 6),
        ):
            body, count = re.subn(pattern, replacement, body)
            assert count == expected, (pattern, count, expected)
        return prefix + marker + body
    if path == 'examples/action_profile_profile_action_path_controls.lp':
        # Only the functor-composition negative changes with the public
        # strict default. The independent raw-transfor negative remains.
        marker = '// Profiles supply paths; they do not install cuts on a raw variable.'
        assert text.count(marker) == 1 and text.count('assertnot') == 2
        prefix, tail = text.split(marker, 1)
        return (prefix + '// Functors now preserve composition by default; the transfor\n'
                '// property still supplies a path without a raw-variable runtime cut.'
                + tail.replace('assertnot', 'assert', 1))
    if path == 'emdash3_2_one_cat_diagram_family_reconstruction.lp':
        assert 'symbol one_cat_oplax_diagram_family_reconstruction_to' not in text
        return (text + '\n'
                + (AUDIT / 'production_native_reconstruction_map_views.lpfragment').read_text()
                + '\n'
                + (AUDIT / 'production_native_reconstruction_endpoint_paths.lpfragment').read_text())
    replacements = {
        'emdash3_2_one_cat_cokernel_family_inputs.lp': (
            '597b9d0d662c4fd9f33a6b5e7c2f7171d8d8aa86ce04630926a98af65c1782e8',
            'production_cokernel_family_inputs.lpfragment'),
        'examples/one_cat_cokernel_family_inputs.lp': (
            '6e32c3289c7c9112385e99e8a11436249849362278d04278d31c4778a5d1938e',
            'production_cokernel_family_inputs_reviewer.lpfragment'),
    }
    if path in replacements:
        digest, fragment = replacements[path]
        assert hashlib.sha256(text.encode()).hexdigest() == digest, path
        return (AUDIT / fragment).read_text()
    return None
