from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_PASSBACK_SCHED(Structure):
    pass

_S(struct_tagNET_DVR_PASSBACK_SCHED, [
    ('struPassBackTime', NET_DVR_SCHEDTIME),
    ('byRes', BYTE * 4),
])

NET_DVR_PASSBACK_SCHED = struct_tagNET_DVR_PASSBACK_SCHED
LPNET_DVR_PASSBACK_SCHED = POINTER(struct_tagNET_DVR_PASSBACK_SCHED)
tagNET_DVR_PASSBACK_SCHED = struct_tagNET_DVR_PASSBACK_SCHED
