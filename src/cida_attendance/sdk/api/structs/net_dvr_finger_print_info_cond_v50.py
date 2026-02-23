from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_INFO_COND_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_INFO_COND_V50, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('dwFingerPrintNum', DWORD),
    ('byFingerPrintID', BYTE),
    ('byCallbackMode', BYTE),
    ('byRes2', BYTE * 2),
    ('byEmployeeNo', BYTE * 32),
    ('byRes1', BYTE * 128),
])

NET_DVR_FINGER_PRINT_INFO_COND_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_COND_V50
LPNET_DVR_FINGER_PRINT_INFO_COND_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_INFO_COND_V50)
tagNET_DVR_FINGER_PRINT_INFO_COND_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_COND_V50
