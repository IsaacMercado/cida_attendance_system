from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_321(Structure):
    pass

_S(struct_anon_321, [
    ('sAESKey', BYTE * 16),
    ('byRes', BYTE * 64),
])

NET_DVR_AES_KEY_INFO = struct_anon_321
LPNET_DVR_AES_KEY_INFO = POINTER(struct_anon_321)
