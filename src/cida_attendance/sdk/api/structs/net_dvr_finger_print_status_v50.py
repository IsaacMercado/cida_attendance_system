from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_STATUS_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_STATUS_V50, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardReaderRecvStatus', BYTE * 512),
    ('byFingerPrintID', BYTE),
    ('byFingerType', BYTE),
    ('byTotalStatus', BYTE),
    ('byRecvStatus', BYTE),
    ('byErrorMsg', BYTE * 32),
    ('dwCardReaderNo', DWORD),
    ('byEmployeeNo', BYTE * 32),
    ('byErrorEmployeeNo', BYTE * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_FINGER_PRINT_STATUS_V50 = struct_tagNET_DVR_FINGER_PRINT_STATUS_V50
LPNET_DVR_FINGER_PRINT_STATUS_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_STATUS_V50)
tagNET_DVR_FINGER_PRINT_STATUS_V50 = struct_tagNET_DVR_FINGER_PRINT_STATUS_V50
