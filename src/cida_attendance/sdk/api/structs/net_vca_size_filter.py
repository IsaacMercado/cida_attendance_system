from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_SIZE_FILTER(Structure):
    pass

_S(struct_tagNET_VCA_SIZE_FILTER, [
    ('byActive', BYTE),
    ('byMode', BYTE),
    ('byRes', BYTE * 2),
    ('struMiniRect', NET_VCA_RECT),
    ('struMaxRect', NET_VCA_RECT),
])

NET_VCA_SIZE_FILTER = struct_tagNET_VCA_SIZE_FILTER
LPNET_VCA_SIZE_FILTER = POINTER(struct_tagNET_VCA_SIZE_FILTER)
tagNET_VCA_SIZE_FILTER = struct_tagNET_VCA_SIZE_FILTER
