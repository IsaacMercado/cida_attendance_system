from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_VCA_REACH_HIGHT(Structure):
    pass

_S(struct_tagNET_VCA_REACH_HIGHT, [
    ('struVcaLine', NET_VCA_LINE),
    ('wDuration', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_REACH_HIGHT = struct_tagNET_VCA_REACH_HIGHT
LPNET_VCA_REACH_HIGHT = POINTER(struct_tagNET_VCA_REACH_HIGHT)
tagNET_VCA_REACH_HIGHT = struct_tagNET_VCA_REACH_HIGHT
