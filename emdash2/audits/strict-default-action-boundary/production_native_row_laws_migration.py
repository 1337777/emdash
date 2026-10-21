"""Replay original whole zero, short-exact and kernel-restriction laws."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_one_cat_zero_family_paths.lp': ('55b63aca794296f729907f739b3c9084fe8c88700adc0463afefbc881dce4dbd',
                                            'production_zero_family_paths.lpfragment'),
 'emdash3_2_one_cat_short_exact_families.lp': ('c0ecb55e418e35e6215616197a94ed4b575535709590ca824f6b8f42c23c78f4',
                                               'production_short_exact_families.lpfragment'),
 'emdash3_2_one_cat_kernel_family_restriction_paths.lp': ('9b386b603bd09e9fc9b78d10af543b4aa51bdd5226a613b662325dc13aed4a25',
                                                          'production_kernel_family_restriction_paths.lpfragment'),
 'examples/one_cat_short_exact_families.lp': ('cda852f0a4946522f33d274b857047ffe1e0f2ccc25f6919c2bce8e67801dfbd',
                                              'production_short_exact_families_reviewer.lpfragment')}


def finish_native_row_laws(path, text):
    if path == 'emdash3_2_one_cat_adjunction_family_views.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == '4ae5402060b5ba8d8575b5f3a7a7215b6ed3e73da67b06749963e750c3c04d5a'
        old = """unif_rule @comp_fapp0 Cat_cat $B $L $R $G
    (@hom_postcomp_fapp0 Cat_cat Cat_cat (@id Cat_cat Cat_cat) $B $C $L $F $A)
  ≡ @comp_fapp0 Cat_cat $B $C $R (@comp_fapp0 Cat_cat $C $L $R $G $F) $A
  ↪ [ tt ≡ tt ];"""
        assert text.count(old) == 1
        text = text.replace(old, (AUDIT / 'production_complete_outer_post_comparison.lpfragment').read_text().rstrip(), 1)
        marker = '// Companion for represented precomposition of a visible composite.'
        assert text.count(marker) == 1
        text = text.replace(marker, (AUDIT / 'production_prepost_composite_comparison.lpfragment').read_text() + '\n' + marker, 1)
        text = text.replace('The eight comparison helpers preserve', 'The comparison helpers preserve', 1)
        text = text.replace('// Associativity where the inner composite retains its represented owner.',
            '// Associativity with represented inner postcomposition. Compare whole\n'
            '// composites before their potentially different intermediate categories.', 1)
        return text
    if path in SOURCES:
        pin, fragment = SOURCES[path]
        assert hashlib.sha256(text.encode()).hexdigest() == pin, path
        return (AUDIT / fragment).read_text()
    return None
