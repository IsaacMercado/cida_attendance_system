from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_VCA_POLYGON(Structure):
    pass

_S(struct_tagNET_VCA_POLYGON, [
    ('dwPointNum', DWORD),
    ('struPos', NET_VCA_POINT * 10),
])

NET_VCA_POLYGON = struct_tagNET_VCA_POLYGON
LPNET_VCA_POLYGON = POINTER(struct_tagNET_VCA_POLYGON)
tagNET_VCA_POLYGON = struct_tagNET_VCA_POLYGON
