from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50, [
    ('dwSize', DWORD),
    ('dwCardReaderNo', DWORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_FINGER_PRINT_INFO_STATUS_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50
LPNET_DVR_FINGER_PRINT_INFO_STATUS_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50)
tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_STATUS_V50
