from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_AUXAREA(Structure):
    pass

_S(struct_tagNET_DVR_AUXAREA, [
    ('dwAreaType', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struPolygon', NET_VCA_POLYGON),
    ('byRes2', BYTE * 16),
])

NET_DVR_AUXAREA = struct_tagNET_DVR_AUXAREA
LPNET_DVR_AUXAREA = POINTER(struct_tagNET_DVR_AUXAREA)
tagNET_DVR_AUXAREA = struct_tagNET_DVR_AUXAREA
