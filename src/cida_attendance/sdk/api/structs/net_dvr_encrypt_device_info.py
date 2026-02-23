from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_ENCRYPT_DEVICE_INFO(Structure):
    pass

_S(struct__NET_DVR_ENCRYPT_DEVICE_INFO, [
    ('dwSize', DWORD),
    ('byAlgorithm', BYTE),
    ('byModelLen', BYTE),
    ('byRes1', BYTE * 30),
    ('dwPublicKeyLen', DWORD),
    ('szPublicKey', c_char * 512),
    ('szChipSerialNumber', c_char * 32),
    ('szDeviceID', c_char * 20),
    ('byRes2', BYTE * 128),
])

NET_DVR_ENCRYPT_DEVICE_INFO = struct__NET_DVR_ENCRYPT_DEVICE_INFO
LPNET_DVR_ENCRYPT_DEVICE_INFO = POINTER(struct__NET_DVR_ENCRYPT_DEVICE_INFO)
_NET_DVR_ENCRYPT_DEVICE_INFO = struct__NET_DVR_ENCRYPT_DEVICE_INFO
