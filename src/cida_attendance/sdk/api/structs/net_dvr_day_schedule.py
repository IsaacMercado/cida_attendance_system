from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_DAY_SCHEDULE(Structure):
    pass

_S(struct_tagNET_DVR_DAY_SCHEDULE, [
    ('byWorkMode', BYTE),
    ('byRes1', BYTE * 3),
    ('struTime', NET_DVR_SCHEDTIME * 8),
    ('byRes2', BYTE * 8),
])

NET_DVR_DAY_SCHEDULE = struct_tagNET_DVR_DAY_SCHEDULE
LPNET_DVR_DAY_SCHEDULE = POINTER(struct_tagNET_DVR_DAY_SCHEDULE)
tagNET_DVR_DAY_SCHEDULE = struct_tagNET_DVR_DAY_SCHEDULE
