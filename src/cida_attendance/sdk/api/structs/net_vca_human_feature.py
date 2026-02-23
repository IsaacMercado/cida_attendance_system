from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_HUMAN_FEATURE(Structure):
    pass

_S(struct_tagNET_VCA_HUMAN_FEATURE, [
    ('byAgeGroup', BYTE),
    ('bySex', BYTE),
    ('byEyeGlass', BYTE),
    ('byAge', BYTE),
    ('byAgeDeviation', BYTE),
    ('byRes0', BYTE),
    ('byMask', BYTE),
    ('bySmile', BYTE),
    ('byFaceExpression', BYTE),
    ('byRes1', BYTE),
    ('byRes2', BYTE),
    ('byHat', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_HUMAN_FEATURE = struct_tagNET_VCA_HUMAN_FEATURE
LPNET_VCA_HUMAN_FEATURE = POINTER(struct_tagNET_VCA_HUMAN_FEATURE)
tagNET_VCA_HUMAN_FEATURE = struct_tagNET_VCA_HUMAN_FEATURE
