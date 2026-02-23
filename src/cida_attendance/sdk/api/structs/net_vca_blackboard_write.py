from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_BLACKBOARD_WRITE(Structure):
    pass

_S(struct_tagNET_VCA_BLACKBOARD_WRITE, [
    ('struRegion', NET_VCA_POLYGON),
    ('byTeacherState', BYTE),
    ('byWritingState', BYTE),
    ('byWritingArea', BYTE),
    ('byRes', BYTE * 5),
])

NET_VCA_BLACKBOARD_WRITE = struct_tagNET_VCA_BLACKBOARD_WRITE
LPNET_VCA_BLACKBOARD_WRITE = POINTER(struct_tagNET_VCA_BLACKBOARD_WRITE)
tagNET_VCA_BLACKBOARD_WRITE = struct_tagNET_VCA_BLACKBOARD_WRITE
