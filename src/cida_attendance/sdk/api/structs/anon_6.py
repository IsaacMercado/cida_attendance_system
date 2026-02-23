from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_6(Structure):
    pass

_S(struct_anon_6, [
    ('byStartHour', BYTE),
    ('byStartMin', BYTE),
    ('byStopHour', BYTE),
    ('byStopMin', BYTE),
])

NET_DVR_SCHEDTIME = struct_anon_6
LPNET_DVR_SCHEDTIME = POINTER(struct_anon_6)
