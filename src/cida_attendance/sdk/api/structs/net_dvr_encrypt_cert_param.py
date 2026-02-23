from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String


class struct__NET_DVR_ENCRYPT_CERT_PARAM(Structure):
    pass

_S(struct__NET_DVR_ENCRYPT_CERT_PARAM, [
    ('dwSize', DWORD),
    ('wCertType', WORD),
    ('byRes1', BYTE * 2),
    ('dwCertLen', DWORD),
    ('byRes2', BYTE * 32),
    ('pCertBuf', String),
])

NET_DVR_ENCRYPT_CERT_PARAM = struct__NET_DVR_ENCRYPT_CERT_PARAM
LPNET_DVR_ENCRYPT_CERT_PARAM = POINTER(struct__NET_DVR_ENCRYPT_CERT_PARAM)
_NET_DVR_ENCRYPT_CERT_PARAM = struct__NET_DVR_ENCRYPT_CERT_PARAM
