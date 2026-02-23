from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UNLOCK_RECORD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UNLOCK_RECORD_INFO, [
    ('byUnlockType', BYTE),
    ('byRes1', BYTE * 3),
    ('byControlSrc', BYTE * 32),
    ('dwPicDataLen', DWORD),
    ('pImage', POINTER(BYTE)),
    ('dwCardUserID', DWORD),
    ('nFloorNumber', SHORT),
    ('wRoomNumber', WORD),
    ('wLockID', WORD),
    ('byRes2', BYTE * 2),
    ('byLockName', BYTE * 32),
    ('byEmployeeNo', BYTE * 32),
    ('byMask', BYTE),
    ('byRes', BYTE * 135),
])

NET_DVR_UNLOCK_RECORD_INFO = struct_tagNET_DVR_UNLOCK_RECORD_INFO
LPNET_DVR_UNLOCK_RECORD_INFO = POINTER(struct_tagNET_DVR_UNLOCK_RECORD_INFO)
tagNET_DVR_UNLOCK_RECORD_INFO = struct_tagNET_DVR_UNLOCK_RECORD_INFO
