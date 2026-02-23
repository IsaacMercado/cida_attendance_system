from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_VIOLENT_MOTION(Structure):
    pass

_S(struct_tagNET_VCA_VIOLENT_MOTION, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('bySensitivity', BYTE),
    ('byMode', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_VIOLENT_MOTION = struct_tagNET_VCA_VIOLENT_MOTION
LPNET_VCA_VIOLENT_MOTION = POINTER(struct_tagNET_VCA_VIOLENT_MOTION)
tagNET_VCA_VIOLENT_MOTION = struct_tagNET_VCA_VIOLENT_MOTION
