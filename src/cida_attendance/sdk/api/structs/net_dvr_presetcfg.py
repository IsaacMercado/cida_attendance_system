from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_PRESETCFG(Structure):
    pass

_S(struct_tagNET_DVR_PRESETCFG, [
    ('dwSize', DWORD),
    ('dwPresetIndex', DWORD),
    ('struVcaPoint', NET_VCA_POINT),
    ('wZoomCoordinate', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_PRESETCFG = struct_tagNET_DVR_PRESETCFG
LPNET_DVR_PRESETCFG = POINTER(struct_tagNET_DVR_PRESETCFG)
tagNET_DVR_PRESETCFG = struct_tagNET_DVR_PRESETCFG
