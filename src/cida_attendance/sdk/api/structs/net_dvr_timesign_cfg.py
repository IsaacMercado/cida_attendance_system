from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TIMESIGN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TIMESIGN_CFG, [
    ('dwSize', DWORD),
    ('byCustomSetTimeSign', BYTE * 32),
    ('byRes', BYTE * 96),
])

NET_DVR_TIMESIGN_CFG = struct_tagNET_DVR_TIMESIGN_CFG
LPNET_DVR_TIMESIGN_CFG = POINTER(struct_tagNET_DVR_TIMESIGN_CFG)
tagNET_DVR_TIMESIGN_CFG = struct_tagNET_DVR_TIMESIGN_CFG
