from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_THERMAL_PIP(Structure):
    pass

_S(struct_tagNET_DVR_THERMAL_PIP, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byPipMode', BYTE),
    ('byOverlapType', BYTE),
    ('byTransparency', BYTE),
    ('struPipRegion', NET_VCA_POLYGON),
    ('byImageFusionRatio', BYTE),
    ('byBorderFusionRatio', BYTE),
    ('byRes1', BYTE * 2),
    ('fDistance', c_float),
    ('byRes', BYTE * 632),
])

NET_DVR_THERMAL_PIP = struct_tagNET_DVR_THERMAL_PIP
LPNET_DVR_THERMAL_PIP = POINTER(struct_tagNET_DVR_THERMAL_PIP)
tagNET_DVR_THERMAL_PIP = struct_tagNET_DVR_THERMAL_PIP
