from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BGA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BGA_INFO, [
    ('byBga', BYTE),
    ('byBgaState', BYTE),
    ('wBgaPercentage', WORD),
    ('byRes', BYTE * 4),
])

NET_DVR_BGA_INFO = struct_tagNET_DVR_BGA_INFO
LPNET_DVR_BGA_INFO = POINTER(struct_tagNET_DVR_BGA_INFO)
tagNET_DVR_BGA_INFO = struct_tagNET_DVR_BGA_INFO
