from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_59(Structure):
    pass

_S(struct_anon_59, [
    ('wPicSize', WORD),
    ('wPicQuality', WORD),
    ('byPicTackleMode', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_PUSHJPEGPARA = struct_anon_59
LPNET_DVR_PUSHJPEGPARA = POINTER(struct_anon_59)
