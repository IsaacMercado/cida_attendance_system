from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_REGION_LIST(Structure):
    pass

_S(struct_tagNET_DVR_REGION_LIST, [
    ('dwSize', DWORD),
    ('byNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struPolygon', NET_VCA_POLYGON * 8),
    ('byRes2', BYTE * 20),
])

NET_DVR_REGION_LIST = struct_tagNET_DVR_REGION_LIST
LPNET_DVR_REGION_LIST = POINTER(struct_tagNET_DVR_REGION_LIST)
tagNET_DVR_REGION_LIST = struct_tagNET_DVR_REGION_LIST
