from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_CYCLE_TIME(Structure):
    pass

_S(struct_tagNET_DVR_CYCLE_TIME, [
    ('byValid', BYTE),
    ('byRes', BYTE * 3),
    ('struTime', NET_DVR_TIME_EX),
])

NET_DVR_CYCLE_TIME = struct_tagNET_DVR_CYCLE_TIME
LPNET_DVR_CYCLE_TIME = POINTER(struct_tagNET_DVR_CYCLE_TIME)
tagNET_DVR_CYCLE_TIME = struct_tagNET_DVR_CYCLE_TIME
