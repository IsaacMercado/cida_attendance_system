from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_SITDOWN(Structure):
    pass

_S(struct_tagNET_VCA_SITDOWN, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 7),
])

NET_VCA_SITDOWN = struct_tagNET_VCA_SITDOWN
LPNET_VCA_SITDOWN = POINTER(struct_tagNET_VCA_SITDOWN)
tagNET_VCA_SITDOWN = struct_tagNET_VCA_SITDOWN
