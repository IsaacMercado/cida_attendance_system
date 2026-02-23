from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_220(Structure):
    pass

_S(struct_anon_220, [
    ('dwValid', DWORD),
    ('dwLongitude', DWORD),
    ('dwLatitude', DWORD),
    ('dwVehicleSpeed', DWORD),
    ('dwVehicleDirection', DWORD),
    ('dwAltitude', DWORD),
])

NET_DVR_ADAS_POSITION_INFO = struct_anon_220
LPNET_DVR_ADAS_POSITION_INFO = POINTER(struct_anon_220)
