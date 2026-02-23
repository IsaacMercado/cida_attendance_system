from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QOSPARAM(Structure):
    pass

_S(struct_tagNET_DVR_QOSPARAM, [
    ('wMaxBitUL', WORD),
    ('wMaxBitDL', WORD),
    ('byTrafficClass', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_QOSPARAM = struct_tagNET_DVR_QOSPARAM
LPNET_DVR_QOSPARAM = POINTER(struct_tagNET_DVR_QOSPARAM)
tagNET_DVR_QOSPARAM = struct_tagNET_DVR_QOSPARAM
