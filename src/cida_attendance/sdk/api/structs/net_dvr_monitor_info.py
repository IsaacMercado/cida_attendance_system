from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_MONITOR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_MONITOR_INFO, [
    ('wPort', WORD),
    ('byRes1', BYTE * 2),
    ('struRestrictRemoteIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 164),
])

NET_DVR_MONITOR_INFO = struct_tagNET_DVR_MONITOR_INFO
LPNET_DVR_MONITOR_INFO = POINTER(struct_tagNET_DVR_MONITOR_INFO)
tagNET_DVR_MONITOR_INFO = struct_tagNET_DVR_MONITOR_INFO
