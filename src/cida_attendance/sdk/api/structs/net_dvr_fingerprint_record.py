from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_FINGERPRINT_RECORD(Structure):
    pass

_S(struct__NET_DVR_FINGERPRINT_RECORD, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwFingerPrintLen', DWORD),
    ('dwEnableReaderNo', DWORD),
    ('byFingerPrintID', BYTE),
    ('byFingerType', BYTE),
    ('byRes1', BYTE * 30),
    ('byFingerData', BYTE * 768),
    ('byRes', BYTE * 96),
])

NET_DVR_FINGERPRINT_RECORD = struct__NET_DVR_FINGERPRINT_RECORD
LPNET_DVR_FINGERPRINT_RECORD = POINTER(struct__NET_DVR_FINGERPRINT_RECORD)
_NET_DVR_FINGERPRINT_RECORD = struct__NET_DVR_FINGERPRINT_RECORD
