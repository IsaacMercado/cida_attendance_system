from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_BYCARD(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_BYCARD, [
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('byFingerPrintID', BYTE * 10),
    ('byRes1', BYTE * 34),
])

NET_DVR_FINGER_PRINT_BYCARD = struct_tagNET_DVR_FINGER_PRINT_BYCARD
LPNET_DVR_FINGER_PRINT_BYCARD = POINTER(struct_tagNET_DVR_FINGER_PRINT_BYCARD)
tagNET_DVR_FINGER_PRINT_BYCARD = struct_tagNET_DVR_FINGER_PRINT_BYCARD
