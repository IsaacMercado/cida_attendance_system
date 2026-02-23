from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIRTUAL_SCREEN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIRTUAL_SCREEN_CFG, [
    ('dwSize', DWORD),
    ('dwResolution', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_VIRTUAL_SCREEN_CFG = struct_tagNET_DVR_VIRTUAL_SCREEN_CFG
LPNET_DVR_VIRTUAL_SCREEN_CFG = POINTER(struct_tagNET_DVR_VIRTUAL_SCREEN_CFG)
tagNET_DVR_VIRTUAL_SCREEN_CFG = struct_tagNET_DVR_VIRTUAL_SCREEN_CFG
