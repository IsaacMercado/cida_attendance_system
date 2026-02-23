from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_26(Structure):
    pass

_S(struct_anon_26, [
    ('byBrightness', BYTE),
    ('byContrast', BYTE),
    ('bySaturation', BYTE),
    ('byHue', BYTE),
])

NET_DVR_COLOR = struct_anon_26
LPNET_DVR_COLOR = POINTER(struct_anon_26)
