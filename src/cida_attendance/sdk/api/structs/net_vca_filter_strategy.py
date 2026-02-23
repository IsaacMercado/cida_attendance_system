from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_FILTER_STRATEGY(Structure):
    pass

_S(struct_tagNET_VCA_FILTER_STRATEGY, [
    ('byStrategy', BYTE),
    ('byRes', BYTE * 11),
])

NET_VCA_FILTER_STRATEGY = struct_tagNET_VCA_FILTER_STRATEGY
LPNET_VCA_FILTER_STRATEGY = POINTER(struct_tagNET_VCA_FILTER_STRATEGY)
tagNET_VCA_FILTER_STRATEGY = struct_tagNET_VCA_FILTER_STRATEGY
