from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_ITC_POLYGON(Structure):
    pass

_S(struct_tagNET_ITC_POLYGON, [
    ('dwPointNum', DWORD),
    ('struPos', NET_VCA_POINT * 20),
])

NET_ITC_POLYGON = struct_tagNET_ITC_POLYGON
LPNET_ITC_POLYGON = POINTER(struct_tagNET_ITC_POLYGON)
tagNET_ITC_POLYGON = struct_tagNET_ITC_POLYGON
