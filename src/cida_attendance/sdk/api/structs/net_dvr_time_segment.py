from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_simple_daytime import NET_DVR_SIMPLE_DAYTIME


class struct_tagNET_DVR_TIME_SEGMENT(Structure):
    pass

_S(struct_tagNET_DVR_TIME_SEGMENT, [
    ('struBeginTime', NET_DVR_SIMPLE_DAYTIME),
    ('struEndTime', NET_DVR_SIMPLE_DAYTIME),
])

NET_DVR_TIME_SEGMENT = struct_tagNET_DVR_TIME_SEGMENT
LPNET_DVR_TIME_SEGMENT = POINTER(struct_tagNET_DVR_TIME_SEGMENT)
tagNET_DVR_TIME_SEGMENT = struct_tagNET_DVR_TIME_SEGMENT
