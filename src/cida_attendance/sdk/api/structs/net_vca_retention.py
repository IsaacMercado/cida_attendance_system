from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_RETENTION(Structure):
    pass

_S(struct_tagNET_VCA_RETENTION, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_RETENTION = struct_tagNET_VCA_RETENTION
LPNET_VCA_RETENTION = POINTER(struct_tagNET_VCA_RETENTION)
tagNET_VCA_RETENTION = struct_tagNET_VCA_RETENTION
