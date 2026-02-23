from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SATELLITETIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SATELLITETIME_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE),
    ('wTimeInterval', WORD),
    ('byRes1', BYTE * 124),
])

NET_DVR_SATELLITETIME_CFG = struct_tagNET_DVR_SATELLITETIME_CFG
LPNET_DVR_SATELLITETIME_CFG = POINTER(struct_tagNET_DVR_SATELLITETIME_CFG)
tagNET_DVR_SATELLITETIME_CFG = struct_tagNET_DVR_SATELLITETIME_CFG
