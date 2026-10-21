"""Original homology-cover and native column projection migration; no new rules."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_commutative_algebra_freyd_column_homology_projection_paths.lp': ('04ec705fbf62140139fa8bccc38fdf458667bcf63390a75fd054c9b44381ab27',
                                                                             'production_freyd_column_projection_paths.lpfragment'),
 'emdash3_2_homology_family_point_paths.lp': ('0579c7995980dd0f32144b7630352731d37bac8ed029e12ed77fffcf5436604d',
                                              'production_homology_family_point_paths.lpfragment'),
 'emdash3_2_one_cat_homology_cover_maps.lp': ('a0095f3c140b7b47592493f04518191fea7f7e91a3ac5b16eb7071c915f48279',
                                              'production_homology_cover_maps.lpfragment'),
 'examples/freyd_native_column_comparisons.lp': ('33309b045fb40c1ea486bcd9f5f5d59297fd6c2a368219fde3d57f8853b1d786',
                                                 'production_freyd_column_comparisons_reviewer.lpfragment'),
 'examples/one_cat_homology_cover_maps.lp': ('f0cd42b21211493c3f4b458c35704ff8525cf518b975ebd1866d679c0c978949',
                                             'production_homology_cover_maps_reviewer.lpfragment')}


def finish_column_projection(path, text):
    if path not in SOURCES:
        return None
    pin, fragment = SOURCES[path]
    assert hashlib.sha256(text.encode()).hexdigest() == pin, path
    return (AUDIT / fragment).read_text()
