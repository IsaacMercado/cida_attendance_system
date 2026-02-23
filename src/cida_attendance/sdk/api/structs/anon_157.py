from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_157(Structure):
    pass

_S(struct_anon_157, [
    ('PresetNum', BYTE),
    ('Dwell', BYTE),
    ('Speed', BYTE),
    ('Reserve', BYTE),
])

NET_DVR_CRUISE_POINT = struct_anon_157
LPNET_DVR_CRUISE_POINT = POINTER(struct_anon_157)
