from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_RULE_TRIGGER_PARAM(Structure):
    pass

_S(struct_tagNET_VCA_RULE_TRIGGER_PARAM, [
    ('byTriggerMode', BYTE),
    ('byTriggerPoint', BYTE),
    ('byRes1', BYTE * 2),
    ('fTriggerArea', c_float),
    ('byRes2', BYTE * 4),
])

NET_VCA_RULE_TRIGGER_PARAM = struct_tagNET_VCA_RULE_TRIGGER_PARAM
LPNET_VCA_RULE_TRIGGER_PARAM = POINTER(struct_tagNET_VCA_RULE_TRIGGER_PARAM)
tagNET_VCA_RULE_TRIGGER_PARAM = struct_tagNET_VCA_RULE_TRIGGER_PARAM
