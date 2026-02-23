from ctypes import Structure

from ..base_classes import _S, BYTE
from .anon_186 import NET_DVR_PTZPOS
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_CB_POINT(Structure):
    pass

_S(struct_tagNET_DVR_CB_POINT, [
    ('struPoint', NET_VCA_POINT),
    ('struPtzPos', NET_DVR_PTZPOS),
    ('byRes', BYTE * 8),
])

NET_DVR_CB_POINT = struct_tagNET_DVR_CB_POINT
LPNET_DVR_CB_POINT = struct_tagNET_DVR_CB_POINT
tagNET_DVR_CB_POINT = struct_tagNET_DVR_CB_POINT
