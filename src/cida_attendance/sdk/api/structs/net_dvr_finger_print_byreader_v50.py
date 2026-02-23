from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_BYREADER_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_BYREADER_V50, [
    ('dwCardReaderNo', DWORD),
    ('byClearAllCard', BYTE),
    ('byRes1', BYTE * 3),
    ('byCardNo', BYTE * 32),
    ('byEmployeeNo', BYTE * 32),
    ('byRes', BYTE * 516),
])

NET_DVR_FINGER_PRINT_BYREADER_V50 = struct_tagNET_DVR_FINGER_PRINT_BYREADER_V50
LPNET_DVR_FINGER_PRINT_BYREADER_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_BYREADER_V50)
tagNET_DVR_FINGER_PRINT_BYREADER_V50 = struct_tagNET_DVR_FINGER_PRINT_BYREADER_V50
