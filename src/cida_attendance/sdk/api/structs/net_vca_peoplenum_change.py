from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_VCA_PEOPLENUM_CHANGE(Structure):
    pass

_S(struct_tagNET_VCA_PEOPLENUM_CHANGE, [
    ('struRegion', NET_VCA_POLYGON),
    ('bySensitivity', BYTE),
    ('byPeopleNumThreshold', BYTE),
    ('byDetectMode', BYTE),
    ('byNoneStateEffective', BYTE),
    ('wDuration', WORD),
    ('byPeopleNum', BYTE),
    ('byRes', BYTE),
])

NET_VCA_PEOPLENUM_CHANGE = struct_tagNET_VCA_PEOPLENUM_CHANGE
LPNET_VCA_PEOPLENUM_CHANGE = POINTER(struct_tagNET_VCA_PEOPLENUM_CHANGE)
tagNET_VCA_PEOPLENUM_CHANGE = struct_tagNET_VCA_PEOPLENUM_CHANGE
