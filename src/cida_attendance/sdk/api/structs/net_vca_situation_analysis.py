from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_SITUATION_ANALYSIS(Structure):
    pass

_S(struct_tagNET_VCA_SITUATION_ANALYSIS, [
    ('struRegion', NET_VCA_POLYGON),
    ('wPeopleNum', WORD),
    ('byRes', BYTE * 6),
])

NET_VCA_SITUATION_ANALYSIS = struct_tagNET_VCA_SITUATION_ANALYSIS
LPNET_VCA_SITUATION_ANALYSIS = POINTER(struct_tagNET_VCA_SITUATION_ANALYSIS)
tagNET_VCA_SITUATION_ANALYSIS = struct_tagNET_VCA_SITUATION_ANALYSIS
