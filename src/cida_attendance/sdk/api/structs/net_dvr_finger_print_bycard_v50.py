from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_BYCARD_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_BYCARD_V50, [
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('byFingerPrintID', BYTE * 10),
    ('byRes1', BYTE * 2),
    ('byEmployeeNo', BYTE * 32),
])

NET_DVR_FINGER_PRINT_BYCARD_V50 = struct_tagNET_DVR_FINGER_PRINT_BYCARD_V50
LPNET_DVR_FINGER_PRINT_BYCARD_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_BYCARD_V50)
tagNET_DVR_FINGER_PRINT_BYCARD_V50 = struct_tagNET_DVR_FINGER_PRINT_BYCARD_V50
