"""Scoped native kernel/cokernel path continuation; validate emitted LP."""
from pathlib import Path
import hashlib
import re

AUDIT = Path(__file__).resolve().parent


def finish_kernel_cokernel_paths(path, text):
    if path == 'emdash3_2_one_cat_adjunction_family_views.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == '298f87061e89739884c139024432e1ec16c9e9d4ad96d720916b1248d0b905cf'
        marker = '// Congruence for a pair of Cat horizontal actions'
        assert text.count(marker) == 1
        return text.replace(marker, (AUDIT / 'production_component_view_congruence.lpfragment').read_text() + '\n' + marker, 1)
    if path == 'emdash3_2_one_cat_kernel_cokernel_family_paths.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == 'a0a3abc63bbb8948a62cce7d85e5860a9e2e6a973f910705aef58cbfe4abb3a2'
        return (AUDIT / 'production_kernel_cokernel_family_paths.lpfragment').read_text()
    counts = {
        'emdash3_2_one_cat_cokernel_family_descent.lp': (17, 3, 6, 5, 19, 3),
        'examples/one_cat_cokernel_family_descent.lp': (87, 10, 5, 2, 52, 10),
    }
    if path in counts:
        changes = (
            (r'Functor_cat(?=\s+WalkingArrow_cat\s+C\b)', 'Functor_oplax_cat'),
            (r'\(Op_cat C\)', '(TotalOp_cat C)'),
            (r'@one_cat_functor_category(?=\s+WalkingArrow_cat\s+C\b)', '@one_cat_oplax_functor_category'),
            (r'@sym_transf_tapp0_transf', '@diagram_oplax_family_map_at'),
            (r'@diagram_family_at_func', '@diagram_oplax_family_at_func'),
            (r'@diagram_family_transf', '@diagram_oplax_family_transf'),
        )
        for (pattern, replacement), expected in zip(changes, counts[path], strict=True):
            text, count = re.subn(pattern, replacement, text)
            assert count == expected, (path, pattern, count, expected)
        return text
    return None
