from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_78 import NET_DVR_IPALARMOUTINFO


class struct_anon_79(Structure):
    pass

_S(struct_anon_79, [
    ('dwSize', DWORD),
    ('struIPAlarmOutInfo', NET_DVR_IPALARMOUTINFO * 64),
])

NET_DVR_IPALARMOUTCFG = struct_anon_79
LPNET_DVR_IPALARMOUTCFG = POINTER(struct_anon_79)
