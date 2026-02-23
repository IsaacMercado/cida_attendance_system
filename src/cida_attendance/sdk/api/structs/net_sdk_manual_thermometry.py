from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_sdk_manualtherm_rule import NET_SDK_MANUALTHERM_RULE


class struct_tagNET_SDK_MANUAL_THERMOMETRY(Structure):
    pass

_S(struct_tagNET_SDK_MANUAL_THERMOMETRY, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byThermometryUnit', BYTE),
    ('byDataType', BYTE),
    ('byRes1', BYTE * 6),
    ('struRuleInfo', NET_SDK_MANUALTHERM_RULE),
    ('byRes', BYTE * 512),
])

NET_SDK_MANUAL_THERMOMETRY = struct_tagNET_SDK_MANUAL_THERMOMETRY
LPNET_SDK_MANUAL_THERMOMETRY = POINTER(struct_tagNET_SDK_MANUAL_THERMOMETRY)
tagNET_SDK_MANUAL_THERMOMETRY = struct_tagNET_SDK_MANUAL_THERMOMETRY
