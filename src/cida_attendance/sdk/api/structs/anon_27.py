from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_27(Structure):
    pass

_S(struct_anon_27, [
    ('byRed', BYTE),
    ('byGreen', BYTE),
    ('byBlue', BYTE),
    ('byRes', BYTE),
])

NET_DVR_RGB_COLOR = struct_anon_27
LPNET_DVR_RGB_COLOR = POINTER(struct_anon_27)
