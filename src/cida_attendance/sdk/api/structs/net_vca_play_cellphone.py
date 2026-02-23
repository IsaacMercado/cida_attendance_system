from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_PLAY_CELLPHONE(Structure):
    pass

_S(struct_tagNET_VCA_PLAY_CELLPHONE, [
    ('struRegion', NET_VCA_POLYGON),
    ('wDuration', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_PLAY_CELLPHONE = struct_tagNET_VCA_PLAY_CELLPHONE
LPNET_VCA_PLAY_CELLPHONE = POINTER(struct_tagNET_VCA_PLAY_CELLPHONE)
tagNET_VCA_PLAY_CELLPHONE = struct_tagNET_VCA_PLAY_CELLPHONE
