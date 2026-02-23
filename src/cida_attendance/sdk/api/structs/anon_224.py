from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_anon_224(Structure):
    pass

_S(struct_anon_224, [
    ('dwPicLen', DWORD),
    ('pPicBuf', String),
    ('byRes', BYTE * 12),
])

NET_DVR_VCA_ATTEND_PICDATA = struct_anon_224
LPNET_DVR_VCA_ATTEND_PICDATA = POINTER(struct_anon_224)
