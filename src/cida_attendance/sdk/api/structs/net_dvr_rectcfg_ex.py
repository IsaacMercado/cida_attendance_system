from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECTCFG_EX(Structure):
    pass

_S(struct_tagNET_DVR_RECTCFG_EX, [
    ('dwXCoordinate', DWORD),
    ('dwYCoordinate', DWORD),
    ('dwWidth', DWORD),
    ('dwHeight', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_RECTCFG_EX = struct_tagNET_DVR_RECTCFG_EX
LPNET_DVR_RECTCFG_EX = POINTER(struct_tagNET_DVR_RECTCFG_EX)
tagNET_DVR_RECTCFG_EX = struct_tagNET_DVR_RECTCFG_EX
