from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEBUG_CMD(Structure):
    pass

_S(struct_tagNET_DVR_DEBUG_CMD, [
    ('dwSize', DWORD),
    ('szDebugCMD', c_char * 1024),
    ('byRes', BYTE * 400),
])

NET_DVR_DEBUG_CMD = struct_tagNET_DVR_DEBUG_CMD
LPNET_DVR_DEBUG_CMD = POINTER(struct_tagNET_DVR_DEBUG_CMD)
tagNET_DVR_DEBUG_CMD = struct_tagNET_DVR_DEBUG_CMD
