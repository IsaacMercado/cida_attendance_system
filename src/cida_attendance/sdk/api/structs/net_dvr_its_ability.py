from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ITS_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_ITS_ABILITY, [
    ('dwSize', DWORD),
    ('dwAbilityType', DWORD),
    ('byMaxRuleNum', BYTE),
    ('byMaxTargetNum', BYTE),
    ('byRes', BYTE * 10),
])

NET_DVR_ITS_ABILITY = struct_tagNET_DVR_ITS_ABILITY
LPNET_DVR_ITS_ABILITY = POINTER(struct_tagNET_DVR_ITS_ABILITY)
tagNET_DVR_ITS_ABILITY = struct_tagNET_DVR_ITS_ABILITY
