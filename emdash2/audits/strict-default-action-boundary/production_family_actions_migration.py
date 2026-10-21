"""Native whole square and kernel/cokernel/homology family-map migration."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_groupoidal_closure.lp': ('7aa149dd5c55fee1bebd770e401973ba4e6e8e22f94fe06de668ced12add3f40',
                                     'production_groupoidal_closure.lpfragment'),
 'emdash3_2_one_cat_arrow_family_maps.lp': ('13966a64eb23c6250664d90ad93b4431c780f5389bf0d00fbd6d54cb637c71a7',
                                            'production_arrow_family_maps.lpfragment'),
 'emdash3_2_one_cat_homology_family_maps.lp': ('47558e903ecab0fe490b1b6f658dcc671ac53e64bdfd0d6f90d3445f51505723',
                                               'production_homology_family_maps.lpfragment'),
 'emdash3_2_one_cat_kernel_cokernel_family_maps.lp': ('c9a48b84bb63440ff7a895aec18d138861621cf492bc34cbeeb638e2adeed8a5',
                                                      'production_kernel_cokernel_family_maps.lpfragment'),
 'examples/functor_category_unit_views.lp': ('c461241123df60f3904e000362286844701e845685e5d974da97cab4360bb99a',
                                             'production_reviewer_functor_category_unit_views.lpfragment'),
 'examples/one_cat_homology_family_maps.lp': ('50148d9ded2fe7bf82627c46c6c92d460100a71ee39bf889e966905bc25d75a7',
                                              'production_homology_family_maps_reviewer.lpfragment')}


def finish_family_actions(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
