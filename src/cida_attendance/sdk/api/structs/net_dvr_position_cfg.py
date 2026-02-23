from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSITION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POSITION_CFG, [
    ('dwSize', DWORD),
    ('bySoftWorkMode', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_POSITION_CFG = struct_tagNET_DVR_POSITION_CFG
LPNET_DVR_POSITION_CFG = POINTER(struct_tagNET_DVR_POSITION_CFG)
tagNET_DVR_POSITION_CFG = struct_tagNET_DVR_POSITION_CFG
