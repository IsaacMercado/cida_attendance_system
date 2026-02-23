from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_anon_25(Structure):
    pass

_S(struct_anon_25, [
    ('wHideAreaTopLeftX', WORD),
    ('wHideAreaTopLeftY', WORD),
    ('wHideAreaWidth', WORD),
    ('wHideAreaHeight', WORD),
])

NET_DVR_SHELTER = struct_anon_25
LPNET_DVR_SHELTER = POINTER(struct_anon_25)
