from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FILTER(Structure):
    pass

_S(struct_tagNET_DVR_FILTER, [
    ('byEnable', BYTE),
    ('byMode', BYTE),
    ('byFrameBeginPos', BYTE),
    ('byRes', BYTE),
    ('byFilterText', BYTE * 16),
    ('byRes2', BYTE * 12),
])

NET_DVR_FILTER = struct_tagNET_DVR_FILTER
LPNET_DVR_FILTER = POINTER(struct_tagNET_DVR_FILTER)
tagNET_DVR_FILTER = struct_tagNET_DVR_FILTER
