from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_PTZ_CRUISE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_CRUISE_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwPTZCruiseCmd', DWORD),
    ('struVcaPoint', NET_VCA_POINT),
    ('wCruiseRoute', WORD),
    ('wCruisePoint', WORD),
    ('wInput', WORD),
    ('wZoomCoordinate', WORD),
    ('byRes', BYTE * 32),
])

NET_DVR_PTZ_CRUISE_PARAM = struct_tagNET_DVR_PTZ_CRUISE_PARAM
LPNET_DVR_PTZ_CRUISE_PARAM = POINTER(struct_tagNET_DVR_PTZ_CRUISE_PARAM)
tagNET_DVR_PTZ_CRUISE_PARAM = struct_tagNET_DVR_PTZ_CRUISE_PARAM
