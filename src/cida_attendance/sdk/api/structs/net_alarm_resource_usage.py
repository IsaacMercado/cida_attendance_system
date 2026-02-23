from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ALARM_RESOURCE_USAGE(Structure):
    pass

_S(struct_tagNET_ALARM_RESOURCE_USAGE, [
    ('byLevel', BYTE),
    ('byRes', BYTE * 491),
])

NET_ALARM_RESOURCE_USAGE = struct_tagNET_ALARM_RESOURCE_USAGE
LPNET_ALARM_RESOURCE_USAGE = POINTER(struct_tagNET_ALARM_RESOURCE_USAGE)
tagNET_ALARM_RESOURCE_USAGE = struct_tagNET_ALARM_RESOURCE_USAGE
