from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_CENTER_POINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CENTER_POINT_CFG, [
    ('dwSize', DWORD),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 512),
])

NET_DVR_CENTER_POINT_CFG = struct_tagNET_DVR_CENTER_POINT_CFG
LPNET_DVR_CENTER_POINT_CFG = POINTER(struct_tagNET_DVR_CENTER_POINT_CFG)
tagNET_DVR_CENTER_POINT_CFG = struct_tagNET_DVR_CENTER_POINT_CFG
