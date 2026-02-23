from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FINGERPRINT_COND(Structure):
    pass

_S(struct_tagNET_DVR_FINGERPRINT_COND, [
    ('dwSize', DWORD),
    ('dwFingerprintNum', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwEnableReaderNo', DWORD),
    ('byFingerPrintID', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_FINGERPRINT_COND = struct_tagNET_DVR_FINGERPRINT_COND
LPNET_DVR_FINGERPRINT_COND = POINTER(struct_tagNET_DVR_FINGERPRINT_COND)
tagNET_DVR_FINGERPRINT_COND = struct_tagNET_DVR_FINGERPRINT_COND
