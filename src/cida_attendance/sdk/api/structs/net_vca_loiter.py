from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_LOITER(Structure):
    pass

_S(struct_tagNET_VCA_LOITER, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byres', BYTE * 1),
    ('dwLoiterDistance', DWORD),
])

NET_VCA_LOITER = struct_tagNET_VCA_LOITER
LPNET_VCA_LOITER = POINTER(struct_tagNET_VCA_LOITER)
tagNET_VCA_LOITER = struct_tagNET_VCA_LOITER
