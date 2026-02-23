from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_anon_432(Structure):
    pass

_S(struct_anon_432, [
    ('wPresetNo', WORD),
    ('wDwell', WORD),
    ('bySpeed', BYTE),
    ('bySupport256PresetNo', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_CRUISEPOINT_PARAM = struct_anon_432
LPNET_DVR_CRUISEPOINT_PARAM = POINTER(struct_anon_432)
