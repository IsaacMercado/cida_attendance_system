from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_POS_PARAM(Structure):
    pass

_S(struct_tagNET_POS_PARAM, [
    ('wLeft', WORD),
    ('wTop', WORD),
    ('wRight', WORD),
    ('wBottom', WORD),
])

NET_POS_PARAM = struct_tagNET_POS_PARAM
LPNET_POS_PARAM = POINTER(struct_tagNET_POS_PARAM)
tagNET_POS_PARAM = struct_tagNET_POS_PARAM
