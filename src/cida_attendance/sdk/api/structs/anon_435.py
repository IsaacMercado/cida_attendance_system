from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_435(Structure):
    pass

_S(struct_anon_435, [
    ('dwSize', DWORD),
    ('byOutScale', BYTE * 8),
    ('byRes', BYTE * 16),
])

NET_DVR_OUT_SCALE_CFG = struct_anon_435
LPNET_DVR_OUT_SCALE_CFG = POINTER(struct_anon_435)
