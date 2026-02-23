from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIN_ROAM_SWITCH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIN_ROAM_SWITCH_CFG, [
    ('dwSize', DWORD),
    ('byEnableRoam', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_WIN_ROAM_SWITCH_CFG = struct_tagNET_DVR_WIN_ROAM_SWITCH_CFG
LPNET_DVR_WIN_ROAM_SWITCH_CFG = POINTER(struct_tagNET_DVR_WIN_ROAM_SWITCH_CFG)
tagNET_DVR_WIN_ROAM_SWITCH_CFG = struct_tagNET_DVR_WIN_ROAM_SWITCH_CFG
