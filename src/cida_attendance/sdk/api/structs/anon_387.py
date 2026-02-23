from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_387(Structure):
    pass

_S(struct_anon_387, [
    ('byObjectSize', BYTE),
    ('byMotionSensitive', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_DNMODE = struct_anon_387
LPNET_DVR_DNMODE = POINTER(struct_anon_387)
