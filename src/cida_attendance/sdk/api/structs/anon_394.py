from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_26 import NET_DVR_COLOR


class struct_anon_394(Structure):
    pass

_S(struct_anon_394, [
    ('struColor', NET_DVR_COLOR * 8),
    ('struHandleTime', NET_DVR_SCHEDTIME * 8),
])

NET_DVR_VICOLOR = struct_anon_394
LPNET_DVR_VICOLOR = POINTER(struct_anon_394)
