from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEBUG_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEBUG_INFO, [
    ('dwSize', DWORD),
    ('szDebugInfo', c_char * 1400),
    ('byRes', BYTE * 32),
])

NET_DVR_DEBUG_INFO = struct_tagNET_DVR_DEBUG_INFO
LPNET_DVR_DEBUG_INFO = POINTER(struct_tagNET_DVR_DEBUG_INFO)
tagNET_DVR_DEBUG_INFO = struct_tagNET_DVR_DEBUG_INFO
