from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_ENCRYPT_DEVICE_COND(Structure):
    pass

_S(struct__NET_DVR_ENCRYPT_DEVICE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byAlgorithm', BYTE),
    ('byModelLen', BYTE),
    ('byCERTSaveLocation', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_ENCRYPT_DEVICE_COND = struct__NET_DVR_ENCRYPT_DEVICE_COND
LPNET_DVR_ENCRYPT_DEVICE_COND = POINTER(struct__NET_DVR_ENCRYPT_DEVICE_COND)
_NET_DVR_ENCRYPT_DEVICE_COND = struct__NET_DVR_ENCRYPT_DEVICE_COND
