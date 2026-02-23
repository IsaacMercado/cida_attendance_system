from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_223(Structure):
    pass

_S(struct_anon_223, [
    ('dwSize', DWORD),
    ('dwSpeedValue', DWORD),
    ('dwSpeedPulse', DWORD),
    ('byUpgPercent', BYTE),
    ('byRes1', BYTE * 3),
    ('dwVideoLostChans', DWORD),
    ('byRes2', BYTE * 44),
])

NET_DVR_VEH_REALTIME_DATA_INFO = struct_anon_223
LPNET_DVR_VEH_REALTIME_DATA_INFO = POINTER(struct_anon_223)
