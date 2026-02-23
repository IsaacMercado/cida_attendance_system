from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_OUTPUT_SCHEDULE(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_SCHEDULE, [
    ('struTime', NET_DVR_SCHEDTIME),
    ('byState', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_OUTPUT_SCHEDULE = struct_tagNET_DVR_OUTPUT_SCHEDULE
LPNET_DVR_OUTPUT_SCHEDULE = POINTER(struct_tagNET_DVR_OUTPUT_SCHEDULE)
tagNET_DVR_OUTPUT_SCHEDULE = struct_tagNET_DVR_OUTPUT_SCHEDULE
