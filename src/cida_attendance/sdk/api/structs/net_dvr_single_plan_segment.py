from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_time_segment import NET_DVR_TIME_SEGMENT


class struct_tagNET_DVR_SINGLE_PLAN_SEGMENT(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_PLAN_SEGMENT, [
    ('byEnable', BYTE),
    ('byDoorStatus', BYTE),
    ('byVerifyMode', BYTE),
    ('byRes', BYTE * 5),
    ('struTimeSegment', NET_DVR_TIME_SEGMENT),
])

NET_DVR_SINGLE_PLAN_SEGMENT = struct_tagNET_DVR_SINGLE_PLAN_SEGMENT
LPNET_DVR_SINGLE_PLAN_SEGMENT = POINTER(struct_tagNET_DVR_SINGLE_PLAN_SEGMENT)
tagNET_DVR_SINGLE_PLAN_SEGMENT = struct_tagNET_DVR_SINGLE_PLAN_SEGMENT
