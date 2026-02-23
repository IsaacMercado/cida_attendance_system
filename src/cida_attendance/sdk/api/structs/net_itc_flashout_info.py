from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_FLASHOUT_INFO(Structure):
    pass

_S(struct_tagNET_ITC_FLASHOUT_INFO, [
    ('byFlashOutIndex', BYTE * 8),
    ('byRes', BYTE * 40),
])

NET_ITC_FLASHOUT_INFO = struct_tagNET_ITC_FLASHOUT_INFO
LPNET_ITC_FLASHOUT_INFO = POINTER(struct_tagNET_ITC_FLASHOUT_INFO)
tagNET_ITC_FLASHOUT_INFO = struct_tagNET_ITC_FLASHOUT_INFO
