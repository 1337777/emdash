"""Original kernel point recovery and Freyd whole column-input migration."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_commutative_algebra_freyd_native_column_input_comparisons.lp': ('865887d4c03a4e67f3ee6ab90a24b2fdf9104165e51f702818d21ae0356805d4',
                                                                            'production_freyd_native_column_input_comparisons.lpfragment'),
 'emdash3_2_commutative_algebra_freyd_native_column_inputs.lp': ('55d3eb508f3957ffd6db197b741404febef2eb1b054888167bb26018320fb418',
                                                                 'production_freyd_native_column_inputs.lpfragment'),
 'emdash3_2_homology_family_point_comparisons.lp': ('725ce9d5f6526c2d8b9d3cd5d44a8d7a2264b7bc84701beac1d4cb227fe991ca',
                                                    'production_homology_family_point_comparisons.lpfragment'),
 'emdash3_2_one_cat_kernel_family_point_paths.lp': ('be1013b10eee61e5c70688b66a57fa3a1e95715c0e381125c310c83b99b590d3',
                                                    'production_kernel_family_point_paths.lpfragment'),
 'examples/homology_family_point_comparisons.lp': ('9fc41d47ed2cc477be6abacb4150f4666c577105dbaf5ddeb1247e587c4eb1fa',
                                                   'production_homology_family_point_comparisons_reviewer.lpfragment')}


def finish_native_column_entry(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
