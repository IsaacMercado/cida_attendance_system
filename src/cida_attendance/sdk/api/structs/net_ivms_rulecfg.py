from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_ivms_one_rule import NET_IVMS_ONE_RULE


class struct_tagNET_IVMS_RULECFG(Structure):
    pass

_S(struct_tagNET_IVMS_RULECFG, [
    ('struRule', NET_IVMS_ONE_RULE * 8),
])

NET_IVMS_RULECFG = struct_tagNET_IVMS_RULECFG
LPNET_IVMS_RULECFG = POINTER(struct_tagNET_IVMS_RULECFG)
tagNET_IVMS_RULECFG = struct_tagNET_IVMS_RULECFG
