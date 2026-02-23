from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_293 import union_anon_293


class struct_tagNET_DVR_SUBSYSTEM_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_ABILITY, [
    ('bySubSystemType', BYTE),
    ('byChanNum', BYTE),
    ('byStartChan', BYTE),
    ('bySlotNum', BYTE),
    ('byRes1', BYTE * 4),
    ('struAbility', union_anon_293),
])

NET_DVR_SUBSYSTEM_ABILITY = struct_tagNET_DVR_SUBSYSTEM_ABILITY
LPNET_DVR_SUBSYSTEM_ABILITY = POINTER(struct_tagNET_DVR_SUBSYSTEM_ABILITY)
tagNET_DVR_SUBSYSTEM_ABILITY = struct_tagNET_DVR_SUBSYSTEM_ABILITY
