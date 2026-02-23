from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_anon_219(Structure):
    pass

_S(struct_anon_219, [
    ('dwPicType', DWORD),
    ('pPicBuf', String),
    ('dwPicLen', DWORD),
    ('dwTime', DWORD),
    ('pVideoBuf', String),
    ('dwVideoLen', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_ADAS_PICTURE_INFO = struct_anon_219
LPNET_DVR_ADAS_PICTURE_INFO = POINTER(struct_anon_219)
