from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_CAPTURE_FINGERPRINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_FINGERPRINT_CFG, [
    ('dwSize', DWORD),
    ('dwFingerPrintDataSize', DWORD),
    ('byFingerData', BYTE * 768),
    ('dwFingerPrintPicSize', DWORD),
    ('pFingerPrintPicBuffer', String),
    ('byFingerNo', BYTE),
    ('byFingerPrintQuality', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_CAPTURE_FINGERPRINT_CFG = struct_tagNET_DVR_CAPTURE_FINGERPRINT_CFG
LPNET_DVR_CAPTURE_FINGERPRINT_CFG = POINTER(struct_tagNET_DVR_CAPTURE_FINGERPRINT_CFG)
tagNET_DVR_CAPTURE_FINGERPRINT_CFG = struct_tagNET_DVR_CAPTURE_FINGERPRINT_CFG
