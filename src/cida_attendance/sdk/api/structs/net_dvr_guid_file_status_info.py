from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GUID_FILE_STATUS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GUID_FILE_STATUS_INFO, [
    ('dwSize', DWORD),
    ('byLockStatus', BYTE),
    ('byPasswd', BYTE),
    ('byRetryNum', BYTE),
    ('byRes1', BYTE),
    ('dwLockTime', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_GUID_FILE_STATUS_INFO = struct_tagNET_DVR_GUID_FILE_STATUS_INFO
LPNET_DVR_GUID_FILE_STATUS_INFO = POINTER(struct_tagNET_DVR_GUID_FILE_STATUS_INFO)
tagNET_DVR_GUID_FILE_STATUS_INFO = struct_tagNET_DVR_GUID_FILE_STATUS_INFO
