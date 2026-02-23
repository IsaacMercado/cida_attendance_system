from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_anon_186(Structure):
    pass

_S(struct_anon_186, [
    ('wAction', WORD),
    ('wPanPos', WORD),
    ('wTiltPos', WORD),
    ('wZoomPos', WORD),
])

NET_DVR_PTZPOS = struct_anon_186
LPNET_DVR_PTZPOS = POINTER(struct_anon_186)
