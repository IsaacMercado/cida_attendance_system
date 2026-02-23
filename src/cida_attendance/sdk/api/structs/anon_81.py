from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_80 import NET_DVR_IPALARMININFO


class struct_anon_81(Structure):
    pass

_S(struct_anon_81, [
    ('dwSize', DWORD),
    ('struIPAlarmInInfo', NET_DVR_IPALARMININFO * 128),
])

NET_DVR_IPALARMINCFG = struct_anon_81
LPNET_DVR_IPALARMINCFG = POINTER(struct_anon_81)
