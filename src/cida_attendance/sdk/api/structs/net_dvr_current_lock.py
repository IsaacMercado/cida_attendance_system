from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CURRENT_LOCK(Structure):
    pass

_S(struct_tagNET_DVR_CURRENT_LOCK, [
    ('dwSize', DWORD),
    ('byCurrentLock', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_CURRENT_LOCK = struct_tagNET_DVR_CURRENT_LOCK
LPNET_DVR_CURRENT_LOCK = POINTER(struct_tagNET_DVR_CURRENT_LOCK)
tagNET_DVR_CURRENT_LOCK = struct_tagNET_DVR_CURRENT_LOCK
