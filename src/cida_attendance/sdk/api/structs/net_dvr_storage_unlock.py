from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STORAGE_UNLOCK(Structure):
    pass

_S(struct_tagNET_DVR_STORAGE_UNLOCK, [
    ('dwSize', DWORD),
    ('szPassWD', c_char * 16),
    ('byRes1', BYTE * 128),
])

NET_DVR_STORAGE_UNLOCK = struct_tagNET_DVR_STORAGE_UNLOCK
LPNET_DVR_STORAGE_UNLOCK = POINTER(struct_tagNET_DVR_STORAGE_UNLOCK)
tagNET_DVR_STORAGE_UNLOCK = struct_tagNET_DVR_STORAGE_UNLOCK
