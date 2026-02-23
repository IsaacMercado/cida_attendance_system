from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPGRADE_STATE(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_STATE, [
    ('dwProgress', DWORD),
    ('byState', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_UPGRADE_STATE = struct_tagNET_DVR_UPGRADE_STATE
LPNET_DVR_UPGRADE_STATE = POINTER(struct_tagNET_DVR_UPGRADE_STATE)
tagNET_DVR_UPGRADE_STATE = struct_tagNET_DVR_UPGRADE_STATE
