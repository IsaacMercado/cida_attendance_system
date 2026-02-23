from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCK_ALARM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LOCK_ALARM_INFO, [
    ('dwLockID', DWORD),
    ('byRes', BYTE * 252),
])

NET_DVR_LOCK_ALARM_INFO = struct_tagNET_DVR_LOCK_ALARM_INFO
LPNET_DVR_LOCK_ALARM_INFO = POINTER(struct_tagNET_DVR_LOCK_ALARM_INFO)
tagNET_DVR_LOCK_ALARM_INFO = struct_tagNET_DVR_LOCK_ALARM_INFO
