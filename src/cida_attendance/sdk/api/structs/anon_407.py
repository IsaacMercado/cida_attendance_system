from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_407(Structure):
    pass

_S(struct_anon_407, [
    ('dwTurbidity', DWORD),
    ('dwChlorine', DWORD),
    ('dwPH', DWORD),
    ('byRes', BYTE * 500),
])

NET_DVR_WATER_QLT_STATE = struct_anon_407
LPNET_DVR_WATER_QLT_STATE = POINTER(struct_anon_407)
