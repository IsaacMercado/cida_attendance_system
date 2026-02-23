from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_INFO_COND(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_INFO_COND, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('dwFingerPrintNum', DWORD),
    ('byFingerPrintID', BYTE),
    ('byCallbackMode', BYTE),
    ('byRes1', BYTE * 26),
])

NET_DVR_FINGER_PRINT_INFO_COND = struct_tagNET_DVR_FINGER_PRINT_INFO_COND
LPNET_DVR_FINGER_PRINT_INFO_COND = POINTER(struct_tagNET_DVR_FINGER_PRINT_INFO_COND)
tagNET_DVR_FINGER_PRINT_INFO_COND = struct_tagNET_DVR_FINGER_PRINT_INFO_COND
