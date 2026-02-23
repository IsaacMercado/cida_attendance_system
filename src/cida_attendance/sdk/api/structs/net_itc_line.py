from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_ITC_LINE(Structure):
    pass

_S(struct_tagNET_ITC_LINE, [
    ('struLine', NET_VCA_LINE),
    ('byLineType', BYTE),
    ('byRes', BYTE * 7),
])

NET_ITC_LINE = struct_tagNET_ITC_LINE
LPNET_ITC_LINE = POINTER(struct_tagNET_ITC_LINE)
tagNET_ITC_LINE = struct_tagNET_ITC_LINE
