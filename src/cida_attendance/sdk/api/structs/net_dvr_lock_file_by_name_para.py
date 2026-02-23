from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCK_FILE_BY_NAME_PARA(Structure):
    pass

_S(struct_tagNET_DVR_LOCK_FILE_BY_NAME_PARA, [
    ('byFileName', BYTE * 32),
    ('dwLockDuration', DWORD),
    ('byRes', BYTE * 512),
])

NET_DVR_LOCK_FILE_BY_NAME_PARA = struct_tagNET_DVR_LOCK_FILE_BY_NAME_PARA
LPNET_DVR_LOCK_FILE_BY_NAME_PARA = POINTER(struct_tagNET_DVR_LOCK_FILE_BY_NAME_PARA)
tagNET_DVR_LOCK_FILE_BY_NAME_PARA = struct_tagNET_DVR_LOCK_FILE_BY_NAME_PARA
