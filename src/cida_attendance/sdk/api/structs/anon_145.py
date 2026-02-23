from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_anon_145(Structure):
    pass

_S(struct_anon_145, [
    ('wPicSize', WORD),
    ('wPicQuality', WORD),
])

NET_DVR_JPEGPARA = struct_anon_145
LPNET_DVR_JPEGPARA = POINTER(struct_anon_145)
