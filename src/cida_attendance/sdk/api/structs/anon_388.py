from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_387 import NET_DVR_DNMODE
from .net_vca_rect import NET_VCA_RECT


class struct_anon_388(Structure):
    pass

_S(struct_anon_388, [
    ('byAreaNo', BYTE),
    ('byRes', BYTE * 3),
    ('struRect', NET_VCA_RECT),
    ('struDayNightDisable', NET_DVR_DNMODE),
    ('struDayModeParam', NET_DVR_DNMODE),
    ('struNightModeParam', NET_DVR_DNMODE),
    ('byRes1', BYTE * 8),
])

NET_DVR_MOTION_MULTI_AREAPARAM = struct_anon_388
LPNET_DVR_MOTION_MULTI_AREAPARAM = POINTER(struct_anon_388)
