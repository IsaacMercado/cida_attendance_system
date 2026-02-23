from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_video_trigger_param_union import NET_ITC_VIDEO_TRIGGER_PARAM_UNION


class struct_tagNET_ITC_VIDEO_TRIGGER_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_VIDEO_TRIGGER_PARAM, [
    ('dwSize', DWORD),
    ('dwMode', DWORD),
    ('uVideoTrigger', NET_ITC_VIDEO_TRIGGER_PARAM_UNION),
    ('byRes', BYTE * 32),
])

NET_ITC_VIDEO_TRIGGER_PARAM = struct_tagNET_ITC_VIDEO_TRIGGER_PARAM
LPNET_ITC_VIDEO_TRIGGER_PARAM = POINTER(struct_tagNET_ITC_VIDEO_TRIGGER_PARAM)
tagNET_ITC_VIDEO_TRIGGER_PARAM = struct_tagNET_ITC_VIDEO_TRIGGER_PARAM
