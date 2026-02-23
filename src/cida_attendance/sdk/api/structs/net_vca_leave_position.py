from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_LEAVE_POSITION(Structure):
    pass

_S(struct_tagNET_VCA_LEAVE_POSITION, [
    ('struRegion', NET_VCA_POLYGON),
    ('wLeaveDelay', WORD),
    ('wStaticDelay', WORD),
    ('byMode', BYTE),
    ('byPersonType', BYTE),
    ('byOnPosition', BYTE),
    ('bySensitivity', BYTE),
])

NET_VCA_LEAVE_POSITION = struct_tagNET_VCA_LEAVE_POSITION
LPNET_VCA_LEAVE_POSITION = POINTER(struct_tagNET_VCA_LEAVE_POSITION)
tagNET_VCA_LEAVE_POSITION = struct_tagNET_VCA_LEAVE_POSITION
