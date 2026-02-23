from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_390(Structure):
    pass

_S(struct_anon_390, [
    ('byMotionScope', (BYTE * 96) * 64),
    ('byMotionSensitive', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_MOTION_SINGLE_AREA = struct_anon_390
LPNET_DVR_MOTION_SINGLE_AREA = POINTER(struct_anon_390)
