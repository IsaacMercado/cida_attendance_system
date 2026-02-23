from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardReaderRecvStatus', BYTE * 512),
    ('byFingerPrintID', BYTE),
    ('byFingerType', BYTE),
    ('byTotalStatus', BYTE),
    ('byRes1', BYTE),
    ('byErrorMsg', BYTE * 32),
    ('dwCardReaderNo', DWORD),
    ('byRes', BYTE * 24),
])

NET_DVR_FINGER_PRINT_STATUS = struct_tagNET_DVR_FINGER_PRINT_STATUS
LPNET_DVR_FINGER_PRINT_STATUS = POINTER(struct_tagNET_DVR_FINGER_PRINT_STATUS)
tagNET_DVR_FINGER_PRINT_STATUS = struct_tagNET_DVR_FINGER_PRINT_STATUS
