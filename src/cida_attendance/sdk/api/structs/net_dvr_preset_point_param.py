from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_PRESET_POINT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PRESET_POINT_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwPTZPresetCmd', DWORD),
    ('struVcaPoint', NET_VCA_POINT),
    ('dwPresetIndex', DWORD),
    ('wZoomCoordinate', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_PRESET_POINT_PARAM = struct_tagNET_DVR_PRESET_POINT_PARAM
LPNET_DVR_PRESET_POINT_PARAM = POINTER(struct_tagNET_DVR_PRESET_POINT_PARAM)
tagNET_DVR_PRESET_POINT_PARAM = struct_tagNET_DVR_PRESET_POINT_PARAM
