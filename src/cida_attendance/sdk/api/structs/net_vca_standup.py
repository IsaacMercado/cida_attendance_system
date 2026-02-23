from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_STANDUP(Structure):
    pass

_S(struct_tagNET_VCA_STANDUP, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byHeightThreshold', BYTE),
    ('wDuration', WORD),
    ('byRes', BYTE * 4),
])

NET_VCA_STANDUP = struct_tagNET_VCA_STANDUP
LPNET_VCA_STANDUP = POINTER(struct_tagNET_VCA_STANDUP)
tagNET_VCA_STANDUP = struct_tagNET_VCA_STANDUP
