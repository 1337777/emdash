"""Pinned original Circle/WalkingEnd consumers; preserve inherited assembly boundaries."""
import hashlib
SOURCES = {'emdash3_2_circle_connectedness.lp': 'f5c76347b15a6edcd26974fdac69e1786f80252064231da85b1dfedab05c5760',
 'emdash3_2_walking_circle_extension.lp': 'a0dff6520f9ee27d7197f649f9c6517b8eb20e138a70549b72fbafc893d5828b',
 'emdash3_2_walking_circle_monodromy.lp': 'ada9edd62782110e7800e1975aeb44e0085b6999ffc5309a98bba9edf99ac60e',
 'emdash3_2_walking_circle_universality.lp': 'da35cc1e977b16724b14aeaf69807b2fdbe548952428da69dc10074e641d312a',
 'examples/circle_connectedness.lp': 'efcb6e29689d4558e932c5a944ca65017e27d0bbed25895e772d10ce6921a422',
 'examples/circle_judgmental_loop_computation.lp': 'd0158d7eea0554410b64bc198976100027aa2a1d82dd826c421c422db35d2950',
 'examples/circle_loop_space.lp': 'bcfee5a9538dd33d40c433e4cab7f7b933a37a3fff9402ffe803a790ea5c2a1a',
 'examples/walking_circle_groupoidification_extension.lp': 'eb52dc73ef926b870b7d2bb5219be0f36a21663aacf19d5eb49a00c9a15c8aff',
 'examples/walking_circle_groupoidification_monodromy.lp': '415232c0331a17c5a57a073a259f69ffd6784ce68dc706dfbaa4db4e239e4c33',
 'examples/walking_circle_groupoidification_universality.lp': 'bb21b23144cbb11bbc2c9d595ae2d6a4b600acda5f71289ba45d2cf4aec12ccc'}

def migrate_circle_consumer(name, original):
    if name not in SOURCES:
        return None
    assert hashlib.sha256(original.encode()).hexdigest()==SOURCES[name], name
    return original
