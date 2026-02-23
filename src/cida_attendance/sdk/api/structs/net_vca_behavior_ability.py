from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_BEHAVIOR_ABILITY(Structure):
    pass

_S(struct_tagNET_VCA_BEHAVIOR_ABILITY, [
    ('dwSize', DWORD),
    ('dwAbilityType', DWORD),
    ('byMaxRuleNum', BYTE),
    ('byMaxTargetNum', BYTE),
    ('bySupport', BYTE),
    ('byRes', BYTE * 5),
    ('dwAbilityTypeEx', DWORD),
])

NET_VCA_BEHAVIOR_ABILITY = struct_tagNET_VCA_BEHAVIOR_ABILITY
LPNET_VCA_BEHAVIOR_ABILITY = POINTER(struct_tagNET_VCA_BEHAVIOR_ABILITY)
tagNET_VCA_BEHAVIOR_ABILITY = struct_tagNET_VCA_BEHAVIOR_ABILITY
