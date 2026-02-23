from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_anon_187(Structure):
    pass

_S(struct_anon_187, [
    ('wPanPosMin', WORD),
    ('wPanPosMax', WORD),
    ('wTiltPosMin', WORD),
    ('wTiltPosMax', WORD),
    ('wZoomPosMin', WORD),
    ('wZoomPosMax', WORD),
])

NET_DVR_PTZSCOPE = struct_anon_187
LPNET_DVR_PTZSCOPE = POINTER(struct_anon_187)
