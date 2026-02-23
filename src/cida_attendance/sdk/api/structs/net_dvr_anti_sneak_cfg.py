from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ANTI_SNEAK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwStartCardReaderNo', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_ANTI_SNEAK_CFG = struct_tagNET_DVR_ANTI_SNEAK_CFG
LPNET_DVR_ANTI_SNEAK_CFG = POINTER(struct_tagNET_DVR_ANTI_SNEAK_CFG)
tagNET_DVR_ANTI_SNEAK_CFG = struct_tagNET_DVR_ANTI_SNEAK_CFG
