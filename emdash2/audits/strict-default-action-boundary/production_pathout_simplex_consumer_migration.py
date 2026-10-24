"""Original whole PathOut/simplex/join consumers at the migrated foundation."""
import hashlib
from production_strict_wrapper_finish import calls, rename_code, ALIASES, RENAMES
SOURCES = {'emdash3_2_dependent_simplex_code_map.lp': '2f6a8f698db8c37f595355bc926fc56811ac52277e7182c53347673a19ae4529',
 'emdash3_2_dependent_simplex_codes.lp': '4e2f8e5241c768f465295124c3d727afec007f852e2a2e8796efd5015a282a33',
 'emdash3_2_dependent_simplex_dimension4.lp': '66c7f5844b961e917746b48120b6052f359c010cd37143d16f9ecc91a7cbe3ff',
 'emdash3_2_dependent_simplex_faces.lp': '44958beaf20181d23fbcb7386a8373f5b424d92364afa7e7628037d0b0a4db45',
 'emdash3_2_join_cross_compatibility.lp': '24cb40ddcdb95c9bd437293216fa06202be6e64283b17969741b2304bf62ea29',
 'emdash3_2_join_generator_compatibility.lp': '566a2416bc9bea251fb7bee531ba3ab430cc28362194d34888b57474673dd439',
 'emdash3_2_ordinal_join_pathout_successor.lp': '8731fcafccfdfdfb427eddd2671fcbe4abdbb36aa1f1bc788ae8f187fb953e0c',
 'emdash3_2_pathout_transformation_lift.lp': '626baac13392ae3b10c25183cfa5e4c7dc01d2ec1abe31da7fa9c9125e2e09d5',
 'examples/dependent_simplex_code_map.lp': '725adb305995845cad7b48209f8cb8a274a4d2fa434919371809dfe3b73e7397',
 'examples/dependent_simplex_codes.lp': 'c03feea79c09d0680e8f7414fbcaedc48aca8b9fd1f35f4dae11ff6964aba8eb',
 'examples/dependent_simplex_dimension4.lp': '8780e795847ff0c703accb9963117c890e4eb105c5a448d5f73c50bcda606144',
 'examples/dependent_simplex_faces.lp': 'a425355b8fd62a20e652b11531a2f4aa0a707d1952f98f5c5d1b595fc7e7d1fc',
 'examples/join_cross_compatibility.lp': '7c9fc7b0bc0a1168fb089666af9adfab4a7e721ec2bac540fb0e968ccb4bb5f8',
 'examples/join_generator_compatibility.lp': 'bde40806718a3a5b7e24f7d14ec37cf2b0575b8f6e98a4df3ea29ea3e6d92a38',
 'examples/pathout_transformation_lift.lp': 'dc4b7cdc11df897d8b21539c46f1bf69ef9ab671eebdca6fa8ae87ff4d6555c7'}

def migrate_pathout_simplex_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest()==SOURCES[name], name
    text=original
    if name=='emdash3_2_join_cross_compatibility.lp':
        start=text.index('symbol join_map_extend_cross_component')
        end=text.index(';',start)+1
        header,body=text[start:end].split('≔',1)
        assert body.strip().startswith('@tdapp0_fapp0')
        text=text[:start]+header+'≔ @strict_transfor _ _ _ _\n    ('+body.strip().removesuffix(';')+');'+text[end:]
    if name=='emdash3_2_ordinal_join_pathout_successor.lp':
        text,count=calls(text,'strict_functor',3,1,lambda args,explicit:args[-1])
        assert count==1
    if name=='emdash3_2_pathout_transformation_lift.lp':
        text=text.replace('  equality-induced hom action, so the construction preserves rather than\n  collapses laxity.  One constructor-visible component beta is owned here;', '  equality-induced hom action. The whole transformation and its higher\n  action are retained. Under the conventional-lax default, the extracted\n  pre/right comparison is strict; the post/left leg remains lax.\n  One constructor-visible component beta is owned here;')
    if name=='examples/pathout_transformation_lift.lp':
        text=text.replace('  transformation retains its ordinary next hom action.', '  transformation retains its ordinary next hom action. The extracted\n  pre/right leg follows the conventional-lax default; the other\n  ordinary naturality leg is not strictified.')
    return rename_code(text, {**ALIASES, **RENAMES})
