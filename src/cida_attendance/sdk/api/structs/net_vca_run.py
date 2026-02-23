from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_RUN(Structure):
    pass

_S(struct_tagNET_VCA_RUN, [
    ('struRegion', NET_VCA_POLYGON),
    ('fRunDistance', c_float),
    ('bySensitivity', BYTE),
    ('byMode', BYTE),
    ('byDetectionTarget', BYTE),
    ('byRes', BYTE),
])

NET_VCA_RUN = struct_tagNET_VCA_RUN
LPNET_VCA_RUN = POINTER(struct_tagNET_VCA_RUN)
tagNET_VCA_RUN = struct_tagNET_VCA_RUN
