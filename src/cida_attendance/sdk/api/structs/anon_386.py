from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_385 import NET_DVR_DAYTIME


class struct_anon_386(Structure):
    pass

_S(struct_anon_386, [
    ('struStartTime', NET_DVR_DAYTIME),
    ('struStopTime', NET_DVR_DAYTIME),
])

NET_DVR_SCHEDULE_DAYTIME = struct_anon_386
LPNET_DVR_SCHEDULE_DAYTIME = POINTER(struct_anon_386)
