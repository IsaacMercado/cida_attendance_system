from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_VCA_POLYLINE(Structure):
    pass

_S(struct_tagNET_VCA_POLYLINE, [
    ('struPoint', NET_VCA_POINT * 4),
])

NET_VCA_POLYLINE = struct_tagNET_VCA_POLYLINE
LPNET_VCA_POLYLINE = POINTER(struct_tagNET_VCA_POLYLINE)
tagNET_VCA_POLYLINE = struct_tagNET_VCA_POLYLINE
