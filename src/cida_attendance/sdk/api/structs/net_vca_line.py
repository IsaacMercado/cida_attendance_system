from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_VCA_LINE(Structure):
    pass

_S(struct_tagNET_VCA_LINE, [
    ('struStart', NET_VCA_POINT),
    ('struEnd', NET_VCA_POINT),
])

NET_VCA_LINE = struct_tagNET_VCA_LINE
LPNET_VCA_LINE = POINTER(struct_tagNET_VCA_LINE)
tagNET_VCA_LINE = struct_tagNET_VCA_LINE
