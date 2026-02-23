from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_PTZCRUISE_POINTCFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZCRUISE_POINTCFG, [
    ('dwSize', DWORD),
    ('dwPresetIndex', DWORD),
    ('struVcaPoint', NET_VCA_POINT),
    ('byDwell', BYTE),
    ('bySpeed', BYTE),
    ('wZoomCoordinate', WORD),
    ('byRes', BYTE * 28),
])

NET_DVR_PTZCRUISE_POINTCFG = struct_tagNET_DVR_PTZCRUISE_POINTCFG
LPNET_DVR_PTZCRUISE_POINTCFG = POINTER(struct_tagNET_DVR_PTZCRUISE_POINTCFG)
tagNET_DVR_PTZCRUISE_POINTCFG = struct_tagNET_DVR_PTZCRUISE_POINTCFG
