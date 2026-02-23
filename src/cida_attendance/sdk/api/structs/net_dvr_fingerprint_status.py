from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_FINGERPRINT_STATUS(Structure):
    pass

_S(struct__NET_DVR_FINGERPRINT_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardReaderRecvStatus', BYTE),
    ('byFingerPrintID', BYTE),
    ('byFingerType', BYTE),
    ('byRecvStatus', BYTE),
    ('byErrorMsg', BYTE * 32),
    ('dwCardReaderNo', DWORD),
    ('byRes', BYTE * 20),
])

NET_DVR_FINGERPRINT_STATUS = struct__NET_DVR_FINGERPRINT_STATUS
LPNET_DVR_FINGERPRINT_STATUS = POINTER(struct__NET_DVR_FINGERPRINT_STATUS)
_NET_DVR_FINGERPRINT_STATUS = struct__NET_DVR_FINGERPRINT_STATUS
