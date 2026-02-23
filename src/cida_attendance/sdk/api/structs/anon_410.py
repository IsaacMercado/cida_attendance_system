from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_anon_410(Structure):
    pass

_S(struct_anon_410, [
    ('struSchedTime', NET_DVR_SCHEDTIME),
    ('wAction', WORD),
    ('wActionNum', WORD),
    ('byres', BYTE * 12),
])

NET_DVR_SCHEDTASK = struct_anon_410
LPNET_DVR_SCHEDTASK = POINTER(struct_anon_410)
