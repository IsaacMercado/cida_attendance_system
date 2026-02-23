from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_ANSWER(Structure):
    pass

_S(struct_tagNET_VCA_ANSWER, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byAlarmState', BYTE),
    ('byZoomOver', BYTE),
    ('byAnswerStudent', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_ANSWER = struct_tagNET_VCA_ANSWER
LPNET_VCA_ANSWER = POINTER(struct_tagNET_VCA_ANSWER)
tagNET_VCA_ANSWER = struct_tagNET_VCA_ANSWER
