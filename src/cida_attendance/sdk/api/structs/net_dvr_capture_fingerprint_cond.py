from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAPTURE_FINGERPRINT_COND(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_FINGERPRINT_COND, [
    ('dwSize', DWORD),
    ('byFingerPrintPicType', BYTE),
    ('byFingerNo', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_CAPTURE_FINGERPRINT_COND = struct_tagNET_DVR_CAPTURE_FINGERPRINT_COND
LPNET_DVR_CAPTURE_FINGERPRINT_COND = POINTER(struct_tagNET_DVR_CAPTURE_FINGERPRINT_COND)
tagNET_DVR_CAPTURE_FINGERPRINT_COND = struct_tagNET_DVR_CAPTURE_FINGERPRINT_COND
