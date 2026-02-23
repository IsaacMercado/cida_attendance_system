from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGER_PRINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_CFG, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFingerPrintLen', DWORD),
    ('byEnableCardReader', BYTE * 512),
    ('byFingerPrintID', BYTE),
    ('byFingerType', BYTE),
    ('byRes1', BYTE * 30),
    ('byFingerData', BYTE * 768),
    ('byRes', BYTE * 64),
])

NET_DVR_FINGER_PRINT_CFG = struct_tagNET_DVR_FINGER_PRINT_CFG
LPNET_DVR_FINGER_PRINT_CFG = POINTER(struct_tagNET_DVR_FINGER_PRINT_CFG)
tagNET_DVR_FINGER_PRINT_CFG = struct_tagNET_DVR_FINGER_PRINT_CFG
