from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwMultiDoorGroup', (DWORD * 8) * 8),
    ('byRes2', BYTE * 64),
])

NET_DVR_MULTI_DOOR_INTERLOCK_CFG = struct_tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG
LPNET_DVR_MULTI_DOOR_INTERLOCK_CFG = POINTER(struct_tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG)
tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG = struct_tagNET_DVR_MULTI_DOOR_INTERLOCK_CFG
