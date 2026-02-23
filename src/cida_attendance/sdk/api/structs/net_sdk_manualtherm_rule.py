from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_sdk_point_thermometry import NET_SDK_POINT_THERMOMETRY
from .net_sdk_region_thermometry import NET_SDK_REGION_THERMOMETRY


class struct_tagNET_SDK_MANUALTHERM_RULE(Structure):
    pass

_S(struct_tagNET_SDK_MANUALTHERM_RULE, [
    ('byRuleID', BYTE),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 2),
    ('szRuleName', c_char * 32),
    ('byRuleCalibType', BYTE),
    ('byRes2', BYTE * 3),
    ('struPointTherm', NET_SDK_POINT_THERMOMETRY),
    ('struRegionTherm', NET_SDK_REGION_THERMOMETRY),
    ('byRes', BYTE * 512),
])

NET_SDK_MANUALTHERM_RULE = struct_tagNET_SDK_MANUALTHERM_RULE
LPNET_SDK_MANUALTHERM_RULE = POINTER(struct_tagNET_SDK_MANUALTHERM_RULE)
tagNET_SDK_MANUALTHERM_RULE = struct_tagNET_SDK_MANUALTHERM_RULE
