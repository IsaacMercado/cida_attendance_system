from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_play_item import NET_DVR_PLAY_ITEM
from .net_dvr_time_segment import NET_DVR_TIME_SEGMENT


class struct_tagNET_DVR_PLAN_ITEM(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_ITEM, [
    ('struPlanPlayItem', NET_DVR_PLAY_ITEM),
    ('struTimeSegment', NET_DVR_TIME_SEGMENT),
    ('byRes', BYTE * 16),
])

NET_DVR_PLAN_ITEM = struct_tagNET_DVR_PLAN_ITEM
LPNET_DVR_PLAN_ITEM = POINTER(struct_tagNET_DVR_PLAN_ITEM)
tagNET_DVR_PLAN_ITEM = struct_tagNET_DVR_PLAN_ITEM
