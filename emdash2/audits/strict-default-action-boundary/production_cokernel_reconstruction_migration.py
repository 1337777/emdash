"""Native whole cokernel projection/reconstruction migration; emitted LP is checked."""
from pathlib import Path
import hashlib

AUDIT = Path(__file__).resolve().parent
SOURCES = {'emdash3_2_one_cat_cokernel_family_projection_paths.lp': ('04ddd287d1b4b57e45948df939074c7e89927d50a78e46213e05fe1eacd590ba',
                                                           'production_cokernel_projection_paths.lpfragment'),
 'emdash3_2_one_cat_cokernel_family_reconstruction.lp': ('8a47a2bd5d6f04cbdf2f00a3fb5b4d3a943c1ed7b2eaa60f9c461e15bb697c30',
                                                         'production_cokernel_reconstruction.lpfragment'),
 'examples/one_cat_cokernel_family_reconstruction.lp': ('7ea46965a98e8ab535408e7eed70f8add143ef1dcd0e2e99a0fe80bf6093766e',
                                                        'production_cokernel_reconstruction_reviewer.lpfragment')}


def finish_cokernel_reconstruction(path, text):
    if path == 'emdash3_2_one_cat_adjunction_family_views.lp':
        assert hashlib.sha256(text.encode()).hexdigest() == '36fb194ded8abab1eb237507809235c3a03a08564abb677a455c30063d4ab499'
        marker = '// Sufficient congruence for the same component observation.'
        assert text.count(marker) == 1
        return text.replace(marker, (AUDIT / 'production_application_classifier_congruence.lpfragment').read_text() + '\n' + marker, 1)
    if path in SOURCES:
        pin, fragment = SOURCES[path]
        assert hashlib.sha256(text.encode()).hexdigest() == pin, path
        return (AUDIT / fragment).read_text()
    return None
