from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_400(Structure):
    pass

_S(struct_anon_400, [
    ('iWindSpeed', c_int),
    ('byRes', BYTE * 508),
])

NET_DVR_WIND_SPEED_STATE = struct_anon_400
LPNET_DVR_WIND_SPEED_STATE = POINTER(struct_anon_400)
