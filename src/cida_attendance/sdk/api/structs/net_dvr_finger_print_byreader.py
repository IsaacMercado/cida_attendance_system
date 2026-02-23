from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_BYREADER(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_BYREADER, [
    ('dwCardReaderNo', DWORD),
    ('byClearAllCard', BYTE),
    ('byRes1', BYTE * 3),
    ('byCardNo', BYTE * 32),
    ('byRes', BYTE * 548),
])

NET_DVR_FINGER_PRINT_BYREADER = struct_tagNET_DVR_FINGER_PRINT_BYREADER
LPNET_DVR_FINGER_PRINT_BYREADER = POINTER(struct_tagNET_DVR_FINGER_PRINT_BYREADER)
tagNET_DVR_FINGER_PRINT_BYREADER = struct_tagNET_DVR_FINGER_PRINT_BYREADER
