from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LUN_CLONE(Structure):
    pass

_S(struct_tagNET_DVR_LUN_CLONE, [
    ('dwSize', DWORD),
    ('dwSrcLunID', DWORD),
    ('dwDstLunID', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_LUN_CLONE = struct_tagNET_DVR_LUN_CLONE
LPNET_DVR_LUN_CLONE = POINTER(struct_tagNET_DVR_LUN_CLONE)
tagNET_DVR_LUN_CLONE = struct_tagNET_DVR_LUN_CLONE
