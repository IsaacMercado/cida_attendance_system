from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_single_video_detect_light_param import (
    NET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM,
)


class struct_tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM, [
    ('struTrafficLight', NET_ITC_SINGLE_VIDEO_DETECT_LIGHT_PARAM * 12),
    ('byRes', BYTE * 8),
])

NET_ITC_VIDEO_DETECT_LIGHT_PARAM = struct_tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM
LPNET_ITC_VIDEO_DETECT_LIGHT_PARAM = POINTER(struct_tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM)
tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM = struct_tagNET_ITC_VIDEO_DETECT_LIGHT_PARAM
