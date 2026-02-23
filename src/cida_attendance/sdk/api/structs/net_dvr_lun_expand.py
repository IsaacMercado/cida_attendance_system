from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LUN_EXPAND(Structure):
    pass

_S(struct_tagNET_DVR_LUN_EXPAND, [
    ('dwSize', DWORD),
    ('dwLunID', DWORD),
    ('dwHSize', DWORD),
    ('dwLSize', DWORD),
    ('szArrayIDGroup', c_char * 32),
    ('szNewLunName', c_char * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_LUN_EXPAND = struct_tagNET_DVR_LUN_EXPAND
LPNET_DVR_LUN_EXPAND = POINTER(struct_tagNET_DVR_LUN_EXPAND)
tagNET_DVR_LUN_EXPAND = struct_tagNET_DVR_LUN_EXPAND
