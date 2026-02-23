from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANUALDEICING_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MANUALDEICING_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_MANUALDEICING_CFG = struct_tagNET_DVR_MANUALDEICING_CFG
LPNET_DVR_MANUALDEICING_CFG = POINTER(struct_tagNET_DVR_MANUALDEICING_CFG)
tagNET_DVR_MANUALDEICING_CFG = struct_tagNET_DVR_MANUALDEICING_CFG
