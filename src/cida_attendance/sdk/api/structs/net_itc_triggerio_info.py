from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_TRIGGERIO_INFO(Structure):
    pass

_S(struct_tagNET_ITC_TRIGGERIO_INFO, [
    ('byTriggerIOIndex', BYTE * 8),
    ('byRes', BYTE * 40),
])

NET_ITC_TRIGGERIO_INFO = struct_tagNET_ITC_TRIGGERIO_INFO
LPNET_ITC_TRIGGERIO_INFO = POINTER(struct_tagNET_ITC_TRIGGERIO_INFO)
tagNET_ITC_TRIGGERIO_INFO = struct_tagNET_ITC_TRIGGERIO_INFO
