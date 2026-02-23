from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STORAGE_RWLOCK(Structure):
    pass

_S(struct_tagNET_DVR_STORAGE_RWLOCK, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes', BYTE * 3),
    ('szPassWD', c_char * 16),
    ('szOriginalPassWD', c_char * 16),
    ('byRes1', BYTE * 128),
])

NET_DVR_STORAGE_RWLOCK = struct_tagNET_DVR_STORAGE_RWLOCK
LPNET_DVR_STORAGE_RWLOCK = POINTER(struct_tagNET_DVR_STORAGE_RWLOCK)
tagNET_DVR_STORAGE_RWLOCK = struct_tagNET_DVR_STORAGE_RWLOCK
